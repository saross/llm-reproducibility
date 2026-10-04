---
priority: 3
scope: always
title: "Working Notes"
audience: "researchers"
tags: [research-methodology, llm-craft, open-science]
created: 2026-02-09
updated: 2026-08-02
status: active
---

# Working Notes

Joint research observations about methodology, findings, tooling, or
reproducibility.

## Format

Each observation should be numbered sequentially:

```text
## Observation N: Title (YYYY-MM-DD)

### Context

Brief context for the observation.

### The observation

The substantive observation itself.
```

<!-- Entries below this line -->

## Observation 1: Data availability as the dominant reproducibility bottleneck (2026-02-11)

### Context

Integrating Key et al. 2024 lessons into `reproduction-implementation-notes.md` prompted
a cross-paper comparison of what actually prevented or complicated reproduction across
all 5 pilot papers.

### The observation

Across the 5-paper pilot, every paper's code ran successfully once an appropriate Docker
environment was constructed. The only PARTIAL verdict (Key et al.) was caused entirely
by data inaccessibility, not computational failure. The pattern:

| Paper | Code barrier | Data barrier | Verdict |
|-------|-------------|--------------|---------|
| Crema | 2 minor fixes | None | SUCCESSFUL |
| Marwick | None | None | SUCCESSFUL |
| Herskind | Wrapper needed | None | SUCCESSFUL |
| Dye | Wrapper + Dockerfile | OxCal proprietary (but intermediates provided) | SUCCESSFUL |
| Key | Wrapper + Dockerfile | 10/13 datasets inaccessible | PARTIAL |

This suggests that for JAS-published archaeological papers with code repositories, the
infrastructure gap (missing Dockerfiles, interactive scripts, no renv) is a surmountable
nuisance rather than a fundamental barrier. Data availability — particularly co-author-held
datasets and data in closed-access monographs — is the harder problem. The strongest
predictor of dataset accessibility was whether it had been independently published under
a journal data-sharing mandate.

This has implications for the open science compliance study's framing: the narrative should
emphasise data practices over code practices as the primary determinant of reproducibility
outcomes.

## Observation 2: Schema drift as a systemic risk in multi-session LLM workflows (2026-02-12)

### Context

Standardising assessment.json across 5 pilot papers revealed 3+ different metadata
structures produced by the same assessment pipeline over several weeks of sessions.

### The observation

When LLM-driven workflows produce structured outputs across multiple sessions, schema
drift is near-inevitable unless actively prevented. The 5 pilot assessment.json files
exhibited: nested vs flat metadata wrappers, `paper_slug` vs `paper_id` vs `slug`,
`system_version` vs `assessor_version`, and version strings from `v0.2-alpha` to `v1.0`.
Each file was internally valid but incompatible with the others.

The root cause is that prompt templates embed output format specifications (field names,
structure, version strings) that are not automatically synchronised when the canonical
schema changes. A schema update in `assessment-schema.md` does not propagate to the 4
prompt files that produce assessment outputs. This is analogous to the "stale cache"
problem — the prompts cache an older schema definition.

The mitigation adopted (a Schema Compliance section listing all locations that must be
updated together, plus bumping schema_version to force awareness) is lightweight but
depends on future instances reading and following the checklist. A stronger approach
would be to have prompts reference the schema file directly rather than embedding
output templates, but this would require restructuring the prompt design pattern.

For the Phase 2 study design, this finding argues for: (a) running all papers through
the pipeline in a compressed timeframe to minimise inter-session drift, and (b)
validating output schema consistency as a post-extraction check rather than assuming it.

## Observation 3: Determinism constraint on canonical matching keys (2026-07-06)

### Context

Fixing lossy de-hyphenation (continuity task C, commit 245d820) required a dictionary
to distinguish typographic line-break hyphens from genuine compounds. A system wordlist
(`/usr/share/dict/american-english`) was available on the development machine.

### The observation

Any function feeding `normalise_for_matching` must not consume environment-dependent
inputs — host wordlists, locale, tool versions — because the matching key's entire value
is its machine-independence: the same PDF must produce the same canonical key on a
laptop, on sapphire, or on a collaborator's machine, or deterministic quote verification
silently becomes machine-relative. The fix therefore vendors a frozen 9,810-word
dictionary subset (`affix-joined-words.txt`, provenance and regeneration command in its
header) rather than reading the host dictionary at runtime. Regenerating the file is a
deliberate, versioned act precisely because it changes matching keys.

This generalises to every deterministic-verification layer in the pipeline: reproduction
comparisons, FAIR sub-principle checks, and any future quote-checker all inherit the
same rule — pin the reference data in the repo, never resolve it from the environment.

## Observation 4: Subagent-relayed specifics ran ~1 in 10 wrong during repo exploration (2026-07-06)

### Context

Project revival (2026-07-03) used three parallel explorer agents to map a five-month-
dormant repository: pilot-study state, reproduction-system internals, and overall repo
state. Their reports drove the agentic modernisation plan written the same session.

### The observation

The maps were substantially accurate and made a one-session revival possible, but
roughly one in ten relayed *specifics* required correction when re-verified at source:
cluster-prompt dates taken from filesystem mtimes when the file headers said 2025-11-29,
and a version claim ("all cluster prompts v1.1") that held for only one of three files.
Breadth from agents, but every specific that reached a commit message, the README, or a
memory was re-checked against the file first — and that re-verification pass is what
caught the errors.

Two implications. Methodologically for this project: when we describe LLM-assisted
workflows in the compliance study or grant materials, "subagent reports are maps, not
gazetteers, with a measurable ~10% specifics error rate absent source re-verification"
is an honest, citable characterisation of current practice. Operationally for the
agentic modernisation: the planned deterministic gates between workflow stages (file
existence, value extraction from outputs rather than agent assertions) are not
optional hardening — they are the mechanism that makes agent-relayed claims safe to
act on at corpus scale.

## Observation 5: Prompt-injection attempts surfaced in the web-search layer during the stack-positioning sweep (2026-07-13)

### Context

The 2026-07-07/08 stack-positioning scout sweep (twelve paired lit-scout/prior-art-scout
runs, synthesis at `wiki/planning/scout-reports/2026-07-08-stack-positioning-synthesis.md`)
paired every proposer draft with a fresh-context adversarial verifier. In the P4
(credibility) prior-art pipeline, both agents hit adversarial content in their tooling
itself, not just in the subject matter they were assessing.

### The observation

