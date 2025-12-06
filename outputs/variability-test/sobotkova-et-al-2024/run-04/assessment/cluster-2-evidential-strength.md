# Cluster 2: Evidential Strength Assessment

**Paper:** sobotkova-et-al-2024
**Assessment Date:** 2025-12-05
**Assessor Version:** v1.0

**Quality State:** HIGH
**Research Approach:** Deductive (confidence: high)
**Paper Type:** Empirical

---

## Signal Scores Summary

| Signal | Score | Band | Approach Anchors |
|--------|-------|------|------------------|
| Plausibility | 82 | Excellent | Deductive |
| Validity | 80 | Excellent | Deductive |
| Robustness | 55 | Moderate | Deductive |
| Generalisability | 75 | Good | Deductive |

**Cluster Rating:** Strong

---

## Signal 3: Plausibility

**Score:** 82/100 (Excellent)

**Approach anchors applied:** Deductive

### Assessment

This paper demonstrates excellent plausibility for deductive hypothesis-testing research. The implicit hypotheses—that a pre-trained CNN can detect burial mounds and that training data curation would improve performance—are grounded in established machine learning theory and prior archaeological remote sensing literature. The paper explicitly references the theoretical basis for transfer learning (IA001: "pre-trained CNNs have been trained on much larger and more diverse datasets... meaning that they should learn more sophisticated ways to generate image representations").

The findings, while negative, are entirely consistent with domain knowledge about feature detection challenges in heterogeneous landscapes. The authors explicitly acknowledge why their results differ from expectations, citing the "wolves in snow" problem (IA005) where CNNs learn background features rather than targets. This honest treatment of anomalous results strengthens rather than weakens plausibility.

Implicit assumptions are made explicit throughout. IA002 acknowledges the assumption that "volume of training data would offset other shortcomings" and documents its failure. IA003 reveals the assumption that "Standard ML performance metrics adequately reflect real-world performance" and demonstrates why it failed. This reflexive treatment of assumptions exemplifies excellent scientific practice.

### Evidence

**Strengths:**
- C058: Transfer learning approach explicitly grounded in established ML theory
- IA001-IA005: All major assumptions identified and evaluated against evidence
- C057: Variability of mound appearance and heterogeneous landscapes explicitly identified as theoretical challenge
- Literature review (M006) situates findings within broader disciplinary context with evidence of publication bias (E005, E006)

**Weaknesses:**
- No prior quantitative predictions for expected detection rates — hypotheses are directional rather than precise
- Transfer learning assumption (ImageNet → archaeological features) could have been examined more critically a priori

### Scoring Rationale

Score of 82 (Excellent band for deductive research) because: Hypotheses grounded in established ML and remote sensing theory (80-100); predictions consistent with domain knowledge about feature detection challenges (80-100); anomalous results (negative findings) thoroughly acknowledged and explained via "wolves in snow" analogy and target-to-tile ratio analysis (80-100); theoretical framework coherent (80-100); implicit assumptions made explicit and evaluated (80-100). The score is at the lower end of Excellent because hypotheses were directional rather than quantitatively precise.

---

## Signal 4: Validity

**Score:** 80/100 (Excellent)

**Approach anchors applied:** Deductive

### Assessment

This paper demonstrates excellent validity for deductive hypothesis-testing research. The evidence directly addresses the implicit hypotheses through a well-designed comparative validation framework. The core methodological innovation—validating CNN predictions against independent ground-truthed field data—provides robust evidence for the central claims about model failure.

Evidence sufficiency is strong. The validation uses 773 GPS-located mounds (E007) collected across 85 sq km of systematic pedestrian survey (M008). This represents a substantial and geographically comprehensive ground-truth dataset. The two-condition experimental design (RD002) comparing all mounds vs. visible-only mounds provides controlled comparison.

Methods are appropriate for the research question. The spatial intersection protocol (P005) for calculating true positives, false positives, and false negatives is transparent and reproducible. Standard ML metrics (F1, precision, recall) are calculated alongside ground-truth validation, enabling direct comparison of internal vs. external performance (C002, C056).

Alternative explanations are considered. The discussion section explicitly explores multiple reasons for model failure: tile boundary effects (C061), target-to-tile ratio (C045), training data quality (C055), positive:negative ratio (C020), and background feature learning (C019). While not all alternatives are tested experimentally, their articulation strengthens validity.

### Evidence

**Strengths:**
- RD001: Comparative validation design explicitly tests predictions against independent ground truth
- E007: 773 ground-truthed mounds provides substantial sample
- M002: Field validation methodology clearly documented
- C061, C045, C020: Multiple alternative explanations for failure explicitly considered
- P005, P006: Validation protocols reproducible

**Weaknesses:**
- No alternative model architectures tested (only ResNet-50 after "preliminary experimentation")
- Sensitivity to probability threshold (60%) not systematically explored
- Alternative causes for failure identified but not experimentally isolated

### Scoring Rationale

