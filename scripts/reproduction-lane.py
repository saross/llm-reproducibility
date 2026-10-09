#!/usr/bin/env python3
"""Deterministic orchestration helpers for the agentic reproduction lane.

**Version:** 1.3

v1.3 (2026-10-09) is gate 1.3 (``wiki/planning/reproduction-gate-1-3-design.md``).
The executor no longer starts containers: ``run-container`` runs each attempt
in a private, instrumented work copy and seals what it ran and wrote, and
the gate accounts for every load, text, connection, and package the runs'
event streams record, bound to content it hashes itself. Issues carry ids
and evidence fingerprints that human rulings bind to; admission needs every
issue ruled, a passing gate, and a clean transcript audit. The gate also
removes cache stores before a run, checks wrappers for what would evade
the hook, and compares declared conversions itself. Execution snapshots and
the executor's conversion evidence are retired.

v1.2 (2026-10-05) answers the cross-model review of PR #7 (Astra, GPT in
Codex). Gate 1.1 had checked only that the executor's own records agree with
one another. Gate 1.2 adds three independent checks. (1) **Provenance
anchors:** each authors' original names a committed record that vouches for
its bytes (an evidence pack's published deposit checksum, bound to the
version the registry selects, or the corpus manifest's sha256); without one,
the result is flagged, never ``identical``. (2) **Execution snapshots:**
``snapshot-code`` hashes every code file in the attempt tree immediately
before and after the container run, and the gate fails on code that changed
between the run and the gate, changed during the run, or appeared during it
undeclared; ``outputs/`` is no longer exempt, and code paths named in
wrappers must be declared files. (3) **Conversion evidence** must be a
machine-readable, successful value-identity check bound to the current
files. ``human-queue`` rebuilds the human queue from the authoritative gate
reports, so a lossy workflow relay cannot hide a flag. The legacy bypass now
works only for attempts listed in ``reproduction-system/legacy-attempts.yaml``,
and such attempts are marked ineligible for the current gate.

v1.1 (2026-10-04) adds the authors'-code integrity check (gate 1.1) to
``check-attempt``, plus a standalone ``check-code``. Shawn's ruling
(fail-and-uplift follow-on 3): the authors' code files are hashed at
retrieval and the executed copies checked byte-identical; any difference is a
declared wrapper or a flagged edit. An undeclared difference fails the gate;
a declared edit passes with a flag for human ruling.

The reproduction workflows (``reproduction-system/workflows/``) spawn the
three governed agents — ``reproduction-planner``, ``reproduction-executor``,
``adversarial-reviewer`` — but workflow scripts have no filesystem access.
Everything that must be checked or persisted *outside* an agent's say-so
(pipeline invariants 1, 3, and 6) lives here, as plain code an operator can
re-run:

``build-plan-args``
    Turn a run configuration into hashed, commit-pinned args for the plan
    workflow. Refuses a dirty tracked tree (the launch commit must describe
    the bytes used) and refuses to re-plan an attempt that already has a plan.
    Both args builders stamp ``args_checksum``; the workflows recompute it and
    refuse to start on any mismatch, so args pasted into the Workflow tool
    cannot carry a silent transcription error.
``supersede-plans``
    Archive unapproved plans beside the run config (a blinded location)
    before a re-plan, so a new planner cannot read and anchor on the old one.
    Approved plans are locked and refused.
``persist-plans``
    Read a completed plan workflow's results (journal, else transcripts),
    validate each planner payload
    against the full plan schema plus plan-level checks, and write
    ``reproduction-plan.json`` (the record the approval binds to),
    ``reproduction-plan.md`` (the human view), and a triage report for
    batched approval. An approved plan is locked: it is never overwritten.
``approve``
    Record a human approval decision bound to the plan file's sha256
    (invariant 1: no execution from an unapproved plan).
``build-exec-args``
    Args for the execute workflow, built only for papers whose committed plan
    carries an approval whose hash still matches. Unapproved papers are listed
    as skipped, never silently dropped.
``check-attempt``
    The deterministic artefact gate (invariants 2, 3, 5, 6): required files
    exist and are non-empty; ``comparisons/comparison.json`` validates; its
    target ids match the locked plan one-to-one; coverage is recomputed from
    the outcomes; publisher files are absent; the Docker image exists; and the
    authors'-code manifest (``authors-code-manifest.json``) proves every
    executed authors' file byte-identical to its retrieved original, with
    every other code file a declared wrapper. Declared edits are flagged.
``check-code``
    The authors'-code integrity check alone, for the human lane (no plan
    JSON) and for retroactive checks.
``snapshot-code``
    Retired at gate 1.3 (it refuses). Its snapshots are still read for
    attempts executed under gate 1.2, which the gate marks ineligible.
``run-container``
    Gate 1.3's lane-owned run (``wiki/planning/reproduction-gate-1-3-design.md``).
    Copies the attempt's input tree to a private work copy, instruments it
    (an exec shim over the image's R front end and a profile hook, so every
    R process reports itself on Docker's log stream), runs the entry with
    networking off, collects what the run wrote into ``outputs/run-NN/``,
    and seals the records in ``lane-records/run-NN/``. ``--detach`` and
    ``--finalise`` split a multi-hour run; ``--consume`` declares an earlier
    run's output as an input; ``--keep-store`` keeps a cache store. At gate
    1.3 a new attempt needs these records.
``human-queue``
    Rebuild the human queue for a run from the authoritative on-disk gate
    reports, and report any flag a workflow relay failed to carry.
``persist-results``
    Write executor and reviewer payloads from the journal into the attempt
    directory, checking the review's overall verdict against the framework's
    concern-count rule.
``audit-run``
    Post-run audit of a workflow run directory: receipts re-validated from
    transcripts (shared with ``reconcile-run.py``), blinded-path accesses
    (Read/Grep/Glob plus Bash commands), writes outside scope, tokens
    deduplicated per API request, API-equivalent cost, and wall-clock; and,
    for each executor, the attempt's ``transcript-audit.json``: paper code
    run other than through ``run-container``, writes into the lane's records
    or outputs, and calls and records that do not pair.

Usage:
    venv/bin/python scripts/reproduction-lane.py build-plan-args \\
        --config <run-config.yaml> --scratch-root <dir> [--out FILE]
    venv/bin/python scripts/reproduction-lane.py persist-plans \\
        --config <run-config.yaml> --run-dir <workflow-run-dir> [--force]
    venv/bin/python scripts/reproduction-lane.py approve --config <cfg> \\
        --slug <slug> --decision approve|hold|reject --approver NAME [--note T]
    venv/bin/python scripts/reproduction-lane.py build-exec-args \\
        --config <run-config.yaml> --scratch-root <dir> [--out FILE]
    venv/bin/python scripts/reproduction-lane.py check-attempt <attempt-dir> \\
        [--plan FILE] [--image TAG] [--forbid-sha256 HEX ...] \\
        [--code-manifest FILE] [--legacy-attempt] [--out FILE|-]
    venv/bin/python scripts/reproduction-lane.py check-code <attempt-dir> \\
        [--manifest FILE] [--legacy-attempt] [--out FILE|-]
    venv/bin/python scripts/reproduction-lane.py run-container <attempt-dir> \\
        --image TAG --entry FILE [--mount-path PATH] [--launch-commit SHA] \\
        [--work-root DIR] [--consume run-NN:files/PATH ...] [--keep-store PATH ...] \\
        [--detach] [--keep-work]
    venv/bin/python scripts/reproduction-lane.py run-container <attempt-dir> \\
        --finalise run-NN
    venv/bin/python scripts/reproduction-lane.py human-queue \\
        --config <run-config.yaml> [--workflow-result FILE] [--out FILE]
    venv/bin/python scripts/reproduction-lane.py persist-results \\
        --config <run-config.yaml> --run-dir <workflow-run-dir> [--force]
    venv/bin/python scripts/reproduction-lane.py audit-run \\
        --config <run-config.yaml> --run-dir <workflow-run-dir> [--out FILE]

Example (the Phase 2 shakedown):
    venv/bin/python scripts/reproduction-lane.py build-plan-args \\
        --config studies/open-science-compliance/outputs/validation/\\
phase2-shakedown/run-config.yaml --scratch-root /tmp/llmr-scratch \\
        --out /tmp/llmr-scratch/plan-args.json
"""

from __future__ import annotations

import argparse
import contextlib
import contextvars
import hashlib
import importlib.machinery
import importlib.util
import json
import os
import posixpath
import re
import secrets
import shutil
import subprocess
import sys
import tempfile
from collections import Counter
from collections.abc import Iterator
from datetime import date as date_type, datetime, time as time_type, timedelta, timezone
from pathlib import Path
from types import ModuleType
from typing import Any, Self
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
HOOKS_DIR = REPO_ROOT / ".claude" / "hooks"
EFFORT_LEVELS = ("low", "medium", "high", "xhigh", "max")
PLAN_FILE = "reproduction-plan.json"
PLAN_VIEW_FILE = "reproduction-plan.md"
APPROVAL_FILE = "plan-approval.json"
GATE_FILE = "gate-report.json"
EXECUTION_FILE = "execution-report.json"
REVIEW_FILE = "adversarial-review.json"
COMPARISON_FILE = Path("comparisons") / "comparison.json"
DEFAULT_COMPARISON_SCHEMA = "reproduction-system/schemas/comparison-record.json"
GATE_VERSION = "1.3"
# Authors'-code integrity (gate 1.1; Shawn's ruling 2026-10-04, fail-and-uplift
# follow-on 3): the authors' files are hashed at retrieval and every executed
# copy must be byte-identical. Any difference is a declared wrapper or a
# flagged edit; an undeclared difference fails the gate.
CODE_MANIFEST_FILE = "authors-code-manifest.json"
RULINGS_FILE = "flag-rulings.json"
AUDIT_FILE = "transcript-audit.json"
DEFAULT_CODE_MANIFEST_SCHEMA = "reproduction-system/schemas/authors-code-manifest.json"
# File suffixes (lower-cased) treated as code in the closed-world inventory;
# names beginning "Dockerfile" count too. Since gate 1.2 nothing is exempt:
# code under outputs/ is inventoried like any other (review of PR #7: an
# edited copy placed there and sourced by a wrapper went unseen).
CODE_SUFFIXES = frozenset({".r", ".rmd", ".qmd", ".rnw", ".py", ".ipynb", ".sh", ".jl",
                           ".do", ".m", ".sql", ".stan", ".js", ".cpp", ".c", ".h", ".hpp",
                           ".jags", ".bug", ".bugs"})
# Start-up and build files that run code without a code suffix (Fable review
# of PR #7, P2-1): R reads ./.Rprofile and Rprofile.site at start-up.
CODE_NAMES = frozenset({".rprofile", "rprofile.site", ".renviron", "makefile"})
# A file passed to a loader is code whatever its suffix (Fable review, P1-1:
# an edited copy saved as .txt and sourced was invisible). R loaders take a
# quoted path; shell launchers may take an unquoted one.
LOADER_R_RE = re.compile(
    r"\b(?:source|sys\.source|parse|knit|knit2html|purl|render|quarto_render|sourceCpp"
    r"|load_all|jags\.model|stan_model|stan)\s*\(\s*(?:(?:file|input|path|model\.file)\s*="
    r"\s*)?[\"']([^\"'\n]+)[\"']")
LOADER_PY_RE = re.compile(r"\bexec\s*\(\s*open\s*\(\s*[\"']([^\"'\n]+)[\"']")
LOADER_SHELL_RE = re.compile(
    r"(?:^|[\s;&|(`\"'])(?:Rscript|python3?|bash|sh|quarto\s+render|R\s+-f|R\s+CMD\s+BATCH"
    r"|source|\.)\s+(?:-{1,2}[\w=-]+\s+)*[\"']?([^\s\"';|&)`]+)", re.MULTILINE)
# Wrapper constructs that patch functions in memory after the authors' file is
# sourced (Fable review, P3-1): invisible to byte identity, so a review
# obligation.
PATCHING_RE = re.compile(r"\bbody\s*\(|\bformals\s*\(|\btrace\s*\(|assignInNamespace"
                         r"|unlockBinding|\benvironment\s*\([^)]*\)\s*<-|<<-")
# Dockerfile lines that edit files at build time, or copy code into the image
# (Fable review, P1-3).
DOCKER_EDIT_RE = re.compile(
    r"^\s*RUN\b.*(?:\bsed\b|\bpatch\b|\bperl\s+-p?i|\bawk\b|\btee\b|>>|<<)",
    re.IGNORECASE | re.MULTILINE)
DOCKER_COPY_RE = re.compile(r"^\s*(?:COPY|ADD)\s+(?!https?://)(.+)$",
                            re.IGNORECASE | re.MULTILINE)
# Records a provenance anchor may rely on (Fable review, P1-2): the gate, not
# the manifest, chooses them, and they must exist unchanged at the launch commit.
EVIDENCE_PACK_ROOT = "corpus/evidence-packs"
CORPUS_MANIFESTS = ("studies/open-science-compliance/corpus/manifest.yaml",
                    "corpus/development-manifest.yaml")
# A wrapper sharing this many substantive lines with an authors' original is
# flagged. This is a heuristic: it catches verbatim inlining, not a
# re-implementation spelled differently, so wrapper semantics remain a review
# obligation for the adversarial reviewer.
EMBEDDED_LINES_FLAG = 5
# Execution snapshots (gate 1.2): code hashes taken by snapshot-code
# immediately before and after the container run.
SNAPSHOT_DIR = "execution-snapshots"
SNAPSHOT_PHASES = ("pre", "post")
# Attempts executed before gate 1.1, the only ones the legacy bypass covers.
LEGACY_ATTEMPTS_FILE = "reproduction-system/legacy-attempts.yaml"
DEFAULT_REGISTRY = "corpus/evidence-packs/declared-links.yaml"
DEFAULT_CORPUS_ROOT = "~/corpora/llm-reproducibility"
CORPUS_PREFIX = "$CORPUS_ROOT/"
# Quoted string literals naming a code file, as a wrapper would source or run it.
CODE_REF_RE = re.compile(r"""["']([^"'\n]+?\.(?:R|r|Rmd|rmd|qmd|Rnw|py|ipynb|sh|jl))["']""")
# Constructs that run code the gate cannot see by reading file names.
DYNAMIC_EVAL_RE = re.compile(
    r"\bparse\s*\(|\b(?:sys\.)?source\s*\(\s*[^\"'\s)]"
    r"|\bexec\s*\(|\bRscript\s+-e\b")
# Dockerfile lines that bring content into the image from outside the attempt.
DOCKER_FETCH_RE = re.compile(
    r"^\s*ADD\s+https?://|^\s*RUN\b.*\b(?:curl|wget|git\s+clone|install_github"
    r"|install_gitlab|install_url)\b", re.IGNORECASE | re.MULTILINE)
# Static start-up checks (gate 1.3 spec §10). Start-up options that skip
# the hook, a script on standard input (R < file), and launchers that avoid
# the front end are errors in a wrapper; options that change start-up
# meaning without evading the hook are flags.
SKIP_HOOK_RE = re.compile(r"(?<![\w-])--(vanilla|no-init-file)\b")
STARTUP_FLAG_RE = re.compile(r"(?<![\w-])--(no-environ|no-site-file)\b")
STDIN_SCRIPT_RE = re.compile(r"\bR(?:\s+--?[\w-]+(?:=\S+)?)*\s*<\s*[\w./-]+")
LITTLER_RE = re.compile(r"\br\s+\S+\.[Rr]\b")
CMD_CHECK_RE = re.compile(r"\bR\s+CMD\s+check\b")
# Hook integrity: errors in a wrapper, flags in an original. An "=" counts
# as assignment only at the start of a statement, so that an argument name
# (f(parse = TRUE)) does not.
LOADER_NAMES = r"(?:source|sys\.source|parse|loadNamespace)"
HOOK_INTEGRITY_RE = re.compile(
    r"\b(?:untrace|tracingState)\s*\("
    r"|\bSys\.(?:un)?setenv\s*\([^)]*\bR_(?:PROFILE_USER|ENVIRON_USER|PROFILE)\b"
    rf"|(?<![\w.$@]){LOADER_NAMES}\s*<<?-"
    rf"|^\s*{LOADER_NAMES}\s*=(?!=)"
    rf"|\bassign\s*\(\s*[\"']{LOADER_NAMES}[\"']", re.MULTILINE)
# A function an original defines, by name (name <- function, name = function).
FUNCTION_DEF_RE = re.compile(r"^\s*([A-Za-z.][\w.]*)\s*(?:<<?-|=)\s*function\b", re.MULTILINE)
RENVIRON_STARTUP_RE = re.compile(r"^\s*(R_PROFILE_USER|R_PROFILE|R_ENVIRON_USER)\s*=",
                                 re.MULTILINE)
DOCKER_STARTUP_RE = re.compile(
    r"Rprofile\.site|Renviron\.site|/etc/R\b"
    r"|^\s*(?:COPY|ADD)\b.*\s(?:\$\{?R_HOME\}?|/usr/local/lib/R|/usr/lib/R)/bin\b",
    re.IGNORECASE | re.MULTILINE)
SUBSTANTIVE_MIN_CHARS = 12
TRIVIAL_LINE_RE = re.compile(r"^(#|//|library\(|require\(|suppress\w*\(library"
                             r"|import |from \S+ import )")
FLAG_EDIT_PREFIX = "FLAGGED EDIT: "
FLAG_PREFIX = "FLAG: "
# Coverage numerator (coverage-rules v1.0): reproduced exactly or within the
# pre-stated tolerance. MINOR_DISCREPANCY is outside tolerance by definition.
REPRODUCED_OUTCOMES = {"EXACT_MATCH", "WITHIN_PRECISION", "WITHIN_CONFIDENCE"}

# Single source of format truth with reproduction-system/workflows/*.js:
# every governed spawn prompt carries these lines verbatim. Change both
# together.
PROVENANCE_RE = re.compile(
    r"Provenance: run (\S+); launch commit ([0-9a-f]{40}); "
    r"reasoning effort pinned: (low|medium|high|xhigh|max)\.")
# Leading whitespace is allowed: since Claude Code 2.1.288 (observed
# 2026-10-03, wf_5d10728a-820) the harness delivers a workflow prompt as a
# "[Workflow harness — computed task]" message with every line indented.
PAPER_RE = re.compile(r"^\s*Paper: (\S+)$", re.MULTILINE)
SCRATCH_RE = re.compile(r"^\s*Scratch directory: (\S+)$", re.MULTILINE)
ATTEMPT_DIR_RE = re.compile(r"^\s*Attempt directory: (\S+)$", re.MULTILINE)
# Tokens in a Bash command that could name a local file: split on shell
# punctuation, then keep path-like tokens that are not URLs (a URL's path
# segment — e.g. a Wikipedia /wiki/ link — is not a local access).
SHELL_SPLIT_RE = re.compile(r"[\s'\"=;|&<>()`,]+")
DATE_SUFFIX_RE = re.compile(r"-\d{8}$")
# The harness spills an over-long tool result to a file and says so in the
# result text; reading back one's OWN spill is not an out-of-scope access.
SPILL_RE = re.compile(r"Full output saved to: (\S+)")


# ---------------------------------------------------------------------------
# Shared helpers
# ---------------------------------------------------------------------------

def load_module(name: str, rel_path: str) -> ModuleType:
    """Import a hyphen-named repository script as a module.

    Args:
        name: Module name to register.
        rel_path: Path of the script relative to the repository root.

    Returns:
        The executed module object.
    """
    loader = importlib.machinery.SourceFileLoader(name, str(REPO_ROOT / rel_path))
    spec = importlib.util.spec_from_loader(name, loader)
    module = importlib.util.module_from_spec(spec)
    loader.exec_module(module)
    return module


def expand(path_text: str) -> Path:
    """Resolve a config path: ``~`` expands; relative paths are repo-relative."""
    path = Path(str(path_text)).expanduser()
    return path if path.is_absolute() else REPO_ROOT / path


def display_path(path: Path | str) -> str:
    """Repo-relative form where possible, ``~/``-relative otherwise."""
    text = str(path)
    for base, label in ((str(REPO_ROOT) + "/", ""), (str(Path.home()) + "/", "~/")):
        if text.startswith(base):
            return label + text[len(base):]
    return text


def sha256_file(path: Path) -> str:
    """Return the sha256 hex digest of a file's bytes."""
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def now_utc() -> str:
    """Current UTC time, ISO 8601 to the second."""
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def write_json(path: Path, payload: Any) -> None:
    """Write pretty, key-stable JSON with a trailing newline."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
                    encoding="utf-8")


def emit(payload: Any, out: Path | None) -> None:
    """Write JSON to ``out`` or print it to stdout."""
    if out is None:
        print(json.dumps(payload, indent=2, ensure_ascii=False))
    else:
        write_json(out, payload)
        print(f"wrote {display_path(out)}")


class LaneError(Exception):
    """A refused operation; the message is shown to the operator verbatim."""


# Each issue code's policy version. Bump a code's version when its check's
# meaning changes; every ruling on that code then expires, and no other.
ISSUE_POLICY: dict[str, int] = {}
RULING_DECISIONS = {"flag": ("admissible", "fail-and-uplift", "excluded"),
                    "obligation": ("discharged", "fail-and-uplift", "excluded")}


def json_digest(value: Any) -> str:
    """sha256 of a value's canonical JSON (sorted keys, no spaces)."""
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"),
                                     ensure_ascii=False).encode("utf-8")).hexdigest()


def file_digests(target_dir: Path, *rels: str | None) -> dict[str, str]:
    """sha256 of each named attempt file, for an issue's evidence fingerprint.

    A path that is absent, or outside the attempt and the corpus store,
    records as ``missing``, so a file appearing later changes the print.
    """
    digests = {}
    for rel in rels:
        if rel:
            path = resolve_stored(target_dir, rel)
            digests[rel] = (sha256_file(path) if path is not None and path.is_file()
                            else "missing")
    return digests


class Issue(str):
    """A flag or review obligation: its message, with a stable identity.

    Gate 1.3 binds each human ruling to an issue id and an evidence
    fingerprint, not to the message text (Astra's design review, point 7;
    spec §6). An ``Issue`` *is* its message, since ``str`` is its base, so
    every list, report, relay, and test that carries flags as text keeps
    working; the identity travels with it.

    - ``kind``: ``flag`` or ``obligation``.
    - ``code`` and ``subject``: the issue id is ``code:subject``, stable
      across re-runs (``edited-copy:authors-code/analysis.R``).
    - ``targets``: the target ids it bears on; empty means all.
    - ``files``: the sha256 of every file it concerns. With the code's
      policy version, the subject, and the targets, these make the
      fingerprint, so changed evidence needs a new ruling.
    """

    kind: str
    code: str
    subject: str
    targets: tuple[str, ...]
    files: dict[str, str]

    def __new__(cls, message: str, *, kind: str, code: str, subject: str,
                targets: tuple[str, ...] | list[str] = (),
                files: dict[str, str] | None = None) -> Self:
        issue = super().__new__(cls, message)
        issue.kind, issue.code, issue.subject = kind, code, subject
        issue.targets = tuple(sorted(set(targets)))
        issue.files = dict(files or {})
        return issue

    @classmethod
    def flag(cls, code: str, subject: str, text: str, prefix: str = FLAG_PREFIX,
             **identity: Any) -> Self:
        """A flag, its message prefixed as the human queue expects."""
        return cls(prefix + text, kind="flag", code=code, subject=subject, **identity)

    @classmethod
    def obligation(cls, code: str, subject: str, text: str, **identity: Any) -> Self:
        """A review obligation."""
        return cls(text, kind="obligation", code=code, subject=subject, **identity)

    @property
    def issue_id(self) -> str:
        """``code:subject``."""
        return f"{self.code}:{self.subject}"

    def fingerprint(self) -> str:
        """sha256 over the policy version, the id, the targets, and the files."""
        return json_digest({"code": self.code, "policy": ISSUE_POLICY.get(self.code, 1),
                            "subject": self.subject, "targets": list(self.targets),
                            "files": self.files})

    def record(self) -> dict:
        """The issue as the gate report lists it."""
        return {"id": self.issue_id, "kind": self.kind, "code": self.code,
                "subject": self.subject, "targets": list(self.targets),
                "files": self.files, "fingerprint": self.fingerprint(),
                "message": str(self)}


def issue_records(messages: list[str]) -> list[dict]:
    """Structured records for a list of flags or obligations.

    A plain string, from a site not yet given an identity, becomes an
    ``unclassified`` issue keyed by its own text: still rulable, but any
    change of wording expires its ruling.
    """
    records = []
    for message in messages:
        if isinstance(message, Issue):
            records.append(message.record())
        else:
            kind = "flag" if str(message).startswith((FLAG_PREFIX, FLAG_EDIT_PREFIX)) \
                else "obligation"
            records.append(Issue(message, kind=kind, code="unclassified",
                                 subject=json_digest(str(message))[:16]).record())
    return records


def args_checksum(payload: dict) -> str:
    """Integrity checksum of workflow args, mirrored in the workflow scripts.

    Workflow args travel inline in the Workflow tool call, so ~10 KB of JSON
    (hashes included) passes through a copy step nothing else re-checks.
    The builder stamps this checksum; each workflow recomputes it over the
    args it actually received and refuses to start on mismatch.

    Algorithm (must match the JavaScript in reproduction-system/workflows/):
    compact JSON (``separators=(",", ":")``, non-ASCII unescaped, key order
    as built) read as UTF-16 code units, hashed by 32-bit FNV-1a and 32-bit
    djb2-xor; the result is the two as 8-digit hex, concatenated.

    Raises:
        LaneError: if the payload holds a float (Python and JavaScript
            serialise some floats differently, e.g. ``1.0`` vs ``1``).
    """
    def reject_floats(node: Any) -> None:
        if isinstance(node, float):
            raise LaneError("args contain a float — checksum serialisation would differ "
                            "between Python and JavaScript")
        if isinstance(node, dict):
            for value in node.values():
                reject_floats(value)
        elif isinstance(node, list):
            for value in node:
                reject_floats(value)

    reject_floats(payload)
    text = json.dumps(payload, separators=(",", ":"), ensure_ascii=False)
    raw = text.encode("utf-16-le")
    fnv, djb = 2166136261, 5381
    for index in range(0, len(raw), 2):
        unit = raw[index] | (raw[index + 1] << 8)
        fnv = ((fnv ^ unit) * 16777619) & 0xFFFFFFFF
        djb = (((djb * 33) & 0xFFFFFFFF) ^ unit) & 0xFFFFFFFF
    return f"{fnv:08x}{djb:08x}"


def emit_args(payload: dict, out: Path | None) -> None:
    """Stamp ``args_checksum`` (last key) and emit workflow args."""
    payload = dict(payload)
    payload.pop("args_checksum", None)
    payload["args_checksum"] = args_checksum(payload)
    emit(payload, out)


def load_config(path: Path) -> dict:
    """Load and validate a reproduction run configuration.

    Args:
        path: The run-config YAML file.

    Returns:
        The parsed configuration, with ``_path`` set to its location.

    Raises:
        LaneError: on any missing or malformed required field.
    """
    try:
        config = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except (OSError, yaml.YAMLError) as exc:
        raise LaneError(f"run config unreadable: {exc}") from exc
    problems = []
    for key in ("run_id", "attempt", "effort", "output_root", "agents", "schemas",
                "blinding", "papers"):
        if key not in config:
            problems.append(f"missing key {key!r}")
    if problems:
        raise LaneError("run config invalid: " + "; ".join(problems))
    if not isinstance(config["attempt"], int) or config["attempt"] < 1:
        problems.append("attempt must be a positive integer")
    if config["effort"] not in EFFORT_LEVELS:
        problems.append(f"effort must be one of {EFFORT_LEVELS}")
    for role in ("planner", "executor", "reviewer"):
        if not (config["agents"] or {}).get(role):
            problems.append(f"agents.{role} missing")
    for name in ("plan", "execution", "review", "comparison_record"):
        if not (config["schemas"] or {}).get(name):
            problems.append(f"schemas.{name} missing")
    if not isinstance((config["blinding"] or {}).get("forbidden_substrings"), list):
        problems.append("blinding.forbidden_substrings must be a list")
    slugs = [p.get("slug") for p in config["papers"] or []]
    if not slugs or not all(slugs) or len(set(slugs)) != len(slugs):
        problems.append("papers must be a non-empty list with unique slugs")
    if problems:
        raise LaneError("run config invalid: " + "; ".join(problems))
    config["_path"] = path
    return config


def attempt_dir(config: dict, slug: str) -> Path:
    """The paper's attempt directory for this run."""
    return (expand(config["output_root"]) / slug / "reproduction"
            / f"attempt-{config['attempt']:02d}")


def runtime_schema(path: Path) -> dict:
    """A schema as handed to agent(): the document-version field stripped.

    The registered file carries a non-standard ``version`` keyword (the
    manifest's E4 carrier); the spawn-side validator is strict JSON Schema
    and rejects top-level combinators (2026-08-17 S4 probe), so both are
    removed from the runtime copy. The registered file stays the contract of
    record and is applied in full post-run.
    """
    schema = json.loads(path.read_text(encoding="utf-8"))
    schema.pop("version", None)
    for combinator in ("allOf", "anyOf", "oneOf"):
        schema.pop(combinator, None)
    return schema


def full_schema(path: Path) -> dict:
    """The registered schema file, for complete post-run validation."""
    return json.loads(path.read_text(encoding="utf-8"))


def schema_problems(payload: Any, schema: dict) -> list[str]:
    """Validate a payload against a draft-07 schema; return readable errors."""
    import jsonschema  # local import: only the validating subcommands need it
    validator = jsonschema.Draft7Validator(schema)
    problems = []
    for error in sorted(validator.iter_errors(payload),
                        key=lambda e: [str(p) for p in e.absolute_path]):
        where = "/".join(str(part) for part in error.absolute_path) or "(root)"
        problems.append(f"schema violation at {where}: {error.message[:200]}")
    return problems


def resolve_launch_commit() -> str:
    """HEAD hash, refusing modified tracked files (shared with the benchmark).

    Reuses ``build-benchmark-args.py``'s implementation so the two lanes
    cannot drift on what "clean enough to launch" means.
    """
    builder = load_module("build_benchmark_args", "scripts/build-benchmark-args.py")
    try:
        return builder.resolve_launch_commit(REPO_ROOT)
    except RuntimeError as exc:
        raise LaneError(str(exc)) from exc


def require_committed(path: Path) -> None:
    """Refuse unless ``path`` is tracked by git and unmodified against HEAD.

    Args:
        path: File that the launch commit must contain.

    Raises:
        LaneError: if the file is untracked or differs from HEAD.
    """
    rel = display_path(path)
    tracked = subprocess.run(["git", "-C", str(REPO_ROOT), "ls-files",
                              "--error-unmatch", rel],
                             capture_output=True, text=True, timeout=30)
    if tracked.returncode != 0:
        raise LaneError(f"{rel} is not committed — commit plans and approvals "
                        f"before building execute args")
    diff = subprocess.run(["git", "-C", str(REPO_ROOT), "diff", "--quiet", "HEAD",
                           "--", rel], capture_output=True, text=True, timeout=30)
    if diff.returncode != 0:
        raise LaneError(f"{rel} differs from HEAD — commit it first")


def paper_inputs(paper: dict) -> dict:
    """Existence-check and hash a paper's PDF and supplements.

    Returns:
        ``{paper_pdf, paper_pdf_sha256, supplements: [{path, sha256}]}``
        with absolute paths (agents receive absolute paths).

    Raises:
        LaneError: if any declared file is missing.
    """
    pdf = expand(paper["paper_pdf"])
    if not pdf.is_file():
        raise LaneError(f"{paper['slug']}: paper PDF missing: {pdf}")
    supplements = []
    for supp in paper.get("supplements") or []:
        supp_path = expand(supp)
        if not supp_path.is_file():
            raise LaneError(f"{paper['slug']}: supplement missing: {supp_path}")
        supplements.append({"path": str(supp_path), "sha256": sha256_file(supp_path)})
    return {"paper_pdf": str(pdf), "paper_pdf_sha256": sha256_file(pdf),
            "supplements": supplements}


def receipt_keys(agent_type: str) -> list[str]:
    """Names of the instruments pushed to ``agent_type`` — the receipt keys.

    Read from the manifest through the hooks' own library, so the keys an
    agent is told to use are exactly the keys the receipt gate checks. The
    first plan round (wf_5d10728a-820) showed why they must be stated: when
    the push payload is spilled to a file the agent may not see the name
    attributes, and one planner keyed by file stem instead.
    """
    sys.path.insert(0, str(HOOKS_DIR))
    try:
        import hooklib  # noqa: PLC0415 — hooks dir is not a package
    finally:
        sys.path.pop(0)
    names = [spec["name"] for spec in hooklib.pushed_instruments(hooklib.load_manifest(),
                                                                  agent_type)]
    if not names:
        raise LaneError(f"no pushed instruments registered for {agent_type!r}")
    return names


def blinding_args(config: dict) -> dict:
    """The blinding block handed to every governed spawn."""
    blinding = config["blinding"]
    return {"forbidden_substrings": list(blinding["forbidden_substrings"]),
            "cross_paper_slugs": list(blinding.get("cross_paper_slugs") or [])}


# ---------------------------------------------------------------------------
# Plan stage
# ---------------------------------------------------------------------------

def cmd_build_plan_args(args: argparse.Namespace) -> int:
    """Build args for reproduction-plan.workflow.js."""
    config = load_config(args.config)
    launch_commit = resolve_launch_commit()
    papers = []
    for paper in config["papers"]:
        target_dir = attempt_dir(config, paper["slug"])
        if (target_dir / APPROVAL_FILE).exists():
            raise LaneError(f"{paper['slug']}: {display_path(target_dir / APPROVAL_FILE)} "
                            f"exists — an approved plan is locked and cannot be re-planned")
        if (target_dir / PLAN_FILE).exists():
            raise LaneError(f"{paper['slug']}: {display_path(target_dir / PLAN_FILE)} "
                            f"already exists — run supersede-plans and commit first, so "
                            f"the new planner cannot read (and anchor on) the old plan")
        scratch = Path(args.scratch_root).expanduser() / config["run_id"] / paper["slug"]
        papers.append({"slug": paper["slug"],
                       "attempt_dir": str(target_dir),
                       **paper_inputs(paper),
                       "deposits": paper.get("deposits") or [],
                       "run_notes": str(paper.get("run_notes") or "").strip(),
                       "scratch_dir": str(scratch / "planner")})
    emit_args({"run_id": config["run_id"], "attempt": config["attempt"],
               "effort": config["effort"], "launch_commit": launch_commit,
               "agent_type": config["agents"]["planner"],
               "receipt_keys": receipt_keys(config["agents"]["planner"]),
               "rulings": [str(r).strip() for r in config.get("rulings") or []],
               "schema": runtime_schema(expand(config["schemas"]["plan"])),
               "blinding": blinding_args(config), "papers": papers}, args.out)
    return 0


def first_user_text(lines: list[str]) -> str:
    """The spawn prompt: every user message before the agent's first reply.

    Workflow spawns may open with more than one user message — current
    harness versions relay the triggering user request first, then the
    script's prompt as an indented "computed task" message — so all user
    text preceding the first assistant entry is joined. Tool results are
    not text blocks and are skipped.
    """
    parts: list[str] = []
    for line in lines:
        try:
            entry = json.loads(line)
        except json.JSONDecodeError:
            continue
        message = entry.get("message")
        if not isinstance(message, dict):
            continue
        if message.get("role") == "assistant":
            break
        if message.get("role") != "user":
            continue
        content = message.get("content")
        if isinstance(content, str):
            parts.append(content)
        elif isinstance(content, list):
            parts.append("".join(str(b.get("text", "")) for b in content
                                 if isinstance(b, dict) and b.get("type") == "text"))
    return "\n".join(parts)


def structured_output(lines: list[str]) -> dict | None:
    """The accepted StructuredOutput payload in a transcript, if any.

    Schema-forced spawns return their result through a StructuredOutput
    tool call; a call the validator rejected comes back with an errored
    tool_result and is retried, so the last call whose result did not
    error is the accepted payload.
    """
    calls: list[tuple[str, dict]] = []
    errored: dict[str, bool] = {}
    for line in lines:
        try:
            entry = json.loads(line)
        except json.JSONDecodeError:
            continue
        message = entry.get("message")
        content = message.get("content") if isinstance(message, dict) else None
        for block in content if isinstance(content, list) else []:
            if not isinstance(block, dict):
                continue
            if (block.get("type") == "tool_use" and block.get("name") == "StructuredOutput"
                    and isinstance(block.get("input"), dict)):
                calls.append((str(block.get("id")), block["input"]))
            elif block.get("type") == "tool_result":
                errored[str(block.get("tool_use_id"))] = bool(block.get("is_error"))
    accepted = [payload for use_id, payload in calls if not errored.get(use_id, False)]
    return accepted[-1] if accepted else None


def journal_results(run_dir: Path) -> list[dict]:
    """Every agent result in a workflow run: journal first, transcripts second.

    The journal records each agent's return value. Agents it does not
    record — for example those of a nested sub-workflow — are recovered
    from their transcripts'
    accepted StructuredOutput payload, so persistence never depends on one
    harness bookkeeping channel.

    Returns:
        ``[{agent_id, agent_type, result, prompt, source}]`` — ``result``
        is the agent's return value (``None`` when it died), ``prompt`` the
        spawn prompt, ``source`` "journal" or "transcript".

    Raises:
        LaneError: if the run directory holds neither journal nor transcripts.
    """
    journal = run_dir / "journal.jsonl"
    transcripts = sorted(run_dir.glob("agent-*.jsonl"))
    if not journal.is_file() and not transcripts:
        raise LaneError(f"no journal.jsonl or agent transcripts in {run_dir}")
    results = []
    journal_lines = (journal.read_text(encoding="utf-8").splitlines()
                     if journal.is_file() else [])
    for line in journal_lines:
        try:
            entry = json.loads(line)
        except json.JSONDecodeError:
            continue
        if entry.get("type") != "result":
            continue
        agent_id = str(entry.get("agentId") or "")
        meta_path = run_dir / f"agent-{agent_id}.meta.json"
        meta = (json.loads(meta_path.read_text(encoding="utf-8"))
                if meta_path.is_file() else {})
        transcript = run_dir / f"agent-{agent_id}.jsonl"
        lines = (transcript.read_text(encoding="utf-8").splitlines()
                 if transcript.is_file() else [])
        results.append({"agent_id": agent_id,
                        "agent_type": str(meta.get("agentType") or ""),
                        "result": entry.get("result"),
                        "prompt": first_user_text(lines), "source": "journal"})
    seen = {item["agent_id"] for item in results}
    for transcript in transcripts:
        agent_id = transcript.stem.replace("agent-", "")
        if agent_id in seen:
            continue
        meta_path = run_dir / f"agent-{agent_id}.meta.json"
        meta = (json.loads(meta_path.read_text(encoding="utf-8"))
                if meta_path.is_file() else {})
        lines = transcript.read_text(encoding="utf-8").splitlines()
        results.append({"agent_id": agent_id,
                        "agent_type": str(meta.get("agentType") or ""),
                        "result": structured_output(lines),
                        "prompt": first_user_text(lines), "source": "transcript"})
    return results


