#!/usr/bin/env python3
"""Tests for the lane-owned run command and its sealed run records (gate 1.3).

Specification: ``wiki/planning/reproduction-gate-1-3-design.md`` §§3–5 and §8.
``scripts/reproduction-lane.py run-container`` copies an attempt's input tree
to a private work copy, instruments it, runs it in a container with
networking off, collects what the run wrote into ``outputs/run-NN/``, and
seals its records in ``lane-records/run-NN/``. These tests pin:

1. The event format and the process census, from synthetic streams: the
   shim's EXEC pairs with the hook's START and END by per-process token;
   gaps and repeated sequence numbers mean an incomplete process; a skipped
   hook fails; R CMD calls and forked children need no handshake.
2. The pieces of a run that need no Docker: the lane Renviron (project lines,
   then the saved profile, then the pin), the work-copy instrumentation, the
   lock, and the input tree.
3. The gate's check of sealed records (``check_run_records``), on records
   built by hand: the receipt chain, the launcher binding, collected outputs
   edited after the run (Fable's A14), the input tree changed after the
   final run, and failed and unsealed runs.
4. End to end in Docker (skipped without Docker or ``rocker/r-ver:4.3.2``):
   a clean run seals ``complete`` and passes the record check; a project
   ``.Renviron`` cannot displace the hook; a ``--vanilla`` child fails the
   census; the run cannot write the lane directory; a pre-existing code file
   the run changes fails; and a held lock refuses a second run.

Run: ``venv/bin/python -m pytest tests/test_run_container.py -q``
"""

from __future__ import annotations

import hashlib
import importlib.machinery
import importlib.util
import json
import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
IMAGE = "rocker/r-ver:4.3.2"


def load_script(name: str, filename: str):
    """Import a hyphen-named script as a module (test_reconcile pattern)."""
    spec = importlib.util.spec_from_loader(
        name, importlib.machinery.SourceFileLoader(
            name, str(REPO_ROOT / "scripts" / filename)))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


lane = load_script("reproduction_lane_runs", "reproduction-lane.py")


def write(path: Path, text: str = "x\n") -> None:
    """Create a file (and parents) with content."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def clean_git_env() -> dict[str, str]:
    """The environment minus inherited ``GIT_*`` variables (a pre-commit hook
    exports GIT_DIR, which would point fixture commands at the real
    repository; see test_reproduction_lane.clean_git_env)."""
    return {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}


def git(repo: Path, *args: str) -> str:
    """Run git in a fixture repository and return its stdout."""
    return subprocess.run(["git", "-C", str(repo), "-c", "user.name=t", "-c", "user.email=t@t",
                           *args], check=True, capture_output=True, text=True,
                          env=clean_git_env()).stdout.strip()


def lane_repo(root: Path) -> tuple[Path, str]:
    """A committed repository holding this lane script, and its HEAD.

    The launcher binding compares a run's recorded lane-script digest with
    the script at the launch commit; the working tree under test may hold
    uncommitted changes, so the fixture commits the bytes actually running.
    """
    repo = root / "lane-repo"
    (repo / "scripts").mkdir(parents=True)
    shutil.copy2(REPO_ROOT / "scripts" / "reproduction-lane.py",
                 repo / "scripts" / "reproduction-lane.py")
    git(repo, "init", "-q")
    git(repo, "add", ".")
    git(repo, "commit", "-q", "-m", "fixture")
    return repo, git(repo, "rev-parse", "HEAD")


def hexed(text: str) -> str:
    """Hex-encode a field as the shim and the hook do."""
    return text.encode("utf-8").hex()


def exec_line(nonce: str, token: str, pid: int, *argv: str, stdin: str = "other") -> str:
    """An EXEC event as the shim writes it."""
    fields = "\t".join([stdin, hexed("/project"), *(hexed(a) for a in argv)])
    return f"LANE1 {nonce} {token} {pid} 1 0 EXEC\t{fields}"


def hook_line(nonce: str, token: str, pid: int, seq: int, event: str, *fields: str) -> str:
    """A hook event (START, LOAD, FORK, END)."""
    return f"LANE1 {nonce} {token} {pid} 1 {seq} {event}" + "".join(f"\t{f}" for f in fields)


def start_line(nonce: str, token: str, pid: int, *argv: str, restore: bool = False) -> str:
    """A START event with the hook's field layout."""
    return hook_line(nonce, token, pid, 1, "START", hexed("1.0-f1"), hexed("/project"),
                     hexed("/lane/hook.R"), hexed("/lane/Renviron"), "none", "none",
                     "restore" if restore else "no-restore", *(hexed(a) for a in argv))


