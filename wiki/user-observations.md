---
title: "llm-reproducibility — User Observations"
tags: [human-ai-collaboration]
created: 2026-07-03
updated: 2026-10-04
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

## 2026-07-27 — Candidates

*Drafted at handoff (session 2026-07-27, amd-tower); held over 2026-07-27 and
carried through 2026-08-02. **Adjudicated by Shawn 2026-08-02:** A and B
ACCEPTED — B generalised at his direction to "investigate, explain, avoid"
(see its closing paragraph). C ("the context-budget check before the
wind-down question" — asking whether anything needs this context before
closing) DISCARDED as routine practice: "I always ask if I think there might
be loose ends". Its residue is systematised instead as handoff-protocol
step 0 (context-residue sweep), so the check no longer depends on him
remembering to ask.*

**Candidate A — "Can we converge X without a prereg update, or does it need an
erratum?" was the right question, asked at the right grain.** You did not ask
Claude to fix the second mirror, and you did not ask whether it *should* be
fixed. You asked what governance class the fix falls into — which is the
question that actually gated the work, and one Claude had left open by
flagging the finding without resolving its status. Answering it required
checking three separate things (frozen-artefact membership, whether the
vocabulary is registered text, whether mirroring is delivery or semantics),
and the answer — no erratum, no amendment — is what made a same-session
convergence legitimate rather than a governance risk. Asking for the
*category* before the action is a pattern worth keeping where registered
artefacts are involved.

**Candidate B — Asking "explain what went wrong so I can avoid it" produced a
better fix than a correction would have.** When the stale-ref collision
surfaced you did not ask Claude to be more careful; you asked for the
mechanism, and then proposed where the guard belongs (the generated handoff
prompt). That framing turned a one-off apology into two durable insertions —
this repo's `CLAUDE.md` and `handoff-protocol.md` step 6 — inside the same
turn. The counterfactual, "please fetch next time", would have produced
nothing durable. Worth noting the diagnosis was only possible because you
asked for it: Claude had already moved on to the reconciliation work.

*Generalised on acceptance (Shawn, 2026-08-02): the pattern is "investigate,
explain, avoid" rather than "fix".* When something looks wrong, the request
shape that pays is mechanism-first: run the cause down, explain it, then
derive where the guard belongs — a correction alone leaves nothing durable
behind. Corroborated the day it was accepted: "was it accidentally
discarded?" (the fifth pilot FAIR assessment) forced a four-command run-down
that found the artefact archived-not-lost, exposed two silent sweep
scope-narrowers, and yielded a new monitoring-plan entity class (E8), a
dated erratum correction, and working-notes Observation 20 — where "please
restore the file" would have produced none of it.

## 2026-08-02 — Sibling-project handover with a translation warning attached

*(Accepted by Shawn 2026-08-02. Candidates D and E from the same handoff
discarded: D — the "is there any reason not to merge?" question that stopped
the PR; E — naming the stopping condition inside the instruction. Candidates
A–C from the 2026-07-27 handoff remain held over and un-adjudicated.)*

**Handing over the sibling project *with* the warning that it would not
transfer.** Pointing me at map-reader-llm's audit apparatus while
saying in the same breath that it "won't translate exactly" pre-empted the
failure I was most likely to commit: importing a good, already-written charter
wholesale. It made "where the analogy stops" a required section rather than an
afterthought, and that section is where the actual thinking happened — the
decision *not* to build a JSONL ledger here, because our entities are
enumerable from the manifest every run and a parallel record would recreate the
exact drift pathology the corpus plan's decision D-10 exists to prevent.


## 2026-08-03 — Candidates — adjudicated 2026-10-04

*Drafted at handoff (session 0360402e). Pending review; A–C from
2026-07-27 remain held separately (A and B since accepted, C discarded).*

Verdicts (Shawn, 2026-10-04, as recommended): A and B **accepted** as
drafted; C **merged** into the 2026-08-15 batch's candidate D (the spend gate
names its billing route). The candidate text is kept below as the record.

