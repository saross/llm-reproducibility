#!/usr/bin/env python3
"""Tests for the production spawn-control hooks (audit 2026-08-03 C4).

The 2026-07-24 build verified these hooks with ephemeral stdin invocations
that were never committed; this suite makes the pipe-tests durable. Two
styles are used deliberately:

- `preflight-agent.py` is exercised as a real subprocess pipe (it logs
  nothing, so there are no side effects), asserting the emitted deny JSON —
  the wiring contract the harness consumes.
- `subagent-receipt-gate.py` is imported and exercised through `validate()`
  with its logger and manifest loader patched, so tests never write to the
  live `receipt-gate-log.jsonl` run evidence.

Run directly (stdlib only): ``python3 tests/test_hooks.py``
"""

from __future__ import annotations

import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
HOOKS_DIR = REPO_ROOT / ".claude" / "hooks"
PREFLIGHT = HOOKS_DIR / "preflight-agent.py"
GATE = HOOKS_DIR / "subagent-receipt-gate.py"


def load_hook_module(path: Path, name: str):
    """Import a hyphen-named hook file as a module."""
    sys.path.insert(0, str(HOOKS_DIR))
    try:
        spec = importlib.util.spec_from_loader(
            name, importlib.machinery.SourceFileLoader(name, str(path)))
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    finally:
        sys.path.pop(0)


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


