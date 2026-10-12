#!/usr/bin/env python3
"""SubagentStop receipt gate (routing design §3.2–§3.3; hardened 2026-08-03).

For governed agents (registered in manifest `agent_definitions`), validates
the layered read receipts in the agent's structured output:

- delivery check — `instrument_versions` matches the manifest per pushed
  instrument (catches stale-file pushes);
- consumption check — `instrument_receipts` quotes each end-of-file receipt
  token (for pulled instruments this defeats header-only reads; for pushed
  instruments the token is present in the injected context, so this check
  evidences delivery-and-echo rather than independent consumption — audit
  2026-08-03 M10);
- identity check — `model_id` matches the manifest's pinned model for the
  agent, tolerating the harness's ``[1m]`` context-window marker suffix
  (hard gate, review D-7; marker observed on the 2026-08-03 opus arm);
- version check — `agent_version` matches "<agent_type> v<registry version>";
- pull check — every path declared in `pulled_files_read` was read in full:
  a successful Read call with no `limit`/`offset`, or (since 2026-10-12, the
  gate 1.3 final review's F2) a successful Bash `cat`, `less`, `more`, or
  `nl` whose output was not truncated, or was spilled to a file the agent
  then Read in full. `head`, `tail`, `sed`, `awk`, and `cut` reads are
  partial and `grep` is a search, so none of them verifies a declared pull.
  Transcripts are written asynchronously and can lag — the hook retries
  briefly before blocking (review D-12).

The structured output is located in the final assistant message OR, for
workflow-lane spawns whose schema-forced output rides a structured-output
tool call, in the transcript's tool_use inputs (audit 2026-08-03 C4: the
final-message-only search blocked every workflow spawn once).

`status: ESCALATE` outputs are passed through to the orchestrator ONLY after
the receipt and model-identity checks pass — escalation is a valid outcome,
but it is not an exemption from provenance (audit 2026-08-03 C5). An
ESCALATE that carries a result (a verdict, a review, or a target list) must
also pass the pull check (2026-10-12, F2: the herskind pilot's executor
returned a complete SUCCESSFUL result as ESCALATE and so was never checked).

Fail-closed (policy decided ONCE for both hooks, audit item 3, 2026-08-14):
unexpected payload shapes, unattributable events (unparseable or non-object
stdin, undecodable bytes — M-2), hook-environment import failures, and
internal errors all block rather than crash-allow (audit 2026-08-03 C9).
Unattributable-event blocks name the fault class so an operator reads them
as environment/parse faults, not receipt verdicts (pre-run audit N2). On
failure the hook returns `decision: "block"` with the reason, re-prompting
the same subagent instead of failing the batch item (§3.2 self-healing).
"""

from __future__ import annotations

import fnmatch
import json
import posixpath
import re
import shlex
import sys
import time
from pathlib import Path

# Fail-closed import (mirrors preflight-agent.py, audit item 3 2026-08-14):
# if the shared library or PyYAML is unavailable, block rather than
# crash-allowing unvalidated output.
try:
    from hooklib import (GATE_LOG, REPO_ROOT, extract_json_object,
                         governed_agents, load_manifest, log_jsonl,
                         pushed_instruments)
    _IMPORT_ERROR = None
except Exception as _exc:  # pragma: no cover - environment defect
    _IMPORT_ERROR = _exc

RECEIPT_FIELDS = ("instrument_versions", "instrument_receipts", "agent_version",
                  "model_id", "pulled_files_read")
# Harness marker appended to a model ID when the 1M context window is active;
# the underlying model is the pinned one (recorded verbatim in run records).
CONTEXT_MARKER = "[1m]"
# Retry budget raised 4x0.75s -> 8x1.0s (C2 probes, 2026-08-14): all 45
# benchmark transcripts held valid payloads yet 39 searches failed at hook
# time — write lag beyond the old 3 s budget is the only surviving
# explanation, so the budget is insurance, and the orchestrator-side
# reconciliation (plan C9) is the authoritative backstop.
TRANSCRIPT_RETRIES = 8
TRANSCRIPT_RETRY_DELAY_S = 1.0


