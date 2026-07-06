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

## 2026-07-06 — The conventions landscape reframed a tooling decision

*(Accepted by Shawn 2026-07-06; candidates 2-4 from the same handoff discarded.)*

When asked how docs/-vs-wiki/ splits are conventionally done, Claude answered
with the ecosystem picture (GitHub Pages builds from /docs, GitHub Wikis are
unarchived separate repos, OSF wikis are platform-specific) rather than
re-presenting the A/B choice. Shawn's in-the-moment reaction: "this is an
important point that I hadn't considered in this light while building my
tooling" — the answer changed not just this repo's layout but the cross-repo
template (README disambiguation map convention, since promoted to PA).

**What generalises:** when Shawn asks "how is this usually done?", the useful
answer is the conventions landscape plus an honest "what I'd do starting
fresh" — it lets him test his own tooling conventions against community norms
rather than just picking between pre-framed options.
