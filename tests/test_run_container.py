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


LANE_FILES = ("scripts/reproduction-lane.py", "reproduction-system/runtime/hook.R",
              "reproduction-system/runtime/r-shim.sh",
              "reproduction-system/runtime/littler-shim.sh")


def lane_repo(root: Path) -> tuple[Path, str]:
    """A committed repository holding this lane's files, and its HEAD.

    The launcher binding compares a run's recorded digests of the lane
    script, the hook, and the shim with those files at the launch commit;
    the working tree under test may hold uncommitted changes, so the fixture
    commits the bytes actually running.
    """
    repo = root / "lane-repo"
    for rel in LANE_FILES:
        (repo / rel).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(REPO_ROOT / rel, repo / rel)
    git(repo, "init", "-q")
    git(repo, "add", ".")
    git(repo, "commit", "-q", "-m", "fixture")
    return repo, git(repo, "rev-parse", "HEAD")


def hexed(text: str) -> str:
    """Hex-encode a field as the shim and the hook do."""
    return text.encode("utf-8").hex()


def captured(kind: str, script: str) -> str:
    """The shim's stdin field for a script it captured from a pipe or file."""
    data = script.encode("utf-8")
    return f"{kind}:{hashlib.md5(data).hexdigest()}:{len(data)}:{data.hex()}"


def exec_line(nonce: str, token: str, pid: int, *argv: str, stdin: str = "other") -> str:
    """An EXEC event as the shim writes it."""
    fields = "\t".join([stdin, hexed("/project"), *(hexed(a) for a in argv)])
    return f"LANE1 {nonce} {token} {pid} 1 0 EXEC\t{fields}"


def hook_line(nonce: str, token: str, pid: int, seq: int, event: str, *fields: str) -> str:
    """A hook event (START, LOAD, FORK, END)."""
    return f"LANE1 {nonce} {token} {pid} 1 {seq} {event}" + "".join(f"\t{f}" for f in fields)


def start_line(nonce: str, token: str, pid: int, *argv: str, restore: bool = False) -> str:
    """A START event with the hook's field layout."""
    return hook_line(nonce, token, pid, 1, "START", hexed("1.1-inst"), hexed("/project"),
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

    def test_forked_child_needs_no_exec_but_its_own_end(self):
        """Astra's specification review, D-2: a fork needs a terminal event."""
        lines = [*clean_process(self.NONCE, "7-a", 7),
                 hook_line(self.NONCE, "12-f", 12, 1, "FORK", "7-a"),
                 hook_line(self.NONCE, "12-f", 12, 2, "LOAD", hexed("x"))]
        unterminated = self.census(*lines)
        self.assertEqual((unterminated["errors"], unterminated["abnormal"],
                          unterminated["gaps"]), ([], [], []))
        self.assertEqual(unterminated["unterminated"], ["12-f"])
        ended = self.census(*lines, hook_line(self.NONCE, "12-f", 12, 3, "END"))
        self.assertEqual((ended["errors"], ended["abnormal"], ended["gaps"],
                          ended["unterminated"]), ([], [], [], []))

    def test_reused_pid_is_two_processes(self):
        """Fable's specification review, D-2: tokens, not PIDs, pair events."""
        report = self.census(*clean_process(self.NONCE, "7-a", 7, "-e", "1"),
                             *clean_process(self.NONCE, "7-b", 7, "-e", "2"))
        self.assertEqual(len(report["processes"]), 2)
        self.assertEqual((report["errors"], report["gaps"]), ([], []))

    def test_a_captured_script_on_standard_input_is_recorded(self):
        """The shim captures a script read from standard input (R < file);
        the census records it, and the account of loads binds it."""
        script = "x <- 1\n"
        report = self.census(exec_line(self.NONCE, "7-a", 7, "--no-save",
                                       stdin=captured("file", script)),
                             start_line(self.NONCE, "7-a", 7, "--no-save"),
                             hook_line(self.NONCE, "7-a", 7, 2, "END"))
        self.assertEqual(report["processes"][0]["stdin"], "file")
        self.assertEqual(report["processes"][0]["script"],
                         {"md5": hashlib.md5(script.encode()).hexdigest(), "bytes": 7,
                          "text": script})
        self.assertEqual(report["obligations"], [])

    def test_workspace_restore_is_recorded(self):
        report = self.census(exec_line(self.NONCE, "7-a", 7, "-f", "a.R"),
                             start_line(self.NONCE, "7-a", 7, "-f", "a.R", restore=True),
                             hook_line(self.NONCE, "7-a", 7, 2, "END"))
        self.assertTrue(report["processes"][0]["restore"])
        self.assertEqual(report["processes"][0]["cwd"], "/project")

    def test_a_fork_with_no_earlier_parent_fails(self):
        """Spec §4: a FORK that no parent event precedes is unaccounted."""
        fork = [hook_line(self.NONCE, "12-f", 12, 1, "FORK", "7-a", "0"),
                hook_line(self.NONCE, "12-f", 12, 2, "END")]
        orphan = self.census(*fork, *clean_process(self.NONCE, "7-a", 7))
        self.assertTrue(any("names parent '7-a', which has no earlier event" in e
                            for e in orphan["errors"]), orphan["errors"])
        child = self.census(*clean_process(self.NONCE, "7-a", 7), *fork)
        self.assertEqual(child["errors"], [])


class CompletenessTests(unittest.TestCase):
    """Delivery, stream end, and process end decide the state (spec §4, §5;
    Astra's specification review, D-2)."""

    GOOD = {"Type": "json-file",
            "Config": {"max-size": "100g", "max-file": "1", "mode": "blocking"}}

    @staticmethod
    def census(**lists) -> dict:
        base = {"processes": [{}], "errors": [], "flags": [], "obligations": [],
                "gaps": [], "abnormal": [], "unterminated": []}
        return {**base, **lists}

    def test_log_options_are_passed_and_read_back(self):
        self.assertEqual(lane.log_opt_args(), ["--log-driver", "json-file", "--log-opt",
                                               "max-size=100g", "--log-opt", "max-file=1",
                                               "--log-opt", "mode=blocking"])
        self.assertIsNone(lane.log_config_problem(self.GOOD))

    def test_non_blocking_logger_is_a_problem(self):
        config = {"Type": "json-file", "Config": {**self.GOOD["Config"],
                                                   "mode": "non-blocking"}}
        self.assertIn("'mode': 'non-blocking'", lane.log_config_problem(config))
        self.assertIn("not json-file", lane.log_config_problem({"Type": "local"}))
        self.assertIn("not json-file", lane.log_config_problem(None))
        rotating = {"Type": "json-file", "Config": {**self.GOOD["Config"], "max-file": "3"}}
        self.assertIn("'max-file': '3'", lane.log_config_problem(rotating))

    def test_missing_tail_is_failed_only_with_the_facts_whole(self):
        abnormal = self.census(abnormal=["7-a"])
        self.assertEqual(lane.run_state([], 137, abnormal), "failed")
        self.assertEqual(lane.run_state(["docker wait failed: x"], None, abnormal),
                         "incomplete")
        self.assertEqual(lane.run_state(["the container's log options differ"], 137,
                                        abnormal), "incomplete")

    def test_unterminated_fork_and_gap_are_incomplete(self):
        self.assertEqual(lane.run_state([], 0, self.census(unterminated=["12-f"])),
                         "incomplete")
        self.assertEqual(lane.run_state([], 0, self.census(gaps=["7-a"])), "incomplete")
        self.assertEqual(lane.run_state([], 0, self.census()), "complete")
        self.assertEqual(lane.run_state([], 1, self.census()), "failed")


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
             consumed: list[dict] | None = None, changes: list[dict] | None = None,
             baseline: dict[str, str] | None = None,
             lane_files: dict[str, str] | None = None) -> None:
        """Write and seal one run's records the way finalise_run does.

        ``changes`` and ``baseline`` stand for the lane's declared changes to
        the work copy (renamed and injected profiles, consumed outputs): the
        baseline is the input tree with ``baseline`` laid over it.
        """
        records = self.dir / lane.RECORDS_DIR
        record = records / run_id
        record.mkdir(parents=True)
        pre, _ = lane.input_inventory(self.dir)
        lane.write_json(record / "pre.json", {"run": run_id, "files": pre})
        lane.write_json(record / "baseline.json", {"run": run_id, "files": {
            **pre, **(baseline or {})}, "changes": changes or []})
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
            "lane_files": lane_files or {name: lane.sha256_file(REPO_ROOT / rel)
                                         for name, rel in lane.BOUND_RUNTIME_FILES.items()},
            "mount_path": "/project", "entry": "run-analysis.R", "interpreter": "Rscript",
            "front_end": {"r_home": "/usr/local/lib/R"},
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

    def test_hook_other_than_the_launch_commit_fails(self):
        """The hook and the shim write the events the gate reads, so they are
        bound to the launch commit as the lane script is."""
        staged = {name: lane.sha256_file(REPO_ROOT / rel)
                  for name, rel in lane.BOUND_RUNTIME_FILES.items()}
        self.seal(lane_files=dict(staged, **{"hook.R": "0" * 64}))
        self.assertTrue(any("ran a hook.R other than" in e for e in self.check()["errors"]))

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


