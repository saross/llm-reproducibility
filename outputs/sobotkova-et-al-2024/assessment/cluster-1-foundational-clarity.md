# Cluster 1: Foundational Clarity Assessment

**Paper:** sobotkova-et-al-2024
**Assessment Date:** 2025-11-30
**Assessor Version:** v1.0

**Quality State:** HIGH
**Research Approach:** Deductive
**Paper Type:** Empirical

---

## Signal Scores Summary

| Signal | Score | Band | Approach Anchors |
|--------|-------|------|------------------|
| Comprehensibility | 82 | Excellent | Deductive |
| Transparency | 74 | Good | Deductive |

**Cluster Rating:** Strong

---

## Signal 1: Comprehensibility

**Score:** 82/100 (Excellent)

**Approach anchors applied:** Deductive

### Assessment

This ML validation study demonstrates excellent comprehensibility for hypothesis-testing research. The central claims are explicitly stated and clearly bounded: the paper tests whether pre-trained CNNs can effectively detect burial mounds in heterogeneous landscapes. The research question is unambiguous, and findings are presented as direct tests of this prediction.

Claims are structured as performance assessments with quantitative precision. C002 states "The pre-trained CNN model failed to identify burial mounds in our study area" - a clear, testable claim directly addressing the research question. The logical structure follows classic deductive workflow: prediction (CNN will detect mounds) → systematic test (validation against field survey data) → conclusion (model failed with 95-96% false negative rate).

Key terms are operationally defined throughout. The paper explains transfer learning, CNN architecture (ResNet-50), training data composition, and validation metrics (precision, recall, F1 scores). Methodological critiques are also clear: C005 identifies "publication bias and rhetoric of unconditional success" in ML-for-archaeology literature with explicit supporting evidence from their review.

### Evidence

**Strengths:**
- C001: "Pre-trained CNNs have significant limitations when detecting varied features of different sizes within heterogeneous landscapes" - explicit, bounded claim with specific conditions
- C002: "The pre-trained CNN model failed to identify burial mounds" - unambiguous finding directly addressing research question
- RD001: "External validation design comparing ML model predictions against comprehensive field survey data" - clear design statement with explicit validation logic
- RD002: "Comparative two-run design testing impact of training data curation" - explicit hypothesis about curation effects

**Weaknesses:**
- Some technical parameters not fully operationalised (e.g., "best performance" in model selection not precisely defined)
- Decision threshold (60%) selection rationale not explained

### Scoring Rationale

Score of 82 (Excellent) reflects: hypotheses explicitly stated and bounded (80-100 criterion); key terms operationally defined; logical structure of hypothesis testing transparent; claims unambiguous and testable; reasoning from test results to conclusions clear. Minor deductions for some unexplained parameter choices, but overall exemplary for deductive ML validation research.

---

## Signal 2: Transparency

**Score:** 74/100 (Good)

**Approach anchors applied:** Deductive

### Assessment

The paper demonstrates good transparency for deductive research, with excellent code sharing but incomplete data availability. The research design is explicitly stated through RD001-RD004, providing clear documentation of the validation approach, comparative design, negative results documentation rationale, and cost-benefit analysis framework.

Code availability is exemplary: three distinct GitHub repositories document the complete analytical workflow (cnn-testing for validation, burial-mounds for 2021 classifier, MoundDetection for 2022 classifier). The code availability statement is explicit and machine-actionable with direct URLs. This represents best practice for computational transparency.

However, data availability is a weakness. The historical field survey data from TRAP (2009-2011) is not deposited in a public repository, and there is no explicit data availability statement. Training data and CNN predictions are presumably available via GitHub but this is not clearly stated. For deductive hypothesis-testing research in 2024, explicit data sharing or justified restrictions would be expected for the 80-100 band.

Methods and protocols are well-documented: 7 methods and 12 protocols capture the CNN architecture, training procedures, and validation workflow. Some expected information is missing (hyperparameters, threshold selection rationale, augmentation specifics) but core methodology is clear.

### Evidence

