#!/usr/bin/env python3
"""
h13-rederive.py — independent, blinded re-derivation of the two validation-phase gate
statistics (3-run stability and concordance against the E8-v2 reference) for six
FAIR-scoring model arms.

Purpose
-------
Amendment 1 to the Phase 2 preregistration (DOI 10.17605/OSF.IO/DQNHG), section 3,
fixes the 3-run stability statistic as the *unanimity proportion* ("the proportion of
sub-principle items on which all three runs agree") with a 0.90 gate, and sets a
concordance floor of "at least 0.90 (same statistic) against the pilot reference
scores". This script recomputes, for each arm:

1. stability — the unanimity proportion over the 150 sub-principle items
   (5 papers x 2 sections x 15 sub-principles);
2. concordance against the E8-v2 reference, over all items and with the items the
   reference tags as "beyond instrument" (BI) excluded, under three readings of
   "same statistic" (see READINGS below), each with over-/under-credit direction.

It reads only the arm score payloads and the E8-v2 reference files, and was written
without sight of any other derivation of these figures.

Readings of "concordance (same statistic)"
------------------------------------------
- A (primary, "four-way unanimity"): an item is concordant iff all three runs agree
  with each other AND their common score equals the reference score.
- B ("per-run agreement"): each run is compared with the reference separately; the
  statistic is the pooled proportion of run-items agreeing (= mean of the three
  per-run proportions, as the denominators are equal). Per-run values and the
  minimum are also reported.
- C ("majority vote"): the item's arm score is the majority of the three binary runs
  (always defined for three binary votes); concordant iff it equals the reference.
- D (supplementary, not recommended): among items on which the three runs are
  unanimous, the proportion whose unanimous score equals the reference.

Usage
-----
Run from the repository root::

    python3 studies/open-science-compliance/outputs/validation/\\
h13-rederivation-2026-10-04/h13-rederive.py

Writes ``h13-results.json`` next to this script and prints a summary table.

Conventions
-----------
- No intermediate rounding: all proportions are held as ``fractions.Fraction`` and
  gate comparisons are exact; floats appear only in the output, rounded to 3 dp
  for display alongside the exact count/denominator.
- Gate: a statistic clears when proportion >= 0.90 (registration §8(a) "≥ 0.90";
  amendment 1 §3 "at least 0.90").
"""

from __future__ import annotations

import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any

# --------------------------------------------------------------------------------------
# Configuration: inputs are named explicitly (no directory listing or globbing), so the
# script touches nothing outside the permitted input set.
# --------------------------------------------------------------------------------------

REPO_ROOT = Path.cwd()
VALIDATION_DIR = REPO_ROOT / "studies/open-science-compliance/outputs/validation"
REFERENCE_DIR = VALIDATION_DIR / "e8-v2-rederivation/reference"
OUTPUT_DIR = Path(__file__).resolve().parent
OUTPUT_JSON = OUTPUT_DIR / "h13-results.json"

#: Arm label -> directory holding run-1..run-3 (benchmark arms ran at "xhigh" effort).
ARMS: dict[str, Path] = {
    "sonnet-5 (xhigh)": VALIDATION_DIR / "benchmark-2026-08-17/arm-sonnet-5",
    "opus-5 (xhigh)": VALIDATION_DIR / "benchmark-2026-08-17/arm-opus-5",
    "fable-5 (xhigh)": VALIDATION_DIR / "benchmark-2026-08-17/arm-fable-5",
    "sonnet-5-high": VALIDATION_DIR / "effort-study-2026-08-17/arm-sonnet-5-high",
    "sonnet-5-max": VALIDATION_DIR / "effort-study-2026-08-17/arm-sonnet-5-max",
    "opus-5-high": VALIDATION_DIR / "effort-study-2026-08-17/arm-opus-5-high",
}
RUNS: tuple[int, ...] = (1, 2, 3)
SLUGS: tuple[str, ...] = (
    "crema-et-al-2024",
    "dye-et-al-2023",
    "herskind-riede-2024",
    "key-et-al-2024",
    "marwick-2025",
)
SECTIONS: tuple[str, ...] = ("data_fair", "code_fair")

#: The 15 GO-FAIR sub-principles (registration §7.1), in payload key form.
SUB_PRINCIPLES: tuple[str, ...] = (
    "F1", "F2", "F3", "F4",
    "A1", "A1_1", "A1_2", "A2",
    "I1", "I2", "I3",
    "R1", "R1_1", "R1_2", "R1_3",
)

