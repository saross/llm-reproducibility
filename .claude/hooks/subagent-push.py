#!/usr/bin/env python3
"""SubagentStart push hook (routing design §3.1).

Injects every canonical instrument registered for the spawned agent type into
its context via `additionalContext`, and logs the sha256 + version of exactly
what was injected — an orchestrator-side receipt that does not depend on the
model at all. Non-governed agent types pass through untouched.

SubagentStart cannot block a spawn; missing-file failures are logged and
surfaced to the agent as an explicit ESCALATE directive, and the
PreToolUse[Agent] pre-flight (`preflight-agent.py`) is the layer that denies
the spawn before token spend.
"""

from __future__ import annotations

import json
import sys

from hooklib import (PUSH_RECEIPT_LOG, REPO_ROOT, load_manifest, log_jsonl,
                     pushed_instruments, sha256_text)


def main() -> int:
    """Read the hook event, assemble pushed content, emit additionalContext."""
    try:
        event = json.load(sys.stdin)
    except json.JSONDecodeError:
        return 0
    agent_type = event.get("agent_type") or ""
    agent_id = event.get("agent_id")

    try:
        manifest = load_manifest()
    except Exception as exc:  # manifest unreadable — pre-flight will block; log only
        log_jsonl(PUSH_RECEIPT_LOG, {"event": "push-error", "agent_type": agent_type,
                                     "error": f"manifest load failed: {exc}"})
        return 0

    specs = pushed_instruments(manifest, agent_type)
    if not specs:
        return 0

    parts = []
    for spec in specs:
        path = REPO_ROOT / spec["path"]
        try:
            text = path.read_text(encoding="utf-8")
        except OSError as exc:
            log_jsonl(PUSH_RECEIPT_LOG, {"event": "push-error", "agent_type": agent_type,
                                         "agent_id": agent_id, "file": spec["path"],
                                         "error": str(exc)})
            parts.append(f"<pushed-instrument name=\"{spec['name']}\" status=\"MISSING\">\n"
                         f"The instrument {spec['path']} could not be injected. "
                         f"Emit status: ESCALATE — do not proceed from memory.\n"
                         f"</pushed-instrument>")
            continue
        log_jsonl(PUSH_RECEIPT_LOG, {"event": "push", "agent_type": agent_type,
                                     "agent_id": agent_id, "file": spec["path"],
                                     "name": spec["name"], "version": spec["version"],
                                     "sha256": sha256_text(text)})
        parts.append(f"<pushed-instrument name=\"{spec['name']}\" path=\"{spec['path']}\" "
                     f"version=\"{spec['version']}\">\n{text}\n</pushed-instrument>")

    context = ("The following canonical instrument files are injected at spawn "
               "(routing design §3.1). Treat them as the authoritative instrument text; "
               "verify each version line and quote each end-of-file Receipt-token in "
               "your output receipts.\n\n" + "\n\n".join(parts))
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "SubagentStart",
                                             "additionalContext": context}}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
