# Cluster 2: Evidential Strength Assessment

**Paper:** sobotkova-et-al-2024
**Assessment Date:** 2025-11-30
**Run:** 03

**Quality State:** HIGH
**Research Approach:** Deductive
**Paper Type:** Empirical

---

## Signal Scores Summary

| Signal | Score | Band | Approach Anchors |
|--------|-------|------|------------------|
| Plausibility | 74 | Good | Deductive |
| Validity | 79 | Good | Deductive |
| Robustness | 66 | Good | Deductive |
| Generalisability | 75 | Good | Deductive |

**Cluster Rating:** Strong

---

## Signal 3: Plausibility

**Score:** 74/100 (Good)

### Assessment

Good theoretical grounding in transfer learning and computer vision literature. The research question (whether pre-trained CNNs can detect burial mounds) is well-motivated. Anomalous results (counterintuitive failure of curated training data) are thoroughly examined and explained. Framework is internally coherent.

### Scoring Rationale

Score of 74 (Good) reflects strong theoretical motivation and thorough explanation of anomalous findings. Not Excellent because hypothesis is implicit rather than formally derived from theory.

---

## Signal 4: Validity

**Score:** 79/100 (Good)

### Assessment

Strong validity through external validation against 773 field-verified mounds. The ground truth dataset is independent and systematically collected. Two-run comparison tests alternative hypothesis about training data selection. Methods appropriate for research question. Limitations extensively acknowledged.

### Scoring Rationale

Score of 79 (Good) reflects strong external validation and appropriate methods. Approaches Excellent but constrained by single study area and lack of direct comparison with other ML approaches.

---

## Signal 5: Robustness

**Score:** 66/100 (Good)

### Assessment

Two-run design provides meaningful sensitivity testing for training data selection. The consistent failure across both approaches strengthens the negative conclusion. However, limited exploration of threshold sensitivity (only >60% used) and tile size parameters.

### Scoring Rationale

Score of 66 (Good) reflects valuable two-run comparison but limited scope of parameter sensitivity analysis.

---

## Signal 6: Generalisability

**Score:** 75/100 (Good)

### Assessment

Claims appropriately bounded to Kazanlak Valley context. Extensive limitation discussion acknowledges constraints of heterogeneous landscape. Transfer conditions to other contexts clearly specified. Authors avoid overgeneralisation despite negative findings.

### Scoring Rationale

Score of 75 (Good) reflects appropriate scope constraint and thorough limitation discussion. Single study area prevents Excellent, but cautious framing is appropriate.

---

## Cluster Synthesis

**Overall Evidential Strength:** Strong

All four signals in Good band (66-79). Validity strongest through robust external validation. Robustness adequate but limited in scope.

```yaml
cluster_2_evidential_strength:
  plausibility: {score: 74, band: "good"}
  validity: {score: 79, band: "good"}
  robustness: {score: 66, band: "good"}
  generalisability: {score: 75, band: "good"}
  overall_rating: "strong"
```
