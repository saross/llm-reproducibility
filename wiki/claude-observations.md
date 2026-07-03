---
title: "llm-reproducibility — Claude Observations"
tags: [human-ai-collaboration, llm-craft]
created: 2026-07-03
updated: 2026-07-03
status: seed
---

# llm-reproducibility — Claude Observations

A **Claude-owned** register of observations about how Shawn and Claude work
together on this project. The symmetric counterpart to
[user-observations.md](user-observations.md), with **default-keep**
semantics: these are Claude's working notes, not candidates awaiting
approval. Shawn may read, respond to, or prune them, but the default is that
they persist.

**The register axis is the observer** (who is observing, not who is observed):

- **claude-observations** (this file): things *Claude* observes — Shawn's
  working style and decision dynamics, plus Claude's own collaboration
  self-critiques. Default-keep.
- **user-observations**: things *Shawn* observes about *Claude*. Gated
  (accept / edit / discard).

**Boundary rule** (especially important in this repo, where the research
subject *is* LLM behaviour): collaboration dynamics live here; findings about
the pipeline, extractions, or LLM-as-research-subject live in
[working-notes.md](working-notes.md); narrative session texture lives in
[reflections/session-reflection.md](reflections/session-reflection.md). The
historical `reflections/llm-observations.md` predates this register and
remains as the LLM-as-data record.

Format: `## claude-obs N — YYYY-MM-DD: <one-line summary>` with
**Pattern.** / **Lesson.** / **How to apply.** sub-blocks. Never modify an
accepted entry in place — corrections land as new cross-referencing entries.

---

## claude-obs 1 — 2026-07-03: Conventions questions deserve the full landscape, not a binary

**Pattern.** During the wiki-migration decision, Shawn paused twice on what
looked like a settled two-option question (docs/ vs wiki/) to ask how the
split reads to *external users* and how research repos conventionally do it.
The answer (GitHub Pages builds from `docs/`, GitHub Wikis are unarchived
separate repos, OSF wikis are platform-specific) materially sharpened the
decision — and surfaced a reusable template convention (README disambiguation
map) that a bare A/B answer would have missed.

**Lesson.** When Shawn asks "how is this usually done?", he is testing his
own tooling conventions against community norms, not stalling — treat it as
a design review of the template, answer with the conventions landscape and
an honest "what I'd do starting fresh", and only then re-present the
decision.

**How to apply.** For infrastructure decisions in any repo, check whether the
answer generalises to the cross-repo template; if it does, say so explicitly
and propose the template amendment alongside the local fix.
