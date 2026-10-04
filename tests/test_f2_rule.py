#!/usr/bin/env python3
"""Unit tests for the mechanical F2 rule (AP-15), ``scripts/score-f2-rule.py``.

The five pilots exercise only the rule's 0 paths (every pilot F2 reference
score is 0), so these synthetic fixtures carry the rest of the burden: each
mechanical-0 path, the confirm-1 path the pilots never reach, every
no-structured-input path, and the conjunctive aggregation between them.

Run: ``venv/bin/python -m pytest tests/test_f2_rule.py -q``
"""

from __future__ import annotations

import importlib.machinery
import importlib.util
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPT = REPO_ROOT / "scripts" / "score-f2-rule.py"

_spec = importlib.util.spec_from_loader(
    "score_f2_rule", importlib.machinery.SourceFileLoader("score_f2_rule", str(SCRIPT)))
rule = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(rule)

FULL = {"creators": ["A. Author"], "titles": ["A dataset"],
        "descriptions": [{"type": "Abstract", "text": "<p>Bead counts by grave.</p>"}],
        "subjects": ["archaeology"]}


def pack_with(doi: str, **overrides: object) -> dict:
    """A one-record harvester v1.2 pack whose DataCite fields default to FULL."""
    fields = dict(FULL)
    fields.update(overrides)
    return {"harvester_version": "1.2", "records": [
        {"record_id": f"datacite:{doi}", "status": "resolved",
         "response_sha256": "0" * 64, "fields": fields}]}


def deposit(doi: str = "10.5281/zenodo.1", **extra: object) -> dict:
    """A curated principal repository entry carrying data and code."""
    entry = {"id": "dep", "type": "data+code", "link": doi,
             "role": "principal", "home": "repository"}
    entry.update(extra)
    return entry


class MechanicalZeroTests(unittest.TestCase):
    """Each AP-15 absence and each no-record home gives a mechanical 0."""

    def test_each_missing_field_is_a_zero(self) -> None:
        for field, empty in (("creators", []), ("titles", []),
                             ("descriptions", []), ("subjects", [])):
            with self.subTest(field=field):
                result = rule.score_item("p", {"links": [deposit()]},
                                         pack_with("10.5281/zenodo.1", **{field: empty}),
                                         "data")
                self.assertEqual((result["status"], result["rule_value"]),
                                 (rule.MECHANICAL_0, 0))

    def test_html_shell_description_counts_as_empty(self) -> None:
        pack = pack_with("10.5281/zenodo.1",
                         descriptions=[{"type": "Abstract", "text": "<p>&nbsp;</p>"}])
        result = rule.score_item("p", {"links": [deposit()]}, pack, "data")
        self.assertEqual(result["status"], rule.MECHANICAL_0)
        self.assertIn("no description", result["reasons"][0])

    def test_supplement_home_is_row_6_zero(self) -> None:
        spec = {"links": [{"id": "supp", "type": "supplement", "role": "principal",
                           "home": "supplement", "carries": ["code"], "link": "10.1016/x"}]}
        result = rule.score_item("p", spec, None, "code")
        self.assertEqual(result["status"], rule.MECHANICAL_0)
        self.assertIn("Row 6", result["reasons"][0])

    def test_unmanaged_home_is_zero(self) -> None:
        spec = {"links": [{"id": "srv", "type": "data", "role": "principal",
                           "home": "unmanaged", "link": "https://example.org/a.csv"}]}
        self.assertEqual(rule.score_item("p", spec, None, "data")["rule_value"], 0)

    def test_unpublished_principal_is_zero(self) -> None:
        spec = {"unpublished_principal": ["data"], "links": []}
        result = rule.score_item("p", spec, None, "data")
        self.assertEqual(result["status"], rule.MECHANICAL_0)
        self.assertIn("AP-13", result["reasons"][0])

    def test_scored_version_record_is_the_one_tested(self) -> None:
        """A rich concept record cannot rescue a bare scored version."""
        pack = pack_with("10.5281/zenodo.2", subjects=[])
        pack["records"].append({"record_id": "datacite:10.5281/zenodo.1",
                                "status": "resolved", "fields": dict(FULL)})
        spec = {"links": [deposit("10.5281/zenodo.1", scored_version="10.5281/zenodo.2")]}
        result = rule.score_item("p", spec, pack, "data")
        self.assertEqual(result["status"], rule.MECHANICAL_0)
        self.assertEqual(result["inputs_read"][0]["record_id"], "datacite:10.5281/zenodo.2")


