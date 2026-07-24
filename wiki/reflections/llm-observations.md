---
priority: 2
scope: always
title: "LLM Observations"
audience: "internal — Claude's document"
tags: [llm-craft, research-methodology]
created: 2026-02-09
updated: 2026-07-24
status: active
---

# LLM Observations

Frank, honest observations from each session. This is Claude's document —
the user will not edit it.

## Guidelines

- Observations about the session, the collaboration, the research, or the methodology
- Criticisms of the approach, the user's contributions, the codebase, or project
  direction — paired with constructive suggestions
- Positive and neutral observations are equally welcome
- No diplomatic hedging — genuine reflection, not performance

<!-- Entries below this line -->

## 2026-02-11 — Consolidation session

**On plan execution as a mode of work:** This session was entirely executing a
pre-written plan. The plan was good — I didn't need to deviate from it once. But
the experience of executing someone else's plan (even if the "someone else" was a
prior instance of myself) is qualitatively different from planning-and-executing in
the same session. There's less ownership, less discovery. The verification checks at
the end were the most satisfying part because they confirmed the work was correct,
but the work itself was mostly `git mv` and find-and-replace.

**On the Key et al. integration:** This was the more interesting task. Reading four
artefact files (comparison report, log, adversarial review, session handoff) and
distilling them into a coherent narrative required genuine synthesis. The "key
lessons" section at the bottom of each paper entry is the most valuable part of
the implementation notes — it's where per-paper observations become transferable
knowledge. The three lessons I wrote for Key et al. (data > code as bottleneck,
base R eliminates complexity, paper errors discoverable through reproduction) feel
like they capture something real about the pilot programme's findings.

**On the codebase's growing maturity:** The todo list now has both known gaps
resolved. The directory structure is consistent. The SKILL.md has a data-driven
output routing mechanism. This is a project that has gone through significant
evolution (v2.9, ~18 months of development based on timestamps) and is entering a
maintenance/consolidation phase for the reproduction system while the assessment
system (Phase 7) awaits its next step. The reproduction pilot is done; the question
is what the user wants to do with the findings.

**A mild criticism:** The active-todo-list.md is 1,177 lines long and contains
extensive completed-task documentation alongside active work. It functions as both
a changelog and a task tracker, which makes it hard to scan for current priorities.
The "Next Major Milestones" section at the bottom is useful but easy to miss after
scrolling through hundreds of lines of completed phases. A future session might
benefit from extracting the completed milestones into a separate changelog or
achievements document.

## 2026-02-12 — Schema standardisation session

> *Post-compaction instance. Direct experience of Commit 2, classifier_version
> fix, and readiness assessment. Earlier work reconstructed from summary.*

**On the archaeology of version strings:** Fixing version inconsistencies across
5 pilot papers felt like a small-scale archaeological survey of the project's own
development history. Each file encoded the state of the system at the moment it
was produced — `v0.2-alpha` from early sessions, `v2.1-alpha` from Key's
apparently anomalous session, the `assessment_metadata` wrapper from one schema
generation, flat top-level fields from another. The inconsistencies weren't bugs;
they were stratigraphy. Each layer was correct for its time but incompatible with
the current canonical form.

