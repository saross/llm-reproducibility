# Cluster 2: Evidential Strength Assessment

**Paper:** sobotkova-et-al-2024
**Assessment Date:** 2025-12-06
**Assessor Version:** v1.0

**Quality State:** HIGH
**Research Approach:** Deductive (confidence: high)
**Paper Type:** Empirical

---

## Signal Scores Summary

| Signal | Score | Band | Approach Anchors |
|--------|-------|------|------------------|
| Plausibility | 82 | Excellent | Deductive |
| Validity | 85 | Excellent | Deductive |
| Robustness | 68 | Good | Deductive |
| Generalisability | 72 | Good | Deductive |

**Cluster Rating:** Strong

---

## Signal 3: Plausibility

**Score:** 82/100 (Excellent)

**Approach anchors applied:** Deductive

### Assessment

The paper demonstrates excellent plausibility in its theoretical grounding and interpretation of results. The core hypothesis—that transfer learning with pre-trained CNNs can detect archaeological features in satellite imagery—is grounded in established deep learning literature and prior archaeological remote sensing research. The paper situates its approach within the growing body of ML applications in archaeology (citing 70 papers from Web of Science).

The results, while negative, are theoretically coherent. The finding that CNNs learned spurious correlations (bright lines, edges, roads) rather than mound morphology is consistent with known challenges in transfer learning when training data is limited and heterogeneous. The paper's interpretation that mound size variability (10-100m diameter) and background heterogeneity created an intractable learning problem is plausible and well-grounded in ML theory.

Anomalous results are explicitly acknowledged and explained: the failure to detect the largest, most visible mounds (E32) is surprising but interpreted coherently through the lens of what features the model actually learned. The theoretical framework is coherent throughout, with no implausible auxiliary assumptions required.

### Evidence

**Strengths:**
- C35: "Transfer learning assumes that large, complex models can be pre-trained using data from one domain, then fine-tuned for a specific task in another domain" - Clear theoretical grounding
- C39: "The challenge centres around the variability of the appearance of the mounds themselves, combined with the heterogeneous landscape surrounding them" - Coherent explanation of failure consistent with ML theory
- IA01: Implicit argument that F1 scores can systematically overestimate real-world performance - theoretically grounded insight

**Weaknesses:**
- Literature review methodology incomplete, limiting assessment of whether publication bias interpretation is fully grounded

### Scoring Rationale

Score of 82 (Excellent for deductive) reflects: hypotheses grounded in established ML and remote sensing theory; predictions consistent with domain knowledge (CNN detection should work if features are learnable); anomalous results (failed detection) explicitly acknowledged and coherently explained through feature learning theory; theoretical framework coherent; no implausible auxiliary assumptions. Meets all criteria for 80-100 band.

---

## Signal 4: Validity

**Score:** 85/100 (Excellent)

**Approach anchors applied:** Deductive

### Assessment

The paper demonstrates excellent validity through its rigorous validation design. The core strength is the use of independent ground-truth data: 773 mounds from TRAP 2009-2011 survey provide a robust validation dataset that was collected prior to and independently of the ML model development. This addresses the key deductive requirement that evidence directly addresses the hypothesis.

The sample is adequate: 773 mounds across 85 sq km of systematically surveyed area provides substantial ground-truth. The validation methodology is appropriate: spatial overlap between predicted tiles and known mound locations enables unambiguous true/false positive calculation. The 60% probability threshold, while potentially arbitrary, is clearly stated and applied consistently.

Alternative explanations for model failure are explicitly considered: training data quality (E10: 249 visible mounds vs 773 total), mound size heterogeneity (E28: 10-100m diameter), background complexity. Confounds are acknowledged: the paper recognises that the training data may have misled the model about detection targets. Limitations are clearly stated.

### Evidence

**Strengths:**
- E03/E04: "dataset of 773 mounds, collected by TRAP during 2009–2011 field survey" with "85 sq km inspected directly via pedestrian survey" - Independent, adequate ground-truth sample
- M03: "We assessed the quality of predictions made by the two models by comparing them to ground-truth data collected during pedestrian survey" - Direct validation methodology
- P08/P09: "mound-probability exceeded 0.599" with "spatially overlapping tiles" - Clear, reproducible validation criteria

