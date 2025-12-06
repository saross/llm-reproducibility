# Cluster 1: Foundational Clarity Assessment

**Paper:** sobotkova-et-al-2024
**Assessment Date:** 2025-12-06
**Assessor Version:** v1.0

**Quality State:** HIGH
**Research Approach:** Deductive
**Paper Type:** Empirical

---

## Signal Scores Summary

| Signal | Score | Band | Approach Anchors |
|--------|-------|------|------------------|
| Comprehensibility | 78 | Good | Deductive |
| Transparency | 75 | Good | Deductive |

**Cluster Rating:** Strong

---

## Signal 1: Comprehensibility

**Score:** 78/100 (Good)

**Approach anchors applied:** Deductive

### Assessment

The paper demonstrates strong comprehensibility for a deductive validation study. The central hypothesis—that a CNN trained on legacy field data can reliably detect burial mounds in satellite imagery—is clearly stated in the Introduction and tested systematically throughout. Claims are explicit and appropriately bounded, focusing on the specific study area (Kazanlak Valley, Bulgaria), the specific model (ResNet-50 with transfer learning), and the specific validation framework (comparison against 773 mounds from TRAP survey).

Key technical terms are operationally defined: "true positive" and "false positive" are clearly specified in terms of tile-mound spatial overlap, the 60% probability threshold is explicitly stated, and the distinction between the two model runs (2021 with all mounds, 2022 with visible mounds only) is clearly articulated. The logical structure of hypothesis testing is transparent: model training → prediction generation → validation against ground-truth → performance assessment.

Minor comprehensibility gaps exist in the literature review methodology (search strategy and coding scheme not fully specified) and in some technical details of model training (hyperparameter tuning, number of epochs). However, these do not significantly impair understanding of the core claims and their evidential basis.

### Evidence

**Strengths:**
- C01: "Validation of results against field data showed that self-reported success rates were misleadingly high" - Clear, bounded empirical finding with explicit validation methodology
- C10: "Although the first model reported a good fit (F1 = 0.87), validation with field data showed the model was confusing our target features with other phenomena" - Clear contrast between internal metrics and external validation
- RD01: "The purpose of this study is to explore how ML, specifically a CNN, could be trained to detect ancient burial mounds in satellite imagery and then tested using existing field data" - Explicit research design statement

**Weaknesses:**
- P10: Literature search protocol incomplete - "Coding scheme not described, inter-rater reliability not reported"

### Scoring Rationale

Score of 78 (Good for deductive) reflects: hypotheses clearly stated and bounded (60-79 criterion met), key terms operationally defined, logical structure of hypothesis testing transparent, claims unambiguous and testable. Falls short of Excellent (80-100) due to incomplete specification of literature review methodology and some training protocol details.

---

## Signal 2: Transparency

**Score:** 75/100 (Good)

**Approach anchors applied:** Deductive

### Assessment

The paper demonstrates good transparency for a deductive validation study. The research design is explicitly stated with clear validation framework: CNN model trained on mound cutouts from satellite imagery, predictions generated for study area, validation against independent ground-truth from prior TRAP survey. Methods are detailed with specific parameters: 150×150m cutouts, 70:20:10 training split, 1:2 positive:negative ratio, 60% probability threshold for prediction acceptance.

Data availability is strong for the ground-truth data: the paper documents that the 773 mounds were collected by TRAP during 2009-2011 field survey, though the exact data repository is not specified. Code availability is documented through GitHub repositories for TRAP project data processing. The IKONOS satellite imagery was acquired through a GeoEye Foundation grant in 2009, with clear specification of resolution (1m panchromatic, 4m multispectral).

Limitations are explicitly acknowledged: the paper discusses challenges with mound size variability, background heterogeneity, and potential spurious correlations learned by the model. The resource investment (135 person-hours) is transparently documented.

Gaps in transparency include: hyperparameter tuning details not fully specified, pan-sharpening algorithm not named, GIS software for spatial validation not identified, and no formal data deposit or code DOI provided.

### Evidence

