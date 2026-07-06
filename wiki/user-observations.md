---
title: "llm-reproducibility — User Observations"
tags: [human-ai-collaboration]
created: 2026-07-03
updated: 2026-07-06
status: active
---

# llm-reproducibility — User Observations

Meta-level log of things **Shawn observed about Claude's work** on this
project — what was very helpful or very unhelpful. Each entry is a candidate
drafted at session-close (`/handoff` step 4a), then accepted / edited /
discarded / replaced by Shawn. Empty is a valid outcome.

The register axis is the **observer**: Shawn-observing-Claude lands here;
Claude-observing-Shawn (and Claude's self-critiques) land in
[claude-observations.md](claude-observations.md).

These feed `~/personal-assistant/notes/working-with-claude.md` at curation
time (`/weekly-review`).

Format: dated entries; first line summary; body explains the context and
what generalises.

---

## 2026-07-06 — Drafted candidates (pending review)

Drafted at the 2026-07-06 `/handoff`. Mark with ✓ (accept) / ✏ (edit, with
revised text) / ✗ (discard) / replace inline. Unanswered candidates hold over
to the next session — silence never discards.

### Candidate 1: The conventions landscape reframed a tooling decision

When asked how docs/-vs-wiki/ splits are conventionally done, Claude answered
with the ecosystem picture (GitHub Pages builds from /docs, GitHub Wikis are
unarchived separate repos, OSF wikis are platform-specific) rather than
re-presenting the A/B choice. Shawn's in-the-moment reaction: "this is an
important point that I hadn't considered in this light while building my
tooling" — the answer changed not just this repo's layout but the cross-repo
template (README disambiguation map convention, since promoted to PA).

### Candidate 2: Paste-ready prompts as the cross-session interface

The copy-paste prompt Claude produced for promoting the README-map convention
was consumed verbatim by a parallel personal-assistant session ("I've already
implemented the PA template promotion"). Zero re-explanation needed. Producing
transfer-ready artefacts at session edges — rather than describing what another
session should do — appears to be the right default when Shawn orchestrates
parallel sessions.

### Candidate 3: Invariant-only autonomy when a decision gate timed out

When the study-shape question timed out (Shawn AFK), Claude proceeded only with
work invariant under all three options (housekeeping, plan document) and
recorded its recommendation without enacting it. On return, Shawn resolved the
decision in one line and nothing needed undoing. Candidate principle: at an
unanswered decision gate, do the intersection of all branches, never the
recommended branch.

### Candidate 4: Parallel explorers made revival fast but needed source re-verification

The three-explorer sweep produced a full, largely accurate state map of a
five-month-dormant project in one sitting — but ~1 in 10 relayed specifics
(file dates from mtimes, version numbers) needed correction against sources
before use. The pattern worked because breadth came from agents and every
committed/published specific was re-verified. Worth noting as a helpfulness
observation only if Shawn found the revival summary trustworthy in practice.
