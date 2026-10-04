#!/usr/bin/env python3
"""Unit tests for the mechanical payload-quality checker (v1.1).

Synthetic arm directories only — each case builds minimal payloads and
asserts the checks behave as documented: the three v1.0 checks (pack_refs
validity, A1-rule consistency, utilisation counting) and the v1.1 Layer 1
checks (section totals, coverage arithmetic and category computed from the
counts, the A1 rule judged against the governing category, the
unavailable-but-scored flag, ESCALATE skipping, ``--strict``, and the JSON
report).

Run: ``venv/bin/python -m pytest tests/test_payload_quality.py -q``
"""

from __future__ import annotations

import contextlib
import hashlib
import importlib.machinery
import importlib.util
import io
import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

REPO_ROOT = Path(__file__).resolve().parent.parent

_spec = importlib.util.spec_from_loader(
    "check_payload_quality",
    importlib.machinery.SourceFileLoader(
        "check_payload_quality",
        str(REPO_ROOT / "scripts" / "check-payload-quality.py")))
checker = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(checker)

PACK_IDS = {"test-paper": {"crossref:10.1/x", "datacite:10.2/y"}}

# Coverage counts (accessible, enumerated) consistent with each category,
# so a fixture is internally consistent unless a test says otherwise.
CATEGORY_COUNTS = {"complete": (2, 2), "substantial": (3, 4),
                   "partial": (1, 2), "minimal": (0, 2)}

# Keys every finding in the JSON report must carry (brief item 7).
FINDING_KEYS = {"payload", "slug", "run", "field", "model_value", "computed_value",
                "governing", "check", "rules_version"}


def payload(slug: str = "test-paper", coverage: str = "complete",
            a1: int = 0, refs_on_f1: list | None = None,
            rationale: str | None = None, counts: tuple[int, int] | None = None,
            percentage: float | None = None) -> dict:
    """Build a schema-shaped ``OK`` payload, consistent by default.

    Args:
        slug: Paper slug.
        coverage: Recorded coverage category.
        a1: Data and code A1 score.
        refs_on_f1: pack_refs to cite on F1 (which is then scored 1).
        rationale: ``a1_exception_rationale``, if any.
        counts: (accessible, enumerated); defaults to counts matching
            ``coverage``.
        percentage: Recorded coverage percentage; defaults to the
            computed one (0 when nothing is enumerated).

    Returns:
        The payload dict; totals equal the item sums.
    """
    subs = {}
    for sub in checker.SUBS:
        node = {"present": 0, "evidence": "looked, not found"}
        if sub == "F1" and refs_on_f1:
            node["pack_refs"] = refs_on_f1
            node["present"] = 1
        if sub == "A1":
            node["present"] = a1
        subs[sub] = dict(node)
    accessible, enumerated = counts if counts is not None else CATEGORY_COUNTS[coverage]
    if percentage is None:
        percentage = 100 * accessible / enumerated if enumerated else 0
    item_sum = sum(node["present"] for node in subs.values())
    body = {
        "status": "OK",
        "paper_slug": slug,
        "data_completeness": {
            "datasets_enumerated": enumerated,
            "datasets_accessible_tier_0_2": accessible,
            "coverage_percentage": percentage,
            "coverage_category": coverage,
            "assessment_scope": "straightforward",
        },
        "data_fair": {"available": True, "total": item_sum,
                      "sub_principles": {k: dict(v) for k, v in subs.items()}},
        "code_fair": {"available": True, "total": item_sum,
                      "sub_principles": {k: dict(v) for k, v in subs.items()}},
    }
    if rationale:
        body["a1_exception_rationale"] = rationale
    return body


def escalate_payload(slug: str = "escalated-paper") -> dict:
    """An ESCALATE payload: no scoring blocks (output schema v1.1)."""
    return {"status": "ESCALATE", "schema_version": "1.1", "paper_slug": slug,
            "escalate_reason": "paper text unreadable", "receipts": {}}


