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
import contextlib
import importlib.machinery
import importlib.util
import io
import json
import re
import shutil
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
        # Admission checks every issue's targets against the locked plan
        # (gate 1.3.2), so the attempt has one, as every real attempt does.
        write(self.dir / lane.PLAN_FILE, json.dumps({"plan": {
            "paper_slug": "paper-a",
            "verification_targets": [{"target_id": t} for t in ("T01", "T02", "T03")]}}))
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

    def run_audit(self, executor: dict | None = None, reviewer: dict | None = None,
                  reviewed: list[str] | None = None, **fields) -> None:
        """Write a run audit from (agent audit record, payload) pairs (F8).

        ``reviewed`` is the attempt states the workflow's gate checks
        recorded; by default, the attempt's state now (D-Astra-3).
        """
        clean = {"clean": True, "receipts": {"valid": True, "problems": []},
                 "blinding": {"contaminating": [], "warnings": []}, "writes_outside_scope": []}
        roles = {"executor": (executor or {**clean, "agent_id": "e1"},
                              {"status": "OK", "verdict": "SUCCESSFUL"}),
                 "reviewer": (reviewer or {**clean, "agent_id": "r1"},
                              {"status": "OK", "overall": "CONFIRMED"})}
        roles.update(fields.pop("roles", {}))
        doc = lane.attempt_run_audit(lane.load_config(self.config), "wf_x", self.dir, roles,
                                     [lane.artefact_state(self.dir)] if reviewed is None
                                     else reviewed)
        doc.update(fields)
        write(self.dir / lane.RUN_AUDIT_FILE, json.dumps(doc))

    def audited(self) -> dict:
        """The identities the run audit cleared, as persist-results binds them."""
        doc = json.loads((self.dir / lane.RUN_AUDIT_FILE).read_text())
        return {"run_id": doc["run_id"], "workflow_run": doc["workflow_run"],
                "roles": {role: {"agent_id": entry["agent_id"],
                                 "payload_sha256": entry["payload_sha256"]}
                          for role, entry in doc["roles"].items()}}

    def admit(self, bound: dict | None = None) -> dict:
        """Admission for the results the run audit cleared, unless ``bound``
        names others; with no run audit, for no result."""
        if bound is None and (self.dir / lane.RUN_AUDIT_FILE).is_file():
            bound = self.audited()
        return lane.admission(self.dir, bound)

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
        reasons = " | ".join(self.admit()["reasons"])
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
        self.assertIn("no run audit recorded", " | ".join(self.admit()["reasons"]))
        self.run_audit()
        verdict = self.admit()
        self.assertEqual((verdict["eligible"], verdict["reasons"]), (True, []))
        self.report(verdict="fail", runs={"credited_runs": ["run-01"],
                                          "runs": {"run-01": {"state": "incomplete"}}})
        reasons = " | ".join(self.admit()["reasons"])
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
        self.run_audit()
        statuses = {i["id"] for i in lane.issue_statuses(lane.load_config(self.config))}
        self.assertIn("host-run:run-analysis.R", statuses)
        self.rule({"issue": "wrapper-semantics:wrappers", "decision": "discharged",
                   "note": "checked"},
                  {"issue": "edited-copy:authors-code/analysis.R",
                   "decision": "fail-and-uplift", "note": "a logic edit"})
        reasons = " | ".join(self.admit()["reasons"])
        self.assertIn("1 unruled transcript-audit issue(s): host-run:run-analysis.R", reasons)
        self.rule({"issue": "host-run:run-analysis.R", "decision": "admissible",
                   "note": "a parse check before the run"})
        self.assertTrue(self.admit()["eligible"])

    # The gate 1.3 final review's F8 (2026-10-12): admission reads the run
    # audit, so receipts, blinding, and review questions block it.

    def eligible_but_for_the_run_audit(self) -> None:
        self.report(verdict="pass", runs={"credited_runs": ["run-01"],
                                          "runs": {"run-01": {"state": "complete"}}})
        self.rule({"issue": "wrapper-semantics:wrappers", "decision": "discharged",
                   "note": "checked"},
                  {"issue": "edited-copy:authors-code/analysis.R",
                   "decision": "fail-and-uplift", "note": "a logic edit"})
        write(self.dir / lane.AUDIT_FILE, json.dumps({"contaminating": []}))

    def reasons(self) -> str:
        return " | ".join(self.admit()["reasons"])

    def test_an_unclean_role_cannot_be_ruled_into_admission(self):
        self.eligible_but_for_the_run_audit()
        invalid = {"clean": False, "receipts": {"valid": False, "problems": [
            "declared pull truncated (a partial shell read): tax.md"]},
            "blinding": {"contaminating": [], "warnings": []}, "writes_outside_scope": []}
        self.run_audit(executor=invalid)
        self.assertIn("the run audit found the executor unclean: declared pull truncated",
                      self.reasons())
        blinded = {"clean": False, "receipts": {"valid": True, "problems": []},
                   "blinding": {"contaminating": [{"path": "attempt-02/x", "rule": "r"}],
                                "warnings": []}, "writes_outside_scope": []}
        self.run_audit(reviewer=blinded)
        self.assertIn("the run audit found the reviewer unclean: blinded access",
                      self.reasons())

    def test_a_missing_review_blocks_admission(self):
        self.eligible_but_for_the_run_audit()
        self.run_audit()
        doc = json.loads((self.dir / lane.RUN_AUDIT_FILE).read_text())
        del doc["roles"]["reviewer"]
        write(self.dir / lane.RUN_AUDIT_FILE, json.dumps(doc))
        self.assertIn("the run audit has no reviewer", self.reasons())

    def test_review_concerns_and_escalations_are_issues_to_rule(self):
        self.eligible_but_for_the_run_audit()
        clean = {"clean": True, "receipts": {"valid": True, "problems": []},
                 "blinding": {"contaminating": [], "warnings": [
                     {"path": "x/verification-strategies.md", "rule": "named in output",
                      "command": "ls refs"}]}, "writes_outside_scope": []}
        executor = {"status": "ESCALATE", "verdict": "SUCCESSFUL", "escalations": [
            {"kind": "PAPER_ERROR", "target_id": "T01", "detail": "8 cells off by one"}]}
        reviewer = {"status": "OK", "overall": "QUALIFIED", "dimensions": {
            k: {"verdict": "CONCERN" if k == "methodological_soundness" else "PASS",
                "findings": []} for k in lane.DIMENSION_KEYS},
            "verdict_challenge": {"reviewer_supports_verdict": True}}
        quiet = {**clean, "blinding": {"contaminating": [], "warnings": []}}
        self.run_audit(roles={"executor": (clean, executor), "reviewer": (quiet, reviewer)})
        statuses = {i["id"]: i["status"] for i in lane.issue_statuses(
            lane.load_config(self.config))}
        for issue_id in ("escalation:executor:PAPER_ERROR:T01", "review:qualified",
                         "blinding-warning:executor:x/verification-strategies.md"):
            self.assertEqual(statuses.get(issue_id), "unruled", issue_id)
        self.assertIn("3 unruled run-audit issue(s)", self.reasons())
        self.rule({"issue": "escalation:executor:PAPER_ERROR:T01", "decision": "admissible",
                   "note": "confirmed against S3"},
                  {"issue": "review:qualified", "decision": "admissible",
                   "note": "the method change was ruled separately"},
                  {"issue": "blinding-warning:executor:x/verification-strategies.md",
                   "decision": "admissible", "note": "a directory listing, not a read"})
        self.assertTrue(self.admit()["eligible"])

    def test_the_run_audit_is_bound_to_the_launch_and_the_plan(self):
        self.eligible_but_for_the_run_audit()
        write(self.dir / lane.APPROVAL_FILE, json.dumps({"plan_sha256": "a" * 64}))
        doc_report = json.loads((self.dir / lane.GATE_FILE).read_text())
        doc_report["launch_commit"] = "c" * 40
        write(self.dir / lane.GATE_FILE, json.dumps(doc_report))
        self.run_audit(launch_commit="d" * 40, plan_sha256="b" * 64)
        reasons = self.reasons()
        self.assertIn("launch commit is not the gate report's", reasons)
        self.assertIn("under a different approved plan", reasons)

    EXECUTION = {"status": "OK", "paper_slug": "paper-a", "verdict": "SUCCESSFUL"}
    REVIEW = {"status": "OK", "paper_slug": "paper-a", "overall": "CONFIRMED"}
    # Reasons that say the run audit is not bound to the results persisted.
    BINDING = ("has no reviewer", "not 'wf_", "cleared reviewer agent", "payload digest",
               "attempt has changed", "no in-workflow gate check", "does not bind")

    def workflow(self, name: str, agents: list[tuple[str, str, dict]],
                 gate_states: tuple[str, ...] = ()) -> Path:
        """A workflow run directory for paper-a.

        One transcript per (agent id, type, payload), returning the payload
        through StructuredOutput, and one ungoverned gate agent per state in
        ``gate_states``, whose check-attempt printed that state.
        """
        run = Path(self.tmp.name) / name
        run.mkdir()
        prompts = {"e": f"  Paper: paper-a\n  Attempt directory: {self.dir}\n",
                   "r": "  Paper: paper-a\n  Review the attempt for paper-a.\n"}
        spawns = [(agent_id, agent_type, prompts[agent_type],
                   {"type": "tool_use", "id": "s", "name": "StructuredOutput", "input": payload},
                   "accepted") for agent_id, agent_type, payload in agents]
        spawns += [(f"gate{n}", "general-purpose", "  Paper: paper-a\n  Mechanical check.\n",
                    {"type": "tool_use", "id": "s", "name": "Bash", "input": {
                        "command": f"venv/bin/python scripts/reproduction-lane.py "
                                   f"check-attempt {self.dir}"}},
                    json.dumps({"verdict": "pass", "artefact_state_sha256": state}, indent=2))
                   for n, state in enumerate(gate_states)]
        for agent_id, agent_type, prompt, call, output in spawns:
            lines = [{"message": {"role": "user", "content": prompt}},
                     {"message": {"role": "assistant", "content": [call]}},
                     {"message": {"role": "user", "content": [
                         {"type": "tool_result", "tool_use_id": "s", "content": output}]}}]
            (run / f"agent-{agent_id}.jsonl").write_text(
                "\n".join(json.dumps(line) for line in lines) + "\n", encoding="utf-8")
            (run / f"agent-{agent_id}.meta.json").write_text(
                json.dumps({"agentType": agent_type}), encoding="utf-8")
        return run

    def audit_run(self, run: Path) -> None:
        with contextlib.redirect_stdout(io.StringIO()):
            lane.cmd_audit_run(argparse.Namespace(config=self.config, run_dir=run,
                                                  out=Path(self.tmp.name) / f"{run.name}.json"))

    def test_audit_run_binds_both_roles_through_the_real_command(self):
        """Fable's delta review, D-1: the reviewer's prompt has no "Attempt
        directory:" line, so audit-run must bind it by its Paper: line, or
        no attempt is ever admissible. Astra's delta review, D-Astra-3: each
        role is bound to its accepted payload, and the attempt to the state
        the workflow's gate check recorded before the review."""
        state = lane.artefact_state(self.dir)
        self.audit_run(self.workflow("wf_test", [("aaa", "e", self.EXECUTION),
                                                 ("bbb", "r", self.REVIEW)], (state,)))
        doc = json.loads((self.dir / lane.RUN_AUDIT_FILE).read_text())
        self.assertEqual((sorted(doc["roles"]), doc["missing_roles"]),
                         (["executor", "reviewer"], []))
        self.assertEqual((doc["roles"]["reviewer"]["agent_id"],
                          doc["roles"]["reviewer"]["payload_sha256"],
                          doc["reviewed_state_sha256"]),
                         ("bbb", lane.json_digest(self.REVIEW), state))
        reasons = " | ".join(self.admit()["reasons"])
        for absent in self.BINDING:
            self.assertNotIn(absent, reasons)

    def test_audit_run_refuses_two_results_for_one_paper(self):
        """D-Astra-3: a retried reviewer in the same workflow is ambiguous;
        version 1.0 kept whichever transcript sorted last."""
        run = self.workflow("wf_dup", [("aaa", "e", self.EXECUTION), ("bbb", "r", self.REVIEW),
                                       ("ccc", "r", self.REVIEW)])
        with self.assertRaisesRegex(lane.LaneError, "two r results for paper-a"):
            self.audit_run(run)
        self.assertFalse((self.dir / lane.RUN_AUDIT_FILE).exists())

    def test_admission_binds_the_results_being_persisted(self):
        """D-Astra-3: another workflow, a reviewer retry, a changed payload,
        a missing role, no named result, or an old audit is not cleared;
        unchanged matching identities are."""
        self.eligible_but_for_the_run_audit()
        self.run_audit()
        self.assertEqual(self.admit()["reasons"], [])
        audited = self.audited()
        other = {**audited, "workflow_run": "wf_new"}
        retry = json.loads(json.dumps(audited))
        retry["roles"]["reviewer"]["agent_id"] = "r2"
        changed = json.loads(json.dumps(audited))
        changed["roles"]["executor"]["payload_sha256"] = lane.json_digest(
            {"status": "OK", "verdict": "PARTIAL"})
        missing = json.loads(json.dumps(audited))
        del missing["roles"]["reviewer"]
        for bound, expected in (
                (other, "for workflow_run 'wf_x', not 'wf_new'"),
                (retry, "cleared reviewer agent 'r1', not 'r2'"),
                (changed, "the executor's result is not the one the run audit cleared"),
                (missing, "has no reviewer result")):
            verdict = self.admit(bound)
            self.assertFalse(verdict["eligible"], expected)
            self.assertIn(expected, " | ".join(verdict["reasons"]))
        self.assertIn("no result was named", " | ".join(lane.admission(self.dir)["reasons"]))
        doc = json.loads((self.dir / lane.RUN_AUDIT_FILE).read_text())
        doc["run_audit_version"] = "1.0"
        write(self.dir / lane.RUN_AUDIT_FILE, json.dumps(doc))
        self.assertIn("which does not bind results", " | ".join(self.admit(audited)["reasons"]))

    def test_a_review_covers_only_the_state_it_was_handed(self):
        """D-Astra-3: post-review records leave the reviewed state alone; a
        changed comparison does not, and a re-audit cannot launder it, since
        the gate check before the review recorded the old state."""
        self.eligible_but_for_the_run_audit()
        reviewed = lane.artefact_state(self.dir)
        self.run_audit()
        for name in (lane.EXECUTION_FILE, lane.REVIEW_FILE):
            write(self.dir / name, "{}")
        self.assertEqual(self.admit()["reasons"], [])
        write(self.dir / "comparisons" / "comparison.json", json.dumps({"verdict": "PARTIAL"}))
        changed = "has changed since the gate check that preceded its review"
        self.assertIn(changed, " | ".join(self.admit()["reasons"]))
        self.run_audit(reviewed=[reviewed])
        self.assertIn(changed, " | ".join(self.admit()["reasons"]))
        self.run_audit(reviewed=[])
        self.assertIn("no in-workflow gate check recorded", " | ".join(self.admit()["reasons"]))
        self.run_audit(reviewed=[reviewed, lane.artefact_state(self.dir)])
        self.assertIn("2 different attempt states", " | ".join(self.admit()["reasons"]))

    def test_persist_results_needs_the_audit_of_its_own_workflow(self):
        """Astra's probe through the real commands: a retried review in a new
        workflow is persisted ineligible while the run audit is the old
        workflow's; the old workflow's own results bind to it."""
        schemas = REPO_ROOT / "reproduction-system" / "schemas"
        config = json.loads(self.config.read_text())
        config["schemas"] = {"plan": str(schemas / "reproduction-plan-output.json"),
                             "execution": str(schemas / "reproduction-execution-output.json"),
                             "review": str(schemas / "adversarial-review-output.json"),
                             "comparison_record": str(schemas / "comparison-record.json")}
        self.config.write_text(json.dumps(config), encoding="utf-8")
        self.eligible_but_for_the_run_audit()
        state = lane.artefact_state(self.dir)
        old = self.workflow("wf_old", [("e1", "e", self.EXECUTION), ("r1", "r", self.REVIEW)],
                            (state,))
        self.audit_run(old)
        new = self.workflow("wf_new", [("e1", "e", self.EXECUTION), ("r2", "r", self.REVIEW)],
                            (state,))

        def persist(run: Path, force: bool) -> dict:
            with contextlib.redirect_stdout(io.StringIO()), \
                    contextlib.redirect_stderr(io.StringIO()):
                lane.cmd_persist_results(argparse.Namespace(
                    config=self.config, run_dir=run, force=force, record_unruled=False))
            return json.loads((self.dir / lane.REVIEW_FILE).read_text())

        saved = persist(new, False)
        self.assertEqual((saved["workflow_run"], saved["agent_id"]), ("wf_new", "r2"))
        reasons = " | ".join(saved["admission"]["reasons"])
        self.assertFalse(saved["admission"]["eligible"])
        self.assertIn("for workflow_run 'wf_old', not 'wf_new'", reasons)
        self.assertIn("cleared reviewer agent 'r1', not 'r2'", reasons)
        reasons = " | ".join(persist(old, True)["admission"]["reasons"])
        for absent in self.BINDING:
            self.assertNotIn(absent, reasons)

    def test_human_queue_lists_issues_as_ruled_or_unruled(self):
        self.rule({"issue": "wrapper-semantics:wrappers", "decision": "discharged",
                   "note": "checked"})
        statuses = {i["id"]: i["status"] for i in lane.issue_statuses(
            lane.load_config(self.config))}
        self.assertEqual(statuses, {"edited-copy:authors-code/analysis.R": "unruled",
                                    "wrapper-semantics:wrappers": "ruled"})
        scopes = {i["id"]: i["scope"] for i in lane.issue_statuses(
            lane.load_config(self.config))}
        self.assertEqual(scopes, {"edited-copy:authors-code/analysis.R": "targets",
                                  "wrapper-semantics:wrappers": "paper"})

    # Gate 1.3.2, criterion 1: a ruling may dispose of single targets.

    def comparison(self) -> None:
        """T01 and T02 reproduced, T03 a minor discrepancy."""
        write(self.dir / "comparisons" / "comparison.json", json.dumps({"targets": [
            {"target_id": "T01", "outcome": "EXACT_MATCH"},
            {"target_id": "T02", "outcome": "EXACT_MATCH"},
            {"target_id": "T03", "outcome": "MINOR_DISCREPANCY"}]}))

    def test_target_scoped_parts_of_a_ruling_are_stored(self):
        self.comparison()
        self.rule({"issue": "wrapper-semantics:wrappers", "decision": "discharged",
                   "targets": {"T02": "excluded"}, "classification": {"T03": "PAPER_ERROR"},
                   "note": "T02 rests on the second wrapper; T03 differs in content"})
        stored = json.loads((self.dir / lane.RULINGS_FILE).read_text())["rulings"][0]
        self.assertEqual((stored["targets"], stored["classification"]),
                         ({"T02": "excluded"}, {"T03": "PAPER_ERROR"}))
        self.assertNotIn("verdict", stored)

    def test_target_scoped_refusals(self):
        """An unknown or out-of-scope target, a decision the kind does not
        take, a classification that would create credit or is no outcome, a
        verdict off the review flag, and a note that does not say why for a
        target singled out are all refused, and nothing is recorded."""
        self.comparison()
        wrappers = {"issue": "wrapper-semantics:wrappers", "decision": "discharged"}
        edit = {"issue": "edited-copy:authors-code/analysis.R", "decision": "admissible"}
        for entry, expected in (
                ({**wrappers, "targets": {"T99": "excluded"}, "note": "T99"},
                 "'T99', which is not a locked target"),
                ({**edit, "targets": {"T02": "excluded"}, "note": "T02"},
                 "T02, outside the issue's targets (T01)"),
                ({**wrappers, "targets": {"T02": "admissible"}, "note": "T02"},
                 "but obligations are ruled discharged"),
                ({**wrappers, "classification": {"T03": "EXACT_MATCH"}, "note": "T03"},
                 "a ruling never creates credit"),
                ({**wrappers, "classification": {"T03": "FINE"}, "note": "T03"},
                 "not a comparison outcome"),
                ({**wrappers, "verdict": "PARTIAL", "note": "partial"},
                 "only on the review's verdict flag"),
                ({**wrappers, "targets": {"T02": "excluded"}, "note": "the second wrapper"},
                 "does not name T02"),
                ({**wrappers, "targets": [], "note": "none"}, "must map target ids")):
            with self.assertRaisesRegex(lane.LaneError, re.escape(expected), msg=entry):
                self.rule(entry)
        self.assertFalse((self.dir / lane.RULINGS_FILE).exists())

    def test_admission_fails_on_an_unknown_target_or_no_plan(self):
        """Gate 1.3.2: a target the plan does not lock would exclude nothing."""
        self.issues = [edit_flag(targets=("T09",)), semantics_obligation()]
        self.report(verdict="pass")
        self.assertIn("edited-copy:authors-code/analysis.R names targets not in the locked "
                      "plan: ['T09']", self.reasons())
        (self.dir / lane.PLAN_FILE).unlink()
        self.assertIn("no readable approved plan", self.reasons())