def md5(text: str) -> str:
    """md5 of a file's UTF-8 content, as the hook records a LOAD."""
    return hashlib.md5(text.encode("utf-8")).hexdigest()


def load(fn: str, path: str, digest: str, depth: int = 0, enclosing: int = 0) -> tuple:
    """A LOAD event's kind and fields, for ``AccountFixture.events``."""
    return ("LOAD", hexed(fn), hexed(path), digest, "1", str(depth), str(enclosing))


def text(digest: str, depth: int = 0, enclosing: int = 0) -> tuple:
    """A TEXT event's kind and fields."""
    return ("TEXT", digest, "1", str(depth), str(enclosing))


def package(name: str, library: str, repository: str | None = None) -> tuple:
    """A PKG event's kind and fields: name, version, library, Repository,
    RemoteType, RemoteSha, Packaged, and the DESCRIPTION's md5."""
    return ("PKG", hexed(name), hexed("1.0"), hexed(library),
            hexed(repository) if repository else "none", "none", "none", "none", md5(name))


# An authors' script and an authors' R Markdown document. The document has a
# labelled chunk with an option, an inline expression, and a chunk whose
# options are Quarto-style "#|" lines, which knitr drops before evaluating.
AUTHORS = "".join(f"x{i} <- {i}\n" for i in range(1, 7))
REPORT = ("---\ntitle: r\n---\n\n```{r setup, echo=FALSE}\ny <- 1\n```\n\n"
          "Inline `r y`.\n\n```{r}\n#| echo: false\nz <- y + 1\n```\n")
RUN_ANALYSIS = 'write.csv(1, "outputs/r.csv")\n'


class AccountFixture(RecordFixture):
    """An attempt with a manifest and sealed run records: two originals (a
    script and a document), each kept pristine and executed byte-identical,
    and the entry script declared as a wrapper. Anchors are ``none``, so the
    tests look only at the account's own findings."""

    def setUp(self):
        super().setUp()
        for rel, content in (("authors-code-raw/analysis.R", AUTHORS),
                             ("authors-code/analysis.R", AUTHORS),
                             ("authors-code-raw/report.Rmd", REPORT),
                             ("authors-code/report.Rmd", REPORT)):
            write(self.dir / rel, content)
        manifest = {
            "manifest_version": "1.1", "paper_slug": "some-paper-2024",
            "originals": [
                {"id": oid, "sha256": hashlib.sha256(content.encode()).hexdigest(),
                 "source": f"https://zenodo.org/records/1/files/{oid}",
                 "retrieved_at": "2026-10-08T00:00:00Z",
                 "local_copy": f"authors-code-raw/{oid}",
                 "anchor": {"kind": "none", "reason": "test"}}
                for oid, content in (("analysis.R", AUTHORS), ("report.Rmd", REPORT))],
            "executed": [{"path": "authors-code/analysis.R", "original": "analysis.R"},
                         {"path": "authors-code/report.Rmd", "original": "report.Rmd"}],
            "wrappers": [{"path": "run-analysis.R", "role": "wrapper",
                          "purpose": "runs the authors' code"}]}
        write(self.dir / "authors-code-manifest.json", json.dumps(manifest))
        self.schema = json.loads((REPO_ROOT / lane.DEFAULT_CODE_MANIFEST_SCHEMA)
                                 .read_text(encoding="utf-8"))

    def events(self, *body: tuple, token: str = "7-a", pid: int = 7) -> list[str]:
        """One process: EXEC, START, the entry script's LOAD (seq 2), the
        given events numbered from 3, and END."""
        lines = [exec_line(self.NONCE, token, pid, "--file=run-analysis.R"),
                 start_line(self.NONCE, token, pid, "--file=run-analysis.R"),
                 hook_line(self.NONCE, token, pid, 2, "LOAD", *load(
                     "file", "/project/run-analysis.R", md5(RUN_ANALYSIS))[1:])]
        for seq, (kind, *fields) in enumerate(body, 3):
            lines.append(hook_line(self.NONCE, token, pid, seq, kind, *fields))
        lines.append(hook_line(self.NONCE, token, pid, len(body) + 3, "END", "0"))
        return lines

    def account(self, *body: tuple, **seal) -> dict:
        """Seal one run with these events and run the integrity check."""
        self.seal(events=self.events(*body), **seal)
        return lane.check_code_integrity(self.dir, self.dir / "authors-code-manifest.json",
                                         self.schema, anchor_root=self.repo,
                                         launch_commit=self.launch)

    @staticmethod
    def codes(issues: list) -> list[str]:
        """The issue codes in a list of flags or obligations."""
        return [i.code for i in issues if isinstance(i, lane.Issue)]


