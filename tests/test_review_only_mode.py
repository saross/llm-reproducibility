#!/usr/bin/env python3
"""Tests for the review-only mode (gate 1.3.2, criterion 4).

Design: ``wiki/planning/reproduction-gate-1-3-design.md``, "The review-only
mode as designed". A review-only run re-reviews an executed attempt with a
fresh reviewer and no executor. These tests pin, on a copy of attempt 04's
real records (the real attempt is never written):

1. The executor binding: the persisted executor result is carried only as
   the attempt's run audit cleared it, for the attempt as it stands; a
   changed comparison is refused (Shawn, 2026-10-13: corrections go into new
   attempts), at args-building and again at admission.
2. The staged copy: the reviewable state and the gate report, digest-equal
   to the attempt's, with the earlier review and the other post-review
   records withheld (Shawn, 2026-10-30).
3. The run audit (1.2): each role bound to its own run, the earlier audit
   kept as history, the reviewed state the review run's.
4. Persistence and adjudication across two workflow runs: the review of
   record replaced and kept as history, the new review's issues unruled
   until ruled, and the adjudicated result naming the review's run.
5. No inherited clearance: a second review-only run, and a review payload
   changed after its audit, are refused; two reviewer results in one run
   are refused as before.
6. The workflow script: its prompt lines match the lane's regexes, its
   checksum guard is the lane's, and, run under node with stub agents, it
   reviews only a staged copy.

Run: ``venv/bin/python -m pytest tests/test_review_only_mode.py -q``
"""

from __future__ import annotations

import argparse
import contextlib
import importlib.machinery
import importlib.util
import io
import json
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest import mock

REPO_ROOT = Path(__file__).resolve().parent.parent
WORKFLOW = REPO_ROOT / "reproduction-system" / "workflows" / "reproduction-review.workflow.js"
ATTEMPT_04 = (REPO_ROOT / "studies" / "open-science-compliance" / "outputs"
              / "herskind-riede-2024" / "reproduction" / "attempt-04")
SLUG = "herskind-riede-2024"
ORIGINAL_RUN = "wf_4fd7a886-ada"
COMMIT = "c" * 40


def load_script(name: str, filename: str):
    """Import a hyphen-named script as a module (test_reconcile pattern)."""
    spec = importlib.util.spec_from_loader(
        name, importlib.machinery.SourceFileLoader(
            name, str(REPO_ROOT / "scripts" / filename)))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


lane = load_script("reproduction_lane_review_only", "reproduction-lane.py")


def reviewer_record(agent_id: str, review_copy: str = "") -> dict:
    """A clean governed reviewer's agent audit, as ``audit_agent`` gives it,
    its prompt naming the staged copy it was handed."""
    return {"agent_id": agent_id, "agent_type": "adversarial-reviewer", "clean": True,
            "receipts": {"valid": True, "problems": []},
            "blinding": {"contaminating": [], "warnings": [], "noted": []},
            "writes_outside_scope": [], "launch_message": None,
            "prompt_head": f"Paper: {SLUG}\nReview copy: {review_copy}\n",
            "provenance": {"run_id": "review-only-test", "launch_commit": COMMIT,
                           "effort": "high"}}


STAGING_KEYS = lane.STAGING_KEYS


def new_review(locked: list[str], summary: str = "T02's comparison rests on one cell") -> dict:
    """A QUALIFIED v1.4 review of the copy: one concern on T02, a method row
    for every locked target."""
    return {"status": "OK", "paper_slug": SLUG, "overall": "QUALIFIED",
            "receipts": {"agent_version": "adversarial-reviewer v1.4"},
            "dimensions": {k: {"verdict": "CONCERN" if k == "quantitative_claims" else "PASS",
                               "findings": []} for k in lane.DIMENSION_KEYS},
            "verdict_challenge": {"executor_verdict": "SUCCESSFUL",
                                  "reviewer_supports_verdict": True, "rationale": "r"},
            "concerns": [{"concern_id": "C1", "dimension": "quantitative_claims",
                          "scope": "targets", "targets": ["T02"], "summary": summary,
                          "evidence": ["comparisons/comparison.json"]}],
            "method_assessment": [
                {"target_id": t, "as_planned": "yes", "aspects": [], "departure": None,
                 "outcome_affected": "no", "after_published_value": "no", "evidence": []}
                for t in locked]}


@unittest.skipUnless((ATTEMPT_04 / lane.RUN_AUDIT_FILE).is_file(),
                     "attempt 04's records are not in this checkout")
