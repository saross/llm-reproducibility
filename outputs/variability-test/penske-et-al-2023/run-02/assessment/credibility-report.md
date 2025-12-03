# Credibility Assessment Report

**Paper:** Early contact between late farming and pastoralist societies in southeastern Europe
**Slug:** penske-et-al-2023
**DOI:** 10.1038/s41586-023-06334-8
**Run:** run-02 (variability test)
**Assessment Date:** 2025-12-02
**Assessor Version:** v1.0

---

## Executive Summary

**Verdict:** GOOD | **Confidence:** High

**Paper Type:** Empirical (archaeogenomics)
**Research Approach:** Inductive
**Publication Era:** Early Majority (2023)

This Nature archaeogenomics paper presents genome-wide data from 135 ancient individuals spanning ~5400-2400 BC to investigate genetic contact between late Copper Age farming societies and early pastoralist groups in southeastern Europe. The paper proposes that early contact during the fourth millennium BC was integral to the formation of Yamnaya pastoralists. Assessment reveals strong foundational clarity and evidential strength, with adequate reproducibility limited by absent code repository.

**Key Strengths:**

- Comprehensive dataset (135 individuals, 8 sites, 3000-year span) with systematic temporal coverage
- Multiple complementary analytical methods (PCA, f-statistics, qpAdm, IBD, ROH) providing robust triangulation
- Excellent data archiving (ENA PRJEB62503) with open access meeting Nature requirements

**Key Concerns:**

- No code repository despite substantial computational analyses
- Interpretive leap from genetic admixture to technology/innovation transfer not fully justified
- Some analytical thresholds (SNP cutoffs, outgroup selection) undocumented

**Bottom Line:** A methodologically rigorous archaeogenomics study with strong genetic evidence for early contact between farming and pastoral populations. Documentation meets high standards for claims about genetic patterns; interpretive claims about cultural processes extend beyond direct evidence. Computational reproduction requires workflow reconstruction due to missing code.

---

## Classification Summary

| Dimension | Value |
|-----------|-------|
| **Paper Type** | Empirical (archaeogenomics) |
| **Research Approach** | Inductive |
| **Framework Applied** | inductive_emphasis |
| **Quality State** | HIGH |
| **Classification Confidence** | High |
| **Publication Year** | 2023 |
| **Era Context** | Early Majority (2020-2025) |

### Quality State Implications

HIGH quality state enables full credibility assessment with precise scoring (±5 point precision). All extraction arrays fully populated, cross-references validated, and classification unambiguous.

### Paper Type Context

This is an inductive archaeogenomics study that systematically documents genetic patterns across a temporal transect and interprets them within an historical framework. Pre-registration not expected for exploratory research. Emphasis on data archiving (achieved) and workflow documentation (partial).

---

## Signal Scores Dashboard

| Signal | Score | Band | Cluster | Context Flag |
|--------|-------|------|---------|--------------|
| Comprehensibility | 78 | Good | 1 | — |
| Transparency | 75 | Good | 1 | — |
| Plausibility | 76 | Good | 2 | — |
| Validity | 80 | Excellent | 2 | — |
| Robustness | 75 | Good | 2 | — |
| Generalisability | 72 | Good | 2 | — |
| Reproducibility | 62 | Good | 3 | — |

**Aggregate Score:** 74/100 (GOOD) *[EXPERIMENTAL]*

> **Note:** The aggregate score is experimental. We are investigating what it means and whether to retain it. Equal weights are used across all 7 signals.

### Context Flag Key

| Flag | Meaning |
|------|---------|
| — | Default expectations apply |
| ⚠️ | Score expected to differ from typical empirical paper |
| 🔧 | Methodological variant anchors applied |

---

## Detailed Findings

### Cluster 1: Foundational Clarity

**Rating:** Strong

Both Comprehensibility (78) and Transparency (75) fall in the Good band, demonstrating the strong foundational documentation typical of Nature publications. Research goals are explicit, pattern descriptions precise with statistical support, and the Methods section comprehensive with software versions documented. FAIR assessment shows 12/16 (moderately_fair) with strengths in Findability and Accessibility.

**Strengths:**

- Explicit research goals with clear temporal/geographic scope
- Comprehensive Methods with all software versions documented
- Data archived in ENA (PRJEB62503) with open access

**Weaknesses:**

- Interpretive framework connecting genetic to cultural evidence is implicit
- No code repository despite computational analyses
- Some analytical thresholds (SNP cutoffs, outgroup selection) undocumented

---

### Cluster 2: Evidential Strength

**Rating:** Strong

All four credibility signals (Plausibility 76, Validity 80, Robustness 75, Generalisability 72) fall in the Good-to-Excellent range. The study marshals substantial evidence through multiple complementary analytical approaches, with Validity reaching Excellent due to systematic sampling and methodological diversity.

**Strengths:**

- 135 individuals across 8 sites and 3000 years provides representative coverage
- Multiple complementary methods (PCA, f-stats, qpAdm, IBD, ROH) enable triangulation
- Alternative ancestry models compared with statistical criteria (P-values)
- Pattern claims appropriately bounded by geographic and temporal constraints

**Weaknesses:**

- Genetic contact → technology transfer inference requires auxiliary assumptions
- Sample selection criteria undocumented
- Some interpretive claims about Yamnaya formation extend beyond immediate evidence scope

---

### Cluster 3: Reproducibility

**Rating:** Adequate
**Pathway:** Standard (computational components present)

Data availability is excellent (ENA open access), but the absence of a code repository limits exact computational reproduction. An experienced archaeogenomics researcher could reproduce analyses methodologically using documented tools and parameters, but workflow reconstruction would be required.

**Strengths:**