def clean_process(nonce: str, token: str, pid: int, *argv: str) -> list[str]:
    """EXEC, START, and END for one instrumented process."""
    return [exec_line(nonce, token, pid, *argv), start_line(nonce, token, pid, *argv),
            hook_line(nonce, token, pid, 2, "END")]


class CensusTests(unittest.TestCase):
    """The event format and the process census (spec §8)."""

    NONCE = "abc123"

    def census(self, *lines: str) -> dict:
        events, stray = lane.parse_events("\n".join(lines) + "\n", self.NONCE)
        self.assertEqual(stray, [])
        return lane.run_census(events)

    def test_instrumented_process_passes(self):
        report = self.census(*clean_process(self.NONCE, "7-a", 7, "--file=run.R"))
        self.assertEqual((report["errors"], report["gaps"], report["abnormal"]), ([], [], []))
        self.assertEqual(report["processes"][0]["argv"], ["--file=run.R"])

    def test_analysis_output_and_foreign_events_are_kept_apart(self):
        text = "\n".join(["Error in f(): ordinary stderr",
                          *clean_process(self.NONCE, "7-a", 7, "--file=run.R"),
                          f"LANE1 othernonce 9-x 9 1 1 START\t{hexed('v')}",
                          "LANE1 malformed line"]) + "\n"
        events, stray = lane.parse_events(text, self.NONCE)
        self.assertEqual(len(events), 3)
        self.assertEqual(len(stray), 2)

    def test_skipped_hook_fails(self):
        report = self.census(exec_line(self.NONCE, "8-a", 8, "--vanilla", "-e", "1"))
        self.assertIn("skipped the lane hook with --vanilla", report["errors"][0])

    def test_uninstrumented_process_fails(self):
        report = self.census(exec_line(self.NONCE, "8-a", 8, "--no-echo", "-e", "1"))
        self.assertIn("never loaded the lane hook", report["errors"][0])

    def test_r_cmd_needs_no_handshake(self):
        """Fable's specification review: R CMD INSTALL is an ordinary route."""
        report = self.census(exec_line(self.NONCE, "8-a", 8, "CMD", "INSTALL", "pkg"))
        self.assertEqual(report["errors"], [])
        self.assertTrue(report["processes"][0]["exempt"])

    def test_start_outside_the_front_end_is_flagged(self):
        report = self.census(start_line(self.NONCE, "9-r", 9), hook_line(
            self.NONCE, "9-r", 9, 2, "END"))
        self.assertIn("outside the R front end", report["flags"][0])

    def test_gap_and_repeat_make_a_process_incomplete(self):
        gap = self.census(exec_line(self.NONCE, "7-a", 7), start_line(self.NONCE, "7-a", 7),
                          hook_line(self.NONCE, "7-a", 7, 3, "END"))
        self.assertEqual(gap["gaps"], ["7-a"])
        repeat = self.census(exec_line(self.NONCE, "7-a", 7), start_line(self.NONCE, "7-a", 7),
                             hook_line(self.NONCE, "7-a", 7, 1, "LOAD"),
                             hook_line(self.NONCE, "7-a", 7, 2, "END"))
        self.assertEqual(repeat["gaps"], ["7-a"])

    def test_missing_end_is_an_abnormal_end(self):
        report = self.census(exec_line(self.NONCE, "7-a", 7), start_line(self.NONCE, "7-a", 7))
        self.assertEqual((report["abnormal"], report["gaps"]), (["7-a"], []))

    def test_forked_child_needs_no_exec_or_end(self):
        report = self.census(*clean_process(self.NONCE, "7-a", 7),
                             hook_line(self.NONCE, "12-f", 12, 1, "FORK", "7-a"),
                             hook_line(self.NONCE, "12-f", 12, 2, "LOAD", hexed("x")))
        self.assertEqual((report["errors"], report["abnormal"], report["gaps"]), ([], [], []))

    def test_reused_pid_is_two_processes(self):
        """Fable's specification review, D-2: tokens, not PIDs, pair events."""
        report = self.census(*clean_process(self.NONCE, "7-a", 7, "-e", "1"),
                             *clean_process(self.NONCE, "7-b", 7, "-e", "2"))
        self.assertEqual(len(report["processes"]), 2)
        self.assertEqual((report["errors"], report["gaps"]), ([], []))

    def test_script_on_standard_input_is_an_obligation(self):
        report = self.census(exec_line(self.NONCE, "7-a", 7, "--no-save", stdin="file"),
                             start_line(self.NONCE, "7-a", 7, "--no-save"),
                             hook_line(self.NONCE, "7-a", 7, 2, "END"))
        self.assertIn("standard input", report["obligations"][0])

    def test_workspace_restore_is_an_obligation(self):
        report = self.census(exec_line(self.NONCE, "7-a", 7, "-f", "a.R"),
                             start_line(self.NONCE, "7-a", 7, "-f", "a.R", restore=True),
                             hook_line(self.NONCE, "7-a", 7, 2, "END"))
        self.assertIn("saved workspace", report["obligations"][0])


