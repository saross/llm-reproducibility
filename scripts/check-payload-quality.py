#!/usr/bin/env python3
"""Mechanical quality checks over committed FAIR scoring payloads.

**Version:** 1.1

Effort-study quality layer (a) — deterministic, no-spend checks that run
over an assembled arm directory's ``run-<N>/<slug>.json`` payloads
(operator-accepted quality-judgement approach, plan decision log
2026-08-17). Three checks:

1. **pack_refs validity** (C6 from v1.1) — every cited evidence-pack
   record id must exist in the paper's committed pack
   (``corpus/evidence-packs/``, enumerated from ``manifest.yaml``). An
   unresolvable pack_ref is a fabricated citation and fails the run
   (exit 1).
2. **A1-rule consistency** (C4 from v1.1) — the instrument's A1
   cross-reference: data coverage_category minimal/partial with data
   A1 = 1 requires a named ``a1_exception_rationale`` (the S4 retreat
   moved this conditional out of the spawn-side schema, so it is
   re-checked here).
3. **pack-utilisation rate** — per arm: the fraction of scored
   sub-principles citing at least one pack_ref, and the total citation
   count. Informational (differences across effort levels show whether
   extra effort goes into using rung-(i) evidence).

v1.1 (2026-10-04; Layer 1 of the mechanical-check policy, ruled by Shawn
2026-10-04 — ``wiki/planning/deterministic-output-checks.md``, "Layer 1"
and "Disagreement policy" item 1): **derived quantities are computed, not
merely checked.** Each derived field is recomputed from the scored items
and counts. On disagreement the computed value governs automatically and
the model's value is kept only as a consistency signal. Every finding
records both values, the rule version (``RULES_VERSION``), and which value
governed (policy item 4). Payload files are evidence and are never
modified: computed values live only in this checker's report. Check ids
follow the planning note's Layer 1 table.

- **C1 section total.** For ``data_fair`` and ``code_fair``, the computed
  total is the sum of the 15 sub-principle ``present`` values (the
  registered definition: total = the item sum).
- **C2 coverage percentage.** Computed as
  ``100 × datasets_accessible_tier_0_2 / datasets_enumerated`` (FAIR
  instrument, data-completeness coverage procedure, step 3). *Tolerance:*
  a disagreement is ``|recorded − computed| > 0.5`` percentage points;
  exactly 0.5 agrees. Models round the percentage to one decimal place or
  to a whole number (4/12 is recorded as 33), and an inclusive 0.5 pp
  admits any rounding to a whole percentage, including either reading of
  a half (1/8 = 12.5 recorded as 12 or 13). A genuine one-dataset slip
  moves the percentage by 100/enumerated pp, which exceeds the tolerance
  whenever fewer than 200 datasets are enumerated. The category (C3) is
  computed from the counts, never from the recorded percentage, so a
  sub-tolerance slip cannot change any downstream rule.
- **Undefined derivation.** When ``datasets_enumerated`` is 0 (0/0), or
  the counts are unusable (missing, not non-negative integers, or more
  accessible datasets than enumerated ones), no computed value exists.
  The recorded percentage and category then stand (governing ``model``)
  and each is flagged for review; the run does not crash.
- **C3 coverage category.** Computed from the exact fraction
  accessible/enumerated, never from a rounded percentage. *Boundary
  reading:* the instrument states the bands as whole percentages
  (complete 100%, substantial 75–99%, partial 25–74%, minimal 0–24%),
  which leave gaps (99.5%, 74.6%, and 24.6% fall in no band). This
  checker reads them as intervals on the fraction with inclusive lower
  bounds: **complete** iff accessible == enumerated (enumerated > 0);
  **substantial** iff fraction ≥ 0.75; **partial** iff fraction ≥ 0.25;
  **minimal** otherwise. So 3/4 is substantial, 1/4 is partial, 199/200
  is substantial (never rounded up to complete), and 74.9% is partial.
  The comparisons run in exact integer arithmetic
  (``4 × accessible ≥ 3 × enumerated``), so floating-point error cannot
  move a boundary.
- **C4 A1 cross-reference.** Now judged against the *governing* category:
  the computed one, or the recorded one when the derivation is undefined.
  Where the outcome would differ under the recorded category, the report
  says so (on the violation itself, or as a ``note`` when the computed
  category clears an apparent violation).
- **C5 unavailable but scored.** ``available: false`` with any
  sub-principle scored 1 is flagged. It is never a failure and never an
  override: nothing in the instrument derives the items from
  ``available``, so the scores stand for human review.
- **ESCALATE payloads** (``status`` ``"ESCALATE"``) carry no scoring
  blocks under output schema v1.1, so the scoring checks are skipped and
  the payloads counted. A payload with any other non-``OK`` status, or an
  ``OK`` payload missing a scoring block (schema-invalid; the reconciler
  should have stopped it), is skipped with an **S0 structure** flag
  instead of crashing the run.
- ``--json PATH`` writes a machine-readable report of every finding,
  plus per-arm and overall summary counts. The path may not lie inside an
  arm directory, so the report can never overwrite a payload.

Finding kinds: ``failure`` (C4 violation, C6 invalid ref), ``derived``
(C1–C3 disagreement; ``governing`` is ``computed``), ``flag`` (C5, an
undefined C2/C3 derivation, S0; ``governing`` is ``model`` where a model
value stands), and ``note`` (C4 outcome changed by the computed category;
its C3 finding carries any exit consequence).

Usage:
    venv/bin/python scripts/check-payload-quality.py <arm_dir> [<arm_dir> ...]
    venv/bin/python scripts/check-payload-quality.py --json report.json --strict <arm_dir>

Exit status: 1 if any invalid pack_ref (C6) or A1-rule violation (C4) is
found in any arm; 0 otherwise (unchanged from v1.0; the A1 rule now uses
the governing category). Utilisation is never a failure condition, and
derived-field disagreements are resolved by computation, so by default
they are reported, not failures. With ``--strict``, any derived-field
disagreement or flag also exits 1. Usage errors (an arm directory that
does not exist, a ``--json`` path inside an arm directory) exit 2.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, NamedTuple

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
ARTEFACTS = ("data_fair", "code_fair")
SUBS = ("F1", "F2", "F3", "F4", "A1", "A1_1", "A1_2", "A2",
        "I1", "I2", "I3", "R1", "R1_1", "R1_2", "R1_3")

# Version of the derivation and check rules, recorded in every finding so
# each override can be audited against the rules that produced it
# (disagreement policy item 4). Bump it whenever a rule changes.
RULES_VERSION = "1.1"

# C2 tolerance in percentage points (inclusive); rationale in the module
# docstring.
COVERAGE_TOLERANCE_PP = 0.5
# Absorbs binary floating-point noise at the tolerance edge, so that a
# decimal difference of exactly 0.5 pp never reads as 0.5000000000001.
_FLOAT_SLACK = 1e-9

# Coverage categories under which the instrument's A1 cross-reference sets
# data A1 = 0 unless a documented ethical or legal restriction applies.
A1_RESTRICTED_CATEGORIES = ("minimal", "partial")

CHECK_NAMES: dict[str, str] = {
    "S0": "payload-structure",
    "C1": "section-total",
    "C2": "coverage-percentage",
    "C3": "coverage-category",
    "C4": "a1-cross-reference",
    "C5": "unavailable-but-scored",
    "C6": "pack-refs-validity",
}

KIND_DESCRIPTIONS: dict[str, str] = {
    "failure": "invalid pack_ref (C6) or A1-rule violation (C4); exit 1 in every mode",
    "derived": "derived-field disagreement (C1-C3); the computed value governs; "
               "exit 1 only with --strict",
    "flag": "for human review, never an override (C5, undefined C2/C3 derivation, "
            "S0); exit 1 only with --strict",
    "note": "informational: the A1 outcome differs under the recorded category "
            "(C4); the matching C3 finding carries any exit consequence",
}

# Per-arm summary counters, in report order.
SUMMARY_KEYS = (
    "payloads_checked",
    "payloads_escalated",
    "payloads_malformed",
    "sub_principles_scored",
    "pack_refs_invalid",
    "a1_rule_violations",
    "a1_outcome_changed_by_computed_category",
    "total_disagreements",
    "coverage_percentage_disagreements",
    "coverage_category_disagreements",
    "coverage_undefined",
    "unavailable_but_scored",
    "failures",
    "derived_disagreements",
    "flags",
    "notes",
)


class PayloadContext(NamedTuple):
    """Where a finding came from: the arm, payload file, paper, and run."""

    arm: str
    path: Path
    slug: str
    run: int


class CoverageDerivation(NamedTuple):
    """Computed coverage values, or the reason they cannot be computed.

    Exactly one of (``percentage`` and ``category``) or
    ``undefined_reason`` is set.
    """

    percentage: float | None
    category: str | None
    undefined_reason: str | None


def load_pack_ids() -> dict[str, set[str]]:
    """Slug -> set of record ids, enumerated from the manifest."""
    manifest = yaml.safe_load((REPO_ROOT / "manifest.yaml").read_text())
    packs = manifest["evidence_packs"]["packs"]
    ids: dict[str, set[str]] = {}
    for slug, entry in packs.items():
        pack = json.loads((REPO_ROOT / entry["file"]).read_text())
        ids[slug] = {r["record_id"] for r in pack.get("records", [])}
    return ids


def display_path(path: Path) -> str:
    """Return ``path`` relative to the repository root where possible.

    Args:
        path: Any filesystem path.

    Returns:
        A POSIX-style repo-relative path, or the absolute path when the
        file lies outside the repository (for example, in a test's
        temporary directory).
    """
    resolved = path.resolve()
    try:
        return resolved.relative_to(REPO_ROOT).as_posix()
    except ValueError:
        return str(resolved)


def make_finding(ctx: PayloadContext, *, check: str, kind: str, field: str,
                 model_value: Any, computed_value: Any, governing: str | None,
                 detail: str, **extra: Any) -> dict[str, Any]:
    """Build one finding record in the report's shape.

    Args:
        ctx: The payload the finding belongs to.
        check: Check id, a key of ``CHECK_NAMES``.
        kind: One of ``KIND_DESCRIPTIONS``.
        field: Dotted payload field the finding concerns.
        model_value: The value the model recorded (None when absent).
        computed_value: The value the rule computed (None when no value is
            derived, or the derivation is undefined).
        governing: ``"computed"``, ``"model"``, or None when nothing is
            derived.
        detail: One-line human-readable explanation.
        **extra: Check-specific keys appended after the common ones.

    Returns:
        The finding as a JSON-serialisable dict.
    """
    finding: dict[str, Any] = {
        "arm": ctx.arm,
        "payload": display_path(ctx.path),
        "slug": ctx.slug,
        "run": ctx.run,
        "check": check,
        "check_name": CHECK_NAMES[check],
        "kind": kind,
        "field": field,
        "model_value": model_value,
        "computed_value": computed_value,
        "governing": governing,
        "rules_version": RULES_VERSION,
        "detail": detail,
    }
    finding.update(extra)
    return finding


def structure_problems(payload: dict[str, Any]) -> list[str]:
    """List what an ``OK`` payload lacks for the scoring checks to run.

    Only the fields the checks read are required: both scoring blocks
    with all 15 sub-principles scored 0 or 1, and a ``data_completeness``
    block. A missing ``total`` or missing coverage counts are not
    structural: C1 and C2/C3 report those themselves.

    Args:
        payload: A parsed payload whose status is ``OK``.

    Returns:
        Human-readable problems; empty when the payload is checkable.
    """
    problems: list[str] = []
    for artefact in ARTEFACTS:
        block = payload.get(artefact)
        if not isinstance(block, dict):
            problems.append(f"{artefact} block missing")
            continue
        subs = block.get("sub_principles")
        if not isinstance(subs, dict):
            problems.append(f"{artefact}.sub_principles missing")
            continue
        for sub in SUBS:
            node = subs.get(sub)
            if not isinstance(node, dict) or node.get("present") not in (0, 1):
                problems.append(f"{artefact}.sub_principles.{sub}.present missing or not 0/1")
    if not isinstance(payload.get("data_completeness"), dict):
        problems.append("data_completeness block missing")
    return problems


def _is_count(value: Any) -> bool:
    """True for a non-negative integer that is not a boolean."""
    return isinstance(value, int) and not isinstance(value, bool) and value >= 0


def coverage_category(accessible: int, enumerated: int) -> str:
    """Compute the instrument's coverage category from the exact fraction.

    Bands are read as intervals on accessible/enumerated with inclusive
    lower bounds (see the module docstring for why): complete iff every
    enumerated dataset is accessible; substantial iff the fraction is at
    least 0.75; partial iff at least 0.25; minimal otherwise. Integer
    cross-multiplication keeps the comparisons exact.

    Args:
        accessible: Datasets accessible at Tier 0-2.
        enumerated: Datasets enumerated; must be positive.

    Returns:
        ``"complete"``, ``"substantial"``, ``"partial"``, or ``"minimal"``.

    Raises:
        ValueError: If the counts do not satisfy
            ``0 <= accessible <= enumerated`` with ``enumerated > 0``.

    Examples:
        >>> coverage_category(3, 4), coverage_category(1, 4)
        ('substantial', 'partial')
        >>> coverage_category(199, 200)
        'substantial'
    """
    if not (_is_count(accessible) and _is_count(enumerated)) \
            or enumerated == 0 or accessible > enumerated:
        raise ValueError(f"coverage undefined for {accessible!r}/{enumerated!r}")
    if accessible == enumerated:
        return "complete"
    if 4 * accessible >= 3 * enumerated:  # fraction >= 0.75
        return "substantial"
    if 4 * accessible >= enumerated:  # fraction >= 0.25
        return "partial"
    return "minimal"


def derive_coverage(completeness: dict[str, Any]) -> CoverageDerivation:
    """Compute coverage percentage and category from a payload's counts.

    Args:
        completeness: The payload's ``data_completeness`` block.

    Returns:
        The computed percentage (``100 × accessible / enumerated``, one
        floating-point rounding) and category, or, when the counts cannot
        support a derivation, the reason it is undefined.
    """
    accessible = completeness.get("datasets_accessible_tier_0_2")
    enumerated = completeness.get("datasets_enumerated")
    # isinstance first so type checkers narrow to int; _is_count then
    # excludes booleans and negative values.
    if not isinstance(accessible, int) or not isinstance(enumerated, int) \
            or not (_is_count(accessible) and _is_count(enumerated)):
        return CoverageDerivation(None, None,
                                  "coverage counts missing or not non-negative integers")
    if enumerated == 0:
        return CoverageDerivation(None, None, "datasets_enumerated is 0 (0/0 is undefined)")
    if accessible > enumerated:
        return CoverageDerivation(None, None,
                                  "datasets_accessible_tier_0_2 exceeds datasets_enumerated")
    return CoverageDerivation(100 * accessible / enumerated,
                              coverage_category(accessible, enumerated), None)


def percentage_disagrees(recorded: Any, computed: float) -> bool:
    """True when a recorded percentage falls outside the C2 tolerance.

    Args:
        recorded: The model's ``coverage_percentage`` (any type; a
            non-numeric or missing value always disagrees).
        computed: The computed percentage.

    Returns:
        Whether ``|recorded - computed|`` exceeds ``COVERAGE_TOLERANCE_PP``.
    """
    if not isinstance(recorded, (int, float)) or isinstance(recorded, bool):
        return True
    return abs(recorded - computed) > COVERAGE_TOLERANCE_PP + _FLOAT_SLACK


def a1_rule_violated(category: Any, a1_present: Any, rationale: Any) -> bool:
    """Apply the instrument's A1 cross-reference to one payload.

    Args:
        category: The coverage category to judge against.
        a1_present: The data_fair A1 score.
        rationale: The payload's ``a1_exception_rationale``, if any.

    Returns:
        True when the category is minimal or partial, A1 is scored 1, and
        no exception rationale is named.
    """
    return category in A1_RESTRICTED_CATEGORIES and a1_present == 1 and not rationale


def check_section_totals(ctx: PayloadContext, payload: dict[str, Any]) -> list[dict[str, Any]]:
    """C1: compare each section's recorded total with its item sum."""
    findings: list[dict[str, Any]] = []
    for artefact in ARTEFACTS:
        block = payload[artefact]
        computed = sum(int(block["sub_principles"][sub]["present"]) for sub in SUBS)
        recorded = block.get("total")
        if recorded != computed:
            findings.append(make_finding(
                ctx, check="C1", kind="derived", field=f"{artefact}.total",
                model_value=recorded, computed_value=computed, governing="computed",
                detail=f"recorded total {recorded!r}; the 15 items sum to {computed}"))
    return findings


