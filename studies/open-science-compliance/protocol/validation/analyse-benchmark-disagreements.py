#!/usr/bin/env python3
"""Mine the 2026-08 validation-benchmark outputs for instrument ambiguities.

Phase A1 of the instrument clarification plan
(``wiki/planning/instrument-clarification-plan.md``). Recomputes the two
registered statistics from primary artefacts — never trusting the published
summaries — then extracts every disputed item with its evidence strings so
that clarification drafting (Phase A2) works from observed failures.

Statistics recomputed and verified against the run records and
``benchmark-summary.md``:

* **Stability** — unanimity proportion across three runs per arm
  (150 items: 5 papers x 2 artefact types x 15 sub-principles).
* **Concordance** — majority-vote item agreement with the E8-registered
  pilot reference scores (``manifest.yaml`` ``reference_datasets``).

Also re-verifies the sonnet guideless-minority correlation noted in the
plan's evidence base (minority votes coming from spawns whose receipts show
``fair-principles-guide.md`` was not pulled).

Usage (from the repository root)::

    python3 studies/open-science-compliance/protocol/validation/\
analyse-benchmark-disagreements.py

Outputs:

* ``disputed-items.json`` in the benchmark package — machine-readable
  record of every disputed item (within-arm disagreement or
  majority-vs-reference mismatch) with all evidence strings.
* A human-readable summary on stdout, including verification lines that
  compare recomputed statistics with the published ones.

No API calls; reads persisted artefacts only.
"""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parents[4]
# Audit F8 (2026-08-17): the benchmark directory is a CLI argument, not a
# constant — running this against a new cycle must be explicit, and the
# concordance half is suppressible: computing concordance against the OLD
# E8 reference for a post-clarification cycle is exactly what the D3 run
# contract's hardening 5 forbids (partial concordance).
DEFAULT_BENCH_DIR = (
    REPO_ROOT
    / "studies/open-science-compliance/outputs/validation/benchmark-2026-08"
)
BENCH_DIR = DEFAULT_BENCH_DIR  # rebound in main() from --bench-dir
MANIFEST = REPO_ROOT / "manifest.yaml"

ARMS = ["sonnet-5", "opus-5", "fable-5"]
RUNS = [1, 2, 3]
ARTEFACTS = ["data_fair", "code_fair"]
SUB_PRINCIPLES = [
    "F1", "F2", "F3", "F4",
    "A1", "A1_1", "A1_2", "A2",
    "I1", "I2", "I3",
    "R1", "R1_1", "R1_2", "R1_3",
]
GUIDE_BASENAME = "fair-principles-guide.md"

# Reference files name sub-principles with descriptive suffixes
# (e.g. ``A1_2_auth_where_needed``); the ID is the leading token(s).
REF_KEY_ID = re.compile(r"^([FAIR]\d+(?:_\d+)?)(?=_[A-Za-z])")


def load_spawns() -> dict[tuple[str, int, str], dict[str, Any]]:
    """Load all 45 spawn outputs keyed by (arm, run, paper slug)."""
    spawns: dict[tuple[str, int, str], dict[str, Any]] = {}
    for arm in ARMS:
        for run in RUNS:
            run_dir = BENCH_DIR / f"arm-{arm}" / f"run-{run}"
            for path in sorted(run_dir.glob("*.json")):
                payload = json.loads(path.read_text())
                slug = payload.get("paper_slug") or path.stem
                if slug != path.stem:
                    sys.exit(f"paper_slug/filename mismatch: {path}")
                spawns[(arm, run, slug)] = payload
    if len(spawns) != len(ARMS) * len(RUNS) * 5:
        sys.exit(f"expected 45 spawn files, found {len(spawns)}")
    return spawns


def spawn_score(payload: dict[str, Any], artefact: str, sub: str) -> int:
    """Return the 0/1 score one spawn gave one sub-principle."""
    node = payload[artefact]["sub_principles"][sub]
    present = node["present"]
    if present not in (0, 1, True, False):
        sys.exit(f"unexpected present value {present!r}")
    return int(present)


