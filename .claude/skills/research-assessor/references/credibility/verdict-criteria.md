# Verdict Criteria and Thresholds

**Purpose:** Define consistent verdict assignment based on primary signal performance

**Date:** 2026-01-17

---

## What Verdict Represents

**Verdict reflects primary signal mean**, NOT the aggregate of all seven signals.

**Rationale:** Different research approaches emphasise different signals. A methodological paper should be judged primarily on transparency and reproducibility, not on robustness or generalisability. The aggregate across all seven signals obscures this approach-specific emphasis.

**Formula:**

```
Verdict = f(Primary Signal Mean)
```

Where **Primary Signal Mean** is the arithmetic mean of the 3 primary signals for the paper's research approach.

---

## Primary Signals by Paper Type

| Paper Type | Primary Signals | Rationale |
|------------|-----------------|-----------|
| **Methodological** | Comprehensibility, Transparency, Reproducibility | Method papers must be clear, documented, and reproducible |
| **Meta-research** | Comprehensibility, Transparency, Reproducibility | Same as methodological—analysis transparency paramount |
| **Empirical (deductive)** | Validity, Robustness, Reproducibility | Hypothesis-testing requires evidential rigour |
| **Empirical (inductive)** | Transparency, Comprehensibility, Generalisability | Pattern-finding requires clear documentation |
| **Empirical (abductive)** | Plausibility, Validity, Robustness | Explanatory inference requires theoretical grounding |

---

## Verdict Thresholds

| Primary Signal Mean | Verdict | Description |
|---------------------|---------|-------------|
| ≥85 | **Excellent** | Exemplary primary signal performance |
| 70–84 | **Good** | Strong primary signal performance with minor gaps |
| 55–69 | **Acceptable** | Adequate primary signal performance with notable limitations |
| 40–54 | **Weak** | Significant deficiencies in primary signals |
| <40 | **Very Weak** | Major deficiencies undermining credibility |

---

## Worked Example: Methodological Paper

**Paper:** Dye et al. (2023) - Bayesian Chronology Construction and Substance Time

**Paper type:** Methodological

**Primary signals:** Comprehensibility (88), Transparency (85), Reproducibility (80)

**Primary signal mean:** (88 + 85 + 80) / 3 = **84.3**

**Verdict:** 84.3 falls in 70–84 band → **Good**

---

## Relationship to Aggregate Score

The aggregate score (mean of all 7 signals) is still reported for completeness, but it does NOT determine verdict.

| Metric | Purpose | Location in assessment.json |
|--------|---------|----------------------------|
| Primary signal mean | Determines verdict | `aggregate_scores.primary_signals_mean` |
| Aggregate (all signals) | Overall profile | `aggregate_scores.mean_all_signals` |
| Verdict | Summary judgement | `aggregate_scores.verdict` |

---

## Why Not Aggregate-Based Verdict?

Consider two methodological papers:

| Paper | Comprehensibility | Transparency | Reproducibility | Validity | Robustness | Generalisability | **Aggregate** | **Primary Mean** |
|-------|-------------------|--------------|-----------------|----------|------------|------------------|---------------|------------------|
| A | 90 | 90 | 90 | 60 | 50 | 60 | 73 | 90 |
| B | 70 | 70 | 70 | 80 | 80 | 80 | 75 | 70 |

Paper A has **higher aggregate** (73 vs 75 due to rounding) but Paper B has **lower primary mean** (70 vs 90).

For methodological papers, Paper A is clearly superior—excellent methods documentation and reproducibility, with expected limitations in robustness (methods papers aren't expected to test multiple frameworks).

An aggregate-based verdict would obscure this, potentially rating B higher than A.

---

## Implementation Notes

1. **Calculate primary signal mean** after scoring all 7 signals
2. **Look up verdict** from threshold table
3. **Report both** primary mean and aggregate in `aggregate_scores`
4. **Place verdict** in `aggregate_scores.verdict`

The credibility report should explain the verdict in context:

> "Overall Verdict: Good (primary signal mean 84.3/100). For this methodological paper, primary signals are Comprehensibility, Transparency, and Reproducibility—all scored in the Excellent band (80+). The aggregate of all signals (77.3) is lower due to deemphasised signals like Robustness (58), which is expected for a framework-introducing paper."

---

## Deprecated: "Strong" Verdict

Early assessments inconsistently used "Strong" as a verdict (e.g., key-et-al-2024). This term is deprecated.

**Mapping:**
- "Strong" → "Good" (if primary mean 70–84)
- "Strong" → "Excellent" (if primary mean ≥85)

---

## Related References

- `assessment-frameworks.md` - Signal priority by research approach
- `signal-definitions-hass.md` - Signal definitions with scoring anchors
- `assessment-pillars.md` - Three pillars framework
