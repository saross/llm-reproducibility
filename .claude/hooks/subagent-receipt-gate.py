#!/usr/bin/env python3
"""SubagentStop receipt gate (routing design §3.2–§3.3).

For governed agents (registered in manifest `agent_definitions`), validates
the layered read receipts in the agent's final structured output:

- delivery check — `instrument_versions` matches the manifest per pushed
  instrument (catches stale-file pushes);
- consumption check — `instrument_receipts` quotes each end-of-file receipt
  token (unguessable; defeats header-only reads);
- identity check — `model_id` matches the manifest's pinned model for the
  agent (hard gate, review D-7);
- pull check — every path declared in `pulled_files_read` has a matching Read
  tool call in the harness-recorded transcript with no `limit`/`offset`
  truncation (harness evidence, not self-report). Transcripts are written
  asynchronously and can lag — the hook retries briefly before blocking
  (review D-12).

On failure the hook returns `decision: "block"` with the reason, re-prompting
the same subagent instead of failing the batch item (§3.2 self-healing).
`status: ESCALATE` outputs pass through — escalation is a valid outcome the
orchestrator handles. Non-governed agent types pass through untouched.
"""

from __future__ import annotations

import json
import sys
import time
from pathlib import Path

from hooklib import (GATE_LOG, REPO_ROOT, extract_json_object, governed_agents,
                     load_manifest, log_jsonl, pushed_instruments)

REQUIRED_FIELDS = ("instrument_versions", "instrument_receipts", "agent_version",
                   "model_id", "pulled_files_read", "status")
TRANSCRIPT_RETRIES = 4
TRANSCRIPT_RETRY_DELAY_S = 0.75


def block(agent_type: str, reason: str) -> int:
    """Emit a block decision (re-prompts the subagent) and log it."""
    log_jsonl(GATE_LOG, {"event": "block", "agent_type": agent_type, "reason": reason})
    print(json.dumps({"decision": "block",
                      "reason": f"Receipt gate (routing design §3.2): {reason}"}))
    return 0


def read_tool_calls(transcript_path: str) -> list[dict] | None:
    """Return Read tool-call inputs from a transcript, or None if unreadable.

    Retries briefly — transcripts are written asynchronously and can lag
    behind the SubagentStop event (review D-12).
    """
    path = Path(transcript_path) if transcript_path.startswith("/") \
        else REPO_ROOT / transcript_path
    for attempt in range(TRANSCRIPT_RETRIES):
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except OSError:
            time.sleep(TRANSCRIPT_RETRY_DELAY_S)
            continue
        calls = []
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
                        and blk.get("name") == "Read":
                    calls.append(blk.get("input") or {})
        return calls
    return None


def main() -> int:
    """Validate one governed agent's receipts; block on failure."""
    try:
        event = json.load(sys.stdin)
    except json.JSONDecodeError:
        return 0
    agent_type = event.get("agent_type") or ""

    try:
        manifest = load_manifest()
    except Exception as exc:
        return block(agent_type, f"manifest unreadable ({exc}) — cannot validate receipts")

    registry = governed_agents(manifest)
    if agent_type not in registry:
        return 0

    output_text = event.get("last_assistant_message") or ""
    payload = extract_json_object(output_text) if output_text else None
    if payload is None:
        return block(agent_type, "no structured JSON output found in the final message — "
                                 "re-emit your full structured output including receipts")

    if str(payload.get("status", "")).upper() == "ESCALATE":
        log_jsonl(GATE_LOG, {"event": "escalate-passthrough", "agent_type": agent_type,
                             "reason": payload.get("reason") or payload.get("status_reason")})
        return 0

    missing = [f for f in REQUIRED_FIELDS if f not in payload]
    if missing:
        return block(agent_type, f"missing required receipt field(s): {', '.join(missing)}")

    versions = payload.get("instrument_versions") or {}
    receipts = payload.get("instrument_receipts") or {}
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

    pinned = str(registry[agent_type].get("model", "")).strip()
    got_model = str(payload.get("model_id", "")).strip()
    if pinned and got_model != pinned:
        return block(agent_type, f"model_id {got_model!r} does not match the manifest pin "
                                 f"{pinned!r} — model identity is part of the instrument "
                                 f"(design §3.3); this item is blocked, not retried: escalate")

    pulled = payload.get("pulled_files_read") or []
    if pulled:
        transcript_path = event.get("agent_transcript_path") or ""
        calls = read_tool_calls(transcript_path) if transcript_path else None
        if calls is None:
            return block(agent_type, "agent transcript unavailable after retries — cannot "
                                     "verify declared pulled-file reads (D-12 fail-closed)")
        for declared in pulled:
            matching = [c for c in calls if declared in str(c.get("file_path", ""))]
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


if __name__ == "__main__":
    sys.exit(main())