**Candidate A — "While we are waiting" turned idle time into the session's
highest-value work.** You slotted the wide audit into benchmark wall-clock
time, and its findings (a receipt gate that had never validated anything)
landed early enough to fix before the expensive arm ran. The pattern —
fill known dead time with independent verification work, not with more
building — found the defect at the cheapest possible moment.

**Candidate B — Scoping by governance rather than by file list.** "At
least where it doesn't touch anything that can't be touched due to the
preregistration" gave the audit a *governance* boundary instead of a path
list — auditors read everything, remediation respected the frozen set, and
GOVERNED findings routed to gated processes instead of being either fixed
recklessly or skipped. A reusable way to authorise broad work inside a
registered study.

**Candidate C — The billing pre-clearance removed a mid-run stall.** Before
the benchmark you volunteered the Fable overflow arrangement ("charged the
account, we should be fine") plus a forward-looking ask (track tokens for
better estimates). The run never paused on a spend question, and the
per-spawn baselines you asked for now exist in three run-records.

## 2026-08-10 — Candidates

*Drafted at handoff (session 52a81f4b). **Adjudicated by Shawn same day:**
A DROPPED; B and C ACCEPTED — "both are good approaches going forward"
(pre-formed infrastructure proposals that operationalise a ruling; batched
decision points with recommendations as the default format for
decision-dense sessions). The 2026-08-03 candidates A–C above remain
pending.*

**Candidate A — The verified scout pipeline exceeded expectations, and said
so mattered.** Your in-the-moment reaction to the prior-art report — "this
is a richer haul than I expected" — arrived before verification, and the
verifier then removed four fabricated quotations from under it. The
pipeline's value was the *pair*: breadth from the cheap proposer, trust
from the adversarial pass. Worth recording that the enthusiasm survived
the corrections — the corrected report was still the decision-grade
artefact you wanted.

**Candidate B — Infrastructure proposals that operationalise your rulings
land best pre-formed.** When your licence ruling implied external API
checks, the harvester proposal arrived as a concrete design (deterministic,
receipt-covered, evidence identical across runs) rather than a question —
and your response was immediate adoption plus extension ("love it...
Dataverse / ADA and Figshare jump to mind"). The pattern: translate a
ruling's operational cost into a designed mechanism before presenting it.

**Candidate C — Batch decision points with recommendations enabled seven
rulings in two messages.** The numbered decision table (each point: what it
resolves, options, a starting recommendation) let you rule quickly where
you agreed, redirect where you disagreed (#1's construct reversal), and
ask precisely where the design genuinely needed your expertise (#6's
granularity question). Decision-dense sessions may want this as the
default presentation format.

## 2026-08-15 batch — adjudicated 2026-10-04 (drafted at handoff, session 04169f15)

Verdicts (Shawn, 2026-10-04, as recommended): A, B, C, and D **accepted** as
drafted. D also absorbs the 2026-08-03 batch's candidate C (billing
pre-clearance). For A, the standing practice is to review the halt-condition
mnemonics during runs; it was missed during the 2026-10-04 Opus 5.5 arms and
is owed at the next run.

**Candidate A — The tripwire mnemonic landed as wanted training.** Your
in-the-moment "thanks for the mnemonic, let's continue to review during
future runs so I can really internalise them" — after recalling three of
six stop-condition classes — converted a comprehension check that could
have read as a quiz into a standing feature you asked to keep. Data point:
recall scaffolds at ritual exits are helpful, not condescending, when the
gaps are closed collaboratively.

**Candidate B — Adjudicated findings, not raw agent output, made the
blocker rulings fast.** The clean-context audit returned four blockers; what
reached you was each one re-derived against the primary artefacts first
(B1 re-counted from the gate log and extended 9/15 → 39/45, B4's §4 text
re-read at source), with dispositions proposed. Your three rulings took one
short message. The pattern: verification-before-presentation turns audit
volume into decision speed.

**Candidate C — Unvarnished incident reporting let you defer process fixes
without losing the record.** Twice this session I shipped a git-state
mistake and reported it in the same message as the results, with the
residual named in the register. Your response — "we'll deal with preventing
future, similar incidents later" — deferred the process work while the
dated record kept it actionable. Honest same-breath reporting appears to
be what makes deferral safe.

**Candidate D — The spend gate needed one more field: where it runs.** The
C2 gate presentation covered model, mode, count, and cost, yet your
approval hinged on a question it hadn't answered — "runs here in Claude
Code, not a separate API call?" Billing *route* (plan allowance vs API
account) belongs in the standing gate template alongside cost.