def check_coverage(ctx: PayloadContext, completeness: dict[str, Any]
                   ) -> tuple[list[dict[str, Any]], CoverageDerivation]:
    """C2 and C3: compare recorded coverage values with computed ones.

    Args:
        ctx: The payload being checked.
        completeness: Its ``data_completeness`` block.

    Returns:
        The findings, and the derivation (C4 needs the governing
        category).
    """
    derivation = derive_coverage(completeness)
    recorded_pct = completeness.get("coverage_percentage")
    recorded_cat = completeness.get("coverage_category")
    pct_field = "data_completeness.coverage_percentage"
    cat_field = "data_completeness.coverage_category"
    findings: list[dict[str, Any]] = []

    if derivation.undefined_reason is not None:
        # No computed value exists, so the model's values stand; flag both.
        for check, field, recorded in (("C2", pct_field, recorded_pct),
                                       ("C3", cat_field, recorded_cat)):
            findings.append(make_finding(
                ctx, check=check, kind="flag", field=field, model_value=recorded,
                computed_value=None, governing="model",
                detail=f"derivation undefined: {derivation.undefined_reason}; "
                       f"recorded value stands"))
        return findings, derivation

    assert derivation.percentage is not None and derivation.category is not None
    if percentage_disagrees(recorded_pct, derivation.percentage):
        findings.append(make_finding(
            ctx, check="C2", kind="derived", field=pct_field, model_value=recorded_pct,
            computed_value=derivation.percentage, governing="computed",
            detail=f"recorded {recorded_pct!r}; computed {derivation.percentage:.2f} "
                   f"(tolerance {COVERAGE_TOLERANCE_PP} pp)",
            tolerance_pp=COVERAGE_TOLERANCE_PP))
    if recorded_cat != derivation.category:
        findings.append(make_finding(
            ctx, check="C3", kind="derived", field=cat_field, model_value=recorded_cat,
            computed_value=derivation.category, governing="computed",
            detail=f"recorded {recorded_cat!r}; computed {derivation.category!r} from "
                   f"{completeness['datasets_accessible_tier_0_2']}/"
                   f"{completeness['datasets_enumerated']}"))
    return findings, derivation


