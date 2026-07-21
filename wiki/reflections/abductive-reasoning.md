---
priority: 4
scope: conditional
title: "Abductive Reasoning Investigation"
audience: "researchers"
conditions: "debugging with surprising results, hypothesis generation, belief revision, default-following corrections"
tags: [llm-craft, research-methodology]
created: 2026-02-09
updated: 2026-07-21
status: active
---

# Abductive Reasoning Investigation

Episodes of abductive reasoning, hypothesis generation, and belief revision
during sessions.

**Only update if the session involved relevant episodes**: debugging with
surprising results, hypothesis generation, belief revision, or
default-following corrections. For routine implementation or execution
sessions, explicitly state the assessment and skip.

<!-- Entries below this line -->

### 2026-02-11 — Assessment: No qualifying episodes

This session involved executing a pre-planned refactoring (file moves, path updates) and
synthesising existing artefacts into documentation. No debugging with surprising results,
no hypothesis generation, no belief revision, and no default-following corrections occurred.
Skipped.

### 2026-02-12 — Assessment: No qualifying episodes

Schema standardisation and version string cleanup. Work was procedural: read files,
identify inconsistencies against a known canonical form, apply fixes, verify. The
classifier_version discovery (v0.2-alpha persisting in classification.json files
adjacent to already-fixed assessment.json files) was a minor surprise but not
abductive — it was straightforward deduction from "if we fixed version X in file
type A, the same version likely persists in adjacent file type B." No belief
revision or hypothesis generation occurred. Skipped.

### 2026-07-06 — One qualifying episode: the dormancy revision

**Surprising fact:** A routine pre-push `git fetch` reported the local clone 8 commits
behind origin — after I had already asserted to the user, in a delivered summary, that
the repo had been "dormant since 2026-02-12".