def write_arm(tmp: Path, payloads: list[dict]) -> Path:
    """Write payloads into a synthetic arm's run-1 (runs 2-3 empty)."""
    arm = tmp / "arm-test"
    for run in (1, 2, 3):
        (arm / f"run-{run}").mkdir(parents=True)
    for p in payloads:
        (arm / "run-1" / f"{p['paper_slug']}.json").write_text(json.dumps(p))
    return arm


def by_check(result: dict, check: str) -> list[dict]:
    """The findings of one check id."""
    return [f for f in result["findings"] if f["check"] == check]


def tree_digest(root: Path) -> dict[str, str]:
    """sha256 of every file under ``root``, keyed by relative path."""
    return {p.relative_to(root).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(root.rglob("*")) if p.is_file()}


class CheckArmTests(unittest.TestCase):
    """The v1.0 checks, unchanged in behaviour."""

    def test_valid_refs_pass_and_are_counted(self):
        with tempfile.TemporaryDirectory() as tmp:
            arm = write_arm(Path(tmp), [payload(refs_on_f1=["crossref:10.1/x"])])
            result = checker.check_arm(arm, PACK_IDS)
        self.assertEqual(result["pack_refs_invalid"], [])
        self.assertEqual(result["utilisation"]["total_citations"], 2)  # both artefacts
        self.assertEqual(result["utilisation"]["sub_principles_citing_pack"], 2)

    def test_fabricated_ref_detected(self):
        with tempfile.TemporaryDirectory() as tmp:
            arm = write_arm(Path(tmp), [payload(refs_on_f1=["zenodo:MADE-UP"])])
            result = checker.check_arm(arm, PACK_IDS)
        self.assertEqual(len(result["pack_refs_invalid"]), 2)
        self.assertEqual(result["pack_refs_invalid"][0][4], "zenodo:MADE-UP")

    def test_a1_rule_violation_detected(self):
        with tempfile.TemporaryDirectory() as tmp:
            arm = write_arm(Path(tmp), [payload(coverage="partial", a1=1)])
            result = checker.check_arm(arm, PACK_IDS)
        self.assertEqual(result["a1_rule_violations"], [("test-paper", 1)])

    def test_a1_exception_rationale_clears_violation(self):
        with tempfile.TemporaryDirectory() as tmp:
            arm = write_arm(Path(tmp), [payload(coverage="partial", a1=1,
                                                rationale="CARE restriction, s7.1")])
            result = checker.check_arm(arm, PACK_IDS)
        self.assertEqual(result["a1_rule_violations"], [])

    def test_complete_coverage_with_a1_is_fine(self):
        with tempfile.TemporaryDirectory() as tmp:
            arm = write_arm(Path(tmp), [payload(coverage="complete", a1=1)])
            result = checker.check_arm(arm, PACK_IDS)
        self.assertEqual(result["a1_rule_violations"], [])


