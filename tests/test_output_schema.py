#!/usr/bin/env python3
"""Defect-injection tests for the benchmark FAIR output schema v1.1 (plan C3).

Every guarantee the v1.1 contract claims is demonstrated to fail before it is
trusted to pass (the monitoring plan's negative-test rule): the ESCALATE
conditional (audit C6 — escalation must not force fabricated scoring blocks),
bounds and minimum lengths (M12), the soft A1 cross-reference with its
ethical-restriction exception (faithful to the instrument's wording — a hard
zero would wrongly reject documented CARE exceptions), the schema_version
const (S3 — the validated contract self-documents), the input_provenance
flag (ratified research-surface rule; non-scoring), and pack_refs hygiene.

Run: ``venv/bin/python -m pytest tests/test_output_schema.py -q``
(requires jsonschema; stdlib unittest discovery also works once the venv
exists — the pre-commit gate's fallback runner will skip nothing because
jsonschema is in requirements.txt).
"""

from __future__ import annotations

import copy
import json
import unittest
from pathlib import Path

from jsonschema import Draft7Validator

REPO_ROOT = Path(__file__).resolve().parent.parent
SCHEMA_PATH = REPO_ROOT / "assessment-system" / "schema" / "benchmark-fair-output-schema.json"

SCHEMA = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
VALIDATOR = Draft7Validator(SCHEMA)

SUB_KEYS = ["F1", "F2", "F3", "F4", "A1", "A1_1", "A1_2", "A2",
            "I1", "I2", "I3", "R1", "R1_1", "R1_2", "R1_3"]


def fair_block(present: int = 1) -> dict:
    """A well-formed fair_score block with uniform sub-principle values."""
    return {
        "available": True,
        "total": present * 15 if present else 0,
        "sub_principles": {k: {"present": present, "evidence": f"fixture evidence for {k}"}
                           for k in SUB_KEYS},
    }


def ok_payload() -> dict:
    """A fully valid status-OK v1.1 payload."""
    return {
        "status": "OK",
        "schema_version": "1.1",
        "paper_slug": "fixture-paper",
        "receipts": {
            "instrument_versions": {"fair-instrument": "2.0"},
            "instrument_receipts": {"fair-instrument": "feedfacecafebeef"},
            "agent_version": "fair-assessor-sonnet-5 v1.0",
            "model_id": "claude-sonnet-5",
            "pulled_files_read": [],
        },
        "stated_availability": "Data on Zenodo; code on GitHub.",
        "input_provenance": [
            {"input": "pXRF dataset", "provenance": "author-deposited"},
        ],
        "data_fair": fair_block(1),
        "code_fair": fair_block(0),
        "data_completeness": {
            "datasets_enumerated": 1,
            "datasets_accessible_tier_0_2": 1,
            "coverage_percentage": 100,
            "coverage_category": "complete",
            "assessment_scope": "straightforward",
        },
    }