def check_a1_rule(ctx: PayloadContext, payload: dict[str, Any],
                  derivation: CoverageDerivation) -> list[dict[str, Any]]:
    """C4: the A1 cross-reference, judged against the governing category.

    The governing category is the computed one, or the recorded one when
    the derivation is undefined. The outcome under the recorded category
    is also evaluated, so a change of outcome is visible in the report.

    Args:
        ctx: The payload being checked.
        payload: The parsed payload.
        derivation: Its coverage derivation from ``check_coverage``.

    Returns:
        A ``failure`` finding for a violation, a ``note`` when the
        computed category clears a violation the recorded one would have
        reported, or nothing.
    """
    recorded_cat = payload["data_completeness"].get("coverage_category")
    if derivation.category is not None:
        governing_cat, source = derivation.category, "computed"
    else:
        governing_cat, source = recorded_cat, "recorded"
    a1_present = payload["data_fair"]["sub_principles"]["A1"]["present"]
    rationale = payload.get("a1_exception_rationale")
    under_governing = a1_rule_violated(governing_cat, a1_present, rationale)
    under_recorded = a1_rule_violated(recorded_cat, a1_present, rationale)
    field = "data_fair.sub_principles.A1"
    common = {"category_used": governing_cat, "category_source": source,
              "recorded_category": recorded_cat,
              "outcome_under_recorded_category":
                  "violation" if under_recorded else "consistent"}

    if under_governing:
        differs = not under_recorded
        detail = (f"coverage {governing_cat} ({source}), A1=1, "
                  f"no a1_exception_rationale")
        if differs:
            detail += f"; the recorded category {recorded_cat!r} would have passed"
        return [make_finding(
            ctx, check="C4", kind="failure", field=field, model_value=a1_present,
            computed_value=None, governing=None, detail=detail,
            a1_outcome_differs=differs, **common)]
    if under_recorded:
        return [make_finding(
            ctx, check="C4", kind="note", field=field, model_value=a1_present,
            computed_value=None, governing="computed",
            detail=f"consistent under the computed category {governing_cat!r}; the "
                   f"recorded category {recorded_cat!r} would have reported a violation",
            a1_outcome_differs=True, **common)]
    return []