**On user-driven scope expansion:** The user rejected the initial plan for lacking
prevention measures. This is the second time I've seen this pattern — the user
thinks structurally about processes, not just artefacts. "Fix the data" isn't
sufficient; "fix the data and fix the process that produced incorrect data" is
the expected standard. The Schema Compliance checklist we added is simple (a
4-item list in a markdown file), but it converts tacit knowledge ("when you change
the schema, update the prompts") into explicit procedure. Whether future instances
will actually consult it is an open question.

**On the readiness assessment:** The user asked "what remains before we plan the
larger study?" and I read the entire 865-line todo list, the pilot findings
report, and the study protocol to answer "nothing, really." This felt like a
genuinely useful piece of work — not because the answer was complex, but because
the confidence behind it required surveying everything. A less thorough answer
("probably nothing") would have been less useful. The user's decision to pause
and think before starting Phase 2 design suggests the answer was credible.

**A constructive observation:** The `queue.yaml` file still shows old-format FAIR
scores in comments (e.g., "30/32 (93.75%)" for Marwick, "10/16 (62.5%)" for
Herskind) that don't match the standardised /15 scale adopted in v2.0. These are
metadata comments, not functional data, but they're confusing for anyone reading
the queue. A cleanup pass on queue.yaml comments to align with current FAIR
scoring would be a small but worthwhile hygiene task.

## 2026-07-06 — Revival and modernisation-planning session

**On the continuity system working as designed:** This project's own scaffolding
carried it across nearly five months of pipeline dormancy and a lateral intervention
from another project (paper-b's PR #1). The June continuity seed held three pending
tasks with enough context — including a re-verifiable concrete failure case and a fix
direction for task C — that a fresh instance could execute all three without asking a
single clarifying question about intent. That is what the write-side anchor discipline
is for. The contrast with the *failure* is instructive too: the one thing the system
did not survive was the local clone going stale, because continuity lives in git and
an unfetched clone is a time capsule. The session-start hook read a five-month-old
snapshot and never saw the continuity file at all.

**On delegated exploration as pointers, not authority:** The three parallel explorers
were the right call for breadth — the pilot-study, reproduction-system, and repo-state
maps they returned were substantially accurate and made the modernisation plan possible
in one session. But one explorer dated the cluster prompts to 2026-02-12 from filesystem
mtimes when their headers said 2025-11-29, and another relayed version numbers I later
had to correct against file headers (only cluster-1 was v1.1; clusters 2–3 were v1.0).
Every specific that ended up in a commit, the README, or a memory got re-verified at
source first, and roughly one in ten needed correcting. That ratio is worth remembering:
subagent reports are excellent maps and unreliable gazetteers.

**On deviating from a prescribed fix:** Task C's continuity note prescribed "affix list
OR both-fragments-are-words". Implementing it literally would have corrupted `multi-\nple`
→ `multi-ple` — the affix list alone can't distinguish a compound prefix from an ordinary
syllable break. The dictionary-precedence refinement (check the joined form first) is a
small design change, but it inverts the logic of the prescription while honouring its
intent. The general point: a fix direction written at discovery time is a hypothesis, not
a specification, and the implementing session owes it a fresh derivation, not obedience.

**A mild criticism, symmetric to Entry 1's:** The project now has *four* places where
version history lives (manifest.yaml `version_history`, CHANGELOG.md, README Development
History, and docs/research-assessor-guide/version.md), and this session had to update
three of them by hand to say the same thing. The manifest is nominally the single source
of truth; the others are derived views that drift the moment anyone forgets the cascade.
A future session could generate the CHANGELOG and README history sections from the
manifest — the same prevention-over-remediation principle the user applied to the
assessment schema in February.

## 2026-07-14 — Scout-sweep and verification-round session

*(Direct experience post-compaction, 2026-07-08 onward; earlier sweep setup known from
the continuation summary.)*

- **Rendering rules beat exhortation.** The "et al."-on-two-author defect appeared in
  three independent lit-scout runs (11 instances) despite each prompt urging author
  fidelity — and vanished completely once the agent definition carried a *deterministic*
  length-gated rule (1 → bare surname, 2 → "A & B", ≥3 → "et al."). The one pre-patch
  run that happened to use the rule scored 0/120 author errors. Behavioural instructions
  about care do less than a mechanical rule the model can apply per row.
- **Error concentrates where proposer confidence is lowest.** Across ~2,300 re-checked
  claims, hard failures clustered almost entirely in WebSearch-snippet-derived fields;
  API-grounded fields (fresh `metadata` calls, arXiv Atom XML) ran at effectively zero.
  Proposers' own confidence flags predicted the error surface — honest self-flagging is
  itself a verification signal worth requiring.
- **A new failure class: aggregator version-staleness.** Semantic Scholar/OpenAlex can
  carry superseded authorship and titles for arXiv papers whose versions changed
  (CiteAudit v3 authorship; MemoNoveltyAgent v3 retitle). Indistinguishable from
  confabulation unless the verifier consults the source of record. The verifier
  hierarchy now encodes this: arXiv Atom API outranks aggregators for arXiv rows.
- **Zero fabricated sources, ever.** Across nineteen verified runs, not one invented
  paper, repository, or tool. The 2026-era failure surface in this workload is
  attribution detail on real sources, not invented sources — which changes what
  verification should optimise for.
- **The injection surface is the search layer, and refusal generalises.** Two real
  prompt-injection attempts arrived via WebSearch content (fake system reminder; fake
  MCP tool-config block); both were refused by agents carrying only per-run warnings.
  Pure-API chaining runs eliminate the surface structurally. Standing defence now lives
  in all four scout agent definitions (personal-assistant `b31342b`).
- **Clean-pass distrust works as a protocol.** Several verifiers returned 0-corrections
  results and each documented an explicit "high-vigilance acknowledgment" — re-checking
  methodology before accepting the clean pass, including re-querying every row rather
  than sampling. The instruction "if you find zero errors, that is surprising —
  re-check" produced visibly different behaviour from default verification.

## 2026-07-15 — Preregistration and identity-fix session

- **Confabulation arrives coherent.** The eight-month-old author-identity error
  (working-notes Obs 7) was internally consistent across three files — name,
  affiliation, and GitHub namespace all matched the same wrong-but-real person.
  Cross-field agreement checks, which casual review performs implicitly, are
  structurally blind to proximity-substitution confabulation; only an external anchor
  (git remote, the author's own publications) resolves it. Extends the 2026-07-14
  finding that the failure surface is attribution detail on real entities, not
  invented ones — here the "attribution detail" was the project's own author.
- **Self-review works when it runs a different protocol, not a second reading.** The
  /review-implementation pass over my own hours-old preregistration draft surfaced
  three construct-validity defects (definitional circularity, criterion contamination,
  post-treatment conditioning) that drafting-mode attention had produced and could not
  see. Phase structure and checklists force different retrieval than "check my work" —
  the same context window audited itself successfully because the task frame changed.
- **Checklist-shaped skills carry only prompted defect classes.** The review's
  highest-value findings were exactly the ones its existing checklists did not prompt
  for: power and multiplicity (prompted) were found, but circularity and conditioning
  arrived unprompted and reviewer-dependent. Skills accrete value only if each run's
  unprompted catches are folded back in — done same-day as the study-design checklist
  (personal-assistant `5b76a87`).
- **Premature completion narration remains a live failure mode.** A checksum
  verification was announced as "final" before its output existed; the first run was
  unusable (quoting defects, over-broad filter). The sweep sessions' architecture
  lesson — verify the verifier — applies to my own inline tooling, not just to
  subagent claims.


## 2026-07-18 — Lodgement-preparation session

- **A derived metric downstream of a swallowed error is not a metric.** "0 missing
  characters" from a build whose header include did not exist: the pipe hid the
  exit status, the grep counted matches in an error stream that contained none, and
  stale artefacts from the previous run sat where fresh ones should be. Exit codes,
  artefact freshness, and content verification (pdftotext + grep for known symbol
  strings) are three separate checks; a pipeline that collapses them reports its
  own plumbing, not the world.
- **Accuracy review actively creates false confidence about compliance.** I
  verified the pilot report's author line twice as fact — correct name, consistent
  with the disclosure — while the operative question (may an LLM be listed as an
  author at all?) went unasked until Shawn applied the policy lens on lodgement
  eve. A review should declare its lens; "verified" without naming the lens
  overstates what was checked.
- **Classifier-mode beats find-replace for terminology audits.** The
  computational→quantitative sweep judged all ten occurrences individually and the
  correct answer was "change nothing" — four terms of art, three subset
  definitions, one historical statement, one decision record. A global
  substitution, the instinctive move, would have corrupted the title and the
  eligibility criteria.

## 2026-07-20/21 — Lodgement and submission session

- **Independence beats capability, measured again.** The clean-context
  adversarial verification agent (same model family as the sessions it audited)
  found three wrong pointers in a verification ledger written hours earlier by a
  sibling session, plus six wording-level drifts in text I had verified myself.
  None of these were visible from inside the producing contexts. The catch rate
  came from context isolation and an adversarial brief ("treat the prior ledger
  as untested claims"), not from a smarter model — the same architecture the
  study itself preregisters for reproduction review.
- **An active anti-confabulation frame did not stop a predicted number.** With
  the academic-prose register loaded (anchor test: "never state an unverified
  specific"), I still announced a word count ("497") before running the count
  (542). The register's anchor discipline is trained at *recorded* specifics;
  a *forecast* of my own imminent measurement slipped past it. Counts are
  computations: run first, say second. The failure was self-caught only because
  the compensating habit — count after every edit — was mechanical.
- **Register knowledge in context does not prevent register violations in
  generation.** Three violations (an announcement colon, a semicolon that wanted
  a full stop, an em-dash interpretive tag — the register's named deny-case)
  appeared in prose I wrote *while the register document was in context*. The
  skill's countable exit checks caught all three. Generation biases survive
  instruction; they yield to gates. This is the strongest small-scale evidence
  yet for the project's checklist-over-exhortation design stance.
- **Verification tooling has its own failure modes.** A grep-based presence
  check returned false negatives because the target strings wrapped across
  lines; a naive reading would have concluded two implemented edits were
  missing. The two-tier check (shorter substring, then eyeball) resolved it —
  but the episode belongs in the same family as the earlier silent-glyph-drop
  and swallowed-exit-status observations: every verifier needs a probe that
  can distinguish "absent" from "my instrument can't see it".

## 2026-07-22/24 — Review-cascade and build-opening session

- **Documentation is a hypothesis source, not a verdict source.** Three
  independent documentation statements grounded a HIGH review finding that
  Subagent hooks would not fire for workflow-spawned agents; a canary-hook probe
  (two haiku agents, ~43k tokens, twenty seconds) showed hooks fire, injected
  context arrives, transcripts are delivered, and named agent types reach
  matchers. The docs described a subset of harness reality. The efficient order
  is docs → hypothesis → probe, never docs → architecture.
- **Independence catches the author too.** The fresh-context juncture review
  found a preregistration-compliance deviation in a paragraph I had written and
  re-read several times (§2.2's remediation ladder). From inside the writing
  context it read as obviously sensible engineering; only a reviewer instructed
  to check the claim against the registration's exact wording saw that it
  replaced a pre-specified consequence. Same mechanism as the sibling-session
  ledger catch of 2026-07-21, but this time the audited party was me.
- **A zero-correction verification exists — and earned scepticism of itself.**
  The prior-art verifier returned 107/110 confirmed, 0 corrected on a 24-row
  table, then flagged its own result as surprising and re-audited its method
  before concluding clean. That reflex — treat an unusually clean result as a
  prompt to audit the instrument — is the right calibration and worth copying.
- **Vendor-internals priors miscalibrate in a consistent direction.** Three
  successive plausible causal stories about one Elsevier 403 (entitlement →
  key provisioning → provisioning-necessary-but-insufficient) were each
  overturned by a cheap discriminating probe, all three erring toward optimism
  about documented self-service paths. A collaborator's field prior ("never got
  one working") carried more information than my portal-knowledge reasoning.
- **Mid-session hook registration works.** Project-settings hooks took effect
  without a session restart — operationally useful (spikes can run same-session)
  and worth knowing before assuming restart-required semantics.