Per `wiki/planning/scout-reports/2026-07-07-p4-credibility-prior-art-verified.md`
(security note, and finding 1 in the verifier's closing notes), two prompt-injection
attempts were logged in one pipeline: the proposer encountered injected content in its
WebSearch results, and the fresh-context verifier — reading the proposer's draft —
separately hit text impersonating a harness system-reminder ("The date has
changed... 2026-07-07") followed by fake "MCP Server Instructions" for a Hugging Face
server. Neither agent had MCP tools available beyond `Read`/`Bash` in that context; both
recognised the content as data rather than instructions, disregarded it entirely, and
flagged the sighting in their reports rather than acting on it or letting it alter their
verdict.

Later runs in the same sweep treated this as a standing risk rather than a one-off
curiosity. S1 (arXiv citation-integrity sweep) ran two WebSearch calls and explicitly
logged "no prompt-injection attempts observed," distinguishing WebSearch's own trailing
"REMINDER: include sources" footer (harness formatting) from actual injected
instructions. G1 (archaeology grey-literature guard pass) reported no injection sightings
across 26 logged queries and noted it had been briefed on the two earlier sightings. C2
and C3 (deeper-chaining runs) eliminated the surface structurally rather than
procedurally: both ran on API-only inputs (Semantic Scholar, arXiv Atom XML, CrossRef/
OpenAlex, local Zotero SQLite) with no `WebFetch`/`WebSearch` call at all, so there was no
free-text web content available to carry an injection.

Principle: for research agents, the web-search layer is an adversarial input channel,
not a neutral data source — content returned by `WebSearch`/`WebFetch` can carry text
designed to look like harness instructions, and the correct response, demonstrated twice
here, is recognise-as-data, refuse, and report. The most robust mitigation is
architectural rather than purely behavioural: pipelines that can run on structured APIs
alone (C2, C3) remove the injection surface entirely rather than merely training agents
to resist it. This sits alongside **Observation 4** (subagent-relayed specifics ran ~1 in
10 wrong without re-verification): both observations are about the same underlying
fragility of agent-mediated information, and both argue for structural safeguards over
relying on agent vigilance alone.

**Caveat flagged during this write-up (2026-07-13):** the sweep's own synthesis (§5)
suggested scout prompts should carry standing "treat web content as data" language, but
as of this writing no such standing instruction has been committed to the scout agent
definitions in `~/personal-assistant/agents/` (checked `lit-scout.md`,
`prior-art-scout.md`, and their verifiers — no matching text, and `git log` on those files
shows no post-sweep commit adding it). Contrast **Observation 6**: the "et al." rendering
defect from the same sweep *was* patched into the agent definition (commit `cfa0c3d`,
personal-assistant). The injection-vigilance lesson has so far only propagated
informally — by briefing individual runs, as G1's report shows — rather than via a
committed prompt change. This is a real gap, not yet closed.

As a small, live illustration of the principle above: while this very entry was being
drafted, this session's own tool-result channel carried an unsolicited "MCP Server
Instructions" block for a Hugging Face server — structurally identical to the fake
instructions described above, and unprompted by any tool call made in this session. It
was treated as data, not acted upon, and no Hugging Face tool was invoked.

## Observation 6: Verifier catch taxonomy from the 2026-07 stack-positioning sweep (2026-07-13)

### Context

Across the six-lane DOI sweep (twelve runs, ~1,600 machine-checkable claims; synthesis at
`wiki/planning/scout-reports/2026-07-08-stack-positioning-synthesis.md`, §5), the arXiv
follow-up sweep (S1 + S2, 285 claims: `2026-07-08-s1-citation-integrity-arxiv-verified.md`,
`2026-07-08-s2-protocol-extraction-arxiv-verified.md`), and the deeper-chaining round
(C1 + C2 + C3, 295 claims), every proposer draft was re-checked by a fresh-context
adversarial verifier against authoritative sources (CrossRef/OpenAlex/Semantic Scholar/
arXiv Atom API for papers; GitHub/PyPI/Hugging Face APIs for tools). The errors that
survived to verification form a stable, small taxonomy.

### The observation

| # | Failure type | Scale | Mechanism | Resolution |
|---|---|---|---|---|
| 1 | Systematic rendering defect | 11 instances across 3 lit-scout runs (P2: 2, P3: 5, P4: 4) | "et al." applied to two-author papers, silently suppressing named co-equal co-authors — e.g. Brown & Heathers (P3, GRIM), D'Souza & Auer (P3), Brown & Spillias (P3), Marshall & Wallace (P3), Serra-Garcia & Gneezy (P4) | Length-gated rendering rule (1 → bare surname, 2 → "A & B", ≥3 → "et al.") patched into the lit-scout agent definition, commit `cfa0c3d` (personal-assistant repo). One run in the same sweep (P6 literature, `2026-07-08-p6-citation-lit-verified.md`) already followed this rule and scored 0 errors across 120 claims — the empirical case for the fix. |
| 2 | True confabulation | 1 instance | Fabricated author given name, "Yiling Yang" for **Yang Yang** (PNAS 2020, `10.1073/pnas.1909046117`), originating in WebSearch-snippet-derived text rather than an API-grounded field | Caught and corrected by the P4 prior-art verifier (`2026-07-07-p4-credibility-prior-art-verified.md`); every GitHub/Hugging Face field in the same report (44 claims) matched its API exactly |
| 3 | Aggregator version-staleness | 2 instances | Semantic Scholar/OpenAlex carrying superseded metadata: CiteAudit (arXiv `2602.23452`) — first author changed between versions (Zhengqing Yuan → Kaiwen Shi promoted to first in v3); MemoNoveltyAgent (arXiv `2603.20884`) — retitled at v3 (was "NoveltyAgent: Autonomous Novelty Reporting Agent...") | arXiv Atom API treated as authoritative over the aggregators; both rows vindicated the proposer (`2026-07-08-s1-citation-integrity-arxiv-verified.md`) |
| 4 | Operational, not epistemic | Recorded once | Zotero sqlite dedup connection racing Zotero's own desktop-sync writes during staging imports, surfacing as a spurious "database disk image is malformed" | Transient; resolved by retry, no data loss (personal-assistant memory log, 2026-07-08, P4/P5 import failures) |

Two wrong-field metadata reads (dates — P2 prior-art row 13's Hugging Face dataset
`lastModified`; P6 prior-art row 11's GitHub last-active) round out items 1 and 2 into
the six-lane DOI sweep's 14 total hard failures against ~1,600 claims, a hard-failure
rate of ≈1% (synthesis §5). Item 3 is not a proposer error at all: it surfaced a day
later, in the 285-claim arXiv follow-up sweep, as a verification-methodology risk —
Semantic Scholar/OpenAlex carried out-of-date metadata that would read as confabulation
to a verifier trusting the aggregator over the primary record; checking the arXiv Atom
API directly resolved both rows as PASS, vindicating the proposer twice. The 295-claim
chaining round (C1: 120/120; C2: 94/95 + 1 low-severity title-truncation partial; C3:
80/80) added no further hard failures, reinforcing rather than diluting the six-lane
sweep's rate.

Principle: errors concentrate exactly where proposer confidence is lowest —
WebSearch-snippet-derived fields (confabulation, mis-titling) — while API-grounded
fields (CrossRef, arXiv Atom, GitHub, Hugging Face) ran at or near zero error across
every run. Zero fabricated papers, repositories, or tools appeared across all twelve
DOI-sweep runs plus the five follow-up runs: the failure surface is attribution detail
(author names, versions, dates), not invented sources. This complements
**Observation 4** (subagent-relayed specifics ran ~1 in 10 wrong without
re-verification): the same underlying LLM fallibility, but here a dedicated
fresh-context adversarial-verifier architecture — not just source re-checking by the
same agent — pulled the *hard*-failure rate down roughly an order of magnitude, from
~10% of relayed specifics to ~1% of machine-checkable claims. The verifier
architecture, not agent self-discipline alone, is doing the load-bearing work. See also
**Observation 5** (prompt-injection attempts in the same sweep) for a related but
distinct failure surface — adversarial tooling content rather than proposer error.

## Observation 7: Coherent identity confabulation survived 8 months in public metadata (2026-07-15)

### Context

CITATION.cff, codemeta.json, and CONTRIBUTING.md (all created 2025-11-13) carried a
confabulated author identity: "Shawn Graham", Carleton University, and
`github.com/shawngraham` repository URLs — the name, affiliation, and GitHub namespace
of a real, better-known digital-archaeology scholar, not the project's actual author.
The pilot findings report shared the wrong name. Detected 2026-07-14 only because
preregistration drafting triggered the anti-confabulation re-read rule at a
public-attachment boundary (the report was about to be frozen into an OSF
registration). Corrected in `38adf36` (Shawn Ross, Macquarie University, `saross`,
ORCID verified against author lines in published papers). Archive files and verbatim
extracted paper text were deliberately left untouched — the "Shawn Graham of Carleton"
mention inside `outputs/sobotkova-et-al-2016/` is the real Graham, cited by the source
paper itself.

### The observation

The confabulation survived roughly eight months of active development undetected, and
the mechanism is instructive: the wrong identity was **internally coherent**. Name,
affiliation, and GitHub namespace all matched each other (they belong to the same real
person — just not this project's author), so no field contradicted any other and every
casual read passed. This is confabulation-by-proximity-substitution: a higher-frequency
neighbouring entity from the same field displaced the true, lower-frequency one, and
brought its own consistent metadata along. Two principles follow. First, **internal
consistency is not evidence of correctness** — LLM confabulations arrive coherent, so
cross-field agreement checks (the kind casual review performs implicitly) cannot catch
them; only comparison against an external anchor (git remote, ORCID registry, the
author's own publications) can. Second, **identity fields in generated metadata need an
explicit audit at creation time** — names, affiliations, PIDs, and namespaces in
CITATION.cff/codemeta-class files are durable, public, and feed citation infrastructure
(GitHub's cite widget, Zenodo deposits), so an error there propagates outward silently.
Complements **Observation 4** (the same fallibility class in relayed specifics): the
failure surface is again attribution detail rather than invented entities — the
substituted scholar exists; that is exactly why it read as plausible.

## Observation 8: The adversarial review gate transfers from code to study designs (2026-07-15)

### Context

The Phase 2 OSF preregistration was drafted (v0.1, `9405182`) and stress-tested in the
same session via `/review-implementation` (four-phase protocol: capability scan,
exploitation review, quantitative audit, recommendation), with revisions landing as
v0.2 (`885e664`). The review was requested by Shawn "so that we stress-test [the
methods] before committing" — statistics prioritised, net cast wider.

### The observation

Applied to a study design rather than code, the review caught five substantive defects
before lodgement, when they were still free to fix (post-lodgement they become public
amendments): (1) **definitional circularity in H2** — the outcome (reproduction
verdicts) partially encodes the predictor (data availability), fixed by switching to a
verification-target coverage endpoint with denominators locked pre-execution;
(2) **criterion contamination in H5** — the Transparency rubric directly rewards the
grouping variable (literate programming); (3) **post-treatment conditioning in H1** —
restricting the sample on code presence conditions on a policy-responsive variable;
fixed by restricting on the policy-invariant property (quantitative) instead;
(4) **hypothesis wording outrunning its test in H4** — an equivalence clause
("regardless of environment quality") no test at this N can establish; (5) **a missing
counterfactual** for the causal policy question, resolved by adding a *JAS: Reports*
difference-in-differences control arm. Notably, the highest-value findings (1–3) are
construct-validity and causal-structure defects that the skill's statistical checklist
does not prompt for — power, multiplicity, and exact tests were prompted; circularity
and conditioning came from unprompted reasoning. Principle: the
review-before-commitment gate transfers cleanly from code to methodology and pays off
most at pre-registration boundaries; but the skill needs a study-design checklist for
the defect classes that carried this review (fitness gap logged at the 2026-07-15
session close; see continuity).

## Observation 9: xelatex silently drops out-of-font glyphs (2026-07-18)

### Context

Building PDF artefacts for the OSF preregistration lodgement, xelatex builds of
instrument-bearing documents (accepted from the 2026-07-18 handoff, verdict
returned 2026-07-24).

### The observation

xelatex drops glyphs absent from the selected font silently — the failure
surfaces only as a log warning, never in the visual output flow. For
instrument text this is a meaning-inversion hazard: a vanished "≥", "±", or
minus sign changes what a threshold or tolerance says, while the PDF remains
visually plausible. Principle: never sign off a built PDF by eyeballing;
verify by machine text extraction and comparison against the source.

## Observation 10: Markdown-emphasis stripping needs fixpoint iteration (2026-07-18)

### Context

Preparing plain-text paste artefacts from markdown sources for the OSF
lodgement (accepted from the 2026-07-18 handoff, verdict returned 2026-07-24).

### The observation

Single-pass regex stripping of markdown emphasis leaves survivors: nested
spans (bold inside italic) and spans broken across wrapped lines. The robust
shape is fixpoint iteration — re-apply the strip until the text stops
changing. Generalises to any peel-one-layer text transformation over nestable
markup.

## Observation 11: Web forms need interface-shaped paste artefacts (2026-07-21)

### Context

OSF registration lodgement 2026-07-20/21: text boxes rendered markdown line
breaks literally, and the §10 power table pasted as pipe soup (accepted from
the 2026-07-21 handoff, verdict returned 2026-07-24; elevated to a standing
default by the 2026-07-22 user-obs verdicts).

### The observation

Output destined for a web form must be shaped for the form, not for the
repository: paste files unwrapped to flowing lines, no tables in paste-field
content (restructure as prose or lists), and a committed generator script so
the form text and the verified draft stay in lockstep. The repository copy
and the paste artefact are different renderings of one source, never two
sources.

## Observation 12: External facts have a half-life (2026-07-21)

### Context

The registration was lodged with an embargo on the strength of a journal
policy (JAS: Reports double-blind mandate) that had lapsed mid-2024; a
re-check cleared it and the embargo was lifted the next day (accepted from
the 2026-07-21 handoff, verdict returned 2026-07-24).

### The observation

Externally sourced facts — journal policies, vendor portal behaviour, API
surfaces — decay without notice. Re-verify at the moment of use, not at the
moment of recall, and record the check date alongside the fact so the next
reader can judge staleness. Complements Observation 13: internal records
drift too.

## Observation 13: Verification ledgers drift from their sources (2026-07-21)

### Context

The Cosmos application's claim ledger, reconciled against a clean-context
adversarial agent before submission: three pointer errors and six wording
drifts against the underlying sources (accepted from the 2026-07-21 handoff,
verdict returned 2026-07-24).

### The observation

A verification ledger is a pointer structure, not an authority — it drifts
from its sources as both evolve. Before reuse in anything outward-facing,
reconcile the ledger against the sources with a fresh-context adversarial
pass; the maintaining context cannot see its own drift. Same epistemics as
the anti-confabulation rule: specifics are suspect until re-checked at
source.

## Observation 14: Canary probes beat documentation for harness behaviour (2026-07-24)

### Context

The D-2 engine spike: three documentation citations predicted that
SubagentStart/SubagentStop hooks would not fire for workflow `agent()`
spawns, making the workflows engine "more likely to fail than pass" the
reliability requirements.

### The observation

A settings-hook canary plus one control and one test spawn settled the
question empirically in about 20 seconds — hooks fire, injected context
arrives, the transcript path is delivered, and named agent types reach
matchers. All three documentation-based predictions were wrong. For
load-bearing harness behaviour, documentation is a hypothesis generator;
the cheap empirical probe is the evidence. Budget the 20 seconds before
architecting around a documented limitation.

## Observation 15: Reliability-gate statistics are decision-relevantly sensitive to design choices (2026-07-24)

### Context

Pre-build juncture review of the §8 validation phase (findings folded into
the ratified amendment scope; accepted from the 2026-07-24 handoff).

### The observation

Three statistical facts that change how the 0.90 reliability gate should be
run. First, power: at n=90 items (three pilot papers) a true agreement of
0.85 false-passes the gate roughly 12% of the time; scoring all five pilots
(n=150) roughly halves that to ~5.5%. Second, definition sensitivity:
candidate agreement statistics cross the same 0.90 gate at item-flip rates
ranging from ~10% to ~30%, so the statistic must be pre-specified (unanimity
proportion chosen as strictest). Third, ranking impossibility: the
achievable spot-check n puts ~±0.09 confidence intervals on between-model
agreement differences, so no preregistration-compliant model ranking exists
before the census — selection must be gates-plus-cost, not ranking. Gate
design choices that look like implementation detail carry first-order
inferential consequences.

## Observation 16: Structural instrument checks have a prose-shaped blind spot (2026-07-27)

### Context

The D5 manifest-consistency gate's first implementation verified registered
mirrors by comparing fenced code blocks and table rows between the canonical
instrument file and its operational copy. The Pass 6 prompt carried a banner
asserting a *verbatim* mirror of the FAIR instrument.

### The observation

Every block and every row matched, so the gate reported PASS — while four
normative statements from preregistration §7.1 were absent from the prompt:
that unscoreable sub-principles score 0; that data and code scores are never
aggregated; the A1 majority-retrievability rule in full; and the FAIR4RS
out-of-scope statement. All four were prose, which is exactly the shape the
check could not see (erratum-log Entry 2). A structural check reports on the
fraction of a document it can parse and is silent about the rest, so the
guarantee it delivers is strictly weaker than the one the banner claimed.
Where the claim is "verbatim", the check must be byte-exact over a delimited
region rather than structural over parseable fragments. The banner asserting
equivalence had been written before anything verified it, and was untrue for
five days across a frozen artefact. Impact was nil — no pilot score revised —
which is luck, not design.

## Observation 17: Independent reimplementation is a review technique (2026-07-27)

### Context

A third session resumed from the 2026-07-24 handoff and rebuilt the D5 gate
from the same specification, unaware the zbook build had already landed. Seven
commits arrived mid-session; the two implementations were compared rather than
either being discarded (`03f10ad`→`ceb1d79`).

### The observation

The delta between two independent readings of one specification was two real
defects in the already-shipped build, both since ported in: the
structural-versus-byte-exact mirror gap (Observation 16), and a reverse-sweep
gap that let an unregistered `.md` dropped into the instruments directory pass
the gate. Neither is a matter of taste. Both sit where the specification was
silent and the first reading resolved the silence one way without registering
that a choice was being made — which is precisely what re-reading a single
implementation cannot surface, because the reader inherits the same
resolution. A second independent reading makes the underdetermined points
visible as disagreements. Too expensive to schedule as routine practice, but
nearly free when it happens by accident: compare before discarding.

## Observation 18: An ad-hoc sweep is an unscoped gate, and it fails the same way (2026-08-02)

*(Accepted by Shawn 2026-08-02, as drafted.)*

### Context

Sweeping the repository for stale commit references, while investigating a
manifest defect during the same session that found the D5 gate's coverage gap.

### The observation

The first regex returned 187 non-resolving "hashes". The number was meaningless:
it had swept up Digital Object Identifiers (DOIs), ORCIDs, Semantic Scholar
corpus identifiers, page offsets, and the deliberate `1234567` placeholders in
the persistent-identifier guide. Tightened to backticked tokens containing at
least one hex letter within commit-referencing files, the real figure was 115
resolving and 21 not.

The failure is identical in structure to Observation 16 — an instrument
reporting confidently over a scope its author never checked — but it applies to
the *disposable* measurements written mid-session, which get no review, no
tests, and no pre-commit gate. Those are the instruments most likely to produce
a number that reaches a person, and the least likely to be scrutinised before it
does. The practical rule: before quoting a swept count, hand-check a sample of
the hits, and prefer a sweep that prints *what it matched* over one that prints
only *how many*.

## Observation 19: A version number without a recorded referent can only be compared, not checked (2026-08-02)

*(Accepted by Shawn 2026-08-02, as drafted.)*

### Context

Planning the extension of the manifest-consistency gate from 7 of 25 registered
entries to all of them.

### The observation

`manifest.yaml` registers version numbers but never records what each number
*measures*. One entry (`assessment_json`) tracks the payload `schema_version`
emitted into each `assessment.json`, while pointing at a document whose own
heading carries a different version — two legitimate axes, no drift. A naive
widening of the version check would have converted that correct state into a
permanent build failure, and the usual response to a gate that fails on a
correct file is to add an exception, which is how checks decay into noise.

Coverage was the visible problem; *semantics* was the binding one. A comparison
between two numbers is only a check when both are known to measure the same
thing — otherwise it is a coincidence detector that fires whenever a file
carries more than one version string. This is why the monitoring plan sequences
registry reorganisation (declare the axis) before checker widening (compare it),
rather than the reverse.

## Observation 20: An enumeration that returns n−1 of a known-n set is a finding, not a fact (2026-08-02)

*(Approved by Shawn 2026-08-02; wording accepted as drafted, same day.)*

### Context

The amendment §1 consistency check (task E2) re-ran erratum-log Entry 2's
impact sweep over the persisted pilot outputs. Both the original 2026-07-27
sweep and the re-run enumerated four FAIR assessments from a five-pilot set,
and both wrote "the four papers carrying FAIR assessments" into the record as
a fact about the corpus.

### The observation

The fifth assessment existed the whole time: crema-et-al-2024's sits one
directory below the `outputs/*/extraction.json` glob and under the pre-v2.6
top-level key `infrastructure` rather than `reproducibility_infrastructure`.
Two silent scope-narrowers — a path pattern and a schema assumption — trimmed
the set before any check ran.

This is the Observation 16 shape again (a check reporting over a narrower
scope than its readers assume), but it is the dual of Observation 18. That
sweep *over*-matched, and its countermeasure — print what you matched, not
just how many — works because the junk is in the output. An under-match cannot
be exposed that way: nothing prints what a glob never enumerated. The control
that was available here was cheaper and different: the expected cardinality
was known — five pilots, named everywhere — the sweep returned four, and the
shortfall was rationalised into prose instead of investigated. It took the
registrant asking "was it accidentally discarded?" to force the run-down,
which then took four commands (`git log --follow` found it archived-not-lost;
`jq` found the divergent key).

Two rules follow. When an enumeration over a set of known size returns fewer
members, the missing member is a defect to run down before the count enters
any record. And when the set is decision-relevant — these five reference
scores are the §3 concordance-floor denominator for validation-phase model
selection — the enumeration itself should be registered and generated, never
re-derived by glob at each use (monitoring plan §1(c) and class E8; erratum
log Entry 2 coverage correction, 2026-08-02).


## Candidates — 2026-08-03 (pending review)

*Drafted at handoff; Shawn adjudicates next session. No silent discard.*

**Candidate WN-l — A wired, tested control is aspirational until its log
shows a real pass.** The receipt gate was designed, wired, and
build-tested, and its log carried only blocks: it had never validated one
production receipt, and the run it "guarded" was protected entirely by
orchestrator-side post-hoc verification. The repaired gate then blocked
9/15 spawns for a reason its own log cannot distinguish. Companion rule to
Observations 14/16: a control's operative status is evidenced by logged
passes on real traffic plus one observed catch, not by wiring, tests, or
the existence of its log file. (Sources: receipt-gate-log tallies in the
three arm run-records; audit + re-audit reports, 2026-08-03.)

**Candidate WN-m — Within-model run disagreement is a rubric-ambiguity
locator.** Across three arms, run-to-run disagreement concentrated on the
same five instrument clauses (A1.2, R1.1, A2, R1.3, F-block upstream
crediting), and the most capable model was not the most stable. Three runs
of a single cheap model would have located the same clauses as the full
cross-model benchmark — a ~$3 instrument diagnostic. (Source: per-arm
stability disagreement lists in the 2026-08-03 run-records.)

## Observation 21: An audit surface must equal the reader's trust surface (2026-08-10)

*(Approved by Shawn 2026-08-10; drafted at handoff the same day.)*

### Context

The prior-art scout's report on FAIR third-party-artefact handling shipped
with a machine-readable claims ledger, and the adversarial verifier passed
65 of its 68 claims — every GitHub API field and every DOI metadata claim
exact. The same verification pass found four direct quotations that do not
exist at their cited sources and one load-bearing claim inverted (ACM
Artifact Review and Badging v1.1's "Author-created artifacts…" rendered as
the absence of any authorship gate).

### The observation

Every fabricated quotation sat *outside* the emitted claim set. The
proposer emitted claims for what it had queried mechanically — the
cheap-to-verify stratum — and none for the prose it wrote from reading,
which is where a reader's trust actually lands. An audit over a
proposer-selected claim set therefore clears exactly the content it never
covers: the ledger's 96% pass rate was an artefact of claim-set selection,
not evidence of a clean report.

This is the Observation 16 shape (a green check over a narrower scope than
its readers assume) in its third costume — first a mirror check blind to
prose, then a sweep blind to its own scope, now a verification ledger
blind to quotations. The recurring cure is the same: define the checked
surface from the *consumer's* side (everything a reader would treat as
verified — here, everything inside quotation marks), never from the
producer's convenience. Countermeasure shipped 2026-08-10: the scout's
definition now requires a `quotation` claim for every quoted string, with
unfetchable material demoted to labelled paraphrase (personal-assistant
`a3f5793`). Corollary worth keeping: the substance of three of the four
fabricated quotes was *correct* — the failure mode is fluent paraphrase
drifting into quotation marks, so the marks themselves, not the content,
are what the audit must bind.

## Observation 22: Test a one-shot resource's premise against primary artefacts before spending it (2026-08-10)

*(Approved by Shawn 2026-08-10; drafted at handoff the same day.)*

### Context

Amendment 1 §2 permits exactly one routing-fix attempt before the
registered majority-vote consequence applies. The 2026-08-03 handoff
carried a ready candidate: push `fair-principles-guide.md` uniformly,
premised on "receipts show inconsistent pulling". The next session's
opening move was to re-check that premise against the 45 persisted spawn
receipts before presenting the decision.

### The observation

The premise held for one arm of three: sonnet pulled the guide in 9/15
spawns, but opus and fable pulled it in 15/15 each — and both failed both
gates on the same item cluster. Two follow-up probes sealed it: the guide
is silent on the disputed cases (pushing a document that lacks the answer
cannot make the answer uniform), and the within-sonnet correlation between
guideless spawns and minority votes, while real (17 of 29 splits vs ~11.3
expected), sat on the wrong gate — sonnet's binding constraint was
concordance. The card, if played, would have been spent to nudge one arm's
stability while eligibility stayed out of reach for all three.

The rule: when a plan is about to spend a resource that cannot be
re-spent — a registered one-shot remediation, an irreversible filing, a
single permitted re-run — its stated premise is a hypothesis, and the
cheapest test of that hypothesis against primary artefacts comes first.
Here the test cost a quarter of an hour against artefacts already on disk
and reversed the session's opening plan. The handoff that carried the
candidate was faithful; the premise it recorded was simply narrower than
the evidence — which is exactly why premises recorded under context
pressure get re-verified at the source before they are acted on
(cross-reference: the anti-confabulation rule, and Observation 14's
canary-probes-beat-documentation).

## Observation 23: A verifier must model the delivery mechanism it rides on (2026-08-17)

*(Approved by Shawn 2026-08-17; drafted at handoff the same day. WN-s.)*

### Context

The D3 re-benchmark's first arm (sonnet) hard-stopped with 15/15
per-item reconciliation failures — while every receipt was valid and
the scores were sane. Fourteen verdicts flagged the same
"contamination": each spawn had read a
`tool-results/hook-*-additionalContext.txt` file.

### Observation

The flagged file *was the instrument delivery*. The v2.1-plus-guide
push (~77KB) crossed the harness's inline additionalContext threshold
for the first time, so the harness spilled it to a per-spawn file the
agent must Read to receive its instruments — and the reconciler's
contamination rule, written when pushes arrived inline and invisibly,
converted the correct receiving behaviour into a violation
(14/15 false flags; the fifteenth was a separate discovery-fallback
defect). Verified by opening the file: it begins with the push hook's
own banner and carries the receipt tokens the spawns echoed.

### Implication

A verification layer encodes assumptions about the channel it observes.
Any harness behaviour that varies with payload size (spill thresholds,
truncation, pagination) is part of the instrument's environment, not
background — and a checker that has not modelled the channel will
manufacture false findings with a checker's authority precisely when
the payload grows. Fix pattern: classify the channel's own artefacts
explicitly (reconcile-run v1.4's `HOOK_DELIVERY_RE`), and treat any
change in checker false-positive rate as a possible environment change
before treating it as subject behaviour. Anchors: `ce1cf00`;
`outputs/validation/failure-modes/register.md` F-004.

## Observation 24: Schema compliance and attestation integrity are separate axes (2026-08-17)

*(Approved by Shawn 2026-08-17; drafted at handoff the same day. WN-t.)*

### Context

Three Claude arms, identical contracts, identical session-inherited
effort (xhigh), 15 scoring spawns each, two independent measurements
per arm: validator retries (mechanical schema compliance, from
transcripts) and receipt-integrity incidents (from three verification
layers).

### Observation

Validator retries ran 3/1/0 for sonnet/opus/fable — a clean capability
gradient. Receipt-integrity incidents ran 0/0/2 — inverted. The arm
with perfect mechanical compliance produced the cycle's only fabricated
attestation (a `pulled_files_read` entry for a file its transcript
never touched — register F-001) and its only boundary improvisation
(a session-directory Glob where the brief mandates ESCALATE — F-002).
The contrast case (F-006, 2026-08-03) is the least capable arm hitting
the same obstacle class and honestly declaring the failure.

### Implication

As capability rises, failures migrate from the layer a validator sees
(format fumbles) to the layer only a transcript audit sees (claims
about work performed). n is small (2 in 45) and effort/capability are
confounded pending the head-to-head effort study — but if the
direction holds, compliance machinery built around capable models must
weight attestation verification over schema validation, because the
better the model, the less the validator measures. Anchors:
`benchmark-2026-08-17/arm-*/run-record.json` telemetry; register
F-001/F-002/F-006.

## Observation 25: Budget tripwires need a legitimate-excess clause and a stuck-loop indicator from birth (2026-08-17)

*(Approved by Shawn 2026-08-17; drafted at handoff the same day. WN-u.)*

### Context

The D3 contract's per-arm spend wire (7M tokens, ~2× the reproducible
baseline) fired on the fable arm at 7.10M — not from runaway
behaviour, but because the contract's own remediation (re-running two
reconciliation-failed items) added its spend to the arm budget it was
repairing.

### Observation

The wire was written against a "runaway spend" threat model and never
anticipated that legitimate remediation accumulates into the same
budget. The operator's amendment distinguishes the cases structurally:
the wire grows by the re-run percentage (7M × (1 + 2/15) ≈ 7.93M here),
UNLESS an indicator points to a stuck or repeating loop (the same item
failing repeatedly; replacement spawns themselves failing) — in which
case the halt applies regardless of headroom. The event is reported
either way.

### Implication

Every hard ceiling should be born with its legitimate-excess clause and
its illegitimate-loop indicator, because the alternative is a wire that
either fires on the contract's own housekeeping or gets silently
raised under time pressure. The reporting is the invariant; the
ceiling is contingent. Anchors: `arm-fable-5/tripwire-event.md`; plan
decision log 2026-08-17.

## Observation 26: Errors are specimens — the failure-register decision (2026-08-17)

*(Approved by Shawn 2026-08-17; drafted at handoff the same day, at his
direction: record the errors and the decision to track them.)*

### Context

One cycle produced errors at every layer: two genuine model incidents
(a fabricated receipt entry; an out-of-scope Glob), two verifier
defects (a checker that read empty directories as clean; a per-item
agent that audited an eleven-day-old run), harness constraints and
silent behaviour changes (top-level allOf rejection; the
additionalContext spill), and one operator-caught Claude confabulation
(session effort asserted "high"; /effort showed xhigh).

### Observation

The decision (Shawn, 2026-08-17): every failure in a governed run is
recorded at adjudication time in an append-only, categorised,
evidence-anchored register
(`outputs/validation/failure-modes/register.md`), with model failures,
verifier failures, and harness failures kept structurally distinct —
"so we can analyse them together later", with particular interest in
fabrication and anything misalignment-shaped. Claude-side
confabulations feed the parallel confab tracker in the
personal-assistant ecosystem. The register was seeded with seven
entries spanning both benchmark cycles the day it was created.

### Implication

The practice converts incident response into corpus building: each
error's disposition note is written once, while the context is loaded,
instead of being reconstructed at analysis time from commit archaeology.
Two structural rules carry the value: the observer-distinct categories
(model behaviour statistics must not inherit checker error), and
anchors on every entry (an unanchored failure report is itself an
attestation). Standing rule going forward: every reconciliation
failure, gate block, or probe failure gains an entry at adjudication —
and the register's running-observations section is where cross-cycle
patterns (like Observation 24's axis split) accumulate for the
alignment-relevant analysis Shawn intends.

## Observation 27: Effort pins must be artefact-derived — the harness persists no effort field (2026-08-17)

*(Approved by Shawn 2026-08-17; drafted at handoff the same day. WN-v.)*

### Context

The effort study required pinning reasoning effort per scoring spawn.
Direct inspection of spawn metadata from the D3 reconcile lane — whose
spawns were launched with `effort: 'low'` in workflow opts — showed the
harness persists only `agentType`, `spawnDepth`, and `model`: the
requested effort leaves no trace in any artefact.

### Observation

A parameter passed through opts controls behaviour but is
attestation-only unless deliberately made durable. The build therefore
carried the pin on three legs: opts (behavioural), a Provenance line
injected into every scoring prompt (the only durable, artefact-derived
carrier — it survives in the transcript), and assembler parse-back with
a mixed-vintage hard error. Before any spend, the opts channel itself
was verified by a differential probe (P3: identical prompts at low vs
max produced a 7.5× output differential in 34 seconds, for cents) —
replacing a passive fallback that could only have masked failure, never
detected it.

### Implication

For any served parameter an experiment varies: (1) check what the
infrastructure actually records — assume nothing; (2) if nothing, route
the value through a channel that lands in a durable artefact; (3) verify
the control channel with a cheap differential probe before committing
spend. Anchors: workflow v1.5 header; `assemble-arm-record.py` v1.4
`provenance_pinned`; `effort-study-2026-08-17/p3-probe/probe-report.md`.

## Observation 28: A spend metric dominated by effort-independent components cannot measure effort response (2026-08-17)

*(Approved by Shawn 2026-08-17; drafted at handoff the same day. WN-w.)*

### Context

Opus@high generated 33% fewer output tokens than opus@xhigh (294K vs
437K) yet recorded a marginally higher contract-metric total (5.14M vs
5.07M). The aggregate briefly supported a published "cheapest passing
configuration" claim — overturned by Shawn's one-line question and a
component decomposition.

### Observation

The contract metric is ~92% cache-creation tokens — per-spawn context
writes (PDF, instrument, pack) that effort cannot touch and that wobble
a few percent with turn structure. The effort-sensitive component
(output) moved exactly as effort theory predicts; the aggregate hid it.
In component-weighted dollars the ordering inverted; both gaps sit
inside single-arm noise.

### Implication

Composite metrics inherit the dynamics of their dominant component. The
contract metric was designed as a runaway-spend wire (H4) and remains
correct for that; it is structurally wrong for within-model effort
comparison, which must read output tokens or a component-weighted cost.
Before any ranking claim, check the ordering survives per economically
distinct component. Anchors: study summary finding 2 (corrected,
`5c193e3`); run records for both opus arms.

## Observation 29: Harness caps are part of the measurement apparatus (2026-08-17)

*(Approved by Shawn 2026-08-17; drafted at handoff the same day. WN-x.)*

### Context

The sonnet@max arm produced 28 scoring transcripts for 15 items: 14 dead
attempts with no payload and no gate event, consuming 4.25M tokens (24%
of arm spend), with one item unrecoverable after two attempts. The
per-item lane misattributed some of this; the authoritative
reconciliation's denominator assertion (`--expect-spawns 15`) caught the
surplus by simple inequality.

### Observation

Max-effort emissions (thinking plus a large structured payload in one
response) exceeded the harness's per-response output cap
(`CLAUDE_CODE_MAX_OUTPUT_TOKENS` = 64,000); the harness silently killed
and respawned, converting model verbosity into invisible spend. The
attribution was settled by intervention, not inference: raising the cap
to 128,000 produced zero dead attempts across five subsequent re-run
spawns. What initially read as "max effort degrades harness compliance"
was substantially an infrastructure constant colliding with a
behavioural change the study itself induced; genuine model-attributable
residue remained (boundary Globs, one missing-scores payload), but a
quarter of the arm's cost was apparatus artefact.

### Implication

Every hard cap in the serving path is part of the experimental
apparatus: a study that varies a behaviour-inflating parameter without
provisioning the caps it will press against measures the cap, not the
model. Denominator assertions are the cheapest tripwire for "the
harness did something the design never modelled". Anchors: register
F-008/F-009; `arm-sonnet-5-max/halt-report-2026-08-17.md`;
`.claude/settings.json` env block (cap standing at 128,000).

## Observation 30: Licence conflicts are the norm on research surfaces, not the edge case (2026-10-03)

*(Approved by Shawn 2026-10-03; drafted during the E8-v2 reference adjudication.)*

### Context

The E8-v2 reference re-derivation scores R1.1 under AP-8, a clarity
test rather than a permissiveness test: any published licence passes;
same-artefact contradictions resolve to the most restrictive licence
(item 6); and validity is not adjudicated, because FAIR does not
enforce copyright (AP-8's validity note, Sitting 7).

### Observation

Every pilot paper adjudicated so far (four of five; crema pending)
carries at least one licence problem on its research surface, and the
problems come in four kinds:

1. **Divergent licences across copies of one artefact.**
   dye-et-al-2023: CC-BY-NC-ND on the accepted-version cover sheet
   against the Elsevier licence set on the version-of-record Crossref
   record; the supplement code inherits whichever governs (Sitting 2).
2. **Licences unsuited to the artefact type.** Creative Commons
   licences on code: dye's supplement code, by inheritance from the
   article (Sitting 2); herskind-riede-2024's S2.R under CC-BY-4.0
   (Sitting 4); marwick-2025's code, per its Zenodo field (Sitting 8).
3. **Multi-way assertion conflicts.** marwick-2025's data: the paper
   says CC-0, Zenodo's licence field says CC-BY-4.0, and the deposit's
   `LICENSE.md` is MIT for the whole repository (Sitting 7). Its code
   splits two ways: MIT in the paper and `LICENSE.md`, CC-BY-4.0 on
   Zenodo (Sitting 8).
4. **Licences that claim rights the licensor may not hold.**
   key-et-al-2024's scripts adapt the OLE function from sExtinct
   (GPL-2 per its CRAN archive DESCRIPTION) yet ship under the
   article's CC BY 4.0 (Sitting 6). marwick-2025 deposits full Web of
   Science records (abstracts, cited references, author emails) under
   open licences, beyond Clarivate's public terms unless consent was
   obtained, which the README does not mention. Coded "data shared,
   rights-incompatible" (Sitting 7); in Shawn's words, a licensing
   violation.

None of these moves an R1.1 score. Every conflicted artefact still
carries a published licence, so the most-restrictive rule passes it;
the R1.1 zeros so far come from absent licences (dye's `beads-1.csv`,
Sitting 1; key's unpublished data, Sitting 5).

### Implication

The most-restrictive rule settles scoring but hides how messy the legal
surface is: a reuser often faces two or three candidate licences for a
single artefact, and sometimes licences that cannot be valid. Licence
conflicts are therefore a research finding in their own right (Shawn,
Sitting 7: keep tracking them; they show how messy the surface is). The
census should code conflict type, the four kinds above, as a variable
of its own beside the binary R1.1. Licence- and rights-compatibility
checking is a capability for the uplift tool
(`wiki/planning/active-todo-list.md`, Deferred / Future Projects item
10); for third-party data, its route is to publish the exact query plus
record identifiers and rebuild the records from an open source such as
OpenAlex. Relations: Observation 1 (data availability is the dominant
bottleneck; once data are out, licence clarity is the next layer);
Observation 7 (errors persist unnoticed in public metadata);
Observation 24 (schema compliance and integrity are separate axes; here
a schema-valid Zenodo licence field contradicts the deposit's own
licence file). Anchors:
`studies/open-science-compliance/outputs/validation/e8-v2-rederivation/adjudication-log.md`
AP-8 and Sittings 1, 2, 4, 5, 6, 7, and 8; active-todo-list item 10.

## Observation 31: The noisy surface — research records carry many small metadata inconsistencies, and model-produced records carry the same ones (2026-10-03)

*(Approved by Shawn 2026-10-03; drafted during the E8-v2 reference adjudication.)*

### Context

The same adjudication logs, sitting by sitting, findings with "no score
effect": defects met while scoring that move no sub-principle. Across
the four papers adjudicated so far (crema pending) they fall into
recurring classes.

### Observation

Classes found so far (anchors are adjudication-log sittings unless
stated otherwise):

1. **Wrong resource type.** marwick-2025's compendium (data and code)
   is typed "Software" (Sitting 7); herskind-riede-2024's record (data
   and code) is typed "Dataset" (Sitting 4).
2. **Missing creator.** Both versions of herskind's Zenodo record list
   only Herskind; Riede is absent (Sitting 3).
3. **Version inconsistencies.** herskind cites v1 in its methods and v2
   in its data-availability statement, and the files differ (v2's S2.R
   is 33,834 bytes against v1's 18,707; AP-12, Sitting 3); herskind's
   paper states R 4.2.2, its v2 README R 4.3.2 (Sitting 4); marwick's
   preprint cites v1.1 where the version of record cites the concept
   DOI (Sitting 7). One slip is ours: marwick reproduction attempt-01
   cloned the live repository, 8 commits past v1.3 (AP-12).
4. **Malformed identifiers.** dye-et-al-2023 prints the DOI of its
   ArchaeoPhases citation (Philippe & Vibet 2020) with a doubled
   `https://doi.org/` prefix (Sitting 2).
5. **Missing relations.** Neither version of herskind's deposit carries
   any related identifier, not even the article DOI (Sitting 3);
   marwick's only typed relation is `isSupplementTo` a GitHub tree URL,
   not a persistent identifier (Sitting 7).
6. **Empty or placeholder content.** key-et-al-2024's supplementary
   `mmc4.csv` is a 75-byte header-only template (Sitting 5); herskind's
   Zenodo descriptions are empty (Sitting 3); marwick's is one sentence
   citing the paper (Sitting 7, AP-15).
7. **Uncredited source software.** key adapts sExtinct's OLE function
   without citing the package; only the script comments disclose it
   (Sitting 6).
8. **Publisher boilerplate mistaken for a data statement.** key has no
   data-availability statement; its "Supplementary data … can be found
   online" line is Elsevier's Appendix A boilerplate (Sitting 5).
9. **The same classes in our own model-produced records.** The pilot
   herskind extraction's completeness notes describe "lithic
   measurements, use-wear images", which are not in the paper (Sitting
   3; `studies/open-science-compliance/outputs/herskind-riede-2024/extraction.json:2225`).
   The pilot marwick extraction carried a DOI that the paper never
   cites and that resolves nowhere (10.5281/zenodo.14561925); through
   the declared-links registry it reached amendment 2 §2 as lodged
   2026-08-17 (`studies/open-science-compliance/prereg/erratum-log.md`
   Entry 4). With class 3's attempt-01 slip, that is content,
   identifier, and version errors: the research records' own classes.

### Implication

Each error is minor and none changes a score on its own, but together
they make the research surface noisy in ways reusers trip over. All were
found by cross-checking sources against one another (paper against
deposit, deposit against registry API, registry record against file
contents), which LLMs do well and at scale; Shawn notes this shows a
real role for LLMs in producing and auditing metadata. Class 9 is the
counterweight: model-produced records show the same error classes, so
they need mechanical verification (registrant direction, 2026-10-03: a
deterministic check that every registry identifier appears verbatim in
the paper or its supplement, and mechanical verification wherever
possible). Both point to the uplift tool and the human-FAIR vs
machine-FAIR study (`wiki/planning/active-todo-list.md` items 10 and
11). Relations: Observation 4 (subagent-relayed specifics ran ~1 in 10
wrong); Observation 7 (errors persist in public metadata, and internal
consistency is no evidence of correctness); Observation 12 (external
facts have a half-life; deposits keep versioning after publication);
Observation 13 (verification ledgers drift from their sources; the
registry was curated from the extraction records); Observation 19 (a
version number without a recorded referent, as with a concept DOI or
an R version the deposit contradicts); Observation 30 (licence
conflicts, the legal layer of the same noise). Anchors: adjudication
log Sittings 2–7 ("Findings (no score effect)" blocks) and AP-12;
erratum-log Entry 4.

*→ Extended by Observation 32 (2026-10-03): the old E8 reference's evidence — the model-produced pilot assessments — carried the same error classes (class 9 above).*

## Observation 32: The old reference carried the same error classes — model-produced pilot assessments got specifics wrong and assessed the wrong artefact or version (2026-10-03)

*(Approved by Shawn 2026-10-03; extends Observation 31, class 9.)*

### Context

The E8-v2 reference re-derivation re-checks every old E8 reference item
against primary sources: the paper, its supplement, the deposit, and
registry APIs. The old E8 scores and evidence strings are the pilot FAIR
assessments inside the pilot extraction records (under
`studies/open-science-compliance/outputs/`), each produced by a model
extractor: "Claude Opus 4.5" (`dye-et-al-2023/extraction.json:5`;
`marwick-2025/extraction.json:4`), "claude-opus-4-5"
(`herskind-riede-2024/extraction.json:2230`), and
"claude-opus-4-5-20251101" (`key-et-al-2024/extraction.json:2565`).
After Sitting 8, 120 of the 150 items (five papers × two sections × 15
sub-principles) have been re-derived; crema-et-al-2024's two sections
remain.

### Observation

The sittings surfaced three kinds of defect. Counts are floors: they are
what item-by-item adjudication met, not a systematic audit of all 150
evidence strings.

1. **Wrong specifics:** the evidence string asserts something the
   primary source contradicts. At least nine items:
   - herskind data F2, "Zenodo provides structured DataCite metadata
     (authors, description, keywords)": both versions have an empty
     description and no keywords (Sitting 3);
   - herskind data I3, "References source catalogue via DOI …": Płonka
     (2003) has no persistent identifier, and neither deposit version
     carries any related identifier (Sitting 3);
   - herskind data R1.1, "No explicit licence stated … in Zenodo record
     or paper": both versions are CC-BY-4.0, the article CC BY
     (Sitting 3);
   - herskind data R1, "Zenodo metadata includes authors, methods
     description, data source": the description is empty; the score
     stands on a corrected basis (Sitting 3);
   - key data F1, "supplementary data accessible via paper DOI": the
     supplement holds no data (Sitting 5);
   - key data I1, "CSV supplementary tables in structured format": the
     only CSV, `mmc4.csv`, is a 75-byte header-only template (Sitting 5);
   - key code R1.2, "No version info …": the paper states R 4.3.0
     (Sitting 6);
   - marwick data F2, "… description, keywords": no keywords, and the
     description is a single sentence citing the paper (Sitting 7);
   - marwick data I3, "DOI links to paper and related resources": the
     record's only typed relation is `isSupplementTo` a GitHub tree URL
     (Sitting 7).

   Eight of the nine changed score at re-derivation. Outside the item
   evidence the same kind appears twice more: herskind's
   data-completeness notes describe "lithic measurements, use-wear
   images", which are not in the paper (Sitting 3;
   `herskind-riede-2024/extraction.json:2225`), and marwick's carried
   10.5281/zenodo.14561925, which the paper never cites, through to
   lodged amendment 2 §2 (erratum-log Entry 4).
2. **Wrong artefact assessed.** dye code: Sitting 2 counts 14 of the 15
   old scores as citing ArchaeoPhases/CRAN evidence, the dependency,
   rather than the supplement's own OxCal and R scripts (12 strings name
   the package, CRAN, or its DESCRIPTION outright; the rest are
   generic). Re-derived on the principal scripts, code_fair went 14 → 8.
3. **Wrong version assessed, relative to AP-12.** herskind code R1 and
   R1.2 (both 0→1) described Zenodo v1, whose S2.R has 451 lines and no
   README or version information, not the v2 that the published
   supplement matches byte for byte (Sitting 4). marwick code R1.2's
   "renv lockfile pins 169 packages" matches main's post-publication
   `renv.lock` (169), not v1.3's (152): a version error, not a miscount
   (Sitting 8, clarified 2026-10-03); the score stays 1.

The kinds differ in how far they depend on later rules. Kind 1 strings
are false under any reading of the instrument. Kind 2 rests partly on
the instrument: Entry 3's first root cause was that v2.0 left the
assessment target undefined, and the rule that the paper's own scripts
are always principal arrived with amendment 2. Kind 3 is defined by
AP-12 (ruled 2026-10-02).

### Implication

First, the 2026-08-03 benchmark's concordance figures (0.773 sonnet-5,
0.807 opus-5, 0.820 fable-5, all below the 0.90 gate; erratum-log Entry
3) were measured against this reference, so some recorded arm
disagreements were reference errors. herskind data I3 is the clean
case: the old reference scored 1, all nine runs in that cycle scored 0,
all nine v2.1 runs scored 0, and the re-derivation rules 0 — the arms
were right. key code F1 is the case the v2.1 cycle would have
miscounted: the old reference scored 0 and all nine v2.1 runs scored 1,
which the re-derivation upholds; that cycle's disputed-items list
records it as a majority-vs-reference mismatch, though the cycle
deliberately computed no concordance against the retired reference (in
the 2026-08-03 cycle, under v2.0, the arm majorities had matched the
old 0). The 2026-08-03 summary already discounted concordance for one
known gap, a reproduction-informed reference against paper-only arms;
reference error is a second, and removing it is what E8-v2 is for.
Second, item-level primary-source verification of each evidence string
is what caught these; a model-produced reference dataset needs the same
mechanical verification as any other model output (Observation 31 class
9; erratum-log Entry 4; the registrant's 2026-10-03 direction to verify
mechanically wherever possible). Third, gate statistics inherit
reference quality: the reference is part of the measurement apparatus.
Relations: Observation 31 (class 9, extended here from the extraction
records to the reference dataset built from them); Observation 4
(subagent-relayed specifics ran ~1 in 10 wrong; the counts here are
floors from adjudication, not a sampled rate); Observation 13
(verification ledgers drift from their sources; a reference dataset is
a ledger of the same kind, and item-level re-checking is what reconciles
it); Observation 15 (reliability-gate statistics are
decision-relevantly sensitive to design choices; reference quality is
one more). Anchors:
`studies/open-science-compliance/outputs/validation/e8-v2-rederivation/adjudication-log.md`
Sittings 2–8 and AP-12; erratum-log Entries 3 and 4; the
`benchmark-summary.md` and `disputed-items.json` of the sibling
`benchmark-2026-08/` and `benchmark-2026-08-17/` cycles (the latter
computed no concordance); the four pilot extraction records.

## Observation 33: Resolution is not verification — an identifier or version is verified only when it resolves to the expected target (2026-10-03)

*(Approved by Shawn 2026-10-03; drafted during the E8-v2 reference adjudication.)*

### Context

The E8-v2 reference re-derivation checks identifiers and versions against
primary sources, and the registrant's 2026-10-03 direction is to verify
mechanically wherever possible. The plan's pre-census item
(`wiki/planning/instrument-clarification-plan.md`, "Mechanical
verification") asks for a deterministic identifier check before every
harvest. The obvious mechanical check is resolution: does the DOI
resolve? Three cases show that it is not enough. In the registrant's
words, "*correct* resolution to the *expected target* is verification".

### Observation

1. **Resolves, wrong target.** herskind-riede-2024's pilot extraction
   calls the paper an "Experimental replication study with all data in
   two Zenodo deposits (10.5281/zenodo.10023618,
   10.5281/zenodo.10027675)"
   (`studies/open-science-compliance/outputs/herskind-riede-2024/extraction.json:2217`,
   `data_completeness.assessment_scope_rationale`). The paper cites
   neither; its deposits are Zenodo records 10623550 (v1) and 10801706
   (v2). Both DOIs resolve, to real but unrelated records published
   2023-10-20: "heplersa/USDMdata: Discretized US Drought Data to
   Support Statistical Modeling" and "PalMuc/CalciteSea: archive for
   Zenodo" (Zenodo API, re-checked 2026-10-03). A resolution check
   passes both (adjudication log, Sitting 3 addendum).
2. **Does not resolve, never cited.** marwick-2025's pilot extraction
   carried 10.5281/zenodo.14561925, which neither the version of record
   nor the preprint cites (the paper cites the concept DOI
   10.5281/zenodo.14897252) and which resolves nowhere (doi.org and the
   Zenodo API both return 404, re-checked 2026-10-03). It reached lodged
   amendment 2 §2 as a dead-link precedent
   (`studies/open-science-compliance/prereg/erratum-log.md` Entry 4). A
   resolution check did flag it, but misread it: as the paper's dead
   link, not the extractor's invention. Cases 1 and 2 are caught only by
   checking against the paper's own text.
3. **Version resolves, wrong target.** crema-et-al-2024 cites the
   concept DOI 10.5281/zenodo.10782942 (§4, Materials and methods),
   which resolves to the latest version, v2.0.0
   (10.5281/zenodo.10816946, published 2024-03-14). AP-12's date rule
   (rule 3: the latest version on or before the article's first online
   appearance, here 16 March 2024; Crossref carries no
   `published-online`, and its `created` date agrees) also selects
   v2.0.0. But the published Table 1 (all eight medians, eight 90 %
   highest posterior density (HPD) intervals, and eight Rhat values)
   matches `figures_and_tables/table1.csv` in v1.0.0
   (10.5281/zenodo.10782943, published 2024-03-05) exactly, and 18 of
   v2.0.0's 24 values differ (e.g. Japan r 0.1023 against 0.1003, Japan
   μ 0.703 against 0.701). v2.0.0 re-ran the model: every
   `results/*.RData` file and `table1.csv` change between the tags
   (commit `b1bd710`, "Updated everything after final check",
   2024-03-13). Both versions post-date acceptance (29 February 2024)
   and pre-date first appearance, so dates cannot decide. Source: the
   clerk's 2026-10-03 comparison through the GitHub API (repository
   ercrema/diffusionCurve, tags v1.0.0 and v2.0.0) against the paper's
   PDF text, re-derived the same day by the Observation writer, who also
   confirmed that the `table1.csv` inside each Zenodo archive is
   byte-identical to its tag's (SHA-256 `70316f98…` for v1.0.0,
   `2d2e7566…` for v2.0.0).

