#!/usr/bin/env python3
"""Unit tests for the effort-pinning build (launcher v1.2, workflow v1.5,
assembler v1.4).

Reasoning effort was session-inherited and attestation-only through the D3
cycle (2026-08-17); the pinning build makes it a launched, transcript-visible,
assembler-verified value. These tests pin three things:

1. The cross-file format contracts: the workflow's injected prompt lines are
   the single source of format truth for the assembler's PROVENANCE_RE and
   PROMPT_RE and the reconciler's PACK_DECLARATION_RE — each template is
   extracted from the workflow source and matched against the live regex, so
   an edit to either side alone fails here.
2. The assembler's provenance parsing and arm-level derivation (mixed-vintage
   hard error).
3. The launcher's launch-commit resolution (dirty-tracked-tree refusal;
   untracked files ignored).

Run: ``venv/bin/python -m pytest tests/test_effort_pinning.py -q``
"""

from __future__ import annotations

import importlib.machinery
import importlib.util
import json
import re
import subprocess
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
WORKFLOW_JS = (REPO_ROOT / "studies" / "open-science-compliance" / "protocol"
               / "validation" / "fair-benchmark-arm.workflow.js")


def load_script(name: str, filename: str):
    """Import a hyphen-named script as a module (test_reconcile pattern)."""
    spec = importlib.util.spec_from_loader(
        name, importlib.machinery.SourceFileLoader(
            name, str(REPO_ROOT / "scripts" / filename)))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


assembler = load_script("assemble_arm_record", "assemble-arm-record.py")
launcher = load_script("build_benchmark_args", "build-benchmark-args.py")
reconciler = load_script("reconcile_run", "reconcile-run.py")

DUMMY_COMMIT = "a" * 40
DUMMY_SHA256 = "b" * 64


def render_workflow_template(marker: str) -> str:
    """Extract the backtick template line containing ``marker`` from the
    workflow source and substitute dummy values for its ``${...}`` slots."""
    source = WORKFLOW_JS.read_text(encoding="utf-8")
    # Require a ${...} slot so quoted mentions of a line (e.g. the reconcile
    # prompt's disambiguation instruction) are not mistaken for the template.
    lines = [ln for ln in source.splitlines()
             if marker in ln and "`" in ln and "${" in ln]
    assert len(lines) == 1, f"expected exactly one template line for {marker!r}"
    template = lines[0].split("`")[1]  # the backtick-quoted segment
    substitutions = {
        "${arm}": "sonnet-5", "${t.run}": "2", "${t.slug}": "dye-et-al-2023",
        "${t.path}": "/home/user/corpora/x/vor.pdf", "${t.pack}": "corpus/evidence-packs/x.json",
        "${t.pack_sha256}": DUMMY_SHA256, "${launch_commit}": DUMMY_COMMIT,
        "${effort}": "max",
    }
    for slot, value in substitutions.items():
        template = template.replace(slot, value)
    assert "${" not in template, f"unsubstituted slot in template: {template}"
    return template.replace("\\n", "\n")


class FormatContractTests(unittest.TestCase):
    """Workflow prompt templates match the Python-side regexes."""

    def test_provenance_line_matches_assembler_regex(self):
        line = render_workflow_template("Provenance: launch commit")
        match = assembler.PROVENANCE_RE.search(line)
        self.assertIsNotNone(match)
        self.assertEqual(match.group(1), DUMMY_COMMIT)
        self.assertEqual(match.group(2), "max")

    def test_pack_line_matches_reconciler_regex(self):
        line = render_workflow_template("Evidence pack (read in full)")
        match = reconciler.PACK_DECLARATION_RE.search(line)
        self.assertIsNotNone(match)
        self.assertEqual(match.group(2), DUMMY_SHA256)

    def test_identity_lines_match_assembler_prompt_regex(self):
        header = render_workflow_template("Benchmark scoring task")
        paper = render_workflow_template("Source (read in full)")
        match = assembler.PROMPT_RE.search(header + paper)
        self.assertIsNotNone(match)
        self.assertEqual(match.group(1), "sonnet-5")
        self.assertEqual(match.group(2), "2")
        self.assertEqual(match.group(3), "dye-et-al-2023")

    def test_workflow_pins_effort_in_scoring_opts(self):
        source = WORKFLOW_JS.read_text(encoding="utf-8")
        self.assertRegex(source, r"agent\(scorePrompt\(t\), \{ agentType, effort,")
        self.assertIn("launch_commit, papers, schema }", source)