# ---------------------------------------------------------------------------
# Gate 1.3.2, criterion 1: target-scoped concerns and the adjudicated result
# ---------------------------------------------------------------------------

def scoped_ruling(issue, decision: str, **parts) -> dict:
    """A stored ruling on an issue, with any target-scoped parts."""
    record = issue.record()
    return {"issue_id": record["id"], "fingerprint": record["fingerprint"],
            "decision": decision, **parts}


def review_concern(cid: str, targets: tuple[str, ...] = ("T02",), **fields) -> dict:
    """A concern as a v1.4 reviewer states it."""
    return {"concern_id": cid, "dimension": "methodological_soundness",
            "scope": "targets" if targets else "paper", "targets": list(targets),
            "summary": f"concern {cid}", "evidence": ["comparisons/t02.csv"], **fields}


def review_payload(*concerns: dict, concern_dims: tuple[str, ...] = ("methodological_soundness",),
                   version: str = "v1.4", **fields) -> dict:
    """A QUALIFIED v1.4 review stating ``concerns``."""
    return {"status": "OK", "paper_slug": "paper-a", "overall": "QUALIFIED",
            "receipts": {"agent_version": f"adversarial-reviewer {version}"},
            "dimensions": {k: {"verdict": "CONCERN" if k in concern_dims else "PASS",
                               "findings": []} for k in lane.DIMENSION_KEYS},
            "verdict_challenge": {"executor_verdict": "SUCCESSFUL",
                                  "reviewer_supports_verdict": True, "rationale": "r"},
            "concerns": list(concerns), **fields}


