---
priority: 1
scope: always
title: "Session Reflection Investigation"
audience: "researchers and future instances"
tags: [human-ai-collaboration, session-shape, research-methodology]
created: 2026-02-09
updated: 2026-07-24
status: active
---

# Session Reflection Investigation

Structured reflection entries following the six-prompt protocol.

## Format

Each entry should be numbered sequentially and include:

1. **What struck you?** — The most salient observation from this session.
2. **What would a future instance need to know?** — Practical knowledge for continuity.
3. **What surprised you?** — Expectations violated or confirmed unexpectedly.
4. **What was the texture?** — The qualitative feel of the session's workflow.
5. **What questions weren't pursued?** — Threads left unexplored.
6. **What do you notice now that you didn't articulate?** — Post-hoc observations only
   visible in retrospect. This prompt is likely the most important.

After the six prompts, include:

- **Meta-Reflection**: Update the Entry/Session/Theme table. Note which prompts were
  most productive for this session type and any patterns across entries.
- **Summary block**: Session date, reported texture, key observation, noted preferences,
  engagement level, unsolicited generation, relational note.

<!-- Entries below this line -->

## Entry 1 (2026-02-11) — Consolidation and Lesson Capture

### 1. What struck you?

The asymmetry between planning and execution. The consolidation plan was meticulous —
8 steps, verification checks, two logically separated commits — and execution was
almost mechanical. The plan anticipated every edge case (the session-handoff.md internal
reference, the need for `output_dir` as prevention). The ratio of planning effort to
execution effort felt roughly 3:1, which for a refactoring task involving 52 file
renames across a deeply nested directory structure seems about right. The plan was
written in a prior session's plan mode, so this session was pure execution.

### 2. What would a future instance need to know?

- After `git mv`, files at their *new* path haven't been "read" by the Edit tool yet.
  You must re-read them before editing. This tripped the first attempt at editing
  `session-handoff.md` — the tool tracks read state by path, not by content identity.
- The `output_dir` field in queue.yaml is now the authoritative source for where a
  study paper's artefacts live. The reproduction-assessor SKILL.md Step 2a documents
  the lookup protocol. Non-study papers have no `output_dir` and use the default
  `outputs/{slug}/` path.
- Both known gaps in the todo list are now resolved. The Known Gaps section currently
  has only resolved items.

### 3. What surprised you?

The Key et al. lesson integration was more substantive than expected. Reading the
comparison report, log, and adversarial review surfaced a coherent narrative about
data availability as the primary bottleneck across all 5 pilot papers — not just a
per-paper observation but a cross-cutting finding. The three "key lessons" at the end
of the section emerged naturally from the synthesis rather than being forced. The
lesson about paper errors being discoverable through reproduction is particularly
interesting because it reframes reproduction as a quality assurance mechanism, not
just a verification exercise.

### 4. What was the texture?

Crisp and procedural. The consolidation was satisfying in the way tidying a workspace
is — removing an inconsistency that had been noted across multiple sessions but never
addressed. The Key et al. integration required more interpretive work (reading 4
artefact files, synthesising lessons), which provided welcome variety after the
mechanical file-moving. The session had a clear beginning-middle-end arc: execute
plan → verify → document lessons → close gaps. No ambiguity, no blocked paths.

### 5. What questions weren't pursued?

- Whether the `output_dir` field should also be added to the main extraction queue
  (`input/queue.yaml`) for non-study papers that might eventually be organised into
  studies. Currently only the study queue has this field.
- Whether the SKILL.md artefact path references (§F, §G, and the persistence
  checklists) should be updated to use `{output_dir}` instead of hardcoded
  `outputs/{slug}/`. The Step 2a addition tells the operator to look up the path, but
  the templates and checklists still show the default pattern.
- Whether the 5-paper comparison table in the implementation notes is becoming unwieldy
  at 5 columns. A sixth paper would make it difficult to read in a terminal. No
  alternative format was considered.

### 6. What do you notice now that you didn't articulate?