Score of 80 (Excellent band for deductive research) because: Evidence directly addresses hypotheses through field validation (80-100); sample adequate with 773 ground-truthed mounds (80-100); methods appropriate for testing CNN performance (80-100); alternative explanations explicitly considered even if not all tested (60-79 to 80-100); major confounds addressed through experimental design (80-100); limitations clearly stated throughout (80-100). Reaches Excellent threshold due to strong ground-truth validation; slight reduction for limited experimental isolation of alternative explanations.

---

## Signal 5: Robustness

**Score:** 55/100 (Moderate)

**Approach anchors applied:** Deductive

### Assessment

This paper demonstrates moderate robustness for deductive hypothesis-testing research. While the paper includes a two-condition comparison (all mounds vs. visible mounds), this represents a narrow exploration of the analytical parameter space. Many analytical choices that could affect results were not systematically varied.

Sensitivity analysis is limited. The 60% probability threshold (P004) is applied without exploring alternative thresholds. The 150×150 pixel tile size is fixed without testing alternatives. The 70:20:10 data split follows convention but sensitivity to different splits is not assessed. The 1:2 positive:negative ratio is identified as potentially insufficient (C020), but alternatives are not tested.

The two model runs (2021, 2022) do represent a form of robustness testing, demonstrating that results were consistent across training data variations—both showed high false negative rates. However, this consistency is in the direction of failure, not success, limiting claims about analytical robustness of the approach.

Triangulation is minimal. Only one model architecture (ResNet-50) was used after "preliminary experimentation" whose results are not reported. No inter-observer reliability was assessed for manual aspects (e.g., selection of "visible" mounds for the 249-mound dataset). The literature review (M006) provides context but not analytical triangulation.

### Evidence

**Strengths:**
- RD002: Two training conditions tested (773 vs. 249 mounds), providing some robustness evidence
- C023: Comparison to "previous, manually trained model" provides baseline
- Both runs showed consistent failure patterns (high FN rates), demonstrating result stability

**Weaknesses:**
- P004: 60% threshold not varied or justified
- No alternative model architectures reported (VGG, other ResNets)
- No sensitivity analysis for tile size, overlap, or data split ratio
- E014: Selection of 249 "visible" mounds not assessed for inter-observer reliability
- No exploration of alternative probability thresholds for classification

### Scoring Rationale

Score of 55 (Moderate band for deductive research) because: Limited sensitivity analysis performed (40-59); results from two conditions consistent but narrow (40-59); few alternatives tested beyond single comparison (40-59); assumptions stated but not systematically tested (40-59); some dependencies noted (tile boundaries, ratio) but not experimentally explored (40-59); minimal robustness checks reported (40-59). Score is at higher end of Moderate because the two-condition experiment does provide some robustness evidence and the consistent failure across conditions is informative.

---

## Signal 7: Generalisability

**Score:** 75/100 (Good)

**Approach anchors applied:** Deductive

### Assessment

This paper demonstrates good generalisability for deductive hypothesis-testing research. The authors are appropriately cautious about generalising their negative findings, explicitly framing the paper as a "cautionary tale" (C011) rather than claiming universal conclusions about CNN applicability. Scope boundaries are clearly stated.

Geographic and contextual bounds are explicit. The study is explicitly bounded to the Kazanlak Valley, Bulgaria (RD005). The authors acknowledge that mound visibility "depends on their size, surrounding terrain, and local land cover" (C059), implying context-specific factors. The paper does not overclaim that all CNN applications to archaeology will fail—it identifies specific challenges in heterogeneous landscapes.

Limitations are prominently stated. The discussion section identifies specific factors contributing to failure: non-overlapping tiles (C061), small mound-to-tile ratio (C045), heterogeneous backgrounds (C057), and insufficient negative training data (C020). These limitations contextualise the findings and specify conditions under which results might differ.

Transfer conditions are partially specified. The paper suggests that CNN approaches might succeed for "homogeneous targets and backgrounds" (implied contrast with their heterogeneous case) but does not formally specify when transfer would be appropriate. The comparison to successful applications in other contexts (cited literature) provides implicit transfer guidance.

### Evidence

**Strengths:**
- C011: Paper explicitly framed as documenting "unsuccessful attempts" and highlighting "problems researchers are likely to face"
- RD005: Case study design explicitly bounded to Kazanlak Valley, Bulgaria
- C057: Heterogeneous landscape and variable mound appearance identified as context-specific challenges
- C062: Specific improvements identified for other contexts (resizing cutouts, segmentation, overlapping tiles)

**Weaknesses:**
- No formal specification of conditions where CNN approaches might succeed vs. fail
- Transfer to other archaeological features or landscapes not systematically analysed
- Sample from single geographic context (though with 773 mounds) limits generalisability claims

### Scoring Rationale

Score of 75 (Good band for deductive research) because: Hypothesis scope clearly bounded to case study context (60-79); main limitations explicitly acknowledged throughout (80-100); bounds mostly clear with geographic and methodological specification (60-79); extrapolations appropriately qualified as "cautionary tale" (80-100); some generalisability discussion through comparison to literature (60-79); transfer considerations present but not formalised (60-79). Score is at upper end of Good because the paper is exemplary in not overclaiming from negative results and in contextualising findings within the broader literature.

