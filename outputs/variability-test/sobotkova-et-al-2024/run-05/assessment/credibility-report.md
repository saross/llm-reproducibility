# Credibility Assessment Report

**Paper:** Validating predictions of burial mounds with field data: the promise and reality of machine learning
**DOI:** 10.1108/JD-05-2022-0096
**Publication Year:** 2024

**Assessment Date:** 2025-12-06
**Assessor Version:** v1.0
**Schema Version:** 1.0

---

## Executive Summary

**Verdict:** GOOD | **Confidence:** HIGH

This empirical paper using deductive reasoning demonstrates strong methodological transparency and excellent evidential strength, with an asymmetric reproducibility profile. As a 2024 publication, it falls within the current era where FAIR and open science expectations are established.

**Key Strengths:**
- Excellent validity (85) through independent ground-truth validation against 773 mounds from prior TRAP survey
- Strong theoretical grounding with coherent interpretation of negative results
- High transparency in methodology, with clear validation framework and explicit parameters

**Key Concerns:**
- Reproducibility limited by data access barriers (IKONOS imagery, survey coordinates not publicly deposited)
- No persistent identifiers for code or data repositories

**Bottom Line:** A well-designed validation study that transparently documents CNN failure in archaeological detection, demonstrating strong credibility despite moderate reproducibility due to data access constraints.

---

## Signal Scores Dashboard

| Signal | Score | Band | Context |
|--------|-------|------|---------|
| Comprehensibility | 78 | Good | Deductive |
| Transparency | 75 | Good | Deductive |
| Plausibility | 82 | Excellent | Deductive |
| Validity | 85 | Excellent | Deductive |
| Robustness | 68 | Good | Deductive |
| Generalisability | 72 | Good | Deductive |
| Reproducibility | 58 | Moderate | Standard pathway |

**Aggregate Score:** 74 (GOOD) — *EXPERIMENTAL: Aggregate scoring under investigation*

---

## Cluster Assessments

### Cluster 1: Foundational Clarity — STRONG

The paper demonstrates strong foundational clarity for a deductive validation study. The central hypothesis—that a CNN trained on legacy field data can reliably detect burial mounds—is clearly stated and systematically tested. Key terms are operationally defined, the logical structure of hypothesis testing is transparent, and the validation framework is explicit.

**Key Strengths:**
- Central hypothesis explicitly stated and clearly bounded
- Key terms operationally defined (true/false positive, probability threshold)
- Research design clearly documented with specific parameters

**Key Weaknesses:**
- Literature review methodology incomplete (coding scheme not described)
- Some technical details missing (hyperparameters, software versions)

---

### Cluster 2: Evidential Strength — STRONG

The paper demonstrates strong evidential strength across all four signals, with particular excellence in Plausibility (82) and Validity (85). The core finding—that the CNN approach failed despite good internal metrics—is well-supported by independent ground-truth validation and theoretically coherent interpretation.

**Key Strengths:**
- Independent ground-truth validation (773 mounds from prior TRAP survey)
- Anomalous results coherently explained through feature learning theory
- Two-run comparison provides robustness evidence across training data conditions

**Key Weaknesses:**
- Limited systematic sensitivity analysis beyond two-run comparison
- Transfer conditions for other contexts not systematically specified

---

### Cluster 3: Reproducibility — ADEQUATE

**Pathway:** Standard (computational paper)

The paper has clear computational components (CNN training, spatial validation) that could potentially be reproduced. Code availability is positive through TRAP GitHub repositories. However, critical barriers exist: primary data (IKONOS imagery, field survey coordinates) are not publicly deposited, no persistent identifiers are provided, and computational environment is not specified.

**Key Strengths:**
- Clear CNN model architecture specification (ResNet-50)
- Training/validation/test split documented (70:20:10)
- GitHub presence for TRAP project

**Key Weaknesses:**
- Primary data not publicly available
- No persistent identifiers for code or data
- Environment specification absent

---

## Infrastructure & FAIR Summary

| Dimension | Status |
|-----------|--------|
| **Code Availability** | Partial — GitHub repositories mentioned, no DOIs |
| **Data Availability** | Partial — IKONOS imagery licensed, survey data unspecified |
| **Preregistration** | Not preregistered |
| **Persistent Identifiers** | No DOIs for code/data; paper DOI present |

**Infrastructure Gaps:**
- No formal data deposit with persistent identifier
- No code DOI or archived version
- No computational environment specification
- GIS and pan-sharpening software not named

---

## Contextual Interpretation

### Reproducibility (58, Moderate)

**Why this score:** This score reflects the asymmetric reproducibility profile common to papers using legacy data and licensed imagery. The analytical workflow is well-documented, but reproduction is blocked by data access rather than methodological opacity.