class LoadAccountTests(AccountFixture, unittest.TestCase):
    """The gate's account of LOAD, TEXT, CONN, PKG, and HOOKERR events (spec §8),
    with per-load binding of nested loads (Astra's specification review, D-3)."""

    def test_sourcing_the_executed_original_is_accounted_for(self):
        result = self.account(load("source", "/project/authors-code/analysis.R", md5(AUTHORS)))
        self.assertEqual(result["errors"], [])
        self.assertEqual(result["account"]["originals_loaded"], ["analysis.R"])
        self.assertEqual(result["account"]["runs"]["run-01"]["original"], 1)
        # The document was never knitted, so its executed copy is flagged.
        self.assertEqual([f.subject for f in result["flags"]
                          if getattr(f, "code", "") == "executed-not-loaded"],
                         ["authors-code/report.Rmd"])

    def test_parse_and_evaluate_counts_as_loading_the_original(self):
        """herskind's pattern: eval(parse(text = readLines(file))) is a TEXT
        with the file's own md5, since the hook hashes text with one final
        newline."""
        self.assertEqual(lane.text_md5(AUTHORS.rstrip("\n")), md5(AUTHORS))
        result = self.account(text(md5(AUTHORS)))
        self.assertEqual(result["errors"], [])
        self.assertEqual(result["account"]["originals_loaded"], ["analysis.R"])
        self.assertNotIn("unmatched-text", self.codes(result["review_obligations"]))
        self.assertNotIn("authors-code/analysis.R",
                         [f.subject for f in result["flags"] if isinstance(f, lane.Issue)])

    def test_undeclared_code_in_the_work_copy_fails(self):
        """A file passed to a loader is code whatever its name (Fable P1-1)."""
        write(self.dir / "helper.txt", "w <- 2\n")
        result = self.account(load("source", "/project/helper.txt", md5("w <- 2\n")))
        self.assertTrue(any("loaded undeclared code helper.txt" in e for e in result["errors"]),
                        result["errors"])

    def test_a_file_the_run_wrote_is_never_loadable(self):
        result = self.account(load("source", "/project/made.R", md5("m <- 1\n")))
        self.assertTrue(any("loaded made.R, which the run itself wrote" in e
                            for e in result["errors"]), result["errors"])

    def test_content_changed_before_the_load_fails(self):
        """The observed bytes must be those the path held at the baseline
        (Astra's design review, Q3)."""
        result = self.account(load("source", "/project/authors-code/analysis.R",
                                   md5("x1 <- 99\n")))
        self.assertTrue(any("changed during the run before it was loaded" in e
                            for e in result["errors"]), result["errors"])

    def test_a_hook_error_fails(self):
        result = self.account(("HOOKERR", hexed("source"), hexed("boom")))
        self.assertTrue(any("the lane hook failed in source (boom)" in e
                            for e in result["errors"]), result["errors"])

    def test_unmatched_text_is_an_obligation_that_survives_an_identical_rerun(self):
        """Its issue id and fingerprint rest on content, not on the run's
        tokens or event log, so a re-run that changes nothing keeps a ruling."""
        first = self.account(text(lane.text_md5("q <- 1")))
        issue = next(i for i in first["review_obligations"]
                     if getattr(i, "code", "") == "unmatched-text")
        self.assertIn("in run-analysis.R", issue)
        self.seal("run-02", events=self.events(text(lane.text_md5("q <- 1")), token="9-b"))
        second = lane.check_code_integrity(self.dir, self.dir / "authors-code-manifest.json",
                                           self.schema, anchor_root=self.repo,
                                           launch_commit=self.launch)
        again = next(i for i in second["review_obligations"]
                     if getattr(i, "code", "") == "unmatched-text")
        self.assertEqual((again.issue_id, again.fingerprint()),
                         (issue.issue_id, issue.fingerprint()))

    def test_a_tool_expression_is_accounted_for(self):
        expression = next(iter(lane.TOOL_EXPRESSIONS))
        result = self.account(text(lane.text_md5(expression)))
        self.assertNotIn("unmatched-text", self.codes(result["review_obligations"]))
        self.assertEqual(result["account"]["runs"]["run-01"]["text-tool"], 1)

    def test_a_connection_is_an_obligation(self):
        result = self.account(("CONN", hexed("source"), hexed("textConnection"),
                               hexed("x <- 3"), "0", "0"))
        self.assertIn("connection-load", self.codes(result["review_obligations"]))

    def test_only_a_package_without_provenance_is_flagged(self):
        result = self.account(package("localpkg", "/usr/local/lib/R/site-library"),
                              package("dplyr", "/usr/local/lib/R/site-library", "CRAN"),
                              package("stats", "/usr/local/lib/R/library"))
        flagged = [f for f in result["flags"] if getattr(f, "code", "") == "local-package"]
        self.assertEqual([f.subject for f in flagged], ["localpkg"])
        self.assertIn("declare its source tree as an original", flagged[0])

    def test_a_declared_package_source_is_compared(self):
        write(self.dir / "pkg-raw" / "DESCRIPTION", "Package: localpkg\nVersion: 0.9\n")
        manifest = json.loads((self.dir / "authors-code-manifest.json").read_text())
        manifest["originals"].append({
            "id": "pkg/DESCRIPTION", "sha256": hashlib.sha256(
                b"Package: localpkg\nVersion: 0.9\n").hexdigest(),
            "source": "https://zenodo.org/records/1/files/pkg.zip",
            "retrieved_at": "2026-10-08T00:00:00Z", "local_copy": "pkg-raw/DESCRIPTION",
            "anchor": {"kind": "none", "reason": "test"}})
        write(self.dir / "authors-code-manifest.json", json.dumps(manifest))
        result = self.account(package("localpkg", "/usr/local/lib/R/site-library"))
        flagged = next(f for f in result["flags"] if getattr(f, "code", "") == "local-package")
        self.assertIn("is version 0.9, not the installed 1.0", flagged)

    def test_image_library_and_temporary_code(self):
        """Image code outside every library is flagged; a package's lazy-load
        stub, nested under its PKG event, is library code; code in a
        temporary directory was written during the run and fails."""
        library = "/usr/local/lib/R/site-library"
        result = self.account(load("source", "/opt/tools/setup.R", "1" * 32),
                              package("dplyr", library, "CRAN"),
                              load("sys.source", f"{library}/dplyr/R/dplyr", "2" * 32, 1, 4),
                              load("source", "/tmp/generated.R", "3" * 32))
        self.assertEqual([f.subject for f in result["flags"]
                          if getattr(f, "code", "") == "image-code"], ["/opt/tools/setup.R"])
        self.assertEqual(result["account"]["runs"]["run-01"]["library"], 1)
        self.assertTrue(any("/tmp/generated.R, code in a temporary directory" in e
                            for e in result["errors"]), result["errors"])

    def test_the_lane_directory_holds_only_lane_files(self):
        hook = (REPO_ROOT / "reproduction-system" / "runtime" / "hook.R").read_bytes()
        good = self.account(load("source", "/lane/hook.R", hashlib.md5(hook).hexdigest()))
        self.assertEqual(good["errors"], [])
        self.assertEqual(good["account"]["runs"]["run-01"]["lane"], 1)

    def test_a_foreign_file_under_the_lane_mount_fails(self):
        result = self.account(load("source", "/lane/hook.R", "4" * 32))
        self.assertTrue(any("is no lane file's" in e for e in result["errors"]))

    def test_knitting_an_original_maps_its_chunks_inline_code_and_options(self):
        """What knitr 1.45 evaluates from a document (2026-10-08 probe): the
        chunk options as parse_params builds them, each chunk's code less its
        "#|" lines, and inline expressions. A chunk written to a temporary
        file and sourced inside the knit is tool-internal."""
        result = self.account(
            load("knitr::knit", "/project/authors-code/report.Rmd", md5(REPORT)),
            text(lane.text_md5("alist( 'setup', echo=FALSE )"), 1, 3),
            text(lane.text_md5("y <- 1"), 1, 3),
            text(lane.text_md5("y"), 1, 3),
            text(lane.text_md5("z <- y + 1"), 1, 3),
            load("source", "/tmp/RtmpA/chunk.R", lane.text_md5("y <- 1"), 1, 3))
        self.assertEqual(result["errors"], [])
        self.assertNotIn("unmatched-text", self.codes(result["review_obligations"]))
        runs = result["account"]["runs"]["run-01"]
        self.assertEqual((runs["text-chunk"], runs["tool-internal"]), (4, 1))
        self.assertIn("report.Rmd", result["account"]["originals_loaded"])

    def test_an_unmapped_load_inside_knit_fails(self):
        """A helper sourced from a path taken from a parameter, outside the
        work tree: nesting under knit waives nothing (D-3)."""
        result = self.account(
            load("knitr::knit", "/project/authors-code/report.Rmd", md5(REPORT)),
            load("source", "/data/helper.R", "5" * 32, 1, 3))
        self.assertTrue(any("inside knitr::knit, but it maps to no original" in e
                            for e in result["errors"]), result["errors"])

    def test_a_generated_file_loaded_under_knit_fails(self):
        result = self.account(
            load("knitr::knit", "/project/authors-code/report.Rmd", md5(REPORT)),
            load("source", "/project/purled.R", "6" * 32, 1, 3))
        self.assertTrue(any("loaded purled.R, which the run itself wrote" in e
                            for e in result["errors"]), result["errors"])

    def test_text_inside_an_original_must_still_match(self):
        """Text evaluated inside an original may come from a parameter rather
        than from its chunks (D-3), so it is an obligation there too."""
        result = self.account(
            load("knitr::knit", "/project/authors-code/report.Rmd", md5(REPORT)),
            text(lane.text_md5("evil <- TRUE"), 1, 3))
        obligation = next(i for i in result["review_obligations"]
                          if getattr(i, "code", "") == "unmatched-text")
        self.assertIn("in authors-code/report.Rmd", obligation)

    def test_a_forked_childs_loads_nest_under_its_parents_call(self):
        """A child forked inside the parent's knit (seq 3) names that load in
        its FORK, and its own loads inside it nest under the FORK (seq 1),
        however its own numbering runs."""
        chunk = lane.text_md5("y <- 1")
        child = [hook_line(self.NONCE, "12-f", 12, 1, "FORK", "7-a", "3"),
                 hook_line(self.NONCE, "12-f", 12, 2, *load(
                     "source", "/tmp/RtmpB/chunk.R", chunk, 1, 1)),
                 hook_line(self.NONCE, "12-f", 12, 3, *load(
                     "source", "/tmp/RtmpB/chunk.R", chunk, 1, 1)),
                 hook_line(self.NONCE, "12-f", 12, 4, "END", "0")]
        self.seal(events=self.events(load("knitr::knit", "/project/authors-code/report.Rmd",
                                          md5(REPORT))) + child)
        result = lane.check_code_integrity(self.dir, self.dir / "authors-code-manifest.json",
                                           self.schema, anchor_root=self.repo,
                                           launch_commit=self.launch)
        self.assertEqual(result["errors"], [])
        self.assertEqual(result["account"]["runs"]["run-01"]["tool-internal"], 2)

    def test_the_project_profile_binds_through_its_rename(self):
        """The lane renames a project .Rprofile to .Rprofile.project and
        injects its own; each binds to what it is (spec §4)."""
        profile = "options(digits = 4)\n"
        write(self.dir / ".Rprofile", profile)
        manifest = json.loads((self.dir / "authors-code-manifest.json").read_text())
        manifest["wrappers"].append({"path": ".Rprofile", "role": "environment",
                                     "purpose": "the project's start-up options"})
        write(self.dir / "authors-code-manifest.json", json.dumps(manifest))
        injected = hashlib.sha256(lane.LANE_PROFILE.encode()).hexdigest()
        result = self.account(
            load("profile", "/project/.Rprofile.project", md5(profile)),
            load("source", "/project/.Rprofile", md5(lane.LANE_PROFILE)),
            baseline={".Rprofile.project": hashlib.sha256(profile.encode()).hexdigest(),
                      ".Rprofile": injected},
            changes=[{"change": "renamed", "from": ".Rprofile", "to": ".Rprofile.project"},
                     {"change": "injected", "path": ".Rprofile", "sha256": injected}])
        self.assertEqual(result["errors"], [])
        runs = result["account"]["runs"]["run-01"]
        self.assertEqual((runs["wrapper"], runs["lane"]), (2, 1))

    def test_a_consumed_output_is_never_loadable_as_code(self):
        self.seal("run-01", outputs={"files/outputs/r.csv": "1\n", "files/lib.R": "l <- 1\n",
                                     "stdout.log": ""})
        lib = hashlib.sha256(b"l <- 1\n").hexdigest()
        consumed = {"run": "run-01", "source": "files/lib.R", "path": "lib.R", "sha256": lib}
        self.seal("run-02", consumed=[consumed], baseline={"lib.R": lib},
                  changes=[{"change": "consumed", **consumed}],
                  events=self.events(load("source", "/project/lib.R", md5("l <- 1\n"))))
        result = lane.check_code_integrity(self.dir, self.dir / "authors-code-manifest.json",
                                           self.schema, anchor_root=self.repo,
                                           launch_commit=self.launch)
        self.assertTrue(any("an output of run-01 consumed as input" in e
                            for e in result["errors"]), result["errors"])

    def script_process(self, token: str, pid: int, script: str, *argv: str) -> list[str]:
        """An R process that read ``script`` from standard input, as the
        shim captures it: EXEC, START, and END."""
        return [exec_line(self.NONCE, token, pid, *argv, stdin=captured("pipe", script)),
                start_line(self.NONCE, token, pid, *argv),
                hook_line(self.NONCE, token, pid, 2, "END", "0")]

    def account_with(self, *extra: list[str], **seal) -> dict:
        """Seal the entry process plus extra processes, and check."""
        lines = self.events()
        for process in extra:
            lines += process
        self.seal(events=lines, **seal)
        return lane.check_code_integrity(self.dir, self.dir / "authors-code-manifest.json",
                                         self.schema, anchor_root=self.repo,
                                         launch_commit=self.launch)

    def declare_package(self, version: str = "0.1") -> None:
        """Declare an authors' package tree, executed from authors-code/mypkg."""
        files = {"DESCRIPTION": f"Package: mypkg\nVersion: {version}\n",
                 "NAMESPACE": "export(f)\n", "R/f.R": "f <- function() 42\n"}
        manifest = json.loads((self.dir / "authors-code-manifest.json").read_text())
        for rel, content in files.items():
            write(self.dir / "authors-code-raw" / "mypkg" / rel, content)
            write(self.dir / "authors-code" / "mypkg" / rel, content)
            manifest["originals"].append({
                "id": f"mypkg/{rel}", "sha256": hashlib.sha256(content.encode()).hexdigest(),
                "source": "https://zenodo.org/records/1/files/mypkg.zip",
                "retrieved_at": "2026-10-08T00:00:00Z",
                "local_copy": f"authors-code-raw/mypkg/{rel}",
                "anchor": {"kind": "none", "reason": "test"}})
            manifest["executed"].append({"path": f"authors-code/mypkg/{rel}",
                                         "original": f"mypkg/{rel}"})
        write(self.dir / "authors-code-manifest.json", json.dumps(manifest))

    INSTALL_HELPERS = (
        "tools:::.install_package_indices(\".\",\n'/project/lib/00LOCK-mypkg/00new/mypkg'\n)\n",
        "tools:::.test_load_package('mypkg', '/project/lib/00LOCK-mypkg/00new')\n")

    def install(self, target: str, first_pid: int = 50) -> list[list[str]]:
        """R CMD INSTALL's dispatcher, its inner start, and two helpers."""
        return [[exec_line(self.NONCE, f"{first_pid}-c", first_pid, "CMD", "INSTALL",
                           "--library=lib", target)],
                self.script_process(f"{first_pid + 1}-i", first_pid + 1,
                                    lane.PACKAGE_INSTALL_SCRIPT, "--no-restore", "--no-echo",
                                    "--args", f"nextArg--library=libnextArg{target}"),
                *(self.script_process(f"{first_pid + 2 + n}-h", first_pid + 2 + n, helper,
                                      "--no-save", "--no-restore", "--no-echo")
                  for n, helper in enumerate(self.INSTALL_HELPERS))]

    def test_a_script_on_standard_input_binds_by_content(self):
        """R < original.R runs the original: the shim's capture binds it."""
        result = self.account_with(self.script_process("9-s", 9, AUTHORS, "--no-save"))
        self.assertEqual(result["account"]["originals_loaded"], ["analysis.R"])
        self.assertNotIn("stdin-script", self.codes(result["review_obligations"]))

    def test_an_unmatched_stdin_script_is_an_obligation_keyed_on_content(self):
        first = self.account_with(self.script_process("9-s", 9, "q <- 1\n", "--no-save"))
        issue = next(i for i in first["review_obligations"]
                     if getattr(i, "code", "") == "stdin-script")
        self.assertIn("beginning 'q <- 1'", issue)
        self.seal("run-02", events=self.events(token="8-b") + self.script_process(
            "10-t", 10, "q <- 1\n", "--no-save"))
        second = lane.check_code_integrity(self.dir, self.dir / "authors-code-manifest.json",
                                           self.schema, anchor_root=self.repo,
                                           launch_commit=self.launch)
        again = next(i for i in second["review_obligations"]
                     if getattr(i, "code", "") == "stdin-script")
        self.assertEqual((again.issue_id, again.fingerprint()),
                         (issue.issue_id, issue.fingerprint()))

    def test_r_cmd_install_of_a_declared_tree_is_accounted_for(self):
        """PKGBUILD: the inner start's script is R's installer, its target a
        declared original tree; the helpers are the installer's own."""
        self.declare_package()
        result = self.account_with(*self.install("authors-code/mypkg"))
        self.assertEqual(result["errors"], [])
        self.assertEqual([i for i in result["review_obligations"]
                          if getattr(i, "code", "") in ("stdin-script", "package-install")], [])
        counts = result["account"]["runs"]["run-01"]
        self.assertEqual((counts["package-install"], counts["installer"]), (1, 2))

    def test_r_cmd_install_of_an_undeclared_tree_is_an_obligation(self):
        write(self.dir / "otherpkg" / "DESCRIPTION", "Package: otherpkg\nVersion: 1.0\n")
        result = self.account_with(*self.install("otherpkg"))
        issue = next(i for i in result["review_obligations"]
                     if getattr(i, "code", "") == "package-install")
        self.assertEqual(issue.subject, "otherpkg")

    def test_an_archive_built_from_a_declared_tree_is_accounted_for(self):
        """devtools::install and remotes::install_local build an archive in
        a temporary directory and install that: bound by name and version
        when the run built one."""
        self.declare_package()
        build = self.script_process("40-b", 40, lane.PACKAGE_BUILD_SCRIPT, "--no-restore",
                                    "--no-echo", "--args", "nextArg/project/authors-code/mypkg")
        bound = self.account_with(build, *self.install("/tmp/RtmpA/mypkg_0.1.tar.gz"))
        self.assertNotIn("package-install", self.codes(bound["review_obligations"]))
        self.assertEqual(bound["account"]["runs"]["run-01"]["package-build"], 1)

    def test_an_archive_of_another_version_is_an_obligation(self):
        self.declare_package("0.2")
        build = self.script_process("40-b", 40, lane.PACKAGE_BUILD_SCRIPT, "--no-restore",
                                    "--no-echo", "--args", "nextArg/tmp/RtmpA/copy/mypkg")
        result = self.account_with(build, *self.install("/tmp/RtmpA/mypkg_0.1.tar.gz"))
        issue = next(i for i in result["review_obligations"]
                     if getattr(i, "code", "") == "package-install")
        self.assertIn("is version 0.2", issue)

    def test_a_local_remote_type_is_no_provenance(self):
        """remotes::install_local records RemoteType "local" (probe)."""
        local = ("PKG", hexed("mypkg"), hexed("0.1"), hexed("/project/lib"), "none",
                 hexed("local"), "none", "none", md5("mypkg"))
        github = ("PKG", hexed("ghpkg"), hexed("0.1"), hexed("/project/lib"), "none",
                  hexed("github"), hexed("abc"), "none", md5("ghpkg"))
        result = self.account(local, github)
        self.assertEqual([f.subject for f in result["flags"]
                          if getattr(f, "code", "") == "local-package"], ["mypkg"])

    def test_a_restored_workspace_is_an_obligation_bound_to_its_content(self):
        write(self.dir / ".RData", "workspace")
        restore = [exec_line(self.NONCE, "9-w", 9, "-f", "run-analysis.R"),
                   start_line(self.NONCE, "9-w", 9, "-f", "run-analysis.R", restore=True),
                   hook_line(self.NONCE, "9-w", 9, 2, "END", "0")]
        result = self.account_with(restore)
        issue = next(i for i in result["review_obligations"]
                     if getattr(i, "code", "") == "workspace-restore")
        self.assertEqual(issue.subject, ".RData")
        self.assertEqual(issue.files, {".RData": hashlib.sha256(b"workspace").hexdigest()})

    def test_callr_bootstrap_files_are_tool_internal_only_at_start_up(self):
        """callr's profile and script (2026-10-08 probe) bind by loader and
        path, at a process's own start-up; sourced any other way, or under
        another name, they are code in a temporary directory."""
        profile, script = "/tmp/RtmpAb1/callr-upr-1a2b", "/tmp/RtmpAb1/callr-scr-3c4d"
        child = [exec_line(self.NONCE, "9-c", 9, "-f", script),
                 start_line(self.NONCE, "9-c", 9, "-f", script),
                 hook_line(self.NONCE, "9-c", 9, 2, *load("file", script, "7" * 32)),
                 hook_line(self.NONCE, "9-c", 9, 3, *load("profile", profile, "8" * 32)),
                 hook_line(self.NONCE, "9-c", 9, 4, "END", "0")]
        good = self.account_with(child)
        self.assertEqual(good["errors"], [])
        self.assertEqual(good["account"]["runs"]["run-01"]["tool-internal"], 2)

    def test_callr_files_loaded_otherwise_are_temporary_code(self):
        bad = self.account(load("source", "/tmp/RtmpAb1/callr-scr-3c4d", "7" * 32),
                           load("profile", "/tmp/RtmpAb1/callr-upr-not-hex", "8" * 32))
        self.assertEqual(len([e for e in bad["errors"] if "temporary directory" in e]), 2)

    def test_the_namespace_reader_and_package_internals_are_package_code(self):
        """R's NAMESPACE parser (verified caller) and text evaluated while a
        namespace loads are the package's own machinery."""
        library = "/usr/local/lib/R/site-library"
        result = self.account(
            ("CONN", hexed("parse"), hexed("textConnection"), hexed("tmp"), "0", "0",
             hexed("base::parseNamespaceFile")),
            package("dplyr", library, "CRAN"),
            ("CONN", hexed("parse"), hexed("textConnection"), hexed("tmp"), "1", "4",
             hexed("loadNamespace")),
            text(lane.text_md5("dplyr internals"), 1, 4),
            ("CONN", hexed("parse"), hexed("textConnection"), hexed("tmp"), "0", "0",
             hexed("parseNamespaceFile")))
        connections = [i for i in result["review_obligations"]
                       if getattr(i, "code", "") == "connection-load"]
        # Only the unverified look-alike caller is left to a reviewer.
        self.assertEqual(len(connections), 1)
        self.assertIn("from parseNamespaceFile", connections[0])
        self.assertNotIn("unmatched-text", self.codes(result["review_obligations"]))
        self.assertEqual(result["account"]["runs"]["run-01"]["text-package"], 1)

    def test_a_relative_package_library_is_resolved(self):
        """library(pkg, lib.loc = "lib") recorded "lib" before hook 1.3; the
        package's stub is then placed by the process's working directory."""
        result = self.account(("PKG", hexed("dplyr"), hexed("1.0"), hexed("lib"),
                               hexed("CRAN"), "none", "none", "none", md5("dplyr")),
                              load("sys.source", "/project/lib/dplyr/R/dplyr", "2" * 32, 1, 3))
        self.assertEqual(result["errors"], [])
        self.assertEqual(result["account"]["runs"]["run-01"]["library"], 1)

    def test_the_installers_parse_of_a_declared_tree_binds(self):
        """For a package with an Encoding field, R CMD INSTALL parses each R
        file with a #line header naming its path in the source directory
        (2026-10-08 probe): bound for the directories the run installed
        from, so an edited copy of the source matches nothing."""
        self.declare_package()
        header = '#line 1 "/project/authors-code/mypkg/R/f.R"'
        good = lane.text_md5(f"{header}\nf <- function() 42")
        edited = lane.text_md5(f"{header}\nf <- function() 43")
        inner = self.install("authors-code/mypkg")
        inner[1].insert(2, hook_line(self.NONCE, "51-i", 51, 2, *text(good)))
        inner[1].insert(3, hook_line(self.NONCE, "51-i", 51, 3, *text(edited)))
        inner[1][-1] = hook_line(self.NONCE, "51-i", 51, 4, "END", "0")
        result = self.account_with(*inner)
        self.assertEqual(result["account"]["runs"]["run-01"]["text-package-source"], 1)
        unmatched = [i for i in result["review_obligations"]
                     if getattr(i, "code", "") == "unmatched-text"]
        self.assertEqual([i.subject.split("@")[0] for i in unmatched], [edited])

    def test_no_original_loaded_flags_every_executed_copy(self):
        result = self.account()
        self.assertEqual(result["account"]["originals_loaded"], [])
        self.assertEqual(sorted(f.subject for f in result["flags"]
                                if getattr(f, "code", "") == "executed-not-loaded"),
                         ["authors-code/analysis.R", "authors-code/report.Rmd"])


