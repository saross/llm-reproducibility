# Cluster 2: Evidential Strength Assessment

**Paper:** sobotkova-et-al-2024
**Assessment Date:** 2025-11-30
**Assessor Version:** v1.0

**Quality State:** HIGH
**Research Approach:** Deductive (confidence: high)
**Paper Type:** Empirical

---

## Signal Scores Summary

| Signal | Score | Band | Approach Anchors |
|--------|-------|------|------------------|
| Plausibility | 78 | Good | Deductive |
| Validity | 80 | Excellent | Deductive |
| Robustness | 72 | Good | Deductive |
| Generalisability | 76 | Good | Deductive |

**Cluster Rating:** Strong

---

## Signal 3: Plausibility

**Score:** 78/100 (Good)

**Approach anchors applied:** Deductive

### Assessment

The paper demonstrates good theoretical grounding for its hypothesis that pre-trained CNNs can detect burial mounds from satellite imagery. The research is situated within established frameworks of transfer learning (ResNet-50), computer vision, and archaeological remote sensing. The authors explicitly acknowledge the publication bias problem in ML-for-archaeology literature (C005: "ML-for-archaeology literature is overwhelmingly positive, reflecting publication bias and rhetoric of unconditional success"), positioning their work as a critical corrective.

The hypothesis is consistent with domain knowledge: CNNs have successfully detected archaeological features in other contexts, making the prediction that they could detect burial mounds reasonable. The paper appropriately draws on diffusion of innovations theory (C013) to contextualise adoption patterns.

Critically, anomalous results are acknowledged and explained rather than ignored. When the model failed (C001, C002), the authors investigated why: the CNN detected incidental features (roads, forest boundaries) rather than mounds themselves. This honest engagement with negative results strengthens plausibility - the explanation for failure is theoretically coherent (visual confounding in heterogeneous landscapes).

### Evidence

**Strengths:**
- C005: "ML-for-archaeology literature is overwhelmingly positive, reflecting publication bias" - theoretical grounding in publication bias literature with extensive citations
- C001: Limitations claim grounded in specific landscape characteristics (heterogeneous landscape with confounding features)
- RD003: "Negative results documentation design to counterbalance publication bias" - explicit theoretical rationale for paper's contribution
- E014-E018: Systematic review evidence (1,376 papers) supporting theoretical claims about literature patterns

**Weaknesses:**
- Limited discussion of why pre-trained models from general imagery might fail on archaeological features specifically
- Could strengthen theoretical explanation of CNN feature detection limitations

### Scoring Rationale

Score of 78 (Good) reflects: hypotheses theoretically motivated in transfer learning and remote sensing literature (60-79); generally consistent with domain knowledge (CNNs work for feature detection); anomalous results (model failure) thoroughly acknowledged and explained; framework coherent; minimal implausible assumptions. Slight gap from Excellent due to limited theoretical depth on CNN feature representation issues.

---

## Signal 4: Validity

**Score:** 80/100 (Excellent)

**Approach anchors applied:** Deductive

### Assessment

The paper demonstrates excellent validity for hypothesis-testing research. The evidence directly and appropriately addresses the hypothesis: can pre-trained CNNs detect burial mounds? The external validation design (RD001) compares model predictions against comprehensive field survey data from the Tundzha Regional Archaeological Project (TRAP), providing rigorous ground truth.

The sample is substantial and appropriate: 773 mounds documented through systematic field survey over 2009-2011, covering a 600 sq km study area. This ground truth dataset enables definitive assessment of model performance, not just self-reported accuracy metrics. The paper explicitly distinguishes between internal validation (automated train/test splits with misleadingly high F1 scores) and external validation against field data (which revealed the true failure).

Methods are appropriate for hypothesis testing. The 70:20:10 train/validation/test split follows ML best practices. The binary classification approach (MOUND/NO MOUND) is appropriate for the detection task. External validation against independent field data is the gold standard for ML model assessment.

Alternative explanations are explicitly considered. The paper investigates why the model failed: E001 reveals "self-reported success rates were misleadingly high" due to internal vs external validation differences; the model detected confounding features rather than mounds. Limitations are prominently stated throughout.

### Evidence

**Strengths:**
- RD001: "External validation design comparing ML model predictions against comprehensive field survey data" - rigorous validation approach
- E001: "12.8% of tiles tagged with >60% probability actually contained mounds" - precise quantitative evidence
- E005: "95.7% of known mounds escaped detection" - definitive failure evidence
- M006: "Field-based external validation comparing model predictions against surveyed ground truth" - appropriate methodology
- 773 mounds from systematic field survey provide robust ground truth

