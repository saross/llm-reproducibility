---
title: "llm-reproducibility — Claude Observations"
tags: [human-ai-collaboration, llm-craft]
created: 2026-07-03
updated: 2026-07-18
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

## claude-obs 14 — 2026-07-18: Shawn banks conventions at the moment they crystallise

**Pattern.** Within minutes of the lodgement-materials convention stabilising
(plain text + verified PDFs + authorship posture), he asked for a /remember
capture of the whole approach; the Quarto-workflow question earlier went straight
to the inbox the moment it was deferred. Tonight's template — the inscriptions
`wiki/prereg/` directory — is itself the product of the same habit in an earlier
project.

**Lesson.** Convention capture is part of his definition of done. Freshly
crystallised workflow patterns are save-worthy when they stabilise, not at a later
curation pass — the inscriptions precedent shows the payoff compounds across
projects.

**How to apply.** When a reusable pattern settles mid-session (build recipe,
review posture, document convention), proactively offer the /remember or inbox
capture rather than waiting to be asked.

## claude-obs 15 — 2026-07-21: Shawn deflates his own claims at final review — draft to his ceiling

**Pattern.** Three times in one day, Shawn's final-pass edits calibrated claims
*downward*: "co-introduced preregistration to archaeology" → "argued the case
for" ("we published a paper arguing researchers should do it… let's not go too
far"); the collaborator entry capped at "the two sentences I was allocated as
proposer"; the pilot claim trimmed from "reproduced five papers" territory
before I even offered it. The corrections were never about grammar — always
about the gap between what was done and what the words implied.

**Lesson.** His ceiling is the strongest *literally accurate* claim; anything
that borrows even rhetorical inflation gets caught and costs a round trip. My
drafts trended one notch above his ceiling and his edits form a consistent
one-way ratchet down.

**How to apply.** Pre-calibrate: for any claim about his work, draft the
version he would write after his own deflation pass — state the act
("argued", "ran", "built"), not the outcome halo ("introduced",
"reproduced", "established"). Where a publication title carries the strong
verb, quote the title and let bibliography do the claiming.

## claude-obs 16 — 2026-07-21: Shawn thinks in submission surfaces — build the paste artefact early

**Pattern.** The working draft was verified, complete, and useless to him at
the form: "it's a bit hard to read / copy… no forced returns… plain text, as
with the preregistration forms." The same request-shape appeared at OSF
(unwrapped paste files) and again at the Cosmos form (fields in form order,
notes separated from copy text) — and both times the live surface differed
from our records (five-file cap; links-only field). He works from the actual
input surface, not the document.

**Lesson.** For Shawn, a deliverable that feeds a form isn't done until it
exists in the form's own shape — one paste block per field, flowing lines,
provenance visibly separated — and the surface has been re-checked at fill
time, not capture time.

**How to apply.** When any output targets an external interface, generate the
interface-shaped artefact from the verified source (committed generator, so
they cannot diverge) as part of the deliverable, not as an afterthought; and
treat any form/UI capture older than days as stale until re-screenshotted.

## claude-obs 17 — 2026-07-21: Self-critique — my own forecasts are unanchored specifics

**Pattern.** I told Shawn a candidate revision was "497 words" before running
the count; it measured 542. The academic-prose register — with its anchor
test — was loaded at the time. The rule I follow for recorded facts
("re-read the source before citing") has a blind spot for numbers I am about
to produce: a prediction of my own measurement feels like knowledge and
isn't. Related same-day miss: I hard-coded `assert == 498` into the paste
generator, freezing that turn's value as an invariant that would have blocked
Shawn's next edit (caught and loosened to the real invariant, `< 500`).

**Lesson.** Compute-then-say applies to my own outputs, not just external
sources; and today's measured value is not a constraint — encode the
*requirement*, never the *observation*.

**How to apply.** Never state a count, size, or diff summary in prose before
the tool call that produces it; in generated checks, assert the specification
limit, not the current reading.

## claude-obs 18 — 2026-07-21: Concurrent sessions and live edits — the draft is shared mutable state

**Pattern.** Shawn ran the PA-hub session (which committed a verification
ledger to this repo mid-stream) and edited the draft in his editor while this
session spliced generated text into the same file. Two of my edits collided
with his; once the risk ran the other way and he needed a stale-buffer
warning before saving over the spliced body. He treats this as normal
working style, not an exception.

**Lesson.** In Shawn's multi-session workflow, no file state older than the
current turn can be assumed; his concurrent edits are intentional inputs to
fold in (and name in commit messages), not noise to revert.

**How to apply.** Late in any interactive session: re-read (or diff) before
every edit to a file he touches; describe his concurrent changes in the
commit that sweeps them; and when I rewrite a file he likely has open, say so
explicitly so he reloads the buffer before his next save.

## claude-obs 19 — 2026-07-24: Shawn gates commitment in separable stages — never bundle his decisions

**Pattern.** Across three days: "hold — discuss first" on the weekend run, then
staged approvals (routing passes yes / run no); sign-off withheld until the
juncture review he requested; ratification given as four separable verdicts with
riders ("start with sonnet and opus, then ASK before Fable"); the amendment
deferred "to as late as possible just in case". He consistently accepts most of a
package and holds exactly the element with open risk or spend.

**Lesson.** His approval style is itemised, not batch. Presenting decisions as
separable line items with independent risk profiles gets fast, clean verdicts;
bundling would force him to either over-approve or block everything.