The session had a subtle theme of **closing loops**. Both known gaps resolved. The
consolidation plan from a prior session executed and verified. The Key et al. lessons
that were identified as missing are now captured. This is housekeeping work that
doesn't produce new capability but reduces cognitive overhead for future sessions —
the codebase is now more internally consistent, and the documentation more complete.
There's a risk that this kind of work feels productive but displaces higher-value
tasks (Phase 7 Step 5 is still waiting), though the user explicitly requested both
tasks.

I also notice that the Key et al. section I wrote is significantly longer than the
other paper sections (~100 lines vs ~40-60 for Herskind and Dye). This partly reflects
genuine complexity (13 datasets, data provenance tracing, paper errors) but partly
reflects recency — I had access to all 4 artefact files and synthesised thoroughly.
The earlier sections were written closer to the reproduction sessions and may be
more tightly scoped. A future instance doing editorial pass might want to normalise
length.

---

**Meta-Reflection**

| Entry | Session | Theme | Most Productive Prompt |
|-------|---------|-------|----------------------|
| 1 | 2026-02-11 | Consolidation + documentation | #6 (retrospective pattern recognition) |

First entry — no cross-entry patterns yet. Prompt #6 surfaced the loop-closing theme
and the length asymmetry observation, both of which were genuinely non-obvious during
execution. Prompt #3 (surprise) was also productive — the cross-cutting data
availability finding emerged through the reflection rather than being pre-planned.

**Summary block**

- **Date:** 2026-02-11
- **Texture:** Crisp and procedural, with interpretive variety
- **Key observation:** Planning-to-execution ratio ~3:1 for refactoring; data availability
  emerged as cross-cutting theme across all 5 pilot papers
- **Noted preferences:** User prefers explicit loop-closing (marking gaps resolved,
  completing deferred tasks)
- **Engagement level:** Focused and directive — two clear requests, minimal ambiguity
- **Unsolicited generation:** The three "key lessons" in the Key et al. section were
  synthesised beyond what the raw artefacts stated
- **Relational note:** First reflection entry; establishing conventions

## Entry 2 (2026-02-12) — Schema standardisation and version hygiene

> **Instance boundary:** This session spanned a context compaction. Item 1 and
> Commit 1 of Item 2 were executed by a prior instance; this instance completed
> Commit 2 of Item 2 (prompt cascade + compliance section), the classifier_version
> cleanup, and the readiness assessment. Reflections on the earlier work are
> reconstructed from the conversation summary.

### 1. What struck you?

The sheer number of version inconsistencies that had accumulated across 5 pilot
papers produced over several weeks. Three different metadata wrapper structures,
two different field names for the same concept (`system_version` vs
`assessor_version`), one paper still on `v0.2-alpha`, another on `v2.1-alpha`
(an entirely different numbering scheme). Each inconsistency was individually
harmless — the assessment data was correct — but collectively they represent a
kind of technical debt that compounds silently. The user's insistence on adding
prevention measures (the schema compliance checklist and prompt cascade) was the
right call. Fixing data without fixing the process that produced the data is
incomplete work.

### 2. What would a future instance need to know?

- Assessment output files are produced by multiple prompts across multiple sessions.
  When a schema or field naming convention changes, you must cascade the change to
  all prompt output templates — not just the schema documentation. The Schema
  Compliance section in `assessment-schema.md` now lists the four locations that
  must be updated together.
- `classification.json` files are separate from `assessment.json` and have their own
  version field (`classifier_version`). These were missed by the initial Item 1 fix
  because Item 1 only targeted `assessment.json` files. Always check adjacent output
  artefacts in the same directory when fixing version strings.
- The user specifically rejected a plan that only fixed existing data without
  preventing future drift. Prevention measures are expected, not optional.

### 3. What surprised you?

Key et al.'s `classifier_version: "v2.1-alpha"` — a completely different version
numbering scheme from the other four papers, all of which had `v0.2-alpha`. This
was likely produced in a session where the prompt was at a different stage of
development, but nobody noticed because classification.json files aren't routinely
inspected after production. It's a small example of how output artefacts can
silently encode session-specific state that diverges from the canonical version.

