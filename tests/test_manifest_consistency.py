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

# The mirrored body is defined once and interpolated into both fixture files,
# so the baseline is byte-identical by construction and any divergence a test
# asserts on is unambiguously the injected one.
MIRRORED_BODY = """## Rubric

```text
CRITERION (max 2):
  C1: First criterion   /1
  C2: Second criterion  /1
```

Unscoreable criteria score 0 — prose the structural check cannot see.

## Bands

| Score | Rating |
|-------|--------|
| 2 | Good |
| 0-1 | Poor |
"""

CANONICAL_TEXT = f"""# Test instrument v1.0 — canonical file

**Status: FROZEN by OSF registration** — governance applies.
**Version:** 1.0 (fixture)

<!-- canon-begin: test-instrument -->
{MIRRORED_BODY}<!-- canon-end: test-instrument -->

---

Receipt-token: feedfacecafebeef
"""

MIRROR_TEXT = f"""# Test mirror prompt

> Canonical home: `protocol/instruments/test-instrument.md`
> (v1.0, receipt token `feedfacecafebeef`, FROZEN).

Human-lane framing prose may differ outside the mirrored region.

<!-- mirror-begin: test-instrument -->
{MIRRORED_BODY}<!-- mirror-end: test-instrument -->

Workflow guidance that is not instrument may follow the region.
"""

AGENT_TEXT = """---
name: test-assessor
model: claude-test-1-20260101
---

Push target: protocol/instruments/test-instrument.md
"""


def build_manifest(agent_sha: str) -> str:
    """Return fixture manifest text with the given agent-definition hash."""
    return f"""shared_content_policy:
  scan_directories:
    - protocol/instruments
  scan_exclusions:
    - README.md
shared_content:
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

    # --- mirror region (byte-exact) -------------------------------------
    # These cover the gap that let the Pass 6 prompt drop four normative
    # statements while every fenced block and table row still matched
    # (erratum-log Entry 2, 2026-07-27).

    def test_mirror_prose_divergence_caught(self) -> None:
        """A prose-only edit inside the region fails, though blocks/rows match."""
        self.rewrite(MIRROR_REL,
                     "Unscoreable criteria score 0 — prose the structural check cannot see.",
                     "Unscoreable criteria are skipped.")
        self.assert_error_containing("not byte-identical to canon")

    def test_mirror_prose_deletion_caught(self) -> None:
        """Deleting a normative sentence from the mirror fails."""
        self.rewrite(MIRROR_REL,
                     "\nUnscoreable criteria score 0 — prose the structural check cannot see.\n",
                     "\n")
        self.assert_error_containing("not byte-identical to canon")

    def test_mirror_whitespace_drift_caught(self) -> None:
        """Byte-exactness means trailing whitespace counts too."""
        self.rewrite(MIRROR_REL, "| 2 | Good |", "| 2 | Good | ")
        self.assert_error_containing("not byte-identical to canon")

    def test_missing_canon_markers_caught(self) -> None:
        """An unmarked canonical file is unverifiable, not silently passing."""
        self.rewrite(CANONICAL_REL, "<!-- canon-begin: test-instrument -->\n", "")
        self.assert_error_containing("marker pair — mirror unverifiable")

    def test_missing_mirror_markers_caught(self) -> None:
        """An unmarked mirror is unverifiable, not silently passing."""
        self.rewrite(MIRROR_REL, "<!-- mirror-begin: test-instrument -->\n", "")
        self.assert_error_containing("marker pair — mirror unverifiable")

    def test_prose_outside_region_is_allowed(self) -> None:
        """Lane-specific framing outside the markers must not fail the check."""
        self.rewrite(MIRROR_REL,
                     "Workflow guidance that is not instrument may follow the region.",
                     "Entirely different human-lane workflow guidance.")
        report = self.run_checks()
        self.assertEqual(report.errors, [])

    def test_structural_mode_warns_and_skips_region(self) -> None:
        """Declared-weaker mode passes prose divergence but announces the gap."""
        self.rewrite("manifest.yaml", f"        mirror_file: {MIRROR_REL}",
                     f"        mirror_file: {MIRROR_REL}\n        mirror_mode: structural")
        self.rewrite(MIRROR_REL,
                     "Unscoreable criteria score 0 — prose the structural check cannot see.",
                     "Unscoreable criteria are skipped.")
        report = self.run_checks()
        self.assertEqual(report.errors, [])
        self.assertTrue(any("structural" in w and "NOT detected" in w
                            for w in report.warnings),
                        f"expected the weaker-guarantee warning, got: {report.warnings}")

    def test_unknown_mirror_mode_caught(self) -> None:
        self.rewrite("manifest.yaml", f"        mirror_file: {MIRROR_REL}",
                     f"        mirror_file: {MIRROR_REL}\n        mirror_mode: sloppy")
        self.assert_error_containing("unknown mirror_mode")

    # --- reverse sweep ---------------------------------------------------

    def test_unregistered_instrument_file_caught(self) -> None:
        """A new instrument nobody registered must not be invisible."""
        stray = self.root / "protocol/instruments/unregistered-instrument.md"
        stray.write_text("# Stray\n", encoding="utf-8")
        self.assert_error_containing("unregistered instrument file")

    def test_scan_exclusion_respected(self) -> None:
        """Excluded filenames (README.md) do not trip the sweep."""
        (self.root / "protocol/instruments/README.md").write_text("# Index\n", encoding="utf-8")
        report = self.run_checks()
        self.assertEqual(report.errors, [])

    def test_absent_scan_policy_warns(self) -> None:
        """Without scan_directories the sweep cannot run — say so, don't imply cover."""
        self.rewrite("manifest.yaml",
                     "shared_content_policy:\n  scan_directories:\n    - protocol/instruments\n"
                     "  scan_exclusions:\n    - README.md\n", "")
        report = self.run_checks()
        self.assertTrue(any("no reverse sweep" in w for w in report.warnings),
                        f"expected a no-sweep warning, got: {report.warnings}")

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
