# Credibility Assessment Report

**Paper:** sobotkova-et-al-2024
**Title:** Validating Predictions of Burial Mounds with Field Data: The Promise and Reality of Machine Learning
**Assessment Date:** 2025-12-01
**Run:** 01

---

## Executive Summary

This paper tests transfer learning Convolutional Neural Network (CNN) approaches for detecting burial mounds in high-resolution satellite imagery, validating predictions against 773 field-verified mounds in Bulgaria's Kazanlak Valley. The study demonstrates that pre-trained models with minimal training curation fail to achieve acceptable detection rates despite good self-reported metrics (F1=0.87), providing crucial cautionary evidence about ML limitations in archaeological prospection.

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
| Foundational Clarity | Comprehensibility | 80 | Excellent |
| Foundational Clarity | Transparency | 82 | Excellent |
| Evidential Strength | Plausibility | 75 | Good |
| Evidential Strength | Validity | 82 | Excellent |
| Evidential Strength | Robustness | 70 | Good |
| Evidential Strength | Generalisability | 76 | Good |
| Reproducibility | Reproducibility | 72 | Good |

**Aggregate Score:** 77/100 (Good)

---

## Cluster Summaries

### Cluster 1: Foundational Clarity (Strong)

Both signals reach Excellent band. Exceptional transparency through three complete public repositories and rare time-on-task documentation (135 person-hours). Strong comprehensibility with explicit quantified claims throughout.

### Cluster 2: Evidential Strength (Strong)

Validity reaches Excellent through rigorous external validation against 773 field-verified mounds collected independently. Other signals consistently in Good band with strong support from well-designed comparative study.

### Cluster 3: Reproducibility (Adequate)

Strong code availability enables analytical reproduction. Data access constrained by commercial satellite imagery licensing. Partial environment specification.

---

## Key Strengths

1. **Rigorous external validation** - 773 independent field-verified mounds as ground truth
2. **Exceptional code transparency** - Three complete public GitHub repositories
3. **Honest failure reporting** - Detailed analysis of negative results with mechanisms
4. **Resource transparency** - 135 person-hours documented (rare in ML-for-archaeology)

## Key Limitations

1. **Data access** - Commercial IKONOS imagery cannot be shared
2. **Single study area** - Results specific to Kazanlak Valley heterogeneous landscape
3. **Limited parameter exploration** - Only >60% probability threshold explored
4. **No environment specification** - Missing formal dependency files (requirements.txt, Docker)

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

This paper demonstrates strong credibility through rigorous validation methodology, exceptional transparency, and honest reporting of negative results. The scientific value of documenting failure is substantial given publication bias in the ML-for-archaeology literature. Methodological limitations (single site, partial data availability) are appropriately acknowledged and do not undermine the core conclusions.

---

## Structured Output

```json
{
  "paper_id": "sobotkova-et-al-2024",
  "assessment_date": "2025-12-01",
  "run": "01",
  "quality_state": "high",
  "research_approach": "deductive",
  "paper_type": "empirical",
  "signals": {
    "comprehensibility": {"score": 80, "band": "excellent"},
    "transparency": {"score": 82, "band": "excellent"},
    "plausibility": {"score": 75, "band": "good"},
    "validity": {"score": 82, "band": "excellent"},
    "robustness": {"score": 70, "band": "good"},
    "generalisability": {"score": 76, "band": "good"},
    "reproducibility": {"score": 72, "band": "good"}
  },
  "aggregate_score": 77,
  "aggregate_band": "good",
  "verdict": "good"
}
```
