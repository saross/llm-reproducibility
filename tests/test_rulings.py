#!/usr/bin/env python3
"""Tests for gate 1.3's issues, rulings, and admission (foundation 3).

Specification: ``wiki/planning/reproduction-gate-1-3-design.md`` §6. Every
flag and review obligation is an ``Issue``: its message, with a stable id
(``code:subject``) and an evidence fingerprint. A human ruling binds to both,
so it lapses when the evidence changes but survives an unchanged re-run
(Astra's design review, point 7). These tests pin:

1. Issue identity: an issue is its message (so text-based relays keep
   working), and its fingerprint follows the evidence, not the wording.
2. Ruling matching and admitted coverage: unruled issues exclude their
   targets (all targets when none are named), negative rulings exclude,
   structural exclusions hold whatever the ruling, and a gate failure
   admits nothing.
3. ``rule-flags``: rulings bind to the authoritative report's fingerprints,
   need a decision valid for the issue's kind and a note, and refuse ids
   the report does not list.
4. ``admission``: the reasons an attempt cannot enter study data.
5. ``human-queue`` lists every issue as ruled or unruled.

The gate-level integration (issues and ``coverage_admitted`` in a real
``check_attempt`` report) is in ``test_reproduction_lane.GateTests``.

Run: ``venv/bin/python -m pytest tests/test_rulings.py -q``
"""

from __future__ import annotations

import argparse
import importlib.machinery
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent


def load_script(name: str, filename: str):
    """Import a hyphen-named script as a module (test_reconcile pattern)."""
    spec = importlib.util.spec_from_loader(
        name, importlib.machinery.SourceFileLoader(
            name, str(REPO_ROOT / "scripts" / filename)))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


lane = load_script("reproduction_lane_rulings", "reproduction-lane.py")


