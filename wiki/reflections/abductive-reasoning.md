---
priority: 4
scope: conditional
title: "Abductive Reasoning Investigation"
audience: "researchers"
conditions: "debugging with surprising results, hypothesis generation, belief revision, default-following corrections"
tags: [llm-craft, research-methodology]
created: 2026-02-09
updated: 2026-07-24
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

**Session anchor (retro-matched 2026-07-22):** `2026-02-11T10-23_178d6a22` — session `178d6a22-27bc-4413-9ab8-3028161e55a3`, confidence: transcript-confirmed.

This session involved executing a pre-planned refactoring (file moves, path updates) and
synthesising existing artefacts into documentation. No debugging with surprising results,
no hypothesis generation, no belief revision, and no default-following corrections occurred.
Skipped.

### 2026-02-12 — Assessment: No qualifying episodes

**Session anchor (retro-matched 2026-07-22):** `2026-02-11T22-30_05d95504` — session `05d95504-543f-4088-af61-8ce05f3a6e4c`, confidence: transcript-confirmed.

Schema standardisation and version string cleanup. Work was procedural: read files,
identify inconsistencies against a known canonical form, apply fixes, verify. The
classifier_version discovery (v0.2-alpha persisting in classification.json files
adjacent to already-fixed assessment.json files) was a minor surprise but not
abductive — it was straightforward deduction from "if we fixed version X in file
type A, the same version likely persists in adjacent file type B." No belief
revision or hypothesis generation occurred. Skipped.

### 2026-07-06 — One qualifying episode: the dormancy revision

**Session anchor (retro-matched 2026-07-22):** `2026-07-03T08-26_revive-llm-reproducibility-with` — session `285a2a41-b2ca-4b6a-b9c5-8fabfe57a2f8`, confidence: transcript-confirmed.

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

**Session anchor (retro-matched 2026-07-22):** `2026-07-06T04-47_7611d1aa` — session `7611d1aa-3419-49ba-a23e-b887887a92ea`, confidence: transcript-confirmed. (Archive completed 2026-07-22: the earlier snapshot ended 2026-07-07T23:21Z mid-session; the full transcript to 2026-07-13T23:41Z was re-archived from zbook.)

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

**Session anchor (retro-matched 2026-07-22):** `2026-07-13T23-54_draft-phase-2-osf-preregistration-with` — session `6590f824-0c1c-4409-9964-cd46192bd67b`, confidence: transcript-confirmed.

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

**Session anchor (retro-matched 2026-07-22):** `2026-07-15T04-21_resolve-phase-2-preregistration-decisions` — session `5c5ebf15-5088-4e1f-8036-b2a2118b4666`, confidence: transcript-confirmed.

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

**Session anchor (retro-matched 2026-07-22):** un-archived transcript `~/.claude/projects/-home-shawn-Code-llm-reproducibility/8b126d42-00d9-4060-bc79-e2b56efc9459.jsonl` — session `8b126d42-00d9-4060-bc79-e2b56efc9459`, confidence: transcript-confirmed.

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

## 2026-07-24 — The hooks the documentation said would not fire

**Session:** 315db0da-e4ee-498b-8951-731bc63f0fc7
**Instance:** primary

### Surprising fact

The pre-build juncture review (fresh context, docs-grounded) rated hook firing
for workflow-spawned agents "more likely to fail than pass", citing three
independent documentation statements — `SubagentStart` scoped to Agent-tool
spawns; workflow `agent()` spawns explicitly distinguished from Agent-tool
spawns; frontmatter hooks documented for Agent-tool and `--agent` paths only.
The empirical spike then passed on every count, first try.

### Probe

A canary hook (logs every firing; injects a token-demand into `additionalContext`)
plus three spawns: an Agent-tool control, a default workflow `agent()` spawn, and
a named-`agentType` workflow spawn. Four measurements per spawn: Start fired /
canary echoed / Stop fired / transcript path delivered.

### Belief revision

