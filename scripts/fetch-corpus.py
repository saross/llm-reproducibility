#!/usr/bin/env python3
"""Corpus acquisition and verification against a corpus manifest.

Implements corpus-management-plan v0.2.1 build item 3. Operates on any manifest
conforming to the corpus-manifest/1.0 schema (see corpus/README.md). Never
touches git-tracked paths: all downloads land in the out-of-tree store.

Commands:
    verify    Check every manifest-listed file exists in the store with a
              matching sha256 (no network access).
    fetch     Resolve each paper's DOI via Unpaywall and download the best
              open-access PDF for papers missing a vor.pdf/preprint.pdf.
              Requires --email (Unpaywall politeness requirement).
    report    List papers with no retrievable open-access copy — the manual
              (or text-and-data-mining) acquisition queue, with source URLs.
    gen-meta  Write <slug>/meta.json into the store as a machine-generated
              projection of the manifest (never hand-edit meta.json).

Examples:
    python3 scripts/fetch-corpus.py verify --manifest corpus/development-manifest.yaml
    python3 scripts/fetch-corpus.py fetch --manifest studies/open-science-compliance/corpus/manifest.yaml \
        --email shawn@faims.edu.au
    python3 scripts/fetch-corpus.py report --manifest corpus/development-manifest.yaml

Politeness: ≤1 request/second, exponential backoff on 429/5xx, contact email in
the User-Agent and Unpaywall query string. ScienceDirect blocks scripted PDF
download (HTTP 403, known from pilot notes) — such items appear in `report` for
manual or TDM-route acquisition; do not attempt workarounds here.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import time
import urllib.error
import urllib.request
from datetime import date, datetime, timezone
from pathlib import Path

import yaml

UNPAYWALL = "https://api.unpaywall.org/v2/{doi}?email={email}"
MIN_REQUEST_INTERVAL_S = 1.0
MAX_RETRIES = 4
_last_request_time = 0.0


def corpus_root(manifest: dict) -> Path:
    """Resolve the store root: CORPUS_ROOT env var beats the manifest key."""
    root = os.environ.get("CORPUS_ROOT") or manifest.get(
        "corpus_root", "~/corpora/llm-reproducibility")
    return Path(root).expanduser()


def sha256(path: Path) -> str:
    """Hex sha256 of a file, streamed."""
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def polite_get(url: str, email: str, expect_json: bool = True):
    """HTTP GET with rate limiting, backoff, and a contactable User-Agent."""
    global _last_request_time
    headers = {"User-Agent":
               f"llm-reproducibility-fetch-corpus/1.0 (mailto:{email})"}
    for attempt in range(MAX_RETRIES):
        wait = MIN_REQUEST_INTERVAL_S - (time.monotonic() - _last_request_time)
        if wait > 0:
            time.sleep(wait)
        _last_request_time = time.monotonic()
        req = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                data = resp.read()
                return json.loads(data) if expect_json else data
        except urllib.error.HTTPError as err:
            if err.code in (429, 500, 502, 503) and attempt < MAX_RETRIES - 1:
                backoff = 2 ** attempt * 5
                print(f"    HTTP {err.code}; backing off {backoff}s", file=sys.stderr)
                time.sleep(backoff)
                continue
            raise
    raise RuntimeError(f"unreachable after {MAX_RETRIES} attempts: {url}")


def load_manifest(path: Path) -> dict:
    manifest = yaml.safe_load(path.read_text())
    if manifest.get("schema") != "corpus-manifest/1.0":
        sys.exit(f"unsupported manifest schema in {path}: {manifest.get('schema')!r}")
    return manifest


def cmd_verify(manifest_path: Path) -> int:
    """Hash-check every manifest-listed file; return count of problems."""
    manifest = load_manifest(manifest_path)
    root = corpus_root(manifest)
    problems = 0
    for paper in manifest.get("papers", []):
        slug = paper["slug"]
        for rec in paper.get("files", []):
            fpath = root / slug / rec["filename"]
            if not fpath.exists():
                print(f"MISSING  {slug}/{rec['filename']}")
                problems += 1
            elif sha256(fpath) != rec["sha256"]:
                print(f"HASH-MISMATCH  {slug}/{rec['filename']}")
                problems += 1
    n = sum(len(p.get("files", [])) for p in manifest.get("papers", []))
    print(f"verify: {n - problems}/{n} files OK "
          f"({manifest_path.name}, store {root})")
    return problems


def cmd_fetch(manifest_path: Path, email: str) -> None:
    """Unpaywall-resolve DOIs and download the best OA PDF for missing papers."""
    manifest = load_manifest(manifest_path)
    root = corpus_root(manifest)
    changed = False
    for paper in manifest.get("papers", []):
        slug, doi = paper["slug"], paper.get("doi")
        have_pdf = any(r["role"] in ("vor", "preprint")
                       for r in paper.get("files", []))
        if have_pdf:
            continue
        if not doi:
            print(f"  {slug}: no DOI in manifest — skipping (enrich first)")
            continue
        print(f"  {slug}: querying Unpaywall for {doi}")
        try:
            record = polite_get(UNPAYWALL.format(doi=doi, email=email), email)
        except urllib.error.HTTPError as err:
            print(f"    Unpaywall error {err.code} — recorded as closed")
            paper["oa_status"] = f"unpaywall-error-{err.code}"
            continue
        paper["oa_status"] = record.get("oa_status")
        best = record.get("best_oa_location") or {}
        pdf_url = best.get("url_for_pdf")
        licence = best.get("license")
        if licence:
            paper["licence"] = licence
        if not pdf_url:
            print(f"    closed (oa_status={paper['oa_status']}) — see `report`")
            continue
        role = "vor" if best.get("version") == "publishedVersion" else "preprint"
        dest = root / slug / f"{role}.pdf"
        dest.parent.mkdir(parents=True, exist_ok=True)
        try:
            blob = polite_get(pdf_url, email, expect_json=False)
        except urllib.error.HTTPError as err:
            print(f"    download failed HTTP {err.code} "
                  f"(ScienceDirect 403 → manual/TDM queue) — see `report`")
            paper.setdefault("source_urls", {})[role] = pdf_url
            continue
        dest.write_bytes(blob)
        digest = sha256(dest)
        paper.setdefault("source_urls", {})[role] = pdf_url
        paper.setdefault("files", []).append({
            "role": role, "filename": dest.name, "sha256": digest,
            "bytes": dest.stat().st_size,
            "acquired": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "migrated": None, "provenance": f"fetched from {pdf_url}",
        })
        changed = True
        print(f"    fetched {role}.pdf ({dest.stat().st_size:,} B, {licence})")
    if changed or True:  # oa_status/licence updates count as changes too
        manifest["generated"] = date.today().isoformat()
        manifest_path.write_text(
            yaml.safe_dump(manifest, sort_keys=False, allow_unicode=True, width=88))
        print(f"manifest updated: {manifest_path}")


def cmd_report(manifest_path: Path) -> None:
    """List papers with no held PDF — the manual/TDM acquisition queue."""
    manifest = load_manifest(manifest_path)
    queue = []
    for paper in manifest.get("papers", []):
        if not any(r["role"] in ("vor", "preprint")
                   for r in paper.get("files", [])):
            queue.append(paper)
    if not queue:
        print("report: no papers awaiting acquisition — corpus complete")
        return
    print(f"report: {len(queue)} paper(s) need manual/TDM acquisition "
          f"(est. 2-3 min each via library proxy):")
    for paper in queue:
        urls = "; ".join(paper.get("source_urls", {}).values()) or "no URL recorded"
        print(f"  {paper['slug']}: doi={paper.get('doi')} "
              f"oa_status={paper.get('oa_status')} [{urls}]")


def cmd_gen_meta(manifest_path: Path) -> None:
    """Write <slug>/meta.json as a machine-generated projection of the manifest."""
    manifest = load_manifest(manifest_path)
    root = corpus_root(manifest)
    for paper in manifest.get("papers", []):
        slug_dir = root / paper["slug"]
        if not slug_dir.exists():
            continue
        meta = {k: paper.get(k) for k in
                ("slug", "doi", "title", "authors", "year", "journal",
                 "oa_status", "licence", "source_urls", "files")}
        meta["_generated"] = (f"by fetch-corpus.py gen-meta from "
                              f"{manifest_path.name} on {date.today().isoformat()}"
                              " — do not hand-edit")
        (slug_dir / "meta.json").write_text(
            json.dumps(meta, indent=2, ensure_ascii=False) + "\n")
    print(f"gen-meta: meta.json written for "
          f"{len(manifest.get('papers', []))} papers under {root}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("command",
                        choices=["verify", "fetch", "report", "gen-meta"])
    parser.add_argument("--manifest", required=True, type=Path)
    parser.add_argument("--email",
                        help="contact email (required for fetch; Unpaywall "
                             "and CrossRef politeness)")
    args = parser.parse_args()
    if args.command == "verify":
        sys.exit(1 if cmd_verify(args.manifest) else 0)
    elif args.command == "fetch":
        if not args.email:
            parser.error("fetch requires --email")
        cmd_fetch(args.manifest, args.email)
    elif args.command == "report":
        cmd_report(args.manifest)
    elif args.command == "gen-meta":
        cmd_gen_meta(args.manifest)


if __name__ == "__main__":
    main()
