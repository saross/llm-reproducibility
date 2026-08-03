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

# Entity-check fixtures (monitoring plan Phase 2): one entity per class
# E3-E8, each with its declared carrier, so every class has a green
# baseline to inject a defect into.
GUIDE_REL = "docs/guide.md"
GUIDE_TEXT = "# Fixture guide\n\n**Version:** v1.0\n\nProse.\n"
DATASPEC_REL = "schema/data.json"
DATASPEC_TEXT = '{"version": "1.0", "title": "fixture"}\n'
TWOAXIS_REL = "docs/twoaxis.md"
TWOAXIS_TEXT = ('# Two-axis fixture\n\n**Version:** 9.9\n\n'
                'The payload stamps "schema_version": "1.0" into outputs.\n')
README_FIXTURE_REL = "docs/readme-fixture.md"
REFITEM_REL = "outputs/t1/extraction.json"
REFITEM_TEXT = '{"infrastructure": {"fair_assessment": {"scale": "fixture"}}}\n'


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
components:
  guide:
    version: "1.0"
    file: {GUIDE_REL}
  dataspec:
    version: "1.0"
    file: {DATASPEC_REL}
  twoaxis:
    version: "1.0"
    file: {TWOAXIS_REL}
documentation:
  readme_fixture: {README_FIXTURE_REL}
reference_datasets:
  test_refset:
    cardinality: 1
    items:
      - slug: t1
        file: {REFITEM_REL}
        fair_key: infrastructure.fair_assessment
entity_checks:
  shared_content.test-instrument: {{class: E1}}
  agent_definitions.test-assessor: {{class: E2}}
  components.guide: {{class: E3, version_source: markdown-header, normalise: strip-v-prefix}}
  components.dataspec: {{class: E4, version_source: json-field, json_path: $.version}}
  components.twoaxis: {{class: E5, axis: payload, version_source: markdown-body-pattern, pattern: '"schema_version": "{{version}}"'}}
  documentation.readme_fixture: {{class: E6, verify: exists}}
  reference_datasets.test_refset: {{class: E8, verify: enumerate-from-registry, assert_cardinality: true}}