From "the documentation bounds what the harness does" to "the documentation
lags the harness; workflow spawns are full participants in the hook system" —
including the unexpected refinement that a named `agentType` reports its own
name to matchers (the generic `workflow-subagent` label appears only for
unnamed spawns), which preserves per-agent hook scoping. The review's finding
was correct *as a risk assessment given its evidence*; the evidence class was
the problem.

### What would change this belief

A harness update altering hook scope or `agent_type` reporting. The exposure is
pinned: the probe is cheap and re-runnable, and any model/harness change already
triggers the §8 regression gate, where the spike belongs as a standing item.

### Implications for practice

Architecture commitments that rest on documented-behaviour claims get an
empirical spike *before* the design text uses a committed verb. The twenty-second
probe was available three days before it ran; the interim cost was a wrongly
committed §9 and a review finding against it.

## 2026-07-24 — Three wrong stories about one 403

**Session:** 315db0da-e4ee-498b-8951-731bc63f0fc7
**Instance:** primary

### Surprising fact

The open-access control returned 403. Under the reigning story (valid key,
missing institutional entitlement), CC BY content should have returned 200 from
any network.

### Probe

A discriminating chain, each step cheap: error-body inspection
(`AUTHENTICATION_ERROR: requestor configuration settings insufficient`); the
OA control; the META view (also 403 — zero ScienceDirect API access); key
re-registration with the TDM provisions accepted (still 403).

### Belief revision

