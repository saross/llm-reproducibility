#!/usr/bin/env python3
"""Post-run reconciliation of governed workflow spawns (plan C8 + C9).

**Version:** 1.1

The C2 probes established that SubagentStop gate decisions are advisory in
the workflow lane (a block is logged but the output is collected anyway)
and that hook-time transcript lag produces false-alarm blocks. This tool is
the authoritative backstop: after a workflow run, it re-derives every
verdict from the completed artefacts —

1. **Receipt re-validation (C9):** for each agent transcript, locate the
   structured output and validate its receipts against the manifest
   (instrument versions, receipt tokens, model pin, agent version,
   declared pulled reads verified against transcript Read calls) — the
   same checks as the live gate, run when the transcript is complete and
   lag cannot exist.
2. **File-access derivation (C8; amendment 1 §4):** list every Read, Grep,
   and Glob target in each transcript and flag any outside the allowed
   prefixes — the per-run file-access list §4 promises, plus the
   out-of-scope alarm that makes the read-scope rule verified rather than
   asserted.
3. **Divergence tripwire (Phase C contract):** compare hook-time gate
   events against spawns found on disk; blocks-with-collected-output and
   spawns-without-gate-events are named, never absorbed.
4. **Archival (audit S8):** the reconciliation report and the relevant
   gate/push log slices are written into the run's artefact directory, so
   run evidence is committed rather than living in a gitignored log.

Exit status: 0 when every spawn reconciles cleanly (valid receipts, no
out-of-scope reads); 1 otherwise — wire into D3 as a hard stop.

Usage:
    venv/bin/python scripts/reconcile-run.py <workflow-transcript-dir> \
        [--allow PREFIX ...] [--out DIR] [--gate-log PATH] [--push-log PATH]

Defaults: allowed prefixes cover the corpus store, the pull-reference
library, and test fixtures; the gate/push logs default to the live hook
logs; --out defaults to <dir>/reconciliation/.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.machinery
import importlib.util
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
HOOKS_DIR = REPO_ROOT / ".claude" / "hooks"

# D3 prep (2026-08-17): the benchmark workflow injects exactly this line per
# spawn (single source of format truth: fair-benchmark-arm.workflow.js); the
# reconciler verifies the pack's bytes still match the declared hash and that
# the spawn actually read the pack in full.
PACK_DECLARATION_RE = re.compile(
    r"Evidence pack \(read in full\): (\S+) \(sha256 ([0-9a-f]{64})\)")

DEFAULT_ALLOWED_PREFIXES = (
    "corpus/",
    "~/corpora/",
    ".claude/skills/research-assessor/references/",
    "tests/fixtures/",
)


def load_gate_module():
    """Import the receipt gate as a module (single source of validation truth)."""
    sys.path.insert(0, str(HOOKS_DIR))
    try:
        spec = importlib.util.spec_from_loader(
            "receipt_gate_for_reconciliation",
            importlib.machinery.SourceFileLoader(
                "receipt_gate_for_reconciliation",
                str(HOOKS_DIR / "subagent-receipt-gate.py")))
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    finally:
        sys.path.pop(0)


def normalise_path(raw: str) -> str:
    """Repo-relative form where possible; home-relative otherwise; else raw."""
    text = str(raw)
    for base, label in ((str(REPO_ROOT) + "/", ""), (str(Path.home()) + "/", "~/")):
        if text.startswith(base):
            return label + text[len(base):]
    return text


def file_accesses(lines: list[str], gate) -> list[dict]:
    """Every Read/Grep/Glob target in a transcript, with success status.

    Pairs each tool_use with its tool_result so an access records whether
    it actually succeeded: a failed Read of an out-of-scope path is an
    attempted access (warning-grade signal — path confusion), not
    contamination; only successful out-of-scope access fails a spawn.
    """
    import json as _json
    uses: list[tuple[str, str, str]] = []
    errors: dict[str, bool] = {}
    result_texts: dict[str, str] = {}
    for line in lines:
        try:
            entry = _json.loads(line)
        except _json.JSONDecodeError:
            continue
        content = ((entry.get("message") or {}).get("content")
                   if isinstance(entry.get("message"), dict) else entry.get("content"))
        if not isinstance(content, list):
            continue
        for blk in content:
            if not isinstance(blk, dict):
                continue
            if blk.get("type") == "tool_use" and blk.get("name") in ("Read", "Grep", "Glob") \
                    and isinstance(blk.get("input"), dict):
                call = blk["input"]
                target = call.get("file_path") or call.get("path") or call.get("pattern") or ""
                if target:
                    uses.append((str(blk.get("id")), blk["name"],
                                 normalise_path(str(target))))
            elif blk.get("type") == "tool_result":
                use_id = str(blk.get("tool_use_id"))
                errors[use_id] = bool(blk.get("is_error"))
                result_texts[use_id] = str(blk.get("content"))[:200]
    accesses: dict[tuple[str, str, bool], dict] = {}
    for use_id, tool, target in uses:
        errored = errors.get(use_id, True)
        # A Glob that succeeded but matched nothing enumerated no content —
        # the live 2026-08-03 case: a wrong-base-path glob over a
        # nonexistent tree. Downgrade to attempt (warning), like an
        # errored access.
        if tool == "Glob" and not errored \
                and "No files found" in result_texts.get(use_id, ""):
            errored = True
        accesses.setdefault((tool, target, errored),
                            {"tool": tool, "target": target, "errored": errored})
    return sorted(accesses.values(),
                  key=lambda a: (a["tool"], a["target"], a["errored"]))


def access_allowed(target: str, allowed_prefixes: tuple[str, ...],
                   extra_allowed: tuple[str, ...]) -> bool:
    """True when a normalised target sits under an allowed prefix."""
    return any(target.startswith(prefix)
               for prefix in tuple(allowed_prefixes) + tuple(extra_allowed))


def declared_pack(lines: list[str]) -> tuple[str, str] | None:
    """The workflow-prompt evidence-pack declaration, if any: (path, sha256).

    Scans raw transcript lines so the check is robust to message shape; the
    first declaration wins (one pack per scoring spawn by design).
    """
    for line in lines:
        match = PACK_DECLARATION_RE.search(line)
        if match:
            return match.group(1), match.group(2)
    return None


def revalidate(lines: list[str], agent_type: str, manifest: dict, gate,
               hooklib) -> dict:
    """Re-run the gate's receipt checks post-hoc on a completed transcript."""
    problems: list[str] = []
    payload = gate.structured_output_from_transcript(lines)
    fields = gate.receipt_fields(payload) if payload else None
    if fields is None:
        return {"valid": False,
                "problems": ["no well-formed receipt payload in transcript"]}
    for spec in hooklib.pushed_instruments(manifest, agent_type):
        if str(fields["instrument_versions"].get(spec["name"], "")).strip() != spec["version"]:
            problems.append(f"instrument version mismatch: {spec['name']}")
        if str(fields["instrument_receipts"].get(spec["name"], "")).strip() != spec["token"]:
            problems.append(f"receipt token mismatch: {spec['name']}")
    entry = hooklib.governed_agents(manifest).get(agent_type) or {}
    pinned = str(entry.get("model", "")).strip()
    if pinned and not gate.model_matches(str(fields["model_id"]).strip(), pinned):
        problems.append(f"model mismatch: {fields['model_id']!r}")
    expected = f"{agent_type} v{str(entry.get('version', '')).strip()}"
    if str(fields["agent_version"]).strip() != expected:
        problems.append(f"agent_version mismatch: {fields['agent_version']!r}")
    calls = gate.read_calls(lines)
    for declared in fields["pulled_files_read"]:
        declared_path = str(declared).strip()
        if not declared_path:
            problems.append("empty pulled path declared")
            continue
        matching = [c for c in calls
                    if declared_path in str(c["input"].get("file_path", ""))]
        successful = [c for c in matching if not c["error"]]
        if not matching:
            problems.append(f"declared pull not in transcript: {declared_path}")
        elif not successful:
            problems.append(f"declared pull attempted but every Read errored "
                            f"(never actually read): {declared_path}")
        elif not any("limit" not in c["input"] and "offset" not in c["input"]
                     for c in successful):
            problems.append(f"declared pull truncated: {declared_path}")

    # D3 pack verification (amendment 2 §2): a workflow-declared evidence
    # pack must still hash to its declared value AND have been fully read —
    # the attempts-are-not-reads rule applies to packs exactly as to pulls.
    pack = declared_pack(lines)
    if pack:
        pack_path, pack_sha = pack
        try:
            actual = hashlib.sha256((REPO_ROOT / pack_path).read_bytes()).hexdigest()
        except OSError:
            actual = None
        if actual is None:
            problems.append(f"declared evidence pack missing on disk: {pack_path}")
        elif actual != pack_sha:
            problems.append(f"evidence pack sha256 drift: {pack_path}")
        pack_calls = [c for c in calls
                      if pack_path in str(c["input"].get("file_path", ""))]
        pack_ok = [c for c in pack_calls if not c["error"]]
        if not pack_calls:
            problems.append(f"declared evidence pack never read: {pack_path}")
        elif not pack_ok:
            problems.append(f"evidence pack read attempted but every Read "
                            f"errored (never actually read): {pack_path}")
        elif not any("limit" not in c["input"] and "offset" not in c["input"]
                     for c in pack_ok):
            problems.append(f"evidence pack read truncated: {pack_path}")
    return {"valid": not problems, "problems": problems,
            "paper_slug": str((payload or {}).get("paper_slug") or "")}


