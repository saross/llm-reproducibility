---
priority: 3
scope: always
title: "Working Notes"
audience: "researchers"
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
