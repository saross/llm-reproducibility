#!/usr/bin/env python3
"""Unit tests for the reproduction-lane orchestration helpers (v1.0).

``scripts/reproduction-lane.py`` carries every check the reproduction
workflows cannot make themselves (workflow scripts have no filesystem
access). These tests pin:

1. The cross-file format contracts: the prompt lines in
   ``reproduction-system/workflows/*.workflow.js`` are the single source of
   truth for the tool's PROVENANCE_RE, PAPER_RE, SCRATCH_RE, and
   ATTEMPT_DIR_RE — each template is extracted from the workflow source and
   matched against the live regex, so an edit to one side alone fails here.
2. The artefact gate (``check_attempt``): invariant 3's one-to-one target
   match, recomputed coverage, the BLOCKED rule, the corpus rule, and
   required artefacts.
3. Plan-level checks, result binding, the approval hash lock, and the
   review overall-verdict rule.
4. The audit: per-request token deduplication, pricing, and blinded-path
   detection across Read and Bash (URL paths excluded).
5. The args checksum: the workflows' own JavaScript, run in Node, agrees
   with the Python builder (skipped when Node is absent).

Run: ``venv/bin/python -m pytest tests/test_reproduction_lane.py -q``
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.machinery
import importlib.util
import json
import re
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
WORKFLOWS = REPO_ROOT / "reproduction-system" / "workflows"
COMPARISON_SCHEMA = REPO_ROOT / "reproduction-system" / "schemas" / "comparison-record.json"


def load_script(name: str, filename: str):
    """Import a hyphen-named script as a module (test_reconcile pattern)."""
    spec = importlib.util.spec_from_loader(
        name, importlib.machinery.SourceFileLoader(
            name, str(REPO_ROOT / "scripts" / filename)))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


lane = load_script("reproduction_lane", "reproduction-lane.py")

DUMMY_COMMIT = "a" * 40


def render_template(workflow: str, marker: str) -> str:
    """Extract the backtick template containing ``marker`` from a workflow
    source and substitute dummy values for its ``${...}`` slots."""
    source = (WORKFLOWS / workflow).read_text(encoding="utf-8")
    line = next(row for row in source.splitlines() if marker in row and "`" in row)
    template = line[line.index("`") + 1:line.rindex("`")]
    values = {"run_id": "run-x", "launch_commit": DUMMY_COMMIT, "effort": "high",
              "p.slug": "some-paper-2024", "p.scratch_dir": "/tmp/scratch/planner",
              "p.executor_scratch_dir": "/tmp/scratch/executor",
              "p.attempt_dir": "/repo/outputs/some-paper-2024/reproduction/attempt-02"}
    return re.sub(r"\$\{([^}]+)\}", lambda m: values.get(m.group(1), "X"), template)


def plan_record(target_ids: list[str], slug: str = "some-paper-2024") -> dict:
    """A minimal persisted plan record with the given target ids."""
    return {"plan_record_version": "1.0", "plan": {
        "status": "OK", "paper_slug": slug,
        "verification_targets": [{"target_id": t} for t in target_ids]}}


def write(path: Path, text: str = "x\n") -> None:
    """Create a file (and parents) with content."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


