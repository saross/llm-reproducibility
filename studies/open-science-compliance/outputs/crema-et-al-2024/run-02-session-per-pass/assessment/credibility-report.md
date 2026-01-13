# Credibility Assessment Report

**Paper:** Modelling diffusion of innovation curves using radiocarbon data
**Slug:** crema-et-al-2024
**Assessment Date:** 2026-01-13
**Assessor Version:** v1.0
**Schema Version:** 1.0

---

## Executive Summary

> **Verdict:** Excellent | **Confidence:** HIGH
>
> This methodological paper using deductive validation demonstrates exemplary transparency and reproducibility. Published in 2024, it represents best practice for computational archaeology in the early_majority era of reproducibility adoption.
>
> **Key Strengths:**
> - Exemplary transparency: full mathematical specification, explicit priors, documented MCMC settings
> - Dual archival (GitHub + Zenodo DOI) with independent code review by JAS Reproducibility Specialist
> - Pre-specified simulation validation before empirical application
>
> **Key Concerns:**
> - Minor: Package dependencies not explicitly listed in paper text (likely in repository)
>
> **Bottom Line:** This paper could serve as a template for reproducible methodological papers in computational archaeology, combining rigorous validation methodology with exemplary open science practice.

---

## Signal Dashboard

| Signal | Score | Band |
|--------|-------|------|
| Comprehensibility | 88 | Excellent |
| Transparency | 92 | Excellent |
| Plausibility | 82 | Excellent |
| Validity | 85 | Excellent |
| Robustness | 75 | Good |
| Generalisability | 78 | Good |
| Reproducibility | 90 | Excellent |

**Aggregate Score:** 84 (EXPERIMENTAL)

**Note:** Aggregate scores are experimental — we are investigating what they mean across different paper types and research approaches.

---

## Classification Summary

| Attribute | Value |
|-----------|-------|
| Paper Type | methodological |
| Research Approach | deductive |
| Validation Strategy | Simulation-based with known parameters |
| Framework | methodological_paper |
| Classification Confidence | HIGH |
| Quality State | HIGH |

**Context Flags:** 🔧 (methodological transparency)

---

## Cluster Summaries

### Cluster 1: Foundational Clarity (Transparency Pillar)

**Rating:** Strong

**Comprehensibility (88, Excellent):** All methodological claims are explicit and bounded. Technical terms are operationally defined with mathematical precision. The argument structure is transparent: limitation identification → method development → validation → application.

**Transparency (92, Excellent):** Full mathematical specification (equations 2-8). Complete documentation of priors, MCMC settings, and simulation parameters. Code and data publicly available with dual archival and independent code review.

### Cluster 2: Evidential Strength (Credibility Pillar)

**Rating:** Strong

**Plausibility (82, Excellent):** Method grounded in established diffusion theory and statistical practice. Case studies from well-researched contexts. Anomalous results acknowledged and contextualised within established literature.

**Validity (85, Excellent):** Pre-specified simulation validation with known parameters. Evidence directly addresses methodological hypotheses through parameter recovery testing. Dual-model approach provides alternative verification.

**Robustness (75, Good):** Dual-model triangulation provides robustness evidence. Convergence diagnostics documented. Comprehensive sensitivity analysis to analytical choices not systematically documented.

**Generalisability (78, Good):** Method scope clearly bounded. Case study boundaries explicit with temporal and geographic constraints. Transfer conditions specified through code documentation.

### Cluster 3: Reproducibility (Reproducibility Pillar)

**Rating:** Strong

**Reproducibility (90, Excellent):** Complete data and code available with DOIs. Independent code review by Ben Marwick. Workflow fully documented. Table 1 provides clear verification targets. Priority 1 candidate for reproduction attempt.

---

## Contextual Interpretation

### Robustness (75, Good) 🔧

**Why this score:** Methodological papers typically emphasise demonstrating that a new method works rather than exhaustively testing sensitivity to all analytical choices. This paper provides triangulation through the dual-model approach (parametric + non-parametric) and validates through simulation, but doesn't systematically vary prior specifications or time-block widths.

**What this means:** The Robustness score reflects standard practice for methodological papers rather than a deficiency. Readers should note that while the method is validated under the specified analytical choices, sensitivity to alternative choices is not exhaustively documented.

**What readers should consider:** If applying this method to different contexts, users should consider testing sensitivity to prior specifications and time-block widths for their specific datasets.

---

## Infrastructure & FAIR Summary

**FAIR Assessment:**

| Dimension | Status | Details |
|-----------|--------|---------|
| **Data Availability** | Available | GitHub + Zenodo (DOI: 10.5281/zenodo.10782942) |
| **Code Availability** | Available | GitHub + Zenodo, R implementation, code reviewed |
| **Preregistration** | Not applicable | Method validation paper (simulation serves similar function) |
| **Persistent Identifiers** | Present | Paper DOI, Data/Code DOI |

**PID Graph Connectivity:** 3/6
- Paper DOI: ✓
- Data DOI: ✓
- Code DOI: ✓
- Author ORCIDs: ✗ (journal display limitation)
- Funder RORs: ✗
- Institution RORs: ✗