class CoverageDerivationTests(unittest.TestCase):
    """Pure derivation rules: band boundaries, tolerance, undefined cases."""

    def test_exactly_three_quarters_is_substantial(self):
        self.assertEqual(checker.coverage_category(3, 4), "substantial")
        self.assertEqual(checker.coverage_category(75, 100), "substantial")

    def test_just_below_three_quarters_is_partial(self):
        self.assertEqual(checker.coverage_category(74, 100), "partial")
        self.assertEqual(checker.coverage_category(2999, 4000), "partial")  # 0.74975

    def test_exactly_one_quarter_is_partial(self):
        self.assertEqual(checker.coverage_category(1, 4), "partial")
        self.assertEqual(checker.coverage_category(25, 100), "partial")

    def test_just_below_one_quarter_is_minimal(self):
        self.assertEqual(checker.coverage_category(24, 100), "minimal")
        self.assertEqual(checker.coverage_category(999, 4000), "minimal")  # 0.24975

    def test_complete_only_when_every_dataset_accessible(self):
        self.assertEqual(checker.coverage_category(5, 5), "complete")
        # 99.5% would round to 100; the fraction rule keeps it substantial.
        self.assertEqual(checker.coverage_category(199, 200), "substantial")

    def test_nothing_accessible_is_minimal(self):
        self.assertEqual(checker.coverage_category(0, 5), "minimal")

    def test_category_rejects_undefined_counts(self):
        for accessible, enumerated in ((0, 0), (3, 2), (-1, 2), (True, 2)):
            with self.subTest(counts=(accessible, enumerated)), \
                    self.assertRaises(ValueError):
                checker.coverage_category(accessible, enumerated)

    def test_tolerance_edge_is_inclusive(self):
        # 1/8 = 12.5%: either whole-number rounding of the half agrees.
        self.assertFalse(checker.percentage_disagrees(13, 12.5))
        self.assertFalse(checker.percentage_disagrees(12, 12.5))
        self.assertTrue(checker.percentage_disagrees(13.01, 12.5))
        self.assertTrue(checker.percentage_disagrees(11.99, 12.5))

    def test_whole_number_rounding_agrees(self):
        # The committed arms record 4/12 as 33.
        self.assertFalse(checker.percentage_disagrees(33, 100 * 4 / 12))

    def test_non_numeric_percentage_disagrees(self):
        for recorded in (None, "50", True):
            with self.subTest(recorded=recorded):
                self.assertTrue(checker.percentage_disagrees(recorded, 50.0))

    def test_enumerated_zero_is_undefined(self):
        derivation = checker.derive_coverage(
            {"datasets_enumerated": 0, "datasets_accessible_tier_0_2": 0})
        self.assertIsNone(derivation.percentage)
        self.assertIsNone(derivation.category)
        self.assertIn("0/0", derivation.undefined_reason)

    def test_more_accessible_than_enumerated_is_undefined(self):
        derivation = checker.derive_coverage(
            {"datasets_enumerated": 2, "datasets_accessible_tier_0_2": 3})
        self.assertIsNone(derivation.category)
        self.assertIn("exceeds", derivation.undefined_reason)

    def test_missing_counts_are_undefined(self):
        derivation = checker.derive_coverage({"coverage_category": "complete"})
        self.assertIsNone(derivation.category)
        self.assertIsNotNone(derivation.undefined_reason)


