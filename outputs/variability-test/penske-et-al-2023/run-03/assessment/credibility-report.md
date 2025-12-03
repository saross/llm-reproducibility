# Credibility Assessment Report

**Paper:** Early contact between late farming and pastoralist societies in southeastern Europe
**Slug:** penske-et-al-2023
**DOI:** 10.1038/s41586-023-06334-8
**Publication Year:** 2023
**Assessment Date:** 2025-12-02
**Assessor Version:** v1.0

---

## Executive Summary

**Verdict:** GOOD | **Confidence:** HIGH | **Aggregate Score:** 77 (EXPERIMENTAL)

This empirical paper using inductive reasoning demonstrates strong credibility across all assessment dimensions. Published in 2023, it falls in the current era of open science expectations where data sharing and transparent methods are expected.

**Key Strengths:**
- Comprehensive data archiving in ENA (PRJEB62503) with open access
- Multi-proxy analytical approach provides convergent evidence (PCA, qpAdm, f-statistics, IBD)
- Well-bounded geographic and temporal scope (SE Europe, 5400-2400 BC)
- Thorough methods documentation with software versions specified

**Key Concerns:**
- No custom code repository provided (analysis reconstruction required)

**Bottom Line:** A methodologically sound archaeogenomics study with excellent transparency and data sharing, demonstrating good practice for the 2023 publication environment. Analytical reproducibility achievable through documented software packages.

---

## Signal Scores Dashboard

| Signal | Score | Band | Cluster |
|--------|-------|------|---------|
| Comprehensibility | 82 | Excellent | Foundational Clarity |
| Transparency | 85 | Excellent | Foundational Clarity |
| Plausibility | 78 | Good | Evidential Strength |
| Validity | 80 | Excellent | Evidential Strength |
| Robustness | 75 | Good | Evidential Strength |
| Generalisability | 72 | Good | Evidential Strength |
| Reproducibility | 72 | Good | Reproducibility |

**Aggregate:** 77/100 (GOOD) — *EXPERIMENTAL: Aggregate scoring under development*

---

## Cluster Ratings

| Cluster | Rating | Pillar |
|---------|--------|--------|
| Cluster 1: Foundational Clarity | **Strong** | Transparency |
| Cluster 2: Evidential Strength | **Strong** | Credibility |
| Cluster 3: Reproducibility | **Adequate** | Reproducibility |

---

## Detailed Findings

### Cluster 1: Foundational Clarity (Strong)

The paper demonstrates excellent comprehensibility and transparency for inductive archaeogenomics research.

**Summary:** Research questions and exploratory goals are explicitly stated. Pattern descriptions are clear, well-bounded with quantitative precision. Methods documentation is comprehensive with 15 methods and 29 protocols captured. Data availability is excellent through ENA archiving.

**Key Strengths:**
- Explicit research goals for genetic contact investigation
- Clear, bounded pattern claims with geographic and temporal scope
- Comprehensive RDMAP extraction (48 items total)
- FAIR score 35/40 (87.5%)

**Key Weaknesses:**
- No custom code repository provided

---

### Cluster 2: Evidential Strength (Strong)

The paper shows consistent credibility across all four signals (Plausibility, Validity, Robustness, Generalisability).

**Summary:** Observed patterns are consistent with established archaeogenomic frameworks. Evidence is sufficient with 135 individuals from 8 sites across 4 chronological periods. Multi-proxy analytical approach provides triangulation. Claims are appropriately bounded to the SE Europe/Black Sea region.

**Key Strengths:**
- Substantial sample size (135 successfully analysed individuals)
- Systematic temporal transect sampling design
- Multiple analytical methods provide convergent evidence
- Appropriate geographic and temporal scoping

**Key Weaknesses:**
- Limited explicit sensitivity analysis of ancestry estimates
- Transfer conditions to other contact zones not fully specified

---

### Cluster 3: Reproducibility (Adequate)

**Pathway:** Standard (computational components present)

**Summary:** Data availability is excellent with ENA archiving. Code availability is limited — no custom repository, but analysis uses open-source packages with documented versions. Analytical reproducibility achievable with moderate effort.