class ScopedCoverageTests(unittest.TestCase):
    """admitted_coverage with per-target decisions and ruled classifications."""

    LOCKED = ["T01", "T02", "T03"]

    def admitted(self, issues, rulings, reproduced=("T01", "T02", "T03")) -> dict:
        return lane.admitted_coverage("pass", [i.record() for i in issues], rulings,
                                      self.LOCKED, list(reproduced), {})

    @staticmethod
    def concern_flag(subject: str, targets: tuple[str, ...]):
        return lane.Issue.flag("review-concern", subject, "a concern", targets=targets,
                               files={"concern": subject})

    def test_scope_is_stated_without_changing_any_fingerprint(self):
        """The scope derives from the targets the print already covers, so
        stating it lapses none of the rulings made before gate 1.3.2."""
        for issue, scope in ((edit_flag(), "targets"), (semantics_obligation(), "paper")):
            record = issue.record()
            self.assertEqual((record["scope"], lane.issue_scope(record)), (scope, scope))
            self.assertEqual(record["fingerprint"], lane.json_digest(
                {"code": issue.code, "policy": 1, "subject": issue.subject,
                 "targets": list(issue.targets), "files": issue.files}))

    def test_a_per_target_decision_disposes_of_that_target_alone(self):
        obligation = semantics_obligation()
        report = self.admitted([obligation], [scoped_ruling(obligation, "discharged",
                                                            targets={"T02": "excluded"})])
        self.assertEqual((report["targets_admitted"], report["excluded_targets"]), (2, ["T02"]))
        self.assertIn("wrapper-semantics:wrappers ruled excluded on T02", report["reasons"])
        kept = self.admitted([obligation], [scoped_ruling(obligation, "excluded",
                                                          targets={"T01": "discharged"})])
        self.assertEqual(kept["excluded_targets"], ["T02", "T03"])

    def test_several_concerns_on_one_target(self):
        first, second = self.concern_flag("C1", ("T02",)), self.concern_flag("C2", ("T02",))
        one_out = self.admitted([first, second], [scoped_ruling(first, "admissible"),
                                                  scoped_ruling(second, "excluded")])
        self.assertEqual(one_out["excluded_targets"], ["T02"])
        both_in = self.admitted([first, second], [scoped_ruling(first, "admissible"),
                                                  scoped_ruling(second, "admissible")])
        self.assertEqual(both_in["targets_admitted"], 3)

    def test_one_concern_on_several_targets(self):
        shared = self.concern_flag("C1", ("T01", "T02"))
        report = self.admitted([shared], [scoped_ruling(shared, "admissible",
                                                        targets={"T02": "excluded"})])
        self.assertEqual((report["targets_admitted"], report["excluded_targets"]), (2, ["T02"]))
        unruled = self.admitted([shared], [])
        self.assertEqual(unruled["excluded_targets"], ["T01", "T02"])

    def test_a_ruled_classification_removes_credit_but_never_adds_it(self):
        obligation = semantics_obligation()
        relabelled = self.admitted([obligation], [scoped_ruling(
            obligation, "discharged", classification={"T02": "PAPER_ERROR"})])
        self.assertEqual(relabelled["excluded_targets"], ["T02"])
        # A hand-edited ruling that would credit T03 adds nothing.
        upgraded = self.admitted([obligation], [scoped_ruling(
            obligation, "discharged", classification={"T03": "EXACT_MATCH"})],
            reproduced=("T01", "T02"))
        self.assertEqual(upgraded["targets_admitted"], 2)

    def test_conflicting_classifications_exclude_the_target(self):
        first, second = self.concern_flag("C1", ("T02",)), self.concern_flag("C2", ("T02",))
        report = self.admitted([first, second], [
            scoped_ruling(first, "admissible", classification={"T02": "WITHIN_PRECISION"}),
            scoped_ruling(second, "admissible", classification={"T02": "EXACT_MATCH"})])
        self.assertEqual(report["excluded_targets"], ["T02"])
        self.assertTrue(any("conflicting" in r for r in report["reasons"]))


