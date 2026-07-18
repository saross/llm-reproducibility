---
title: "llm-reproducibility — Claude Observations"
tags: [human-ai-collaboration, llm-craft]
created: 2026-07-03
updated: 2026-07-15
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

## claude-obs 4 — 2026-07-14: When three verifiers prescribe the same fix, bring the patch, not the question

**Pattern.** Shawn's mid-turn "please also patch the lit-scout agent" came after three
independent verifier reports had converged on the identical prescription (length-gate
author rendering). He didn't want options or a proposal — the evidence had already made
the decision, and he expected the fix applied and committed. The same shape recurred
with the arXiv-handling question ("do we need to update the agents?"): once the failure
mode was demonstrated systematic, assessment and patch belonged in the same turn.

**Lesson.** For Shawn, converging independent evidence *is* the authorisation for
low-risk, reversible, git-tracked fixes. Asking "shall I?" after the third identical
verifier prescription reads as friction, not care.

**How to apply.** Distinguish evidence-settled fixes (apply, commit, report) from
judgement calls (§9-style — externalise and wait). The discriminator is whether
independent verification already made the decision, not whether the change is code.

## claude-obs 5 — 2026-07-14: A declined permission is a routing instruction, not a setback

**Pattern.** The `git push --force` for the history purge was denied at my hands. The
productive response turned out to be exactly right: split the compound operation,
complete every local/reversible step (backup, rewrite, remote re-add, commit-map),
stage the irreversible step as three exact commands, and hand it over. Shawn ran them
within the hour and confirmed without comment — the denial wasn't distrust of the
purge, it was (correctly) keeping the one outward irreversible action in human hands.

**Lesson.** On this project the boundary is precise: I rewrite history locally with
full backups; Shawn pushes it to the world. Pre-staging everything up to that line is
the collaboration working as designed, not a workaround.

**How to apply.** For any public/irreversible operation, structure the work so the
human's step is minimal, exact, and copy-pasteable — and treat a permission denial as
information about where that line sits, never as something to retry.

## claude-obs 6 — 2026-07-14: Correct false premises in the user's favourable memory, cheaply and immediately

**Pattern.** Shawn asked me to "keep the two working notes you created" — but they had
only ever been flagged as candidates, never written. The tempting path (silently write
them now and let the premise stand) would have ratified a false memory. Stating the
correction in one clause and writing the notes in the same turn cost nothing; the
obs-writer then caught *my* equivalent false premise (claiming anti-injection language
was "standing" when it was per-run only) and the same correct-then-fix pattern closed
it as a real patch the same day.

**Lesson.** Shawn's trust in the artefact record is the project's core asset — this is
a project *about* verification. Small favourable-to-me false premises are exactly the
ones most corrosive if ratified, and cheapest to correct at the moment they appear.

