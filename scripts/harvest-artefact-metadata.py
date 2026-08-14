#!/usr/bin/env python3
"""Artefact-metadata harvester — deterministic evidence packs (plan C6).

**Version:** 1.0

Resolves each pilot paper's declared artefact links (the curated registry at
``corpus/evidence-packs/declared-links.yaml``) into a per-paper evidence pack
via the ratified endpoint list (erratum-log Entry 3, item 8: DataCite,
Crossref, Zenodo, GitHub, GitLab, Open Science Framework (OSF); CRAN and
Dryad flagged as early additions — flagged endpoints are recorded as honest
gaps, never improvised). Packs give scoring spawns verified, identical
evidence across runs: every record carries its retrieval timestamp and a
sha256 of the raw response body (Phase C contract hardening 8), and the
record shape follows the C3/C6 joint design note
(``wiki/planning/instrument-clarification-plan.md``).

Conflict detection (erratum item 6): where the registry carries a
``paper_asserted_licence`` and the service records a different licence, the
record gains a conflict flag naming both sides — the most-restrictive rule
governs scoring, applied by the scorer, not silently by this script.

Network conduct: public metadata APIs only; one request per second; a
descriptive User-Agent; one retry then a dead-link record (never a silent
skip). GitHub authentication: reads ``GITHUB_API_TOKEN_LLMR`` from
``~/personal-assistant/.env`` when present (read-only public scope; the
token is used in a request header and never logged or printed); falls back
to polite unauthenticated requests otherwise.

Usage:
    venv/bin/python scripts/harvest-artefact-metadata.py            # all papers
    venv/bin/python scripts/harvest-artefact-metadata.py --only crema-et-al-2024

Outputs: ``corpus/evidence-packs/<paper-slug>.json`` (sorted keys, stable
layout — diffs between harvests are meaningful).
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
REGISTRY_PATH = REPO_ROOT / "corpus" / "evidence-packs" / "declared-links.yaml"
OUT_DIR = REPO_ROOT / "corpus" / "evidence-packs"
ENV_PATH = Path.home() / "personal-assistant" / ".env"

HARVESTER_VERSION = "1.0"
USER_AGENT = ("llm-reproducibility-harvester/1.0 "
              "(mailto:shawn@faims.edu.au; research-integrity study OSF "
              "10.17605/OSF.IO/DQNHG)")
REQUEST_DELAY_S = 1.0
TIMEOUT_S = 30

DOI_RE = re.compile(r"^10\.\d{4,9}/\S+$")
# Endpoints in the ratified item-8 list that this version implements.
IMPLEMENTED = ("datacite", "crossref", "zenodo", "github", "gitlab", "osf")
# Flagged additions (ratified): recorded as honest gaps, never resolved ad hoc.
FLAGGED_HOSTS = {"cran.r-project.org": "cran", "datadryad.org": "dryad"}


def github_token() -> str | None:
    """Read GITHUB_API_TOKEN_LLMR from the operator's env file, if present.

    The value is returned for use in a request header only — callers must
    never log or print it.
    """
    try:
        for line in ENV_PATH.read_text(encoding="utf-8").splitlines():
            if line.strip().startswith("GITHUB_API_TOKEN_LLMR="):
                return line.split("=", 1)[1].strip().strip('"').strip("'") or None
    except OSError:
        return None
    return None


def fetch(url: str, extra_headers: dict | None = None) -> tuple[int, bytes]:
    """GET a URL politely: UA header, timeout, one retry, 1 s spacing.

    Returns (HTTP status, body bytes); (0, b"") when the transport itself
    fails twice (DNS, refused connection) — the caller records a dead link.
    """
    headers = {"User-Agent": USER_AGENT, "Accept": "application/json"}
    headers.update(extra_headers or {})
    for attempt in (1, 2):
        try:
            request = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(request, timeout=TIMEOUT_S) as response:
                body = response.read()
                time.sleep(REQUEST_DELAY_S)
                return response.status, body
        except urllib.error.HTTPError as exc:
            time.sleep(REQUEST_DELAY_S)
            return exc.code, exc.read() or b""
        except (urllib.error.URLError, TimeoutError, OSError):
            time.sleep(REQUEST_DELAY_S * attempt)
    return 0, b""


def canonical_licence(value: str) -> str:
    """Canonicalise licence URLs to short ids where mechanically safe.

    Creative Commons URLs map to their SPDX-style short form (the live
    harvest showed Crossref records licence URLs while papers assert
    licence names — 'CC BY' vs .../licenses/by/4.0 is the same statement,
    and flagging it as a conflict would be a false positive). Anything
    unrecognised passes through unchanged.
    """
    match = re.search(r"creativecommons\.org/(?:licenses|publicdomain)/"
                      r"([a-z0-9-]+)(?:/(\d\.\d))?", value)
    if match:
        base = "cc0" if match.group(1) == "zero" else f"cc-{match.group(1)}"
        return base + (f"-{match.group(2)}" if match.group(2) else "")
    return value


_FETCH_CACHE: dict[str, tuple[int, bytes]] = {}


def cached_fetch(url: str, extra_headers: dict | None = None) -> tuple[int, bytes]:
    """fetch() memoised per run: two registry entries naming one identifier
    share a single request (and therefore a single, deduplicable record)."""
    if url not in _FETCH_CACHE:
        _FETCH_CACHE[url] = fetch(url, extra_headers)
    return _FETCH_CACHE[url]


def classify(link: str) -> list[tuple[str, str]]:
    """Map one declared link to [(endpoint, request_url)] resolution steps.

    A Zenodo DOI resolves at BOTH DataCite (registration-agency record) and
    the Zenodo REST API (licence field, access_right); an article DOI goes
    to Crossref; other DOIs go to DataCite. URLs route by host. Flagged
    hosts return a single ('<flagged-name>', '') step the harvester records
    as an unimplemented-endpoint gap.
    """
    link = link.strip().rstrip(".")
    if DOI_RE.match(link):
        steps = []
        if link.startswith("10.5281/zenodo."):
            record_number = link.rsplit(".", 1)[-1]
            steps.append(("datacite", f"https://api.datacite.org/dois/{urllib.parse.quote(link, safe='')}"))
            steps.append(("zenodo", f"https://zenodo.org/api/records/{record_number}"))
        elif link.startswith("10.1016/") or link.startswith("10.1111/"):
            steps.append(("crossref", f"https://api.crossref.org/works/{urllib.parse.quote(link, safe='')}"))
        else:
            steps.append(("datacite", f"https://api.datacite.org/dois/{urllib.parse.quote(link, safe='')}"))
        return steps
    parsed = urllib.parse.urlparse(link)
    host = parsed.netloc.lower()
    if host in FLAGGED_HOSTS:
        return [(FLAGGED_HOSTS[host], "")]
    if host.endswith("github.com"):
        owner_repo = "/".join(parsed.path.strip("/").split("/")[:2])
        return [("github", f"https://api.github.com/repos/{owner_repo}")]
    if host.endswith("gitlab.com"):
        project = urllib.parse.quote(parsed.path.strip("/"), safe="")
        # license=true is opt-in — without it GitLab omits licence data
        # entirely (platform-row verification note, 2026-08-15: a live
        # false-negative risk, not a theoretical one).
        return [("gitlab", f"https://gitlab.com/api/v4/projects/{project}?license=true")]
    if host.endswith("zenodo.org"):
        match = re.search(r"/records?/(\d+)", parsed.path)
        if match:
            return [("zenodo", f"https://zenodo.org/api/records/{match.group(1)}")]
    if host.endswith("osf.io"):
        node = parsed.path.strip("/").split("/")[0]
        return [("osf", f"https://api.osf.io/v2/nodes/{node}/")]
    return [("unrouted", "")]


def extract_fields(endpoint: str, document: dict) -> dict:
    """Pull the scoring-relevant fields from one endpoint response."""
    if endpoint == "datacite":
        attributes = (document.get("data") or {}).get("attributes") or {}
        return {
            "doi": attributes.get("doi"),
            "state": attributes.get("state"),
            "publisher": attributes.get("publisher"),
            "publication_year": attributes.get("publicationYear"),
            "resource_type": ((attributes.get("types") or {}).get("resourceTypeGeneral")),
            "licences": sorted({r.get("rightsIdentifier") or r.get("rights") or ""
                                for r in attributes.get("rightsList") or []} - {""}),
            "metadata_record": True,
            "identifier_in_metadata": bool(attributes.get("doi")),
        }
    if endpoint == "crossref":
        message = document.get("message") or {}
        return {
            "doi": message.get("DOI"),
            "type": message.get("type"),
            "publisher": message.get("publisher"),
            "licences": sorted({canonical_licence(l.get("URL", ""))
                                for l in message.get("license") or []} - {""}),
            "metadata_record": True,
            "identifier_in_metadata": bool(message.get("DOI")),
        }
    if endpoint == "zenodo":
        metadata = document.get("metadata") or {}
        licence = metadata.get("license")
        licence_id = (licence or {}).get("id") if isinstance(licence, dict) else licence
        return {
            "record_id_on_service": document.get("id"),
            "doi": document.get("doi") or metadata.get("doi"),
            "concept_doi": document.get("conceptdoi"),
            "access_right": metadata.get("access_right"),
            "licences": [licence_id] if licence_id else [],
            "resource_type": ((metadata.get("resource_type") or {}).get("type")),
            "metadata_record": True,
            "identifier_in_metadata": bool(document.get("doi") or metadata.get("doi")),
        }
    if endpoint == "github":
        licence = (document.get("license") or {})
        return {
            "full_name": document.get("full_name"),
            "archived_flag": document.get("archived"),
            "default_branch": document.get("default_branch"),
            "pushed_at": document.get("pushed_at"),
            "licences": [licence.get("spdx_id")] if licence.get("spdx_id")
                        and licence.get("spdx_id") != "NOASSERTION" else [],
            "metadata_record": False,
            "persistence_entitlement": False,
        }
    if endpoint == "gitlab":
        licence = document.get("license") or {}
        return {
            "full_name": document.get("path_with_namespace"),
            "default_branch": document.get("default_branch"),
            "last_activity_at": document.get("last_activity_at"),
            # GitLab exposes key/name only — no SPDX identifier field
            # (platform-row verification note, 2026-08-15).
            "licences": [licence.get("key")] if licence.get("key") else [],
            "metadata_record": False,
            "persistence_entitlement": False,
        }
    if endpoint == "osf":
        attributes = ((document.get("data") or {}).get("attributes")) or {}
        return {
            "title": attributes.get("title"),
            "public": attributes.get("public"),
            "licences": [],
            "metadata_record": False,
        }
    return {}


def licences_conflict(asserted: str, recorded: list[str]) -> bool:
    """True when a paper-asserted licence and service-recorded licences
    cannot be read as the same statement (case/punctuation-insensitive
    containment either way). Deliberately conservative: any doubt flags."""
    if not asserted or not recorded:
        return False
    normalise = lambda s: re.sub(r"[^a-z0-9]+", "", s.lower())
    asserted_norm = normalise(asserted)
    for item in recorded:
        item_norm = normalise(str(item))
        if item_norm and (item_norm in asserted_norm or asserted_norm in item_norm):
            return False
    return True


def harvest_link(entry: dict) -> list[dict]:
    """Resolve one registry entry into one or more pack records.

    Each record carries a `declared_by` list (which registry entries name
    this identifier) and a `licence_conflicts` list — both merged by
    harvest_paper when several entries share one identifier.
    """
    link = str(entry["link"])
    declared = {"declared_id": entry.get("id"), "artefact_type": entry.get("type")}
    records = []
    for endpoint, request_url in classify(link):
        retrieved_at = datetime.now(timezone.utc).isoformat()
        base = {
            "record_id": f"{endpoint}:{link.rstrip('.')}",
            "declared_by": [dict(declared)],
            "source_endpoint": endpoint,
            "declared_link": link,
            "retrieved_at": retrieved_at,
            "licence_conflicts": [],
        }
        if endpoint not in IMPLEMENTED:
            base.update({"status": "endpoint-flagged",
                         "note": f"'{endpoint}' is on the ratified flagged-additions "
                                 f"list (or unrouted) — recorded as a gap, not resolved "
                                 f"ad hoc; see erratum-log Entry 3 item 8"})
            records.append(base)
            continue
        headers = {}
        if endpoint == "github":
            token = github_token()
            if token:
                headers["Authorization"] = f"Bearer {token}"
        status, body = cached_fetch(request_url, headers)
        base["request_url"] = request_url
        base["http_status"] = status
        base["response_sha256"] = hashlib.sha256(body).hexdigest() if body else None
        if status != 200:
            base["status"] = "unresolved"
            base["note"] = ("transport failure after retry" if status == 0
                            else f"HTTP {status}")
            records.append(base)
            continue
        try:
            document = json.loads(body.decode("utf-8"))
        except (json.JSONDecodeError, UnicodeDecodeError) as exc:
            base["status"] = "unparseable-response"
            base["note"] = f"{exc.__class__.__name__}"
            records.append(base)
            continue
        base["status"] = "resolved"
        base["fields"] = extract_fields(endpoint, document)
        asserted = str(entry.get("paper_asserted_licence") or "")
        if asserted:
            recorded = base["fields"].get("licences") or []
            base["licence_conflicts"].append({
                "declared_id": entry.get("id"),
                "paper_asserted": asserted,
                "service_recorded": recorded,
                "conflict": licences_conflict(asserted, recorded),
                "rule": "same-artefact disagreement: most restrictive governs "
                        "(erratum-log Entry 3, item 6); applied by the scorer",
            })
        records.append(base)
    return records


def harvest_paper(slug: str, spec: dict) -> dict:
    """Build one paper's evidence pack, deduplicating by record_id.

    Two registry entries naming the same identifier (e.g. an article and
    its landing-page supplement) merge into one record whose declared_by
    and licence_conflicts lists carry both perspectives — record_id stays
    unique within the pack, per the C3/C6 joint design note.
    """
    records: list[dict] = []
    by_id: dict[str, dict] = {}
    for entry in spec.get("links", []):
        for record in harvest_link(entry):
            existing = by_id.get(record["record_id"])
            if existing is None:
                by_id[record["record_id"]] = record
                records.append(record)
                continue
            for declarer in record["declared_by"]:
                if declarer not in existing["declared_by"]:
                    existing["declared_by"].append(declarer)
            existing.setdefault("licence_conflicts", []).extend(
                record.get("licence_conflicts") or [])
    return {
        "pack_schema": "evidence-pack v1.0 (C3/C6 joint design note)",
        "paper_slug": slug,
        "article_doi": spec.get("article_doi"),
        "harvested_at": datetime.now(timezone.utc).isoformat(),
        "harvester_version": HARVESTER_VERSION,
        "registry": str(REGISTRY_PATH.relative_to(REPO_ROOT)),
        "records": records,
    }


def main() -> int:
    """CLI entry point: harvest all papers (or --only one) to the pack dir."""
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--only", help="harvest a single paper slug")
    parser.add_argument("--registry", type=Path, default=REGISTRY_PATH)
    parser.add_argument("--out", type=Path, default=OUT_DIR)
    args = parser.parse_args()

    registry = yaml.safe_load(args.registry.read_text(encoding="utf-8")) or {}
    papers = registry.get("papers") or {}
    if args.only:
        papers = {args.only: papers[args.only]}
    args.out.mkdir(parents=True, exist_ok=True)
    for slug, spec in papers.items():
        pack = harvest_paper(slug, spec)
        out_path = args.out / f"{slug}.json"
        out_path.write_text(json.dumps(pack, indent=2, sort_keys=True,
                                       ensure_ascii=False) + "\n",
                            encoding="utf-8")
        resolved = sum(1 for r in pack["records"] if r.get("status") == "resolved")
        flagged = sum(1 for r in pack["records"] if r.get("status") != "resolved")
        print(f"{slug}: {len(pack['records'])} records "
              f"({resolved} resolved, {flagged} flagged/unresolved) -> {out_path.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
