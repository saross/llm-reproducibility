#!/usr/bin/env python3
"""Unit tests for assembler v1.6 (register F-013 and F-015, ruled 2026-10-04).

Pins two fixes in ``scripts/assemble-arm-record.py``:

1. **F-015:** since Claude Code 2.1.288 a workflow spawn receives the
   script's prompt as a "[Workflow harness — computed task]" message with
   every line indented two spaces. ``PROMPT_RE`` must still identify the
   spawn's arm, run, and paper, in both the raw and the JSON-escaped form,
   without losing the pre-2.1.288 form.
2. **F-013:** the harness repeats a response's ``usage`` on every
   content-block entry, so ``transcript_tokens`` must count each API request
   once (input and cache fields identical within a request; output
   cumulative, so its maximum).

Run: ``venv/bin/python -m pytest tests/test_assembler_v16.py -q``
"""

from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent


def load_script(name: str, filename: str):
    """Import a hyphen-named script as a module (test_reconcile pattern)."""
    spec = importlib.util.spec_from_file_location(name, REPO_ROOT / "scripts" / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


assembler = load_script("assemble_arm_record", "assemble-arm-record.py")

HEADER = ("Benchmark scoring task (preregistered validation phase, "
          "arm opus-5-5, run 2 of 3).")
PAPER = "Paper: herskind-riede-2024. Source (read in full): /x/vor.pdf"


class PromptIdentityTests(unittest.TestCase):
    """PROMPT_RE across harness prompt shapes (F-015)."""

    def assert_identity(self, text: str) -> None:
        """The parsed identity is (arm, run, slug) for the fixture prompt."""
        self.assertEqual(assembler.transcript_identity(text),
                         ("opus-5-5", 2, "herskind-riede-2024"))

    def test_legacy_unindented_prompt(self):
        self.assert_identity(f"{HEADER}\n{PAPER}\n")

    def test_indented_computed_task_raw(self):
        computed = ("[Workflow harness — computed task] The task text below "
                    "was computed at runtime by a workflow script.\n"
                    f"  {HEADER}\n  {PAPER}\n")
        self.assert_identity(computed)

    def test_indented_computed_task_json_escaped(self):
        computed = f"[Workflow harness — computed task] ...\n  {HEADER}\n  {PAPER}\n"
        line = json.dumps({"type": "user", "message": {"role": "user", "content": computed}})
        self.assertIn("\\n  Paper:", line)  # the transcript's on-disk shape
        self.assert_identity(line)

    def test_unrelated_text_is_not_an_identity(self):
        self.assertIsNone(assembler.transcript_identity("Paper: x. arm y, run 1 of 3)."))


def entry(request_id: str | None, message_id: str, **usage: int) -> str:
    """One transcript JSONL line carrying a usage block."""
    record = {"message": {"id": message_id, "usage": usage}}
    if request_id is not None:
        record["requestId"] = request_id
    return json.dumps(record)


class PerRequestTokenTests(unittest.TestCase):
    """transcript_tokens counts each API request once (F-013)."""

    def test_repeated_blocks_count_once(self):
        # One request written as three content blocks (thinking, text,
        # tool_use): input/cache repeated, output cumulative.
        lines = [entry("req_1", "msg_1", input_tokens=10, output_tokens=5,
                       cache_creation_input_tokens=100, cache_read_input_tokens=1000),
                 entry("req_1", "msg_1", input_tokens=10, output_tokens=20,
                       cache_creation_input_tokens=100, cache_read_input_tokens=1000),
                 entry("req_1", "msg_1", input_tokens=10, output_tokens=30,
                       cache_creation_input_tokens=100, cache_read_input_tokens=1000),
                 entry("req_2", "msg_2", input_tokens=3, output_tokens=7,
                       cache_creation_input_tokens=0, cache_read_input_tokens=1100)]
        totals = assembler.transcript_tokens(lines)
        self.assertEqual(totals["api_requests"], 2)
        self.assertEqual(totals["input_tokens"], 13)
        self.assertEqual(totals["output_tokens"], 37)
        self.assertEqual(totals["cache_creation_input_tokens"], 100)
        self.assertEqual(totals["cache_read_input_tokens"], 2100)
        self.assertEqual(totals["contract_metric_tokens"], 13 + 37 + 100)

    def test_falls_back_to_message_id(self):
        lines = [entry(None, "msg_9", input_tokens=4, output_tokens=1),
                 entry(None, "msg_9", input_tokens=4, output_tokens=6)]
        totals = assembler.transcript_tokens(lines)
        self.assertEqual(totals["api_requests"], 1)
        self.assertEqual(totals["output_tokens"], 6)

    def test_ignores_malformed_and_usage_free_lines(self):
        lines = ["not json", json.dumps({"message": {"content": "hi"}}),
                 entry("req_1", "m", input_tokens=2, output_tokens=2)]
        self.assertEqual(assembler.transcript_tokens(lines)["contract_metric_tokens"], 4)


if __name__ == "__main__":
    unittest.main()