class FormatContracts(unittest.TestCase):
    """Workflow prompt lines must match the tool's regexes."""

    def test_provenance_line_both_workflows(self):
        for workflow in ("reproduction-plan.workflow.js",
                         "reproduction-execute.workflow.js"):
            rendered = render_template(workflow, "Provenance: run")
            match = lane.PROVENANCE_RE.search(rendered)
            self.assertIsNotNone(match, workflow)
            self.assertEqual(match.group(2), DUMMY_COMMIT)
            self.assertEqual(match.group(3), "high")

    def test_paper_line(self):
        for workflow in ("reproduction-plan.workflow.js",
                         "reproduction-execute.workflow.js"):
            rendered = render_template(workflow, "`Paper: ${p.slug}")
            self.assertEqual(lane.PAPER_RE.search(rendered.replace("\\n", "\n")).group(1),
                             "some-paper-2024")

    def test_scratch_and_attempt_lines(self):
        rendered = render_template("reproduction-plan.workflow.js", "Scratch directory:")
        self.assertIsNotNone(lane.SCRATCH_RE.search(rendered.replace("\\n", "\n")))
        rendered = render_template("reproduction-execute.workflow.js", "`Attempt directory:")
        self.assertIsNotNone(lane.ATTEMPT_DIR_RE.search(rendered.replace("\\n", "\n")))

    def test_harness_wrapped_prompt(self):
        # Claude Code 2.1.288 wraps a workflow prompt: a relayed user request,
        # then the computed task with every line indented two spaces.
        relay = "[Workflow harness — user request] relayed:\n  please go"
        task = ("[Workflow harness — computed task] The computed task text follows:\n"
                "  Reproduction-lane planning task (run r, attempt 2).\n"
                "  Paper: a-2024\n"
                f"  Provenance: run r; launch commit {DUMMY_COMMIT}; "
                "reasoning effort pinned: high.\n"
                "  Scratch directory: /tmp/s\n")
        lines = [json.dumps({"message": {"role": "user", "content": relay}}),
                 json.dumps({"message": {"role": "user", "content": task}}),
                 json.dumps({"message": {"role": "assistant", "content": [
                     {"type": "text", "text": "Paper: other-2024"}]}})]
        prompt = lane.first_user_text(lines)
        self.assertEqual(lane.PAPER_RE.search(prompt).group(1), "a-2024")
        self.assertEqual(lane.PROVENANCE_RE.search(prompt).group(3), "high")
        self.assertEqual(lane.SCRATCH_RE.search(prompt).group(1), "/tmp/s")

    def test_planner_prompt_grants_no_write_root(self):
        # The planner must not get an "Attempt directory:" line — the audit
        # would read it as a permitted write root.
        source = (WORKFLOWS / "reproduction-plan.workflow.js").read_text(encoding="utf-8")
        self.assertNotIn("`Attempt directory:", source)