class DocumentTextTests(unittest.TestCase):
    """The lane's mapping of what knitr evaluates from a document."""

    def test_label_quoting_follows_knitr(self):
        for params, quoted in (("setup, echo=FALSE", "'setup', echo=FALSE"),
                               ("a", "'a'"), ("'q', x=1", "'q', x=1"),
                               ("echo=FALSE", "echo=FALSE"), (", fig, w=2", "'fig', w=2")):
            self.assertEqual(lane.knitr_label_quoted(params), quoted, params)

    def test_document_texts(self):
        found = lane.document_texts(REPORT)
        for snippet in ("alist( 'setup', echo=FALSE )", "y <- 1", "y", "z <- y + 1",
                        "#| echo: false\nz <- y + 1"):
            self.assertIn(lane.text_md5(snippet), found, snippet)
        self.assertEqual(len(found), 5)


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

    def test_loader_events_nest_and_children_end(self):
        """The instrumented hook (spec §8): LOAD nesting by depth and enclosing
        seq, TEXT repeats counted on END, CONN for a connection, PKG for a
        namespace, and a forked child's own END from mcexit. Nothing reaches
        stdout but the script's own line."""
        doc = self.run_entry('source("helper.R")\n'
                             'invisible(parse(text = "1 + 1")); invisible(parse(text = "1 + 1"))\n'
                             'suppressPackageStartupMessages(library(stats4))\n'
                             'r <- parallel::mclapply(1:2, function(i) i, mc.cores = 2)\n'
                             'con <- textConnection("x <- 3"); source(con); close(con)\n'
                             'cat("only this line\\n")\n',
                             **{"helper.R": 'source("inner.R")\n', "inner.R": "y <- 2\n"})
        self.assertEqual(doc["state"], "complete", doc["problems"])
        self.assertEqual(doc["census"]["unterminated"], [])
        events, _ = lane.parse_events((self.dir / lane.RECORDS_DIR / "run-01" /
                                       "events.log").read_text(), doc["nonce"])
        by_kind = {}
        for event in events:
            by_kind.setdefault(event["event"], []).append(event)
        self.assertNotIn("HOOKERR", by_kind)
        loads = {lane.decode_field(e["fields"][1]): e for e in by_kind["LOAD"]
                 if lane.decode_field(e["fields"][0]) == "source"}
        helper, inner = loads["/project/helper.R"], loads["/project/inner.R"]
        # The entry script is a frame-less "file" LOAD at the top level, so the
        # first source() is at depth 0 and the one inside it at depth 1.
        self.assertEqual((helper["fields"][4], helper["fields"][5]), ("0", "0"))
        self.assertEqual((inner["fields"][4], inner["fields"][5]), ("1", str(helper["seq"])))
        self.assertEqual(len(by_kind["TEXT"]), 1)
        main = [e for e in by_kind["END"] if e["token"] == by_kind["START"][0]["token"]]
        self.assertEqual(main[0]["fields"], ["1"])  # the repeated parse(text =)
        self.assertEqual(len(by_kind["FORK"]), 2)
        self.assertEqual(sorted(e["token"] for e in by_kind["FORK"]),
                         sorted(e["token"] for e in by_kind["END"]
                                if e["token"] != main[0]["token"]))
        self.assertEqual(lane.decode_field(by_kind["CONN"][0]["fields"][1]), "textConnection")
        self.assertIn("stats4", [lane.decode_field(e["fields"][0]) for e in by_kind["PKG"]])
        self.assertEqual((self.dir / "outputs" / "run-01" / "stdout.log").read_text(),
                         "only this line\n")

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