def check_unavailable_scored(ctx: PayloadContext,
                             payload: dict[str, Any]) -> list[dict[str, Any]]:
    """C5: flag ``available: false`` with any sub-principle scored 1."""
    findings: list[dict[str, Any]] = []
    for artefact in ARTEFACTS:
        block = payload[artefact]
        if block.get("available") is not False:
            continue
        scored = [sub for sub in SUBS if block["sub_principles"][sub]["present"] == 1]
        if scored:
            findings.append(make_finding(
                ctx, check="C5", kind="flag", field=f"{artefact}.available",
                model_value=False, computed_value=None, governing="model",
                detail=f"available is false but {len(scored)} item(s) scored 1: "
                       f"{', '.join(scored)}",
                items_scored_1=scored))
    return findings


def summarise(findings: list[dict[str, Any]], *, payloads_checked: int,
              payloads_escalated: int, payloads_malformed: int,
              sub_principles_scored: int) -> dict[str, int]:
    """Count one arm's findings by check and kind.

    Args:
        findings: The arm's findings.
        payloads_checked: Payload files found in the arm.
        payloads_escalated: Of those, ESCALATE payloads (skipped).
        payloads_malformed: Of those, payloads skipped with an S0 flag.
        sub_principles_scored: Sub-principles the C6 and utilisation pass
            visited.

    Returns:
        A dict keyed by ``SUMMARY_KEYS``.
    """
    def count(check: str, kind: str) -> int:
        return sum(1 for f in findings if f["check"] == check and f["kind"] == kind)

    summary = {
        "payloads_checked": payloads_checked,
        "payloads_escalated": payloads_escalated,
        "payloads_malformed": payloads_malformed,
        "sub_principles_scored": sub_principles_scored,
        "pack_refs_invalid": count("C6", "failure"),
        "a1_rule_violations": count("C4", "failure"),
        "a1_outcome_changed_by_computed_category": sum(
            1 for f in findings if f["check"] == "C4" and f.get("a1_outcome_differs")),
        "total_disagreements": count("C1", "derived"),
        "coverage_percentage_disagreements": count("C2", "derived"),
        "coverage_category_disagreements": count("C3", "derived"),
        # One undefined derivation raises a C2 and a C3 flag; count payloads.
        "coverage_undefined": count("C2", "flag"),
        "unavailable_but_scored": count("C5", "flag"),
    }
    for kind, key in (("failure", "failures"), ("derived", "derived_disagreements"),
                      ("flag", "flags"), ("note", "notes")):
        summary[key] = sum(1 for f in findings if f["kind"] == kind)
    return {key: summary[key] for key in SUMMARY_KEYS}


