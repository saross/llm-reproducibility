#!/usr/bin/env python3
"""One-shot corpus migration: repo-resident third-party files -> out-of-tree store.

Implements corpus-management-plan v0.2.1 build items 1-2 (copy-then-verify;
originals untouched). Creates ~/corpora/llm-reproducibility/<slug>/ per paper,
copies PDFs, extracted texts, processed markdown, and the dye supplement with
sha256 verification, then generates the two manifests:

  corpus/development-manifest.yaml                       (11 pre-study papers)
  studies/open-science-compliance/corpus/manifest.yaml   (5 pilot papers)

Metadata: legacy papers from outputs/<slug>/extraction.json project_metadata;
pilots from the study queue.yaml. Missing values recorded as null for later
CrossRef enrichment by fetch-corpus.py.

Usage: python3 migrate-corpus.py
"""
from __future__ import annotations

import hashlib
import json
import shutil
import sys
from datetime import date
from pathlib import Path

import yaml

REPO = Path.home() / "Code" / "llm-reproducibility"
STORE = Path.home() / "corpora" / "llm-reproducibility"
TODAY = date.today().isoformat()

STUDY_PDF_DIR = REPO / "studies/open-science-compliance/corpus/pdfs"
LEGACY_PDF_DIR = REPO / "input/sources/original-pdf"
PROCESSED_MD_DIR = REPO / "input/sources/processed-md"
QUEUE = REPO / "studies/open-science-compliance/corpus/queue.yaml"

PILOTS = ["crema-et-al-2024", "dye-et-al-2023", "herskind-riede-2024",
          "key-et-al-2024", "marwick-2025"]

# Publisher-named PDF prefix -> slug (legacy/development corpus).
LEGACY_MAP = {
    "Ballsun-Stanton et al. - 2018": "ballsun-stanton-et-al-2018",
    "Connor et al. - 2013": "connor-et-al-2013",
    "Eftimoski et al. - 2017": "eftimoski-et-al-2017",
    "Penske et al. - 2023": "penske-et-al-2023",
    "Ross - 2005": "ross-2005",
    "Ross and Ballsun-Stanton - 2022": "ross-ballsun-stanton-2022",
    "Ross et al. - 2009": "ross-et-al-2009",
    "Sobotkova et al. - 2016": "sobotkova-et-al-2016",
    "Sobotkova et al. - 2021": "sobotkova-et-al-2021",
    "Sobotkova et al. - 2023": "sobotkova-et-al-2023",
    "Sobotkova et al. - 2024": "sobotkova-et-al-2024",
}

PROCESSED_MD_MAP = {
    "sobotkova-et-al-2016.md": ("sobotkova-et-al-2016", "processed.md"),
    "sobotkova-et-al-2023-creating-large-high-quality-geospatial-datasets-"
    "from-historical-maps-using-novice-volunteers.md":
        ("sobotkova-et-al-2023", "processed.md"),
    "sobotkova-et-al-2023-gemini.md": ("sobotkova-et-al-2023", "processed-gemini.md"),
}


def sha256(path: Path) -> str:
    """Return the hex sha256 of a file, streamed in 1 MiB chunks."""
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def copy_verified(src: Path, slug: str, dest_name: str, role: str,
                  records: dict[str, list[dict]]) -> None:
    """Copy src into the store under <slug>/<dest_name>, verify by hash, record."""
    dest_dir = STORE / slug
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / dest_name
    src_hash = sha256(src)
    if dest.exists() and sha256(dest) == src_hash:
        status = "already-present"
    else:
        shutil.copy2(src, dest)
        if sha256(dest) != src_hash:
            sys.exit(f"HASH MISMATCH after copy: {src} -> {dest}")
        status = "copied"
    records.setdefault(slug, []).append({
        "role": role,
        "filename": dest_name,
        "sha256": src_hash,
        "bytes": dest.stat().st_size,
        "acquired": None,
        "migrated": TODAY,
        "provenance": f"migrated from {src.relative_to(REPO)}",
    })
    print(f"  {status:15s} {slug}/{dest_name}  ({dest.stat().st_size:,} B)")


def legacy_metadata(slug: str) -> dict:
    """Pull bibliographic fields from outputs/<slug>/extraction.json, nulls where absent."""
    pm: dict = {}
    ej = REPO / "outputs" / slug / "extraction.json"
    if ej.exists():
        try:
            pm = json.loads(ej.read_text()).get("project_metadata") or {}
        except json.JSONDecodeError:
            print(f"  WARNING: unparseable extraction.json for {slug}")
    return {
        "doi": pm.get("doi"),
        "title": pm.get("paper_title") or pm.get("title"),
        "authors": pm.get("authors"),
        "year": pm.get("publication_year"),
        "journal": pm.get("journal"),
    }