class Layer1ArmTests(unittest.TestCase):
    """v1.1 checks over synthetic arms."""

    def test_consistent_payload_has_no_findings(self):
        with tempfile.TemporaryDirectory() as tmp:
            arm = write_arm(Path(tmp), [payload(coverage="substantial",
                                                refs_on_f1=["crossref:10.1/x"])])
            result = checker.check_arm(arm, PACK_IDS)
        self.assertEqual(result["findings"], [])
        self.assertEqual(result["summary"]["payloads_checked"], 1)

    def test_total_disagreement_computed_governs(self):
        p = payload(a1=1)  # each section's items sum to 1
        p["code_fair"]["total"] = 0
        with tempfile.TemporaryDirectory() as tmp:
            arm = write_arm(Path(tmp), [p])
            result = checker.check_arm(arm, PACK_IDS)
        [finding] = by_check(result, "C1")
        self.assertEqual(finding["field"], "code_fair.total")
        self.assertEqual((finding["model_value"], finding["computed_value"]), (0, 1))
        self.assertEqual((finding["kind"], finding["governing"]), ("derived", "computed"))
        self.assertEqual(finding["rules_version"], "1.1")
        self.assertEqual(result["summary"]["total_disagreements"], 1)

    def test_coverage_percentage_disagreement(self):
        p = payload(coverage="partial", counts=(1, 2), percentage=100)
        with tempfile.TemporaryDirectory() as tmp:
            arm = write_arm(Path(tmp), [p])
            result = checker.check_arm(arm, PACK_IDS)
        [finding] = by_check(result, "C2")
        self.assertEqual((finding["model_value"], finding["computed_value"]), (100, 50.0))
        self.assertEqual((finding["kind"], finding["governing"]), ("derived", "computed"))
        self.assertEqual(by_check(result, "C3"), [])  # the category was right

    def test_rounded_percentage_within_tolerance(self):
        p = payload(coverage="partial", counts=(4, 12), percentage=33)
        with tempfile.TemporaryDirectory() as tmp:
            arm = write_arm(Path(tmp), [p])
            result = checker.check_arm(arm, PACK_IDS)
        self.assertEqual(result["findings"], [])

    def test_category_disagreement_computed_governs(self):
        p = payload(coverage="substantial", counts=(1, 2))
        with tempfile.TemporaryDirectory() as tmp:
            arm = write_arm(Path(tmp), [p])
            result = checker.check_arm(arm, PACK_IDS)
        [finding] = by_check(result, "C3")
        self.assertEqual((finding["model_value"], finding["computed_value"]),
                         ("substantial", "partial"))
        self.assertEqual(finding["governing"], "computed")
        self.assertEqual(result["summary"]["coverage_category_disagreements"], 1)

    def test_band_boundaries_through_check_arm(self):
        cases = [("complete", (4, 4)), ("substantial", (3, 4)), ("partial", (74, 100)),
                 ("partial", (1, 4)), ("minimal", (24, 100))]
        for category, counts in cases:
            with self.subTest(counts=counts), tempfile.TemporaryDirectory() as tmp:
                arm = write_arm(Path(tmp), [payload(coverage=category, counts=counts)])
                result = checker.check_arm(arm, PACK_IDS)
                self.assertEqual(result["findings"], [])

    def test_enumerated_zero_flags_without_crashing(self):
        p = payload(coverage="minimal", counts=(0, 0), percentage=0)
        with tempfile.TemporaryDirectory() as tmp:
            arm = write_arm(Path(tmp), [p])
            result = checker.check_arm(arm, PACK_IDS)
        flags = [f for f in result["findings"] if f["kind"] == "flag"]
        self.assertEqual(sorted(f["check"] for f in flags), ["C2", "C3"])
        for f in flags:
            self.assertIsNone(f["computed_value"])
            self.assertEqual(f["governing"], "model")
        self.assertEqual(result["summary"]["coverage_undefined"], 1)
        self.assertEqual(result["summary"]["derived_disagreements"], 0)

    def test_undefined_derivation_a1_uses_recorded_category(self):
        p = payload(coverage="partial", counts=(0, 0), percentage=0, a1=1)
        with tempfile.TemporaryDirectory() as tmp:
            arm = write_arm(Path(tmp), [p])
            result = checker.check_arm(arm, PACK_IDS)
        [finding] = by_check(result, "C4")
        self.assertEqual(finding["kind"], "failure")
        self.assertEqual(finding["category_source"], "recorded")
        self.assertFalse(finding["a1_outcome_differs"])

    def test_a1_violation_from_computed_category(self):
        # Recorded "complete" would pass; the counts say partial.
        p = payload(coverage="complete", counts=(1, 2), percentage=100, a1=1)
        with tempfile.TemporaryDirectory() as tmp:
            arm = write_arm(Path(tmp), [p])
            result = checker.check_arm(arm, PACK_IDS)
        self.assertEqual(result["a1_rule_violations"], [("test-paper", 1)])
        [finding] = by_check(result, "C4")
        self.assertEqual(finding["kind"], "failure")
        self.assertEqual(finding["category_used"], "partial")
        self.assertEqual(finding["category_source"], "computed")
        self.assertEqual(finding["outcome_under_recorded_category"], "consistent")
        self.assertTrue(finding["a1_outcome_differs"])
        self.assertIn("would have passed", finding["detail"])
        self.assertEqual(result["summary"]["a1_outcome_changed_by_computed_category"], 1)

    def test_computed_category_clears_recorded_a1_violation(self):
        # Recorded "partial" would fail; the counts say complete.
        p = payload(coverage="partial", counts=(2, 2), a1=1)
        with tempfile.TemporaryDirectory() as tmp:
            arm = write_arm(Path(tmp), [p])
            result = checker.check_arm(arm, PACK_IDS)
        self.assertEqual(result["a1_rule_violations"], [])
        [note] = by_check(result, "C4")
        self.assertEqual(note["kind"], "note")
        self.assertEqual(note["outcome_under_recorded_category"], "violation")
        self.assertEqual(len(by_check(result, "C3")), 1)
        self.assertEqual(result["summary"]["failures"], 0)
        self.assertEqual(result["summary"]["notes"], 1)

    def test_unavailable_but_scored_is_flagged_not_failed(self):
        p = payload(refs_on_f1=["crossref:10.1/x"])
        p["data_fair"]["available"] = False
        with tempfile.TemporaryDirectory() as tmp:
            arm = write_arm(Path(tmp), [p])
            result = checker.check_arm(arm, PACK_IDS)
        [finding] = by_check(result, "C5")
        self.assertEqual(finding["field"], "data_fair.available")
        self.assertEqual(finding["items_scored_1"], ["F1"])
        self.assertEqual((finding["kind"], finding["governing"]), ("flag", "model"))
        self.assertEqual(result["summary"]["failures"], 0)

    def test_unavailable_with_nothing_scored_is_fine(self):
        p = payload()
        p["code_fair"]["available"] = False
        with tempfile.TemporaryDirectory() as tmp:
            arm = write_arm(Path(tmp), [p])
            result = checker.check_arm(arm, PACK_IDS)
        self.assertEqual(result["findings"], [])

    def test_escalate_payload_skipped_and_counted(self):
        with tempfile.TemporaryDirectory() as tmp:
            arm = write_arm(Path(tmp), [payload(), escalate_payload()])
            result = checker.check_arm(arm, PACK_IDS)
        self.assertEqual(result["findings"], [])
        self.assertEqual(result["summary"]["payloads_checked"], 2)
        self.assertEqual(result["summary"]["payloads_escalated"], 1)
        self.assertEqual(result["sub_principles_scored"], 30)  # the OK payload only
        self.assertEqual(result["escalated"][0]["escalate_reason"], "paper text unreadable")

    def test_unknown_status_or_missing_block_is_structure_flag(self):
        no_status = payload(slug="no-status")
        del no_status["status"]
        no_block = payload(slug="no-block")
        del no_block["code_fair"]
        with tempfile.TemporaryDirectory() as tmp:
            arm = write_arm(Path(tmp), [no_status, no_block])
            result = checker.check_arm(arm, PACK_IDS)
        flags = by_check(result, "S0")
        self.assertEqual(sorted(f["slug"] for f in flags), ["no-block", "no-status"])
        self.assertTrue(all(f["kind"] == "flag" for f in flags))
        self.assertEqual(result["summary"]["payloads_malformed"], 2)


