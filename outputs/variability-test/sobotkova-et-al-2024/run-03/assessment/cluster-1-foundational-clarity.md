# Cluster 1: Foundational Clarity Assessment

**Paper:** sobotkova-et-al-2024
**Assessment Date:** 2025-12-05
**Assessor Version:** v1.0

**Quality State:** HIGH
**Research Approach:** deductive (confidence: high)
**Paper Type:** empirical

---

## Signal Scores Summary

| Signal | Score | Band | Approach Anchors |
|--------|-------|------|------------------|
| Comprehensibility | 82 | Excellent | deductive |
| Transparency | 78 | Good | deductive |

**Cluster Rating:** Strong

---

## Signal 1: Comprehensibility

**Score:** 82/100 (Excellent)

**Approach anchors applied:** deductive

### Assessment

This paper demonstrates excellent comprehensibility for deductive hypothesis-testing research. The central hypothesis is explicit and clearly bounded: testing whether "low-touch" transfer learning using pre-trained CNNs with minimal additional training can effectively detect archaeological features (burial mounds) in satellite imagery. The hypothesis is operationalised through a comparative two-run experimental design with pre-specified predictions.

All key terms are operationally defined: "low-touch approach" (pre-trained model with sufficient but minimally curated training data), false positive/negative rates, F1 scores, ground-truthed validation. The logical structure is transparent: hypothesis specification → method operationalisation → two-run comparative testing → field data validation → hypothesis rejection. Claims are unambiguous and testable, with clear reasoning from test results to conclusions.

The argument structure follows a classic hypothesis-testing format. The paper explicitly positions itself as a "cautionary tale" testing the proposition that transfer learning works for archaeological prospection — this framing makes the research design purpose transparent from the outset.

### Evidence

**Strengths:**
- C13: "We employed a pre-trained CNN model with a low-touch approach to additional training" — Explicit operationalisation of testable hypothesis
- C01: "Validation of results against field data showed that self-reported success rates were misleadingly high" — Clear, bounded claim with transparent reasoning from evidence
- RD01: Comparative Two-Run Experimental Design explicitly states testable predictions about training data curation effects

**Weaknesses:**
- Some ML technical terms (e.g., "trainable parameters", "F1 score") assume reader familiarity, though these are standard in the domain

### Scoring Rationale

Score: 82 (Excellent for deductive). Hypotheses explicitly stated and clearly bounded (80-100 criterion: "Hypotheses explicitly stated and clearly bounded"). All key terms operationally defined (model parameters, performance metrics, validation procedures). Logical structure of hypothesis testing transparent — from a priori predictions through comparative testing to hypothesis rejection. Claims unambiguous and testable. Minor limitation: some ML terminology assumed. Overall, this paper exemplifies clear hypothesis-testing communication.

---

## Signal 2: Transparency

**Score:** 78/100 (Good)

**Approach anchors applied:** deductive

### Assessment

The paper demonstrates good transparency for deductive research. While not pre-registered (understandable for a retrospective evaluation of existing fieldwork data), the research design is comprehensive and clearly specified. The comparative two-run experimental design with field data validation is explicitly documented, with detailed methods for model training, data preparation, and validation protocols.

Data and code availability is strong: three GitHub repositories provide complete access to CNN training scripts, data preparation workflows, and validation code. The paper includes detailed technical specifications (ResNet-50 with 25.6m trainable parameters, TensorFlow 2, 70:20:10 train/validation/test split, 150×150 pixel cutouts). All major limitations are explicitly acknowledged, including the failure of the approach and resource costs.

Minor transparency gaps exist: the field survey data from TRAP (773 mounds) is referenced but not deposited in a public repository, and IKONOS satellite imagery is proprietary. However, these are access restrictions rather than documentation failures.

### Evidence

**Strengths:**
- Code availability: Three public GitHub repositories (cnn-testing, burial-mounds, MoundDetection) with Python/R scripts
- M01: Detailed transfer learning methodology with model architecture, data augmentation, and training procedures specified
- P05: Field data validation protocol explicitly documented with probability thresholds and spatial intersection methods
- E02: Resource requirements transparently reported (135 person-hours)