## 2026-08-17 — Curiosity questions as audit probes (accepted from batch candidate B)

*(Adjudicated by Shawn 2026-08-17: B and C accepted; A dropped — "there's
no reason you should have thought of effort level, I only did because it
was important in map-reader"; D dropped.)*

Two casual questions each found a real gap this session: "what
thinking/effort levels are we using?" (→ a Claude confabulation caught
plus the unpinned-parameter finding) and "any other metadata we aren't
capturing?" (→ the opus `[1m]` served-variant marker and the telemetry
expansion). Light-touch steering in the curiosity register was more
productive per word than any formal review request in the session — and
the correct Claude response to such questions is artefact-checking
rigour with named sources, not conversational recall.

## 2026-08-17 — Escalating to /pre-run-review + clean-context audit was vindicated within hours (accepted from batch candidate C)

Shawn's call to stress-test the D3 block rather than run on the API gate
alone ("I'm still getting a feeling for when the usual gate is
sufficient") produced 19 findings including 5 pre-spend blockers — one of
which (an empty-set reconciliation reading clean) would have silently
hollowed the per-arm acceptance rule. His calibration instinct about when
a spend gate is not enough was empirically right, and the two-run
evidence base justified codifying the clean-context pass into the skill
the same day.

## 2026-08-17 (second session) batch — adjudicated same session

Verdicts (Shawn): A and D accepted (below); B (P3 substitution) and C
(halt discipline) dropped — sound behaviour, but routine
contract-following rather than observations worth the register.

## 2026-08-17 — The claims layer has no mechanical verifier (accepted from s2 candidate A)

The one error that reached Shawn all session was a claim-framing error —
"cheapest known passing configuration" asserted from an aggregate metric
whose components (already computed, already in context) contradicted the
ranking. Every mechanical layer (reconciler, assembler, format
contracts, quality checker) held; none of them checks claim framing.
Shawn's one-line question ("is it really cheaper?") was the only
verification layer operating at the synthesis level, and it overturned a
committed headline within minutes. Correction landed as a visible fix
commit (`5c193e3`), not a silent edit.

## 2026-08-17 — Build-while-waiting on unratified no-spend tooling is the right default (accepted from s2 candidate D, ruling attached)

While arms ran, Claude built the mechanical quality checkers it had
proposed but Shawn had not yet ratified (no-spend, read-only, pure
analysis over committed artefacts) and had cross-arm findings ready
within the hour — including the pack-utilisation separation (opus ~80%
vs sonnet 47–57%) that fed the selection argument. **Shawn's ruling
(2026-08-17): this is the right default.** Standing guidance: when a
proposed tool is spend-free, read-only, and squarely inside the agreed
work, build it during dead time rather than waiting for ratification;
the gate stays where it belongs — on spend, on governed artefacts, and
on anything hard to reverse.

## 2026-08-19 batch — adjudicated 2026-10-04 (drafted at handoff, session 92427cb5)

Verdicts (Shawn, 2026-10-04, as recommended): A **discarded**, because it
duplicates the build-while-waiting entry accepted on 2026-08-17 (second
session, candidate D). B and C **accepted** as drafted. The candidate text
is kept below as the record.

**Candidate A — the build-while-waiting ruling delivered on its first
outing.** The session opened blocked on Shawn's worksheet sitting;
under the standing default ruled at the previous close, Claude scoped,
built, tested, and pushed the `--arms` extension (`48568fb`) with zero
permission round-trips, and the session ended with the carry-forward
cleared rather than merely re-described. Evidence that ratifying
default behaviours converts dead time into work.

**Candidate B — ground-truth-first verification caught what no gate
could.** Before trusting the extended tool's novel output, Claude made
it reproduce known figures (legacy byte-identical diff against the
committed disputed-items; six-arm stability cross-checked against run
records). That habit — not any test or gate — exposed the vacuously
guideless statistic (90/90 spawns "guideless" post-A3). The failure
class is invisible to unit tests written alongside the same
misunderstanding.

**Candidate C — a direct ownership answer at wind-down.** Asked "any
outstanding tasks before we wind down? I *think* the ball is in my
court", Claude answered with a definite ownership audit (nothing
agent-owned; two named Shawn-tasks; one dated deadline) rather than a
hedge — which is what makes a multi-day absence safe to start.