class OutputSchemaTests(unittest.TestCase):
    """One green baseline per status, then one injected defect per test."""

    def assert_valid(self, payload: dict) -> None:
        errors = list(VALIDATOR.iter_errors(payload))
        self.assertEqual(errors, [], [e.message for e in errors])

    def assert_invalid(self, payload: dict) -> None:
        self.assertTrue(list(VALIDATOR.iter_errors(payload)),
                        "expected the injected defect to fail validation")

    def test_schema_file_version_is_1_1(self) -> None:
        self.assertEqual(SCHEMA["version"], "1.1")

    def test_ok_baseline_validates(self) -> None:
        self.assert_valid(ok_payload())

    def test_escalate_minimal_payload_validates(self) -> None:
        """Audit C6: escalation no longer forces fabricated scoring blocks."""
        self.assert_valid({
            "status": "ESCALATE",
            "schema_version": "1.1",
            "paper_slug": "fixture-paper",
            "escalate_reason": "instrument absent from context",
            "receipts": ok_payload()["receipts"],
        })

    def test_escalate_without_reason_fails(self) -> None:
        payload = {
            "status": "ESCALATE",
            "schema_version": "1.1",
            "paper_slug": "fixture-paper",
            "receipts": ok_payload()["receipts"],
        }
        self.assert_invalid(payload)

    def test_ok_without_scoring_blocks_fails(self) -> None:
        payload = ok_payload()
        del payload["data_fair"]
        self.assert_invalid(payload)

    def test_ok_without_provenance_fails(self) -> None:
        """The ratified provenance flag is part of every OK scoring record."""
        payload = ok_payload()
        del payload["input_provenance"]
        self.assert_invalid(payload)

    def test_bad_provenance_enum_fails(self) -> None:
        payload = ok_payload()
        payload["input_provenance"][0]["provenance"] = "authors-fault"
        self.assert_invalid(payload)

    def test_empty_evidence_fails(self) -> None:
        """M12: an empty evidence string is a schema failure, not a shrug."""
        payload = ok_payload()
        payload["data_fair"]["sub_principles"]["F1"]["evidence"] = ""
        self.assert_invalid(payload)

    def test_coverage_percentage_bounds(self) -> None:
        payload = ok_payload()
        payload["data_completeness"]["coverage_percentage"] = 150
        self.assert_invalid(payload)

    def test_present_out_of_enum_fails(self) -> None:
        payload = ok_payload()
        payload["code_fair"]["sub_principles"]["I1"]["present"] = 2
        self.assert_invalid(payload)

    def test_wrong_schema_version_fails(self) -> None:
        """S3: the const pins the contract — a v1.0 claim cannot validate."""
        payload = ok_payload()
        payload["schema_version"] = "1.0"
        self.assert_invalid(payload)

    def test_missing_schema_version_fails(self) -> None:
        payload = ok_payload()
        del payload["schema_version"]
        self.assert_invalid(payload)

    def a1_exception_payload(self, coverage: str, a1_present: int,
                             rationale: str | None) -> dict:
        payload = ok_payload()
        payload["data_completeness"]["coverage_category"] = coverage
        payload["data_completeness"]["coverage_percentage"] = 30
        payload["data_completeness"]["datasets_accessible_tier_0_2"] = 0
        payload["data_fair"]["sub_principles"]["A1"]["present"] = a1_present
        payload["data_fair"]["total"] = 14 + a1_present
        if rationale is not None:
            payload["a1_exception_rationale"] = rationale
        return payload

    def test_minimal_coverage_with_a1_needs_rationale(self) -> None:
        """M12 A1 cross-reference: minimal/partial coverage with A1 = 1 must
        name the instrument's ethical-restriction exception."""
        self.assert_invalid(self.a1_exception_payload("minimal", 1, None))
        self.assert_invalid(self.a1_exception_payload("partial", 1, None))

    def test_a1_exception_with_rationale_validates(self) -> None:
        """The exception is honoured, not hard-zeroed: CARE-restricted data
        can legitimately score A1 = 1 when the restriction is named."""
        self.assert_valid(self.a1_exception_payload(
            "minimal", 1, "Human-subjects data under documented CARE restriction"))

    def test_minimal_coverage_with_a1_zero_needs_no_rationale(self) -> None:
        self.assert_valid(self.a1_exception_payload("minimal", 0, None))

    def test_complete_coverage_needs_no_rationale(self) -> None:
        self.assert_valid(ok_payload())

    def test_empty_pulled_path_fails(self) -> None:
        """Mirror of hook L-3: an empty declared pull is malformed here too."""
        payload = ok_payload()
        payload["receipts"]["pulled_files_read"] = [""]
        self.assert_invalid(payload)

    def test_empty_pack_ref_fails(self) -> None:
        payload = ok_payload()
        payload["data_fair"]["sub_principles"]["F1"]["pack_refs"] = [""]
        self.assert_invalid(payload)

    def test_pack_refs_validate(self) -> None:
        payload = ok_payload()
        payload["data_fair"]["sub_principles"]["F1"]["pack_refs"] = [
            "datacite:10.5281/zenodo.0000000"]
        self.assert_valid(payload)

    def test_v1_0_era_payload_fails_v1_1(self) -> None:
        """Documented breaking change: v1.0-era outputs (no schema_version,
        no input_provenance) do not validate against v1.1 — v1.1 is for the
        D3 re-benchmark onward, never applied retroactively."""
        payload = ok_payload()
        del payload["schema_version"]
        del payload["input_provenance"]
        self.assert_invalid(payload)


if __name__ == "__main__":
    unittest.main(verbosity=2)