Serial: entitlement gap → key-provisioning gap → provisioning necessary but not
sufficient → (Brian's field prior) the Elsevier key path is unreliable in
practice; route switched to Zotero-plus-proxy, support email drafted but
deprioritised. End state genuinely unresolved — no confirmed root cause, three
eliminated hypotheses, all three of my causal stories having erred in the same
direction (optimism about documented self-service paths).

### What this is not

Not a confabulation episode: each story was stated as probable, probed, and
discarded on evidence — elimination working as designed. The finding is about
prior calibration, not fabrication: vendor-internal behaviour recalled from
training belongs in the same low-trust class as stale external facts (cf. the
2026-07-21 expired-embargo entry), and a practitioner's lived prior outweighed
three rounds of my documented-behaviour reasoning.

## 2026-07-24 — The dated snapshot IDs that don't exist

**Session:** 87be8687-d934-4a3e-a240-a44a21b28554
**Instance:** primary

### Surprising fact

The routing design (v0.2.2, reviewed twice, signed off) mandates pinning "full
model IDs" in agent frontmatter, explicitly contrasting them with the
"floating aliases" that per-call overrides accept — language implying dated
snapshot identifiers exist for the census models. The authoritative model
reference, loaded before authoring the pins, states the opposite: for Sonnet 5
and Opus 4.8 the alias is the complete ID, no dated form exists, and appending
a date suffix is an error that 404s.

### Probe

Reading the claude-api reference before writing any pin (the skill's own
discipline forced this — "never answer model-ID questions from memory"), then
cross-checking the models catalogue's Full ID column: "—" for every
current-generation model; only legacy models (Opus 4.5, Haiku 4.5) carry dated
full IDs.

### Belief revision

The pin/alias dichotomy the design leans on is a property of an older model
generation, silently dissolved for current models. Pinning an alias is not a
weaker choice than pinning a snapshot — it is the only choice, and the
byte-string can no longer do drift-detection work: if Anthropic re-points an
alias, the frontmatter is unchanged. The design survives because its receipt
layer already hard-gates the *runtime* `model_id` against the manifest pin —
drift detection was always going to be runtime work; the snapshot-ID language
just obscured that.

### What would change this belief

Anthropic publishing dated snapshot IDs for Sonnet 5/Opus 4.8 (as it did for
earlier generations), or the Models API's `id` field diverging from the alias
at retrieval time — either would restore a meaningful byte-level pin and
justify tightening the manifest to it.

### Implications for practice

Design documents inherit vocabulary from the API generation they were drafted
against; when a design mandates an artefact ("full ID", "snapshot", "beta
header"), verify the artefact still exists before building the mandate.
Direction note for the corpus: unlike the 2026-07-24 Elsevier entry (three
stories erring optimistic about vendor self-service), this prior erred toward
assuming *more* vendor machinery than exists — miscalibration about external
systems runs both ways.

## 2026-07-27 — The sync check that could not fail

**Session:** 44849478-4899-4ba6-ba71-3d85740448e3
**Instance:** primary

### Surprising fact

Roughly fourteen minutes into the session I ran `git fetch -q origin` before
committing, and the working tree went from `0 behind, 0 ahead` to `7 behind` —
seven commits containing the entire Phase 1 build queue I had just spent the
session reimplementing. The surprise was not that another machine had pushed;
this is a two-machine project and the resume prompt named zbook explicitly. The
surprise was that I had *already run the sync check*, early and deliberately,
precisely to avoid this. Its output was `0 0`. Nothing about that output
distinguished it from the same check run against current data.

### Probe

Two questions, in order: is this a race (did zbook push in the last fourteen
minutes?), or was the earlier check wrong? `git reflog show origin/main
--date=iso` settles it without inference: the local `origin/main` pointer moved
2026-07-24 14:16:36 (a push from this machine), then did not move again until
`2026-07-27 11:25:14: fetch -q origin: fast-forward`. That fetch was mine.
Cross-checking the commits themselves — `git log --format='%h %cd'` on the two
endpoints — put the zbook work at 24 July 14:29 to 20:01, thirteen minutes after
this machine's last push and nearly three days before my check.

So: not a race. The earlier check compared `HEAD` against a ref that had been
stale for three days. The failure was not in the timing, and it was not that I
skipped a step.

### Belief revision

I had been treating `git rev-list --count --left-right origin/main...HEAD` as *a
sync check*. It is not. It is a comparison against a **local cache** of the
remote's state — `refs/remotes/origin/main` is a file on disk, updated only by
`fetch`, `pull`, or `push`. The command performs no network operation. The same
is true of `git status`'s "ahead/behind" line, and of the harness's session-start
git snapshot.

The general form: **a read of a cached remote ref cannot distinguish "the remote
agrees with me" from "I have not asked the remote recently"** — and it reports
the first in both cases. Any check whose failure mode is silently returning the
reassuring answer needs a freshness precondition, not just correct logic. Before
this I would have said the risk of a stale check was that it might be *slightly*
out of date; the actual risk is that it is unfalsifiable from its own output.

The revision compounded a prior belief. On 2026-07-24 I recorded the project's
concurrent-session discipline as "re-verify 0 behind before committing", copied
from `CLAUDE.md`. That wording is defective in the same way the check is: it
specifies the comparison and omits the fetch. I had followed the instruction
exactly and still been wrong, which is the signature of a rule that under-
specifies rather than an operator who deviated.

### What would change this belief

If `git rev-list origin/main...HEAD` were shown to contact the remote under some
configuration (a background `fetch.auto` setting, a filesystem-shared remote, a
`remote.origin.fetch` refspec side-effect), the "cannot distinguish" claim would
need narrowing to the default configuration. I have not tested those cases; the
reflog evidence establishes only that no fetch occurred here over three days,
which is sufficient for the practical rule but not for the strong general claim.

### Implications for practice

Fetch-first became an instruction in two places the same day: this repository's
`CLAUDE.md` session-continuity line, and step 6 of
`~/personal-assistant/global-claude-md/handoff-protocol.md`, so the generated
resume prompt itself opens with `git fetch && git status -sb`. Shawn's framing
was the better one — put the guard in the generator rather than in anyone's
memory. Worth noting the fix is *cheap*: a fetch costs under a second, and the
failure it prevents cost a day of duplicated build.

### What this is not

Not an argument that the duplicate work was worthless — comparing the two
implementations found two real gaps and one live governance defect. But that is
a consolation, not a justification: the same comparison was available
deliberately and cheaply at any point, and treating the accident as vindication
would be the wrong lesson.
