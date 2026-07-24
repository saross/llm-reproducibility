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

## 2026-07-18 — Domain judgement → formalisation division of labour on instruments

*(Accepted by Shawn 2026-07-22: the formalisation captured the intent and the
pattern is worth naming — with the standing rider that critical-friend
pushback on his domain judgements remains welcome; the division of labour is
not a deference instruction.)*

Shawn supplied the discriminating domain insight ("data available on request"
is a practice open advocates particularly resent; registration with an
archive is different in kind — discretionary versus procedural access) and
Claude formalised it into the availability taxonomy's two named boundaries
(machine-retrievable at L2/L3; procedural-vs-discretionary at L3/L4), the
three-level analysis collapse, and the standardised L4 request protocol. The
result is now frozen in the OSF registration as H2's predictor variable.

**What generalises:** instrument co-design default — Shawn supplies the
discriminating judgement, Claude names the boundaries and encodes the
analysis structure; and Claude stress-tests the judgement itself rather than
merely formalising it.

## 2026-07-18 — Update-in-the-open when field experience contradicts the risk model

*(Accepted by Shawn 2026-07-22, edited: update-in-the-open is preferable, with
the symmetric rider to hold ground when the pushback is off-base — the goal
is calibration, not capitulation.)*

When Shawn challenged the pull-miss risk framing ("I've not seen an agent
fail this way"), Claude conceded the per-call point explicitly and relocated
the risk to where the evidence still supported it: silent failures,
census-scale accumulation, and the consistently-wrong-scorer case that
stability checks cannot catch (the n = 12 human subsample can). The
recalibrated framing, not the original, drove the read-receipts decision.

**What generalises:** when Shawn's field experience contradicts a risk model,
concede what his evidence covers and relocate the residual risk precisely,
rather than defending the original emphasis — and, symmetrically, hold
ground when his pushback misses the mechanism.

## 2026-07-18 — Productive pushback protected the pilot record (redact vs bridge)

*(Accepted by Shawn 2026-07-22: "I really appreciated the productive
pushback.")*

Against Shawn's instinct to redact the pilot's already-public per-paper
credibility scores for consistency with Phase 2's aggregate-only policy,
Claude argued record integrity (published artefacts), provenance (H5's
rationale derives from them), and supplied the alternative in the same
breath: the bridging note plus the registered wording that the restriction
"is a Phase 2 policy… not a retraction of the pilot record."

**What generalises:** when an instinct risks the integrity of a public
record, object *with* a concrete alternative instrument — the pushback that
lands pairs the objection with the better option, not with compliance or bare
disagreement.

## 2026-07-18 — Deviate-with-documented-reason is the convention-transfer default

*(Accepted by Shawn 2026-07-22 as drafted.)*

Pointed at inscriptions/ for OSF lodgement materials, Claude located the
convention, adopted the house build recipe, and deviated deliberately where
the convention would have failed here (DejaVu fonts after Latin Modern
silently dropped statistical symbols; markdown-only for glyph-bearing
instruments), documenting each deviation in the README recipe. Postscript:
within 72 hours the same convention absorbed two further documented
extensions (line-break unwrapping; the tables ban) and generalised to the
Cosmos form-paste pipeline — the transfer-and-extend pattern proved
load-bearing immediately.

**What generalises:** transfer conventions by locating, adopting, and
deviating where they would fail — each deviation documented at the point of
use. Faithful copying without scrutiny and silent deviation are both wrong.

## 2026-07-21 — Two independent verification passes plus reconciliation

*(Accepted by Shawn 2026-07-22, as drafted. Candidates 6 and 8 from the same
handoff discarded.)*

The PA-hub session's claim ledger and the project session's clean-context
adversarial agent each verified the Cosmos application; reconciling them
caught three ledger pointer errors and six wording drifts that neither pass
saw alone. The producing context could not see its own from-memory pointers;
the second pass was instructed to treat the first pass's record as untested
claims, and that adversarial independence — not extra capability — produced
the catches.

**What generalises:** for submission-grade documents, run two independent
verification passes and reconcile them explicitly; the reconciliation step is
where the value concentrates, because it surfaces disagreements between
verifiers that single-pass review presents as settled facts.

## 2026-07-21 — Interface-shaped paste artefacts are the default for web-form output

*(Accepted by Shawn 2026-07-22, edited: elevated from question to standing
default — generalise the OSF prereg approach to any web-form-based output.)*

After "it's a bit hard to read / copy", the generated form-paste file (fields
in form order, NOTE lines separated from copy text, one flowing line per
paragraph, committed generator keeping paste text and verified source in
lockstep) became the actual submission tool. The same convention had already
worked twice at OSF (prereg summary and project metadata), and the friction
disappeared the moment the artefact matched the input surface.

**What generalises (Shawn's standing default):** whenever output targets a
web form or similar external interface, build the interface-shaped paste
artefact early as part of the deliverable — the OSF preregistration approach,
generalised: plain flowing text, form-order fields, provenance separated from
copy text, generated from the verified source, and the live surface re-checked
at fill time rather than trusted from capture.

## 2026-07-24 — Candidates

*Drafted at handoff (session 2026-07-22/24). All three ACCEPTED by Shawn
2026-07-24 (decision pass, second session). Candidate C's acceptance makes
confidence labels on external-system predictions a bilateral standing rule
(pairs with claude-obs 21).*

**Candidate A — The review-of-the-reviewer request paid for itself.** Your
"can we please /review-implementation at this juncture" caught a
preregistration-compliance deviation inside Claude's own signed-off-ready
synthesis (§2.2), plus the workflows hook risk and the undefined spot-check
statistics — four catches Claude's in-context re-reading had missed. Verdict
data point: "Great, I'm happy…", "Good catch", "great finds". The pattern —
fresh-context review of Claude's synthesis at every commitment boundary, even
when the synthesis is itself built from reviews — looks like a keeper.

**Candidate B — Remote-hands diagnosis with copy-paste probes worked.** The
Elsevier trail ran through your campus terminal via one-liners Claude designed
to print status codes and error bodies but never the key: three hypotheses
eliminated in four short probes, no credential ever touching the transcript,
and the entitlement test ran from the network that mattered. Worth keeping as
the default shape for anything network- or credential-dependent.

**Candidate C — Claude's confident vendor-behaviour predictions cost a
round-trip.** "The likely fix costs five minutes: recreate the key with the
TDM use case" — stated with more confidence than portal knowledge from
training merits, and wrong. If Claude had labelled it "worth trying first,
uncertain", the expectation would have been set right. You may want
confidence labels on any prediction about external-system behaviour as a
standing rule (Claude has self-imposed a version of this in claude-obs 21;
your verdict would make it bilateral).