def select_results(results: list[dict], agent_type: str,
                   config: dict) -> tuple[dict[str, dict], list[str]]:
    """One result per configured paper for a governed agent type.

    The paper is bound twice — by the prompt's ``Paper:`` line and by the
    payload's ``paper_slug`` — and the two must agree (a payload naming a
    different paper than its spawn is substitution, not a result).

    Returns:
        ``(chosen, dead)``: results keyed by paper slug, and the paper slugs
        whose agent returned nothing (died after harness retries) — reported
        to the operator, never silently dropped.

    Raises:
        LaneError: on a binding mismatch, an unknown slug, or duplicates.
    """
    known = {p["slug"] for p in config["papers"]}
    chosen: dict[str, dict] = {}
    dead: list[str] = []
    for item in results:
        if item["agent_type"] != agent_type:
            continue
        prompt_match = PAPER_RE.search(item["prompt"])
        prompt_slug = prompt_match.group(1) if prompt_match else ""
        payload = item["result"] if isinstance(item["result"], dict) else None
        payload_slug = str((payload or {}).get("paper_slug") or "")
        if payload is None:
            dead.append(prompt_slug or f"? (agent {item['agent_id']})")
            continue
        if prompt_slug != payload_slug:
            raise LaneError(f"agent {item['agent_id']}: prompt names {prompt_slug!r} but "
                            f"payload names {payload_slug!r} — not bound to its item")
        if payload_slug not in known:
            raise LaneError(f"agent {item['agent_id']}: unknown paper {payload_slug!r}")
        if payload_slug in chosen:
            raise LaneError(f"two {agent_type} results for {payload_slug} "
                            f"({chosen[payload_slug]['agent_id']}, {item['agent_id']}) — "
                            f"resolve by hand")
        chosen[payload_slug] = item
    return chosen, dead


def plan_checks(plan: dict) -> tuple[list[str], list[str]]:
    """Plan-level checks the runtime schema cannot express.

    Returns:
        ``(errors, warnings)``. Errors block persistence; warnings go to the
        approver in the triage report.
    """
    errors: list[str] = []
    warnings: list[str] = []
    if plan.get("status") == "ESCALATE":
        if not str(plan.get("escalate_reason") or "").strip():
            errors.append("ESCALATE without escalate_reason")
        return errors, warnings
    for section in ("paper", "reproduction_type", "materials", "environment",
                    "execution_steps", "verification_targets", "enumeration_check",
                    "eligibility"):
        if not plan.get(section):
            errors.append(f"status OK but section {section!r} missing or empty")
    targets = plan.get("verification_targets") or []
    ids = [t.get("target_id") for t in targets]
    duplicates = sorted({i for i in ids if ids.count(i) > 1})
    if duplicates:
        errors.append(f"duplicate target ids: {duplicates}")
    check = plan.get("enumeration_check") or {}
    if check and check.get("targets_enumerated") != len(targets):
        errors.append(f"enumeration_check.targets_enumerated "
                      f"({check.get('targets_enumerated')}) != targets listed ({len(targets)})")
    if check and check.get("items_excluded") != len(plan.get("exclusions") or []):
        warnings.append(f"enumeration_check.items_excluded ({check.get('items_excluded')}) "
                        f"!= exclusions listed ({len(plan.get('exclusions') or [])})")
    detected = check.get("display_items_detected")
    if isinstance(detected, int) and detected > len(targets) + len(plan.get("exclusions") or []):
        warnings.append(f"display items detected ({detected}) exceed targets + exclusions "
                        f"({len(targets)} + {len(plan.get('exclusions') or [])}) — "
                        f"enumeration may be incomplete")
    if check.get("flag_for_human"):
        warnings.append("planner flagged the enumeration for human attention")
    eligibility = plan.get("eligibility") or {}
    for key in ("computational_component", "code_available", "primary_language_r",
                "within_compute_cap"):
        if eligibility.get(key) is False:
            warnings.append(f"eligibility.{key} is false")
    return errors, warnings


def md_cell(value: Any) -> str:
    """Make a value safe for a Markdown table cell."""
    return str(value if value is not None else "—").replace("|", "\\|").replace("\n", " ")


def render_plan(record: dict) -> str:
    """Render a persisted plan record as Markdown for the human approver."""
    plan = record["plan"]
    out = [f"# Reproduction plan — {plan.get('paper_slug')}",
           "",
           f"Generated from `{PLAN_FILE}` by `scripts/reproduction-lane.py "
           f"persist-plans`; do not edit (the approval binds to the JSON's sha256).",
           "",
           f"- **Run:** {record['run_id']} (workflow run `{record['workflow_run']}`, "
           f"agent `{record['agent_id']}`)",
           f"- **Launch commit:** `{record.get('launch_commit') or 'not found'}`; "
           f"effort `{record.get('effort') or 'not found'}`",
           f"- **Status:** {plan.get('status')}"]
    if plan.get("status") == "ESCALATE":
        out += ["", f"**Escalation:** {plan.get('escalate_reason')}"]
        return "\n".join(out) + "\n"
    paper = plan.get("paper") or {}
    rtype = plan.get("reproduction_type") or {}
    out += [f"- **Paper:** {paper.get('title')} — doi:{paper.get('doi')}",
            f"- **Reproduction type:** {', '.join(rtype.get('types') or [])} — "
            f"{rtype.get('rationale')}", "", "## Materials", "",
            "| Name | Kind | Location | Version | Access route | Checksum |",
            "|---|---|---|---|---|---|"]
    for m in plan.get("materials") or []:
        out.append("| " + " | ".join(md_cell(m.get(k)) for k in
                                      ("name", "kind", "location", "version",
                                       "access_route", "checksum")) + " |")
    env = plan.get("environment") or {}
    out += ["", "## Environment", "",
            f"- Provided by authors: {env.get('provided_by_authors')}",
            f"- Planned base image: `{env.get('planned_base_image')}`",
            f"- Language version target: {env.get('language_version_target')}",
            f"- Packages: {', '.join(env.get('packages') or []) or '—'}",
            "", "## Execution steps", ""]
    for step in plan.get("execution_steps") or []:
        out.append(f"{step.get('step')}. {step.get('action')} — *expected:* "
                   f"{step.get('expected_output')}")
    out += ["", f"## Verification targets ({len(plan.get('verification_targets') or [])}"
            f" — the locked denominator on approval)", "",
            "| Id | Display item | Location | Values | Type | Tolerance | Published values |",
            "|---|---|---|---|---|---|---|"]
    for t in plan.get("verification_targets") or []:
        out.append("| " + " | ".join(md_cell(t.get(k)) for k in
                                      ("target_id", "display_item", "location", "n_values",
                                       "analysis_type", "tolerance",
                                       "published_values_source")) + " |")
    out += ["", "Target descriptions and comparison methods:", ""]
    for t in plan.get("verification_targets") or []:
        out.append(f"- **{t.get('target_id')}** {t.get('description')} "
                   f"*Method:* {t.get('comparison_method')}")
    out += ["", "## Exclusions", ""]
    out += [f"- {e.get('item')} ({e.get('location')}): {e.get('reason')}"
            for e in plan.get("exclusions") or []] or ["- none"]
    check = plan.get("enumeration_check") or {}
    out += ["", "## Enumeration-completeness check", "",
            f"- Method: {check.get('method')}",
            f"- Display items detected: {check.get('display_items_detected')}; "
            f"targets enumerated: {check.get('targets_enumerated')}; excluded: "
            f"{check.get('items_excluded')}; flagged for human: "
            f"{check.get('flag_for_human')}",
            f"- Notes: {check.get('notes')}", "", "## Eligibility", ""]
    out += [f"- {k}: {v}" for k, v in (plan.get("eligibility") or {}).items()]
    out += ["", "## Data retrieval plan", ""]
    out += [f"- **{d.get('dataset')}** — stated: {d.get('stated_route')}; planned: "
            f"{d.get('planned_retrieval')}" for d in plan.get("data_retrieval_plan") or []] \
        or ["- none listed"]
    out += ["", "## Risks", ""]
    out += [f"- ({r.get('likelihood', '?')}) {r.get('risk')} — *mitigation:* "
            f"{r.get('mitigation')}" for r in plan.get("risks") or []] or ["- none listed"]
    out += ["", "## Compute strategy", "", str(plan.get("compute_strategy") or "—"),
            "", "## Scope limitations", ""]
    out += [f"- {s}" for s in plan.get("scope_limitations") or []] or ["- none"]
    out += ["", "## Questions for the approver", ""]
    out += [f"- {q}" for q in plan.get("questions_for_approver") or []] or ["- none"]
    if record.get("warnings"):
        out += ["", "## Orchestrator warnings", ""]
        out += [f"- {w}" for w in record["warnings"]]
    return "\n".join(out) + "\n"


def supersede_plan(config: dict, slug: str) -> Path:
    """Move an unapproved plan out of the attempt directory before a re-plan.

    The archive sits beside the run config (a blinded location), keyed by
    the superseded plan's workflow run, so the executor never sees two
    plans and nothing is lost.

    Returns:
        The archive directory.

    Raises:
        LaneError: if the plan is approved (approved plans are locked).
    """
    target_dir = attempt_dir(config, slug)
    if (target_dir / APPROVAL_FILE).exists():
        raise LaneError(f"{slug}: plan is approved and locked — cannot supersede it")
    old_record = json.loads((target_dir / PLAN_FILE).read_text(encoding="utf-8"))
    archive = (Path(config["_path"]).parent / "superseded-plans"
               / str(old_record.get("workflow_run") or "unknown") / slug)
    archive.mkdir(parents=True, exist_ok=True)
    for name in (PLAN_FILE, PLAN_VIEW_FILE):
        if (target_dir / name).exists():
            (target_dir / name).replace(archive / name)
    return archive


def cmd_supersede_plans(args: argparse.Namespace) -> int:
    """Archive unapproved plans so a paper can be re-planned independently."""
    config = load_config(args.config)
    slugs = [p["slug"] for p in config["papers"]] if args.all else [args.slug]
    for slug in slugs:
        if slug not in {p["slug"] for p in config["papers"]}:
            raise LaneError(f"unknown paper {slug!r}")
        if not (attempt_dir(config, slug) / PLAN_FILE).exists():
            print(f"{slug}: no plan to supersede")
            continue
        print(f"{slug}: archived to {display_path(supersede_plan(config, slug))}")
    return 0


def cmd_persist_plans(args: argparse.Namespace) -> int:
    """Persist planner payloads from a plan-workflow run, plus a triage report."""
    config = load_config(args.config)
    run_dir = args.run_dir.expanduser().resolve()
    planner = config["agents"]["planner"]
    chosen, _dead = select_results(journal_results(run_dir), planner, config)
    # Dead spawns and never-spawned papers both surface as missing plans.
    missing = [p["slug"] for p in config["papers"] if p["slug"] not in chosen]
    schema = full_schema(expand(config["schemas"]["plan"]))
    rows = []
    blocking = []
    for slug, item in sorted(chosen.items()):
        plan = item["result"]
        errors = schema_problems(plan, schema)
        check_errors, warnings = plan_checks(plan)
        errors += check_errors
        provenance = PROVENANCE_RE.search(item["prompt"])
        if not provenance:
            errors.append("spawn prompt carries no Provenance line")
        target_dir = attempt_dir(config, slug)
        if (target_dir / APPROVAL_FILE).exists():
            errors.append(f"{display_path(target_dir / APPROVAL_FILE)} exists — the plan "
                          f"is approved and locked (coverage-rules denominator lock)")
        elif (target_dir / PLAN_FILE).exists() and not args.force:
            errors.append(f"{display_path(target_dir / PLAN_FILE)} exists — pass --force "
                          f"to replace an unapproved plan")
        if errors:
            blocking.append((slug, errors))
            continue
        if (target_dir / PLAN_FILE).exists():
            archive = supersede_plan(config, slug)
            print(f"superseded plan archived to {display_path(archive)}")
        record = {"plan_record_version": "1.0", "run_id": config["run_id"],
                  "attempt": config["attempt"], "workflow_run": run_dir.name,
                  "agent_id": item["agent_id"],
                  "launch_commit": provenance.group(2) if provenance else None,
                  "effort": provenance.group(3) if provenance else None,
                  "persisted_at": now_utc(), "warnings": warnings, "plan": plan}
        write_json(target_dir / PLAN_FILE, record)
        (target_dir / PLAN_VIEW_FILE).write_text(render_plan(record), encoding="utf-8")
        rows.append((slug, plan, warnings, sha256_file(target_dir / PLAN_FILE)))
        print(f"persisted {display_path(target_dir / PLAN_FILE)}")
    triage = Path(config["_path"]).parent / f"triage-{run_dir.name}.md"
    triage.write_text(render_triage(config, run_dir, rows, blocking, missing),
                      encoding="utf-8")
    print(f"wrote {display_path(triage)}")
    for slug, errors in blocking:
        print(f"BLOCKED {slug}: " + "; ".join(errors), file=sys.stderr)
    if missing:
        print(f"MISSING plans (never returned): {missing}", file=sys.stderr)
    return 1 if blocking or missing else 0


def render_triage(config: dict, run_dir: Path, rows: list, blocking: list,
                  missing: list) -> str:
    """One-page triage report for batched plan approval (plan §4.4)."""
    out = [f"# Plan triage — {config['run_id']}", "",
           f"Workflow run `{run_dir.name}`; generated {now_utc()} by "
           f"`scripts/reproduction-lane.py persist-plans`. Approve, hold, or reject each "
           f"plan with `reproduction-lane.py approve`. On approval the target list "
           f"becomes the locked coverage denominator.", "",
           "| Paper | Status | Type | Targets | Excluded | Detected | Compute (h) | "
           "Flags | Plan sha256 |",
           "|---|---|---|---|---|---|---|---|---|"]
    for slug, plan, warnings, digest in rows:
        check = plan.get("enumeration_check") or {}
        out.append("| " + " | ".join(md_cell(v) for v in (
            slug, plan.get("status"),
            ",".join((plan.get("reproduction_type") or {}).get("types") or []),
            len(plan.get("verification_targets") or []),
            len(plan.get("exclusions") or []), check.get("display_items_detected"),
            (plan.get("eligibility") or {}).get("estimated_compute_hours"),
            len(warnings), digest[:12])) + " |")
    for slug, plan, warnings, _ in rows:
        if warnings or plan.get("questions_for_approver"):
            out += ["", f"## {slug}", ""]
            out += [f"- ⚠ {w}" for w in warnings]
            out += [f"- ❓ {q}" for q in plan.get("questions_for_approver") or []]
    if blocking:
        out += ["", "## Not persisted (blocking problems)", ""]
        out += [f"- **{slug}:** " + "; ".join(errors) for slug, errors in blocking]
    if missing:
        out += ["", "## Missing (no planner result)", ""]
        out += [f"- {slug}" for slug in missing]
    return "\n".join(out) + "\n"


def cmd_approve(args: argparse.Namespace) -> int:
    """Record a plan decision bound to the plan file's current sha256."""
    config = load_config(args.config)
    if args.slug not in {p["slug"] for p in config["papers"]}:
        raise LaneError(f"unknown paper {args.slug!r}")
    target_dir = attempt_dir(config, args.slug)
    plan_path = target_dir / PLAN_FILE
    if not plan_path.is_file():
        raise LaneError(f"no plan to approve: {display_path(plan_path)}")
    digest = sha256_file(plan_path)
    approval_path = target_dir / APPROVAL_FILE
    if approval_path.exists():
        existing = json.loads(approval_path.read_text(encoding="utf-8"))
        if existing.get("decision") == "approve":
            raise LaneError(f"{display_path(approval_path)} already records an approval "
                            f"(plan sha256 {str(existing.get('plan_sha256'))[:12]}…) — "
                            f"approved plans are locked")
        if not args.force:
            raise LaneError(f"{display_path(approval_path)} exists "
                            f"(decision {existing.get('decision')!r}); pass --force to "
                            f"replace a hold/reject")
    plan = json.loads(plan_path.read_text(encoding="utf-8"))["plan"]
    if args.decision == "approve" and plan.get("status") != "OK":
        raise LaneError("cannot approve a plan whose status is not OK")
    record = {"approval_record_version": "1.0", "run_id": config["run_id"],
              "slug": args.slug, "attempt": config["attempt"],
              "decision": args.decision, "approver": args.approver,
              "decided_at": now_utc(), "plan_file": display_path(plan_path),
              "plan_sha256": digest,
              "locked_target_ids": [t["target_id"]
                                    for t in plan.get("verification_targets") or []],
              "note": args.note or ""}
    write_json(approval_path, record)
    print(f"recorded {args.decision} for {args.slug} → {display_path(approval_path)} "
          f"(plan sha256 {digest[:12]}…, {len(record['locked_target_ids'])} locked targets)")
    return 0


