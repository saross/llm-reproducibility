# Cluster 3: Reproducibility Assessment

**Paper:** sobotkova-et-al-2024
**Assessment Date:** 2025-11-30
**Run:** 05

**Quality State:** HIGH
**Research Approach:** Deductive
**Assessment Pathway:** Standard (computational components)

---

## Signal Score Summary

| Signal | Score | Band | Pathway |
|--------|-------|------|---------|
| Reproducibility | 73 | Good | Standard |

**Cluster Rating:** Adequate

---

## Signal 7: Reproducibility

**Score:** 73/100 (Good)

### Assessment

Good computational reproducibility via three GitHub repositories with complete pipeline. Open-source stack (R, Python, TensorFlow). Clear code organisation. Primary constraint is commercial imagery and reference-only field data. No formal environment specification.

### Strengths
- Three complete public repositories
- Open-source technology
- Clear documentation
- Validation scripts included

### Weaknesses
- Commercial imagery not shareable
- Field data reference-only
- No requirements.txt/Docker
- No explicit dependency versions

### Scoring Rationale

Score of 73 (Good) reflects excellent code availability with data access constraints and partial environment specification.

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

Code infrastructure enables analytical reproducibility; data access is primary limitation.

```yaml
cluster_3_reproducibility:
  reproducibility: {score: 73, band: "good"}
  overall_rating: "adequate"
```