- Complete data archiving in standard repository with open access
- All primary software tools documented with versions
- Standard open-source tools (ADMIXTOOLS, EAGER, GLIMPSE) enable methodological reproduction

**Weaknesses:**

- No code repository for analysis scripts
- Environment not containerised or formally specified
- Workflow orchestration (how tools were combined) not documented
- Low machine-actionability

---

## Infrastructure & FAIR Summary

### FAIR Compliance

| Dimension | Score | Rating |
|-----------|-------|--------|
| **Overall FAIR** | 12/16 | Moderately FAIR |

### Availability Status

| Resource | Status | Details |
|----------|--------|---------|
| **Code** | ❌ Not Available | No code repository. Uses standard tools with documented versions. |
| **Data** | ✅ Available | ENA PRJEB62503, open access |
| **Preregistration** | N/A | Not expected for inductive research |

### Persistent Identifiers

| Type | Status |
|------|--------|
| Paper DOI | ✅ 10.1038/s41586-023-06334-8 |
| Author ORCIDs | Partial (some authors) |
| Software DOIs | ❌ None for custom scripts |
| Data DOIs | ✅ ENA accession PRJEB62503 |

### Infrastructure Gaps

1. **Missing code repository:** Substantial computational analysis (bioinformatics pipeline, population genetics) without shared scripts
2. **No containerised environment:** Software versions documented but dependencies implicit
3. **Limited machine-actionability:** Manual integration required to reproduce analyses

---

## Contextual Interpretation

This section explains what scores mean for this specific paper type, helping readers understand why certain scores may differ from typical empirical research expectations.

As an inductive archaeogenomics study, expectations differ from hypothesis-testing research:

- **Pre-registration not expected:** Exploratory pattern documentation doesn't require pre-registration
- **Data archiving critical:** ENA deposition meets field standards and enables data reuse
- **Code sharing increasingly expected:** Absence of code repository is a notable gap for 2023 Nature publication
- **Interpretive claims extend genetic evidence:** Connection between genetic admixture and cultural processes involves standard archaeogenomics inference but requires auxiliary assumptions

### Signal-Specific Context

- **Validity (80 - Excellent):** Strong score reflects systematic temporal sampling and methodological triangulation appropriate for inductive pattern documentation
- **Reproducibility (62 - Good):** Score reflects excellent data sharing but missing code. Standard for archaeogenomics field though below expectations for computational papers
- **Generalisability (72 - Good):** Regional pattern claims appropriately bounded; broader Yamnaya formation claims extend evidence somewhat

---

## Era Context

**Publication Year:** 2023
**Era:** Early Majority (2020-2025)

In the Early Majority era, data sharing is increasingly standard but code sharing remains inconsistent. This paper exceeds expectations for data archiving (ENA with open access) but falls short on code sharing (no repository). For archaeogenomics specifically:

- ENA deposition is standard practice (met)
- Code repositories are emerging but not yet universal (not met)
- FAIR compliance is increasingly assessed (12/16 moderate)

The aggregate score of 74 places this paper in the GOOD band, consistent with high-quality archaeogenomics research that meets data sharing norms but lacks the code sharing practices increasingly expected in computational fields.

---

## Structured Output

The following JSON block contains all assessment data in machine-readable format.

```json
{
  "credibility_assessment": {
    "paper_slug": "penske-et-al-2023",
    "run": "run-02",
    "paper_title": "Early contact between late farming and pastoralist societies in southeastern Europe",
    "doi": "10.1038/s41586-023-06334-8",
    "assessment_date": "2025-12-02",
    "assessor_version": "v1.0",

    "classification": {
      "paper_type": "empirical",
      "paper_subtype": "archaeogenomics",
      "research_approach": "inductive",
      "framework_applied": "inductive_emphasis",
      "quality_state": "high",
      "classification_confidence": "high",
      "publication_year": 2023,
      "era_context": "early_majority"
    },

    "signal_scores": {
      "comprehensibility": {"score": 78, "band": "good", "cluster": 1},
      "transparency": {"score": 75, "band": "good", "cluster": 1},
      "plausibility": {"score": 76, "band": "good", "cluster": 2},
      "validity": {"score": 80, "band": "excellent", "cluster": 2},
      "robustness": {"score": 75, "band": "good", "cluster": 2},
      "generalisability": {"score": 72, "band": "good", "cluster": 2},
      "reproducibility": {"score": 62, "band": "good", "cluster": 3}
    },

    "cluster_ratings": {
      "cluster_1_foundational_clarity": "strong",
      "cluster_2_evidential_strength": "strong",
      "cluster_3_reproducibility": "adequate"
    },

    "aggregate_score": {
      "score": 74,
      "band": "good",
      "experimental": true,
      "calculation": "mean of 7 signals"
    },

    "infrastructure": {
      "fair_score": 12,
      "fair_maximum": 16,
      "fair_category": "moderately_fair",
      "data_available": true,
      "data_repository": "ENA PRJEB62503",
      "code_available": false,
      "preregistered": false
    },

    "verdict": {
      "band": "GOOD",
      "confidence": "high",
      "bottom_line": "Methodologically rigorous archaeogenomics study with strong genetic evidence. Documentation meets high standards for genetic pattern claims; interpretive claims extend beyond direct evidence. Computational reproduction requires workflow reconstruction."
    }
  }
}
```

---

## Assessment Metadata

| Field | Value |
|-------|-------|
| **Assessment Date** | 2025-12-02 |
| **Assessor Version** | v1.0 |
| **Schema Version** | 2.6 |
| **Report Template** | credibility-assessment-report-template v1.0 |
| **Variability Test Run** | run-02 of 5 |

---

**End of Report**