class ReviewOnlyTests(unittest.TestCase):
    """The review-only mode on a labelled copy of attempt 04."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.dir = self.root / "outputs" / SLUG / "reproduction" / "attempt-04"
        shutil.copytree(ATTEMPT_04, self.dir)
        self.config_path = self.root / "run-config.yaml"
        self.config_path.write_text(json.dumps({
            "run_id": "review-only-test", "attempt": 4, "effort": "high", "mode": "review-only",
            "output_root": str(self.root / "outputs"),
            "agents": {"planner": "reproduction-planner", "executor": "reproduction-executor",
                       "reviewer": "adversarial-reviewer"},
            "schemas": {"plan": "reproduction-system/schemas/reproduction-plan-output.json",
                        "execution":
                            "reproduction-system/schemas/reproduction-execution-output.json",
                        "review": "reproduction-system/schemas/adversarial-review-output.json",
                        "comparison_record": "reproduction-system/schemas/comparison-record.json"},
            "blinding": {"forbidden_substrings": [], "cross_paper_slugs": []},
            "papers": [{"slug": SLUG,
                        "paper_pdf": str(self.root / "vor.pdf")}]}), encoding="utf-8")
        (self.root / "vor.pdf").write_bytes(b"%PDF-1.4 stand-in\n")
        self.config = lane.load_config(self.config_path)
        self.locked = lane.locked_targets(self.dir)

    def tearDown(self):
        self.tmp.cleanup()

    # -- helpers -------------------------------------------------------------

    def stage(self, run: str) -> dict:
        """Stage the reviewer's copy for one run, as its gate step does."""
        staged = lane.stage_review(self.dir, self.root / "scratch" / run / "review")
        return {key: staged[key] for key in STAGING_KEYS}

    def audit(self, run: str, payload: dict, agent_id: str = "rev-1",
              staged: dict | None = None) -> dict:
        """Write the copy's run audit for one review-only run, as audit-run
        does, from a staging record (staged afresh unless given)."""
        staged = staged or self.stage(run)
        return lane.write_attempt_run_audit(
            self.config, run, self.dir,
            {"reviewer": (reviewer_record(agent_id, staged["review_dir"]), payload)},
            [], [staged])

    def run_dir(self, run: str, *results: tuple[str, dict]) -> Path:
        """A workflow run directory holding reviewer results in its journal."""
        path = self.root / "runs" / run
        path.mkdir(parents=True)
        prompt = (f"Adversarial review task (run review-only-test, attempt 4; review-only "
                  f"re-run).\nPaper: {SLUG}\nProvenance: run review-only-test; launch commit "
                  f"{COMMIT}; reasoning effort pinned: high.\n")
        journal = []
        for agent_id, payload in results:
            (path / f"agent-{agent_id}.meta.json").write_text(
                json.dumps({"agentType": "adversarial-reviewer"}), encoding="utf-8")
            (path / f"agent-{agent_id}.jsonl").write_text(json.dumps(
                {"message": {"role": "user", "content": prompt}}) + "\n", encoding="utf-8")
            journal.append(json.dumps({"type": "result", "agentId": agent_id,
                                       "result": payload}))
        (path / "journal.jsonl").write_text("\n".join(journal) + "\n", encoding="utf-8")
        return path

    def persist(self, run_dir: Path, force: bool = False) -> int:
        with contextlib.redirect_stdout(io.StringIO()), \
                contextlib.redirect_stderr(io.StringIO()):
            return lane.cmd_persist_results(argparse.Namespace(
                config=self.config_path, run_dir=run_dir, force=force, record_unruled=False))

    def rule_unruled(self) -> list[str]:
        """Rule every unruled issue admissible; returns their ids."""
        report = json.loads((self.dir / lane.GATE_FILE).read_text(encoding="utf-8"))
        rulings = lane.load_rulings(self.dir)
        unruled = [i["id"] for i in lane.attempt_issues(self.dir, report).values()
                   if lane.ruling_for(i, rulings) is None]
        path = self.root / "rulings.json"
        path.write_text(json.dumps([{"issue": i, "decision": "admissible",
                                     "note": "fixture: the review-only test's ruling"}
                                    for i in unruled]), encoding="utf-8")
        with contextlib.redirect_stdout(io.StringIO()):
            lane.cmd_rule_flags(argparse.Namespace(config=self.config_path, slug=SLUG,
                                                   approver="fixture", rulings=path))
        return unruled

    def binding_reasons(self, reasons: list[str]) -> list[str]:
        """Admission reasons other than unruled issues."""
        return [r for r in reasons if "unruled" not in r]

    # -- 1. the executor binding ---------------------------------------------

    def test_the_cleared_executor_is_carried(self):
        entry, payload, problems = lane.carried_executor(self.dir)
        execution = json.loads((self.dir / lane.EXECUTION_FILE).read_text(encoding="utf-8"))
        self.assertEqual(problems, [])
        self.assertTrue(entry["clean"])
        self.assertEqual((entry["workflow_run"], entry["agent_id"], entry["launch_commit"]),
                         (ORIGINAL_RUN, execution["agent_id"], execution["launch_commit"]))
        self.assertEqual(entry["cleared_state_sha256"], lane.artefact_state(self.dir))
        self.assertEqual(entry["carried_from"]["workflow_run"], ORIGINAL_RUN)
        self.assertEqual(lane.json_digest(payload), entry["payload_sha256"])

    def test_a_changed_comparison_is_refused(self):
        """The changed-comparison test: a new review cannot clear it."""
        path = self.dir / lane.COMPARISON_FILE
        doc = json.loads(path.read_text(encoding="utf-8"))
        doc["targets"][0]["outcome"] = "REPRODUCED"
        path.write_text(json.dumps(doc), encoding="utf-8")
        _, _, problems = lane.carried_executor(self.dir)
        self.assertTrue(any("corrections go into a new attempt" in p for p in problems))
        with mock.patch.object(lane, "require_committed"), \
                mock.patch.object(lane, "resolve_launch_commit", return_value=COMMIT), \
                self.assertRaisesRegex(lane.LaneError, "cannot be bound"):
            lane.cmd_build_review_args(argparse.Namespace(
                config=self.config_path, scratch_root=str(self.root / "scratch"), out=None))

    def test_a_comparison_changed_after_the_review_is_not_admitted(self):
        self.audit("wf_review-1", new_review(self.locked))
        path = self.dir / lane.COMPARISON_FILE
        path.write_text(path.read_text(encoding="utf-8") + "\n", encoding="utf-8")
        reasons = lane.run_audit_reasons(self.dir, {}, lane.load_rulings(self.dir), None)
        self.assertTrue(any("changed since the gate check" in r for r in reasons))

    def test_an_executor_the_audit_did_not_clear_is_refused(self):
        path = self.dir / lane.EXECUTION_FILE
        doc = json.loads(path.read_text(encoding="utf-8"))
        doc["payload"]["verdict"] = "PARTIAL"
        path.write_text(json.dumps(doc), encoding="utf-8")
        entry, _, problems = lane.carried_executor(self.dir)
        self.assertFalse(entry["clean"])
        self.assertTrue(any("did not clear this executor result" in p for p in problems))

    def test_the_args_bind_the_executor(self):
        out = self.root / "review-args.json"
        with mock.patch.object(lane, "require_committed"), \
                mock.patch.object(lane, "resolve_launch_commit", return_value=COMMIT), \
                contextlib.redirect_stdout(io.StringIO()):
            lane.cmd_build_review_args(argparse.Namespace(
                config=self.config_path, scratch_root=str(self.root / "scratch"), out=out))
        args = json.loads(out.read_text(encoding="utf-8"))
        paper = args["papers"][0]
        self.assertEqual(args["mode"], "review-only")
        self.assertNotIn("executor", args["agent_types"])
        self.assertEqual(paper["executor"]["workflow_run"], ORIGINAL_RUN)
        self.assertEqual(paper["review_dir"],
                         str(self.root / "scratch" / "review-only-test" / SLUG / "review"))
        self.assertEqual(len(paper["target_ids"]), 18)
        with self.assertRaisesRegex(lane.LaneError, "build-review-args"):
            lane.cmd_build_exec_args(argparse.Namespace(
                config=self.config_path, scratch_root=str(self.root / "scratch"), out=None))

    # -- 2. the staged copy --------------------------------------------------

    def test_the_review_copy_holds_the_reviewed_state_only(self):
        result = lane.stage_review(self.dir, self.root / "review")
        staged = self.root / "review"
        self.assertEqual(result["artefact_state_sha256"], lane.artefact_state(self.dir))
        self.assertEqual(lane.artefact_state(staged), lane.artefact_state(self.dir))
        self.assertTrue((staged / lane.GATE_FILE).is_file())
        self.assertTrue((staged / lane.COMPARISON_FILE).is_file())
        for name in (lane.REVIEW_FILE, lane.EXECUTION_FILE, lane.RULINGS_FILE,
                     lane.RUN_AUDIT_FILE, lane.ADJUDICATED_FILE, lane.AUDIT_FILE):
            self.assertFalse((staged / name).exists(), name)
            self.assertIn(name, result["withheld"])
        with self.assertRaisesRegex(lane.LaneError, "not empty"):
            lane.stage_review(self.dir, staged)
        with self.assertRaisesRegex(lane.LaneError, "inside the attempt"):
            lane.stage_review(self.dir, self.dir / "review")

    def test_the_attempts_withheld_records_are_blinded(self):
        """The reviewer is pointed at the copy; reading the attempt's own
        earlier review, or its history, is a blinded access, while the
        copy, and the attempt's reviewable files, are not."""
        blind = lane.Blinding(self.config, SLUG)
        review_dir = self.root / "scratch" / "review-only-test" / SLUG / "review"
        for path in (self.dir / lane.REVIEW_FILE, self.dir / lane.RULINGS_FILE,
                     self.dir / lane.ADJUDICATED_FILE,
                     self.dir / lane.SUPERSEDED_DIR / ORIGINAL_RUN / lane.REVIEW_FILE):
            self.assertIsNotNone(blind.hit(str(path)), path)
        for path in (review_dir / lane.GATE_FILE, review_dir / lane.COMPARISON_FILE,
                     self.dir / lane.GATE_FILE, self.dir / lane.COMPARISON_FILE):
            self.assertIsNone(blind.hit(str(path)), path)
        self.assertEqual(lane.blinding_args(self.config)["forbidden_substrings"],
                         lane.withheld_records(self.config))
        execute = {**self.config, "mode": "execute"}
        self.assertEqual(lane.withheld_records(execute), [])

    # -- 3 and 4. the run audit, persistence, and adjudication -----------------

    def test_a_review_only_run_is_audited_persisted_and_adjudicated(self):
        payload = new_review(self.locked)
        doc = self.audit("wf_review-1", payload)
        self.assertEqual(doc["run_audit_version"], "1.2")
        self.assertEqual(doc["missing_roles"], [])
        self.assertEqual(doc["roles"]["executor"]["workflow_run"], ORIGINAL_RUN)
        self.assertEqual(doc["roles"]["reviewer"]["workflow_run"], "wf_review-1")
        self.assertEqual(doc["roles"]["reviewer"]["launch_commit"], COMMIT)
        self.assertEqual(doc["launch_commit"], doc["roles"]["executor"]["launch_commit"])
        history = self.dir / lane.SUPERSEDED_DIR / ORIGINAL_RUN
        self.assertTrue((history / lane.RUN_AUDIT_FILE).is_file())
        # The executor's issues are derived again, with their fingerprints.
        self.assertTrue(any(i["id"].startswith("escalation:executor:")
                            for i in doc["issues"]))

        run = self.run_dir("wf_review-1", ("rev-1", payload))
        self.persist(run)
        review = json.loads((self.dir / lane.REVIEW_FILE).read_text(encoding="utf-8"))
        self.assertEqual(review["workflow_run"], "wf_review-1")
        self.assertTrue((history / lane.REVIEW_FILE).is_file())
        self.assertTrue((history / lane.ADJUDICATED_FILE).is_file())
        self.assertFalse((self.dir / lane.ADJUDICATED_FILE).exists())
        # Bound across two runs; only the new review's issues wait.
        self.assertEqual(self.binding_reasons(review["admission"]["reasons"]), [])
        self.assertFalse(review["admission"]["eligible"])
        ruled = self.rule_unruled()
        self.assertIn("review-concern:C1", ruled)
        self.persist(run, force=True)
        result = lane.adjudicate(self.dir)
        self.assertEqual(result["workflow_run"], ORIGINAL_RUN)
        self.assertEqual(result["review_run"],
                         {"run_id": "review-only-test", "workflow_run": "wf_review-1"})
        self.assertEqual(result["coverage"]["targets_enumerated"], 18)

    def test_history_is_never_overwritten(self):
        path = self.dir / "record.json"
        path.write_text("{}", encoding="utf-8")
        moved = lane.supersede(self.dir, "record.json", "wf_x")
        self.assertEqual(moved, self.dir / lane.SUPERSEDED_DIR / "wf_x" / "record.json")
        path.write_text("{}", encoding="utf-8")
        lane.supersede(self.dir, "record.json", "wf_x")
        path.write_text('{"other": 1}', encoding="utf-8")
        with self.assertRaisesRegex(lane.LaneError, "different record"):
            lane.supersede(self.dir, "record.json", "wf_x")
        # History sits outside the reviewed state.
        path.unlink()
        self.assertEqual(lane.artefact_state(self.dir), lane.artefact_state(ATTEMPT_04))

    # -- 5. no inherited clearance -------------------------------------------

    def test_a_later_review_only_run_takes_the_clearance(self):
        payload = new_review(self.locked)
        self.audit("wf_review-1", payload)
        self.audit("wf_review-2", new_review(self.locked, "another reading"), "rev-2")
        self.assertTrue((self.dir / lane.SUPERSEDED_DIR / "wf_review-1"
                         / lane.RUN_AUDIT_FILE).is_file())
        self.persist(self.run_dir("wf_review-1", ("rev-1", payload)))
        review = json.loads((self.dir / lane.REVIEW_FILE).read_text(encoding="utf-8"))
        self.assertTrue(any("wf_review-2" in r for r in review["admission"]["reasons"]))

    def test_a_review_changed_after_its_audit_is_not_admitted(self):
        self.audit("wf_review-1", new_review(self.locked))
        self.persist(self.run_dir("wf_review-1", ("rev-1", new_review(self.locked, "edited"))))
        review = json.loads((self.dir / lane.REVIEW_FILE).read_text(encoding="utf-8"))
        self.assertTrue(any("payload digest differs" in r
                            for r in review["admission"]["reasons"]))

    def test_two_reviewer_results_in_one_run_are_refused(self):
        """The reviewer-retry test: a retried result is resolved by hand."""
        payload = new_review(self.locked)
        run = self.run_dir("wf_review-1", ("rev-1", payload), ("rev-2", payload))
        with self.assertRaisesRegex(lane.LaneError, "two adversarial-reviewer results"):
            self.persist(run)

    def test_an_adjudicated_attempt_can_be_gated_again(self):
        """Found while building the mode (2026-10-30): the input-tree check
        read adjudicated-result.json as an input added after the final run,
        so re-gating any adjudicated attempt failed. The re-gate keeps every
        issue's fingerprint, so rulings carry; gate 1.3.2 has retired only
        the paper-wide method-adherence obligation."""
        execution = json.loads((self.dir / lane.EXECUTION_FILE).read_text(encoding="utf-8"))
        commit = execution["launch_commit"]
        known = subprocess.run(["git", "-C", str(REPO_ROOT), "cat-file", "-e", commit],
                               capture_output=True, timeout=30)
        if known.returncode != 0:
            self.skipTest("the original run's launch commit is not in this clone's history")
        old = json.loads((ATTEMPT_04 / lane.GATE_FILE).read_text(encoding="utf-8"))
        result = subprocess.run(
            [str(REPO_ROOT / "venv" / "bin" / "python"),
             str(REPO_ROOT / "scripts" / "reproduction-lane.py"), "check-attempt",
             str(self.dir), "--plan", str(self.dir / lane.PLAN_FILE),
             "--launch-commit", commit, "--out", "-"],
            capture_output=True, text=True, timeout=600, cwd=REPO_ROOT)
        report = json.loads(result.stdout)
        self.assertEqual((report["verdict"], report["errors"]), ("pass", []), result.stderr)
        fresh = {i["id"]: i["fingerprint"] for i in report["issues"]}
        before = {i["id"]: i["fingerprint"] for i in old["issues"]}
        self.assertEqual(set(before) - set(fresh), {"method-adherence:targets"})
        self.assertEqual({k: before[k] for k in fresh}, fresh)

    # -- Astra's review of PR #15 (2026-10-30) -------------------------------

    def test_a_later_review_cannot_relabel_the_executors_cleared_state(self):
        """F1: the executor was cleared for state A. A review audit that
        records state B, followed by the attempt becoming B, must not leave
        the executor cleared for B."""
        original = lane.artefact_state(self.dir)
        staged = self.stage("wf_review-1")
        path = self.dir / lane.COMPARISON_FILE
        body = path.read_bytes()
        self.audit("wf_review-1", new_review(self.locked),
                   staged={**staged, "artefact_state_sha256": "b" * 64})
        audit = json.loads((self.dir / lane.RUN_AUDIT_FILE).read_text(encoding="utf-8"))
        self.assertEqual(audit["roles"]["executor"]["cleared_state_sha256"], original)
        path.write_bytes(body + b"\n")
        entry, _, problems = lane.carried_executor(self.dir)
        self.assertEqual(entry["cleared_state_sha256"], original)
        self.assertFalse(entry["clean"])
        self.assertTrue(any("corrections go into a new attempt" in p for p in problems))

    def test_a_fresh_reviewer_meets_no_earlier_rulings(self):
        """F2: identical review content from another run's reviewer is new
        to rule; a re-audit of the same run keeps its rulings, and the
        executor's issues keep theirs."""
        payload = new_review(self.locked)
        staged = self.stage("wf_review-1")
        first = self.audit("wf_review-1", payload, staged=staged)
        rulings = [{"issue_id": i["id"], "fingerprint": i["fingerprint"]}
                   for i in first["issues"]]
        again = self.audit("wf_review-1", payload, staged=staged)
        self.assertEqual([i["fingerprint"] for i in again["issues"]],
                         [i["fingerprint"] for i in first["issues"]])
        second = self.audit("wf_review-2", json.loads(json.dumps(payload)), "rev-2")
        inherited = sorted(i["id"] for i in second["issues"] if lane.ruling_for(i, rulings))
        # Only the executor's issues, and its own run's launch message, carry.
        self.assertTrue(inherited)
        self.assertTrue(all(":executor:" in i or (i.startswith("launch-message:") and "@" not in i)
                            for i in inherited), inherited)
        for issue in ("review-concern:C1", "review:qualified"):
            self.assertIn(issue, {i["id"] for i in second["issues"]})
            self.assertNotIn(issue, inherited)

    def test_the_staged_copy_must_be_unchanged_and_the_one_reviewed(self):
        """F3: a staged copy changed after staging, a reviewer handed another
        copy, a copy no longer there, and a run with no successful staging
        are each refused; the staged state alone is the reviewed state."""
        staged = self.stage("wf_review-1")
        copy = Path(staged["review_dir"])
        doc = json.loads((copy / lane.COMPARISON_FILE).read_text(encoding="utf-8"))
        doc["targets"][0]["outcome"] = "BLOCKED"
        (copy / lane.COMPARISON_FILE).write_text(json.dumps(doc), encoding="utf-8")
        audit = self.audit("wf_review-1", new_review(self.locked), staged=staged)
        self.assertFalse(audit["staging"]["verified"])
        reasons = lane.run_audit_reasons(self.dir, {}, [], None)
        self.assertTrue(any("staged copy changed" in r for r in reasons), reasons)
        shutil.rmtree(copy)
        self.assertIn("the staged copy is gone, so it cannot be shown unchanged",
                      lane.verify_staging([staged], f"Review copy: {staged['review_dir']}")[
                          "problems"])
        other = self.stage("wf_review-2")
        result = lane.verify_staging([other], "Review copy: /elsewhere/review")
        self.assertIn("the reviewer's prompt does not name the staged copy", result["problems"])
        self.assertIn("no successful stage-review record", lane.verify_staging([], "")["problems"])
        self.assertTrue(lane.verify_staging([other, dict(other)],
                                            f"Review copy: {other['review_dir']}")["verified"])

    def test_a_re_audit_keeps_its_verification_once_the_copy_is_gone(self):
        """A side agent's note on F3: deleting the scratch copy after the first
        audit must not undo the result; a re-audit of the same run keeps that
        run's verification of the same record. Another run, a changed record,
        or a copy present but changed do not."""
        staged = self.stage("wf_review-1")
        first = self.audit("wf_review-1", new_review(self.locked), staged=staged)
        self.assertTrue(first["staging"]["verified"])
        shutil.rmtree(staged["review_dir"])
        again = self.audit("wf_review-1", new_review(self.locked), staged=staged)
        self.assertTrue(again["staging"]["verified"])
        self.assertEqual(again["staging"]["verified_at"], first["staging"]["verified_at"])
        self.assertFalse(any("staged copy" in r
                             for r in lane.run_audit_reasons(self.dir, {}, [], None)))
        moved = {**staged, "gate_report_sha256": "0" * 64}
        self.assertFalse(self.audit("wf_review-1", new_review(self.locked),
                                    staged=moved)["staging"]["verified"])
        other = self.audit("wf_review-2", new_review(self.locked), "rev-2", staged=staged)
        self.assertEqual(other["staging"]["problems"], [lane.STAGED_COPY_GONE])

    def test_staging_is_read_only_from_a_successful_stage_review(self):
        """F3: a failed stage-review never falls back to a check-attempt digest."""
        run = self.root / "runs" / "wf_gate"
        run.mkdir(parents=True)
        staged = self.stage("wf_gate")

        def call(n: int, command: str, output: str, error: bool) -> list[dict]:
            return [{"message": {"role": "assistant", "content": [
                        {"type": "tool_use", "id": f"g{n}", "name": "Bash",
                         "input": {"command": command}}]}},
                    {"message": {"role": "user", "content": [
                        {"type": "tool_result", "tool_use_id": f"g{n}", "content": output,
                         "is_error": error}]}}]
        state = '{"artefact_state_sha256": "' + "a" * 64 + '"}'
        entries = [{"message": {"role": "user", "content": f"Paper: {SLUG}\n"}}]
        entries += call(1, "reproduction-lane.py check-attempt x", state, False)
        entries += call(2, "reproduction-lane.py stage-review x --to y", "error: not empty",
                        True)
        (run / "agent-g.meta.json").write_text(json.dumps({"agentType": "general-purpose"}),
                                               encoding="utf-8")
        (run / "agent-g.jsonl").write_text("\n".join(json.dumps(e) for e in entries) + "\n",
                                           encoding="utf-8")
        self.assertEqual(lane.staging_records(run, self.config), {})
        entries += call(3, "reproduction-lane.py stage-review x --to y", json.dumps(staged),
                        False)
        (run / "agent-g.jsonl").write_text("\n".join(json.dumps(e) for e in entries) + "\n",
                                           encoding="utf-8")
        self.assertEqual(lane.staging_records(run, self.config), {SLUG: [staged]})

    def test_an_executor_persisted_ineligible_is_refused_before_any_spend(self):
        """F4: review-only persistence never re-persists the executor, so an
        executor record persisted ineligible is refused at args-building."""
        path = self.dir / lane.EXECUTION_FILE
        doc = json.loads(path.read_text(encoding="utf-8"))
        doc["admission"]["eligible"] = False
        path.write_text(json.dumps(doc), encoding="utf-8")
        with mock.patch.object(lane, "require_committed"), \
                mock.patch.object(lane, "resolve_launch_commit", return_value=COMMIT), \
                self.assertRaisesRegex(lane.LaneError, "persisted ineligible"):
            lane.cmd_build_review_args(argparse.Namespace(
                config=self.config_path, scratch_root=str(self.root / "scratch"), out=None))

    def test_a_1_1_audit_binds_both_roles_to_its_run(self):
        audit = json.loads((ATTEMPT_04 / lane.RUN_AUDIT_FILE).read_text(encoding="utf-8"))
        self.assertEqual(audit["run_audit_version"], "1.1")
        for role in ("executor", "reviewer"):
            self.assertEqual(lane.role_identity(audit, role)["workflow_run"], ORIGINAL_RUN)