def write(path: Path, text: str) -> None:
    """Create a file (and parents) with content."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def edit_flag(digest: str = "a" * 64, targets: tuple[str, ...] = ("T01",)):
    """An edited-copy flag on authors-code/analysis.R."""
    return lane.Issue.flag("edited-copy", "authors-code/analysis.R", "it differs",
                           prefix=lane.FLAG_EDIT_PREFIX, targets=targets,
                           files={"authors-code/analysis.R": digest})


def semantics_obligation(digest: str = "b" * 64):
    """The wrapper-semantics obligation every attempt with wrappers raises."""
    return lane.Issue.obligation("wrapper-semantics", "wrappers", "confirm the wrappers",
                                 files={"run-analysis.R": digest})


class IssueTests(unittest.TestCase):
    """Issue identity and fingerprints."""

    def test_an_issue_is_its_message(self):
        flag = edit_flag()
        self.assertEqual(flag, lane.FLAG_EDIT_PREFIX + "it differs")
        self.assertIsInstance(flag, str)
        self.assertEqual(json.loads(json.dumps([flag])), [str(flag)])
        self.assertEqual(flag.issue_id, "edited-copy:authors-code/analysis.R")

    def test_fingerprint_follows_evidence_not_wording(self):
        base = edit_flag()
        reworded = lane.Issue.flag("edited-copy", "authors-code/analysis.R", "reworded",
                                   targets=("T01",),
                                   files={"authors-code/analysis.R": "a" * 64})
        self.assertEqual(base.fingerprint(), reworded.fingerprint())
        self.assertNotEqual(base.fingerprint(), edit_flag(digest="c" * 64).fingerprint())
        self.assertNotEqual(base.fingerprint(), edit_flag(targets=("T02",)).fingerprint())

    def test_policy_version_expires_only_its_own_code(self):
        flag, obligation = edit_flag(), semantics_obligation()
        before = flag.fingerprint(), obligation.fingerprint()
        lane.ISSUE_POLICY["edited-copy"] = 2
        try:
            self.assertNotEqual(flag.fingerprint(), before[0])
            self.assertEqual(obligation.fingerprint(), before[1])
        finally:
            del lane.ISSUE_POLICY["edited-copy"]

    def test_plain_strings_become_unclassified_issues(self):
        records = lane.issue_records([lane.FLAG_PREFIX + "old site", "an obligation"])
        self.assertEqual([r["kind"] for r in records], ["flag", "obligation"])
        self.assertEqual({r["code"] for r in records}, {"unclassified"})


class AdmittedCoverageTests(unittest.TestCase):
    """Ruling matching and coverage_admitted."""

    LOCKED = ("T01", "T02", "T03")

    def admitted(self, issues, rulings, verdict="pass", structural=None) -> dict:
        return lane.admitted_coverage(verdict, [i.record() for i in issues], rulings,
                                      list(self.LOCKED), list(self.LOCKED), structural or {})

    def ruling(self, issue, decision: str) -> dict:
        record = issue.record()
        return {"issue_id": record["id"], "fingerprint": record["fingerprint"],
                "decision": decision}

    def test_unruled_issue_excludes_its_targets(self):
        report = self.admitted([edit_flag()], [])
        self.assertEqual(report["excluded_targets"], ["T01"])
        self.assertEqual(report["unruled_issues"], ["edited-copy:authors-code/analysis.R"])

    def test_unruled_issue_without_targets_excludes_all(self):
        self.assertEqual(self.admitted([semantics_obligation()], [])["targets_admitted"], 0)

    def test_rulings_admit_or_exclude(self):
        obligation = semantics_obligation()
        discharged = self.admitted([obligation], [self.ruling(obligation, "discharged")])
        self.assertEqual(discharged["targets_admitted"], 3)
        excluded = self.admitted([obligation], [self.ruling(obligation, "excluded")])
        self.assertEqual(excluded["targets_admitted"], 0)

    def test_a_ruling_lapses_when_the_evidence_changes(self):
        """Astra's acceptance test: a changed input under an unchanged message."""
        ruled = self.ruling(semantics_obligation(), "discharged")
        changed = semantics_obligation(digest="d" * 64)
        self.assertEqual(str(changed), str(semantics_obligation()))
        self.assertEqual(self.admitted([changed], [ruled])["targets_admitted"], 0)

    def test_latest_matching_ruling_wins(self):
        obligation = semantics_obligation()
        rulings = [self.ruling(obligation, "excluded"), self.ruling(obligation, "discharged")]
        self.assertEqual(self.admitted([obligation], rulings)["targets_admitted"], 3)

    def test_structural_exclusion_holds_whatever_the_ruling(self):
        flag = edit_flag()
        report = self.admitted([flag], [self.ruling(flag, "admissible")],
                               structural={"declared edit": {"T01"}})
        self.assertEqual(report["excluded_targets"], ["T01"])

    def test_a_failed_gate_admits_nothing(self):
        self.assertEqual(self.admitted([], [], verdict="fail")["targets_admitted"], 0)


