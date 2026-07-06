---
title: "llm-reproducibility — Claude Observations"
tags: [human-ai-collaboration, llm-craft]
created: 2026-07-03
updated: 2026-07-06
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

## claude-obs 2 — 2026-07-06: Shawn orchestrates parallel sessions; paste-ready handoffs are the interface

**Pattern.** While this session held the llm-reproducibility thread across four
calendar days, Shawn ran the Cosmos grant discussion and the personal-assistant
template promotion in *other* sessions — then returned here saying both were
already done. The paste-ready prompt I produced for the PA promotion was
consumed verbatim by one of those sessions. He treats sessions as scoped
workers and himself as the orchestrator routing artefacts between them.

**Lesson.** A session's job is to keep its own thread clean and to produce
*transferable* artefacts at its edges — paste-ready prompts, committed plans,
anchored memories — because the consumer of those artefacts is often another
Claude instance, not Shawn directly. Cross-session state that lives only in
conversation is lost to the orchestration.

**How to apply.** When work touches another project or could be delegated to a
parallel session, offer a copy-paste-ready prompt (as with the PA promotion)
rather than a description of what to do. Assume any artefact might be read by
an instance with zero context from this conversation.

## claude-obs 3 — 2026-07-06: Direction approval is not build authorisation

**Pattern.** Shawn approved the modernisation plan's direction (Option A,
architecture, phases) and in the same breath said "don't start building quite
yet — I need to spend a bit more time with your responses." Days later he
still sequenced loose ends (task C, README) *before* the build. This mirrors
the February pattern ("I'll be back in a day or two") logged in Entry 2's
relational note: at design inflection points he deliberately inserts a
deliberation gap between deciding and executing.

**Lesson.** For Shawn, agreeing a plan is a checkpoint, not a starting gun.
The failure mode to avoid is momentum — treating an approved plan as licence
to begin Phase 1 in the next idle moment. The build trigger will be explicit.

**How to apply.** After any substantial plan is approved in direction, record
the build as ON HOLD in the plan status and continuity (done this session),
and wait for an explicit "go" before creating implementation artefacts — even
when autonomous time is available and the work is reversible.
