# Cluster 1: Foundational Clarity Assessment

**Paper:** sobotkova-et-al-2024
**Assessment Date:** 2025-11-28
**Assessor Version:** v1.0

**Quality State:** HIGH
**Research Approach:** deductive (confidence: high)
**Paper Type:** empirical

---

## Signal Scores Summary

| Signal | Score | Band | Approach Anchors |
|--------|-------|------|------------------|
| Comprehensibility | 78 | Good | deductive |
| Transparency | 78 | Good | deductive |

**Cluster Rating:** Strong

---

## Signal 1: Comprehensibility

**Score:** 78/100 (Good)

**Approach anchors applied:** deductive

### Assessment

This validation study demonstrates good comprehensibility for deductive research. The core validation framework is clearly articulated: ML model predictions (functioning as implicit hypotheses) are tested against comprehensive field survey data (ground truth), with results reported as quantified performance metrics. The logical structure of prediction → test → result is transparent throughout.

Claims are specific and bounded. Rather than vague assertions about "model limitations," the paper reports precise outcomes: "high false positive (87.1%) and false negative (95.3%) rates" (C001-C002). The scope is explicitly constrained to the Kazanlak Valley context, avoiding over-generalisation. Technical terms (CNN, transfer learning, false positive/negative, F1 score) are defined or used consistently within established ML conventions.

The paper falls short of excellent comprehensibility primarily because the validation predictions are not framed as formal hypotheses. While RD001 and RD002 describe validation designs, neither states testable hypotheses in conventional form (e.g., "H1: The pre-trained CNN will detect >80% of known mounds"). The prediction-testing logic is clear, but the hypothesis structure remains implicit rather than operationally defined.

### Evidence

**Strengths:**
- C001: "Our attempt to deploy a pre-trained CNN demonstrates the limitations of this approach when it is used to detect varied features of different sizes within a heterogeneous landscape" — Clear, bounded finding with specified conditions
- RD001: "External validation design comparing ML model predictions against comprehensive field survey data" — Explicit validation framework with clear rationale
- RD004: Cost-benefit analysis with quantified comparison (135 hours ML development vs 42 hours manual processing) — Claims evaluable against specific metrics

**Weaknesses:**
- RD002 notes "Hypothesis stated explicitly" as expected information missing — validation design clear, but formal hypothesis absent
- Implicit arguments (IA001-IA005) reveal sophisticated reasoning, but some key assumptions unstated (e.g., "self-reported metrics insufficient without field validation")

### Scoring Rationale

Score of 78 falls in the Good band (60-79) for deductive research. The paper meets Good criteria: hypotheses/predictions stated (implicitly through validation design), most key terms defined, logical structure mostly clear, claims understandable and evaluable. Score does not reach Excellent (80-100) because validation predictions are not explicitly stated as testable hypotheses, and some key assumptions remain implicit (documented in IA001-IA005). Reasoning from test results to conclusions is clear, supporting upper range of Good band.

---

## Signal 2: Transparency

**Score:** 78/100 (Good)

**Approach anchors applied:** deductive

### Assessment

The paper demonstrates good transparency for a deductive validation study. Research designs are explicitly stated with rationale (RD001-RD004). Methods documentation is comprehensive, with 7 methods and 12 protocols extracted covering the ML workflow from model selection through validation. The validation approach is transparent: predictions tested against field-verified ground truth with performance metrics reported.

Transparency is enhanced by the explicit documentation of methodological gaps. The extraction notes "expected_information_missing" fields throughout (e.g., training hyperparameters, hardware specifications, decision threshold selection criteria). While these represent transparency gaps, the paper's acknowledgement of limitations (RD003: "negative results documentation design") and detailed discussion of failure modes demonstrates commitment to methodological transparency.

The paper provides code availability through three GitHub repositories: (1) cnn-testing for training data preparation and validation, (2) burial-mounds for 2021 CNN classifier, and (3) MoundDetection for 2022 CNN classifier. This significantly supports analytical reproducibility. However, the paper falls short of excellent transparency because code repositories lack persistent identifiers (DOIs), no field survey data is shared (historical data from TRAP 2009-2011 not deposited), and some ML implementation details remain under-documented (augmentation techniques, cross-validation approach, computational environment). For deductive ML research, the 80-100 band requires "data and code publicly available with persistent identifiers."

### Evidence

**Strengths:**
- RD001-RD004: Four explicit research designs with stated rationale — comprehensive design documentation
- M001-M007: Detailed method descriptions including transfer learning (M001), binary classification (M003), performance evaluation (M005)
- P001-P005: Protocols document specific procedures (150x150m cutouts, 1:2 class ratio, 70:20:10 train/val/test split)
- Three GitHub repositories provide code for training data preparation, CNN classifiers (2021, 2022 versions) — supports analytical reproducibility
- Extensive limitations discussion (RD003 explicitly frames as "counterbalance" to publication bias)

