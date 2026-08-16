#!/usr/bin/env python3
"""Build the E8-v2 reference re-derivation adjudication worksheet (Phase B1).

**Version:** 1.0

Implements the registrant's 2026-08-15 shape ruling (amendment 2 §3):
ruling-driven re-derivation with targeted human adjudication. For every one
of the 150 reference items (5 pilot papers × data/code × 15 sub-principles)
the worksheet carries the old E8 score and evidence, whether the item was
among the 68 disputed items (with per-arm majorities), the applicable
instrument-v2.1 ruling pointers, entailed-flip flags, and blank adjudication
columns (census-surface check; new score; note). A seeded spot-check sample
of undisputed items is pre-selected (seed fixed in this file so the sample
is reproducible, per the no-clock/no-RNG-at-runtime discipline).

Inputs (all committed):
    manifest.yaml (E8 registry — enumeration from the registry, never glob)
    studies/.../benchmark-2026-08/disputed-items.json (the 68)

Outputs:
    studies/open-science-compliance/outputs/validation/e8-v2-rederivation/
        worksheet.md    — the registrant's adjudication document
        worksheet.json  — machine copy (E8-v2 assembly reads adjudicated
                          scores back from the completed worksheet)

Usage:
    venv/bin/python scripts/build-e8v2-worksheet.py
"""

from __future__ import annotations

import json
import random
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
DISPUTED = (REPO_ROOT / "studies/open-science-compliance/outputs/validation/"
            "benchmark-2026-08/disputed-items.json")
OUT_DIR = (REPO_ROOT / "studies/open-science-compliance/outputs/validation/"
           "e8-v2-rederivation")
SPOT_CHECK_SEED = 20260817  # fixed: the sample must be reproducible
SPOT_CHECK_N = 10

# Canonical sub-principle order and the extraction-key prefixes they map to.
SUB_PRINCIPLES = [
    ("findable", "F1"), ("findable", "F2"), ("findable", "F3"),
    ("findable", "F4"),
    ("accessible", "A1"), ("accessible", "A1_1"), ("accessible", "A1_2"),
    ("accessible", "A2"),
    ("interoperable", "I1"), ("interoperable", "I2"), ("interoperable", "I3"),
    ("reusable", "R1"), ("reusable", "R1_1"), ("reusable", "R1_2"),
    ("reusable", "R1_3"),
]

# Instrument-v2.1 ruling pointers per sub-principle (erratum-log Entry 3
# item numbers; "table" = the platform entitlement table).
RULING_POINTERS = {
    "F1": "item 5 (supplement under article DOI = 1)",
    "F2": "item 5 + table row 6 (artefact-level; supplement-only = 0)",
    "F3": "item 5 + table row 6 (artefact-level; supplement-only = 0)",
    "F4": "item 5 + table row 6 (artefact-level; supplement-only = 0)",
    "A1": "unchanged (completeness rule + ethical exception)",
    "A1_1": "unchanged",
    "A1_2": "item 4 (fully open, no auth needed = 1)",
    "A2": "table rows 2/6 (Zenodo persistence entitlements; supplement-only = 0)",
    "I1": "unchanged (aggregation: principal artefacts)",
    "I2": "unchanged (aggregation: principal artefacts)",
    "I3": "item 2 (third-party dependencies enter here)",
    "R1": "unchanged",
    "R1_1": "item 6 (per-artefact; most-restrictive same-artefact; "
            "service licence via pack; default operative)",
    "R1_2": "unchanged",
    "R1_3": "item 7 + graded table row 4 (ADS by construction; "
            "DANS/tDAR need rung-(i))",
}

# Entailed flips documented before re-scoring (amendment 2 §3).
ENTAILED_FLIPS = {
    ("dye-et-al-2023", "data_fair", "R1_3"):
        "ENTAILED: ADS deposit (10.5284/1018290) → R1.3 = 1 by construction "
        "(ruling #4 + graded row 4)",
    ("key-et-al-2024", "data_fair", "A2"):
        "ENTAILED review: A2 under the clarified metadata-persistence "
        "entitlements (Entry 3 consequence note)",
    ("key-et-al-2024", "code_fair", "A2"):
        "ENTAILED review: A2 under the clarified metadata-persistence "
        "entitlements (Entry 3 consequence note)",
}


def sub_key_match(block: dict, code: str) -> tuple[str, dict] | None:
    """Find the extraction key for a canonical sub-principle code.

    Extraction keys look like 'F1_persistent_identifier' or
    'A1_2_auth_where_needed' — the code is the leading token(s).
    """
    for key, value in block.items():
        if key in ("subtotal", "max"):
            continue
        if key == code or key.startswith(code + "_"):
            # Guard against A1 matching A1_1/A1_2: the remainder after the
            # code must not start with a digit.
            rest = key[len(code):]
            if rest.startswith("_") and rest[1:2].isdigit():
                continue
            return key, value
    return None


