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


if __name__ == "__main__":
    unittest.main()
