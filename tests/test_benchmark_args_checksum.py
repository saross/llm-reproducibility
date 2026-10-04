#!/usr/bin/env python3
"""Args-integrity guard for the FAIR benchmark workflow (v1.7, 2026-10-04).

``scripts/build-benchmark-args.py`` (v1.5) stamps ``args_checksum`` on the
key-sorted args it writes. ``fair-benchmark-arm.workflow.js`` (v1.7)
recomputes the checksum over the args that actually arrive in the Workflow
tool call and refuses to start on any difference. These tests pin:

1. byte-identity of the workflow's checksum block with the reproduction
   lane's workflows, whose algorithm ``args_checksum()`` implements, so the
   two lanes cannot drift;
2. that args stamped by the builder verify under the FAIR workflow's own
   JavaScript, run in Node, from the exact file text the builder writes;
3. that a one-character alteration is refused.

Run: ``venv/bin/python -m pytest tests/test_benchmark_args_checksum.py -q``
"""

from __future__ import annotations

import importlib.util
import json
import shutil
import subprocess
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
FAIR_WORKFLOW = (REPO_ROOT / "studies/open-science-compliance/protocol/validation"
                 / "fair-benchmark-arm.workflow.js")
LANE_WORKFLOW = REPO_ROOT / "reproduction-system/workflows/reproduction-execute.workflow.js"
BLOCK_START = "const { args_checksum, ...UNSUMMED } = ARGS"
BLOCK_END = "if (COMPUTED !== args_checksum)"


def load_script(name: str, filename: str):
    """Import a hyphen-named script as a module (test_reconcile pattern)."""
    spec = importlib.util.spec_from_file_location(name, REPO_ROOT / "scripts" / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


builder = load_script("build_benchmark_args", "build-benchmark-args.py")

# Shaped like real args: nested schema, hashes, a list of papers, non-ASCII.
PAYLOAD = {
    "arm": "opus-5-5", "agentType": "fair-assessor-opus-5-5", "effort": "high",
    "launch_commit": "a" * 40,
    "papers": [{"slug": "marwick-2025", "path": "/x/vor.pdf",
                "pack": "corpus/packs/m.json", "pack_sha256": "b" * 64}],
    "items": [{"slug": "marwick-2025", "run": 1}],
    "schema": {"type": "object", "properties": {"note": {"description": "Ertebølle — ü"}},
               "required": ["note"], "version": "1.1"},
}


def guard_script(args_text: str) -> str:
    """Node program: the workflow's ARGS parse and checksum guard, then OK."""
    source = FAIR_WORKFLOW.read_text(encoding="utf-8")
    start = source.index("const ARGS = ")
    end = source.index("const { agentType, arm, effort")
    return (f"const args = {args_text};\n{source[start:end]}\n"
            "process.stdout.write('OK ' + COMPUTED)")


class ChecksumGuardTests(unittest.TestCase):
    """The FAIR workflow's args guard against the builder's stamp."""

    def test_block_identical_to_lane(self):
        fair = FAIR_WORKFLOW.read_text(encoding="utf-8")
        lane = LANE_WORKFLOW.read_text(encoding="utf-8")
        extract = (lambda s: s[s.index(BLOCK_START):s.index(BLOCK_END)])
        self.assertEqual(extract(fair), extract(lane))

    def test_stamp_is_sorted_and_last_key_free(self):
        stamped = builder.stamp_checksum(PAYLOAD)
        self.assertIn("args_checksum", stamped)
        self.assertEqual(list(stamped)[:-1], sorted(PAYLOAD))
        self.assertRegex(stamped["args_checksum"], r"^[0-9a-f]{16}$")

    def run_guard(self, args_text: str) -> subprocess.CompletedProcess:
        """Run the workflow guard in Node over the given args text."""
        return subprocess.run(["node", "-e", guard_script(args_text)],
                               capture_output=True, text=True, timeout=30, check=False)

    def test_builder_output_verifies_in_workflow_javascript(self):
        if shutil.which("node") is None:
            self.skipTest("node not installed")
        stamped = builder.stamp_checksum(PAYLOAD)
        text = json.dumps(stamped, indent=1, sort_keys=True)  # as the builder writes
        result = self.run_guard(text)
        self.assertEqual(result.stdout, f"OK {stamped['args_checksum']}", result.stderr)

    def test_altered_args_are_refused(self):
        if shutil.which("node") is None:
            self.skipTest("node not installed")
        stamped = builder.stamp_checksum(PAYLOAD)
        text = json.dumps(stamped, indent=1, sort_keys=True).replace("b" * 64, "b" * 63 + "c")
        result = self.run_guard(text)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("args_checksum mismatch", result.stderr)


if __name__ == "__main__":
    unittest.main()