MATRIX_IMAGE = "llmr-launcher-matrix:4.3.2"


def image_ready(image: str) -> bool:
    """Docker answers and ``image`` is local (built from
    ``tests/fixtures/launcher-matrix/Dockerfile``; tests never build it)."""
    if shutil.which("docker") is None:
        return False
    return subprocess.run(["docker", "image", "inspect", image], capture_output=True,
                          check=False).returncode == 0


class AccountRunMixin:
    """Real runs through the lane, then the full integrity check with its
    account of loads (spec §8)."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        self.dir = root / "attempt-01"
        self.work = root / "work"
        self.work.mkdir()
        self.repo, self.launch = lane_repo(root)
        self.schema = json.loads((REPO_ROOT / lane.DEFAULT_CODE_MANIFEST_SCHEMA)
                                 .read_text(encoding="utf-8"))

    def tearDown(self):
        self.tmp.cleanup()

    def attempt(self, entry: str, originals: dict[str, str]) -> None:
        """Write the entry wrapper and each original (pristine under
        ``authors-code-raw/``, executed under ``authors-code/``), and the
        manifest declaring them."""
        write(self.dir / "run-analysis.R", entry)
        for oid, content in originals.items():
            write(self.dir / "authors-code-raw" / oid, content)
            write(self.dir / "authors-code" / oid, content)
        write(self.dir / "authors-code-manifest.json", json.dumps({
            "manifest_version": "1.1", "paper_slug": "some-paper-2024",
            "originals": [{"id": oid, "sha256": hashlib.sha256(content.encode()).hexdigest(),
                           "source": f"https://zenodo.org/records/1/files/{oid}",
                           "retrieved_at": "2026-10-08T00:00:00Z",
                           "local_copy": f"authors-code-raw/{oid}",
                           "anchor": {"kind": "none", "reason": "test"}}
                          for oid, content in originals.items()],
            "executed": [{"path": f"authors-code/{oid}", "original": oid}
                         for oid in originals],
            "wrappers": [{"path": "run-analysis.R", "role": "wrapper",
                          "purpose": "runs the authors' code"}]}))

    def run_and_check(self, image: str) -> tuple[dict, dict]:
        doc = lane.start_run(self.dir, image, "run-analysis.R", mount_path="/project",
                             launch_commit=self.launch, work_root=self.work)
        doc = lane.finalise_run(self.dir, doc["run"])
        return doc, lane.check_code_integrity(
            self.dir, self.dir / "authors-code-manifest.json", self.schema,
            anchor_root=self.repo, launch_commit=self.launch)


@unittest.skipUnless(docker_ready(), f"needs Docker and {IMAGE}")
class AccountDockerTests(AccountRunMixin, unittest.TestCase):
    """The account of a real run in the base image."""

    def test_ordinary_launchers_and_loaders_are_accounted_for(self):
        """source(), the parse-and-evaluate pattern, an Rscript -e child, a
        PSOCK worker, and forked children that source the original: every
        load binds, and only the -e child's own code is left to a reviewer.
        The -e text is hashed as R evaluates it, unescaped (hook 1.2)."""
        self.attempt('source("authors-code/analysis.R")\n'
                     'eval(parse(text = readLines("authors-code/analysis.R")))\n'
                     "invisible(system(\"Rscript -e 'q <- 1'\"))\n"
                     'cl <- parallel::makePSOCKcluster(1)\n'
                     'invisible(parallel::clusterEvalQ(cl, 1))\n'
                     'parallel::stopCluster(cl)\n'
                     'r <- parallel::mclapply(1:2, function(i) {\n'
                     '  source("authors-code/analysis.R"); i }, mc.cores = 2)\n'
                     'dir.create("outputs"); write.csv(1, "outputs/r.csv")\n',
                     {"analysis.R": AUTHORS})
        doc, result = self.run_and_check(IMAGE)
        self.assertEqual(doc["state"], "complete", doc["problems"])
        self.assertEqual(result["errors"], [])
        self.assertEqual(result["account"]["originals_loaded"], ["analysis.R"])
        unmatched = [i for i in result["review_obligations"]
                     if getattr(i, "code", "") == "unmatched-text"]
        self.assertEqual([i.subject for i in unmatched],
                         [f"{lane.text_md5('q <- 1')}@the command line"])
        counts = result["account"]["runs"]["run-01"]
        self.assertEqual((counts["original"], counts["text-original"], counts["text-tool"]),
                         (3, 1, 1))
        self.assertNotIn("executed-not-loaded", [getattr(f, "code", "")
                                                 for f in result["flags"]])


# An authors' package tree. The Encoding field makes R CMD INSTALL parse its
# R files as text with a #line header (the probed branch).
PACKAGE = {"mypkg/DESCRIPTION": ("Package: mypkg\nVersion: 0.1\nTitle: Probe\n"
                                 "Description: Probe package.\nLicense: MIT\nAuthor: t\n"
                                 "Maintainer: t <t@t.t>\nEncoding: UTF-8\n"),
           "mypkg/NAMESPACE": "export(f)\n", "mypkg/R/f.R": "f <- function() 42\n"}
PACKAGE_RUN = ('dir.create("lib"); dir.create("outputs")\n'
               '.libPaths(c(normalizePath("lib"), .libPaths()))\n'
               '{install}\n'
               'library(mypkg, lib.loc = "lib"); write.csv(f(), "outputs/f.csv")\n')
QUIET = ("stdin-script", "package-install", "connection-load", "unmatched-text")


@unittest.skipUnless(docker_ready(), f"needs Docker and {IMAGE}")
class LauncherDockerTests(AccountRunMixin, unittest.TestCase):
    """Step 2 of the instrumentation, in the base image: R -f, R < file,
    littler, and R CMD INSTALL (spec §8)."""

    def test_r_f_r_stdin_and_littler_load_the_original(self):
        """R -f reaches R unrewritten (hook 1.3 reads it); a script on
        standard input binds by the shim's capture; littler runs Rscript."""
        self.attempt('invisible(system("R --no-echo -f authors-code/analysis.R"))\n'
                     'invisible(system("R --no-echo < authors-code/analysis.R"))\n'
                     'invisible(system("r authors-code/analysis.R"))\n'
                     "invisible(system(\"r -e 'q <- 2'\"))\n"
                     'dir.create("outputs"); write.csv(1, "outputs/r.csv")\n',
                     {"analysis.R": AUTHORS})
        doc, result = self.run_and_check(IMAGE)
        self.assertEqual(doc["state"], "complete", doc["problems"])
        self.assertEqual(result["errors"], [])
        counts = result["account"]["runs"]["run-01"]
        self.assertEqual((counts["original"], counts["stdin-original"]), (2, 1))
        self.assertEqual(doc["census"]["processes"], 5)
        self.assertEqual([i.subject for i in result["review_obligations"]
                          if getattr(i, "code", "") == "unmatched-text"],
                         [f"{lane.text_md5('q <- 2')}@the command line"])

    def test_r_cmd_install_of_a_declared_tree(self):
        """PKGBUILD: the installer and its helpers are R's own; the tree's
        code binds by reconstruction; the installed package is flagged as
        local, with its declared source's version compared."""
        self.attempt(PACKAGE_RUN.format(
            install='invisible(system("R CMD INSTALL --library=lib authors-code/mypkg"))'),
            PACKAGE)
        doc, result = self.run_and_check(IMAGE)
        self.assertEqual(doc["state"], "complete", doc["problems"])
        self.assertEqual(result["errors"], [])
        self.assertEqual([i for i in result["review_obligations"]
                          if getattr(i, "code", "") in QUIET], [])
        local = [f for f in result["flags"] if getattr(f, "code", "") == "local-package"]
        self.assertEqual([f.subject for f in local], ["mypkg"])
        self.assertIn("has the same version", local[0])
        self.assertEqual(sorted(result["account"]["originals_loaded"]), sorted(PACKAGE))
        counts = result["account"]["runs"]["run-01"]
        self.assertEqual((counts["package-install"], counts["text-package-source"]), (1, 1))


