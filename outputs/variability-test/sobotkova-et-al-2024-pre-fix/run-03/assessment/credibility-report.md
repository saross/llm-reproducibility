# Credibility Assessment Report

**Paper:** sobotkova-et-al-2024
**Title:** Validating Predictions of Burial Mounds with Field Data
**Assessment Date:** 2025-11-30
**Run:** 03

---

## Executive Summary

This paper tests whether a pre-trained Convolutional Neural Network (CNN) can detect burial mounds in high-resolution satellite imagery, comparing model predictions against 773 field-verified mounds in the Kazanlak Valley, Bulgaria. The study demonstrates that transfer learning approaches fail to achieve acceptable detection rates despite promising self-reported metrics, providing valuable cautionary evidence about ML limitations in archaeological prospection.

**Overall Credibility:** Good (75/100)

---

## Quality Gating Result

**Quality State:** HIGH

- Extraction Confidence: HIGH
- Classification Confidence: HIGH
- Assessment Pathway: Standard (full assessment)

---

## Research Classification

**Paper Type:** Empirical
**Primary Approach:** Deductive (high confidence)
**Mixed Methods:** No

Clear hypothesis-testing research with two-run experimental design validated against independent field data.

---

## Signal Scores

| Cluster | Signal | Score | Band |
|---------|--------|-------|------|
| Foundational Clarity | Comprehensibility | 77 | Good |
| Foundational Clarity | Transparency | 81 | Excellent |
| Evidential Strength | Plausibility | 74 | Good |
| Evidential Strength | Validity | 79 | Good |
| Evidential Strength | Robustness | 66 | Good |
| Evidential Strength | Generalisability | 75 | Good |
| Reproducibility | Reproducibility | 71 | Good |

**Aggregate Score:** 75/100 (Good)

---

## Cluster Summaries

### Cluster 1: Foundational Clarity (Strong)

Excellent transparency through three public repositories and rare time-on-task documentation. Good comprehensibility with explicit claims and clear logical structure.

### Cluster 2: Evidential Strength (Strong)

All signals in Good band. Validity strongest through external validation against 773 field-verified mounds. Robustness adequate through two-run comparison design.

### Cluster 3: Reproducibility (Adequate)

Strong code infrastructure enables analytical reproduction. Data access constrained by commercial imagery and reference-only field data.

---

## Key Strengths

1. **Exceptional code transparency** - Three public GitHub repositories with complete analytical pipeline
2. **Rigorous external validation** - 773 field-verified mounds as independent ground truth
3. **Honest failure reporting** - Detailed analysis of why model failed
4. **Resource transparency** - 135 person-hours investment documented (rare in literature)

## Key Limitations

1. **Data access constraints** - Commercial IKONOS imagery not shareable
2. **Single study region** - Results specific to Kazanlak Valley
3. **Limited parameter sensitivity** - Only >60% threshold tested
4. **No environment specification** - Missing requirements.txt or Docker

---

## Reproducibility Readiness

```yaml
reproducibility_readiness:
  inputs_available: "partial"
  code_available: "yes"
  environment_specified: "partial"
  execution_feasibility: "needs_work"
  publication_year: 2024
```

---

## Assessment Verdict

**Verdict:** Good

This paper demonstrates strong foundational clarity and evidential strength through rigorous external validation and exceptional transparency. The honest reporting of negative results and resource requirements significantly enhance scientific value. Main limitations relate to data access constraints inherent to commercial imagery.

---

## Structured Output

```json
{
  "paper_id": "sobotkova-et-al-2024",
  "assessment_date": "2025-11-30",
  "run": "03",
  "quality_state": "high",
  "research_approach": "deductive",
  "paper_type": "empirical",
  "signals": {
    "comprehensibility": {"score": 77, "band": "good"},
    "transparency": {"score": 81, "band": "excellent"},
    "plausibility": {"score": 74, "band": "good"},
    "validity": {"score": 79, "band": "good"},
    "robustness": {"score": 66, "band": "good"},
    "generalisability": {"score": 75, "band": "good"},
    "reproducibility": {"score": 71, "band": "good"}
  },
  "aggregate_score": 75,
  "aggregate_band": "good",
  "verdict": "good"
}
```