class ReviewConcernTests(unittest.TestCase):
    """A v1.4 reviewer's concerns, each its own scoped issue (gate 1.3.2)."""

    LOCKED = ["T01", "T02", "T03"]

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self.tmp.name)
        write(self.dir / "comparisons" / "t02.csv", "a,b\n1,2\n")

    def tearDown(self):
        self.tmp.cleanup()

    def issues(self, payload: dict, role: str = "reviewer") -> dict[str, dict]:
        return {r["id"]: r for r in lane.issue_records(
            lane.review_issues(role, payload, [], self.dir, self.LOCKED))}

    def test_each_concern_is_its_own_scoped_issue(self):
        found = self.issues(review_payload(review_concern("C1"), review_concern("C2", ())))
        self.assertEqual(sorted(found), ["review-concern:C1", "review-concern:C2",
                                         "review:qualified"])
        self.assertEqual((found["review-concern:C1"]["targets"],
                          found["review-concern:C1"]["scope"]), (["T02"], "targets"))
        self.assertEqual(found["review-concern:C2"]["scope"], "paper")
        self.assertIn("comparisons/t02.csv", found["review-concern:C1"]["files"])
        self.assertIn("a human rules the verdict", found["review:qualified"]["message"])

    def test_a_concern_lapses_when_its_evidence_changes(self):
        payload = review_payload(review_concern("C1"))
        before = self.issues(payload)["review-concern:C1"]["fingerprint"]
        write(self.dir / "comparisons" / "t02.csv", "a,b\n1,3\n")
        self.assertNotEqual(self.issues(payload)["review-concern:C1"]["fingerprint"], before)

    def test_a_malformed_concern_bears_on_the_whole_paper(self):
        """Shawn, 2026-10-18: a slip costs a ruling, not a re-run. While
        unruled, a paper-wide issue excludes every target, so nothing a
        reviewer mistyped can pass silently."""
        for fields, defect in (
                ({"targets": ["T99"]}, "not in the locked plan: ['T99']"),
                ({"targets": [], "scope": "targets"}, "scoped to targets but names none"),
                ({"scope": "paper"}, "paper-wide but names targets"),
                ({"dimension": "provenance"}, "which the review does not mark CONCERN"),
                ({"evidence": ["comparisons/absent.csv"]}, "is not a file in the attempt"),
                ({"evidence": ["../../etc/passwd"]}, "is not a file in the attempt"),
                ({"evidence": []}, "cites no evidence")):
            issue = self.issues(review_payload(review_concern("C1", **fields)))[
                "review-concern:C1"]
            self.assertEqual(issue["scope"], "paper", fields)
            self.assertIn(defect, issue["message"], fields)

    def test_a_repeated_id_does_not_hide_a_concern(self):
        found = self.issues(review_payload(review_concern("C1"), review_concern("C1", ("T03",))))
        self.assertEqual(found["review-concern:C1"]["targets"], ["T02"])
        self.assertEqual(found["review-concern:C1#2"]["scope"], "paper")
        self.assertIn("used by an earlier concern", found["review-concern:C1#2"]["message"])

    def test_missing_concerns_are_paper_wide_flags(self):
        uncovered = self.issues(review_payload(
            review_concern("C1"), concern_dims=("methodological_soundness",
                                                "confirmation_bias")))
        self.assertEqual(uncovered["review-defect:uncovered:confirmation_bias"]["scope"],
                         "paper")
        no_list = review_payload()
        del no_list["concerns"]
        self.assertIn("review-defect:no-concerns", self.issues(no_list))
        # A v1.3 review's prose findings keep the single verdict flag.
        legacy = review_payload(version="v1.3")
        del legacy["concerns"]
        self.assertEqual(sorted(self.issues(legacy)), ["review:qualified"])

    def test_an_escalation_on_an_unknown_target_is_paper_wide(self):
        found = self.issues({"status": "ESCALATE", "escalations": [
            {"kind": "PAPER_ERROR", "target_id": "T99", "detail": "d"},
            {"kind": "OTHER", "target_id": "T03", "detail": "d"}]}, role="executor")
        self.assertEqual(found["escalation:executor:PAPER_ERROR:T99"]["scope"], "paper")
        self.assertEqual(found["escalation:executor:OTHER:T03"]["targets"], ["T03"])

    def test_an_absolute_evidence_path_binds_the_same_file(self):
        relative = self.issues(review_payload(review_concern("C1")))["review-concern:C1"]
        absolute = self.issues(review_payload(review_concern(
            "C1", evidence=[str(self.dir / "comparisons" / "t02.csv")])))["review-concern:C1"]
        self.assertEqual(absolute["scope"], "targets")
        self.assertEqual(absolute["files"]["comparisons/t02.csv"],
                         relative["files"]["comparisons/t02.csv"])

    def test_a_slip_leaves_the_role_clean(self):
        clean = {"clean": True, "receipts": {"valid": True, "problems": []},
                 "blinding": {"contaminating": [], "warnings": []}, "writes_outside_scope": []}
        write(self.dir / lane.PLAN_FILE, json.dumps({"plan": {"verification_targets": [
            {"target_id": t} for t in self.LOCKED]}}))
        doc = lane.attempt_run_audit(
            {"run_id": "t"}, "wf_x", self.dir,
            {"executor": (clean, {"status": "OK"}),
             "reviewer": (clean, review_payload(review_concern("C1", targets=["T99"])))})
        self.assertTrue(doc["roles"]["reviewer"]["clean"])
        self.assertIn("review-concern:C1", [i["id"] for i in doc["issues"]])


