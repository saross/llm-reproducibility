#!/bin/bash
# Subagent hook logger (Phase 1 scaffolding; production push/receipt hooks will
# replace this). D-2 spike PASSED 2026-07-24 — see routing design §9. The spike's
# canary injection has been removed; this now only logs firings for build-time
# observability. Log: .claude/hooks/spike-log.jsonl (gitignored).

input=$(cat)
log="$(dirname "$0")/spike-log.jsonl"
echo "$input" | jq -c '{ts: now|todate, ev: .hook_event_name, type: (.agent_type // null), id: (.agent_id // null), has_transcript: (has("agent_transcript_path"))}' >> "$log" 2>/dev/null
exit 0
