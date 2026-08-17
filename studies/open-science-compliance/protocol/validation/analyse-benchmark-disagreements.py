#!/usr/bin/env python3
"""Mine validation-benchmark outputs for instrument ambiguities.

**Version:** 1.1

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
  pilot reference scores (``manifest.yaml`` ``reference_datasets``),
  with a per-arm error-direction split (over-credit: majority 1 vs
  reference 0; under-credit: majority 0 vs reference 1).

Also re-verifies the guideless-minority correlation noted in the plan's
evidence base (minority votes coming from spawns whose receipts show
``fair-principles-guide.md`` was not pulled) — per arm since v1.1.

Usage (from the repository root)::

    # Legacy three-arm cycle layout (default: the 2026-08-03 cycle)
    python3 studies/open-science-compliance/protocol/validation/\
analyse-benchmark-disagreements.py [--bench-dir DIR]

    # Explicit arm directories, may span cycles (effort-study arms
    # included); --out-dir is REQUIRED so no cycle's disputed-items.json
    # is overwritten implicitly
    python3 studies/open-science-compliance/protocol/validation/\
analyse-benchmark-disagreements.py --arms ARM_DIR [ARM_DIR ...] \
--out-dir DIR

Outputs:

* ``disputed-items.json`` in the output directory — machine-readable
  record of every disputed item (within-arm disagreement or
  majority-vs-reference mismatch) with all evidence strings and, per
  arm, the error direction of any reference mismatch.
* A human-readable summary on stdout, including verification lines that
  compare recomputed statistics with the published ones.

No API calls; reads persisted artefacts only.

Changelog: v1.1 (2026-08-17) adds ``--arms`` (explicit arm directories
spanning cycles — the effort-study arms join the one-pass computation),
``--reference-key``, the per-arm error-direction split, and per-arm
guideless-minority reporting. v1.0 is the audit-F8 state (``--bench-dir``
+ ``--stability-only``).
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
MANIFEST = REPO_ROOT / "manifest.yaml"

# Default (legacy) three-arm cycle layout; --arms replaces this with
# explicit arm directories whose labels derive from their basenames.
DEFAULT_ARMS = ["sonnet-5", "opus-5", "fable-5"]
ARMS: list[str] = DEFAULT_ARMS  # rebound in main()
ARM_DIRS: dict[str, Path] = {}  # label -> arm directory, rebound in main()
PAPERS_PER_RUN = 5
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


def resolve_arms(arm_paths: list[Path]) -> dict[str, Path]:
    """Map explicit ``--arms`` directories to labels (basename minus ``arm-``).

    Fails loudly on a missing directory, a basename without the ``arm-``
    prefix (the layout convention every cycle follows), or a duplicate
    label (two cycles both offering ``arm-sonnet-5`` would silently
    shadow each other in every keyed structure downstream).
    """
    arm_dirs: dict[str, Path] = {}
    for raw in arm_paths:
        arm_dir = raw.resolve()
        if not arm_dir.is_dir():
            sys.exit(f"--arms: not a directory: {raw}")
        if not arm_dir.name.startswith("arm-"):
            sys.exit(f"--arms: basename must start with 'arm-': {raw}")
        label = arm_dir.name[len("arm-"):]
        if label in arm_dirs:
            sys.exit(f"--arms: duplicate arm label {label!r} "
                     f"({arm_dirs[label]} vs {arm_dir})")
        arm_dirs[label] = arm_dir
    return arm_dirs


def error_direction(majority: int, reference: int) -> str | None:
    """Classify a majority-vs-reference mismatch, or None on a match.

    ``over_credit``: the arm awarded a point the reference withholds
    (majority 1, reference 0). ``under_credit``: the arm withheld a point
    the reference awards (majority 0, reference 1).
    """
    if majority == reference:
        return None
    return "over_credit" if majority == 1 else "under_credit"


def load_spawns() -> dict[tuple[str, int, str], dict[str, Any]]:
    """Load all spawn outputs keyed by (arm label, run, paper slug)."""
    spawns: dict[tuple[str, int, str], dict[str, Any]] = {}
    for arm in ARMS:
        for run in RUNS:
            run_dir = ARM_DIRS[arm] / f"run-{run}"
            if not run_dir.is_dir():
                sys.exit(f"missing run directory: {run_dir}")
            paths = sorted(run_dir.glob("*.json"))
            if len(paths) != PAPERS_PER_RUN:
                sys.exit(f"expected {PAPERS_PER_RUN} spawn files in "
                         f"{run_dir}, found {len(paths)}")
            for path in paths:
                payload = json.loads(path.read_text())
                slug = payload.get("paper_slug") or path.stem
                if slug != path.stem:
                    sys.exit(f"paper_slug/filename mismatch: {path}")
                spawns[(arm, run, slug)] = payload
    expected = len(ARMS) * len(RUNS) * PAPERS_PER_RUN
    if len(spawns) != expected:
        sys.exit(f"expected {expected} spawn files, found {len(spawns)}")
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
    """True if this spawn's receipts show the principles guide was read.

    Two delivery eras: pre-A3 the guide was pull-on-demand (appears in
    ``pulled_files_read`` only when the spawn chose to read it — the
    correlation this tool re-checks); post-A3 (promoted to push,
    2026-08-15) it is receipted under ``instrument_receipts`` as
    ``fair-principles-guide``, so post-A3 spawns are never guideless.
    """
    receipts = payload.get("receipts", {})
    pulled = receipts.get("pulled_files_read", []) or []
    if any(GUIDE_BASENAME in p for p in pulled):
        return True
    return "fair-principles-guide" in (
        receipts.get("instrument_receipts", {}) or {}
    )


def load_references(
    reference_key: str = "pilot_fair_assessments",
) -> dict[str, dict[str, dict[str, dict[str, Any]]]]:
    """Load E8-registered reference scores keyed slug -> artefact -> sub.

    Each leaf is ``{"present": int, "evidence": str, "ref_key": str}``.
    Registration is enumerated from ``manifest.yaml`` (never re-derived by
    glob — working-notes Observation 20). ``reference_key`` selects the
    ``reference_datasets`` entry, so a successor reference (E8 v2) joins
    by manifest registration, not by code edit.
    """
    manifest = yaml.safe_load(MANIFEST.read_text())
    datasets = manifest["reference_datasets"]
    if reference_key not in datasets:
        sys.exit(f"reference key {reference_key!r} not in "
                 f"manifest reference_datasets ({sorted(datasets)})")
    items = datasets[reference_key]["items"]
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
    """Recompute statistics, verify them, and emit the disputed-item record."""
    global ARMS, ARM_DIRS
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--bench-dir", type=Path, default=None,
                        help="benchmark cycle directory with the fixed "
                             "three-arm layout (default: the 2026-08-03 "
                             "cycle); mutually exclusive with --arms")
    parser.add_argument("--arms", type=Path, nargs="+", default=None,
                        help="explicit arm directories (arm-<label>), may "
                             "span cycles; requires --out-dir")
    parser.add_argument("--out-dir", type=Path, default=None,
                        help="where disputed-items.json is written "
                             "(default: the bench dir; REQUIRED with "
                             "--arms so no cycle's file is overwritten "
                             "implicitly)")
    parser.add_argument("--reference-key", default="pilot_fair_assessments",
                        help="manifest reference_datasets entry to score "
                             "concordance against (default: the E8 pilot "
                             "reference)")
    parser.add_argument("--stability-only", action="store_true",
                        help="suppress concordance (D3 contract hardening 5: "
                             "no partial concordance against a retired "
                             "reference)")
    cli = parser.parse_args()
    if cli.arms is not None:
        if cli.bench_dir is not None:
            sys.exit("--arms and --bench-dir are mutually exclusive: "
                     "explicit arm dirs replace the cycle layout")
        if cli.out_dir is None:
            sys.exit("--arms requires --out-dir (no implicit overwrite of "
                     "a cycle's disputed-items.json)")
        ARM_DIRS = resolve_arms(cli.arms)
        ARMS = list(ARM_DIRS)
        out_dir = cli.out_dir.resolve()
    else:
        bench_dir = (cli.bench_dir or DEFAULT_BENCH_DIR).resolve()
        ARMS = list(DEFAULT_ARMS)
        ARM_DIRS = {arm: bench_dir / f"arm-{arm}" for arm in ARMS}
        out_dir = (cli.out_dir or bench_dir).resolve()
    stability_only = cli.stability_only
    spawns = load_spawns()
    refs = load_references(cli.reference_key)
    slugs = sorted({slug for (_, _, slug) in spawns})

    published = {}
    for arm in ARMS:
        record = json.loads(
            (ARM_DIRS[arm] / "run-record.json").read_text()
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
                    direction = error_direction(majority, ref["present"])
                    if not stability_only:
                        concordance[arm]["items"] += 1
                        concordance[arm]["agreed"] += int(direction is None)
                        if direction:
                            concordance[arm][direction] += 1
                    if not unanimous or majority != ref["present"]:
                        item_disputed = True
                    arms_detail[arm] = {
                        "votes": votes,
                        "unanimous": unanimous,
                        "majority": majority,
                        "matches_reference": majority == ref["present"],
                        "error_direction": direction,
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
            f"(summary table published to 3 dp); errors: "
            f"{concordance[arm]['over_credit']} over-credit, "
            f"{concordance[arm]['under_credit']} under-credit"
        )

    # Guideless-minority correlation (plan evidence base re-check),
    # per arm since v1.1 — any arm can have guideless spawns.
    print("\n=== Guideless-minority correlation (per arm) ===")
    for arm in ARMS:
        guideless = {
            (run, slug)
            for (spawn_arm, run, slug), payload in spawns.items()
            if spawn_arm == arm and not pulled_guide(payload)
        }
        minority_from_guideless = 0
        splits = 0
        for (slug, artefact, sub), item in disputed.items():
            votes = item["arms"][arm]["votes"]
            if len(set(votes)) == 1:
                continue
            splits += 1
            minority_value = min(set(votes), key=votes.count)
            minority_runs = [
                RUNS[i] for i, v in enumerate(votes) if v == minority_value
            ]
            if any((run, slug) in guideless for run in minority_runs):
                minority_from_guideless += 1
        print(
            f"{arm}: guideless spawns {sorted(guideless)}; 2-1 splits "
            f"{splits}; minority vote from a guideless spawn: "
            f"{minority_from_guideless}"
        )

    print("\n=== Disputed items by sub-principle (any arm, either criterion) ===")
    by_sub = Counter(sub for (_, _, sub) in disputed)
    for sub, count in by_sub.most_common():
        print(f"  {sub}: {count}")
    total_items = len(slugs) * len(ARTEFACTS) * len(SUB_PRINCIPLES)
    print(f"total disputed items: {len(disputed)} of {total_items}")

    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "disputed-items.json"

    def rel(path: Path) -> str:
        try:
            return str(path.relative_to(REPO_ROOT))
        except ValueError:
            return str(path)

    out_path.write_text(
        json.dumps(
            {
                "generated_by":
                    "analyse-benchmark-disagreements.py v1.1 (Phase A1)",
                "criteria": "within-arm disagreement OR majority-vs-reference mismatch",
                "arms": {arm: rel(ARM_DIRS[arm]) for arm in ARMS},
                "reference_key": cli.reference_key,
                "stability_only": stability_only,
                "items": [disputed[k] for k in sorted(disputed)],
            },
            indent=2,
        )
        + "\n"
    )
    print(f"\nwrote {rel(out_path)} ({len(disputed)} items)")


if __name__ == "__main__":
    main()