def check_arm(arm_dir: Path, pack_ids: dict[str, set[str]]) -> dict[str, Any]:
    """Run every check over one assembled arm directory.

    Payloads are only read, never written.

    Args:
        arm_dir: An arm directory holding ``run-1`` to ``run-3``.
        pack_ids: Slug -> evidence-pack record ids (``load_pack_ids``).

    Returns:
        The v1.0 keys (``arm``, ``sub_principles_scored``,
        ``pack_refs_invalid`` as (slug, run, artefact, sub, ref) tuples,
        ``a1_rule_violations`` as (slug, run) tuples, ``utilisation``),
        plus ``path``, ``findings``, ``escalated``, and ``summary``.
    """
    findings: list[dict[str, Any]] = []
    bad_refs: list[tuple[str, int, str, str, str]] = []
    a1_violations: list[tuple[str, int]] = []
    escalated: list[dict[str, Any]] = []
    checked = malformed = scored = cited = citations = 0

    for run in (1, 2, 3):
        for path in sorted((arm_dir / f"run-{run}").glob("*.json")):
            checked += 1
            payload = json.loads(path.read_text())
            slug = payload.get("paper_slug") or path.stem
            ctx = PayloadContext(arm_dir.name, path, slug, run)
            status = payload.get("status")

            # ESCALATE payloads carry no scoring blocks: count and skip.
            if status == "ESCALATE":
                escalated.append({"payload": display_path(path), "slug": slug, "run": run,
                                  "escalate_reason": payload.get("escalate_reason")})
                continue
            problems = ([f"status {status!r} is neither 'OK' nor 'ESCALATE'"]
                        if status != "OK" else structure_problems(payload))
            if problems:
                malformed += 1
                findings.append(make_finding(
                    ctx, check="S0", kind="flag", field="(payload)", model_value=status,
                    computed_value=None, governing=None,
                    detail="scoring checks skipped: " + "; ".join(problems),
                    problems=problems))
                continue

            findings.extend(check_section_totals(ctx, payload))
            coverage_findings, derivation = check_coverage(ctx, payload["data_completeness"])
            findings.extend(coverage_findings)
            a1_findings = check_a1_rule(ctx, payload, derivation)
            findings.extend(a1_findings)
            if any(f["kind"] == "failure" for f in a1_findings):
                a1_violations.append((slug, run))
            findings.extend(check_unavailable_scored(ctx, payload))

            # C6 and pack utilisation (v1.0 checks 1 and 3).
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
                            findings.append(make_finding(
                                ctx, check="C6", kind="failure",
                                field=f"{artefact}.sub_principles.{sub}.pack_refs",
                                model_value=ref, computed_value=None, governing=None,
                                detail=f"{ref!r} is not a record id in the committed "
                                       f"evidence pack for {slug}"))

    return {
        "arm": arm_dir.name,
        "path": display_path(arm_dir),
        "sub_principles_scored": scored,
        "pack_refs_invalid": bad_refs,
        "a1_rule_violations": a1_violations,
        "utilisation": {
            "sub_principles_citing_pack": cited,
            "rate": round(cited / scored, 4) if scored else None,
            "total_citations": citations,
        },
        "findings": findings,
        "escalated": escalated,
        "summary": summarise(findings, payloads_checked=checked,
                             payloads_escalated=len(escalated),
                             payloads_malformed=malformed, sub_principles_scored=scored),
    }