class RunPieceTests(unittest.TestCase):
    """The parts of a run that need no Docker."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def test_renviron_keeps_project_lines_then_saves_then_pins(self):
        write(self.root / ".Renviron", "MY_VAR=1\nR_PROFILE_USER=/project/p.R\n")
        lines = lane.compose_renviron(self.root).splitlines()
        self.assertLess(lines.index("MY_VAR=1"),
                        lines.index("LANE_PARENT_PROFILE=${R_PROFILE_USER}"))
        self.assertEqual(lines[-1], "R_PROFILE_USER=/lane/hook.R")

    def test_instrumentation_renames_the_project_profile(self):
        write(self.root / ".Rprofile", "options(x = 1)\n")
        changes = lane.instrument_work_copy(self.root)
        self.assertEqual((self.root / lane.PROJECT_PROFILE).read_text(), "options(x = 1)\n")
        self.assertTrue((self.root / ".Rprofile").read_text().startswith(
            lane.LANE_PROFILE_MARKER))
        self.assertEqual([c["change"] for c in changes], ["renamed", "injected"])

    def test_instrumentation_refuses_a_name_clash(self):
        write(self.root / lane.PROJECT_PROFILE, "x\n")
        with self.assertRaises(lane.LaneError):
            lane.instrument_work_copy(self.root)

    def test_lock_admits_one_run_and_only_its_holder_releases_it(self):
        records = self.root / lane.RECORDS_DIR
        lane.acquire_lock(records, "run-01")
        with self.assertRaises(lane.LaneError):
            lane.acquire_lock(records, "run-02")
        lane.release_lock(records, "run-02")
        self.assertTrue((records / lane.LOCK_FILE).exists())
        lane.release_lock(records, "run-01")
        self.assertFalse((records / lane.LOCK_FILE).exists())

    def test_input_tree_leaves_out_documents_and_records(self):
        for rel in ("run.R", "data/x.csv", "log.md", "comparisons/c.json", "outputs/o.csv",
                    "lane-records/index.jsonl", "authors-code-manifest.json"):
            write(self.root / rel)
        inventory, problems = lane.input_inventory(self.root)
        self.assertEqual(sorted(inventory), ["data/x.csv", "run.R"])
        self.assertEqual(problems, [])


class RecordFixture:
    """Shared fixture: an attempt, and sealed run records built by hand the way
    finalise_run writes them, checked against a committed lane script."""

    NONCE = "feedbeef"

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        self.dir = root / "attempt-01"
        write(self.dir / "run-analysis.R", 'write.csv(1, "outputs/r.csv")\n')
        write(self.dir / "log.md", "notes\n")
        self.repo, self.launch = lane_repo(root)

    def tearDown(self):
        self.tmp.cleanup()

    def seal(self, run_id: str = "run-01", state: str = "complete", exit_status: int = 0,
             events: list[str] | None = None, outputs: dict[str, str] | None = None,
             launch: str | None = "fixture", script_sha256: str | None = None,
             consumed: list[dict] | None = None) -> None:
        """Write and seal one run's records the way finalise_run does."""
        records = self.dir / lane.RECORDS_DIR
        record = records / run_id
        record.mkdir(parents=True)
        pre, _ = lane.input_inventory(self.dir)
        lane.write_json(record / "pre.json", {"run": run_id, "files": pre})
        lane.write_json(record / "baseline.json", {"run": run_id, "files": pre, "changes": []})
        lane.write_json(record / "post.json", {"run": run_id, "files": pre})
        lines = events if events is not None else clean_process(self.NONCE, "7-a", 7,
                                                                "--file=run-analysis.R")
        (record / "events.log").write_text("\n".join(lines) + "\n", encoding="utf-8")
        files = []
        for rel, text in (outputs if outputs is not None
                          else {"files/outputs/r.csv": "1\n", "stdout.log": ""}).items():
            write(self.dir / "outputs" / run_id / rel, text)
            kind = ("console" if rel == "stdout.log" else
                    "generated" if lane.is_code_file(Path(rel)) else "output")
            files.append({"path": rel, "sha256": hashlib.sha256(text.encode()).hexdigest(),
                          "class": kind, "replaced_input": False})
        lane.write_json(record / "outputs.json", {"run": run_id, "files": files, "deleted": []})
        lane.write_json(record / "run.json", {
            "run": run_id, "state": state, "exit_status": exit_status, "nonce": self.NONCE,
            "image": {"id": "sha256:" + "0" * 64},
            "launch_commit": self.launch if launch == "fixture" else launch,
            "lane_script_sha256": script_sha256 or lane.sha256_file(
                REPO_ROOT / "scripts" / "reproduction-lane.py"),
            "consumed": consumed or [], "problems": []})
        lane.seal_run(records, run_id, state)

    def check(self, launch: str | None = "fixture") -> dict:
        return lane.check_run_records(self.dir, self.launch if launch == "fixture" else launch,
                                      self.repo)