def load_log(path: Path) -> list[dict]:
    """Best-effort JSONL load (missing log = empty list, reported upstream)."""
    try:
        return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()
                if line.strip()]
    except OSError:
        return []


def reconcile(run_dir: Path, allowed_prefixes: tuple[str, ...],
              gate_log_path: Path, push_log_path: Path,
              paper_paths_allowed: tuple[str, ...] = (),
              manifest: dict | None = None) -> dict:
    """Reconcile every agent transcript in a workflow run directory.

    `manifest` is injectable for tests; the live default is the repo
    manifest — the same single source of truth the hooks use.
    """
    gate = load_gate_module()
    sys.path.insert(0, str(HOOKS_DIR))
    try:
        import hooklib
    finally:
        sys.path.pop(0)
    if manifest is None:
        manifest = hooklib.load_manifest()

    gate_events = load_log(gate_log_path)
    push_events = load_log(push_log_path)

    agents = []
    skipped_ungoverned = []
    for transcript in sorted(run_dir.glob("agent-*.jsonl")):
        agent_id = transcript.stem.replace("agent-", "")
        meta_path = transcript.parent / f"{transcript.stem}.meta.json"
        meta = json.loads(meta_path.read_text(encoding="utf-8")) if meta_path.is_file() else {}
        agent_type = str(meta.get("agentType") or "")
        # v1.1: only governed agent types are reconciled. The D3 workflow's
        # per-item reconcile agents (general-purpose, mechanical) write
        # transcripts into the same run directory; validating them as
        # governed spawns would poison every report. They are counted, not
        # judged — the governed set is the reconciliation's whole subject.
        if agent_type not in (manifest.get("agent_definitions") or {}):
            skipped_ungoverned.append({"agent_id": agent_id,
                                       "agent_type": agent_type})
            continue
        lines = transcript.read_text(encoding="utf-8").splitlines()

        validation = revalidate(lines, agent_type, manifest, gate, hooklib)
        accesses = file_accesses(lines, gate)
        flagged = [a for a in accesses
                   if not access_allowed(a["target"], allowed_prefixes,
                                         paper_paths_allowed)]
        contaminating = [a for a in flagged if not a["errored"]]
        own_gate_events = [e for e in gate_events if e.get("agent_id") == agent_id]
        own_push_events = [e for e in push_events if e.get("agent_id") == agent_id]
        agents.append({
            "agent_id": agent_id,
            "agent_type": agent_type,
            "receipts": validation,
            "file_access": {"all": accesses, "flagged": flagged,
                            "contaminating": contaminating},
            "gate_events": [e.get("event") for e in own_gate_events],
            "push_events": len(own_push_events),
            "divergence": {
                "no_gate_event": not own_gate_events,
                "blocked_but_output_present": (
                    any(e.get("event") == "block" for e in own_gate_events)
                    and validation.get("valid", False)),
            },
            "reconciled": validation.get("valid", False) and not contaminating,
        })

    clean = all(a["reconciled"] for a in agents)
    return {
        "reconciliation_version": "1.1",
        "run_dir": str(run_dir),
        "reconciled_at": datetime.now(timezone.utc).isoformat(),
        "agents": agents,
        "skipped_ungoverned": skipped_ungoverned,
        "spawns": len(agents),
        "spawns_reconciled": sum(a["reconciled"] for a in agents),
        "clean": clean,
    }


