#!/usr/bin/env python3
"""Assemble the E8-v2 pilot FAIR reference from the adjudicated worksheet.

**Version:** 1.0

Phase B2 of the instrument-clarification plan: the registrant adjudicated
all 150 reference items (5 pilot papers × data/code × 15 sub-principles) in
ten sittings (2026-09-03, 2026-10-01 → 10-03); the machine copy of those
rulings is ``e8-v2-rederivation/worksheet.json``. This script turns it into
the E8-v2 reference dataset — one JSON file per paper — in the same nesting
the E8 v1 reference uses (``fair_assessment`` → artefact → dimension →
``<ID>_<label>`` leaf carrying ``present``), so the registered analysis tool
(``analyse-benchmark-disagreements.py``) reads it through ``--reference-key``
with no code change: a successor reference joins by manifest registration.

Each leaf also carries the provenance the concordance analysis needs:
``old_present`` (the E8 v1 score), ``changed``, ``beyond_instrument`` (BI
tags — items whose adjudication needed input or a rule outside the frozen
instrument, so concordance can be reported with and without them), and the
adjudication note (used as the leaf's ``evidence``; the v1 evidence string is
kept as ``old_evidence``).

Deterministic: no clock in the content, sorted output, and the worksheet's
sha256 recorded so a reference file is traceable to the exact rulings.

Inputs (committed):
    studies/open-science-compliance/outputs/validation/e8-v2-rederivation/
        worksheet.json, adjudication-log.md

Outputs:
    studies/open-science-compliance/outputs/validation/e8-v2-rederivation/
        reference/<slug>.json   (one per pilot paper)

Usage:
    venv/bin/python scripts/assemble-e8v2-reference.py [--check]

``--check`` rebuilds in memory and exits 1 if any committed reference file
differs (a drift guard for later sessions).
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import defaultdict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
E8V2_DIR = (REPO_ROOT / "studies/open-science-compliance/outputs/validation/"
            "e8-v2-rederivation")
WORKSHEET = E8V2_DIR / "worksheet.json"
OUT_DIR = E8V2_DIR / "reference"
ARTEFACTS = ("data_fair", "code_fair")
# Canonical order and dimension of each sub-principle (mirrors the worksheet
# builder and the E8 v1 extraction layout).
SUB_PRINCIPLES = [
    ("findable", "F1"), ("findable", "F2"), ("findable", "F3"), ("findable", "F4"),
    ("accessible", "A1"), ("accessible", "A1_1"), ("accessible", "A1_2"),
    ("accessible", "A2"),
    ("interoperable", "I1"), ("interoperable", "I2"), ("interoperable", "I3"),
    ("reusable", "R1"), ("reusable", "R1_1"), ("reusable", "R1_2"), ("reusable", "R1_3"),
]
EXPECTED_ITEMS = 150


def build(worksheet_path: Path = WORKSHEET) -> dict[str, dict]:
    """Return {slug: reference document} built from the worksheet.

    Raises:
        SystemExit: on any structural defect — wrong item count, an
            unadjudicated item, a duplicate or missing (paper, artefact,
            sub-principle) cell, or a non-binary score.
    """
    raw = worksheet_path.read_bytes()
    worksheet = json.loads(raw)
    items = worksheet["items"]
    if len(items) != EXPECTED_ITEMS:
        sys.exit(f"expected {EXPECTED_ITEMS} worksheet items, found {len(items)}")
    cells: dict[tuple[str, str, str], dict] = {}
    for item in items:
        key = (item["paper"], item["artefact"], item["sub_principle"])
        if key in cells:
            sys.exit(f"duplicate worksheet cell {key}")
        if item.get("new_score") not in (0, 1):
            sys.exit(f"cell {key} not adjudicated (new_score={item.get('new_score')!r})")
        cells[key] = item
    papers = sorted({paper for paper, _, _ in cells})
    for paper in papers:
        for artefact in ARTEFACTS:
            for _, sub in SUB_PRINCIPLES:
                if (paper, artefact, sub) not in cells:
                    sys.exit(f"missing worksheet cell {(paper, artefact, sub)}")

    digest = hashlib.sha256(raw).hexdigest()
    documents: dict[str, dict] = {}
    for paper in papers:
        assessment: dict = {"version": "E8-v2",
                            "scale": "15 binary sub-principles per artefact type"}
        for artefact in ARTEFACTS:
            dims: dict[str, dict] = defaultdict(dict)
            total = 0
            for dim, sub in SUB_PRINCIPLES:
                item = cells[(paper, artefact, sub)]
                present = int(item["new_score"])
                total += present
                dims[dim][item["ref_key"]] = {
                    "present": present,
                    "evidence": str(item["adjudication_note"]).strip(),
                    "old_present": int(item["old_score"]),
                    "changed": int(item["old_score"]) != present,
                    "beyond_instrument": sorted(item.get("beyond_instrument") or []),
                    "old_evidence": str(item.get("old_evidence") or ""),
                }
            block: dict = {}
            for dim in ("findable", "accessible", "interoperable", "reusable"):
                leaves = dims[dim]
                block[dim] = {**leaves,
                              "subtotal": sum(leaf["present"] for leaf in leaves.values()),
                              "max": len(leaves)}
            block["total"] = total
            block["max"] = len(SUB_PRINCIPLES)
            assessment[artefact] = block
        documents[paper] = {
            "reference_record_version": "1.0",
            "reference": "E8-v2",
            "slug": paper,
            "generated_by": "scripts/assemble-e8v2-reference.py v1.0",
            "worksheet": str(worksheet_path.relative_to(REPO_ROOT)),
            "worksheet_sha256": digest,
            "adjudication_log": str((E8V2_DIR / "adjudication-log.md")
                                    .relative_to(REPO_ROOT)),
            "fair_assessment": assessment,
        }
    return documents


def render(document: dict) -> str:
    """Stable serialisation (the --check drift guard compares these bytes)."""
    return json.dumps(document, indent=2, ensure_ascii=False) + "\n"


def main() -> int:
    """Write (or, with --check, verify) the per-paper reference files."""
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--check", action="store_true",
                        help="verify committed files match a fresh build; write nothing")
    args = parser.parse_args()
    documents = build()
    drift = []
    for slug, document in documents.items():
        path = OUT_DIR / f"{slug}.json"
        text = render(document)
        if args.check:
            if not path.is_file() or path.read_text(encoding="utf-8") != text:
                drift.append(str(path.relative_to(REPO_ROOT)))
            continue
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        data = document["fair_assessment"]
        print(f"{slug}: data {data['data_fair']['total']}/15, "
              f"code {data['code_fair']['total']}/15 → {path.relative_to(REPO_ROOT)}")
    if args.check:
        print("E8-v2 reference: " + ("DRIFT in " + ", ".join(drift) if drift else "in sync"))
        return 1 if drift else 0
    old = sum(leaf["old_present"] for d in documents.values()
              for a in ARTEFACTS for dim in ("findable", "accessible", "interoperable",
                                             "reusable")
              for k, leaf in d["fair_assessment"][a][dim].items() if isinstance(leaf, dict))
    new = sum(d["fair_assessment"][a]["total"] for d in documents.values() for a in ARTEFACTS)
    print(f"reference totals: E8 v1 {old} → E8-v2 {new} of {EXPECTED_ITEMS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