class AdjudicationTests(unittest.TestCase):
    """adjudicate and verify_adjudicated on a synthetic eligible attempt."""

    LOCKED = ("T01", "T02", "T03")

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
        self.rulings_file = root / "rulings.json"
        write(self.dir / lane.PLAN_FILE, json.dumps({"plan": {
            "paper_slug": "paper-a",
            "verification_targets": [{"target_id": t} for t in self.LOCKED]}}))
        plan_sha = lane.sha256_file(self.dir / lane.PLAN_FILE)
        write(self.dir / "comparisons" / "comparison.json", json.dumps({
            "paper_slug": "paper-a", "plan_sha256": plan_sha, "verdict": "SUCCESSFUL",
            "targets": [{"target_id": "T01", "outcome": "EXACT_MATCH"},
                        {"target_id": "T02", "outcome": "EXACT_MATCH"},
                        {"target_id": "T03", "outcome": "MINOR_DISCREPANCY"}]}))
        write(self.dir / "comparisons" / "t02.csv", "a,b\n1,2\n")
        issues = [semantics_obligation(),
                  lane.Issue.flag("method-deviation", "T01", "T01 departed", targets=("T01",),
                                  files={"record": "x"})]
        records = [i.record() for i in issues]
        write(self.dir / lane.GATE_FILE, json.dumps({
            "gate_version": lane.GATE_VERSION, "checked_at": "2026-10-18T00:00:00+00:00",
            "verdict": "pass", "plan_sha256": plan_sha, "flags": [str(issues[1])],
            "coverage": {"targets_enumerated": 3, "targets_reproduced": 2,
                         "coverage_fraction": 0.6667},
            "coverage_admitted": lane.admitted_coverage("pass", records, [], list(self.LOCKED),
                                                        ["T01", "T02"], {}),
            "code_integrity": {"runs": {"credited_runs": ["run-01"],
                                        "runs": {"run-01": {"state": "complete"}}}},
            "issues": records}))
        write(self.dir / lane.AUDIT_FILE, json.dumps({"contaminating": [], "issues": []}))
        self.execution = {"status": "ESCALATE", "paper_slug": "paper-a",
                          "verdict": "SUCCESSFUL", "escalations": [
                              {"kind": "OTHER", "target_id": "T03", "detail": "two cells"}]}
        self.audit(review_payload(review_concern("C1"), review_concern(
            "C2", (), evidence=[lane.PLAN_FILE])))

    def tearDown(self):
        self.tmp.cleanup()

    def audit(self, review: dict, reviewed: list[str] | None = None) -> None:
        """The run audit and persisted results for ``review``, as the post-run
        order leaves them; by default the attempt was reviewed as it stands."""
        clean = {"clean": True, "receipts": {"valid": True, "problems": []},
                 "blinding": {"contaminating": [], "warnings": []}, "writes_outside_scope": []}
        roles = {"executor": ({**clean, "agent_id": "e1"}, self.execution),
                 "reviewer": ({**clean, "agent_id": "r1"}, review)}
        write(self.dir / lane.RUN_AUDIT_FILE, json.dumps(lane.attempt_run_audit(
            lane.load_config(self.config), "wf_x", self.dir, roles,
            [lane.artefact_state(self.dir)] if reviewed is None else reviewed)))
        for name, agent_id, payload in ((lane.EXECUTION_FILE, "e1", self.execution),
                                        (lane.REVIEW_FILE, "r1", review)):
            write(self.dir / name, json.dumps({"record_version": "1.0", "run_id": "run-x",
                                               "workflow_run": "wf_x", "agent_id": agent_id,
                                               "admission": {"eligible": True},
                                               "payload": payload}))

    def rule(self, *entries: dict) -> None:
        self.rulings_file.write_text(json.dumps(list(entries)), encoding="utf-8")
        with contextlib.redirect_stdout(io.StringIO()):
            lane.cmd_rule_flags(argparse.Namespace(config=self.config, slug="paper-a",
                                                   approver="Shawn", rulings=self.rulings_file))

    def rule_all(self, **changes: dict) -> None:
        """Rule every issue admissible (or discharged), with ``changes`` by id."""
        issue_ids = lane.attempt_issues(self.dir, json.loads(
            (self.dir / lane.GATE_FILE).read_text()))
        entries = []
        for issue_id, issue in issue_ids.items():
            decision = "discharged" if issue["kind"] == "obligation" else "admissible"
            entries.append({"issue": issue_id, "decision": decision,
                            "note": f"checked ({issue_id})", **changes.get(issue_id, {})})
        self.rule(*entries)

    def adjudicated(self) -> dict:
        return lane.adjudicate(self.dir)

    def write_adjudicated(self, check: bool = False) -> int:
        """Run the adjudicate command (``--check`` when ``check``)."""
        with contextlib.redirect_stdout(io.StringIO()):
            return lane.cmd_adjudicate(argparse.Namespace(attempt_dir=self.dir, check=check))

    def credit(self, result: dict) -> dict[str, str]:
        return {row["target_id"]: row["credit"] for row in result["targets"]}

    def test_the_result_is_derived_per_target(self):
        self.rule_all(**{"review-concern:C1": {"decision": "excluded",
                                               "note": "C1 is right about T02"},
                         "escalation:executor:OTHER:T03": {
                             "classification": {"T03": "PAPER_ERROR"},
                             "note": "T03 differs in content, so PAPER_ERROR"}})
        result = self.adjudicated()
        self.assertEqual(self.credit(result), {"T01": "credited", "T02": "excluded",
                                               "T03": "not-reproduced"})
        self.assertEqual((result["coverage"]["targets_enumerated"],
                          result["coverage"]["targets_credited"]), (3, 1))
        t03 = result["targets"][2]
        self.assertEqual((t03["raw_outcome"], t03["ruled_outcome"]),
                         ("MINOR_DISCREPANCY", "PAPER_ERROR"))
        self.assertEqual(t03["classification_set_by"]["issue_id"],
                         "escalation:executor:OTHER:T03")
        self.assertIn("review-concern:C1 ruled excluded", result["targets"][1]["reasons"])
        self.assertEqual(result["verdict"]["ruled"], "SUCCESSFUL")
        self.assertIsNone(result["verdict"]["set_by"])
        self.assertEqual(result["history"]["raw_coverage"]["targets_reproduced"], 2)
        self.assertEqual(result["history"]["gate_coverage_admitted"]["targets_admitted"], 0)
        self.assertEqual({i["issue_id"] for i in result["paper_issues"]},
                         {"wrapper-semantics:wrappers", "review-concern:C2",
                          "review:qualified"})

    def test_several_concerns_on_one_target(self):
        self.audit(review_payload(review_concern("C1"), review_concern("C3")))
        self.rule_all(**{"review-concern:C3": {"decision": "excluded", "note": "T02 fails"}})
        self.assertEqual(self.credit(self.adjudicated())["T02"], "excluded")
        self.rule({"issue": "review-concern:C3", "decision": "admissible",
                   "note": "on reflection, T02 holds"})
        self.assertEqual(self.credit(self.adjudicated())["T02"], "credited")

    def test_one_concern_on_several_targets(self):
        self.audit(review_payload(review_concern("C1", ("T01", "T02"))))
        self.rule_all(**{"review-concern:C1": {"targets": {"T02": "excluded"},
                                               "note": "it holds for T02 only"}})
        result = self.adjudicated()
        self.assertEqual((self.credit(result)["T01"], self.credit(result)["T02"]),
                         ("credited", "excluded"))
        bearing = {i["issue_id"]: i["decision"] for i in result["targets"][1]["issues"]}
        self.assertEqual(bearing["review-concern:C1"], "excluded")

    def test_a_paper_wide_concern(self):
        self.rule_all(**{"review-concern:C2": {"decision": "excluded", "note": "all fall"}})
        self.assertEqual(self.adjudicated()["coverage"]["targets_credited"], 0)
        self.rule({"issue": "review-concern:C2", "decision": "admissible",
                   "targets": {"T01": "fail-and-uplift"}, "note": "only T01 rests on it"})
        result = self.adjudicated()
        self.assertEqual(self.credit(result), {"T01": "uplift", "T02": "credited",
                                               "T03": "not-reproduced"})
        self.assertEqual(result["coverage"]["uplift_targets"], ["T01"])

    def test_the_verdict_is_ruled_on_the_review_flag(self):
        self.rule_all(**{"review:qualified": {"verdict": "PARTIAL",
                                              "note": "the uncredited target matters"}})
        verdict = self.adjudicated()["verdict"]
        self.assertEqual((verdict["executor"], verdict["ruled"],
                          verdict["set_by"]["issue_id"]),
                         ("SUCCESSFUL", "PARTIAL", "review:qualified"))

    def test_a_slip_costs_a_ruling_not_a_rerun(self):
        """Shawn, 2026-10-18: a concern naming an unknown target bears on the
        whole paper; ruled per target, the attempt is final with no re-run."""
        self.audit(review_payload(review_concern("C1", ("T99",)), review_concern("C2", ())))
        with self.assertRaisesRegex(lane.LaneError, "review-concern:C1 is unruled"):
            self.adjudicated()
        self.rule_all(**{"review-concern:C1": {"targets": {"T02": "excluded"},
                                               "note": "it meant T02, not T99"}})
        self.assertEqual(self.credit(self.adjudicated())["T02"], "excluded")

    def test_written_only_when_final(self):
        with self.assertRaisesRegex(lane.LaneError, "not final") as raised:
            lane.cmd_adjudicate(argparse.Namespace(attempt_dir=self.dir, check=False))
        self.assertIn("review-concern:C1 is unruled", str(raised.exception))
        self.assertFalse((self.dir / lane.ADJUDICATED_FILE).exists())
        with self.assertRaisesRegex(lane.LaneError, "no adjudicated result"):
            lane.verify_adjudicated(self.dir)

    def test_a_result_persisted_ineligible_needs_persisting_again(self):
        """Spec §6: only a fresh persist-results makes a record eligible, so
        adjudication cannot launder one persisted with --record-unruled."""
        self.rule_all()
        record = json.loads((self.dir / lane.EXECUTION_FILE).read_text())
        record["admission"] = {"eligible": False, "reasons": ["2 unruled issue(s)"]}
        write(self.dir / lane.EXECUTION_FILE, json.dumps(record))
        with self.assertRaisesRegex(lane.LaneError, "execution-report.json was persisted "
                                                    "ineligible"):
            self.adjudicated()

    def test_incomplete_dispositions_are_not_final(self):
        """Conflicting classifications, and a hand-edited ruling that would
        create credit, leave the result unwritten."""
        self.rule_all(**{"escalation:executor:OTHER:T03": {
                             "classification": {"T03": "PAPER_ERROR"}, "note": "T03 content"},
                         "review-concern:C2": {"classification": {"T03": "MAJOR_DISCREPANCY"},
                                               "note": "T03 is major"}})
        with self.assertRaisesRegex(lane.LaneError, "T03 has conflicting ruled classifications"):
            self.adjudicated()
        doc = json.loads((self.dir / lane.RULINGS_FILE).read_text())
        doc["rulings"] = [{**r, "classification": {"T03": "EXACT_MATCH"}}
                          if r["issue_id"] == "escalation:executor:OTHER:T03" else
                          {k: v for k, v in r.items() if k != "classification"}
                          for r in doc["rulings"]]
        write(self.dir / lane.RULINGS_FILE, json.dumps(doc))
        with self.assertRaisesRegex(lane.LaneError, "a ruling never creates credit"):
            self.adjudicated()

    def test_a_changed_ruling_makes_the_stored_result_stale(self):
        """The study reads through verify_adjudicated, which re-derives the
        record; writing the record leaves the reviewed state alone."""
        self.rule_all()
        state = lane.artefact_state(self.dir)
        self.assertEqual(self.write_adjudicated(), 0)
        self.assertEqual(lane.artefact_state(self.dir), state)
        self.assertEqual(lane.verify_adjudicated(self.dir)["coverage"]["targets_credited"], 2)
        self.assertEqual(self.write_adjudicated(check=True), 0)
        self.rule({"issue": "review-concern:C1", "decision": "excluded", "note": "T02 fails"})
        with self.assertRaisesRegex(lane.LaneError, "stale"):
            lane.verify_adjudicated(self.dir)
        self.write_adjudicated()
        self.assertEqual(lane.verify_adjudicated(self.dir)["coverage"]["excluded_targets"],
                         ["T02"])

    def test_changed_evidence_needs_a_new_review_and_a_new_ruling(self):
        self.rule_all()
        write(self.dir / "comparisons" / "t02.csv", "a,b\n1,3\n")
        with self.assertRaisesRegex(lane.LaneError, "has changed since the gate check"):
            self.adjudicated()
        # A fresh review of the changed attempt binds the concern to the new
        # file, so the old ruling on it no longer applies.
        self.audit(json.loads((self.dir / lane.REVIEW_FILE).read_text())["payload"])
        with self.assertRaisesRegex(lane.LaneError, "review-concern:C1 is unruled"):
            self.adjudicated()