@unittest.skipUnless(image_ready(MATRIX_IMAGE), f"needs Docker and {MATRIX_IMAGE}")
class CallrDockerTests(AccountRunMixin, unittest.TestCase):
    """callr's children (callr 3.7.5), which substitute their own user
    environ file: the shim re-pins the hook (spec §8)."""

    def test_callr_children_are_instrumented_and_accounted_for(self):
        self.attempt('x <- callr::r(function() { source("authors-code/analysis.R"); x6 })\n'
                     'y <- callr::r(function() 2, user_profile = FALSE)\n'
                     'dir.create("outputs"); write.csv(x + y, "outputs/r.csv")\n',
                     {"analysis.R": AUTHORS})
        doc, result = self.run_and_check(MATRIX_IMAGE)
        self.assertEqual(doc["state"], "complete", doc["problems"])
        self.assertEqual(doc["census"]["errors"], 0)
        self.assertEqual(result["errors"], [])
        self.assertEqual([i for i in result["review_obligations"]
                          if getattr(i, "code", "") in QUIET], [])
        self.assertEqual(result["account"]["runs"]["run-01"]["tool-internal"], 4)
        self.assertEqual(result["account"]["originals_loaded"], ["analysis.R"])

    def test_remotes_and_devtools_installs_are_accounted_for(self):
        """Both build an archive of the tree in a temporary directory and
        install that through callr: bound by name and version."""
        self.attempt(PACKAGE_RUN.format(install=(
            'remotes::install_local("authors-code/mypkg", lib = "lib", upgrade = "never",\n'
            '                       force = TRUE, quiet = TRUE)\n'
            'withr::with_libpaths("lib", devtools::install(\n'
            '    "authors-code/mypkg", upgrade = "never", quiet = TRUE, reload = FALSE))')),
            PACKAGE)
        doc, result = self.run_and_check(MATRIX_IMAGE)
        self.assertEqual(doc["state"], "complete", doc["problems"])
        self.assertEqual(doc["census"]["errors"], 0)
        self.assertEqual(result["errors"], [])
        self.assertEqual([i for i in result["review_obligations"]
                          if getattr(i, "code", "") in QUIET], [])
        self.assertEqual(sorted(result["account"]["originals_loaded"]), sorted(PACKAGE))
        counts = result["account"]["runs"]["run-01"]
        self.assertEqual((counts["package-install"], counts["package-build"]), (2, 2))


