---
priority: 4
scope: conditional
title: "Abductive Reasoning Investigation"
audience: "researchers"
conditions: "debugging with surprising results, hypothesis generation, belief revision, default-following corrections"
tags: [llm-craft, research-methodology]
created: 2026-02-09
updated: 2026-10-04
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

## 2026-08-02 — The mismatch that was two measurements

**Session:** f4a97952-5a82-4631-907e-805722b20b0e
**Instance:** primary

### Surprising fact

A sweep of every registered `file`+`version` pair in `manifest.yaml` reported one
genuine conflict: `assessment_json` registered at `1.1`, while the file it points
at opens `**Version:** 2.1`. The provenance was worse than the conflict — the
manifest cited commit `c3654f6` as the authority for the `1.1` figure, and
`git cat-file -t c3654f6` returned *not a valid object name*. A version claim
whose only anchor does not exist looked like drift with the audit trail already
gone. I reported it to Shawn as a defect needing his adjudication, on the grounds
that which number was correct could not be settled from the record.

### Probe

`git log -S'**Version:** 2.1'` and `-S'**Version:** 1.1'` against the file, then
reading both candidate version strings at each of its four commits.

The result inverted the framing. The document heading went `2.0` → `2.1` at
`05e9706` (2025-11-29) and was *never* `1.x`. A second, different version string
— `"schema_version": "1.1"` — appeared inside the same file at `aa75817`
(2026-02-12), describing the payload stamped into each `assessment.json`. Two
version axes in one document: the version *of the guide*, and the version *of the
thing the guide specifies*. The manifest entry tracks the second; its `file:`
field points at the document carrying the first. Both numbers correct. No drift.

The dead hash resolved separately and cleanly: `faef450` carries the manifest
description's wording verbatim ("cascade schema v1.1 to assessment prompt
templates"). Testing its two logged siblings showed all three stale, all three
message-matchable to commits of the same date — a history rewrite had orphaned
the identifiers while leaving contents untouched.

### Belief revision

I had believed I was measuring drift. I was measuring the difference between two
quantities that were never supposed to be equal, and reporting it as a defect
because my instrument had no representation of *what each number meant*. The
registry records version numbers; it does not record their referents. Absent a
referent, "manifest says X, file says Y, therefore drift" is not a check — it is
a coincidence detector that fires whenever a file happens to carry more than one
version string.

This sharpens the widening decision taken the same day. "Check every registered
entity hard" reads as a coverage problem — 7 of 25 entries checked, widen to 25.
But coverage was not the binding constraint here; **semantics** was. A naive
widening would have promoted this false positive to a permanent build failure,
and the likely response to a gate that fails on a correct file is to add an
exception, which is how checks decay into noise. The registry therefore has to
name the axis (`version_source: json-field`, `$.schema_version`) before the
checker can be widened over it — which is why entity class E5 exists in the plan
and why Phase 1 (registry reorganisation) precedes Phase 2 (widen the checker)
rather than following it.

### What would change this belief

If Phase 0's enumeration finds that `assessment_json` is the only entry with two
axes, the semantic problem is a single special case and plain coverage widening
would have been nearly right — the ordering of Phases 1 and 2 would be defensible
but not load-bearing. If several entries conflate axes, the ordering is
essential. I have not enumerated; the claim currently rests on one instance.

### What this is not

Not evidence that the dead commit hash was harmless. It was a real defect, and
the reason the episode was legible at all: had `c3654f6` resolved, I would have
read its diff, seen the cascade, and probably concluded the file's own heading
was simply stale — reaching the wrong answer with more confidence. The broken
anchor forced the reconstruction that found the two axes.

## 2026-08-02 — A green gate is not evidence about the change that turned it green

**Session:** f4a97952-5a82-4631-907e-805722b20b0e
**Instance:** primary

### Surprising fact

After bumping the reproduction preparation prompt to v1.1 in both the file and
the manifest, the D5 consistency gate returned `PASS (0 errors, 0 warnings)`.
Expected. Then, testing whether the gate had actually *seen* the change, I set
the manifest version to a deliberately wrong `9.9` and re-ran. Still `PASS`.

### Probe

Read the checker rather than inferring from behaviour:
`scripts/check-manifest-consistency.py:467-468` is
`for name, entry in shared.items(): check_canonical_entry(...)`. The
version-line comparison iterates `shared_content` — the seven registered
instruments — and nothing else. Enumerating the manifest gave the ratio: 7 of 25
registered `file`+`version` entries within scope. The extraction prompts, the
assessment prompts, the reproduction prompts, the schemas, and the workflow had
never been checked.

### Belief revision

My belief that the gate verified version lines came from this repository's own
`continuity.md`, which describes D5 as "verifies version lines" without
qualification — a description I had also repeated to Shawn earlier in the same
session. The description was not false so much as unscoped, and an unscoped
description of a check is indistinguishable from a complete one when the check
is passing.

This is the same structure as the stale-ref episode of 2026-07-27, one level up.
There, a command reported "in sync" whether or not it had asked the remote. Here,
a gate reports PASS whether or not it examined the artefact in question. In both
cases the failure mode is *silently returning the reassuring answer*, and in both
cases the output carries no signal distinguishing "checked and fine" from "not
checked". The generalisation I now hold: **any verification whose scope is
narrower than its verdict's apparent scope will be read as the wider claim**, and
the fix is not more careful reading but making the instrument state its own
coverage — which is why the monitoring plan's §6 requires the gate to print
`25/25 entities checked` beside `PASS`.

### Implications for practice

Break it on purpose. After wiring any change into a checked system, inject a
defect and confirm the check notices before trusting the green. Twenty seconds
here; the gap it exposed had been live since the gate was built on 2026-07-24 and
would have persisted indefinitely, because a passing check generates no occasion
to inspect it.

