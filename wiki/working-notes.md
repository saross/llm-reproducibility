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
