# Cluster 3: Reproducibility Assessment

**Paper:** sobotkova-et-al-2024
**Assessment Date:** 2025-11-30
**Run:** 04

**Quality State:** HIGH
**Research Approach:** Deductive
**Assessment Pathway:** Standard (computational components)

---

## Signal Score Summary

| Signal | Score | Band | Pathway |
|--------|-------|------|---------|
| Reproducibility | 72 | Good | Standard |

**Cluster Rating:** Adequate

---

## Signal 7: Reproducibility

**Score:** 72/100 (Good)

### Assessment

Good computational reproducibility via three public GitHub repositories. Complete analytical pipeline available in R and Python. Open-source tools (TensorFlow, R, Python) enable broad accessibility. Main constraints are data availability (commercial imagery) and lack of formal environment specification.

### Strengths
- Three complete public code repositories
- Open-source technology stack
- Validation scripts included
- Clear code organisation

### Weaknesses
- Commercial IKONOS imagery not shareable
- Field data reference-only
- No requirements.txt or Docker
- No conda environment file

### Scoring Rationale

Score of 72 (Good) reflects strong code availability with data access limitations and partial environment specification.

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

Code enables analytical reproducibility; data access is primary constraint.

```yaml
cluster_3_reproducibility:
  reproducibility: {score: 72, band: "good"}
  overall_rating: "adequate"
```