def main() -> None:
    records: dict[str, list[dict]] = {}

    print("== Study pilot PDFs ==")
    for slug in PILOTS:
        copy_verified(STUDY_PDF_DIR / f"{slug}.pdf", slug, "vor.pdf", "vor", records)
    copy_verified(STUDY_PDF_DIR / "marwick-2025-socarxiv-preprint.pdf",
                  "marwick-2025", "preprint.pdf", "preprint", records)

    print("== Dye supplement ==")
    supp = (REPO / "studies/open-science-compliance/outputs/dye-et-al-2023/"
            "reproduction/attempt-01/supplement.pdf")
    copy_verified(supp, "dye-et-al-2023", "supplement-1.pdf", "supplement", records)

    print("== Legacy PDFs ==")
    for prefix, slug in LEGACY_MAP.items():
        matches = sorted(LEGACY_PDF_DIR.glob(prefix + "*"))
        if len(matches) != 1:
            sys.exit(f"expected exactly one match for {prefix!r}, got {matches}")
        copy_verified(matches[0], slug, "vor.pdf", "vor", records)

    print("== Extracted texts ==")
    for base in [REPO / "outputs",
                 REPO / "studies/open-science-compliance/outputs"]:
        for slug_dir in sorted(p for p in base.iterdir() if p.is_dir()):
            txt = slug_dir / f"{slug_dir.name}.txt"
            if txt.exists():
                copy_verified(txt, slug_dir.name, "extracted.txt",
                              "extracted_text", records)

    print("== Processed markdown ==")
    for name, (slug, dest_name) in PROCESSED_MD_MAP.items():
        src = PROCESSED_MD_DIR / name
        if src.exists():
            copy_verified(src, slug, dest_name, "processed_text", records)
        else:
            print(f"  MISSING (skipped): {name}")

    # --- Manifests -----------------------------------------------------------
    print("== Manifests ==")
    queue = yaml.safe_load(QUEUE.read_text())
    queue_by_slug = {p["slug"]: p for p in queue.get("papers", [])}

    def paper_entry(slug: str, meta: dict, extra: dict | None = None) -> dict:
        entry = {
            "slug": slug,
            "doi": meta.get("doi"),
            "title": meta.get("title"),
            "authors": meta.get("authors"),
            "year": meta.get("year"),
            "journal": meta.get("journal"),
            "oa_status": None,
            "licence": None,
            "source_urls": {},
            "files": records.get(slug, []),
        }
        if extra:
            entry.update(extra)
        return entry

    common_header = {
        "schema": "corpus-manifest/1.0",
        "corpus_root": "~/corpora/llm-reproducibility",
        "generated": TODAY,
        "note": ("Canonical record of corpus holdings. meta.json files in the "
                 "store are machine-generated projections of this manifest — "
                 "never hand-edit either in divergence. Rebuild open-access "
                 "holdings with scripts/fetch-corpus.py."),
    }

    dev_papers = []
    for slug in sorted(LEGACY_MAP.values()):
        dev_papers.append(paper_entry(slug, legacy_metadata(slug)))
    dev = dict(common_header,
               corpus="development (pre-study pilot papers)",
               papers=dev_papers)
    dev_path = REPO / "corpus/development-manifest.yaml"
    dev_path.parent.mkdir(exist_ok=True)
    dev_path.write_text(yaml.safe_dump(dev, sort_keys=False,
                                       allow_unicode=True, width=88))
    print(f"  wrote {dev_path.relative_to(REPO)} ({len(dev_papers)} papers)")

    study_papers = []
    for slug in PILOTS:
        q = queue_by_slug.get(slug, {})
        meta = {"doi": q.get("doi"), "title": q.get("title"),
                "authors": q.get("authors"), "year": q.get("year"),
                "journal": "Journal of Archaeological Science"}
        extra = {"role_in_study": "pilot"}
        if slug == "dye-et-al-2023":
            extra["notes"] = ("DOI prefix is 2023 (online-first) though article "
                              "year is 2024; the 2024-prefix form 404s "
                              "(verified 2026-07-13, queue.yaml)")
        study_papers.append(paper_entry(slug, meta, extra))
    study = dict(common_header,
                 corpus="open-science-compliance study (Phase 1 pilots; "
                        "census entries appended by fetch-corpus.py)",
                 papers=study_papers)
    study_path = REPO / "studies/open-science-compliance/corpus/manifest.yaml"
    study_path.write_text(yaml.safe_dump(study, sort_keys=False,
                                         allow_unicode=True, width=88))
    print(f"  wrote {study_path.relative_to(REPO)} ({len(study_papers)} papers)")

    n_files = sum(len(v) for v in records.values())
    n_bytes = sum(f["bytes"] for v in records.values() for f in v)
    print(f"\nStore: {len(records)} papers, {n_files} files, "
          f"{n_bytes/1e6:.1f} MB at {STORE}")


if __name__ == "__main__":
    main()