---

## Cluster Synthesis

**Overall Evidential Strength:** Strong

This paper exhibits strong evidential strength for deductive hypothesis-testing research. The two high-scoring signals—Plausibility (82) and Validity (80)—indicate that the paper's claims are well-grounded in theory and well-supported by appropriate evidence. The moderate Robustness score (55) reflects the limited sensitivity analysis rather than fundamental methodological weaknesses; the paper honestly documents a "failed" hypothesis rather than cherry-picking successful analyses. The good Generalisability score (75) reflects appropriate caution in not overclaiming from a single case study.

The overall pattern is characteristic of honest negative-result reporting. The paper does not manufacture robustness through selective reporting—it presents both model runs transparently despite both showing failure. The lower Robustness score is thus interpretable as methodological transparency rather than methodological weakness: the authors did not pursue extensive parameter tuning to find conditions under which the model might appear to succeed.

### Pattern Summary

The Plausibility-Validity-Generalisability scores form a coherent pattern: theoretically grounded hypotheses (82) tested with appropriate methods (80) leading to appropriately bounded conclusions (75). The Robustness score (55) is the outlier, but this reflects the paper's character as hypothesis-testing rather than parameter-optimisation research. The pattern indicates a paper that prioritises honest reporting over optimisation for publication.

### Implications for Cluster 3

- **For Reproducibility:** The strong Validity score (particularly the clear validation protocols P005-P007) supports computational reproducibility assessment. The three GitHub repositories provide the basis for re-executing the analytical workflow. However, the lack of deposited field data (773 mound points) limits full reproduction—the validation step cannot be independently repeated without access to ground-truth data. This creates an asymmetric reproducibility profile: analytical reproduction feasible, validation reproduction limited.

---

## Structured Output

```yaml
cluster_2_evidential_strength:
  paper_slug: "sobotkova-et-al-2024"
  assessment_date: "2025-12-05"
  quality_state: "high"
  research_approach: "deductive"

  plausibility:
    score: 82
    band: "excellent"
    strengths:
      - "Hypotheses grounded in established ML transfer learning theory"
      - "All major implicit assumptions identified and evaluated"
      - "Anomalous results thoroughly explained via theoretical analysis"
      - "Literature review contextualises findings within publication bias patterns"
    weaknesses:
      - "Hypotheses directional rather than quantitatively precise"
      - "Transfer learning assumption could have been examined more critically a priori"
    rationale: "Excellent plausibility for deductive research. Theoretical grounding strong, anomalies honestly addressed, implicit assumptions made explicit. Lower end of Excellent due to directional rather than precise predictions."

  validity:
    score: 80
    band: "excellent"
    strengths:
      - "Strong ground-truth validation against 773 GPS-located mounds"
      - "Comparative validation design with two training conditions"
      - "Clear validation protocols (spatial intersection, confusion matrix)"
      - "Multiple alternative explanations explicitly considered"
    weaknesses:
      - "Alternative model architectures not systematically compared"
      - "Probability threshold sensitivity not explored"
      - "Alternative causes identified but not experimentally isolated"
    rationale: "Excellent validity for deductive research. Evidence directly tests hypotheses through robust field validation. Strong sample size and clear protocols. Slight reduction for limited experimental isolation of alternatives."

  robustness:
    score: 55
    band: "moderate"
    strengths:
      - "Two training conditions provide some robustness evidence"
      - "Consistent failure patterns across both runs informative"
      - "Comparison to previous manually trained model provides baseline"
    weaknesses:
      - "60% probability threshold not varied or justified"
      - "No alternative model architectures systematically tested"
      - "No sensitivity analysis for tile size, overlap, or data split"
      - "No inter-observer reliability for visible mound selection"
    rationale: "Moderate robustness for deductive research. Two-condition comparison is informative but narrow. Limited sensitivity analysis reflects hypothesis-testing rather than parameter-optimisation approach."

  generalisability:
    score: 75
    band: "good"
    strengths:
      - "Paper explicitly framed as cautionary tale, not universal claim"
      - "Case study bounded to specific geographic context"
      - "Context-specific challenges (heterogeneous landscape) identified"
      - "Specific improvements for other contexts suggested"
    weaknesses:
      - "No formal specification of success vs. failure conditions"
      - "Single geographic context limits broader claims"
      - "Transfer conditions not systematically analysed"
    rationale: "Good generalisability for deductive research. Appropriately cautious about overclaiming from negative results. Explicit bounds and limitations. Upper end of Good due to exemplary contextualisation."

  cluster_synthesis:
    overall_rating: "strong"
    pattern_summary: "Coherent pattern of theoretically grounded (82) hypotheses tested with appropriate methods (80) yielding appropriately bounded conclusions (75). Lower Robustness (55) reflects honest reporting rather than methodological weakness."
    consistency_check: "consistent"
    implications:
      cluster_3: "Strong validation protocols support computational reproducibility. Asymmetric profile expected: analytical reproduction feasible via GitHub, validation reproduction limited by missing ground-truth data deposit."
```