def combine_summaries(results: list[dict[str, Any]]) -> dict[str, int]:
    """Sum the per-arm summary counters across arms."""
    return {key: sum(r["summary"][key] for r in results) for key in SUMMARY_KEYS}


def exit_status(totals: dict[str, int], strict: bool) -> int:
    """Map summary counts to the exit status.

    Args:
        totals: Summary counters (one arm or combined).
        strict: Whether derived disagreements and flags also fail.

    Returns:
        1 on any failure, or (with ``strict``) on any derived
        disagreement or flag; otherwise 0.
    """
    if totals["failures"]:
        return 1
    if strict and (totals["derived_disagreements"] or totals["flags"]):
        return 1
    return 0


def _short(finding: dict[str, Any]) -> str:
    """Console label for a finding: slug, run, and field."""
    return f"{finding['slug']} r{finding['run']} {finding['field']}"


def print_arm(result: dict[str, Any]) -> None:
    """Print one arm's human-readable report (v1.0 lines first)."""
    util = result["utilisation"]
    summary = result["summary"]
    findings = result["findings"]
    rate = f"{util['rate']:.1%}" if util["rate"] is not None else "n/a"
    print(f"== {result['arm']} ==")
    print(f"  payloads: {summary['payloads_checked']} found, "
          f"{summary['payloads_escalated']} ESCALATE skipped, "
          f"{summary['payloads_malformed']} malformed skipped")
    print(f"  sub-principles scored: {result['sub_principles_scored']}")
    print(f"  pack-utilisation: {util['sub_principles_citing_pack']} citing "
          f"({rate}), {util['total_citations']} citations")
    if result["pack_refs_invalid"]:
        print(f"  INVALID pack_refs ({len(result['pack_refs_invalid'])}):")
        for slug, run, artefact, sub, ref in result["pack_refs_invalid"]:
            print(f"    {slug} r{run} {artefact}.{sub}: {ref!r}")
    else:
        print("  pack_refs: all resolve against committed packs")
    a1 = [f for f in findings if f["check"] == "C4"]
    violations = [f for f in a1 if f["kind"] == "failure"]
    if violations:
        print(f"  A1-RULE violations ({len(violations)}):")
        for f in violations:
            print(f"    {f['slug']} r{f['run']}: {f['detail']}")
    else:
        print("  A1 cross-reference rule (governing category): consistent")
    for f in (f for f in a1 if f["kind"] == "note"):
        print(f"    note: {f['slug']} r{f['run']}: {f['detail']}")

    sections = (
        ("C1", "derived", "section totals (C1)"),
        ("C2", "derived", f"coverage percentage (C2, tolerance {COVERAGE_TOLERANCE_PP} pp)"),
        ("C3", "derived", "coverage category (C3)"),
    )
    for check, kind, label in sections:
        hits = [f for f in findings if f["check"] == check and f["kind"] == kind]
        if not hits:
            print(f"  {label}: consistent")
            continue
        print(f"  {label}: {len(hits)} disagreement(s), computed value governs:")
        for f in hits:
            print(f"    {_short(f)}: recorded {f['model_value']!r}, "
                  f"computed {f['computed_value']!r}")
    flags = [f for f in findings if f["kind"] == "flag"]
    if flags:
        print(f"  FLAGS for review ({len(flags)}; never an override):")
        for f in flags:
            print(f"    [{f['check']}] {_short(f)}: {f['detail']}")
    else:
        print("  flags (C5, undefined coverage, structure): none")


