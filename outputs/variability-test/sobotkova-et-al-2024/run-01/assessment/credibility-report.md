# Credibility Assessment Report

**Paper:** Validating predictions of burial mounds with field data: the promise and reality of machine learning
**Slug:** sobotkova-et-al-2024
**DOI:** 10.1108/JD-05-2022-0096
**Assessment Date:** 2025-12-04
**Assessor Version:** v1.0

---

## Executive Summary

**Verdict:** GOOD | **Confidence:** High

**Paper Type:** Empirical (ML validation study)
**Research Approach:** Deductive
**Publication Era:** Early Majority (2024)

This paper presents a rigorous validation of CNN-based archaeological feature detection against field data. The authors test the hypothesis that curated training data improves transfer learning CNN performance for burial mound detection in satellite imagery. The study finds that both uncurated (2021) and curated (2022) approaches produce misleadingly high self-reported F1 scores that fail field validation catastrophically, with the counterintuitive result that more curation led to worse performance.

The paper demonstrates exemplary methodological transparency for ML validation research. The honest reporting of failure—rather than success-washing typical of the literature—substantially enhances credibility. The field validation against independent ground truth (773 mounds documented via pedestrian survey) provides robust evidence for the core finding.

**Key Strengths:**
- Field validation against independent ground truth provides gold-standard ML evaluation
- Three code repositories share analytical workflow (training data prep, both CNN models)
- Methodological transparency about failure modes and limitations exceeds literature norms
- Carefully constrained claims with explicit scope boundaries (heterogeneous landscape, varied features)

**Key Concerns:**
- Data not deposited (field mound locations, satellite imagery, training cutouts)
- Computational environment underdocumented (no software versions, hyperparameters)
- Single geographic case study limits empirical testing of claimed constraints

**Bottom Line:** A credible ML validation study that honestly documents failure. The transparent reporting of what doesn't work contributes more to the field than success-framed papers hiding limitations. Reproducing the exact analysis requires data access and environment details not provided, but the methodological lessons are transferable.

---

## Classification Summary

| Dimension | Value |
|-----------|-------|
| **Paper Type** | Empirical (ML validation study) |
| **Research Approach** | Deductive |
| **Framework Applied** | Deductive emphasis (Validity, Robustness, Reproducibility primary) |
| **Quality State** | HIGH |
| **Classification Confidence** | High |
| **Publication Year** | 2024 |
| **Era Context** | Early Majority |

### Quality State Implications

HIGH quality state enables full credibility assessment with precise scoring (±5 points). Extraction captured comprehensive evidence (23 items), claims (27 items), and RDMAP items (25 total). Classification confidence is high with matched expressed/revealed approaches.

### Paper Type Context

As an empirical ML validation study, this paper is assessed against deductive research standards. The core hypothesis (curated training data improves performance) is testable and systematically evaluated. The quasi-experimental design (comparing uncurated baseline to curated intervention) provides robust hypothesis testing structure.

---

## Signal Scores Dashboard

| Signal | Score | Band | Cluster | Context Flag |
|--------|-------|------|---------|--------------|
| Comprehensibility | 78 | Good | 1 | — |
| Transparency | 68 | Good | 1 | — |
| Plausibility | 75 | Good | 2 | — |
| Validity | 82 | Excellent | 2 | — |
| Robustness | 62 | Good | 2 | — |
| Generalisability | 80 | Excellent | 2 | — |
| Reproducibility | 55 | Moderate | 3 | — |

**Aggregate Score:** 71/100 (GOOD) *[EXPERIMENTAL]*

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

This paper demonstrates strong foundational clarity. The hypothesis is explicitly stated ("if we curate the input training data, we can improve the results"), key terms are operationally defined (F1 score, true positive rate, mound dimensions), and the argument structure is traceable from hypothesis through test to interpretation.

Methods documentation is detailed for most aspects (training data preparation, validation approach) but has gaps in computational details (hyperparameters, software versions). Code availability is strong with three GitHub repositories covering the analytical workflow.

