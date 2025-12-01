# Credibility Assessment Report

**Paper:** sobotkova-et-al-2024
**Title:** Validating Predictions of Burial Mounds with Field Data
**Assessment Date:** 2025-11-30
**Run:** 04

---

## Executive Summary

This paper tests transfer learning CNN approaches for detecting burial mounds in high-resolution satellite imagery, validating model predictions against 773 field-verified mounds in Bulgaria's Kazanlak Valley. The study finds that pre-trained models with low-touch training fail to achieve acceptable detection rates despite promising self-reported metrics, offering important cautionary evidence about ML limitations in archaeological prospection.

**Overall Credibility:** Good (76/100)

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

Clear hypothesis-testing research with external validation against independent ground truth.

---

## Signal Scores

| Cluster | Signal | Score | Band |
|---------|--------|-------|------|
| Foundational Clarity | Comprehensibility | 78 | Good |
| Foundational Clarity | Transparency | 82 | Excellent |
| Evidential Strength | Plausibility | 75 | Good |
| Evidential Strength | Validity | 80 | Excellent |
| Evidential Strength | Robustness | 67 | Good |
| Evidential Strength | Generalisability | 77 | Good |
| Reproducibility | Reproducibility | 72 | Good |

**Aggregate Score:** 76/100 (Good)

---

## Cluster Summaries

### Cluster 1: Foundational Clarity (Strong)

Excellent transparency with three public repositories and rare time documentation. Good comprehensibility through explicit quantified claims.

### Cluster 2: Evidential Strength (Strong)

Validity reaches Excellent through rigorous external validation. Other signals in Good band with consistent evidential support.

### Cluster 3: Reproducibility (Adequate)

Strong code availability enables analytical reproduction. Data access constrained by commercial imagery.

---

## Key Strengths

1. **Rigorous external validation** - 773 field-verified mounds as independent ground truth
2. **Exceptional code transparency** - Three public GitHub repositories
3. **Honest negative results** - Detailed failure analysis
4. **Resource documentation** - 135 person-hours (rare in literature)

## Key Limitations

1. **Data access** - Commercial imagery not shareable
2. **Single study region** - Kazanlak Valley only
3. **Limited parameter testing** - Only >60% threshold used
4. **No environment specification** - Missing formal dependency documentation

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

This paper demonstrates strong credibility through rigorous validation and exceptional transparency. The honest reporting of negative results and resource requirements enhances scientific value significantly.

---

## Structured Output

```json
{
  "paper_id": "sobotkova-et-al-2024",
  "assessment_date": "2025-11-30",
  "run": "04",
  "quality_state": "high",
  "research_approach": "deductive",
  "paper_type": "empirical",
  "signals": {
    "comprehensibility": {"score": 78, "band": "good"},
    "transparency": {"score": 82, "band": "excellent"},
    "plausibility": {"score": 75, "band": "good"},
    "validity": {"score": 80, "band": "excellent"},
    "robustness": {"score": 67, "band": "good"},
    "generalisability": {"score": 77, "band": "good"},
    "reproducibility": {"score": 72, "band": "good"}
  },
  "aggregate_score": 76,
  "aggregate_band": "good",
  "verdict": "good"
}
```
