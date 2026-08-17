#!/usr/bin/env python3
"""Unit tests for the post-run reconciliation tool (plan C8 + C9).

Synthetic run directories only — each case builds a transcript, meta file,
and hook-log fixture, then asserts the reconciliation verdict. The live
invocations against the retained benchmark and C2 runs are recorded in the
C6/C8/C9 closure notes; these tests keep the verdict logic honest.

Run: ``venv/bin/python -m pytest tests/test_reconcile.py -q``
"""

from __future__ import annotations

import importlib.machinery
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPT = REPO_ROOT / "scripts" / "reconcile-run.py"

_spec = importlib.util.spec_from_loader(
    "reconcile_run",
    importlib.machinery.SourceFileLoader("reconcile_run", str(SCRIPT)))
reconciler = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(reconciler)

FIXTURE_MANIFEST = {
    "shared_content": {
        "test-instrument": {
            "canonical_file": "protocol/instruments/test-instrument.md",
            "version": "1.0",
            "receipt_token": "feedfacecafebeef",
            "consumers": [{"agent": "test-scorer", "mechanism": "push"}],
        },
    },
    "agent_definitions": {
        "test-scorer": {"file": ".claude/agents/test-scorer.md",
                        "version": "1.0", "model": "claude-test-1"},
    },
}

ALLOWED = ("corpus/", "tests/fixtures/")


def payload(**overrides) -> dict:
    """A receipt-valid structured output for the fixture manifest."""
    base = {
        "status": "OK",
        "paper_slug": "fixture",
        "receipts": {
            "instrument_versions": {"test-instrument": "1.0"},
            "instrument_receipts": {"test-instrument": "feedfacecafebeef"},
            "agent_version": "test-scorer v1.0",
            "model_id": "claude-test-1",
            "pulled_files_read": [],
        },
    }
    base.update(overrides)
    return base


