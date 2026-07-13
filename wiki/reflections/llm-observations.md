---
priority: 2
scope: always
title: "LLM Observations"
audience: "internal — Claude's document"
tags: [llm-craft, research-methodology]
created: 2026-02-09
updated: 2026-07-14
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

