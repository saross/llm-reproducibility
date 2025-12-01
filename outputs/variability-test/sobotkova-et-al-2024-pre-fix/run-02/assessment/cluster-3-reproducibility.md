# Cluster 3: Reproducibility Assessment

**Paper:** sobotkova-et-al-2024
**Assessment Date:** 2025-11-30
**Run:** 02

**Quality State:** HIGH
**Research Approach:** Deductive
**Assessment Pathway:** Standard (computational components)

---

## Signal Score Summary

| Signal | Score | Band | Pathway |
|--------|-------|------|---------|
| Reproducibility | 70 | Good | Standard |

**Cluster Rating:** Adequate

---

## Signal 7: Reproducibility

**Score:** 70/100 (Good)

### Assessment

Good computational reproducibility through three public GitHub repositories. R and Python scripts cover complete analytical pipeline. Main limitation is data access: commercial IKONOS imagery and reference-only field data create barriers. No formal environment specification (requirements.txt, Docker).

### Strengths
- Three public GitHub repositories
- Open scriptable tools (R, Python)
- Well-organised workflow

### Weaknesses
- Commercial satellite imagery not shareable
- No environment specification
- Field data reference-only

### Scoring Rationale

Score of 70 (Good) reflects excellent code sharing but limited data availability and no environment specification.

---

## Reproducibility Readiness

```yaml
reproducibility_readiness:
  inputs_available: "partial"
  code_available: "yes"
  environment_specified: "partial"
  execution_feasibility: "needs_work"
  publication_year: 2024
```

---

## Cluster Synthesis

**Overall Reproducibility:** Adequate

Code infrastructure strong; data access is main limitation.

```yaml
cluster_3_reproducibility:
  reproducibility: {score: 70, band: "good"}
  overall_rating: "adequate"
```
