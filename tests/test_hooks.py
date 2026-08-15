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
    "assessment": {
        "schemas": {"benchmark_fair_output": {"version": "1.1"}},
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

    def _transcript_with(self, payload: dict) -> str:
        """Write a one-line transcript carrying a structured-output tool call."""
        with tempfile.NamedTemporaryFile("w", suffix=".jsonl", delete=False) as f:
            f.write(json.dumps({"message": {"content": [
                {"type": "tool_use", "name": "StructuredOutput",
                 "input": payload}]}}) + "\n")
            path = f.name
        self.addCleanup(os.unlink, path)
        return path

    def run_gate_text(self, final_text: str, transcript: str) -> list[str]:
        """Run validate() with a raw final-message text (not JSON-serialised)."""
        import contextlib
        import io
        event = {"agent_type": "test-scorer",
                 "last_assistant_message": final_text,
                 "agent_transcript_path": transcript}
        with contextlib.redirect_stdout(io.StringIO()):
            self.gate.validate(event)
        return [e.get("event") for e in self.events]

    def test_receiptless_final_json_does_not_suppress_transcript(self) -> None:
        """Item 1 re-spec (2026-08-14): a receipt-less JSON object in the
        final message must not reinstate the C4 final-message-only regression."""
        transcript = self._transcript_with(valid_payload())
        summary = json.dumps({"status": "OK", "note": "summary only"})
        self.assertEqual(self.run_gate_text(summary, transcript), ["pass"])

    def test_transcript_substitution_for_other_item_blocks(self) -> None:
        """Item 1 re-spec (2026-08-14): a transcript payload for a different
        paper_slug is substitution, not fallback — receipts must bind."""
        transcript = self._transcript_with(valid_payload())  # slug "fixture"
        other = json.dumps({"status": "OK", "paper_slug": "other-paper"})
        self.assertEqual(self.run_gate_text(other, transcript), ["block"])
        self.assertIn("not bound", self.events[0]["reason"])

    def test_transcript_fallback_with_matching_slug_passes(self) -> None:
        transcript = self._transcript_with(valid_payload())
        same = json.dumps({"status": "OK", "paper_slug": "fixture"})
        self.assertEqual(self.run_gate_text(same, transcript), ["pass"])

    def test_wellformed_final_payload_is_not_overridden(self) -> None:
        """Item 1 re-spec (2026-08-14): a well-formed final-message payload is
        validated as-is; the transcript is not consulted."""
        wrong = valid_payload()
        wrong["receipts"]["model_id"] = "claude-other"
        transcript = self._transcript_with(valid_payload())  # would pass
        self.assertEqual(self.run_gate_text(json.dumps(wrong), transcript),
                         ["block"])
        self.assertIn("model_id", self.events[0]["reason"])

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
        self.assertEqual(self.events[0]["transcript_state"], "read")

    def test_unavailable_transcript_is_named_in_log_and_reason(self) -> None:
        """C2 finding (2026-08-14): transcript-unavailable blocks are
        distinguished from searched-and-empty blocks — conflating them hid
        the benchmark's write-lag failure mode."""
        self.gate.TRANSCRIPT_RETRIES = 1
        self.gate.TRANSCRIPT_RETRY_DELAY_S = 0
        self.run_gate(None, transcript="/nonexistent/never-written.jsonl")
        record = self.events[0]
        self.assertEqual(record["event"], "block")
        self.assertEqual(record["transcript_state"], "unavailable-after-retries")
        self.assertIn("write lag", record["reason"])

    def test_matching_schema_version_passes(self) -> None:
        """C3b / S3 (2026-08-14): a payload naming the registered contract
        version validates."""
        self.assertEqual(self.run_gate(valid_payload(schema_version="1.1")),
                         ["pass"])

    def test_stale_schema_version_blocks(self) -> None:
        """C3b / S3 (2026-08-14): a stale schema_version means the spawn was
        supplied the wrong contract — block, escalate to the orchestrator."""
        self.assertEqual(self.run_gate(valid_payload(schema_version="1.0")),
                         ["block"])
        self.assertIn("schema_version", self.events[0]["reason"])

    def test_absent_schema_version_passes(self) -> None:
        """v1.0-era payloads predate self-identification and pass unchanged."""
        self.assertEqual(self.run_gate(valid_payload()), ["pass"])

    def _transcript_with_read(self, path: str, error: bool,
                              payload: dict) -> str:
        """Transcript with a Read use+result pair plus a structured output."""
        entries = [
            {"message": {"content": [{"type": "tool_use", "name": "Read",
                                      "id": "toolu_r1",
                                      "input": {"file_path": path}}]}},
            {"message": {"content": [{"type": "tool_result",
                                      "tool_use_id": "toolu_r1",
                                      "is_error": error, "content": "x"}]}},
            {"message": {"content": [{"type": "tool_use",
                                      "name": "StructuredOutput",
                                      "id": "toolu_s1", "input": payload}]}},
        ]
        with tempfile.NamedTemporaryFile("w", suffix=".jsonl", delete=False) as f:
            for entry in entries:
                f.write(json.dumps(entry) + "\n")
            transcript = f.name
        self.addCleanup(os.unlink, transcript)
        return transcript

    def test_errored_pull_blocks(self) -> None:
        """2026-08-15 (C6/C8 finding): a declared pull whose every Read
        errored was never actually read — attempts are not reads."""
        payload = valid_payload()
        payload["receipts"]["pulled_files_read"] = ["/ref/guide.md"]
        transcript = self._transcript_with_read("/ref/guide.md", True, payload)
        self.assertEqual(self.run_gate(None, transcript=transcript), ["block"])
        self.assertIn("never actually read", self.events[0]["reason"])

    def test_successful_pull_passes(self) -> None:
        payload = valid_payload()
        payload["receipts"]["pulled_files_read"] = ["/ref/guide.md"]
        transcript = self._transcript_with_read("/ref/guide.md", False, payload)
        self.assertEqual(self.run_gate(None, transcript=transcript), ["pass"])

    def test_incomplete_receipts_dict_does_not_mask_flat_fields(self) -> None:
        """Item 7 / L-1 (2026-08-14): an incomplete nested `receipts` dict
        must not mask complete, well-typed flat receipt fields."""
        flat = valid_payload()
        flat.update(flat.pop("receipts"))
        flat["receipts"] = {"note": "not the receipt carrier"}
        self.assertEqual(self.run_gate(flat), ["pass"])

    def test_empty_pulled_path_blocks(self) -> None:
        """Item 7 / L-3 (2026-08-14): an empty declared pull is a block,
        not a substring-of-everything free pass."""
        payload = valid_payload()
        payload["receipts"]["pulled_files_read"] = [""]
        transcript = self._transcript_with(valid_payload())
        self.assertEqual(self.run_gate_text(json.dumps(payload), transcript),
                         ["block"])
        self.assertIn("empty path", self.events[0]["reason"])

    def test_main_handler_blocks_on_internal_error(self) -> None:
        """Item 7 / L-6 (2026-08-14): main()'s last-resort handler emits a
        block decision instead of crash-allowing."""
        import contextlib
        import io
        self.gate.validate = lambda event: (_ for _ in ()).throw(
            RuntimeError("boom"))
        out = io.StringIO()
        real_stdin = sys.stdin
        sys.stdin = io.StringIO(json.dumps({"agent_type": "test-scorer"}))
        try:
            with contextlib.redirect_stdout(out):
                self.gate.main()
        finally:
            sys.stdin = real_stdin
        decision = json.loads(out.getvalue())
        self.assertEqual(decision["decision"], "block")
        self.assertIn("internal error", decision["reason"])

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

    def test_list_tool_input_denies(self) -> None:
        """Item 3 / L-7 (2026-08-14): an unreadable tool_input fails closed —
        the docstring's fail-closed claim is now the actual behaviour."""
        result = self.run_hook(json.dumps({"tool_name": "Agent", "tool_input": [1, 2]}))
        self.assertIsNotNone(self.deny_reason(result))
        self.assertEqual(result.returncode, 0)

    def test_clean_governed_spawn_allows(self) -> None:
        """Item 7 / L-8 (2026-08-14): the positive path — a governed spawn
        against the real, green manifest is allowed, not denied."""
        result = self.run_hook(json.dumps(
            {"tool_name": "Agent",
             "tool_input": {"subagent_type": "fair-assessor-sonnet-5"}}))
        self.assertIsNone(self.deny_reason(result))
        self.assertEqual(result.returncode, 0)

    def test_non_utf8_stdin_denies(self) -> None:
        """Item 3 / M-2 (2026-08-14): undecodable bytes deny, not crash-allow."""
        env = dict(os.environ)
        env.pop("CLAUDE_CODE_SUBAGENT_MODEL", None)
        result = subprocess.run([sys.executable, str(PREFLIGHT)],
                                input=b"\xff\xfe garbage", capture_output=True,
                                env=env, timeout=120)
        decision = json.loads(result.stdout.decode("utf-8"))
        self.assertEqual(decision["hookSpecificOutput"]["permissionDecision"],
                         "deny")


class GatePipeTests(unittest.TestCase):
    """Pipe tests for the gate's unattributable-event policy (item 3) and the
    log env seam (item 2a) — a temp log keeps the live run evidence clean."""

    def setUp(self) -> None:
        handle, self.log_path = tempfile.mkstemp(suffix=".jsonl")
        os.close(handle)
        self.addCleanup(os.unlink, self.log_path)

    def run_gate_pipe(self, stdin_data):
        env = dict(os.environ)
        env["LLMR_RECEIPT_GATE_LOG"] = self.log_path
        kwargs = {"input": stdin_data, "capture_output": True, "env": env,
                  "timeout": 120}
        if isinstance(stdin_data, str):
            kwargs["text"] = True
        return subprocess.run([sys.executable, str(GATE)], **kwargs)

    def logged_events(self) -> list[dict]:
        text = Path(self.log_path).read_text(encoding="utf-8")
        return [json.loads(line) for line in text.splitlines()]

    def test_garbage_stdin_blocks_and_logs_via_seam(self) -> None:
        """Item 3 (2026-08-14): unattributable event blocks, names the fault
        class, and the decision lands in the env-overridden log (item 2a)."""
        result = self.run_gate_pipe("not json at all")
        decision = json.loads(result.stdout)
        self.assertEqual(decision["decision"], "block")
        self.assertIn("parse fault", decision["reason"])
        self.assertEqual(self.logged_events()[-1]["event"], "block")

    def test_non_object_event_blocks(self) -> None:
        result = self.run_gate_pipe(json.dumps([1, 2]))
        self.assertEqual(json.loads(result.stdout)["decision"], "block")

    def test_ungoverned_stop_event_passes_quietly(self) -> None:
        """A well-formed event for an ungoverned agent emits nothing."""
        result = self.run_gate_pipe(json.dumps(
            {"agent_type": "general-purpose", "last_assistant_message": "done"}))
        self.assertEqual(result.stdout.strip(), "")
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
            self.assertEqual(spec["version"], "2.1")
            self.assertTrue(spec["token"])

    def test_fair_assessors_receive_the_principles_guide(self) -> None:
        """A3 (2026-08-15): the guide is pushed, not pulled — uniform
        interpretive context by construction. Regression-pins the promotion."""
        hooklib = load_hook_module(HOOKS_DIR / "hooklib.py", "hooklib_under_test")
        manifest = hooklib.load_manifest()
        for arm in ("fair-assessor-sonnet-5", "fair-assessor-opus-5",
                    "fair-assessor-fable-5"):
            specs = hooklib.pushed_instruments(manifest, arm)
            names = {s["name"] for s in specs}
            self.assertIn("fair-principles-guide", names,
                          f"{arm} must be pushed the principles guide; got {names}")
            spec = next(s for s in specs if s["name"] == "fair-principles-guide")
            self.assertEqual(spec["version"], "1.1")
            self.assertTrue(spec["token"])


if __name__ == "__main__":
    unittest.main()