class ReviewWorkflowTests(unittest.TestCase):
    """The review-only workflow script against the lane's contracts."""

    SOURCE = WORKFLOW.read_text(encoding="utf-8")

    def test_prompt_lines_match_the_lane(self):
        line = next(r for r in self.SOURCE.splitlines() if "`Provenance: run" in r)
        rendered = line[line.index("`") + 1:line.rindex("`")]
        rendered = rendered.replace("${run_id}", "r").replace("${launch_commit}", COMMIT) \
            .replace("${effort}", "high")
        self.assertIsNotNone(lane.PROVENANCE_RE.search(rendered))
        self.assertIn("`Paper: ${p.slug}\\n`", self.SOURCE)
        # The reviewer is granted no write root, and the gate checks the
        # executor's commit, against which its sealed records were made.
        self.assertNotIn("Attempt directory:", self.SOURCE)
        self.assertIn("--launch-commit ${p.executor.launch_commit}", self.SOURCE)
        self.assertIn("stage-review ${p.attempt_dir} --to ${p.review_dir}", self.SOURCE)

    def node(self, script: str) -> subprocess.CompletedProcess:
        if shutil.which("node") is None:
            self.skipTest("node not installed")
        return subprocess.run(["node", "-e", script], capture_output=True, text=True,
                              timeout=60)

    def test_the_checksum_guard_is_the_lanes(self):
        payload = {"mode": "review-only", "papers": [{"note": "ü & 'q' \"x\" \\ \n 🦴"}]}
        block = self.SOURCE[self.SOURCE.index("const { args_checksum, ...UNSUMMED } = ARGS"):
                            self.SOURCE.index("if (COMPUTED !== args_checksum)")]
        result = self.node(f"const ARGS = {json.dumps(dict(payload, args_checksum='x'))};\n"
                           f"{block}\nprocess.stdout.write(COMPUTED)")
        self.assertEqual(result.stdout, lane.args_checksum(payload), result.stderr)

    def dry_run(self, staged: bool) -> dict:
        """Run the workflow under node with stub agents; returns its result
        and the prompts each phase was given."""
        paper = {"slug": SLUG, "attempt": 4, "attempt_dir": "/repo/a/attempt-04",
                 "plan_path": "/repo/a/attempt-04/reproduction-plan.json",
                 "plan_sha256": "p" * 64, "approval_path": "/repo/a/attempt-04/x.json",
                 "target_ids": ["T01", "T02"], "paper_pdf": "/c/vor.pdf",
                 "paper_pdf_sha256": "f" * 64, "supplements": [], "deposits": [],
                 "run_notes": "", "image_tag": "llmr-x", "review_dir": "/s/review",
                 "executor": {"run_id": "r0", "workflow_run": ORIGINAL_RUN, "agent_id": "e1",
                              "payload_sha256": "d" * 64, "launch_commit": "e" * 40}}
        args = {"mode": "review-only", "run_id": "r1", "attempt": 4, "effort": "high",
                "launch_commit": COMMIT, "agent_types": {"reviewer": "adversarial-reviewer"},
                "receipt_keys": {"reviewer": ["framework"]}, "rulings": [],
                "schemas": {"review": {"type": "object"}}, "repo_root": "/repo",
                "blinding": {"forbidden_substrings": ["wiki/"], "cross_paper_slugs": []},
                "papers": [paper], "skipped": []}
        args["args_checksum"] = lane.args_checksum(args)
        body = self.SOURCE.replace("export const meta", "const meta")
        gate = {"slug": SLUG, "exit_code": 0, "verdict": "pass", "report_path": "r",
                "errors": [], "warnings": [], "flags": [], "staged": staged,
                "artefact_state_sha256": "s" * 64 if staged else ""}
        review = {"status": "OK", "overall": "QUALIFIED", "paper_slug": SLUG}
        script = f"""
const args = {json.dumps(args)};
const calls = [];
const log = () => {{}};
async function agent(prompt, opts) {{
  calls.push({{phase: opts.phase, agentType: opts.agentType, prompt}});
  return opts.phase === 'Gate' ? {json.dumps(gate)} : {json.dumps(review)};
}}
async function pipeline(items, ...stages) {{
  return Promise.all(items.map(async item => {{
    let value = await stages[0](item);
    for (const stage of stages.slice(1)) value = await stage(value, item);
    return value;
  }}));
}}
(async () => {{
  const result = await (async () => {{ {body} }})();
  process.stdout.write(JSON.stringify({{result, calls}}));
}})().catch(e => {{ process.stderr.write(String(e)); process.exit(1); }});
"""
        out = self.node(script)
        self.assertEqual(out.returncode, 0, out.stderr)
        return json.loads(out.stdout)

    def test_the_reviewer_reads_only_the_staged_copy(self):
        run = self.dry_run(staged=True)
        phases = [c["phase"] for c in run["calls"]]
        self.assertEqual(phases, ["Gate", "Review"])
        prompt = run["calls"][1]["prompt"]
        self.assertIn("/s/review/reproduction-plan.json", prompt)
        self.assertIn(f"workflow run {ORIGINAL_RUN}", prompt)
        self.assertEqual(lane.REVIEW_COPY_RE.search(prompt).group(1), "/s/review")
        self.assertNotIn("/repo/a/attempt-04", prompt)
        self.assertIsNotNone(lane.PROVENANCE_RE.search(prompt))
        self.assertIn("--launch-commit " + "e" * 40, run["calls"][0]["prompt"])
        self.assertEqual(run["result"]["summary"][0]["review"], "QUALIFIED")

    def test_nothing_is_reviewed_without_a_staged_copy(self):
        run = self.dry_run(staged=False)
        self.assertEqual([c["phase"] for c in run["calls"]], ["Gate"])
        self.assertTrue(any("not staged" in item for item in run["result"]["human_queue"]))


if __name__ == "__main__":
    unittest.main()
