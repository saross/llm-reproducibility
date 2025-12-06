# Cluster 1: Foundational Clarity Assessment

**Paper:** sobotkova-et-al-2024
**Assessment Date:** 2025-12-04
**Assessor Version:** v1.0

**Quality State:** HIGH
**Research Approach:** deductive (confidence: high)
**Paper Type:** empirical

---

## Signal Scores Summary

| Signal | Score | Band | Approach Anchors |
|--------|-------|------|------------------|
| Comprehensibility | 78 | Good | deductive |
| Transparency | 68 | Good | deductive |

**Cluster Rating:** Strong

---

## Signal 1: Comprehensibility

**Score:** 78/100 (Good)

**Approach anchors applied:** deductive

### Assessment

This paper demonstrates good comprehensibility for deductive research. The core hypothesis is explicitly stated in the Methods section: "We hypothesised that if we curate the input training data, we can improve the results." This provides clear, testable expectations that structure the entire analysis. The logical progression from hypothesis to test to interpretation is transparent.

Key terms are well-defined. "Burial mounds" are characterised with dimensional parameters (10-100m diameter, <1m to >20m height). Technical ML concepts (F1 score, true positive rate, false positive rate, transfer learning, CNN) are introduced and operationalised. The distinction between self-reported model performance (F1 scores) and field-validated performance (true positive rates against ground truth) is central to the argument and clearly explained.

The argument structure is traceable: theoretical expectation (transfer learning should work, curation should help) → operationalised hypothesis → systematic test (two CNN runs) → field validation against ground truth → rejection of expectations. Claims are bounded and evaluable. The paper explicitly scopes its conclusions to the specific landscape context (heterogeneous Bulgarian valley with varied mound sizes and confounding features).

### Evidence

**Strengths:**
- C001: "Validation of results against field data showed that self-reported success rates were misleadingly high" - Clear, bounded claim with explicit contrast between two measurement approaches
- RD001: Explicit hypothesis stated ("if we curate the input training data, we can improve the results")
- C002: "Our attempt to deploy a pre-trained CNN demonstrates the limitations of this approach when it is used to detect varied features of different sizes within a heterogeneous landscape" - Appropriately scoped to specific context

**Weaknesses:**
- IA003: "Transfer learning effectiveness assumption" - The paper assumes ImageNet pre-training is relevant to satellite imagery of archaeological features; this assumption could be made more explicit
- Some implicit reasoning about why curated data might help (selection of "highly visible" mounds) without fully explaining the theoretical basis

### Scoring Rationale

Score: 78 (Good for deductive). Hypothesis explicitly stated and clearly bounded (60-79 criterion met). Key terms operationally defined including ML metrics and archaeological features (60-79). Logical structure mostly clear with transparent progression from hypothesis to validation (60-79). Reasoning generally traceable with some implicit assumptions about transfer learning applicability. Would need fully explicit theoretical framework for ImageNet-to-archaeology transfer for 80-100 band.

---

## Signal 2: Transparency

**Score:** 68/100 (Good)

**Approach anchors applied:** deductive

### Assessment

The paper demonstrates good methodological transparency for deductive ML validation research. Research design is clearly stated: comparative evaluation of two CNN model configurations (2021 uncurated baseline, 2022 curated intervention) validated against independently collected field data. The quasi-experimental design provides robust hypothesis testing.

Methods documentation is detailed in most areas. The training data preparation pipeline is documented: 150x150 pixel cutouts centred on field-recorded mound locations, 773 MOUND cutouts, ~1:2 positive/negative ratio. The transfer learning approach uses ResNet-50 with ImageNet pre-training. Field validation methodology cross-references model predictions against 773 ground-truthed mounds from TRAP survey.

Code availability is strong: three GitHub repositories are provided (cnn-testing, burial-mounds, MoundDetection) covering training data preparation and both model runs. Data availability is weak: no formal data availability statement, field data not deposited in repository, satellite imagery not accessible (proprietary IKONOS). Computational environment underdocumented: UCloud HPC mentioned but software versions (Python, TensorFlow/Keras), GPU specifications, and hyperparameters not documented.

Limitations are prominently acknowledged throughout, particularly the heterogeneous landscape challenge and the failure mode where the model detected edges/lines rather than round shapes.

### Evidence