def block(agent_type: str, reason: str, ctx: dict | None = None) -> int:
    """Emit a block decision (re-prompts the subagent) and log it.

    `ctx` carries the re-audit C-1 decision context — the event's key names
    (so the real SubagentStop field names are learned from live traffic),
    the agent_id where the event supplies one, the branch that supplied the
    payload, and the item identifier (M-9) — logged on every decision.
    """
    log_jsonl(GATE_LOG, {"event": "block", "agent_type": agent_type,
                         **(ctx or {}), "reason": reason})
    print(json.dumps({"decision": "block",
                      "reason": f"Receipt gate (routing design §3.2): {reason}"}))
    return 0


def transcript_lines(transcript_path: str) -> list[str] | None:
    """Return transcript lines, retrying briefly (async write lag, D-12)."""
    path = Path(transcript_path) if transcript_path.startswith("/") \
        else REPO_ROOT / transcript_path
    for _ in range(TRANSCRIPT_RETRIES):
        try:
            return path.read_text(encoding="utf-8").splitlines()
        except OSError:
            time.sleep(TRANSCRIPT_RETRY_DELAY_S)
    return None


def tool_use_inputs(lines: list[str], names: tuple[str, ...] | None) -> list[dict]:
    """Collect tool_use input dicts from transcript lines.

    With `names`, only calls to those tools; with None, every tool_use input.
    """
    inputs: list[dict] = []
    for line in lines:
        try:
            entry = json.loads(line)
        except json.JSONDecodeError:
            continue
        content = ((entry.get("message") or {}).get("content")
                   if isinstance(entry.get("message"), dict) else entry.get("content"))
        if not isinstance(content, list):
            continue
        for blk in content:
            if isinstance(blk, dict) and blk.get("type") == "tool_use" \
                    and (names is None or blk.get("name") in names) \
                    and isinstance(blk.get("input"), dict):
                inputs.append(blk["input"])
    return inputs


def read_calls(lines: list[str]) -> list[dict]:
    """Read tool calls paired with their result status from the transcript.

    Returns [{"input": dict, "error": bool}]. A call with no recorded
    result counts as errored: an unverifiable read must not verify a
    declared pull. Added 2026-08-15 (C6/C8 reconciliation finding): a
    benchmark spawn declared pulls whose only Read attempts had failed
    with file-not-found — attempt-matching passed them, success-matching
    must not.
    """
    uses: list[tuple[str, dict]] = []
    errors: dict[str, bool] = {}
    for line in lines:
        try:
            entry = json.loads(line)
        except json.JSONDecodeError:
            continue
        content = ((entry.get("message") or {}).get("content")
                   if isinstance(entry.get("message"), dict) else entry.get("content"))
        if not isinstance(content, list):
            continue
        for blk in content:
            if not isinstance(blk, dict):
                continue
            if blk.get("type") == "tool_use" and blk.get("name") == "Read" \
                    and isinstance(blk.get("input"), dict):
                uses.append((str(blk.get("id")), blk["input"]))
            elif blk.get("type") == "tool_result":
                errors[str(blk.get("tool_use_id"))] = bool(blk.get("is_error"))
    return [{"input": call_input, "error": errors.get(use_id, True)}
            for use_id, call_input in uses]


# Reads made through Bash (2026-10-12, the gate 1.3 final review's F2). Agents
# in the harness's auto mode are told to read files with cat or sed -n, so a
# Read-only check failed every such run while saying nothing true about it.
FULL_READERS = frozenset({"cat", "less", "more", "nl"})
PARTIAL_READERS = frozenset({"head", "tail", "sed", "awk", "cut"})
SEARCHERS = frozenset({"grep", "egrep", "fgrep", "rg", "ugrep", "ag"})
COMMAND_PREFIXES = frozenset({"sudo", "env", "time", "nohup", "nice", "command"})
SPILL_PATH_RE = re.compile(r"Full output saved to:\s*(\S+)")
SPILL_MARKERS = ("<persisted-output>", "Full output saved to:")
HEREDOC_START_RE = re.compile(r"(?<!<)<<(?!<)-?[ \t]*(['\"]?)([A-Za-z_][A-Za-z0-9_]*)\1")
RESULT_KEYS = ("verdict", "overall", "verification_targets", "coverage", "dimensions")


