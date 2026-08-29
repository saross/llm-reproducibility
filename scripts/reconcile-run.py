#!/usr/bin/env python3
"""Post-run reconciliation of governed workflow spawns (plan C8 + C9).

**Version:** 1.5

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
   asserted. **Path rule (v1.5, F-010 ruling 2026-08-29):** an enumeration
   (Glob/Grep) is judged by the paths it *returned* — the content that
   entered the spawn's context — not by its pattern string. Any returned
   out-of-scope path is contamination; a truncated result list is
   unverifiable and also fails. An enumeration whose search root lies
   outside the allowed prefixes is additionally recorded as an
   `unscoped` enumeration — a warning-grade behavioural signal for the
   failure-mode register, never a verdict on its own.
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
    r"Evidence pack \(read in full\): (\S+) \(sha256 ([0-9a-fA-F]{64})\)")

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


GLOB_WILDCARDS = "*?["
# Harness enumeration results: Glob returns newline-separated paths (absolute,
# or relative to its base path), "No files found" when nothing matched, and a
# trailing parenthesised notice when the list was cut short; Grep returns
# "No matches found", a "Found N file(s)" header followed by paths, or
# "path:line:content" / "path-line-content" / "path:count" lines.
GLOB_EMPTY = "No files found"
GREP_EMPTY = "No matches found"
GREP_FOUND_RE = re.compile(r"^Found \d+ files?$")
GREP_LINE_RE = re.compile(r"^(?P<path>[^:\n]+?)[:-]\d+(?:[:-]|$)")
GREP_SINGLE_FILE_RE = re.compile(r"^\d+[:-]")
TRUNCATION_RE = re.compile(r"truncat", re.IGNORECASE)


def result_text(content) -> str:
    """Flatten a tool_result content field (string or text-block list)."""
    if isinstance(content, list):
        return "".join(str(part.get("text", "")) for part in content
                       if isinstance(part, dict))
    return str(content if content is not None else "")


def search_root(tool: str, call: dict) -> str:
    """The narrowest directory an enumeration could have touched, normalised.

    Glob: the base path joined with the pattern's literal (pre-wildcard)
    prefix; an absolute or home-anchored pattern ignores the base. Grep:
    the path argument. No base at all means the harness cwd — the repo
    root — which is exactly the unscoped case the F-010 ruling records.
    """
    base = str(call.get("path") or "")
    if tool == "Glob":
        pattern = str(call.get("pattern") or "")
        anchored = pattern.startswith("/") or pattern.startswith("~")
        literal: list[str] = []
        segments = pattern.split("/")
        for segment in segments:
            if any(ch in segment for ch in GLOB_WILDCARDS):
                break
            literal.append(segment)
        prefix = "/".join(literal)
        if len(literal) < len(segments) and prefix:
            prefix += "/"  # a wildcard followed: the literal part is a directory
        if anchored:
            root = prefix
        else:
            root = (base or str(REPO_ROOT)).rstrip("/") + "/" + prefix
    else:
        root = base or str(REPO_ROOT) + "/"
    if root.startswith("~/"):
        root = str(Path.home()) + root[1:]
    return normalise_path(root)


def resolve_returned(line: str, base: str) -> str:
    """Normalise one returned path; base-relative lines are re-rooted."""
    text = line.strip()
    if text.startswith("~/"):
        text = str(Path.home()) + text[1:]
    if not text.startswith("/"):
        text = (base or str(REPO_ROOT)).rstrip("/") + "/" + text
    return normalise_path(text)


def returned_paths(tool: str, call: dict, text: str) -> dict:
    """Parse an enumeration result into {paths, empty, truncated, unparsed}.

    `unparsed` lines are ones that could not be attributed to a path — the
    conservative reading is that unknown content entered context.
    """
    base = str(call.get("path") or "")
    lines = [ln for ln in text.splitlines() if ln.strip()]
    empty_marker = GLOB_EMPTY if tool == "Glob" else GREP_EMPTY
    if not lines or (len(lines) == 1 and lines[0].strip().startswith(empty_marker)):
        return {"paths": [], "empty": True, "truncated": False, "unparsed": []}
    paths: list[str] = []
    unparsed: list[str] = []
    truncated = False
    for line in lines:
        stripped = line.strip()
        if TRUNCATION_RE.search(stripped) and stripped.startswith(("(", "[")):
            truncated = True
            continue
        if tool == "Grep":
            if GREP_FOUND_RE.match(stripped):
                continue
            if GREP_SINGLE_FILE_RE.match(stripped) and base:
                # "N:content" — a grep whose path argument was one file
                paths.append(resolve_returned(base, ""))
                continue
            match = GREP_LINE_RE.match(stripped)
            if match:
                paths.append(resolve_returned(match.group("path"), base))
            elif "/" in stripped and " " not in stripped:
                paths.append(resolve_returned(stripped, base))
            else:
                unparsed.append(stripped[:120])
            continue
        paths.append(resolve_returned(stripped, base))
    seen: list[str] = []
    for path in paths:
        if path not in seen:
            seen.append(path)
    return {"paths": seen, "empty": False, "truncated": truncated,
            "unparsed": unparsed}


def file_accesses(lines: list[str], gate) -> list[dict]:
    """Every Read/Grep/Glob access in a transcript, with success status.

    Pairs each tool_use with its tool_result so an access records whether
    it actually succeeded: a failed Read of an out-of-scope path is an
    attempted access (warning-grade signal — path confusion), not
    contamination; only successful out-of-scope access fails a spawn.

    Reads carry `target` (the path). Enumerations (Glob/Grep) carry
    `target` = search root, `pattern`, and `returned` = the paths the
    harness handed back (v1.5 path rule) plus `truncated`/`unparsed`
    verifiability flags. v1.4 and earlier recorded a Glob's base `path`
    in preference to its pattern and never read its result — the F-012
    verifier error (an exact-filename existence check with base = repo
    root was reported as a repository-root listing).
    """
    import json as _json
    uses: list[tuple[str, str, dict]] = []
    errors: dict[str, bool] = {}
    results: dict[str, str] = {}
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
                uses.append((str(blk.get("id")), blk["name"], blk["input"]))
            elif blk.get("type") == "tool_result":
                use_id = str(blk.get("tool_use_id"))
                errors[use_id] = bool(blk.get("is_error"))
                results[use_id] = result_text(blk.get("content"))
    accesses: dict[tuple, dict] = {}
    for use_id, tool, call in uses:
        errored = errors.get(use_id, True)
        if tool == "Read":
            target = normalise_path(str(call.get("file_path") or ""))
            if not target:
                continue
            accesses.setdefault((tool, target, "", errored),
                                {"tool": tool, "target": target, "errored": errored})
            continue
        pattern = str(call.get("pattern") or "")
        root = search_root(tool, call)
        parsed = returned_paths(tool, call, results.get(use_id, ""))
        # An enumeration that succeeded but matched nothing enumerated no
        # content — the live 2026-08-03 case: a wrong-base-path glob over a
        # nonexistent tree. Downgrade to attempt (warning), like an errored
        # access.
        if not errored and parsed["empty"]:
            errored = True
        accesses.setdefault((tool, root, pattern, errored), {
            "tool": tool, "target": root, "pattern": pattern, "errored": errored,
            "returned": parsed["paths"], "truncated": parsed["truncated"],
            "unparsed": parsed["unparsed"]})
    return sorted(accesses.values(),
                  key=lambda a: (a["tool"], a["target"], a.get("pattern", ""), a["errored"]))


# v1.4 (arm-1 adjudication, 2026-08-17): when the pushed-instrument payload
# exceeds the harness's inline additionalContext threshold, the harness
# spills it to a per-spawn file under tool-results/ and the agent must Read
# it — that Read IS the push delivery (verified: the flagged file opens
# with the push hook's banner and carries the receipt tokens the spawn
# echoed). Scoring agents are read-only, so the pattern cannot be forged
# into existence by a spawn.
HOOK_DELIVERY_RE = re.compile(r"/tool-results/hook-[0-9a-f-]+-\d+-additionalContext\.txt$")


def access_allowed(target: str, allowed_prefixes: tuple[str, ...],
                   extra_allowed: tuple[str, ...], tool: str = "Read") -> bool:
    """True when a normalised target sits under an allowed prefix, or is a
    harness hook-delivery file read by the spawn (the push channel itself).

    v1.5: the hook-delivery exemption applies to Reads only. An enumeration
    that lists delivery files (F-002 listed other spawns' hook outputs) is
    out-of-scope content and must not inherit the exemption.
    """
    if tool == "Read" and HOOK_DELIVERY_RE.search(target):
        return True
    # A directory named without its trailing slash ("corpus") is inside the
    # scope its slashed prefix ("corpus/") describes.
    forms = (target, target.rstrip("/") + "/")
    return any(form.startswith(prefix)
               for prefix in tuple(allowed_prefixes) + tuple(extra_allowed)
               for form in forms)


def judge_access(access: dict, allowed_prefixes: tuple[str, ...],
                 extra_allowed: tuple[str, ...]) -> dict:
    """Apply the scope rule to one access; returns the access annotated with
    `flagged`, `contaminating`, `unscoped`, and `out_of_scope` (paths).

    Reads: flagged when the target is out of scope; contaminating when the
    read also succeeded. Enumerations (path rule, F-010 ruling): judged by
    the paths returned — contaminating when any returned path is out of
    scope, the list was truncated, or a result line could not be attributed
    to a path (unverifiable); an empty or errored enumeration is at most an
    attempt. `unscoped` records a search root outside the allowed prefixes
    regardless of what came back — the behavioural signal, not a verdict.
    """
    judged = dict(access)
    tool = access["tool"]
    if tool == "Read":
        allowed = access_allowed(access["target"], allowed_prefixes, extra_allowed, tool)
        judged.update({"flagged": not allowed,
                       "contaminating": not allowed and not access["errored"],
                       "unscoped": False, "out_of_scope": []})
        return judged
    root_ok = access_allowed(access["target"], allowed_prefixes, extra_allowed, tool)
    judged["unscoped"] = not root_ok
    if access["errored"]:
        judged.update({"flagged": not root_ok, "contaminating": False,
                       "out_of_scope": []})
        return judged
    out_of_scope = [path for path in access.get("returned", [])
                    if not access_allowed(path, allowed_prefixes, extra_allowed, tool)]
    unverifiable = bool(access.get("truncated")) or bool(access.get("unparsed"))
    # A grep rooted inside the allowed scope can only have returned content
    # from under that root; parse gaps there are recording noise, not risk.
    if tool == "Grep" and root_ok:
        unverifiable = False
    failed = bool(out_of_scope) or unverifiable
    judged.update({"flagged": failed, "contaminating": failed,
                   "out_of_scope": out_of_scope})
    return judged


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
               hooklib, require_pack: bool = False,
               contract_schema: dict | None = None) -> dict:
    """Re-run the gate's receipt checks post-hoc on a completed transcript."""
    problems: list[str] = []
    payload = gate.structured_output_from_transcript(lines)
    fields = gate.receipt_fields(payload) if payload else None
    if fields is None:
        return {"valid": False,
                "problems": ["no well-formed receipt payload in transcript"]}
    # v1.3 (S4 retreat, probed 2026-08-17): the spawn-side API rejects
    # top-level allOf, so schema v1.1's conditional requirements are
    # enforced HERE — the payload is validated in full against the
    # registered contract file (draft-07, jsonschema), which the runtime
    # variant could not carry.
    if contract_schema is not None:
        try:
            import jsonschema
            validator = jsonschema.Draft7Validator(contract_schema)
            for error in sorted(validator.iter_errors(payload),
                                key=lambda e: list(e.absolute_path)):
                path = "/".join(str(part) for part in error.absolute_path) or "(root)"
                problems.append(f"contract-schema violation at {path}: "
                                f"{error.message[:160]}")
        except ImportError:
            problems.append("contract-schema validation requested but "
                            "jsonschema is not importable")
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
    if require_pack and not pack:
        # v1.2 (audit F18): a silent regex non-match must not disable pack
        # verification — benchmark scoring spawns are launched with packs
        # by construction, so absence of a declaration is itself a fault.
        problems.append("no evidence-pack declaration found in transcript "
                        "(--require-pack set)")
    if pack:
        pack_path, pack_sha = pack
        pack_sha = pack_sha.lower()
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
            "paper_slug": str((payload or {}).get("paper_slug") or ""),
            # v1.2 (audit F7): the receipted VALUES are recorded, not just
            # their validity — the cross-arm receipt-identity check
            # (contract hardening 12) is mechanical over these.
            "receipted": {
                "instrument_versions": dict(fields["instrument_versions"]),
                "instrument_receipts": dict(fields["instrument_receipts"]),
                "model_id": str(fields["model_id"]).strip(),
                "agent_version": str(fields["agent_version"]).strip(),
            }}


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
              manifest: dict | None = None,
              expect_spawns: int | None = None,
              require_pack: bool = False,
              contract_schema: dict | None = None) -> dict:
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
        # v1.2 (audit F2): a transcript with NO meta sidecar or an EMPTY
        # agentType is unattributable — it fails the run rather than being
        # silently reclassified as ungoverned (a meta-write lag or partial
        # directory copy must shrink `clean`, never the denominator).
        if not agent_type:
            agents.append({
                "agent_id": agent_id,
                "agent_type": "",
                "receipts": {"valid": False,
                             "problems": ["unattributable transcript: missing "
                                          "meta sidecar or empty agentType"]},
                "file_access": {"all": [], "flagged": [], "contaminating": [],
                                "unscoped": []},
                "gate_events": [], "push": {"events": [], "problems": []},
                "divergence": {"no_gate_event": True,
                               "blocked_but_output_present": False},
                "reconciled": False,
            })
            continue
        if agent_type not in (manifest.get("agent_definitions") or {}):
            skipped_ungoverned.append({"agent_id": agent_id,
                                       "agent_type": agent_type})
            continue
        lines = transcript.read_text(encoding="utf-8").splitlines()

        validation = revalidate(lines, agent_type, manifest, gate, hooklib,
                                require_pack=require_pack,
                                contract_schema=contract_schema)
        accesses = [judge_access(a, allowed_prefixes, paper_paths_allowed)
                    for a in file_accesses(lines, gate)]
        flagged = [a for a in accesses if a["flagged"]]
        contaminating = [a for a in accesses if a["contaminating"]]
        unscoped = [a for a in accesses if a["unscoped"]]
        own_gate_events = [e for e in gate_events if e.get("agent_id") == agent_id]
        own_push_events = [e for e in push_events if e.get("agent_id") == agent_id]
        # v1.2 (audit F6): pushed-instrument BYTES are verified, not just the
        # version/token echo — each push event's logged sha256 is compared to
        # the registered C7 hash, and push-error events are problems.
        push_problems: list[str] = []
        registry = {s["name"]: s for s in hooklib.pushed_instruments(manifest, agent_type)}
        for event in own_push_events:
            if event.get("event") == "push-error":
                push_problems.append(f"push-error logged: {event.get('error', '?')}")
                continue
            spec = registry.get(str(event.get("name")))
            want = (spec or {}).get("registry_sha256", "")
            got = str(event.get("sha256") or "")
            if want and got and got != want:
                push_problems.append(
                    f"pushed bytes differ from registered hash: {event.get('name')} "
                    f"(pushed {got[:16]}…, registered {want[:16]}…)")
        if push_problems:
            validation["problems"] = list(validation.get("problems") or []) + push_problems
            validation["valid"] = False
        agents.append({
            "agent_id": agent_id,
            "agent_type": agent_type,
            "receipts": validation,
            "file_access": {"all": accesses, "flagged": flagged,
                            "contaminating": contaminating,
                            "unscoped": unscoped},
            "gate_events": [e.get("event") for e in own_gate_events],
            "push": {"events": [{k: e.get(k) for k in ("event", "name", "sha256")}
                                for e in own_push_events],
                     "problems": push_problems},
            "divergence": {
                "no_gate_event": not own_gate_events,
                "blocked_but_output_present": (
                    any(e.get("event") == "block" for e in own_gate_events)
                    and validation.get("valid", False)),
            },
            "reconciled": validation.get("valid", False) and not contaminating,
        })

    clean = all(a["reconciled"] for a in agents)
    count_problems: list[str] = []
    # v1.2 (audit F1): a reconciliation over ZERO governed spawns says
    # nothing and must never read as clean; with an expected count, the
    # denominator itself is asserted.
    if not agents:
        clean = False
        count_problems.append("no governed spawns found in run directory")
    if expect_spawns is not None and len(agents) != expect_spawns:
        clean = False
        count_problems.append(f"expected {expect_spawns} governed spawns, "
                              f"found {len(agents)}")
    return {
        # The report stamp lagged the tool (stuck at 1.2 through v1.3/1.4);
        # from v1.5 it tracks the module version.
        "reconciliation_version": "1.5",
        "run_dir": str(run_dir),
        "reconciled_at": datetime.now(timezone.utc).isoformat(),
        "agents": agents,
        "skipped_ungoverned": skipped_ungoverned,
        "spawns": len(agents),
        "spawns_reconciled": sum(a["reconciled"] for a in agents),
        "count_problems": count_problems,
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
    parser.add_argument("--expect-spawns", type=int, default=None,
                        help="assert exactly N governed spawns (audit F1: an "
                             "empty or partial directory must not read clean)")
    parser.add_argument("--require-pack", action="store_true",
                        help="every governed spawn must carry an evidence-pack "
                             "declaration (audit F18)")
    parser.add_argument("--contract-schema", type=Path, default=None,
                        help="validate each governed payload in full against "
                             "this JSON Schema file (S4 retreat: conditional "
                             "requirements enforce here, not spawn-side)")
    args = parser.parse_args()
    contract_schema = (json.loads(args.contract_schema.read_text(encoding="utf-8"))
                       if args.contract_schema else None)

    report = reconcile(args.run_dir.resolve(), DEFAULT_ALLOWED_PREFIXES,
                       args.gate_log, args.push_log,
                       tuple(args.allow),
                       expect_spawns=args.expect_spawns,
                       require_pack=args.require_pack,
                       contract_schema=contract_schema)
    out_dir = args.out or (args.run_dir / "reconciliation")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "reconciliation-report.json").write_text(
        json.dumps(report, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8")
    # v1.2 (audit F10): the gate/push log slices the docstring promises are
    # actually written — filtered to this run's agent ids, so the committed
    # artefact directory carries the full decision trail.
    run_ids = {a["agent_id"] for a in report["agents"]} | {
        s["agent_id"] for s in report["skipped_ungoverned"]}
    for log_path, slice_name in ((args.gate_log, "gate-log-slice.jsonl"),
                                 (args.push_log, "push-log-slice.jsonl")):
        entries = [e for e in load_log(log_path)
                   if e.get("agent_id") in run_ids]
        (out_dir / slice_name).write_text(
            "\n".join(json.dumps(e, ensure_ascii=False) for e in entries)
            + ("\n" if entries else ""), encoding="utf-8")

    for agent in report["agents"]:
        state = "OK " if agent["reconciled"] else "FAIL"
        flagged = len(agent["file_access"]["flagged"])
        contaminating = len(agent["file_access"]["contaminating"])
        unscoped = len(agent["file_access"].get("unscoped", []))
        warn = (f"; WARN {flagged - contaminating} failed out-of-scope attempt(s)"
                if flagged > contaminating else "")
        warn += f"; WARN {unscoped} unscoped enumeration(s)" if unscoped else ""
        print(f"[{state}] {agent['agent_type']} {agent['agent_id']}: "
              f"receipts {'valid' if agent['receipts']['valid'] else 'INVALID'}; "
              f"{contaminating} contaminating access(es){warn}; gate events "
              f"{agent['gate_events'] or ['NONE']}")
    for problem in report["count_problems"]:
        print(f"[FAIL] denominator: {problem}")
    print(f"reconciliation: {report['spawns_reconciled']}/{report['spawns']} clean "
          f"-> {out_dir / 'reconciliation-report.json'}")
    return 0 if report["clean"] else 1


if __name__ == "__main__":
    sys.exit(main())