ATTEMPT_04 = (REPO_ROOT / "studies" / "open-science-compliance" / "outputs"
              / "herskind-riede-2024" / "reproduction" / "attempt-04")


@unittest.skipUnless((ATTEMPT_04 / lane.GATE_FILE).is_file(),
                     "attempt 04's records are not in this checkout")
class PilotAdjudicationTests(unittest.TestCase):
    """Gate 1.3.2's acceptance fixture: attempt 04's real records, in a copy.

    Shawn's rulings of 2026-10-17 exclude T17 (ruling Q5, under amendment 3
    §7(d)) and record T03 as PAPER_ERROR, but only in their notes, so the
    lane admitted 14/18. Restated with target-scoped parts, the same
    records derive 13/18 with T17 alone excluded, all 18 in the
    denominator, and T03 shown as PAPER_ERROR, keeping the raw 14/18 and
    the pre-ruling 0/18 as history. The real attempt is never written.
    """

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        self.dir = root / "outputs" / "herskind-riede-2024" / "reproduction" / "attempt-04"
        shutil.copytree(ATTEMPT_04, self.dir)
        self.config = root / "run-config.yaml"
        self.config.write_text(json.dumps({
            "run_id": "gate-1-3-1-pilot-rerun-2026-10", "attempt": 4, "effort": "high",
            "output_root": str(root / "outputs"),
            "agents": {"planner": "p", "executor": "e", "reviewer": "r"},
            "schemas": {"plan": "p", "execution": "e", "review": "r",
                        "comparison_record": "c"},
            "blinding": {"forbidden_substrings": []},
            "papers": [{"slug": "herskind-riede-2024"}]}), encoding="utf-8")

    def tearDown(self):
        self.tmp.cleanup()

    def as_ruled_on_2026_10_17(self) -> None:
        """The copy's rulings as they stood before the restatement: the
        2026-10-17 rulings, none with target-scoped parts."""
        path = self.dir / lane.RULINGS_FILE
        doc = json.loads(path.read_text())
        doc["rulings"] = [r for r in doc["rulings"]
                          if not any(k in r for k in ("targets", "classification", "verdict"))]
        write(path, json.dumps(doc))
        (self.dir / lane.ADJUDICATED_FILE).unlink(missing_ok=True)

    def restate_rulings(self) -> None:
        """The two rulings' target-scoped parts, as Shawn's notes state them."""
        rulings = Path(self.tmp.name) / "rulings.json"
        rulings.write_text(json.dumps([
            {"issue": "review:qualified", "decision": "admissible",
             "targets": {"T17": "excluded"}, "verdict": "SUCCESSFUL",
             "note": "Restates the 2026-10-17 ruling: T17 is not creditable under amendment 3 "
                     "s7(d) (ruling Q5), since its rule was applied to S1, not to outputs of "
                     "the authors' code; the verdict SUCCESSFUL stands."},
            {"issue": "escalation:executor:OTHER:T03", "decision": "admissible",
             "classification": {"T03": "PAPER_ERROR"},
             "note": "Restates the 2026-10-17 ruling: T03 is recorded as PAPER_ERROR, not "
                     "MINOR_DISCREPANCY; its two cells differ in content against S1."}]),
            encoding="utf-8")
        with contextlib.redirect_stdout(io.StringIO()):
            lane.cmd_rule_flags(argparse.Namespace(config=self.config,
                                                   slug="herskind-riede-2024",
                                                   approver="fixture", rulings=rulings))

    def test_the_notes_alone_leave_the_lanes_14_of_18(self):
        self.as_ruled_on_2026_10_17()
        result = lane.adjudicate(self.dir)
        self.assertEqual(result["coverage"]["targets_credited"], 14)
        self.assertIn("T17", result["coverage"]["credited_targets"])
        self.assertEqual(result["targets"][2]["ruled_outcome"], "MINOR_DISCREPANCY")

    def test_the_ruled_result_is_13_of_18(self):
        self.as_ruled_on_2026_10_17()
        self.restate_rulings()
        result = lane.adjudicate(self.dir)
        coverage = result["coverage"]
        self.assertEqual((coverage["targets_enumerated"], coverage["targets_credited"],
                          coverage["excluded_targets"], coverage["uplift_targets"]),
                         (18, 13, ["T17"], []))
        self.assertEqual(coverage["not_reproduced_targets"], ["T01", "T03", "T04", "T05"])
        self.assertEqual(len(result["targets"]), 18)
        rows = {row["target_id"]: row for row in result["targets"]}
        self.assertEqual((rows["T03"]["raw_outcome"], rows["T03"]["ruled_outcome"],
                          rows["T03"]["classification_set_by"]["issue_id"]),
                         ("MINOR_DISCREPANCY", "PAPER_ERROR", "escalation:executor:OTHER:T03"))
        self.assertEqual((rows["T17"]["raw_outcome"], rows["T17"]["credit"]),
                         ("EXACT_MATCH", "excluded"))
        self.assertIn("review:qualified ruled excluded on T17", rows["T17"]["reasons"])
        self.assertEqual((result["verdict"]["ruled"], result["verdict"]["set_by"]["issue_id"]),
                         ("SUCCESSFUL", "review:qualified"))
        history = result["history"]
        self.assertEqual((history["raw_coverage"]["targets_reproduced"],
                          history["gate_coverage_admitted"]["targets_admitted"]), (14, 0))
        # Written, the record leaves the reviewed state alone and reads back.
        with contextlib.redirect_stdout(io.StringIO()):
            lane.cmd_adjudicate(argparse.Namespace(attempt_dir=self.dir, check=False))
        self.assertEqual(lane.verify_adjudicated(self.dir)["coverage"]["targets_credited"], 13)
        self.assertEqual(lane.artefact_state(self.dir), json.loads(
            (self.dir / lane.RUN_AUDIT_FILE).read_text())["reviewed_state_sha256"])

    def test_the_recorded_result_is_current(self):
        """Shawn approved the restated rulings (2026-10-18); the attempt's own
        adjudicated result, as committed, still derives from its records."""
        if not (ATTEMPT_04 / lane.ADJUDICATED_FILE).is_file():
            self.skipTest("attempt 04 has no adjudicated result in this checkout")
        stored = lane.verify_adjudicated(self.dir)
        self.assertEqual((stored["coverage"]["targets_credited"],
                          stored["coverage"]["excluded_targets"],
                          stored["verdict"]["ruled"]), (13, ["T17"], "SUCCESSFUL"))


if __name__ == "__main__":
    unittest.main()