def spawn_evidence(payload: dict[str, Any], artefact: str, sub: str) -> str:
    """Return the evidence string one spawn gave one sub-principle."""
    return str(payload[artefact]["sub_principles"][sub].get("evidence", ""))


def pulled_guide(payload: dict[str, Any]) -> bool:
    """True if this spawn's receipts show the principles guide was read."""
    pulled = payload.get("receipts", {}).get("pulled_files_read", []) or []
    return any(GUIDE_BASENAME in p for p in pulled)


def load_references() -> dict[str, dict[str, dict[str, dict[str, Any]]]]:
    """Load E8-registered reference scores keyed slug -> artefact -> sub.

    Each leaf is ``{"present": int, "evidence": str, "ref_key": str}``.
    Registration is enumerated from ``manifest.yaml`` (never re-derived by
    glob — working-notes Observation 20).
    """
    manifest = yaml.safe_load(MANIFEST.read_text())
    items = manifest["reference_datasets"]["pilot_fair_assessments"]["items"]
    if len(items) != 5:
        sys.exit(f"expected 5 reference items, found {len(items)}")
    refs: dict[str, dict[str, dict[str, dict[str, Any]]]] = {}
    for item in items:
        slug = item["slug"]
        payload = json.loads((REPO_ROOT / item["file"]).read_text())
        node: Any = payload
        for part in item["fair_key"].split("."):
            node = node[part]
        refs[slug] = {}
        for artefact in ARTEFACTS:
            refs[slug][artefact] = {}
            for dim, dim_node in node[artefact].items():
                if not isinstance(dim_node, dict):
                    continue  # available flag and similar scalars
                for ref_key, leaf in dim_node.items():
                    if not isinstance(leaf, dict) or "present" not in leaf:
                        continue  # subtotal / max entries
                    match = REF_KEY_ID.match(ref_key)
                    if not match:
                        sys.exit(f"unmappable reference key {ref_key!r}")
                    refs[slug][artefact][match.group(1)] = {
                        "present": int(bool(leaf["present"])),
                        "evidence": str(leaf.get("evidence", "")),
                        "ref_key": ref_key,
                    }
            missing = set(SUB_PRINCIPLES) - set(refs[slug][artefact])
            if missing:
                sys.exit(f"{slug} {artefact} reference missing {sorted(missing)}")
    return refs


