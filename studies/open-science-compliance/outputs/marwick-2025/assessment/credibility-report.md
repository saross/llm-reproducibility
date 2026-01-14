# Credibility Assessment Report

**Paper:** marwick-2025
**Title:** Is archaeology a science? Insights and imperatives from 10,000 articles and a year of reproducibility reviews
**DOI:** 10.1016/j.jas.2025.106281
**Publication Year:** 2025

**Assessment Date:** 2026-01-14
**Assessor Version:** v1.0
**Schema Version:** 1.0

---

## Executive Summary

**Verdict:** Excellent | **Confidence:** HIGH

This meta_research paper using inductive reasoning demonstrates exemplary credibility across all assessment dimensions. Publication in 2025 places it in the current era where FAIR and open science expectations are established.

**Key Strengths:**
- Exceptional reproducibility infrastructure (93.75% FAIR compliance) with complete research compendium
- Clear theoretical grounding in established Fanelli & Glänzel (2013) bibliometric framework
- Strong transparency with explicit methodology and documented workflow

**Key Concerns:**
- Single-reviewer reproducibility assessment component lacks inter-rater reliability
- Some implicit assumptions about bibliometric-consensus validity

**Bottom Line:** This paper exemplifies the reproducibility practices it advocates, providing a credible evidence base for understanding archaeology's scientific status and reproducibility challenges.

---

## Signal Scores Dashboard

| Signal | Score | Band | Context |
|--------|-------|------|---------|
| Comprehensibility | 85 | excellent | — |
| Transparency | 90 | excellent | — |
| Plausibility | 80 | excellent | — |
| Validity | 78 | good | — |
| Robustness | 68 | good | — |
| Generalisability | 75 | good | — |
| Reproducibility | 90 | excellent | 🔧 |

**Aggregate Score:** 81/100 (Excellent) ⚠️ EXPERIMENTAL

*Note: Aggregate score calculation is experimental. We are investigating what this composite metric means.*

---

## Cluster Summaries

### Cluster 1: Foundational Clarity — Strong

The paper demonstrates strong foundational clarity with excellent comprehensibility (85) and transparency (90). Research goals are explicitly stated, key terms are operationally defined, and the logical progression from data to patterns is transparent. The research compendium with 93.75% FAIR compliance represents exemplary transparency.

**Key Strengths:**
- Explicit research goals with clear rationale
- All five bibliometric variables operationally defined
- Complete research compendium with DOI and open licences

**Key Weaknesses:**
- 5 implicit arguments indicate minor reasoning gaps
- Bibliometric-consensus theoretical link assumed rather than validated

---

### Cluster 2: Evidential Strength — Strong

The paper demonstrates strong evidential strength across all four signals (68-80). Plausibility is excellent (80) due to grounding in established frameworks. Validity (78) reflects systematic sampling with some single-reviewer limitations. Robustness (68) shows good triangulation via five bibliometric variables but lacks inter-rater reliability for reproducibility categorisation. Generalisability (75) features explicit scope boundaries and thoughtful applicability discussion.

**Key Strengths:**
- Large bibliometric sample (9,697 papers, 50 years, 20 journals)
- Five-variable triangulation provides convergent evidence
- Extensive discussion of applicability limits (Section 7)

**Key Weaknesses:**
- Single-reviewer reproducibility assessment without reliability check
- H-index journal selection may exclude regional/innovative work
- Issue taxonomy methodology undocumented

---

### Cluster 3: Reproducibility — Strong

**Pathway:** Standard (computational meta-research)

The paper demonstrates excellent reproducibility (90) with all components available for reproduction attempt. Complete R code and data are archived in Zenodo with DOI and open licences. FAIR compliance is 93.75%. The paper exemplifies the reproducibility practices it advocates.

**Key Strengths:**
- Complete research compendium (DOI: 10.5281/zenodo.14897252)
- Explicit open licences (MIT code, CC-0 data)
- Paper demonstrates practices it recommends

**Key Weaknesses:**
- Environment specification not detailed in manuscript text
- Runtime/execution time not documented

**Execution Feasibility:** Ready — Priority candidate for reproduction attempt

---

## Contextual Interpretation

### Reproducibility (90, Excellent) 🔧

**Why this score:** This computational meta-research paper achieves excellent reproducibility through exemplary infrastructure: complete code, archived data, persistent identifiers, and open licences. The author, as JAS Associate Editor for Reproducibility, demonstrates the practices advocated in the paper itself.

**What this means:** Readers can expect to reproduce all figures, tables, and statistical tests from the provided materials. The research compendium follows contemporary best practices.

**What readers should consider:** While computational reproducibility is high, the reproducibility review findings reflect single-reviewer judgments. Readers evaluating the failure taxonomy should consider that category boundaries may involve subjective interpretation.

---

## Infrastructure & FAIR Summary

| Component | Status | Details |
|-----------|--------|---------|
| **FAIR Score** | 30/32 (93.75%) | Highly FAIR for both data and code |
| **Code Availability** | Available | Zenodo, MIT licence |
| **Data Availability** | Available | Zenodo, CC-0 licence |
| **Preregistration** | Not preregistered | Appropriate for exploratory meta-research |
| **Paper DOI** | Present | 10.1016/j.jas.2025.106281 |
| **Software DOI** | Present | 10.5281/zenodo.14897252 |
| **Author ORCID** | Not provided | Gap in PID coverage |