## 2026-08-03 — The operative control was not the one on the org chart

**Session:** 0360402e-e4b8-4e21-9de6-1eb48c14b416
**Instance:** primary

### Surprising fact

Arm 1 of the validation benchmark completed 15/15 with receipts that
verified perfectly — yet `receipt-gate-log.jsonl` showed the SubagentStop
receipt gate had emitted fifteen `block` decisions and zero `pass` events
for those spawns. The mechanism the design documents named as the runtime
receipt control had never validated a production receipt; the run was
clean anyway.

### Probe

Tallied the gate log by arm and event type; read the gate source against
the workflow's output path. The gate searched the agent's *final message*
for JSON, but workflow-lane structured output rides a tool call the gate
never inspects — so every spawn was blocked once, re-prompted after its
output was already banked, and the data flowed through untouched. The
operative control was my orchestrator-side post-hoc verification, which
the run records had (accurately) described all along. Fixed the gate to
read transcript tool calls; the fix commit's own re-audit then showed the
fable arm still blocking 9 of 15 — the fallback keyed on an event field
name sourced from a design document, never confirmed against a live event.

### Belief revision

Before: the layered receipt apparatus (push hook, receipt gate, pre-flight)
was operative because it was wired, tested at build, and its log existed.
After: a control is operative only when its log shows it *passing real
traffic* — wiring plus green tests plus a log of blocks is fully consistent
with a control that has never once done its job. And a fix to such a
control inherits the same burden: my repair was ~40% effective for the same
root reason (an unverified interface assumption) that made the original 0%
effective. The reliable pattern in this repo remains: the orchestrator-side
verification that reads persisted artefacts is the control that has caught
things (marwick r2's arithmetic, the model-id marker); hook-lane controls
are aspirational until their pass-events exist.

### What would change this belief

A census run whose gate log shows per-item pass events with agent ids,
where a deliberately injected bad receipt (wrong model_id) is blocked at
SubagentStop and the block demonstrably re-prompts to a corrected output —
the end-to-end catch, observed once, would promote the gate from
aspirational to operative.

### Implications for practice

Before trusting any event-driven control, capture one real event and diff
its keys against the code's assumptions (Observation 14, applied to hooks);
and after "fixing" a control, demand its first live pass-event before
declaring it repaired — the follow-ups register now requires exactly this
before the census.

## 2026-08-10 — The routing fix's premise died on a receipts count

**Session:** 52a81f4b-eb60-481f-a02e-a80edde49fb9
**Instance:** primary

### Surprising fact

The handoff carried a ready-to-play remediation candidate — amendment 1
§2's single permitted routing-fix attempt, premised on "receipts show
inconsistent pulling of fair-principles-guide.md". Re-checked against all
45 spawn receipts at session start, the premise held for one arm only:
sonnet pulled the guide in 9/15 spawns, but opus and fable pulled it in
15/15 each — and both full-pulling arms failed both 0.90 gates on the
same item cluster.

### Probe

Three steps, cheapest first. (1) Count guide pulls per arm across the
persisted receipts (minutes; the premise-breaker). (2) Read the guide
against the disputed cases — it is silent on A1.2's
fully-open-no-authentication case, R1.1's licence target, and F-block
upstream crediting, so pushing it could not make the missing answers
uniform. (3) Test the within-sonnet correlation properly: of 29 two-one
splits, 17 minority votes came from guideless spawns against ~11.3
expected by chance — a real delivery effect, but secondary, and on the
wrong gate (sonnet's binding constraint was concordance at 0.773).

### Belief revision

Delivery was not the binding constraint; instrument ambiguity was. The
registered one-shot card would have been spent to nudge one arm's
stability while concordance stayed structurally out of reach for all
three. Recommended declining the card; the registrant agreed and chose
the instrument-clarification route (erratum → amendment 2 → re-benchmark).

### What would change this belief

If the re-benchmark on the clarified instrument — with the guide pushed
uniformly and the evidence pack supplied — still shows the
A1.2/R1.1/F-block cluster unstable, then ambiguity was not the operative
cause and the delivery hypothesis regains standing. The post-fix run is
the falsification test, and both pre- and post-fix results are reported
per the registered rule.

### Implications for practice

Before spending a registered one-shot resource, test its premise against
primary artefacts. The check cost a quarter of an hour and reversed the
session's opening plan; the alternative was burning the only permitted
remediation attempt on a hypothesis two-thirds of the evidence already
contradicted.

## 2026-08-15 — The gate blocked 39 spawns, stopped none, and everything it blocked was valid

**Session:** 04169f15-06f9-421d-a149-39a04367b3b5
**Instance:** primary

### Surprising fact

The audit register carried the finding as "gate blocked 9/15 fable spawns
and cannot say why." The clean-context pre-run audit re-derived the true
scale from the gate log: 39 of 45 benchmark spawns "blocked" (opus 15/15,
sonnet 15/15, fable 9/15) — and every one of the 45 outputs was collected
and published anyway. Two shocks in one: the blocking was near-universal,
and it was inert.

### Probe

Three operator-approved probes plus a retrospective sweep. Probe A
(Agent lane): full pass, field names captured. Probe B (workflow lane,
schema-forced): transcript-borne pass — so the search path works when the
transcript is readable. Probe C (engineered receipt omission): the gate
correctly blocked, the block message appeared nowhere in the agent's
transcript, no retry occurred, and the workflow collected the receipt-less
output — consequence absence demonstrated under controlled conditions.
Then the retrospective: today's search function finds a well-formed
receipt payload in all 45 retained benchmark transcripts, and full
validation (versions, tokens, model pins, agent versions, declared pulls
against transcript Read calls) passes 45/45. With payloads provably
present, the only surviving explanation for the runtime failures is
transcript write-lag beyond the gate's 3-second retry budget — and the
block message had conflated "transcript unavailable" with "searched and
found nothing", which is why the register mis-described the fault for
eleven days.

### Belief revision

Three revisions, one per layer. The 39 blocks were false alarms, not
detections — the gate's failure mode was crying wolf, not sleeping.
SubagentStop block decisions are advisory in the workflow lane — the
harness collects structured output regardless, so any real consequence
must live orchestrator-side, after completion. And the benchmark's
provenance was sound all along: the run the blocks appeared to indict is
now machine-verified cleaner than the hand tally claimed. The reconciling
tool built in response (receipt re-validation from completed transcripts,
exit-1 hard stop) is the authoritative control; hook-time gating is
demoted to a fast path.

### What would change this belief

A future reconciled run finding an invalid payload the hook passed (the
lag story explains blocks, not passes — a false pass would reopen the
question), or lag-shaped blocks persisting under the raised 8-second
budget now that `transcript_state` is logged per decision — the new field
makes the write-lag hypothesis directly testable at D3.

### Implications for practice

Authoritative verification belongs after completion, on durable
artefacts; in-flight hooks are advisory speed, not integrity. And distinct
fault classes need distinct messages — one block message covering two
branches hid a systemic timing fault behind an apparent payload fault for
eleven days.

## 2026-08-15 — The licence floor was a form default

**Session:** 04169f15-06f9-421d-a149-39a04367b3b5
**Instance:** primary

### Surprising fact

Of 298 newest Zenodo records sampled by the platform-floor verification
agent, 82.6% carry `cc-by-4.0` — the value Zenodo pre-fills. And the
"licence field on every record" entitlement is falsified outright for
restricted deposits (27/100 sampled carry the field at all): the policy
scopes the requirement to publicly available files.

### Probe

The agent quoted the platform's own deposit documentation ("Zenodo
defaults to the Creative Commons Attribution 4.0 International (CC-BY)
license"; "Users must specify a license for all publicly available
files") and sampled the live REST API across access classes. DANS shares
the artefact: its deposit manual pre-fills CC0. CRAN, by contrast, has a
mandatory licence field with a controlled vocabulary and *no default* —
the one row where a licence value is genuine evidence of an author act.

### Belief revision

Platform by-construction entitlements are *presence* floors, not *choice*
floors. A licence value on a Zenodo record is weak evidence of an author
decision; the ratified rule that "a platform's mandatory licence field
does not itself satisfy R1.1 — the licence must be identified" is thereby
upgraded from prudent caution to load-bearing instrument design. The
floors themselves were empirical claims, and measuring them moved every
row of the table to HOLDS WITH CAVEAT.

### What would change this belief

A properly random corpus-wide sample showing the default-value rate far
below the recency-sampled 82.6% would soften the artefact's magnitude —
though not the structural point, which rests on the platform's own
documentation of the pre-fill.

### Implications for practice

Never let an instrument credit field presence where the platform supplies
the value; and re-verify "by construction" claims against the
construction, dated — the table's corrections are now amendment-2 draft
material for the registrant's D1 ruling.

## 2026-08-17 — Fifteen failures, zero failures: the verifier had not noticed the harness changed under it

**Session:** 6e8352ed-2013-4674-8720-85245d97fbc7
**Instance:** primary

### Surprising fact

The first re-benchmark arm (sonnet) hard-stopped with **15/15 per-item
reconciliation verdicts failing** — yet every spawn's receipts were valid,
every gate event on 14 of them was `pass`, and the scores looked sane.
Fourteen verdicts cited the same contamination: a Read of a
`tool-results/hook-*-additionalContext.txt` file. The fifteenth cited
v1.0-vintage properties (instrument 2.0, agent v1.0, no evidence pack)
that nothing in the current run should possess.

### Probe

Opened the flagged file for one spawn: 76,828 bytes beginning with the
push hook's own banner and carrying the exact receipt tokens the spawn
had echoed — the "contaminating" file *was the instrument delivery*. The
v2.1-plus-guide push (~77KB) had crossed the harness's inline
additionalContext threshold for the first time, so the harness spilled it
to a per-spawn file the agent must Read to receive its instruments.
Then searched for the fifteenth verdict's agent id: it did not exist in
the live run directory at all — it resolved to the **2026-08-03 run's
directory**, where the per-item verifier had fallen back (identical
prompt wording, transcript-write lag in the live dir) and confidently
audited an eleven-day-old spawn as if it were today's.

### Belief revision

I had modelled the verification stack as observing the run from outside.
It is not outside: the reconciler's contamination rule encoded an
assumption about *how instruments arrive* (inline, invisibly), and when
the harness silently changed delivery shape under a heavier payload, the
checker converted every correct behaviour into a violation. Revised
belief: **a verifier must model the delivery mechanism it rides on, and
any harness behaviour that varies with payload size is part of the
instrument's environment, not background.** Corollary from the
fifteenth verdict: a checker that guesses under uncertainty (falling back
to an older directory rather than declaring unverifiable) manufactures
false findings *with a checker's authority* — the failure register now
separates verifier-error from model-failure for exactly this reason.

### What would change this belief

Finding that the spill threshold is documented and stable (making this a
foreseeable-and-missed case rather than a silent environment change), or
a future cycle where the authoritative pass disagrees with adjudicated
ground truth in the other direction — a verifier *missing* a real
violation — which would shift the lesson from "checkers encode
environment assumptions" to "this checker was simply miscalibrated".

### Implications for practice

The per-item catch-rate table now reads: three verification layers, and
in one afternoon each failed differently — the live gate false-alarmed
(2026-08-03, transcript lag), the per-item agent audited the wrong run,
and the authoritative reconciler misclassified the push channel. Every
one was caught by an adjacent layer or the operator. Defence-in-depth is
not redundancy against model failure alone; it is how checker failures
get caught.

## 2026-08-17 (second session) — Twenty-eight transcripts for fifteen items

**Session:** f605c78a-e90b-4d9d-bbec-1fd3903ced31
**Instance:** primary

### Surprising fact

The sonnet@max arm's authoritative reconciliation reported "expected 15
governed spawns, found 28" — thirteen extra fair-assessor transcripts,
none with a payload, none with a gate event. The workflow had returned
15 results with `missing: 0`, and the per-item reconcile stage had run
for every item. Nothing in the design anticipated surplus transcripts.

### Probe

Mapped every transcript to its (paper, run) identity via the assembler's
prompt regex, with payload presence, timestamps, and per-transcript
token counts. Pattern: items with multiple transcripts had earlier
attempts dying at ~64–75K accumulated output and later attempts
starting at ~16-minute intervals; the workflow's failures line named a
64K output-token API error; the journal held no result entry for either
of dye r2's transcripts, yet dye r2's reconcile stage had run —
exposing a second, independent defect (the stage-2 null guard tested
the wrapper object, not the inner result). Causal confirmation came by
intervention: raising `CLAUDE_CODE_MAX_OUTPUT_TOKENS` to 128K produced
zero dead attempts across five subsequent re-run spawns.

### Belief revision

From "max effort degrades sonnet's harness compliance" (a model-
behaviour claim) to "max-effort verbosity collides with an undocumented
harness constant, and the harness's silent retry loop converts that
collision into invisible spend" (an infrastructure × behaviour
interaction). The model-behaviour residue is real but smaller than it
first appeared: the boundary Globs and the missing-scores payload
remain model-attributable; the 24%-of-spend churn does not.

### What would change this belief

If a 128K-capped sonnet@max arm still produced dead attempts (it did
not — 0/5 re-run spawns), or if other models at max showed churn at the
raised cap, the constant would be exonerated and the verbosity itself
implicated.

### Implications for practice

Denominator assertions (--expect-spawns) are the cheapest tripwire for
"the harness did something the design didn't model" — the surplus was
caught by an inequality, not by any behavioural check. And every hard
cap in the serving path is part of the experimental apparatus; a study
that varies effort without provisioning output headroom measures the
cap, not the model.

## 2026-08-17 (second session) — The cheapest arm that wasn't

**Session:** f605c78a-e90b-4d9d-bbec-1fd3903ced31
**Instance:** primary

### Surprising fact

Opus@high — generating a third fewer output tokens than opus@xhigh
(294K vs 437K) — nonetheless recorded a *higher* contract-metric total
(5.14M vs 5.07M). I had already published "cheapest known passing
configuration" before Shawn's one-line question surfaced the
contradiction.

### Probe

Component decomposition of both run records: the contract metric is
~92% cache-creation tokens (per-spawn context writes — PDF, instrument,
pack), which are effort-independent and wobble a few percent with turn
structure. The −143K output saving was swamped by a +213K cache-write
wobble. In API-equivalent dollars the ordering inverts (output prices
at 4× the cache-write rate), and both gaps sit inside single-arm noise.

### Belief revision

From "the contract metric measures arm cost" to "the contract metric
measures spend for wire purposes and is structurally insensitive to
effort — within-model effort comparisons must read the effort-sensitive
component (output tokens) or a component-weighted dollar figure".
Corrected in the committed record (`5c193e3`) rather than silently.

### Implications for practice

Composite metrics inherit the dynamics of their dominant component;
before any ranking claim, check the ordering survives in each
economically distinct component. The claims layer has no mechanical
verifier — this error passed every gate in the stack and was caught
only by operator scepticism.

## 2026-08-19 — Ninety guideless spawns: the statistic outlived its carrier

**Session:** 92427cb5-9fa4-47f0-9571-ebaf54089c1b
**Instance:** primary

### Surprising fact

The first all-arms run of the newly extended analysis tool (v1.1,
`--arms` spanning both 2026-08-17 cycles) reported **all 90 spawns in
all six arms as guideless** — the guide never read — with every 2-1
minority vote consequently attributed to a guideless spawn (22/22,
7/7, 8/8, 28/28, 20/20, 7/7 across the arms). This included the two
opus arms at 0.953 stability. Meanwhile the same binary, in legacy
mode, reproduced the old 2026-08 cycle's expected pattern exactly
(6 guideless sonnet spawns; 17 of 29 minority votes guideless).

### Probe

Diffed receipts for the same paper/arm position across cycles. Old
cycle: the guide appears in `pulled_files_read` (spawn chose to read
it) and `instrument_receipts` lists only `fair-instrument`. New cycle:
`pulled_files_read` carries the paper PDF, the evidence pack, and a
hook-delivery artefact — no guide — while `instrument_receipts` lists
both `fair-instrument` **and** `fair-principles-guide`. Cross-checked
the governance record: A3 promoted the guide from pull-on-demand to
push delivery in instrument v2.1 (2026-08-15). Every post-promotion
spawn receives the guide; none pulls it.

### Belief revision

From "the detection predicate identifies guideless spawns" to "the
predicate identifies *pull-era* guideless spawns; guide presence has
two carriers, one per delivery era." The general revision: a derived
statistic's definition silently binds to the apparatus version that
existed when it was written. Apparatus evolution does not fail loudly —
it renders downstream statistics vacuously true or false, and the
vacuity surfaces only when a new consumer runs against post-change data
with known figures to compare. Fixed by making detection span both
carriers (commit `48568fb`); after the fix, the old cycle's correlation
is byte-identical and post-A3 arms correctly report guideless = ∅.

### What would change this belief

A post-A3 spawn whose `instrument_receipts` lacks the guide entry —
that would mean push delivery is not universal and the era boundary is
soft, requiring per-spawn rather than per-era semantics. None exists
in 90/90 spawns. Also: a third delivery mechanism appearing in a future
instrument version would reopen the question in the same form.

### Implications for practice

When a governed instrument changes delivery mode, grep for every
consumer of its receipts at change time — the reconciler was updated
for A3, the analysis tool was not, and nothing connected the two. And
the catching mechanism generalises: new tooling must first reproduce
known ground truth (here, the run-record cross-check lines) before its
novel outputs are read; the absurd 100% figure was only visibly absurd
because correct known figures sat directly above it in the same output.

## 2026-10-03 — The precedent that was never in the paper

**Session:** 003fda8b-6037-409d-94d1-c7ed1b2a5202
**Instance:** primary (Opus 5.5; the registry curation that seeded the
error predates this session)

### Surprising fact

Preparing marwick-2025 `data_fair`, the evidence pack's "dead cited DOI" —
10.5281/zenodo.14561925, 404 at DataCite and Zenodo, and the precedent case
named in lodged amendment 2 §2 — appeared nowhere in the paper: zero hits in
the version of record, the preprint, and the corpus extracted text. The
deposit "recovered" for it, 10.5281/zenodo.15603267, turned out to be v1.3
of the concept DOI (10.5281/zenodo.14897252) that the paper does cite.

### Probe

Counted each identifier across all three text sources; traced the dead DOI
through the repository to its only origin, the pilot extraction's
`data_completeness.assessment_scope_rationale`; listed the concept's
versions through the Zenodo API; and read the declared-links registry's
header, which says it was curated from the extraction records.

### Belief revision

The registry was never an independent reading of the papers: "the paper
cites X" in the apparatus can be second-hand, inherited from a
model-produced record. The identifier-recovery rule worked as specified;
its premise was wrong. Corrected as erratum-log Entry 4, with a standing
direction for a mechanical identifier check — presence in the paper's text,
not mere resolution (a later scan found two more such identifiers in
herskind's record, both resolving to unrelated records).

### What would change this belief

Finding the identifier in a version of the paper the corpus does not hold
(an earlier online version, say). Only the version of record, the preprint,
and the extracted text were checked.

## 2026-10-03 — The version the dates chose never produced the paper

**Session:** 003fda8b-6037-409d-94d1-c7ed1b2a5202
**Instance:** primary

### Surprising fact

Under the version rule as then written, crema-et-al-2024's cited concept
DOI resolved to v2.0.0 (2024-03-14), and the date fallback — the latest
version before the article first appeared (2024-03-16) — also picked
v2.0.0. But the paper's Table 1 matched v1.0.0's `table1.csv` on all 24
values (8 medians, 8 intervals, 8 Rhat values), and 18 of v2.0.0's 24
differ.

### Probe

Read the article history (accepted 29 February 2024, so both versions
post-date acceptance and dates cannot decide); diffed v1.0.0 → v2.0.0 at
GitHub (11 commits re-running the analyses and regenerating every figure
and `table1.csv`); compared each tag's `table1.csv` with the PDF's Table 1.
The Obs 33 writer agent re-derived the comparison independently and found
each Zenodo archive's `table1.csv` byte-identical to its tag's copy.

### Belief revision

Dates are a weak proxy for the version of record; a published-values match
is decisive wherever outputs are tabular. Shawn's prior — a deposit eleven
days before publication is a plausible target, given publication lags —
was right where the rule was wrong. AP-12 was refined (score and reproduce
the cited version; always run the checks; a failing citation is a
correction finding), and the general point became Observation 33:
resolution is not verification.

### Implications for practice

Before trusting any version selection, look for something in the paper
that only one version can reproduce.

## 2026-10-03 (second session) — Most of the cache writes were echoes

**Session:** 4d22016c-9af3-43a8-9ab6-f14c9391eacd
**Instance:** primary (Opus 5.5)

### Surprising fact

Building the reproduction lane's cost audit, I summed `message.usage` over
one effort-study run's transcripts (`wf_d691e836-2f2`). Cache-creation
came to 4.84M tokens. Keeping one usage record per `requestId` gave
1.86M, while output tokens barely moved. A 2.6× gap in the input-side
fields alone did not fit any billing model I knew.

### Probe

1. Checked whether the repeated entries were one API call or several. All
   209 requests in that run carry a single message id, with identical
   input and cache usage across their entries. There are 499 entries,
   one per content block: thinking, text, tool_use.
2. Recomputed all six recorded `contract_metric_tokens` values from their
   own spawn lists. Each was reproduced **exactly** by the per-entry sum,
   and each was 1.90–2.63× the per-request value.
3. Checked the variation. The ratio tracks blocks per response: Sonnet
   about 1.9–2.1, Opus about 2.4, Fable about 2.6.

### Belief revision

The registered spend metric counted each request once per content block,
not once per request. So it overstates spend, and it does so in a
model-dependent way, which biases any cross-model cost comparison against
the more verbose-thinking models. The effort study's "cost-indistinguishable"
reading and the upward correction to the study cost estimate both used
this metric. Both need re-derivation (register F-013, awaiting ruling).

### What would change this belief

A provider usage report for the same runs showing totals near the
per-entry sums. That would mean repeated entries are separately billed,
which contradicts the one-message-id evidence. It is not available on the
Max plan, so the dedup rests on transcript structure alone.

### Implications for practice

Before trusting a token metric, find the unit the provider bills
(request/message) and dedupe to it. Shape-checking a figure ("this run
cost 5M tokens") cannot catch a constant-factor inflation applied
everywhere.

## 2026-10-03 (second session) — The baseline was the thing that failed

**Session:** 4d22016c-9af3-43a8-9ab6-f14c9391eacd
**Instance:** primary (Opus 5.5)

### Surprising fact

The agentic executor escalated dye T06 as a PAPER_ERROR: the paper's 0.87
for BE1-Cowrie→BE1-Disc does not reproduce (0.99967). The pilot's
attempt-01 table lists the same published 0.87 as an EXACT match. The
regression test's premise was that a disagreement means the new harness
is wrong.

### Probe

1. Compared values first. The regression script found all 54 Supplement
   Table 2–10 cells and the 12-cell section-7 matrix identical between the
   attempts, so the two runs computed the same numbers.
2. Read the paper itself (accepted manuscript, p.16, ll.374–376): "bead
   type BE1-Disc most likely descended from bead type BE1-Cowrie … with a
   probability of 0.87".
3. Compared that with the matrix. 0.87 is the Amethyst→Disc cell (0.867);
   Cowrie→Disc is 1.00.
4. Found where 0.87 sat in the pilot's table: listed as "Published 0.87"
   against Amethyst→Disc, which the text does not say.

### Belief revision

The pilot's comparison had silently re-mapped the published value to the
cell where it fits. The disagreement exposed a baseline error, not a
harness error. The same pattern recurred at herskind, where the pilot had
never compared Table 1 with the paper (8 of 130 cells disagree with the
authors' own S3). A regression test against a human-directed baseline
also audits the baseline. The pre-committed criterion's labels (PASS,
FAIL, explained drift, inconclusive) have no category for "the baseline
was wrong".

### What would change this belief

The version of record printing Amethyst, not Cowrie, at p.16, which
would mean a correction in proof that our accepted-manuscript copy lacks.
The pilot would then have been right, from a source we did not hold.

### Implications for practice

When a regression disagrees, check the baseline against the primary
source before attributing the difference to the new system. And design
regression criteria with an explicit branch for "baseline incorrect,
confirmed at source".

## 2026-10-04 — No public release ever ran the published code

**Session:** c51bef29-c20e-400f-94db-056e31bb50f3
**Instance:** primary (Opus 5.5)

### Surprising fact

Dye's section-4 code indexes column 78 of a `read_oxcal()` object that
ArchaeoPhases 1.8 returns with 77 columns. In raw-CSV numbering, though,
the authors' indices select exactly 72 dates, one per grave, which matches
the paper's 72 interments. The adversarial reviewer explained this as an
environment effect: the authors must have used an earlier release whose
`read_oxcal()` kept the `Pass` column. I relayed that as the likely
explanation, and Shawn ruled the pilot's −1 shift "mechanical".

### Probe

1. Shawn's question (routine fix or fail-and-uplift?) made the
   explanation decisive. If a public release keeps `Pass`, pinning it is
   routine. If none does, the published code is defective.
2. Listed the CRAN archive. `read_oxcal()` exists only in 1.5
   (2020-12-01), 1.6 (2022-02-17), and 1.8 (2022-06-21); there was no 1.7.
3. Downloaded 1.5 and 1.6 and read `R/ImportCSV.R`. Both have
   `data <- data[, -1]`, the same as 1.8.
4. Cross-checked dates: `beads-1.csv` is dated 2022-10-20, when 1.8 was
   the current release.

### Belief revision

The earlier-release hypothesis is false for every public release. The
authors counted columns in the raw CSV, so the published code never ran
as printed on any release a reader could obtain. (A contributor's
development build remains possible: T. S. Dye is listed as a contributor in
the package's DESCRIPTION.) The −1 shift recovers the intended selection
exactly, but it is a repair, not an adaptation. The ruling moved to
fail-and-uplift: CANNOT_COMPARE stands, the pilot's credit was generous,
and the repair goes to the uplift tool. The bright line now reads:
choosing among public dependency versions is routine; editing code logic
is not.

### What would change this belief

A published or archived ArchaeoPhases build (GitHub tag, r-universe
snapshot) whose `read_oxcal()` keeps the iteration column, dated before the
paper's analysis. The authors' code would then be correct for that release,
and T02 would become a routine version pin.

### Implications for practice

When a recommendation rests on a checkable explanation, check it before
asking for the ruling. Here the check was local, free, and took minutes.
Offering it to the registrant as an *option* deferred work that was mine,
and let a ruling stand on an untested premise for most of a morning.

## 2026-10-04 — One failed spawn is not a loading mechanism

**Session:** c51bef29-c20e-400f-94db-056e31bb50f3
**Instance:** primary (Opus 5.5)

### Surprising fact

The P4 probe failed at its first spawn: "agent type
'fair-assessor-opus-5-5' not found". The agent definition had been
committed several turns earlier, and the error's agent list was exactly the
session's start-up list.

### Probe

None worth the name. I read the error, inferred "definitions load only at
session start", and wrote that rule into register F-018 and the design
note.

### Belief revision

Minutes later the harness announced the agent as available in the same
session. Definitions are re-read during a session, on a trigger I do not
know. I corrected F-018 visibly, striking the claim rather than deleting
it, relaunched P4 in this session, and it passed.

### Implications for practice

A single negative observation licenses "X was not available at time T",
not a mechanism. Register entries are read later as rules. Write the
observation, and leave the mechanism open until a second observation
discriminates.

## 2026-10-04 (second session) — 882 output tokens for a 14,000-character answer

**Session:** c5ee7a27-c9d0-4641-8bb3-6a5fdcc3ddce
**Instance:** primary (Opus 5.5)

### Surprising fact

Arm 1's assembled record listed a scoring spawn (key r3) with 882 output
tokens. Every spawn emits a FAIR payload of about 13,000–14,000
characters, which cannot fit in 882 tokens. Three more spawns read 481,
639, and 912. Their wall-clock times (105–145 s) matched the spawns
reporting 10,000–16,000.

### Probe

1. Read the per-entry usage in one low transcript and one normal one. In
   the low spawn, the request carrying the `StructuredOutput` call had
   `stop_reason: None` and `output_tokens: 8` on every entry. In the normal
   spawn, the same request ended with `stop_tool_use` and 14,652.
2. Counted requests with no final entry across arms, including the
   registered opus-5 transcripts from 2.1.233. They were present there
   too: 26 of 209 requests (high) and 11 of 209 (xhigh).
3. Checked the workflow journal and meta sidecars for an independent usage
   source. There is none.
4. Imputed the missing outputs (median and maximum of complete requests of
   the same kind) and re-priced every eligible arm.

### Belief revision

- **Before:** per-request counting (the F-013 fix) made the transcript a
  trustworthy cost source.
- **After:** it is trustworthy for input and cache fields, and a lower
  bound for output. The gap was not a new halt-worthy anomaly in this run.
  It was a pre-existing property of the apparatus.
- **A second revision followed.** The registered D4 record's "opus-5
  `high` is about 11% cheaper than `xhigh`" is not robust. `high` lost 8
  final requests to the gap and `xhigh` only 2. Imputed, the two efforts
  are about 2% apart, and the order reverses at the upper bound.

### What would change this belief

A usage source that records final usage per request, such as harness
telemetry, showing that the placeholder requests' true outputs are small.
That would make the imputation an overestimate.

### Implications for practice

When a number is physically implausible against the artefact it
describes, check the measuring before the measured. Then check whether
past measurements share the defect before treating it as specific to
this run. The second step turned a local anomaly into a correction of a
recorded ruling.

## 2026-10-04 (second session) — The relayed message fired in one arm out of three

**Session:** c5ee7a27-c9d0-4641-8bb3-6a5fdcc3ddce
**Instance:** primary (Opus 5.5)

### Surprising fact

Since Claude Code 2.1.288, a workflow spawn can receive the session's last
user message, relayed (register F-015). The P4 probe saw no relay. Arm 1's
30 spawns all received it: Shawn's "Go". Arms 2 and 3 (0 of 30 each)
received nothing.

### Probe

Compared the launch turns. Arm 1 launched in the same turn as Shawn's
typed "Go". Arms 2 and 3 launched from turns triggered by task
notifications. The harness's own preamble describes the relay as "the
user request that triggered this workflow run".

### Belief revision

- **Before:** the relay carries the session's last user message to every
  spawn, so every launch needs a neutral last message (ruling Q7).
- **After, provisionally:** the relay carries the user message that
  triggered the launch turn. A launch from a notification turn relays
  nothing.

Two consistent observations (arms 2 and 3), plus the preamble's wording.
P4's launch turn is not recorded, so it neither confirms nor refutes this.

### What would change this belief

A notification-turn launch whose spawns receive a relay, or a typed-turn
launch whose spawns do not.

### Implications for practice

Q7's neutral go-ahead matters only for the launch made in the typed turn.
Chained launches from notifications are clean by construction. This is
worth recording beside F-015, but not yet as a rule. Following the F-018
lesson, record the observations and leave the mechanism open until a
deliberate test discriminates.

## 2026-10-04 → 10-05 — The scorer's systematic miss was an input gap it had reported

**Session:** ef0412bd-73e2-4c97-b695-695856453f0c
**Instance:** primary (Opus 5.5)

### Surprising fact

Six F2 over-credits were unanimous in every run of every Opus arm, across
two model generations and four efforts (Observation 34). I had read the
miss as a stable judgement error, which is why a mechanical F2 rule was
the first step in the checks policy. Building the rule, I found that the
evidence packs every arm read contain no creators, descriptions, or
keywords at all. Harvester v1.1 extracted only identifier, licence, and
type fields, and kept only a checksum of each raw response.

### Probe

I searched the 90 Opus F2 evidence strings for the three Zenodo pilots
for any mention of keywords. Twenty of them say the pack did not show the
description or keyword fields, then credit F2 on the record's existence
and the platform row. A re-harvest (v1.2) confirmed that all three
deposits have empty keyword fields and either pointer descriptions or none.

### Belief revision

The miss was not judgement the model could have got right. The model
lacked the input it would have needed, and in a fifth of the strings it
said so. "Stable across models and efforts" was evidence that the cause
lay outside the model, and I had read it as evidence of a robust model
error. Two consequences:
- the F2 gate items were counted against the model when their basis was
  missing input, which makes the gate figures cautious, not generous;
- the census-input re-validation (amendment 3 §6) became necessary,
  because the gates had validated the scorer on inputs the census will not
  use.

### What would change this belief

If the re-validation on v1.2 packs, which show empty keyword fields, still
gives F2 = 1 on these deposits, the error is judgement after all: credit
despite visible negative evidence, not credit in its absence.

### Implications for practice

When an error survives a change of model and effort, check what the
models were given before modelling the error. Search the model's own
evidence strings for the word you expected it to need. It may have
already told you it did not have it.

## 2026-10-05 — `git status` in the main checkout said "not a work tree"

**Session:** ef0412bd-73e2-4c97-b695-695856453f0c
**Instance:** primary (Opus 5.5)

### Surprising fact

After a commit attempt in a linked worktree failed its pre-commit test run,
`git status` in the *main* checkout failed with "this operation must be
run in a work tree". The worktree branch also carried a new commit called
"fixture", whose tree was two files.

### Probe

I read the shared `.git/config`, read-only, before changing anything:
`core.bare = true`. The worktree's reflog showed exactly one "commit:
fixture". Both matched my new test helper, which runs `git -C <tmp> init`,
then `add .` and `commit -m fixture`. Git exports `GIT_DIR` and
`GIT_INDEX_FILE` to hook processes, and these override `-C`. So the
fixture reinitialised the real repository, writing `core.bare` to the
shared config, staged the temporary files into the real index, and
committed them. A search then found the repository's own record of the
same failure class, in `tests/test_effort_pinning.py` (2026-09-23), with
the scrubbing idiom I had not used.

### Belief revision

Before this, I treated `git -C <dir>` as confining a command to `<dir>`.
Under a hook it does not; the inherited environment wins. Unscrubbed test
fixtures are therefore not hermetic. Whether the suite is run by hand or
by the hook decides what they touch.

### What would change this belief

None needed for the mechanism; the regression test reproduces it with a
decoy `GIT_DIR`. What remains open is whether other repositories' suites
shell out to git without scrubbing.

### Implications for practice

Any code that runs git as a subprocess, in tests or in tools, scrubs `GIT_*`
from its environment, and is tested once under a decoy `GIT_DIR`. When a
command fails in a place it should not have touched, read the shared state
before repairing it, and repair the minimum.

## 2026-10-05 — A project file outranked the variable the design relied on

**Session:** b1a1e102-fc08-4962-a341-6da21988b13d
**Instance:** primary (Opus 5.5)

### Surprising fact

The gate 1.3 design loaded its logging hook by setting `R_PROFILE_USER`
with `docker run -e`, on the assumption that a variable set in the
process environment governs R's start-up. In the first probe, a fixture
project held a `.Renviron` naming a different profile. Under every
launcher tried (`Rscript`, `R -f`, a `system()` child, and a PSOCK
worker), the project's profile loaded and the lane's hook did not. Only
`Rscript --no-environ` loaded the hook.

### Probe

I made the next probe discriminating rather than repeating the first. I
pointed `R_ENVIRON_USER` at a lane file that copies the project's lines
and then sets `R_PROFILE_USER` to the hook as its final line. The hook
then loaded, the project's own variable (`PROJECT_VAR`) still applied,
and a child started after `Sys.unsetenv("R_PROFILE_USER")` loaded the
hook as well, because the child re-reads the environment file. The same
container also tested the event channel: `/proc/1/fd/2` and a read-only
FIFO both reached the host from a grandchild, while R's `system2(stderr =
TRUE)` captured a child's own stderr.

### Belief revision

Before: the process environment is the authority on start-up variables,
and a container's `-e` cannot be displaced. After: R reads its
environment files during start-up, and in this image a value there
(`R_PROFILE_USER`, the only variable tested) overrode the inherited one.
The authority is therefore whichever file R reads last, not the variable
the launcher set. So the lane must own the environment-file
phase (`R_ENVIRON_USER`), not just the variable. It also changed which
design the reviewers' points pointed to. Fable's "set `R_ENVIRON_USER`
too" had read as belt and braces. It was the load-bearing fix.

### What would change this belief

An R version in which `Renviron` values no longer override existing
variables, or an image whose front end resets them. The launcher matrix
(specification §13) re-tests the pin on each image the lane meets. A
project `.Renviron` that names its own profile is now flagged statically
(§10), so a change in behaviour would surface as a census or static
finding rather than a silent unhooked run.

### Implications for practice

Where a design's guarantee rests on a runtime precedence rule (which
setting wins), test the precedence in the target runtime before building
on it. Arrange the test so that the two candidate authorities disagree:
an environment that merely agrees with the variable proves nothing.

## 2026-10-08 — The guard against a stray revision could never fire

**Session:** fabeab56-1b7a-4539-8524-caed6e956c93
**Instance:** primary (Opus 5.5)

### Surprising fact

`lodge-osf-amendment.py` reads the registration's revision list
anonymously and refuses to continue if the newest revision is not
approved. I wrote that guard, and the header's account of failure recovery
relied on it: a failed write would leave an unsubmitted revision, and the
next `plan` would see it and stop. Astra's re-check said the guard is
inert, because OSF filters the anonymous listing to approved revisions. An
unsubmitted revision is invisible to the call that was meant to detect it.

### Probe

I fetched OSF's source from its develop branch (2026-10-08).
`RegistrationSchemaResponseList.get_default_queryset`
(`api/registrations/views.py`) returns every revision to contributors,
pending and approved ones to moderators, and approved ones only to anyone
else. `SchemaResponse.create_from_previous_response`
(`osf/models/schema_response.py`) raises `PreviousSchemaResponseError`
while any revision on the registration is not approved.

### Belief revision

I had assumed that a list endpoint shows a resource's full state and that
authentication only changes what you may do. On OSF, authentication also
changes what you can see, so an anonymous reader can be correctly told that
everything is in order while a private revision exists. The safety I
attributed to `plan` sits with the server: the authenticated create refuses
while an unfinished revision exists. The script was safe all along, but
for a different reason from the one its header gave. The header now gives
the server's reason, with the source cited.

### What would change this belief

An OSF change that lets a second unfinished revision be created, or an
anonymous listing that shows pending ones. Either would bring back the case
the guard was written for. The check is the two functions named above.

### Implications for practice

A guard should be tested against the visibility of the caller that runs
it. The fake OSF in the tests returns the same listing whoever asks, which
is why the tests could not catch this. When a check reads remote state,
record which identity it reads as, and what that identity cannot see.