#: Reference files use descriptive leaf keys grouped by principle; map each to the
#: payload's short code. An explicit table (rather than prefix parsing) means any
#: unexpected key fails loudly instead of being silently mis-assigned.
REFERENCE_KEY_TO_CODE: dict[str, str] = {
    "F1_persistent_identifier": "F1",
    "F2_rich_metadata": "F2",
    "F3_metadata_includes_identifier": "F3",
    "F4_searchable_registry": "F4",
    "A1_standard_protocol": "A1",
    "A1_1_open_free_protocol": "A1_1",
    "A1_2_auth_where_needed": "A1_2",
    "A2_metadata_persistent": "A2",
    "I1_formal_language": "I1",
    "I2_fair_vocabularies": "I2",
    "I3_qualified_references": "I3",
    "R1_rich_metadata": "R1",
    "R1_1_clear_licence": "R1_1",
    "R1_2_provenance": "R1_2",
    "R1_3_community_standards": "R1_3",
}
REFERENCE_GROUPS: tuple[str, ...] = ("findable", "accessible", "interoperable", "reusable")

GATE = Fraction(9, 10)

#: An item is identified by (paper slug, section, sub-principle code).
ItemKey = tuple[str, str, str]


# --------------------------------------------------------------------------------------
# Loading and validation
# --------------------------------------------------------------------------------------


def load_json(path: Path) -> Any:
    """Load and return the JSON document at ``path``.

    Args:
        path: File to read.

    Returns:
        The parsed JSON value.
    """
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def validate_score(value: Any, where: str, anomalies: list[str]) -> int | None:
    """Return a binary score as ``int`` or record an anomaly and return ``None``.

    Booleans are rejected deliberately (``True`` is an ``int`` subclass in Python), so a
    payload that wrote ``true`` instead of ``1`` is surfaced rather than coerced.

    Args:
        value: The raw ``present`` value from a payload or reference leaf.
        where: Human-readable location for the anomaly message.
        anomalies: List to which any anomaly description is appended.

    Returns:
        0 or 1, or ``None`` if the value is missing, null, or not a binary integer.
    """
    if isinstance(value, bool) or not isinstance(value, int) or value not in (0, 1):
        anomalies.append(f"non-binary or missing score at {where}: {value!r}")
        return None
    return value


def load_reference(anomalies: list[str]) -> tuple[dict[ItemKey, int], dict[ItemKey, list[str]]]:
    """Load the E8-v2 reference scores and beyond-instrument (BI) tags.

    An item is BI-tagged when its leaf ``beyond_instrument`` field is a non-empty list.
    Only the leaf ``present`` value is used as the reference score; ``old_present``
    (the pre-re-derivation value) is ignored.

    Args:
        anomalies: List to which any structural anomaly is appended.

    Returns:
        A pair ``(scores, bi_tags)``: reference score per item, and the BI tag list for
        every BI-tagged item.

    Raises:
        SystemExit: If a reference file has an unexpected key or item set, since the
            denominator cannot then be trusted.
    """
    scores: dict[ItemKey, int] = {}
    bi_tags: dict[ItemKey, list[str]] = {}
    for slug in SLUGS:
        doc = load_json(REFERENCE_DIR / f"{slug}.json")
        if doc.get("slug") != slug:
            sys.exit(f"reference slug mismatch in {slug}.json: {doc.get('slug')!r}")
        assessment = doc["fair_assessment"]
        for section in SECTIONS:
            seen: set[str] = set()
            for group in REFERENCE_GROUPS:
                for key, leaf in assessment[section][group].items():
                    if not isinstance(leaf, dict):
                        continue  # subtotal / max fields
                    if key not in REFERENCE_KEY_TO_CODE:
                        sys.exit(f"unexpected reference key {slug}/{section}/{key}")
                    code = REFERENCE_KEY_TO_CODE[key]
                    if code in seen:
                        sys.exit(f"duplicate reference item {slug}/{section}/{code}")
                    seen.add(code)
                    item: ItemKey = (slug, section, code)
                    score = validate_score(
                        leaf.get("present"), f"reference {slug}/{section}/{key}", anomalies
                    )
                    if score is not None:
                        scores[item] = score
                    tags = leaf.get("beyond_instrument")
                    if not isinstance(tags, list):
                        anomalies.append(
                            f"beyond_instrument not a list at reference {slug}/{section}/{key}"
                            f": {tags!r}"
                        )
                    elif tags:
                        bi_tags[item] = list(tags)
            if seen != set(SUB_PRINCIPLES):
                sys.exit(
                    f"reference item set wrong for {slug}/{section}: "
                    f"missing {sorted(set(SUB_PRINCIPLES) - seen)}"
                )
    return scores, bi_tags


