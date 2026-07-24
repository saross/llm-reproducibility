#!/usr/bin/env python3
"""Negative tests for scripts/check-manifest-consistency.py (build item D5).

Builds a minimal fixture repository in a temporary directory — one canonical
instrument, one mirror, one push consumer, one registered agent definition —
then mutates it one defect at a time and asserts each mutation is caught. A
green baseline run confirms the fixture itself is consistent, so every failure
asserted below is attributable to the injected defect.

Run directly (stdlib only): ``python3 tests/test_manifest_consistency.py``
"""

from __future__ import annotations

import hashlib
import importlib.util
import re
import shutil
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPT = REPO_ROOT / "scripts" / "check-manifest-consistency.py"

# Import the checker as a module despite its hyphenated filename.
_spec = importlib.util.spec_from_loader(
    "check_manifest_consistency",
    importlib.machinery.SourceFileLoader("check_manifest_consistency", str(SCRIPT)),
)
checker = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(checker)

CANONICAL_REL = "protocol/instruments/test-instrument.md"
MIRROR_REL = "prompts/test-mirror-prompt.md"
AGENT_REL = ".claude/agents/test-assessor.md"

CANONICAL_TEXT = """# Test instrument v1.0 — canonical file

**Status: FROZEN by OSF registration** — governance applies.
**Version:** 1.0 (fixture)

## Rubric

```text
CRITERION (max 2):
  C1: First criterion   /1
  C2: Second criterion  /1
```

## Bands

| Score | Rating |
|-------|--------|
| 2 | Good |
| 0-1 | Poor |

---

Receipt-token: feedfacecafebeef
"""

MIRROR_TEXT = """# Test mirror prompt

> Canonical home: `protocol/instruments/test-instrument.md`
> (v1.0, receipt token `feedfacecafebeef`, FROZEN).

Human-lane framing prose may differ from the canonical file.

```text
CRITERION (max 2):
  C1: First criterion   /1
  C2: Second criterion  /1
```

| Score | Rating |
|-------|--------|
| 2 | Good |
| 0-1 | Poor |
"""

AGENT_TEXT = """---
name: test-assessor
model: claude-test-1-20260101
---

Push target: protocol/instruments/test-instrument.md
"""


def build_manifest(agent_sha: str) -> str:
    """Return fixture manifest text with the given agent-definition hash."""
    return f"""shared_content:
  test-instrument:
    canonical_file: {CANONICAL_REL}
    version: "1.0"
    receipt_token: "feedfacecafebeef"
    consumers:
      - agent: test-assessor
        mechanism: push
      - agent: session-lane
        mechanism: mirror
        mirror_file: {MIRROR_REL}
agent_definitions:
  test-assessor:
    file: {AGENT_REL}
    sha256: "{agent_sha}"
"""


