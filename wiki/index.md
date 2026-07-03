---
title: "llm-reproducibility wiki — index"
tags: [index]
created: 2026-07-03
updated: 2026-07-03
status: active
---

# llm-reproducibility Wiki

**What this directory is (and is not).** This `wiki/` is the project's
**versioned research process record** — session continuity, lab notebook,
reflections, observations, and planning documents, maintained by the
`/handoff`, `/reflect`, and `/observe` rituals. It is *not* user
documentation: for how to install and use the extraction, assessment, and
reproduction systems, see [`docs/`](../docs/) at the repository root. Keeping
the process record inside the repository (rather than a detached GitHub Wiki
or external site) means it is versioned with the code and archived with every
repository snapshot — part of this project's own open-science practice.

## Project layer

| Artefact | Path | Job |
|---|---|---|
| Continuity | [continuity.md](continuity.md) | Cross-session state; the load-bearing handoff document |
| Working notes | [working-notes.md](working-notes.md) | Research lab notebook — empirical, chronological (`/observe`, `/handoff`) |
| Reflections | [`reflections/`](reflections/) | Meta-research — session reflection, session log, LLM observations, abductive reasoning (`/reflect`) |
| User observations | [user-observations.md](user-observations.md) | Shawn's observations about Claude's work (gated candidates) |
| Claude observations | [claude-observations.md](claude-observations.md) | Claude's observations about how we work together (default-keep) |
| Planning | [`planning/`](planning/) | Implementation plans, roadmaps, strategy documents |

`working-notes.md` (research record) and `reflections/` (meta-research) are
separate layers with separate owners — never write Observations into
reflection documents, and never reflect into working-notes.

## Key planning documents

- [planning/agentic-modernisation-plan.md](planning/agentic-modernisation-plan.md) —
  current milestone: agentic reproduction + FAIR lane, JAS corpus run
- [planning/active-todo-list.md](planning/active-todo-list.md) — task tracker
- [planning/credibility-implementation-plan-v2.0.md](planning/credibility-implementation-plan-v2.0.md) —
  assessment framework master plan (complete)

## Conventions

Pages carry YAML frontmatter (`title`/`tags`/`created`/`updated`/`status`);
tags come from the 24-term vocabulary in
`~/personal-assistant/wiki/index.md`. Filenames are lowercase-with-hyphens,
no dates. Reflection pages additionally carry the `/reflect` skill's
`priority`/`scope`/`audience` keys.
