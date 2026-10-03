#!/usr/bin/env python3
"""Deterministic orchestration helpers for the agentic reproduction lane.

**Version:** 1.0

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
``persist-plans``
    Read a completed plan workflow's journal, validate each planner payload
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
    The deterministic artefact gate (invariants 3, 5, 6): required files exist
    and are non-empty; ``comparisons/comparison.json`` validates; its target
    ids match the locked plan one-to-one; coverage is recomputed from the
    outcomes; publisher files are absent; the Docker image exists.
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
        [--plan FILE] [--image TAG] [--forbid-sha256 HEX ...] [--out FILE|-]
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
import re
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
# Coverage numerator (coverage-rules v1.0): reproduced exactly or within the
# pre-stated tolerance. MINOR_DISCREPANCY is outside tolerance by definition.
REPRODUCED_OUTCOMES = {"EXACT_MATCH", "WITHIN_PRECISION", "WITHIN_CONFIDENCE"}

# Single source of format truth with reproduction-system/workflows/*.js:
# every governed spawn prompt carries these lines verbatim. Change both
# together.
PROVENANCE_RE = re.compile(
    r"Provenance: run (\S+); launch commit ([0-9a-f]{40}); "
    r"reasoning effort pinned: (low|medium|high|xhigh|max)\.")
PAPER_RE = re.compile(r"^Paper: (\S+)$", re.MULTILINE)
SCRATCH_RE = re.compile(r"^Scratch directory: (\S+)$", re.MULTILINE)
ATTEMPT_DIR_RE = re.compile(r"^Attempt directory: (\S+)$", re.MULTILINE)
# Tokens in a Bash command that could name a local file: split on shell
# punctuation, then keep path-like tokens that are not URLs (a URL's path
# segment — e.g. a Wikipedia /wiki/ link — is not a local access).
SHELL_SPLIT_RE = re.compile(r"[\s'\"=;|&<>()`,]+")
DATE_SUFFIX_RE = re.compile(r"-\d{8}$")


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
        if (target_dir / PLAN_FILE).exists():
            raise LaneError(f"{paper['slug']}: {display_path(target_dir / PLAN_FILE)} "
                            f"already exists — this attempt has been planned")
        scratch = Path(args.scratch_root).expanduser() / config["run_id"] / paper["slug"]
        papers.append({"slug": paper["slug"],
                       "attempt_dir": str(target_dir),
                       **paper_inputs(paper),
                       "deposits": paper.get("deposits") or [],
                       "run_notes": str(paper.get("run_notes") or "").strip(),
                       "scratch_dir": str(scratch / "planner")})
    emit({"run_id": config["run_id"], "attempt": config["attempt"],
          "effort": config["effort"], "launch_commit": launch_commit,
          "agent_type": config["agents"]["planner"],
          "schema": runtime_schema(expand(config["schemas"]["plan"])),
          "blinding": blinding_args(config), "papers": papers}, args.out)
    return 0


def first_user_text(lines: list[str]) -> str:
    """The spawn prompt: the first user message's text in a transcript."""
    for line in lines:
        try:
            entry = json.loads(line)
        except json.JSONDecodeError:
            continue
        message = entry.get("message")
        if not isinstance(message, dict) or message.get("role") != "user":
            continue
        content = message.get("content")
        if isinstance(content, str):
            return content
        if isinstance(content, list):
            return "".join(str(b.get("text", "")) for b in content
                           if isinstance(b, dict) and b.get("type") == "text")
    return ""


def journal_results(run_dir: Path) -> list[dict]:
    """Every agent result recorded in a workflow run's journal.

    Returns:
        ``[{agent_id, agent_type, result, prompt}]`` — ``result`` is the
        agent's return value (``None`` when it died), ``prompt`` the spawn
        prompt from its transcript.

    Raises:
        LaneError: if the journal is missing.
    """
    journal = run_dir / "journal.jsonl"
    if not journal.is_file():
        raise LaneError(f"no journal.jsonl in {run_dir}")
    results = []
    for line in journal.read_text(encoding="utf-8").splitlines():
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
                        "prompt": first_user_text(lines)})
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
    emit({"run_id": config["run_id"], "attempt": config["attempt"],
          "effort": config["effort"], "launch_commit": launch_commit,
          "agent_types": {"executor": config["agents"]["executor"],
                          "reviewer": config["agents"]["reviewer"]},
          "schemas": {"execution": runtime_schema(expand(config["schemas"]["execution"])),
                      "review": runtime_schema(expand(config["schemas"]["review"]))},
          "comparison_schema_path": str(expand(config["schemas"]["comparison_record"])),
          "repo_root": str(REPO_ROOT),
          "blinding": blinding_args(config), "papers": papers, "skipped": skipped},
         args.out)
    return 0


def check_attempt(target_dir: Path, plan_path: Path, comparison_schema: dict,
                  image: str | None = None,
                  forbid_sha256: tuple[str, ...] = ()) -> dict:
    """The deterministic artefact gate for one attempt directory.

    Args:
        target_dir: The attempt directory.
        plan_path: The approved plan record (``reproduction-plan.json``).
        comparison_schema: The full comparison-record schema.
        image: Docker image tag that must exist locally, if given.
        forbid_sha256: Hashes of publisher files (paper, supplements) that
            must not appear anywhere in the attempt directory.

    Returns:
        A report dict with ``verdict`` ``pass`` or ``fail``, ``errors``,
        ``warnings``, and recomputed ``coverage``.
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
    return {"gate_version": "1.0", "checked_at": now_utc(),
            "attempt_dir": display_path(target_dir), "plan_file": display_path(plan_path),
            "plan_sha256": plan_digest, "locked_targets": len(locked),
            "verdict": "fail" if errors else "pass", "errors": errors,
            "warnings": warnings, "coverage": coverage,
            "executor_verdict": (comparison or {}).get("verdict")
            if isinstance(comparison, dict) else None}


def cmd_check_attempt(args: argparse.Namespace) -> int:
    """CLI wrapper for check_attempt(); exit 0 pass, 1 fail."""
    target_dir = args.attempt_dir.expanduser().resolve()
    plan_path = (args.plan or target_dir / PLAN_FILE).expanduser().resolve()
    schema = full_schema(expand(args.comparison_schema))
    report = check_attempt(target_dir, plan_path, schema, args.image,
                           tuple(args.forbid_sha256 or ()))
    if args.out == "-":
        print(json.dumps(report, indent=2))
    else:
        out = Path(args.out).expanduser() if args.out else target_dir / GATE_FILE
        write_json(out, report)
        print(json.dumps({k: report.get(k) for k in ("verdict", "errors", "warnings",
                                                       "coverage")}, indent=2))
    return 0 if report["verdict"] == "pass" else 1


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
    for access in reconcile.file_accesses(lines, gate):
        targets = [access["target"]] if access["tool"] == "Read" else \
            list(access.get("returned") or []) + [access["target"]]
        for target in targets:
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
        output_hits = [t for t in path_tokens(call["output"]) if blinding.hit(t)]
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
    p.add_argument("--out", default=None, help="report path, or - for stdout only")
    p.set_defaults(func=cmd_check_attempt)

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