def attempt_issues(target_dir: Path, report: dict) -> dict[str, dict]:
    """An attempt's rulable issues, by id: the gate report's, then the
    transcript audit's (spec §12: a host run before the final run)."""
    issues = {i["id"]: i for i in report.get("issues") or []}
    try:
        audit = json.loads((target_dir / AUDIT_FILE).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        audit = {}
    for issue in audit.get("issues") or []:
        issues.setdefault(issue["id"], issue)
    return issues


def cmd_rule_flags(args: argparse.Namespace) -> int:
    """Record human rulings on an attempt's issues (spec §6).

    Each ruling binds to the issue's id and its current evidence
    fingerprint, read from the authoritative gate report, so it lapses when
    the evidence changes. The rulings file is JSON: a list (or ``{"rulings":
    [...]}``) of ``{"issue": "<id>", "decision": "...", "note": "..."}``.
    Flags take ``admissible``, ``fail-and-uplift``, or ``excluded``;
    obligations take ``discharged``, ``fail-and-uplift``, or ``excluded``.
    A gate failure is not an issue and cannot be ruled.
    """
    config = load_config(args.config)
    if args.slug not in {p["slug"] for p in config["papers"]}:
        raise LaneError(f"unknown paper {args.slug!r}")
    target_dir = attempt_dir(config, args.slug)
    gate_path = target_dir / GATE_FILE
    try:
        report = json.loads(gate_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise LaneError(f"no readable authoritative gate report: {exc}") from exc
    issues = attempt_issues(target_dir, report)
    if not issues:
        raise LaneError(f"{display_path(gate_path)} lists no issues (a pre-1.3 report, or "
                        f"nothing to rule)")
    given = json.loads(args.rulings.expanduser().read_text(encoding="utf-8"))
    given = given.get("rulings") if isinstance(given, dict) else given
    if not isinstance(given, list) or not given:
        raise LaneError("the rulings file holds no rulings")
    new = []
    for entry in given:
        issue = issues.get(str(entry.get("issue")))
        if issue is None:
            raise LaneError(f"no issue {entry.get('issue')!r} in the gate report; its issues "
                            f"are: {', '.join(sorted(issues))}")
        allowed = RULING_DECISIONS[issue["kind"]]
        if entry.get("decision") not in allowed:
            raise LaneError(f"{issue['id']} is a {issue['kind']}: rule it {', '.join(allowed)}")
        if not str(entry.get("note") or "").strip():
            raise LaneError(f"{issue['id']}: a ruling needs a note saying why")
        new.append({"issue_id": issue["id"], "fingerprint": issue["fingerprint"],
                    "kind": issue["kind"], "decision": entry["decision"],
                    "note": entry["note"], "approver": args.approver, "ruled_at": now_utc(),
                    "gate_report_sha256": sha256_file(gate_path)})
    rulings = load_rulings(target_dir) + new
    write_json(target_dir / RULINGS_FILE, {"rulings_version": "1.0", "slug": args.slug,
                                           "rulings": rulings})
    open_ids = [i for i, issue in issues.items() if ruling_for(issue, rulings) is None]
    print(f"recorded {len(new)} ruling(s) for {args.slug} in "
          f"{display_path(target_dir / RULINGS_FILE)}; {len(open_ids)} issue(s) still "
          f"unruled" + (f": {', '.join(open_ids)}" if open_ids else ""))
    return 0


# ---------------------------------------------------------------------------
# Execute stage
# ---------------------------------------------------------------------------

def cmd_build_exec_args(args: argparse.Namespace) -> int:
    """Build args for reproduction-execute.workflow.js (approved papers only)."""
    config = load_config(args.config)
    launch_commit = resolve_launch_commit()
    papers, skipped = [], []
    for paper in config["papers"]:
        slug = paper["slug"]
        target_dir = attempt_dir(config, slug)
        plan_path, approval_path = target_dir / PLAN_FILE, target_dir / APPROVAL_FILE
        if not plan_path.is_file() or not approval_path.is_file():
            skipped.append({"slug": slug, "reason": "no plan or no approval record"})
            continue
        approval = json.loads(approval_path.read_text(encoding="utf-8"))
        if approval.get("decision") != "approve":
            skipped.append({"slug": slug,
                            "reason": f"decision is {approval.get('decision')!r}"})
            continue
        digest = sha256_file(plan_path)
        if approval.get("plan_sha256") != digest:
            raise LaneError(f"{slug}: plan sha256 {digest[:12]}… does not match the "
                            f"approved {str(approval.get('plan_sha256'))[:12]}… — the plan "
                            f"changed after approval")
        require_committed(plan_path)
        require_committed(approval_path)
        if (target_dir / COMPARISON_FILE).exists():
            raise LaneError(f"{slug}: {display_path(target_dir / COMPARISON_FILE)} already "
                            f"exists — this attempt has been executed")
        plan = json.loads(plan_path.read_text(encoding="utf-8"))["plan"]
        scratch = Path(args.scratch_root).expanduser() / config["run_id"] / slug
        papers.append({"slug": slug, "attempt": config["attempt"],
                       "attempt_dir": str(target_dir), "plan_path": str(plan_path),
                       "plan_sha256": digest, "approval_path": str(approval_path),
                       "target_ids": [t["target_id"] for t in plan["verification_targets"]],
                       **paper_inputs(paper),
                       "deposits": paper.get("deposits") or [],
                       "run_notes": str(paper.get("run_notes") or "").strip(),
                       "executor_scratch_dir": str(scratch / "executor"),
                       "image_tag": f"llmr-{slug}-attempt-{config['attempt']:02d}"})
    if not papers:
        raise LaneError("no approved papers — nothing to execute: "
                        + "; ".join(f"{s['slug']}: {s['reason']}" for s in skipped))
    emit_args({"run_id": config["run_id"], "attempt": config["attempt"],
               "effort": config["effort"], "launch_commit": launch_commit,
               "agent_types": {"executor": config["agents"]["executor"],
                               "reviewer": config["agents"]["reviewer"]},
               "receipt_keys": {"executor": receipt_keys(config["agents"]["executor"]),
                                "reviewer": receipt_keys(config["agents"]["reviewer"])},
               "rulings": [str(r).strip() for r in config.get("rulings") or []],
               "schemas": {"execution": runtime_schema(expand(config["schemas"]["execution"])),
                           "review": runtime_schema(expand(config["schemas"]["review"]))},
               "comparison_schema_path": str(expand(config["schemas"]["comparison_record"])),
               "repo_root": str(REPO_ROOT),
               "blinding": blinding_args(config), "papers": papers, "skipped": skipped},
              args.out)
    return 0


# ---------------------------------------------------------------------------
# Authors'-code integrity (gate 1.1)
# ---------------------------------------------------------------------------

def is_code_file(path: Path) -> bool:
    """True when ``path`` counts as code by its name alone.

    Code suffixes, start-up and build files (``.Rprofile``, ``Rprofile.site``,
    ``.Renviron``, ``Makefile``), and any name containing ``dockerfile``
    (``r.dockerfile`` included). A file passed to a loader is code whatever
    its name; ``loader_references`` finds those.
    """
    name = path.name.lower()
    return ("dockerfile" in name or name in CODE_NAMES
            or path.suffix.lower() in CODE_SUFFIXES)


def loader_references(text: str, shell: bool) -> set[str]:
    """Paths a file passes to a code loader, quoted (R, Python) or not (shell).

    Args:
        text: The file's text.
        shell: Also parse unquoted shell launchers (``Rscript x``, ``R -f x``,
            ``bash x``, ``. x``). R files are parsed for these too, because they
            appear inside ``system()`` strings.
    """
    found = set(LOADER_R_RE.findall(text)) | set(LOADER_PY_RE.findall(text))
    found |= set(LOADER_SHELL_RE.findall(text)) if shell or "system" in text else set()
    # A path has a slash or a dot; a bare word (an ``Rscript -e`` expression,
    # a shell builtin argument) is not a file, and inline expressions are
    # reported separately as dynamic evaluation.
    return {ref for ref in found if ref and not ref.startswith(("-", "$", "http"))
            and ("/" in ref or "." in ref) and "+" not in ref and "(" not in ref}


def walk_tree(target_dir: Path) -> tuple[list[Path], list[str]]:
    """Every regular file in the attempt tree, and its symlink problems.

    A directory symlink would hide a tree from the inventory, and a link
    resolving outside the attempt would make the gate vouch for files it does
    not hold (Fable review, P2-2). Both are reported; a file symlink inside
    the tree is followed and hashed like any file.

    Returns:
        ``(files, problems)``, with snapshot records and bytecode caches
        excluded from ``files``.
    """
    files: list[Path] = []
    problems: list[str] = []
    if not target_dir.is_dir():
        return files, problems
    root = target_dir.resolve()
    for dirpath, dirnames, filenames in os.walk(target_dir, followlinks=False):
        here = Path(dirpath)
        rel_dir = here.relative_to(target_dir)
        if rel_dir.parts[:1] in ((SNAPSHOT_DIR,), ("__pycache__",)) or "__pycache__" in \
                rel_dir.parts:
            dirnames[:] = []
            continue
        for name in list(dirnames):
            if (here / name).is_symlink():
                problems.append(f"directory symlink {(rel_dir / name).as_posix()}: it hides "
                                f"a tree from the inventory")
                dirnames.remove(name)
        for name in sorted(filenames):
            path = here / name
            if path.is_symlink():
                target = path.resolve()
                if root not in target.parents:
                    problems.append(f"symlink {(rel_dir / name).as_posix()} resolves outside "
                                    f"the attempt directory")
                    continue
            if path.is_file():
                files.append(path)
    return sorted(files), problems


# Digests shared within one pass over the tree, keyed by (resolved path,
# algorithm) and holding (file identity, digest). None means no pass is open,
# and then nothing is cached. A ContextVar rather than a module global, so
# that the scope ends exactly where the ``with`` block (or decorated call)
# that opened it ends.
_DIGEST_SCOPE: contextvars.ContextVar[
    dict[tuple[str, str], tuple[tuple[int, ...], str]] | None] = \
    contextvars.ContextVar("digest_scope", default=None)


@contextlib.contextmanager
def digest_snapshot() -> Iterator[None]:
    """Share file digests across one pass that treats the tree as immutable.

    A deposit archive can be hundreds of megabytes and is consulted once per
    original (Fable review, P3-4), so one pass reads each file once. The cache
    lives only as long as that pass. A cache that outlived it, keyed by size
    and modification time, returned the old digest for an edit that kept the
    size and restored the time, so a change across a run went unseen (Astra's
    gate 1.3 design review, point 5). Each snapshot and each gate check
    therefore opens its own scope, and an inner scope starts empty.

    Works as a ``with`` block or, through ``contextlib.ContextDecorator``, as
    a decorator that opens a fresh scope on every call.
    """
    token = _DIGEST_SCOPE.set({})
    try:
        yield
    finally:
        _DIGEST_SCOPE.reset(token)


def cached_digest(path: Path, algorithm: str = "sha256") -> str:
    """A file's digest, read at most once within the current digest scope.

    Outside a scope (see ``digest_snapshot``) nothing is cached. Inside one,
    a repeated request returns the first digest once the file's identity
    (device, inode, size, and modification and change times) is confirmed
    unchanged. The change time cannot be set back by a user, so a same-size
    edit with a restored modification time still shows, where the
    filesystem's clock is fine enough to separate the two writes.

    Raises:
        LaneError: when a file already read in this scope has changed, since
            the pass assumed an immutable tree and its result would be mixed.
    """
    stat = path.stat()
    identity = (stat.st_dev, stat.st_ino, stat.st_size, stat.st_mtime_ns, stat.st_ctime_ns)
    cache = _DIGEST_SCOPE.get()
    key = (str(path.resolve()), algorithm)
    if cache is not None and key in cache:
        seen, digest = cache[key]
        if seen != identity:
            raise LaneError(f"{display_path(path)} changed while the tree was being read: "
                            f"re-run once nothing is writing to the attempt")
        return digest
    hasher = hashlib.new(algorithm)
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            hasher.update(block)
    digest = hasher.hexdigest()
    if cache is not None:
        cache[key] = (identity, digest)
    return digest


def inside(target_dir: Path, rel: str) -> Path | None:
    """Resolve a manifest path inside the attempt directory.

    Args:
        target_dir: The attempt directory.
        rel: A path as written in the manifest.

    Returns:
        The resolved path, or None when ``rel`` is absolute or escapes the
        attempt directory (the gate can only vouch for files it can read
        there, and scratch is never part of the artefact set).
    """
    if not rel or Path(rel).is_absolute():
        return None
    root = target_dir.resolve()
    resolved = (root / rel).resolve()
    return resolved if resolved == root or root in resolved.parents else None


def substantive_lines(text: str) -> set[str]:
    """Whitespace-normalised code lines long enough to identify their source.

    Comments, package loads, and short lines (braces, ``}``, ``x <- 1``) are
    dropped, so a wrapper and an original sharing them proves nothing.
    """
    lines = set()
    for raw in text.splitlines():
        line = " ".join(raw.split())
        if len(line) >= SUBSTANTIVE_MIN_CHARS and not TRIVIAL_LINE_RE.match(line):
            lines.add(line)
    return lines


def lines_changed(original: bytes, edited: bytes) -> dict[str, int]:
    """Size of an edit as lines changed (ruling 2026-10-04, item 6).

    Uses difflib's opcodes over the two texts' lines. ``changed`` counts each
    replaced block at the larger of its two sides, plus pure insertions and
    deletions, so a one-line substitution is 1, not 2.

    Returns:
        ``{"changed": n, "removed": r, "added": a}``.
    """
    import difflib  # local import: only flagged edits need it
    old = original.decode("utf-8", errors="replace").splitlines()
    new = edited.decode("utf-8", errors="replace").splitlines()
    changed = removed = added = 0
    matcher = difflib.SequenceMatcher(None, old, new, autojunk=False)
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == "equal":
            continue
        changed += max(i2 - i1, j2 - j1)
        removed += i2 - i1
        added += j2 - j1
    return {"changed": changed, "removed": removed, "added": added}


def archive_member_bytes(archive: Path, member: str) -> bytes:
    """Read one member from a zip or tar archive.

    Raises:
        KeyError: if the member is absent.
        ValueError: if the archive format is not zip or tar.
    """
    import tarfile  # local imports: only archive-backed originals need them
    import zipfile
    if zipfile.is_zipfile(archive):
        with zipfile.ZipFile(archive) as handle:
            return handle.read(member)
    if tarfile.is_tarfile(archive):
        with tarfile.open(archive) as handle:
            extracted = handle.extractfile(member)
            if extracted is None:
                raise KeyError(member)
            return extracted.read()
    raise ValueError(f"not a zip or tar archive: {archive.name}")


def corpus_root() -> Path:
    """The out-of-tree corpus store: ``$CORPUS_ROOT``, else the default."""
    return Path(os.environ.get("CORPUS_ROOT") or DEFAULT_CORPUS_ROOT).expanduser().resolve()


def resolve_stored(target_dir: Path, rel: str) -> Path | None:
    """Resolve a manifest path in the attempt directory or the corpus store.

    A path beginning ``$CORPUS_ROOT/`` names a file in the out-of-tree store,
    where deposit archives and publisher supplements live, because they may
    not enter git. Any other path must lie inside the attempt directory.

    Returns:
        The resolved path, or None when it escapes its root.
    """
    if rel.startswith(CORPUS_PREFIX):
        root = corpus_root()
        resolved = (root / rel[len(CORPUS_PREFIX):]).resolve()
        return resolved if root in resolved.parents else None
    return inside(target_dir, rel)


def committed_unmodified(repo_root: Path, rel: str) -> str | None:
    """Check that a file is tracked by git and unmodified against HEAD.

    A provenance anchor is independent of the executor only if the record it
    relies on was committed before the run and has not been edited since.

    Returns:
        None when the file is tracked and clean, else the problem found.
    """
    if not (repo_root / rel).is_file():
        return f"{rel} not found"
    # Inherited GIT_* variables (a hook exports GIT_DIR) would override -C and
    # make the check read another repository.
    env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
    try:
        tracked = subprocess.run(["git", "-C", str(repo_root), "ls-files", "--error-unmatch",
                                  "--", rel], capture_output=True, text=True, timeout=60,
                                 env=env)
        if tracked.returncode != 0:
            return f"{rel} is not tracked by git"
        clean = subprocess.run(["git", "-C", str(repo_root), "diff", "--quiet", "HEAD", "--",
                                rel], capture_output=True, text=True, timeout=60, env=env)
    except (OSError, subprocess.SubprocessError) as exc:
        return f"git unavailable to verify {rel}: {exc}"
    return None if clean.returncode == 0 else f"{rel} has uncommitted changes"


def bound_at_launch(repo_root: Path, rel: str, launch: str | None) -> str | None:
    """Check that a record existed at the launch commit and is unchanged since.

    "Tracked and clean" alone is satisfied by a record the executor writes and
    the operator later commits with the run's artefacts (Fable review of PR
    #7, P1-2). A record the run relies on must predate the run.

    Args:
        repo_root: The repository.
        rel: The record's repository-relative path.
        launch: The run's launch commit, or None when not supplied.

    Returns:
        None when the record is tracked, clean, present at ``launch``, and
        unchanged since; otherwise the problem. With ``launch`` None, only
        tracked-and-clean is checked (the caller treats the anchor as unbound).
    """
    problem = committed_unmodified(repo_root, rel)
    if problem or launch is None:
        return problem
    env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
    try:
        present = subprocess.run(["git", "-C", str(repo_root), "cat-file", "-e",
                                  f"{launch}:{rel}"], capture_output=True, text=True,
                                 timeout=60, env=env)
        if present.returncode != 0:
            return f"{rel} did not exist at the launch commit {launch[:12]}"
        same = subprocess.run(["git", "-C", str(repo_root), "diff", "--quiet", launch,
                               "HEAD", "--", rel], capture_output=True, text=True,
                              timeout=60, env=env)
    except (OSError, subprocess.SubprocessError) as exc:
        return f"git unavailable to verify {rel} at the launch commit: {exc}"
    return None if same.returncode == 0 else (f"{rel} changed after the launch commit "
                                              f"{launch[:12]}")


def registry_principal_links(repo_root: Path, slug: str,
                             launch: str | None = None) -> list[dict] | None:
    """A paper's principal links in the curated declared-links registry.

    Returns:
        The links whose ``role`` is ``principal``, or None when the registry
        is not committed and clean, or not as it was at ``launch`` (it then
        cannot vouch for anything).
    """
    if bound_at_launch(repo_root, DEFAULT_REGISTRY, launch) is not None:
        return None
    registry = yaml.safe_load((repo_root / DEFAULT_REGISTRY).read_text(encoding="utf-8")) or {}
    spec = (registry.get("papers") or {}).get(slug) or {}
    return [link for link in spec.get("links") or [] if link.get("role") == "principal"]


def registry_selected_dois(repo_root: Path, slug: str,
                           launch: str | None = None) -> set[str] | None:
    """The deposit versions the registry selects for a paper (AP-12).

    For each principal link, its ``scored_version`` if it has one, else the
    link itself.

    Returns:
        Lower-cased identifiers, or None when the registry is not committed
        and clean, or not as it was at ``launch``.
    """
    links = registry_principal_links(repo_root, slug, launch)
    if links is None:
        return None
    return {str(link.get("scored_version") or link.get("link") or "").lower()
            for link in links}


def git_blob_sha1(data: bytes) -> str:
    """The git object id of a file's bytes, as ``git hash-object`` computes it."""
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def candidate_packs(repo_root: Path, slug: str, named: str | None) -> list[str]:
    """Evidence packs that may anchor a paper, newest harvest first.

    The gate chooses: ``corpus/evidence-packs/harvest-*/<slug>.json`` in
    descending order, then ``corpus/evidence-packs/<slug>.json``. A pack the
    manifest names is used only if it is one of these (Fable review, P1-2: a
    pack written inside the attempt directory must never anchor anything).
    """
    root = repo_root / EVIDENCE_PACK_ROOT
    found = sorted((p.relative_to(repo_root).as_posix()
                    for p in root.glob(f"harvest-*/{slug}.json")), reverse=True)
    found.append(f"{EVIDENCE_PACK_ROOT}/{slug}.json")
    if named:
        return [named] if named in found else []
    return found


def verify_anchor(item: dict, target_dir: Path, repo_root: Path, slug: str | None,
                  original: bytes | None,
                  launch: str | None = None) -> tuple[str, list[str], list[str]]:
    """Check one original's provenance anchor against an independent record.

    Gate 1.1 compared the executor's files with hashes in the executor's own
    manifest, so a file edited before it was hashed passed as identical (PR #7
    review, finding 1). An anchor names a record the executor did not write:

    - ``evidence-pack``: a committed evidence pack whose registry record
      publishes the deposit file's checksum. The deposit file (``archive.path``
      or ``local_copy``) must match it, and the record must be the version the
      registry selects under AP-12.
    - ``corpus-manifest``: a committed corpus manifest's sha256 for a file in
      the corpus store (a publisher supplement, or the source of a
      transcription). The entry must be this paper's. A checksum establishes
      the file's bytes, not that it is the paper's selected original, so the
      anchor verifies only a journal supplement (corpus role ``supplement``)
      of a paper whose registry declares a principal artefact held in the
      supplement. Any other corpus file is flagged (PR #7 delta review,
      finding 1); a deposit kept in the store is anchored through its
      evidence-pack record, which carries the AP-12 version binding.
    - ``git``: a repository, commit, path, and blob id. The gate checks that the
      blob id matches the original's bytes, but cannot reach the remote, so the
      claim stays a flag for a reviewer to confirm.

    Args:
        item: The manifest's ``originals`` entry.
        target_dir: The attempt directory.
        repo_root: The repository whose committed records anchors name.
        slug: The paper slug, which binds evidence-pack anchors to the registry.
        original: The original's bytes, recovered from its pristine copy or
            archive member, or None when they could not be recovered.
        launch: The run's launch commit. Every record an anchor relies on must
            exist at it, unchanged since. Without it, an anchor that would
            verify is ``recorded`` and flagged as unbound.

    Returns:
        ``(state, errors, flags)``. ``state`` is ``verified`` (a committed,
        independent record that predates the run vouches for the bytes),
        ``recorded`` (a checkable claim the gate cannot settle), ``failed``,
        or ``absent``.
    """
    state, errors, notes = _verify_anchor(item, target_dir, repo_root, slug, original, launch)
    if state == "verified" and launch is None:
        notes.append(("anchor-unbound", f"original {item['id']!r}: the anchor's records are "
                      f"committed but not bound to a launch commit, so they may postdate the "
                      f"run (pass --launch-commit to the authoritative gate)"))
        state = "recorded"
    # Each flag's evidence is the original's recorded digest and the anchor
    # declaration itself: a changed anchor, or changed bytes, needs a new ruling.
    evidence = {"original": str(item.get("sha256")),
                "anchor": json_digest(item.get("anchor") or {})}
    return state, errors, [Issue.flag(code, str(item["id"]), text, files=evidence)
                           for code, text in notes]


def _verify_anchor(item: dict, target_dir: Path, repo_root: Path, slug: str | None,
                   original: bytes | None,
                   launch: str | None) -> tuple[str, list[str], list[tuple[str, str]]]:
    """``verify_anchor`` before the launch-commit downgrade (see there).

    Flags are returned as ``(code, text)`` pairs; the caller gives them their
    identity.
    """
    oid = item["id"]
    anchor = item.get("anchor") or {}
    if not anchor or anchor.get("kind") == "none":
        reason = f" ({anchor['reason']})" if anchor.get("reason") else ""
        return "absent", [], [("anchor-absent", f"original {oid!r} has no independent "
                               f"provenance anchor{reason}: its identity rests on the "
                               f"executor's own manifest, which cannot show the file was "
                               f"unedited when hashed")]
    kind = anchor["kind"]

    def failed(message: str) -> tuple[str, list[str], list[tuple[str, str]]]:
        return "failed", [f"original {oid!r}: provenance anchor ({kind}): {message}"], []

    if kind == "evidence-pack":
        if slug is None:
            return failed("the paper slug is unknown, so no pack can be chosen")
        candidates = candidate_packs(repo_root, slug, anchor.get("pack"))
        if not candidates:
            return failed(f"{anchor.get('pack')!r} is not an evidence pack for {slug} under "
                          f"{EVIDENCE_PACK_ROOT}/; the gate chooses the pack, and a pack "
                          f"outside that directory never anchors")
        record = None
        pack_rel = None
        unusable: list[str] = []
        for rel in candidates:
            if not (repo_root / rel).is_file():
                continue
            problem = bound_at_launch(repo_root, rel, launch)
            if problem:
                unusable.append(problem)
                continue
            pack = json.loads((repo_root / rel).read_text(encoding="utf-8"))
            record = next((r for r in pack.get("records") or []
                           if r.get("record_id") == anchor["record_id"]
                           and r.get("status") == "resolved"), None)
            if record is not None:
                pack_rel = rel
                break
        if record is None:
            return failed(f"no usable evidence pack for {slug} holds a resolved record "
                          f"{anchor['record_id']}" + (f" ({'; '.join(unusable)})"
                                                      if unusable else ""))
        fields = record.get("fields") or {}
        entry = next((f for f in fields.get("files") or [] if f.get("key") == anchor["file"]),
                     None)
        algorithm, _, expected = str((entry or {}).get("checksum") or "").partition(":")
        if not expected or algorithm not in hashlib.algorithms_available:
            # A record without checksums cannot anchor; that is a gap in the
            # pack, not the executor's fault (Fable review, P2-5).
            return "recorded", [], [("anchor-unanchorable", f"original {oid!r} is "
                                     f"unanchorable: {pack_rel} record {anchor['record_id']} "
                                     f"publishes no usable checksum for {anchor['file']!r} "
                                     f"(re-harvest with harvester v1.2 or later)")]
        deposit_rel = (item.get("archive") or {}).get("path") or item.get("local_copy")
        deposit = resolve_stored(target_dir, deposit_rel) if deposit_rel else None
        if deposit is None or not deposit.is_file():
            return failed(f"the deposit file {anchor['file']!r} is not kept (archive.path or "
                          f"local_copy), so its published checksum cannot be checked")
        if cached_digest(deposit, algorithm) != expected.lower():
            return failed(f"{deposit_rel} does not match the {algorithm} checksum that "
                          f"{anchor['record_id']} publishes for {anchor['file']!r}")
        if original is None:
            return "failed", [], []  # the member or copy mismatch is already an error
        selected = registry_selected_dois(repo_root, slug, launch) if slug else None
        doi = str(fields.get("doi") or "").lower()
        if selected is None:
            return "recorded", [], [("anchor-registry-unclean", f"original {oid!r}: the "
                                     f"registry is not committed and clean, so the anchored "
                                     f"version cannot be checked against the version AP-12 "
                                     f"selects")]
        if doi not in selected:
            return "recorded", [], [("anchor-version-unselected", f"original {oid!r} is "
                                     f"anchored to {doi or '?'}, which is not a version the "
                                     f"registry selects for {slug} (AP-12): "
                                     f"{sorted(selected) or 'none'}")]
        return "verified", [], []

    if kind == "corpus-manifest":
        if slug is None or anchor["entry"] != slug:
            return failed(f"the corpus entry {anchor['entry']!r} is not this paper ({slug!r})")
        if anchor["manifest"] not in CORPUS_MANIFESTS:
            return failed(f"{anchor['manifest']!r} is not a registered corpus manifest "
                          f"({', '.join(CORPUS_MANIFESTS)})")
        problem = bound_at_launch(repo_root, anchor["manifest"], launch)
        if problem:
            return failed(problem)
        corpus = yaml.safe_load((repo_root / anchor["manifest"]).read_text(encoding="utf-8"))
        entry = next((p for p in (corpus or {}).get("papers") or []
                      if p.get("slug") == anchor["entry"]), None)
        record = next((f for f in (entry or {}).get("files") or []
                       if f.get("filename") == anchor["filename"]), None) or {}
        recorded = record.get("sha256")
        if not recorded:
            return failed(f"{anchor['manifest']} records no {anchor['filename']!r} for "
                          f"{anchor['entry']}")
        stored = corpus_root() / anchor["entry"] / anchor["filename"]
        if not stored.is_file():
            return failed(f"{anchor['entry']}/{anchor['filename']} is not in the corpus store")
        if cached_digest(stored) != recorded:
            return failed(f"the stored {anchor['filename']} does not match the corpus manifest")
        derivation = item.get("derivation")
        if derivation and derivation["from_sha256"] != recorded:
            return failed("the transcription's source digest differs from the corpus record")
        if not derivation:
            archive_rel = (item.get("archive") or {}).get("path")
            archive = resolve_stored(target_dir, archive_rel) if archive_rel else None
            if archive is not None and archive.resolve() == stored.resolve():
                if original is None:
                    return "failed", [], []  # the member mismatch is already an error
            elif recorded != item["sha256"]:
                return failed("the anchored corpus file is neither the original nor the "
                              "archive it was extracted from")
        # The bytes are now established; admissibility as this paper's selected
        # original is a separate question (PR #7 delta review, finding 1).
        links = registry_principal_links(repo_root, slug, launch)
        role = str(record.get("role") or "unstated")
        in_supplement = bool(links) and any(link.get("home") == "supplement" for link in links)
        if role != "supplement" or not in_supplement:
            reason = ("the registry is not committed and clean" if links is None else
                      f"the corpus role is {role!r}" if role != "supplement" else
                      f"the registry declares no principal artefact held in {slug}'s "
                      f"journal supplement")
            return "recorded", [], [("anchor-corpus-unselected", f"original {oid!r} is "
                                     f"anchored to corpus file {anchor['entry']}/"
                                     f"{anchor['filename']}, which establishes its bytes but "
                                     f"not that it is this paper's selected original: "
                                     f"{reason}. A deposit kept in the corpus store is "
                                     f"anchored through its evidence-pack record instead")]
        # A transcription stays "recorded": its fidelity is flagged by the caller.
        return ("recorded" if derivation else "verified"), [], []

    if kind == "git":
        if original is None:
            return failed("the original's bytes are not recoverable to compare with the blob")
        if git_blob_sha1(original) != str(anchor["blob_sha1"]).lower():
            return failed(f"blob {anchor['blob_sha1']} does not match the original's bytes")
        return "recorded", [], [("anchor-git-offline", f"original {oid!r} is anchored to "
                                 f"blob {anchor['blob_sha1'][:12]}… at "
                                 f"{anchor['repository']}@{anchor['commit'][:12]}:"
                                 f"{anchor['path']}, a claim the gate cannot verify offline: "
                                 f"a reviewer confirms it at the remote")]
    return failed(f"unknown anchor kind {kind!r}")


def tree_inventory(target_dir: Path) -> dict[str, str]:
    """sha256 of every regular file in the attempt tree, keyed by relative path.

    Since gate 1.3 snapshots record every file, not only code (Fable review,
    P1-1), so a sourced file with any name, and an edited input, are visible.
    Symlinks that escape are left out here and reported by ``walk_tree``.
    """
    files, _ = walk_tree(target_dir)
    return {path.relative_to(target_dir).as_posix(): cached_digest(path) for path in files}


def code_inventory(target_dir: Path, extra_code: set[str] | frozenset[str] = frozenset()
                   ) -> dict[str, str]:
    """sha256 of every code file in the attempt tree, keyed by relative path.

    Code is anything ``is_code_file`` names, plus ``extra_code``: the relative
    paths some file passes to a loader. Nothing is exempt, except bytecode
    caches and the snapshot records themselves.
    """
    return {rel: digest for rel, digest in tree_inventory(target_dir).items()
            if rel in extra_code or is_code_file(Path(rel))}


@digest_snapshot()  # one scope per snapshot: never shared with another
def write_snapshot(target_dir: Path, phase: str, force: bool = False) -> Path:
    """Record the attempt's code inventory at one execution boundary.

    The executor takes ``pre`` immediately before the container run and
    ``post`` immediately after. The run mounts the attempt directory, so these
    are the files the run could execute. Each snapshot is taken once.

    Raises:
        LaneError: on an unknown phase, an existing snapshot without ``force``,
            or a ``post`` snapshot with no ``pre``.
    """
    if phase not in SNAPSHOT_PHASES:
        raise LaneError(f"phase must be one of {SNAPSHOT_PHASES}")
    out = target_dir / SNAPSHOT_DIR / f"{phase}.json"
    if out.exists() and not force:
        raise LaneError(f"{display_path(out)} exists: a snapshot is taken once per run "
                        f"(pass --force only when the run itself is redone)")
    pre_path = target_dir / SNAPSHOT_DIR / "pre.json"
    record: dict[str, Any] = {"snapshot_version": "1.0", "phase": phase, "taken_at": now_utc(),
                              "tool": f"scripts/reproduction-lane.py (gate {GATE_VERSION})"}
    if phase == "pre":
        # A fresh token per run: the post snapshot must carry the same one.
        record["run_token"] = secrets.token_hex(16)
    else:
        if not pre_path.is_file():
            raise LaneError("take the pre snapshot before the run first")
        try:
            pre = json.loads(pre_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            raise LaneError(f"pre snapshot unreadable: {exc}") from exc
        record["run_token"] = pre.get("run_token")
        record["pre_sha256"] = sha256_file(pre_path)
    files, problems = walk_tree(target_dir)
    if problems:
        raise LaneError("refusing to snapshot: " + "; ".join(problems))
    record["files"] = tree_inventory(target_dir)
    write_json(out, record)
    return out


def snapshot_problems(pre_doc: Any, post_doc: Any, pre_digest: str) -> list[str]:
    """Structural and identity checks on a pair of execution snapshots.

    Reading only each record's ``files`` would not show which phase or which
    run a record belongs to (PR #7 delta review, finding 2). The pair must be
    well formed, labelled with its phases, and bound together: the post
    record carries the pre record's run token and sha256, and is not earlier.
    """
    problems: list[str] = []
    for phase, doc in (("pre", pre_doc), ("post", post_doc)):
        if not isinstance(doc, dict):
            problems.append(f"{phase} snapshot is not a JSON object")
            continue
        if doc.get("snapshot_version") != "1.0" or doc.get("phase") != phase:
            problems.append(f"{phase} snapshot has the wrong version or phase label")
        files = doc.get("files")
        if not isinstance(files, dict) or not all(
                isinstance(k, str) and isinstance(v, str) and re.fullmatch(r"[0-9a-f]{64}", v)
                for k, v in files.items()):
            problems.append(f"{phase} snapshot's files are not a map of path to sha256")
        if not isinstance(doc.get("taken_at"), str) or not doc.get("run_token"):
            problems.append(f"{phase} snapshot lacks taken_at or run_token")
    if problems:
        return problems
    if post_doc.get("run_token") != pre_doc.get("run_token"):
        problems.append("the post snapshot belongs to a different run than the pre snapshot")
    if post_doc.get("pre_sha256") != pre_digest:
        problems.append("the post snapshot does not bind the pre snapshot as it now stands")
    if post_doc["taken_at"] < pre_doc["taken_at"]:
        problems.append("the post snapshot is earlier than the pre snapshot")
    return problems


# ---------------------------------------------------------------------------
# Lane-owned execution: run-container and sealed run records (gate 1.3)
# ---------------------------------------------------------------------------
#
# Specification: wiki/planning/reproduction-gate-1-3-design.md, §§3–5 (F1 and
# the run lifecycle of F2). The executor no longer starts containers itself.
# run-container copies the attempt's input tree to a private work copy,
# instruments it, runs it with networking off, and collects everything the run
# wrote into outputs/run-NN/. Its records sit in lane-records/run-NN/, which is
# never mounted, and are sealed by a receipt whose digest is appended to
# lane-records/index.jsonl. The gate re-checks the whole chain.

RUNTIME_DIR = REPO_ROOT / "reproduction-system" / "runtime"
RECORDS_DIR = "lane-records"
RUN_INDEX_FILE = "index.jsonl"
LOCK_FILE = "lock"
RUN_ID_RE = re.compile(r"^run-(\d{2,})$")
RECORD_VERSION = "1.0"
LANE_MOUNT = "/lane"
EVENT_PREFIX = "LANE1"
LANE_PROFILE_MARKER = "# reproduction lane profile"
LANE_PROFILE = (f"{LANE_PROFILE_MARKER}\n"
                "# Injected by run-container (gate 1.3): a child R process that reads the\n"
                "# working directory's profile instead of R_PROFILE_USER still loads the hook.\n"
                f'sys.source("{LANE_MOUNT}/hook.R", envir = new.env(parent = baseenv()))\n')
PROJECT_PROFILE = ".Rprofile.project"
# Executor documents: never copied into a run and never loadable (spec §3).
# Everything else in the attempt directory is the input tree.
DOCUMENT_NAMES = frozenset({
    PLAN_FILE, PLAN_VIEW_FILE, APPROVAL_FILE, CODE_MANIFEST_FILE, EXECUTION_FILE,
    GATE_FILE, RULINGS_FILE, AUDIT_FILE, REVIEW_FILE, "log.md", "environment.md",
    "comparisons", "outputs", RECORDS_DIR, SNAPSHOT_DIR, "__pycache__"})
# Interpreters run-container starts the entry with, by suffix.
ENTRY_INTERPRETERS = {".r": "Rscript", ".sh": "bash"}
# Front-end calls that start no interpreter needing the hook: R RHOME,
# R --version, and the R CMD dispatcher. A subcommand that runs R re-enters
# the front end, and that start is counted as its own process: BATCH runs
# "${R_HOME}/bin/R -f ${in}" (bin/BATCH line 60 in rocker/r-ver:4.3.2), so a
# --vanilla there still fails the census. INSTALL's inner start, which pipes
# tools:::.install_packages() into R with init files off (bin/INSTALL line
# 34), needs the PKGBUILD binding planned for the instrumentation stage.
CENSUS_EXEMPT = frozenset({"CMD", "RHOME", "--version"})
HOOK_SKIP_OPTIONS = frozenset({"--vanilla", "--no-init-file"})
# Options that name the code an R process runs; without one, a script fed on
# standard input (R < file) is code no load event covers.
SCRIPT_OPTIONS = ("--file=", "-f", "--file", "-e")
# An explicit, effectively unbounded log size: a rotated stream loses events,
# and Docker refuses max-size=-1 at start. The read-back must match it.
LOG_MAX_SIZE = "100g"


def log_opts() -> dict[str, str]:
    """The json-file log options a run is created with, and must read back.

    One retained file and blocking delivery, as well as the size: Docker's
    non-blocking mode drops new messages when its buffer fills, which is a
    supported configuration and not daemon misbehaviour, so a daemon default
    of ``mode=non-blocking`` would lose events silently (spec §4; Astra's
    specification review, D-2).
    """
    return {"max-size": LOG_MAX_SIZE, "max-file": "1", "mode": "blocking"}


def log_opt_args() -> list[str]:
    """``--log-driver`` and ``--log-opt`` arguments for ``docker run``."""
    args = ["--log-driver", "json-file"]
    for key, value in log_opts().items():
        args += ["--log-opt", f"{key}={value}"]
    return args


def log_config_problem(config: dict | None) -> str | None:
    """Why a container's log configuration cannot carry the event stream.

    The read-back of ``HostConfig.LogConfig`` must show the json-file driver
    with exactly the options of :func:`log_opts`. A differing read-back is a
    problem, and a run with a problem seals ``incomplete``, which no ruling
    clears (spec §4, completeness fact 1).

    Returns:
        The problem text, or ``None`` when the configuration is as required.
    """
    if not config or config.get("Type") != "json-file":
        return (f"the container's log driver is {(config or {}).get('Type')!r}, not "
                f"json-file: the event stream is not retained")
    opts = config.get("Config") or {}
    expected = log_opts()
    wrong = {key: opts.get(key) for key in expected if opts.get(key) != expected[key]}
    if wrong:
        return (f"the container's log options {wrong} differ from {expected}: the event "
                f"stream could be rotated or dropped")
    return None
RECORD_FILES = ("run.json", "pre.json", "baseline.json", "post.json", "events.log",
                "outputs.json", "lane-renviron.txt")


def docker(args: list[str], *, binary: bool = False,
           timeout: float | None = 600) -> subprocess.CompletedProcess:
    """Run a docker CLI command and capture its output.

    Args:
        args: Arguments after ``docker``.
        binary: Capture bytes rather than text (logs, file contents).
        timeout: Seconds before giving up; None waits indefinitely.

    Raises:
        LaneError: when docker is not installed.
    """
    try:
        return subprocess.run(["docker", *args], capture_output=True, text=not binary,
                              timeout=timeout, check=False)
    except FileNotFoundError as exc:
        raise LaneError("docker is not installed or not on PATH") from exc


def inspect_image(tag: str) -> dict:
    """Resolve an image tag to its immutable id, with its working directory.

    The run uses the id, so a tag rebuilt between runs shows up as a new id
    (Astra's design review, point 2).
    """
    proc = docker(["image", "inspect", tag])
    if proc.returncode:
        raise LaneError(f"docker image {tag!r} not found locally: {proc.stderr.strip()}")
    info = json.loads(proc.stdout)[0]
    config = info.get("Config") or {}
    return {"tag": tag, "id": info["Id"], "repo_digests": info.get("RepoDigests") or [],
            "workdir": config.get("WorkingDir") or "", "labels": config.get("Labels") or {}}


LITTLER_MARK = "--littler--"
FRONT_END_PROBE = ('r="$(R RHOME)" || exit 3; printf "%s\\n" "$r"; '
                   'for d in $(printf "%s" "$PATH" | tr ":" " "); do '
                   '[ -f "$d/R" ] && readlink -f "$d/R"; done; '
                   f'printf "%s\\n" "{LITTLER_MARK}"; '
                   'for d in $(printf "%s" "$PATH" | tr ":" " "); do '
                   '[ -f "$d/r" ] && readlink -f "$d/r"; done; exit 0')


def image_front_end(image_id: str) -> dict:
    """Find the image's R front end and every copy of it on the PATH.

    The exec shim is mounted over ``$R_HOME/bin/R`` and over each PATH copy
    with the same bytes (``/usr/local/bin/R`` in the rocker images), so every
    interpreter start passes through it (spec §4, probe fact 3). A PATH ``R``
    with other bytes is reported: starts through it would not be counted.

    littler's ``r`` embeds libR and starts R without the front end, so the
    littler shim is mounted over every littler binary on the PATH (resolved
    through its symlinks), and ``r`` runs ``Rscript`` instead (spec §8).

    Returns:
        ``{r_home, front_end, front_end_bytes, front_end_sha256,
        shim_targets, unshimmed, littler_targets}``.
    """
    probe = docker(["run", "--rm", "--network", "none", "--entrypoint", "sh", image_id,
                    "-c", FRONT_END_PROBE])
    lines = [line.strip() for line in probe.stdout.splitlines() if line.strip()]
    if probe.returncode or not lines:
        raise LaneError(f"could not find R in image {image_id[:19]}: "
                        f"{probe.stderr.strip() or 'R RHOME failed'}")
    r_home, found = lines[0], lines[1:]
    mark = found.index(LITTLER_MARK) if LITTLER_MARK in found else len(found)
    candidates, littler = found[:mark], list(dict.fromkeys(found[mark + 1:]))
    front_end = f"{r_home.rstrip('/')}/bin/R"

    def file_bytes(path: str) -> bytes:
        got = docker(["run", "--rm", "--network", "none", "--entrypoint", "cat", image_id,
                      path], binary=True)
        if got.returncode:
            raise LaneError(f"could not read {path} from image {image_id[:19]}")
        return got.stdout

    original = file_bytes(front_end)
    if not original.startswith(b"#!"):
        raise LaneError(f"{front_end} in image {image_id[:19]} is not a script front end; "
                        f"the exec shim cannot stand in for it")
    targets, unshimmed = [front_end], []
    for path in dict.fromkeys(candidates):
        if path == front_end:
            continue
        (targets if file_bytes(path) == original else unshimmed).append(path)
    return {"r_home": r_home, "front_end": front_end, "front_end_bytes": original,
            "front_end_sha256": hashlib.sha256(original).hexdigest(),
            "shim_targets": targets, "unshimmed": unshimmed, "littler_targets": littler}


@digest_snapshot()
def input_inventory(target_dir: Path) -> tuple[dict[str, str], list[str]]:
    """sha256 of every file in the input tree, and the tree's symlink problems.

    The input tree is the attempt directory less the executor's documents and
    the lane's records (spec §3). It is what a run's work copy is made from,
    and at gate time it must equal the final run's pre snapshot.
    """
    files, problems = walk_tree(target_dir)
    inventory = {}
    for path in files:
        rel = path.relative_to(target_dir)
        if rel.parts[0] not in DOCUMENT_NAMES:
            inventory[rel.as_posix()] = cached_digest(path)
    return inventory, problems


@digest_snapshot()
def work_inventory(root: Path) -> tuple[dict[str, str], list[str]]:
    """sha256 of every file in a work copy, and its symlink problems."""
    files, problems = walk_tree(root)
    return {path.relative_to(root).as_posix(): cached_digest(path) for path in files}, problems


def inventory_difference(expected: dict[str, str], found: dict[str, str]) -> list[str]:
    """Paths added, removed, or changed between two inventories, for messages."""
    added = sorted(set(found) - set(expected))
    removed = sorted(set(expected) - set(found))
    changed = sorted(rel for rel in set(expected) & set(found) if expected[rel] != found[rel])
    return ([f"added {rel}" for rel in added] + [f"removed {rel}" for rel in removed]
            + [f"changed {rel}" for rel in changed])


def run_ids(records: Path) -> list[str]:
    """The run directories under ``lane-records/``, in run order."""
    if not records.is_dir():
        return []
    found = [p.name for p in records.iterdir() if p.is_dir() and RUN_ID_RE.match(p.name)]
    return sorted(found, key=lambda name: int(RUN_ID_RE.match(name).group(1)))


def acquire_lock(records: Path, run_id: str) -> None:
    """Take the attempt's run lock, or refuse (one run at a time; spec §5)."""
    records.mkdir(parents=True, exist_ok=True)
    lock = records / LOCK_FILE
    try:
        handle = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o644)
    except FileExistsError:
        holder = lock.read_text(encoding="utf-8", errors="replace").strip()
        raise LaneError(f"{display_path(lock)} exists: another run holds this attempt "
                        f"({holder}). Finalise that run; if it is gone, the operator clears "
                        f"the lock with run-container --clear-lock") from None
    with os.fdopen(handle, "w", encoding="utf-8") as out:
        out.write(json.dumps({"run": run_id, "pid": os.getpid(), "host": os.uname().nodename,
                              "since": now_utc()}) + "\n")


def release_lock(records: Path, run_id: str) -> None:
    """Release the lock if, and only if, this run holds it."""
    lock = records / LOCK_FILE
    try:
        holder = json.loads(lock.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return
    if holder.get("run") == run_id:
        lock.unlink()


def copy_input_tree(target_dir: Path, project: Path) -> None:
    """Copy the input tree into the work copy, never by hard link.

    ``cp -a --reflink=auto`` shares blocks on filesystems that support it and
    copies otherwise (Fable's design review, Q1). A hard link would make the
    originals writable through the work copy. Where ``cp`` lacks
    ``--reflink`` (BSD), Python copies the files.
    """
    project.mkdir(parents=True)
    for entry in sorted(target_dir.iterdir()):
        if entry.name in DOCUMENT_NAMES:
            continue
        dest = project / entry.name
        proc = subprocess.run(["cp", "-a", "--reflink=auto", str(entry), str(dest)],
                              capture_output=True, text=True, check=False)
        if proc.returncode:
            if entry.is_dir() and not entry.is_symlink():
                shutil.copytree(entry, dest, symlinks=True, dirs_exist_ok=True)
            else:
                shutil.copy2(entry, dest, follow_symlinks=False)


# Cache stores (spec §9): Quarto's _freeze and .quarto, the targets store,
# and knitr's <stem>_cache beside its document (knitr's default cache.path).
# A run starts without them, so that it computes afresh.
STORE_NAMES = frozenset({"_freeze", ".quarto", "_targets"})
KNITR_DOCUMENTS = frozenset({".rmd", ".qmd", ".rnw", ".rmarkdown"})


def cache_stores(root: Path) -> list[str]:
    """The known cache stores in a tree, as relative directory paths."""
    found: list[str] = []
    for dirpath, dirnames, filenames in os.walk(root):
        here = Path(dirpath)
        documents = {Path(f).stem for f in filenames
                     if Path(f).suffix.lower() in KNITR_DOCUMENTS}
        for name in sorted(dirnames):
            if name in STORE_NAMES or (name.endswith("_cache") and name[:-6] in documents):
                found.append((here / name).relative_to(root).as_posix())
                dirnames.remove(name)
    return found


def tree_digest(root: Path) -> tuple[int, str]:
    """The number of files under a directory, and a digest of their sha256s."""
    files = {p.relative_to(root).as_posix(): sha256_file(p)
             for p in sorted(root.rglob("*")) if p.is_file()}
    return len(files), json_digest(files)


def instrument_work_copy(project: Path, keep_stores: list[str] | None = None) -> list[dict]:
    """Make the lane's declared changes to a verified work copy (spec §4).

    A project-root ``.Rprofile`` is renamed ``.Rprofile.project`` (the hook
    sources it in R's place), and the lane's own ``.Rprofile`` is written, so
    a child that reads the working directory's profile still loads the hook.
    Every known cache store is removed, so the run computes afresh, unless
    the executor declared it an input (``keep_stores``), which the gate
    makes an obligation (spec §9).

    Returns:
        The changes, as recorded in ``baseline.json``.

    Raises:
        LaneError: a declared store that is not a known store in the tree.
    """
    changes: list[dict] = []
    stores = cache_stores(project)
    for kept in keep_stores or []:
        if kept.rstrip("/") not in stores:
            raise LaneError(f"--keep-store {kept}: not a known cache store in the input tree "
                            f"(found: {', '.join(stores) or 'none'})")
    kept_set = {k.rstrip("/") for k in keep_stores or []}
    for store in stores:
        count, digest = tree_digest(project / store)
        if store in kept_set:
            changes.append({"change": "kept-store", "path": store, "files": count,
                            "sha256": digest})
        else:
            shutil.rmtree(project / store)
            changes.append({"change": "removed-store", "path": store, "files": count,
                            "sha256": digest})
    profile = project / ".Rprofile"
    if (project / PROJECT_PROFILE).exists():
        raise LaneError(f"the input tree already has a {PROJECT_PROFILE}, the name the lane "
                        f"gives a project profile: rename it")
    if profile.is_symlink() or profile.is_dir():
        raise LaneError(".Rprofile must be a regular file")
    if profile.is_file():
        profile.rename(project / PROJECT_PROFILE)
        changes.append({"change": "renamed", "from": ".Rprofile", "to": PROJECT_PROFILE})
    profile.write_text(LANE_PROFILE, encoding="utf-8")
    changes.append({"change": "injected", "path": ".Rprofile",
                    "sha256": hashlib.sha256(LANE_PROFILE.encode()).hexdigest()})
    return changes


def compose_renviron(project: Path) -> str:
    """The lane's user ``Renviron``: the project's, verbatim, then the pin.

    R reads ``R_ENVIRON_USER`` in place of the project ``.Renviron``, so the
    project's variables are copied in to keep them in the environment phase
    (Astra's design review, point 3). The final line pins ``R_PROFILE_USER``
    to the hook: probe fact 1 showed a project ``.Renviron`` otherwise
    displaces it, and probe fact 2 that children re-read the pin. Just before
    it, ``LANE_PARENT_PROFILE`` saves whatever profile the process inherited,
    so ``callr``'s bootstrap profile still runs after the hook (Fable's
    specification review, Q3). The pin is never conditional, or a project
    line above it would win again.
    """
    parts = []
    project_env = project / ".Renviron"
    if project_env.is_file():
        parts.append("# The project .Renviron, verbatim:")
        parts.append(project_env.read_text(encoding="utf-8", errors="replace").rstrip("\n"))
    parts.append("# Reproduction lane pin (gate 1.3): save any inherited profile (callr's,")
    parts.append("# or one the project names) for the hook to source, then pin the hook.")
    parts.append("LANE_PARENT_PROFILE=${R_PROFILE_USER}")
    parts.append(f"R_PROFILE_USER={LANE_MOUNT}/hook.R")
    return "\n".join(parts) + "\n"


def stage_lane_dir(lane_dir: Path, project: Path, front_end: bytes,
                   nonce: str) -> dict[str, str]:
    """Write the read-only lane directory a run mounts at ``/lane``.

    The run's nonce is staged as a file too: a child whose environment was
    cleared (``env -i``) loses ``LANE_RUN_NONCE``, and its events would
    otherwise be strays the census never sees; the shim and the hook read
    the file then, so such a child is still counted, and fails the census
    if it skipped the hook (spec §13).

    Returns:
        The sha256 of each lane file, for ``run.json``.
    """
    lane_dir.mkdir(parents=True)
    files = {"hook.R": (RUNTIME_DIR / "hook.R").read_bytes(),
             "r-shim.sh": (RUNTIME_DIR / "r-shim.sh").read_bytes(),
             "littler-shim.sh": (RUNTIME_DIR / "littler-shim.sh").read_bytes(),
             "R.orig": front_end,
             "Renviron": compose_renviron(project).encode("utf-8"),
             "nonce": nonce.encode("ascii")}
    for name, data in files.items():
        path = lane_dir / name
        path.write_bytes(data)
        path.chmod(0o755 if name in ("r-shim.sh", "littler-shim.sh", "R.orig") else 0o644)
    return {name: hashlib.sha256(data).hexdigest() for name, data in files.items()}


def container_argv(image_id: str, project: Path, lane_dir: Path, mount: str,
                   shim_targets: list[str], interpreter: str, entry: str,
                   nonce: str, name: str, littler_targets: list[str] = ()) -> list[str]:
    """The ``docker run`` command for one run (spec §§4, 5).

    Networking is off, the run is a non-root user, PID 1 is Docker's init
    (so its stderr is the event stream), and the only writable mount is the
    work copy. The records and ``outputs/`` are never mounted. The log driver
    is set explicitly, with no size limit (a rotated stream loses events, and
    a multi-hour run would end incomplete: Fable's specification review, Q2),
    one retained file, and blocking delivery (:func:`log_opts`). The entry
    point is set explicitly too, so an image's own
    ``ENTRYPOINT`` cannot turn the lane's command into its arguments.
    """
    argv = ["docker", "run", "-d", "--name", name, "--init", "--network", "none",
            *log_opt_args(),
            "--user", f"{os.getuid()}:{os.getgid()}", "-w", mount,
            "--mount", f"type=bind,src={project},dst={mount}",
            "--mount", f"type=bind,src={lane_dir},dst={LANE_MOUNT},readonly"]
    for target in shim_targets:
        argv += ["--mount", f"type=bind,src={lane_dir / 'r-shim.sh'},dst={target},readonly"]
    for target in littler_targets:
        argv += ["--mount",
                 f"type=bind,src={lane_dir / 'littler-shim.sh'},dst={target},readonly"]
    for variable, value in (("R_ENVIRON_USER", f"{LANE_MOUNT}/Renviron"),
                            ("R_PROFILE_USER", f"{LANE_MOUNT}/hook.R"),
                            ("LANE_RUN_NONCE", nonce), ("LANE_PROJECT_ROOT", mount)):
        argv += ["-e", f"{variable}={value}"]
    return argv + ["--entrypoint", interpreter, image_id, entry]


def read_run_index(records: Path) -> tuple[dict[str, dict], list[str]]:
    """The sealed runs listed in ``lane-records/index.jsonl``, and bad lines.

    Returns:
        ``({run_id: {run, receipt_sha256, state}}, problems)``; the first
        entry for a run wins, since the index is append-only.
    """
    indexed: dict[str, dict] = {}
    problems: list[str] = []
    index_path = records / RUN_INDEX_FILE
    lines = index_path.read_text(encoding="utf-8").splitlines() if index_path.is_file() else []
    for number, line in enumerate(lines, 1):
        try:
            entry = json.loads(line)
            indexed.setdefault(entry["run"], entry)
        except (json.JSONDecodeError, KeyError, TypeError):
            problems.append(f"{RECORDS_DIR}/{RUN_INDEX_FILE} line {number} is not a run entry")
    return indexed, problems


def resolve_consumed(target_dir: Path, specs: list[str]) -> list[dict]:
    """Resolve ``--consume run-NN:files/<path>`` against sealed earlier runs.

    A run may use an earlier run's output only when it says so (Astra's
    design review, point 2). The output must be one the earlier run sealed,
    unchanged since; it is copied into the work copy at its original path.

    Raises:
        LaneError: on a malformed declaration, an unsealed or incomplete
            source run, or an output that is missing or changed.
    """
    records = target_dir / RECORDS_DIR
    indexed, _ = read_run_index(records)
    resolved = []
    for spec in specs:
        run_id, sep, rel = spec.partition(":")
        if not sep or not RUN_ID_RE.match(run_id) or not rel.startswith("files/"):
            raise LaneError(f"--consume {spec!r}: write run-NN:files/<path>, a file the run "
                            f"collected")
        if run_id not in indexed or indexed[run_id].get("state") not in ("complete", "failed"):
            raise LaneError(f"--consume {spec!r}: {run_id} is not a sealed complete or failed "
                            f"run")
        listed = json.loads((records / run_id / "outputs.json").read_text(encoding="utf-8"))
        item = next((f for f in listed.get("files") or [] if f.get("path") == rel), None)
        source = target_dir / "outputs" / run_id / rel
        if item is None or not source.is_file():
            raise LaneError(f"--consume {spec!r}: {run_id} did not collect {rel}")
        if sha256_file(source) != item["sha256"]:
            raise LaneError(f"--consume {spec!r}: outputs/{run_id}/{rel} changed after "
                            f"{run_id} collected it")
        resolved.append({"run": run_id, "source": rel, "path": rel.removeprefix("files/"),
                         "sha256": item["sha256"], "file": source})
    return resolved


def start_run(target_dir: Path, image_tag: str, entry: str, *, mount_path: str | None = None,
              launch_commit: str | None = None, work_root: Path | None = None,
              consume: list[str] | None = None,
              keep_stores: list[str] | None = None) -> dict:
    """Prepare and start one run; the container is left running.

    Steps 1–4 of the lifecycle (spec §5): lock, resolve the image, snapshot
    and copy the input tree, verify the copy, instrument it, add any declared
    consumed outputs of earlier runs, take the baseline, and start the
    container. ``finalise_run`` does the rest.

    Returns:
        The run's ``run.json`` record, state ``running``.

    Raises:
        LaneError: on any refusal. Nothing is left behind except when the
            container started: then the run stays ``running`` and holds the
            lock until it is finalised.
    """
    entry_rel = Path(entry)
    if entry_rel.is_absolute() or ".." in entry_rel.parts or not entry_rel.parts:
        raise LaneError("--entry must be a relative path inside the attempt directory")
    if entry_rel.parts[0] in DOCUMENT_NAMES:
        raise LaneError(f"--entry {entry} is in a document directory, which a run never sees")
    interpreter = ENTRY_INTERPRETERS.get(entry_rel.suffix.lower())
    if interpreter is None:
        raise LaneError(f"--entry must be an R script or a shell script "
                        f"({', '.join(ENTRY_INTERPRETERS)})")
    image = inspect_image(image_tag)
    mount = mount_path or image["workdir"]
    if not mount.startswith("/") or mount == "/":
        raise LaneError(f"image {image_tag!r} sets no WORKDIR to mount the work copy at: "
                        f"pass --mount-path (the path the wrappers use, such as /project)")
    front = image_front_end(image["id"])
    records = target_dir / RECORDS_DIR
    existing = run_ids(records)
    run_id = f"run-{(int(RUN_ID_RE.match(existing[-1]).group(1)) + 1) if existing else 1:02d}"
    if (target_dir / "outputs" / run_id).exists():
        raise LaneError(f"outputs/{run_id} already exists: a run starts with an empty output "
                        f"destination, so remove what is there")
    acquire_lock(records, run_id)
    record_dir = records / run_id
    work_dir: Path | None = None
    started = False
    try:
        record_dir.mkdir()
        pre, problems = input_inventory(target_dir)
        if problems:
            raise LaneError("refusing to run: " + "; ".join(problems))
        if entry_rel.as_posix() not in pre:
            raise LaneError(f"--entry {entry} is not a file in the input tree")
        write_json(record_dir / "pre.json", {"record_version": RECORD_VERSION, "run": run_id,
                                             "taken_at": now_utc(), "files": pre})
        work_dir = Path(tempfile.mkdtemp(prefix=f"llmr-{run_id}-", dir=work_root))
        project, lane_dir = work_dir / "project", work_dir / "lane"
        copy_input_tree(target_dir, project)
        copied, _ = work_inventory(project)
        if copied != pre:
            raise LaneError("the work copy does not match the input tree: "
                            + "; ".join(inventory_difference(pre, copied)[:10]))
        changes = instrument_work_copy(project, keep_stores)
        consumed = resolve_consumed(target_dir, consume or [])
        for item in consumed:
            dest = project / item["path"]
            if dest.exists():
                raise LaneError(f"--consume {item['run']}:{item['source']} would overwrite "
                                f"{item['path']} in the input tree")
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(item.pop("file"), dest)
            changes.append({"change": "consumed", **item})
        baseline, _ = work_inventory(project)
        write_json(record_dir / "baseline.json",
                   {"record_version": RECORD_VERSION, "run": run_id, "taken_at": now_utc(),
                    "changes": changes, "files": baseline})
        nonce = secrets.token_hex(8)
        lane_files = stage_lane_dir(lane_dir, project, front["front_end_bytes"], nonce)
        (record_dir / "lane-renviron.txt").write_bytes((lane_dir / "Renviron").read_bytes())
        name = f"llmr-{run_id}-{nonce}"
        argv = container_argv(image["id"], project, lane_dir, mount, front["shim_targets"],
                              interpreter, entry_rel.as_posix(), nonce, name,
                              front["littler_targets"])
        dockerfile = target_dir / "Dockerfile"
        label = image["labels"].get("llmr.dockerfile.sha256")
        doc: dict[str, Any] = {
            "record_version": RECORD_VERSION, "run": run_id, "state": "running",
            "started_at": now_utc(), "ended_at": None, "exit_status": None,
            "image": {"tag": image_tag, "id": image["id"], "repo_digests": image["repo_digests"],
                      "dockerfile_label": label,
                      "dockerfile_sha256": sha256_file(dockerfile) if dockerfile.is_file()
                      else None},
            "front_end": {k: front[k] for k in ("r_home", "front_end", "front_end_sha256",
                                                "shim_targets", "unshimmed",
                                                "littler_targets")},
            "mount_path": mount, "entry": entry_rel.as_posix(), "interpreter": interpreter,
            "nonce": nonce, "argv": argv, "lane_files": lane_files,
            "launch_commit": launch_commit,
            "lane_script_sha256": sha256_file(Path(__file__).resolve()),
            "consumed": consumed, "work_dir": str(work_dir), "container_id": None,
            "problems": []}
        proc = docker(argv[1:])
        if proc.returncode:
            # docker run can create the container and then fail to start it.
            docker(["rm", "-f", name])
            raise LaneError(f"docker run failed: {proc.stderr.strip()}")
        started = True
        doc["container_id"] = proc.stdout.strip()
        log_config = docker(["inspect", "--format", "{{json .HostConfig.LogConfig}}",
                             doc["container_id"]])
        doc["log_config"] = (json.loads(log_config.stdout) if log_config.returncode == 0
                             else None)
        problem = log_config_problem(doc["log_config"])
        if problem:
            doc["problems"].append(problem)
        write_json(record_dir / "run.json", doc)
        return doc
    except BaseException:
        if not started:
            # Nothing ran: leave no record, no lock, and no work copy behind.
            shutil.rmtree(record_dir, ignore_errors=True)
            if work_dir is not None:
                shutil.rmtree(work_dir, ignore_errors=True)
            release_lock(records, run_id)
        raise


def decode_field(field: str) -> str:
    """Decode one hex-encoded event field (UTF-8; undecodable bytes replaced)."""
    try:
        return bytes.fromhex(field).decode("utf-8", errors="replace")
    except ValueError:
        return f"<undecodable {field[:20]}>"


def parse_events(text: str, nonce: str) -> tuple[list[dict], list[str]]:
    """The lane events in a run's stream, and lines that claim to be events
    but do not belong to this run.

    An event line is ``LANE1 <nonce> <token> <pid> <ppid> <seq> <event>``
    followed by tab-separated fields. Lines without the prefix are the
    analysis's own stderr and are skipped. A prefixed line with another nonce
    or a malformed head is reported: it is forged, or comes from another run,
    and is never counted (spec §14).
    """
    events: list[dict] = []
    stray: list[str] = []
    for number, line in enumerate(text.splitlines(), 1):
        if not line.startswith(EVENT_PREFIX + " "):
            continue
        head, *fields = line.split("\t")
        parts = head.split(" ")
        if (len(parts) != 7 or parts[1] != nonce or not parts[2]
                or not all(part.isdigit() for part in parts[3:6])):
            stray.append(f"line {number}: {line[:120]}")
            continue
        events.append({"token": parts[2], "pid": int(parts[3]), "ppid": int(parts[4]),
                       "seq": int(parts[5]), "event": parts[6], "fields": fields,
                       "line": number})
    return events, stray


def run_census(events: list[dict], run_id: str = "") -> dict:
    """The process census for one run (spec §8), from its events alone.

    Events are grouped by the per-process token the shim mints, not by PID,
    which can repeat in a long run (Fable's specification review, D-2). Every
    interpreter start the shim saw (``EXEC``) must pair with the hook's
    ``START`` and ``END``. A forked child announces itself with ``FORK`` and
    needs no ``EXEC`` or ``START``, but it must end with its own ``END``: it
    leaves through ``_exit`` and runs no finaliser, so the hook emits that
    ``END`` from a trace on ``parallel:::mcexit``, which every ``mclapply``
    and ``mcparallel`` child calls before it exits. A forked child with no
    ``END`` is unterminated, and its run is incomplete (spec §4, completeness
    fact 3). A sequence gap or a repeated sequence number means lost or
    inserted lines, so the process is incomplete.

    Args:
        events: The run's parsed events.
        run_id: The run, named in each message and issue subject.

    A ``FORK`` must name a parent process with an earlier event in the
    stream; one that does not is unaccounted, and fails (spec §4). A script
    read from standard input and a restored workspace are recorded on the
    process, and the account of loads makes them obligations where their
    content does not bind (spec §8), since that needs the attempt's files.

    Returns:
        ``{processes, errors, flags, obligations, gaps, abnormal,
        unterminated}``, where ``gaps``, ``abnormal``, and ``unterminated``
        list tokens (incomplete, abnormally ended, and never-ended forked
        processes), ``errors`` holds messages, and ``flags`` and
        ``obligations`` hold ``Issue``s. Each process records its argv,
        working directory, standard input (``stdin``: tty, pipe, file, or
        other; ``script``: the shim's capture of a script read from it, as
        ``{md5, bytes, text}``), and whether R restored a saved workspace.
    """
    lead = f"{run_id}: " if run_id else ""
    by_token: dict[str, list[dict]] = {}
    for event in events:
        by_token.setdefault(event["token"], []).append(event)
    first_line = {token: evs[0]["line"] for token, evs in by_token.items()}
    report: dict[str, Any] = {"processes": [], "errors": [], "flags": [], "obligations": [],
                              "gaps": [], "abnormal": [], "unterminated": []}
    for token, evs in by_token.items():
        execs = [e for e in evs if e["event"] == "EXEC"]
        hooked = [e for e in evs if e["event"] != "EXEC"]
        starts = [e for e in hooked if e["event"] == "START"]
        ends = [e for e in hooked if e["event"] == "END"]
        forked = any(e["event"] == "FORK" for e in hooked)
        exec_argv = [decode_field(f) for f in execs[-1]["fields"][2:]] if execs else []
        start_argv = [decode_field(f) for f in starts[0]["fields"][7:]] if starts else []
        argv = exec_argv or start_argv
        # R CMD INSTALL and the like start no interpreter needing the hook; a
        # CMD that does start R re-enters the front end and is counted there.
        exempt = bool(execs) and all(len(e["fields"]) > 2 and decode_field(e["fields"][2])
                                     in CENSUS_EXEMPT for e in execs)
        pid = evs[0]["pid"]
        stdin, script = None, None
        if execs and execs[-1]["fields"]:
            stdin, _, captured = execs[-1]["fields"][0].partition(":")
            md5, _, rest = captured.partition(":")
            size, _, text = rest.partition(":")
            if md5:
                script = {"md5": md5, "bytes": int(size) if size.isdigit() else None,
                          "text": bytes.fromhex(text).decode("utf-8", errors="replace")
                          if text else None}
        cwd = (decode_field(execs[-1]["fields"][1]) if execs and len(execs[-1]["fields"]) > 1
               else decode_field(starts[0]["fields"][1])
               if starts and len(starts[0]["fields"]) > 1 else None)
        process = {"token": token, "pid": pid, "ppid": evs[0]["ppid"], "argv": argv,
                   "cwd": cwd, "stdin": stdin, "script": script,
                   "exec": bool(execs), "start": bool(starts), "end": bool(ends),
                   "fork": forked, "exempt": exempt,
                   "restore": bool(starts) and len(starts[0]["fields"]) > 6
                   and starts[0]["fields"][6] == "restore"}
        report["processes"].append(process)
        shown = f"{pid} ({' '.join(argv)[:160] or 'no arguments'})"
        seqs = sorted(e["seq"] for e in hooked)
        if seqs != list(range(1, len(seqs) + 1)) or len(execs) > 1:
            report["gaps"].append(token)
        if execs and not starts and not exempt:
            skipped = sorted(HOOK_SKIP_OPTIONS & set(argv))
            if skipped:
                report["errors"].append(f"{lead}R process {shown} skipped the lane hook with "
                                        f"{skipped[0]}: the gate cannot see what it loaded")
            else:
                report["errors"].append(f"{lead}R process {shown} never loaded the lane hook, "
                                        f"so the gate cannot see what it loaded: start R "
                                        f"through Rscript, R, or a supported tool (callr, "
                                        f"future, parallel, targets, knitr, rmarkdown, "
                                        f"Quarto), without clearing its environment")
        if starts and not execs:
            # Identified by what it ran, not by its token, so that a re-run
            # that changes nothing keeps its ruling (spec §6).
            started = " ".join(argv)
            report["flags"].append(Issue.flag(
                "process-outside-front-end", started[:120] or "no arguments",
                f"{lead}R process {shown} started outside the R front end (no EXEC from the "
                f"shim)", files={"argv": json_digest(argv)}))
        for fork in (e for e in hooked if e["event"] == "FORK"):
            parent = fork["fields"][0] if fork["fields"] else ""
            if first_line.get(parent, fork["line"]) >= fork["line"]:
                report["errors"].append(f"{lead}forked process {pid} names parent {parent!r}, "
                                        f"which has no earlier event in the stream: it is "
                                        f"unaccounted")
        if starts and not ends and not forked and token not in report["gaps"]:
            report["abnormal"].append(token)
        if forked and not ends and token not in report["gaps"]:
            report["unterminated"].append(token)
    return report


def collect_outputs(project: Path, baseline: dict[str, str], post: dict[str, str],
                    dest: Path) -> dict:
    """Copy everything the run wrote into ``outputs/run-NN/files/`` and class it.

    Collected files keep their work-copy paths under ``files/``, so they
    cannot collide with the console output at ``outputs/run-NN/stdout.log``.

    A new or changed file that is not code is an output. New code is
    ``generated`` (flagged, never loadable). A pre-existing code file the run
    changed is ``changed-code``, which fails the gate (spec §3).
    """
    files = []
    for rel, digest in sorted(post.items()):
        before = baseline.get(rel)
        if before == digest:
            continue
        code = is_code_file(Path(rel))
        kind = ("changed-code" if code and before is not None
                else "generated" if code else "output")
        target = dest / "files" / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(project / rel, target)
        files.append({"path": f"files/{rel}", "sha256": digest, "class": kind,
                      "replaced_input": before is not None})
    return {"files": files, "deleted": sorted(set(baseline) - set(post))}


def seal_run(records: Path, run_id: str, state: str) -> str:
    """Write the run's receipt and append its digest to the index.

    Returns:
        The receipt's sha256.
    """
    record_dir = records / run_id
    files = {name: sha256_file(record_dir / name) for name in RECORD_FILES
             if (record_dir / name).is_file()}
    write_json(record_dir / "receipt.json",
               {"record_version": RECORD_VERSION, "run": run_id, "state": state,
                "sealed_at": now_utc(), "files": files})
    digest = sha256_file(record_dir / "receipt.json")
    with (records / RUN_INDEX_FILE).open("a", encoding="utf-8") as index:
        index.write(json.dumps({"run": run_id, "receipt_sha256": digest, "state": state}) + "\n")
    return digest


def finalise_run(target_dir: Path, run_id: str, keep_work: bool = False) -> dict:
    """Wait for a run's container, collect and class its results, and seal it.

    Steps 5–7 of the lifecycle (spec §5). A detached run is finished by
    calling this later (``run-container --finalise``).

    Returns:
        The sealed ``run.json`` record.
    """
    records = target_dir / RECORDS_DIR
    record_dir = records / run_id
    try:
        doc = json.loads((record_dir / "run.json").read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise LaneError(f"no readable run record for {run_id}: {exc}") from exc
    if doc.get("state") != "running":
        raise LaneError(f"{run_id} is already sealed (state {doc.get('state')})")
    problems: list[str] = list(doc.get("problems") or [])
    cid = doc["container_id"]
    waited = docker(["wait", cid], timeout=None)
    status_text = waited.stdout.strip()
    exit_status = int(status_text) if waited.returncode == 0 and status_text.lstrip(
        "-").isdigit() else None
    if exit_status is None:
        problems.append(f"docker wait failed: {waited.stderr.strip()}")
    logs = docker(["logs", cid], binary=True, timeout=None)
    if logs.returncode:
        problems.append("the container's log stream could not be collected")
    (record_dir / "events.log").write_bytes(logs.stderr or b"")
    docker(["rm", cid])

    work_dir = Path(doc["work_dir"])
    project = work_dir / "project"
    if not project.is_dir():
        problems.append("the work copy is gone, so the run's results cannot be collected")
    else:
        baseline = json.loads((record_dir / "baseline.json").read_text(encoding="utf-8"))
        post, symlinks = work_inventory(project)
        problems.extend(f"work copy: {p}" for p in symlinks)
        write_json(record_dir / "post.json", {"record_version": RECORD_VERSION, "run": run_id,
                                              "taken_at": now_utc(), "files": post})
        collected = collect_outputs(project, baseline["files"], post,
                                    target_dir / "outputs" / run_id)
        # The console output is an output like any other, so a target read
        # from printed results can cite it by path, sha256, and line range
        # (Fable's specification review, Q1).
        console = target_dir / "outputs" / run_id / "stdout.log"
        console.parent.mkdir(parents=True, exist_ok=True)
        console.write_bytes(logs.stdout or b"")
        collected["files"].append({"path": "stdout.log", "sha256": sha256_file(console),
                                   "class": "console", "replaced_input": False})
        write_json(record_dir / "outputs.json",
                   {"record_version": RECORD_VERSION, "run": run_id, **collected})

    events, stray = parse_events((record_dir / "events.log").read_text(
        encoding="utf-8", errors="replace"), doc["nonce"])
    census = run_census(events)
    state = run_state(problems, exit_status, census)
    doc.update(state=state, exit_status=exit_status, ended_at=now_utc(), problems=problems,
               census={"processes": len(census["processes"]), "errors": len(census["errors"]),
                       "gaps": census["gaps"], "abnormal": census["abnormal"],
                       "unterminated": census["unterminated"],
                       "stray_event_lines": len(stray)})
    write_json(record_dir / "run.json", doc)
    seal_run(records, run_id, state)
    release_lock(records, run_id)
    if not keep_work:
        shutil.rmtree(work_dir, ignore_errors=True)
    return doc


def run_state(problems: list[str], exit_status: int | None, census: dict) -> str:
    """The sealed state of a run (spec §5 step 7, under §4's completeness facts).

    ``incomplete`` whenever a completeness fact is in doubt: a recorded
    problem (a differing log read-back, a failed ``docker wait`` or
    ``docker logs``, a lost work copy), a process with a sequence gap, or a
    forked child with no ``END``. Only with those facts whole does a missing
    ``END`` mean an abnormal end, and the run ``failed``; missing terminal
    evidence never defaults to ``failed`` (Astra's specification review,
    D-2). ``complete`` needs exit 0 and every process ended.
    """
    if problems or exit_status is None or census["gaps"] or census["unterminated"]:
        return "incomplete"
    if exit_status != 0 or census["abnormal"]:
        return "failed"
    return "complete"


def clear_lock(target_dir: Path) -> str:
    """Operator-only: remove a stale lock once its container is gone.

    The run it names stays unsealed, so the gate treats it as incomplete.
    """
    records = target_dir / RECORDS_DIR
    lock = records / LOCK_FILE
    if not lock.exists():
        raise LaneError("no lock to clear")
    holder = json.loads(lock.read_text(encoding="utf-8"))
    run_doc = records / str(holder.get("run")) / "run.json"
    cid = None
    if run_doc.is_file():
        cid = json.loads(run_doc.read_text(encoding="utf-8")).get("container_id")
    if cid:
        state = docker(["inspect", "--format", "{{.State.Running}}", cid])
        if state.returncode == 0 and state.stdout.strip() == "true":
            raise LaneError(f"container {cid[:12]} for {holder.get('run')} is still running: "
                            f"finalise the run instead")
    lock.unlink()
    return str(holder.get("run"))


def lane_script_at(repo_root: Path, commit: str,
                   rel: str = "scripts/reproduction-lane.py") -> str | None:
    """sha256 of a lane file (default: the lane script) as committed at ``commit``."""
    env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
    proc = subprocess.run(["git", "-C", str(repo_root), "show", f"{commit}:{rel}"],
                          capture_output=True, check=False, env=env)
    return hashlib.sha256(proc.stdout).hexdigest() if proc.returncode == 0 else None


# The lane files a run stages from the repository, which the launcher binding
# checks at the launch commit as it checks the lane script: the hook and the
# shim produce the events the gate reads, so a stale copy of either is a
# stale lane (spec §4, launcher binding).
BOUND_RUNTIME_FILES = {"hook.R": "reproduction-system/runtime/hook.R",
                       "r-shim.sh": "reproduction-system/runtime/r-shim.sh",
                       "littler-shim.sh": "reproduction-system/runtime/littler-shim.sh"}


@digest_snapshot()
def check_run_records(target_dir: Path, launch_commit: str | None,
                      repo_root: Path = REPO_ROOT) -> dict | None:
    """Verify an attempt's sealed run records (spec §§4, 5, 8).

    Checks the receipt chain, the launcher binding, each run's collected
    outputs, the final run's process census, and that the input tree is
    unchanged since the final run started.

    Returns:
        None when the attempt has no ``lane-records/`` (it was run before
        gate 1.3). Otherwise ``{runs, final_run, final_pre, errors, flags,
        obligations, warnings, generated, collected}``, where ``generated``
        and ``collected`` are attempt-relative paths under ``outputs/``.
    """
    records = target_dir / RECORDS_DIR
    if not records.is_dir():
        return None
    report: dict[str, Any] = {"runs": {}, "final_run": None, "final_pre": None,
                              "credited_runs": [], "outputs": {}, "errors": [], "flags": [],
                              "obligations": [], "warnings": [], "generated": [],
                              "collected": [], "credited_records": {}}
    errors, flags = report["errors"], report["flags"]
    indexed, index_problems = read_run_index(records)
    errors.extend(index_problems)
    present = run_ids(records)
    for run_id in sorted(set(indexed) - set(present)):
        errors.append(f"{run_id} is in the run index but its records are gone")
    if (records / LOCK_FILE).exists():
        report["warnings"].append("a run still holds the attempt lock")

    sealed: dict[str, dict] = {}
    for run_id in present:
        record_dir = records / run_id
        if run_id not in indexed:
            report["runs"][run_id] = {"state": "incomplete", "sealed": False}
            report["warnings"].append(f"{run_id} was never finalised, so it is incomplete")
            continue
        broken = []
        receipt_path = record_dir / "receipt.json"
        if not receipt_path.is_file() or sha256_file(receipt_path) != \
                indexed[run_id]["receipt_sha256"]:
            broken.append("its receipt does not match the index")
        else:
            receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
            for name, digest in (receipt.get("files") or {}).items():
                if not (record_dir / name).is_file() or sha256_file(record_dir / name) != digest:
                    broken.append(f"{name} does not match its receipt")
            for name in ("run.json", "pre.json", "events.log"):
                if name not in (receipt.get("files") or {}):
                    broken.append(f"the receipt does not seal {name}")
        if broken:
            errors.append(f"{run_id}: broken receipt chain ({'; '.join(broken)})")
            report["runs"][run_id] = {"state": "broken", "sealed": True}
            continue
        doc = json.loads((record_dir / "run.json").read_text(encoding="utf-8"))
        sealed[run_id] = doc
        report["runs"][run_id] = {"state": doc.get("state"), "sealed": True,
                                  "image_id": (doc.get("image") or {}).get("id"),
                                  "exit_status": doc.get("exit_status")}
        # Launcher binding (Astra's design review, point 10).
        receipt = {"receipt.json": indexed[run_id]["receipt_sha256"]}
        if launch_commit is None:
            flags.append(Issue.flag("run-launch-unbound", run_id, f"{run_id} is not bound to a "
                                    f"launch commit, so the lane that ran it is unverified",
                                    files=receipt))
        elif doc.get("launch_commit") != launch_commit:
            errors.append(f"{run_id} records launch commit {doc.get('launch_commit')!r}, not "
                          f"the run's {launch_commit[:12]}")
        elif lane_script_at(repo_root, launch_commit) != doc.get("lane_script_sha256"):
            errors.append(f"{run_id} was run by a lane script other than the one at the "
                          f"launch commit {launch_commit[:12]}")
        else:
            staged = doc.get("lane_files") or {}
            for name, rel in BOUND_RUNTIME_FILES.items():
                if name not in staged:
                    errors.append(f"{run_id} records no digest for the lane's {name}")
                elif lane_script_at(repo_root, launch_commit, rel) != staged[name]:
                    errors.append(f"{run_id} ran a {name} other than the one at the launch "
                                  f"commit {launch_commit[:12]}")
        # Collected outputs must be exactly what the run recorded (Fable A14).
        outputs_doc = record_dir / "outputs.json"
        recorded = ({f["path"]: f for f in json.loads(outputs_doc.read_text(
            encoding="utf-8")).get("files", [])} if outputs_doc.is_file() else {})
        out_root = target_dir / "outputs" / run_id
        on_disk, _ = work_inventory(out_root) if out_root.is_dir() else ({}, [])
        report["outputs"][run_id] = {rel: item["sha256"] for rel, item in recorded.items()}
        for rel in sorted(set(on_disk) - set(recorded)):
            errors.append(f"outputs/{run_id}/{rel} was not written by {run_id}")
        for rel, item in sorted(recorded.items()):
            shown = f"outputs/{run_id}/{rel}"
            if rel not in on_disk:
                errors.append(f"{shown}, written by {run_id}, is missing")
            elif on_disk[rel] != item["sha256"]:
                errors.append(f"{shown} changed after {run_id} wrote it")
            report["collected"].append(shown)
            if item["class"] == "generated":
                report["generated"].append(shown)
            elif item["class"] == "changed-code":
                errors.append(f"{run_id} changed pre-existing code "
                              f"{rel.removeprefix('files/')} during the run")
        problems = doc.get("problems") or []
        if problems:
            report["warnings"].append(f"{run_id}: {'; '.join(problems)}")

    credible = [r for r in present if r in sealed
                and sealed[r].get("state") in ("complete", "failed")]
    if not credible:
        errors.append("no run reached complete or failed: there is nothing to credit")
        return report
    final = credible[-1]
    report["final_run"] = final
    for later in present[present.index(final) + 1:]:
        report["warnings"].append(f"{later}, after the final run {final}, is "
                                  f"{report['runs'][later]['state']}")
    doc = sealed[final]
    pre = json.loads((records / final / "pre.json").read_text(encoding="utf-8"))["files"]
    report["final_pre"] = pre
    current, symlinks = input_inventory(target_dir)
    errors.extend(symlinks)
    for change in inventory_difference(pre, current):
        errors.append(f"input tree {change} after the final run {final} started: re-run")

    # Credit rests on the final run and every run whose outputs it consumed,
    # transitively; each must be sealed, and each is held to the same census
    # (spec §5).
    credited, queue = [final], [final]
    while queue:
        for item in (sealed.get(queue.pop()) or {}).get("consumed") or []:
            source = item.get("run")
            if source not in credited:
                credited.append(source)
                queue.append(source)
            recorded_digest = report["outputs"].get(source, {}).get(item.get("source"))
            if recorded_digest != item.get("sha256"):
                errors.append(f"a run consumed {source}'s {item.get('source')} at a digest "
                              f"{source} did not seal")
    report["credited_runs"] = credited
    final_code = {k: v for k, v in pre.items() if is_code_file(Path(k))}
    for run_id in credited:
        run_doc = sealed.get(run_id)
        if run_doc is None or run_doc.get("state") not in ("complete", "failed"):
            errors.append(f"credit rests on {run_id}, which is "
                          f"{report['runs'].get(run_id, {}).get('state', 'missing')}: an "
                          f"incomplete run cannot be ruled")
            continue
        events_log = records / run_id / "events.log"
        events, stray = parse_events(events_log.read_text(encoding="utf-8", errors="replace"),
                                     run_doc.get("nonce", ""))
        evidence = {f"{run_id}/events.log": sha256_file(events_log)}
        # The sealed records the gate's account of loads reads (spec §8): the
        # events, the run record, the baseline the run started from, and what
        # the run wrote.
        census = run_census(events, run_id)
        baseline_path = records / run_id / "baseline.json"
        outputs_path = records / run_id / "outputs.json"
        report["credited_records"][run_id] = {
            "doc": run_doc, "events": events, "census": census,
            "baseline": json.loads(baseline_path.read_text(encoding="utf-8"))
            if baseline_path.is_file() else {},
            "outputs": json.loads(outputs_path.read_text(encoding="utf-8")).get("files") or []
            if outputs_path.is_file() else []}
        errors.extend(census["errors"])
        flags.extend(census["flags"])
        report["obligations"].extend(census["obligations"])
        if stray:
            flags.append(Issue.flag("stray-events", run_id, f"{run_id}'s stream holds "
                                    f"{len(stray)} event line(s) from no process of this run "
                                    f"(forged, or another run's)", files=evidence))
        if not census["processes"]:
            errors.append(f"{run_id} recorded no R process: the run's code was not seen")
        if run_doc.get("state") == "failed":
            flags.append(Issue.flag(
                "run-failed", run_id, f"{run_id} failed (exit status "
                f"{run_doc.get('exit_status')}"
                + (f"; abnormal end of {len(census['abnormal'])} process(es)"
                   if census["abnormal"] else "")
                + "): its partial results need a ruling",
                files={"receipt.json": indexed[run_id]["receipt_sha256"]}))
        if run_id != final:
            run_pre = json.loads((records / run_id / "pre.json").read_text(
                encoding="utf-8"))["files"]
            run_code = {k: v for k, v in run_pre.items() if is_code_file(Path(k))}
            if run_code != final_code:
                differences = "; ".join(inventory_difference(final_code, run_code)[:5])
                flags.append(Issue.flag(
                    "consumed-other-code", f"{final}<-{run_id}", f"{final} consumed outputs "
                    f"of {run_id}, which ran other code ({differences})",
                    files={f"{run_id}/pre.json": json_digest(run_code),
                           f"{final}/pre.json": json_digest(final_code)}))
    # Fresh computation (spec §9): a store a credited run kept as input is a
    # dependency whose admissibility is unresolved, and any other directory
    # in the input tree named like a cache is an obligation too.
    stores: set[str] = set()
    for run_id, record in report["credited_records"].items():
        for change in (record["baseline"] or {}).get("changes") or []:
            if change.get("change") not in ("kept-store", "removed-store"):
                continue
            stores.add(str(change.get("path")))
            if change["change"] == "kept-store" and not any(
                    getattr(o, "issue_id", "") == f"cache-store-input:{change['path']}"
                    for o in report["obligations"]):
                report["obligations"].append(Issue.obligation(
                    "cache-store-input", str(change["path"]), f"{run_id} kept the cache store "
                    f"{change['path']} as an input rather than computing afresh: confirm its "
                    f"cached results may stand", files={str(change["path"]): str(
                        change.get("sha256"))}))
    directories: dict[str, dict[str, str]] = {}
    for rel, digest in pre.items():
        parts = rel.split("/")[:-1]
        for depth in range(1, len(parts) + 1):
            directories.setdefault("/".join(parts[:depth]), {})[rel] = digest
    raised: list[str] = []
    for directory, files in sorted(directories.items()):
        inside_another = any(directory.startswith(d + "/") for d in [*stores, *raised])
        if ("cache" in directory.rsplit("/", 1)[-1].lower() and directory not in stores
                and not inside_another):
            raised.append(directory)
            report["obligations"].append(Issue.obligation(
                "cache-directory", directory, f"{directory} in the input tree looks like a "
                f"cache, but is no store the lane knows to remove: confirm the run did not "
                f"reuse results from it", files={directory: json_digest(files)}))
    image = doc.get("image") or {}
    if image.get("dockerfile_sha256") and image.get("dockerfile_label") != \
            image.get("dockerfile_sha256"):
        flags.append(Issue.flag(
            "image-stale", final, f"{final} ran image {str(image.get('id'))[:19]}, whose "
            f"llmr.dockerfile.sha256 label does not match the attempt's Dockerfile: stale, or "
            f"built from another file",
            files={"image": str(image.get("id")), "Dockerfile": str(image.get(
                "dockerfile_sha256"))}))
    if (doc.get("front_end") or {}).get("unshimmed"):
        report["warnings"].append(f"{final}: R on the PATH at "
                                  f"{doc['front_end']['unshimmed']} is not the front end, so "
                                  f"starts through it were not counted")
    return report


# ---------------------------------------------------------------------------
# The gate's account of what each credited run loaded (gate 1.3, spec §8)
# ---------------------------------------------------------------------------
#
# Every LOAD, TEXT, CONN, PKG, and HOOKERR event of a credited run is bound on
# its own. An observation is bound to its run, its process, its resolved path,
# and the content that path held when the run started, not to a digest found
# anywhere in the manifest (Astra's design review, Q3). Nesting confers
# nothing: a load inside a tool call is accounted for only where the lane can
# map it to its source (Astra's specification review, D-3).

# The packages that ship with R. They carry no Repository field, so they are
# exempt from the local-package flag by name.
BASE_PACKAGES = frozenset({"base", "compiler", "datasets", "graphics", "grDevices", "grid",
                           "methods", "parallel", "splines", "stats", "stats4", "tcltk",
                           "tools", "utils"})
# The hook's names for traced tool loaders. A load nested in one of their
# calls may be tool-internal (spec §3, class 5), but only where it maps.
TOOL_LOADERS = frozenset({"knitr::knit", "rmarkdown::render", "Rcpp::sourceCpp",
                          "pkgload::load_all", "reticulate::source_python",
                          "reticulate::py_run_file", "box::use", "modules::import"})
# The lane's list of tool expressions: code a common tool evaluates from a
# string, by its exact text. Each entry was seen in a probe.
TOOL_EXPRESSIONS: dict[str, str] = {
    # parallel::makePSOCKcluster's worker start-up -e (2026-10-08 probe, R 4.3.2).
    "tryCatch(parallel:::.workRSOCK,error=function(e)parallel:::.slaveRSOCK)()":
        "a PSOCK worker's start-up expression (parallel, R 4.3.2)",
}
# rmarkdown 2.25 evaluates an output format's name, from render()'s call or
# the document's YAML, as code (create_output_format_function:
# eval(xfun::parse_only(name))). A name only looks up a function, so its own
# formats are listed, bare and qualified (2026-10-08 probe). Another
# package's format name stays an obligation.
RMARKDOWN_FORMATS = ("beamer_presentation", "context_document", "github_document",
                     "html_document", "html_fragment", "html_notebook", "html_vignette",
                     "ioslides_presentation", "latex_document", "latex_fragment",
                     "md_document", "odt_document", "pdf_document",
                     "powerpoint_presentation", "rtf_document", "slidy_presentation",
                     "word_document")
for _format in RMARKDOWN_FORMATS:
    for _name in (_format, f"rmarkdown::{_format}"):
        TOOL_EXPRESSIONS[_name] = "an rmarkdown output format's name (rmarkdown 2.25)"
# The lane's list of tool-generated bootstrap files (spec §3, class 5), as
# (within, loader, path pattern, description): a load by that loader whose
# resolved path matches the pattern is tool-internal. ``within`` names the
# traced tool call it must be nested in; None means a process's own
# start-up load (the hook's "profile" and "file"), at depth 0. The launcher
# matrix (spec §13) supplies the entries.
TOOL_BOOTSTRAP: tuple[tuple[str | None, str, re.Pattern[str], str], ...] = (
    # callr 3.7.5 starts a child as R -f <callr-scr-...> with R_PROFILE_USER
    # set to its bootstrap profile <callr-upr-...>, which the hook sources
    # as the inherited profile (2026-10-08 probe; callr's make_profiles).
    (None, "profile", re.compile(r"/tmp/Rtmp[A-Za-z0-9]+/callr-upr-[0-9a-f]+"),
     "callr's bootstrap profile"),
    (None, "file", re.compile(r"/tmp/Rtmp[A-Za-z0-9]+/callr-scr-[0-9a-f]+"),
     "callr's child script"),
)
# Tool launchers in the image, by md5 (wherever the tool is installed):
# image code accepted without a flag (spec §3). The launcher matrix
# supplies the entries.
IMAGE_LAUNCHERS: dict[str, str] = {
    # Quarto 1.10.19's knitr engine: Quarto starts Rscript on rmd.R, which
    # sources the others (2026-10-08 probe, /opt/quarto/share/rmd/).
    "fbcea28a6701025defaf608d82284066": "Quarto 1.10.19's knitr engine (rmd.R)",
    "6b21cd6051e0e5116c7e4b0ecb3466ed": "Quarto 1.10.19's knitr engine (patch.R)",
    "8916068bceda06893ffbd8b2c54c4fa0": "Quarto 1.10.19's knitr engine (execute.R)",
    "6b42303a1f03288a5a5afdfe505db302": "Quarto 1.10.19's knitr engine (hooks.R)",
    "841e8d9a1820518b60900801fcf84556": "Quarto 1.10.19's knitr engine (ojs.R)",
    "b2f68e6b00c7a2dafc140248d428c484": "Quarto 1.10.19's knitr engine (ojs_static.R)",
}
# Quarto's knitr engine renders <stem>.rmarkdown, which it writes beside the
# document <stem>.qmd and removes afterwards (Quarto 1.10.19: the document,
# preprocessed; for a plain document, with a blank line appended).
QUARTO_INTERMEDIATE = ".rmarkdown"
# Code loaded from a temporary directory was written during the run, by the
# run or by a tool, so it is not image code.
TRANSIENT_ROOTS = ("/tmp/", "/var/tmp/", "/dev/shm/")
# R's package tools, as scripts on standard input, which the exec shim
# captures (spec §8, PKGBUILD). bin/INSTALL and bin/build pipe a fixed
# expression into R, which reads the package paths from its --args; the
# installer then runs helpers through tools:::R_runR. The helpers' only
# variable parts are quoted string literals, which these patterns admit
# without quotes, backslashes, or newlines, so no code rides in them. All
# were read from a probe (2026-10-08, R 4.3.2); any other script is an
# obligation, never a pass.
PACKAGE_INSTALL_SCRIPT = "tools:::.install_packages()\n"
PACKAGE_BUILD_SCRIPT = "tools:::.build_packages()\n"
_SQ = r"'[^'\\\n]*'"
_DQ = r'"[^"\\\n]*"'
_TF = r"(?:TRUE|FALSE)"
INSTALLER_SCRIPTS = tuple(re.compile(pattern) for pattern in (
    # Lazy-load preparation, with the byte compiler's set-up when compiling.
    (r"(?:Sys\.setenv\(R_ENABLE_JIT = 0L\)\ninvisible\(compiler::enableJIT\(0\)\)\n"
     r"invisible\(compiler::compilePKGS\([01]L\)\)\n"
     rf"compiler::setCompilerOptions\(suppressAll = {_TF}\)\n"
     rf"compiler::setCompilerOptions\(suppressUndefined = {_TF}\)\n"
     rf"compiler::setCompilerOptions\(suppressNoSuperAssignVar = {_TF}\);\n)?"
     rf"setwd\({_SQ}\)\nif \(isNamespaceLoaded\({_DQ}\)\) unloadNamespace\({_DQ}\)\n"
     r"suppressPackageStartupMessages\(\.getRequiredPackages\(quietly = TRUE\)\)\n"
     rf"tools:::makeLazyLoading\({_DQ}, {_SQ}, keep\.source = {_TF}, "
     rf"keep\.parse\.data = {_TF}, set\.install\.dir = {_SQ}\)\n"),
    # The help indices.
    rf'tools:::\.install_package_indices\("\.",\n{_SQ}\n\)\n',
    # The load test from the staging library.
    rf"tools:::\.test_load_package\({_SQ}, {_SQ}\)\n",
    # The load test from the final library, saving the namespace's contents.
    (rf"tools:::\.test_load_package\({_SQ}, {_SQ}\)\nf <- base::file\({_SQ}, \"wb\"\)\n"
     r"base::invisible\(base::suppressWarnings\(base::serialize\(base::as\.list\("
     rf"base::getNamespace\({_DQ}\), all\.names=TRUE\), f\)\)\)\nbase::close\(f\)\n"),
))
# Callers the hook verified as R's own NAMESPACE parser, which reads a
# package's NAMESPACE file through a text connection (2026-10-08 probe).
NAMESPACE_READERS = frozenset({"base::parseNamespaceFile"})
# Tool expressions with variable parts, matched against a text the gate
# holds verbatim: an -e argument in a run's EXEC, which the shim records
# raw (a TEXT whose md5 is that argument's is that text). As with the
# installer's scripts, the only holes are string literals. parallelly 1.37
# starts a future multisession worker with these (2026-10-08 probe).
TEXT_TEMPLATES = tuple(re.compile(pattern) for pattern in (
    rf"try\(suppressWarnings\(cat\(Sys\.getpid\(\),file={_DQ}\)\), silent = TRUE\)",
    rf"file\.exists\({_DQ}\)",
    r'options\(socketOptions = "no-delay"\)',
    rf"\.libPaths\(c\({_DQ}(?:,{_DQ})*\)\)",
    (r"workRSOCK <- tryCatch\(parallel:::\.workRSOCK, "
     r"error=function\(e\) parallel:::\.slaveRSOCK\); workRSOCK\(\)"),
))
# An R name as a template hole. A syntactic name only looks a value up, so a
# text whose holes are names adds no logic of its own: it reads or calls what
# other code defined, and that code reached the gate by its own route.
_NAME = r"(?:[A-Za-z]|\.(?![0-9]))[A-Za-z0-9._]*"
# Package-internal texts, matched against the text a TEXT event carries
# verbatim (hook 1.5) and the caller it names. Each pattern is safe alone, as
# above; the callers narrow it to the route a probe saw. A caller without
# "::" is a bare name the hook could not verify as a namespace's own. All
# were seen in the herskind pilot dry run (2026-10-09; ggplot2 3.5.0, rlang,
# glue, and cli in the attempt-02 image).
PACKAGE_TEXTS: tuple[tuple[frozenset[str], re.Pattern[str], str], ...] = (
    (frozenset({"rlang::chr_parse"}), re.compile(r"scale_[a-z]+_[a-z]+\(\)"),
     "ggplot2 parsing a scale's name (rlang::parse_expr)"),
    (frozenset({"rlang::chr_parse"}), re.compile(rf"theme\({_NAME}\)"),
     "ggplot2 parsing a theme element's name (rlang::parse_expr)"),
    (frozenset({".transformer"}), re.compile(rf" ?{_NAME} ?"),
     "a glue placeholder that is one name, in an rlang or cli message template"),
)
# Callers the hook names without a function: how each reads in a message.
CALLER_ROUTES = {"top level": "at the top level", "promise": "with no calling function "
                 "(a promise, as in a dplyr data mask)", "command line": "on the command line",
                 "unknown": "from an unknown caller"}
PACKAGE_ARCHIVE_RE = re.compile(r"([A-Za-z][A-Za-z0-9.]*)_([0-9][0-9.-]*)\.tar\.gz")
# R's code-file suffixes in a package's R/ directory (tools'
# list_files_with_type("code")).
R_CODE_SUFFIXES = frozenset({".R", ".r", ".S", ".s", ".q"})


def install_targets(argv: list[str]) -> list[str]:
    """The package paths an ``R CMD INSTALL`` inner start installs.

    bin/INSTALL passes its own arguments to R after ``--args``, each prefixed
    ``nextArg`` (``nextArg--library=libnextArgmypkg``). Options are skipped,
    and so is ``-l``'s separate value.
    """
    if "--args" not in argv:
        return []
    tokens = [t for t in "".join(argv[argv.index("--args") + 1:]).split("nextArg") if t]
    paths: list[str] = []
    skip = False
    for token in tokens:
        if skip:
            skip = False
        elif token == "-l":
            skip = True
        elif not token.startswith("-"):
            paths.append(token)
    return paths
# R Markdown and Quarto chunk fences and inline code: knitr 1.45's own
# patterns (knitr::all_patterns$md), read in the launcher-matrix image.
CHUNK_START_RE = re.compile(r"^[\t >]*```+\s*\{([a-zA-Z0-9_]+)(.*)\}\s*$")
CHUNK_END_RE = re.compile(r"^[\t >]*```+\s*$")
INLINE_CODE_RE = re.compile(r"(?<!^``)(?<!\n``)`r[ #]([^`]+)\s*`")
DOCUMENT_SUFFIXES = (".rmd", ".qmd")


def text_fields(fields: list[str]) -> tuple[bytes | None, str | None]:
    """A TEXT event's verbatim bytes and caller (hook 1.5).

    Args:
        fields: The event's fields: md5, bytes, depth, enclosing seq, the
            text as hex (``empty``, or ``none`` when it was too long), and the
            caller as hex.

    Returns:
        ``(bytes, caller)``, either None when the event does not carry it (an
        older hook, or a text over the hook's verbatim limit).

    Raises:
        ValueError: if the verbatim field is not hex.
    """
    if len(fields) < 6:
        return None, None
    held = fields[4]
    raw = b"" if held == "empty" else None if held == "none" else bytes.fromhex(held)
    return raw, decode_field(fields[5])


def caller_phrase(caller: str) -> str:
    """How a TEXT event's caller reads in a message."""
    if caller in CALLER_ROUTES:
        return CALLER_ROUTES[caller]
    if "::" in caller:
        return f"called from {caller}"
    return f"called from {caller} (a bare name the hook could not verify)"


def text_md5(text: str) -> str:
    """The md5 the hook gives a text: its UTF-8 bytes and one final newline.

    The hook writes the text with ``writeLines`` before hashing it, because
    ``tools::md5sum`` hashes files only, so text joined by newlines gains one
    more at the end (spec §8, ``TEXT``). A whole file evaluated as text
    (``parse(text = readLines(f))``) therefore has the file's own md5 when
    the file ends in a newline.
    """
    return hashlib.md5((text + "\n").encode("utf-8")).hexdigest()


def knitr_label_quoted(params: str) -> str:
    """knitr's ``quote_label``: quote an unquoted chunk label (knitr 1.45).

    ``setup, echo=FALSE`` becomes ``'setup', echo=FALSE``. The two patterns
    are knitr's own; Python's backtracking finds the same match as R's
    leftmost-longest one for these anchored patterns.
    """
    params = re.sub(r"^\s*,?", "", params, count=1)
    if re.match(r"^\s*[^'\"](,|\s*$)", params):
        return re.sub(r"^\s*([^'\"])(,|\s*$)", r"'\1'\2", params, count=1)
    if re.match(r"^\s*[^'\"](,|[^=]*(,|\s*$))", params):
        return re.sub(r"^\s*([^'\"][^=]*)(,|\s*$)", r"'\1'\2", params, count=1)
    return params


def document_texts(text: str) -> dict[str, str]:
    """What knitr evaluates from an R Markdown or Quarto document, by md5.

    The 2026-10-08 probe (knitr 1.45, in the launcher-matrix image) showed
    knitr evaluating three kinds of text from a document through
    ``parse(text =)``, each a deterministic derivation of the document's own
    content (spec §8, ``TEXT``):

    - each R chunk's code, less its leading ``#|`` option lines, which knitr
      reads as options (``partition_chunk``); the code with those lines is
      kept too, should a tool evaluate it whole;
    - each inline expression (`` `r expr` ``), exactly as captured;
    - each chunk header's options, as ``parse_params`` builds them for
      evaluation: ``alist( <options, the label quoted> )``.

    Returns:
        ``{md5: description}``, the description naming the chunk.
    """
    texts: dict[str, str] = {}
    body: list[str] | None = None
    prose: list[str] = []
    number = 0
    for line in text.splitlines():
        if body is None:
            start = CHUNK_START_RE.match(line)
            if start and start.group(1).lower() == "r":
                number += 1
                body = []
                params = re.sub(r"^\s*,*|,*\s*$", "", start.group(2))
                if params:
                    texts[text_md5(f"alist( {knitr_label_quoted(params)} )")] = \
                        f"chunk {number}'s options"
            elif start is None:
                prose.append(line)
        elif CHUNK_END_RE.match(line):
            texts[text_md5("\n".join(body))] = f"chunk {number}"
            options = 0
            while options < len(body) and body[options].startswith("#|"):
                options += 1
            if 0 < options < len(body):
                texts[text_md5("\n".join(body[options:]))] = f"chunk {number}"
            body = None
        else:
            body.append(line)
    for inline in INLINE_CODE_RE.findall("\n".join(prose)):
        texts.setdefault(text_md5(inline), "inline code")
    return texts


def description_fields(data: bytes) -> dict[str, str]:
    """The fields of an R ``DESCRIPTION`` file (Debian control format)."""
    fields: dict[str, str] = {}
    key = None
    for line in data.decode("utf-8", errors="replace").splitlines():
        if line[:1] in (" ", "\t") and key:
            fields[key] += " " + line.strip()
        elif ":" in line:
            key, _, value = line.partition(":")
            key = key.strip()
            fields[key] = value.strip()
    return fields


def load_catalogue(target_dir: Path, by_id: dict[str, dict], original_bytes: dict[str, bytes],
                   executed: list[dict], wrappers: list[dict],
                   generated: list[str]) -> dict:
    """What a credited run may load, as the gate itself computes it (spec §8).

    The gate computes the md5 of every original from bytes it has verified
    against the retrieval hash, and of every declared copy and wrapper from
    the attempt directory, so a load is bound to content, never to a digest
    the executor wrote down.

    Args:
        target_dir: The attempt directory.
        by_id: The manifest's originals, by id.
        original_bytes: Verified bytes of each original that has them.
        executed: ``check_code_integrity``'s executed records (path, original,
            identical).
        wrappers: The manifest's wrappers.
        generated: Attempt-relative paths of code the runs generated.

    Returns:
        ``{paths, md5, chunks, packages, executed}``:

        - ``paths``: attempt-relative path to ``{class, id, md5}``, where the
          class is ``original``, ``edited-copy``, ``wrapper``, or
          ``generated``, and the id an original's id or a wrapper's role;
        - ``md5``: md5 to ``(class, id)``, for content found off its path;
        - ``chunks``: an original document's id to the md5 of each chunk;
        - ``packages``: a package name to ``(original id, version)``, from
          a declared source tree's ``DESCRIPTION``;
        - ``scripts``: each R original's bytes, for slices evaluated as text;
        - ``trees``: a package name to its declared source tree, as
          ``{roots, code}``: the attempt directories holding it, and its R
          code files' bytes by their path in the tree (``R/f.R``);
        - ``executed``: each executed copy's path to its original's id.
    """
    paths: dict[str, dict] = {}
    by_md5: dict[str, tuple[str, str]] = {}
    chunks: dict[str, set[str]] = {}
    packages: dict[str, tuple[str, str]] = {}
    names: dict[str, set[str]] = {oid: set() for oid in by_id}

    def file_md5(rel: str) -> str | None:
        path = inside(target_dir, rel)
        return cached_digest(path, "md5") if path is not None and path.is_file() else None

    for oid, data in original_bytes.items():
        by_md5[hashlib.md5(data).hexdigest()] = ("original", oid)
    for oid, item in by_id.items():
        if item.get("local_copy"):
            names[oid].add(item["local_copy"])
            digest = file_md5(item["local_copy"])
            if digest and oid in original_bytes:
                paths[item["local_copy"]] = {"class": "original", "id": oid, "md5": digest}
        member = (item.get("archive") or {}).get("member")
        if member:
            names[oid].add(member)
    executed_map: dict[str, str] = {}
    for record in executed:
        oid, rel = record.get("original"), record.get("path")
        if oid not in by_id or "sha256" not in record:
            continue
        names[oid].add(rel)
        executed_map[rel] = oid
        digest = file_md5(rel)
        if digest is None:
            continue
        kind = "original" if record.get("identical") else "edited-copy"
        paths[rel] = {"class": kind, "id": oid, "md5": digest}
        by_md5.setdefault(digest, (kind, oid))
    for item in wrappers:
        digest = file_md5(item["path"])
        if digest is not None:
            kind = "generated" if item["role"] == "generated" else "wrapper"
            paths[item["path"]] = {"class": kind, "id": item["role"], "md5": digest}
            by_md5.setdefault(digest, (kind, item["path"]))
    for rel in generated:
        digest = file_md5(rel)
        if digest is not None:
            by_md5.setdefault(digest, ("generated", rel))
    for oid, data in original_bytes.items():
        suffixes = {Path(name).suffix.lower() for name in names[oid]}
        if suffixes & set(DOCUMENT_SUFFIXES):
            chunks[oid] = set(document_texts(data.decode("utf-8", errors="replace")))
        if any(Path(name).name == "DESCRIPTION" for name in names[oid]):
            fields = description_fields(data)
            if fields.get("Package"):
                packages[fields["Package"]] = (oid, fields.get("Version", ""))
    trees: dict[str, dict] = {}
    for oid, data in original_bytes.items():
        roots = {posixpath.dirname(name) for name in names[oid]
                 if Path(name).name == "DESCRIPTION"}
        package = description_fields(data).get("Package") if roots else None
        if not package:
            continue
        code: dict[str, bytes] = {}
        for other, content in original_bytes.items():
            for name in names[other]:
                for root in roots:
                    inner = name[len(root) + 1:] if name.startswith(root + "/") else ""
                    if (inner.startswith("R/") and inner.count("/") == 1
                            and Path(inner).suffix in R_CODE_SUFFIXES):
                        code[inner] = content
        trees[package] = {"roots": sorted(roots), "code": code}
    scripts = {oid: data for oid, data in original_bytes.items()
               if any(Path(name).suffix.lower() == ".r" for name in names[oid])}
    return {"paths": paths, "md5": by_md5, "chunks": chunks, "packages": packages,
            "trees": trees, "scripts": scripts, "executed": executed_map}


def package_source_texts(trees: dict[str, dict], sources: set[str]) -> dict[str, str]:
    """What R CMD INSTALL parses from a declared tree's code, by md5.

    For a package with an Encoding field, the installer parses each R file
    as text with a ``#line 1 "<path>"`` line before its lines, where the
    path is the file's absolute path in the source directory it installs
    from (``tools:::.install_package_code_files``, R 4.3.2; 2026-10-08
    probe). ``sources`` are the directories a run installed from; an edited
    copy of the source matches nothing.

    Returns:
        ``{md5: "<package> <R file>"}``.
    """
    texts: dict[str, str] = {}
    for package, tree in trees.items():
        for inner, data in tree["code"].items():
            lines = re.split(r"\r\n|\r|\n", data.decode("utf-8", errors="replace"))
            if lines and lines[-1] == "":
                lines.pop()
            for source in sources:
                header = f'#line 1 "{posixpath.join(source, inner)}"'
                texts[text_md5("\n".join([header, *lines]))] = f"{package} {inner}"
    return texts


def lane_md5s(doc: dict) -> dict[str, str]:
    """md5 of each lane R file a run staged, where the gate holds its bytes.

    Only the hook is R code a process could load from ``/lane``. Its bytes
    are taken from the runtime directory when their sha256 is the one the run
    recorded; the launcher binding has already tied that digest to the
    launch commit.
    """
    found = {}
    data = (RUNTIME_DIR / "hook.R").read_bytes()
    if hashlib.sha256(data).hexdigest() == (doc.get("lane_files") or {}).get("hook.R"):
        found[hashlib.md5(data).hexdigest()] = "hook.R"
    return found


class SliceTracker:
    """An R original evaluated as text in contiguous, in-order slices.

    A wrapper may run the authors' script part by part, evaluating each
    part's lines with ``parse(text =)`` and ``eval``, in the script's own
    order (herskind's pilot does, by its ``#PART`` headers). Each slice is a
    ``TEXT`` whose md5 is that of its lines joined by newlines, with one
    more at the end, as the hook hashes it. Within a process, the slices
    must follow one another; between them, and before the first, only
    comment and blank lines may be skipped, since those run no code. A
    sequence that covers every code line runs the original; one that does
    not leaves lines that never ran, which is an omission and is flagged.
    Hashing is incremental, so a slice is found without enumerating every
    range.
    """

    def __init__(self, scripts: dict[str, bytes]) -> None:
        self.lines = {oid: [line + b"\n" for line in self.split(data)]
                      for oid, data in scripts.items()}
        self.cursor: dict[tuple[str, str], int] = {}
        self.ranges: dict[tuple[str, str], list[tuple[int, int]]] = {}

    @staticmethod
    def split(data: bytes) -> list[bytes]:
        """Lines as R's readLines gives them (LF, CRLF, or CR endings)."""
        lines = re.split(rb"\r\n|\r|\n", data)
        if lines and lines[-1] == b"":
            lines.pop()
        return lines

    @staticmethod
    def inert(line: bytes) -> bool:
        """A blank or comment line, which runs no code."""
        stripped = line.strip()
        return not stripped or stripped.startswith(b"#")

    def match(self, token: str, md5: str) -> str | None:
        """The original a text is the next slice of, in this process."""
        for oid, lines in self.lines.items():
            start = self.cursor.get((token, oid), 0)
            starts = [start]
            while starts[-1] < len(lines) and self.inert(lines[starts[-1]]):
                starts.append(starts[-1] + 1)
            for first in starts:
                hasher = hashlib.md5()
                for last in range(first, len(lines)):
                    hasher.update(lines[last])
                    if hasher.hexdigest() == md5:
                        self.cursor[(token, oid)] = last + 1
                        self.ranges.setdefault((token, oid), []).append((first, last))
                        return oid
        return None

    def missing(self, token: str, oid: str) -> list[tuple[int, int]]:
        """1-based ranges of code lines no slice covered, in this process."""
        covered = {i for first, last in self.ranges.get((token, oid), [])
                   for i in range(first, last + 1)}
        gaps: list[tuple[int, int]] = []
        for index, line in enumerate(self.lines[oid]):
            if index in covered or self.inert(line):
                continue
            if gaps and gaps[-1][1] == index:
                gaps[-1] = (gaps[-1][0], index + 1)
            else:
                gaps.append((index + 1, index + 1))
        return gaps


def account_loads(target_dir: Path, runs: dict[str, dict], catalogue: dict,
                  final_run: str) -> dict:
    """The gate's account of every load in the credited runs (spec §8).

    - ``LOAD``: each is bound on its own, whatever call encloses it. In the
      work copy, the loaded content must be what that path held at the run's
      baseline, and the path must be an original, a declared edited copy or
      wrapper, or lane instrumentation; code the run wrote is never loadable.
      Under ``/lane`` it must be a lane file. Elsewhere it is an original or
      wrapper by content, a tool-internal load the lane can map, library
      code, or image code, which is flagged. A temporary directory holds
      code written during the run, so a load from one that maps to nothing
      fails.
    - ``TEXT`` must match by md5 an original (or a declared edited copy,
      flagged in its own right), a code chunk of an original document, or a
      tool expression on the lane's list, or, by the text the event carries
      verbatim and its caller, a package template (``PACKAGE_TEXTS``). A
      verbatim text must hash back to its md5. Anything else is an
      obligation: texts held verbatim are grouped into one per place and
      caller, listing every text (``run-time-texts``); a text not held
      verbatim is one on its own (``unmatched-text``).
    - ``CONN`` is always an obligation (``connection-load``): a path hash does
      not cover a connection's content.
    - ``PKG``: a package that is not base and has no repository or remote
      provenance is flagged (``local-package``).
    - ``HOOKERR`` is an error: a load may have gone unlogged.

    Finally, a declared executed copy that no credited run loaded is flagged
    (``executed-not-loaded``).

    Args:
        target_dir: The attempt directory.
        runs: ``check_run_records``' ``credited_records``.
        catalogue: ``load_catalogue``'s result.
        final_run: The final run's id.

    Returns:
        ``{errors, flags, obligations, warnings, originals_loaded, runs}``,
        where ``runs`` counts each run's loads by class.
    """
    errors: list[str] = []
    flags: list[str] = []
    obligations: list[str] = []
    warnings: list[str] = []
    issued: set[str] = set()
    loaded_paths: set[str] = set()
    loaded_md5s: set[str] = set()
    originals_loaded: set[str] = set()
    expressions = {text_md5(text): what for text, what in TOOL_EXPRESSIONS.items()}
    chunk_owner = {digest: oid for oid, digests in catalogue["chunks"].items()
                   for digest in digests}
    summary: dict[str, dict[str, int]] = {}
    # Unmatched texts held verbatim, by (place, caller), across the runs.
    groups: dict[tuple[str, str], dict] = {}

    def mark_tree(roots: list[str]) -> None:
        """Count a declared package tree's executed copies as run: an
        install of the tree runs the authors' package."""
        for rel, oid in catalogue["executed"].items():
            if any(rel.startswith(root.rstrip("/") + "/") for root in roots):
                loaded_paths.add(rel)
                originals_loaded.add(oid)

    # Content anywhere in the attempt, by sha256: the input tree and every
    # sealed output. A run's baseline names content by sha256, and this finds
    # bytes to take its md5 from, wherever the content now sits (a renamed
    # project profile, an output consumed from an earlier run).
    content: dict[str, Path] = {}
    tree, _ = input_inventory(target_dir)
    for rel, digest in tree.items():
        content.setdefault(digest, target_dir / rel)
    for run_id, run in runs.items():
        for item in run["outputs"]:
            path = target_dir / "outputs" / run_id / item.get("path", "")
            if item.get("sha256") and path.is_file():
                content.setdefault(item["sha256"], path)
    lane_profile = LANE_PROFILE.encode("utf-8")

    def content_md5(sha256: str | None) -> str | None:
        if sha256 == hashlib.sha256(lane_profile).hexdigest():
            return hashlib.md5(lane_profile).hexdigest()
        path = content.get(sha256 or "")
        return cached_digest(path, "md5") if path is not None else None

    def add(bucket: list[str], issue: Issue) -> None:
        if issue.issue_id not in issued:
            issued.add(issue.issue_id)
            bucket.append(issue)

    def bind_install(path: str, cwd: str, where: str, built: bool, baseline: dict[str, str],
                     mount: str) -> None:
        """PKGBUILD: an install of a declared original tree or archive is
        accounted for, and so is an archive named for a declared tree's
        package and version when the run built one (devtools::install and
        remotes::install_local build first). Anything else is an
        obligation; the local-package flag covers the installed result."""
        full = path if path.startswith("/") else posixpath.normpath(posixpath.join(cwd, path))
        archive = PACKAGE_ARCHIVE_RE.fullmatch(posixpath.basename(full))
        if mount and full.startswith(mount + "/"):
            rel = full[len(mount) + 1:]
            tree = catalogue["paths"].get(posixpath.join(rel, "DESCRIPTION"))
            if tree is not None and tree["class"] in ("original", "edited-copy"):
                mark_tree([rel])
                return
            archived = catalogue["paths"].get(rel)
            if archived is not None and archived["class"] in ("original", "edited-copy"):
                loaded_paths.add(rel)
                originals_loaded.add(archived["id"])
                return
            subject = rel
            files = {rel: baseline.get(rel) or baseline.get(posixpath.join(
                rel, "DESCRIPTION")) or "missing"}
        else:
            subject = posixpath.basename(full)
            files = {"archive": subject}
        note = ""
        if archive:
            source = catalogue["packages"].get(archive.group(1))
            if source is not None and source[1] == archive.group(2) and built:
                mark_tree(catalogue["trees"].get(archive.group(1), {}).get("roots", []))
                return
            if source is not None:
                note = (f" (the declared tree {source[0]} is version {source[1]}"
                        + (", and the run built no package)" if not built else ")"))
        add(obligations, Issue.obligation(
            "package-install", subject, f"{where} ran R CMD INSTALL on {full}, which is no "
            f"declared original tree or archive{note}: confirm what was installed",
            files=files))

    def bind_script(process: dict, where: str, built: bool, baseline: dict[str, str],
                    mount: str, count: Any) -> None:
        """A script read from standard input (R < file): an original by
        content, R's package tools, or an obligation keyed on its content."""
        argv = process["argv"]
        options = argv[:argv.index("--args")] if "--args" in argv else argv
        script = process.get("script")
        if script is None:
            # A record from a shim that did not capture the script.
            if (process["exec"] and not process["exempt"]
                    and process["stdin"] in ("file", "pipe")
                    and not any(a.startswith(SCRIPT_OPTIONS) for a in options)):
                add(obligations, Issue.obligation(
                    "stdin-script", f"uncaptured@{process.get('cwd')}", f"{where} read its "
                    f"script from standard input (R < file), which was not captured: confirm "
                    f"what it ran", files={"argv": json_digest(argv)}))
            return
        md5, text = script["md5"], script.get("text")
        known = catalogue["md5"].get(md5)
        if known is not None and known[0] in ("original", "edited-copy"):
            originals_loaded.add(known[1])
            loaded_md5s.add(md5)
            count("stdin-original")
        elif text == PACKAGE_BUILD_SCRIPT:
            count("package-build")
        elif text == PACKAGE_INSTALL_SCRIPT:
            count("package-install")
            for path in install_targets(argv):
                bind_install(path, str(process.get("cwd") or mount), where, built, baseline,
                             mount)
        elif text is not None and any(p.fullmatch(text) for p in INSTALLER_SCRIPTS):
            count("installer")
        else:
            count("stdin-unmatched")
            first = (text or "").split("\n", 1)[0][:80]
            add(obligations, Issue.obligation(
                "stdin-script", md5, f"{where} read its script from standard input (R < "
                f"file; md5 {md5[:12]}…" + (f", beginning {first!r}" if first else "")
                + "): it matches no original and no R package tool, so confirm what it ran",
                files={"script": md5}))

    for run_id, run in runs.items():
        doc, events = run["doc"], run["events"]
        mount = str(doc.get("mount_path") or "").rstrip("/")
        baseline = (run["baseline"] or {}).get("files") or {}
        changes = (run["baseline"] or {}).get("changes") or []
        consumed = {c.get("path"): c.get("run") for c in changes if c.get("change") == "consumed"}
        injected = {c.get("path") for c in changes if c.get("change") == "injected"}
        renamed = {c.get("to"): c.get("from") for c in changes if c.get("change") == "renamed"}
        lane_files = lane_md5s(doc)
        processes = (run.get("census") or {}).get("processes") or []
        cwd_of = {p["token"]: str(p.get("cwd") or "") for p in processes}

        def library_of(event: dict) -> str:
            # A PKG event's library, absolute; an older hook recorded
            # lib.loc as given, which may be relative to the process.
            library = decode_field(event["fields"][2])
            return (library if library.startswith("/") else
                    posixpath.normpath(posixpath.join(cwd_of.get(event["token"], "/"), library)))

        r_home = str((doc.get("front_end") or {}).get("r_home") or "").rstrip("/")
        libraries = {f"{r_home}/library"} if r_home else set()
        libraries |= {library_of(e) for e in events
                      if e["event"] == "PKG" and len(e["fields"]) > 2 and e["fields"][2] != "none"}
        # The directories the run installed packages from: each install's
        # target, and the staging directory the installer's helpers ran in.
        sources: set[str] = set()
        for process in processes:
            script_text = (process.get("script") or {}).get("text")
            if script_text == PACKAGE_INSTALL_SCRIPT:
                for target in install_targets(process["argv"]):
                    full = (target if target.startswith("/") else posixpath.normpath(
                        posixpath.join(cwd_of.get(process["token"]) or mount, target)))
                    if not PACKAGE_ARCHIVE_RE.fullmatch(posixpath.basename(full)):
                        sources.add(full)
            elif script_text is not None and any(p.fullmatch(script_text)
                                                 for p in INSTALLER_SCRIPTS):
                sources.add(cwd_of.get(process["token"], ""))
        package_texts = package_source_texts(catalogue["trees"], sources - {""})
        slices = SliceTracker(catalogue.get("scripts") or {})
        # Texts the gate holds verbatim: each -e argument the shim recorded.
        verbatim: dict[str, str] = {}
        for process in processes:
            argv = process["argv"]
            options = argv[:argv.index("--args")] if "--args" in argv else argv
            for index, option in enumerate(options[:-1]):
                if option == "-e":
                    verbatim[text_md5(options[index + 1])] = options[index + 1]
        counts: dict[str, int] = {}
        summary[run_id] = counts
        by_seq: dict[tuple[str, int], dict] = {(e["token"], e["seq"]): e for e in events}
        forked_from = {e["token"]: e["fields"][0] for e in events
                       if e["event"] == "FORK" and e["fields"]}
        top_file: dict[str, dict] = {}
        bindings: dict[tuple[str, int], dict] = {}

        def lookup(token: str, seq: int) -> dict | None:
            # A forked child's events inside a load its parent had open at the
            # fork nest under the child's FORK, which names that load's seq in
            # the parent (0 when none was open); follow it there.
            found = by_seq.get((token, seq))
            while found is not None and found["event"] == "FORK":
                fields = found["fields"]
                outer = int(fields[1]) if len(fields) > 1 and fields[1].isdigit() else 0
                found = by_seq.get((fields[0], outer)) if outer else None
            return found

        def script_of(token: str) -> dict | None:
            # The command-line script a process runs, or, for a forked child,
            # its parent's.
            seen: set[str] = set()
            while token not in top_file and token in forked_from and token not in seen:
                seen.add(token)
                token = forked_from[token]
            return top_file.get(token)

        def enclosing_of(event: dict, index: int) -> int:
            fields = event["fields"]
            return int(fields[index]) if len(fields) > index and fields[index].isdigit() else 0

        def label(event: dict, enclosing: int) -> tuple[str, dict[str, str]]:
            """Where a text or connection was evaluated: the enclosing load,
            else the process's own script, as a label and its evidence."""
            outer = lookup(event["token"], enclosing) if enclosing else None
            if outer is None or outer["event"] != "LOAD":
                outer = script_of(event["token"])
            if outer is None:
                return "the command line", {}
            where = decode_field(outer["fields"][1])
            if mount and where.startswith(mount + "/"):
                where = where[len(mount) + 1:]
            return where, {where: outer["fields"][2]}

        def count(kind: str) -> None:
            counts[kind] = counts.get(kind, 0) + 1

        def under_package(event: dict, index: int) -> bool:
            # Whether the innermost enclosing event is a package's PKG.
            enclosing = enclosing_of(event, index)
            outer = lookup(event["token"], enclosing) if enclosing else None
            return outer is not None and outer["event"] == "PKG"

        def tool_call(event: dict) -> tuple[dict | None, dict | None, dict | None]:
            """The innermost enclosing tool LOAD and its binding, and the
            immediately enclosing PKG event, if any."""
            enclosing = enclosing_of(event, 5)
            parent = lookup(event["token"], enclosing) if enclosing else None
            package = parent if parent is not None and parent["event"] == "PKG" else None
            while parent is not None and parent["event"] == "LOAD":
                if decode_field(parent["fields"][0]) in TOOL_LOADERS:
                    return parent, bindings.get((parent["token"], parent["seq"])), package
                outer = enclosing_of(parent, 5)
                parent = lookup(parent["token"], outer) if outer else None
            return None, None, package

        def bind_declared(declared: dict, rel: str) -> dict:
            if declared["class"] in ("original", "edited-copy"):
                originals_loaded.add(declared["id"])
            loaded_paths.add(rel)
            loaded_md5s.add(declared["md5"])
            return dict(declared, rel=rel)

        def bind_load(event: dict, where: str) -> dict:
            fields = event["fields"]
            fn, path, md5 = decode_field(fields[0]), decode_field(fields[1]), fields[2]
            if md5 == "none":
                if fn in TOOL_LOADERS:
                    return {"class": "tool-call"}
                warnings.append(f"{where} called {fn} on {path}, which is not a readable file, "
                                f"so nothing was loaded from it")
                return {"class": "not-a-file"}
            tool, tool_binding, package = tool_call(event)
            if package is not None and path.startswith(library_of(package) + "/"):
                return {"class": "library"}
            if path.startswith(LANE_MOUNT + "/"):
                if md5 in lane_files:
                    return {"class": "lane", "id": lane_files[md5]}
                errors.append(f"{where} loaded {path} from the lane directory, but its content "
                              f"is no lane file's")
                return {"class": "unaccounted"}
            tool_fn = decode_field(tool["fields"][0]) if tool is not None else None
            depth = int(fields[4]) if fields[4].isdigit() else -1
            for within, loader, pattern, what in TOOL_BOOTSTRAP:
                if (loader == fn and pattern.fullmatch(path)
                        and (within == tool_fn if within is not None
                             else tool is None and depth == 0)):
                    return {"class": "tool-internal", "id": what}
            if tool is not None:
                document = (tool_binding or {}).get("id")
                if md5 in catalogue["chunks"].get(document, ()):
                    return {"class": "tool-internal", "id": f"{tool_fn} chunk of {document}"}
            in_work = bool(mount) and path.startswith(mount + "/")
            if in_work:
                rel = path[len(mount) + 1:]
                if (rel not in baseline and fn in ("rmarkdown::render", "knitr::knit")
                        and rel.endswith(QUARTO_INTERMEDIATE)):
                    # Quarto's intermediate for a declared document: its
                    # input, not code; every text knitr evaluates from it
                    # must still bind to the original's own (D-3).
                    stem = rel[:-len(QUARTO_INTERMEDIATE)]
                    document = catalogue["paths"].get(f"{stem}.qmd")
                    if document is not None and document["class"] in ("original",
                                                                      "edited-copy"):
                        bind_declared(document, f"{stem}.qmd")
                        return {"class": "tool-internal", "id": document["id"]}
                if rel not in baseline:
                    errors.append(f"{where} loaded {rel}, which the run itself wrote: generated "
                                  f"code is never loadable (load the original that generated "
                                  f"it)")
                    return {"class": "generated"}
                if rel in consumed:
                    errors.append(f"{where} loaded {rel}, an output of {consumed[rel]} consumed "
                                  f"as input: generated code is never loadable")
                    return {"class": "generated"}
                expected = content_md5(baseline[rel])
                if expected is None:
                    warnings.append(f"{where} loaded {rel}, whose baseline content is no longer "
                                    f"in the attempt, so the gate cannot check what was loaded")
                elif expected != md5:
                    errors.append(f"{where} loaded {rel} at md5 {md5[:12]}…, but the run's "
                                  f"baseline holds md5 {expected[:12]}…: it changed during the "
                                  f"run before it was loaded")
                    return {"class": "unaccounted"}
                if rel in injected:
                    return {"class": "lane", "id": rel}
                declared_rel = renamed.get(rel, rel)
                declared = catalogue["paths"].get(declared_rel)
                if declared is not None:
                    if declared["class"] == "generated":
                        errors.append(f"{where} loaded {declared_rel}, declared as generated "
                                      f"code, which is never loadable")
                        return {"class": "generated"}
                    if declared["md5"] != md5:
                        message = (f"{where} loaded {declared_rel} at content other than the "
                                   f"declared file's")
                        if run_id == final_run:
                            errors.append(message)
                            return {"class": "unaccounted"}
                        # An earlier, consumed run that ran other code is the
                        # consumed-other-code issue's business.
                        warnings.append(message + " (see consumed-other-code)")
                    return bind_declared(declared, declared_rel)
            known = catalogue["md5"].get(md5)
            if known is not None:
                kind, ident = known
                if kind == "generated":
                    errors.append(f"{where} loaded {path}, whose content is generated code "
                                  f"({ident}), which is never loadable")
                    return {"class": "generated"}
                if kind in ("original", "edited-copy"):
                    originals_loaded.add(ident)
                loaded_md5s.add(md5)
                return {"class": kind, "id": ident}
            if in_work:
                errors.append(f"{where} loaded undeclared code {path[len(mount) + 1:]}: neither "
                              f"an authors' file, a declared wrapper, nor lane instrumentation")
                return {"class": "unaccounted"}
            if tool is not None:
                # Nesting waives nothing: a load inside a tool call that maps
                # to no source is unaccounted, never image code (Astra's
                # specification review, D-3).
                errors.append(f"{where} loaded {path} inside {decode_field(tool['fields'][0])}, "
                              f"but it maps to no original, declared wrapper, chunk of the "
                              f"document, or tool-generated file")
                return {"class": "unaccounted"}
            if path.startswith(TRANSIENT_ROOTS):
                errors.append(f"{where} loaded {path}, code in a temporary directory that maps "
                              f"to no original, declared wrapper, or tool-generated file")
                return {"class": "unaccounted"}
            if any(path.startswith(library.rstrip("/") + "/") for library in libraries):
                return {"class": "library"}
            if md5 in IMAGE_LAUNCHERS:
                return {"class": "image-launcher", "id": IMAGE_LAUNCHERS[md5]}
            add(flags, Issue.flag(
                "image-code", path, f"{where} loaded {path} from the image, outside the work "
                f"copy and every R library: image code is not the authors' deposit, so confirm "
                f"what it is", files={path: md5}))
            return {"class": "image"}

        for event in events:
            kind, fields, token = event["event"], event["fields"], event["token"]
            where = f"{run_id}: process {event['pid']}"
            if kind == "HOOKERR":
                errors.append(f"{where}: the lane hook failed in {decode_field(fields[0])} "
                              f"({decode_field(fields[1]) if len(fields) > 1 else 'no message'})"
                              f", so a load may have gone unlogged")
            elif kind == "LOAD" and len(fields) >= 6:
                binding = bind_load(event, where)
                bindings[(token, event["seq"])] = binding
                count(binding["class"])
                if decode_field(fields[0]) == "file":
                    top_file.setdefault(token, event)
            elif kind == "TEXT" and fields:
                md5 = fields[0]
                # The text itself, where the hook carried it, must hash back
                # to the md5; otherwise the stream is not consistent.
                try:
                    raw, caller = text_fields(fields)
                except ValueError:
                    raw, caller = None, None
                    errors.append(f"{where}: a TEXT event (md5 {md5[:12]}…) carries a "
                                  f"verbatim field that is not hex")
                if raw is not None and hashlib.md5(raw + b"\n").hexdigest() != md5:
                    errors.append(f"{where}: a TEXT event's verbatim text does not hash to its "
                                  f"md5 {md5[:12]}…, so the event stream is not consistent")
                    raw = None
                try:
                    held = raw.decode("utf-8") if raw is not None else None
                except UnicodeDecodeError:
                    held = None
                known = catalogue["md5"].get(md5)
                if known is not None and known[0] in ("original", "edited-copy"):
                    originals_loaded.add(known[1])
                    loaded_md5s.add(md5)
                    count("text-original")
                elif md5 in chunk_owner:
                    count("text-chunk")
                elif md5 in expressions or (md5 in verbatim and any(
                        p.fullmatch(verbatim[md5]) for p in TEXT_TEMPLATES)):
                    count("text-tool")
                elif md5 in package_texts:
                    count("text-package-source")
                    mark_tree(catalogue["trees"][package_texts[md5].split(" ")[0]]["roots"])
                elif slices.match(token, md5) is not None:
                    count("text-original-part")
                elif under_package(event, 3):
                    # Evaluated while a package's namespace loads: that
                    # package's own code, which its provenance or the
                    # local-package flag covers.
                    count("text-package")
                elif held is not None and any(
                        caller in callers and pattern.fullmatch(held)
                        for callers, pattern, _ in PACKAGE_TEXTS):
                    count("text-template")
                elif held is not None:
                    # Held verbatim, so a reviewer can read it: grouped with
                    # the other texts from this place and caller, and ruled
                    # once with every text shown.
                    count("text-unmatched")
                    place, evidence = label(event, enclosing_of(event, 3))
                    group = groups.setdefault((place, caller or "unknown"),
                                              {"texts": {}, "evidence": {}, "runs": []})
                    group["texts"].setdefault(md5, held)
                    group["evidence"].update(evidence)
                    if run_id not in group["runs"]:
                        group["runs"].append(run_id)
                else:
                    count("text-unmatched")
                    place, evidence = label(event, enclosing_of(event, 3))
                    route = f", {caller_phrase(caller)}," if caller else ""
                    add(obligations, Issue.obligation(
                        "unmatched-text", f"{md5}@{place}", f"{where} evaluated code from a "
                        f"string (md5 {md5[:12]}…, not held verbatim) in {place}{route} that "
                        f"matches no original, no chunk of an original document, and no tool "
                        f"expression: confirm what it ran",
                        files={"text": md5, **evidence}))
            elif kind == "CONN" and len(fields) >= 3:
                count("connection")
                caller = decode_field(fields[5]) if len(fields) > 5 else ""
                if under_package(event, 4) or caller in NAMESPACE_READERS:
                    # A package's own load, or R reading a NAMESPACE file
                    # (the installer calls the parser directly): package
                    # machinery, which the package's provenance covers.
                    continue
                place, evidence = label(event, enclosing_of(event, 4))
                fn, cls, what = (decode_field(f) for f in fields[:3])
                add(obligations, Issue.obligation(
                    "connection-load", f"{fn}:{cls}:{what}@{place}", f"{where} called {fn} on a "
                    f"{cls} ({what}) in {place}" + (f", from {caller}" if caller else "")
                    + ": no path hash covers a connection's content, so confirm what it "
                    "evaluated", files=evidence))
            elif kind == "PKG" and len(fields) >= 8:
                count("package")
                name, version = decode_field(fields[0]), fields[1]
                # remotes records RemoteType "local" for a package installed
                # from a local path, which is no provenance (2026-10-08 probe).
                remote_type = decode_field(fields[4]) if fields[4] != "none" else None
                if (name in BASE_PACKAGES or version == "none" or fields[3] != "none"
                        or remote_type not in (None, "local")):
                    continue
                version = decode_field(version)
                source = catalogue["packages"].get(name)
                if source is None:
                    note = "declare its source tree as an original"
                elif source[1] == version:
                    note = f"its declared source tree ({source[0]}) has the same version"
                else:
                    note = (f"its declared source tree ({source[0]}) is version {source[1]}, "
                            f"not the installed {version}")
                add(flags, Issue.flag(
                    "local-package", name, f"{where} loaded package {name} {version} from "
                    f"{decode_field(fields[2])}, which records no repository or remote source: "
                    f"it was installed locally, so {note}",
                    files={"DESCRIPTION": fields[7], "version": version}))

        # An original run part by part: loaded when the slices cover every
        # code line, in order; otherwise an omission, flagged.
        for (token, oid), _ in sorted(slices.ranges.items()):
            gaps = slices.missing(token, oid)
            if not gaps:
                originals_loaded.add(oid)
                loaded_md5s.add(hashlib.md5(catalogue["scripts"][oid]).hexdigest())
                continue
            shown = ", ".join(f"{a}" if a == b else f"{a}-{b}" for a, b in gaps[:8])
            add(flags, Issue.flag(
                "original-partly-run", f"{oid}@{run_id}", f"{run_id} evaluated original "
                f"{oid!r} in slices that leave code lines {shown}"
                + (" and more" if len(gaps) > 8 else "") + " unrun: running only some of "
                "the authors' statements is an omission, so confirm it changes no result",
                files={"original": hashlib.sha256(catalogue["scripts"][oid]).hexdigest(),
                       "gaps": json_digest(gaps)}))

        # Each process's script read from standard input, which the exec
        # shim captured, and its restored workspace, bound to content.
        built = any((p.get("script") or {}).get("text") == PACKAGE_BUILD_SCRIPT
                    for p in processes)
        for process in processes:
            where = f"{run_id}: process {process['pid']}"
            bind_script(process, where, built, baseline, mount, count)
            if process.get("restore"):
                cwd = str(process.get("cwd") or "")
                rel = (".RData" if cwd == mount else
                       posixpath.join(cwd[len(mount) + 1:], ".RData")
                       if mount and cwd.startswith(mount + "/") else None)
                subject = rel or posixpath.join(cwd, ".RData")
                add(obligations, Issue.obligation(
                    "workspace-restore", subject, f"{where} restored a saved workspace "
                    f"({subject}): a declared input needing review",
                    files={subject: baseline.get(rel, "missing") if rel else "outside the "
                           "work copy"}))

    # Run-time texts held verbatim: one obligation per place and caller,
    # listing every text, so that one ruling sees them all. Its identity is
    # the place, the caller, and every text's md5, so a changed set needs a
    # new ruling.
    for (place, caller), group in sorted(groups.items()):
        texts = group["texts"]
        listed = "; ".join(json.dumps(t, ensure_ascii=False)
                           for t in sorted(texts.values()))
        add(obligations, Issue.obligation(
            "run-time-texts", f"{place}|{caller}",
            f"{', '.join(group['runs'])}: {len(texts)} text(s) built at run time and "
            f"evaluated in {place}, {caller_phrase(caller)}, match no original, no chunk "
            f"of an original document, and no tool expression or package template: confirm "
            f"what they ran. The texts: {listed}",
            files={**group["evidence"], **{f"text:{m}": m for m in sorted(texts)}}))

    # A run whose entry is a shell script ran it without any R load event.
    final_doc = runs.get(final_run, {}).get("doc") or {}
    if final_doc.get("interpreter") == "bash" and final_doc.get("entry") in catalogue["executed"]:
        loaded_paths.add(final_doc["entry"])
        originals_loaded.add(catalogue["executed"][final_doc["entry"]])
    for rel, oid in sorted(catalogue["executed"].items()):
        declared = catalogue["paths"].get(rel)
        if rel in loaded_paths or (declared is not None and declared["md5"] in loaded_md5s):
            continue
        add(flags, Issue.flag(
            "executed-not-loaded", rel, f"{rel} is declared as an executed copy of {oid!r}, but "
            f"no credited run loaded it: confirm how it ran, or that it did not",
            files=file_digests(target_dir, rel)))
    return {"errors": errors, "flags": flags, "obligations": obligations,
            "warnings": warnings, "originals_loaded": sorted(originals_loaded),
            "runs": summary}


def citation_findings(targets: list[dict], runs: dict, locked: list[str],
                      comparison_sha256: str = "") -> tuple[list[str], list[str], set[str]]:
    """Check comparison citations against sealed run outputs (spec §5).

    Each cited output must belong to a credited run (the final run or one it
    consumed) and carry the digest that run sealed. A reproduced target that
    cites nothing has a result not bound to any run: it stays in raw
    coverage but is not admitted until ruled (``target-unbound``).

    Args:
        targets: The comparison record's target entries.
        runs: ``check_code_integrity``'s ``runs`` block.
        locked: The plan's locked target ids.
        comparison_sha256: The comparison record's digest, the evidence an
            unbound target's issue is fingerprinted on.

    Returns:
        ``(errors, flags, unbound_target_ids)``; the flags are ``Issue``s.
    """
    errors: list[str] = []
    flags: list[str] = []
    unbound: set[str] = set()
    credited = set(runs.get("credited_runs") or [])
    sealed = runs.get("outputs") or {}
    for target in targets:
        tid = target.get("target_id")
        cites = target.get("outputs") or []
        for cite in cites:
            run_id, rel = cite.get("run"), cite.get("path")
            if run_id not in credited:
                errors.append(f"{tid} cites {run_id}, which credit does not rest on "
                              f"(credited: {sorted(credited) or 'none'})")
            elif sealed.get(run_id, {}).get(rel) != cite.get("sha256"):
                errors.append(f"{tid} cites outputs/{run_id}/{rel} at a digest {run_id} did "
                              f"not seal")
        if (not cites and tid in locked and target.get("testable") is not False
                and target.get("outcome") in REPRODUCED_OUTCOMES):
            unbound.add(tid)
            flags.append(Issue.flag("target-unbound", str(tid), f"{tid} cites no sealed run "
                                    f"output, so its result is not bound to a run "
                                    f"(target-unbound): not admitted until ruled",
                                    targets=(str(tid),),
                                    files={str(COMPARISON_FILE): comparison_sha256}))
    return errors, flags, unbound


# ---------------------------------------------------------------------------
# Conversions (gate 1.3, spec §11)
# ---------------------------------------------------------------------------
#
# Amendment 3 §7(d) allows a format conversion "only when a mechanical check
# confirms every value is unchanged", and any change of value is
# fail-and-uplift. The lane makes that check itself; the executor writes no
# evidence. Nothing is trimmed and nothing is normalised: text compares as
# text, and a typed workbook cell by its accepted renderings (spec §11).

TEXT_DELIMITERS = {".csv": ",", ".tsv": "\t", ".tab": "\t"}
WORKBOOK_SUFFIXES = (".xlsx", ".xlsm")
MISSING_MARKERS = frozenset({"", "NA", "NaN", "NULL"})
NUMBER_RE = re.compile(r"[+-]?(?:\d+\.?\d*|\.\d+)(?:[eE][+-]?\d+)?")
DATE_RE = re.compile(r"(\d{4})-(\d{2})-(\d{2})")
DATETIME_RE = re.compile(r"(\d{4})-(\d{2})-(\d{2})[T ](\d{2}):(\d{2})(?::(\d{2})(\.\d+)?)?"
                         r"(Z|[+-]\d{2}:?\d{2})?")
# Collision clearing (spec §11): the only reader the lane can confirm keeps a
# literal value and a missing value apart is one that reads a quoted field as
# text whatever its content, with the output quoting every literal and never
# a missing value. R's read.csv reads "NA" as missing even when quoted.
QUOTE_AWARE_READERS = frozenset({"readr::read_csv", "readr::read_tsv", "vroom::vroom"})
DIFFERENCES_SHOWN = 5


def read_delimited(data: bytes, encoding: str, delimiter: str) -> list[list[tuple[str, bool]]]:
    """A delimited text file's rows, each field as ``(text, quoted)``.

    RFC 4180 quoting: a field opening with a double quote runs to the next
    lone one, and a doubled quote inside it is one quote character. The
    quoting is kept, because a missing-marker collision can be cleared only
    by a reader that tells a quoted literal from an unquoted marker.

    Raises:
        UnicodeDecodeError, LookupError: the bytes do not decode as declared.
    """
    text = data.decode(encoding)
    rows: list[list[tuple[str, bool]]] = []
    row: list[tuple[str, bool]] = []
    field: list[str] = []
    quoted = in_quotes = False
    index, length = 0, len(text)
    while index < length:
        char = text[index]
        if in_quotes:
            if char == '"' and index + 1 < length and text[index + 1] == '"':
                field.append('"')
                index += 2
                continue
            if char == '"':
                in_quotes = False
            else:
                field.append(char)
        elif char == '"' and not field and not quoted:
            in_quotes = quoted = True
        elif char == delimiter:
            row.append(("".join(field), quoted))
            field, quoted = [], False
        elif char in "\r\n":
            row.append(("".join(field), quoted))
            rows.append(row)
            row, field, quoted = [], [], False
            if char == "\r" and index + 1 < length and text[index + 1] == "\n":
                index += 1
        else:
            field.append(char)
        index += 1
    if field or quoted or row:
        row.append(("".join(field), quoted))
        rows.append(row)
    return rows


def read_workbook(path: Path, sheet: str, cell_range: str | None, header_row: int) -> dict:
    """One sheet of an Excel workbook, typed, as the comparison needs it.

    The workbook is read twice with openpyxl: once for formulas, once for
    cached values. A formula or external-link cell is counted whatever its
    cached value, since a cached value is not evidence of a fresh
    calculation (Astra 6). Fully empty trailing rows and columns are trimmed
    and counted, and rows above the header are skipped and counted.

    Returns:
        ``{rows, formulas, errors, trimmed_rows, trimmed_columns, skipped_rows,
        other_sheets}``, where each row is a list of ``(type, value)`` cells
        (blank, string, number, boolean, date, datetime, time, error, or
        formula, the last carrying its cached value) and ``other_sheets``
        names the workbook's other non-empty sheets.

    Raises:
        LaneError: openpyxl is not installed, or the sheet is not in the book.
    """
    try:
        import openpyxl  # imported here: only a workbook conversion needs it
        from openpyxl.styles.numbers import is_date_format
    except ImportError as exc:
        raise LaneError("openpyxl is not installed (requirements.txt), so the gate cannot "
                        "read a workbook") from exc
    formulas_book = openpyxl.load_workbook(path, data_only=False)
    values_book = openpyxl.load_workbook(path, data_only=True)
    if sheet not in values_book.sheetnames:
        raise LaneError(f"sheet {sheet!r} is not in {path.name} "
                        f"(sheets: {', '.join(values_book.sheetnames)})")
    formula_sheet, value_sheet = formulas_book[sheet], values_book[sheet]
    grid_values = (value_sheet[cell_range] if cell_range
                   else tuple(value_sheet.iter_rows()))
    grid_formulas = (formula_sheet[cell_range] if cell_range
                     else tuple(formula_sheet.iter_rows()))
    rows: list[list[tuple[str, Any]]] = []
    formulas = errors = 0
    for value_row, formula_row in zip(grid_values, grid_formulas):
        row = []
        for cell, source in zip(value_row, formula_row):
            value = cell.value
            if source.data_type == "f" or (isinstance(source.value, str)
                                           and source.value.startswith("=")):
                formulas += 1
                row.append(("formula", value))
            elif cell.data_type == "e":
                errors += 1
                row.append(("error", value))
            elif value is None:
                row.append(("blank", None))
            elif isinstance(value, bool):
                row.append(("boolean", value))
            elif isinstance(value, (int, float)):
                row.append(("number", value))
            elif isinstance(value, datetime):
                fmt = (cell.number_format or "").lower()
                timed = is_date_format(fmt) and bool(re.search(r"[hs]|am/pm", fmt))
                row.append(("datetime", value) if timed or value.time() != datetime.min.time()
                           else ("date", value.date()))
            elif isinstance(value, date_type):
                row.append(("date", value))
            elif isinstance(value, time_type):
                row.append(("time", value))
            else:
                row.append(("string", str(value)))
        rows.append(row)
    # Trim fully empty trailing rows and columns, and count them.
    original_rows = len(rows)
    while rows and all(kind == "blank" for kind, _ in rows[-1]):
        rows.pop()
    trimmed_rows = original_rows - len(rows)
    width = max((len(r) for r in rows), default=0)
    last = max((i for r in rows for i, (kind, _) in enumerate(r) if kind != "blank"),
               default=-1) + 1
    rows = [r[:last] for r in rows]
    skipped = min(header_row - 1, len(rows))
    other = []
    for name in values_book.sheetnames:
        if name != sheet and any(c.value is not None for r in values_book[name].iter_rows()
                                 for c in r):
            other.append(name)
    return {"rows": rows[skipped:], "formulas": formulas, "errors": errors,
            "trimmed_rows": trimmed_rows, "trimmed_columns": width - last,
            "skipped_rows": skipped, "other_sheets": other}


def make_names(name: str) -> str:
    """R's make.names for one name: what read.csv's check.names makes of it."""
    made = re.sub(r"[^A-Za-z0-9._]", ".", name)
    if not re.match(r"[A-Za-z]|\.(?![0-9])", made):
        made = "X" + made
    return made


def canonical_number(value: float) -> str:
    """A number rendered at 15 significant digits, as R's write.csv does."""
    return format(float(value), ".15g")


def cell_text(kind: str, value: Any, na: str | None) -> str:
    """A typed cell's canonical rendering, for headers and reorder checks."""
    if kind in ("blank", "error"):
        return na or ""
    if kind == "boolean":
        return "TRUE" if value else "FALSE"
    if kind == "number":
        return canonical_number(value)
    if kind in ("date", "datetime", "time"):
        return value.isoformat(sep=" ") if kind == "datetime" else value.isoformat()
    if kind == "formula":
        return cell_text(*(("blank", None) if value is None else (
            "number", value) if isinstance(value, (int, float)) and not isinstance(
                value, bool) else ("string", str(value))), na)
    return str(value)


def wall_clock(text: str) -> tuple[datetime, str | None] | None:
    """An ISO datetime's wall-clock fields and its offset text, if it is one."""
    match = DATETIME_RE.fullmatch(text)
    if not match:
        return None
    year, month, day, hour, minute, second, fraction, offset = match.groups()
    micro = int(round(float(fraction) * 1_000_000)) if fraction else 0
    return datetime(int(year), int(month), int(day), int(hour), int(minute),
                    int(second or 0), micro), offset


def compare_cell(kind: str, value: Any, field: str, na: str | None,
                 zone: str | None) -> str:
    """How an output field renders a typed workbook cell (spec §11 table).

    Returns:
        ``match`` (the canonical rendering), ``rendering`` (the same value,
        another rendering: cleared but counted), ``missing-marker``,
        ``whitespace``, ``formula``, ``error``, or ``changed``.
    """
    if kind == "formula":
        return "formula"
    if kind == "error":
        return "error"
    if kind == "blank":
        if field == "" or (na is not None and field == na):
            return "match"
        return "missing-marker" if field in MISSING_MARKERS else "changed"
    if kind == "string":
        if field == value:
            return "match"
        if field.strip() == value.strip():
            return "whitespace"
        if field in MISSING_MARKERS and value in MISSING_MARKERS:
            return "missing-marker"
        return "changed"
    if kind == "boolean":
        return "match" if field == ("TRUE" if value else "FALSE") else "changed"
    if kind == "number":
        if field == canonical_number(value):
            return "match"
        if NUMBER_RE.fullmatch(field) and canonical_number(float(field)) == canonical_number(
                value):
            return "rendering"
        return "missing-marker" if field in MISSING_MARKERS else "changed"
    if kind == "date":
        return "match" if field == value.isoformat() else "changed"
    if kind == "datetime":
        parsed = wall_clock(field)
        if parsed is None:
            return "changed"
        clock, offset = parsed
        if zone is None:
            # No declared zone: compare the wall-clock fields, and any zone
            # the output asserts is a value change (spec §11, D-4).
            if offset is not None:
                return "changed"
            return "match" if clock == value else "changed"
        tz = ZoneInfo(zone)
        source_instant = value.replace(tzinfo=tz)
        if offset is None:
            field_instant = clock.replace(tzinfo=tz)
        else:
            sign = 1 if offset[0] == "+" else -1
            hours, minutes = (0, 0) if offset == "Z" else (
                int(offset[1:3]), int(offset[-2:]))
            field_instant = clock.replace(tzinfo=timezone(sign * timedelta(
                hours=hours, minutes=minutes)))
        if field_instant != source_instant:
            return "changed"
        return "match" if offset is None and clock == value else "rendering"
    if kind == "time":
        return "match" if field == value.isoformat() else "changed"
    return "changed"


def compare_text_field(source: str, field: str) -> str:
    """How an output field renders a source text field (text to text)."""
    if field == source:
        return "match"
    if NUMBER_RE.fullmatch(source) and NUMBER_RE.fullmatch(field) and float(source) == float(
            field):
        return "numeric-equivalent"
    if field.strip() == source.strip():
        return "whitespace"
    if field in MISSING_MARKERS and source in MISSING_MARKERS:
        return "missing-marker"
    return "changed"


def compare_conversion(target_dir: Path, item: dict, final_pre: dict[str, str] | None,
                       sealed_outputs: dict[str, dict[str, str]]) -> tuple[Issue | None, dict]:
    """The lane's check of one declared conversion (spec §11).

    Args:
        target_dir: The attempt directory.
        item: The conversion wrapper's manifest entry.
        final_pre: The final run's pre snapshot, or None without run records.
        sealed_outputs: Each run's sealed outputs, ``{run: {path: sha256}}``.

    Returns:
        ``(issue, report)``: no issue when every value is unchanged under §11's
        rules; otherwise a ``conversion-differs`` issue with the counts and the
        first differing cells, raw and typed. The report holds the counts.
    """
    declared = item.get("conversion") if isinstance(item.get("conversion"), dict) else {}
    wrapper_rel = item["path"]
    evidence = file_digests(target_dir, wrapper_rel, declared.get("input"),
                            declared.get("output"))
    evidence["declaration"] = json_digest(declared)
    report: dict[str, Any] = {"wrapper": wrapper_rel, "input": declared.get("input"),
                              "output": declared.get("output"), "counts": {},
                              "differences": [], "notes": [], "cleared": False}

    def issue(reason: str, note: bool = True) -> tuple[Issue, dict]:
        if note:
            report["notes"].append(reason)
        return Issue.flag("conversion-differs", wrapper_rel, f"conversion wrapper "
                          f"{wrapper_rel} ({declared.get('input')} to "
                          f"{declared.get('output')}): {reason}. A conversion counts only when "
                          f"every value is unchanged (amendment 3 §7(d)); a human rules "
                          f"admissible, where nothing changed in value, or fail-and-uplift",
                          files=evidence), report

    if not declared.get("input") or not declared.get("output"):
        return issue("the wrapper declares no conversion input and output")
    if declared.get("timezone") and not declared.get("timezone_evidence"):
        return issue("a timezone is declared without the evidence for it")
    source_path = resolve_stored(target_dir, declared["input"])
    output_path = inside(target_dir, declared["output"])
    if source_path is None or not source_path.is_file():
        return issue(f"the input {declared['input']} is missing")
    if output_path is None or not output_path.is_file():
        return issue(f"the output {declared['output']} is missing")
    # The compared output must be the one a credited run used.
    output_rel = declared["output"]
    output_digest = sha256_file(output_path)
    in_tree = final_pre is not None and final_pre.get(output_rel) == output_digest
    collected = output_rel.startswith("outputs/") and any(
        output_rel == f"outputs/{run}/{path}" and digest == output_digest
        for run, paths in sealed_outputs.items() for path, digest in paths.items())
    if final_pre is not None and not (in_tree or collected):
        return issue(f"the output {output_rel} is not in the final run's input tree, nor a "
                     f"sealed run output, at its current digest: the run did not use it")
    source_suffix = source_path.suffix.lower()
    output_delimiter = TEXT_DELIMITERS.get(output_path.suffix.lower())
    if output_delimiter is None:
        return issue(f"the output format {output_path.suffix or '(none)'} is unsupported")
    na = declared.get("na")
    zone = declared.get("timezone")
    if zone:
        try:
            ZoneInfo(zone)
        except (ZoneInfoNotFoundError, ValueError):
            return issue(f"the declared timezone {zone!r} is unknown")
    try:
        output_rows = read_delimited(output_path.read_bytes(),
                                     declared.get("output_encoding", "utf-8"), output_delimiter)
    except (UnicodeDecodeError, LookupError) as exc:
        report["counts"]["decoding failures"] = 1
        return issue(f"the output does not decode as declared ({exc})")
    counts: dict[str, int] = {}

    def count(key: str, by: int = 1) -> None:
        if by:
            counts[key] = counts.get(key, 0) + by

    workbook = source_suffix in WORKBOOK_SUFFIXES
    if workbook:
        if not declared.get("sheet"):
            return issue("a workbook input needs its sheet declared")
        try:
            book = read_workbook(source_path, declared["sheet"], declared.get("range"),
                                 int(declared.get("header_row", 1)))
        except LaneError as exc:
            return issue(str(exc))
        except Exception as exc:  # openpyxl raises many types for a bad file
            return issue(f"the workbook could not be read ({type(exc).__name__}: {exc})")
        source_rows: list[list[tuple[str, Any]]] = book["rows"]
        count("formulae", book["formulas"])
        count("error values", book["errors"])
        count("trailing empty rows trimmed", book["trimmed_rows"])
        count("trailing empty columns trimmed", book["trimmed_columns"])
        if book["other_sheets"]:
            count("unchecked sheets", len(book["other_sheets"]))
            report["notes"].append(f"non-empty sheets not checked: {book['other_sheets']}")
    elif source_suffix in TEXT_DELIMITERS:
        try:
            text_rows = read_delimited(source_path.read_bytes(),
                                       declared.get("encoding", "utf-8"),
                                       TEXT_DELIMITERS[source_suffix])
        except (UnicodeDecodeError, LookupError) as exc:
            report["counts"]["decoding failures"] = 1
            return issue(f"the input does not decode as {declared.get('encoding', 'UTF-8')} "
                         f"({exc})")
        source_rows = [[("text", text) for text, _ in row] for row in text_rows]
    else:
        return issue(f"the input format {source_suffix or '(none)'} is unsupported")

    # 1-2. Dimensions, with rows in another order reported as such.
    source_header, source_data = (source_rows[0], source_rows[1:]) if source_rows else ([], [])
    output_header, output_data = (output_rows[0], output_rows[1:]) if output_rows else ([], [])
    width = max((len(r) for r in source_rows), default=0)
    out_width = max((len(r) for r in output_rows), default=0)
    dimensions_equal = (len(source_data) == len(output_data) and width == out_width)
    if not dimensions_equal:
        report["notes"].append(f"dimensions differ: {len(source_data)} x {width} in, "
                               f"{len(output_data)} x {out_width} out")
    # 3. Headers, on their own line.
    rendered = [text if kind == "text" else cell_text(kind, text, None)
                for kind, text in source_header]
    output_names = [text for text, _ in output_header]
    headers_exact = rendered == output_names
    if not headers_exact:
        rewrites = [n for s, n in zip(rendered, output_names) if s != n and make_names(s) == n]
        report["notes"].append(f"headers differ ({len(rewrites)} R make.names rewrite(s))")
        count("header differences", sum(1 for s, n in zip(rendered, output_names) if s != n)
              + abs(len(rendered) - len(output_names)))
    # 4. Cells, position by position.
    collisions: dict[int, list[tuple[bool, bool]]] = {}
    for r, (source_row, output_row) in enumerate(zip(source_data, output_data), start=2):
        for c in range(max(len(source_row), len(output_row))):
            kind, value = source_row[c] if c < len(source_row) else ("blank", None)
            field, quoted = output_row[c] if c < len(output_row) else ("", False)
            outcome = (compare_text_field(value, field) if kind == "text"
                       else compare_cell(kind, value, field, na, zone))
            # A typed source's literal that a reader would take for the
            # marker; a text-to-text conversion writes no marker.
            literal = kind == "string" and (value == "" or (na is not None and value == na))
            if literal or kind == "blank":
                collisions.setdefault(c, []).append((literal, quoted))
            if outcome == "match":
                continue
            count({"rendering": "same value, other rendering",
                   "numeric-equivalent": "numeric-equivalent fields",
                   "missing-marker": "missing-marker changes",
                   "whitespace": "whitespace-only differences", "formula": "formulae",
                   "error": "error values", "changed": "other value changes"}[outcome],
                  0 if outcome in ("formula", "error") else 1)
            if outcome != "rendering" and len(report["differences"]) < DIFFERENCES_SHOWN:
                report["differences"].append({"row": r, "column": c + 1, "type": kind,
                                              "source": str(value), "output": field,
                                              "outcome": outcome})
    reordered = False
    if dimensions_equal and any(k in counts for k in ("other value changes",
                                                      "missing-marker changes")):
        def norm(text: str) -> str:
            return canonical_number(float(text)) if NUMBER_RE.fullmatch(text) else text
        reordered = (Counter(tuple(norm(v if k == "text" else cell_text(k, v, na))
                                   for k, v in row) for row in source_data)
                     == Counter(tuple(norm(f) for f, _ in row) for row in output_data))
        if reordered:
            report["notes"].append("the rows are the same multiset in another order")
    # Missing-marker collisions: a column where the marker also occurs as a
    # literal source value (spec §11, A-1); cleared only by a reader that the
    # lane can confirm keeps the two apart.
    reader = declared.get("reader") or {}
    confirmable = (reader.get("function") in QUOTE_AWARE_READERS
                   and reader.get("quoted_na") is False)
    colliding = [c for c, seen in collisions.items() if any(lit for lit, _ in seen)]
    unresolved = [c for c in colliding
                  if not (confirmable and all(q == lit for lit, q in collisions[c]))]
    count("missing-marker collisions", len(unresolved))
    if colliding and not unresolved:
        report["notes"].append(f"missing-marker collisions in {len(colliding)} column(s), "
                               f"kept apart by {reader['function']} (quoted_na = FALSE)")
    report["counts"] = counts
    scope = declared.get("scope")
    sheets_ok = "unchecked sheets" not in counts or scope in ("sheet", "range")
    if scope and "unchecked sheets" in counts:
        report["notes"].append(f"identity is claimed for the checked {scope} only")
    cleared = (dimensions_equal and headers_exact and sheets_ok
               and not any(k in counts for k in (
                   "other value changes", "missing-marker changes", "whitespace-only "
                   "differences", "numeric-equivalent fields", "formulae", "error values",
                   "missing-marker collisions", "header differences")))
    report["cleared"] = cleared
    if cleared:
        return None, report
    shown = "; ".join(f"{n} {k}" for k, n in sorted(counts.items()) if not k.startswith(
        "trailing") and k != "same value, other rendering")
    first = "; ".join(f"row {d['row']} column {d['column']} ({d['type']}): "
                      f"{d['source']!r} -> {d['output']!r}" for d in report["differences"])
    parts = [shown or "", "; ".join(report["notes"]), f"first differences: {first}"
             if first else ""]
    return issue(". ".join(p for p in parts if p) or "the values could not be confirmed",
                 note=False)


def legacy_allowed(target_dir: Path, allowlist: Path | None = None) -> bool:
    """True when the attempt is listed as executed before gate 1.1.

    The legacy bypass exists only for those attempts (PR #7 review); a new run
    can never use it.
    """
    listing = allowlist or expand(LEGACY_ATTEMPTS_FILE)
    if not listing.is_file():
        return False
    entries = (yaml.safe_load(listing.read_text(encoding="utf-8")) or {}).get("attempts") or []
    return any(entry and expand(str(entry)).resolve() == target_dir.resolve()
               for entry in entries)


@digest_snapshot()  # one scope per gate check: never shared with a snapshot
def check_code_integrity(target_dir: Path, manifest_path: Path, schema: dict,
                         comparison: dict | None = None, plan_slug: str | None = None,
                         legacy: bool = False, anchor_root: Path | None = None,
                         launch_commit: str | None = None) -> dict:
    """Verify the authors' code manifest against the attempt directory.

    The rule (Shawn, 2026-10-04): authors' files are hashed at retrieval and
    the executed copies checked byte-identical; any difference is a declared
    wrapper or a flagged edit. The gate **fails** on anything that would hide
    a difference:

    - a missing or invalid manifest, or missing execution snapshots;
    - an executed copy that differs without a declaration;
    - a pristine copy or archive member that no longer matches its hash;
    - a provenance anchor that contradicts the original;
    - code that changed between the run and the gate, changed during the run,
      or appeared during it undeclared;
    - a code file anywhere in the attempt (``outputs/`` included) that is
      neither an authors' file nor a declared wrapper;
    - a wrapper that loads code the run generated.

    It **flags** (the gate still passes, and the flag goes to the human queue)
    what is declared or unverifiable and needs a human ruling: each declared
    edit with its computed size; a credited target resting on one; a wrapper
    that embeds authors' lines (a heuristic); a run that executed no authors'
    file; an original with no pristine copy, or with no verified provenance
    anchor; a transcribed original; generated code; and a conversion whose
    value-identity evidence is not valid.

    ``pass`` means only that every code file is accounted for. Whether a
    flagged edit is mechanics or fail-and-uplift is a human ruling, recorded
    before the result enters study data, and a repaired result never counts
    toward coverage. What the gate cannot see (wrapper semantics, dynamic
    evaluation, content fetched into the image) is listed under
    ``review_obligations`` for the adversarial reviewer.

    Args:
        target_dir: The attempt directory.
        manifest_path: The manifest (normally ``<attempt>/authors-code-manifest.json``).
        schema: The full authors-code-manifest schema.
        comparison: The parsed ``comparison.json``, to cross-check credited
            targets; None skips that check.
        plan_slug: The plan's paper slug, which the manifest must name.
        legacy: The attempt is a listed legacy attempt (``legacy_allowed``):
            a missing manifest or snapshots warn instead of failing, and the
            result is marked ineligible for the current gate.
        anchor_root: The repository whose committed records anchors name
            (default: this repository).
        launch_commit: The run's launch commit. Anchors verify only against
            records that existed, unchanged, at it.

    Returns:
        ``{status, errors, flags, warnings, review_obligations, anchors,
        snapshots, eligible_for_current_gate, manifest_sha256, originals,
        executed, wrappers}``. ``status`` is ``fail`` (errors), ``flagged``
        (flags only), ``identical`` (every executed copy byte-identical and
        independently anchored), ``no-authors-code``, or ``not-checked``.
    """
    repo_root = anchor_root or REPO_ROOT
    errors: list[str] = []
    flags: list[str] = []
    warnings: list[str] = []
    obligations: list[str] = []
    result: dict[str, Any] = {"manifest": display_path(manifest_path), "errors": errors,
                              "flags": flags, "warnings": warnings,
                              "review_obligations": obligations, "anchors": {},
                              "snapshots": {}, "eligible_for_current_gate": not legacy,
                              "originals": 0, "executed": [], "wrappers": 0,
                              "manifest_sha256": None}
    if not manifest_path.is_file():
        message = (f"authors' code manifest missing: {manifest_path.name} — hash every "
                   f"authors' file at retrieval (preparation prompt section 1.0.2)")
        if legacy:
            warnings.append(message + " [listed legacy attempt: integrity not checked; "
                                      "ineligible for the current gate]")
            result["status"] = "not-checked"
        else:
            errors.append(message)
            result["status"] = "fail"
        return result
    result["manifest_sha256"] = sha256_file(manifest_path)
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append(f"authors' code manifest does not parse: {exc}")
        result["status"] = "fail"
        return result
    problems = schema_problems(manifest, schema)
    if problems:
        errors.extend(f"authors' code manifest {p}" for p in problems)
        result["status"] = "fail"
        return result
    if plan_slug is not None and manifest["paper_slug"] != plan_slug:
        errors.append(f"manifest paper_slug {manifest['paper_slug']!r} != plan {plan_slug!r}")

    originals = manifest["originals"]
    executed = manifest["executed"]
    wrappers = manifest["wrappers"]
    result["originals"], result["wrappers"] = len(originals), len(wrappers)
    if not originals:
        if not manifest.get("no_authors_code_reason"):
            errors.append("manifest lists no originals and gives no no_authors_code_reason")
        if executed:
            errors.append("manifest lists executed copies but no originals")

    # -- Originals: unique ids; pristine copies and archive members re-hashed;
    #    then each anchored to an independent, committed record.
    by_id: dict[str, dict] = {}
    original_bytes: dict[str, bytes] = {}
    pristine_paths: set[Path] = set()
    for item in originals:
        oid = item["id"]
        if oid in by_id:
            errors.append(f"duplicate original id {oid!r}")
            continue
        by_id[oid] = item
        errors_before = len(errors)
        if item.get("local_copy"):
            local = inside(target_dir, item["local_copy"])
            if local is None:
                errors.append(f"original {oid!r}: local_copy must be a relative path inside "
                              f"the attempt directory")
            elif not local.is_file():
                errors.append(f"original {oid!r}: local_copy missing: {item['local_copy']}")
            else:
                pristine_paths.add(local)
                data = local.read_bytes()
                if hashlib.sha256(data).hexdigest() != item["sha256"]:
                    errors.append(f"original {oid!r}: pristine copy {item['local_copy']} no "
                                  f"longer matches its retrieval hash — it was changed after "
                                  f"retrieval")
                else:
                    original_bytes[oid] = data
        archive = item.get("archive") or {}
        if archive.get("path"):
            archive_path = resolve_stored(target_dir, archive["path"])
            if archive_path is None:
                errors.append(f"original {oid!r}: archive path must be inside the attempt "
                              f"directory or the corpus store ({CORPUS_PREFIX}…)")
            elif not archive_path.is_file():
                warnings.append(f"original {oid!r}: archive {archive['path']} not kept; "
                                f"the retrieval hash is self-reported")
            else:
                if archive.get("sha256") and sha256_file(archive_path) != archive["sha256"]:
                    errors.append(f"original {oid!r}: archive {archive['path']} does not "
                                  f"match its recorded sha256")
                try:
                    member = archive_member_bytes(archive_path, archive["member"])
                except (KeyError, ValueError, OSError) as exc:
                    errors.append(f"original {oid!r}: archive member {archive['member']!r} "
                                  f"unreadable: {exc}")
                else:
                    if hashlib.sha256(member).hexdigest() != item["sha256"]:
                        errors.append(f"original {oid!r}: archive member "
                                      f"{archive['member']!r} does not hash to the recorded "
                                      f"retrieval sha256")
                    else:
                        original_bytes.setdefault(oid, member)
        if oid not in original_bytes and len(errors) == errors_before:
            flags.append(Issue.flag(
                "no-pristine-copy", str(oid), f"original {oid!r} has no pristine copy in the "
                f"attempt directory: byte identity rests on the recorded hash alone, and no "
                f"wrapper can be checked for an inlined copy of it",
                files={"original": str(item["sha256"])}))
        state, anchor_errors, anchor_flags = verify_anchor(
            item, target_dir, repo_root, manifest["paper_slug"], original_bytes.get(oid),
            launch_commit)
        result["anchors"][oid] = state
        errors.extend(anchor_errors)
        flags.extend(anchor_flags)
        if item.get("derivation"):
            flags.append(Issue.flag(
                "transcription", str(oid), f"original {oid!r} is a "
                f"{item['derivation']['method']} of "
                f"{item['derivation'].get('from') or 'another file'}: a deterministic "
                f"transcription shows repeatability, not fidelity to the page, so a human "
                f"checks the consequential code against the source",
                files={"original": str(item["sha256"]),
                       "derivation": json_digest(item["derivation"])}))

    # -- Executed copies: byte-identical, or a declared (flagged) edit.
    original_hashes = {item["sha256"]: oid for oid, item in by_id.items()}
    credited = {}
    if isinstance(comparison, dict):
        credited = {t.get("target_id"): t.get("outcome")
                    for t in comparison.get("targets") or [] if isinstance(t, dict)
                    and t.get("testable") is not False
                    and t.get("outcome") in REPRODUCED_OUTCOMES}
    executed_paths: set[Path] = set()
    for item in executed:
        record: dict[str, Any] = {"path": item["path"], "original": item["original"]}
        result["executed"].append(record)
        path = inside(target_dir, item["path"])
        if path is None:
            errors.append(f"executed {item['path']!r}: must be a relative path inside the "
                          f"attempt directory")
            continue
        if path in executed_paths:
            errors.append(f"executed {item['path']!r} listed twice")
        executed_paths.add(path)
        source = by_id.get(item["original"])
        if source is None:
            errors.append(f"executed {item['path']!r}: original {item['original']!r} is not "
                          f"in originals")
            continue
        if not path.is_file():
            errors.append(f"executed copy missing: {item['path']}")
            continue
        data = path.read_bytes()
        digest = hashlib.sha256(data).hexdigest()
        record["sha256"] = digest
        record["identical"] = digest == source["sha256"]
        edit = item.get("declared_edit")
        if record["identical"]:
            if edit:
                warnings.append(f"executed {item['path']!r} declares an edit but is "
                                f"byte-identical to {item['original']!r}")
            continue
        if not edit:
            errors.append(f"UNDECLARED DIFFERENCE: {item['path']} (sha256 {digest[:12]}…) is "
                          f"not byte-identical to original {item['original']!r} (sha256 "
                          f"{source['sha256'][:12]}…) and declares no edit — mechanics belong "
                          f"in a wrapper, and any edit to an authors' file must be declared")
            continue
        size = (lines_changed(original_bytes[item["original"]], data)
                if item["original"] in original_bytes else None)
        record["declared_edit"] = edit
        record["lines_changed"] = size
        size_text = (f"{size['changed']} line(s) changed (computed)" if size
                     else "size not computable (no pristine copy)")
        if size and "lines_changed" in edit and edit["lines_changed"] != size["changed"]:
            size_text += f"; declared {edit['lines_changed']} — the computed value governs"
        edit_evidence = {item["path"]: digest, "original": str(source["sha256"]),
                         "declared_edit": json_digest(edit)}
        flags.append(Issue.flag(
            "edited-copy", item["path"], f"{item['path']} differs from original "
            f"{item['original']!r}; {size_text}; kind {edit.get('kind', 'unstated')}; affected "
            f"targets {edit['affected_targets'] or 'none stated'}; declared: "
            f"{edit['summary']}. Declaring an edit does not make a repaired result creditable",
            prefix=FLAG_EDIT_PREFIX, targets=edit["affected_targets"], files=edit_evidence))
        for target in edit["affected_targets"]:
            if target in credited:
                flags.append(Issue.flag(
                    "credited-edited-target", f"{target}@{item['path']}", f"target {target} "
                    f"is credited ({credited[target]}) but rests on the flagged edit to "
                    f"{item['path']} — a repaired result never counts toward coverage or the "
                    f"verdict (queued amendment 3, item 7(d))", targets=(target,),
                    files=edit_evidence))

    if originals and not executed:
        flags.append(Issue.flag(
            "no-executed-original", "attempt", "no authors' file is listed as executed: every "
            "result rests on the reproducer's own code (a re-implementation is not the "
            "authors' code run unmodified)",
            files={manifest_path.name: str(result["manifest_sha256"])}))

    # -- Wrappers: exist, are separate files, and do not inline authors' code.
    wrapper_paths: set[Path] = set()
    conversions: list[dict] = []
    generated_paths: set[Path] = set()
    for item in wrappers:
        path = inside(target_dir, item["path"])
        if path is None:
            errors.append(f"wrapper {item['path']!r}: must be a relative path inside the "
                          f"attempt directory")
            continue
        if path in wrapper_paths or path in generated_paths:
            errors.append(f"wrapper {item['path']!r} listed twice")
        (generated_paths if item["role"] == "generated" else wrapper_paths).add(path)
        if path in executed_paths or path in pristine_paths:
            errors.append(f"{item['path']} is declared both as a wrapper and as an authors' "
                          f"file")
            continue
        if not path.is_file():
            errors.append(f"declared wrapper missing: {item['path']}")
            continue
        data = path.read_bytes()
        if hashlib.sha256(data).hexdigest() in original_hashes:
            errors.append(f"wrapper {item['path']} is byte-identical to authors' original "
                          f"{original_hashes[hashlib.sha256(data).hexdigest()]!r} — declare "
                          f"it under executed")
            continue
        if item["role"] == "generated":
            generated_text = data.decode("utf-8", errors="replace")
            inlined = [oid for oid, original in original_bytes.items()
                       if len(substantive_lines(generated_text) & substantive_lines(
                           original.decode("utf-8", errors="replace"))) >= EMBEDDED_LINES_FLAG]
            if inlined:
                # An edited copy of an authors' file declared as generated
                # (Fable review, P3-3).
                errors.append(f"{item['path']} is declared generated but shares "
                              f"{EMBEDDED_LINES_FLAG}+ substantive lines with authors' "
                              f"original(s) {inlined}: an edited copy is not generated code")
            flags.append(Issue.flag(
                "generated-code", item["path"], f"{item['path']} is code the run generated: "
                f"the gate cannot show it was not executed, so a human confirms what made it "
                f"and that nothing ran it", files={item["path"]: hashlib.sha256(
                    data).hexdigest()}))
            continue
        if item["role"] == "conversion":
            conversions.append(item)
        text = data.decode("utf-8", errors="replace")
        mine = substantive_lines(text)
        for oid, original in original_bytes.items():
            shared = mine & substantive_lines(original.decode("utf-8", errors="replace"))
            if len(shared) >= EMBEDDED_LINES_FLAG:
                flags.append(Issue.flag(
                    "wrapper-embeds-original", f"{item['path']}~{oid}", f"wrapper "
                    f"{item['path']} embeds {len(shared)} substantive line(s) of authors' "
                    f"original {oid!r} (a heuristic for verbatim inlining) — inlined authors' "
                    f"code is an edited copy unless the original file is what runs",
                    files={item["path"]: hashlib.sha256(data).hexdigest()}))
        wrapper_file = {item["path"]: hashlib.sha256(data).hexdigest()}
        if DYNAMIC_EVAL_RE.search(text):
            obligations.append(Issue.obligation(
                "dynamic-evaluation", item["path"], f"{item['path']} evaluates code "
                f"dynamically (parse, eval, source of a computed path, or exec): confirm it "
                f"evaluates only the declared authors' files, unmodified", files=wrapper_file))
        if PATCHING_RE.search(text):
            obligations.append(Issue.obligation(
                "in-memory-patching", item["path"], f"{item['path']} can patch functions in "
                f"memory (body, formals, trace, assignInNamespace, unlockBinding, or <<-): "
                f"confirm it changes no function of the authors' code", files=wrapper_file))
        if "dockerfile" in path.name.lower():
            if DOCKER_FETCH_RE.search(text):
                obligations.append(Issue.obligation(
                    "docker-fetch", item["path"], f"{item['path']} brings content into the "
                    f"image from outside the attempt directory: confirm none of it is "
                    f"analysis code", files=wrapper_file))
            if DOCKER_EDIT_RE.search(text):
                obligations.append(Issue.obligation(
                    "docker-build-edit", item["path"], f"{item['path']} edits files at build "
                    f"time (sed, patch, perl -i, awk, tee, a redirect, or a heredoc): confirm "
                    f"it edits no authors' file and no R start-up file", files=wrapper_file))
            if DOCKER_COPY_RE.search(text):
                obligations.append(Issue.obligation(
                    "docker-copy", item["path"], f"{item['path']} copies attempt files into "
                    f"the image: confirm the run executes the mounted, checked tree and not "
                    f"the image's copy", files=wrapper_file))

    # -- Static start-up checks (spec §10): what would skip, evade, or
    #    undo the lane hook. Errors in a wrapper; in an original, which
    #    cannot be changed, the hook-integrity patterns are flags.
    defined: dict[str, str] = {}
    for oid, data in original_bytes.items():
        names = {Path(n).name.lower() for n in (by_id[oid].get("local_copy"),
                                               (by_id[oid].get("archive") or {}).get("member"))
                 if n} | {Path(r["path"]).name.lower() for r in result["executed"]
                          if r.get("original") == oid}
        if not any(Path(n).suffix in (".r", ".rmd", ".qmd", ".rnw") or n == ".rprofile"
                   for n in names):
            continue
        text = data.decode("utf-8", errors="replace")
        for name in FUNCTION_DEF_RE.findall(text):
            defined.setdefault(name, oid)
        hit = HOOK_INTEGRITY_RE.search(text)
        if hit:
            flags.append(Issue.flag(
                "hook-integrity", str(oid), f"original {oid!r} contains {hit.group(0).strip()!r}, "
                f"which can undo or evade the lane hook: confirm it does not, in this run",
                files={"original": str(by_id[oid]["sha256"])}))
    root_dir = target_dir.resolve()
    shadowing_sources = sorted(wrapper_paths) + [
        p for p in [(target_dir / ".Rprofile").resolve()]
        if p.is_file() and p not in wrapper_paths]
    for path in shadowing_sources:
        if not path.is_file():
            continue
        rel_text = path.relative_to(root_dir).as_posix()
        text = path.read_text(encoding="utf-8", errors="replace")
        evidence = file_digests(target_dir, rel_text)
        for name in sorted(defined):
            pattern = (rf"(?<![\w.$@]){re.escape(name)}\s*<<?-"
                       rf"|^\s*{re.escape(name)}\s*=(?!=)")
            if re.search(pattern, text, re.MULTILINE):
                flags.append(Issue.flag(
                    "function-shadowing", f"{rel_text}~{name}", f"{rel_text} assigns "
                    f"{name}, which original {defined[name]!r} defines as a function: the run "
                    f"may use this definition instead of the authors'", files=evidence))
        if path not in wrapper_paths:
            continue
        for pattern, why in ((SKIP_HOOK_RE, "which skips the lane hook"),
                             (STDIN_SCRIPT_RE, "a script on standard input, which no load "
                                               "event covers (use R -f file)"),
                             (LITTLER_RE, "littler, which starts R without the front end "
                                          "(use Rscript)"),
                             (CMD_CHECK_RE, "R CMD check, which is not a reproduction "
                                            "action"),
                             (HOOK_INTEGRITY_RE, "which can undo or evade the lane hook")):
            hit = pattern.search(text)
            if hit:
                errors.append(f"wrapper {rel_text}: {hit.group(0).strip()!r}, {why}")
        hit = STARTUP_FLAG_RE.search(text)
        if hit:
            flags.append(Issue.flag(
                "startup-option", f"{rel_text}~{hit.group(1)}", f"wrapper {rel_text} starts R "
                f"with --{hit.group(1)}, which changes what R reads at start-up: confirm the "
                f"run's environment is the one the authors' code expects", files=evidence))
        if "dockerfile" in path.name.lower() and DOCKER_STARTUP_RE.search(text):
            obligations.append(Issue.obligation(
                "docker-startup-files", rel_text, f"{rel_text} touches R's start-up files "
                f"(Rprofile.site, Renviron.site, /etc/R) or R's bin directory, where code "
                f"runs before the lane hook: confirm what it changes", files=evidence))
    renviron = target_dir / ".Renviron"
    if renviron.is_file():
        hit = RENVIRON_STARTUP_RE.search(renviron.read_text(encoding="utf-8",
                                                              errors="replace"))
        if hit:
            flags.append(Issue.flag(
                "renviron-startup", hit.group(1), f"the project .Renviron sets {hit.group(1)}, "
                f"which names start-up code: the hook sources a profile it names in place of "
                f"the project profile, so confirm what it is",
                files=file_digests(target_dir, ".Renviron")))

    # -- Sealed run records (gate 1.3): the lane, not the executor, recorded
    #    each run. Code a run generated joins the generated files: flagged,
    #    checked for inlined authors' code, and never loadable (spec §3).
    lane = check_run_records(target_dir, launch_commit, repo_root)
    collected_paths: set[Path] = set()
    if lane is not None:
        result["runs"] = {k: lane[k] for k in ("final_run", "credited_runs", "runs",
                                               "outputs")}
        errors.extend(lane["errors"])
        flags.extend(lane["flags"])
        warnings.extend(lane["warnings"])
        obligations.extend(lane["obligations"])
        collected_paths = {(target_dir / rel).resolve() for rel in lane["collected"]}
        for rel_text in lane["generated"]:
            path = (target_dir / rel_text).resolve()
            generated_paths.add(path)
            generated_text = path.read_text(encoding="utf-8", errors="replace")
            inlined = [oid for oid, original in original_bytes.items()
                       if len(substantive_lines(generated_text) & substantive_lines(
                           original.decode("utf-8", errors="replace"))) >= EMBEDDED_LINES_FLAG]
            if inlined:
                errors.append(f"{rel_text}, generated by the run, shares {EMBEDDED_LINES_FLAG}+ "
                              f"substantive lines with authors' original(s) {inlined}: an "
                              f"edited copy is not generated code")
            flags.append(Issue.flag(
                "generated-code", rel_text, f"{rel_text} is code the run generated: never "
                f"loadable, so a human confirms what made it and that nothing ran it",
                files=file_digests(target_dir, rel_text)))
        # The account of every load the credited runs made (spec §8), bound
        # to content the gate computes itself.
        if lane["final_run"] is not None:
            catalogue = load_catalogue(target_dir, by_id, original_bytes, result["executed"],
                                       wrappers, lane["generated"])
            account = account_loads(target_dir, lane["credited_records"], catalogue,
                                    lane["final_run"])
            errors.extend(account["errors"])
            flags.extend(account["flags"])
            obligations.extend(account["obligations"])
            warnings.extend(account["warnings"])
            result["account"] = {k: account[k] for k in ("originals_loaded", "runs")}
        if lane["final_pre"] is not None:
            in_run = {item["path"] for item in wrappers
                      if item["role"] in ("wrapper", "tooling")}
            for path in executed_paths | {inside(target_dir, rel) for rel in in_run} - {None}:
                rel_text = path.relative_to(target_dir.resolve()).as_posix()
                if rel_text not in lane["final_pre"]:
                    errors.append(f"{rel_text} is declared as run code but was not in the final "
                                  f"run's input tree ({lane['final_run']})")

    # -- Conversions (spec §11): the lane compares each declared conversion's
    #    files itself; an executor-written record is retired.
    result["conversions"] = []
    for item in conversions:
        if item.get("value_identity_check"):
            warnings.append(f"conversion wrapper {item['path']}: value_identity_check is "
                            f"retired and ignored; the gate compares the files itself")
        issue, conversion_report = compare_conversion(
            target_dir, item, lane["final_pre"] if lane is not None else None,
            lane["outputs"] if lane is not None else {})
        result["conversions"].append(conversion_report)
        if issue is not None:
            flags.append(issue)

    # -- Code paths named by wrappers (and loaded by executed authors' files) must
    #    be declared, and never generated code. A file passed to a loader is
    #    code whatever its suffix (Fable review, P1-1).
    declared_paths = executed_paths | pristine_paths | wrapper_paths
    tree_files, symlink_issues = walk_tree(target_dir)
    errors.extend(symlink_issues)
    by_basename: dict[str, list[Path]] = {}
    for path in tree_files:
        by_basename.setdefault(path.name, []).append(path.resolve())
    root = target_dir.resolve()
    loaded_as_code: set[str] = set()

    def resolve_reference(literal: str) -> Path | None:
        """Resolve a referenced path: container prefixes stripped, then the
        tree, then a unique basename (after ``setwd``, Fable review P3-5)."""
        rel = re.sub(r"^(?:/project/|/work/|/home/\w+/|\./)+", "", literal)
        named = inside(target_dir, rel)
        if named is not None and named.is_file():
            return named
        matches = by_basename.get(Path(rel).name, [])
        if len(matches) > 1:
            # A basename shared by a pristine copy and its executed copy
            # names the declared executed copy.
            matches = ([m for m in matches if m in executed_paths]
                       or [m for m in matches if m in declared_paths])
        return matches[0] if len(matches) == 1 else None

    for source_path in sorted(wrapper_paths | executed_paths):
        if not source_path.is_file():
            continue
        text = source_path.read_text(encoding="utf-8", errors="replace")
        is_wrapper = source_path in wrapper_paths
        shell = source_path.suffix.lower() in (".sh", "") or "dockerfile" in \
            source_path.name.lower() or source_path.name.lower() == "makefile"
        literals = loader_references(text, shell)
        if is_wrapper:
            literals |= set(CODE_REF_RE.findall(text))
        source_rel = source_path.relative_to(root).as_posix()
        for literal in sorted(literals):
            named = resolve_reference(literal)
            if named is None:
                if is_wrapper:
                    obligations.append(Issue.obligation(
                        "external-code-reference", f"{source_rel}~{literal}", f"{source_rel} "
                        f"names code {literal!r} that is not in the attempt directory: confirm "
                        f"where it comes from", files=file_digests(target_dir, source_rel)))
                continue
            loaded_as_code.add(named.relative_to(root).as_posix())
            if named in generated_paths:
                errors.append(f"{source_rel} loads {named.relative_to(root).as_posix()}, which "
                              f"the run generated: generated code is never an authors' file "
                              f"or a declared wrapper")
            elif named not in declared_paths:
                errors.append(f"{source_rel} loads undeclared code "
                              f"{named.relative_to(root).as_posix()} (a file passed to a "
                              f"loader is code whatever its name)")
    if wrapper_paths:
        obligations.append(Issue.obligation(
            "wrapper-semantics", "wrappers", "wrapper semantics are not verified by the gate: "
            "its line-overlap check is a heuristic, so the reviewer confirms that each wrapper "
            "only mechanises the authors' code (paths, seeds, capture)",
            files=file_digests(target_dir, *sorted(
                p.relative_to(root).as_posix() for p in wrapper_paths))))

    # -- Closed-world inventory: every code file anywhere is accounted for.
    declared_rel = {p.relative_to(root).as_posix()
                    for p in declared_paths | generated_paths if root in p.parents}
    current = code_inventory(target_dir, loaded_as_code | declared_rel)
    known = declared_paths | generated_paths | collected_paths
    for rel_text, digest in current.items():
        path = (target_dir / rel_text).resolve()
        if path in known:
            continue
        if digest in original_hashes:
            warnings.append(f"{rel_text} is a byte-identical, undeclared copy of original "
                            f"{original_hashes[digest]!r}; declare it under executed if the "
                            f"run used it")
        else:
            errors.append(f"undeclared code file {rel_text}: neither a byte-identical authors' "
                          f"file nor a declared wrapper")

    # -- Execution snapshots (gate 1.2): for an attempt without sealed run
    #    records, what the run could execute is what the executor-taken
    #    snapshots show. Run records replace them (spec §5).
    if lane is None:
        docs: dict[str, Any] = {}
        for phase in SNAPSHOT_PHASES:
            snap_path = target_dir / SNAPSHOT_DIR / f"{phase}.json"
            try:
                docs[phase] = json.loads(snap_path.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError):
                docs[phase] = None
            result["snapshots"][phase] = docs[phase] is not None
        structural = (snapshot_problems(docs["pre"], docs["post"],
                                        sha256_file(target_dir / SNAPSHOT_DIR / "pre.json"))
                      if docs["pre"] is not None and docs["post"] is not None else [])
        if docs["pre"] is None and docs["post"] is None and not legacy:
            # A new attempt (gate 1.3): only run-container's sealed records
            # show what a run executed.
            errors.append(f"no sealed run records ({RECORDS_DIR}/): run the analysis with "
                          f"run-container (gate 1.3), which records each run; execution "
                          f"snapshots are retired")
        elif docs["pre"] is None or docs["post"] is None or structural:
            message = (f"execution snapshots missing, unreadable, or not a bound pair "
                       f"({SNAPSHOT_DIR}/pre.json and post.json, taken by snapshot-code around the "
                       f"container run): the gate cannot show which code the run executed"
                       + (f" ({'; '.join(structural)})" if structural else ""))
            (warnings if legacy else errors).append(message)
        else:
            if not legacy:
                # Executed under gate 1.2: checked by its rules, but sealed
                # run records are what admission rests on now.
                result["eligible_for_current_gate"] = False
                warnings.append(f"executed under gate 1.2 (execution snapshots, no sealed "
                                f"run records): checked, but ineligible at gate "
                                f"{GATE_VERSION} until re-run with run-container")
            # Snapshots record every file (gate 1.3). The code rules apply to code,
            # meaning anything named as code, loaded as code, or declared; other
            # files may legitimately change (logs, comparison reports).
            code_rel = set(current) | loaded_as_code | declared_rel
            pre = {k: v for k, v in docs["pre"]["files"].items()
                   if k in code_rel or is_code_file(Path(k))}
            post = {k: v for k, v in docs["post"]["files"].items()
                    if k in code_rel or is_code_file(Path(k))}
            generated_rel = {p.relative_to(target_dir.resolve()).as_posix()
                             for p in generated_paths}
            # Pre-run code missing at the post boundary is a change across the run,
            # however it is restored afterwards (PR #7 delta review, finding 2).
            for rel_text in sorted(set(pre) - set(post)):
                errors.append(f"{rel_text} was present when the run started but missing when it "
                              f"ended")
            for rel_text, digest in pre.items():
                if rel_text not in current:
                    errors.append(f"{rel_text} was present when the run started and is gone now")
                elif current[rel_text] != digest:
                    errors.append(f"{rel_text} changed after the run started: the gate must see "
                                  f"the code that ran")
                if rel_text in generated_rel:
                    errors.append(f"{rel_text} is declared generated but existed before the run")
            for rel_text, digest in post.items():
                if rel_text in pre and pre[rel_text] != digest:
                    errors.append(f"{rel_text} was modified during the run")
                elif rel_text not in pre and rel_text not in generated_rel:
                    errors.append(f"{rel_text} appeared during the run and is not declared as "
                                  f"generated")
            for path in executed_paths:
                rel_text = path.relative_to(target_dir.resolve()).as_posix()
                if rel_text not in pre or rel_text not in post:
                    errors.append(f"executed copy {rel_text} is not in both execution snapshots")
                elif not pre[rel_text] == post[rel_text] == current.get(rel_text):
                    errors.append(f"executed copy {rel_text} differs between the snapshots and the "
                                  f"tree the gate sees")
            for rel_text in sorted(set(current) - set(post)):
                warnings.append(f"{rel_text} was added after the run: it was not part of the "
                                f"recorded execution")

    result["issues"] = issue_records(flags + obligations)
    if errors:
        result["status"] = "fail"
    elif flags:
        result["status"] = "flagged"
    elif not originals:
        result["status"] = "no-authors-code"
    else:
        result["status"] = "identical"
    return result


def load_rulings(target_dir: Path) -> list[dict]:
    """The attempt's recorded rulings (``flag-rulings.json``), oldest first."""
    path = target_dir / RULINGS_FILE
    if not path.is_file():
        return []
    try:
        doc = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise LaneError(f"{display_path(path)} does not parse: {exc}") from exc
    return [r for r in doc.get("rulings") or [] if isinstance(r, dict)]


def ruling_for(issue: dict, rulings: list[dict]) -> dict | None:
    """The latest ruling on an issue, if one still applies.

    A ruling applies only when both the issue id and the evidence
    fingerprint match (spec §6). A re-run that changes the files concerned
    needs a new ruling; one that changes nothing keeps it.
    """
    matches = [r for r in rulings if r.get("issue_id") == issue.get("id")
               and r.get("fingerprint") == issue.get("fingerprint")]
    return matches[-1] if matches else None


def admitted_coverage(verdict: str, issues: list[dict], rulings: list[dict],
                      locked: list[str], reproduced_ids: list[str],
                      structural: dict[str, set[str]]) -> dict:
    """``coverage_admitted``: what counts once every issue is ruled (spec §6).

    Raw coverage counts outcomes. Admitted coverage removes:

    - every target, when the gate failed (a hard failure cannot be ruled);
    - targets excluded by structure whatever the ruling: those resting on a
      declared edit until the class (ii) wrapper-only re-run exists, and all
      of them when no authors' file ran (``structural``, reason to targets);
    - every target an unruled issue names, where an empty list names all;
    - every target an issue was ruled ``fail-and-uplift`` or ``excluded`` on.

    Returns:
        ``{targets_enumerated, targets_admitted, coverage_fraction,
        excluded_targets, reasons, unruled_issues}``.
    """
    excluded: set[str] = set()
    reasons: list[str] = []
    unruled: list[str] = []
    if verdict != "pass":
        excluded |= set(locked)
        reasons.append("the gate failed: a hard failure cannot be ruled")
    for reason, targets in structural.items():
        excluded |= targets
        reasons.append(reason)
    for issue in issues:
        named = set(issue.get("targets") or []) or set(locked)
        ruling = ruling_for(issue, rulings)
        if ruling is None:
            unruled.append(issue["id"])
            excluded |= named
        elif ruling.get("decision") in ("fail-and-uplift", "excluded"):
            excluded |= named
            reasons.append(f"{issue['id']} ruled {ruling['decision']}")
    if unruled:
        reasons.append(f"{len(unruled)} unruled issue(s)")
    kept = [tid for tid in reproduced_ids if tid not in excluded]
    return {"targets_enumerated": len(locked), "targets_admitted": len(kept),
            "coverage_fraction": round(len(kept) / len(locked), 4) if locked else 0.0,
            "excluded_targets": sorted(excluded & set(reproduced_ids)), "reasons": reasons,
            "unruled_issues": unruled}


def admission(target_dir: Path) -> dict:
    """Whether an attempt's results may enter study data (spec §6).

    Admission needs a passing gate, every issue ruled, every credited run
    complete (a failed one is covered by its ``run-failed`` issue), and a
    clean transcript audit (``transcript-audit.json``, spec §12). Nothing
    here can be overridden: a record persisted while ineligible stays so
    until ``persist-results`` is run afresh after the rulings.
    """
    reasons: list[str] = []
    try:
        report = json.loads((target_dir / GATE_FILE).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {"eligible": False, "assessed_at": now_utc(),
                "reasons": ["no readable authoritative gate report"]}
    runs = (report.get("code_integrity") or {}).get("runs")
    if runs is None:
        reasons.append("no sealed run records: the attempt predates gate 1.3")
    else:
        for run_id in runs.get("credited_runs") or []:
            state = (runs.get("runs") or {}).get(run_id, {}).get("state")
            if state not in ("complete", "failed"):
                reasons.append(f"credited run {run_id} is {state}")
    if report.get("verdict") != "pass":
        reasons.append(f"the gate verdict is {report.get('verdict')!r}")
    rulings = load_rulings(target_dir)
    unruled = [i["id"] for i in report.get("issues") or [] if ruling_for(i, rulings) is None]
    if unruled:
        reasons.append(f"{len(unruled)} unruled issue(s): {', '.join(unruled[:5])}"
                       + (" …" if len(unruled) > 5 else ""))
    try:
        audit = json.loads((target_dir / AUDIT_FILE).read_text(encoding="utf-8"))
        if audit.get("contaminating"):
            reasons.append(f"the transcript audit found {len(audit['contaminating'])} "
                           f"contaminating finding(s)")
        audit_unruled = [i["id"] for i in audit.get("issues") or []
                         if ruling_for(i, rulings) is None]
        if audit_unruled:
            reasons.append(f"{len(audit_unruled)} unruled transcript-audit issue(s): "
                           f"{', '.join(audit_unruled[:5])}")
    except (OSError, json.JSONDecodeError):
        reasons.append(f"no transcript audit recorded ({AUDIT_FILE}, spec §12)")
    return {"eligible": not reasons, "assessed_at": now_utc(), "reasons": reasons,
            "gate_report_sha256": sha256_file(target_dir / GATE_FILE)}


def check_attempt(target_dir: Path, plan_path: Path, comparison_schema: dict,
                  image: str | None = None,
                  forbid_sha256: tuple[str, ...] = (),
                  code_manifest: Path | None = None,
                  code_manifest_schema: dict | None = None,
                  legacy_attempt: bool = False,
                  legacy_list: Path | None = None,
                  anchor_root: Path | None = None,
                  launch_commit: str | None = None) -> dict:
    """The deterministic artefact gate for one attempt directory.

    Args:
        target_dir: The attempt directory.
        plan_path: The approved plan record (``reproduction-plan.json``).
        comparison_schema: The full comparison-record schema.
        image: Docker image tag that must exist locally, if given.
        forbid_sha256: Hashes of publisher files (paper, supplements) that
            must not appear anywhere in the attempt directory.
        code_manifest: The authors' code manifest; defaults to
            ``<attempt>/authors-code-manifest.json``.
        code_manifest_schema: Its full schema; defaults to the registered file.
        legacy_attempt: Request the legacy bypass. It applies only when the
            attempt is listed in ``legacy_list`` (default
            ``reproduction-system/legacy-attempts.yaml``); otherwise the request
            is itself an error.
        legacy_list: The legacy allowlist (tests override it).
        anchor_root: The repository whose committed records provenance
            anchors name (tests override it).
        launch_commit: The run's launch commit; provenance anchors verify only
            against records unchanged since it. The operator's authoritative
            re-run must pass it.

    Returns:
        A report dict with ``verdict`` ``pass`` or ``fail``, ``errors``,
        ``warnings`` (flags included, prefixed ``FLAGGED EDIT:``/``FLAG:`` so a
        relay copying warnings verbatim carries them), ``flags``, the
        ``code_integrity`` block, and recomputed ``coverage``.
    """
    errors: list[str] = []
    warnings: list[str] = []

    def nonempty(rel: str) -> bool:
        path = target_dir / rel
        if not path.is_file() or path.stat().st_size == 0:
            errors.append(f"required artefact missing or empty: {rel}")
            return False
        return True

    for rel in ("Dockerfile", "environment.md", "log.md",
                "comparisons/comparison-report.md", str(COMPARISON_FILE)):
        nonempty(rel)
    outputs = target_dir / "outputs"
    if not outputs.is_dir() or not any(p.is_file() and p.stat().st_size
                                       for p in outputs.rglob("*")):
        errors.append("outputs/ missing or holds no non-empty file")
    scripts = [p for p in target_dir.iterdir() if p.is_file()
               and p.suffix in (".R", ".r", ".sh", ".py")] if target_dir.is_dir() else []
    if not scripts:
        errors.append("no run script (*.R, *.sh, *.py) at the attempt root")

    try:
        plan_record = json.loads(plan_path.read_text(encoding="utf-8"))
        locked = [t["target_id"] for t in plan_record["plan"]["verification_targets"]]
        plan_slug = plan_record["plan"]["paper_slug"]
        plan_digest = sha256_file(plan_path)
    except (OSError, KeyError, TypeError, json.JSONDecodeError) as exc:
        errors.append(f"plan unreadable: {exc}")
        return {"verdict": "fail", "errors": errors, "warnings": warnings}

    comparison = None
    if (target_dir / COMPARISON_FILE).is_file():
        try:
            comparison = json.loads((target_dir / COMPARISON_FILE).read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"comparison.json does not parse: {exc}")
    coverage = None
    if isinstance(comparison, dict):
        errors += schema_problems(comparison, comparison_schema)
        if comparison.get("paper_slug") != plan_slug:
            errors.append(f"comparison paper_slug {comparison.get('paper_slug')!r} != "
                          f"plan {plan_slug!r}")
        if comparison.get("plan_sha256") != plan_digest:
            errors.append("comparison plan_sha256 does not match the plan file")
        dir_attempt = re.search(r"attempt-(\d+)$", target_dir.name)
        if dir_attempt and comparison.get("attempt") != int(dir_attempt.group(1)):
            errors.append(f"comparison attempt {comparison.get('attempt')} != directory "
                          f"{target_dir.name}")
        records = [t for t in comparison.get("targets") or [] if isinstance(t, dict)]
        ids = [t.get("target_id") for t in records]
        dupes = sorted({i for i in ids if ids.count(i) > 1})
        missing = [i for i in locked if i not in ids]
        extra = [i for i in ids if i not in locked]
        if dupes:
            errors.append(f"duplicate target records: {dupes}")
        if missing:
            errors.append(f"locked targets with no record (invariant 3): {missing}")
        if extra:
            errors.append(f"records for targets not in the locked plan: {extra}")
        for t in records:
            tid = t.get("target_id")
            if isinstance(t.get("values_matched"), int) and isinstance(
                    t.get("values_compared"), int) and t["values_matched"] > t["values_compared"]:
                errors.append(f"{tid}: values_matched > values_compared")
            needs_mode = t.get("testable") is False or t.get("outcome") == "CANNOT_COMPARE"
            if needs_mode and not str(t.get("failure_mode") or "").strip():
                errors.append(f"{tid}: untestable/CANNOT_COMPARE without failure_mode")
            if t.get("testable") is False and t.get("outcome") in REPRODUCED_OUTCOMES:
                errors.append(f"{tid}: marked untestable but outcome {t.get('outcome')}")
            evidence = str(t.get("evidence") or "")
            if (evidence and " " not in evidence and "/" in evidence
                    and not (target_dir / evidence).exists()):
                warnings.append(f"{tid}: evidence path not found: {evidence}")
        reproduced = sum(1 for t in records if t.get("target_id") in locked
                         and t.get("testable") is not False
                         and t.get("outcome") in REPRODUCED_OUTCOMES)
        coverage = {"targets_enumerated": len(locked), "targets_reproduced": reproduced,
                    "coverage_fraction": round(reproduced / len(locked), 4) if locked else 0.0}
        declared = comparison.get("coverage") or {}
        for key in ("targets_enumerated", "targets_reproduced"):
            if key in declared and declared[key] != coverage[key]:
                errors.append(f"declared coverage {key}={declared[key]} != recomputed "
                              f"{coverage[key]}")
        if comparison.get("verdict") == "BLOCKED" and reproduced:
            errors.append("verdict BLOCKED with reproduced targets (BLOCKED scores 0)")

    forbidden = {h.lower() for h in forbid_sha256}
    if forbidden and target_dir.is_dir():
        for path in target_dir.rglob("*"):
            if path.is_file() and sha256_file(path) in forbidden:
                errors.append(f"publisher file inside the attempt directory (corpus rule): "
                              f"{display_path(path)}")
    if image:
        probe = subprocess.run(["docker", "image", "inspect", image],
                               capture_output=True, text=True, timeout=60)
        if probe.returncode != 0:
            errors.append(f"docker image {image!r} not found locally")

    legacy = legacy_attempt and legacy_allowed(target_dir, legacy_list)
    if legacy_attempt and not legacy:
        errors.append("legacy bypass refused: this attempt is not listed in "
                      f"{LEGACY_ATTEMPTS_FILE} (only attempts executed before gate 1.1 are)")
    integrity = check_code_integrity(
        target_dir, code_manifest or target_dir / CODE_MANIFEST_FILE,
        code_manifest_schema or full_schema(expand(DEFAULT_CODE_MANIFEST_SCHEMA)),
        comparison=comparison if isinstance(comparison, dict) else None,
        plan_slug=plan_slug, legacy=legacy, anchor_root=anchor_root,
        launch_commit=launch_commit)
    errors += [f"code integrity: {e}" for e in integrity["errors"]]
    warnings += integrity["warnings"] + integrity["flags"]
    flags = list(integrity["flags"])
    if integrity.get("runs") is not None and isinstance(comparison, dict):
        # An unbound target is an issue, so admission excludes it until ruled.
        cite_errors, cite_flags, _ = citation_findings(
            records, integrity["runs"], locked, sha256_file(target_dir / COMPARISON_FILE))
        errors += cite_errors
        warnings += cite_flags
        flags += cite_flags

    # Admitted coverage (spec §6). The recomputed coverage counts outcomes,
    # so a target resting on a declared edit would be counted: exclude every
    # target a declared edit names (an empty list names them all), every
    # target when no authors' file was executed or loaded, and each target
    # citing no sealed output. A flagged result counts only once ruled.
    # (coverage_creditable, part 1's interim measure, was dropped at the
    # workflow switch.)
    admitted = None
    issues = issue_records(flags + integrity["review_obligations"])
    if coverage is not None:
        edited: set[str] = set()
        manifest = {}
        manifest_file = code_manifest or target_dir / CODE_MANIFEST_FILE
        try:
            manifest = json.loads(manifest_file.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            manifest = {}
        for item in manifest.get("executed") or []:
            edit = item.get("declared_edit") if isinstance(item, dict) else None
            if edit:
                edited |= set(edit.get("affected_targets") or list(locked))
        reproduced_ids = [t.get("target_id") for t in records if t.get("target_id") in locked
                          and t.get("testable") is not False
                          and t.get("outcome") in REPRODUCED_OUTCOMES]
        structural = {}
        account = integrity.get("account")
        if (account is not None and manifest.get("originals") and manifest.get("executed")
                and not account["originals_loaded"]):
            # The run records show what ran (spec §6): a manifest listing
            # executed copies is not enough when no credited run loaded one.
            structural["no credited run loaded an authors' file"] = set(locked)
        if manifest.get("originals") and not manifest.get("executed"):
            structural["no authors' file was executed"] = set(locked)
        elif edited:
            structural["resting on a declared edit, until the class (ii) wrapper-only "
                       "re-run"] = edited
        admitted = admitted_coverage("fail" if errors else "pass", issues,
                                     load_rulings(target_dir), locked, reproduced_ids,
                                     structural)
    return {"gate_version": GATE_VERSION, "checked_at": now_utc(),
            "attempt_dir": display_path(target_dir), "plan_file": display_path(plan_path),
            "plan_sha256": plan_digest, "locked_targets": len(locked),
            "verdict": "fail" if errors else "pass", "errors": errors,
            "warnings": warnings, "flags": flags,
            "review_obligations": integrity["review_obligations"], "coverage": coverage,
            "coverage_admitted": admitted,
            "issues": issues, "launch_commit": launch_commit,
            "eligible_for_current_gate": integrity["eligible_for_current_gate"],
            "code_integrity": {k: integrity[k] for k in (
                "status", "manifest", "manifest_sha256", "originals", "executed",
                "wrappers", "anchors", "snapshots")} | (
                    {"runs": integrity["runs"]} if integrity.get("runs") is not None else {}) | (
                    {"account": integrity["account"]} if integrity.get("account") is not None
                    else {}) | (
                    {"conversions": integrity["conversions"]} if integrity.get("conversions")
                    else {}),
            "executor_verdict": (comparison or {}).get("verdict")
            if isinstance(comparison, dict) else None}


def cmd_check_attempt(args: argparse.Namespace) -> int:
    """CLI wrapper for check_attempt(); exit 0 pass, 1 fail.

    Flags do not fail the gate; they are printed and recorded so the human
    queue sees them.
    """
    target_dir = args.attempt_dir.expanduser().resolve()
    plan_path = (args.plan or target_dir / PLAN_FILE).expanduser().resolve()
    schema = full_schema(expand(args.comparison_schema))
    report = check_attempt(target_dir, plan_path, schema, args.image,
                           tuple(args.forbid_sha256 or ()),
                           code_manifest=(args.code_manifest.expanduser().resolve()
                                          if args.code_manifest else None),
                           code_manifest_schema=full_schema(expand(args.code_manifest_schema)),
                           legacy_attempt=args.legacy_attempt,
                           launch_commit=args.launch_commit)
    if args.out == "-":
        print(json.dumps(report, indent=2))
    else:
        out = Path(args.out).expanduser() if args.out else target_dir / GATE_FILE
        write_json(out, report)
        print(json.dumps({k: report.get(k) for k in ("verdict", "errors", "warnings",
                                                       "coverage")}, indent=2))
    return 0 if report["verdict"] == "pass" else 1


def cmd_check_code(args: argparse.Namespace) -> int:
    """Run only the authors'-code integrity check; exit 0 unless it fails.

    For the session-per-phase human lane (no plan JSON) and for retroactive
    checks. Flags are reported but do not fail it.
    """
    target_dir = args.attempt_dir.expanduser().resolve()
    manifest = (args.manifest.expanduser().resolve() if args.manifest
                else target_dir / CODE_MANIFEST_FILE)
    comparison = None
    if (target_dir / COMPARISON_FILE).is_file():
        try:
            comparison = json.loads((target_dir / COMPARISON_FILE).read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            comparison = None
    legacy = args.legacy_attempt and legacy_allowed(target_dir)
    if args.legacy_attempt and not legacy:
        print(f"ERROR: legacy bypass refused: {display_path(target_dir)} is not listed in "
              f"{LEGACY_ATTEMPTS_FILE}", file=sys.stderr)
        return 1
    report = check_code_integrity(target_dir, manifest,
                                  full_schema(expand(args.code_manifest_schema)),
                                  comparison=comparison, legacy=legacy,
                                  launch_commit=args.launch_commit)
    report = {"check": "authors-code-integrity", "gate_version": GATE_VERSION,
              "checked_at": now_utc(), "attempt_dir": display_path(target_dir), **report}
    if args.out and args.out != "-":
        write_json(Path(args.out).expanduser(), report)
        print(f"wrote {args.out}")
    print(json.dumps({k: report[k] for k in ("status", "errors", "flags", "warnings",
                                             "review_obligations")},
                     indent=2, ensure_ascii=False))
    return 1 if report["status"] == "fail" else 0


def cmd_snapshot_code(args: argparse.Namespace) -> int:
    """Retired at gate 1.3 (spec §5): run-container records every run.

    The snapshots it wrote are still read for attempts executed under gate
    1.2, and the transcript audit treats a call as contaminating (§12).
    """
    raise LaneError("snapshot-code is retired at gate 1.3: run the analysis with "
                    "run-container, which records each run in lane-records/")


def cmd_run_container(args: argparse.Namespace) -> int:
    """CLI wrapper: start a run, finalise one, or clear a stale lock.

    Exit status 0 means the run is sealed ``complete``, or a detached run has
    started. 1 means it sealed ``failed`` or ``incomplete``; the records are
    kept either way.
    """
    target_dir = args.attempt_dir.expanduser().resolve()
    if not target_dir.is_dir():
        raise LaneError(f"attempt directory not found: {display_path(target_dir)}")
    if args.clear_lock:
        print(f"cleared the lock held by {clear_lock(target_dir)}; that run stays unsealed "
              f"and counts as incomplete")
        return 0
    if args.finalise:
        doc = finalise_run(target_dir, args.finalise, keep_work=args.keep_work)
    else:
        if not args.image or not args.entry:
            raise LaneError("a new run needs --image and --entry")
        doc = start_run(target_dir, args.image, args.entry, mount_path=args.mount_path,
                        launch_commit=args.launch_commit, work_root=args.work_root,
                        consume=args.consume, keep_stores=args.keep_store)
        if args.detach:
            print(f"started {doc['run']} (container {doc['container_id'][:12]}); finish it "
                  f"with: run-container {display_path(target_dir)} --finalise {doc['run']}")
            return 0
        doc = finalise_run(target_dir, doc["run"], keep_work=args.keep_work)
    census = doc.get("census") or {}
    print(f"{doc['run']}: {doc['state']} (exit status {doc['exit_status']}; "
          f"{census.get('processes', 0)} R process(es), {census.get('errors', 0)} census "
          f"error(s)); outputs in outputs/{doc['run']}/, records in "
          f"{RECORDS_DIR}/{doc['run']}/")
    for problem in doc.get("problems") or []:
        print(f"  problem: {problem}")
    return 0 if doc["state"] == "complete" else 1


def authoritative_queue(config: dict) -> tuple[list[str], list[str]]:
    """The human queue as the on-disk gate reports state it.

    Returns:
        ``(queue, problems)``: one item per failed gate and per flag, in the
        workflow's ``<slug>: <text>`` form; problems are missing or unreadable
        gate reports, which block clearing the queue.
    """
    queue: list[str] = []
    problems: list[str] = []
    for paper in config["papers"]:
        slug = paper["slug"]
        path = attempt_dir(config, slug) / GATE_FILE
        try:
            report = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            problems.append(f"{slug}: no readable authoritative gate report ({exc})")
            continue
        if report.get("verdict") != "pass":
            queue.append(f"{slug}: gate {report.get('verdict')}")
        if not isinstance(report.get("flags"), list):
            problems.append(f"{slug}: gate report has no flags list (pre-1.1 report?)")
            continue
        queue += [f"{slug}: {flag}" for flag in report["flags"]]
    return queue, problems


def issue_statuses(config: dict) -> list[dict]:
    """Every issue in the authoritative gate reports, ruled or unruled (spec §6).

    Obligations are listed as well as flags: both block admission until a
    human rules on them.
    """
    statuses = []
    for paper in config["papers"]:
        target_dir = attempt_dir(config, paper["slug"])
        try:
            report = json.loads((target_dir / GATE_FILE).read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        rulings = load_rulings(target_dir)
        for issue in attempt_issues(target_dir, report).values():
            ruling = ruling_for(issue, rulings)
            statuses.append({"slug": paper["slug"], "id": issue["id"], "kind": issue["kind"],
                             "status": "ruled" if ruling else "unruled",
                             "decision": ruling.get("decision") if ruling else None,
                             "message": issue.get("message")})
    return statuses


def cmd_human_queue(args: argparse.Namespace) -> int:
    """Rebuild the human queue from the authoritative gate reports.

    The workflow's in-run gate is a relay, and a relay can drop a flag (PR #7
    review, finding 4). Run this after the operator's authoritative
    ``check-attempt`` re-runs: it lists every failed gate and every flag, and,
    given the workflow's result, reports any of them the relay did not carry.
    The human queue is cleared from this output, never from the relay alone.
    Exit 1 when a gate report is missing or any item was lost in the relay.
    """
    config = load_config(args.config)
    queue, problems = authoritative_queue(config)
    lost: list[str] = []
    if args.workflow_result:
        data = json.loads(args.workflow_result.expanduser().read_text(encoding="utf-8"))
        relayed = data.get("human_queue") if isinstance(data, dict) else data
        if not isinstance(relayed, list):
            raise LaneError("workflow result carries no human_queue list")
        lost = [item for item in queue if item not in set(relayed)]
    issues = issue_statuses(config)
    report = {"run_id": config["run_id"], "built_at": now_utc(), "queue": queue,
              "problems": problems, "lost_in_relay": lost, "issues": issues,
              "unruled": sum(1 for i in issues if i["status"] == "unruled")}
    if args.out:
        write_json(args.out.expanduser(), report)
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 1 if problems or lost else 0


DIMENSION_KEYS = ("provenance", "quantitative_claims", "scope_completeness",
                  "confirmation_bias", "methodological_soundness")


def expected_overall(review: dict) -> str | None:
    """The framework's overall rule: 0 concerns CONFIRMED, 1–2 QUALIFIED, 3+ CHALLENGED."""
    dims = review.get("dimensions") or {}
    if not all(k in dims for k in DIMENSION_KEYS):
        return None
    concerns = sum(1 for k in DIMENSION_KEYS if dims[k].get("verdict") == "CONCERN")
    return "CONFIRMED" if concerns == 0 else "QUALIFIED" if concerns <= 2 else "CHALLENGED"


def cmd_persist_results(args: argparse.Namespace) -> int:
    """Persist executor and reviewer payloads into their attempt directories."""
    config = load_config(args.config)
    run_dir = args.run_dir.expanduser().resolve()
    results = journal_results(run_dir)
    problems = []
    for role, filename, schema_key in (("executor", EXECUTION_FILE, "execution"),
                                       ("reviewer", REVIEW_FILE, "review")):
        chosen, dead = select_results(results, config["agents"][role], config)
        problems += [f"{role} for {slug} returned no result — re-run that item"
                     for slug in dead]
        schema = full_schema(expand(config["schemas"][schema_key]))
        for slug, item in sorted(chosen.items()):
            payload = item["result"]
            notes = schema_problems(payload, schema)
            if role == "reviewer" and payload.get("status") == "OK":
                expected = expected_overall(payload)
                if expected and payload.get("overall") != expected:
                    notes.append(f"overall {payload.get('overall')!r} disagrees with the "
                                 f"framework's concern-count rule ({expected!r})")
            path = attempt_dir(config, slug) / filename
            if path.exists() and not args.force:
                problems.append(f"{display_path(path)} exists — pass --force to replace")
                continue
            # Gate 1.3 admission (spec §6): an attempt with sealed run records
            # is persisted only when eligible, or, with --record-unruled, as
            # ineligible. Nothing downstream can make that record eligible.
            admitted = admission(attempt_dir(config, slug))
            sealed = (attempt_dir(config, slug) / RECORDS_DIR).is_dir()
            if role == "executor" and sealed and not admitted["eligible"] \
                    and not args.record_unruled:
                problems.append(f"{slug} is not eligible for study data "
                                f"({'; '.join(admitted['reasons'])}); pass --record-unruled to "
                                f"persist it as ineligible")
                continue
            provenance = PROVENANCE_RE.search(item["prompt"])
            write_json(path, {"record_version": "1.0", "run_id": config["run_id"],
                              "workflow_run": run_dir.name, "agent_id": item["agent_id"],
                              "agent_type": item["agent_type"],
                              "launch_commit": provenance.group(2) if provenance else None,
                              "effort": provenance.group(3) if provenance else None,
                              "persisted_at": now_utc(), "orchestrator_notes": notes,
                              "admission": admitted, "payload": payload})
            print(f"persisted {display_path(path)}"
                  + (f" ({len(notes)} note(s))" if notes else ""))
    for problem in problems:
        print(f"SKIPPED: {problem}", file=sys.stderr)
    return 1 if problems else 0


# ---------------------------------------------------------------------------
# Audit
# ---------------------------------------------------------------------------

def transcript_usage(lines: list[str]) -> dict:
    """Token usage summed once per API request, plus the models seen.

    The harness writes one transcript entry per content block and repeats
    the response's ``usage`` on each, so a naive per-entry sum counts a
    request's input and cache tokens once per block (measured 2026-10-03 on
    wf_d691e836-2f2: cache-creation 4.84M summed vs 1.86M per request).
    Each field is taken at its maximum within a request — identical for
    input/cache fields, cumulative for output.
    """
    per_request: dict[str, dict[str, int]] = {}
    models: dict[str, str] = {}
    fields = ("input_tokens", "output_tokens", "cache_creation_input_tokens",
              "cache_read_input_tokens", "cache_write_5m", "cache_write_1h")
    for index, line in enumerate(lines):
        try:
            entry = json.loads(line)
        except json.JSONDecodeError:
            continue
        message = entry.get("message")
        if not isinstance(message, dict) or not isinstance(message.get("usage"), dict):
            continue
        usage = message["usage"]
        key = str(entry.get("requestId") or message.get("id") or f"line-{index}")
        split = usage.get("cache_creation") if isinstance(usage.get("cache_creation"),
                                                          dict) else {}
        created = int(usage.get("cache_creation_input_tokens") or 0)
        one_hour = int(split.get("ephemeral_1h_input_tokens") or 0)
        values = {"input_tokens": int(usage.get("input_tokens") or 0),
                  "output_tokens": int(usage.get("output_tokens") or 0),
                  "cache_creation_input_tokens": created,
                  "cache_read_input_tokens": int(usage.get("cache_read_input_tokens") or 0),
                  "cache_write_1h": one_hour,
                  "cache_write_5m": max(created - one_hour, 0)}
        current = per_request.setdefault(key, {f: 0 for f in fields})
        for field_name in fields:
            current[field_name] = max(current[field_name], values[field_name])
        # Harness-generated entries carry placeholder names like
        # "<synthetic>"; only real model ids price an agent.
        if message.get("model") and not str(message["model"]).startswith("<"):
            models[key] = str(message["model"])
    totals = {f: sum(r[f] for r in per_request.values()) for f in fields}
    totals["requests"] = len(per_request)
    totals["models"] = sorted(set(models.values()))
    return totals


def price_usage(usage: dict, pricing: dict) -> float | None:
    """API-equivalent USD for one agent's usage, or None if unpriceable."""
    models = {DATE_SUFFIX_RE.sub("", m.replace("[1m]", "")) for m in usage["models"]}
    if len(models) != 1 or next(iter(models)) not in pricing:
        return None
    rates = pricing[next(iter(models))]
    cost = (usage["input_tokens"] * rates["input"]
            + usage["output_tokens"] * rates["output"]
            + usage["cache_write_5m"] * rates["cache_write_5m"]
            + usage["cache_write_1h"] * rates["cache_write_1h"]
            + usage["cache_read_input_tokens"] * rates["cache_read"]) / 1_000_000
    return round(cost, 4)


def bash_calls(lines: list[str]) -> list[dict]:
    """Every Bash call in a transcript with its success flag and output text."""
    uses: list[tuple[str, str]] = []
    errors: dict[str, bool] = {}
    outputs: dict[str, str] = {}
    for line in lines:
        try:
            entry = json.loads(line)
        except json.JSONDecodeError:
            continue
        message = entry.get("message")
        content = message.get("content") if isinstance(message, dict) else None
        if not isinstance(content, list):
            continue
        for block in content:
            if not isinstance(block, dict):
                continue
            if block.get("type") == "tool_use" and block.get("name") == "Bash":
                uses.append((str(block.get("id")),
                             str((block.get("input") or {}).get("command") or "")))
            elif block.get("type") == "tool_result":
                use_id = str(block.get("tool_use_id"))
                errors[use_id] = bool(block.get("is_error"))
                raw = block.get("content")
                outputs[use_id] = ("".join(str(p.get("text", "")) for p in raw
                                           if isinstance(p, dict))
                                   if isinstance(raw, list) else str(raw or ""))
    return [{"command": command, "errored": errors.get(use_id, True),
             "output": outputs.get(use_id, "")} for use_id, command in uses]


def write_targets(lines: list[str]) -> list[str]:
    """Paths written by Write/Edit/NotebookEdit tool calls."""
    targets = []
    for line in lines:
        try:
            entry = json.loads(line)
        except json.JSONDecodeError:
            continue
        message = entry.get("message")
        content = message.get("content") if isinstance(message, dict) else None
        for block in content if isinstance(content, list) else []:
            if (isinstance(block, dict) and block.get("type") == "tool_use"
                    and block.get("name") in ("Write", "Edit", "NotebookEdit")):
                path = (block.get("input") or {}).get("file_path") \
                    or (block.get("input") or {}).get("notebook_path")
                if path:
                    targets.append(str(path))
    return targets


def own_spill_files(lines: list[str]) -> set[str]:
    """Spill files the harness created for THIS transcript's own tool results.

    Matched exactly (display form), so another agent's or the orchestrator's
    spill under the same ``tool-results/`` directory stays blinded.
    """
    spills: set[str] = set()
    for line in lines:
        try:
            entry = json.loads(line)
        except json.JSONDecodeError:
            continue
        message = entry.get("message")
        content = message.get("content") if isinstance(message, dict) else None
        for block in content if isinstance(content, list) else []:
            if not isinstance(block, dict) or block.get("type") != "tool_result":
                continue
            raw = block.get("content")
            text = ("".join(str(p.get("text", "")) for p in raw if isinstance(p, dict))
                    if isinstance(raw, list) else str(raw or ""))
            spills.update(display_path(path) for path in SPILL_RE.findall(text))
    return spills


def path_tokens(text: str) -> list[str]:
    """Path-like tokens in shell text (URLs excluded)."""
    return [t for t in SHELL_SPLIT_RE.split(text)
            if t and "://" not in t and ("/" in t or t.endswith((".json", ".md", ".csv")))]


class Blinding:
    """Judges paths against a run's blinded set for one paper's agents."""

    def __init__(self, config: dict, own_slug: str) -> None:
        blinding = config["blinding"]
        self.forbidden = [str(s) for s in blinding["forbidden_substrings"]]
        pattern = blinding.get("exempt_regex")
        self.exempt = re.compile(pattern) if pattern else None
        self.others = [s for s in blinding.get("cross_paper_slugs") or [] if s != own_slug]

    def hit(self, path: str) -> str | None:
        """The rule a path breaks, or None when it is in scope."""
        if self.exempt and self.exempt.search(path):
            return None
        for substring in self.forbidden:
            if substring in path:
                return f"blinded: {substring}"
        for slug in self.others:
            if slug in path:
                return f"other paper: {slug}"
        return None


def audit_agent(lines: list[str], agent_type: str, config: dict, manifest: dict,
                reconcile: ModuleType, gate: ModuleType, hooklib: ModuleType) -> dict:
    """Audit one agent transcript: receipts, blinding, write scope, usage."""
    prompt = first_user_text(lines)
    paper = PAPER_RE.search(prompt)
    own_slug = paper.group(1) if paper else ""
    blinding = Blinding(config, own_slug)
    governed = agent_type in (manifest.get("agent_definitions") or {})
    record: dict[str, Any] = {"agent_type": agent_type, "paper": own_slug,
                              "governed": governed}
    provenance = PROVENANCE_RE.search(prompt)
    record["provenance"] = ({"run_id": provenance.group(1),
                             "launch_commit": provenance.group(2),
                             "effort": provenance.group(3)} if provenance else None)
    if governed:
        role_schema = {config["agents"]["planner"]: "plan",
                       config["agents"]["executor"]: "execution",
                       config["agents"]["reviewer"]: "review"}.get(agent_type)
        contract = full_schema(expand(config["schemas"][role_schema])) if role_schema else None
        record["receipts"] = reconcile.revalidate(lines, agent_type, manifest, gate,
                                                  hooklib, contract_schema=contract)
        if not provenance:
            record["receipts"]["valid"] = False
            record["receipts"]["problems"].append("no Provenance line in spawn prompt")
        elif provenance.group(3) != config["effort"]:
            record["receipts"]["valid"] = False
            record["receipts"]["problems"].append(
                f"effort {provenance.group(3)!r} != run config {config['effort']!r}")
    contaminating, warnings = [], []
    own_spills = own_spill_files(lines)
    for access in reconcile.file_accesses(lines, gate):
        targets = [access["target"]] if access["tool"] == "Read" else \
            list(access.get("returned") or []) + [access["target"]]
        for target in targets:
            if display_path(target) in own_spills:
                continue
            rule = blinding.hit(target)
            if rule:
                bucket = warnings if access["errored"] else contaminating
                bucket.append({"tool": access["tool"], "path": target, "rule": rule})
                break
    for call in bash_calls(lines):
        command_hits = [(t, blinding.hit(t)) for t in path_tokens(call["command"])]
        command_hits = [(t, r) for t, r in command_hits if r]
        if command_hits:
            bucket = warnings if call["errored"] else contaminating
            bucket.append({"tool": "Bash", "path": command_hits[0][0],
                           "rule": command_hits[0][1], "command": call["command"][:300]})
            continue
        output_hits = [t for t in path_tokens(call["output"])
                       if blinding.hit(t) and display_path(t) not in own_spills]
        if output_hits:
            warnings.append({"tool": "Bash", "path": output_hits[0],
                             "rule": "blinded path named in command output (review)",
                             "command": call["command"][:300]})
    record["blinding"] = {"contaminating": contaminating, "warnings": warnings}
    allowed_roots = [m.group(1) for m in (ATTEMPT_DIR_RE.search(prompt),
                                          SCRATCH_RE.search(prompt)) if m]
    record["writes_outside_scope"] = [
        display_path(t) for t in write_targets(lines)
        if not any(str(Path(t).expanduser()).startswith(root.rstrip("/") + "/")
                   for root in allowed_roots)]
    usage = transcript_usage(lines)
    record["usage"] = usage
    record["cost_usd"] = price_usage(usage, config.get("pricing_usd_per_mtok") or {})
    telemetry = reconcile_telemetry(lines)
    record.update(telemetry)
    record["clean"] = (not contaminating and not record["writes_outside_scope"]
                       and (not governed or record["receipts"]["valid"]))
    return record


def reconcile_telemetry(lines: list[str]) -> dict:
    """First/last transcript timestamps and the wall-clock between them."""
    stamps = []
    for line in lines:
        try:
            stamp = json.loads(line).get("timestamp")
        except json.JSONDecodeError:
            continue
        if isinstance(stamp, str) and stamp:
            stamps.append(stamp)
    if not stamps:
        return {"started_at": None, "finished_at": None, "wallclock_seconds": None}

    def parse(value: str) -> datetime:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))

    return {"started_at": stamps[0], "finished_at": stamps[-1],
            "wallclock_seconds": round((parse(stamps[-1]) - parse(stamps[0]))
                                       .total_seconds(), 1)}


# ---------------------------------------------------------------------------
# Transcript audit of an attempt's execution (gate 1.3, spec §12)
# ---------------------------------------------------------------------------
#
# The harness transcript is the one record the executor cannot edit. The
# audit reads it for paper code run other than through run-container, for
# writes into the lane's records or a run's outputs, for changes to the input
# tree after the final run started, and for run-container calls and run
# records that do not pair. Contaminating findings block admission (spec §6).
# It is supporting evidence: shell indirection can avoid any pattern, which
# is why runs are bound by receipt, not by command (Astra 10).

TRANSCRIPT_AUDIT_VERSION = "1.0"
SEGMENT_SPLIT_RE = re.compile(r"&&|\|\||;|\||\n")
DOCKER_RUN_RE = re.compile(
    r"\bdocker(?:-compose|\s+(?:container\s+)?(run|exec|cp|start|compose))\b")
HOST_RUN_RE = re.compile(r"(?:^|[\s/])(Rscript|R\s+(?:--file|-f)|python3?|bash)\b")
CD_RE = re.compile(r"\bcd\s+([^\s;&|]+)")
REDIRECT_RE = re.compile(r"(?<![0-9&])>>?\s*([^\s;&|<>]+)")
COPY_LIKE_RE = re.compile(r"(?:^|\s)(cp|mv|install|rsync)\s+(.*)")
TEE_RE = re.compile(r"(?:^|\s)tee\s+(.*)")
SED_IN_PLACE_RE = re.compile(
    r"(?:^|\s)sed\s+(?:[^|;&]*\s)?(?:-[a-zA-Z]*i[a-zA-Z]*|--in-place)\s+(.*)")


def timed_tool_calls(lines: list[str]) -> list[dict]:
    """Every tool call in a transcript, in order, with its time and outcome.

    Returns:
        ``[{name, input, at, errored, output}]``, ``at`` the timestamp of the
        entry that made the call.
    """
    calls: list[dict] = []
    by_id: dict[str, dict] = {}
    for line in lines:
        try:
            entry = json.loads(line)
        except json.JSONDecodeError:
            continue
        message = entry.get("message")
        content = message.get("content") if isinstance(message, dict) else None
        for block in content if isinstance(content, list) else []:
            if not isinstance(block, dict):
                continue
            if block.get("type") == "tool_use":
                call = {"name": block.get("name"), "input": block.get("input") or {},
                        "at": entry.get("timestamp"), "errored": None, "output": ""}
                calls.append(call)
                by_id[str(block.get("id"))] = call
            elif block.get("type") == "tool_result" and str(block.get("tool_use_id")) in by_id:
                call = by_id[str(block.get("tool_use_id"))]
                call["errored"] = bool(block.get("is_error"))
                raw = block.get("content")
                call["output"] = ("".join(str(p.get("text", "")) for p in raw
                                          if isinstance(p, dict))
                                  if isinstance(raw, list) else str(raw or ""))
    return calls


def segment_writes(segment: str) -> list[str]:
    """Paths a shell segment writes: redirects, cp/mv/install/rsync
    destinations, tee's files, and sed -i's files."""
    targets = list(REDIRECT_RE.findall(segment))
    copy = COPY_LIKE_RE.search(segment)
    if copy:
        args = [a for a in copy.group(2).split() if not a.startswith("-")]
        if len(args) >= 2:
            targets.append(args[-1])
    tee = TEE_RE.search(segment)
    if tee:
        targets += [a for a in tee.group(1).split() if not a.startswith("-")]
    sed = SED_IN_PLACE_RE.search(segment)
    if sed:
        args = [a for a in sed.group(1).split() if not a.startswith("-")]
        targets += args[1:]
    return [t.strip("'\"") for t in targets if t and not t.startswith("/dev/")]


def audit_execution(lines: list[str], target_dir: Path, manifest_doc: dict | None) -> dict:
    """The §12 audit of one attempt's executor transcript.

    Args:
        lines: The executor's transcript.
        target_dir: The attempt directory.
        manifest_doc: The authors' code manifest, for the code paths a host
            run must not name.

    Returns:
        The ``transcript-audit.json`` record: ``contaminating`` findings
        (hard failures), ``issues`` (flags for a ruling: ``host-run``), and
        what the audit compared.
    """
    root = target_dir.resolve()
    records = root / RECORDS_DIR
    indexed, _ = read_run_index(records)
    sealed = {}
    for run_id in run_ids(records):
        try:
            sealed[run_id] = json.loads((records / run_id / "run.json").read_text(
                encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
    credible = [r for r in run_ids(records)
                if r in indexed and sealed.get(r, {}).get("state") in ("complete", "failed")]
    final = credible[-1] if credible else None
    final_start = sealed[final].get("started_at") if final else None
    # Code a host run must not name: originals' copies, executed copies, and
    # wrappers, except those that run on the host by design (§5, §11).
    manifest_doc = manifest_doc or {}
    host_exempt = {w["path"] for w in manifest_doc.get("wrappers") or []
                   if w.get("role") in ("comparison", "conversion")}
    code_paths = sorted({p for p in (
        [o.get("local_copy") for o in manifest_doc.get("originals") or []]
        + [e.get("path") for e in manifest_doc.get("executed") or []]
        + [w.get("path") for w in manifest_doc.get("wrappers") or []
           if w.get("role") != "generated"]) if p and p not in host_exempt})
    contaminating: list[dict] = []
    issues: list[Issue] = []

    def after_final(stamp: str | None) -> bool:
        return bool(final_start and stamp and stamp.replace("Z", "+00:00") >=
                    str(final_start).replace("Z", "+00:00"))

    def place(path_text: str, cwd: str | None) -> str | None:
        """An attempt-relative path, when a written or named path is in the
        attempt: absolute, or relative to an explicit cd."""
        if not path_text:
            return None
        path = Path(path_text).expanduser()
        if not path.is_absolute():
            if cwd is None:
                return None
            path = Path(cwd).expanduser() / path
        try:
            return Path(os.path.normpath(path)).relative_to(root).as_posix()
        except ValueError:
            return None

    def find(kind: str, at: str | None, detail: str) -> None:
        contaminating.append({"kind": kind, "at": at, "detail": detail[:400]})

    def written(rel: str, at: str | None, how: str) -> None:
        first = rel.split("/", 1)[0]
        if first in (RECORDS_DIR, "outputs"):
            find("write-to-lane-owned", at, f"{how} wrote {rel}, which only the lane writes")
        elif first not in DOCUMENT_NAMES and after_final(at):
            find("input-tree-changed-after-run", at, f"{how} wrote {rel} after the final run "
                 f"{final} started")

    runs_called: set[str] = set()
    for call in timed_tool_calls(lines):
        at = call["at"]
        if call["name"] in ("Write", "Edit", "NotebookEdit", "MultiEdit"):
            target = call["input"].get("file_path") or call["input"].get("notebook_path")
            rel = place(str(target or ""), None)
            if rel is not None:
                written(rel, at, call["name"])
            continue
        if call["name"] != "Bash":
            continue
        command = str(call["input"].get("command") or "")
        cd = CD_RE.search(command)
        cwd = cd.group(1).strip("'\"") if cd else None
        for segment in SEGMENT_SPLIT_RE.split(command):
            segment = segment.strip()
            if not segment:
                continue
            if "reproduction-lane.py" in segment:
                if re.search(r"\bsnapshot-code\b", segment):
                    find("snapshot-code", at, f"the executor ran snapshot-code: {segment}")
                elif re.search(r"\brun-container\b", segment):
                    if "--clear-lock" in segment:
                        find("clear-lock", at, f"the executor cleared a run lock: {segment}")
                    elif "--finalise" not in segment:
                        named = set(re.findall(r"\b(run-\d{2,})\b", call["output"]))
                        runs_called |= named
                        if not named and call["errored"] is False:
                            find("run-without-record", at, f"run-container reported no run: "
                                 f"{segment}")
                    else:
                        runs_called |= set(re.findall(r"\b(run-\d{2,})\b", segment))
                continue
            docker = DOCKER_RUN_RE.search(segment)
            if docker:
                find("docker-direct", at, f"paper code may run other than through "
                     f"run-container: {segment}")
                continue
            if HOST_RUN_RE.search(segment):
                named = [p for p in code_paths if p in segment or str(root / p) in segment]
                if named:
                    if after_final(at):
                        find("host-run-after-final", at, f"a host run named {named[0]} after "
                             f"the final run {final} started: {segment}")
                    else:
                        issues.append(Issue.flag(
                            "host-run", named[0], f"the executor ran {named[0]} on the host "
                            f"before the final run ({segment[:160]}): credit comes only from "
                            f"sealed outputs, but invariant 5 is an environment rule, so a "
                            f"human rules on it", files={named[0]: json_digest(segment)}))
            for target in segment_writes(segment):
                rel = place(target, cwd)
                if rel is not None:
                    written(rel, at, "a shell command")
    for run_id in run_ids(records):
        if run_id not in runs_called:
            find("record-without-call", None, f"{run_id} has a run record but no "
                 f"run-container call in the transcript names it")
    deduped = {(c["kind"], c["detail"]): c for c in contaminating}
    seen: set[str] = set()
    unique_issues = [i for i in issues if not (i.issue_id in seen or seen.add(i.issue_id))]
    return {"audit_version": TRANSCRIPT_AUDIT_VERSION, "audited_at": now_utc(),
            "attempt_dir": display_path(target_dir), "final_run": final,
            "final_run_started_at": final_start, "runs_called": sorted(runs_called),
            "contaminating": list(deduped.values()),
            "issues": issue_records(unique_issues)}


def cmd_audit_run(args: argparse.Namespace) -> int:
    """Audit every agent in a workflow run directory; exit 1 if any is unclean."""
    config = load_config(args.config)
    run_dir = args.run_dir.expanduser().resolve()
    reconcile = load_module("reconcile_run", "scripts/reconcile-run.py")
    gate = reconcile.load_gate_module()
    sys.path.insert(0, str(HOOKS_DIR))
    try:
        import hooklib  # noqa: PLC0415 — hooks dir is not a package
    finally:
        sys.path.pop(0)
    manifest = hooklib.load_manifest()
    agents = []
    for transcript in sorted(run_dir.glob("agent-*.jsonl")):
        meta_path = transcript.with_name(f"{transcript.stem}.meta.json")
        meta = (json.loads(meta_path.read_text(encoding="utf-8"))
                if meta_path.is_file() else {})
        lines = transcript.read_text(encoding="utf-8").splitlines()
        record = audit_agent(lines, str(meta.get("agentType") or ""), config, manifest,
                             reconcile, gate, hooklib)
        record["agent_id"] = transcript.stem.replace("agent-", "")
        # The executor's transcript also gets the attempt's own audit (spec
        # §12), written into the attempt as admission requires.
        attempt = ATTEMPT_DIR_RE.search(first_user_text(lines))
        if meta.get("agentType") == config["agents"]["executor"] and attempt:
            attempt_path = expand(attempt.group(1))
            manifest_path = attempt_path / CODE_MANIFEST_FILE
            try:
                manifest_doc = json.loads(manifest_path.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError):
                manifest_doc = None
            execution = audit_execution(lines, attempt_path, manifest_doc)
            execution["transcript"] = display_path(transcript)
            if attempt_path.is_dir():
                write_json(attempt_path / AUDIT_FILE, execution)
            record["execution_audit"] = {"contaminating": execution["contaminating"],
                                         "issues": len(execution["issues"])}
            if execution["contaminating"]:
                record["clean"] = False
        if not meta.get("agentType"):
            record["clean"] = False
            record["unattributable"] = True
        agents.append(record)
    per_paper: dict[str, dict] = {}
    for record in agents:
        bucket = per_paper.setdefault(record["paper"] or "(none)", {
            "agents": 0, "output_tokens": 0, "input_side_tokens": 0, "cost_usd": 0.0,
            "agent_wallclock_seconds": 0.0, "unpriced_agents": 0})
        usage = record["usage"]
        bucket["agents"] += 1
        bucket["output_tokens"] += usage["output_tokens"]
        bucket["input_side_tokens"] += (usage["input_tokens"]
                                        + usage["cache_creation_input_tokens"]
                                        + usage["cache_read_input_tokens"])
        if record["cost_usd"] is None:
            bucket["unpriced_agents"] += 1
        else:
            bucket["cost_usd"] = round(bucket["cost_usd"] + record["cost_usd"], 4)
        bucket["agent_wallclock_seconds"] += record["wallclock_seconds"] or 0.0
    clean = bool(agents) and all(r["clean"] for r in agents)
    report = {"audit_version": "1.0", "audited_at": now_utc(), "run_id": config["run_id"],
              "workflow_run": run_dir.name, "agents": agents, "per_paper": per_paper,
              "clean": clean}
    out = args.out or Path(config["_path"]).parent / f"audit-{run_dir.name}.json"
    write_json(out, report)
    out.with_suffix(".md").write_text(render_audit(report), encoding="utf-8")
    print(f"wrote {display_path(out)} and {display_path(out.with_suffix('.md'))}")
    print(f"clean: {clean}")
    return 0 if clean else 1


def render_audit(report: dict) -> str:
    """Human summary of an audit record."""
    out = [f"# Run audit — {report['run_id']}", "",
           f"Workflow run `{report['workflow_run']}`, audited {report['audited_at']}. "
           f"**Clean: {report['clean']}**", "",
           "| Agent | Type | Paper | Receipts | Contaminating | Warnings | Writes out "
           "of scope | Output tok | Input-side tok | USD | Wall-clock (s) |",
           "|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in report["agents"]:
        receipts = ("valid" if r["receipts"]["valid"] else "INVALID") \
            if r.get("receipts") else "n/a"
        usage = r["usage"]
        out.append("| " + " | ".join(md_cell(v) for v in (
            r["agent_id"][:10], r["agent_type"], r["paper"], receipts,
            len(r["blinding"]["contaminating"]), len(r["blinding"]["warnings"]),
            len(r["writes_outside_scope"]), usage["output_tokens"],
            usage["input_tokens"] + usage["cache_creation_input_tokens"]
            + usage["cache_read_input_tokens"], r["cost_usd"],
            r["wallclock_seconds"])) + " |")
    out += ["", "## Per paper", "",
            "| Paper | Agents | Output tok | Input-side tok | USD (API-equivalent) | "
            "Agent wall-clock (min) |", "|---|---|---|---|---|---|"]
    for paper, b in sorted(report["per_paper"].items()):
        out.append("| " + " | ".join(md_cell(v) for v in (
            paper, b["agents"], b["output_tokens"], b["input_side_tokens"],
            f"{b['cost_usd']:.2f}" + (f" (+{b['unpriced_agents']} unpriced)"
                                      if b["unpriced_agents"] else ""),
            round(b["agent_wallclock_seconds"] / 60, 1))) + " |")
    problems = [r for r in report["agents"] if not r["clean"] or r["blinding"]["warnings"]]
    if problems:
        out += ["", "## Findings", ""]
        for r in problems:
            for item in r["blinding"]["contaminating"]:
                out.append(f"- **{r['agent_id'][:10]}** CONTAMINATING {item['tool']} "
                           f"`{item['path']}` ({item['rule']})")
            for item in r["blinding"]["warnings"]:
                out.append(f"- {r['agent_id'][:10]} warning {item['tool']} "
                           f"`{item['path']}` ({item['rule']})")
            for path in r["writes_outside_scope"]:
                out.append(f"- **{r['agent_id'][:10]}** write outside scope `{path}`")
            if r.get("receipts") and not r["receipts"]["valid"]:
                out.append(f"- **{r['agent_id'][:10]}** receipts: "
                           + "; ".join(r["receipts"]["problems"]))
    return "\n".join(out) + "\n"


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    """The subcommand parser."""
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("build-plan-args", help="args for the plan workflow")
    p.add_argument("--config", type=Path, required=True)
    p.add_argument("--scratch-root", required=True)
    p.add_argument("--out", type=Path, default=None)
    p.set_defaults(func=cmd_build_plan_args)

    p = sub.add_parser("supersede-plans", help="archive unapproved plans before a re-plan")
    p.add_argument("--config", type=Path, required=True)
    group = p.add_mutually_exclusive_group(required=True)
    group.add_argument("--slug")
    group.add_argument("--all", action="store_true")
    p.set_defaults(func=cmd_supersede_plans)

    p = sub.add_parser("persist-plans", help="persist planner payloads + triage")
    p.add_argument("--config", type=Path, required=True)
    p.add_argument("--run-dir", type=Path, required=True)
    p.add_argument("--force", action="store_true",
                   help="replace an existing UNAPPROVED plan")
    p.set_defaults(func=cmd_persist_plans)

    p = sub.add_parser("approve", help="record a plan decision")
    p.add_argument("--config", type=Path, required=True)
    p.add_argument("--slug", required=True)
    p.add_argument("--decision", choices=("approve", "hold", "reject"), required=True)
    p.add_argument("--approver", required=True)
    p.add_argument("--note", default="")
    p.add_argument("--force", action="store_true", help="replace a hold/reject")
    p.set_defaults(func=cmd_approve)

    p = sub.add_parser("rule-flags", help="record human rulings on an attempt's issues")
    p.add_argument("--config", type=Path, required=True)
    p.add_argument("--slug", required=True)
    p.add_argument("--approver", required=True)
    p.add_argument("--rulings", type=Path, required=True,
                   help='JSON list of {"issue": id, "decision": ..., "note": ...}')
    p.set_defaults(func=cmd_rule_flags)

    p = sub.add_parser("build-exec-args", help="args for the execute workflow")
    p.add_argument("--config", type=Path, required=True)
    p.add_argument("--scratch-root", required=True)
    p.add_argument("--out", type=Path, default=None)
    p.set_defaults(func=cmd_build_exec_args)

    p = sub.add_parser("check-attempt", help="deterministic artefact gate")
    p.add_argument("attempt_dir", type=Path)
    p.add_argument("--plan", type=Path, default=None)
    p.add_argument("--comparison-schema", default=DEFAULT_COMPARISON_SCHEMA)
    p.add_argument("--image", default=None)
    p.add_argument("--forbid-sha256", action="append", default=[])
    p.add_argument("--code-manifest", type=Path, default=None,
                   help=f"authors' code manifest (default: <attempt>/{CODE_MANIFEST_FILE})")
    p.add_argument("--code-manifest-schema", default=DEFAULT_CODE_MANIFEST_SCHEMA)
    p.add_argument("--launch-commit", default=None,
                   help="the run's launch commit: anchors verify only against records that "
                        "existed, unchanged, at it (required for the authoritative gate)")
    p.add_argument("--legacy-attempt", action="store_true",
                   help=f"attempts listed in {LEGACY_ATTEMPTS_FILE} only (executed before "
                        f"gate 1.1): a missing manifest or snapshots warn instead of failing, "
                        f"and the attempt is marked ineligible for the current gate")
    p.add_argument("--out", default=None, help="report path, or - for stdout only")
    p.set_defaults(func=cmd_check_attempt)

    p = sub.add_parser("check-code", help="authors'-code integrity check only")
    p.add_argument("attempt_dir", type=Path)
    p.add_argument("--manifest", type=Path, default=None)
    p.add_argument("--code-manifest-schema", default=DEFAULT_CODE_MANIFEST_SCHEMA)
    p.add_argument("--launch-commit", default=None,
                   help="the run's launch commit (see check-attempt)")
    p.add_argument("--legacy-attempt", action="store_true",
                   help=f"attempts listed in {LEGACY_ATTEMPTS_FILE} only")
    p.add_argument("--out", default=None, help="report path, or - (default) for stdout only")
    p.set_defaults(func=cmd_check_code)

    p = sub.add_parser("snapshot-code", help="hash the attempt's code at an execution boundary")
    p.add_argument("attempt_dir", type=Path)
    p.add_argument("--phase", choices=SNAPSHOT_PHASES, required=True)
    p.add_argument("--force", action="store_true",
                   help="replace an existing snapshot (only when the run itself is redone)")
    p.set_defaults(func=cmd_snapshot_code)

    p = sub.add_parser("run-container",
                       help="run the attempt's code in the lane-owned container (gate 1.3)")
    p.add_argument("attempt_dir", type=Path)
    p.add_argument("--image", default=None, help="image tag; the run uses its immutable id")
    p.add_argument("--entry", default=None,
                   help="R or shell script to run, relative to the attempt directory")
    p.add_argument("--mount-path", default=None,
                   help="where the work copy is mounted (default: the image's WORKDIR)")
    p.add_argument("--launch-commit", default=None,
                   help="the run's launch commit, recorded for the gate's launcher binding")
    p.add_argument("--work-root", type=Path, default=None,
                   help="where the work copy is made (default: the system temporary "
                        "directory; use the attempt's filesystem for large data)")
    p.add_argument("--consume", action="append", default=[], metavar="RUN:PATH",
                   help="use an earlier run's collected output (run-NN:files/<path>); it is "
                        "copied into the work copy at <path> (repeatable)")
    p.add_argument("--keep-store", action="append", default=[], metavar="PATH",
                   help="keep a cache store (knitr cache, _freeze, .quarto, _targets) as a "
                        "declared input rather than removing it; an obligation (spec §9)")
    p.add_argument("--detach", action="store_true",
                   help="return once the container starts; finish with --finalise")
    p.add_argument("--finalise", metavar="RUN", default=None,
                   help="wait for a detached run (run-NN), then collect and seal it")
    p.add_argument("--keep-work", action="store_true",
                   help="keep the work copy after sealing, for debugging")
    p.add_argument("--clear-lock", action="store_true",
                   help="operator only: remove a stale lock once its container is gone")
    p.set_defaults(func=cmd_run_container)

    p = sub.add_parser("human-queue", help="rebuild the human queue from the gate reports")
    p.add_argument("--config", type=Path, required=True)
    p.add_argument("--workflow-result", type=Path, default=None,
                   help="the execute workflow's result JSON (or its human_queue list)")
    p.add_argument("--out", type=Path, default=None)
    p.set_defaults(func=cmd_human_queue)

    p = sub.add_parser("persist-results", help="persist executor/reviewer payloads")
    p.add_argument("--config", type=Path, required=True)
    p.add_argument("--run-dir", type=Path, required=True)
    p.add_argument("--force", action="store_true")
    p.add_argument("--record-unruled", action="store_true",
                   help="persist an ineligible gate 1.3 attempt, marked eligible: false")
    p.set_defaults(func=cmd_persist_results)

    p = sub.add_parser("audit-run", help="receipts, blinding, cost, wall-clock")
    p.add_argument("--config", type=Path, required=True)
    p.add_argument("--run-dir", type=Path, required=True)
    p.add_argument("--out", type=Path, default=None)
    p.set_defaults(func=cmd_audit_run)
    return parser


def main(argv: list[str] | None = None) -> int:
    """Dispatch a subcommand; LaneError becomes exit 1 with its message."""
    args = build_parser().parse_args(argv)
    if hasattr(args, "config") and isinstance(args.config, Path):
        args.config = expand(str(args.config))
    try:
        return args.func(args)
    except LaneError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
