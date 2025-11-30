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
| Comprehensibility | 78 | Good | Deductive |
| Transparency | 82 | Excellent | Deductive |

**Cluster Rating:** Strong

---

## Signal 1: Comprehensibility

**Score:** 78/100 (Good)

**Approach anchors applied:** Deductive

### Assessment

This paper demonstrates strong comprehensibility for deductive research. The core hypothesis — that a pre-trained CNN with transfer learning can effectively detect burial mounds — is implicit but clearly testable. The validation design comparing model predictions to field-verified data operationalises the test. Key claims are explicit, bounded, and quantified: "tile-based false negative rates were 95–96%, false positive rates were 87–95% of tagged tiles, while true positives were only 5–13%."

Key domain terms are well-defined. The paper explains CNN architecture (ResNet-18), transfer learning mechanisms, and validation metrics (F1 score, false positive/negative rates). The logical structure is transparent: design approach → apply to study area → generate predictions → validate against ground truth → evaluate success/failure. The two-run experimental design (all mounds vs. visible mounds only) is clearly articulated.

The argument structure is traceable from abstract through conclusion. Core claims (model failure, metric/performance mismatch, manual alternatives may be more efficient) are supported by specific quantitative evidence. Implicit arguments are identified but do not undermine comprehensibility — they bridge rather than obscure.

### Evidence

**Strengths:**
- C001: "Validation of results against field data showed that self-reported success rates were misleadingly high" — explicit, testable claim with clear evidence basis
- C008: "Counterintuitively, more selective training data led to worse model performance" — bounded claim with quantitative support
- RD003: Two-run experimental design explicitly stated with clear rationale

**Weaknesses:**
- IA003: "Volume of training data can compensate for quality" — this unstated assumption only becomes explicit in Discussion/Conclusion, reducing early comprehensibility slightly

### Scoring Rationale

Score of 78 (Good for deductive) reflects: hypotheses implicit but clearly testable (would need explicit hypothesis statement for 80+); key terms operationally defined (meets 60-79); logical structure transparent with clear reasoning from test results to conclusions (meets 60-79). Paper falls short of Excellent because hypothesis is implicit rather than explicitly stated as formal hypothesis, and some assumptions only become clear retrospectively.

---

## Signal 2: Transparency

**Score:** 82/100 (Excellent)

**Approach anchors applied:** Deductive

### Assessment

This paper demonstrates excellent transparency for deductive research. The research design is explicitly stated: comparative evaluation of CNN predictions against field-verified ground truth, with two-run experimental design comparing training data selection strategies. Methods are comprehensively documented: CNN architecture (ResNet-18 with modified binary classification head), transfer learning approach, training data preparation, tile-based detection, and validation procedures.

The paper provides exceptional code availability with three public GitHub repositories covering: (1) training data preparation and validation scripts, (2) 2021 CNN classifier, and (3) 2022 CNN classifier. This exceeds typical transparency standards. Data availability is more limited — field survey data is referenced to a prior publication (Ross et al. 2018) rather than directly deposited, and satellite imagery is commercial (IKONOS). However, the validation methodology is reproducible with the provided code.

Limitations are explicitly and extensively acknowledged. The Discussion section devotes substantial space to "Limitations and challenges of pre-trained CNNs" and the Conclusion acknowledges the failed approach directly. The paper is unusually transparent about failure, which itself enhances credibility.

### Evidence

**Strengths:**
- M002: "A ResNet-18 model pre-trained with ImageNet data was modified for binary classification" — detailed architecture documentation
- E017: Three public GitHub repositories provided — exceptional code transparency
- `reproducibility_infrastructure.code_availability.repositories`: All three repositories accessible with clear purpose descriptions

**Weaknesses:**
- No pre-registration mentioned (reduces score from potential 90+)
- Data availability limited: field data referenced rather than deposited, satellite imagery commercial

### Scoring Rationale

Score of 82 (Excellent for deductive) reflects: comprehensive methods with protocols documented (80-100 criterion); code publicly available with persistent URLs (80-100); explicit limitations (80-100). Score would be higher with pre-registration and direct data deposit, but paper meets Excellent threshold through exceptional code sharing and methodological documentation.

---

## Cluster Synthesis

**Overall Foundational Clarity:** Strong

This paper demonstrates strong foundational clarity across both signals. Comprehensibility is Good (78) — the logical structure is clear and claims are well-bounded, though formal hypothesis statement is implicit. Transparency is Excellent (82) — methods are thoroughly documented and code sharing is exceptional for archaeological research.

### Pattern Summary

Both signals consistently indicate strong foundational clarity. The paper's focus on documenting a "failure" has enhanced its transparency, as the authors have been careful to explain what they did and why it didn't work. This unusual transparency pattern (stronger documentation of failure than typical success papers) is notable and credible.

### Implications for Subsequent Assessment

- **For Cluster 2 (Evidential Strength):** Strong foundation enables confident assessment of Validity and Robustness. The clear methodology means evidence adequacy can be properly evaluated. The two-run design provides some robustness information.
- **For Cluster 3 (Reproducibility):** Excellent code sharing suggests strong Reproducibility signal. The computational workflow is documented and code is available. Main limitation is data access (commercial imagery, reference-only field data).

---

## Structured Output

```yaml
cluster_1_foundational_clarity:
  paper_slug: "sobotkova-et-al-2024"
  assessment_date: "2025-11-30"
  quality_state: "high"
  research_approach: "deductive"

  comprehensibility:
    score: 78
    band: "good"
    strengths:
      - "Core claims explicit, bounded, and quantified with clear evidence basis"
      - "Key terms operationally defined (CNN architecture, validation metrics)"
      - "Logical structure transparent from design through conclusions"
    weaknesses:
      - "Hypothesis implicit rather than formally stated"
      - "Some assumptions only become explicit in Discussion"
    rationale: "Good for deductive research. Hypotheses testable but implicit; key terms defined; logical structure clear. Falls short of Excellent due to implicit hypothesis statement."

  transparency:
    score: 82
    band: "excellent"
    strengths:
      - "Three public GitHub repositories with complete code"
      - "Comprehensive methods documentation including architecture details"
      - "Extensive, honest limitation discussion"
    weaknesses:
      - "No pre-registration"
      - "Data availability limited (reference-only, commercial imagery)"
    rationale: "Excellent for deductive research. Exceptional code sharing, comprehensive methods, explicit limitations. Would score higher with pre-registration and direct data deposit."

  cluster_synthesis:
    overall_rating: "strong"
    pattern_summary: "Consistent high clarity across both signals. Unusual transparency about failure enhances credibility."
    consistency_check: "consistent"
    implications:
      cluster_2: "Strong foundation enables confident Validity and Robustness assessment"
      cluster_3: "Excellent code sharing suggests strong Reproducibility; data access is main limitation"
```