**Infrastructure Gaps:**
- Author ORCIDs not displayed (JAS journal policy issue, not author choice)
- Funder and institution RORs not present (emerging practice)

---

## Era Context

**Publication Year:** 2024
**Era:** early_majority (2020-2025)
**Era Label:** "Current era — FAIR and open science expectations established"

**Expectations Note:** In 2024, data and code sharing are increasingly expected for computational papers. This paper exceeds era expectations by providing independent code review and dual archival — practices that will likely become standard in the mainstream era (post-2025).

---

## Detailed Findings

### Key Strengths

1. **Methodological Transparency:** The paper provides complete mathematical specification of both models with explicit equations, prior distributions, MCMC settings, and convergence diagnostics. This enables full understanding and independent implementation.

2. **Validation Strategy:** The simulation-based validation with pre-specified parameters (P010) represents best practice — testing model recovery under known conditions before empirical application is paradigmatic deductive validation.

3. **Reproducibility Infrastructure:** Dual archival (GitHub + Zenodo DOI) addresses both usability and preservation. Independent code review by Ben Marwick adds verification that the code runs and produces claimed outputs.

4. **Anomaly Handling:** When posterior predictive checks revealed poor model fit for agricultural case studies, the paper interprets these deviations rather than ignoring them, contextualising within established literature.

### Key Limitations

1. **Package Dependencies:** R package dependencies and versions are not explicitly listed in the paper text — reproduction would require checking repository documentation.

2. **Sensitivity Analysis:** While dual-model triangulation provides robustness evidence, comprehensive sensitivity analysis varying analytical choices (priors, time-blocks, thresholds) is not systematically documented.

3. **Proxy Assumptions:** The paper acknowledges that direct dating of seeds is an imperfect proxy for farming practice adoption (IA002), with potential biases from differential preservation.

---

## Reproduction Readiness

**Execution Feasibility:** Ready

**Priority:** 1 (Priority candidate for Open Science Compliance Study)

**Expected Effort:** Low-to-moderate

**Steps for Reproduction:**
1. Clone repository from GitHub (or download Zenodo archive)
2. Install R and identify required packages from repository documentation
3. Download IntCal20 calibration curve
4. Run simulation validation — verify parameter recovery against P010 specifications
5. Run case study analyses — compare parameter estimates to Table 1
6. Generate posterior predictive checks — compare to Figures 3-4
7. Run ICAR cremation analysis — compare to Figure 5

**Verification Targets:**
- Table 1 parameter estimates (r, m, mu, phi with 90% HPD intervals)
- Simulation parameter recovery (should fall within 95% posterior range)
- Posterior predictive check patterns (Japan double-s, Britain deviations)

---

## Structured Output (JSON)

```json
{
  "credibility_report": {
    "version": "1.0",
    "paper": {
      "slug": "crema-et-al-2024",
      "title": "Modelling diffusion of innovation curves using radiocarbon data",
      "doi": "10.1016/j.jas.2024.105962",
      "publication_year": 2024
    },
    "classification": {
      "paper_type": "methodological",
      "paper_subtype": "analytical_method",
      "approach": "deductive",
      "framework": "methodological_paper",
      "quality_state": "high",
      "classification_confidence": "high"
    },
    "verdict": {
      "band": "excellent",
      "confidence": "high",
      "aggregate_score": 84,
      "aggregate_experimental": true
    },
    "signals": {
      "comprehensibility": { "score": 88, "band": "excellent" },
      "transparency": { "score": 92, "band": "excellent" },
      "plausibility": { "score": 82, "band": "excellent" },
      "validity": { "score": 85, "band": "excellent" },
      "robustness": { "score": 75, "band": "good", "context_flag": "🔧" },
      "generalisability": { "score": 78, "band": "good" },
      "reproducibility": { "score": 90, "band": "excellent", "pathway": "standard" }
    },
    "aggregates": {
      "cluster_1_rating": "strong",
      "cluster_2_rating": "strong",
      "cluster_3_rating": "strong"
    },
    "infrastructure": {
      "fair_score": null,
      "fair_rating": "highly_fair",
      "fair_maximum": 40,
      "code_availability": "available",
      "data_availability": "available",
      "preregistration": "not_applicable",
      "code_reviewed": true,
      "code_reviewer": "Ben Marwick"
    },
    "era_context": {
      "publication_year": 2024,
      "era": "early_majority",
      "era_label": "Current era — FAIR and open science expectations established",
      "expectations_note": "Paper exceeds era expectations with independent code review and dual archival"
    },
    "assessment_metadata": {
      "assessment_date": "2026-01-13",
      "assessor_version": "v1.0",
      "schema_version": "1.0"
    }
  }
}
```

---

## Assessment Metadata

| Field | Value |
|-------|-------|
| Assessment Date | 2026-01-13 |
| Assessor Version | v1.0 |
| Schema Version | 1.0 |
| Extraction Run | run-02-session-per-pass |
| Quality State | HIGH |

---

*This credibility assessment was generated using the research-assessor skill (v0.2-alpha) as part of the Open Science Compliance Study, Phase 1.*