"""


class ManifestConsistencyTests(unittest.TestCase):
    """One green baseline, then one injected defect per test."""

    def setUp(self) -> None:
        self.root = Path(tempfile.mkdtemp(prefix="d5-fixture-"))
        self.addCleanup(shutil.rmtree, self.root, ignore_errors=True)
        for rel, text in ((CANONICAL_REL, CANONICAL_TEXT),
                          (MIRROR_REL, MIRROR_TEXT),
                          (AGENT_REL, AGENT_TEXT),
                          (GUIDE_REL, GUIDE_TEXT),
                          (DATASPEC_REL, DATASPEC_TEXT),
                          (TWOAXIS_REL, TWOAXIS_TEXT),
                          (README_FIXTURE_REL, "# Fixture readme\n"),
                          (REFITEM_REL, REFITEM_TEXT)):
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
        self.assert_error_containing("canonical file carries no")

    def test_missing_mirror_markers_caught(self) -> None:
        """An unmarked mirror is unverifiable, not silently passing."""
        self.rewrite(MIRROR_REL, "<!-- mirror-begin: test-instrument -->\n", "")
        self.assert_error_containing("carries no")

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

    # --- multi-segment mirrors -------------------------------------------
    # For mirrors whose canonical content lands in several places in the
    # consuming document (reproduction-assessor SKILL.md sections C, E, F, H).

    def segment_the_fixture(self) -> None:
        """Split the single region into two named segments in both files."""
        for rel, kind in ((CANONICAL_REL, "canon"), (MIRROR_REL, "mirror")):
            path = self.root / rel
            text = path.read_text(encoding="utf-8")
            text = text.replace(
                f"<!-- {kind}-begin: test-instrument -->\n## Rubric",
                f"<!-- {kind}-begin: test-instrument#rubric -->\n## Rubric")
            text = text.replace(
                "\n## Bands",
                f"<!-- {kind}-end: test-instrument#rubric -->\n\n"
                f"<!-- {kind}-begin: test-instrument#bands -->\n## Bands")
            text = text.replace(
                f"<!-- {kind}-end: test-instrument -->",
                f"<!-- {kind}-end: test-instrument#bands -->")
            path.write_text(text, encoding="utf-8")

    def test_segmented_mirror_baseline_passes(self) -> None:
        self.segment_the_fixture()
        report = self.run_checks()
        self.assertEqual(report.errors, [])

    def test_segment_missing_from_mirror_caught(self) -> None:
        """Canon declares a segment the mirror never carries."""
        self.segment_the_fixture()
        self.rewrite(MIRROR_REL, "<!-- mirror-begin: test-instrument#bands -->\n", "")
        self.rewrite(MIRROR_REL, "<!-- mirror-end: test-instrument#bands -->\n", "")
        self.assert_error_containing("missing canonical segment 'test-instrument#bands'")

    def test_segment_not_in_canon_caught(self) -> None:
        """The mirror claims a segment canon does not define."""
        self.segment_the_fixture()
        self.rewrite(MIRROR_REL, "<!-- mirror-end: test-instrument#bands -->",
                     "<!-- mirror-end: test-instrument#bands -->\n"
                     "<!-- mirror-begin: test-instrument#invented -->\n"
                     "Invented content.\n"
                     "<!-- mirror-end: test-instrument#invented -->")
        self.assert_error_containing("declares segment 'test-instrument#invented'")

    def test_per_segment_divergence_caught(self) -> None:
        """A prose edit inside one segment names that segment in the error."""
        self.segment_the_fixture()
        self.rewrite(MIRROR_REL,
                     "Unscoreable criteria score 0 — prose the structural check cannot see.",
                     "Unscoreable criteria are skipped.")
        self.assert_error_containing("segment 'test-instrument#rubric' is not byte-identical")

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

    # --- entity checks (monitoring plan Phase 2, 2026-08-03) -------------
    # One injected defect per class, per the plan's negative-test rule:
    # every new check is demonstrated to fail before it is trusted to pass.

    def test_missing_entity_checks_section_caught(self) -> None:
        """A manifest without entity_checks fails — coverage is not optional."""
        manifest_text = self.manifest.read_text(encoding="utf-8")
        head = manifest_text.split("entity_checks:")[0]
        self.manifest.write_text(head, encoding="utf-8")
        self.assert_error_containing("no entity_checks section")

    def test_undeclared_entity_caught(self) -> None:
        """A registry entry with no check declaration fails the gate (plan §5)."""
        (self.root / "docs/orphan.md").write_text("**Version:** 1.0\n", encoding="utf-8")
        self.rewrite("manifest.yaml", "  dataspec:",
                     "  orphan:\n    version: \"1.0\"\n    file: docs/orphan.md\n  dataspec:")
        self.assert_error_containing("undeclared entity: components.orphan")

    def test_unresolvable_check_entry_caught(self) -> None:
        """A check declaration pointing at nothing is stale, not ignorable."""
        self.rewrite("manifest.yaml", "entity_checks:",
                     "entity_checks:\n  components.ghost: {class: E3}")
        self.assert_error_containing("entity_checks.components.ghost: does not resolve")

    def test_class_mismatch_caught(self) -> None:
        """Declaring E1 for a non-shared_content entity is a classification error."""
        self.rewrite("manifest.yaml",
                     "  components.guide: {class: E3, version_source: markdown-header, "
                     "normalise: strip-v-prefix}",
                     "  components.guide: {class: E1}")
        self.assert_error_containing("class E1 declared for a non-shared_content")

    def test_e3_version_drift_caught(self) -> None:
        """E3: a prose artefact whose header moves off the registered version."""
        self.rewrite(GUIDE_REL, "**Version:** v1.0", "**Version:** v2.0")
        self.assert_error_containing("entity_checks.components.guide: version drift")

    def test_e3_v_prefix_normalisation_is_declared_not_automatic(self) -> None:
        """Removing the declared normalise rule makes the v-prefix a drift."""
        self.rewrite("manifest.yaml", ", normalise: strip-v-prefix}", "}")
        self.assert_error_containing("entity_checks.components.guide: version drift")

    def test_e4_json_version_drift_caught(self) -> None:
        """E4: a JSON schema whose version field moves off the manifest."""
        self.rewrite(DATASPEC_REL, '"version": "1.0"', '"version": "2.0"')
        self.assert_error_containing("entity_checks.components.dataspec: version drift")

    def test_e4_missing_json_field_caught(self) -> None:
        """E4: a schema with no version field is unverifiable, not passing."""
        self.rewrite(DATASPEC_REL, '"version": "1.0", ', "")
        self.assert_error_containing("has no $.version field")

    def test_e5_tracked_axis_drift_caught(self) -> None:
        """E5: the declared payload axis drifts; the document axis stays out of it."""
        self.rewrite(TWOAXIS_REL, '"schema_version": "1.0"', '"schema_version": "9.9"')
        self.assert_error_containing("declared axis pattern")

    def test_e5_other_axis_ignored(self) -> None:
        """E5: moving the document-version axis alone must NOT fail the check."""
        self.rewrite(TWOAXIS_REL, "**Version:** 9.9", "**Version:** 10.0")
        report = self.run_checks()
        self.assertEqual(report.errors, [],
                         f"document-axis edit must not trip the payload check: {report.errors}")

    def test_e6_missing_file_caught(self) -> None:
        """E6: a declared-unversioned file that vanishes is an error, not silence."""
        (self.root / README_FIXTURE_REL).unlink()
        self.assert_error_containing("declared-unversioned file missing")

    def test_e8_cardinality_drift_caught(self) -> None:
        """E8: the registry must list exactly the asserted number of items."""
        self.rewrite("manifest.yaml", "    cardinality: 1", "    cardinality: 2")
        self.assert_error_containing("cardinality drift")

    def test_e8_declared_key_unresolvable_caught(self) -> None:
        """E8: an item whose declared key no longer resolves fails loudly."""
        self.rewrite(REFITEM_REL, '"fair_assessment"', '"renamed_assessment"')
        self.assert_error_containing("declared key 'infrastructure.fair_assessment' "
                                     "does not resolve")

    def test_e8_missing_item_file_caught(self) -> None:
        """E8: a reference item whose file is gone fails, not shrinks the set."""
        (self.root / REFITEM_REL).unlink()
        self.assert_error_containing("item 't1' file missing")

    def test_coverage_self_report_generated(self) -> None:
        """Phase 3: coverage is generated from the registry, never asserted."""
        report = self.run_checks()
        self.assertIn("7/7 entities checked", report.coverage)
        for fragment in ("E1:1", "E2:1", "E3:1", "E4:1", "E5:1", "E6:1", "E8:1"):
            self.assertIn(fragment, report.coverage,
                          f"expected {fragment!r} in: {report.coverage}")
        self.assertIn("0 undeclared", report.coverage)

    def test_coverage_counts_undeclared(self) -> None:
        """Phase 3: an undeclared entity shows in the coverage line, not just errors."""
        (self.root / "docs/orphan.md").write_text("**Version:** 1.0\n", encoding="utf-8")
        self.rewrite("manifest.yaml", "  dataspec:",
                     "  orphan:\n    version: \"1.0\"\n    file: docs/orphan.md\n  dataspec:")
        report = self.run_checks()
        self.assertIn("7/8 entities checked", report.coverage)
        self.assertIn("1 undeclared", report.coverage)


if __name__ == "__main__":
    unittest.main(verbosity=2)