**Strengths:**
- Explicit hypothesis statement in Methods section
- Well-defined operational terms (ML metrics, archaeological features)
- Three functional code repositories

**Weaknesses:**
- Software versions and hyperparameters not documented
- No formal data availability statement
- Train/validation/test split procedure implicit

---

### Cluster 2: Evidential Strength

**Rating:** Strong

This paper demonstrates strong evidential strength, with particular excellence in validity (82) and generalisability (80). The hypothesis test is well-designed: 773 ground-truthed mounds provide comprehensive validation data, field validation against independent ground truth represents gold-standard ML evaluation, and alternative explanations are explicitly considered.

The counterintuitive finding (curated data performed worse) is honestly reported and explained rather than ignored. The paper carefully constrains claims to the specific context (heterogeneous landscape, varied features) and explicitly specifies transfer conditions.

**Strengths:**
- 773 ground-truthed mounds provide robust validation dataset
- Field validation against independent ground truth (gold standard)
- Claims carefully bounded with explicit scope constraints
- Counterintuitive results acknowledged and explained

**Weaknesses:**
- Hyperparameters and threshold sensitivity not tested
- Single geographic study area
- No cross-validation documented

---

### Cluster 3: Reproducibility

**Rating:** Adequate
**Pathway:** Standard (computational component present)

The paper demonstrates adequate reproducibility infrastructure. Code availability is strong—three GitHub repositories cover training data preparation and both CNN model implementations. However, data availability is weak: field survey data is referenced to a prior publication but not deposited, satellite imagery is proprietary, and training cutouts are not shared. Environment documentation is minimal (HPC platform mentioned but no software versions).

This creates an asymmetric reproducibility profile: the analytical code is available, but the inputs required to run it are not.

**Strengths:**
- Three GitHub repositories cover core analytical workflow
- Open scriptable tools (Python/CNN)
- CC BY 4.0 paper licence

**Weaknesses:**
- Field data (773 mound locations) not deposited
- Satellite imagery proprietary
- No software versions or hyperparameters documented
- No data availability statement

---

## Infrastructure & FAIR Summary

### FAIR Compliance

| Dimension | Score | Rating |
|-----------|-------|--------|
| **Overall FAIR** | 2/6 | Limited |

### Availability Status

| Resource | Status | Details |
|----------|--------|---------|
| **Code** | Available | Three GitHub repositories (cnn-testing, burial-mounds, MoundDetection) |
| **Data** | Not Available | Field data referenced to prior publication; satellite imagery proprietary |
| **Preregistration** | No | Not mentioned |

### Persistent Identifiers

| Type | Status |
|------|--------|
| Paper DOI | ✅ 10.1108/JD-05-2022-0096 |
| Author ORCIDs | ❌ Not visible in PDF |
| Software DOIs | ❌ GitHub URLs only, no Zenodo |
| Data DOIs | ❌ None |

### Infrastructure Gaps

- No formal data availability statement
- Field survey data (773 mound coordinates) not deposited in repository
- Satellite imagery proprietary (IKONOS via GeoEye grant)
- Training data cutouts not deposited
- Code repositories lack Zenodo DOIs for preservation
- Software versions not documented (Python, TensorFlow/Keras)
- Hyperparameters not documented

---

## Contextual Interpretation

This section explains what scores **mean for this specific paper type**, helping readers understand why certain scores may differ from typical empirical research expectations.

This paper is assessed as deductive empirical research testing a specific hypothesis about ML model performance. The high validity score (82) reflects the gold-standard validation approach: testing predictions against independently collected field data rather than just held-out model data. This is rare in ML papers and substantially increases credibility.

The moderate reproducibility score (55) reflects the asymmetric sharing profile common in ML research: code is shared, but data inputs are not. For satellite imagery, this is partly unavoidable (proprietary data). For field survey coordinates, deposition would be possible but was not done.