class RecordCheckTests(RecordFixture, unittest.TestCase):
    """The gate's check of sealed run records (spec §§4, 5)."""

    def test_clean_run_passes(self):
        self.seal()
        report = self.check()
        self.assertEqual((report["errors"], report["flags"]), ([], []))
        self.assertEqual(report["final_run"], "run-01")
        self.assertIn("outputs/run-01/stdout.log", report["collected"])

    def test_no_records_means_a_pre_gate_attempt(self):
        self.assertIsNone(self.check())

    def test_output_edited_after_the_run_fails(self):
        """Fable's A14: a result edited by hand after the run."""
        self.seal()
        write(self.dir / "outputs" / "run-01" / "files" / "outputs" / "r.csv", "2\n")
        self.assertTrue(any("changed after run-01 wrote it" in e for e in self.check()["errors"]))

    def test_file_added_to_a_run_output_fails(self):
        self.seal()
        write(self.dir / "outputs" / "run-01" / "files" / "extra.csv", "x\n")
        self.assertTrue(any("was not written by run-01" in e for e in self.check()["errors"]))

    def test_edited_record_breaks_the_chain(self):
        self.seal()
        events = self.dir / lane.RECORDS_DIR / "run-01" / "events.log"
        events.write_text(events.read_text() + "tampered\n", encoding="utf-8")
        self.assertTrue(any("broken receipt chain" in e for e in self.check()["errors"]))

    def test_input_tree_changed_after_the_final_run_fails(self):
        self.seal()
        write(self.dir / "run-analysis.R", 'write.csv(2, "outputs/r.csv")\n')
        write(self.dir / "log.md", "a document may change\n")
        errors = self.check()["errors"]
        self.assertEqual(len(errors), 1, errors)
        self.assertIn("changed run-analysis.R after the final run", errors[0])

    def test_launcher_binding(self):
        self.seal()
        self.assertTrue(any("not bound to a launch commit" in f
                            for f in self.check(launch=None)["flags"]))
        self.assertTrue(any("records launch commit" in e
                            for e in self.check(launch="0" * 40)["errors"]))

    def test_lane_script_other_than_the_launch_commit_fails(self):
        self.seal(script_sha256="0" * 64)
        self.assertTrue(any("lane script other than" in e for e in self.check()["errors"]))

    def test_failed_run_is_flagged_for_a_ruling(self):
        self.seal(state="failed", exit_status=1)
        self.assertTrue(any("partial results need a ruling" in f for f in self.check()["flags"]))

    def test_unsealed_run_is_incomplete_and_credits_nothing(self):
        (self.dir / lane.RECORDS_DIR / "run-01").mkdir(parents=True)
        report = self.check()
        self.assertEqual(report["runs"]["run-01"]["state"], "incomplete")
        self.assertTrue(any("nothing to credit" in e for e in report["errors"]))

    def test_census_errors_reach_the_gate(self):
        self.seal(events=[*clean_process(self.NONCE, "7-a", 7, "--file=run-analysis.R"),
                          exec_line(self.NONCE, "9-b", 9, "--vanilla", "-e", "1")])
        self.assertTrue(any("skipped the lane hook" in e for e in self.check()["errors"]))

    def test_generated_code_is_reported(self):
        self.seal(outputs={"files/made.R": "y <- 2\n", "stdout.log": ""})
        self.assertEqual(self.check()["generated"], ["outputs/run-01/files/made.R"])