## 2026-10-03 batch — adjudicated 2026-10-04 (drafted at handoff, session 003fda8b)

Verdicts (Shawn, 2026-10-04, as recommended): A, B, C, and D **accepted** as
drafted. D is accepted with its self-flagged counterweight (several briefs
carried errors that were corrected later). The candidate text is kept below
as the record.

**Candidate A — tracking minor errors as findings even when no score
moves.** Claude logged small defects as findings at every sitting —
records typed "Software" that hold data, creators missing from deposits,
two versions cited in one paper, a doubled DOI prefix — although none
changed a score. Shawn, in the moment: "it's really good that you're
tracking minor errors like incorrect typing … it shows how messy things
are, and demonstrates a real role for LLMs in producing metadata". The
running record became Observations 30–31.

**Candidate B — holding the governing principle steady across many
rulings.** Across ten sittings Claude carried the rulings forward as
named principles (AP-1 to AP-17) and checked each new case against them,
including the research-surface rule when the repair question tempted a
score lift. Shawn, in the moment: "Thanks for keeping the *principle* in
mind: scores assess published research surfaces."

**Candidate C — primary-source checks that overturned inherited claims.**
Checking at source found that amendment 2's precedent DOI was never in
the paper, that crema's published Table 1 matches v1.0.0 rather than the
date rule's v2.0.0, and that Clarivate's terms restrict the redistribution
Shawn had believed permitted. Shawn: "Excellent observation"; "a really
important finding".

**Candidate D — decision-focused briefs, with entailed items separated
from the real calls.** After Shawn asked to "focus on the judgement calls
I need to make … so that I can make a careful and informed decision",
the briefs split each section into decisions (with options, the
perversity check, and a recommendation) and nods. Most sittings then
closed in a single exchange. The counterweight, which Claude self-flagged:
several briefs carried errors that were corrected later (a supplements
framing, a double-counting argument, a misquote, a total off by one).

## 2026-10-03 (second session) batch — adjudicated 2026-10-04 (drafted at handoff, session 4d22016c)

Verdicts (Shawn, 2026-10-04): A, B, and C **accepted** as drafted; D
**discarded**. The candidate text is kept below as the accepted record.

**Candidate A (ACCEPTED 2026-10-04) — checking the registration before
answering a question about the model pin.** Shawn asked whether the Opus 5 pin was intentional.
Claude read the preregistration and amendments before answering. It
answered the question: the pin was a provisional default, and nothing
registered binds the lane. It also found that §8 already fixes the
regression criterion, adds a Crema leg, and orders the registered gate
after model selection. The run was reframed as a pre-gate shakedown before
any spend, rather than claimed as the gate afterwards.

**Candidate B (ACCEPTED 2026-10-04) — proceeding overnight inside the
existing gates.** Asked to
"proceed as far as you can overnight", Claude did the following with no
new spend:

- finished the post-run gate, persistence, and audit;
- reviewed the two subagents whose safety-classifier check had timed out;
- ran the value-identity check and wrote the results report;
- opened PRs #5 and #6;
- reported to cv-and-applications;
- registered E8-v2 and ran the six-arm concordance in a worktree.