class MainTests(unittest.TestCase):
    """Exit codes, the JSON report, and payload immutability."""

    def run_main(self, *argv: str | Path) -> int:
        """Call ``main`` with the synthetic packs and stdout captured."""
        with mock.patch.object(checker, "load_pack_ids", return_value=PACK_IDS), \
                contextlib.redirect_stdout(io.StringIO()), \
                contextlib.redirect_stderr(io.StringIO()):
            return checker.main([str(a) for a in argv])

    @staticmethod
    def derived_and_flagged() -> list[dict]:
        """One total disagreement and one C5 flag; no failures."""
        p = payload(slug="other-paper", a1=1)
        p["code_fair"]["total"] = 5
        q = payload(refs_on_f1=["crossref:10.1/x"])  # a valid ref in test-paper's pack
        q["data_fair"]["available"] = False
        return [p, q]

    def test_clean_arm_exits_zero_in_both_modes(self):
        with tempfile.TemporaryDirectory() as tmp:
            arm = write_arm(Path(tmp), [payload()])
            self.assertEqual(self.run_main(arm), 0)
            self.assertEqual(self.run_main("--strict", arm), 0)

    def test_derived_and_flags_fail_only_with_strict(self):
        with tempfile.TemporaryDirectory() as tmp:
            arm = write_arm(Path(tmp), self.derived_and_flagged())
            self.assertEqual(self.run_main(arm), 0)
            self.assertEqual(self.run_main("--strict", arm), 1)

    def test_flag_alone_fails_with_strict(self):
        with tempfile.TemporaryDirectory() as tmp:
            arm = write_arm(Path(tmp), [payload(counts=(0, 0), coverage="minimal")])
            self.assertEqual(self.run_main(arm), 0)
            self.assertEqual(self.run_main("--strict", arm), 1)

    def test_failure_exits_one_in_both_modes(self):
        with tempfile.TemporaryDirectory() as tmp:
            arm = write_arm(Path(tmp), [payload(refs_on_f1=["zenodo:MADE-UP"])])
            self.assertEqual(self.run_main(arm), 1)
            self.assertEqual(self.run_main("--strict", arm), 1)

    def test_missing_arm_directory_is_usage_error(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(self.run_main(Path(tmp) / "no-such-arm"), 2)

    def test_report_inside_arm_directory_refused(self):
        with tempfile.TemporaryDirectory() as tmp:
            arm = write_arm(Path(tmp), [payload()])
            target = arm / "run-1" / "test-paper.json"
            before = target.read_bytes()
            self.assertEqual(self.run_main("--json", target, arm), 2)
            self.assertEqual(target.read_bytes(), before)

    def test_json_report_shape(self):
        p = payload(slug="third-paper", refs_on_f1=["zenodo:MADE-UP"])  # two C6 failures
        with tempfile.TemporaryDirectory() as tmp:
            arm = write_arm(Path(tmp), self.derived_and_flagged() + [p])
            out = Path(tmp) / "reports" / "report.json"
            status = self.run_main("--json", out, arm)
            report = json.loads(out.read_text())
        self.assertEqual(status, 1)
        self.assertEqual(report["exit_status"], 1)
        self.assertEqual(report["rules_version"], "1.1")
        self.assertEqual(report["coverage_tolerance_pp"], 0.5)
        self.assertFalse(report["strict"])
        self.assertEqual(set(report["checks"]), {"S0", "C1", "C2", "C3", "C4", "C5", "C6"})
        [arm_entry] = report["arms"]
        self.assertEqual(set(arm_entry["summary"]), set(checker.SUMMARY_KEYS))
        self.assertEqual(report["totals"], arm_entry["summary"])
        self.assertEqual(report["totals"]["total_disagreements"], 1)
        self.assertEqual(report["totals"]["unavailable_but_scored"], 1)
        self.assertEqual(report["totals"]["pack_refs_invalid"], 2)
        self.assertEqual(len(report["findings"]), 4)
        for finding in report["findings"]:
            self.assertLessEqual(FINDING_KEYS, set(finding))
            self.assertEqual(finding["rules_version"], "1.1")
            self.assertEqual(finding["run"], 1)
            if finding["kind"] == "derived":
                self.assertEqual(finding["governing"], "computed")

    def test_payloads_never_modified(self):
        with tempfile.TemporaryDirectory() as tmp:
            arm = write_arm(Path(tmp), self.derived_and_flagged() + [escalate_payload()])
            before = tree_digest(arm)
            self.run_main("--strict", "--json", Path(tmp) / "report.json", arm)
            self.assertEqual(tree_digest(arm), before)


if __name__ == "__main__":
    unittest.main()
