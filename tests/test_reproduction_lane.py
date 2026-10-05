#!/usr/bin/env python3
"""Unit tests for the reproduction-lane orchestration helpers (v1.0).

``scripts/reproduction-lane.py`` carries every check the reproduction
workflows cannot make themselves (workflow scripts have no filesystem
access). These tests pin:

1. The cross-file format contracts: the prompt lines in
   ``reproduction-system/workflows/*.workflow.js`` are the single source of
   truth for the tool's PROVENANCE_RE, PAPER_RE, SCRATCH_RE, and
   ATTEMPT_DIR_RE — each template is extracted from the workflow source and
   matched against the live regex, so an edit to one side alone fails here.
2. The artefact gate (``check_attempt``): invariant 3's one-to-one target
   match, recomputed coverage, the BLOCKED rule, the corpus rule, and
   required artefacts; and the authors'-code integrity check (gate 1.2):
   provenance anchors, execution snapshots, wrapper references, conversion
   evidence, the legacy allowlist, and the authoritative human queue,
   including the two attack cases from the cross-model review of PR #7.
3. Plan-level checks, result binding, the approval hash lock, and the
   review overall-verdict rule.
4. The audit: per-request token deduplication, pricing, and blinded-path
   detection across Read and Bash (URL paths excluded).
5. The args checksum: the workflows' own JavaScript, run in Node, agrees
   with the Python builder (skipped when Node is absent).

Run: ``venv/bin/python -m pytest tests/test_reproduction_lane.py -q``
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.machinery
import importlib.util
import json
import os
import re
import shutil
import subprocess
import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest import mock

REPO_ROOT = Path(__file__).resolve().parent.parent
WORKFLOWS = REPO_ROOT / "reproduction-system" / "workflows"
COMPARISON_SCHEMA = REPO_ROOT / "reproduction-system" / "schemas" / "comparison-record.json"


def load_script(name: str, filename: str):
    """Import a hyphen-named script as a module (test_reconcile pattern)."""
    spec = importlib.util.spec_from_loader(
        name, importlib.machinery.SourceFileLoader(
            name, str(REPO_ROOT / "scripts" / filename)))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


lane = load_script("reproduction_lane", "reproduction-lane.py")

DUMMY_COMMIT = "a" * 40


def render_template(workflow: str, marker: str) -> str:
    """Extract the backtick template containing ``marker`` from a workflow
    source and substitute dummy values for its ``${...}`` slots."""
    source = (WORKFLOWS / workflow).read_text(encoding="utf-8")
    line = next(row for row in source.splitlines() if marker in row and "`" in row)
    template = line[line.index("`") + 1:line.rindex("`")]
    values = {"run_id": "run-x", "launch_commit": DUMMY_COMMIT, "effort": "high",
              "p.slug": "some-paper-2024", "p.scratch_dir": "/tmp/scratch/planner",
              "p.executor_scratch_dir": "/tmp/scratch/executor",
              "p.attempt_dir": "/repo/outputs/some-paper-2024/reproduction/attempt-02"}
    return re.sub(r"\$\{([^}]+)\}", lambda m: values.get(m.group(1), "X"), template)


def plan_record(target_ids: list[str], slug: str = "some-paper-2024") -> dict:
    """A minimal persisted plan record with the given target ids."""
    return {"plan_record_version": "1.0", "plan": {
        "status": "OK", "paper_slug": slug,
        "verification_targets": [{"target_id": t} for t in target_ids]}}


def write(path: Path, text: str = "x\n") -> None:
    """Create a file (and parents) with content."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def sha(text: str) -> str:
    """sha256 of a UTF-8 string, as the manifest records it."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


# An authors' script long enough to identify when a wrapper inlines it.
AUTHORS_R = "".join(f"result_{i} <- compute_statistic(data, index = {i})\n"
                    for i in range(1, 9))


# The evidence-pack anchor every fixture original carries: the deposit's own
# file analysis.R, whose md5 the committed pack publishes.
ANCHOR = {"kind": "evidence-pack", "pack": "packs/some-paper-2024.json",
          "record_id": "zenodo:10.5281/zenodo.101", "file": "analysis.R"}


def clean_git_env() -> dict[str, str]:
    """The environment minus every inherited ``GIT_*`` variable.

    Git exports GIT_DIR and GIT_INDEX_FILE to hook processes. When the suite
    runs from the pre-commit gate they override ``git -C``, so a fixture's
    init, add, and commit act on the repository being committed, not the
    temporary one. On 2026-10-05 this set core.bare in the shared config and
    committed a "fixture" tree over a worktree branch (repaired the same day;
    the same class as test_effort_pinning's 2026-09-23 note).
    """
    return {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}


def git(repo: Path, *args: str) -> None:
    """Run git quietly in a fixture repository, never in an inherited one."""
    subprocess.run(["git", "-C", str(repo), "-c", "user.name=t", "-c", "user.email=t@t",
                    *args], check=True, capture_output=True, env=clean_git_env())


def anchor_repo(root: Path, scored_version: str = "10.5281/zenodo.101",
                checksum_of: str = AUTHORS_R) -> Path:
    """A committed repository holding a registry and an evidence pack.

    The registry selects ``scored_version`` for some-paper-2024; the pack's
    record 10.5281/zenodo.101 publishes the md5 of ``checksum_of`` for its
    file analysis.R. Provenance anchors are verified against these.
    """
    repo = root / "anchor-repo"
    write(repo / "corpus" / "evidence-packs" / "declared-links.yaml", json.dumps(
        {"papers": {"some-paper-2024": {"links": [
            {"id": "deposit", "type": "data+code", "link": "10.5281/zenodo.100",
             "role": "principal", "home": "repository",
             "scored_version": scored_version}]}}}))
    write(repo / "packs" / "some-paper-2024.json", json.dumps({"records": [
        {"record_id": "zenodo:10.5281/zenodo.101", "status": "resolved",
         "fields": {"doi": "10.5281/zenodo.101", "files": [
             {"key": "analysis.R",
              "checksum": "md5:" + hashlib.md5(checksum_of.encode()).hexdigest()}]}}]}))
    git(repo, "init", "-q")
    git(repo, "add", ".")
    git(repo, "commit", "-q", "-m", "fixture")
    return repo


def snapshot(attempt: Path) -> None:
    """Take both execution snapshots of the attempt as it stands (a clean run)."""
    lane.write_snapshot(attempt, "pre", force=True)
    lane.write_snapshot(attempt, "post", force=True)


def write_code_manifest(attempt: Path, **overrides) -> dict:
    """A valid authors'-code manifest for the GateTests fixture.

    One authors' original kept pristine under ``authors-code-raw/`` and executed
    from ``authors-code/`` byte-identical, anchored to a committed evidence
    pack; the fixture's run script and Dockerfile are declared wrappers.
    """
    write(attempt / "authors-code-raw" / "analysis.R", AUTHORS_R)
    write(attempt / "authors-code" / "analysis.R", AUTHORS_R)
    manifest = {"manifest_version": "1.1", "paper_slug": "some-paper-2024",
                "originals": [{"id": "analysis.R", "sha256": sha(AUTHORS_R),
                               "source": "https://zenodo.org/records/101/files/analysis.R",
                               "retrieved_at": "2026-10-04T00:00:00Z",
                               "local_copy": "authors-code-raw/analysis.R",
                               "anchor": dict(ANCHOR)}],
                "executed": [{"path": "authors-code/analysis.R", "original": "analysis.R"}],
                "wrappers": [{"path": "run-analysis.R", "role": "wrapper",
                              "purpose": "sources the authors' file"},
                             {"path": "Dockerfile", "role": "environment",
                              "purpose": "pinned environment"}]}
    manifest.update(overrides)
    write(attempt / lane.CODE_MANIFEST_FILE, json.dumps(manifest))
    return manifest


class FormatContracts(unittest.TestCase):
    """Workflow prompt lines must match the tool's regexes."""

    def test_provenance_line_both_workflows(self):
        for workflow in ("reproduction-plan.workflow.js",
                         "reproduction-execute.workflow.js"):
            rendered = render_template(workflow, "Provenance: run")
            match = lane.PROVENANCE_RE.search(rendered)
            self.assertIsNotNone(match, workflow)
            self.assertEqual(match.group(2), DUMMY_COMMIT)
            self.assertEqual(match.group(3), "high")

    def test_paper_line(self):
        for workflow in ("reproduction-plan.workflow.js",
                         "reproduction-execute.workflow.js"):
            rendered = render_template(workflow, "`Paper: ${p.slug}")
            self.assertEqual(lane.PAPER_RE.search(rendered.replace("\\n", "\n")).group(1),
                             "some-paper-2024")

    def test_scratch_and_attempt_lines(self):
        rendered = render_template("reproduction-plan.workflow.js", "Scratch directory:")
        self.assertIsNotNone(lane.SCRATCH_RE.search(rendered.replace("\\n", "\n")))
        rendered = render_template("reproduction-execute.workflow.js", "`Attempt directory:")
        self.assertIsNotNone(lane.ATTEMPT_DIR_RE.search(rendered.replace("\\n", "\n")))

    def test_harness_wrapped_prompt(self):
        # Claude Code 2.1.288 wraps a workflow prompt: a relayed user request,
        # then the computed task with every line indented two spaces.
        relay = "[Workflow harness — user request] relayed:\n  please go"
        task = ("[Workflow harness — computed task] The computed task text follows:\n"
                "  Reproduction-lane planning task (run r, attempt 2).\n"
                "  Paper: a-2024\n"
                f"  Provenance: run r; launch commit {DUMMY_COMMIT}; "
                "reasoning effort pinned: high.\n"
                "  Scratch directory: /tmp/s\n")
        lines = [json.dumps({"message": {"role": "user", "content": relay}}),
                 json.dumps({"message": {"role": "user", "content": task}}),
                 json.dumps({"message": {"role": "assistant", "content": [
                     {"type": "text", "text": "Paper: other-2024"}]}})]
        prompt = lane.first_user_text(lines)
        self.assertEqual(lane.PAPER_RE.search(prompt).group(1), "a-2024")
        self.assertEqual(lane.PROVENANCE_RE.search(prompt).group(3), "high")
        self.assertEqual(lane.SCRATCH_RE.search(prompt).group(1), "/tmp/s")

    def test_planner_prompt_grants_no_write_root(self):
        # The planner must not get an "Attempt directory:" line — the audit
        # would read it as a permitted write root.
        source = (WORKFLOWS / "reproduction-plan.workflow.js").read_text(encoding="utf-8")
        self.assertNotIn("`Attempt directory:", source)


class GateTests(unittest.TestCase):
    """check_attempt(): the deterministic artefact gate."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self.tmp.name) / "attempt-02"
        for rel in ("Dockerfile", "environment.md", "log.md", "run-analysis.R",
                    "comparisons/comparison-report.md", "outputs/values.csv"):
            write(self.dir / rel)
        self.plan = Path(self.tmp.name) / "reproduction-plan.json"
        self.plan.write_text(json.dumps(plan_record(["T01", "T02"])), encoding="utf-8")
        self.schema = json.loads(COMPARISON_SCHEMA.read_text(encoding="utf-8"))
        write_code_manifest(self.dir)
        self.repo = anchor_repo(Path(self.tmp.name))
        snapshot(self.dir)

    def tearDown(self):
        self.tmp.cleanup()

    def comparison(self, **overrides) -> dict:
        record = {"schema_version": "1.0", "paper_slug": "some-paper-2024", "attempt": 2,
                  "plan_sha256": hashlib.sha256(self.plan.read_bytes()).hexdigest(),
                  "verdict": "SUCCESSFUL",
                  "targets": [
                      {"target_id": "T01", "outcome": "EXACT_MATCH", "testable": True,
                       "values_compared": 3, "values_matched": 3, "evidence": "procedure"},
                      {"target_id": "T02", "outcome": "WITHIN_PRECISION", "testable": True,
                       "values_compared": 1, "values_matched": 1, "evidence": "procedure"}],
                  "coverage": {"targets_enumerated": 2, "targets_reproduced": 2}}
        record.update(overrides)
        write(self.dir / "comparisons" / "comparison.json", json.dumps(record))
        return record

    def run_gate(self, **kwargs) -> dict:
        kwargs.setdefault("anchor_root", self.repo)
        return lane.check_attempt(self.dir, self.plan, self.schema, **kwargs)

    def test_clean_attempt_passes(self):
        self.comparison()
        report = self.run_gate()
        self.assertEqual(report["verdict"], "pass", report["errors"])
        self.assertEqual(report["coverage"]["coverage_fraction"], 1.0)

    def test_missing_locked_target_fails(self):
        record = self.comparison()
        record["targets"] = record["targets"][:1]
        record["coverage"] = {"targets_enumerated": 2, "targets_reproduced": 1}
        write(self.dir / "comparisons" / "comparison.json", json.dumps(record))
        report = self.run_gate()
        self.assertEqual(report["verdict"], "fail")
        self.assertTrue(any("invariant 3" in e for e in report["errors"]))

    def test_extra_target_fails(self):
        record = self.comparison()
        record["targets"].append(dict(record["targets"][0], target_id="T99"))
        write(self.dir / "comparisons" / "comparison.json", json.dumps(record))
        self.assertTrue(any("not in the locked plan" in e
                            for e in self.run_gate()["errors"]))

    def test_declared_coverage_must_match_recomputed(self):
        record = self.comparison()
        record["targets"][1]["outcome"] = "MINOR_DISCREPANCY"  # outside tolerance
        write(self.dir / "comparisons" / "comparison.json", json.dumps(record))
        report = self.run_gate()
        self.assertEqual(report["coverage"]["targets_reproduced"], 1)
        self.assertTrue(any("recomputed" in e for e in report["errors"]))

    def test_blocked_scores_zero(self):
        self.comparison(verdict="BLOCKED")
        self.assertTrue(any("BLOCKED" in e for e in self.run_gate()["errors"]))

    def test_untestable_needs_failure_mode(self):
        record = self.comparison()
        record["targets"][1].update(testable=False, outcome="CANNOT_COMPARE")
        record["coverage"] = {"targets_enumerated": 2, "targets_reproduced": 1}
        write(self.dir / "comparisons" / "comparison.json", json.dumps(record))
        self.assertTrue(any("failure_mode" in e for e in self.run_gate()["errors"]))

    def test_plan_hash_mismatch_fails(self):
        self.comparison(plan_sha256="0" * 64)
        self.assertTrue(any("plan_sha256" in e for e in self.run_gate()["errors"]))

    def test_publisher_file_inside_attempt_fails(self):
        self.comparison()
        write(self.dir / "materials" / "paper.pdf", "publisher bytes")
        digest = hashlib.sha256(b"publisher bytes").hexdigest()
        report = self.run_gate(forbid_sha256=(digest,))
        self.assertTrue(any("publisher file" in e for e in report["errors"]))

    def test_missing_artefacts_fail(self):
        self.comparison()
        (self.dir / "log.md").unlink()
        self.assertTrue(any("log.md" in e for e in self.run_gate()["errors"]))

    def test_gate_reports_code_integrity(self):
        self.comparison()
        report = self.run_gate()
        self.assertEqual(report["gate_version"], "1.2")
        self.assertEqual(report["code_integrity"]["status"], "identical", report["errors"])
        self.assertEqual(report["code_integrity"]["anchors"], {"analysis.R": "verified"})
        self.assertEqual(report["flags"], [])
        self.assertTrue(report["eligible_for_current_gate"])

    def test_gate_fails_on_undeclared_edit(self):
        """The T02 class: an index shifted inside the authors' file, undeclared."""
        self.comparison()
        write(self.dir / "authors-code" / "analysis.R",
              AUTHORS_R.replace("index = 4", "index = 3"))
        report = self.run_gate()
        self.assertEqual(report["verdict"], "fail")
        self.assertTrue(any("UNDECLARED DIFFERENCE" in e for e in report["errors"]))

    def test_gate_passes_declared_edit_with_flag_relayed_in_warnings(self):
        self.comparison()
        write(self.dir / "authors-code" / "analysis.R",
              AUTHORS_R.replace("index = 4", "index = 3"))
        manifest = json.loads((self.dir / lane.CODE_MANIFEST_FILE).read_text())
        manifest["executed"][0]["declared_edit"] = {
            "summary": "shifted an index", "kind": "repair", "affected_targets": ["T02"]}
        write(self.dir / lane.CODE_MANIFEST_FILE, json.dumps(manifest))
        snapshot(self.dir)  # the edit was made before the run
        report = self.run_gate()
        self.assertEqual(report["verdict"], "pass", report["errors"])
        self.assertEqual(report["code_integrity"]["status"], "flagged")
        self.assertTrue(any(w.startswith(lane.FLAG_EDIT_PREFIX) for w in report["warnings"]))
        # T02 is credited WITHIN_PRECISION in the fixture: a repaired result is flagged.
        self.assertTrue(any("target T02 is credited" in f for f in report["flags"]))

    def test_gate_missing_manifest_fails_unless_listed_legacy(self):
        self.comparison()
        (self.dir / lane.CODE_MANIFEST_FILE).unlink()
        self.assertEqual(self.run_gate()["verdict"], "fail")
        unlisted = Path(self.tmp.name) / "legacy-empty.yaml"
        write(unlisted, "attempts: []\n")
        refused = self.run_gate(legacy_attempt=True, legacy_list=unlisted)
        self.assertEqual(refused["verdict"], "fail")
        self.assertTrue(any("legacy bypass refused" in e for e in refused["errors"]))
        listed = Path(self.tmp.name) / "legacy.yaml"
        write(listed, f"attempts:\n  - {self.dir}  # executed before gate 1.1\n")
        legacy = self.run_gate(legacy_attempt=True, legacy_list=listed)
        self.assertEqual(legacy["verdict"], "pass", legacy["errors"])
        self.assertEqual(legacy["code_integrity"]["status"], "not-checked")
        self.assertFalse(legacy["eligible_for_current_gate"])


class IntegrityFixture:
    """Shared fixture: an anchored original executed byte-identical, with clean
    execution snapshots, checked against a committed anchor repository."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self.tmp.name) / "attempt-03"
        write(self.dir / "run-analysis.R", 'source("authors-code/analysis.R")\n')
        write(self.dir / "Dockerfile", "FROM rocker/r-ver:4.3.2\n")
        self.manifest = write_code_manifest(self.dir)
        self.schema = json.loads((REPO_ROOT / lane.DEFAULT_CODE_MANIFEST_SCHEMA)
                                 .read_text(encoding="utf-8"))
        self.repo = anchor_repo(Path(self.tmp.name))
        snapshot(self.dir)

    def tearDown(self):
        self.tmp.cleanup()

    def check(self, **kwargs) -> dict:
        kwargs.setdefault("anchor_root", self.repo)
        return lane.check_code_integrity(self.dir, self.dir / lane.CODE_MANIFEST_FILE,
                                         self.schema, **kwargs)

    def rewrite(self, **changes) -> None:
        manifest = dict(self.manifest, **changes)
        write(self.dir / lane.CODE_MANIFEST_FILE, json.dumps(manifest))

    def unanchored(self, **changes) -> list[dict]:
        """The fixture's originals with the anchor replaced by kind none."""
        return [dict(o, anchor={"kind": "none", "reason": "test"}, **changes)
                for o in self.manifest["originals"]]

class CodeIntegrityTests(IntegrityFixture, unittest.TestCase):
    """check_code_integrity(): hash at retrieval, byte identity at execution."""

    def test_identical_copy_passes(self):
        result = self.check(plan_slug="some-paper-2024")
        self.assertEqual(result["status"], "identical", result["errors"])
        self.assertTrue(result["executed"][0]["identical"])

    def test_slug_mismatch_fails(self):
        self.assertEqual(self.check(plan_slug="other-2024")["status"], "fail")

    def test_pristine_copy_changed_after_retrieval_fails(self):
        write(self.dir / "authors-code-raw" / "analysis.R", AUTHORS_R + "# note\n")
        result = self.check()
        self.assertTrue(any("changed after retrieval" in e for e in result["errors"]))

    def test_declared_edit_size_is_computed_and_governs(self):
        write(self.dir / "authors-code" / "analysis.R",
              AUTHORS_R.replace("index = 4", "index = 3").replace("index = 6", "index = 5"))
        executed = [dict(self.manifest["executed"][0], declared_edit={
            "summary": "two indices", "kind": "repair", "affected_targets": [],
            "lines_changed": 1})]
        self.rewrite(executed=executed)
        snapshot(self.dir)
        result = self.check()
        self.assertEqual(result["status"], "flagged", result["errors"])
        self.assertEqual(result["executed"][0]["lines_changed"]["changed"], 2)
        self.assertIn("declared 1 — the computed value governs", result["flags"][0])

    def test_one_line_substitution_counts_one(self):
        size = lane.lines_changed(b"a\nb\nc\n", b"a\nB\nc\n")
        self.assertEqual(size, {"changed": 1, "removed": 1, "added": 1})

    def test_undeclared_code_file_fails(self):
        write(self.dir / "scripts" / "compare.R", "x <- 1\n")
        result = self.check()
        self.assertTrue(any("undeclared code file scripts/compare.R" in e
                            for e in result["errors"]))

    def test_outputs_are_inventoried(self):
        """Gate 1.2: outputs/ is no longer exempt (PR #7 review, finding 2)."""
        write(self.dir / "outputs" / "generated.R", "x <- 1\n")
        snapshot(self.dir)
        result = self.check()
        self.assertTrue(any("undeclared code file outputs/generated.R" in e
                            for e in result["errors"]))

    def test_undeclared_identical_copy_only_warns(self):
        write(self.dir / "extra" / "analysis.R", AUTHORS_R)
        result = self.check()
        self.assertEqual(result["status"], "identical", result["errors"])
        self.assertTrue(any("byte-identical, undeclared copy" in w for w in result["warnings"]))

    def test_wrapper_inlining_authors_code_is_flagged(self):
        write(self.dir / "run-analysis.R", "# reassembled\n" + AUTHORS_R + "write_out()\n")
        snapshot(self.dir)
        result = self.check()
        self.assertEqual(result["status"], "flagged", result["errors"])
        self.assertTrue(any("embeds 8 substantive line(s)" in f for f in result["flags"]))

    def test_wrapper_that_is_an_authors_file_fails(self):
        write(self.dir / "run-analysis.R", AUTHORS_R)
        result = self.check()
        self.assertTrue(any("byte-identical to authors' original" in e
                            for e in result["errors"]))

    def test_paths_must_stay_inside_the_attempt(self):
        wrappers = self.manifest["wrappers"] + [
            {"path": "../elsewhere.R", "role": "tooling", "purpose": "x"}]
        self.rewrite(wrappers=wrappers)
        self.assertTrue(any("inside the attempt directory" in e
                            for e in self.check()["errors"]))

    def test_schema_violation_fails(self):
        self.rewrite(originals=[{"id": "analysis.R", "sha256": "not-a-hash",
                                 "source": "x", "retrieved_at": "2026-10-04"}])
        self.assertEqual(self.check()["status"], "fail")

    def test_archive_member_rehashed(self):
        import zipfile
        with zipfile.ZipFile(self.dir / "deposit.zip", "w") as archive:
            archive.writestr("repo-v1/analysis.R", AUTHORS_R)
        originals = self.unanchored(
            archive={"path": "deposit.zip", "member": "repo-v1/analysis.R",
                     "sha256": hashlib.sha256(
                         (self.dir / "deposit.zip").read_bytes()).hexdigest()})
        self.rewrite(originals=originals)
        result = self.check()
        self.assertEqual(result["errors"], [])
        self.assertEqual(result["status"], "flagged")  # unanchored: never "identical"
        originals[0]["sha256"] = sha("something else\n")
        self.rewrite(originals=originals)
        result = self.check()
        self.assertTrue(any("does not hash to the recorded" in e for e in result["errors"]))

    def test_no_authors_code_needs_a_reason(self):
        (self.dir / "authors-code" / "analysis.R").unlink()
        (self.dir / "authors-code-raw" / "analysis.R").unlink()
        snapshot(self.dir)
        self.rewrite(originals=[], executed=[])
        self.assertEqual(self.check()["status"], "fail")
        self.rewrite(originals=[], executed=[], no_authors_code_reason="none released")
        self.assertEqual(self.check()["status"], "no-authors-code")

    def test_reimplementation_without_executed_original_is_flagged(self):
        """The pilot pattern: the authors' file kept but never run."""
        (self.dir / "authors-code" / "analysis.R").unlink()
        snapshot(self.dir)
        self.rewrite(executed=[])
        result = self.check()
        self.assertEqual(result["status"], "flagged", result["errors"])
        self.assertTrue(any("no authors' file is listed as executed" in f
                            for f in result["flags"]))

    def test_original_without_pristine_copy_is_flagged(self):
        (self.dir / "authors-code-raw" / "analysis.R").unlink()
        snapshot(self.dir)
        originals = [{k: v for k, v in self.unanchored()[0].items() if k != "local_copy"}]
        self.rewrite(originals=originals)
        result = self.check()
        self.assertEqual(result["status"], "flagged", result["errors"])
        self.assertTrue(result["executed"][0]["identical"])
        self.assertTrue(any("no pristine copy" in f for f in result["flags"]))

    def test_conversion_without_identity_evidence_is_flagged(self):
        write(self.dir / "convert.py", "print('xlsx to csv')\n")
        wrappers = self.manifest["wrappers"] + [
            {"path": "convert.py", "role": "conversion", "purpose": "xlsx to csv"}]
        self.rewrite(wrappers=wrappers)
        self.assertTrue(any("value-identity evidence missing" in f
                            for f in self.check()["flags"]))

    def test_check_code_cli_exit_status(self):
        # The CLI anchors against this repository, which holds no fixture pack.
        self.rewrite(originals=self.unanchored())
        args = argparse.Namespace(attempt_dir=self.dir, manifest=None, out="-",
                                  code_manifest_schema=lane.DEFAULT_CODE_MANIFEST_SCHEMA,
                                  legacy_attempt=False)
        self.assertEqual(lane.cmd_check_code(args), 0)
        write(self.dir / "authors-code" / "analysis.R", AUTHORS_R + "fix()\n")
        self.assertEqual(lane.cmd_check_code(args), 1)

    def test_execute_workflow_carries_manifest_and_flags(self):
        """The executor is told to write the manifest and snapshots; the gate relay
        must carry flags (a required field) and fails closed when it does not."""
        source = (WORKFLOWS / "reproduction-execute.workflow.js").read_text(encoding="utf-8")
        self.assertIn(lane.CODE_MANIFEST_FILE, source)
        self.assertIn("snapshot-code", source)
        schema = re.search(r"const GATE_SCHEMA = \{(.*?)\n\}", source, re.S).group(1)
        required = re.search(r"required: \[([^\]]*)\]", schema).group(1)
        for field in ("'warnings'", "'flags'"):
            self.assertIn(field, required)
        self.assertIn("gate relay omitted its flags", source)


class GateHardeningTests(IntegrityFixture, unittest.TestCase):
    """Gate 1.2: the cross-model review of PR #7 (Astra, GPT in Codex)."""

    # -- Finding 1: provenance anchored outside the executor's manifest.

    def test_edit_before_hashing_is_caught_by_the_anchor(self):
        """Astra's case: the executor shifts an index BEFORE writing the manifest
        and records the edited file as both original and executed copy."""
        edited = AUTHORS_R.replace("index = 4", "index = 3")
        write(self.dir / "authors-code-raw" / "analysis.R", edited)
        write(self.dir / "authors-code" / "analysis.R", edited)
        self.rewrite(originals=[dict(self.manifest["originals"][0], sha256=sha(edited))])
        snapshot(self.dir)
        result = self.check()
        self.assertEqual(result["status"], "fail")
        self.assertTrue(any("does not match the md5 checksum" in e for e in result["errors"]),
                        result["errors"])

    def test_same_attack_without_an_anchor_is_never_identical(self):
        edited = AUTHORS_R.replace("index = 4", "index = 3")
        write(self.dir / "authors-code-raw" / "analysis.R", edited)
        write(self.dir / "authors-code" / "analysis.R", edited)
        self.rewrite(originals=self.unanchored(sha256=sha(edited)))
        snapshot(self.dir)
        result = self.check()
        self.assertEqual(result["status"], "flagged", result["errors"])
        self.assertTrue(any("no independent provenance anchor" in f for f in result["flags"]))

    def test_anchor_to_a_version_the_registry_does_not_select_is_flagged(self):
        repo = anchor_repo(Path(self.tmp.name) / "other", scored_version="10.5281/zenodo.999")
        result = self.check(anchor_root=repo)
        self.assertEqual(result["status"], "flagged", result["errors"])
        self.assertTrue(any("not a version the registry selects" in f
                            for f in result["flags"]))

    def test_uncommitted_pack_cannot_anchor(self):
        pack = self.repo / "packs" / "some-paper-2024.json"
        pack.write_text(pack.read_text() + "\n", encoding="utf-8")
        result = self.check()
        self.assertTrue(any("has uncommitted changes" in e for e in result["errors"]))

    def test_corpus_manifest_anchor_with_store_archive(self):
        """A supplement zip held in the corpus store, anchored by the committed
        corpus manifest, never copied into the attempt directory."""
        store = Path(self.tmp.name) / "store"
        (store / "some-paper-2024").mkdir(parents=True)
        archive = store / "some-paper-2024" / "supplement-1.zip"
        with zipfile.ZipFile(archive, "w") as handle:
            handle.writestr("scripts/analysis.R", AUTHORS_R)
        digest = hashlib.sha256(archive.read_bytes()).hexdigest()
        write(self.repo / "corpus.yaml", json.dumps({"papers": [{
            "slug": "some-paper-2024",
            "files": [{"filename": "supplement-1.zip", "sha256": digest}]}]}))
        git(self.repo, "add", "corpus.yaml")
        git(self.repo, "commit", "-q", "-m", "corpus manifest")
        originals = [dict(
            {k: v for k, v in self.manifest["originals"][0].items() if k != "local_copy"},
            archive={"path": "$CORPUS_ROOT/some-paper-2024/supplement-1.zip",
                     "member": "scripts/analysis.R"},
            anchor={"kind": "corpus-manifest", "manifest": "corpus.yaml",
                    "entry": "some-paper-2024", "filename": "supplement-1.zip"})]
        (self.dir / "authors-code-raw" / "analysis.R").unlink()
        snapshot(self.dir)
        self.rewrite(originals=originals)
        with mock.patch.dict(os.environ, {"CORPUS_ROOT": str(store)}):
            result = self.check()
        self.assertEqual(result["status"], "identical", result["errors"] + result["flags"])
        self.assertEqual(result["anchors"], {"analysis.R": "verified"})

    def test_transcription_is_always_flagged_for_fidelity(self):
        originals = [dict(self.manifest["originals"][0],
                          derivation={"method": "transcription", "from": "supplement-1.pdf",
                                      "from_sha256": "0" * 64})]
        self.rewrite(originals=originals)
        result = self.check()
        self.assertTrue(any("repeatability, not fidelity" in f for f in result["flags"]))

    def test_git_anchor_is_checked_then_flagged_as_unverifiable_offline(self):
        blob = lane.git_blob_sha1(AUTHORS_R.encode())
        anchor = {"kind": "git", "repository": "https://github.com/x/y", "commit": "a" * 40,
                  "path": "analysis.R", "blob_sha1": blob}
        self.rewrite(originals=[dict(self.manifest["originals"][0], anchor=anchor)])
        result = self.check()
        self.assertEqual(result["status"], "flagged", result["errors"])
        self.assertEqual(result["anchors"], {"analysis.R": "recorded"})
        self.rewrite(originals=[dict(self.manifest["originals"][0],
                                     anchor=dict(anchor, blob_sha1="b" * 40))])
        self.assertEqual(self.check()["status"], "fail")

    # -- Finding 2: which code ran, with no exempt directory.

    def test_edited_copy_in_outputs_sourced_by_the_wrapper_fails(self):
        """Astra's case: the nominated copy is untouched, an edited copy sits in
        outputs/, and the run wrapper sources it."""
        write(self.dir / "outputs" / "edited.R", AUTHORS_R.replace("index = 4", "index = 3"))
        write(self.dir / "run-analysis.R", 'source("outputs/edited.R")\n')
        snapshot(self.dir)
        result = self.check()
        self.assertEqual(result["status"], "fail")
        self.assertTrue(any("undeclared code file outputs/edited.R" in e
                            for e in result["errors"]))
        self.assertTrue(any("names undeclared code outputs/edited.R" in e
                            for e in result["errors"]))

    def test_declaring_the_edited_copy_generated_does_not_help(self):
        write(self.dir / "run-analysis.R", 'source("/project/outputs/edited.R")\n')
        lane.write_snapshot(self.dir, "pre", force=True)
        write(self.dir / "outputs" / "edited.R", AUTHORS_R.replace("index = 4", "index = 3"))
        lane.write_snapshot(self.dir, "post", force=True)
        self.rewrite(wrappers=self.manifest["wrappers"] + [
            {"path": "outputs/edited.R", "role": "generated", "purpose": "x"}])
        result = self.check()
        self.assertTrue(any("loads outputs/edited.R, which the run generated" in e
                            for e in result["errors"]), result["errors"])

    def test_code_changed_after_the_run_fails(self):
        write(self.dir / "authors-code" / "analysis.R", AUTHORS_R + "tweak()\n")
        write(self.dir / "authors-code" / "analysis.R", AUTHORS_R)  # restored: passes
        self.assertEqual(self.check()["status"], "identical")
        write(self.dir / "run-analysis.R", 'source("authors-code/analysis.R")\nextra()\n')
        result = self.check()
        self.assertTrue(any("run-analysis.R changed after the run started" in e
                            for e in result["errors"]))

    def test_code_modified_during_the_run_fails(self):
        lane.write_snapshot(self.dir, "pre", force=True)
        write(self.dir / "run-analysis.R", 'source("authors-code/analysis.R")\nextra()\n')
        lane.write_snapshot(self.dir, "post", force=True)
        result = self.check()
        self.assertTrue(any("run-analysis.R was modified during the run" in e
                            for e in result["errors"]))

    def test_generated_code_must_be_declared_and_is_flagged(self):
        lane.write_snapshot(self.dir, "pre", force=True)
        write(self.dir / "outputs" / "made.R", "y <- 2\n")
        lane.write_snapshot(self.dir, "post", force=True)
        failed = self.check()
        self.assertTrue(any("appeared during the run" in e for e in failed["errors"]))
        self.rewrite(wrappers=self.manifest["wrappers"] + [
            {"path": "outputs/made.R", "role": "generated", "purpose": "written by the run"}])
        result = self.check()
        self.assertEqual(result["status"], "flagged", result["errors"])
        self.assertTrue(any("code the run generated" in f for f in result["flags"]))

    def test_missing_snapshots_fail_a_new_run(self):
        shutil.rmtree(self.dir / lane.SNAPSHOT_DIR)
        result = self.check()
        self.assertTrue(any("execution snapshots missing" in e for e in result["errors"]))

    def test_snapshot_is_taken_once(self):
        with self.assertRaises(lane.LaneError):
            lane.write_snapshot(self.dir, "pre")

    def test_review_obligations_for_what_the_gate_cannot_see(self):
        write(self.dir / "run-analysis.R",
              'exprs <- parse(file = "authors-code/analysis.R")\nfor (e in exprs) eval(e)\n')
        write(self.dir / "Dockerfile",
              "FROM rocker/r-ver:4.3.2\nRUN R -e \"remotes::install_github('a/b')\"\n")
        snapshot(self.dir)
        result = self.check()
        obligations = " | ".join(result["review_obligations"])
        self.assertIn("evaluates code dynamically", obligations)
        self.assertIn("brings content into the image", obligations)
        self.assertIn("wrapper semantics are not verified", obligations)

    # -- Finding 3: conversion evidence must be a valid, current check.

    def conversion(self, evidence) -> list[str]:
        """Flags for a conversion wrapper with the given evidence content."""
        write(self.dir / "data" / "in.xlsx", "raw")
        write(self.dir / "data" / "out.csv", "a,b\n1,2\n")
        write(self.dir / "convert.py", "print('xlsx to csv')\n")
        if evidence is not None:
            write(self.dir / "checks" / "identity.json",
                  evidence if isinstance(evidence, str) else json.dumps(evidence))
        self.rewrite(wrappers=self.manifest["wrappers"] + [
            {"path": "convert.py", "role": "conversion", "purpose": "xlsx to csv",
             "value_identity_check": "checks/identity.json"}])
        snapshot(self.dir)
        return [f for f in self.check()["flags"] if "conversion wrapper" in f]

    def valid_evidence(self) -> dict:
        return {"check": "value-identity", "result": "identical",
                "input": {"path": "data/in.xlsx", "sha256": sha("raw")},
                "output": {"path": "data/out.csv", "sha256": sha("a,b\n1,2\n")},
                "values_compared": 2, "values_total": 2}

    def test_conversion_evidence_cases(self):
        self.assertEqual(self.conversion(self.valid_evidence()), [])
        cases = {"missing": None, "unreadable": "",
                 "failed": dict(self.valid_evidence(), result="different"),
                 "stale": dict(self.valid_evidence(),
                               output={"path": "data/out.csv", "sha256": "0" * 64}),
                 "incomplete": dict(self.valid_evidence(), values_compared=1)}
        for word, evidence in cases.items():
            with self.subTest(word):
                flags = self.conversion(evidence)
                if evidence is None:
                    (self.dir / "checks" / "identity.json").unlink(missing_ok=True)
                    flags = [f for f in self.check()["flags"] if "conversion wrapper" in f]
                self.assertEqual(len(flags), 1, flags)
                self.assertIn(word, flags[0])


class InheritedGitEnvTests(unittest.TestCase):
    """Fixtures and the gate never act on a repository named by GIT_DIR.

    Regression for 2026-10-05: run from a pre-commit hook, the suite's fixture
    git calls followed the hook's GIT_DIR into the real repository.
    """

    def test_fixture_and_gate_ignore_an_inherited_git_dir(self):
        with tempfile.TemporaryDirectory() as tmp:
            decoy = Path(tmp) / "decoy"
            decoy.mkdir()
            git(decoy, "init", "-q")
            write(decoy / "keep.txt", "keep\n")
            git(decoy, "add", "keep.txt")
            git(decoy, "commit", "-q", "-m", "decoy")
            head = (decoy / ".git" / "HEAD").read_text()
            config = (decoy / ".git" / "config").read_text()
            hostile = {"GIT_DIR": str(decoy / ".git"),
                       "GIT_INDEX_FILE": str(decoy / ".git" / "index")}
            with mock.patch.dict(os.environ, hostile):
                repo = anchor_repo(Path(tmp) / "fixture")
                self.assertIsNone(lane.committed_unmodified(
                    repo, "packs/some-paper-2024.json"))
            self.assertEqual((decoy / ".git" / "HEAD").read_text(), head)
            self.assertEqual((decoy / ".git" / "config").read_text(), config)
            log = subprocess.run(["git", "-C", str(decoy), "log", "--format=%s"],
                                 capture_output=True, text=True, env=clean_git_env())
            self.assertEqual(log.stdout.split(), ["decoy"])


class HumanQueueTests(unittest.TestCase):
    """human-queue: the authoritative queue, reconciled with the relay (finding 4)."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        self.config = root / "run-config.yaml"
        self.config.write_text(json.dumps({
            "run_id": "run-x", "attempt": 2, "effort": "medium",
            "output_root": str(root / "outputs"),
            "agents": {"planner": "p", "executor": "e", "reviewer": "r"},
            "schemas": {"plan": "p", "execution": "e", "review": "r",
                        "comparison_record": "c"},
            "blinding": {"forbidden_substrings": []},
            "papers": [{"slug": "paper-a"}, {"slug": "paper-b"}]}), encoding="utf-8")
        for slug, flags in (("paper-a", ["FLAGGED EDIT: x differs"]), ("paper-b", [])):
            write(root / "outputs" / slug / "reproduction" / "attempt-02" / lane.GATE_FILE,
                  json.dumps({"verdict": "pass", "flags": flags}))
        self.result = root / "workflow-result.json"

    def tearDown(self):
        self.tmp.cleanup()

    def run_queue(self, relayed) -> int:
        self.result.write_text(json.dumps({"human_queue": relayed}), encoding="utf-8")
        args = argparse.Namespace(config=self.config, workflow_result=self.result, out=None)
        return lane.cmd_human_queue(args)

    def test_flag_lost_in_the_relay_is_reported(self):
        self.assertEqual(self.run_queue([]), 1)
        self.assertEqual(self.run_queue(["paper-a: FLAGGED EDIT: x differs"]), 0)

    def test_missing_gate_report_blocks_clearance(self):
        (Path(self.tmp.name) / "outputs" / "paper-b" / "reproduction" / "attempt-02"
         / lane.GATE_FILE).unlink()
        self.assertEqual(self.run_queue(["paper-a: FLAGGED EDIT: x differs"]), 1)


class PlanAndBindingTests(unittest.TestCase):
    """plan_checks(), select_results(), expected_overall()."""

    def test_plan_checks(self):
        plan = {"status": "OK", "paper": {"title": "t", "doi": "d"},
                "reproduction_type": {"types": ["C"], "rationale": "r"},
                "materials": [{}], "environment": {"x": 1}, "execution_steps": [{}],
                "verification_targets": [{"target_id": "T01"}, {"target_id": "T01"}],
                "enumeration_check": {"targets_enumerated": 3, "items_excluded": 0,
                                      "display_items_detected": 9,
                                      "flag_for_human": False},
                "eligibility": {"within_compute_cap": True}, "exclusions": []}
        errors, warnings = lane.plan_checks(plan)
        self.assertTrue(any("duplicate target ids" in e for e in errors))
        self.assertTrue(any("targets_enumerated" in e for e in errors))
        self.assertTrue(any("enumeration may be incomplete" in w for w in warnings))

    def test_escalate_needs_reason(self):
        errors, _ = lane.plan_checks({"status": "ESCALATE", "escalate_reason": " "})
        self.assertEqual(errors, ["ESCALATE without escalate_reason"])

    def test_select_results_binding(self):
        config = {"papers": [{"slug": "a-2024"}, {"slug": "b-2024"}]}
        good = {"agent_id": "1", "agent_type": "reproduction-planner",
                "result": {"paper_slug": "a-2024"}, "prompt": "x\nPaper: a-2024\ny"}
        dead = {"agent_id": "2", "agent_type": "reproduction-planner", "result": None,
                "prompt": "Paper: b-2024"}
        chosen, dead_slugs = lane.select_results([good, dead], "reproduction-planner", config)
        self.assertEqual(list(chosen), ["a-2024"])
        self.assertEqual(dead_slugs, ["b-2024"])
        swapped = dict(good, prompt="Paper: b-2024")
        with self.assertRaises(lane.LaneError):
            lane.select_results([swapped], "reproduction-planner", config)

    def test_expected_overall(self):
        dims = {k: {"verdict": "PASS", "findings": []} for k in lane.DIMENSION_KEYS}
        self.assertEqual(lane.expected_overall({"dimensions": dims}), "CONFIRMED")
        dims["provenance"]["verdict"] = "CONCERN"
        self.assertEqual(lane.expected_overall({"dimensions": dims}), "QUALIFIED")
        for key in ("scope_completeness", "confirmation_bias"):
            dims[key]["verdict"] = "CONCERN"
        self.assertEqual(lane.expected_overall({"dimensions": dims}), "CHALLENGED")


class ApprovalLockTests(unittest.TestCase):
    """approve binds to the plan hash; a changed plan cannot be executed."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        self.config_path = root / "run-config.yaml"
        pdf = root / "paper.pdf"
        pdf.write_bytes(b"%PDF fake")
        self.config_path.write_text(json.dumps({
            "run_id": "t", "attempt": 2, "effort": "high", "output_root": str(root),
            "agents": {"planner": "reproduction-planner",
                       "executor": "reproduction-executor",
                       "reviewer": "adversarial-reviewer"},
            "schemas": {"plan": "reproduction-system/schemas/reproduction-plan-output.json",
                        "execution":
                            "reproduction-system/schemas/reproduction-execution-output.json",
                        "review": "reproduction-system/schemas/adversarial-review-output.json",
                        "comparison_record": str(COMPARISON_SCHEMA)},
            "blinding": {"forbidden_substrings": []},
            "papers": [{"slug": "a-2024", "paper_pdf": str(pdf)}]}), encoding="utf-8")
        self.plan_path = root / "a-2024" / "reproduction" / "attempt-02" / lane.PLAN_FILE
        write(self.plan_path, json.dumps(plan_record(["T01"], slug="a-2024")))
        self._real_commit = lane.resolve_launch_commit
        lane.resolve_launch_commit = lambda: DUMMY_COMMIT

    def tearDown(self):
        lane.resolve_launch_commit = self._real_commit
        self.tmp.cleanup()

    def approve(self, **overrides):
        args = argparse.Namespace(config=self.config_path, slug="a-2024", decision="approve",
                                  approver="Tester", note="", force=False)
        vars(args).update(overrides)
        return lane.cmd_approve(args)

    def test_approval_records_hash_and_locks(self):
        self.assertEqual(self.approve(), 0)
        record = json.loads((self.plan_path.parent / lane.APPROVAL_FILE).read_text())
        self.assertEqual(record["plan_sha256"],
                         hashlib.sha256(self.plan_path.read_bytes()).hexdigest())
        self.assertEqual(record["locked_target_ids"], ["T01"])
        with self.assertRaises(lane.LaneError):
            self.approve()  # an approved plan is locked

    def test_changed_plan_refused_at_execute(self):
        self.approve()
        write(self.plan_path, json.dumps(plan_record(["T01", "T02"], slug="a-2024")))
        args = argparse.Namespace(config=self.config_path, scratch_root=self.tmp.name,
                                  out=None)
        with self.assertRaisesRegex(lane.LaneError, "changed after approval"):
            lane.cmd_build_exec_args(args)


def transcript(*entries: dict) -> list[str]:
    """Serialise transcript entries as JSONL lines."""
    return [json.dumps(e) for e in entries]


class ResultRecoveryTests(unittest.TestCase):
    """Transcript fallback for results, and the args checksum."""

    def test_structured_output_takes_last_accepted_call(self):
        lines = transcript(
            {"message": {"role": "assistant", "content": [
                {"type": "tool_use", "id": "s1", "name": "StructuredOutput",
                 "input": {"paper_slug": "rejected"}}]}},
            {"message": {"role": "user", "content": [
                {"type": "tool_result", "tool_use_id": "s1", "is_error": True,
                 "content": "schema violation"}]}},
            {"message": {"role": "assistant", "content": [
                {"type": "tool_use", "id": "s2", "name": "StructuredOutput",
                 "input": {"paper_slug": "accepted"}}]}},
            {"message": {"role": "user", "content": [
                {"type": "tool_result", "tool_use_id": "s2", "content": "ok"}]}})
        self.assertEqual(lane.structured_output(lines), {"paper_slug": "accepted"})

    def test_journal_results_falls_back_to_transcripts(self):
        with tempfile.TemporaryDirectory() as tmp:
            run_dir = Path(tmp)
            (run_dir / "agent-x1.meta.json").write_text(
                json.dumps({"agentType": "reproduction-planner"}))
            (run_dir / "agent-x1.jsonl").write_text("\n".join(transcript(
                {"message": {"role": "user", "content": "task\nPaper: a-2024\n"}},
                {"message": {"role": "assistant", "content": [
                    {"type": "tool_use", "id": "s1", "name": "StructuredOutput",
                     "input": {"paper_slug": "a-2024", "status": "OK"}}]}},
                {"message": {"role": "user", "content": [
                    {"type": "tool_result", "tool_use_id": "s1", "content": "ok"}]}})))
            results = lane.journal_results(run_dir)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["source"], "transcript")
        self.assertEqual(results[0]["result"]["paper_slug"], "a-2024")
        self.assertEqual(lane.PAPER_RE.search(results[0]["prompt"]).group(1), "a-2024")

    def test_args_checksum_matches_workflow_javascript(self):
        """The workflows' own checksum code, run in Node, agrees with Python."""
        if shutil.which("node") is None:
            self.skipTest("node not installed")
        payload = {"run_id": "r", "attempt": 2, "flag": True, "none": None,
                   "papers": [{"sha256": "f" * 64, "note": "ü & 'q' \"x\" \\ \n 🦴",
                               "n": [0, 1, -3]}]}
        expected = lane.args_checksum(payload)
        for workflow in ("reproduction-plan.workflow.js", "reproduction-execute.workflow.js"):
            source = (WORKFLOWS / workflow).read_text(encoding="utf-8")
            block = source[source.index("const { args_checksum, ...UNSUMMED } = ARGS"):
                           source.index("if (COMPUTED !== args_checksum)")]
            script = (f"const ARGS = {json.dumps(dict(payload, args_checksum='x'))};\n"
                      f"{block}\nprocess.stdout.write(COMPUTED)")
            result = subprocess.run(["node", "-e", script], capture_output=True, text=True,
                                    timeout=30)
            self.assertEqual(result.stdout, expected, (workflow, result.stderr))

    def test_args_checksum_rejects_floats(self):
        with self.assertRaises(lane.LaneError):
            lane.args_checksum({"x": 1.0})

    def test_emit_args_stamps_checksum_last(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "args.json"
            lane.emit_args({"run_id": "r", "args_checksum": "stale"}, out)
            written = json.loads(out.read_text(encoding="utf-8"))
        self.assertEqual(list(written), ["run_id", "args_checksum"])
        self.assertEqual(written["args_checksum"], lane.args_checksum({"run_id": "r"}))

class AuditTests(unittest.TestCase):
    """Token deduplication, pricing, and blinded-path detection."""

    def test_usage_counted_once_per_request(self):
        usage = {"input_tokens": 10, "cache_creation_input_tokens": 1000,
                 "cache_read_input_tokens": 5000,
                 "cache_creation": {"ephemeral_5m_input_tokens": 600,
                                    "ephemeral_1h_input_tokens": 400}}
        lines = transcript(
            {"requestId": "r1", "message": {"model": "claude-opus-5-5",
                                            "usage": dict(usage, output_tokens=3)}},
            {"requestId": "r1", "message": {"model": "claude-opus-5-5",
                                            "usage": dict(usage, output_tokens=250)}},
            {"requestId": "r2", "message": {"model": "<synthetic>",
                                            "usage": dict(usage, output_tokens=7)}})
        totals = lane.transcript_usage(lines)
        self.assertEqual(totals["requests"], 2)
        self.assertEqual(totals["cache_creation_input_tokens"], 2000)
        self.assertEqual(totals["cache_write_1h"], 800)
        self.assertEqual(totals["output_tokens"], 257)
        self.assertEqual(totals["models"], ["claude-opus-5-5"])

    def test_pricing_strips_date_suffix_and_refuses_unknown(self):
        pricing = {"claude-haiku-4-5": {"input": 1.0, "output": 5.0, "cache_write_5m": 1.25,
                                        "cache_write_1h": 2.0, "cache_read": 0.1}}
        usage = {"models": ["claude-haiku-4-5-20251001"], "input_tokens": 1_000_000,
                 "output_tokens": 0, "cache_write_5m": 0, "cache_write_1h": 0,
                 "cache_read_input_tokens": 0}
        self.assertEqual(lane.price_usage(usage, pricing), 1.0)
        self.assertIsNone(lane.price_usage(dict(usage, models=["mystery"]), pricing))

    def test_blinding_rules(self):
        config = {"blinding": {"forbidden_substrings": ["reproduction/attempt-01", "wiki/"],
                               "exempt_regex": r"/tool-results/hook-[0-9a-f-]+-\d+-"
                                               r"additionalContext\.txt$",
                               "cross_paper_slugs": ["a-2024", "b-2024"]}}
        blind = lane.Blinding(config, "a-2024")
        self.assertIsNotNone(blind.hit("outputs/a-2024/reproduction/attempt-01/log.md"))
        self.assertIsNotNone(blind.hit("outputs/b-2024/reproduction/attempt-02/log.md"))
        self.assertIsNone(blind.hit("outputs/a-2024/reproduction/attempt-02/log.md"))
        self.assertIsNone(blind.hit("~/.claude/projects/x/tool-results/"
                                    "hook-ab12-3-additionalContext.txt"))

    def test_url_paths_are_not_local_accesses(self):
        tokens = lane.path_tokens("curl -sL https://en.wikipedia.org/wiki/PMI "
                                  "&& cat /repo/wiki/continuity.md")
        self.assertEqual(tokens, ["/repo/wiki/continuity.md"])

    def test_audit_flags_blinded_read_and_bash(self):
        config = {"run_id": "t", "effort": "high",
                  "agents": {"planner": "reproduction-planner",
                             "executor": "reproduction-executor",
                             "reviewer": "adversarial-reviewer"},
                  "schemas": {}, "pricing_usd_per_mtok": {},
                  "blinding": {"forbidden_substrings": ["reproduction/attempt-01"],
                               "cross_paper_slugs": []}}
        prompt = ("Mechanical task\nPaper: a-2024\n"
                  "Attempt directory: /repo/out/a-2024/reproduction/attempt-02\n")
        lines = transcript(
            {"message": {"role": "user", "content": prompt}},
            {"message": {"role": "assistant", "content": [
                {"type": "tool_use", "id": "u1", "name": "Read",
                 "input": {"file_path": "/x/a-2024/reproduction/attempt-01/log.md"}},
                {"type": "tool_use", "id": "u2", "name": "Bash",
                 "input": {"command": "curl https://x.org/reproduction/attempt-01/z"}},
                {"type": "tool_use", "id": "u3", "name": "Write",
                 "input": {"file_path": "/elsewhere/notes.md", "content": "x"}}]}},
            {"message": {"role": "user", "content": [
                {"type": "tool_result", "tool_use_id": "u1", "content": "text"},
                {"type": "tool_result", "tool_use_id": "u2", "content": "ok"},
                {"type": "tool_result", "tool_use_id": "u3", "content": "ok"}]}})
        reconcile = load_script("reconcile_run_t", "reconcile-run.py")
        gate = reconcile.load_gate_module()
        record = lane.audit_agent(lines, "general-purpose", config, {"agent_definitions": {}},
                                  reconcile, gate, None)
        self.assertEqual([c["tool"] for c in record["blinding"]["contaminating"]], ["Read"])
        self.assertEqual(record["writes_outside_scope"], ["/elsewhere/notes.md"])
        self.assertFalse(record["clean"])


class SpillExemptionTests(unittest.TestCase):
    """Own spill files are in scope; another agent's spill stays blinded."""

    def test_own_spill_exempt_other_spill_flagged(self):
        home = str(Path.home())
        own = f"{home}/.claude/projects/p/s/tool-results/own123.txt"
        other = f"{home}/.claude/projects/p/s/tool-results/other456.txt"
        config = {"run_id": "t", "effort": "high",
                  "agents": {"planner": "reproduction-planner",
                             "executor": "reproduction-executor",
                             "reviewer": "adversarial-reviewer"},
                  "schemas": {}, "pricing_usd_per_mtok": {},
                  "blinding": {"forbidden_substrings": [".claude/projects/"],
                               "cross_paper_slugs": []}}
        lines = transcript(
            {"message": {"role": "user", "content": "  Paper: a-2024\n"}},
            {"message": {"role": "assistant", "content": [
                {"type": "tool_use", "id": "b1", "name": "Bash",
                 "input": {"command": "cat big.R"}}]}},
            {"message": {"role": "user", "content": [
                {"type": "tool_result", "tool_use_id": "b1",
                 "content": f"<persisted-output>\nFull output saved to: {own}\n"}]}},
            {"message": {"role": "assistant", "content": [
                {"type": "tool_use", "id": "r1", "name": "Read", "input": {"file_path": own}},
                {"type": "tool_use", "id": "r2", "name": "Read",
                 "input": {"file_path": other}}]}},
            {"message": {"role": "user", "content": [
                {"type": "tool_result", "tool_use_id": "r1", "content": "x"},
                {"type": "tool_result", "tool_use_id": "r2", "content": "y"}]}})
        reconcile = load_script("reconcile_run_s", "reconcile-run.py")
        record = lane.audit_agent(lines, "general-purpose", config, {"agent_definitions": {}},
                                  reconcile, reconcile.load_gate_module(), None)
        flagged = [c["path"] for c in record["blinding"]["contaminating"]]
        self.assertEqual(len(flagged), 1)
        self.assertIn("other456", flagged[0])
        self.assertEqual(record["blinding"]["warnings"], [])

class ReplanTests(unittest.TestCase):
    """Receipt keys come from the manifest; re-planning respects the lock."""

    def test_receipt_keys_match_manifest_pushes(self):
        import yaml
        manifest = yaml.safe_load((REPO_ROOT / "manifest.yaml").read_text(encoding="utf-8"))
        for agent in ("reproduction-planner", "reproduction-executor", "adversarial-reviewer"):
            expected = [name for name, entry in manifest["shared_content"].items()
                        for c in entry.get("consumers") or []
                        if c.get("agent") == agent and c.get("mechanism") == "push"]
            self.assertEqual(lane.receipt_keys(agent), expected, agent)
        self.assertIn("pipeline-invariants", lane.receipt_keys("reproduction-planner"))

    def test_supersede_archives_unapproved_and_refuses_approved(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            config = {"attempt": 2, "output_root": str(root),
                      "_path": root / "cfg" / "run-config.yaml"}
            target = root / "a-2024" / "reproduction" / "attempt-02"
            record = dict(plan_record(["T01"], slug="a-2024"), workflow_run="wf_old")
            write(target / lane.PLAN_FILE, json.dumps(record))
            write(target / lane.PLAN_VIEW_FILE, "# view\n")
            archive = lane.supersede_plan(config, "a-2024")
            self.assertFalse((target / lane.PLAN_FILE).exists())
            self.assertTrue((archive / lane.PLAN_FILE).exists())
            self.assertEqual(archive, root / "cfg" / "superseded-plans" / "wf_old" / "a-2024")
            write(target / lane.PLAN_FILE, json.dumps(record))
            write(target / lane.APPROVAL_FILE, "{}")
            with self.assertRaises(lane.LaneError):
                lane.supersede_plan(config, "a-2024")

    def test_prompt_exemption_matches_audit_regex(self):
        import yaml
        config = yaml.safe_load((REPO_ROOT / "studies" / "open-science-compliance" / "outputs"
                                 / "validation" / "phase2-shakedown" / "run-config.yaml")
                                .read_text(encoding="utf-8"))
        exempt = re.compile(config["blinding"]["exempt_regex"])
        example = ("~/.claude/projects/p/s/tool-results/"
                   "hook-1d8724ae-a365-4faa-85a9-43914d631a73-1-additionalContext.txt")
        self.assertIsNotNone(exempt.search(example))
        for workflow in ("reproduction-plan.workflow.js", "reproduction-execute.workflow.js"):
            source = (WORKFLOWS / workflow).read_text(encoding="utf-8")
            self.assertIn("additionalContext.txt", source, workflow)
            self.assertIn("Full output saved to", source, workflow)
            self.assertIn("receipt_keys", source, workflow)

if __name__ == "__main__":
    unittest.main()
