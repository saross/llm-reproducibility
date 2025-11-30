# Credibility Assessment Report

**Paper:** sobotkova-et-al-2024
**Title:** Detecting Burial Mounds Using Transfer Learning
**Assessment Date:** 2025-11-30
**Run:** 02

---

## Executive Summary

This paper tests whether a pre-trained CNN can detect burial mounds in satellite imagery, comparing model predictions against field-verified ground truth. The study finds that transfer learning approaches fail to achieve acceptable detection rates despite good self-reported metrics, providing valuable evidence about ML limitations in archaeological prospection.

**Overall Credibility:** Good (74/100)

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

The paper follows clear deductive hypothesis-testing research, testing whether transfer learning approaches work for archaeological feature detection against field-verified ground truth.

---

## Signal Scores

| Cluster | Signal | Score | Band |
|---------|--------|-------|------|
| Foundational Clarity | Comprehensibility | 76 | Good |
| Foundational Clarity | Transparency | 80 | Excellent |
| Evidential Strength | Plausibility | 73 | Good |
| Evidential Strength | Validity | 78 | Good |
| Evidential Strength | Robustness | 65 | Good |
| Evidential Strength | Generalisability | 76 | Good |
| Reproducibility | Reproducibility | 70 | Good |

**Aggregate Score:** 74/100 (Good)

---

## Cluster Summaries

### Cluster 1: Foundational Clarity (Strong)

The paper demonstrates good comprehensibility with explicit, quantified claims and clear logical structure. Transparency is excellent with three public GitHub repositories and comprehensive methods documentation.

### Cluster 2: Evidential Strength (Strong)

All four signals in the Good band. Validity is strongest through external validation against 773 field-verified mounds. Robustness adequate through two-run design but limited sensitivity analyses.

### Cluster 3: Reproducibility (Adequate)

Code infrastructure strong with three public repositories. Main limitation is data access: commercial satellite imagery and reference-only field data create barriers.

---

## Key Strengths

1. **Exceptional code transparency** - Three public GitHub repositories with complete analytical pipeline
2. **Strong external validation** - 773 field-verified mounds as ground truth
3. **Honest negative results** - Thorough acknowledgement of model failure
4. **Clear methodology** - Well-documented two-run design testing alternative hypotheses

## Key Limitations

1. **Data access barriers** - Commercial IKONOS imagery cannot be shared
2. **Single study area** - Results limited to Kazanlak Valley context
3. **Limited sensitivity testing** - Threshold and tile size variations not fully explored
4. **No environment specification** - Missing requirements.txt or Docker configuration

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

This paper demonstrates strong foundational clarity and evidential strength. The exceptional code transparency and honest reporting of negative results enhance credibility. Main limitations relate to data access constraints inherent to commercial satellite imagery.

---

## Structured Output

```json
{
  "paper_id": "sobotkova-et-al-2024",
  "assessment_date": "2025-11-30",
  "run": "02",
  "quality_state": "high",
  "research_approach": "deductive",
  "paper_type": "empirical",
  "signals": {
    "comprehensibility": {"score": 76, "band": "good"},
    "transparency": {"score": 80, "band": "excellent"},
    "plausibility": {"score": 73, "band": "good"},
    "validity": {"score": 78, "band": "good"},
    "robustness": {"score": 65, "band": "good"},
    "generalisability": {"score": 76, "band": "good"},
    "reproducibility": {"score": 70, "band": "good"}
  },
  "aggregate_score": 74,
  "aggregate_band": "good",
  "verdict": "good"
}
```