**Probe:** `git log HEAD..origin/main` and a diffstat before any push or rebase.
The commits were May–June 2026: a merged PR adding a PDF matching layer (built in a
*different* repo's session), a `wiki/continuity.md` seed carrying pending tasks, and a
file relocation.

**Belief revision:** "The project is dormant" → "the *pipeline* is paused, but
infrastructure work continued laterally from an adjacent project, and there exists a
continuity document that supersedes my session-start picture." The revision was not
merely additive — it changed the plan (three pending tasks became session work), changed
a public claim (the plan document's dormancy framing needed correcting before commit),
and revealed *why* my orientation was wrong (the session-start hook had read a stale
clone, so the continuity file designed to orient me was invisible).

**What made it abductive rather than deductive:** the anomaly (behind 8) did not entail
the explanation. Candidate hypotheses at the moment of surprise: another *clone* of this
session's work (double-session collision — the dangerous case), an automated process,
or forgotten manual commits. Inspecting authorship, dates, and content selected the
best explanation (lateral single-author work from the paper-b project) and ruled out
the collision case, which determined that a simple rebase was safe. The generalisable
correction: on project revival, fetch and read `HEAD..origin` *before* forming a state
assessment, because absence of local evidence is not evidence of absence when the
evidence lives in a distributed system.

### 2026-07-14 — Assessment: Qualifying episodes (three)

This session qualifies — three genuine surprising-fact → probe → belief-revision
sequences, all in the verification layer.

**Episode 1 — the 2501 identifier that wasn't 2025.** Surprising fact: a proposer
claimed year 2024 for arXiv `2501.10385`, whose identifier prefix denotes the
January-2025 announcement cycle. Hypothesis (mine, flagged to the verifier as a likely
silent error): the proposer misread the v1 date. Probe: the verifier fetched the arXiv
Atom `<published>` field directly. Revision: `2024-12-18` — a late-December submission
issued a January identifier. The proposer was right; my heuristic ("ID prefix ⇒ year")
was the error, and it would have *introduced* a defect if applied without the probe.
Lesson: identifier conventions are administrative metadata, not publication facts.

**Episode 2 — confabulation or staleness?** Surprising fact: Semantic Scholar and
OpenAlex both listed a different first author for CiteAudit (`2602.23452`) than the
proposer's "Shi et al.", and a different title for MemoNoveltyAgent (`2603.20884`).
Competing hypotheses: proposer confabulation (the base-rate expectation the whole
verifier architecture assumes) vs aggregator lag. Probe: version-current arXiv records.
Revision: both papers changed between arXiv versions (authorship reordering; retitle) —
the aggregators were stale, the proposer current. This generated a new named failure
class ("aggregator version-staleness"), now encoded in the verifier's source-of-record
hierarchy. Belief revised at the architecture level, not just the instance level.

**Episode 3 — the marwick extraction source.** Surprising fact: extraction metadata for
a closed-access article recorded `source: null`, making its licence status
undecidable on paper. Hypothesis: the text came from the closed version of record
(no preprint PDF anywhere in the tree; only the VoR DOI recorded). Probe: first-page
text of the on-disk corpus PDF. Confirmation: Elsevier VoR banner — the hypothesis
held, the file joined the purge, and the fix generalised into a provenance rule
(extractions must record source file + hash) in the corpus-management plan.

### 2026-07-15 — Qualifying episodes (two)

**Episode 1 — whose name is on the pilot report?** Surprising fact: the pilot findings
report's author line read "Shawn Graham" — a different, real digital-archaeology
scholar — during preparation for OSF attachment. Competing hypotheses: a deliberate
early collaboration I lacked context for, vs a confabulated identity from the
scaffolding-generation era. Probe: git author config, user email, repo remote
(`saross`), and ORCID resolution against author lines in the style-corpus copies of
Shawn's own publications. Revision: confabulation, and wider than the report — the
same coherent wrong identity (name + Carleton + `shawngraham` URLs) sat in
CITATION.cff, codemeta.json, and CONTRIBUTING.md since 2025-11-13. The instructive
part: the competing-hypothesis step mattered, because the extracted text of
sobotkova-et-al-2016 *legitimately* mentions the real Graham — one more grep hit that
had to be classified as genuine citation, not error, before the sweep could be
declared complete. Lesson: internal consistency is camouflage; classification of each
occurrence against an external anchor, not pattern-matching on the name, is what
separated the six fixes from the one legitimate mention.

**Episode 2 — is JAS: Reports a valid policy control?** Surprising fact (welcome
kind): the difference-in-differences design needed JAS: Reports to lack the
reproducibility-review policy, and this was assumed but unevidenced. Hypothesis:
Reports, as the sister journal, was not covered by the January 2024 Associate Editor
for Reproducibility appointment. Probe: ScienceDirect journal pages returned HTTP 403
(the pilot's own Finding 5 biting the project that documented it); web search
conflated the two journals; resolution came from the locally held CC BY Marwick
preprint, whose text enumerates the 2024 AER adopters (JAS, Advances in Archaeological
Practice, Journal of Field Archaeology, American Antiquity) — Reports absent.
Confirmation with a caveat: evidence is dated to that paper's writing, so the
registration pre-commits to a guidelines re-check before census launch with a
pre-specified fallback. Lesson: the licence-clean local corpus is not just a
compliance artefact — it was the only machine-accessible authority when both live
routes failed.


### 2026-07-18 — Qualifying episodes (two)

**Episode 1 — the directory that wasn't there.** Surprising fact: Shawn asked for
"the OSF preregistration materials in inscriptions/" — no such directory in this
repo. Competing hypotheses: (a) misremembered, never existed (create fresh); (b)
uncommitted laptop work lost in the machine swap (plausible — the swap was three
days earlier); (c) a different repository entirely. Probe: repo-scoped find
(nothing), git history grep, then filesystem-wide find → `~/Code/inscriptions`, a
sibling project with a mature `wiki/prereg/` lodgement convention (plain-prose
addenda, house PDF flags, per-lodgement git tags). Revision: (c), with large
payoff — the convention transferred wholesale with one documented deviation
(fonts). The default under hypothesis (a) — invent the materials — would have
produced plausible artefacts while silently discarding a battle-tested convention.

**Episode 2 — the impossible clean build.** Surprising fact: a rebuild reported
zero missing-character warnings immediately after a build with thirteen. Competing
hypotheses: (a) the font change fixed everything; (b) the check itself was broken.
The tell: the run referenced a header file never created, so it should have failed,
not succeeded cleanly. Probe: create the header, re-run with exit status captured
separately and stderr to a file, verify content by extracting known symbol strings
from the PDF. Revision: (b) first (swallowed error, stale artefacts), then
legitimately (a) on the honest re-run. Cross-referenced as claude-obs 13: a
verification that cannot fail visibly verifies nothing.

## 2026-07-21 — The embargo guarding an expired fact

**Surprising fact.** Shawn lodged the OSF registration WITH an embargo,
contradicting the lodgement plan's explicit "no embargo (public immediately)"
recipe. His stated reason: some candidate journals require author anonymity for
double-blind review, and a public preregistration would break it.

**Probe.** A background agent checked the three candidate venues' live author
guidelines against their Wayback histories, plus OSF's own embargo mechanics
documentation. Hypothesis space at launch: (a) the embargo is necessary (a
candidate journal mandates double-blind); (b) it is unnecessary (no candidate
does); (c) it is unnecessary but was once necessary (policy drift).

**Revision.** The answer was (c), which nobody had on the board explicitly:
JAS: Reports *did* mandate double-anonymised review as of the 18 July 2024
snapshot and has since dropped it — the current guide carries single-anonymised
wording only. Shawn's caution encoded a fact that was true when he formed the
belief and false when he acted on it. The embargo was lifted the same day, the
registration went public with its DOI, and the sequence is now recorded in the
prereg README. The generalisation joins Entry 6's policy lens: institutional
facts are time-indexed, and a verification project must date-stamp not only its
claims but the *external policies its decisions are calibrated against*. The
recheck cost one agent-run; the alternative was submitting a grant application
whose central link resolved to "Page Not Found".

Cross-reference: the same session's verifier-of-the-verifier sequence (three
wrong pointers found in a sibling session's verification ledger) is recorded in
llm-observations 2026-07-20/21 and session-reflection Entry 7 — same shape,
internal rather than external: a record about sources drifted from the sources.