class ConfirmOneTests(unittest.TestCase):
    """The rule never awards a 1: a complete record goes to confirmation."""

    def test_complete_record_needs_confirmation(self) -> None:
        result = rule.score_item("p", {"links": [deposit()]},
                                 pack_with("10.5281/zenodo.1"), "data")
        self.assertEqual(result["status"], rule.CONFIRM_1)
        self.assertIsNone(result["rule_value"])
        self.assertEqual(result["inputs_read"][0]["descriptions_visible_text"],
                         ["Bead counts by grave."])

    def test_duplicate_entries_for_one_version_test_it_once(self) -> None:
        spec = {"links": [deposit("10.5281/zenodo.9", scored_version="10.5281/zenodo.1"),
                          dict(deposit("10.5281/zenodo.1"), id="v1")]}
        result = rule.score_item("p", spec, pack_with("10.5281/zenodo.1"), "data")
        self.assertEqual(len(result["inputs_read"]), 1)


class NoStructuredInputTests(unittest.TestCase):
    """Missing inputs fall back to the model's score, flagged."""

    def test_missing_record_falls_back(self) -> None:
        result = rule.score_item("p", {"links": [deposit()]}, {"records": []}, "data")
        self.assertEqual(result["status"], rule.NO_INPUT)

    def test_no_principal_artefact_falls_back(self) -> None:
        spec = {"links": [{"id": "dep", "type": "code", "role": "dependency",
                           "link": "https://cran.r-project.org/package=x"}]}
        self.assertEqual(rule.score_item("p", spec, None, "code")["status"], rule.NO_INPUT)

    def test_uncurated_link_falls_back(self) -> None:
        spec = {"links": [{"id": "x", "type": "data", "link": "10.5281/zenodo.1"}]}
        self.assertEqual(rule.score_item("p", spec, pack_with("10.5281/zenodo.1"),
                                         "data")["status"], rule.NO_INPUT)

    def test_supplement_without_carries_falls_back(self) -> None:
        spec = {"links": [{"id": "s", "type": "supplement", "role": "principal",
                           "home": "supplement", "link": "10.1016/x"}]}
        self.assertEqual(rule.score_item("p", spec, None, "data")["status"], rule.NO_INPUT)


class ConjunctionTests(unittest.TestCase):
    """One failing principal artefact decides; a gap cannot hide a zero."""

    def test_zero_beats_gap(self) -> None:
        spec = {"links": [deposit(),
                          {"id": "srv", "type": "data", "role": "principal",
                           "home": "unmanaged", "link": "https://example.org/a.csv"}]}
        result = rule.score_item("p", spec, {"records": []}, "data")
        self.assertEqual(result["status"], rule.MECHANICAL_0)
        self.assertTrue(result["unresolved_inputs"])

    def test_zero_beats_confirm(self) -> None:
        spec = {"links": [deposit(),
                          {"id": "supp", "type": "supplement", "role": "principal",
                           "home": "supplement", "carries": ["data"], "link": "10.1016/x"}]}
        result = rule.score_item("p", spec, pack_with("10.5281/zenodo.1"), "data")
        self.assertEqual(result["status"], rule.MECHANICAL_0)

    def test_mirror_and_upstream_do_not_count(self) -> None:
        spec = {"links": [deposit(),
                          {"id": "gh", "type": "data+code", "role": "mirror",
                           "link": "https://github.com/x/y"},
                          {"id": "ads", "type": "data", "role": "upstream",
                           "link": "10.5284/1"}]}
        result = rule.score_item("p", spec, pack_with("10.5281/zenodo.1"), "data")
        self.assertEqual(result["status"], rule.CONFIRM_1)


class VisibleTextTests(unittest.TestCase):
    """Description text is judged as a reader sees it."""

    def test_tags_entities_and_whitespace(self) -> None:
        self.assertEqual(rule.visible_text("<p>A&nbsp;<em>b</em>\n c</p>"), "A b c")
        self.assertEqual(rule.visible_text(None), "")


if __name__ == "__main__":
    unittest.main()