class ConsumptionAndCitationTests(RecordFixture, unittest.TestCase):
    """Runs that consume earlier runs' outputs, and citations (spec §5)."""

    R_CSV = hashlib.sha256(b"1\n").hexdigest()

    def consumed(self, digest: str | None = None) -> list[dict]:
        return [{"run": "run-01", "source": "files/outputs/r.csv", "path": "outputs/r.csv",
                 "sha256": digest or self.R_CSV}]

    def test_credit_rests_on_the_final_run_and_what_it_consumed(self):
        self.seal("run-01")
        self.seal("run-02", consumed=self.consumed())
        report = self.check()
        self.assertEqual((report["errors"], report["flags"]), ([], []))
        self.assertEqual(report["credited_runs"], ["run-02", "run-01"])

    def test_consumed_digest_must_be_sealed(self):
        self.seal("run-01")
        self.seal("run-02", consumed=self.consumed("0" * 64))
        self.assertTrue(any("did not seal" in e for e in self.check()["errors"]))

    def test_consumed_run_with_other_code_is_flagged(self):
        self.seal("run-01")
        write(self.dir / "run-analysis.R", 'write.csv(3, "outputs/r.csv")\n')
        self.seal("run-02", consumed=self.consumed())
        self.assertTrue(any("which ran other code" in f for f in self.check()["flags"]))

    def test_consumed_run_is_held_to_the_census(self):
        self.seal("run-01", events=[exec_line(self.NONCE, "8-a", 8, "--vanilla", "-e", "1"),
                                    *clean_process(self.NONCE, "7-a", 7, "--file=x.R")])
        self.seal("run-02", consumed=self.consumed())
        self.assertTrue(any(e.startswith("run-01: ") and "skipped the lane hook" in e
                            for e in self.check()["errors"]))

    def test_consume_declarations_are_checked_before_a_run(self):
        self.seal("run-01")
        for spec in ("run-01", "run-01:outputs/r.csv", "run-09:files/outputs/r.csv",
                     "run-01:files/missing.csv"):
            with self.assertRaises(lane.LaneError, msg=spec):
                lane.resolve_consumed(self.dir, [spec])
        write(self.dir / "outputs" / "run-01" / "files" / "outputs" / "r.csv", "2\n")
        with self.assertRaises(lane.LaneError):
            lane.resolve_consumed(self.dir, ["run-01:files/outputs/r.csv"])

    def test_citations(self):
        self.seal("run-01")
        self.seal("run-02", consumed=self.consumed())
        runs = self.check()
        good = {"run": "run-01", "path": "files/outputs/r.csv", "sha256": self.R_CSV}
        targets = [
            {"target_id": "T01", "outcome": "EXACT_MATCH", "testable": True, "outputs": [good]},
            {"target_id": "T02", "outcome": "EXACT_MATCH", "testable": True,
             "outputs": [dict(good, sha256="0" * 64)]},
            {"target_id": "T03", "outcome": "EXACT_MATCH", "testable": True,
             "outputs": [dict(good, run="run-07")]},
            {"target_id": "T04", "outcome": "EXACT_MATCH", "testable": True},
            {"target_id": "T05", "outcome": "MAJOR_DISCREPANCY", "testable": True}]
        errors, flags, unbound = lane.citation_findings(
            targets, runs, ["T01", "T02", "T03", "T04", "T05"])
        self.assertEqual([e.split()[0] for e in errors], ["T02", "T03"])
        self.assertEqual(unbound, {"T04"})
        self.assertIn("target-unbound", flags[0])