def main() -> int:
    """CLI entry point; exit 1 unless every spawn reconciles cleanly."""
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("run_dir", type=Path)
    parser.add_argument("--allow", action="append", default=[],
                        help="additional allowed path prefix (repeatable)")
    parser.add_argument("--out", type=Path, default=None)
    parser.add_argument("--gate-log", type=Path,
                        default=HOOKS_DIR / "receipt-gate-log.jsonl")
    parser.add_argument("--push-log", type=Path,
                        default=HOOKS_DIR / "push-receipts.jsonl")
    args = parser.parse_args()

    report = reconcile(args.run_dir.resolve(), DEFAULT_ALLOWED_PREFIXES,
                       args.gate_log, args.push_log,
                       tuple(args.allow))
    out_dir = args.out or (args.run_dir / "reconciliation")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "reconciliation-report.json").write_text(
        json.dumps(report, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8")

    for agent in report["agents"]:
        state = "OK " if agent["reconciled"] else "FAIL"
        flagged = len(agent["file_access"]["flagged"])
        contaminating = len(agent["file_access"]["contaminating"])
        warn = (f"; WARN {flagged - contaminating} failed out-of-scope attempt(s)"
                if flagged > contaminating else "")
        print(f"[{state}] {agent['agent_type']} {agent['agent_id']}: "
              f"receipts {'valid' if agent['receipts']['valid'] else 'INVALID'}; "
              f"{contaminating} contaminating access(es){warn}; gate events "
              f"{agent['gate_events'] or ['NONE']}")
    print(f"reconciliation: {report['spawns_reconciled']}/{report['spawns']} clean "
          f"-> {out_dir / 'reconciliation-report.json'}")
    return 0 if report["clean"] else 1


if __name__ == "__main__":
    sys.exit(main())
