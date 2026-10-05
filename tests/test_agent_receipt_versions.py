#!/usr/bin/env python3
"""Each agent definition's receipt string must match its manifest version.

The subagent receipt gate (``.claude/hooks/subagent-receipt-gate.py``)
compares a spawn's ``agent_version`` with ``"<name> v<manifest version>"``
by string equality and blocks the spawn on any difference. The definition
tells the agent which string to emit, so a version bump that misses that
line blocks every later spawn. This happened on 2026-10-05: the executor
definition's header said v1.3 while its receipt line still said v1.2
(Fable review of PR #7, P1-4).

Run: ``venv/bin/python -m pytest tests/test_agent_receipt_versions.py -q``
"""

from __future__ import annotations

import re
import unittest
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
RECEIPT_RE = re.compile(r'`agent_version` \("([^"]+)"\)')


class AgentReceiptVersionTests(unittest.TestCase):
    """Definition receipt strings agree with manifest.yaml agent_definitions."""

    def test_receipt_strings_match_manifest_versions(self) -> None:
        manifest = yaml.safe_load((REPO_ROOT / "manifest.yaml").read_text(encoding="utf-8"))
        checked = 0
        for name, entry in (manifest.get("agent_definitions") or {}).items():
            path = REPO_ROOT / entry["file"]
            receipts = RECEIPT_RE.findall(path.read_text(encoding="utf-8"))
            if not receipts:
                continue  # definitions without a receipt contract are not gated
            expected = f"{name} v{entry['version']}"
            with self.subTest(agent=name):
                self.assertEqual(set(receipts), {expected},
                                 f"{entry['file']} tells the agent to emit {receipts}, "
                                 f"but the receipt gate expects {expected!r}")
            checked += 1
        self.assertGreater(checked, 0, "no agent definition carries a receipt string")


if __name__ == "__main__":
    unittest.main()