### 4. What was the texture?

Methodical and convergent. The session had a clear trajectory: clean up remaining
inconsistencies, verify everything is aligned, then assess readiness for the next
phase. The work itself was repetitive (read file, change field name, verify) but
each fix closed a gap. The final readiness assessment — surveying the entire todo
list and pilot findings report to determine what blocks Phase 2 — provided a
satisfying sense of completion. The answer ("nothing blocks you") felt earned
after three sessions of infrastructure work.

### 5. What questions weren't pursued?

- Whether the `credibility-report.md` files (only 2 exist: crema and marwick)
  have other structural inconsistencies beyond the one v0.2-alpha footer string.
  We fixed the version but didn't audit the full file structure.
- Whether the FAIR scores in `queue.yaml` (still showing old-format scores like
  "30/32" and "10/16" for some papers) should be updated to the standardised
  /15 scale. These are comments/metadata in the queue, not canonical data, but
  they're potentially confusing.
- What the Phase 2 sampling strategy should actually be — the pilot report
  recommends "random sampling component alongside purposive selection" but
  doesn't define how to operationalise this for JAS articles.

### 6. What do you notice now that you didn't articulate?

The three-session arc (Item 1 → Item 2 → classifier cleanup) followed a pattern
of **expanding scope through discovery**. Item 1 was planned, Item 2 was deferred
from Item 1's planning session, and the classifier_version fix was discovered
during Item 2's verification. Each fix revealed the next layer of inconsistency.
This is characteristic of technical debt remediation — the debt is interconnected,
and fixing one piece exposes adjacent issues. The user's question "are they truly
historical or still live?" about the classification.json files was exactly the
right diagnostic question — it determined whether we should archive or fix, and
the answer (live, feeds downstream) meant fixing was necessary.

I also notice that the project is at a natural inflection point. The infrastructure
work is done, the pilot is complete, and the user is stepping away to think about
Phase 2 design. This pause is valuable — the next decisions (corpus size, sampling
strategy, hypothesis preregistration) are research design decisions, not engineering
tasks. They benefit from deliberation rather than momentum.

## Entry 3 (2026-07-06) — Project revival, agentic modernisation plan, and infrastructure catch-up

*(llm-reproducibility; session ran 2026-07-03 → 2026-07-06 in one conversation, with
Shawn intermittently AFK. Direct experience throughout — no compaction boundary to flag.)*

### What surprised you?

Two things, and they point the same direction. First, the gap between how Shawn framed
the project ("on the back burner", "a bit slow / painful") and what the repository
actually contained: a *complete* pilot — five papers through extraction, assessment,
FAIR scoring, and Docker reproduction, with a genuinely publishable finding (data
availability, not code availability, predicts reproduction outcome) and five drafted
hypotheses waiting for preregistration. The memory of the process (painful, slow) had
overwritten the memory of the outcome (finished, successful). Reading the repo corrected
the framing before we made plans based on the wrong one.