@unittest.skipUnless(image_ready(MATRIX_IMAGE), f"needs Docker and {MATRIX_IMAGE}")
class AccountKnitDockerTests(AccountRunMixin, unittest.TestCase):
    """The account of a knit, in the launcher-matrix image (knitr 1.45)."""

    def test_knitting_an_original_document_is_accounted_for(self):
        """Chunk code, inline code, and chunk options all map to the document,
        and a child forked inside a chunk nests under the knit."""
        report = REPORT + ("\n```{r forked, echo=FALSE}\n"
                           "r <- parallel::mclapply(1:2, function(i) {\n"
                           "  source('analysis.R'); i }, mc.cores = 2)\n```\n")
        self.attempt('dir.create("outputs")\n'
                     'knitr::knit("authors-code/report.Rmd", output = "outputs/report.md",\n'
                     '            quiet = TRUE)\n',
                     {"report.Rmd": report, "analysis.R": AUTHORS})
        doc, result = self.run_and_check(MATRIX_IMAGE)
        self.assertEqual(doc["state"], "complete", doc["problems"])
        self.assertEqual(result["errors"], [])
        self.assertEqual(result["account"]["originals_loaded"], ["analysis.R", "report.Rmd"])
        self.assertNotIn("unmatched-text", [getattr(i, "code", "")
                                            for i in result["review_obligations"]])
        counts = result["account"]["runs"]["run-01"]
        self.assertEqual(counts["text-chunk"], 6)
        # Each FORK names the parent's knit load, and the child's source()
        # nests under its own FORK (seq 1), not under a parent's number.
        events, _ = lane.parse_events((self.dir / lane.RECORDS_DIR / "run-01" /
                                       "events.log").read_text(), doc["nonce"])
        knit = next(e for e in events if e["event"] == "LOAD"
                    and lane.decode_field(e["fields"][0]) == "knitr::knit")
        forks = [e for e in events if e["event"] == "FORK"]
        self.assertEqual(len(forks), 2)
        self.assertEqual({tuple(f["fields"]) for f in forks}, {(knit["token"], str(knit["seq"]))})
        child_loads = [e for e in events if e["token"] in {f["token"] for f in forks}
                       and e["event"] == "LOAD"]
        self.assertEqual({e["fields"][5] for e in child_loads}, {"1"})


if __name__ == "__main__":
    unittest.main()