def docker_ready() -> bool:
    """Docker answers and the test image is local (no pulls in tests)."""
    if shutil.which("docker") is None:
        return False
    probe = subprocess.run(["docker", "image", "inspect", IMAGE], capture_output=True,
                           check=False)
    return probe.returncode == 0


@unittest.skipUnless(docker_ready(), f"needs Docker and {IMAGE}")
class RunContainerDockerTests(unittest.TestCase):
    """run-container end to end, in the local rocker image."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        self.dir = root / "attempt-01"
        self.work = root / "work"
        self.work.mkdir()
        self.repo, self.launch = lane_repo(root)

    def tearDown(self):
        self.tmp.cleanup()

    def run_entry(self, script: str, **files: str) -> dict:
        """Write an entry script (and other files), run it, and seal the run."""
        write(self.dir / "run-analysis.R", script)
        for rel, text in files.items():
            write(self.dir / rel.replace("__", "/"), text)
        doc = lane.start_run(self.dir, IMAGE, "run-analysis.R", mount_path="/project",
                             launch_commit=self.launch, work_root=self.work)
        return lane.finalise_run(self.dir, doc["run"])

    def test_clean_run_seals_complete_and_passes_the_record_check(self):
        doc = self.run_entry('dir.create("outputs")\n'
                             'write.csv(data.frame(x = 1:3), "outputs/r.csv")\n'
                             'cat("mean 2\\n")\n')
        self.assertEqual(doc["state"], "complete", doc["problems"])
        self.assertEqual(doc["census"]["processes"], 1)
        report = lane.check_run_records(self.dir, self.launch, self.repo)
        self.assertEqual((report["errors"], report["flags"]), ([], []))
        self.assertIn("mean 2", (self.dir / "outputs" / "run-01" / "stdout.log").read_text())
        self.assertTrue((self.dir / "outputs" / "run-01" / "files" / "outputs" /
                         "r.csv").is_file())
        self.assertFalse((self.dir / lane.RECORDS_DIR / lane.LOCK_FILE).exists())
        self.assertEqual(list(self.work.iterdir()), [])

    def test_project_renviron_cannot_displace_the_hook(self):
        """Probe fact 1: a project .Renviron overrides R_PROFILE_USER."""
        doc = self.run_entry('cat(Sys.getenv("R_PROFILE_USER"), "\\n")\n',
                             **{".Renviron": "R_PROFILE_USER=/project/other.R\n",
                                "other.R": "options(other = TRUE)\n"})
        self.assertEqual(doc["state"], "complete", doc["problems"])
        report = lane.check_run_records(self.dir, self.launch, self.repo)
        self.assertEqual(report["errors"], [])
        events = (self.dir / lane.RECORDS_DIR / "run-01" / "events.log").read_text()
        self.assertIn(" START\t", events)
        self.assertIn(hexed("/project/other.R"), events)  # its own profile still ran

    def test_vanilla_child_fails_the_census(self):
        self.run_entry('invisible(system("Rscript --vanilla -e 1"))\n')
        report = lane.check_run_records(self.dir, self.launch, self.repo)
        self.assertTrue(any("skipped the lane hook with --vanilla" in e
                            for e in report["errors"]), report["errors"])

    def test_children_and_psock_workers_are_instrumented(self):
        doc = self.run_entry('invisible(system("Rscript -e 1"))\n'
                             'cl <- parallel::makePSOCKcluster(1)\n'
                             'invisible(parallel::clusterEvalQ(cl, 1))\n'
                             'parallel::stopCluster(cl)\n')
        self.assertEqual(doc["state"], "complete", doc["problems"])
        self.assertEqual(doc["census"]["processes"], 3)
        self.assertEqual(lane.check_run_records(self.dir, self.launch, self.repo)["errors"], [])

    def test_run_cannot_write_the_lane_directory(self):
        doc = self.run_entry('writeLines("x", "/lane/hook.R")\n')
        self.assertEqual(doc["state"], "failed")
        self.assertNotEqual(doc["exit_status"], 0)

    def test_changed_pre_existing_code_fails(self):
        self.run_entry('cat("extra()\\n", file = "helper.R", append = TRUE)\n',
                       **{"helper.R": "x <- 1\n"})
        report = lane.check_run_records(self.dir, self.launch, self.repo)
        self.assertTrue(any("changed pre-existing code helper.R" in e
                            for e in report["errors"]), report["errors"])

    def test_failed_start_leaves_nothing_behind(self):
        """docker run can create a container and then fail to start it (a log
        size Docker refuses at start); the lane removes it, and leaves no
        record, lock, or work copy."""
        write(self.dir / "run-analysis.R", "1\n")
        original = lane.LOG_MAX_SIZE
        lane.LOG_MAX_SIZE = "-1"
        try:
            with self.assertRaises(lane.LaneError):
                lane.start_run(self.dir, IMAGE, "run-analysis.R", mount_path="/project",
                               work_root=self.work)
        finally:
            lane.LOG_MAX_SIZE = original
        left = subprocess.run(["docker", "ps", "-a", "--filter", "name=llmr-run-01-",
                               "--format", "{{.Names}}"], capture_output=True, text=True,
                              check=False).stdout.split()
        self.assertEqual(left, [])
        self.assertEqual(lane.run_ids(self.dir / lane.RECORDS_DIR), [])
        self.assertFalse((self.dir / lane.RECORDS_DIR / lane.LOCK_FILE).exists())
        self.assertEqual(list(self.work.iterdir()), [])

    def test_a_run_consumes_a_sealed_output(self):
        self.run_entry('dir.create("outputs")\nsaveRDS(1:3, "outputs/model.rds")\n')
        write(self.dir / "run-analysis.R",
              'm <- readRDS("outputs/model.rds")\nwrite.csv(sum(m), "outputs/sum.csv")\n')
        doc = lane.start_run(self.dir, IMAGE, "run-analysis.R", mount_path="/project",
                             launch_commit=self.launch, work_root=self.work,
                             consume=["run-01:files/outputs/model.rds"])
        doc = lane.finalise_run(self.dir, doc["run"])
        self.assertEqual(doc["state"], "complete", doc["problems"])
        report = lane.check_run_records(self.dir, self.launch, self.repo)
        self.assertEqual(report["credited_runs"], ["run-02", "run-01"])
        self.assertTrue(any("which ran other code" in f for f in report["flags"]))
        collected = json.loads((self.dir / lane.RECORDS_DIR / "run-02" / "outputs.json")
                               .read_text())["files"]
        self.assertEqual(sorted(f["path"] for f in collected),
                         ["files/outputs/sum.csv", "stdout.log"])

    def test_held_lock_refuses_a_second_run(self):
        write(self.dir / "run-analysis.R", "1\n")
        lane.acquire_lock(self.dir / lane.RECORDS_DIR, "run-01")
        with self.assertRaises(lane.LaneError):
            lane.start_run(self.dir, IMAGE, "run-analysis.R", mount_path="/project",
                           work_root=self.work)


if __name__ == "__main__":
    unittest.main()
