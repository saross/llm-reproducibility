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
- pull check — every path declared in `pulled_files_read` has a matching Read
  tool call in the harness-recorded transcript with no `limit`/`offset`
  truncation. Transcripts are written asynchronously and can lag — the hook
  retries briefly before blocking (review D-12).

The structured output is located in the final assistant message OR, for
workflow-lane spawns whose schema-forced output rides a structured-output
tool call, in the transcript's tool_use inputs (audit 2026-08-03 C4: the
final-message-only search blocked every workflow spawn once).

`status: ESCALATE` outputs are passed through to the orchestrator ONLY after
the receipt and model-identity checks pass — escalation is a valid outcome,
but it is not an exemption from provenance (audit 2026-08-03 C5).

Fail-closed: unexpected payload shapes and internal errors block rather than
crash-allow (audit 2026-08-03 C9). On failure the hook returns
`decision: "block"` with the reason, re-prompting the same subagent instead
of failing the batch item (§3.2 self-healing).
"""

from __future__ import annotations

import json
import sys
import time
from pathlib import Path

from hooklib import (GATE_LOG, REPO_ROOT, extract_json_object, governed_agents,
                     load_manifest, log_jsonl, pushed_instruments)

RECEIPT_FIELDS = ("instrument_versions", "instrument_receipts", "agent_version",
                  "model_id", "pulled_files_read")
# Harness marker appended to a model ID when the 1M context window is active;
# the underlying model is the pinned one (recorded verbatim in run records).
CONTEXT_MARKER = "[1m]"
TRANSCRIPT_RETRIES = 4
TRANSCRIPT_RETRY_DELAY_S = 0.75


def block(agent_type: str, reason: str) -> int:
    """Emit a block decision (re-prompts the subagent) and log it."""
    log_jsonl(GATE_LOG, {"event": "block", "agent_type": agent_type, "reason": reason})
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
    definitions list them without specifying nesting. Accept both; None if
    any field is missing or the carrier has the wrong type.
    """
    carrier = payload.get("receipts") if isinstance(payload.get("receipts"), dict) \
        else payload
    if not all(f in carrier for f in RECEIPT_FIELDS):
        return None
    fields = {f: carrier[f] for f in RECEIPT_FIELDS}
    if not isinstance(fields["instrument_versions"], dict) \
            or not isinstance(fields["instrument_receipts"], dict) \
            or not isinstance(fields["pulled_files_read"], list):
        return None
    return fields


def model_matches(got: str, pinned: str) -> bool:
    """Exact pin match, tolerating the harness context-window marker."""
    return got == pinned or got == pinned + CONTEXT_MARKER


def validate(event: dict) -> int:
    """Validate one governed agent's receipts; block on failure."""
    agent_type = str(event.get("agent_type") or "")

    try:
        manifest = load_manifest()
    except Exception as exc:
        return block(agent_type, f"manifest unreadable ({exc}) — cannot validate receipts")

    registry = governed_agents(manifest)
    if agent_type not in registry:
        return 0

    output_text = event.get("last_assistant_message") or ""
    payload = extract_json_object(output_text) if output_text else None
    lines = None
    if payload is None or receipt_fields(payload) is None:
        transcript_path = str(event.get("agent_transcript_path") or "")
        lines = transcript_lines(transcript_path) if transcript_path else None
        if lines:
            from_tool = structured_output_from_transcript(lines)
            if from_tool is not None:
                payload = from_tool
    if payload is None:
        return block(agent_type, "no structured output found in the final message or "
                                 "the transcript's tool calls — re-emit your full "
                                 "structured output including receipts")

    fields = receipt_fields(payload)
    if fields is None:
        return block(agent_type, "receipt fields missing or malformed (need "
                                 + ", ".join(RECEIPT_FIELDS)
                                 + ", flat or under 'receipts') — re-emit receipts")

    versions, receipts = fields["instrument_versions"], fields["instrument_receipts"]
    for spec in pushed_instruments(manifest, agent_type):
        got_version = str(versions.get(spec["name"], "")).strip()
        if got_version != spec["version"]:
            return block(agent_type, f"instrument_versions[{spec['name']}] is "
                                     f"{got_version!r}, manifest says {spec['version']!r} — "
                                     f"re-read the injected instrument and re-emit receipts")
        got_token = str(receipts.get(spec["name"], "")).strip()
        if got_token != spec["token"]:
            return block(agent_type, f"instrument_receipts[{spec['name']}] does not match "
                                     f"the end-of-file Receipt-token — read the injected "
                                     f"instrument to its final line and re-emit receipts")

    entry = registry[agent_type]
    pinned = str(entry.get("model", "")).strip()
    got_model = str(fields["model_id"]).strip()
    if pinned and not model_matches(got_model, pinned):
        return block(agent_type, f"model_id {got_model!r} does not match the manifest pin "
                                 f"{pinned!r} — model identity is part of the instrument "
                                 f"(design §3.3); this item is blocked, not retried: escalate")

    expected_agent_version = f"{agent_type} v{str(entry.get('version', '')).strip()}"
    got_agent_version = str(fields["agent_version"]).strip()
    if got_agent_version != expected_agent_version:
        return block(agent_type, f"agent_version {got_agent_version!r} does not match "
                                 f"{expected_agent_version!r} — re-emit receipts from your "
                                 f"agent brief")

    # ESCALATE passes through to the orchestrator only after provenance holds.
    if str(payload.get("status", "")) == "ESCALATE":
        log_jsonl(GATE_LOG, {"event": "escalate-passthrough", "agent_type": agent_type,
                             "model_id": got_model,
                             "reason": payload.get("escalate_reason")})
        return 0

    pulled = fields["pulled_files_read"]
    if pulled:
        if lines is None:
            transcript_path = str(event.get("agent_transcript_path") or "")
            lines = transcript_lines(transcript_path) if transcript_path else None
        if lines is None:
            return block(agent_type, "agent transcript unavailable after retries — cannot "
                                     "verify declared pulled-file reads (D-12 fail-closed)")
        calls = tool_use_inputs(lines, ("Read",))
        for declared in pulled:
            matching = [c for c in calls if str(declared) in str(c.get("file_path", ""))]
            if not matching:
                return block(agent_type, f"declared pulled read {declared!r} has no matching "
                                         f"Read call in the transcript — re-read it in full "
                                         f"and re-emit receipts")
            if not any("limit" not in c and "offset" not in c for c in matching):
                return block(agent_type, f"pulled read {declared!r} was truncated with "
                                         f"limit/offset — re-read the file in full")

    log_jsonl(GATE_LOG, {"event": "pass", "agent_type": agent_type,
                         "model_id": got_model, "pulled": len(pulled)})
    return 0


def main() -> int:
    """Parse the SubagentStop event and validate fail-closed."""
    try:
        event = json.load(sys.stdin)
    except json.JSONDecodeError:
        return 0  # not a JSON event for us; nothing to gate
    if not isinstance(event, dict):
        return 0
    agent_type = str(event.get("agent_type") or "")
    try:
        return validate(event)
    except Exception as exc:  # fail-closed: block rather than crash-allow (C9)
        return block(agent_type, f"receipt gate internal error ({exc.__class__.__name__}: "
                                 f"{exc}) — blocking rather than passing unvalidated output")


if __name__ == "__main__":
    sys.exit(main())