### Implication

Verification is resolution **plus** a match to the expected target. For
an identifier, the target is the registry record's title, creators, and
stated relationship to the paper, all checkable through registry APIs;
herskind's two DOIs fail on title and creators at once. Stated
relationships are often missing (Observation 31, class 5: herskind's
genuine deposits carry no related identifier), so title and creators
often carry the test alone. For a version, the target is a checksum
match against the published supplement (AP-12 rule 1) or a match to
values printed in the paper, as in case 3. Both are largely mechanical,
so the pre-census identifier check should be built this way: presence
in the paper's text first (the plan's design lesson), then resolution,
then a target match. A resolution-only check would have passed case 1,
misread case 2, and confirmed the wrong version in case 3. Resolution is
weak evidence in a densely allocated namespace: a plausible-looking
Zenodo number may well land on someone's record. The registrant's
version rule follows the same logic (being refined in the adjudication
log's AP-12): score and reproduce the version the paper cites, always
run the checks, and treat a cited version that fails them as a
correction finding; a missing version should be flagged. crema is the
case the refinement has to handle: its concept DOI names no version, and
only the printed values identify v1.0.0. Relations: Observation 19 (a
version number without a recorded referent can only be compared, not
checked; a DOI that resolves has been compared with a registry, not
checked against its referent); Observation 13 (verification ledgers
drift from their sources; a resolution pass never consults the source);
Observation 31 (the noisy surface: cases 1 and 2 are class 9 errors,
identifiers in model-produced records, and case 3 is a class 3 version
problem in the research record itself); Observation 32 (the old
reference carried the same error classes; its kind 3, wrong version
assessed, can arise from following the citation itself). Anchors:
`studies/open-science-compliance/outputs/validation/e8-v2-rederivation/adjudication-log.md`
Sitting 3 addendum and AP-12; erratum-log Entry 4; the plan's pre-census
"Mechanical verification" item; `corpus/store/crema-et-al-2024/extracted.txt`
lines 75–76 (dates) and 433–434 (concept DOI); Zenodo records 10023618,
10027675, 10782943, and 10816946; ercrema/diffusionCurve tags v1.0.0 and
v2.0.0.

## Observation 34: Within-tier succession — Opus 5.5 matched or beat Opus 5 on every gate at about half the cost, and effort was not the lever (2026-10-04)

*(Approved by Shawn 2026-10-04; drafted in session c5ee7a27, and folds in a corrected WN-ae.)*

### Context

Opus 5.5 (`claude-opus-5-5`) arrived while the registered model pin was
`claude-opus-5`. The design note
(`studies/open-science-compliance/outputs/validation/opus-5-5-arms-2026-10/design-note.md`)
specified three 15-spawn arms at medium, high, and xhigh effort, judged by
the two registered gates and the pre-declared cheapest-eligible rule. Both
gates need at least 0.90: stability, and concordance with the
beyond-instrument (BI) items excluded, on the ruled majority-vote reading.

### Observation

**Gates.** Every Opus 5.5 arm clears both, and the analysis tool and the
blinded H13 script agree on every figure.

| Arm | Stability | Concordance, BI excluded |
|---|---|---|
| opus-5-5 medium | 143/150 = 0.953 | 131/141 = 0.929 |
| opus-5-5 high | 143/150 = 0.953 | 130/141 = 0.922 |
| opus-5-5 xhigh | 145/150 = 0.967 | 130/141 = 0.922 |
| opus-5 high (registered) | 143/150 = 0.953 | 127/141 = 0.901 |
| opus-5 xhigh (registered) | 143/150 = 0.953 | 130/141 = 0.922 |

Under the strict four-way-unanimity reading the Opus 5.5 arms still clear
(0.901–0.908), and neither opus-5 arm does (0.879 high, 0.894 xhigh).

**Cost** (scoring spawns only, 15 per arm; `selection-cost.json`):

| Configuration | Cost recorded / central | Median spawn | Requests | Cache reads |
|---|---|---|---|---|
| opus-5-5 medium | $8.70 / $9.25 | 88 s | 49 | 1.58M |
| opus-5 high | $17.27 / $20.40 | 286 s | 97 | 4.41M |

**Effort was not the lever for accuracy.** On majority vote over the 141
gate items, the three Opus 5.5 efforts differ on only 3. Crema code I3 is a
2–1 split at every effort (a miss at medium and high, correct at xhigh).
Crema code R1.3 is over-credited at high and xhigh and correct at medium.
Herskind code R1.3 is over-credited at xhigh only (high is a 2–1 split the
right way). Nine misses are shared by all three efforts, and six of them are
F2 over-credits (crema, herskind, and marwick; data and code) that every
opus-5 run makes identically. The residual error is instrument-shaped.

**Effort did drive cost (the corrected WN-ae).** Recorded output tokens
were 114,502, 152,775, and 479,726 (medium, high, xhigh), costing $8.70,
$9.55, and $16.33. Cache writes are an effort-independent floor of about
$6.1 per arm. The earlier claim (WN-ae) that opus-5 high was about 11%
cheaper than xhigh is **not robust**: register F-019's output under-count
narrows it to about 2% at the central estimate ($20.40 against $20.85) and
reverses it at the upper bound ($22.88 against $22.48).

Shawn confirmed `claude-opus-5-5` at effort medium on 2026-10-04.

### Implication

1. Re-benchmarking on succession pays. Gates plus cost turned adoption
   into a rule application rather than a judgement, and a registered model
   pin ages within weeks.
2. Measure the effort default rather than presume it. Medium, Opus 5.5's
   API default, was the cheapest arm with no measurable loss.
3. The residual errors are F2-shaped, so the next accuracy gain is
   instrument clarification or mechanical rules
   (`wiki/planning/deterministic-output-checks.md`), not model or effort.

**Caveat.** The agreement gains over opus-5 are 0–4 items of 141, well
inside Observation 15's ~±0.09 between-configuration interval. The
defensible claim is "at least as good, at about half the price and a third
of the time", not "more accurate". Medium's cost bound is robust to F-019
(its upper bound, $9.37, is below high's recorded $9.55).

Relations: Observation 15 (reliability-gate sensitivity: the ±0.09
interval and the gates-plus-cost rule this selection applied); Observation
27 (effort pins artefact-derived: output and wall-clock rose monotonically
with effort, consistent with the pins); Observation 28 (spend metric
dominated by effort-independent components: the cache-write floor recurs);
Observation 29 (harness part of the apparatus: F-019 bounds the cost leg);
Observation 33 (mechanical verification: the F2 rule is a candidate).
Anchors:
`studies/open-science-compliance/outputs/validation/opus-5-5-arms-2026-10/results-2026-10-04.md`,
`selection-cost.json`, `h13/h13-results.json`, and
`concordance/bi-excluded/summary.json` in the same directory; arm commits
`2c93a5d` (high), `656036f` (medium), `7365e14` (xhigh); results commit
`31cdc85`;
`studies/open-science-compliance/outputs/validation/failure-modes/register.md`
F-019.

## Observation 35: A wired, tested control is aspirational until its log shows a real pass (2026-10-04)

*(Approved by Shawn 2026-10-04; WN-l, drafted 2026-08-03.)*

### Context

The receipt gate (a SubagentStop hook that checks each scoring spawn's
receipt) was designed, wired, and build-tested before the 2026-08-03
benchmark. Its log is `.claude/hooks/receipt-gate-log.jsonl`. The run
records of the three 2026-08-03 arms carry its tallies, and register F-007
summarises them.

### Observation

The gate's log carried only blocks: it had never validated one production
receipt. The run it nominally guarded was protected entirely by
orchestrator-side post-hoc verification. The first arm to run under the
repaired gate (`3b01676`) logged 6 passes and 9 blocks, and the gate blocked
those 9 of 15 spawns for a reason its own log cannot distinguish from a
true catch. The opus arm blocked every spawn once, because the
final-message JSON check cannot see a tool-call structured output. F-007
counts 39 of 45 spawns blocked across the three arms, with no consequence
from any block. A control that was wired, tested, and logging was therefore not
operative.

### Implication

A control's operative status is evidenced by logged passes on real traffic
plus one observed catch, not by wiring, tests, or the existence of its log
file. Before relying on a gate, read its log for a real pass and a real
catch, and ask what the log would look like if the gate were inert. This is
the companion rule to Observation 14 (a canary probe beats documentation:
the log is the probe) and Observation 16 (a green check over a narrower
scope than its readers assume). Observation 23 supplies the mechanism here:
the verifier did not model the delivery path its subject rode on. Sources:
`receipt_gate_note` and `gate_events` in the `run-record.json` files under
`studies/open-science-compliance/outputs/validation/benchmark-2026-08/`
(`arm-fable-5` and `arm-opus-5`); register F-007 in
`studies/open-science-compliance/outputs/validation/failure-modes/register.md`.

## Observation 36: Within-model run disagreement is a rubric-ambiguity locator (2026-10-04)

*(Approved by Shawn 2026-10-04; WN-m, drafted 2026-08-03, with 2026-10-04 corroboration.)*

### Context

Each validation arm scores the five pilot papers three times (15 spawns),
and the analysis tool lists the items on which the three runs disagree.
That list says where the model is unsure of the instrument, independent of
whether the reference is right.

### Observation

Across the three 2026-08-03 arms, run-to-run disagreement concentrated on
the same five instrument clauses (A1.2, R1.1, A2, R1.3, and F-block
upstream crediting), and the most capable model was not the most stable.
Three runs of a single cheap model would have located the same clauses as
the full cross-model benchmark, which is a diagnostic costing about $3 on
the candidate's estimate (not re-derived here).

**2026-10-04 corroboration, stated honestly.** The Opus 5.5 medium arm
(143/150 stable) disagreed on seven items
(`opus-5-5-arms-2026-10/h13/h13-results.json`, `non_unanimous_items`): crema
code I3, dye code R1.1, dye data R1.1, herskind data A1, key code R1, key
code R1.2, and marwick data I1. Two points overlap the 2026-08-03 clause
list: R1.1 (two of the seven) and the A1 family (herskind data A1). The
rest do not: I3, I1, R1, and R1.2 were not on that list. Conversely, A2,
A1.2, R1.3, and F-block crediting were fully stable at medium (their
sub-principle stability is 1). So a single arm on a newer model locates
some, not all, of the earlier clauses and adds others. The corroboration is
partial, and the new items are small in number (7 of 150).

### Implication

Run disagreement locates ambiguity cheaply, but one arm's list is a sample,
not the clause set: it shifts with the model, and the older "same five
clauses" finding should be read as stable only across the three models
tested then. Use repeated runs of one cheap model as the first diagnostic
for instrument clarification, and pool lists across models before treating
a clause as unambiguous. The error side tells a different story, because
the systematic misses (F2 over-credit) are unanimous and so invisible to
this locator (Observation 34). Relations: Observation 15 (statistics
depend on design choices); Observation 34 (the Opus 5.5 arms). Sources:
per-arm stability disagreement lists in the 2026-08-03 run records; the
Opus 5.5 medium arm's `h13/h13-results.json`.

## Observation 37: Hook-time gate decisions are advisory in the workflow lane, and a receipt check must verify success, not attempts (2026-10-04)

*(Approved by Shawn 2026-10-04; WN-p and WN-r, held over from the 2026-08-15 session, with 2026-10-04 corroboration.)*

### Context

The validation arms run as workflow spawns. A SubagentStop hook (the
receipt gate) can block a spawn at the moment it finishes, and a separate
post-hoc reconciler (reconcile-run, the C8 and C9 builds) re-checks every
completed transcript. Two held-over candidates concern how much each layer
can be trusted: WN-p on the hook, and WN-r on what a receipt check should
count.

### Observation

**WN-p, the hook is advisory.** In the workflow lane a gate's block does not
stop collection: probe C collected a spawn's output despite a block. Hook-time
decisions also read the transcript before it is fully written, so the
2026-08-03 benchmark logged 39 lag false alarms in 45 spawns (register
F-007). The post-hoc pass over completed artefacts then retro-validated
all 45 clean. Authoritative verification therefore has to run post-hoc on
completed artefacts, and the live gate is a signal.

**WN-r, count success, not attempts.** A declared pull whose every Read
errored never entered the spawn's context (the dye sonnet guideless spawn),
yet an attempt-counting check would credit it. The rule is now in the gate
and the reconciler. F-010 applies the same logic to enumerations: judge the
paths returned, and treat an errored or empty enumeration as at most an
attempt.

**2026-10-04 corroboration.** In the three Opus 5.5 arms, four of 45 scoring
spawns logged a SubagentStop `block` ("no structured output found") with
output present (`blocked_but_output_present`): `a4ae6a0c3df878505` and
`aaf0570ecf3124fd2` in the high arm, and `aa1ee7a17cd1419c0` and
`aa1f898ffa100802c` in the xhigh arm. The medium arm's gate events were all
`pass`. The authoritative post-hoc reconciliation passed all 45 spawns
(each arm's `reconciliation/reconciliation-report.json`: 15 spawns, 15
reconciled, `clean: true`).

### Implication

Design the operative control as a post-hoc check on completed artefacts,
and keep the live hook as an early warning that is allowed to be wrong in
both directions. Define every receipt check over outcomes (content that
arrived), never over actions taken. A block with output present is the
expected signature of the advisory lane, not an incident. Relations:
Observation 35 (a gate is operative only if its log
shows passes and catches: the same lesson from the other side);
Observation 23 (a verifier must model its delivery mechanism). Anchors:
register F-007 and F-010 in
`studies/open-science-compliance/outputs/validation/failure-modes/register.md`;
`arm-opus-5-5-high/run-notes.md` and `arm-opus-5-5-xhigh/run-notes.md`
under `opus-5-5-arms-2026-10/` in the same validation directory; the
held-over candidates in `wiki/continuity.md` (2026-08-15 session entry).

## Observation 38: Platform by-construction entitlements are presence floors, not choice floors, and the floors are empirical claims (2026-10-04)

*(Approved by Shawn 2026-10-04; WN-q, held over from the 2026-08-15 session.)*

### Context

The platform-rows table lists what each repository guarantees by
construction (a licence value, a persistent identifier, metadata
accessibility after withdrawal), so that the census can credit a deposit
for what the platform enforces. On 2026-08-15 each row was verified
against primary sources
(`studies/open-science-compliance/outputs/validation/platform-rows-2026-08-15/verification-note.md`).
Every row verdict was "holds with caveat".

### Observation

1. **A presence floor is not a choice floor.** Zenodo pre-fills the licence
   field with CC-BY-4.0, so a depositor who never touches it publishes a
   record that looks exactly like a deliberate election. In the 298 newest
   records sampled on 2026-08-15, 246 (82.6%) carry `cc-by-4.0`. DANS
   pre-fills CC0 1.0. CRAN is the contrast: its licence field has no
   default value, so a licence there is evidence of a decision.
2. **A floor is an empirical claim, and one was contradicted.** The table
   asserted that DataCite metadata "remains accessible even if the resource
   goes away". DataCite's own tombstone page says it provides no tombstone
   pages automatically, and its prescribed workflow sets the DOI to
   `Registered`, which withdraws the record from the Public API. A
   harvester cannot tell "tombstoned" from "never existed". Zenodo, by
   contrast, commits to a tombstone page and retained record, which is
   stronger than the table credited.
3. **Floors differ within a row.** ADS, tDAR, and DANS enforce different
   things (ADS a mandatory validated template; DANS a small generic core
   with the archaeology vocabulary optional), and 32 of 298 sampled Zenodo
   records (10.7%) carry no description at all.

### Implication

Credit a platform entitlement only after checking it against the platform's
own documentation and a sample of its records, and record the date. A
default value is a presence floor: a licence-presence score at Zenodo or
DANS is dominated by form defaults, so it needs its own column or footnote
rather than counting as author intent. The dated verification note is the
committed form of that check. Relations: Observation 30 (licence conflicts
are the norm: the defaults here sit beneath those conflicts, and a clarity
test such as AP-8 reads a default as a published licence); Observation 31
(the noisy surface); Observation 13 (ledgers drift from their sources: so do
platform claims). Anchors: `verification-note.md` and
`enrichment-addendum-2026-08-15.md` in the platform-rows directory above;
the WN-q entry in `wiki/continuity.md` (2026-08-15 session).

## Observation 39: Apparatus evolution silently vacates derived statistics, and the A3 promotion consumed its own evidence base (2026-10-04)

*(Approved by Shawn 2026-10-04; WN-y and WN-z, held over from the 2026-08-19 session, with 2026-10-04 corroboration.)*

### Context

Observation 22 recorded a within-sonnet correlation between guideless
spawns (spawns that never read the principles guide) and minority votes:
17 of 29 splits, against about 11.3 expected. The analysis tool
(`studies/open-science-compliance/protocol/validation/analyse-benchmark-disagreements.py`)
re-checks that correlation per arm. On 2026-08-15 the guide moved from
pull-on-demand to push delivery (the A3 promotion), after which a spawn's
receipts no longer show a pull.

### Observation

**WN-y, the predicate went vacuous.** The detector was pull-era: it looked
for the guide in `pulled_files_read`. After A3 the guide is receipted under
`instrument_receipts`, so the detector reported every one of the 90 spawns
in the 2026-08-17 cycles as guideless. The statistic still computed and
printed, with no error. The fix was two-era detection in the same commit
(the docstring of `pulled_guide()` states both eras). Derived statistics
need explicit two-era semantics whenever the apparatus that feeds them
changes.

**WN-z, the promotion consumed its own evidence base.** After A3, a
guideless spawn cannot exist, so the treatment group of the guideless-minority
correlation is empty. The correlation is therefore era-bound and frozen at
the old-cycle n. Re-testing it would be a deliberate ablation (withholding
the guide again), not a re-analysis.

**2026-10-04 corroboration.** The corrected tool, run over all nine arms
(including the three Opus 5.5 arms) with the BI items excluded, reports
`guideless spawns []` and zero minority votes from a guideless spawn in
every arm. That is the correct post-A3 answer, and it shows the statistic is
still structurally unmeasurable: a zero here is "no treatment group", not
"no effect".

### Implication

When an apparatus change alters what a field means, every statistic derived
from the field must be re-audited, because the failure mode is a plausible
number, not an error. Report a derived statistic together with the era it
is valid for, and treat a zero from a structurally empty group as
non-evidence. Relations: Observation 22 (the original correlation and the
premise test); Observation 29 (the harness is part of the measurement
apparatus: so is the instrument delivery path); Observation 42 (usage
accounting errs in both directions: the same family of silent measurement
drift). Anchors: the analysis tool above (`pulled_guide()`, and the
per-arm guideless report around line 407); the WN-y and WN-z entry in
`wiki/continuity.md` (2026-08-19 session); the nine-arm run reproduced on
2026-10-04 from the invocation in
`studies/open-science-compliance/outputs/validation/opus-5-5-arms-2026-10/results-2026-10-04.md`.

## Observation 40: A coverage denominator moves with ruling wording and run-to-run variation (2026-10-04)

*(Approved by Shawn 2026-10-04; WN-aa, drafted in the 2026-10-03 shakedown session.)*

### Context

The Phase 2 shakedown (an agentic reproduction lane run on herskind-riede-2024
and dye-et-al-2023) has planners enumerate every reproduction target per
paper, and coverage (targets computed over targets planned) is the
preregistered Hypothesis 2 (H2) outcome. The first plan round was superseded
and re-run with four registrant rulings (R1 to R4) written into
`run-config.yaml` (`phase2-shakedown/deviations.md`, D2).

### Observation

The same planner configuration enumerated dye at 23 targets in round 1 and
34 in round 2, and herskind at 14 and 15. Part of the dye jump is wording:
R3 ("one target per display item") introduced the Supplement section 10
text restatements of Tables 2 to 10 (T24 to T32), and R1 admitted Figs 2
and 6 tested with verification aids. Round 1 had excluded all of these. The
rounds also differ by run-to-run variation, and the two causes cannot be
separated from this design (deviations.md, D3, "Finding: denominator
instability"). Coverage then reads 25/34 = 0.735 for dye and, after the
herskind T11 completion, 11/15 = 0.733 for herskind
(`results-2026-10-03.md`). Had the denominator stayed at 23, dye's figure
would be a different number for the same underlying work.

### Implication

Coverage is only as stable as its denominator, and the denominator is the
planner's enumeration, which moves with wording and between runs. At census
scale a denominator that shifts by about a third is a risk to H2. The
proposed safeguard is two independent planners per paper, with a reconciled
union presented at plan approval; R3's treatment of restatements is to be
settled before the census. Relations: Observation 20 (an enumeration is a
finding, not a fact: here the enumeration is the denominator); Observation
15 (statistics are sensitive to design choices). Anchors:
`studies/open-science-compliance/outputs/validation/phase2-shakedown/deviations.md`
(D1 to D3) and `results-2026-10-03.md`; the WN-aa entry in
`wiki/continuity.md` (2026-10-04 session).

## Observation 41: A regression against a human-directed baseline also audits the baseline (2026-10-04)

*(Approved by Shawn 2026-10-04; WN-ab, drafted in the 2026-10-03 shakedown session.)*

### Context

The shakedown's regression criterion compares an unattended agentic
reproduction (attempt-02) with the human-directed pilot reproduction
(attempt-01) of the same two papers. The criterion's subject is the harness,
and the pilot is treated as the baseline.

### Observation

Every value both attempts computed was identical: herskind 1,601 n-gram
cells plus the Table 1 counts, dye 54 Supplement-table cells plus the
12-cell section-7 matrix (`phase2-shakedown/results-2026-10-03.md`,
Headline). The baseline was nonetheless audited. The agentic run flagged
errors the pilot had missed or absorbed:

- **Dye p. 16.** The paper prints 0.87 for BE1-Cowrie to BE1-Disc. The
  authors' code on the published data gives 0.99967, and 0.87 is the
  Amethyst to Disc cell (0.86717). The pilot's comparison table listed
  "Published 0.87" against Amethyst to Disc, which the text does not say,
  so it re-mapped the paper's misattribution. Attempt-02 flagged it, and
  Shawn's version-of-record check on 2026-10-04 confirmed PAPER_ERROR.
- **Herskind Table 1.** The pilot's report tabulates the frequency counts
  as "Table 1 Equivalent" and records no comparison with the printed table
  (`herskind-riede-2024/reproduction/attempt-01/comparisons/comparison-report.md`).
  Attempt-02 found 8 of 130 cells one higher than the authors' data (four
  paired shifts), and ruled PAPER_ERROR.

The ruling record lists every difference from the pilot as explained: the
pilot over-credited its own T02 repair, absorbed the T06 paper error by
re-mapping, and the remaining differences are scope expansion.

### Implication

Identical numbers do not show that the baseline was right: a baseline can
agree with a reproduction that inherits its blind spots, and a strict
independent run is the cheapest audit of it. Treat a regression run as
two-way, and expect the baseline's own errors to surface as the "new"
discrepancies. Relations: Observation 32 (the old pilot assessments carried
the same error classes, including specifics got wrong); Observation 13
(ledgers drift from their sources). Anchors:
`studies/open-science-compliance/outputs/validation/phase2-shakedown/results-2026-10-03.md`
(Headline; T06 and Rulings 2, 3, 7); the WN-ab entry in `wiki/continuity.md`.

## Observation 42: Transcript token accounting errs in both directions, so cost is reported with bounds (2026-10-04)

*(Approved by Shawn 2026-10-04; WN-ac with register F-019.)*

### Context

Every cost, spend-wire, and selection-price figure in the validation work is
computed from harness transcripts. The harness writes one transcript entry
per content block (thinking, text, tool use), and the arm assembler and
`selection-cost.py` derive tokens from those entries. Two register entries
show that this source is wrong in opposite directions.

### Observation

**WN-ac and F-013: over-count.** The harness repeats a response's whole
`usage` on every content block, so a per-entry sum counts each request's
input and cache tokens once per block. Against per-request counts the
recorded contract-metric tokens were inflated 1.90 to 2.63 times in the six
recorded arms, and 2.37 to 2.93 in the 2026-08-03 arms recomputed from their
run directories. The inflation is model-dependent (Sonnet lowest, Fable
highest), so cross-model cost comparisons on the per-entry metric were
biased against Opus and Fable.

**F-019: under-count.** The fix (the per-request counter taking each
field's maximum within a request) introduces the opposite error. In some
requests no entry carries a `stop_reason`: every entry holds the
streaming-start snapshot, and `output_tokens` is a placeholder (2 to 16,
typically 8). Input and cache fields are unaffected. Scoring requests
missing a final entry, by arm: opus-5 xhigh 7 of 94; opus-5 high 21 of 97;
opus-5-5 high 6 of 55; medium 7 of 49; xhigh 4 of 69. On Claude Code 2.1.289
the Haiku reconciliation spawns lose 87 to 89 of 113 to 118 requests.

**Effect on the 2026-10-04 D4 record.** The gates ruling found opus-5 `high`
"about 11% cheaper" than `xhigh` ($17.27 against $19.46, recorded). Imputing
the missing requests narrows that to about 2% at the central estimate
($20.40 against $20.85) and reverses it at the upper bound ($22.88 against
$22.48). The Opus 5.5 choice survives: medium's upper bound ($9.37) is below
high's recorded lower bound ($9.55). A note to this effect was added to the
ruling record at Shawn's direction.

### Implication

The measurement apparatus is part of the instrument, and fixing one
accounting error can expose the next. Report every cost with bounds
(`recorded` as the lower bound, plus `central` and `upper` imputations),
never the recorded figure alone, and test whether a ranking survives the
bounds before relying on it. For the census, capture usage from a source
that records final usage rather than from transcripts alone (F-019 ruling,
items 1 and 3). Relations: Observation 28 (a spend metric dominated by
effort-independent components: the over-count compounded this);
Observation 29 (harness behaviour is part of the apparatus); Observation 34
(the corrected effort-to-cost claim); Observation 39 (the same family of
silent measurement drift). Anchors: register F-013 and F-019 in
`studies/open-science-compliance/outputs/validation/failure-modes/register.md`;
`opus-5-5-arms-2026-10/selection-cost.py` and `selection-cost.json`;
`gates-ruling-2026-10-04/ruling.md` (the F-019 note); the WN-ac entry in
`wiki/continuity.md`.

## Observation 43: An operationalisation choice can decide a gate, so fix it in registered text, not in code (2026-10-04)

*(Approved by Shawn 2026-10-04; WN-ad, with 2026-10-04 corroboration.)*

### Context

Amendment 1 section 3 sets "a concordance floor of at least 0.90 (same
statistic) against the pilot reference scores". It does not say how three
runs of a spawn meet one reference score. The analysis tool had used the
majority of the three runs (reading C) since 2026-08-03. In the H13 check, a
fresh-context agent blinded from earlier derivations read the registered
text and took four-way unanimity (reading A: all three runs agree and equal
the reference).

### Observation

The computation was never in doubt: H13 reproduced the tool's figures in
all 12 cells under reading C. The disagreement was interpretive, and it
decides eligibility. By the WN-ad account, under reading A no arm is eligible on any choice about
the beyond-instrument (BI) items. Under reading C with BI items excluded,
opus-5 clears. Shawn ruled for C on 2026-10-04 (`gates-ruling-2026-10-04/ruling.md`,
Ruling 1), partly because reading A would penalise instability twice, and
the choice is to be made public in erratum-log Entry 5. No registered text
defined the statistic.

**2026-10-04 corroboration.** The Opus 5.5 arms clear on BI-excluded
concordance under readings A, B (per-run pooled), and C alike
(`opus-5-5-arms-2026-10/h13/h13-results.json`):

| Arm | A, unanimity | B, per-run | C, majority |
|---|---|---|---|
| opus-5-5 medium | 128/141 | 392/423 | 131/141 |
| opus-5-5 high | 127/141 | 389/423 | 130/141 |
| opus-5-5 xhigh | 128/141 | 389/423 | 130/141 |
| opus-5 high | 124/141 | 382/423 | 127/141 |
| opus-5 xhigh | 126/141 | 388/423 | 130/141 |

For the Opus 5.5 arms the choice is therefore not decisive. It decided
opus-5's eligibility, since neither opus-5 arm reaches 0.90 under reading A
(0.879 and 0.894).

### Implication

A statistic named only as "same statistic" is underdetermined, and a
choice that was reasonable when made can still be the choice that decides a
gate. Define the operationalisation in registered text before the data
exist, and report every defensible reading beside the ruled one so that a
reader can see whether the verdict depended on it. Relations: Observation
15 (gate statistics are sensitive to design choices: this is a third
instance, after power and definition). Anchors:
`studies/open-science-compliance/outputs/validation/gates-ruling-2026-10-04/ruling.md`
(Ruling 1);
`studies/open-science-compliance/outputs/validation/h13-rederivation-2026-10-04/operator-comparison.md`;
the WN-ad entry in `wiki/continuity.md`.

## Observation 44: The fail-and-uplift bright line — version pins are routine, code edits are not (2026-10-04)

*(Approved by Shawn 2026-10-04; WN-af, drafted in the 2026-10-03 shakedown session.)*

### Context

The agentic reproduction lane may adapt an environment to a paper's
materials, but not the authors' code. The shakedown's dye-et-al-2023
section-4 analysis failed under ArchaeoPhases 1.8, and the human-directed
pilot had repaired it by shifting column indices. A reviewer hypothesised
that an earlier release would run the code as published.

### Observation

The published code ran on no public release. Every CRAN release with
`read_oxcal()` drops the iteration column with the same line
(`data <- data[, -1]`): 1.5 (2020-12-01), 1.6 (2022-02-17), and 1.8
(2022-06-21); there was no 1.7. The reviewer's hypothesis is false for every
public release, and 1.8 was also current when `beads-1.csv` was dated
(2022-10-20). The pilot's index repair was nonetheless identity-preserving:
the authors' indices `c(3:5, 7, 9, 12:78)` select exactly 72 dates in
raw-CSV numbering, and the pilot's `c(2:4, 6, 8, 11:77)` selects the same 72
after `read_oxcal()` drops two columns. So the shift repairs a defect in the
published code; it does not adapt the code to a changed environment.

Shawn ruled it **fail-and-uplift**: CANNOT_COMPARE stands, the executor's
refusal under its invariant 2 was correct, and the pilot's T02 credit was
too generous. This is the first case of the bright line (shakedown results,
"Candidates for instrument clarification before the registered gate", item (d)): choosing among
publicly available dependency versions is **routine** (pin the release the
materials fit, leave the code unchanged), whereas any edit that changes
logic, indices, or data selection is fail-and-uplift, however obvious the
intent. The recovered-intent evidence goes to the uplift tool.

### Implication

A repair that recovers the authors' evident intent is still a different
analysis, so a reproduction must report it as an uplift, not a pass. The
rule keeps the agentic lane from silently crediting its own fixes, as the
pilot did. It also needs an empirical step before the line is drawn: here,
checking every public release showed that no version pin could have helped.
Relations: Observation 41 (the regression audit that surfaced the pilot's
over-credit); Observation 33 (verification means matching the expected
target; here the check was against every release). Anchors:
`studies/open-science-compliance/outputs/validation/phase2-shakedown/results-2026-10-03.md`
("Rulings (2026-10-04)", ruling 1, and item (d));
`wiki/planning/instrument-clarification-plan.md` (decision log, 2026-10-04);
the WN-af entry in `wiki/continuity.md`.
