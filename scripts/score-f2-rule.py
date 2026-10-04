#!/usr/bin/env python3
"""Mechanical F2 rule (AP-15) from registry metadata — the hybrid scorer's F2.

**Version:** 1.0

Scores the Findable sub-principle F2 ("rich metadata") for each paper's data
and code from structured inputs only: the curated declared-links registry
(``corpus/evidence-packs/declared-links.yaml``, curation fields ``role``,
``home``, ``carries``, ``scored_version``, ``unpublished_principal``) and the
DataCite records in a harvester v1.2 evidence pack. It implements the
registrant's AP-15 ruling (E8-v2 adjudication log, 2026-10-03): F2 = 1
requires all four of creators, title, a substantive description of the
artefact's own content, and at least one subject keyword, read from the
deposit's own machine-readable record.

Scope (registrant ruling, 2026-10-04: "the rule gives the 0s; you confirm
the 1s"):

* **mechanical-0** — decided by the rule. Any principal artefact is
  unpublished (AP-13), served only as a journal supplement (Row 6), or on
  unmanaged hosting with no record (AP-3); or a principal deposit's
  scored-version DataCite record has no creators, no title, no non-empty
  description, or no subject keyword. Aggregation is conjunctive: one
  failing principal artefact decides the item.
* **confirm-1** — every principal artefact is a deposit whose record has all
  four fields. Whether the description is *substantive* (AP-15's one
  residual judgement: not merely a citation of the paper) goes to the
  registrant. The rule never awards a 1 by itself.
* **no-structured-input** — the inputs needed are missing: no principal
  artefact of that class in the registry, an uncurated link, a principal
  home that is not a DataCite-registered deposit, or a scored-version
  record absent from the pack. The model's score stands and is flagged
  (disagreement policy, item 2 fallback;
  ``wiki/planning/deterministic-output-checks.md``).

Every result records the rule version, the record ids and field values it
read, and its reasons, so each override can be audited (policy item 4).

Usage (from the repository root):
    venv/bin/python scripts/score-f2-rule.py \\
        --packs corpus/evidence-packs/harvest-2026-10-04 \\
        --out studies/open-science-compliance/outputs/validation/\\
f2-rule-hybrid-2026-10-04/f2-rule-results.json
"""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import sys
from pathlib import Path
from typing import Any

import yaml

RULE_VERSION = "1.0"
REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_REGISTRY = REPO_ROOT / "corpus" / "evidence-packs" / "declared-links.yaml"

ARTEFACT_CLASSES: dict[str, str] = {"data": "data_fair", "code": "code_fair"}
TYPE_CARRIES: dict[str, list[str]] = {
    "data": ["data"], "code": ["code"], "data+code": ["data", "code"],
}
ROLES = {"principal", "mirror", "dependency", "upstream"}
HOMES = {"repository", "supplement", "unmanaged"}

MECHANICAL_0 = "mechanical-0"
CONFIRM_1 = "confirm-1"
NO_INPUT = "no-structured-input"


def visible_text(markup: str | None) -> str:
    """Return a description's visible text: tags removed, entities decoded,
    whitespace collapsed. An HTML shell such as ``<p></p>`` is empty."""
    text = re.sub(r"<[^>]+>", " ", markup or "")
    return re.sub(r"\s+", " ", html.unescape(text)).strip()


def link_carries(entry: dict) -> list[str] | None:
    """Artefact classes a registry entry holds: explicit ``carries`` first,
    else implied by its type; None when neither says (a curation gap)."""
    if entry.get("carries") is not None:
        return [str(c) for c in entry["carries"]]
    return TYPE_CARRIES.get(str(entry.get("type") or ""))


def datacite_record(pack: dict, doi: str) -> dict | None:
    """Return the resolved DataCite record for one DOI, or None."""
    wanted = f"datacite:{doi.strip().rstrip('.')}"
    for record in pack.get("records") or []:
        if record.get("record_id") == wanted and record.get("status") == "resolved":
            return record
    return None


def check_deposit(record: dict) -> tuple[str, list[str], dict[str, Any]]:
    """Apply AP-15's four-field test to one scored-version DataCite record.

    Returns (status, reasons, inputs read). Only absences are mechanical;
    when all four fields are present the item needs the registrant's
    confirmation that the description describes the artefact's content.
    """
    fields = record.get("fields") or {}
    descriptions = [visible_text(d.get("text")) for d in fields.get("descriptions") or []
                    if isinstance(d, dict)]
    descriptions = [d for d in descriptions if d]
    inputs = {
        "record_id": record.get("record_id"),
        "response_sha256": record.get("response_sha256"),
        "creators": fields.get("creators") or [],
        "titles": fields.get("titles") or [],
        "subjects": fields.get("subjects") or [],
        "descriptions_visible_text": descriptions,
    }
    missing = [name for name, value in (("creators", inputs["creators"]),
                                        ("title", inputs["titles"]),
                                        ("description", descriptions),
                                        ("subject keyword", inputs["subjects"]))
               if not value]
    if missing:
        return MECHANICAL_0, [f"{record.get('record_id')}: no {m}" for m in missing], inputs
    return CONFIRM_1, [f"{record.get('record_id')}: creators, title, description, and "
                       f"keywords present; description substance needs confirmation"], inputs


