# Comparison Report

## {Paper Author(s)} {Year} — Reproduction Verdict: {SUCCESSFUL / PARTIAL / FAILED / BLOCKED}

**Paper:** {Full citation}

**Date:** {YYYY-MM-DD}
**Reproduction scope:** {Brief description of what was reproduced and any scope limitations}

---

### Quantitative Results

<!-- For each table or set of results reproduced, create a subsection with a -->
<!-- comparison table. Include ALL values, not just matches. -->

#### {Table/Analysis Description} ({Paper Table/Figure reference})

| {Relation/Variable} | Published | Reproduced | Match |
|----------------------|-----------|------------|-------|
| {item} | {value} | {value} | {EXACT_MATCH / WITHIN_PRECISION / WITHIN_CONFIDENCE / MINOR_DISCREPANCY / MAJOR_DISCREPANCY / CANNOT_COMPARE / PAPER_ERROR} |

<!-- Repeat for each table or analysis -->

**Total quantitative comparisons: {N} values, {M} exact matches ({percentage}%)**

<!-- If stochastic, also report: -->
<!-- "{K} values within published HPD intervals ({percentage}%)" -->

---

### Qualitative Results

<!-- For figures and non-numerical outputs -->

#### {Figure Description} (Paper Figure {N})

- **Figure type:** {statistical plot / map / diagram / composite panel}
- **Data equivalence:** {underlying data verified numerically / visual comparison only}
- **Structural match:** {axes, scales, legends match / differ}
- **Scientific content:** {trends, magnitudes, orderings match / differ}
- **Acceptable differences:** {colour palette, fonts, rendering — if any}
- **Verdict:** {Match / Minor visual differences / Substantive difference}

---

### Methodology

1. **Environment:** {Docker image, key packages}
2. **Data:** {Data source and format}
3. **Analysis:** {Brief description of analysis type — deterministic/stochastic}
4. **Comparison:** {How values were compared — source of reference values}

### Why {Exact Matches Are / Variation Is} Expected

<!-- Explain the determinism/stochasticity of the analysis and why the -->
<!-- observed match level is appropriate -->

### Paper Errors Identified

<!-- Include only if the reproduction detected errors in the published paper. -->
<!-- For each suspected error, document: -->
<!-- 1. The published value and location -->
<!-- 2. The reproduced value -->
<!-- 3. Independent verification (apply the paper's formula to its own tabulated inputs) -->
<!-- 4. Classification: PAPER_ERROR (not MAJOR_DISCREPANCY) -->

### Scope Limitation(s)

<!-- Include only if relevant. Classify each limitation by category: -->
<!-- - Proprietary upstream: depends on commercial software (e.g., OxCal) -->
<!-- - Data unavailability: data cannot be accessed (quantify impact) -->
<!-- - Stochastic non-reproducibility: no set.seed(); results vary between runs -->
<!-- - Publishing error: supplement files empty/corrupted/mislabelled -->
<!-- - Compute constraints: pipeline too expensive for verification scope -->

### Verdict Justification

**{VERDICT}** — {2-3 sentence justification connecting the evidence -->
<!-- (match counts, qualitative results, scope) to the verdict.} -->