**Weaknesses:**
- E10: Two-run comparison is informative but not a full sensitivity analysis of threshold or training parameters

### Scoring Rationale

Score of 85 (Excellent for deductive) reflects: evidence directly addresses hypothesis (independent ground-truth validation); sample adequate (773 mounds, 85 sq km); methods appropriate for testing (spatial validation against field data); alternative explanations considered (training data quality, mound heterogeneity); major confounds addressed (spurious feature learning); limitations stated. Meets all criteria for 80-100 band.

---

## Signal 5: Robustness

**Score:** 68/100 (Good)

**Approach anchors applied:** Deductive

### Assessment

The paper demonstrates good robustness through its two-run comparison and explicit acknowledgement of analytical choices. The comparison between 2021 run (all 773 mounds) and 2022 run (249 visible mounds only) provides some sensitivity analysis of training data composition. The finding that both runs failed—with the "better quality" training data actually performing worse—is informative about robustness.

However, the paper does not systematically vary other analytical choices: the 60% probability threshold is applied without testing alternatives; hyperparameters are not varied; only ResNet-50 is tested despite mentioning preliminary experiments with other models. The lack of systematic sensitivity analysis limits robustness assessment.

There is no triangulation with alternative detection methods (e.g., traditional image analysis, other ML architectures, human visual inspection as systematic comparison rather than anecdotal). The paper relies on a single analytical approach with only training data variation.

### Evidence

**Strengths:**
- RD02: "In the 2021 run of the model, we used all 773 cutouts for training... In the 2022 run, we selected 249 cutouts where a mound was discernible" - Two-run comparison provides some robustness evidence
- C09: "despite additional curation of the training data, the second run was even less successful than the first" - Robustness finding across training data conditions

**Weaknesses:**
- M02: "After some preliminary experimentation with a range of different pre-trained models" - Other models tested but not reported systematically
- P08: 60% threshold applied without sensitivity testing
- No hyperparameter sensitivity analysis

### Scoring Rationale

Score of 68 (Good for deductive) reflects: some sensitivity analysis through two-run comparison (60-79 criterion met); results appear robust to training data composition (both runs failed); some alternatives tested (multiple pre-trained models mentioned); assumptions mostly tested (transfer learning applicability); dependencies documented (ResNet-50, probability threshold). Falls short of Excellent (80-100) due to limited systematic sensitivity analysis of threshold, hyperparameters, and alternative architectures.

---

## Signal 7: Generalisability

**Score:** 72/100 (Good)

**Approach anchors applied:** Deductive

### Assessment

The paper demonstrates good attention to scope and limitations. Claims are explicitly bounded to the Kazanlak Valley context, the specific IKONOS imagery, and the specific mound population (Bronze and Iron Age burial mounds). The paper does not overclaim generalisability to other archaeological features, other regions, or other imagery types.

Limitations are thoroughly discussed: mound size variability (10-100m diameter), background heterogeneity, training data quality, and resource requirements are all acknowledged. The paper explicitly cautions against assuming that success in other archaeological ML applications will transfer to this context.

However, conditions for transfer to other contexts are not explicitly specified. The paper discusses why this approach failed but does not systematically identify what conditions would be needed for success (e.g., more homogeneous target features, larger training sets, different architectures). This limits the utility for readers seeking to apply the lessons to their own contexts.

### Evidence

**Strengths:**
- RD06: "The Kazanlak Valley in central Bulgaria was selected as the study area" - Clear geographic bounding
- C42: "Researchers and heritage specialists seeking efficient methods for extracting features from remotely sensed data should weigh the costs and benefits of ML versus manual approaches carefully" - Appropriately qualified recommendation
- C44: "The degree of manual intervention required... raises the question of whether it would be more efficient to identify all of the mounds manually" - Honest limitation acknowledgement

**Weaknesses:**
- Transfer conditions for successful application not systematically specified
- Resource threshold for ML vs manual approaches not quantified for other contexts

### Scoring Rationale