**Strengths:**
- Code availability: "Scripts are available in public repositories" with three GitHub URLs (machine-actionable, open access)
- M001: "Transfer learning using pre-trained ResNet-50 convolutional neural network" - clear method specification
- P002: "150x150m square polygons centred on mound points, clipped from IKONOS imagery" - detailed spatial protocol
- Limitations explicitly acknowledged: "model failed", "good-faith attempt", "counterbalance and cautionary tale"
- FAIR assessment: 75% (12/16) - highly FAIR for code, weaker for data

**Weaknesses:**
- Data availability: "statement_present: false" - no explicit data availability statement
- Historical TRAP field data (773 mounds) not deposited in public repository
- Training data availability unclear despite GitHub repositories
- No pre-registration (acceptable for retrospective study but noted)
- Missing: hyperparameters, threshold selection rationale, augmentation strategy specifics

### Scoring Rationale

Score of 74 (Good) reflects: clear research design and methods (60-79 criterion); excellent code availability via GitHub; data availability not fully addressed (prevents 80-100); comprehensive methods description; major limitations acknowledged. The gap between exemplary code sharing and absent data sharing creates the ceiling at Good band.

---

## Cluster Synthesis

**Overall Foundational Clarity:** Strong

This paper demonstrates strong foundational clarity as a deductive ML validation study. Both signals score in the Good-to-Excellent range (Comprehensibility 82, Transparency 74), with no major gaps identified. The paper exemplifies good practice in hypothesis-testing research: clear claims, explicit design, honest reporting of negative results.

### Pattern Summary

The paper exhibits a coherent pattern of methodological transparency with asymmetric data sharing. Code transparency is excellent (three repositories, explicit statement, machine-actionable URLs), while data transparency is incomplete (historical field data not deposited). This is a common pattern in computational archaeology where legacy field data precedes current open science norms. The strong comprehensibility score reflects the paper's unusual honesty about ML limitations - claims about model failure are as clear and well-supported as claims about model success would be.

### Implications for Subsequent Assessment

- **For Cluster 2 (Evidential Strength):** Clear claims and methods enable confident validity and robustness assessment. The two-run comparative design (2021 vs 2022) provides internal robustness test. Evidence quality should be straightforward to assess given explicit performance metrics.

- **For Cluster 3 (Reproducibility):** Excellent code availability suggests high reproducibility potential. Data gap (field survey data not deposited) may limit full computational reproduction. Machine actionability of code repositories should support reproducibility assessment.

---

## Structured Output

```yaml
cluster_1_foundational_clarity:
  paper_slug: "sobotkova-et-al-2024"
  assessment_date: "2025-11-30"
  quality_state: "high"
  research_approach: "deductive"

  comprehensibility:
    score: 82
    band: "excellent"
    strengths:
      - "Hypotheses explicitly stated and clearly bounded"
      - "Key terms operationally defined (CNN, transfer learning, validation metrics)"
      - "Logical structure transparent: prediction → test → conclusion"
      - "Claims unambiguous and testable with quantitative precision"
    weaknesses:
      - "Some technical parameters not fully explained (model selection criteria, threshold rationale)"
    rationale: "Exemplary deductive comprehensibility. Clear hypotheses, operational definitions, transparent reasoning. Minor gaps in parameter justification prevent perfect score."

  transparency:
    score: 74
    band: "good"
    strengths:
      - "Excellent code availability (3 GitHub repositories, explicit statement)"
      - "Research design explicitly documented (RD001-RD004)"
      - "Methods and protocols well-documented (7 methods, 12 protocols)"
      - "Limitations explicitly acknowledged"
    weaknesses:
      - "No explicit data availability statement"
      - "Historical field data not deposited"
      - "Training data availability unclear"
    rationale: "Good deductive transparency with asymmetric sharing. Code exemplary, data incomplete. Gap between code and data sharing creates ceiling at Good band."

  cluster_synthesis:
    overall_rating: "strong"
    pattern_summary: "Coherent methodological transparency with excellent code sharing but incomplete data sharing. Strong comprehensibility from honest reporting of negative results."
    consistency_check: "consistent"
    implications:
      cluster_2: "Clear claims and explicit validation design enable confident evidential strength assessment"
      cluster_3: "Excellent code availability suggests high reproducibility; data gap may limit full reproduction"
```
