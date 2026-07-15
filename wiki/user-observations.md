---
title: "llm-reproducibility — User Observations"
tags: [human-ai-collaboration]
created: 2026-07-03
updated: 2026-07-15
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

## 2026-07-14 — Run-verify-bank makes overnight/AFK programmes cheap to interrupt

*(Accepted by Shawn 2026-07-14, edited: interruption-event specifics dropped;
core pattern retained. Candidate 4 from the same handoff discarded.)*

Large autonomous programmes (the six-lane scout sweep and its follow-up rounds)
are worth launching when Shawn is AFK or overnight, provided the discipline
holds: every intermediate product is verified and banked to the repository the
moment it exists — never held only in conversation context. Under that
discipline, interruptions of any kind (context loss, usage limits, session
death) cost almost nothing: the sweep survived several and resumed from
artefacts, not memory. Shawn's verdict on reviewing the results was that the
outcome justified the cost of running long.

**What generalises:** the trigger for launching a big autonomous run is not
"is there enough context budget?" but "is every artefact banked before it is
needed?" — a compaction-resilient state file plus incremental commits make the
answer yes. Pairs with the compressed-delegation entry below: banking is what
makes both patterns safe.

## 2026-07-14 — Compressed delegation: when numbered task lists work without a questions round

*(Accepted by Shawn 2026-07-14, with elaboration requested on his good practice
and the appropriate circumstances. Kept separate from the entry above by
Claude's judgement — that one governs when to launch autonomous programmes;
this one governs how to steer interactive sessions — but they share the
banking precondition.)*

From mid-session Shawn issued numbered rapid-fire task lists (including
mid-turn additions such as "please also patch the lit-scout agent") and got
them executed and committed without a clarification round. What made that
safe was visible in *his* practice, not just Claude's:

- **Each item pointed at a durable referent** — a repo artefact, a verified
  report, or a numbered option from Claude's own summary ("do #4") — never at
  ambient conversational context that might have drifted.
- **Items were scoped to outcomes, not methods** ("import all bibliography,
  one collection per workstream"), leaving implementation latitude where
  Claude had the fuller picture.
- **He delegated only what evidence had already settled.** The agent patches
  came after three verifiers converged on the same prescription; the imports
  came after verification cleared the tables. Correctness had been
  adjudicated by the verification layer before the delegation, not by trust
  in Claude's say-so.
- **Judgement calls were explicitly withheld** from the lists — the §9
  verdicts, the authorship model, the force-push — and routed to himself.
- **Mid-turn additions were additive**, extending the queue rather than
  redirecting work in flight.

**Appropriate circumstances:** evidence-settled, reversible, git-tracked work
with clear completion criteria and an artefact trail. **Not appropriate** for
judgement calls, for irreversible/outward actions (see the boundary entry
below), or for work whose success criteria are still being discovered — those
warrant the slower propose-discuss loop.

## 2026-07-14 — High-stakes irreversible actions are Shawn's to execute; Claude pre-stages everything

*(Accepted by Shawn 2026-07-14: "leave forced-pushes and other high-stakes,
irreversible actions to me — I think we have this boundary about right at
present." Now the codified standing pattern.)*

The force-push publishing the history rewrite was declined at Claude's hands
and met with everything pre-staged: full mirror backup, the rewrite itself,
commit-map, restored remote, and three exact copy-pasteable commands. Shawn
ran them himself shortly after. The division of labour — Claude completes
every local, reversible, backed-up step up to the line; Shawn executes the
single outward irreversible step from prepared commands — is the standing
pattern for public-repo history operations and analogous high-stakes actions.
A permission denial at that line is routing, not rejection: split the
operation, finish the local half, and hand over a minimal, exact final step.

## 2026-07-15 — Session observations

*(All three candidates accepted by Shawn 2026-07-15: "user obs: keep 1, 2, 3".)*

**Candidate 1 — The confabulation catch came from the re-read habit, and landed
well.** While drafting the preregistration, Claude re-read the pilot report's
author line before attaching it to a public registration and found "Shawn
Graham" — a confabulated identity that had sat in CITATION.cff, codemeta.json,
and CONTRIBUTING.md since 2025-11-13. Shawn's in-the-moment reaction ("Hah…
obviously more famous than me") suggests the flag-not-propagate move was the
right call. The generalisable bit: the catch was produced by the standing
anti-confabulation rule (re-read specifics before citing them into anything
public), not by luck.

**Candidate 2 — The requested register ("direct, information-dense, no
filler") shaped a stress-testable deliverable.** Asked for a preregistration
in a dense, direct style, Claude delivered claim → sample → measure → test →
predicted-direction blocks rather than prose. Open question for Shawn's
verdict: did this land closer to the target register than the
'write like me' skill's output, and is the format worth reusing for other
instrument-grade documents?

**Candidate 3 — Verify-what-you-can, ask-only-the-irreducible.** During the
identity fix, Claude resolved the ORCID from Shawn's own published papers and
the repo URL from the git remote, but stopped to ask exactly one question —
current affiliation — where three candidates (Macquarie/ANU/FAIMS) were all
plausible and unverifiable from disk. One interruption instead of four;
nothing guessed.
