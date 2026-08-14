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
    # Decision context, logged on every outcome (re-audit C-1): the event's
    # key names teach us the real SubagentStop field shape from live traffic
    # (design-doc names like agent_transcript_path are unconfirmed until the
    # C2 capture), agent_id attributes the decision where the event carries
    # one, payload_source records which branch supplied the payload, and
    # paper_slug identifies the item (M-9).
    ctx = {"event_keys": sorted(str(k) for k in event.keys()),
           "agent_id": str(event.get("agent_id") or ""),
           "payload_source": "none"}

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
        lines = transcript_lines(transcript_path) if transcript_path else None
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

    # ESCALATE passes through to the orchestrator only after provenance holds.
    if str(payload.get("status", "")) == "ESCALATE":
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
        calls = tool_use_inputs(lines, ("Read",))
        for declared in pulled:
            matching = [c for c in calls if str(declared) in str(c.get("file_path", ""))]
            if not matching:
                return block(agent_type, f"declared pulled read {declared!r} has no matching "
                                         f"Read call in the transcript — re-read it in full "
                                         f"and re-emit receipts", ctx)
            if not any("limit" not in c and "offset" not in c for c in matching):
                return block(agent_type, f"pulled read {declared!r} was truncated with "
                                         f"limit/offset — re-read the file in full", ctx)

    log_jsonl(GATE_LOG, {"event": "pass", "agent_type": agent_type,
                         **ctx, "model_id": got_model, "pulled": len(pulled)})
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
                                 f"{exc}) — blocking rather than passing unvalidated output",
                     {"event_keys": sorted(str(k) for k in event.keys())})


if __name__ == "__main__":
    sys.exit(main())