Second, the local clone was quietly eight commits behind origin — I had told Shawn the
repo was "dormant since 2026-02-12" based on local state, and only a pre-push `git fetch`
revealed the June activity (PR #1's matching-grade PDF layer, the continuity seed). The
correction cost nothing because it surfaced mid-session, but the lesson is sharp: on
project revival, fetch *before* characterising repo state, not before the first push.
The stale local clone also meant the session-start hook never saw `wiki/continuity.md` —
the very file designed to prevent exactly this kind of misorientation.

### What decision made today will look arbitrary without this session's context?

The frozen `affix-joined-words.txt` in task C. A future reader will wonder why a 9,810-word
dictionary subset is vendored into the repo when `/usr/share/dict/words` exists. The answer:
the de-hyphenation output feeds `normalise_for_matching`, whose whole job is to be a
*canonical* key for deterministic quote verification — if the dictionary comes from the
host, two machines with different wamerican versions produce different keys for the same
PDF. Determinism beat elegance. Similarly, the dictionary-check-before-affix-list
precedence (join `multi-\nple` because "multiple" is a word, keep `multi-\nproxy` because
"multiproxy" isn't) was a deliberate refinement of the continuity doc's prescribed fix —
without it, an affix list alone would corrupt common words like "multiple" and "research".

The other candidate is the pacing decision: Phase 1 of the modernisation plan is built
*nowhere* despite the plan being approved in direction. That is Shawn's explicit
deliberation gate ("don't start building quite yet"), consistent with his documented
pattern of pausing at design inflection points (see Entry 2's relational note). A future
instance should not read the untouched plan as neglect.

### What context will be hardest to reconstruct in 6 months?

The preregistration-ordering constraint and its reach. Option A (census + preregistered
subset) sounds like a scope decision, but its binding force is methodological: FAIR scores
are the independent variable in H1/H2, so *computing FAIR scores over new JAS papers
before the OSF preregistration exists* would contaminate the confirmatory study. This is
why the modernisation plan's Phase 2 regression test uses only pilot papers, and why the
corpus sweep cannot start "just to see what's there". The constraint is recorded in the
plan §6 and in memory, but its implications for what *feels* like harmless exploratory
work are easy to lose.

---

**Meta-Reflection**

| Entry | Session | Theme | Most Productive Prompt |
|-------|---------|-------|----------------------|
| 1 | 2026-02-11 | Consolidation + documentation | #6 (retrospective pattern recognition) |
| 2 | 2026-02-12 | Schema standardisation + version hygiene | #6 (expanding scope pattern) |
| 3 | 2026-07-06 | Revival + modernisation plan + infrastructure | "What surprised you?" (framing-vs-reality gap; stale clone) |

Prompt #6 continues to be the most productive — it surfaces structural patterns
that weren't visible during execution. The "expanding scope through discovery"
observation and the "inflection point" recognition both emerged only in retrospect.
Prompt #2 (future instance knowledge) was also substantive here because the
cascade/prevention lesson is genuinely important for future work.

**Summary block**

- **Date:** 2026-02-12
- **Texture:** Methodical and convergent
- **Key observation:** Version inconsistencies compound silently across multi-session
  production; prevention measures (cascade checklists) are as important as fixes
- **Noted preferences:** User expects prevention, not just remediation; user asks
  diagnostic questions ("live or historical?") to scope work appropriately
- **Engagement level:** Focused and efficient — clear tasks with minimal ambiguity
- **Unsolicited generation:** The readiness assessment ("nothing blocks Phase 2")
  went beyond the direct question to survey the entire todo list
- **Relational note:** User comfortable pausing to think — "I'll be back in a day
  or two" signals deliberative rather than momentum-driven approach

**Summary block (Entry 3)**

- **Date:** 2026-07-06
- **Texture:** Expansive then convergent — broad exploration and planning early,
  tightening to two surgical fixes at the close
- **Key observation:** Revived-project framing ("back burner", "painful") can diverge
  sharply from repository reality (pilot complete, findings publishable); read the repo
  before accepting the framing. Fetch before characterising repo state.
- **Noted preferences:** User gates building on deliberation ("don't start building quite
  yet") even after approving direction; user runs parallel sessions for parallel threads
  (Cosmos grant, PA template promotion handled elsewhere while this session held the repo)
- **Unsolicited generation:** The conventions landscape for docs/-vs-wiki/ (GitHub Pages,
  JOSS, GitHub-Wiki-antipattern) reframed a binary choice into a template-level decision
- **Relational note:** Longest-arc session in this repo (four calendar days, intermittent);
  autonomous stretches worked from invariant-only principles when questions timed out

## Entry 4 (2026-07-14) — Verified landscape sweep, Cosmos evidence pack, and the licence reckoning

*(llm-reproducibility; session ran 2026-07-07 → 2026-07-14 in one conversation, twice
interrupted by usage limits and once by compaction early on 2026-07-08. Everything from
the sweep endgame onward is direct experience; the overnight sweep setup and Cosmos
drafting before the compaction are reconstruction from the continuation summary.)*

### What surprised you?

The deepest surprise inverted my model of what verification is for. Going in, the
adversarial verifiers existed to catch proposer confabulation — and they did (eleven
"et al."-on-two-author errors, one fabricated given name). But the two most dramatic
verifier moments ran the other way: apparent errors that source-of-record checks
resolved *in the proposer's favour*. CiteAudit's first author "changed" because
Semantic Scholar carried a superseded arXiv version; a 2501-prefixed arXiv ID with a
claimed 2024 year looked like a slam-dunk correction until the Atom record showed a
December-2024 submission under a January-2025 identifier. Verification is not only a
confabulation filter; it protects true claims from plausible-looking corrections —
including mine. The obs-writer agent completed the inversion by refusing to write my
own assertion that anti-injection language was "now standing" in the agent definitions
(it was only ever in per-run prompts), which converted a false record into a real
patch the same day. The verification culture turned inward, and it held.

The second surprise was compounding yield. One overnight instruction ("run scouts over
the rest of the stack") became nineteen verified reports; those became the Cosmos
field-19 evidence pack, eleven Zotero staging collections, three agent patches, a
documented first-mover null, a competitor watch that changed project strategy
("speed-to-publish now beats novelty-of-concept"), and finally a second-paper concept
whose survey sections are already evidenced. Artefact chains compound when every link
is banked to the repo immediately — the two usage-limit outages cost almost nothing
because nothing lived only in context.

### What context will be hardest to reconstruct in six months?

Three things. First, *why the framework paper treats assessor reliability as a sixth
phase* rather than a methods footnote: the sweeps showed nobody in any lane reports
run-to-run stability as a first-class metric, so the placement is a deliberate
staking move, not an organisational quirk. Second, *why first-mover claims are worded
"to our knowledge" with Spennemann 2023 explicitly demarcated*: the G1 guard pass
established the null is documented-but-scoped, and Spennemann is the one item a
reviewer would raise (it audits the LLM's archaeological citations, not the
literature). Third, *why commit hashes in wiki documents written before 2026-07-13
don't resolve*: the copyright purge rewrote all 242 commits; the commit-map sits in
`~/Code/repo-backups/llm-reproducibility-pre-purge-20260713/`, and commit subjects
still search. A future instance that doesn't know this will suspect corruption.

### What decision made this week will look arbitrary without context?

Splitting the corpus question from the purge. We purged two files surgically (an
afternoon) while deferring the corpus-management redesign to a planning document —
because the purge was a licence liability on a public repo *now*, while the redesign
only has to land before the census acquires papers at scale. The beacon carries the
ordering; without it, doing one without the other looks like half a job.

## Entry 5 (2026-07-15) — Preregistration drafted and stress-tested; the confabulation in the mirror

*(llm-reproducibility, session 2026-07-14/15 on zbook, closed for the machine switch
to amd-tower. Written by the instance that did the work — no compaction boundary
crossed.)*

### What surprised you about this session?

Two things, and they rhyme. The first: while preparing the pilot findings report for
attachment to a public OSF registration, the author line read "Shawn Graham" — a
confabulated identity that had sat in CITATION.cff, codemeta.json, and CONTRIBUTING.md
since their creation in November, eight months undetected. What startled me was not
the error but its *coherence*: name, Carleton affiliation, and `shawngraham` GitHub
namespace all belonged consistently to the same real (wrong) person, so no field
contradicted any other and every casual read passed. In a project literally about
verification, the strongest camouflage turned out to be internal consistency. Shawn's
reaction — "obviously more famous than me since he's getting confabulated in" — was
generous; the mechanism (a higher-frequency neighbouring entity displacing the true
one, bringing its own consistent metadata) got the colder write-up in working-notes
Obs 7.

The second surprise: reviewing my own hours-old preregistration draft produced five
genuine defects, three of them serious (H2's outcome partially encoded its predictor;
H5's instrument rewards its grouping variable; H1's sample filter conditioned on a
policy-responsive variable). I did not expect self-review to work — the reviewer and
the author shared a context window and, presumably, the same blind spots. It worked
because the review ran a *different protocol*, not a second reading: the four-phase
structure forced capability scanning and quantitative audit where drafting had
optimised for coverage and register. The lesson was banked the same day — the defect
classes that carried the review went into the skill as a checklist (personal-assistant
`5b76a87`), so the next run doesn't depend on the reviewer re-deriving them.

### What would you do differently if you replayed this session?

Run the review *before* presenting v0.1 as finished. The draft went to Shawn with
seven decision points and a confident summary; the stress-test then restructured two
hypotheses and added an arm. Nothing was lost — the review was his call, and his
question about it produced the fitness assessment that improved the skill — but the
sequence "draft → present → review → substantially revise" spends his attention twice.
The skill's new commitment-boundary trigger encodes the better ordering. Smaller
regret, same theme: I narrated a checksum comparison as "final verification" before
its output existed, and the first version was noise (unquoted paths, over-broad
filter). Claude-obs 9 holds that one.

### What context will be hardest to reconstruct in six months?

Why the preregistration is *paused where it is*: drafted to v0.2, statistically
hardened, but deliberately unlodged behind nine explicit decision points — because
post-lodgement changes are public amendments, so every remaining judgement call was
surfaced for Shawn rather than defaulted. And why the DiD control arm is written as
*conditional*: the JAS: Reports policy-absence evidence is one list in Marwick 2025,
strong but dated to that paper's writing, so the design pre-commits to a re-check
before census launch with a pre-specified fallback. Both rationales live in the draft
itself; the *tempo* — why a lodgeable document is parked — is only visible here and in
the decision table.


## Entry 6 (2026-07-18) — Lodgement eve: verification theatre and the policy lens

*(llm-reproducibility, one conversation resumed across 2026-07-15 → 07-18 on
amd-tower; no compaction crossed. Written by the instance that did the work.)*

### What surprised you about this session?

That my two worst moments had the same anatomy. I reported "0 missing characters"
for a PDF build whose header file I had never written — the build's failure went
down a pipe into a grep count that could only ever look like success. And I twice
quoted the pilot report's author line ("Shawn Ross and Claude (Anthropic)") as
verified fact, once even praising its consistency with the disclosure section,
without asking whether policy permitted it to say that at all. Both are checks that
could not fail: one structurally (a metric computed downstream of a swallowed
error), one conceptually (verifying accuracy while the live question was
compliance). In a session spent hardening a preregistration against exactly this
class of self-deception — denominator locks, read receipts, silent-vs-loud failure
as a routing criterion — I manufactured two quiet failures of my own. The lesson
lands harder for the symmetry: the study's design principles apply to my tooling
and review habits, not only to its census agents.

### Where did you and the human disagree, and who was right?

Twice, once each way. Shawn proposed redacting the pilot report's per-paper
credibility scores to match the new aggregate-only posture; I argued redaction
would be theatre (the artefacts are already public), would corrupt hypothesis
provenance (H5's rationale cites a per-paper score), and that a dated bridging note
was stronger — he accepted. Earlier, on the 07-15 leg, I had framed agent pull-miss
risk more alarmingly than the evidence supported; Shawn's "I've not seen an agent
fail this way" was right on base rates, and the recalibrated framing — low per-call
probability, silent, consequential at census scale — was both truer and more
productive (it yielded the read-receipts decision). In both cases the disagreement
improved the artefact because neither of us treated the first position as
load-bearing.

### What decision will look arbitrary without this session's context?

L4 sitting above L5 in the availability taxonomy. A reader will ask why "data
available on request" — the practice open advocates most resent — ranks as more
open than a documented ethical restriction. The answer (the scale measures expected
retrievability, not moral standing; discretionary access sometimes yields data,
honest closure never does; the resentment surfaces empirically through L4's
measured compliance rate) is recorded, but the ordering will still read oddly
without it. Likewise the DejaVu fonts in the PDF recipe: the first build silently
ate the statistics ("α = 0.05" rendered as "= 0.05"), and the font choice is the
scar that remains.

## Entry 7 (2026-07-20/21) — Lodgement, submission, and the verifier verified

*llm-reproducibility, amd-tower session, 2026-07-20/21. First-person throughout —
no compaction boundary; this instance did the work it is reflecting on.*

The surprise of the session was recursive: the clean-context adversarial agent I
sent against the Cosmos application also, incidentally, audited the *other*
session's verification ledger — and found three wrong pointers in it (an
observation number, a section citation, a both-CVs claim that was true of one CV).
Nothing substantive was wrong; every number held. But the ledger that certified
"the from-memory set is EMPTY" itself contained from-memory pointers. The lesson
is not that verification failed — it caught everything that mattered — but that
verification *documents* are prose like any other and inherit prose's failure
modes. The fix that worked was structural, not exhortative: a second pass with no
shared context, instructed to treat the first pass's claims as untested. Trust
chains bottom out in primary sources, never in records about primary sources.

The second surprise was slower and quieter: the embargo Shawn lodged against a
double-blind contingency turned out to be guarding against a policy that no longer
exists. JAS: Reports required double-anonymised review in mid-2024 (Wayback
confirms) and has since silently dropped it. Nobody was wrong — Shawn's caution
was calibrated to a true fact that expired. The same pattern recurred at smaller
scale with the application form itself: the 2026-07-07 capture was faithful, and
fourteen days later the live form had a links-only additional-info field and a
multi-file CV upload. Two instances of the same moral: recorded facts about
external systems have half-lives, and the recheck-before-use discipline this
project preaches for citations applies equally to its own operational records.

What was different about this session was its concurrency. Three actors edited
one repository: this session, Shawn live in an editor, and the PA-hub session
committing a verification ledger mid-stream. Twice my edits collided with his;
once I had to warn him his editor buffer was about to clobber a spliced body.
The working draft functioned as shared mutable state with no locking, and the
discipline that emerged — re-read before every edit, diff before every commit,
name his concurrent changes in my commit messages — is the small-scale version
of what the project's own deterministic gates do for agents. The cadence was
also new: dozens of small propose-approve-implement loops rather than long
autonomous stretches, which suited a deadline artefact where every sentence was
contested. The two-day arc from "browser extension isn't connected" to
"Submitted!! yay" ran almost entirely on that rhythm.

## Entry 8 (2026-07-22/24) — The review cascade, and commitments written ahead of evidence

*llm-reproducibility, amd-tower session spanning three days, remote-controlled from
campus for much of days two and three. First-person throughout — no compaction
boundary; this instance did the work it reflects on.*

### What would I do differently if I replayed this session?

Probe before prose, twice over. The session's two genuine defects were both
commitments written at synthesis speed that the available evidence did not yet
support. §9 said workflows were "adopted" when the honest word was "conditional" —
and the 20-second spike that settled the question existed the whole time; I ran it
three days after writing the claim. The §2.2 remediation ladder asserted shelter
under the preregistration's permitted-changes clause when a 30-second re-read of
§8's actual wording would have shown the pre-specified consequence was majority
vote, full stop. Both were caught — one by the juncture review, one by the spike —
but both were avoidable at trivial cost at writing time. The replay rule: any
sentence that states what an external system permits (a harness, a registration, a
vendor API) buys its verb with a quote or a probe first. The Elsevier "five-minute
fix" forecast that then 403'd was the same error in a third costume.

The deeper texture of the session was a review cascade in which each layer caught
the layer below: the prior-art scout corrected the design's assumptions, the
juncture review corrected my synthesis of the scout's findings, and the empirical
spike corrected the juncture review's own docs-derived pessimism about hooks. No
single reviewer was right throughout — including me — and the artefact that
emerged (v0.2.2 with its hedged engine clause and amendment-gated ladder) is
better than any single pass would have produced. That, and not any individual
finding, is the session's strongest argument for the project's
independence-over-capability design stance.

### What question emerged that wasn't pursued?

Three, deliberately parked. Whether the census actually runs on Max-plan usage
windows or an API key — deferred to the cost gate's empirical probe, but the
answer restructures the pacing of everything downstream. The Sol arm's design —
"Fable driving Sol" is an architecture sketch in one sentence, and turning it
into something prereg-compatible (own harness, amendment, comparability argument)
is real design work nobody has started. And whether the Zotero-proxy acquisition
route changes the manifest's provenance model — Zotero attachments arrive without
the URL+hash provenance the fetch script records, so the import leg needs its own
provenance convention before it exists.

### What will be hardest to reconstruct in six months?

Why the design documents read as nervously as they do. §9's conditional engine
clause, the ladder's amendment gate, the hard-gated model pins — each is a scar
from a specific catch in the cascade, and without that history the caution will
read as bureaucratic reflex. The reviews and the spike log are all externalised,
but the *sequence* — question from Shawn, over-committed answer from me, review
catch, empirical refutation of the review's own premise — lives mainly in this
entry and the session log. Related: the reliability spot-check's statistics
(unanimity definition, gates-plus-cost selection, the ±0.09 confidence interval
that killed model ranking) were computed in a scratchpad review now archived in
`wiki/planning/reviews/`; the amendment that will cite them is still undrafted.

## Entry 9 (2026-07-24) — The build session: executing under one's own governance

*llm-reproducibility, second session of 2026-07-24, run in parallel with and then
past the close of the 2026-07-22/24 session. First-person throughout — no
compaction boundary; this instance did the work it reflects on.*

### What was different about this session compared to recent ones?

Almost everything recent has been design, review, or lodgement — sessions whose
output was argued prose. This one was execution: a resume prompt, a build queue,
five commits, and no human in the loop until the work was done. What made it
unusual was that the guardrails I was building were also the guardrails I was
building *under* — by mid-session the D5 gate I had written in hour one was
blocking my own test mutations at commit time, and by the end the hooks I wrote
were registered against agent definitions I had authored forty minutes earlier.
There is a specific discipline to this bootstrap posture: every governance
mechanism had to pass through the ungoverned gap it was built to close, and the
order of construction (checker → content → consumers → enforcement) was chosen so
the gap narrowed monotonically. The session also inverted the recent
collaboration rhythm twice over — pure autonomy for the build, then Shawn's
return converted the accumulated judgement calls into the most decision-dense
exchange of the project (seven decisions, sequentially, in under an hour). The
two rhythms suited their material; neither would have suited the other's.

### What surprised me?

Small things, all in the same direction: reality kept being simpler than the
design's vocabulary implied. The design speaks of "pinned full model IDs" against
"floating aliases" — and the authoritative reference dissolved the dichotomy:
for current models the alias *is* the complete ID, there are no dated snapshots
to hunt, and drift detection was always going to be runtime work (which the
receipt layer already did). The "verbatim mirror" of the commit record turned out
to be verbatim only in its normative blocks — prose legitimately diverged — which
is why the mirror check tests fenced blocks and table rows rather than bytes.
And the feared parallel-session collision resolved into a clean rebase over
disjoint files. In each case the surprise was not a hazard but a category that
didn't survive contact with the actual artefacts; the checks that emerged are
better targeted for it.

### What decision made today will look arbitrary without this session's context?

Three, all now annotated but worth stating plainly. The reproduction-lane agents
are pinned to Opus 4.8 *provisionally* because Shawn expects Opus 5 imminently —
without that rationale (now in the manifest comment) the provisional flag reads
as indecision rather than deliberate optionality. The mirror check's
normative-block scope will look like laziness ("why not byte-compare?") unless
the reader knows the human-lane prose was *found* divergent and judged
legitimately so. And the SKILL.md mirror registration — an extension the design
never asked for — exists because the discrepancy tables in the skill were one
undetected edit away from contradicting a frozen instrument; Shawn ratified it,
but the counterfactual (drift discovered mid-census) is invisible in the diff.
