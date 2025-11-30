# Credibility Assessment Report

**Paper:** Validating predictions of burial mounds with field data: the promise and reality of machine learning
**Slug:** sobotkova-et-al-2024
**DOI:** 10.1108/JD-05-2022-0096
**Assessment Date:** 2025-11-30
**Schema Version:** 1.0

---

## Executive Summary

**Verdict:** Good | **Confidence:** HIGH

This empirical paper using deductive reasoning demonstrates strong credibility. The research tests whether pre-trained CNN with transfer learning can detect burial mounds, finding that self-reported metrics overstate actual performance when validated against field data.

**Era Context:** Current era (2024) — FAIR and open science expectations established.

**Key Strengths:**
- External validation against 773 field-verified mounds provides strong evidence basis
- Three public GitHub repositories demonstrate exceptional code transparency
- Honest reporting of failure with thorough mechanistic explanation

**Key Concerns:**
- Data access limitations (commercial imagery, reference-only field data) affect full reproducibility

**Bottom Line:** A methodologically rigorous cautionary study that provides strong evidence for its claims about ML limitations in archaeological prospection.

---

## Signal Scores Dashboard

| Pillar | Signal | Score | Band |
|--------|--------|-------|------|
| **Transparency** | Comprehensibility | 78 | Good |
| | Transparency | 82 | Excellent |
| **Credibility** | Plausibility | 75 | Good |
| | Validity | 80 | Excellent |
| | Robustness | 68 | Good |
| | Generalisability | 78 | Good |
| **Reproducibility** | Reproducibility | 72 | Good |

**Aggregate Score:** 76 (Good) — EXPERIMENTAL

> **Note:** Aggregate score is experimental. We are investigating what a single number means for credibility assessment across diverse paper types.

---

## Classification Summary

| Attribute | Value |
|-----------|-------|
| Paper Type | Empirical |
| Paper Subtype | Validation study |
| Research Approach | Deductive |
| Framework | Hypothesis testing (transfer learning effectiveness) |
| Quality State | HIGH |
| Classification Confidence | HIGH |

---

## Cluster Summaries

### Cluster 1: Foundational Clarity (Transparency Pillar)

**Rating:** Strong

The paper demonstrates strong foundational clarity. Claims are explicit, bounded, and quantified — readers can clearly understand what is being tested and what was found. Core claims (model failure, metric/performance mismatch, manual alternatives may be more efficient) are supported by specific evidence. Methodology is comprehensively documented with exceptional code sharing through three GitHub repositories. Limitations are extensively acknowledged.

**Key Strengths:**
- Clear argumentative structure from design through conclusions
- Three public GitHub repositories with complete pipeline code
- Honest, extensive limitation discussion

**Key Weaknesses:**
- Hypothesis implicit rather than formally stated
- Data availability limited (commercial imagery, reference-only field data)

### Cluster 2: Evidential Strength (Credibility Pillar)

**Rating:** Strong

The paper demonstrates consistently strong evidential strength. The key methodological contribution — external validation against field data — provides robust evidence that self-reported ML metrics overstate actual performance. The two-run experimental design tests an alternative hypothesis (curated training data), finding consistent failure across both approaches. Claims are carefully scoped to the study context with extensive limitation acknowledgement.

**Key Strengths:**
- External validation against 773 field-verified mounds
- Two-run design tests training data selection alternative
- Comprehensive limitation and scope discussion

**Key Weaknesses:**
- Single study area limits generalisability (acknowledged)
- Limited threshold and tile size sensitivity analyses

### Cluster 3: Reproducibility (Reproducibility Pillar)

**Rating:** Adequate

The paper demonstrates adequate computational reproducibility with notable strengths and limitations. Code sharing is exemplary — three organised public repositories cover the complete analytical pipeline (training prep, 2021 model, 2022 model). The primary limitation is data access: commercial satellite imagery and reference-only field data create barriers to full reproduction.

**Key Strengths:**
- Three public GitHub repositories
- Open scriptable tools (R, Python)
- Well-organised workflow separation

**Key Weaknesses:**
- Commercial satellite imagery not shareable
- No formal environment specification

---

## Infrastructure & FAIR Summary

| Component | Status | Details |
|-----------|--------|---------|
| **Code Availability** | ✅ Available | Three GitHub repositories (public) |
| **Data Availability** | ⚠️ Partial | Field data: reference to Ross et al. 2018; Imagery: commercial IKONOS |
| **Preregistration** | ❌ Not preregistered | Exploratory/evaluative study |
| **DOI (Paper)** | ✅ Present | 10.1108/JD-05-2022-0096 |
| **Software PIDs** | ❌ Absent | GitHub URLs only, no DOIs |

**FAIR Assessment:** Partial compliance. Strong on code sharing (Reusable), limited on data accessibility (Accessible). Findability good through paper DOI. Interoperability through open formats (R, Python).

---

## Era Context

**Publication Year:** 2024
**Era:** Current era (2020-present)
**Expectations Note:** FAIR and open science expectations established. Code sharing increasingly expected. Data sharing standard where legally/ethically possible.

This paper meets or exceeds current era expectations for code sharing. Data access limitations reflect common constraints in commercial satellite imagery research rather than transparency failures.

---

## Contextual Interpretation

No context flags applied. This is a standard empirical deductive study with scores reflecting actual credibility assessment.

**Note on Robustness (68, Good):** This score is appropriate for the paper. While the two-run design provides robustness evidence, more comprehensive sensitivity analyses (threshold testing, tile size variations) would strengthen the score. This is not a methodological paper where lower robustness would be expected by genre.

---

## Structured Output

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
      "paper_subtype": "validation_study",
      "approach": "deductive",
      "framework": "hypothesis_testing",
      "quality_state": "high",
      "classification_confidence": "high"
    },
    "verdict": {
      "band": "Good",
      "confidence": "HIGH",
      "aggregate_score": 76,
      "aggregate_experimental": true
    },
    "signals": {
      "comprehensibility": { "score": 78, "band": "good" },
      "transparency": { "score": 82, "band": "excellent" },
      "plausibility": { "score": 75, "band": "good" },
      "validity": { "score": 80, "band": "excellent" },
      "robustness": { "score": 68, "band": "good" },
      "generalisability": { "score": 78, "band": "good" },
      "reproducibility": { "score": 72, "band": "good", "variant": "standard" }
    },
    "aggregates": {
      "cluster_1_rating": "strong",
      "cluster_2_rating": "strong",
      "cluster_3_rating": "adequate"
    },
    "infrastructure": {
      "fair_score": null,
      "fair_rating": "partial",
      "fair_maximum": 40,
      "code_availability": "available",
      "data_availability": "partially_available",
      "preregistration": "not_preregistered"
    },
    "era_context": {
      "publication_year": 2024,
      "era": "current",
      "era_label": "Current era",
      "expectations_note": "FAIR and open science expectations established"
    },
    "assessment_metadata": {
      "assessment_date": "2025-11-30",
      "assessor_version": "v1.0",
      "schema_version": "1.0",
      "run_id": "variability-test/run-01"
    }
  }
}
```

---

**End of Credibility Assessment Report**