**What this means:** The conceptual reproducibility is high—someone with access to equivalent data could implement this workflow. The practical reproducibility is constrained by data licensing and absence of formal deposits.

**What readers should consider:** Researchers interested in reproducing or extending this work should contact the TRAP project directly for data access and code details. The methodological transparency supports independent implementation even if exact reproduction is not immediately feasible.

---

## Era Context

**Publication Year:** 2024
**Era:** Current
**Era Label:** Current era — FAIR and open science expectations established

**Expectations Note:** By 2024, data availability statements and code repositories with DOIs are increasingly expected, particularly for computational research. The paper's GitHub presence is consistent with era norms, but the absence of persistent identifiers and formal data deposits falls below emerging best practices for ML-based research.

---

## Detailed Signal Assessments

### Signal 1: Comprehensibility (78, Good)

The paper demonstrates strong comprehensibility with clearly stated hypotheses, operationally defined key terms, and transparent logical structure. The validation framework from hypothesis through testing to conclusion is explicit. Minor gaps exist in literature review methodology specification.

### Signal 2: Transparency (75, Good)

Research design is explicitly stated with clear validation framework. Methods are detailed with specific parameters. Data and code availability are documented through GitHub references. Major limitations are acknowledged. Falls short of Excellent due to absence of pre-registration and incomplete protocol documentation for some technical details.

### Signal 3: Plausibility (82, Excellent)

The core hypothesis is grounded in established ML and remote sensing theory. The negative results are theoretically coherent—the finding that CNNs learned spurious correlations is consistent with known challenges in transfer learning. Anomalous results are explicitly acknowledged and coherently explained.

### Signal 4: Validity (85, Excellent)

Excellent validity through independent ground-truth validation. The 773 mounds from TRAP 2009-2011 survey provide a robust, independently collected validation dataset. Sample is adequate (85 sq km), validation methodology is appropriate (spatial overlap detection), and alternative explanations are explicitly considered.

### Signal 5: Robustness (68, Good)

Good robustness through two-run comparison with different training data compositions. Both runs failed, providing evidence that results are robust to training data selection. Falls short of Excellent due to limited systematic sensitivity analysis of threshold, hyperparameters, and alternative architectures.

### Signal 6: Generalisability (72, Good)

Claims are explicitly bounded to Kazanlak Valley context and specific imagery. Limitations are thoroughly discussed. Recommendations are appropriately qualified. Falls short of Excellent because transfer conditions for other contexts are not systematically specified.

### Signal 7: Reproducibility (58, Moderate)

Standard pathway assessment. Data partially available, code shared with basic documentation, workflow partially documented. Falls short of Good (60-79) primarily due to no persistent identifiers, no formal data deposit, and incomplete environment specification.

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
      "framework": "deductive_emphasis",
      "quality_state": "high",
      "classification_confidence": "high"
    },
    "verdict": {
      "band": "good",
      "confidence": "high",
      "aggregate_score": 74,
      "aggregate_experimental": true
    },
    "signals": {
      "comprehensibility": { "score": 78, "band": "good" },
      "transparency": { "score": 75, "band": "good" },
      "plausibility": { "score": 82, "band": "excellent" },
      "validity": { "score": 85, "band": "excellent" },
      "robustness": { "score": 68, "band": "good" },
      "generalisability": { "score": 72, "band": "good" },
      "reproducibility": { "score": 58, "band": "moderate", "variant": "standard" }
    },
    "aggregates": {
      "cluster_1_rating": "strong",
      "cluster_2_rating": "strong",
      "cluster_3_rating": "adequate"
    },
    "infrastructure": {
      "fair_score": null,
      "fair_rating": "not_assessed",
      "fair_maximum": 40,
      "code_availability": "partial",
      "data_availability": "partial",
      "preregistration": "not_preregistered"
    },
    "era_context": {
      "publication_year": 2024,
      "era": "current",
      "era_label": "Current era — FAIR and open science expectations established",
      "expectations_note": "By 2024, data availability statements and code repositories with DOIs are increasingly expected"
    },
    "assessment_metadata": {
      "assessment_date": "2025-12-06",
      "assessor_version": "v1.0",
      "schema_version": "1.0"
    }
  }
}
```

---

## Assessment Lineage

| Pass | Output | Status |
|------|--------|--------|
| 0-7 | extraction.json | Complete |
| 8 | classification.json | Complete |
| 8.5 | track-a-quality.md | HIGH |
| 9a | cluster-1-foundational-clarity.md | Strong |
| 9b | cluster-2-evidential-strength.md | Strong |
| 9c | cluster-3-reproducibility.md | Adequate |
| 10 | credibility-report.md | Complete |

---

**End of Credibility Assessment Report**