def load_arm_runs(
    arm_dir: Path, anomalies: list[str], provenance: dict[str, Any]
) -> dict[int, dict[ItemKey, int]]:
    """Load the three runs' per-item scores for one arm.

    Every run x paper payload must carry exactly the 15 sub-principles in each of the
    data and code sections. Missing, extra, null, or non-binary scores are recorded as
    anomalies (and, if any occur, handled downstream by excluding the item for that
    arm, which is reported). Sections with ``available: false`` are recorded as an
    anomaly but their per-item scores are used exactly as written.

    Args:
        arm_dir: Arm directory containing ``run-1`` .. ``run-3``.
        anomalies: List to which anomaly descriptions are appended.
        provenance: Dict updated with model identifiers, agent versions, and
            instrument versions seen in the payload receipts.

    Returns:
        Mapping run number -> {item: score}.
    """
    runs: dict[int, dict[ItemKey, int]] = {}
    for run in RUNS:
        scores: dict[ItemKey, int] = {}
        for slug in SLUGS:
            path = arm_dir / f"run-{run}" / f"{slug}.json"
            where = f"{arm_dir.name}/run-{run}/{slug}"
            if not path.is_file():
                anomalies.append(f"missing payload {where}")
                continue
            doc = load_json(path)
            if doc.get("paper_slug") != slug:
                anomalies.append(f"paper_slug mismatch at {where}: {doc.get('paper_slug')!r}")
            if doc.get("status") != "OK":
                anomalies.append(f"status not OK at {where}: {doc.get('status')!r}")
            if doc.get("escalate_reason") is not None:
                anomalies.append(f"escalate_reason set at {where}: {doc['escalate_reason']!r}")
            receipts = doc.get("receipts", {})
            provenance.setdefault("model_id", set()).add(receipts.get("model_id"))
            provenance.setdefault("agent_version", set()).add(receipts.get("agent_version"))
            provenance.setdefault("instrument_versions", set()).add(
                json.dumps(receipts.get("instrument_versions"), sort_keys=True)
            )
            for section in SECTIONS:
                block = doc.get(section) or {}
                if block.get("available") is not True:
                    anomalies.append(
                        f"{section} available={block.get('available')!r} at {where} "
                        "(scores used as recorded)"
                    )
                sub = block.get("sub_principles") or {}
                extra = sorted(set(sub) - set(SUB_PRINCIPLES))
                missing = sorted(set(SUB_PRINCIPLES) - set(sub))
                if extra:
                    anomalies.append(f"extra items {extra} at {where}/{section}")
                if missing:
                    anomalies.append(f"missing items {missing} at {where}/{section}")
                for code in SUB_PRINCIPLES:
                    if code not in sub:
                        continue
                    score = validate_score(
                        sub[code].get("present"), f"{where}/{section}/{code}", anomalies
                    )
                    if score is not None:
                        scores[(slug, section, code)] = score
                # Internal consistency check only: does the recorded total match?
                recorded_total = block.get("total")
                computed = sum(
                    scores.get((slug, section, c), 0) for c in SUB_PRINCIPLES
                )
                if recorded_total != computed:
                    anomalies.append(
                        f"total mismatch at {where}/{section}: recorded {recorded_total!r},"
                        f" item sum {computed}"
                    )
        runs[run] = scores
    return runs


# --------------------------------------------------------------------------------------
# Statistics
# --------------------------------------------------------------------------------------


def stat_record(count: int, denominator: int, **extra: Any) -> dict[str, Any]:
    """Build a result record with exact and display forms of a proportion.

    Args:
        count: Numerator (agreeing items).
        denominator: Number of items in the statistic.
        **extra: Additional fields (e.g. over/under counts) to include.

    Returns:
        Dict with count, denominator, exact fraction string, 3-dp proportion, and
        whether the 0.90 gate is cleared (exact comparison).
    """
    exact = Fraction(count, denominator) if denominator else None
    record: dict[str, Any] = {
        "count": count,
        "denominator": denominator,
        "exact": f"{count}/{denominator}",
        "proportion_3dp": round(float(exact), 3) if exact is not None else None,
        "clears_0_90": (exact >= GATE) if exact is not None else None,
    }
    record.update(extra)
    return record


