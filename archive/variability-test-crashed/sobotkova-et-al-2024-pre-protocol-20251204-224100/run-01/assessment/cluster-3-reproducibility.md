# Cluster 3: Reproducibility Assessment

**Paper:** sobotkova-et-al-2024
**Assessment Date:** 2025-12-01
**Run:** 01

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

Good computational reproducibility through three complete public GitHub repositories covering all analysis stages. Open-source technology stack (R, Python, TensorFlow). Clear code organisation and documentation. Primary constraint is commercial satellite imagery (IKONOS via GeoEye Foundation) which cannot be redistributed. Field data available as reference through published TRAP reports but not as downloadable dataset. No formal environment specification (requirements.txt, Docker, conda environment) limits exact reproduction.

### Analytical Reproducibility Components

| Component | Status | Notes |
|-----------|--------|-------|
| Code availability | Complete | Three public repositories |
| Technology stack | Open-source | R, Python, TensorFlow 2 |
| Data availability | Partial | Commercial imagery restricted |
| Environment specification | Partial | No requirements.txt/Docker |
| Workflow documentation | Good | Steps described in paper |

### Strengths

- Three complete public repositories
- Open-source technology (R, Python, TensorFlow)
- Clear documentation of workflow
- Validation scripts included

### Weaknesses

- Commercial satellite imagery not shareable
- Field data reference-only (published reports)
- No requirements.txt or Docker specification
- No explicit dependency versions

### Scoring Rationale

Score of 72 (Good) reflects excellent code availability offset by data access constraints and partial environment specification. Analytical reproducibility achievable with substitute imagery but exact replication constrained.

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

Strong code infrastructure enables analytical reproduction with substitute data. Data access is the primary limitation, though this is a common constraint for studies using commercial satellite imagery.

```yaml
cluster_3_reproducibility:
  reproducibility: {score: 72, band: "good"}
  overall_rating: "adequate"
```