The paper's methodological transparency about failure modes is unusual and valuable. Most ML papers in the literature review showed positive framing (63% of abstracts mention no limitations). This paper's willingness to document and explain failure enhances its contribution to the field.

### Signal-Specific Context

**Validity (82 - Excellent):** The field validation design is exceptionally strong. Testing against 773 independently documented mounds provides robust ground truth that most ML papers lack.

**Generalisability (80 - Excellent):** The score reflects careful constraint rather than broad claims. The authors explicitly limit applicability to heterogeneous landscapes with varied features—this is methodological virtue.

**Robustness (62 - Good):** The two-run comparison (uncurated vs curated) provides some sensitivity analysis. The consistent failure pattern across both approaches actually demonstrates robustness of the core finding.

**Reproducibility (55 - Moderate):** Code sharing is commendable (3 repositories). Data unavailability is the primary limitation. Environment documentation would lift this score.

---

## Era Context

**Publication Year:** 2024
**Era:** Early Majority

By 2024 standards in the early majority era of reproducibility adoption:

- **Code sharing (3 repositories):** Meets current expectations. Increasingly standard for ML research.
- **Data deposit (absent):** Below emerging best practice, though common for archaeology with proprietary imagery.
- **Pre-registration (absent):** Not expected for this type of validation study.
- **Software versions (absent):** Below current best practice for ML research.

The paper performs above average for archaeological ML literature (which shows strong positive framing bias) but below emerging computational reproducibility standards.

---

## Structured Output

The following JSON block contains all assessment data in machine-readable format.

```json
{
  "paper_slug": "sobotkova-et-al-2024",
  "paper_title": "Validating predictions of burial mounds with field data: the promise and reality of machine learning",
  "paper_doi": "10.1108/JD-05-2022-0096",
  "assessment_date": "2025-12-04",
  "assessor_version": "v1.0",

  "classification": {
    "paper_type": "empirical",
    "paper_subtype": "ML_validation_study",
    "research_approach": "deductive",
    "framework_applied": "deductive_emphasis",
    "quality_state": "high",
    "classification_confidence": "high",
    "publication_year": 2024,
    "era_context": "early_majority"
  },

  "signal_scores": {
    "comprehensibility": {"score": 78, "band": "good"},
    "transparency": {"score": 68, "band": "good"},
    "plausibility": {"score": 75, "band": "good"},
    "validity": {"score": 82, "band": "excellent"},
    "robustness": {"score": 62, "band": "good"},
    "generalisability": {"score": 80, "band": "excellent"},
    "reproducibility": {"score": 55, "band": "moderate"}
  },

  "aggregate_score": 71,
  "verdict_band": "GOOD",
  "verdict_confidence": "high",

  "cluster_ratings": {
    "cluster_1_foundational_clarity": "strong",
    "cluster_2_evidential_strength": "strong",
    "cluster_3_reproducibility": "adequate"
  },

  "infrastructure": {
    "code_available": true,
    "code_repositories": 3,
    "data_available": false,
    "preregistration": false,
    "fair_score": 2,
    "fair_maximum": 6,
    "pid_graph_connectivity": 2
  },

  "reproducibility_readiness": {
    "execution_feasibility": "needs_work",
    "pathway": "standard"
  },

  "key_strengths": [
    "Field validation against independent ground truth (773 mounds)",
    "Three code repositories share analytical workflow",
    "Transparent reporting of failure modes exceeds literature norms",
    "Carefully constrained claims with explicit scope boundaries"
  ],

  "key_concerns": [
    "Data not deposited (field locations, imagery, training cutouts)",
    "Computational environment underdocumented",
    "Single geographic case study"
  ],

  "context_flags": []
}
```

---

## Assessment Metadata

| Field | Value |
|-------|-------|
| **Assessment Date** | 2025-12-04 |
| **Assessor Version** | v1.0 |
| **Schema Version** | 1.0 |
| **Report Template** | credibility-assessment-report-template v1.0 |

---

**End of Report**
