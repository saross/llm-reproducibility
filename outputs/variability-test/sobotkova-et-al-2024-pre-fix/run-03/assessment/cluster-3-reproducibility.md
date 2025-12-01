# Cluster 3: Reproducibility Assessment

**Paper:** sobotkova-et-al-2024
**Assessment Date:** 2025-11-30
**Run:** 03

**Quality State:** HIGH
**Research Approach:** Deductive
**Assessment Pathway:** Standard (computational components)

---

## Signal Score Summary

| Signal | Score | Band | Pathway |
|--------|-------|------|---------|
| Reproducibility | 71 | Good | Standard |

**Cluster Rating:** Adequate

---

## Signal 7: Reproducibility

**Score:** 71/100 (Good)

### Assessment

Good computational reproducibility through three public GitHub repositories covering the complete analytical pipeline. R and Python scripts enable recreation of training, prediction, and validation workflows. Primary limitation is data access: commercial IKONOS imagery cannot be shared and field data is reference-only. No formal environment specification (requirements.txt, Docker, conda environment).

### Strengths
- Three complete public repositories
- Open-source tools (R, Python, TensorFlow)
- Clear code organisation
- Validation scripts included

### Weaknesses
- Commercial satellite imagery not shareable
- Field data available by reference only
- No environment specification file
- No containerisation

### Scoring Rationale

Score of 71 (Good) reflects excellent code availability but limited data reproducibility and no environment specification.

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

Strong code infrastructure enables analytical reproducibility; data access is the main constraint.

```yaml
cluster_3_reproducibility:
  reproducibility: {score: 71, band: "good"}
  overall_rating: "adequate"
```