**Weaknesses:**
- Data availability: Field survey data (773 mounds) not deposited in public repository
- Satellite imagery: IKONOS scenes proprietary (acquired through GeoEye Foundation grant)
- No pre-registration (though retrospective analysis using existing data)

### Scoring Rationale

Score: 78 (Good for deductive). Research design clearly specified (meets 60-79 "Clear research design and hypothesis specification"). Methods fully documented with protocols (meets 60-79 "Detailed methods"). Code publicly available on GitHub (meets 60-79 "code/workflow documented"). Data availability stated but with gaps — field data not deposited (60-79 not 80-100). Major limitations explicitly acknowledged including approach failure (meets 60-79 "major limitations acknowledged"). Falls short of Excellent due to data accessibility limitations and absence of pre-registration.

---

## Cluster Synthesis

**Overall Foundational Clarity:** Strong

This paper demonstrates strong foundational clarity appropriate for deductive hypothesis-testing research. Both signals score in the Good-to-Excellent range (82 and 78), with consistent patterns across both dimensions. The paper clearly communicates what hypothesis was tested, how it was tested, why it was tested, and what the results mean.

The consistency between Comprehensibility (82) and Transparency (78) reflects a research design that is both clearly articulated and well-documented. The 4-point gap is explained by data accessibility limitations (field data not publicly deposited, satellite imagery proprietary) rather than documentation quality issues.

### Pattern Summary

This paper exemplifies good practice for hypothesis-testing research in computational archaeology: explicit research questions, operationalised methods, comparative experimental design, external validation, transparent failure reporting. The "cautionary tale" framing is itself a transparency strength — explicitly positioning negative results as valuable contributions to methodological discourse.

### Implications for Subsequent Assessment

- **For Cluster 2 (Evidential Strength):** Strong foundational clarity enables confident assessment of evidence quality. The explicit methodology makes evidence-claim relationships easy to evaluate. Expect strong Validity scores given the 773-mound ground truth dataset.

- **For Cluster 3 (Reproducibility):** Code availability through three GitHub repositories positions this paper well for reproducibility assessment. The main limitation will be data accessibility (field data not deposited, imagery proprietary), which may constrain execution feasibility.

---

## Structured Output

```yaml
cluster_1_foundational_clarity:
  paper_slug: "sobotkova-et-al-2024"
  assessment_date: "2025-12-05"
  quality_state: "high"
  research_approach: "deductive"

  comprehensibility:
    score: 82
    band: "excellent"
    strengths:
      - "Hypothesis explicitly stated and clearly bounded (testing low-touch transfer learning for mound detection)"
      - "All key terms operationally defined (model architecture, performance metrics, validation procedures)"
      - "Logical structure of hypothesis testing fully transparent"
    weaknesses:
      - "Some ML terminology assumes domain familiarity"
    rationale: "Exemplary hypothesis-testing communication with explicit predictions, operationalised methods, and clear reasoning from evidence to conclusions."

  transparency:
    score: 78
    band: "good"
    strengths:
      - "Three public GitHub repositories with complete code"
      - "Comprehensive technical specification of methods and protocols"
      - "Resource requirements transparently reported (135 person-hours)"
      - "Explicit limitation acknowledgement including approach failure"
    weaknesses:
      - "Field survey data not deposited in public repository"
      - "Satellite imagery proprietary"
      - "No pre-registration (though retrospective analysis)"
    rationale: "Well-documented research design with good code availability. Data accessibility limitations prevent Excellent rating but documentation quality is high."

  cluster_synthesis:
    overall_rating: "strong"
    pattern_summary: "Consistent strong clarity across both signals reflecting well-documented hypothesis-testing research with explicit methodology and transparent failure reporting."
    consistency_check: "consistent"
    implications:
      cluster_2: "Strong foundational clarity enables confident evidence assessment. Expect strong Validity given 773-mound ground truth."
      cluster_3: "Code availability strong; main limitation is data accessibility for execution feasibility."
```
