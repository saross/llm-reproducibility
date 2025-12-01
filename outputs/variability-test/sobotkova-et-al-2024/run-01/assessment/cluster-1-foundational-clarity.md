# Cluster 1: Foundational Clarity Assessment

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
| Comprehensibility | 80 | Excellent | Deductive |
| Transparency | 82 | Excellent | Deductive |

**Cluster Rating:** Strong

---

## Signal 1: Comprehensibility

**Score:** 80/100 (Excellent)

### Assessment

Excellent comprehensibility with explicit quantified claims throughout. The paper clearly states its purpose ("cautionary tale"), presents testable research questions, and follows a logical progression from literature review through methods, results, and discussion. Technical terminology (CNN, transfer learning, F1 scores) is well-explained for non-specialist readers. Claims are precisely quantified with confidence intervals implicit in the measurement methodology.

### Strengths

- Explicit, quantified performance claims (F1 scores, detection rates, false positive/negative rates)
- Clear experimental logic: train → apply → validate against ground truth
- Technical terms defined accessibly
- Research question clearly testable

### Weaknesses

- Hypothesis not formally stated (implicit in research design)
- Some ML technical detail assumes background knowledge

### Scoring Rationale

Score of 80 (Excellent) reflects clear argumentation, traceable logic, and explicit quantification. Meets Excellent threshold for deductive research through precise operationalisation and clear claim-evidence relationships.

---

## Signal 2: Transparency

**Score:** 82/100 (Excellent)

### Assessment

Excellent transparency through complete code sharing across three public GitHub repositories. Comprehensive methods documentation including training data preparation, model parameters, and validation protocols. Rare time-on-task reporting (135 person-hours) provides valuable resource transparency. Extensive limitation acknowledgement including honest discussion of failure modes and potential improvements.

### Strengths

- Three complete public repositories with all analysis code
- 135 person-hours explicitly documented (rare in ML-for-archaeology)
- Thorough limitation discussion with specific improvement paths
- Honest negative results reporting

### Weaknesses

- Commercial satellite imagery cannot be shared (commercial licensing)
- No formal environment specification (requirements.txt, Docker)
- No pre-registration

### Scoring Rationale

Score of 82 (Excellent) reflects exceptional code transparency, rare resource documentation, and scientific honesty about negative results. Meets Excellent threshold despite data constraints through comprehensive method disclosure.

---

## Cluster Synthesis

**Overall Foundational Clarity:** Strong

Both signals reach Excellent band, indicating strong foundational clarity through explicit claims, complete code transparency, and honest limitation acknowledgement.

```yaml
cluster_1_foundational_clarity:
  comprehensibility: {score: 80, band: "excellent"}
  transparency: {score: 82, band: "excellent"}
  overall_rating: "strong"
```