**Key Strengths:**
- Data archived in ENA with open access (PRJEB62503)
- All primary software packages are open source
- Software versions specified throughout Methods
- FAIR compliance strong (87.5%)

**Key Weaknesses:**
- No custom code repository or automated pipeline
- Environment specification incomplete
- Pipeline reconstruction required for reproduction

**Execution Feasibility:** Needs work — data accessible, methods documented, but pipeline reconstruction required from Methods text.

---

## Infrastructure & FAIR Summary

| Component | Status | Details |
|-----------|--------|---------|
| **FAIR Score** | 35/40 (87.5%) | Strong compliance |
| **Data Availability** | ✅ Available | ENA PRJEB62503, open access |
| **Code Availability** | ⚠️ Partial | No repository; published packages documented |
| **Preregistration** | ❌ Not applicable | Exploratory research |
| **DOI** | ✅ Present | 10.1038/s41586-023-06334-8 |
| **Author ORCIDs** | ❌ Not extracted | Not present in extraction |

**Infrastructure Gaps:**
- Custom code repository absent
- Complete computational environment not documented

---

## Contextual Interpretation

### Era Context

**Publication Year:** 2023
**Era:** Current (2020-present)
**Expectations:** FAIR and open science expectations established. Data sharing expected in major repositories. Code sharing increasingly expected but not yet universal.

The reproducibility score of 72 reflects good practice for 2023 — data sharing is exemplary (ENA archiving), while the absence of a custom code repository reflects evolving norms rather than poor practice.

### Approach-Specific Notes

**Inductive Research:** This exploratory archaeogenomics study appropriately uses pattern-discovery methods. Pre-registration is not expected for inductive research. The Transparency score (85) reflects excellent workflow documentation without penalising absence of pre-registered hypotheses.

---

## JSON Output

```json
{
  "credibility_report": {
    "version": "1.0",
    "paper": {
      "slug": "penske-et-al-2023",
      "title": "Early contact between late farming and pastoralist societies in southeastern Europe",
      "doi": "10.1038/s41586-023-06334-8",
      "publication_year": 2023
    },
    "classification": {
      "paper_type": "empirical",
      "paper_subtype": null,
      "approach": "inductive",
      "framework": "inductive_emphasis",
      "quality_state": "high",
      "classification_confidence": "high"
    },
    "verdict": {
      "band": "good",
      "confidence": "high",
      "aggregate_score": 77,
      "aggregate_experimental": true
    },
    "signals": {
      "comprehensibility": { "score": 82, "band": "excellent" },
      "transparency": { "score": 85, "band": "excellent" },
      "plausibility": { "score": 78, "band": "good" },
      "validity": { "score": 80, "band": "excellent" },
      "robustness": { "score": 75, "band": "good" },
      "generalisability": { "score": 72, "band": "good" },
      "reproducibility": { "score": 72, "band": "good", "variant": "standard" }
    },
    "aggregates": {
      "cluster_1_rating": "strong",
      "cluster_2_rating": "strong",
      "cluster_3_rating": "adequate"
    },
    "infrastructure": {
      "fair_score": 35,
      "fair_rating": "excellent",
      "fair_maximum": 40,
      "code_availability": "partial",
      "data_availability": "available",
      "preregistration": "not_applicable"
    },
    "era_context": {
      "publication_year": 2023,
      "era": "current",
      "era_label": "Current era (2020-present)",
      "expectations_note": "FAIR and open science expectations established. Data sharing expected; code sharing increasingly expected."
    },
    "assessment_metadata": {
      "assessment_date": "2025-12-02",
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
| Assessment Date | 2025-12-02 |
| Assessor Version | v1.0 |
| Schema Version | 2.6 |
| Quality State | HIGH |
| Classification Confidence | HIGH |

**Note:** Aggregate score (77) is EXPERIMENTAL. The meaning and utility of aggregate credibility scores across diverse paper types is under investigation.

---

*Report generated as part of LLM Reproducibility Project variability testing (run-03)*