def stability(runs: dict[int, dict[ItemKey, int]], items: list[ItemKey]) -> dict[str, Any]:
    """Unanimity proportion: share of items on which all three runs give the same score.

    Also reports the mean of the 15 per-sub-principle unanimity proportions, which the
    registration's wording ("mean per-sub-principle agreement") could be read as; with a
    balanced design (10 items per sub-principle) it must equal the pooled value, and the
    equality is asserted.

    Args:
        runs: Run number -> {item: score}.
        items: Items in the denominator (those scored in all three runs).

    Returns:
        A stat record with the per-sub-principle breakdown.
    """
    unanimous = {i for i in items if len({runs[r][i] for r in RUNS}) == 1}
    per_sp: dict[str, Fraction] = {}
    for code in SUB_PRINCIPLES:
        sp_items = [i for i in items if i[2] == code]
        sp_unan = [i for i in sp_items if i in unanimous]
        per_sp[code] = Fraction(len(sp_unan), len(sp_items))
    mean_per_sp = sum(per_sp.values(), Fraction(0)) / len(per_sp)
    pooled = Fraction(len(unanimous), len(items))
    balanced = len({sum(1 for i in items if i[2] == c) for c in SUB_PRINCIPLES}) == 1
    if balanced:
        assert mean_per_sp == pooled, "balanced design: mean per-sp must equal pooled"
    return stat_record(
        len(unanimous),
        len(items),
        mean_of_per_sub_principle=str(mean_per_sp),
        mean_of_per_sub_principle_3dp=round(float(mean_per_sp), 3),
        per_sub_principle={c: str(v) for c, v in per_sp.items()},
        non_unanimous_items=["/".join(i) for i in items if i not in unanimous],
    )


def concordance(
    runs: dict[int, dict[ItemKey, int]], reference: dict[ItemKey, int], items: list[ItemKey]
) -> dict[str, Any]:
    """Concordance against the reference under readings A, B, C, and D.

    Direction: with binary scores, an item-level miss is over-credit when the reference
    is 0 (some or all run scores are 1) and under-credit when the reference is 1; no
    item can be both. For reading A, misses are further split into "split" (runs not
    unanimous) and "unanimous-wrong" (all three runs agree, against the reference).

    Args:
        runs: Run number -> {item: score}.
        reference: Item -> reference score.
        items: Items in the denominator.

    Returns:
        Dict keyed by reading letter, each a stat record with direction counts.
    """
    out: dict[str, Any] = {}

    # Reading A: four-way unanimity (r1 = r2 = r3 = reference).
    hits = {i for i in items if all(runs[r][i] == reference[i] for r in RUNS)}
    misses = [i for i in items if i not in hits]
    split = {i for i in misses if len({runs[r][i] for r in RUNS}) > 1}
    out["A_four_way_unanimity"] = stat_record(
        len(hits),
        len(items),
        misses=len(misses),
        over_credit=sum(1 for i in misses if reference[i] == 0),
        under_credit=sum(1 for i in misses if reference[i] == 1),
        misses_split_runs=len(split),
        misses_unanimous_wrong=len(misses) - len(split),
        over_credit_unanimous_wrong=sum(
            1 for i in misses if i not in split and reference[i] == 0
        ),
        under_credit_unanimous_wrong=sum(
            1 for i in misses if i not in split and reference[i] == 1
        ),
        miss_items=[
            {
                "item": "/".join(i),
                "runs": [runs[r][i] for r in RUNS],
                "reference": reference[i],
                "direction": "over" if reference[i] == 0 else "under",
            }
            for i in misses
        ],
    )

    # Reading B: each run against the reference; pooled over run-items.
    per_run: dict[str, Any] = {}
    pooled_hits = pooled_over = pooled_under = 0
    for r in RUNS:
        agree = sum(1 for i in items if runs[r][i] == reference[i])
        over = sum(1 for i in items if runs[r][i] > reference[i])
        under = sum(1 for i in items if runs[r][i] < reference[i])
        per_run[f"run-{r}"] = stat_record(agree, len(items), over_credit=over, under_credit=under)
        pooled_hits += agree
        pooled_over += over
        pooled_under += under
    run_props = [Fraction(per_run[f"run-{r}"]["count"], len(items)) for r in RUNS]
    out["B_per_run_pooled"] = stat_record(
        pooled_hits,
        len(items) * len(RUNS),
        misses=pooled_over + pooled_under,
        over_credit=pooled_over,
        under_credit=pooled_under,
        per_run=per_run,
        min_run_proportion_exact=str(min(run_props)),
        min_run_proportion_3dp=round(float(min(run_props)), 3),
        min_run_clears_0_90=min(run_props) >= GATE,
    )

    # Reading C: majority vote of the three binary runs against the reference.
    def majority(item: ItemKey) -> int:
        """Return the majority score of the three runs for ``item``."""
        return 1 if sum(runs[r][item] for r in RUNS) >= 2 else 0

    c_hits = [i for i in items if majority(i) == reference[i]]
    out["C_majority_vote"] = stat_record(
        len(c_hits),
        len(items),
        misses=len(items) - len(c_hits),
        over_credit=sum(1 for i in items if majority(i) > reference[i]),
        under_credit=sum(1 for i in items if majority(i) < reference[i]),
    )

    # Reading D (supplementary): conditional on unanimous runs.
    unan = [i for i in items if len({runs[r][i] for r in RUNS}) == 1]
    d_hits = [i for i in unan if runs[1][i] == reference[i]]
    out["D_conditional_on_unanimous_runs"] = stat_record(
        len(d_hits),
        len(unan),
        misses=len(unan) - len(d_hits),
        over_credit=sum(1 for i in unan if runs[1][i] > reference[i]),
        under_credit=sum(1 for i in unan if runs[1][i] < reference[i]),
    )
    return out


