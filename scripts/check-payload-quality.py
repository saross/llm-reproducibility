#!/usr/bin/env python3
"""Mechanical quality checks over committed FAIR scoring payloads.

**Version:** 1.0

Effort-study quality layer (a) — deterministic, no-spend checks that run
over an assembled arm directory's ``run-<N>/<slug>.json`` payloads
(operator-accepted quality-judgement approach, plan decision log
2026-08-17). Three checks:

1. **pack_refs validity** — every cited evidence-pack record id must
   exist in the paper's committed pack (``corpus/evidence-packs/``,
   enumerated from ``manifest.yaml``). An unresolvable pack_ref is a
   fabricated citation and fails the run (exit 1).
2. **A1-rule consistency** — the instrument's A1 cross-reference: data
   coverage_category minimal/partial with data A1 = 1 requires a named
   ``a1_exception_rationale`` (the S4 retreat moved this conditional out
   of the spawn-side schema, so it is re-checked here).
3. **pack-utilisation rate** — per arm: the fraction of scored
   sub-principles citing at least one pack_ref, and the total citation
   count. Informational (differences across effort levels show whether
   extra effort goes into using rung-(i) evidence).

Usage:
    venv/bin/python scripts/check-payload-quality.py <arm_dir> [<arm_dir> ...]

Exit status: 1 if any invalid pack_ref or A1-rule violation is found in
any arm; 0 otherwise. Utilisation is never a failure condition.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
ARTEFACTS = ("data_fair", "code_fair")
SUBS = ("F1", "F2", "F3", "F4", "A1", "A1_1", "A1_2", "A2",
        "I1", "I2", "I3", "R1", "R1_1", "R1_2", "R1_3")


def load_pack_ids() -> dict[str, set[str]]:
    """Slug -> set of record ids, enumerated from the manifest."""
    manifest = yaml.safe_load((REPO_ROOT / "manifest.yaml").read_text())
    packs = manifest["evidence_packs"]["packs"]
    ids: dict[str, set[str]] = {}
    for slug, entry in packs.items():
        pack = json.loads((REPO_ROOT / entry["file"]).read_text())
        ids[slug] = {r["record_id"] for r in pack.get("records", [])}
    return ids


def check_arm(arm_dir: Path, pack_ids: dict[str, set[str]]) -> dict:
    """Run all three checks over one assembled arm directory."""
    bad_refs: list[tuple[str, int, str, str, str]] = []
    a1_violations: list[tuple[str, int]] = []
    scored = cited = citations = 0

    for run in (1, 2, 3):
        for path in sorted((arm_dir / f"run-{run}").glob("*.json")):
            payload = json.loads(path.read_text())
            slug = payload["paper_slug"]
            known = pack_ids.get(slug, set())
            for artefact in ARTEFACTS:
                for sub in SUBS:
                    node = payload[artefact]["sub_principles"][sub]
                    refs = node.get("pack_refs") or []
                    scored += 1
                    if refs:
                        cited += 1
                        citations += len(refs)
                    for ref in refs:
                        if ref not in known:
                            bad_refs.append((slug, run, artefact, sub, ref))
            coverage = payload["data_completeness"]["coverage_category"]
            a1 = payload["data_fair"]["sub_principles"]["A1"]["present"]
            if coverage in ("minimal", "partial") and int(a1) == 1 \
                    and not payload.get("a1_exception_rationale"):
                a1_violations.append((slug, run))

    return {
        "arm": arm_dir.name,
        "sub_principles_scored": scored,
        "pack_refs_invalid": bad_refs,
        "a1_rule_violations": a1_violations,
        "utilisation": {
            "sub_principles_citing_pack": cited,
            "rate": round(cited / scored, 4) if scored else None,
            "total_citations": citations,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("arm_dirs", nargs="+", type=Path)
    args = parser.parse_args()

    pack_ids = load_pack_ids()
    failed = False
    for arm_dir in args.arm_dirs:
        result = check_arm(arm_dir, pack_ids)
        util = result["utilisation"]
        print(f"== {result['arm']} ==")
        print(f"  sub-principles scored: {result['sub_principles_scored']}")
        print(f"  pack-utilisation: {util['sub_principles_citing_pack']} citing "
              f"({util['rate']:.1%}), {util['total_citations']} citations")
        if result["pack_refs_invalid"]:
            failed = True
            print(f"  INVALID pack_refs ({len(result['pack_refs_invalid'])}):")
            for slug, run, artefact, sub, ref in result["pack_refs_invalid"]:
                print(f"    {slug} r{run} {artefact}.{sub}: {ref!r}")
        else:
            print("  pack_refs: all resolve against committed packs")
        if result["a1_rule_violations"]:
            failed = True
            print(f"  A1-RULE violations ({len(result['a1_rule_violations'])}):")
            for slug, run in result["a1_rule_violations"]:
                print(f"    {slug} r{run}: coverage partial/minimal, A1=1, "
                      f"no a1_exception_rationale")
        else:
            print("  A1 cross-reference rule: consistent")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