class ManifestConsistencyTests(unittest.TestCase):
    """One green baseline, then one injected defect per test."""

    def setUp(self) -> None:
        self.root = Path(tempfile.mkdtemp(prefix="d5-fixture-"))
        self.addCleanup(shutil.rmtree, self.root, ignore_errors=True)
        for rel, text in ((CANONICAL_REL, CANONICAL_TEXT),
                          (MIRROR_REL, MIRROR_TEXT),
                          (AGENT_REL, AGENT_TEXT)):
            path = self.root / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")
        agent_sha = hashlib.sha256((self.root / AGENT_REL).read_bytes()).hexdigest()
        self.manifest = self.root / "manifest.yaml"
        self.manifest.write_text(build_manifest(agent_sha), encoding="utf-8")

    def run_checks(self) -> "checker.Report":
        return checker.run_checks(self.manifest, self.root, preflight=False)

    def assert_error_containing(self, fragment: str) -> None:
        report = self.run_checks()
        self.assertTrue(any(fragment in e for e in report.errors),
                        f"expected an error containing {fragment!r}, got: {report.errors}")

    def rewrite(self, rel: str, old: str, new: str) -> None:
        path = self.root / rel
        text = path.read_text(encoding="utf-8")
        self.assertIn(old, text, f"fixture defect: {old!r} not in {rel}")
        path.write_text(text.replace(old, new), encoding="utf-8")

    def test_baseline_passes(self) -> None:
        report = self.run_checks()
        self.assertEqual(report.errors, [], f"fixture should be green: {report.errors}")

    def test_version_drift_caught(self) -> None:
        self.rewrite(CANONICAL_REL, "**Version:** 1.0", "**Version:** 1.1")
        self.assert_error_containing("version drift")

    def test_receipt_token_drift_caught(self) -> None:
        self.rewrite(CANONICAL_REL, "Receipt-token: feedfacecafebeef",
                     "Receipt-token: 0000000000000000")
        self.assert_error_containing("receipt-token drift")

    def test_token_not_final_line_caught(self) -> None:
        path = self.root / CANONICAL_REL
        path.write_text(path.read_text(encoding="utf-8") + "\nTrailing prose.\n",
                        encoding="utf-8")
        self.assert_error_containing("not a 'Receipt-token:' line")

    def test_missing_canonical_file_caught(self) -> None:
        (self.root / CANONICAL_REL).unlink()
        self.assert_error_containing("canonical file missing")

    def test_mirror_block_drift_caught(self) -> None:
        self.rewrite(MIRROR_REL, "C2: Second criterion  /1", "C2: Second criterion  /2")
        self.assert_error_containing("lacks canonical fenced block")

    def test_mirror_table_drift_caught(self) -> None:
        self.rewrite(MIRROR_REL, "| 2 | Good |", "| 2 | Great |")
        self.assert_error_containing("lacks canonical table row")

    def test_mirror_missing_token_citation_caught(self) -> None:
        self.rewrite(MIRROR_REL, "receipt token `feedfacecafebeef`", "receipt token elided")
        self.assert_error_containing("does not cite receipt token")

    def reregister_agent_hash(self) -> None:
        """Update the manifest's registered hash after a deliberate agent-file edit."""
        new_sha = hashlib.sha256((self.root / AGENT_REL).read_bytes()).hexdigest()
        manifest_text = self.manifest.read_text(encoding="utf-8")
        self.manifest.write_text(
            re.sub(r'sha256: "[0-9a-f]{64}"', f'sha256: "{new_sha}"', manifest_text),
            encoding="utf-8")

    def test_push_consumer_without_evidence_caught(self) -> None:
        self.rewrite(AGENT_REL, "Push target: protocol/instruments/test-instrument.md",
                     "Push target: (none)")
        self.reregister_agent_hash()
        self.assert_error_containing("no routing evidence")

    def test_planned_consumer_downgrades_to_warning(self) -> None:
        self.rewrite(AGENT_REL, "Push target: protocol/instruments/test-instrument.md",
                     "Push target: (none)")
        self.reregister_agent_hash()
        self.rewrite("manifest.yaml", "      - agent: test-assessor\n        mechanism: push",
                     "      - agent: test-assessor\n        mechanism: push\n"
                     "        status: planned")
        report = self.run_checks()
        self.assertEqual(report.errors, [])
        self.assertTrue(any("planned" in w for w in report.warnings))

    def test_agent_hash_mismatch_caught(self) -> None:
        path = self.root / AGENT_REL
        path.write_text(path.read_text(encoding="utf-8") + "\nHot-reloaded edit.\n",
                        encoding="utf-8")
        self.assert_error_containing("hash mismatch")

    def test_unregistered_agent_caught(self) -> None:
        (self.root / ".claude/agents/rogue-agent.md").write_text("---\nname: rogue\n---\n",
                                                                 encoding="utf-8")
        self.assert_error_containing("unregistered agent definition")

    def test_missing_model_pin_caught(self) -> None:
        self.rewrite(AGENT_REL, "model: claude-test-1-20260101\n", "")
        self.reregister_agent_hash()
        self.assert_error_containing("no 'model:' pin")

    def test_inherit_model_pin_caught(self) -> None:
        self.rewrite(AGENT_REL, "model: claude-test-1-20260101", "model: inherit")
        self.reregister_agent_hash()
        self.assert_error_containing("model pin is 'inherit'")

    def test_model_pin_drift_caught(self) -> None:
        self.rewrite("manifest.yaml", 'file: {AGENT}'.replace("{AGENT}", AGENT_REL),
                     f"file: {AGENT_REL}\n    model: claude-other-model")
        self.assert_error_containing("model-pin drift")

    def test_memory_frontmatter_caught(self) -> None:
        self.rewrite(AGENT_REL, "model: claude-test-1-20260101",
                     "model: claude-test-1-20260101\nmemory: project")
        self.reregister_agent_hash()
        self.assert_error_containing("'memory:' frontmatter is prohibited")

    def test_duplicate_receipt_tokens_caught(self) -> None:
        second = CANONICAL_TEXT.replace("Test instrument", "Second instrument")
        (self.root / "protocol/instruments/second-instrument.md").write_text(
            second, encoding="utf-8")
        self.rewrite("manifest.yaml", "agent_definitions:",
                     """  second-instrument:
    canonical_file: protocol/instruments/second-instrument.md
    version: "1.0"
    receipt_token: "feedfacecafebeef"
agent_definitions:""")
        self.assert_error_containing("tokens must be unique")


if __name__ == "__main__":
    unittest.main(verbosity=2)
