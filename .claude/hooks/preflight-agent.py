#!/usr/bin/env python3
"""PreToolUse[Agent] pre-flight (routing design §3.4, review D-3).

`SubagentStart` cannot block a spawn; `PreToolUse` can deny it before token
spend. For governed agent types (registered in manifest `agent_definitions`)
this hook denies the spawn unless:

- the D5 manifest-consistency check passes (canonical files exist and are
  non-empty, version lines and receipt tokens match, mirrors intact,
  agent-definition hashes match — the §3.4 hot-reload guard);
- `CLAUDE_CODE_SUBAGENT_MODEL` is unset (it silently outranks agent model
  pins; review D-7);
- every instrument pushed to the target agent exists and is non-empty.

Ungoverned agent types pass through untouched — this gate protects the
study's scoring and reproduction lanes, not general subagent use.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys

# Fail-closed import (audit 2026-08-03 C8): if the shared library or PyYAML is
# unavailable, deny governed-unknown spawns rather than crash-allowing them.
try:
    from hooklib import REPO_ROOT, governed_agents, load_manifest, pushed_instruments
    _IMPORT_ERROR = None
except Exception as _exc:  # pragma: no cover - environment defect
    _IMPORT_ERROR = _exc
    REPO_ROOT = None

D5_SCRIPT = (REPO_ROOT / "scripts" / "check-manifest-consistency.py") if REPO_ROOT else None


def deny(reasons: list[str]) -> int:
    """Emit a PreToolUse deny decision listing every failed check."""
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "deny",
        "permissionDecisionReason": ("Pre-flight failed (routing design §3.4): "
                                     + "; ".join(reasons)),
    }}))
    return 0


def main() -> int:
    """Gate governed-agent spawns on the consistency and environment checks.

    Fail-closed (audit 2026-08-03 C8): unparseable events, import failures,
    unexpected input shapes, and checker errors all DENY rather than
    crash-allow — this is the only layer that can stop a governed scoring
    spawn before token spend, so a visible deny beats a silent pass.
    """
    if _IMPORT_ERROR is not None:
        return deny([f"hook environment broken ({_IMPORT_ERROR}) — cannot determine "
                     f"whether this spawn is governed"])
    try:
        event = json.load(sys.stdin)
    except json.JSONDecodeError:
        return deny(["unparseable PreToolUse event — cannot determine whether this "
                     "spawn is governed"])
    if not isinstance(event, dict):
        return deny(["unexpected PreToolUse event shape — cannot determine whether "
                     "this spawn is governed"])
    if event.get("tool_name") not in ("Agent", "Task"):
        return 0
    tool_input = event.get("tool_input")
    if not isinstance(tool_input, dict):
        tool_input = {}
    subagent_type = str(tool_input.get("subagent_type") or "")

    try:
        manifest = load_manifest()
    except Exception as exc:
        return deny([f"manifest unreadable: {exc}"])

    if subagent_type not in governed_agents(manifest):
        return 0

    reasons = []
    if os.environ.get("CLAUDE_CODE_SUBAGENT_MODEL"):
        reasons.append("CLAUDE_CODE_SUBAGENT_MODEL is set — it silently outranks the "
                       "agent's model pin; unset it before spawning scoring agents")

    try:
        result = subprocess.run([sys.executable, str(D5_SCRIPT), "--quiet"],
                                capture_output=True, text=True, timeout=60)
    except Exception as exc:  # timeout or spawn failure: deny, don't crash-allow
        return deny([f"manifest consistency check could not run ({exc.__class__.__name__})"])
    if result.returncode != 0:
        detail = (result.stdout or result.stderr).strip().splitlines()
        reasons.append("manifest consistency check failed: " + "; ".join(detail[:5]))

    for spec in pushed_instruments(manifest, subagent_type):
        path = REPO_ROOT / spec["path"]
        if not path.is_file() or not path.stat().st_size:
            reasons.append(f"pushed instrument missing/empty: {spec['path']}")

    if reasons:
        return deny(reasons)
    return 0


if __name__ == "__main__":
    sys.exit(main())