**Weaknesses:**
- E001 notes: Some expected information missing (validation protocol details, inter-rater reliability for field identification)
- Training data from visual inspection may have systematic bias

### Scoring Rationale

Score of 80 (Excellent) reflects: evidence directly addresses hypothesis through external validation (80-100 criterion); sample adequate with 773 ground truth mounds from systematic survey; methods appropriate for hypothesis testing (standard ML validation with external ground truth); alternative hypotheses considered (model detecting confounding features); confounds discussed (landscape heterogeneity); limitations prominently stated. Meets excellent criteria for deductive validity.

---

## Signal 5: Robustness

**Score:** 72/100 (Good)

**Approach anchors applied:** Deductive

### Assessment

The paper demonstrates good robustness through its two-run comparative design, which constitutes a form of sensitivity analysis for the core hypothesis. The 2021 and 2022 model runs tested whether training data curation affects performance: RD002 explicitly compares "all 773 cutouts for training regardless of what was visible" (2021) versus "249 cutouts where a mound was discernible with the naked eye" (2022). Both runs failed to detect mounds effectively, suggesting the conclusion is robust to training data composition.

Results appear consistent across analytical choices. The 60% probability threshold is tested, though threshold selection rationale is not fully documented. The failure is consistent across both model versions, reducing concern that results are artefactual or threshold-dependent.

However, sensitivity analysis is not comprehensive. The paper does not systematically test alternative thresholds, different CNN architectures beyond ResNet-50, or varying tile sizes. Some dependencies are documented (training data composition) but others remain unexplored (augmentation strategies, hyperparameters).

### Evidence

**Strengths:**
- RD002: "Comparative two-run design testing impact of training data curation" - built-in robustness test
- Consistent failure across 2021 and 2022 runs demonstrates robustness of negative conclusion
- M007: "Probability thresholding at >60%" documents analytical choice
- P001-P012: Detailed protocols document many analytical decisions

**Weaknesses:**
- Limited sensitivity analysis beyond training data curation
- M007 expected_information_missing: "Threshold selection rationale, threshold sensitivity analysis, alternative thresholds tested"
- M001 expected_information_missing: "Other models tested" - alternatives not systematically explored
- No cross-validation or bootstrap confidence intervals reported

### Scoring Rationale

Score of 72 (Good) reflects: some sensitivity analysis through two-run design (60-79); results appear robust to training data curation (60-79); some alternatives tested (curated vs uncurated training); assumptions stated (60% threshold) but not fully tested; dependencies documented for training data; some robustness evidence from consistent failure. Gap from Excellent due to limited systematic sensitivity testing and unexplored alternatives.

---

## Signal 6: Generalisability

**Score:** 76/100 (Good)

**Approach anchors applied:** Deductive

### Assessment

The paper demonstrates good scope constraint and appropriate limitation acknowledgement. Claims are explicitly bounded to the Kazanlak Valley context (C001): pre-trained CNNs fail "when detecting varied features of different sizes within a heterogeneous landscape that contains confounding natural and modern features, such as roads, forests and field boundaries."

The authors appropriately distinguish between their specific context and other potential applications. They note their landscape is particularly challenging due to modern development, agricultural modification, and heterogeneous terrain. The implicit transfer condition is that more homogeneous landscapes with less confounding features might yield better results.

Limitations are prominently stated throughout. The paper explicitly positions itself as a cautionary tale for "potential adopters of the technology" (RD003). Extrapolations are qualified: recommendations about manual inspection alternatives (C004) are presented as considerations rather than universal conclusions.

The scope of generalisation is well-matched to evidence. The paper does not claim CNNs can never work for burial mound detection; it claims they failed in this specific context with these specific methods.

### Evidence

**Strengths:**
- C001: "heterogeneous landscape that contains confounding natural and modern features" - explicit contextual constraints
- RD003: "counterbalance and cautionary tale to potential adopters" - appropriate scope for contribution
- C004: "manual inspection by experts or crowdsourcing may be more efficient" - qualified recommendation
- Explicit acknowledgement that results may not generalise beyond similar heterogeneous landscapes

**Weaknesses:**
- Limited discussion of what landscape characteristics would enable CNN success
- Transfer conditions could be more explicitly specified
- No formal population definition or external validity discussion

### Scoring Rationale

