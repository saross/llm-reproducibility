# Cluster 2: Evidential Strength Assessment

**Paper:** sobotkova-et-al-2024
**Assessment Date:** 2025-11-30
**Run:** 04

**Quality State:** HIGH
**Research Approach:** Deductive
**Paper Type:** Empirical

---

## Signal Scores Summary

| Signal | Score | Band | Approach Anchors |
|--------|-------|------|------------------|
| Plausibility | 75 | Good | Deductive |
| Validity | 80 | Excellent | Deductive |
| Robustness | 67 | Good | Deductive |
| Generalisability | 77 | Good | Deductive |

**Cluster Rating:** Strong

---

## Signal 3: Plausibility

**Score:** 75/100 (Good)

### Assessment

Well-grounded in transfer learning and computer vision literature. Research question appropriately motivated by prior ML successes and the gap in critical assessment. Anomalous results (worse performance with curated data) explained through background feature detection mechanism.

### Scoring Rationale

Score of 75 (Good) reflects solid theoretical grounding and coherent explanation of anomalies. Not Excellent because hypothesis is implicit rather than formally derived.

---

## Signal 4: Validity

**Score:** 80/100 (Excellent)

### Assessment

Strong external validation against 773 independently collected field-verified mounds. Two-run design tests alternative hypothesis about training strategy. Methods appropriate for research question. Extensive acknowledgement of limitations.

### Scoring Rationale

Score of 80 (Excellent) reflects rigorous external validation and appropriate methods. Meets Excellent threshold through independent ground truth and systematic validation.

---

## Signal 5: Robustness

**Score:** 67/100 (Good)

### Assessment

Two-run comparison provides meaningful sensitivity analysis for training data selection. Consistent failure across both runs strengthens negative conclusion. Limited exploration of other parameters (threshold values, tile sizes).

### Scoring Rationale

Score of 67 (Good) reflects valuable two-run comparison but limited parameter exploration.

---

## Signal 6: Generalisability

**Score:** 77/100 (Good)

### Assessment

Claims appropriately bounded to Kazanlak Valley. Authors explicitly compare to successful Siberian applications, noting landscape heterogeneity as key difference. Transfer conditions carefully specified. Appropriate scope constraint.

### Scoring Rationale

Score of 77 (Good) reflects careful scope bounding and explicit transfer conditions. Single study area prevents Excellent.

---

## Cluster Synthesis

**Overall Evidential Strength:** Strong

Validity reaches Excellent; other signals in Good band. Strong overall evidential support.

```yaml
cluster_2_evidential_strength:
  plausibility: {score: 75, band: "good"}
  validity: {score: 80, band: "excellent"}
  robustness: {score: 67, band: "good"}
  generalisability: {score: 77, band: "good"}
  overall_rating: "strong"
```
