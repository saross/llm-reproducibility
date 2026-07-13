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

## Pending review — 2026-07-14 handoff candidates (accept / edit / discard)

1. **(In-the-moment reaction, relayed)** On reviewing the overnight sweep: "ok,
   this is a great outcome — I see I ran us out of context and through a compact
   event, which I try to avoid, but these results were worth it." The
   run-verify-bank overnight pattern justified its context cost; worth treating
   compaction as an acceptable price for large autonomous programmes when every
   artefact is banked to the repo before it is needed in context.
2. **Compressed delegation worked without clarification overhead.** From mid-week
   Shawn issued numbered rapid-fire task lists (including mid-turn additions like
   "3. please also patch the lit-scout agent") and got them executed and committed
   without a round of questions — evidence that the artefact-banking discipline
   and verified reports made low-bandwidth steering safe.
3. **The irreversibility boundary held without friction.** The declined
   force-push was met with everything pre-staged (backup, rewrite, commit-map,
   exact commands), and Shawn ran the three commands himself within the hour.
   The division — Claude prepares everything up to the outward irreversible
   step; Shawn executes it — may be worth codifying as the standing pattern for
   public-repo history operations.
4. **Transparent corrections did not interrupt flow.** Twice the record was
   corrected mid-stream (the "working notes you created" had never been written;
   the obs-writer refused an unverified "standing rule" claim) and both times the
   correction plus the fix landed in the same turn — the honesty cost nothing and
   kept the artefact record trustworthy.