Everything needing a ruling was queued rather than decided. Built to show
whether "as far as you can" was read as intended.
*Relayed reaction (2026-10-04, morning):* "this is excellent work".

**Candidate C (unhelpful; ACCEPTED 2026-10-04) — generalising rulings
beyond what was ruled.**
Claude turned Shawn's round-1 answers into general rulings R1–R4 for the
re-plan. Its wording of R3 ("Named values in the text are separate
targets") led the dye planner to enumerate text restatements of table
values that round 1 had excluded, and that Shawn had accepted as
excluded. Dye went from 23 targets to 34. Claude disclosed this at
triage, but the generalisation should have gone to Shawn before it went
into the prompt.

**Candidate D (mixed; DISCARDED 2026-10-04) — engineering against the
tool's grain.** To avoid
hand-copying 10 KB of arguments, Claude built a launcher script outside
the repository that ran a nested workflow. The permission dialog then
offered Shawn only "no" ("sorry, that workflow failed, I had no option to
approve, just a 'no'"). Claude recovered with the standard invocation plus
a checksum guard, which is a better design. The detour cost a round trip
and a failed approval at a moment when Shawn was trying to go to bed.

## 2026-10-04 batch — adjudicated 2026-10-04 (drafted at handoff, session c51bef29)

Verdicts (Shawn, 2026-10-04, as recommended): A, B, C, and D **accepted** as
drafted (A mixed, B and C helpful, D unhelpful). The candidate text is kept
below as the record.

**Candidate A (mixed) — a reversal brought cleanly, after an avoidable
first error.** Claude recommended ruling dye T02 "mechanical", partly on
the reviewer's untested earlier-release hypothesis. When Shawn asked
"routine fix or fail-and-uplift?", Claude checked the CRAN 1.5 and 1.6
source and found the hypothesis false. It said plainly that this
superseded the morning's ruling, and recorded the superseded ruling
visibly. The correction was helpful; the first recommendation should
have been checked before it was put to him.

**Candidate B (helpful) — explaining before asking for the ruling.** Asked
"can you give me a brief explanation of the BI-exclusion?", Claude
answered with the two tag types and real items (herskind I1, dye I1), and
named the effect on every arm. In the same reply it flagged and corrected
its own "6 of 9" from the previous question.

**Candidate C (helpful) — a no-spend build delivered review-ready.** In
one stretch Claude:

- fixed F-013 and F-015, with tests and a replay that left recorded values
  untouched;
- added the Opus 5.5 agent and manifest entries;
- verified the inputs byte-identical to the registered arms;
- wrote a design note pre-declaring how results would be used;
- ported the args checksum guard before launch.

The P4 probe then caught a harness constraint at zero cost.

**Candidate D (unhelpful) — a rule written from one observation.** After
P4's first attempt failed, Claude wrote "agent definitions load only at
session start" into the failure register as a rule. The harness
contradicted it within minutes. The correction was visible, but the
register is read later as guidance, and one failure did not justify a
mechanism.

## Pending review — 2026-10-04 (second session) batch (drafted at handoff, session c5ee7a27)

*Candidates for Shawn to accept / edit / discard / replace. Silence
holds them over — never discards.*

**Candidate A (helpful) — a finding that weakened an earlier ruling was
raised and bounded, not used as a reason to halt.** Mid-arms, Claude found
that some requests' output tokens are placeholders (F-019). It judged that
this was not a halt condition, giving reasons: it was pre-existing, it
affected cost only, and stopping could not fix it. It kept the arms going,
then quantified the bounds and showed that the morning's D4 "11% cheaper"
ordering did not survive them. Shawn's ruling was "Agree, add a note".

**Candidate B (helpful) — "is there a substantive lead?" answered with
item-level evidence.** Asked whether `high` or `xhigh` had any tangible
advantage, Claude reported:

- the three efforts differ on only 3 of 141 gate items;
- most of the 9 shared misses are one F2 rule that higher effort does not
  touch;
- reading depth is identical;
- the cost is $0.58 against $1.09 per scoring.

Shawn: "Great, confirm medium."

**Candidate C (mixed) — a backwards rule, corrected after approval.**
Claude's deprecated-function recommendation said "fail-and-uplift, unless
no public version runs the original name", and Shawn approved it as
recommended. Claude's next drafting pass caught the inversion and stated
the coherent rule. In the moment Shawn said: "ah, thank you, I agree with
your correction, sorry I missed it". The correction helped. But the error
was Claude's, and it put a backwards rule in front of him for approval.

**Candidate D (helpful) — "anything else we should consider?" answered
with concrete, recommended considerations.** After ruling the
fail-and-uplift line, Shawn asked what else to weigh. Claude gave six
considerations, each with a recommendation and a note on which needed a
ruling. All six were adopted; on "report what repairs would recover",
Shawn said "great idea". Two needed clarifications were settled with two
structured questions.

**Candidate E (helpful; Shawn's in-the-moment reaction, relayed) — the
project's momentum restored across the last few sessions.** At close
Shawn said: "thanks for a great session, we've really revitalised this
project, which had stalled for a while", and then "the last few sessions
were really very good, and I'm relieved/excited to have this work moving
again". The run of sessions from 2026-10-03 to 10-04 covered:

- the agentic reproduction lane and shakedown;
- the E8-v2 registration and concordance;
- the gates ruling;
- the Opus 5.5 arms and selection;
- the clarifications and the first mechanical checks.

These moved the study from a stall to a clear path to the registered
regression gate. What may generalise: long autonomous blocks inside
pre-approved gates, with dense batched rulings when Shawn is present,
restored throughput without loosening governance.

## Pending review — 2026-10-05 batch (drafted at handoff, session ef0412bd)

*Candidates for Shawn to accept / edit / discard / replace. Silence
holds them over — never discards.*

**Candidate A (helpful; Shawn's in-the-moment reaction, relayed) — a
self-contained brief let a peer model act without help.** Claude's review
brief for the Fable session carried the commit hash, files, reading order,
attack focus, ground rules, and reply route. Shawn: "Fable's check is in
progress, they got the mail and actioned it without any interventions
from me, which is exactly right". Fable's review then found four serious
and six moderate routes that both Opus reviews and Astra had missed.

**Candidate B (helpful; reaction relayed) — routing a gate through
cross-model review before relying on it.** Claude put PR #7 to Astra, then
Fable, and later sent the gate 1.3 design to both before building. Shawn:
"remember you have access to Fable and Astra for second opinions, that
seemed useful". The reviews changed the design's foundations: the record
boundary, binding rulings to evidence, and a fresh-computation policy.

**Candidate C (mixed) — options written in jargon needed a second round.**
"May break projects that write beside their code" prompted: "can you
explain the risk? I don't fully understand…". On conversions Shawn asked to
talk the trade-offs through. Claude's explanation, using herskind's
`ggsave()` line and saying the failure would be loud, not silent, settled
both quickly. The first framing cost a round-trip.

**Candidate D (unhelpful, reported in full) — Claude's test fixtures broke
the repository's git config.** Run by the pre-commit hook, the new
fixtures inherited `GIT_DIR`, set `core.bare = true` in the shared config
(so `git status` failed in the main checkout), and committed a fixture tree
over the PR branch. Claude stopped, diagnosed, repaired the config and
branch before any push, added a scrub and a regression test, and led its
next message with the incident. The repository had recorded the fix three
weeks earlier, and Claude had not looked. Shawn filed `/feedback`.

**Candidate E (unhelpful) — review briefs invited posting under Shawn's
name.** Claude's first two briefs to Astra and its first to Fable invited
findings "as a PR comment", which posts through Shawn's GitHub account and
breaks the outbound rule. Fable declined. Astra posted two reviews to PR
#7. Claude corrected the instruction in later briefs and recorded it as
claude-obs 70. Shawn to judge whether the two posted reviews are
acceptable.