class ProvenanceParsingTests(unittest.TestCase):
    """transcript_provenance against realistic transcript encodings."""

    def test_parses_json_escaped_prompt(self):
        prompt = (f"Benchmark scoring task (preregistered validation phase, "
                  f"arm opus-5, run 1 of 3).\n"
                  f"Paper: marwick-2025. Source (read in full): /x/vor.pdf\n"
                  f"Evidence pack (read in full): corpus/p.json (sha256 {DUMMY_SHA256})\n"
                  f"Provenance: launch commit {DUMMY_COMMIT}; "
                  f"reasoning effort pinned: xhigh.\n")
        transcript_line = json.dumps({"message": {"content": prompt}})
        self.assertEqual(assembler.transcript_provenance(transcript_line),
                         (DUMMY_COMMIT, "xhigh"))

    def test_absent_line_returns_none(self):
        self.assertIsNone(assembler.transcript_provenance(
            "arm opus-5, run 1 of 3).\nPaper: marwick-2025."))

    def test_rejects_non_enum_effort(self):
        for bad in ("maximum", "Max", "ultra", ""):
            line = (f"Provenance: launch commit {DUMMY_COMMIT}; "
                    f"reasoning effort pinned: {bad}.")
            self.assertIsNone(assembler.transcript_provenance(line), bad)

    def test_rejects_short_commit(self):
        line = ("Provenance: launch commit abc123; "
                "reasoning effort pinned: max.")
        self.assertIsNone(assembler.transcript_provenance(line))


class DeriveArmProvenanceTests(unittest.TestCase):
    """Arm-level consistency: uniform, pre-pinning, and mixed cases."""

    def test_uniform_values_derive(self):
        values = [(DUMMY_COMMIT, "max")] * 15
        self.assertEqual(assembler.derive_arm_provenance(values),
                         (DUMMY_COMMIT, "max"))

    def test_all_absent_derives_nulls(self):
        self.assertEqual(assembler.derive_arm_provenance([None] * 15),
                         (None, None))

    def test_mixed_efforts_raise(self):
        values = [(DUMMY_COMMIT, "max")] * 14 + [(DUMMY_COMMIT, "high")]
        with self.assertRaises(ValueError):
            assembler.derive_arm_provenance(values)

    def test_absent_beside_present_raises(self):
        values = [(DUMMY_COMMIT, "max")] * 14 + [None]
        with self.assertRaises(ValueError):
            assembler.derive_arm_provenance(values)

    def test_mixed_commits_raise(self):
        values = [(DUMMY_COMMIT, "max"), ("c" * 40, "max")]
        with self.assertRaises(ValueError):
            assembler.derive_arm_provenance(values)


class ResolveLaunchCommitTests(unittest.TestCase):
    """Launcher dirty-tree refusal in a throwaway git repository."""

    def _git(self, repo: Path, *argv: str) -> None:
        subprocess.run(
            ["git", "-C", str(repo), "-c", "user.name=t",
             "-c", "user.email=t@example.invalid", *argv],
            check=True, capture_output=True)

    def _repo_with_commit(self, tmp: str) -> Path:
        repo = Path(tmp)
        self._git(repo, "init", "-q")
        (repo / "tracked.txt").write_text("v1\n")
        self._git(repo, "add", "tracked.txt")
        self._git(repo, "commit", "-qm", "initial")
        return repo

    def test_clean_tree_returns_head(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = self._repo_with_commit(tmp)
            commit = launcher.resolve_launch_commit(repo)
            self.assertTrue(re.fullmatch(r"[0-9a-f]{40}", commit))

    def test_modified_tracked_file_refused(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = self._repo_with_commit(tmp)
            (repo / "tracked.txt").write_text("v2\n")
            with self.assertRaises(RuntimeError):
                launcher.resolve_launch_commit(repo)

    def test_staged_change_refused(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = self._repo_with_commit(tmp)
            (repo / "tracked.txt").write_text("v2\n")
            self._git(repo, "add", "tracked.txt")
            with self.assertRaises(RuntimeError):
                launcher.resolve_launch_commit(repo)

    def test_untracked_file_ignored(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = self._repo_with_commit(tmp)
            (repo / "untracked-args.json").write_text("{}\n")
            commit = launcher.resolve_launch_commit(repo)
            self.assertTrue(re.fullmatch(r"[0-9a-f]{40}", commit))


if __name__ == "__main__":
    unittest.main()