**How to apply.** When a request embeds a premise that flatters prior work ("you
created", "we already have"), verify it first; if false, correct it in a clause and
fulfil the intent in the same turn. Never let the fulfilment silently backdate itself.

## claude-obs 7 — 2026-07-15: Shawn treats methods like code — the review gate applies to designs

**Pattern.** Handed a complete preregistration draft, Shawn didn't line-edit it; he
requested `/review-implementation` over its methods "so that we stress-test them
before committing" — prioritising statistics but explicitly widening the net. He then
accepted every must-fix and low-effort finding wholesale and made exactly one design
decision himself (the DiD arm), once evidence was in hand.

**Lesson.** In this collaboration a design artefact is not done when drafted; it is
done when adversarially reviewed. The review gate Shawn applies to code and API spend
extends to methodology, and he expects the reviewer to be harder on the draft than he
would be.

**How to apply.** At future design milestones (instruments, protocols, analysis plans),
proactively offer the review pass rather than waiting for the ask, and budget a
same-session revision cycle. Reviewing one's own hours-old draft works when the review
runs a genuinely different protocol (capability scan / exploitation / quantitative
audit) rather than re-reading for agreement.

## claude-obs 8 — 2026-07-15: A domain expert's terminology question can be a design insight in disguise

**Pattern.** Shawn asked whether "quantitative" would beat "computational" for the H1
sample restriction — framed as a wording preference. The right answer was causal, not
lexical: code presence is post-treatment (the policy can cause it), so filtering on it
biases the comparison; the quantitative nature of the research is policy-invariant.
Shawn had intuited the correct boundary without naming the mechanism.

**Lesson.** His construct-precision questions are frequently hypotheses about design
validity wearing terminology clothing. Answering them at the lexical level would
squander the insight.

**How to apply.** When Shawn queries a category boundary or term choice in a design
document, check whether the boundary interacts with the causal structure (selection,
conditioning, measurement) before answering as a word-choice question.

## claude-obs 9 — 2026-07-15: Self-critique — verification code deserves the rigour of what it verifies

**Pattern.** My first cross-machine checksum comparison broke on unquoted filenames
with spaces and used an over-broad filter that swept in tracked files — producing a
wall of noise presented under the label "final verification". The null-safe redo took
two minutes and passed cleanly (30/30).

**Lesson.** A sloppy verifier is worse than no verifier: it consumes trust while
measuring nothing. Filename sets of unknown provenance get `-print0`/`xargs -0` by
default, and a verification step should never be narrated as "final" before its
output has been seen.

**How to apply.** Dry-run verification mechanics on one item before batch execution;
treat verification scripts as production code; keep the "final" label for output
actually in hand.

## claude-obs 10 — 2026-07-15: Shawn applies the anti-confabulation rule to his own memory

*(Augmentation entry: /handoff wrote obs 7–9 earlier this session; this covers the
post-handoff turns, per the symmetric dedup guard.)*

**Pattern.** Before letting the skill update proceed, Shawn flagged his own recollection
as unreliable ("I have a vague memory that they are symlinked… but I haven't updated one
in a while and have forgotten") and asked for two independent checks — the filesystem
and `/recall` — rather than authorising an edit on either his memory or mine. Later,
juggling parallel sessions, he asked directly whether `/reflect` had run rather than
guessing. Both moves treat human memory the way the project's standing rules treat
mine: as a pointer to be re-verified at the source, not an authority.

**Lesson.** The anti-confabulation discipline in this collaboration is symmetric and
Shawn models it himself. Infrastructure conventions especially (where his machines,
cron jobs, and my context all hold partial copies of the truth) get verified before
they get acted on. And ritual-state questions ("have we run X?") are legitimate load
to place on me — the session state is mine to track precisely so he doesn't have to
across parallel sessions.

**How to apply.** When Shawn prefixes a request with a hedged memory, treat the
verification as part of the request, not a preliminary — answer with what the source
of truth says, note where his recollection was right or stale, and only then act.
Volunteer ritual/state accounting (what has and hasn't run this session) whenever a
session nears close or he signals he's context-switching between machines or projects.

## claude-obs 11 — 2026-07-18: Shawn reviews instruments by interrogating design implications, not prose

**Pattern.** Every read-through pass on the preregistration produced
methodological challenges, not wording notes: window symmetry (→ 2022 start),
compute-cap arbitrariness (→ cap bounds scope, not membership), "available on
request" (→ six-level friction taxonomy), credibility-instrument maturity
(→ descriptive-only posture), AI authorship policy (→ report v1.2). Zero
comments on style across five revision batches.

**Lesson.** For instrument-grade documents his review is a design review;
polish is never the bottleneck. The highest-value preparation is anticipating
the methodologist's questions — circularity, boundary cases, policy
compliance, auditability — not tightening prose.

**How to apply.** Before presenting an instrument or protocol, run an explicit
design-review pass against those four lenses and surface the weak points
proactively; treat prose-level review as his lowest-priority need.

## claude-obs 12 — 2026-07-18: Deferral hooks, never bare "no" — Shawn's scope-control idiom

**Pattern.** Every scope pressure this session resolved to a named future
vehicle rather than a refusal: FAIR4RS (OSF amendment path), cloud compute
("let's not commit now"), Quarto workflow (inbox capture), Python support
(validated follow-on), late data responses (revise-and-resubmit window).

**Lesson.** Scope discipline with Shawn is not about refusing additions; it
is about finding each addition its correct future home, in the same breath as
the deferral.

**How to apply.** When a good idea threatens the current artefact, propose the
deferral vehicle immediately (amendment, inbox item, follow-on with
validation, limitation note) rather than asking whether to include it.

## claude-obs 13 — 2026-07-18: Self-critique — two verification failures with the same shape

**Pattern.** (a) I reported "0 missing characters" for a PDF build whose
--include-in-header pointed at a file I had never created; the pipe swallowed
pandoc's error and grep -c returned 0 on an empty error stream. Only separate
exit-status capture plus pdftotext content verification caught it. (b) I
twice quoted the pilot report's author line ("Shawn Ross and Claude") as
verified fact — even calling it "consistent with the §8 disclosure" — without
evaluating it against journal AI-authorship policy; Shawn caught it on the
eve of lodgement.

**Lesson.** Two failures, one shape: a check that cannot fail visibly is not
a check. A metric computed downstream of a swallowed error is not a metric;
verifying a fact's accuracy is not evaluating its compliance.

**How to apply.** In shell pipelines, capture exit codes separately from
derived counts. For lodgement/publication artefacts, run a distinct
policy-compliance lens (authorship, licensing, disclosure) after the accuracy
lens — accuracy review actively creates false confidence about compliance.
