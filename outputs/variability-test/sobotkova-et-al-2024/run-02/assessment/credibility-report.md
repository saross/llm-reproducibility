# Credibility Assessment Report

**Paper:** Validating predictions of burial mounds with field data: the promise and reality of machine learning
**Authors:** Sobotkova, A., Kristensen-McLachlan, R.D., Mallon, O., Ross, S.A.
**DOI:** 10.1108/JD-05-2022-0096
**Publication Year:** 2024
**Assessment Date:** 2025-12-05
**Assessor:** research-assessor-skill-opus4.5

---

## Executive Summary

**Verdict:** GOOD | **Confidence:** High

This empirical paper using deductive reasoning demonstrates solid credibility with appropriate epistemic constraints. As a 2024 publication, it reflects current era expectations for FAIR and open science compliance.

**Key Strengths:**
- Clear hypothesis-testing framework with explicit predictions and quantified test results
- Comprehensive code transparency (3 GitHub repositories covering all computational components)
- Appropriate handling of negative findings (95-96% false negative rate honestly reported)

**Key Concerns:**
- Asymmetric reproducibility: excellent code availability but no data deposit
- Limited systematic robustness testing beyond the two-run comparison

**Bottom Line:** Well-executed validation study that transparently reports hypothesis rejection. Credibility is strong for the claims made, with appropriate acknowledgment of scope limitations.

---

## Signal Dashboard

| # | Signal | Score | Band | Cluster |
|---|--------|-------|------|---------|
| 1 | Comprehensibility | 78 | Good | C1: Foundational Clarity |
| 2 | Transparency | 72 | Good | C1: Foundational Clarity |
| 3 | Plausibility | 75 | Good | C2: Evidential Strength |
| 4 | Validity | 78 | Good | C2: Evidential Strength |
| 5 | Robustness | 68 | Good | C2: Evidential Strength |
| 6 | Generalisability | 65 | Good | C2: Evidential Strength |
| 7 | Reproducibility | 62 | Good | C3: Reproducibility |

**Aggregate Score: 71** (EXPERIMENTAL)

**Verdict Band:** Good (60-79)

---

## Classification Summary

| Dimension | Value |
|-----------|-------|
| Paper Type | Empirical |
| Research Approach | Deductive |
| Expressed vs Revealed | Matched |
| Classification Confidence | High |
| Quality State | High |
| Era Context | Current (2024) — FAIR and open science expectations established |

---

## Cluster Summaries

### Cluster 1: Foundational Clarity (Strong)

**Signals:** Comprehensibility (78), Transparency (72)

The paper demonstrates strong foundational clarity. Hypotheses are explicitly stated ("validating predictions" framing), key terms operationally defined (detection thresholds, validation rates), and logical structure is transparent. Methods are comprehensively documented with 9 methods and 14 protocols. Code is publicly available via three GitHub repositories.

**Key Finding:** Clear hypothesis-testing framework with comprehensive methodology documentation. Minor gaps in literature review methodology and some implicit protocols.

### Cluster 2: Evidential Strength (Strong)

**Signals:** Plausibility (75), Validity (78), Robustness (68), Generalisability (65)

All four signals score in the Good band, with validity (78) and plausibility (75) strongest. Evidence directly addresses the hypothesis (773 field-verified mounds), the two-run comparison enables controlled inference, and anomalous results (curated data performing worse) are explicitly acknowledged and explained.

**Key Finding:** Well-executed empirical research with direct evidence-hypothesis connection. Robustness and generalisability scores reflect study design constraints (limited sensitivity analysis, single-case design) rather than methodological failures.

### Cluster 3: Reproducibility (Adequate)

**Signal:** Reproducibility (62)

Asymmetric reproducibility profile: excellent code availability (3 repositories, HPC documentation) but significant data gap (no deposit, commercial imagery inaccessible). FAIR score of 62.5% reflects this pattern. Computational workflow is transparent and could theoretically be re-executed, but data dependencies prevent practical replication.

**Key Finding:** Code reproducibility is strong; data reproducibility is weak. This pattern is characteristic of field science with commercial data dependencies.

---

## Context Flags Applied

No special context flags required. This is a standard empirical deductive paper with straightforward signal interpretation.

---

## FAIR Assessment Summary

| Principle | Score | Notes |
|-----------|-------|-------|
| Findable | 3/4 | DOI present, 3 GitHub repos linked |
| Accessible | 2/4 | Code in public repos, data not deposited |
| Interoperable | 3/4 | Standard formats (geoTIFF, Python), common frameworks (TensorFlow) |
| Reusable | 2/4 | Code available but data, trained models, documentation incomplete |
| **Total** | **10/16** | **62.5%** |

---

## Implications for Trust

### What These Scores Mean

**For researchers citing this work:**
- Claims about CNN failure to detect burial mounds are well-supported (Validity 78)
- Methodology is clearly documented and could be understood and adapted (Comprehensibility 78, Transparency 72)
- Negative findings should be taken seriously given appropriate handling of anomalies (Plausibility 75)

**For practitioners considering similar approaches:**
- Results suggest caution with transfer learning for archaeological feature detection
- Single study area limits generalisability — additional landscape tests would strengthen conclusions
- Code availability enables methodological learning even without data access

**For reproducibility:**
- Computational workflow can be examined and understood
- Full replication requires obtaining equivalent data independently
- Ground-truth coordinates could be archived even if satellite imagery cannot

---

## Recommendations

1. **For this paper:** Archive ground-truth mound coordinates in a public repository (Zenodo, tDAR) to improve Reproducibility and Reusable FAIR scores
2. **For future work:** Consider pre-registration for hypothesis-testing ML studies
3. **For the field:** Develop data sharing agreements that enable mound coordinate archiving without requiring satellite imagery release

---

## Assessment Limitations

- Assessment based on extraction without manual verification against full text
- Some implicit RDMAP items (RD006, M008-M009, P013-P014) may reflect extraction limitations rather than paper gaps
- FAIR assessment based on published materials only; additional materials may exist

---

## Structured Output

```yaml
credibility_assessment:
  paper_slug: "sobotkova-et-al-2024"
  paper_title: "Validating predictions of burial mounds with field data: the promise and reality of machine learning"
  doi: "10.1108/JD-05-2022-0096"
  publication_year: 2024
  assessment_date: "2025-12-05"

  classification:
    paper_type: "empirical"
    research_approach: "deductive"
    expressed_vs_revealed: "matched"
    classification_confidence: "high"
    quality_state: "high"
    era_context: "current"

  signals:
    comprehensibility: 78
    transparency: 72
    plausibility: 75
    validity: 78
    robustness: 68
    generalisability: 65
    reproducibility: 62

  aggregate:
    score: 71
    band: "good"
    status: "experimental"

  cluster_ratings:
    c1_foundational_clarity: "strong"
    c2_evidential_strength: "strong"
    c3_reproducibility: "adequate"

  fair_assessment:
    findable: 3
    accessible: 2
    interoperable: 3
    reusable: 2
    total: 10
    percentage: 62.5

  verdict:
    overall: "GOOD"
    confidence: "high"
    key_strengths:
      - "Clear hypothesis-testing framework with quantified results"
      - "Comprehensive code transparency (3 GitHub repositories)"
      - "Transparent handling of negative findings"
    key_concerns:
      - "Asymmetric reproducibility (code yes, data no)"
      - "Limited systematic robustness testing"
    bottom_line: "Well-executed validation study with credible negative findings and appropriate scope acknowledgment"
```