Score of 72 (Good for deductive) reflects: scope of hypothesis clearly bounded to Kazanlak Valley and specific imagery (60-79 criterion met); limitations to external validity stated; population/context bounds clear; extrapolations qualified; some generalisability discussion present. Falls short of Excellent (80-100) because transfer conditions for other contexts not systematically specified and threats to generalisation not fully enumerated.

---

## Cluster Synthesis

**Overall Evidential Strength:** Strong

The paper demonstrates strong evidential strength across all four signals, with particular excellence in Plausibility (82) and Validity (85). The core credibility claim—that this CNN approach failed to detect burial mounds despite good internal metrics—is well-supported by independent ground-truth validation and theoretically coherent interpretation.

The slightly lower Robustness score (68) reflects the lack of systematic sensitivity analysis beyond the two-run comparison, which is a genuine limitation but does not undermine the core findings. The Good Generalisability score (72) reflects appropriate scope constraint with some gaps in transfer condition specification.

### Pattern Summary

All four signals are in the Good-to-Excellent range, indicating a well-designed and well-executed deductive validation study. The pattern shows strongest performance in validity (direct hypothesis testing with independent data) and plausibility (theoretically grounded interpretation), with moderate limitation in robustness (limited sensitivity analysis beyond training data) and generalisability (transfer conditions not fully specified).

### Implications for Cluster 3

- **For Reproducibility:** Strong validity and good transparency suggest reproducibility should be high. However, the absence of persistent identifiers and some technical gaps (hyperparameters, software versions) may limit exact reproducibility. Code availability through GitHub is positive but needs verification.

---

## Structured Output

```yaml
cluster_2_evidential_strength:
  paper_slug: "sobotkova-et-al-2024"
  assessment_date: "2025-12-06"
  quality_state: "high"
  research_approach: "deductive"

  plausibility:
    score: 82
    band: "excellent"
    strengths:
      - "Hypothesis grounded in established ML and remote sensing theory"
      - "Anomalous results (failed detection) coherently explained through feature learning theory"
      - "Theoretical framework consistent with domain knowledge"
    weaknesses:
      - "Literature review methodology limits full assessment of publication bias interpretation"
    rationale: "Meets all criteria for Excellent (80-100): hypotheses grounded, predictions consistent, anomalies explained, framework coherent, no implausible assumptions."

  validity:
    score: 85
    band: "excellent"
    strengths:
      - "Independent ground-truth validation (773 mounds from prior TRAP survey)"
      - "Adequate sample size (85 sq km systematic survey)"
      - "Clear validation methodology (spatial overlap detection)"
    weaknesses:
      - "Two-run comparison informative but not full sensitivity analysis"
    rationale: "Meets all criteria for Excellent (80-100): evidence directly addresses hypothesis, sample adequate, methods appropriate, alternatives considered, confounds addressed, limitations stated."

  robustness:
    score: 68
    band: "good"
    strengths:
      - "Two-run comparison with different training data provides some sensitivity evidence"
      - "Results robust to training data composition (both runs failed)"
    weaknesses:
      - "60% threshold not systematically tested"
      - "Hyperparameter sensitivity not analysed"
      - "No triangulation with alternative methods"
    rationale: "Meets Good criteria (60-79): some sensitivity analysis, results appear robust, some alternatives tested. Falls short of Excellent due to limited systematic sensitivity analysis."

  generalisability:
    score: 72
    band: "good"
    strengths:
      - "Claims bounded to Kazanlak Valley and specific imagery"
      - "Limitations thoroughly discussed"
      - "Appropriately qualified recommendations"
    weaknesses:
      - "Transfer conditions for other contexts not systematically specified"
      - "Threshold for ML vs manual not quantified for other contexts"
    rationale: "Meets Good criteria (60-79): scope bounded, limitations stated, extrapolations qualified. Falls short of Excellent because transfer conditions not fully specified."

  cluster_synthesis:
    overall_rating: "strong"
    pattern_summary: "Excellent validity and plausibility with good robustness and generalisability. Well-designed deductive validation study with strong independent ground-truth evidence."
    consistency_check: "consistent"
    implications:
      cluster_3: "Strong validity and good transparency suggest reproducibility should be high; code availability through GitHub is positive but technical gaps may limit exact reproducibility"
```
