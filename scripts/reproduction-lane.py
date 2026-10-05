#!/usr/bin/env python3
"""Deterministic orchestration helpers for the agentic reproduction lane.

**Version:** 1.2

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
    Hash every code file in an attempt directory into
    ``execution-snapshots/<phase>.json``. The executor runs ``--phase pre``
    immediately before the container run and ``--phase post`` immediately
    after; the gate compares both with the tree it finds.
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
    deduplicated per API request, API-equivalent cost, and wall-clock.

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
    venv/bin/python scripts/reproduction-lane.py snapshot-code <attempt-dir> \\
        --phase pre|post [--force]
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
import hashlib
import importlib.machinery
import importlib.util
import json
import os
import re
import secrets
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from types import ModuleType
from typing import Any

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
GATE_VERSION = "1.2"
# Authors'-code integrity (gate 1.1; Shawn's ruling 2026-10-04, fail-and-uplift
# follow-on 3): the authors' files are hashed at retrieval and every executed
# copy must be byte-identical. Any difference is a declared wrapper or a
# flagged edit; an undeclared difference fails the gate.
CODE_MANIFEST_FILE = "authors-code-manifest.json"
DEFAULT_CODE_MANIFEST_SCHEMA = "reproduction-system/schemas/authors-code-manifest.json"
# File suffixes (lower-cased) treated as code in the closed-world inventory;
# names beginning "Dockerfile" count too. Since gate 1.2 nothing is exempt:
# code under outputs/ is inventoried like any other (review of PR #7: an
# edited copy placed there and sourced by a wrapper went unseen).
CODE_SUFFIXES = frozenset({".r", ".rmd", ".qmd", ".rnw", ".py", ".ipynb", ".sh", ".jl",
                           ".do", ".m", ".sql", ".stan", ".js"})
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
    """True when ``path`` counts as code for the closed-world inventory."""
    return path.name.lower().startswith("dockerfile") or path.suffix.lower() in CODE_SUFFIXES


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


def registry_principal_links(repo_root: Path, slug: str) -> list[dict] | None:
    """A paper's principal links in the curated declared-links registry.

    Returns:
        The links whose ``role`` is ``principal``, or None when the registry
        is not committed and clean (it then cannot vouch for anything).
    """
    if committed_unmodified(repo_root, DEFAULT_REGISTRY) is not None:
        return None
    registry = yaml.safe_load((repo_root / DEFAULT_REGISTRY).read_text(encoding="utf-8")) or {}
    spec = (registry.get("papers") or {}).get(slug) or {}
    return [link for link in spec.get("links") or [] if link.get("role") == "principal"]


def registry_selected_dois(repo_root: Path, slug: str) -> set[str] | None:
    """The deposit versions the registry selects for a paper (AP-12).

    For each principal link, its ``scored_version`` if it has one, else the
    link itself.

    Returns:
        Lower-cased identifiers, or None when the registry is not committed
        and clean.
    """
    links = registry_principal_links(repo_root, slug)
    if links is None:
        return None
    return {str(link.get("scored_version") or link.get("link") or "").lower()
            for link in links}


def git_blob_sha1(data: bytes) -> str:
    """The git object id of a file's bytes, as ``git hash-object`` computes it."""
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def verify_anchor(item: dict, target_dir: Path, repo_root: Path, slug: str | None,
                  original: bytes | None) -> tuple[str, list[str], list[str]]:
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

    Returns:
        ``(state, errors, flags)``. ``state`` is ``verified`` (a committed,
        independent record vouches for the bytes), ``recorded`` (a checkable
        claim the gate cannot settle), ``failed``, or ``absent``.
    """
    oid = item["id"]
    anchor = item.get("anchor") or {}
    if not anchor or anchor.get("kind") == "none":
        reason = f" ({anchor['reason']})" if anchor.get("reason") else ""
        return "absent", [], [f"{FLAG_PREFIX}original {oid!r} has no independent provenance "
                              f"anchor{reason}: its identity rests on the executor's own "
                              f"manifest, which cannot show the file was unedited when hashed"]
    kind = anchor["kind"]

    def failed(message: str) -> tuple[str, list[str], list[str]]:
        return "failed", [f"original {oid!r}: provenance anchor ({kind}): {message}"], []

    if kind == "evidence-pack":
        problem = committed_unmodified(repo_root, anchor["pack"])
        if problem:
            return failed(problem)
        pack = json.loads((repo_root / anchor["pack"]).read_text(encoding="utf-8"))
        record = next((r for r in pack.get("records") or []
                       if r.get("record_id") == anchor["record_id"]
                       and r.get("status") == "resolved"), None)
        if record is None:
            return failed(f"no resolved record {anchor['record_id']} in {anchor['pack']}")
        fields = record.get("fields") or {}
        entry = next((f for f in fields.get("files") or [] if f.get("key") == anchor["file"]),
                     None)
        algorithm, _, expected = str((entry or {}).get("checksum") or "").partition(":")
        if not expected or algorithm not in hashlib.algorithms_available:
            return failed(f"{anchor['record_id']} publishes no usable checksum for "
                          f"{anchor['file']!r}")
        deposit_rel = (item.get("archive") or {}).get("path") or item.get("local_copy")
        deposit = resolve_stored(target_dir, deposit_rel) if deposit_rel else None
        if deposit is None or not deposit.is_file():
            return failed(f"the deposit file {anchor['file']!r} is not kept (archive.path or "
                          f"local_copy), so its published checksum cannot be checked")
        if hashlib.new(algorithm, deposit.read_bytes()).hexdigest() != expected.lower():
            return failed(f"{deposit_rel} does not match the {algorithm} checksum that "
                          f"{anchor['record_id']} publishes for {anchor['file']!r}")
        if original is None:
            return "failed", [], []  # the member or copy mismatch is already an error
        selected = registry_selected_dois(repo_root, slug) if slug else None
        doi = str(fields.get("doi") or "").lower()
        if selected is None:
            return "recorded", [], [f"{FLAG_PREFIX}original {oid!r}: the registry is not "
                                    f"committed and clean, so the anchored version cannot be "
                                    f"checked against the version AP-12 selects"]
        if doi not in selected:
            return "recorded", [], [f"{FLAG_PREFIX}original {oid!r} is anchored to {doi or '?'}, "
                                    f"which is not a version the registry selects for {slug} "
                                    f"(AP-12): {sorted(selected) or 'none'}"]
        return "verified", [], []

    if kind == "corpus-manifest":
        if slug is None or anchor["entry"] != slug:
            return failed(f"the corpus entry {anchor['entry']!r} is not this paper ({slug!r})")
        problem = committed_unmodified(repo_root, anchor["manifest"])
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
        if sha256_file(stored) != recorded:
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
        links = registry_principal_links(repo_root, slug)
        role = str(record.get("role") or "unstated")
        in_supplement = bool(links) and any(link.get("home") == "supplement" for link in links)
        if role != "supplement" or not in_supplement:
            reason = ("the registry is not committed and clean" if links is None else
                      f"the corpus role is {role!r}" if role != "supplement" else
                      f"the registry declares no principal artefact held in {slug}'s "
                      f"journal supplement")
            return "recorded", [], [f"{FLAG_PREFIX}original {oid!r} is anchored to corpus file "
                                    f"{anchor['entry']}/{anchor['filename']}, which establishes "
                                    f"its bytes but not that it is this paper's selected "
                                    f"original: {reason}. A deposit kept in the corpus store is "
                                    f"anchored through its evidence-pack record instead"]
        # A transcription stays "recorded": its fidelity is flagged by the caller.
        return ("recorded" if derivation else "verified"), [], []

    if kind == "git":
        if original is None:
            return failed("the original's bytes are not recoverable to compare with the blob")
        if git_blob_sha1(original) != str(anchor["blob_sha1"]).lower():
            return failed(f"blob {anchor['blob_sha1']} does not match the original's bytes")
        return "recorded", [], [f"{FLAG_PREFIX}original {oid!r} is anchored to blob "
                                f"{anchor['blob_sha1'][:12]}… at {anchor['repository']}@"
                                f"{anchor['commit'][:12]}:{anchor['path']}, a claim the gate "
                                f"cannot verify offline: a reviewer confirms it at the remote"]
    return failed(f"unknown anchor kind {kind!r}")


def code_inventory(target_dir: Path) -> dict[str, str]:
    """sha256 of every code file in the attempt tree, keyed by relative path.

    Nothing is exempt (gate 1.2), except bytecode caches and the snapshot
    records themselves.
    """
    files: dict[str, str] = {}
    for path in sorted(target_dir.rglob("*")) if target_dir.is_dir() else []:
        rel = path.relative_to(target_dir)
        if (not path.is_file() or "__pycache__" in rel.parts or rel.parts[0] == SNAPSHOT_DIR
                or not is_code_file(path)):
            continue
        files[rel.as_posix()] = sha256_file(path)
    return files


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
    record["files"] = code_inventory(target_dir)
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


def conversion_evidence_flag(target_dir: Path, item: dict) -> str | None:
    """Validate a conversion wrapper's value-identity evidence (PR #7 review, finding 3).

    The ruled condition is that every converted value is unchanged. The
    wrapper declares the conversion it performs (``conversion: {input,
    output}``). The evidence must be a JSON record: ``{"check":
    "value-identity", "result": "identical", "converter": {"path",
    "sha256"}, "input": {"path", "sha256"}, "output": {"path", "sha256"},
    "values_compared": n, "values_total": n}``. It must name this wrapper at
    its current digest and the declared input and output (so a valid record
    for some other conversion cannot clear the flag: PR #7 delta review,
    finding 3), be current, and cover every value.

    Returns:
        None when the evidence is valid, else a flag naming why it is not:
        missing, unreadable, failed, unbound, stale, or incomplete.
    """
    head = f"{FLAG_PREFIX}conversion wrapper {item['path']}: value-identity evidence "
    rel = item.get("value_identity_check")
    path = inside(target_dir, rel) if rel else None
    if path is None or not path.is_file():
        return head + f"missing ({rel or 'none named'}); a format conversion is allowed only " \
                      f"with a mechanical value-identity check"
    try:
        evidence = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, UnicodeDecodeError):
        evidence = None
    if not isinstance(evidence, dict) or evidence.get("check") != "value-identity":
        return head + f"unreadable: {rel} is empty or not a value-identity record"
    if evidence.get("result") != "identical":
        return head + f"failed: {rel} reports result {evidence.get('result')!r}"
    declared = item.get("conversion") if isinstance(item.get("conversion"), dict) else {}
    if not declared.get("input") or not declared.get("output"):
        return head + "unbound: the wrapper declares no conversion input and output, so no " \
                      "evidence can be tied to it"
    converter = evidence.get("converter") if isinstance(evidence.get("converter"), dict) else {}
    wrapper = inside(target_dir, item["path"])
    if (converter.get("path") != item["path"] or wrapper is None or not wrapper.is_file()
            or converter.get("sha256") != sha256_file(wrapper)):
        return head + f"unbound: {rel} does not name this converter ({item['path']}) at its " \
                      f"current sha256"
    for side in ("input", "output"):
        named = (evidence.get(side) or {}).get("path") if isinstance(evidence.get(side),
                                                                      dict) else None
        if named != declared[side]:
            return head + f"unbound: {rel} covers {side} {named!r}, not the declared " \
                          f"{declared[side]!r}"
    for side in ("input", "output"):
        spec = evidence.get(side) if isinstance(evidence.get(side), dict) else {}
        target = resolve_stored(target_dir, str(spec.get("path") or ""))
        if (not spec.get("sha256") or target is None or not target.is_file()
                or sha256_file(target) != spec["sha256"]):
            return head + f"stale: its {side} ({spec.get('path') or 'unnamed'}) is missing or " \
                          f"no longer matches the recorded sha256"
    compared, total = evidence.get("values_compared"), evidence.get("values_total")
    if not (isinstance(compared, int) and isinstance(total, int) and total > 0
            and compared == total):
        return head + f"incomplete: {compared!r} of {total!r} values compared"
    return None


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


def check_code_integrity(target_dir: Path, manifest_path: Path, schema: dict,
                         comparison: dict | None = None, plan_slug: str | None = None,
                         legacy: bool = False, anchor_root: Path | None = None) -> dict:
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
            flags.append(f"{FLAG_PREFIX}original {oid!r} has no pristine copy in the attempt "
                         f"directory: byte identity rests on the recorded hash alone, and no "
                         f"wrapper can be checked for an inlined copy of it")
        state, anchor_errors, anchor_flags = verify_anchor(
            item, target_dir, repo_root, manifest["paper_slug"], original_bytes.get(oid))
        result["anchors"][oid] = state
        errors.extend(anchor_errors)
        flags.extend(anchor_flags)
        if item.get("derivation"):
            flags.append(f"{FLAG_PREFIX}original {oid!r} is a {item['derivation']['method']} "
                         f"of {item['derivation'].get('from') or 'another file'}: a "
                         f"deterministic transcription shows repeatability, not fidelity to "
                         f"the page, so a human checks the consequential code against the "
                         f"source")

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
        flags.append(f"{FLAG_EDIT_PREFIX}{item['path']} differs from original "
                     f"{item['original']!r}; {size_text}; kind {edit.get('kind', 'unstated')}; "
                     f"affected targets {edit['affected_targets'] or 'none stated'}; declared: "
                     f"{edit['summary']}. Declaring an edit does not make a repaired result "
                     f"creditable")
        for target in edit["affected_targets"]:
            if target in credited:
                flags.append(f"{FLAG_PREFIX}target {target} is credited ({credited[target]}) "
                             f"but rests on the flagged edit to {item['path']} — a repaired "
                             f"result never counts toward coverage or the verdict (queued "
                             f"amendment 3, item 7(d))")

    if originals and not executed:
        flags.append(f"{FLAG_PREFIX}no authors' file is listed as executed: every result "
                     f"rests on the reproducer's own code (a re-implementation is not the "
                     f"authors' code run unmodified)")

    # -- Wrappers: exist, are separate files, and do not inline authors' code.
    wrapper_paths: set[Path] = set()
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
            flags.append(f"{FLAG_PREFIX}{item['path']} is code the run generated: the gate "
                         f"cannot show it was not executed, so a human confirms what made it "
                         f"and that nothing ran it")
            continue
        if item["role"] == "conversion":
            flag = conversion_evidence_flag(target_dir, item)
            if flag:
                flags.append(flag)
        text = data.decode("utf-8", errors="replace")
        mine = substantive_lines(text)
        for oid, original in original_bytes.items():
            shared = mine & substantive_lines(original.decode("utf-8", errors="replace"))
            if len(shared) >= EMBEDDED_LINES_FLAG:
                flags.append(f"{FLAG_PREFIX}wrapper {item['path']} embeds {len(shared)} "
                             f"substantive line(s) of authors' original {oid!r} (a heuristic "
                             f"for verbatim inlining) — inlined authors' code is an edited "
                             f"copy unless the original file is what runs")
        if DYNAMIC_EVAL_RE.search(text):
            obligations.append(f"{item['path']} evaluates code dynamically (parse, eval, "
                               f"source of a computed path, or exec): confirm it evaluates "
                               f"only the declared authors' files, unmodified")
        if path.name.lower().startswith("dockerfile") and DOCKER_FETCH_RE.search(text):
            obligations.append(f"{item['path']} brings content into the image from outside "
                               f"the attempt directory: confirm none of it is analysis code")

    # -- Code paths the wrappers name must be declared, and never generated code.
    declared_paths = executed_paths | pristine_paths | wrapper_paths
    for wrapper in sorted(wrapper_paths):
        if not wrapper.is_file():
            continue
        text = wrapper.read_text(encoding="utf-8", errors="replace")
        for literal in sorted(set(CODE_REF_RE.findall(text))):
            rel = re.sub(r"^(?:/project/|\./)", "", literal)
            named = inside(target_dir, rel)
            wrapper_rel = wrapper.relative_to(target_dir.resolve()).as_posix()
            if named is not None and named in generated_paths:
                errors.append(f"wrapper {wrapper_rel} loads {rel}, which the run generated: "
                              f"generated code is never an authors' file or a declared "
                              f"wrapper")
            elif named is None or not named.is_file():
                obligations.append(f"{wrapper_rel} names code {literal!r} that is not in the "
                                   f"attempt directory: confirm where it comes from")
            elif named not in declared_paths:
                errors.append(f"wrapper {wrapper_rel} names undeclared code {rel}")
    if wrapper_paths:
        obligations.append("wrapper semantics are not verified by the gate: its line-overlap "
                           "check is a heuristic, so the reviewer confirms that each wrapper "
                           "only mechanises the authors' code (paths, seeds, capture)")

    # -- Closed-world inventory: every code file anywhere is accounted for.
    current = code_inventory(target_dir)
    known = declared_paths | generated_paths
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

    # -- Execution snapshots: what the run could execute is what the gate sees.
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
    if docs["pre"] is None or docs["post"] is None or structural:
        message = (f"execution snapshots missing, unreadable, or not a bound pair "
                   f"({SNAPSHOT_DIR}/pre.json and post.json, taken by snapshot-code around the "
                   f"container run): the gate cannot show which code the run executed"
                   + (f" ({'; '.join(structural)})" if structural else ""))
        (warnings if legacy else errors).append(message)
    else:
        pre, post = docs["pre"]["files"], docs["post"]["files"]
        generated_rel = {p.relative_to(target_dir.resolve()).as_posix() for p in generated_paths}
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

    if errors:
        result["status"] = "fail"
    elif flags:
        result["status"] = "flagged"
    elif not originals:
        result["status"] = "no-authors-code"
    else:
        result["status"] = "identical"
    return result


def check_attempt(target_dir: Path, plan_path: Path, comparison_schema: dict,
                  image: str | None = None,
                  forbid_sha256: tuple[str, ...] = (),
                  code_manifest: Path | None = None,
                  code_manifest_schema: dict | None = None,
                  legacy_attempt: bool = False,
                  legacy_list: Path | None = None,
                  anchor_root: Path | None = None) -> dict:
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
        plan_slug=plan_slug, legacy=legacy, anchor_root=anchor_root)
    errors += [f"code integrity: {e}" for e in integrity["errors"]]
    warnings += integrity["warnings"] + integrity["flags"]
    return {"gate_version": GATE_VERSION, "checked_at": now_utc(),
            "attempt_dir": display_path(target_dir), "plan_file": display_path(plan_path),
            "plan_sha256": plan_digest, "locked_targets": len(locked),
            "verdict": "fail" if errors else "pass", "errors": errors,
            "warnings": warnings, "flags": integrity["flags"],
            "review_obligations": integrity["review_obligations"], "coverage": coverage,
            "eligible_for_current_gate": integrity["eligible_for_current_gate"],
            "code_integrity": {k: integrity[k] for k in (
                "status", "manifest", "manifest_sha256", "originals", "executed",
                "wrappers", "anchors", "snapshots")},
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
                           legacy_attempt=args.legacy_attempt)
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
                                  comparison=comparison, legacy=legacy)
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
    """CLI wrapper for write_snapshot(): record one execution boundary."""
    target_dir = args.attempt_dir.expanduser().resolve()
    out = write_snapshot(target_dir, args.phase, force=args.force)
    files = json.loads(out.read_text(encoding="utf-8"))["files"]
    print(f"wrote {display_path(out)} ({len(files)} code file(s))")
    return 0


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
    report = {"run_id": config["run_id"], "built_at": now_utc(), "queue": queue,
              "problems": problems, "lost_in_relay": lost}
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
            provenance = PROVENANCE_RE.search(item["prompt"])
            write_json(path, {"record_version": "1.0", "run_id": config["run_id"],
                              "workflow_run": run_dir.name, "agent_id": item["agent_id"],
                              "agent_type": item["agent_type"],
                              "launch_commit": provenance.group(2) if provenance else None,
                              "effort": provenance.group(3) if provenance else None,
                              "persisted_at": now_utc(), "orchestrator_notes": notes,
                              "payload": payload})
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