class RuleFlagsTests(unittest.TestCase):
    """rule-flags, admission, and the issue listing in human-queue."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        self.config = root / "run-config.yaml"
        self.config.write_text(json.dumps({
            "run_id": "run-x", "attempt": 2, "effort": "medium",
            "output_root": str(root / "outputs"),
            "agents": {"planner": "p", "executor": "e", "reviewer": "r"},
            "schemas": {"plan": "p", "execution": "e", "review": "r",
                        "comparison_record": "c"},
            "blinding": {"forbidden_substrings": []},
            "papers": [{"slug": "paper-a"}]}), encoding="utf-8")
        self.dir = root / "outputs" / "paper-a" / "reproduction" / "attempt-02"
        self.issues = [edit_flag(), semantics_obligation()]
        self.report(verdict="pass")
        self.rulings_file = root / "rulings.json"

    def tearDown(self):
        self.tmp.cleanup()

    def report(self, verdict: str, runs: dict | None = None) -> None:
        integrity = {"runs": runs} if runs is not None else {}
        write(self.dir / lane.GATE_FILE, json.dumps({
            "verdict": verdict, "flags": [str(self.issues[0])], "code_integrity": integrity,
            "issues": [i.record() for i in self.issues]}))

    def rule(self, *entries: dict) -> int:
        self.rulings_file.write_text(json.dumps(list(entries)), encoding="utf-8")
        return lane.cmd_rule_flags(argparse.Namespace(
            config=self.config, slug="paper-a", approver="Shawn", rulings=self.rulings_file))

    def test_rulings_bind_to_the_reports_fingerprints(self):
        self.rule({"issue": "wrapper-semantics:wrappers", "decision": "discharged",
                   "note": "wrappers only set paths"})
        stored = json.loads((self.dir / lane.RULINGS_FILE).read_text())["rulings"]
        self.assertEqual(stored[0]["fingerprint"], self.issues[1].fingerprint())
        self.assertEqual(stored[0]["approver"], "Shawn")

    def test_refusals(self):
        for entry in ({"issue": "nope:x", "decision": "discharged", "note": "n"},
                      {"issue": "wrapper-semantics:wrappers", "decision": "admissible",
                       "note": "a flag's decision on an obligation"},
                      {"issue": "edited-copy:authors-code/analysis.R",
                       "decision": "admissible", "note": "  "}):
            with self.assertRaises(lane.LaneError, msg=entry):
                self.rule(entry)
        self.assertFalse((self.dir / lane.RULINGS_FILE).exists())

    def test_admission_reasons(self):
        reasons = " | ".join(lane.admission(self.dir)["reasons"])
        self.assertIn("predates gate 1.3", reasons)
        self.assertIn("2 unruled issue(s)", reasons)
        self.assertIn("no transcript audit", reasons)
        self.report(verdict="pass", runs={"credited_runs": ["run-01"],
                                          "runs": {"run-01": {"state": "complete"}}})
        self.rule({"issue": "wrapper-semantics:wrappers", "decision": "discharged",
                   "note": "checked"},
                  {"issue": "edited-copy:authors-code/analysis.R",
                   "decision": "fail-and-uplift", "note": "a logic edit"})
        write(self.dir / lane.AUDIT_FILE, json.dumps({"contaminating": []}))
        verdict = lane.admission(self.dir)
        self.assertEqual((verdict["eligible"], verdict["reasons"]), (True, []))
        self.report(verdict="fail", runs={"credited_runs": ["run-01"],
                                          "runs": {"run-01": {"state": "incomplete"}}})
        reasons = " | ".join(lane.admission(self.dir)["reasons"])
        self.assertIn("run-01 is incomplete", reasons)
        self.assertIn("verdict is 'fail'", reasons)

    def test_a_transcript_audit_flag_is_listed_ruled_and_admitted(self):
        """Spec §12: a host run before the final run is a flag in the audit,
        which the human queue lists and rule-flags rules like any other."""
        host = lane.Issue.flag("host-run", "run-analysis.R", "the executor ran it on the host",
                               files={"run-analysis.R": "abc"})
        write(self.dir / lane.AUDIT_FILE, json.dumps({"contaminating": [],
                                                      "issues": [host.record()]}))
        self.report(verdict="pass", runs={"credited_runs": ["run-01"],
                                          "runs": {"run-01": {"state": "complete"}}})
        statuses = {i["id"] for i in lane.issue_statuses(lane.load_config(self.config))}
        self.assertIn("host-run:run-analysis.R", statuses)
        self.rule({"issue": "wrapper-semantics:wrappers", "decision": "discharged",
                   "note": "checked"},
                  {"issue": "edited-copy:authors-code/analysis.R",
                   "decision": "fail-and-uplift", "note": "a logic edit"})
        reasons = " | ".join(lane.admission(self.dir)["reasons"])
        self.assertIn("1 unruled transcript-audit issue(s): host-run:run-analysis.R", reasons)
        self.rule({"issue": "host-run:run-analysis.R", "decision": "admissible",
                   "note": "a parse check before the run"})
        self.assertTrue(lane.admission(self.dir)["eligible"])

    def test_human_queue_lists_issues_as_ruled_or_unruled(self):
        self.rule({"issue": "wrapper-semantics:wrappers", "decision": "discharged",
                   "note": "checked"})
        statuses = {i["id"]: i["status"] for i in lane.issue_statuses(
            lane.load_config(self.config))}
        self.assertEqual(statuses, {"edited-copy:authors-code/analysis.R": "unruled",
                                    "wrapper-semantics:wrappers": "ruled"})


if __name__ == "__main__":
    unittest.main()