def _tool_calls(lines: list[str], name: str) -> list[dict]:
    """Calls to one tool, each with its result: {input, error, text}.

    A call with no recorded result counts as errored, as in read_calls().
    """
    uses: list[tuple[str, dict, str | None]] = []
    results: dict[str, tuple[bool, str]] = {}
    for line in lines:
        try:
            entry = json.loads(line)
        except json.JSONDecodeError:
            continue
        content = ((entry.get("message") or {}).get("content")
                   if isinstance(entry.get("message"), dict) else entry.get("content"))
        if not isinstance(content, list):
            continue
        for blk in content:
            if not isinstance(blk, dict):
                continue
            if blk.get("type") == "tool_use" and blk.get("name") == name \
                    and isinstance(blk.get("input"), dict):
                uses.append((str(blk.get("id")), blk["input"], entry.get("cwd")))
            elif blk.get("type") == "tool_result":
                raw = blk.get("content")
                text = ("".join(str(part.get("text", "")) for part in raw
                                if isinstance(part, dict))
                        if isinstance(raw, list) else str(raw or ""))
                results[str(blk.get("tool_use_id"))] = (bool(blk.get("is_error")), text)
    return [{"input": call_input, "error": results.get(use_id, (True, ""))[0],
             "text": results.get(use_id, (True, ""))[1], "cwd": cwd}
            for use_id, call_input, cwd in uses]


def _mask_quoted(text: str) -> str:
    """The text with quoted and escaped characters blanked (same length)."""
    out: list[str] = []
    quote: str | None = None
    escaped = False
    for ch in text:
        if escaped:
            out.append(" ")
            escaped = False
        elif quote == "'":
            out.append(ch if ch == "'" else " ")
            quote = None if ch == "'" else quote
        elif ch == "\\":
            out.append(" ")
            escaped = True
        elif quote == '"':
            out.append(ch if ch == '"' else " ")
            quote = None if ch == '"' else quote
        else:
            if ch in "'\"":
                quote = ch
            out.append(ch)
    return "".join(out)


def _shell_pipelines(command: str) -> list[list[str]]:
    """A command's pipelines, each a list of its stages: heredoc bodies
    dropped, commands split at unquoted &&, ||, ;, and newlines, and stages
    at unquoted single |."""
    kept: list[str] = []
    delimiter: str | None = None
    for line in command.splitlines():
        if delimiter is not None:
            if line.strip() == delimiter:
                delimiter = None
            continue
        found = HEREDOC_START_RE.search(line)
        if found and _mask_quoted(line)[found.start():found.start() + 2] == "<<":
            delimiter = found.group(2)
        kept.append(line)
    text = "\n".join(kept)
    masked = _mask_quoted(text)
    pipelines: list[list[str]] = []
    stages: list[str] = []
    start = i = 0
    while i < len(text):
        if masked[i:i + 2] in ("&&", "||") or masked[i] in ";\n":
            stages.append(text[start:i])
            pipelines.append(stages)
            stages = []
            i += 2 if masked[i:i + 2] in ("&&", "||") else 1
            start = i
        elif masked[i] == "|":
            stages.append(text[start:i])
            i += 1
            start = i
        else:
            i += 1
    stages.append(text[start:])
    pipelines.append(stages)
    return [[st.strip() for st in pipe if st.strip()] for pipe in pipelines
            if any(st.strip() for st in pipe)]