class GateTests(unittest.TestCase):
    """check_attempt(): the deterministic artefact gate."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self.tmp.name) / "attempt-02"
        for rel in ("Dockerfile", "environment.md", "log.md", "run-analysis.R",
                    "comparisons/comparison-report.md", "outputs/values.csv"):
            write(self.dir / rel)
        self.plan = Path(self.tmp.name) / "reproduction-plan.json"
        self.plan.write_text(json.dumps(plan_record(["T01", "T02"])), encoding="utf-8")
        self.schema = json.loads(COMPARISON_SCHEMA.read_text(encoding="utf-8"))

    def tearDown(self):
        self.tmp.cleanup()

    def comparison(self, **overrides) -> dict:
        record = {"schema_version": "1.0", "paper_slug": "some-paper-2024", "attempt": 2,
                  "plan_sha256": hashlib.sha256(self.plan.read_bytes()).hexdigest(),
                  "verdict": "SUCCESSFUL",
                  "targets": [
                      {"target_id": "T01", "outcome": "EXACT_MATCH", "testable": True,
                       "values_compared": 3, "values_matched": 3, "evidence": "procedure"},
                      {"target_id": "T02", "outcome": "WITHIN_PRECISION", "testable": True,
                       "values_compared": 1, "values_matched": 1, "evidence": "procedure"}],
                  "coverage": {"targets_enumerated": 2, "targets_reproduced": 2}}
        record.update(overrides)
        write(self.dir / "comparisons" / "comparison.json", json.dumps(record))
        return record

    def run_gate(self, **kwargs) -> dict:
        return lane.check_attempt(self.dir, self.plan, self.schema, **kwargs)

    def test_clean_attempt_passes(self):
        self.comparison()
        report = self.run_gate()
        self.assertEqual(report["verdict"], "pass", report["errors"])
        self.assertEqual(report["coverage"]["coverage_fraction"], 1.0)

    def test_missing_locked_target_fails(self):
        record = self.comparison()
        record["targets"] = record["targets"][:1]
        record["coverage"] = {"targets_enumerated": 2, "targets_reproduced": 1}
        write(self.dir / "comparisons" / "comparison.json", json.dumps(record))
        report = self.run_gate()
        self.assertEqual(report["verdict"], "fail")
        self.assertTrue(any("invariant 3" in e for e in report["errors"]))

    def test_extra_target_fails(self):
        record = self.comparison()
        record["targets"].append(dict(record["targets"][0], target_id="T99"))
        write(self.dir / "comparisons" / "comparison.json", json.dumps(record))
        self.assertTrue(any("not in the locked plan" in e
                            for e in self.run_gate()["errors"]))

    def test_declared_coverage_must_match_recomputed(self):
        record = self.comparison()
        record["targets"][1]["outcome"] = "MINOR_DISCREPANCY"  # outside tolerance
        write(self.dir / "comparisons" / "comparison.json", json.dumps(record))
        report = self.run_gate()
        self.assertEqual(report["coverage"]["targets_reproduced"], 1)
        self.assertTrue(any("recomputed" in e for e in report["errors"]))

    def test_blocked_scores_zero(self):
        self.comparison(verdict="BLOCKED")
        self.assertTrue(any("BLOCKED" in e for e in self.run_gate()["errors"]))

    def test_untestable_needs_failure_mode(self):
        record = self.comparison()
        record["targets"][1].update(testable=False, outcome="CANNOT_COMPARE")
        record["coverage"] = {"targets_enumerated": 2, "targets_reproduced": 1}
        write(self.dir / "comparisons" / "comparison.json", json.dumps(record))
        self.assertTrue(any("failure_mode" in e for e in self.run_gate()["errors"]))

    def test_plan_hash_mismatch_fails(self):
        self.comparison(plan_sha256="0" * 64)
        self.assertTrue(any("plan_sha256" in e for e in self.run_gate()["errors"]))

    def test_publisher_file_inside_attempt_fails(self):
        self.comparison()
        write(self.dir / "materials" / "paper.pdf", "publisher bytes")
        digest = hashlib.sha256(b"publisher bytes").hexdigest()
        report = self.run_gate(forbid_sha256=(digest,))
        self.assertTrue(any("publisher file" in e for e in report["errors"]))

    def test_missing_artefacts_fail(self):
        self.comparison()
        (self.dir / "log.md").unlink()
        self.assertTrue(any("log.md" in e for e in self.run_gate()["errors"]))


class PlanAndBindingTests(unittest.TestCase):
    """plan_checks(), select_results(), expected_overall()."""

    def test_plan_checks(self):
        plan = {"status": "OK", "paper": {"title": "t", "doi": "d"},
                "reproduction_type": {"types": ["C"], "rationale": "r"},
                "materials": [{}], "environment": {"x": 1}, "execution_steps": [{}],
                "verification_targets": [{"target_id": "T01"}, {"target_id": "T01"}],
                "enumeration_check": {"targets_enumerated": 3, "items_excluded": 0,
                                      "display_items_detected": 9,
                                      "flag_for_human": False},
                "eligibility": {"within_compute_cap": True}, "exclusions": []}
        errors, warnings = lane.plan_checks(plan)
        self.assertTrue(any("duplicate target ids" in e for e in errors))
        self.assertTrue(any("targets_enumerated" in e for e in errors))
        self.assertTrue(any("enumeration may be incomplete" in w for w in warnings))

    def test_escalate_needs_reason(self):
        errors, _ = lane.plan_checks({"status": "ESCALATE", "escalate_reason": " "})
        self.assertEqual(errors, ["ESCALATE without escalate_reason"])

    def test_select_results_binding(self):
        config = {"papers": [{"slug": "a-2024"}, {"slug": "b-2024"}]}
        good = {"agent_id": "1", "agent_type": "reproduction-planner",
                "result": {"paper_slug": "a-2024"}, "prompt": "x\nPaper: a-2024\ny"}
        dead = {"agent_id": "2", "agent_type": "reproduction-planner", "result": None,
                "prompt": "Paper: b-2024"}
        chosen, dead_slugs = lane.select_results([good, dead], "reproduction-planner", config)
        self.assertEqual(list(chosen), ["a-2024"])
        self.assertEqual(dead_slugs, ["b-2024"])
        swapped = dict(good, prompt="Paper: b-2024")
        with self.assertRaises(lane.LaneError):
            lane.select_results([swapped], "reproduction-planner", config)

    def test_expected_overall(self):
        dims = {k: {"verdict": "PASS", "findings": []} for k in lane.DIMENSION_KEYS}
        self.assertEqual(lane.expected_overall({"dimensions": dims}), "CONFIRMED")
        dims["provenance"]["verdict"] = "CONCERN"
        self.assertEqual(lane.expected_overall({"dimensions": dims}), "QUALIFIED")
        for key in ("scope_completeness", "confirmation_bias"):
            dims[key]["verdict"] = "CONCERN"
        self.assertEqual(lane.expected_overall({"dimensions": dims}), "CHALLENGED")


class ApprovalLockTests(unittest.TestCase):
    """approve binds to the plan hash; a changed plan cannot be executed."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        self.config_path = root / "run-config.yaml"
        pdf = root / "paper.pdf"
        pdf.write_bytes(b"%PDF fake")
        self.config_path.write_text(json.dumps({
            "run_id": "t", "attempt": 2, "effort": "high", "output_root": str(root),
            "agents": {"planner": "reproduction-planner",
                       "executor": "reproduction-executor",
                       "reviewer": "adversarial-reviewer"},
            "schemas": {"plan": "reproduction-system/schemas/reproduction-plan-output.json",
                        "execution":
                            "reproduction-system/schemas/reproduction-execution-output.json",
                        "review": "reproduction-system/schemas/adversarial-review-output.json",
                        "comparison_record": str(COMPARISON_SCHEMA)},
            "blinding": {"forbidden_substrings": []},
            "papers": [{"slug": "a-2024", "paper_pdf": str(pdf)}]}), encoding="utf-8")
        self.plan_path = root / "a-2024" / "reproduction" / "attempt-02" / lane.PLAN_FILE
        write(self.plan_path, json.dumps(plan_record(["T01"], slug="a-2024")))
        self._real_commit = lane.resolve_launch_commit
        lane.resolve_launch_commit = lambda: DUMMY_COMMIT

    def tearDown(self):
        lane.resolve_launch_commit = self._real_commit
        self.tmp.cleanup()

    def approve(self, **overrides):
        args = argparse.Namespace(config=self.config_path, slug="a-2024", decision="approve",
                                  approver="Tester", note="", force=False)
        vars(args).update(overrides)
        return lane.cmd_approve(args)

    def test_approval_records_hash_and_locks(self):
        self.assertEqual(self.approve(), 0)
        record = json.loads((self.plan_path.parent / lane.APPROVAL_FILE).read_text())
        self.assertEqual(record["plan_sha256"],
                         hashlib.sha256(self.plan_path.read_bytes()).hexdigest())
        self.assertEqual(record["locked_target_ids"], ["T01"])
        with self.assertRaises(lane.LaneError):
            self.approve()  # an approved plan is locked

    def test_changed_plan_refused_at_execute(self):
        self.approve()
        write(self.plan_path, json.dumps(plan_record(["T01", "T02"], slug="a-2024")))
        args = argparse.Namespace(config=self.config_path, scratch_root=self.tmp.name,
                                  out=None)
        with self.assertRaisesRegex(lane.LaneError, "changed after approval"):
            lane.cmd_build_exec_args(args)