**Infrastructure gaps:** Author ORCID not provided in paper. No formal preregistration (not expected for inductive research).

---

## Era Context

**Publication Year:** 2025
**Era:** Current (2020-present)
**Era Label:** "FAIR and open science expectations established"

**Expectations Note:** Papers from 2025 are expected to provide data/code sharing, use persistent identifiers, and document computational workflows. This paper exceeds contemporary expectations with 93.75% FAIR compliance and complete research compendium.

---

## Detailed Signal Assessments

### Signal 1: Comprehensibility (85, Excellent)

Research goals explicitly stated with clear rationale. Key terms (hardness/softness, consensus, bibliometric variables) operationally defined. Pattern descriptions bounded and qualified. Logical progression from observations to patterns transparent. Minor gaps due to 5 implicit arguments requiring reader inference.

### Signal 2: Transparency (90, Excellent)

Exemplary transparency via research compendium. Complete R code and data archived with DOIs. Explicit open licences. 10 explicit methods and 9 explicit protocols document procedures. FAIR compliance 93.75%. Minor gaps: 2 implicit research designs, environment specification partial in manuscript.

### Signal 3: Plausibility (80, Excellent)

Patterns grounded in established Fanelli & Glänzel (2013) framework. Anomalies acknowledged and contextualised (Journal of Cultural Heritage outlier, mixed temporal trends). Interpretations consistent with disciplinary knowledge. Gap: bibliometric-consensus link assumed without independent validation.

### Signal 4: Validity (78, Good)

Large bibliometric sample (9,697 papers) with systematic WoS query. Multiple statistical approaches (GAMs, PCA, concordance). Sampling criteria explicit. Limitations: single-reviewer reproducibility assessment, h-index selection may bias sample, small reproducibility review sample (25 manuscripts).

### Signal 5: Robustness (68, Good)

Five bibliometric variables provide triangulation. Kendall's concordance (Wt=0.64) validates variable agreement. Low r-squared values transparently reported. Limitations: no inter-rater reliability for reproducibility categorisation, issue taxonomy undocumented, no formal sensitivity analysis.

### Signal 7: Generalisability (75, Good)

Pattern claims explicitly bounded (h-index journals, 1975-2025). Section 7 provides extensive applicability discussion for qualitative research. Claims appropriately qualified ("on average"). Limitations: Anglophone focus not prominently discussed, JAS-only reproducibility rates may not generalise.

### Signal 6: Reproducibility (90, Excellent)

Complete research compendium with DOI. Code (MIT) and data (CC-0) openly available. FAIR compliance 93.75%. Paper exemplifies practices it advocates. Execution feasibility: ready for reproduction attempt. Gap: environment specification partial in manuscript (likely complete in compendium).

---

## Structured Output

```json
{
  "credibility_report": {
    "version": "1.0",
    "paper": {
      "slug": "marwick-2025",
      "title": "Is archaeology a science? Insights and imperatives from 10,000 articles and a year of reproducibility reviews",
      "doi": "10.1016/j.jas.2025.106281",
      "publication_year": 2025
    },
    "classification": {
      "paper_type": "meta_research",
      "paper_subtype": "bibliometric_analysis_reproducibility_review",
      "approach": "inductive",
      "framework": "inductive_emphasis",
      "quality_state": "high",
      "classification_confidence": "high"
    },
    "verdict": {
      "band": "excellent",
      "confidence": "high",
      "aggregate_score": 81,
      "aggregate_experimental": true
    },
    "signals": {
      "comprehensibility": { "score": 85, "band": "excellent" },
      "transparency": { "score": 90, "band": "excellent" },
      "plausibility": { "score": 80, "band": "excellent" },
      "validity": { "score": 78, "band": "good" },
      "robustness": { "score": 68, "band": "good" },
      "generalisability": { "score": 75, "band": "good" },
      "reproducibility": { "score": 90, "band": "excellent", "context_flag": "🔧", "variant": "standard" }
    },
    "aggregates": {
      "cluster_1_rating": "strong",
      "cluster_2_rating": "strong",
      "cluster_3_rating": "strong"
    },
    "infrastructure": {
      "fair_score": 30,
      "fair_rating": "highly_fair",
      "fair_maximum": 32,
      "fair_percentage": 93.75,
      "code_availability": "available",
      "data_availability": "available",
      "preregistration": "not_preregistered"
    },
    "era_context": {
      "publication_year": 2025,
      "era": "current",
      "era_label": "FAIR and open science expectations established",
      "expectations_note": "Paper exceeds contemporary expectations with 93.75% FAIR compliance"
    },
    "assessment_metadata": {
      "assessment_date": "2026-01-14",
      "assessor_version": "v1.0",
      "schema_version": "1.0"
    }
  }
}
```

---

## Assessment Validity Notes

- **Quality State:** HIGH — Enables precise scoring and full assessment
- **Classification Confidence:** HIGH — Clear inductive meta-research classification
- **Approach Anchors:** Inductive anchors applied throughout
- **Context Flags Applied:** 🔧 (methodological transparency) for Reproducibility signal

---

**End of Credibility Report**
