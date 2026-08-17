#!/usr/bin/env python3
"""Unit tests for the mechanical payload-quality checker (v1.0).

Synthetic arm directories only — each case builds minimal payloads and
asserts the three checks (pack_refs validity, A1-rule consistency,
utilisation counting) behave as documented.

Run: ``venv/bin/python -m pytest tests/test_payload_quality.py -q``
"""

from __future__ import annotations

import importlib.machinery
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

_spec = importlib.util.spec_from_loader(
    "check_payload_quality",
    importlib.machinery.SourceFileLoader(
        "check_payload_quality",
        str(REPO_ROOT / "scripts" / "check-payload-quality.py")))
checker = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(checker)

PACK_IDS = {"test-paper": {"crossref:10.1/x", "datacite:10.2/y"}}


def payload(slug: str = "test-paper", coverage: str = "complete",
            a1: int = 0, refs_on_f1: list | None = None,
            rationale: str | None = None) -> dict:
    subs = {}
    for sub in checker.SUBS:
        node = {"present": 0, "evidence": "looked, not found"}
        if sub == "F1" and refs_on_f1:
            node["pack_refs"] = refs_on_f1
            node["present"] = 1
        if sub == "A1":
            node["present"] = a1
        subs[sub] = dict(node)
    body = {
        "paper_slug": slug,
        "data_completeness": {"coverage_category": coverage},
        "data_fair": {"sub_principles": {k: dict(v) for k, v in subs.items()}},
        "code_fair": {"sub_principles": {k: dict(v) for k, v in subs.items()}},
    }
    if rationale:
        body["a1_exception_rationale"] = rationale
    return body


def write_arm(tmp: Path, payloads: list[dict]) -> Path:
    arm = tmp / "arm-test"
    for run in (1, 2, 3):
        (arm / f"run-{run}").mkdir(parents=True)
    for p in payloads:
        (arm / "run-1" / f"{p['paper_slug']}.json").write_text(json.dumps(p))
    return arm


class CheckArmTests(unittest.TestCase):

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


if __name__ == "__main__":
    unittest.main()