**Weaknesses:**
- P001 notes missing: "Hardware specifications, Training time, Framework/library used" — computational environment not fully specified
- P003 notes missing: "Seed for reproducibility" — random sampling not reproducible
- M004 notes missing: "Augmentation techniques used, Augmentation factor" — key ML details under-documented
- Code repositories lack persistent identifiers (DOIs); field survey data not deposited

### Scoring Rationale

Score of 78 falls in the upper Good band (60-79) for deductive research. The paper meets Good criteria with notable strengths: clear research design and hypothesis specification (implicit), detailed methods documentation, major limitations acknowledged, and code publicly available via three GitHub repositories. Score does not reach Excellent (80-100) because code lacks persistent identifiers (no DOIs), field survey data is not deposited, and computational environment is not fully specified. The combination of code availability, thorough methods documentation, and explicit limitations acknowledgement supports upper range of Good band.

---

## Cluster Synthesis

**Overall Foundational Clarity:** Strong

Both signals score identically at 78 (Good band), with consistent patterns across dimensions. The paper demonstrates strong foundational clarity for a deductive validation study: the validation framework is transparent, claims are specific and bounded, methods are well-documented, code is publicly available, and limitations are extensively discussed.

### Pattern Summary

The paper excels at methodological transparency regarding what was done and why, with code available via three GitHub repositories supporting analytical reproducibility. Remaining gaps are in persistent identifiers for code (no DOIs), field data sharing (historical TRAP data not deposited), and some computational environment details. The validation logic is clear, but formal hypothesis specification is implicit rather than explicit — appropriate for the validation study genre, though not meeting the highest deductive standards.

### Implications for Subsequent Assessment

- **For Cluster 2 (Evidential Strength):** High foundational clarity enables confident assessment of Validity and Robustness. The transparent validation design and specific performance metrics provide clear basis for evaluating evidential adequacy. The two-run comparative design (RD002) provides robustness evidence.

- **For Cluster 3 (Reproducibility & Scope):** Replicability assessment is supported by code availability (three GitHub repos), though constrained by absence of field data sharing and lack of persistent identifiers. Transparency score (78) suggests good analytical reproducibility. Generalisability well-addressed — paper explicitly constrains scope to Kazanlak Valley and discusses environmental factors affecting transferability (IA005).

---

## Structured Output

```yaml
cluster_1_foundational_clarity:
  paper_slug: "sobotkova-et-al-2024"
  assessment_date: "2025-11-28"
  quality_state: "high"
  research_approach: "deductive"

  comprehensibility:
    score: 78
    band: "good"
    strengths:
      - "Clear validation framework: prediction → test → result structure transparent"
      - "Claims specific and bounded with quantified outcomes (87.1% false positive, 95.3% false negative)"
      - "Explicit research designs with stated rationale (RD001-RD004)"
    weaknesses:
      - "Validation predictions not stated as formal hypotheses"
      - "Some key assumptions implicit (documented in IA001-IA005)"
    rationale: "Good band (60-79) for deductive. Validation logic clear, claims evaluable, logical structure transparent. Falls short of Excellent due to implicit hypothesis structure."

  transparency:
    score: 78
    band: "good"
    strengths:
      - "Comprehensive methods documentation (7 methods, 12 protocols)"
      - "Explicit research designs with rationale"
      - "Three GitHub repositories for code (cnn-testing, burial-mounds, MoundDetection)"
      - "Extensive limitations discussion and negative results framing"
    weaknesses:
      - "Code repositories lack persistent identifiers (DOIs)"
      - "Field survey data not deposited"
      - "Computational environment under-documented"
      - "Some ML implementation details missing (augmentation, hyperparameters)"
    rationale: "Good band (60-79) for deductive. Clear design, detailed methods, code available via GitHub, limitations acknowledged. Falls short of Excellent due to lack of persistent identifiers and no data sharing."

  cluster_synthesis:
    overall_rating: "strong"
    pattern_summary: "Identical Good scores (78) across both signals. Strong methodological transparency, specific claims, clear validation logic, code available. Remaining gaps in persistent identifiers and data sharing."
    consistency_check: "consistent"
    implications:
      cluster_2: "High clarity enables confident Validity/Robustness assessment. Two-run design provides robustness evidence."
      cluster_3: "Replicability supported by code availability. Generalisability well-addressed with explicit scope constraints."
```
