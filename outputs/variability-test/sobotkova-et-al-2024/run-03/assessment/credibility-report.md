# Credibility Assessment Report

**Paper:** sobotkova-et-al-2024
**Title:** Validating predictions of burial mounds with field data: the promise and reality of machine learning
**DOI:** 10.1108/JD-05-2022-0096
**Publication Year:** 2024

**Assessment Date:** 2025-12-05
**Assessor Version:** v1.0
**Quality State:** HIGH

---

## Executive Summary

**Verdict:** GOOD | **Confidence:** HIGH

This empirical paper using deductive hypothesis-testing reasoning demonstrates strong credibility across all major dimensions. Published in 2024 (Current era — FAIR and open science expectations established), it exemplifies good practice for computational archaeology with legacy data constraints.

**Key Strengths:**
- Exceptional transparency in reporting negative results ("cautionary tale" framing)
- Strong external validation using 773 ground-truthed burial mounds from independent fieldwork
- Exemplary code availability through three public GitHub repositories

**Key Concerns:**
- Field data not deposited in public repository (requires author coordination)
- IKONOS satellite imagery proprietary and not shareable

**Bottom Line:** A credible, well-documented study that honestly reports the failure of low-touch transfer learning for archaeological feature detection, providing valuable methodological guidance for the field.

---

## Signal Scores Dashboard

| Signal | Score | Band | Cluster | Context |
|--------|-------|------|---------|---------|
| Comprehensibility | 82 | Excellent | 1 | — |
| Transparency | 78 | Good | 1 | — |
| Plausibility | 85 | Excellent | 2 | — |
| Validity | 82 | Excellent | 2 | — |
| Robustness | 75 | Good | 2 | — |
| Generalisability | 68 | Adequate | 2 | — |
| Reproducibility | 65 | Good | 3 | — |

**Aggregate Score:** 76/100 (GOOD) — *EXPERIMENTAL*

*Note: The aggregate score is experimental. We are investigating what it means for assessment interpretation.*

---

## Cluster Ratings Summary

| Cluster | Rating | Pillar |
|---------|--------|--------|
| Cluster 1: Foundational Clarity | Strong | Transparency |
| Cluster 2: Evidential Strength | Strong | Credibility |
| Cluster 3: Reproducibility | Adequate | Reproducibility |

---

## Detailed Findings

### Cluster 1: Foundational Clarity (Strong)

This paper demonstrates strong foundational clarity appropriate for deductive hypothesis-testing research. The central hypothesis is explicit: testing whether "low-touch" transfer learning using pre-trained CNNs can effectively detect archaeological features. The research design is fully documented with comprehensive protocols.

**Key Strengths:**
- Hypothesis explicitly stated and clearly bounded
- All key terms operationally defined (model architecture, performance metrics, validation procedures)
- Three public GitHub repositories with complete code

**Key Weaknesses:**
- Some ML terminology assumes domain familiarity
- Field survey data not deposited in public repository
- No pre-registration (though retrospective analysis using existing data)

---

### Cluster 2: Evidential Strength (Strong)

The paper demonstrates strong evidential strength through the 773-mound ground truth dataset providing robust external validation. The two-run comparative design tests sensitivity to training data curation, and the gap between self-reported metrics (F1 = 0.87) and field-validated performance (4.9% detection rate) demonstrates why external validation is essential.

**Key Strengths:**
- 773 ground-truthed mounds from pedestrian survey provides independent validation
- Two-run comparative design with comprehensive validation metrics
- Evidence-claim relationships direct and traceable
- Counterintuitive finding (curated data performed worse) suggests robustness

**Key Weaknesses:**
- Single geographic context (Bulgaria)
- Single probability threshold (60%) without sensitivity analysis
- No alternative architecture testing beyond preliminary experimentation

---

### Cluster 3: Reproducibility (Adequate)

The paper demonstrates an asymmetric reproducibility profile: excellent code availability but limited data accessibility. Three public GitHub repositories provide complete analytical code, but the 773-mound field dataset is not publicly deposited.

**Pathway:** Standard (computational)

**Key Strengths:**
- Three public GitHub repositories with complete analytical code
- Comprehensive protocol documentation enables methodological reproduction
- Open scriptable tools (Python, R, TensorFlow 2)
- Resource requirements transparently reported (135 person-hours)

**Key Weaknesses:**
- Field survey data (773 mounds) not deposited in public repository
- Satellite imagery proprietary (IKONOS via GeoEye Foundation)
- No environment specification files (requirements.txt, Docker)

---

## Contextual Interpretation

### Generalisability (68, Adequate)

**Why this score:** Single-context empirical research testing a specific hypothesis in one geographic location naturally has constrained generalisability. This is appropriate for hypothesis-testing research — the paper tests whether low-touch transfer learning works for Bulgarian burial mounds, not whether it works everywhere.