def load_reference_items() -> list[dict]:
    """All 150 reference items, enumerated from the E8 registry."""
    manifest = yaml.safe_load((REPO_ROOT / "manifest.yaml").read_text())
    registry = manifest["reference_datasets"]["pilot_fair_assessments"]
    assert len(registry["items"]) == registry["cardinality"]
    items = []
    for entry in registry["items"]:
        slug = entry["slug"]
        data = json.loads((REPO_ROOT / entry["file"]).read_text())
        node = data
        for part in entry["fair_key"].split("."):
            node = node[part]
        for artefact in ("data_fair", "code_fair"):
            block = node[artefact]
            for dimension, code in SUB_PRINCIPLES:
                found = sub_key_match(block.get(dimension) or {}, code)
                if found is None:
                    items.append({"paper": slug, "artefact": artefact,
                                  "sub_principle": code, "ref_key": None,
                                  "old_score": None,
                                  "old_evidence": "(no sub-principle record; "
                                                  "available=" + str(block.get("available")) + ")"})
                    continue
                key, value = found
                items.append({
                    "paper": slug, "artefact": artefact, "sub_principle": code,
                    "ref_key": key,
                    "old_score": int(bool(value.get("present"))),
                    "old_evidence": str(value.get("evidence") or ""),
                })
    return items


def main() -> int:
    disputed_doc = json.loads(DISPUTED.read_text())
    disputed = {(i["paper"], i["artefact"], i["sub_principle"]): i
                for i in disputed_doc["items"]}
    items = load_reference_items()
    assert len(items) == 150, f"expected 150 items, got {len(items)}"

    undisputed = [i for i in items
                  if (i["paper"], i["artefact"], i["sub_principle"]) not in disputed]
    rng = random.Random(SPOT_CHECK_SEED)
    spot = {(i["paper"], i["artefact"], i["sub_principle"])
            for i in rng.sample(undisputed, SPOT_CHECK_N)}

    for item in items:
        key = (item["paper"], item["artefact"], item["sub_principle"])
        d = disputed.get(key)
        item["disputed"] = bool(d)
        if d:
            item["arm_majorities"] = {arm: v["majority"]
                                      for arm, v in d["arms"].items()}
        item["ruling"] = RULING_POINTERS[item["sub_principle"]]
        item["entailed_flip"] = ENTAILED_FLIPS.get(key, "")
        item["spot_check"] = key in spot
        item["surface_check"] = ""   # registrant: paper+pack derivable? (y/n)
        item["new_score"] = None     # registrant
        item["adjudication_note"] = ""  # registrant

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "worksheet.json").write_text(
        json.dumps({"generated_by": "scripts/build-e8v2-worksheet.py v1.0",
                    "shape_ruling": "2026-08-15 (amendment 2 §3)",
                    "spot_check_seed": SPOT_CHECK_SEED,
                    "items": items}, indent=1, sort_keys=True) + "\n")

    lines = [
        "# E8-v2 reference re-derivation — adjudication worksheet",
        "",
        "**Generated by:** `scripts/build-e8v2-worksheet.py` v1.0 (regenerate,",
        "never hand-edit the tables' fixed columns; adjudication columns are",
        "the registrant's).",
        "**Procedure (amendment 2 §3, ruled 2026-08-15):** start from the old",
        "E8 score; apply the ratified clarifications item by item; the",
        "registrant adjudicates every disputed item (D), every entailed flip",
        "(F), every item whose old score rests on reproduction-only evidence",
        "(the census-surface check: mark S=n where paper + evidence pack",
        "cannot support the score, then re-derive through the ladder), and",
        "the seeded spot-check sample (C). Unmarked items default to the old",
        "score under the clarified instrument unless the surface check says",
        "otherwise. Blinding: this exercise is unblinded (recorded in the",
        f"amendment). Spot-check seed {SPOT_CHECK_SEED}, n={SPOT_CHECK_N}.",
        "",
        f"**Counts:** 150 items; {len(disputed)} disputed; "
        f"{len(ENTAILED_FLIPS)} entailed-flip rows; {SPOT_CHECK_N} spot-check.",
        "",
        "Columns: old = old E8 score; D = disputed (with per-arm majorities",
        "s/o/f = sonnet/opus/fable); flags = F entailed flip, C spot-check;",
        "S = census-surface check (y = derivable from paper+pack; n = not);",
        "new = adjudicated v2.1 score; note = adjudication note.",
        "",
    ]
    for slug in dict.fromkeys(i["paper"] for i in items):
        for artefact in ("data_fair", "code_fair"):
            rows = [i for i in items
                    if i["paper"] == slug and i["artefact"] == artefact]
            lines.append(f"## {slug} — {artefact}")
            lines.append("")
            lines.append("| sub | old | D (s/o/f) | flags | v2.1 ruling | "
                         "old evidence | S | new | note |")
            lines.append("|---|---|---|---|---|---|---|---|---|")
            for i in rows:
                dcell = ""
                if i["disputed"]:
                    m = i["arm_majorities"]
                    dcell = (f"D {m.get('sonnet-5','?')}/"
                             f"{m.get('opus-5','?')}/{m.get('fable-5','?')}")
                flags = " ".join(p for p in (
                    "F" if i["entailed_flip"] else "",
                    "C" if i["spot_check"] else "") if p)
                evidence = i["old_evidence"].replace("|", "/")[:70]
                lines.append(f"| {i['sub_principle']} | {i['old_score']} | "
                             f"{dcell} | {flags} | {i['ruling'][:52]} | "
                             f"{evidence} |  |  |  |")
            lines.append("")
            flips = [i for i in rows if i["entailed_flip"]]
            for i in flips:
                lines.append(f"- **{i['sub_principle']} flip note:** "
                             f"{i['entailed_flip']}")
            if flips:
                lines.append("")
    (OUT_DIR / "worksheet.md").write_text("\n".join(lines) + "\n")
    print(f"worksheet: 150 items, {len(disputed)} disputed, "
          f"{SPOT_CHECK_N} spot-check → {OUT_DIR.relative_to(REPO_ROOT)}/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