def _stage_words(stage: str) -> tuple[str, list[str]]:
    """A stage's command name (basename) and its arguments, quotes removed,
    redirections and assignments dropped."""
    try:
        words = shlex.split(stage, comments=True)
    except ValueError:
        words = stage.split()
    words = [w for w in words if not re.fullmatch(r"[0-9&]*[<>].*", w)]
    k = 0
    while k < len(words) and (words[k] in COMMAND_PREFIXES
                              or re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*=.*", words[k])):
        k += 1
    if k >= len(words):
        return "", []
    return posixpath.basename(words[k]), words[k + 1:]


def bash_reads(lines: list[str]) -> list[dict]:
    """Files that Bash commands read, and how.

    Returns:
        ``[{"path", "cwd", "kind", "error", "spill"}]``: ``kind`` is
        ``complete`` (cat and the like, with nothing downstream but tee or
        cat), ``partial`` (head, tail, sed, awk, cut, or a complete reader
        piped into anything else, such as head, wc, or grep), or
        ``searched`` (grep and the like). ``cwd`` is the directory a relative
        path is read from: a ``cd`` in the command, else the working
        directory the transcript records for the call. ``spill`` is the file
        the harness saved a truncated output to, if it did.
    """
    reads: list[dict] = []
    for call in _tool_calls(lines, "Bash"):
        command = str(call["input"].get("command") or "")
        spilled = SPILL_PATH_RE.search(call["text"])
        truncated = any(marker in call["text"] for marker in SPILL_MARKERS)
        cwd: str | None = call.get("cwd")
        for stages in _shell_pipelines(command):
            for position, stage in enumerate(stages):
                name, rest = _stage_words(stage)
                args = [w for w in rest if not w.startswith("-")]
                if name == "cd" and len(stages) == 1:
                    target = args[0] if args else "~"
                    cwd = (target if target.startswith(("/", "~"))
                           else posixpath.join(cwd, target) if cwd else None)
                    continue
                downstream = [_stage_words(later)[0] for later in stages[position + 1:]]
                if name in FULL_READERS:
                    kind = ("complete" if all(d in ("tee", "cat") for d in downstream)
                            else "partial")
                    files = args
                elif name in PARTIAL_READERS:
                    kind = "partial"
                    files = args[1:] if name in ("sed", "awk") else args
                elif name in SEARCHERS:
                    kind, files = "searched", args[1:]
                else:
                    continue
                for path in files:
                    reads.append({"path": path, "cwd": cwd, "kind": kind,
                                  "error": call["error"],
                                  "spill": (spilled.group(1) if spilled else "") if truncated
                                  else None})
    return reads


def _names(declared: str, written: str, cwd: str | None) -> bool:
    """Whether a path or glob as written in a command names a declared file.

    Both are compared as whole, normalised paths: a relative path is read
    from ``cwd`` (the command's own cd, or the working directory the
    transcript records), and a relative declaration from the repository
    root. A bare file name never matches a same-named file elsewhere (Fable's
    delta review, D-2).
    """
    base = cwd or str(REPO_ROOT)
    path = written if written.startswith("/") else posixpath.join(base, written)
    path = posixpath.normpath(posixpath.expanduser(path))
    target = declared if declared.startswith("/") else posixpath.join(str(REPO_ROOT), declared)
    target = posixpath.normpath(posixpath.expanduser(target))
    if any(ch in written for ch in "*?["):
        return fnmatch.fnmatchcase(target, path)
    return target == path


def pull_verdict(declared: str, reads: list[dict], shell: list[dict]) -> tuple[str, str]:
    """How a declared pull was read: ``read``, ``truncated``, ``searched``,
    ``errored``, or ``missing``, with a short account of how.

    Args:
        declared: the path the agent declared in ``pulled_files_read``.
        reads: ``read_calls(lines)``.
        shell: ``bash_reads(lines)``.
    """
    tool = [c for c in reads if declared in str(c["input"].get("file_path", ""))]
    tool_ok = [c for c in tool if not c["error"]]
    bash = [b for b in shell if _names(declared, b["path"], b["cwd"])]
    bash_ok = [b for b in bash if not b["error"]]

    def spill_read(spill: str | None) -> bool:
        return spill is None or any(
            spill and spill in str(c["input"].get("file_path", "")) and not c["error"]
            and "limit" not in c["input"] and "offset" not in c["input"] for c in reads)

    if any("limit" not in c["input"] and "offset" not in c["input"] for c in tool_ok) or \
            any(b["kind"] == "complete" and spill_read(b["spill"]) for b in bash_ok):
        return "read", ""
    if tool_ok or any(b["kind"] in ("complete", "partial") for b in bash_ok):
        how = ("Read with limit/offset" if tool_ok else
               "a partial shell read (head, tail, sed, awk, or cut)"
               if any(b["kind"] == "partial" for b in bash_ok)
               else "a shell read whose output the harness truncated")
        return "truncated", how
    if bash_ok:
        return "searched", "only searched (grep), never read"
    if tool or bash:
        return "errored", "every attempt errored"
    return "missing", ""


def structured_output_from_transcript(lines: list[str]) -> dict | None:
    """Find the last schema-shaped structured output among tool_use inputs.

    Workflow-lane spawns emit their schema-forced output through a
    structured-output tool call rather than the final message. Anchor on the
    output contract (a `status` plus receipt content) rather than a tool
    name, which is harness-internal and may change.
    """
    candidates = [inp for inp in tool_use_inputs(lines, None)
                  if "status" in inp and ("receipts" in inp or "instrument_versions" in inp)]
    return candidates[-1] if candidates else None


def receipt_fields(payload: dict) -> dict | None:
    """Return the five receipt fields from a payload, flat or nested.

    The benchmark output schema nests them under `receipts`; the agent
    definitions list them without specifying nesting. Try the nested
    carrier first, then the payload itself (L-1, 2026-08-14: an incomplete
    `receipts` dict must not mask complete flat fields). None if no
    carrier holds all five fields well-typed.
    """
    nested = payload.get("receipts") \
        if isinstance(payload.get("receipts"), dict) else None
    for carrier in (nested, payload):
        if carrier is None or not all(f in carrier for f in RECEIPT_FIELDS):
            continue
        fields = {f: carrier[f] for f in RECEIPT_FIELDS}
        if isinstance(fields["instrument_versions"], dict) \
                and isinstance(fields["instrument_receipts"], dict) \
                and isinstance(fields["pulled_files_read"], list):
            return fields
    return None


def model_matches(got: str, pinned: str) -> bool:
    """Exact pin match, tolerating the harness context-window marker."""
    return got == pinned or got == pinned + CONTEXT_MARKER


def validate(event: dict) -> int:
    """Validate one governed agent's receipts; block on failure."""
    agent_type = str(event.get("agent_type") or "")
    # Decision context, logged on every outcome (re-audit C-1): the event's
    # key names teach us the real SubagentStop field shape from live traffic
    # (design-doc names like agent_transcript_path are unconfirmed until the
    # C2 capture), agent_id attributes the decision where the event carries
    # one, payload_source records which branch supplied the payload, and
    # paper_slug identifies the item (M-9).
    ctx = {"event_keys": sorted(str(k) for k in event.keys()),
           "agent_id": str(event.get("agent_id") or ""),
           "payload_source": "none",
           "transcript_state": "not-needed"}

    try:
        manifest = load_manifest()
    except Exception as exc:
        return block(agent_type,
                     f"manifest unreadable ({exc}) — cannot validate receipts", ctx)

    registry = governed_agents(manifest)
    if agent_type not in registry:
        return 0

    # Payload selection (re-audit C-2, re-specified 2026-08-14): prefer a
    # WELL-FORMED receipt payload from the final message; only when the final
    # message carries none may the transcript's tool calls supply one — and a
    # receipt-less JSON object in the final message must not suppress that
    # search (the C4-era regression). A transcript payload adopted while the
    # final message names a different paper_slug is substitution, not
    # fallback, and blocks: receipts must be bound to this item.
    output_text = event.get("last_assistant_message") or ""
    final_payload = extract_json_object(output_text) if output_text else None
    payload = None
    lines = None
    if final_payload is not None and receipt_fields(final_payload) is not None:
        payload = final_payload
        ctx["payload_source"] = "final_message"
    else:
        transcript_path = str(event.get("agent_transcript_path") or "")
        if not transcript_path:
            lines = None
            ctx["transcript_state"] = "none-declared"
        else:
            lines = transcript_lines(transcript_path)
            ctx["transcript_state"] = ("read" if lines is not None
                                       else "unavailable-after-retries")
        from_tool = structured_output_from_transcript(lines) if lines else None
        if from_tool is not None and receipt_fields(from_tool) is not None:
            final_slug = str((final_payload or {}).get("paper_slug") or "")
            tool_slug = str(from_tool.get("paper_slug") or "")
            if final_slug and tool_slug and final_slug != tool_slug:
                ctx["payload_source"] = "transcript_tool_call"
                return block(agent_type,
                             f"final message names paper_slug {final_slug!r} but the "
                             f"transcript's structured output names {tool_slug!r} — "
                             f"receipts are not bound to this item; re-emit your full "
                             f"structured output including receipts", ctx)
            payload = from_tool
            ctx["payload_source"] = "transcript_tool_call"
        elif from_tool is not None:
            # Malformed in both places (or final absent): report against the
            # transcript candidate so the reason names real receipt fields.
            payload = from_tool
            ctx["payload_source"] = "transcript_tool_call"
        elif final_payload is not None:
            payload = final_payload
            ctx["payload_source"] = "final_message"
    if payload is None:
        # Distinct reasons per branch (re-audit C-1; C2 finding 2026-08-14):
        # "transcript unavailable" and "searched and found nothing" are
        # different faults with different remedies — conflating them hid the
        # benchmark's write-lag failure mode for eleven days.
        if ctx["transcript_state"] == "unavailable-after-retries":
            return block(agent_type, "no structured output in the final message and "
                                     "the agent transcript was unavailable after "
                                     "retries — transcript write lag suspected, not "
                                     "a missing payload; re-emit your full "
                                     "structured output including receipts", ctx)
        return block(agent_type, "no structured output found in the final message or "
                                 "the transcript's tool calls — re-emit your full "
                                 "structured output including receipts", ctx)
    ctx["paper_slug"] = str(payload.get("paper_slug") or "")

    fields = receipt_fields(payload)
    if fields is None:
        return block(agent_type, "receipt fields missing or malformed (need "
                                 + ", ".join(RECEIPT_FIELDS)
                                 + ", flat or under 'receipts') — re-emit receipts", ctx)

    versions, receipts = fields["instrument_versions"], fields["instrument_receipts"]
    for spec in pushed_instruments(manifest, agent_type):
        got_version = str(versions.get(spec["name"], "")).strip()
        if got_version != spec["version"]:
            return block(agent_type, f"instrument_versions[{spec['name']}] is "
                                     f"{got_version!r}, manifest says {spec['version']!r} — "
                                     f"re-read the injected instrument and re-emit receipts",
                         ctx)
        got_token = str(receipts.get(spec["name"], "")).strip()
        if got_token != spec["token"]:
            return block(agent_type, f"instrument_receipts[{spec['name']}] does not match "
                                     f"the end-of-file Receipt-token — read the injected "
                                     f"instrument to its final line and re-emit receipts",
                         ctx)

    entry = registry[agent_type]
    pinned = str(entry.get("model", "")).strip()
    got_model = str(fields["model_id"]).strip()
    if pinned and not model_matches(got_model, pinned):
        return block(agent_type, f"model_id {got_model!r} does not match the manifest pin "
                                 f"{pinned!r} — model identity is part of the instrument "
                                 f"(design §3.3); this item is blocked, not retried: escalate",
                     ctx)

    expected_agent_version = f"{agent_type} v{str(entry.get('version', '')).strip()}"
    got_agent_version = str(fields["agent_version"]).strip()
    if got_agent_version != expected_agent_version:
        return block(agent_type, f"agent_version {got_agent_version!r} does not match "
                                 f"{expected_agent_version!r} — re-emit receipts from your "
                                 f"agent brief", ctx)

    # Delivery verification for the output contract (audit S3, 2026-08-14):
    # v1.1+ payloads carry a validator-enforced schema_version; when present
    # it must match the registered contract. v1.0-era payloads lack the
    # field and pass unchanged (the old contract predates
    # self-identification).
    declared_schema = str(payload.get("schema_version") or "").strip()
    if declared_schema:
        registered = str((((manifest.get("assessment") or {}).get("schemas") or {})
                          .get("benchmark_fair_output") or {}).get("version", "")).strip()
        if registered and declared_schema != registered:
            return block(agent_type, f"schema_version {declared_schema!r} does not match "
                                     f"the registered output contract {registered!r} — "
                                     f"the spawn was supplied a stale or unregistered "
                                     f"schema; orchestrator attention needed, not a "
                                     f"retry: escalate", ctx)

    # ESCALATE passes through to the orchestrator only after provenance holds,
    # and, when it carries a result, only after the pull check too (F2).
    escalated = str(payload.get("status", "")) == "ESCALATE"
    if escalated and not any(key in payload for key in RESULT_KEYS):
        log_jsonl(GATE_LOG, {"event": "escalate-passthrough", "agent_type": agent_type,
                             **ctx, "model_id": got_model,
                             "reason": payload.get("escalate_reason")})
        return 0

    pulled = fields["pulled_files_read"]
    if pulled:
        if lines is None:
            transcript_path = str(event.get("agent_transcript_path") or "")
            lines = transcript_lines(transcript_path) if transcript_path else None
        if lines is None:
            return block(agent_type, "agent transcript unavailable after retries — cannot "
                                     "verify declared pulled-file reads (D-12 fail-closed)",
                         ctx)
        calls = read_calls(lines)
        shell = bash_reads(lines)
        for declared in pulled:
            declared_path = str(declared).strip()
            if not declared_path:
                # L-3 (2026-08-14): "" is a substring of every path — an
                # empty declaration must not be a free pass.
                return block(agent_type, "pulled_files_read contains an empty path — "
                                         "declare the actual file read or remove the "
                                         "entry", ctx)
            verdict, how = pull_verdict(declared_path, calls, shell)
            if verdict == "missing":
                return block(agent_type, f"declared pulled read {declared!r} has no matching "
                                         f"Read call or shell read in the transcript — "
                                         f"re-read it in full and re-emit receipts", ctx)
            if verdict == "errored":
                # 2026-08-15: attempts are not reads — a declared pull whose
                # every attempt errored never entered the agent's context.
                return block(agent_type, f"declared pulled read {declared!r} was attempted "
                                         f"but every matching Read errored — the file was "
                                         f"never actually read; re-read it in full from "
                                         f"its canonical path and re-emit receipts", ctx)
            if verdict == "searched":
                return block(agent_type, f"declared pulled read {declared!r} was {how} — "
                                         f"read the file in full and re-emit receipts", ctx)
            if verdict == "truncated":
                return block(agent_type, f"pulled read {declared!r} was truncated ({how}) — "
                                         f"re-read the file in full", ctx)

    log_jsonl(GATE_LOG, {"event": "escalate-passthrough" if escalated else "pass",
                         "agent_type": agent_type, **ctx, "model_id": got_model,
                         "pulled": len(pulled),
                         **({"reason": payload.get("escalate_reason"), "checked": True}
                            if escalated else {})})
    return 0


def main() -> int:
    """Parse the SubagentStop event and validate fail-closed.

    Unattributable events (unparseable, undecodable, or non-object stdin)
    BLOCK: governedness cannot be determined, and refusing beats letting a
    governed scoring spawn stop ungated (policy decided once for both
    hooks, 2026-08-14). The block reason names the fault class so it reads
    as an environment/parse fault, not a receipt verdict.
    """
    if _IMPORT_ERROR is not None:
        print(json.dumps({"decision": "block",
                          "reason": f"Receipt gate: hook environment broken "
                                    f"({_IMPORT_ERROR}) — environment fault, not a "
                                    f"receipt verdict; fix the hook environment"}))
        return 0
    try:
        event = json.load(sys.stdin)
    except Exception as exc:  # includes non-UTF-8 bytes (M-2)
        return block("", f"unattributable SubagentStop event "
                         f"({exc.__class__.__name__}: {exc}) — parse fault, not a "
                         f"receipt verdict", {"event_keys": []})
    if not isinstance(event, dict):
        return block("", "SubagentStop event is not a JSON object — parse fault, "
                         "not a receipt verdict", {"event_keys": []})
    agent_type = str(event.get("agent_type") or "")
    try:
        return validate(event)
    except Exception as exc:  # fail-closed: block rather than crash-allow (C9)
        return block(agent_type, f"receipt gate internal error ({exc.__class__.__name__}: "
                                 f"{exc}) — blocking rather than passing unvalidated output",
                     {"event_keys": sorted(str(k) for k in event.keys())})


if __name__ == "__main__":
    sys.exit(main())
