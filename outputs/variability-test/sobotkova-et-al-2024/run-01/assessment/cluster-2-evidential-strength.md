# Cluster 2: Evidential Strength Assessment

**Paper:** sobotkova-et-al-2024
**Assessment Date:** 2025-12-01
**Run:** 01

**Quality State:** HIGH
**Research Approach:** Deductive
**Paper Type:** Empirical

---

## Signal Scores Summary

| Signal | Score | Band | Approach Anchors |
|--------|-------|------|------------------|
| Plausibility | 75 | Good | Deductive |
| Validity | 82 | Excellent | Deductive |
| Robustness | 70 | Good | Deductive |
| Generalisability | 76 | Good | Deductive |

**Cluster Rating:** Strong

---

## Signal 3: Plausibility

**Score:** 75/100 (Good)

### Assessment

Research question well-grounded in transfer learning literature and prior successful applications (e.g., Caspari and Crespo 2019 in Siberia). Motivation clearly established through gap between optimistic literature and real-world challenges. Counterintuitive finding (curated training data performing worse) explained through plausible mechanism (background feature detection). Limitations of the specific approach clearly bounded.

### Strengths

- Strong theoretical grounding in transfer learning literature
- Clear motivation through literature gap analysis
- Counterintuitive results explained through mechanism
- Prior work properly contextualised

### Weaknesses

- Hypothesis implicit rather than formally stated
- Alternative explanations for failure not exhaustively explored

### Scoring Rationale

Score of 75 (Good) reflects strong theoretical grounding and coherent explanation of unexpected results. Not Excellent due to implicit hypothesis formulation and incomplete exploration of alternative explanations.

---

## Signal 4: Validity

**Score:** 82/100 (Excellent)

### Assessment

Rigorous external validation against 773 independently collected, field-verified mounds. Ground truth data collected through systematic pedestrian survey over 85 sq km (2009-2011), independent from model development. Two-run comparison tests alternative hypothesis (curated vs. uncurated training data). Methods appropriate for research question. Extensive limitation acknowledgement strengthens rather than undermines validity.

### Strengths

- 773 independent field-verified mounds as ground truth
- Ground truth temporally and methodologically independent from model
- Two-run design tests alternative training strategies
- Comprehensive limitation disclosure

### Weaknesses

- Ground truth from single geographic region
- Validation threshold (>60% probability) somewhat arbitrary

### Scoring Rationale

Score of 82 (Excellent) reflects rigorous independent validation and appropriate methods. Meets Excellent threshold through external ground truth verification.

---

## Signal 5: Robustness

**Score:** 70/100 (Good)

### Assessment

Two-run design provides meaningful robustness test through comparison of training strategies (all mounds vs. visible mounds only). Consistent failure across both approaches strengthens negative conclusion. Limited exploration of parameter sensitivity (only >60% threshold). No formal sensitivity analysis of tile size, overlap, or other model parameters.

### Strengths

- Two-run comparison with different training data
- Consistent failure pattern across approaches
- Results stable across both model versions

### Weaknesses

- Limited threshold exploration (only >60%)
- No tile size sensitivity analysis
- No formal parameter sensitivity testing

### Scoring Rationale

Score of 70 (Good) reflects meaningful comparative design but limited parameter exploration. Findings robust within tested conditions but sensitivity to parameter choices not systematically assessed.

---

## Signal 6: Generalisability

**Score:** 76/100 (Good)

### Assessment

Claims appropriately bounded to Kazanlak Valley context. Comparison to Siberian success (Caspari and Crespo 2019) explicitly addresses landscape heterogeneity as key factor. Transfer conditions (homogeneous vs. heterogeneous landscapes) well-specified. Authors avoid overgeneralisation, explicitly noting their results apply to "varied features in heterogeneous landscapes." Broader implications for ML adoption appropriately hedged.

### Strengths

- Claims explicitly bounded to study region
- Landscape heterogeneity identified as limiting factor
- Comparison to contrasting (successful) case
- Authors avoid overgeneralisation

### Weaknesses

- Single study area limits scope
- Transfer to other heterogeneous landscapes untested
- No cross-validation across sub-regions

### Scoring Rationale

Score of 76 (Good) reflects appropriate scope constraint and explicit specification of transfer conditions. Single site prevents Excellent, but careful boundary specification strengthens generalisability within stated limits.

---

## Cluster Synthesis

**Overall Evidential Strength:** Strong

Validity reaches Excellent through rigorous independent ground truth validation. Other signals consistently in Good band with strong support from well-designed comparative study.

```yaml
cluster_2_evidential_strength:
  plausibility: {score: 75, band: "good"}
  validity: {score: 82, band: "excellent"}
  robustness: {score: 70, band: "good"}
  generalisability: {score: 76, band: "good"}
  overall_rating: "strong"
```
