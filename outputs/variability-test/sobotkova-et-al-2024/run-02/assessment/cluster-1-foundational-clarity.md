# Cluster 1: Foundational Clarity Assessment

**Paper:** sobotkova-et-al-2024
**Assessment Date:** 2025-12-05
**Assessor Version:** v1.0

**Quality State:** HIGH
**Research Approach:** deductive
**Paper Type:** empirical

---

## Signal Scores Summary

| Signal | Score | Band | Approach Anchors |
|--------|-------|------|------------------|
| Comprehensibility | 78 | Good | deductive |
| Transparency | 72 | Good | deductive |

**Cluster Rating:** Strong

---

## Signal 1: Comprehensibility

**Score:** 78/100 (Good)

**Approach anchors applied:** deductive

### Assessment

The paper demonstrates strong comprehensibility for deductive research. The central hypothesis is clearly framed: transfer learning with pre-trained CNNs can detect burial mounds in satellite imagery. The title ("Validating predictions...") and abstract explicitly establish this as a hypothesis-testing study. Core claims are well-bounded and testable - C001 states "The CNN model failed to accurately detect burial mounds when validated against field data, with 95-96% false negative rates."

Key terms are operationally defined: "mounds" refer to 773 field-verified burial mounds from the TRAP survey; detection thresholds (60% probability), false positive/negative rates, and validation procedures are quantified. The logical structure flows clearly: hypothesis specification → methodology → empirical test → conclusion. The two-run comparative design (2021 vs 2022, different training data curation) adds methodological clarity.

Minor comprehensibility gaps exist around the literature review methodology (RD006) where 70 abstracts are analysed but the systematic search protocol is implicit rather than explicit. However, this is supplementary to the core hypothesis test.

### Evidence

**Strengths:**
- C001: "The CNN model failed to accurately detect burial mounds when validated against field data, with 95-96% false negative rates" - Precisely bounded, quantified hypothesis test result
- RD002: "Comparative evaluation of two CNN model runs with different training data curation levels" - Clear experimental design with control comparison
- C002: "Self-reported ML model metrics (F1=0.87) can be misleading without external field validation" - Well-scoped claim with specific metric reference

**Weaknesses:**
- RD006 (implicit): Literature review design undocumented - "44 abstracts (63%) fail to mention any negative aspects" presents results without explicit methodology
- Some implicit arguments around training data sufficiency assumptions (IA002, IA004)

### Scoring Rationale

Score of 78 reflects Good comprehensibility: hypotheses explicitly stated ("validating predictions"), key terms operationally defined (detection thresholds, validation rates), logical structure transparent (test → result → conclusion). Falls short of Excellent due to implicit literature review methodology and some undocumented assumptions about what constitutes sufficient training data.

---

## Signal 2: Transparency

**Score:** 72/100 (Good)

**Approach anchors applied:** deductive

### Assessment

The paper demonstrates good transparency for deductive research, with notable asymmetry between code and data sharing. The research design is explicitly stated across 6 documented research designs (RD001-RD005 explicit, RD006 implicit). Methods are comprehensively documented: 9 methods covering transfer learning (M001), data augmentation (M002), model assessment (M003), spatial validation (M004-M006), and computational workflows. 14 protocols detail specific procedures from tile generation to field recording.

Code availability is excellent: three GitHub repositories (cnn-testing, burial-mounds, MoundDetection) provide complete implementation code. HPC environment (UCloud at University of Southern Denmark) is documented. However, data transparency is limited - no formal data availability statement exists, field data from TRAP 2009-2011 is not deposited, and trained model weights are not shared. FAIR score of 62.5% (10/16) reflects this asymmetry.

The paper lacks pre-registration (acceptable for this type of research), but would benefit from data archiving. Limitations are acknowledged extensively in Discussion, particularly around training data quality and model architecture constraints.

### Evidence

**Strengths:**
- `reproducibility_infrastructure.code_availability`: 3 GitHub repositories (high machine-actionability)
- M001: "Binary image classification method using pre-trained CNN with transfer learning" - Comprehensive method documentation
- P001-P012: Detailed protocols for data preparation, model training, and validation

**Weaknesses:**
- `reproducibility_infrastructure.data_availability`: No formal statement, data not deposited (low machine-actionability)
- P013-P014 (implicit): Mound visibility assessment and model comparison protocols undocumented
- No pre-registration (acceptable but reduces transparency for deductive study)

### Scoring Rationale

Score of 72 reflects Good transparency: clear research design, detailed methods and protocols, extensive code sharing via GitHub. Falls short of Excellent due to data accessibility gap (no repository deposit), absence of pre-registration, and undocumented ancillary protocols. The asymmetric reproducibility profile (excellent code, minimal data) is characteristic of this score band.

---

## Cluster Synthesis

**Overall Foundational Clarity:** Strong

Both Comprehensibility (78) and Transparency (72) score in the Good band, with consistent patterns across both signals. The paper establishes clear hypothesis-testing framework with well-bounded claims and comprehensive methodological documentation. The primary limitation in both signals relates to implicit elements - literature review methodology for comprehensibility, data sharing for transparency.

### Pattern Summary

The paper demonstrates strong foundational clarity typical of well-executed deductive research. Claims are testable and bounded; methods are documented with protocols; code is publicly available. The consistent pattern is that explicit, documented elements score highly while implicit or undocumented elements (literature methodology, data deposit) create the gap between Good and Excellent.

### Implications for Subsequent Assessment

- **For Cluster 2 (Evidential Strength):** Strong foundation enables confident assessment of validity and robustness. Quantitative evidence (95-96% FN rates) clearly supports claims. Two-run comparison provides internal replication.
- **For Cluster 3 (Reproducibility & Scope):** Asymmetric reproducibility profile will affect scoring - computational workflow reproducible via GitHub, but data dependency creates gap. Scope claims appropriately bounded to study area.

---

## Structured Output

```yaml
cluster_1_foundational_clarity:
  paper_slug: "sobotkova-et-al-2024"
  assessment_date: "2025-12-05"
  quality_state: "high"
  research_approach: "deductive"

  comprehensibility:
    score: 78
    band: "good"
    strengths:
      - "Hypotheses explicitly stated with clear testing framework"
      - "Key terms operationally defined (detection thresholds, validation rates)"
      - "Logical structure transparent (hypothesis → test → conclusion)"
    weaknesses:
      - "Literature review methodology implicit"
      - "Some assumptions about training data sufficiency undocumented"
    rationale: "Good comprehensibility with explicit hypothesis testing framework and bounded claims. Falls short of excellent due to implicit supplementary methodology."

  transparency:
    score: 72
    band: "good"
    strengths:
      - "Three GitHub repositories with complete implementation code"
      - "Comprehensive methods and protocols documentation (9M, 14P)"
      - "HPC computational environment documented"
    weaknesses:
      - "No data repository deposit - asymmetric reproducibility"
      - "No pre-registration"
      - "Some protocols implicit (visibility assessment, model comparison)"
    rationale: "Good transparency with detailed methodology and excellent code sharing. Falls short of excellent due to data accessibility gap and absence of pre-registration."

  cluster_synthesis:
    overall_rating: "strong"
    pattern_summary: "Consistent Good scores across both signals reflect well-executed deductive research with explicit hypothesis testing and comprehensive documentation. Gaps relate to implicit elements rather than fundamental clarity issues."
    consistency_check: "consistent"
    implications:
      cluster_2: "Strong foundation enables confident validity/robustness assessment; quantitative evidence clearly supports claims"
      cluster_3: "Asymmetric reproducibility profile (code yes, data no) will shape reproducibility scoring; scope appropriately bounded"
```