**What this means:** The specific empirical findings (95-96% false negative rates) are bounded to the tested context (Kazanlak Valley, Bulgaria; IKONOS imagery; ResNet-50 architecture). However, the methodological insights (importance of external validation, publication bias concerns, cost-benefit considerations) have broader applicability.

**What readers should consider:** Before applying transfer learning to their own archaeological contexts, readers should consider whether their features share characteristics with Bulgarian burial mounds (heterogeneous landscapes, variable feature visibility).

---

### Reproducibility (65, Good)

**Why this score:** The asymmetric profile (excellent code, limited data) reflects common constraints in computational archaeology using legacy fieldwork data and proprietary remote sensing imagery. The 2009-2011 TRAP fieldwork predates current data deposit norms.

**What this means:** Someone could retrain the CNN model with different data and verify the methodology, but cannot verify the specific detection rates without access to the original field data.

**What readers should consider:** The computational workflow is fully documented and executable. Reproduction requires coordinating with authors for field data access or using comparable substitute datasets.

---

## Infrastructure & FAIR Summary

| Dimension | Score | Status |
|-----------|-------|--------|
| **FAIR Total** | 20/40 | 50% |
| Findable | 6/10 | DOI present; code URLs provided; data not findable |
| Accessible | 5/10 | Code public; imagery proprietary; field data not deposited |
| Interoperable | 5/10 | Standard formats (Python, R, GeoTIFF) |
| Reusable | 4/10 | Code reusable; data reuse limited |

**Code Availability:** Available (three GitHub repositories)
**Data Availability:** Partial (field data not deposited; imagery proprietary)
**Preregistration:** Not preregistered (retrospective analysis)
**PID Coverage:** Paper DOI present; no data DOIs; no software DOIs

**Infrastructure Gaps:**
- Field survey data needs public repository deposit
- Software repositories need DOIs (e.g., Zenodo archival)
- Environment specification files (requirements.txt, Docker) not provided

---

## Era Context

**Publication Year:** 2024
**Era:** Current (2020-present)
**Expectations:** FAIR and open science expectations established

By 2024 standards, the code availability is exemplary (three public repositories) while data availability lags current expectations. The gap between code transparency (excellent) and data accessibility (limited) reflects the common challenge of publishing research using legacy fieldwork data collected before current open science norms.

---

## Structured JSON Output

```json
{
  "credibility_report": {
    "version": "1.0",
    "paper": {
      "slug": "sobotkova-et-al-2024",
      "title": "Validating predictions of burial mounds with field data: the promise and reality of machine learning",
      "doi": "10.1108/JD-05-2022-0096",
      "publication_year": 2024
    },
    "classification": {
      "paper_type": "empirical",
      "paper_subtype": "hypothesis_testing",
      "approach": "deductive",
      "framework": "deductive_emphasis",
      "quality_state": "high",
      "classification_confidence": "high"
    },
    "verdict": {
      "band": "good",
      "confidence": "high",
      "aggregate_score": 76,
      "aggregate_experimental": true
    },
    "signals": {
      "comprehensibility": { "score": 82, "band": "excellent" },
      "transparency": { "score": 78, "band": "good" },
      "plausibility": { "score": 85, "band": "excellent" },
      "validity": { "score": 82, "band": "excellent" },
      "robustness": { "score": 75, "band": "good" },
      "generalisability": { "score": 68, "band": "adequate" },
      "reproducibility": { "score": 65, "band": "good", "variant": "standard" }
    },
    "aggregates": {
      "cluster_1_rating": "strong",
      "cluster_2_rating": "strong",
      "cluster_3_rating": "adequate"
    },
    "infrastructure": {
      "fair_score": 20,
      "fair_rating": "partial",
      "fair_maximum": 40,
      "code_availability": "available",
      "data_availability": "partial",
      "preregistration": "not_preregistered"
    },
    "era_context": {
      "publication_year": 2024,
      "era": "current",
      "era_label": "Current era — FAIR and open science expectations established",
      "expectations_note": "Code availability exemplary; data availability lags current expectations due to legacy fieldwork constraints"
    },
    "assessment_metadata": {
      "assessment_date": "2025-12-05",
      "assessor_version": "v1.0",
      "schema_version": "1.0"
    }
  }
}
```

---

## Assessment Notes

This assessment was generated using the standard deductive hypothesis-testing framework. The paper's explicit negative result format ("cautionary tale") demonstrates exemplary scientific transparency — testing a plausible hypothesis, finding it unsupported, and honestly reporting this outcome with comprehensive resource documentation.

The asymmetric reproducibility profile (excellent code, limited data) is characteristic of computational archaeology using legacy fieldwork data. The code transparency is ahead of field norms; the data gap reflects common limitations when using pre-existing fieldwork collected before current open science expectations were established.

**Verdict Rationale:** GOOD rating based on:
- All signals ≥ 65 (no signal < 50)
- Aggregate score 76 (in 60-79 range)
- Strong foundational clarity and evidential strength
- Adequate reproducibility constrained by data accessibility

---

*Generated by Claude Opus 4 using the research-assessor skill*
