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

from hooklib import REPO_ROOT, governed_agents, load_manifest, pushed_instruments

D5_SCRIPT = REPO_ROOT / "scripts" / "check-manifest-consistency.py"


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
    """Gate governed-agent spawns on the consistency and environment checks."""
    try:
        event = json.load(sys.stdin)
    except json.JSONDecodeError:
        return 0
    if event.get("tool_name") not in ("Agent", "Task"):
        return 0
    subagent_type = (event.get("tool_input") or {}).get("subagent_type") or ""

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

    result = subprocess.run([sys.executable, str(D5_SCRIPT), "--quiet"],
                            capture_output=True, text=True, timeout=60)
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
