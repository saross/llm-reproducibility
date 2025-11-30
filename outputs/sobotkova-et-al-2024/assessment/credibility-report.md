# Credibility Assessment Report

**Paper:** Validating predictions of burial mounds with field data: the promise and reality of machine learning  
**Authors:** Sobotkova, Kristensen-McLachlan, Mallon, Ross  
**DOI:** [10.1108/JD-05-2022-0096](https://doi.org/10.1108/JD-05-2022-0096)  
**Publication Year:** 2024

**Assessment Date:** 2025-11-30  
**Assessor Version:** v1.0  
**Schema Version:** 1.0

---

## Executive Summary

> **Verdict:** Good | **Confidence:** HIGH
>
> This **empirical** paper using **deductive** reasoning demonstrates strong methodological rigour with honest reporting of negative results. Published in 2024 (current era), it meets contemporary expectations for code sharing while falling slightly short on data archiving.
>
> **Key Strengths:**
> - Excellent external validation design comparing ML predictions against comprehensive field survey ground truth
> - Exemplary code transparency with three GitHub repositories documenting complete workflow
> - Honest reporting of negative results — model failed, not reframed as success
>
> **Key Concerns:**
> - Historical field survey data (773 mounds) not deposited in public repository
>
> **Bottom Line:** A methodologically rigorous validation study that honestly documents ML limitations, providing valuable negative results for the ML-for-archaeology community.

---

## Verdict & Classification

| Aspect | Value |
|--------|-------|
| **Verdict Band** | Good |
| **Aggregate Score** | 76/100 (EXPERIMENTAL) |
| **Confidence Level** | HIGH |
| **Quality State** | HIGH |
| **Paper Type** | Empirical |
| **Research Approach** | Deductive |
| **Framework Applied** | Deductive emphasis (Validity, Robustness, Reproducibility prioritised) |

---

## Signal Scores Dashboard

| # | Signal | Score | Band | Context |
|---|--------|-------|------|---------|
| 1 | Comprehensibility | 82 | Excellent | — |
| 2 | Transparency | 74 | Good | — |
| 3 | Plausibility | 78 | Good | — |
| 4 | Validity | 80 | Excellent | — |
| 5 | Robustness | 72 | Good | — |
| 6 | Generalisability | 76 | Good | — |
| 7 | Reproducibility | 71 | Good | Standard pathway |

**Aggregate:** 76/100 ⚠️ *EXPERIMENTAL — we are investigating what aggregate scores mean*

---

## Cluster Summaries

### Cluster 1: Foundational Clarity (Transparency Pillar)

**Rating:** Strong

This cluster assesses whether the work is documented and understandable. The paper demonstrates excellent comprehensibility for hypothesis-testing research, with clear claims, operational definitions, and transparent logical structure. Transparency is good, with exemplary code sharing offset by incomplete data archiving.

| Signal | Score | Band |
|--------|-------|------|
| Comprehensibility | 82 | Excellent |
| Transparency | 74 | Good |

**Key Strengths:**
- Hypotheses explicitly stated and clearly bounded
- Three GitHub repositories with complete workflow documentation
- Detailed protocols (12) document analytical procedures

**Key Weaknesses:**
- No explicit data availability statement for field survey data
- Historical field data (773 mounds) not deposited

---

### Cluster 2: Evidential Strength (Credibility Pillar)

**Rating:** Strong

This cluster addresses the core question: How much faith can we put in the results? The paper demonstrates strong evidential strength across all four signals, with highest scores on Validity (external validation design) and lowest on Robustness (limited sensitivity analysis beyond two-run comparison).

| Signal | Score | Band |
|--------|-------|------|
| Plausibility | 78 | Good |
| Validity | 80 | Excellent |
| Robustness | 72 | Good |
| Generalisability | 76 | Good |

**Key Strengths:**
- External validation against comprehensive field survey ground truth (773 mounds)
- Two-run comparative design provides internal robustness test
- Claims appropriately bounded to Kazanlak Valley context
- Honest acknowledgement of model failure

**Key Weaknesses:**
- Limited sensitivity analysis beyond training data curation comparison
- Transfer conditions implicit rather than explicit

---

### Cluster 3: Reproducibility (Reproducibility Pillar)

**Rating:** Adequate

This cluster assesses whether computational aspects can be re-executed. The paper demonstrates good computational reproducibility with excellent code sharing but incomplete data availability.

| Signal | Score | Band | Pathway |
|--------|-------|------|---------|
| Reproducibility | 71 | Good | Standard |

**Key Strengths:**
- Three GitHub repositories (cnn-testing, burial-mounds, MoundDetection)
- Open-source tools (Python, R) enable full code reproducibility
- FAIR score of 75% (12/16)

**Key Weaknesses:**
- Field survey ground truth data not deposited
- No explicit data availability statement
- Environment specification incomplete (no version pinning)

**Execution Feasibility:** Needs Work — Code reproducible but complete validation blocked by field data access gap

---

## Era Context

**Publication Year:** 2024  
**Era:** Current (2020-present)  
**Era Label:** Current era — FAIR and open science expectations established

**Interpretation:** Published in 2024, this paper is assessed against contemporary open science expectations. The excellent code sharing meets current standards. The data availability gap (historical field data not deposited) falls slightly short of 2024 best practice, though this reflects common challenges with legacy field data collected before current open data norms.

---

## Infrastructure & FAIR Summary

| Aspect | Status | Details |
|--------|--------|---------|
| **FAIR Score** | 12/16 (75%) | Highly FAIR |
| **FAIR Rating** | Highly FAIR | Strong on Findable, Accessible, Interoperable; minor gaps on Reusable |
| **Code Availability** | Available | 3 GitHub repositories (R, Python) |
| **Data Availability** | Partial | Code available; field survey data NOT deposited |
| **Preregistration** | Not Preregistered | Retrospective study — pre-registration not applicable |
| **PID Coverage** | Partial | Paper DOI present; no author ORCIDs visible; no code DOIs |

**Infrastructure Gaps:**
- Field survey data (773 mounds) should be deposited in appropriate repository (tDAR, Open Context, Zenodo)
- Code releases should be minted with DOIs via Zenodo-GitHub integration
- Author ORCIDs should be added to journal metadata
- Explicit data availability statement needed

---

## Detailed Findings

### Comprehensibility (82, Excellent)

The paper demonstrates excellent comprehensibility for deductive research. The central hypothesis (can pre-trained CNNs detect burial mounds?) is explicitly stated and tested. Claims are structured as performance assessments with quantitative precision — the 12.8% precision and 95.7% false negative rates provide clear, evaluable findings. Key terms (transfer learning, CNN, ResNet-50) are operationally defined. The logical structure follows classic deductive workflow: prediction → test → conclusion.

### Transparency (74, Good)

Research design is explicitly documented through four formal research designs (RD001-RD004). Code transparency is exemplary with three GitHub repositories covering the complete workflow. However, data transparency has gaps: no explicit data availability statement exists, and the historical field survey data (773 mounds from TRAP 2009-2011) is not deposited. This asymmetric transparency (excellent code, incomplete data) is common in computational archaeology using legacy field data.

### Plausibility (78, Good)

The hypothesis is theoretically grounded in transfer learning literature and archaeological remote sensing. The paper appropriately situates itself within the publication bias discourse, positioning negative results as a valuable contribution. Crucially, when the model failed, the authors investigated and explained why (CNN detected confounding features rather than mounds) — this honest engagement with anomalous results strengthens plausibility.

### Validity (80, Excellent)

The paper's core strength is its validation design. Rather than relying on potentially misleading internal accuracy metrics (F1 scores from train/test splits), the authors validated against independent field survey data from TRAP. The 773 mounds documented through systematic pedestrian survey provide robust ground truth. The paper explicitly distinguishes internal vs external validation, demonstrating methodological sophistication.

### Robustness (72, Good)

The two-run design (2021 vs 2022 with curated training data) provides a built-in sensitivity test. Both runs failed consistently, suggesting the conclusion is robust to training data composition. However, sensitivity analysis is not comprehensive: threshold sensitivity is not systematically tested, alternative architectures beyond ResNet-50 are not explored, and cross-validation is not reported.

### Generalisability (76, Good)

Claims are appropriately bounded to the Kazanlak Valley context. The paper explicitly acknowledges that heterogeneous landscapes with confounding features pose challenges for CNN detection. Transfer conditions are implied (homogeneous landscapes might yield better results) but not formally specified. The paper positions itself as a "cautionary tale" for potential adopters rather than making universal claims.

### Reproducibility (71, Good)

Computational reproducibility is good. Code is available in three GitHub repositories using open-source tools (Python, R). However, complete reproduction is limited by data gaps: the field survey ground truth is not deposited, satellite imagery would need separate access, and environment specifications are not detailed. An independent researcher could reproduce the CNN training but not the specific external validation.

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
      "paper_subtype": "ML validation study",
      "approach": "deductive",
      "framework": "deductive_emphasis",
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
      "comprehensibility": { "score": 82, "band": "Excellent" },
      "transparency": { "score": 74, "band": "Good" },
      "plausibility": { "score": 78, "band": "Good" },
      "validity": { "score": 80, "band": "Excellent" },
      "robustness": { "score": 72, "band": "Good" },
      "generalisability": { "score": 76, "band": "Good" },
      "reproducibility": { "score": 71, "band": "Good", "variant": "standard" }
    },
    "aggregates": {
      "cluster_1_rating": "Strong",
      "cluster_2_rating": "Strong",
      "cluster_3_rating": "Adequate"
    },
    "infrastructure": {
      "fair_score": 12,
      "fair_rating": "highly_fair",
      "fair_maximum": 16,
      "code_availability": "available",
      "data_availability": "partial",
      "preregistration": "not_applicable"
    },
    "era_context": {
      "publication_year": 2024,
      "era": "current",
      "era_label": "Current era — FAIR and open science expectations established",
      "expectations_note": "2024 paper meets code sharing expectations but falls slightly short on data archiving"
    },
    "assessment_metadata": {
      "assessment_date": "2025-11-30",
      "assessor_version": "v1.0",
      "schema_version": "1.0"
    }
  }
}
```

---

*Generated by Research Assessor v1.0 | Assessment Framework: Three Pillars (Transparency, Credibility, Reproducibility)*