class ReconcileTests(unittest.TestCase):
    """One synthetic run directory per case."""

    def setUp(self) -> None:
        self.run_dir = Path(tempfile.mkdtemp(prefix="recon-fixture-"))
        import shutil
        self.addCleanup(shutil.rmtree, self.run_dir, ignore_errors=True)
        self.gate_log = self.run_dir / "gate.jsonl"
        self.push_log = self.run_dir / "push.jsonl"
        self.gate_log.write_text("", encoding="utf-8")
        self.push_log.write_text("", encoding="utf-8")

    def write_agent(self, agent_id: str, reads: list[tuple[str, bool]],
                    output: dict, prompt: str | None = None) -> None:
        """Write one agent transcript (reads = [(path, is_error)]) + meta."""
        entries = []
        if prompt is not None:
            entries.append({"message": {"role": "user", "content": [
                {"type": "text", "text": prompt}]}})
        for index, (path, is_error) in enumerate(reads):
            use_id = f"toolu_{agent_id}_{index}"
            entries.append({"message": {"content": [
                {"type": "tool_use", "name": "Read", "id": use_id,
                 "input": {"file_path": path}}]}})
            entries.append({"message": {"content": [
                {"type": "tool_result", "tool_use_id": use_id,
                 "is_error": is_error, "content": "x"}]}})
        entries.append({"message": {"content": [
            {"type": "tool_use", "name": "StructuredOutput",
             "id": f"toolu_{agent_id}_out", "input": output}]}})
        transcript = self.run_dir / f"agent-{agent_id}.jsonl"
        transcript.write_text("\n".join(json.dumps(e) for e in entries) + "\n",
                              encoding="utf-8")
        (self.run_dir / f"agent-{agent_id}.meta.json").write_text(
            json.dumps({"agentType": "test-scorer"}), encoding="utf-8")

    def log_gate_event(self, agent_id: str, event: str) -> None:
        with self.gate_log.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps({"agent_id": agent_id, "event": event}) + "\n")

    def run_reconcile(self) -> dict:
        return reconciler.reconcile(self.run_dir, ALLOWED,
                                    self.gate_log, self.push_log,
                                    manifest=FIXTURE_MANIFEST)

    def test_valid_spawn_reconciles(self) -> None:
        self.write_agent("a1", [("corpus/paper.md", False)], payload())
        self.log_gate_event("a1", "pass")
        report = self.run_reconcile()
        self.assertTrue(report["clean"], report)
        agent = report["agents"][0]
        self.assertTrue(agent["reconciled"])
        self.assertFalse(agent["divergence"]["no_gate_event"])

    # --- evidence-pack verification (D3 prep, reconcile-run v1.1) ---------

    def write_pack(self, rel: str = "corpus/evidence-packs/fixture.json",
                   body: str = '{"paper_slug": "fixture", "records": []}') -> tuple[str, str]:
        """Write a fixture pack under a patched REPO_ROOT; return (path, sha)."""
        import hashlib as _hashlib
        original_root = reconciler.REPO_ROOT
        reconciler.REPO_ROOT = self.run_dir
        self.addCleanup(setattr, reconciler, "REPO_ROOT", original_root)
        pack = self.run_dir / rel
        pack.parent.mkdir(parents=True, exist_ok=True)
        pack.write_text(body, encoding="utf-8")
        return rel, _hashlib.sha256(pack.read_bytes()).hexdigest()

    def pack_prompt(self, rel: str, sha: str) -> str:
        return (f"Benchmark scoring task. "
                f"Evidence pack (read in full): {rel} (sha256 {sha})")

    def test_pack_declared_read_and_hashed_reconciles(self) -> None:
        rel, sha = self.write_pack()
        self.write_agent("a1", [("corpus/paper.md", False), (rel, False)],
                         payload(), prompt=self.pack_prompt(rel, sha))
        self.log_gate_event("a1", "pass")
        report = self.run_reconcile()
        self.assertTrue(report["clean"], report)

    def test_pack_sha_drift_fails(self) -> None:
        rel, sha = self.write_pack()
        (self.run_dir / rel).write_text('{"tampered": true}', encoding="utf-8")
        self.write_agent("a1", [(rel, False)], payload(),
                         prompt=self.pack_prompt(rel, sha))
        self.log_gate_event("a1", "pass")
        report = self.run_reconcile()
        self.assertFalse(report["clean"])
        self.assertTrue(any("evidence pack sha256 drift" in p
                            for p in report["agents"][0]["receipts"]["problems"]), report)

    def test_pack_declared_but_never_read_fails(self) -> None:
        rel, sha = self.write_pack()
        self.write_agent("a1", [("corpus/paper.md", False)], payload(),
                         prompt=self.pack_prompt(rel, sha))
        self.log_gate_event("a1", "pass")
        report = self.run_reconcile()
        self.assertFalse(report["clean"])
        self.assertTrue(any("never read" in p
                            for p in report["agents"][0]["receipts"]["problems"]), report)

    def test_pack_read_that_only_errored_fails(self) -> None:
        rel, sha = self.write_pack()
        self.write_agent("a1", [(rel, True)], payload(),
                         prompt=self.pack_prompt(rel, sha))
        self.log_gate_event("a1", "pass")
        report = self.run_reconcile()
        self.assertFalse(report["clean"])
        self.assertTrue(any("every Read errored" in p
                            for p in report["agents"][0]["receipts"]["problems"]), report)

    def test_ungoverned_agent_skipped_not_judged(self) -> None:
        """A general-purpose reconcile agent's own transcript in the run dir
        must not poison the report (reconcile-run v1.1)."""
        self.write_agent("a1", [("corpus/paper.md", False)], payload())
        self.log_gate_event("a1", "pass")
        # An ungoverned agent with no receipts at all, same directory.
        self.write_agent("r1", [("scripts/reconcile-run.py", False)],
                         {"slug": "fixture", "verdict": "pass"})
        (self.run_dir / "agent-r1.meta.json").write_text(
            json.dumps({"agentType": "general-purpose"}), encoding="utf-8")
        report = self.run_reconcile()
        self.assertTrue(report["clean"], report)
        self.assertEqual(report["spawns"], 1)
        self.assertEqual(len(report["skipped_ungoverned"]), 1)
        self.assertEqual(report["skipped_ungoverned"][0]["agent_type"],
                         "general-purpose")

    # --- v1.2 audit fixes (clean-context Opus audit, 2026-08-17) ----------

    def test_empty_directory_is_not_clean(self) -> None:
        """Audit F1: zero governed spawns must never read as clean."""
        report = self.run_reconcile()
        self.assertFalse(report["clean"])
        self.assertTrue(any("no governed spawns" in p
                            for p in report["count_problems"]), report)

    def test_expected_spawn_count_enforced(self) -> None:
        """Audit F1: a partial directory fails the denominator assertion."""
        self.write_agent("a1", [("corpus/paper.md", False)], payload())
        self.log_gate_event("a1", "pass")
        report = reconciler.reconcile(self.run_dir, ALLOWED,
                                      self.gate_log, self.push_log,
                                      manifest=FIXTURE_MANIFEST,
                                      expect_spawns=15)
        self.assertFalse(report["clean"])
        self.assertTrue(any("expected 15" in p
                            for p in report["count_problems"]), report)

    def test_missing_meta_fails_not_skips(self) -> None:
        """Audit F2: an unattributable transcript shrinks clean, never the
        denominator."""
        self.write_agent("a1", [("corpus/paper.md", False)], payload())
        (self.run_dir / "agent-a1.meta.json").unlink()
        self.log_gate_event("a1", "pass")
        report = self.run_reconcile()
        self.assertFalse(report["clean"])
        self.assertEqual(report["spawns"], 1)
        self.assertEqual(report["skipped_ungoverned"], [])
        self.assertTrue(any("unattributable" in p
                            for p in report["agents"][0]["receipts"]["problems"]))

    def test_push_error_event_fails_spawn(self) -> None:
        """Audit F6: a logged push-error is a reconciliation problem."""
        self.write_agent("a1", [("corpus/paper.md", False)], payload())
        self.log_gate_event("a1", "pass")
        with self.push_log.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps({"agent_id": "a1", "event": "push-error",
                                     "error": "sha256 drift"}) + "\n")
        report = self.run_reconcile()
        self.assertFalse(report["clean"])
        self.assertTrue(any("push-error" in p
                            for p in report["agents"][0]["receipts"]["problems"]))

    def test_pushed_sha_mismatch_fails_spawn(self) -> None:
        """Audit F6: pushed bytes differing from the registered C7 hash fail."""
        manifest = json.loads(json.dumps(FIXTURE_MANIFEST))
        manifest["shared_content"]["test-instrument"]["sha256"] = "a" * 64
        self.write_agent("a1", [("corpus/paper.md", False)], payload())
        self.log_gate_event("a1", "pass")
        with self.push_log.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps({"agent_id": "a1", "event": "push",
                                     "name": "test-instrument",
                                     "sha256": "b" * 64}) + "\n")
        report = reconciler.reconcile(self.run_dir, ALLOWED,
                                      self.gate_log, self.push_log,
                                      manifest=manifest)
        self.assertFalse(report["clean"])
        self.assertTrue(any("differ from registered hash" in p
                            for p in report["agents"][0]["receipts"]["problems"]))

    def test_require_pack_flags_missing_declaration(self) -> None:
        """Audit F18: a regex non-match must fail loudly under --require-pack."""
        self.write_agent("a1", [("corpus/paper.md", False)], payload())
        self.log_gate_event("a1", "pass")
        report = reconciler.reconcile(self.run_dir, ALLOWED,
                                      self.gate_log, self.push_log,
                                      manifest=FIXTURE_MANIFEST,
                                      require_pack=True)
        self.assertFalse(report["clean"])
        self.assertTrue(any("no evidence-pack declaration" in p
                            for p in report["agents"][0]["receipts"]["problems"]))

    def test_uppercase_pack_hash_matches(self) -> None:
        """Audit F18: an uppercase-hex declared sha256 must not silently
        disable pack verification."""
        rel, sha = self.write_pack()
        self.write_agent("a1", [(rel, False)], payload(),
                         prompt=self.pack_prompt(rel, sha.upper()))
        self.log_gate_event("a1", "pass")
        report = self.run_reconcile()
        self.assertTrue(report["clean"], report)

    def test_receipted_values_recorded(self) -> None:
        """Audit F7: the report carries receipted VALUES for the cross-arm
        identity check."""
        self.write_agent("a1", [("corpus/paper.md", False)], payload())
        self.log_gate_event("a1", "pass")
        report = self.run_reconcile()
        receipted = report["agents"][0]["receipts"]["receipted"]
        self.assertEqual(receipted["instrument_versions"],
                         {"test-instrument": "1.0"})
        self.assertEqual(receipted["model_id"], "claude-test-1")

    def test_invalid_receipts_fail(self) -> None:
        bad = payload()
        bad["receipts"]["instrument_receipts"]["test-instrument"] = "0000"
        self.write_agent("a1", [("corpus/paper.md", False)], bad)
        report = self.run_reconcile()
        self.assertFalse(report["clean"])
        self.assertIn("receipt token mismatch",
                      " ".join(report["agents"][0]["receipts"]["problems"]))

    def test_successful_out_of_scope_read_fails(self) -> None:
        """C8 / amendment 1 §4: a successful read outside the allowed scope
        is contamination and fails the spawn."""
        self.write_agent("a1", [("corpus/paper.md", False),
                                ("outputs/pilot/assessment.json", False)],
                         payload())
        report = self.run_reconcile()
        agent = report["agents"][0]
        self.assertFalse(agent["reconciled"])
        self.assertEqual(agent["file_access"]["contaminating"][0]["target"],
                         "outputs/pilot/assessment.json")

    def test_errored_out_of_scope_attempt_warns_not_fails(self) -> None:
        """The live 2026-08-03 case: a failed Read of a wrong path is a
        warning-grade attempt, not contamination."""
        self.write_agent("a1", [("corpus/paper.md", False),
                                ("~/nonexistent/guide.md", True)],
                         payload())
        report = self.run_reconcile()
        agent = report["agents"][0]
        self.assertTrue(agent["reconciled"], agent)
        self.assertEqual(len(agent["file_access"]["flagged"]), 1)
        self.assertEqual(len(agent["file_access"]["contaminating"]), 0)

    def test_declared_pull_that_only_errored_fails(self) -> None:
        """C6/C8 finding (2026-08-15): attempts are not reads."""
        declared = payload()
        declared["receipts"]["pulled_files_read"] = ["corpus/ref.md"]
        self.write_agent("a1", [("corpus/ref.md", True)], declared)
        report = self.run_reconcile()
        self.assertIn("every Read errored",
                      " ".join(report["agents"][0]["receipts"]["problems"]))

    def test_block_with_collected_output_is_named_divergence(self) -> None:
        """The B1 tripwire: a blocked spawn whose output validates post hoc
        is exactly the silent-collection case — it must be named."""
        self.write_agent("a1", [("corpus/paper.md", False)], payload())
        self.log_gate_event("a1", "block")
        report = self.run_reconcile()
        agent = report["agents"][0]
        self.assertTrue(agent["divergence"]["blocked_but_output_present"])

    def test_missing_gate_event_is_named_divergence(self) -> None:
        self.write_agent("a1", [("corpus/paper.md", False)], payload())
        report = self.run_reconcile()
        self.assertTrue(report["agents"][0]["divergence"]["no_gate_event"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
