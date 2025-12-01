# Cluster 2: Evidential Strength Assessment

**Paper:** sobotkova-et-al-2024
**Assessment Date:** 2025-11-30
**Run:** 02

**Quality State:** HIGH
**Research Approach:** Deductive
**Paper Type:** Empirical

---

## Signal Scores Summary

| Signal | Score | Band | Approach Anchors |
|--------|-------|------|------------------|
| Plausibility | 73 | Good | Deductive |
| Validity | 78 | Good | Deductive |
| Robustness | 65 | Good | Deductive |
| Generalisability | 76 | Good | Deductive |

**Cluster Rating:** Strong

---

## Signal 3: Plausibility

**Score:** 73/100 (Good)

### Assessment

Good theoretical grounding in ML transfer learning literature. Anomalous results (model failure) thoroughly explained. Framework coherent.

### Scoring Rationale

Score of 73 (Good) reflects theoretical motivation and thorough anomaly handling. Not Excellent because hypothesis is implied rather than formally derived.

---

## Signal 4: Validity

**Score:** 78/100 (Good)

### Assessment

Strong evidence through external validation against 773 field-verified mounds. Two-run design tests alternative hypothesis. Methods appropriate for research question. Strong limitation acknowledgement.

### Scoring Rationale

Score of 78 (Good) reflects strong external validation evidence. Approaches Excellent but single study area and no direct method comparison limit score.

---

## Signal 5: Robustness

**Score:** 65/100 (Good)

### Assessment

Two-run design provides some sensitivity analysis. Consistent failure across both approaches strengthens conclusions. However, limited threshold and tile size sensitivity testing.

### Scoring Rationale

Score of 65 (Good) reflects meaningful two-run comparison but limited scope of sensitivity analyses.

---

## Signal 6: Generalisability

**Score:** 76/100 (Good)

### Assessment

Claims carefully bounded to Kazanlak Valley context. Extensive limitation discussion. Transfer conditions specified. Appropriate scope constraint.

### Scoring Rationale

Score of 76 (Good) reflects strong scope constraint and limitation acknowledgement. Single study area prevents Excellent.

---

## Cluster Synthesis

**Overall Evidential Strength:** Strong

All four signals in Good band (65-78). Validity strongest through external validation. Robustness weakest but still adequate.

```yaml
cluster_2_evidential_strength:
  plausibility: {score: 73, band: "good"}
  validity: {score: 78, band: "good"}
  robustness: {score: 65, band: "good"}
  generalisability: {score: 76, band: "good"}
  overall_rating: "strong"
```
