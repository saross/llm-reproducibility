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

This empirical paper using deductive hypothesis-testing reasoning demonstrates strong credibility across foundational and evidential dimensions. Published in 2024 (early majority era for reproducibility practices), it exemplifies good scientific practice in honestly reporting negative results and provides valuable methodological guidance for the field.

**Key Strengths:**
- Exceptional transparency in documenting a "failed" hypothesis with quantified evidence
- Strong external validation using 773 ground-truthed burial mounds from independent pedestrian survey
- Exemplary code availability through three public GitHub repositories covering the complete workflow

**Key Concerns:**
- Field survey data (773 mound points) not deposited in public repository
- Satellite imagery access restricted by proprietary terms (GeoEye Foundation grant)
- Limited robustness testing (single architecture, threshold, tile size)

**Bottom Line:** A credible, well-documented study that honestly reports the failure of low-touch transfer learning for archaeological feature detection in heterogeneous landscapes. The negative result is as valuable as a positive one — possibly more so given publication bias in the field.

---

## Signal Scores Dashboard

| Signal | Score | Band | Cluster | Context |
|--------|-------|------|---------|---------|
| Comprehensibility | 78 | Good | 1 | Deductive |
| Transparency | 80 | Excellent | 1 | Deductive |
| Plausibility | 82 | Excellent | 2 | Deductive |
| Validity | 80 | Excellent | 2 | Deductive |
| Robustness | 55 | Moderate | 2 | Deductive |
| Generalisability | 75 | Good | 2 | Deductive |
| Reproducibility | 62 | Good | 3 | Standard pathway |

**Aggregate Score:** 73/100 (GOOD) — *EXPERIMENTAL*

*Note: The aggregate score is experimental. It is calculated as the mean of all seven signal scores and provides a rough summary measure. We are investigating what it means for assessment interpretation.*

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

This paper demonstrates strong foundational clarity appropriate for deductive hypothesis-testing research. While formal hypotheses are not stated (e.g., "H1: CNN will detect ≥50% of mounds"), the implicit hypotheses are clearly framed and their testing is transparent.

**Key Strengths:**
- Clear core claims (C001-C003) with quantified performance metrics
- Explicit research design with comparative validation framework (RD001, RD002)
- Three public GitHub repositories with complete computational workflow
- Comprehensive methods and protocols documentation (M001-M009, P001-P015)
- Thorough acknowledgement of limitations and failed expectations

**Key Weaknesses:**
- Hypotheses implicit rather than formally stated
- No pre-registration of study design
- Field survey data not deposited in public repository
- No explicit licence for code repositories

---

### Cluster 2: Evidential Strength (Strong)

The paper demonstrates strong evidential strength through the 773-mound ground truth dataset providing robust external validation. The gap between self-reported metrics (F1 = 0.87) and field-validated performance (4.9% detection, 95% false negatives) demonstrates precisely why external validation is essential.

**Key Strengths:**
- Hypotheses grounded in established ML transfer learning theory
- 773 ground-truthed mounds from pedestrian survey provides independent validation
- Two-run comparative design tests sensitivity to training data curation
- Multiple alternative explanations for failure explicitly considered
- Paper explicitly framed as "cautionary tale" with appropriate scope limitations

**Key Weaknesses:**
- Limited sensitivity analysis (60% threshold not varied)
- No alternative model architectures systematically compared
- Single geographic context limits generalisability claims
- Robustness score (55) reflects honest reporting rather than exhaustive parameter search

---

### Cluster 3: Reproducibility (Adequate)

The paper demonstrates an asymmetric reproducibility profile: excellent code availability but limited data accessibility. This creates a situation where the analytical workflow can be examined and understood but cannot be fully executed without independent data acquisition.

**Pathway:** Standard (computational component present)

**Key Strengths:**
- Three public GitHub repositories covering complete analytical pipeline
- Open scriptable tools (Python, TensorFlow 2, R) enable technical reproduction
- Protocols documented with specific parameters (thresholds, ratios, tile sizes)
- FAIR score: 24/40 (60%)

**Key Weaknesses:**
- Field survey data (773 mounds) not deposited in public repository
- Satellite imagery access unclear (GeoEye Foundation grant terms)
- No explicit environment specification (Python/package versions, Docker)
- No code DOIs (GitHub URLs only, no archival)

---

## Contextual Interpretation

### Robustness (55, Moderate)