def build_report(results: list[dict[str, Any]], totals: dict[str, int], *,
                 strict: bool, status: int) -> dict[str, Any]:
    """Assemble the machine-readable report written by ``--json``.

    Args:
        results: Per-arm results from ``check_arm``.
        totals: Combined summary counters.
        strict: Whether ``--strict`` was in force.
        status: The exit status the run returns.

    Returns:
        A JSON-serialisable dict: rules metadata, per-arm summaries, the
        combined totals, and every finding.
    """
    return {
        "tool": "scripts/check-payload-quality.py",
        "rules_version": RULES_VERSION,
        "policy": ("wiki/planning/deterministic-output-checks.md, 'Disagreement policy' "
                   "item 1 and 'Layer 1' (ruled 2026-10-04)"),
        "coverage_tolerance_pp": COVERAGE_TOLERANCE_PP,
        "strict": strict,
        "exit_status": status,
        "checks": CHECK_NAMES,
        "kinds": KIND_DESCRIPTIONS,
        "arms": [
            {"arm": r["arm"], "path": r["path"], "summary": r["summary"],
             "utilisation": r["utilisation"], "escalated": r["escalated"]}
            for r in results
        ],
        "totals": totals,
        "findings": [f for r in results for f in r["findings"]],
    }


def main(argv: list[str] | None = None) -> int:
    """Parse arguments, check each arm, print, optionally write JSON.

    Args:
        argv: Argument list (defaults to ``sys.argv[1:]``).

    Returns:
        The exit status (see the module docstring).
    """
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("arm_dirs", nargs="+", type=Path)
    parser.add_argument("--json", dest="json_path", type=Path, metavar="PATH",
                        help="write a machine-readable report of every finding to PATH")
    parser.add_argument("--strict", action="store_true",
                        help="exit 1 on any derived-field disagreement or flag as well")
    args = parser.parse_args(argv)

    missing = [d for d in args.arm_dirs if not d.is_dir()]
    if missing:
        for d in missing:
            print(f"check-payload-quality: not a directory: {d}", file=sys.stderr)
        return 2
    if args.json_path is not None:
        target = args.json_path.resolve()
        for d in args.arm_dirs:
            if target.is_relative_to(d.resolve()):
                print(f"check-payload-quality: refusing to write the report inside "
                      f"arm directory {d} (payloads are evidence)", file=sys.stderr)
                return 2

    pack_ids = load_pack_ids()
    results = [check_arm(arm_dir, pack_ids) for arm_dir in args.arm_dirs]
    for result in results:
        print_arm(result)
    totals = combine_summaries(results)
    status = exit_status(totals, args.strict)
    print(f"== rules v{RULES_VERSION}: {totals['failures']} failure(s), "
          f"{totals['derived_disagreements']} derived disagreement(s) (computed governs), "
          f"{totals['flags']} flag(s), {totals['notes']} note(s); "
          f"{'strict' if args.strict else 'default'} mode, exit {status} ==")

    if args.json_path is not None:
        report = build_report(results, totals, strict=args.strict, status=status)
        args.json_path.parent.mkdir(parents=True, exist_ok=True)
        args.json_path.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
        print(f"report written: {args.json_path}")
    return status


if __name__ == "__main__":
    raise SystemExit(main())