def main() -> None:
    global BENCH_DIR
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--bench-dir", type=Path, default=DEFAULT_BENCH_DIR,
                        help="benchmark cycle directory (default: the "
                             "2026-08-03 cycle)")
    parser.add_argument("--stability-only", action="store_true",
                        help="suppress concordance (D3 contract hardening 5: "
                             "no partial concordance against a retired "
                             "reference)")
    cli = parser.parse_args()
    BENCH_DIR = cli.bench_dir.resolve()
    stability_only = cli.stability_only
    """Recompute statistics, verify them, and emit the disputed-item record."""
    spawns = load_spawns()
    refs = load_references()
    slugs = sorted({slug for (_, _, slug) in spawns})

    published = {}
    for arm in ARMS:
        record = json.loads(
            (BENCH_DIR / f"arm-{arm}" / "run-record.json").read_text()
        )
        # A fresh cycle's run records carry no published stability figure
        # yet (this tool is what derives it); the cross-check is only
        # meaningful against a cycle whose figures were already published.
        published[arm] = record.get("stability")

    disputed: dict[tuple[str, str, str], dict[str, Any]] = {}
    stability: dict[str, Counter] = {arm: Counter() for arm in ARMS}
    concordance: dict[str, Counter] = {arm: Counter() for arm in ARMS}

    for slug in slugs:
        for artefact in ARTEFACTS:
            for sub in SUB_PRINCIPLES:
                item_key = (slug, artefact, sub)
                ref = refs[slug][artefact][sub]
                arms_detail: dict[str, Any] = {}
                item_disputed = False
                for arm in ARMS:
                    votes = [
                        spawn_score(spawns[(arm, run, slug)], artefact, sub)
                        for run in RUNS
                    ]
                    unanimous = len(set(votes)) == 1
                    majority = int(sum(votes) >= 2)
                    stability[arm]["items"] += 1
                    stability[arm]["agreed"] += int(unanimous)
                    if not stability_only:
                        concordance[arm]["items"] += 1
                        concordance[arm]["agreed"] += int(majority == ref["present"])
                    if not unanimous or majority != ref["present"]:
                        item_disputed = True
                    arms_detail[arm] = {
                        "votes": votes,
                        "unanimous": unanimous,
                        "majority": majority,
                        "matches_reference": majority == ref["present"],
                        "evidence_by_run": {
                            str(run): spawn_evidence(
                                spawns[(arm, run, slug)], artefact, sub
                            )
                            for run in RUNS
                        },
                    }
                if item_disputed:
                    disputed[item_key] = {
                        "paper": slug,
                        "artefact": artefact,
                        "sub_principle": sub,
                        "reference": ref,
                        "arms": arms_detail,
                    }

    print("=== Verification against published figures ===")
    for arm in ARMS:
        agreed, items = stability[arm]["agreed"], stability[arm]["items"]
        pub = published[arm]
        if pub is None:
            print(f"{arm}: stability {agreed}/{items} = {agreed / items:.4f} "
                  f"(fresh cycle — no published figure to verify against)")
        else:
            flag = "OK" if (agreed, items) == (pub["agreed"], pub["items"]) else "MISMATCH"
            print(
                f"{arm}: stability {agreed}/{items} = {agreed / items:.4f} "
                f"(run-record {pub['agreed']}/{pub['items']}) {flag}"
            )
        if stability_only:
            print(f"{arm}: concordance SUPPRESSED (--stability-only; "
                  f"pending E8 v2)")
            continue
        c_agreed, c_items = concordance[arm]["agreed"], concordance[arm]["items"]
        print(
            f"{arm}: concordance {c_agreed}/{c_items} = {c_agreed / c_items:.4f} "
            f"(summary table published to 3 dp)"
        )

    # Sonnet guideless-minority correlation (plan evidence base re-check).
    print("\n=== Sonnet guideless-minority correlation ===")
    guideless = {
        (run, slug)
        for (arm, run, slug), payload in spawns.items()
        if arm == "sonnet-5" and not pulled_guide(payload)
    }
    print(f"guideless sonnet spawns: {sorted(guideless)}")
    minority_from_guideless = 0
    splits = 0
    for (slug, artefact, sub), item in disputed.items():
        votes = item["arms"]["sonnet-5"]["votes"]
        if len(set(votes)) == 1:
            continue
        splits += 1
        minority_value = min(set(votes), key=votes.count)
        minority_runs = [RUNS[i] for i, v in enumerate(votes) if v == minority_value]
        if any((run, slug) in guideless for run in minority_runs):
            minority_from_guideless += 1
    print(
        f"sonnet 2-1 splits: {splits}; minority vote from a guideless spawn: "
        f"{minority_from_guideless}"
    )

    print("\n=== Disputed items by sub-principle (any arm, either criterion) ===")
    by_sub = Counter(sub for (_, _, sub) in disputed)
    for sub, count in by_sub.most_common():
        print(f"  {sub}: {count}")
    print(f"total disputed items: {len(disputed)} of 150")

    out_path = BENCH_DIR / "disputed-items.json"
    out_path.write_text(
        json.dumps(
            {
                "generated_by": "analyse-benchmark-disagreements.py (Phase A1)",
                "criteria": "within-arm disagreement OR majority-vs-reference mismatch",
                "items": [disputed[k] for k in sorted(disputed)],
            },
            indent=2,
        )
        + "\n"
    )
    print(f"\nwrote {out_path.relative_to(REPO_ROOT)} ({len(disputed)} items)")


if __name__ == "__main__":
    main()
