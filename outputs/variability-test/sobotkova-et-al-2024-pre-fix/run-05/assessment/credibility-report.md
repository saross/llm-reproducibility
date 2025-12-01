# Credibility Assessment Report

**Paper:** sobotkova-et-al-2024
**Title:** Validating Predictions of Burial Mounds with Field Data
**Assessment Date:** 2025-11-30
**Run:** 05

---

## Executive Summary

This paper tests transfer learning Convolutional Neural Network (CNN) approaches for detecting burial mounds in high-resolution satellite imagery, validating predictions against 773 field-verified mounds in Bulgaria's Kazanlak Valley. The study demonstrates that pre-trained models with minimal training curation fail to achieve acceptable detection rates despite good self-reported metrics, providing crucial cautionary evidence about ML limitations in archaeological prospection.

**Overall Credibility:** Good (77/100)

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

Clear hypothesis-testing research with rigorous external validation against independent ground truth.

---

## Signal Scores

| Cluster | Signal | Score | Band |
|---------|--------|-------|------|
| Foundational Clarity | Comprehensibility | 79 | Good |
| Foundational Clarity | Transparency | 83 | Excellent |
| Evidential Strength | Plausibility | 76 | Good |
| Evidential Strength | Validity | 81 | Excellent |
| Evidential Strength | Robustness | 68 | Good |
| Evidential Strength | Generalisability | 78 | Good |
| Reproducibility | Reproducibility | 73 | Good |

**Aggregate Score:** 77/100 (Good)

---

## Cluster Summaries

### Cluster 1: Foundational Clarity (Strong)

Excellent transparency through three complete public repositories and rare time-on-task documentation (135 hours). Good comprehensibility with explicit quantified claims.

### Cluster 2: Evidential Strength (Strong)

Validity reaches Excellent through rigorous external validation against 773 field-verified mounds. Other signals in Good band with consistent support.

### Cluster 3: Reproducibility (Adequate)

Strong code availability enables analytical reproduction. Data access constrained by commercial imagery licensing.

---

## Key Strengths

1. **Rigorous external validation** - 773 independent field-verified mounds
2. **Exceptional code transparency** - Three complete public GitHub repositories
3. **Honest failure reporting** - Detailed analysis of negative results
4. **Resource transparency** - 135 person-hours documented (rare)

## Key Limitations

1. **Data access** - Commercial IKONOS imagery cannot be shared
2. **Single study area** - Results specific to Kazanlak Valley
3. **Limited sensitivity testing** - Only >60% probability threshold explored
4. **No environment specification** - Missing formal dependency files

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

This paper demonstrates strong credibility through rigorous validation, exceptional transparency, and honest reporting of negative results. The scientific value of documenting failure is substantial given publication bias in the field.

---

## Structured Output

```json
{
  "paper_id": "sobotkova-et-al-2024",
  "assessment_date": "2025-11-30",
  "run": "05",
  "quality_state": "high",
  "research_approach": "deductive",
  "paper_type": "empirical",
  "signals": {
    "comprehensibility": {"score": 79, "band": "good"},
    "transparency": {"score": 83, "band": "excellent"},
    "plausibility": {"score": 76, "band": "good"},
    "validity": {"score": 81, "band": "excellent"},
    "robustness": {"score": 68, "band": "good"},
    "generalisability": {"score": 78, "band": "good"},
    "reproducibility": {"score": 73, "band": "good"}
  },
  "aggregate_score": 77,
  "aggregate_band": "good",
  "verdict": "good"
}
```