**How to apply.** Structure every approval request as discrete numbered items,
each with its own cost/risk, and expect partial acceptance. Record the riders
verbatim (ask-before-Fable is a hard gate, not a preference) and treat a held
item as a scheduling fact, not an obstacle.

## claude-obs 20 — 2026-07-24: His outsider questions at review boundaries are discovery probes — treat them as such

**Pattern.** "Would it be useful to use CC 'workflows' for any of this?" — asked
at sign-off, from the self-described non-programmer — surfaced the one execution
engine the expert-lane synthesis had never considered, reshaping §9 and then the
build. Earlier equivalents: the self-containment challenge on the corpus store
(which forced the registration-integrity argument into words) and "is anyone
identifiable"-class questions in other projects. The question's power came from
its altitude: he asks about capabilities and purposes, not implementations.

**Lesson.** When Shawn asks "would X help?" at a commitment boundary, the
expected value of a serious scoped answer is high — these questions have found
real gaps at a rate my own capability scans should envy.

**How to apply.** Never deflect such questions with a quick yes/no. Give the
scoped fit analysis (where it helps, where it does not, what it would break),
fold the answer into the governing document the same turn, and check whether the
new capability invalidates any existing design assumption — his workflows
question did, twice.

## claude-obs 21 — 2026-07-24: Self-critique — I wrote committed verbs on uncommitted evidence, three times

**Pattern.** §9 said workflows were "adopted" three days before the spike that
justified any verb at all; §2.2 claimed shelter under a prereg clause whose text
said otherwise; the Elsevier TDM checkbox got called "the likely five-minute fix"
and then 403'd. Three domains, one error shape: at synthesis speed I stated what
an external system permits without quoting or probing it first. Every catch came
from outside the writing context — the juncture review twice, reality once.

**Lesson.** My prose defaults to commitment ahead of evidence when the claim
concerns external-system behaviour; in-context re-reading does not catch it
because the claim reads as sensible engineering from inside.

**How to apply.** Claims about what a harness, registration, vendor API, or
policy permits buy their verb with a quote or probe *before* drafting — the
probes are almost always seconds long (the spike: 20 s; the §8 re-read: 30 s).
Where the probe must wait, the verb is "conditional on", not "adopted". This is
the write-side anti-confabulation rule extended from specifics to permissions.

## claude-obs 22 — 2026-07-24: Shawn prunes to terminal options — closure beats parking

**Pattern.** In the seven-decision pass I recommended "hold until the proxy
verdict" for the MQ TDM enquiry — the option-preserving choice. Shawn picked
"drop it" without hesitation. Same signature elsewhere in the project: 2 of 8
user-obs candidates discarded outright on 2026-07-22 where I would have
parked them; the superseded "weekend run" was deleted, not deferred, when the
validation phase absorbed its purpose. When a queue item's value depends on a
contingency, he prices the carrying cost of keeping it higher than I do.

**Lesson.** My recommendations skew toward optionality — park, hold, revisit —
which quietly grows the carry-forward list he then has to re-read every
session. He treats an explicit DISCARD as a first-class outcome, not a loss.

**How to apply.** When presenting decisions, make the terminal option a real
candidate with its case argued, not a reluctant third bullet — and when a
contingency would moot an item, say so explicitly (he'll usually close it).
Complements claude-obs 19 (separable stages): stage the decisions, but within
each stage, offer closure.

## claude-obs 23 — 2026-07-24: Self-critique — two standing guards were decorative this session

**Pattern.** Two rules that existed in writing failed to bind my behaviour.
The concurrent-session protocol says re-verify `0 behind` before pushing; I
ran the status check inside a compound `&&` chain where it *displayed*
`[behind 3]` and succeeded anyway — commit landed on a stale base, push
bounced. And the 2026-07-16 scratchpad rule (never pair substantive prose
with an AskUserQuestion dialog in the same turn) went unconsulted while I
structured the entire decision pass exactly that way; I only noticed when the
scratchpad happened to scroll past near session end. Both worked out — clean
rebase, Shawn engaged with the prose — but by luck, not design.

**Lesson.** A guard whose output is displayed rather than enforced is
decoration to an agent moving through a command chain; a standing rule stored
in a file I didn't read is indistinguishable from no rule. The fix is
structural, not attentional: wire state checks as failing conditionals, and
check the scratchpad's standing interaction rules *before* choosing an
interaction pattern, not after.

**How to apply.** Before multi-question exchanges: grep the scratchpad for
standing rules about the surface I'm about to use. Before any push in this
multi-machine setup: a behind-check that fails the chain, not one that prints.

## claude-obs 24 — 2026-07-24: Rationale arrives mid-turn — capture it in the governed record immediately

**Pattern.** Shawn dropped the load-bearing rationale for the provisional
model pins ("everyone expects Opus 5 to drop any day now") as a mid-turn
aside while I was already presenting the next decision. It was not an answer
to any question I had asked — it was him annotating a decision already made.
Written straight into the manifest comment, it converts a flag that would
read as indecision into recorded optionality.

**Lesson.** His decision rationale often arrives asynchronously and
informally, decoupled from the decision itself; the governed artefacts only
capture it if I treat the aside as a first-class input at the moment it
lands. Six months out, the rationale is worth more than the decision — the
decision is visible in the diff, the why is not.

**How to apply.** When a mid-turn aside explains a recorded decision, write it
into the artefact that carries the decision (manifest comment, continuity
bullet) in the same session — not into memory, not into the reflection layer
alone.