# --------------------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------------------


def main() -> None:
    """Load inputs, compute every statistic, write ``h13-results.json``, print a table."""
    anomalies: list[str] = []
    reference, bi_tags = load_reference(anomalies)
    all_items: list[ItemKey] = [
        (slug, section, code) for slug in SLUGS for section in SECTIONS for code in SUB_PRINCIPLES
    ]
    results: dict[str, Any] = {
        "script": "h13-rederive.py",
        "data_checks": {
            "reference_items": len(reference),
            "enumerated_items": len(all_items),
            "bi_tagged_items": len(bi_tags),
            "bi_items": [
                {"item": "/".join(i), "tags": t, "reference": reference[i]}
                for i, t in sorted(bi_tags.items())
            ],
            "reference_score_distribution": {
                "ones": sum(reference.values()),
                "zeros": len(reference) - sum(reference.values()),
            },
        },
        "arms": {},
    }

    for arm, arm_dir in ARMS.items():
        arm_anomalies: list[str] = []
        provenance: dict[str, Any] = {}
        runs = load_arm_runs(arm_dir, arm_anomalies, provenance)
        # Items in the denominator: scored in all three runs and in the reference. With
        # clean inputs this is all 150; any shortfall is reported, never silent.
        items = [i for i in all_items if i in reference and all(i in runs[r] for r in RUNS)]
        dropped = [i for i in all_items if i not in items]
        items_no_bi = [i for i in items if i not in bi_tags]
        results["arms"][arm] = {
            "directory": str(arm_dir.relative_to(REPO_ROOT)),
            "provenance": {k: sorted(map(str, v)) for k, v in provenance.items()},
            "anomalies": arm_anomalies,
            "items_dropped": ["/".join(i) for i in dropped],
            "stability": stability(runs, items),
            "concordance_all": concordance(runs, reference, items),
            "concordance_bi_excluded": concordance(runs, reference, items_no_bi),
            "item_scores": {
                "/".join(i): {"runs": [runs[r][i] for r in RUNS], "reference": reference[i]}
                for i in items
            },
        }
        anomalies.extend(f"{arm}: {a}" for a in arm_anomalies)

    results["anomalies"] = anomalies
    OUTPUT_JSON.write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")

    # ---- Console summary --------------------------------------------------------------
    print(f"items={len(all_items)} reference={len(reference)} BI={len(bi_tags)}")
    print(f"anomalies ({len(anomalies)}):")
    for a in anomalies:
        print("  -", a)
    header = f"{'arm':18} {'stability':>16} {'concA all':>22} {'concA noBI':>22}"
    print(header)
    for arm, res in results["arms"].items():
        s = res["stability"]
        ca = res["concordance_all"]["A_four_way_unanimity"]
        cb = res["concordance_bi_excluded"]["A_four_way_unanimity"]
        cells = [f"{arm:18} {s['exact']:>8} {s['proportion_3dp']:.3f}"]
        for c in (ca, cb):
            cells.append(
                f"{c['exact']:>8} {c['proportion_3dp']:.3f}"
                f" o{c['over_credit']}/u{c['under_credit']}"
            )
        print(" ".join(cells))
    print(f"wrote {OUTPUT_JSON.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
