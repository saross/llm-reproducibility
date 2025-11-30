# Cluster 2: Evidential Strength Assessment

**Paper:** sobotkova-et-al-2024
**Assessment Date:** 2025-11-30
**Run:** 05

**Quality State:** HIGH
**Research Approach:** Deductive
**Paper Type:** Empirical

---

## Signal Scores Summary

| Signal | Score | Band | Approach Anchors |
|--------|-------|------|------------------|
| Plausibility | 76 | Good | Deductive |
| Validity | 81 | Excellent | Deductive |
| Robustness | 68 | Good | Deductive |
| Generalisability | 78 | Good | Deductive |

**Cluster Rating:** Strong

---

## Signal 3: Plausibility

**Score:** 76/100 (Good)

### Assessment

Well-grounded in transfer learning literature. Research question motivated by prior successes and critical assessment gap. Counterintuitive results (curated data performing worse) explained through background feature detection mechanism.

### Scoring Rationale

Score of 76 (Good) reflects strong theoretical grounding and coherent anomaly explanation. Not Excellent due to implicit hypothesis.

---

## Signal 4: Validity

**Score:** 81/100 (Excellent)

### Assessment

Rigorous external validation against 773 independently verified mounds. Two-run comparison tests alternative hypothesis. Methods appropriate. Extensive limitation acknowledgement strengthens credibility.

### Scoring Rationale

Score of 81 (Excellent) reflects strong independent validation and appropriate methods. Meets Excellent through rigorous external ground truth.

---

## Signal 5: Robustness

**Score:** 68/100 (Good)

### Assessment

Two-run design provides meaningful robustness test. Consistent failure across both approaches strengthens conclusions. Limited parameter sensitivity exploration (threshold, tile size).

### Scoring Rationale

Score of 68 (Good) reflects valuable comparison design but limited parameter exploration.

---

## Signal 6: Generalisability

**Score:** 78/100 (Good)

### Assessment

Claims appropriately bounded to Kazanlak Valley. Comparison to Siberian success explicitly addresses landscape heterogeneity factor. Transfer conditions specified. Authors avoid overgeneralisation.

### Scoring Rationale

Score of 78 (Good) reflects appropriate scope constraint and explicit transfer conditions. Single site prevents Excellent.

---

## Cluster Synthesis

**Overall Evidential Strength:** Strong

Validity reaches Excellent; other signals in Good band with strong support.

```yaml
cluster_2_evidential_strength:
  plausibility: {score: 76, band: "good"}
  validity: {score: 81, band: "excellent"}
  robustness: {score: 68, band: "good"}
  generalisability: {score: 78, band: "good"}
  overall_rating: "strong"
```