**Why this score:** The paper tests two training conditions (773 vs. 249 mounds) but does not systematically vary other parameters (probability threshold, tile size, data split ratios, model architecture). This is characteristic of hypothesis-testing research rather than parameter-optimisation research.

**What this means:** The consistent failure across both runs suggests the negative result is robust to training data variation. However, we cannot determine whether different analytical choices (e.g., overlapping tiles, different thresholds) might yield different results.

**What readers should consider:** The moderate Robustness score reflects methodological transparency rather than methodological weakness. The authors did not "tune" parameters to find conditions where the model might appear to succeed — they honestly reported the first reasonable approach and its failure.

---

### Generalisability (75, Good)

**Why this score:** The paper is appropriately bounded as a case study of the Kazanlak Valley, Bulgaria. The authors frame findings as a "cautionary tale" rather than universal conclusions about CNN applicability.

**What this means:** The specific findings (95-96% false negative rates) are bounded to the tested context. The methodological lessons (importance of external validation, publication bias, heterogeneous landscape challenges) have broader applicability.

**What readers should consider:** Before applying transfer learning to other archaeological contexts, consider whether your features share characteristics with Bulgarian burial mounds: variable sizes, heterogeneous backgrounds, low target-to-image ratios.

---

## Infrastructure & FAIR Summary

| Dimension | Score | Status |
|-----------|-------|--------|
| **FAIR Total** | 24/40 | 60% |
| Findable | 7/10 | DOI present; code URLs provided; data not findable in repository |
| Accessible | 6/10 | Code public; imagery proprietary; field data not deposited |
| Interoperable | 5/10 | Standard formats (Python, R, GeoTIFF, EPSG:32635) |
| Reusable | 6/10 | Code reusable via GitHub; data reuse limited; no explicit licence |

**Code Availability:** Available (three GitHub repositories: cnn-testing, burial-mounds, MoundDetection)
**Data Availability:** Partial (field data referenced but not deposited; imagery proprietary)
**Preregistration:** Not preregistered
**PID Coverage:** Paper DOI present; no data DOIs; no software DOIs

**Infrastructure Gaps:**
- Field survey data needs public repository deposit with PID
- Software repositories need archival with DOIs (e.g., Zenodo)
- Environment specification files needed (requirements.txt, Docker)
- Explicit open-source licence needed for code

---

## Era Context

**Publication Year:** 2024
**Era:** Early Majority
**Expectations:** Code and data sharing increasingly expected; FAIR principles well-established

By 2024 standards, the code availability is exemplary (three public repositories) while data availability lags current expectations. The gap between code transparency (excellent) and data accessibility (limited) reflects the common challenge of publishing research using legacy fieldwork data collected before current open science norms. The 2009-2011 TRAP fieldwork predates widespread data deposit requirements.

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
      "aggregate_score": 73,
      "aggregate_experimental": true
    },
    "signals": {
      "comprehensibility": { "score": 78, "band": "good" },
      "transparency": { "score": 80, "band": "excellent" },
      "plausibility": { "score": 82, "band": "excellent" },
      "validity": { "score": 80, "band": "excellent" },
      "robustness": { "score": 55, "band": "moderate" },
      "generalisability": { "score": 75, "band": "good" },
      "reproducibility": { "score": 62, "band": "good", "variant": "standard" }
    },
    "aggregates": {
      "cluster_1_rating": "strong",
      "cluster_2_rating": "strong",
      "cluster_3_rating": "adequate"
    },
    "infrastructure": {
      "fair_score": 24,
      "fair_maximum": 40,
      "fair_percentage": 60,
      "fair_rating": "partial",
      "code_availability": "available",
      "data_availability": "partial",
      "preregistration": "not_preregistered"
    },
    "era_context": {
      "publication_year": 2024,
      "era": "early_majority",
      "era_label": "Early majority era — FAIR and open science expectations established",
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
- Aggregate score 73 (in 60-79 range = GOOD band)
- Four signals in Excellent band (80+): Transparency, Plausibility, Validity
- One signal in Moderate band (55): Robustness — reflects honest reporting not weakness
- Strong foundational clarity and evidential strength clusters
- Adequate reproducibility constrained by data accessibility

**Signal Score Calculation:**
- Comprehensibility: 78
- Transparency: 80
- Plausibility: 82
- Validity: 80
- Robustness: 55
- Generalisability: 75
- Reproducibility: 62
- **Mean: 73.1 → 73**

---

*Generated by Claude Opus 4.5 using the research-assessor skill*
