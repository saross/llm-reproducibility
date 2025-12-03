# Credibility Assessment Report

**Paper:** Early contact between late farming and pastoralist societies in southeastern Europe
**Slug:** penske-et-al-2023
**DOI:** 10.1038/s41586-023-06334-8
**Publication Year:** 2023

**Assessment Date:** 2025-12-01
**Assessor Version:** v1.0
**Schema Version:** 1.0

---

## Executive Summary

**Verdict:** Good | **Aggregate Score:** 77/100 (EXPERIMENTAL) | **Confidence:** HIGH

This empirical research article using deductive (hypothesis-testing) reasoning demonstrates strong methodological transparency and evidential support for claims about early genetic contact between farming and pastoralist populations in southeastern Europe. Published in 2023, it reflects current era expectations for open science with exemplary data sharing but a gap in code availability.

**Key Strengths:**
- Raw sequence data openly available in ENA (PRJEB62503) with FAIR score 35/40
- Multiple complementary methods (PCA, qpAdm, f-statistics, IBD, ROH) provide convergent evidence
- Claims clearly bounded by geography, chronology, and sampled populations

**Key Concerns:**
- No code repository for analysis scripts (common in archaeogenetics but limits exact reproducibility)

**Bottom Line:** A methodologically sound archaeogenetics study meeting current disciplinary standards for transparency and reproducibility, with strong theoretical grounding and appropriate scope constraints.

---

## Signal Scores Dashboard

| # | Signal | Score | Band | Cluster |
|---|--------|-------|------|---------|
| 1 | Comprehensibility | 82 | Excellent | Foundational Clarity |
| 2 | Transparency | 78 | Good | Foundational Clarity |
| 3 | Plausibility | 80 | Excellent | Evidential Strength |
| 4 | Validity | 78 | Good | Evidential Strength |
| 5 | Robustness | 75 | Good | Evidential Strength |
| 6 | Generalisability | 76 | Good | Evidential Strength |
| 7 | Reproducibility | 68 | Good | Reproducibility |

**Score Range:** 68-82 | **Mean:** 76.7

---

## Classification Summary

| Attribute | Value |
|-----------|-------|
| Paper Type | Research article |
| Paper Subtype | Empirical archaeogenetics |
| Research Approach | Deductive (hypothesis-testing) |
| Assessment Framework | Scientific empirical |
| Quality State | HIGH |
| Classification Confidence | HIGH |

---

## Cluster 1: Foundational Clarity

**Rating:** Strong

The paper demonstrates excellent comprehensibility with hypotheses explicitly stated and clearly bounded to southeastern Europe, 5400-2400 BC. Research design rationale is transparent, and key genetic/statistical terms are operationally defined. Transparency is good with strong data sharing (ENA PRJEB62503, 5 protocols.io DOIs) but limited by absence of code repository.

**Key Strengths:**
- Clear research question with explicit temporal and spatial bounds
- 19 methods and 39 protocols documented
- FAIR score 35/40 indicates strong data sharing practices

**Key Weaknesses:**
- No code repository for analysis scripts
- No author ORCIDs

---

## Cluster 2: Evidential Strength

**Rating:** Strong

The paper demonstrates strong evidential strength across all four signals. Claims are well-grounded in established population genetics theory with multiple methods providing convergent evidence. The sample of 135 individuals across 3000 years provides adequate support for population-level claims. Scope is appropriately bounded with limitations acknowledged.

**Key Strengths:**
- Multiple independent methods (PCA, qpAdm, f-statistics, IBD, ROH) converge
- Adequate sample for claims made (n=135 across 8 sites)
- Alternative ancestry models explicitly tested with statistical criteria

**Key Weaknesses:**
- No formal sensitivity analysis for qpAdm parameters
- Uneven site representation limits some generalisations

---

## Cluster 3: Reproducibility

**Rating:** Adequate
**Pathway:** Standard (computational)

The paper has excellent data availability (raw sequences in ENA with open access) but incomplete code documentation. Standard archaeogenetics tools are specified with versions (ADMIXTOOLS v5.1, EAGER v1.92.56, etc.), enabling reproduction by experienced practitioners. However, custom scripts and configurations are not shared.

**Reproducibility Readiness:**
- **Inputs:** Available (ENA PRJEB62503)
- **Code:** Partial (tools specified, no scripts)
- **Environment:** Partial (versions listed)
- **Feasibility:** Needs work (pipeline reconstruction required)

**Key Strengths:**
- Raw data openly available with persistent identifier
- All software tools specified with versions
- Supplementary outputs enable verification