**Strengths:**
- M002 (Training data preparation): "Mound points taken during fieldwork were used as centroids for the generation of 150 × 150 m square polygons" - Clear procedure documentation
- reproducibility_infrastructure.code_availability: Three GitHub repositories provided with clear descriptions
- Paper explicitly states limitations throughout (mound variability, landscape heterogeneity, confounding features)

**Weaknesses:**
- reproducibility_infrastructure.data_availability: No formal data availability statement; field data and satellite imagery not deposited
- M-IMP-001: "Train/validation/test split procedure" identified as implicit - split ratio and procedure undocumented
- P-IMP-002: "Hyperparameters" identified as implicit - learning rate, epochs, batch size not specified
- No pre-registration mentioned

### Scoring Rationale

Score: 68 (Good for deductive). Research design and hypothesis specification clear (60-79). Methods detailed with some gaps (60-79). Code availability excellent - three repositories (approaches 80-100). Data availability stated as unavailable (satellite imagery proprietary) - this is transparent about limitations rather than a transparency failure. Major limitations acknowledged prominently (60-79). Missing: pre-registration, complete computational environment documentation, hyperparameters, and data deposit would be needed for 80-100.

---

## Cluster Synthesis

**Overall Foundational Clarity:** Strong

This paper demonstrates strong foundational clarity overall. Comprehensibility (78) and Transparency (68) scores are consistent and mutually reinforcing. The paper's core strength is its methodological honesty: the hypothesis is clearly stated, the methods are documented (with acknowledged gaps), and the limitations are prominently discussed.

### Pattern Summary

Both signals reveal a paper with strong conceptual clarity but moderate documentation completeness. The authors clearly understand and communicate what they did and why, but some implementation details (hyperparameters, data splits, environment) are underdocumented. This is typical of ML validation studies where the focus is on outcome interpretation rather than method reproduction.

The paper's unusual transparency about failure modes (model detected edges not mounds, curated data performed worse) is notable. Most ML papers in the literature review showed positive framing; this paper's willingness to document failure enhances credibility despite documentation gaps.

### Implications for Subsequent Assessment

- **For Cluster 2 (Evidential Strength):** Strong foundation for assessing validity and robustness. The clear hypothesis and documented methods enable evaluation of whether evidence adequately tests the hypothesis. The acknowledged limitations provide explicit scope constraints.
- **For Cluster 3 (Reproducibility):** Code availability (3 repositories) is strong, but data availability (field data and imagery not deposited) and environment documentation (HPC mentioned, versions missing) will likely limit reproducibility score. The pathway is standard (computational component present via CNN models).

---

## Structured Output

```yaml
cluster_1_foundational_clarity:
  paper_slug: "sobotkova-et-al-2024"
  assessment_date: "2025-12-04"
  quality_state: "high"
  research_approach: "deductive"

  comprehensibility:
    score: 78
    band: "good"
    strengths:
      - "Hypothesis explicitly stated in Methods section ('if we curate the input training data, we can improve the results')"
      - "Key terms operationally defined (F1 score, true positive rate, mound dimensions, transfer learning)"
      - "Claims appropriately bounded to specific landscape context"
    weaknesses:
      - "Transfer learning assumption (ImageNet→archaeology) could be more explicitly theorised"
    rationale: "Good for deductive research. Hypothesis stated, key terms defined, logical structure clear, reasoning mostly traceable. Some implicit assumptions about transfer learning applicability prevent excellent rating."

  transparency:
    score: 68
    band: "good"
    strengths:
      - "Three GitHub code repositories provided with clear descriptions"
      - "Training data preparation methodology documented"
      - "Limitations prominently acknowledged throughout paper"
    weaknesses:
      - "No formal data availability statement; field data and imagery not deposited"
      - "Computational environment underdocumented (no software versions, hyperparameters)"
      - "No pre-registration"
    rationale: "Good for deductive research. Clear research design, detailed methods with some gaps, excellent code availability, acknowledged data limitations. Missing pre-registration and complete environment documentation for excellent rating."

  cluster_synthesis:
    overall_rating: "strong"
    pattern_summary: "Strong conceptual clarity with moderate documentation completeness. Unusual transparency about failure modes enhances credibility. Code well-documented; data and environment less so."
    consistency_check: "consistent"
    implications:
      cluster_2: "Clear hypothesis and documented methods enable robust validity/robustness assessment. Acknowledged limitations provide explicit scope constraints."
      cluster_3: "Code availability strong (3 repos), but data unavailability and environment gaps will limit reproducibility score."
```