def score_item(slug: str, spec: dict, pack: dict | None, artefact_class: str) -> dict:
    """Score F2 for one paper's data or code under AP-15, conjunctively."""
    result: dict[str, Any] = {"paper": slug, "artefact": ARTEFACT_CLASSES[artefact_class],
                              "sub_principle": "F2", "rule_version": RULE_VERSION}
    zeros: list[str] = []
    gaps: list[str] = []
    confirms: list[str] = []
    inputs: list[dict] = []

    if artefact_class in (spec.get("unpublished_principal") or []):
        zeros.append(f"unpublished principal {artefact_class} (AP-13): "
                     f"{spec.get('unpublished_principal_basis', 'no basis recorded')}")

    links = [e for e in spec.get("links") or [] if e.get("type") != "article"]
    principals = []
    for entry in links:
        role = entry.get("role")
        if role not in ROLES:
            gaps.append(f"{entry.get('id')}: no curated role")
            continue
        carries = link_carries(entry)
        if carries is None:
            gaps.append(f"{entry.get('id')}: artefact classes unknown (no carries)")
            continue
        if role == "principal" and artefact_class in carries:
            principals.append(entry)

    if not principals and not zeros:
        gaps.append(f"no principal {artefact_class} artefact in the registry")

    seen_records: dict[str, str] = {}  # scored DOI -> first declaring entry
    for entry in principals:
        home = entry.get("home")
        if home == "supplement":
            zeros.append(f"{entry['id']}: journal supplement only, no deposit record (Row 6)")
        elif home == "unmanaged":
            zeros.append(f"{entry['id']}: unmanaged hosting, no metadata record (AP-3)")
        elif home == "repository":
            doi = str(entry.get("scored_version") or entry.get("link") or "")
            # Two entries can resolve to one scored version (a concept DOI and
            # its selected version): test that record once.
            if doi in seen_records:
                continue
            seen_records[doi] = str(entry["id"])
            record = datacite_record(pack or {}, doi)
            if record is None:
                gaps.append(f"{entry['id']}: no resolved DataCite record for {doi} in the pack")
                continue
            status, reasons, read = check_deposit(record)
            inputs.append(dict(read, declared_id=entry["id"]))
            (zeros if status == MECHANICAL_0 else confirms).extend(reasons)
        else:
            gaps.append(f"{entry['id']}: no curated home")

    # Conjunction: any mechanical 0 decides; otherwise a gap blocks the rule.
    if zeros:
        result.update(status=MECHANICAL_0, rule_value=0, reasons=zeros)
    elif gaps:
        result.update(status=NO_INPUT, rule_value=None, reasons=gaps)
    else:
        result.update(status=CONFIRM_1, rule_value=None, reasons=confirms)
    result["unresolved_inputs"] = gaps if zeros else []
    result["inputs_read"] = inputs
    return result


def sha256_file(path: Path) -> str:
    """Return the sha256 hex digest of a file's bytes."""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    """CLI entry point: score every registry paper, write one JSON report."""
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--registry", type=Path, default=DEFAULT_REGISTRY)
    parser.add_argument("--packs", type=Path, required=True,
                        help="directory of harvester v1.2 packs (<slug>.json)")
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()

    registry = yaml.safe_load(args.registry.read_text(encoding="utf-8")) or {}
    results: list[dict] = []
    pack_hashes: dict[str, str | None] = {}
    for slug, spec in sorted((registry.get("papers") or {}).items()):
        pack_path = args.packs / f"{slug}.json"
        pack = None
        if pack_path.exists():
            pack = json.loads(pack_path.read_text(encoding="utf-8"))
            if not str(pack.get("harvester_version", "")).startswith("1.2"):
                sys.exit(f"{pack_path}: harvester v1.2 pack required (descriptive fields)")
            pack_hashes[slug] = sha256_file(pack_path)
        else:
            pack_hashes[slug] = None
        for artefact_class in ARTEFACT_CLASSES:
            results.append(score_item(slug, spec, pack, artefact_class))

    def rel(path: Path) -> str:
        resolved = path.resolve()
        return str(resolved.relative_to(REPO_ROOT)) if resolved.is_relative_to(REPO_ROOT) \
            else str(path)

    report = {
        "generated_by": f"scripts/score-f2-rule.py v{RULE_VERSION}",
        "rule": "AP-15 (E8-v2 adjudication log, ruled 2026-10-03); scope ruled 2026-10-04",
        "registry": rel(args.registry),
        "registry_sha256": sha256_file(args.registry),
        "packs": {slug: {"file": rel(args.packs / f"{slug}.json"), "sha256": digest}
                  for slug, digest in pack_hashes.items()},
        "results": results,
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n",
                        encoding="utf-8")
    for item in results:
        print(f"{item['paper']:<22} {item['artefact']:<10} {item['status']:<20} "
              f"{item['rule_value']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