**Key Weaknesses:**
- No analysis code repository
- Pipeline workflow must be inferred from text

---

## Infrastructure & FAIR Summary

| Component | Status |
|-----------|--------|
| **FAIR Score** | 35/40 (Good) |
| Findable | 9/10 |
| Accessible | 10/10 |
| Interoperable | 8/10 |
| Reusable | 8/10 |
| **Data Availability** | Available (ENA PRJEB62503) |
| **Code Availability** | Not available (standard tools documented) |
| **Preregistration** | Not applicable |
| **Paper DOI** | Present |
| **Data PID** | Present (ENA accession) |
| **Protocol DOIs** | 5 protocols.io references |
| **Author ORCIDs** | Not present |

**Infrastructure Gaps:**
- No code repository for custom analysis scripts
- No author ORCIDs listed

---

## Era Context

**Publication Year:** 2023
**Era:** Current (2020-present)
**Label:** Current era — FAIR and open science expectations established

This paper was published in an era where data sharing is expected and FAIR principles are increasingly standard. The paper meets these expectations for data availability (exemplary) and partially meets them for code availability (standard tools documented, custom scripts absent). This pattern is common in archaeogenetics where standardised pipelines are used.

---

## Contextual Interpretation

### Reproducibility (68, Good)

**Why this score:** The paper uses standard archaeogenetics tools (ADMIXTOOLS, EAGER) with versions specified, enabling reproduction by practitioners familiar with these pipelines. However, the absence of custom analysis scripts means that exact reproduction requires inferring workflow configurations from the methods section.

**What this means:** Technical and analytical reproducibility is achievable with moderate effort by an experienced archaeogeneticist. The score reflects the gap between "tools documented" (good) and "workflow executable" (not yet achieved).

**What readers should consider:** For exact reproduction, expect to reconstruct the analysis pipeline from methods text and supplementary materials. The use of standard tools and availability of intermediate outputs increases confidence that reproduction would yield consistent results.

---

## Aggregate Assessment (EXPERIMENTAL)

| Metric | Value |
|--------|-------|
| Aggregate Score | 77/100 |
| Verdict Band | Good |
| Confidence | HIGH |

⚠️ **Note:** Aggregate scoring across signals is experimental. We are investigating what combined scores mean and how they should be interpreted across different paper types.

**Score Composition:**
- Foundational Clarity: Strong (Comprehensibility 82, Transparency 78)
- Evidential Strength: Strong (Plausibility 80, Validity 78, Robustness 75, Generalisability 76)
- Reproducibility: Adequate (Reproducibility 68)

The "Good" verdict reflects consistent performance across all signals (range 68-82) with no major credibility gaps. The lowest score (Reproducibility 68) reflects a common pattern in archaeogenetics rather than a paper-specific deficiency.

---

## Structured Output

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
      "paper_type": "research_article",
      "paper_subtype": "empirical_archaeogenetics",
      "approach": "deductive",
      "framework": "scientific_empirical",
      "quality_state": "HIGH",
      "classification_confidence": "HIGH"
    },
    "verdict": {
      "band": "good",
      "confidence": "HIGH",
      "aggregate_score": 77,
      "aggregate_experimental": true
    },
    "signals": {
      "comprehensibility": { "score": 82, "band": "excellent" },
      "transparency": { "score": 78, "band": "good" },
      "plausibility": { "score": 80, "band": "excellent" },
      "validity": { "score": 78, "band": "good" },
      "robustness": { "score": 75, "band": "good" },
      "generalisability": { "score": 76, "band": "good" },
      "reproducibility": { "score": 68, "band": "good", "variant": "standard" }
    },
    "aggregates": {
      "cluster_1_rating": "strong",
      "cluster_2_rating": "strong",
      "cluster_3_rating": "adequate"
    },
    "infrastructure": {
      "fair_score": 35,
      "fair_rating": "good",
      "fair_maximum": 40,
      "code_availability": "not_available",
      "data_availability": "available",
      "preregistration": "not_applicable"
    },
    "era_context": {
      "publication_year": 2023,
      "era": "current",
      "era_label": "Current era (2020-present)",
      "expectations_note": "FAIR and open science expectations established; paper meets data sharing expectations, partially meets code sharing expectations"
    },
    "assessment_metadata": {
      "assessment_date": "2025-12-01",
      "assessor_version": "v1.0",
      "schema_version": "1.0"
    }
  }
}
```

---

**End of Credibility Assessment Report**
