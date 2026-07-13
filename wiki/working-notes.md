---
priority: 3
scope: always
title: "Working Notes"
audience: "researchers"
tags: [research-methodology, llm-craft, open-science]
created: 2026-02-09
updated: 2026-07-06
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
