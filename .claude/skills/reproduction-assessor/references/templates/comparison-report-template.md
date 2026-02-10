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
| {item} | {value} | {value} | {EXACT_MATCH / WITHIN_PRECISION / WITHIN_CONFIDENCE / MINOR_DISCREPANCY / MAJOR_DISCREPANCY} |

<!-- Repeat for each table or analysis -->

**Total quantitative comparisons: {N} values, {M} exact matches ({percentage}%)**

<!-- If stochastic, also report: -->
<!-- "{K} values within published HPD intervals ({percentage}%)" -->

---

### Qualitative Results

<!-- For figures and non-numerical outputs -->

#### {Figure Description} (Paper Figure {N})

- {Key observation about the reproduced figure}
- {Comparison with published figure}
- {Any notable differences or confirmations}

---

### Methodology

1. **Environment:** {Docker image, key packages}
2. **Data:** {Data source and format}
3. **Analysis:** {Brief description of analysis type — deterministic/stochastic}
4. **Comparison:** {How values were compared — source of reference values}

### Why {Exact Matches Are / Variation Is} Expected

<!-- Explain the determinism/stochasticity of the analysis and why the -->
<!-- observed match level is appropriate -->

### Scope Limitation(s)

<!-- Include only if relevant. Explain what was not reproduced and why. -->
<!-- Frame as documentation, not failure. -->

### Verdict Justification

**{VERDICT}** — {2-3 sentence justification connecting the evidence -->
<!-- (match counts, qualitative results, scope) to the verdict.} -->