Score of 76 (Good) reflects: hypothesis scope clearly bounded to Kazanlak Valley context (60-79); limitations to external validity stated prominently (60-79); population, context, temporal bounds mostly clear; extrapolations appropriately qualified; some generalisability discussion around landscape characteristics; transfer considerations present though informal. Gap from Excellent due to implicit rather than explicit transfer conditions.

---

## Cluster Synthesis

**Overall Evidential Strength:** Strong

This paper demonstrates strong evidential strength across all four credibility signals, with scores ranging from 72-80 (Good to Excellent). The overall pattern reflects exemplary hypothesis-testing research that honestly reports negative results.

The highest score (Validity: 80) reflects the rigorous external validation design comparing CNN predictions against comprehensive field survey ground truth. This is the core methodological strength of the paper: rather than relying on potentially misleading internal accuracy metrics, the authors used independent field data to assess actual model performance.

The consistent performance across signals indicates coherent research design. Plausibility (78) is supported by appropriate theoretical grounding in ML literature and honest engagement with anomalous results. Robustness (72) benefits from the built-in sensitivity test (two-run design) though comprehensive sensitivity analysis is limited. Generalisability (76) is appropriately constrained with explicit contextual limitations.

### Pattern Summary

The dominant pattern is methodological rigour combined with intellectual honesty. The paper does not overstate its findings or ignore negative results. This is unusual in ML-for-archaeology literature (as the paper itself notes) and contributes to high credibility. The main credibility gap is limited exploration of analytical alternatives beyond the two-run design.

### Implications for Cluster 3

- **For Reproducibility:** Excellent code availability (3 GitHub repositories) suggests high potential for computational reproducibility. The detailed protocols (P001-P012) provide clear workflow documentation. Data availability gap (field survey data not deposited) may limit complete reproduction, but CNN training and validation code should be reproducible.

---

## Structured Output

```yaml
cluster_2_evidential_strength:
  paper_slug: "sobotkova-et-al-2024"
  assessment_date: "2025-11-30"
  quality_state: "high"
  research_approach: "deductive"

  plausibility:
    score: 78
    band: "good"
    strengths:
      - "Hypotheses grounded in transfer learning and remote sensing literature"
      - "Anomalous results (model failure) thoroughly acknowledged and explained"
      - "Publication bias critique positions work in broader methodological discourse"
    weaknesses:
      - "Limited theoretical depth on CNN feature representation limitations"
    rationale: "Good theoretical grounding with coherent explanation of failure. Anomalies addressed honestly. Gap from Excellent due to limited depth on why CNNs might fail on archaeological features specifically."

  validity:
    score: 80
    band: "excellent"
    strengths:
      - "External validation against comprehensive field survey ground truth (773 mounds)"
      - "Rigorous distinction between internal and external validation"
      - "Alternative explanations explicitly considered (model detecting confounds)"
      - "Quantitative performance metrics with definitive evidence"
    weaknesses:
      - "Some validation protocol details missing (inter-rater reliability)"
    rationale: "Excellent deductive validity. Evidence directly addresses hypothesis through external validation gold standard. Sample adequate. Methods appropriate. Alternatives considered. Limitations stated."

  robustness:
    score: 72
    band: "good"
    strengths:
      - "Two-run comparative design tests training data curation sensitivity"
      - "Consistent failure across runs demonstrates conclusion robustness"
      - "Analytical choices documented in protocols"
    weaknesses:
      - "Limited sensitivity analysis beyond training data comparison"
      - "Threshold sensitivity not systematically tested"
      - "Alternative architectures not explored"
    rationale: "Good robustness with built-in sensitivity test. Gap from Excellent due to limited systematic exploration of analytical alternatives."

  generalisability:
    score: 76
    band: "good"
    strengths:
      - "Claims explicitly bounded to Kazanlak Valley context"
      - "Landscape heterogeneity constraints clearly stated"
      - "Appropriate positioning as cautionary tale"
      - "Extrapolations qualified"
    weaknesses:
      - "Transfer conditions implicit rather than explicit"
      - "Limited specification of conditions for CNN success"
    rationale: "Good scope constraint with explicit contextual limitations. Gap from Excellent due to informal transfer condition specification."

  cluster_synthesis:
    overall_rating: "strong"
    pattern_summary: "Coherent credibility profile reflecting rigorous hypothesis-testing with honest negative results. Highest score on Validity (external validation design). Consistent Good-to-Excellent across all signals."
    consistency_check: "consistent"
    implications:
      cluster_3: "Excellent code availability suggests high reproducibility potential. Data gap may limit complete reproduction but CNN workflow should be reproducible."
```