def transcript(*entries: dict) -> list[str]:
    """Serialise transcript entries as JSONL lines."""
    return [json.dumps(e) for e in entries]


class ResultRecoveryTests(unittest.TestCase):
    """Transcript fallback for results, and the args checksum."""

    def test_structured_output_takes_last_accepted_call(self):
        lines = transcript(
            {"message": {"role": "assistant", "content": [
                {"type": "tool_use", "id": "s1", "name": "StructuredOutput",
                 "input": {"paper_slug": "rejected"}}]}},
            {"message": {"role": "user", "content": [
                {"type": "tool_result", "tool_use_id": "s1", "is_error": True,
                 "content": "schema violation"}]}},
            {"message": {"role": "assistant", "content": [
                {"type": "tool_use", "id": "s2", "name": "StructuredOutput",
                 "input": {"paper_slug": "accepted"}}]}},
            {"message": {"role": "user", "content": [
                {"type": "tool_result", "tool_use_id": "s2", "content": "ok"}]}})
        self.assertEqual(lane.structured_output(lines), {"paper_slug": "accepted"})

    def test_journal_results_falls_back_to_transcripts(self):
        with tempfile.TemporaryDirectory() as tmp:
            run_dir = Path(tmp)
            (run_dir / "agent-x1.meta.json").write_text(
                json.dumps({"agentType": "reproduction-planner"}))
            (run_dir / "agent-x1.jsonl").write_text("\n".join(transcript(
                {"message": {"role": "user", "content": "task\nPaper: a-2024\n"}},
                {"message": {"role": "assistant", "content": [
                    {"type": "tool_use", "id": "s1", "name": "StructuredOutput",
                     "input": {"paper_slug": "a-2024", "status": "OK"}}]}},
                {"message": {"role": "user", "content": [
                    {"type": "tool_result", "tool_use_id": "s1", "content": "ok"}]}})))
            results = lane.journal_results(run_dir)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["source"], "transcript")
        self.assertEqual(results[0]["result"]["paper_slug"], "a-2024")
        self.assertEqual(lane.PAPER_RE.search(results[0]["prompt"]).group(1), "a-2024")

    def test_args_checksum_matches_workflow_javascript(self):
        """The workflows' own checksum code, run in Node, agrees with Python."""
        if shutil.which("node") is None:
            self.skipTest("node not installed")
        payload = {"run_id": "r", "attempt": 2, "flag": True, "none": None,
                   "papers": [{"sha256": "f" * 64, "note": "ü & 'q' \"x\" \\ \n 🦴",
                               "n": [0, 1, -3]}]}
        expected = lane.args_checksum(payload)
        for workflow in ("reproduction-plan.workflow.js", "reproduction-execute.workflow.js"):
            source = (WORKFLOWS / workflow).read_text(encoding="utf-8")
            block = source[source.index("const { args_checksum, ...UNSUMMED } = ARGS"):
                           source.index("if (COMPUTED !== args_checksum)")]
            script = (f"const ARGS = {json.dumps(dict(payload, args_checksum='x'))};\n"
                      f"{block}\nprocess.stdout.write(COMPUTED)")
            result = subprocess.run(["node", "-e", script], capture_output=True, text=True,
                                    timeout=30)
            self.assertEqual(result.stdout, expected, (workflow, result.stderr))

    def test_args_checksum_rejects_floats(self):
        with self.assertRaises(lane.LaneError):
            lane.args_checksum({"x": 1.0})

    def test_emit_args_stamps_checksum_last(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "args.json"
            lane.emit_args({"run_id": "r", "args_checksum": "stale"}, out)
            written = json.loads(out.read_text(encoding="utf-8"))
        self.assertEqual(list(written), ["run_id", "args_checksum"])
        self.assertEqual(written["args_checksum"], lane.args_checksum({"run_id": "r"}))

class AuditTests(unittest.TestCase):
    """Token deduplication, pricing, and blinded-path detection."""

    def test_usage_counted_once_per_request(self):
        usage = {"input_tokens": 10, "cache_creation_input_tokens": 1000,
                 "cache_read_input_tokens": 5000,
                 "cache_creation": {"ephemeral_5m_input_tokens": 600,
                                    "ephemeral_1h_input_tokens": 400}}
        lines = transcript(
            {"requestId": "r1", "message": {"model": "claude-opus-5-5",
                                            "usage": dict(usage, output_tokens=3)}},
            {"requestId": "r1", "message": {"model": "claude-opus-5-5",
                                            "usage": dict(usage, output_tokens=250)}},
            {"requestId": "r2", "message": {"model": "<synthetic>",
                                            "usage": dict(usage, output_tokens=7)}})
        totals = lane.transcript_usage(lines)
        self.assertEqual(totals["requests"], 2)
        self.assertEqual(totals["cache_creation_input_tokens"], 2000)
        self.assertEqual(totals["cache_write_1h"], 800)
        self.assertEqual(totals["output_tokens"], 257)
        self.assertEqual(totals["models"], ["claude-opus-5-5"])

    def test_pricing_strips_date_suffix_and_refuses_unknown(self):
        pricing = {"claude-haiku-4-5": {"input": 1.0, "output": 5.0, "cache_write_5m": 1.25,
                                        "cache_write_1h": 2.0, "cache_read": 0.1}}
        usage = {"models": ["claude-haiku-4-5-20251001"], "input_tokens": 1_000_000,
                 "output_tokens": 0, "cache_write_5m": 0, "cache_write_1h": 0,
                 "cache_read_input_tokens": 0}
        self.assertEqual(lane.price_usage(usage, pricing), 1.0)
        self.assertIsNone(lane.price_usage(dict(usage, models=["mystery"]), pricing))

    def test_blinding_rules(self):
        config = {"blinding": {"forbidden_substrings": ["reproduction/attempt-01", "wiki/"],
                               "exempt_regex": r"/tool-results/hook-[0-9a-f-]+-\d+-"
                                               r"additionalContext\.txt$",
                               "cross_paper_slugs": ["a-2024", "b-2024"]}}
        blind = lane.Blinding(config, "a-2024")
        self.assertIsNotNone(blind.hit("outputs/a-2024/reproduction/attempt-01/log.md"))
        self.assertIsNotNone(blind.hit("outputs/b-2024/reproduction/attempt-02/log.md"))
        self.assertIsNone(blind.hit("outputs/a-2024/reproduction/attempt-02/log.md"))
        self.assertIsNone(blind.hit("~/.claude/projects/x/tool-results/"
                                    "hook-ab12-3-additionalContext.txt"))

    def test_url_paths_are_not_local_accesses(self):
        tokens = lane.path_tokens("curl -sL https://en.wikipedia.org/wiki/PMI "
                                  "&& cat /repo/wiki/continuity.md")
        self.assertEqual(tokens, ["/repo/wiki/continuity.md"])

    def test_audit_flags_blinded_read_and_bash(self):
        config = {"run_id": "t", "effort": "high",
                  "agents": {"planner": "reproduction-planner",
                             "executor": "reproduction-executor",
                             "reviewer": "adversarial-reviewer"},
                  "schemas": {}, "pricing_usd_per_mtok": {},
                  "blinding": {"forbidden_substrings": ["reproduction/attempt-01"],
                               "cross_paper_slugs": []}}
        prompt = ("Mechanical task\nPaper: a-2024\n"
                  "Attempt directory: /repo/out/a-2024/reproduction/attempt-02\n")
        lines = transcript(
            {"message": {"role": "user", "content": prompt}},
            {"message": {"role": "assistant", "content": [
                {"type": "tool_use", "id": "u1", "name": "Read",
                 "input": {"file_path": "/x/a-2024/reproduction/attempt-01/log.md"}},
                {"type": "tool_use", "id": "u2", "name": "Bash",
                 "input": {"command": "curl https://x.org/reproduction/attempt-01/z"}},
                {"type": "tool_use", "id": "u3", "name": "Write",
                 "input": {"file_path": "/elsewhere/notes.md", "content": "x"}}]}},
            {"message": {"role": "user", "content": [
                {"type": "tool_result", "tool_use_id": "u1", "content": "text"},
                {"type": "tool_result", "tool_use_id": "u2", "content": "ok"},
                {"type": "tool_result", "tool_use_id": "u3", "content": "ok"}]}})
        reconcile = load_script("reconcile_run_t", "reconcile-run.py")
        gate = reconcile.load_gate_module()
        record = lane.audit_agent(lines, "general-purpose", config, {"agent_definitions": {}},
                                  reconcile, gate, None)
        self.assertEqual([c["tool"] for c in record["blinding"]["contaminating"]], ["Read"])
        self.assertEqual(record["writes_outside_scope"], ["/elsewhere/notes.md"])
        self.assertFalse(record["clean"])


class SpillExemptionTests(unittest.TestCase):
    """Own spill files are in scope; another agent's spill stays blinded."""

    def test_own_spill_exempt_other_spill_flagged(self):
        home = str(Path.home())
        own = f"{home}/.claude/projects/p/s/tool-results/own123.txt"
        other = f"{home}/.claude/projects/p/s/tool-results/other456.txt"
        config = {"run_id": "t", "effort": "high",
                  "agents": {"planner": "reproduction-planner",
                             "executor": "reproduction-executor",
                             "reviewer": "adversarial-reviewer"},
                  "schemas": {}, "pricing_usd_per_mtok": {},
                  "blinding": {"forbidden_substrings": [".claude/projects/"],
                               "cross_paper_slugs": []}}
        lines = transcript(
            {"message": {"role": "user", "content": "  Paper: a-2024\n"}},
            {"message": {"role": "assistant", "content": [
                {"type": "tool_use", "id": "b1", "name": "Bash",
                 "input": {"command": "cat big.R"}}]}},
            {"message": {"role": "user", "content": [
                {"type": "tool_result", "tool_use_id": "b1",
                 "content": f"<persisted-output>\nFull output saved to: {own}\n"}]}},
            {"message": {"role": "assistant", "content": [
                {"type": "tool_use", "id": "r1", "name": "Read", "input": {"file_path": own}},
                {"type": "tool_use", "id": "r2", "name": "Read",
                 "input": {"file_path": other}}]}},
            {"message": {"role": "user", "content": [
                {"type": "tool_result", "tool_use_id": "r1", "content": "x"},
                {"type": "tool_result", "tool_use_id": "r2", "content": "y"}]}})
        reconcile = load_script("reconcile_run_s", "reconcile-run.py")
        record = lane.audit_agent(lines, "general-purpose", config, {"agent_definitions": {}},
                                  reconcile, reconcile.load_gate_module(), None)
        flagged = [c["path"] for c in record["blinding"]["contaminating"]]
        self.assertEqual(len(flagged), 1)
        self.assertIn("other456", flagged[0])
        self.assertEqual(record["blinding"]["warnings"], [])

class ReplanTests(unittest.TestCase):
    """Receipt keys come from the manifest; re-planning respects the lock."""

    def test_receipt_keys_match_manifest_pushes(self):
        import yaml
        manifest = yaml.safe_load((REPO_ROOT / "manifest.yaml").read_text(encoding="utf-8"))
        for agent in ("reproduction-planner", "reproduction-executor", "adversarial-reviewer"):
            expected = [name for name, entry in manifest["shared_content"].items()
                        for c in entry.get("consumers") or []
                        if c.get("agent") == agent and c.get("mechanism") == "push"]
            self.assertEqual(lane.receipt_keys(agent), expected, agent)
        self.assertIn("pipeline-invariants", lane.receipt_keys("reproduction-planner"))

    def test_supersede_archives_unapproved_and_refuses_approved(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            config = {"attempt": 2, "output_root": str(root),
                      "_path": root / "cfg" / "run-config.yaml"}
            target = root / "a-2024" / "reproduction" / "attempt-02"
            record = dict(plan_record(["T01"], slug="a-2024"), workflow_run="wf_old")
            write(target / lane.PLAN_FILE, json.dumps(record))
            write(target / lane.PLAN_VIEW_FILE, "# view\n")
            archive = lane.supersede_plan(config, "a-2024")
            self.assertFalse((target / lane.PLAN_FILE).exists())
            self.assertTrue((archive / lane.PLAN_FILE).exists())
            self.assertEqual(archive, root / "cfg" / "superseded-plans" / "wf_old" / "a-2024")
            write(target / lane.PLAN_FILE, json.dumps(record))
            write(target / lane.APPROVAL_FILE, "{}")
            with self.assertRaises(lane.LaneError):
                lane.supersede_plan(config, "a-2024")

    def test_prompt_exemption_matches_audit_regex(self):
        import yaml
        config = yaml.safe_load((REPO_ROOT / "studies" / "open-science-compliance" / "outputs"
                                 / "validation" / "phase2-shakedown" / "run-config.yaml")
                                .read_text(encoding="utf-8"))
        exempt = re.compile(config["blinding"]["exempt_regex"])
        example = ("~/.claude/projects/p/s/tool-results/"
                   "hook-1d8724ae-a365-4faa-85a9-43914d631a73-1-additionalContext.txt")
        self.assertIsNotNone(exempt.search(example))
        for workflow in ("reproduction-plan.workflow.js", "reproduction-execute.workflow.js"):
            source = (WORKFLOWS / workflow).read_text(encoding="utf-8")
            self.assertIn("additionalContext.txt", source, workflow)
            self.assertIn("Full output saved to", source, workflow)
            self.assertIn("receipt_keys", source, workflow)

if __name__ == "__main__":
    unittest.main()
