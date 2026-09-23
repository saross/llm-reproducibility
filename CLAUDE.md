# Project: llm-reproducibility

Claude Code entry point. It carries only Claude-specific mechanisms.

This project's shared policy — session continuity, the session-per-pass
execution mode and its checkpoints, the extraction and reproduction workflows,
file-operations safety, PDF handling, the filename gate, acronyms, the
directory map, validation checks, and agent ownership — lives in a
harness-neutral file that every agent working here follows, and is imported
here so it loads at session start:

@docs/agent-guidance.md

Project policy changes go in that file, not in this one. Global instructions
from `~/.claude/CLAUDE.md` also apply.

⚠ **Run `git fetch` before reading anything**, and report ahead/behind. The
harness's session-start git snapshot does not fetch, and a stale `origin/main`
ref reports "in sync" indistinguishably from genuinely being in sync. This cost
a duplicate D5 gate build on 2026-07-27. Rationale in the shared guidance.

## Claude-specific mechanisms

- **Extraction and assessment:** invoke the `research-assessor` skill.
- **Reproduction:** invoke the `reproduction-assessor` skill for Docker-based
  reproduction, verification, and adversarial review.
- **⚠ The `limit` parameter is the file-truncation hazard here.** The shared
  guidance's file-operations rule, in Claude terms:

  ```python
  # ✅ CORRECT
  data = Read("outputs/paper-name/extraction.json")  # No limit
  # ... modify data ...
  Write("outputs/paper-name/extraction.json", data)

  # ❌ WRONG - Will truncate file
  data = Read("outputs/paper-name/extraction.json", limit=5000)  # Dangerous!
  Write("outputs/paper-name/extraction.json", data)  # Loses data
  ```

- **PDFs:** read them with the Read tool directly rather than extracting text
  first. Quality is equivalent or better and page numbers survive for
  `location` fields.
- **Agents and subagents:** `.claude/agents/` holds this project's definitions,
  including the FAIR assessors and the adversarial reviewer.
- **Observation registers:** `wiki/claude-observations.md` is Claude's own and
  Claude maintains it. `wiki/user-observations.md` is gated — draft labelled
  candidates, leave acceptance to Shawn.