def valid_payload(**overrides) -> dict:
    """A gate-passing nested payload; override fields to inject defects."""
    payload = {
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
    payload.update(overrides)
    return payload


class ReceiptGateTests(unittest.TestCase):
    """Decision-logic tests via validate(), with logging and manifest patched."""

    def setUp(self) -> None:
        self.gate = load_hook_module(GATE, "subagent_receipt_gate_under_test")
        self.events: list[dict] = []
        self.gate.log_jsonl = lambda path, record: self.events.append(record)
        self.gate.load_manifest = lambda: FIXTURE_MANIFEST

    def run_gate(self, payload: dict | None, agent_type: str = "test-scorer",
                 transcript: str = "") -> list[str]:
        """Run validate() on a synthetic event; return logged event names."""
        import contextlib
        import io
        event = {"agent_type": agent_type,
                 "last_assistant_message": json.dumps(payload) if payload else "",
                 "agent_transcript_path": transcript}
        with contextlib.redirect_stdout(io.StringIO()):
            self.gate.validate(event)
        return [e.get("event") for e in self.events]

    def test_valid_nested_payload_passes(self) -> None:
        self.assertEqual(self.run_gate(valid_payload()), ["pass"])

    def test_valid_flat_payload_passes(self) -> None:
        """Back-compat: the agent definitions list the fields without nesting."""
        flat = valid_payload()
        flat.update(flat.pop("receipts"))
        self.assertEqual(self.run_gate(flat), ["pass"])

    def test_wrong_model_id_blocks(self) -> None:
        payload = valid_payload()
        payload["receipts"]["model_id"] = "claude-other"
        self.assertEqual(self.run_gate(payload), ["block"])
        self.assertIn("model_id", self.events[0]["reason"])

    def test_context_marker_suffix_accepted(self) -> None:
        """The harness 1M marker on the pinned ID is a match, recorded verbatim."""
        payload = valid_payload()
        payload["receipts"]["model_id"] = "claude-test-1[1m]"
        self.assertEqual(self.run_gate(payload), ["pass"])

    def test_escalate_with_wrong_model_blocks(self) -> None:
        """C5 regression: escalation is not an exemption from provenance."""
        payload = valid_payload(status="ESCALATE", escalate_reason="fixture")
        payload["receipts"]["model_id"] = "gpt-9"
        self.assertEqual(self.run_gate(payload), ["block"])

    def test_escalate_with_valid_receipts_passes_through(self) -> None:
        payload = valid_payload(status="ESCALATE", escalate_reason="unreadable input")
        self.assertEqual(self.run_gate(payload), ["escalate-passthrough"])
        self.assertEqual(self.events[0]["reason"], "unreadable input")

    def test_wrong_receipt_token_blocks(self) -> None:
        payload = valid_payload()
        payload["receipts"]["instrument_receipts"]["test-instrument"] = "0000"
        self.assertEqual(self.run_gate(payload), ["block"])

    def test_wrong_instrument_version_blocks(self) -> None:
        payload = valid_payload()
        payload["receipts"]["instrument_versions"]["test-instrument"] = "9.9"
        self.assertEqual(self.run_gate(payload), ["block"])

    def test_wrong_agent_version_blocks(self) -> None:
        """M8 regression: agent_version is validated, not merely required."""
        payload = valid_payload()
        payload["receipts"]["agent_version"] = "whatever"
        self.assertEqual(self.run_gate(payload), ["block"])

    def test_list_typed_receipts_block_not_crash(self) -> None:
        """C9 regression: a wrong-typed receipt field blocks instead of crashing."""
        payload = valid_payload()
        payload["receipts"]["instrument_versions"] = ["1.0"]
        self.assertEqual(self.run_gate(payload), ["block"])

    def test_structured_output_found_in_transcript_tool_call(self) -> None:
        """C4 regression: workflow-lane output rides a tool call, not the message."""
        with tempfile.NamedTemporaryFile("w", suffix=".jsonl", delete=False) as f:
            f.write(json.dumps({"message": {"content": [
                {"type": "tool_use", "name": "StructuredOutput",
                 "input": valid_payload()}]}}) + "\n")
            transcript = f.name
        self.addCleanup(os.unlink, transcript)
        self.assertEqual(self.run_gate(None, transcript=transcript), ["pass"])

    def test_no_output_anywhere_blocks(self) -> None:
        self.assertEqual(self.run_gate(None), ["block"])

    def test_ungoverned_agent_passes_through(self) -> None:
        self.assertEqual(self.run_gate(valid_payload(), agent_type="general-purpose"),
                         [])

    def test_pass_log_carries_decision_context(self) -> None:
        """Item 2a (2026-08-14): every decision logs the event's key names,
        the agent_id, the payload-source branch, and the item slug (M-9)."""
        self.run_gate(valid_payload())
        record = self.events[0]
        self.assertEqual(record["event"], "pass")
        self.assertEqual(record["event_keys"],
                         ["agent_transcript_path", "agent_type",
                          "last_assistant_message"])
        self.assertEqual(record["payload_source"], "final_message")
        self.assertEqual(record["paper_slug"], "fixture")
        self.assertIn("agent_id", record)

    def test_block_log_carries_decision_context(self) -> None:
        """Item 2a (2026-08-14): block decisions carry the same context."""
        self.run_gate(None)
        record = self.events[0]
        self.assertEqual(record["event"], "block")
        self.assertEqual(record["payload_source"], "none")
        self.assertIn("event_keys", record)

    def test_transcript_payload_source_is_logged_as_branch(self) -> None:
        """Item 2a (2026-08-14): the fallback branch is named in the log."""
        with tempfile.NamedTemporaryFile("w", suffix=".jsonl", delete=False) as f:
            f.write(json.dumps({"message": {"content": [
                {"type": "tool_use", "name": "StructuredOutput",
                 "input": valid_payload()}]}}) + "\n")
            transcript = f.name
        self.addCleanup(os.unlink, transcript)
        self.run_gate(None, transcript=transcript)
        self.assertEqual(self.events[0]["payload_source"], "transcript_tool_call")

    def test_internal_error_blocks_not_crashes(self) -> None:
        """Fail-closed: an unexpected internal error blocks the item."""
        self.gate.load_manifest = lambda: (_ for _ in ()).throw(RuntimeError("boom"))
        event = {"agent_type": "test-scorer", "last_assistant_message": "{}"}
        import contextlib
        import io
        with contextlib.redirect_stdout(io.StringIO()):
            self.gate.validate(event)
        self.assertEqual([e.get("event") for e in self.events], ["block"])


class PreflightPipeTests(unittest.TestCase):
    """Real subprocess pipe tests for the PreToolUse deny contract."""

    def run_hook(self, stdin_text: str, env_extra: dict | None = None):
        env = dict(os.environ)
        env.pop("CLAUDE_CODE_SUBAGENT_MODEL", None)
        if env_extra:
            env.update(env_extra)
        return subprocess.run([sys.executable, str(PREFLIGHT)], input=stdin_text,
                              capture_output=True, text=True, env=env, timeout=120)

    def deny_reason(self, result) -> str | None:
        if not result.stdout.strip():
            return None
        decision = json.loads(result.stdout)
        output = decision.get("hookSpecificOutput", {})
        if output.get("permissionDecision") == "deny":
            return output.get("permissionDecisionReason", "")
        return None

    def test_garbage_stdin_denies(self) -> None:
        """C8 regression: an unparseable event fails closed with deny JSON."""
        result = self.run_hook("not json at all")
        self.assertIsNotNone(self.deny_reason(result))

    def test_non_agent_tool_allows(self) -> None:
        result = self.run_hook(json.dumps({"tool_name": "Bash", "tool_input": {}}))
        self.assertIsNone(self.deny_reason(result))
        self.assertEqual(result.returncode, 0)

    def test_ungoverned_spawn_allows(self) -> None:
        result = self.run_hook(json.dumps({"tool_name": "Agent",
                                           "tool_input": {"subagent_type": "Explore"}}))
        self.assertIsNone(self.deny_reason(result))

    def test_governed_spawn_with_env_override_denies(self) -> None:
        """C2/D-7 regression: the env var outranks pins, so the spawn is denied."""
        result = self.run_hook(
            json.dumps({"tool_name": "Agent",
                        "tool_input": {"subagent_type": "fair-assessor-sonnet-5"}}),
            env_extra={"CLAUDE_CODE_SUBAGENT_MODEL": "claude-x"})
        reason = self.deny_reason(result)
        self.assertIsNotNone(reason)
        self.assertIn("CLAUDE_CODE_SUBAGENT_MODEL", reason)

    def test_list_tool_input_denies_not_crashes(self) -> None:
        """C8 regression: unexpected tool_input shape cannot crash-allow."""
        result = self.run_hook(json.dumps({"tool_name": "Agent", "tool_input": [1, 2]}))
        # A list tool_input means the type cannot be read; the hook treats it
        # as ungoverned-unknown but must not crash (rc 0 either way).
        self.assertEqual(result.returncode, 0)


class PushListTests(unittest.TestCase):
    """The push hook's routing derives from the manifest; pin today's routing."""

    def test_fair_assessors_receive_the_instrument(self) -> None:
        hooklib = load_hook_module(HOOKS_DIR / "hooklib.py", "hooklib_under_test")
        manifest = hooklib.load_manifest()
        for arm in ("fair-assessor-sonnet-5", "fair-assessor-opus-5",
                    "fair-assessor-fable-5"):
            specs = hooklib.pushed_instruments(manifest, arm)
            names = {s["name"] for s in specs}
            self.assertIn("fair-instrument", names,
                          f"{arm} must be pushed the FAIR instrument; got {names}")
            spec = next(s for s in specs if s["name"] == "fair-instrument")
            self.assertEqual(spec["version"], "2.0")
            self.assertTrue(spec["token"])


if __name__ == "__main__":
    unittest.main()