**Strengths:**
- M02: "After some preliminary experimentation with a range of different pre-trained models, we concluded that ResNet-50 seemed to perform best for our data. This model is one of the smaller pre-trained CNNs available, with only around 25.6m trainable parameters" - Clear model selection rationale
- P04: "cutouts were divided into training, validation, and test sets following a 70:20:10 ratio for automated performance validation" - Explicit protocol specification
- P08: "We selected prediction records whose mound-probability exceeded 0.599 and used the coordinates to generate square polygons of 150 m side" - Clear threshold and validation procedure

**Weaknesses:**
- P05: Data augmentation specified but "Rotation angles not specified, augmentation library not specified"
- P11: Pan-sharpening described but "Fusion algorithm not specified, software not specified"

### Scoring Rationale

Score of 75 (Good for deductive) reflects: clear research design and hypothesis specification (60-79 criterion met), detailed methods (60-79), data availability stated (60-79), code/workflow documented through GitHub references, major limitations acknowledged. Falls short of Excellent (80-100) due to absence of pre-registration, incomplete protocol documentation for some technical details, and no persistent identifiers for data/code.

---

## Cluster Synthesis

**Overall Foundational Clarity:** Strong

The paper demonstrates strong foundational clarity across both signals. Comprehensibility and Transparency scores are consistent (78 and 75), both in the Good band, indicating a well-documented study with clear claims and methods. The deductive validation design is explicit and the logical structure from hypothesis (CNN can detect mounds) through testing (validation against field data) to conclusion (model failed) is transparent.

### Pattern Summary

Both signals show a paper that meets the standards for good deductive research: hypotheses are clearly stated and testable, methods are well-documented with specific parameters, and the validation framework is transparent. The primary limitation across both signals is incomplete technical specification of some secondary procedures (hyperparameters, software tools), which would be needed for exact replication but do not impair critical evaluation of the core claims.

### Implications for Subsequent Assessment

- **For Cluster 2 (Evidential Strength):** High foundational clarity enables confident assessment of validity and robustness. The clear validation framework supports strong validity assessment. The two-run comparison (2021 vs 2022) provides some robustness evidence.

- **For Cluster 3 (Reproducibility & Scope):** Good transparency supports reproducibility assessment, though absence of persistent identifiers and some technical gaps may limit reproducibility score. Code availability through GitHub is positive. Scope is appropriately constrained to Kazanlak Valley context.

---

## Structured Output

```yaml
cluster_1_foundational_clarity:
  paper_slug: "sobotkova-et-al-2024"
  assessment_date: "2025-12-06"
  quality_state: "high"
  research_approach: "deductive"

  comprehensibility:
    score: 78
    band: "good"
    strengths:
      - "Central hypothesis explicitly stated and clearly bounded"
      - "Key terms operationally defined (true/false positive, probability threshold)"
      - "Logical structure of hypothesis testing transparent"
    weaknesses:
      - "Literature review methodology incomplete (coding scheme not described)"
    rationale: "Hypotheses stated with definitional clarity, logical structure of validation clear, claims unambiguous and testable. Falls short of Excellent due to incomplete specification of secondary methodology."

  transparency:
    score: 75
    band: "good"
    strengths:
      - "Research design explicitly stated with clear validation framework"
      - "Methods detailed with specific parameters (cutout size, data splits, thresholds)"
      - "Limitations explicitly acknowledged"
    weaknesses:
      - "Some technical details missing (hyperparameters, software tools)"
      - "No persistent identifiers for data/code"
    rationale: "Clear research design, detailed methods, data availability stated, major limitations acknowledged. Falls short of Excellent due to absence of pre-registration and incomplete protocol documentation."

  cluster_synthesis:
    overall_rating: "strong"
    pattern_summary: "Consistent Good scores across both signals indicate well-documented deductive validation study with clear claims and transparent methods."
    consistency_check: "consistent"
    implications:
      cluster_2: "High foundational clarity enables confident validity and robustness assessment"
      cluster_3: "Good transparency supports reproducibility assessment though some technical gaps exist"
```
