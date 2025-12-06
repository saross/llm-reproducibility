# Credibility Assessment Report

**Paper:** sobotkova-et-al-2024
**Title:** Validating Predictions of Burial Mounds with Field Data
**Assessment Date:** 2025-12-01
**Run:** 02

---

## Executive Summary

This paper evaluates transfer learning CNN approaches for burial mound detection in satellite imagery, validating against 773 field-verified mounds. The study demonstrates that pre-trained models with minimal training curation fail to achieve acceptable detection despite good self-reported metrics, providing essential cautionary evidence about ML limitations.

**Overall Credibility:** Good (75/100)

---

## Quality Gating Result

**Quality State:** HIGH

- Extraction Confidence: HIGH
- Classification Confidence: HIGH
- Assessment Pathway: Standard

---

## Research Classification

**Paper Type:** Empirical
**Primary Approach:** Deductive (high confidence)
**Mixed Methods:** No

---

## Signal Scores

| Cluster | Signal | Score | Band |
|---------|--------|-------|------|
| Foundational Clarity | Comprehensibility | 78 | Good |
| Foundational Clarity | Transparency | 83 | Excellent |
| Evidential Strength | Plausibility | 74 | Good |
| Evidential Strength | Validity | 80 | Excellent |
| Evidential Strength | Robustness | 68 | Good |
| Evidential Strength | Generalisability | 75 | Good |
| Reproducibility | Reproducibility | 71 | Good |

**Aggregate Score:** 75/100 (Good)

---

## Cluster Summaries

### Cluster 1: Foundational Clarity (Strong)

Transparency reaches Excellent through complete code sharing and rare resource reporting. Comprehensibility Good with explicit quantified claims.

### Cluster 2: Evidential Strength (Strong)

Validity Excellent through independent ground truth validation. Other signals consistently Good.

### Cluster 3: Reproducibility (Adequate)

Good code infrastructure with data access constraints.

---

## Key Strengths

1. Rigorous external validation (773 field-verified mounds)
2. Three complete public repositories
3. Honest failure reporting
4. 135 person-hours documented

## Key Limitations

1. Commercial imagery not shareable
2. Single study area
3. Limited parameter exploration
4. No environment specification

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

Strong credibility through rigorous validation, exceptional transparency, and honest negative results reporting.

---

## Structured Output

```json
{
  "paper_id": "sobotkova-et-al-2024",
  "assessment_date": "2025-12-01",
  "run": "02",
  "quality_state": "high",
  "research_approach": "deductive",
  "paper_type": "empirical",
  "signals": {
    "comprehensibility": {"score": 78, "band": "good"},
    "transparency": {"score": 83, "band": "excellent"},
    "plausibility": {"score": 74, "band": "good"},
    "validity": {"score": 80, "band": "excellent"},
    "robustness": {"score": 68, "band": "good"},
    "generalisability": {"score": 75, "band": "good"},
    "reproducibility": {"score": 71, "band": "good"}
  },
  "aggregate_score": 75,
  "aggregate_band": "good",
  "verdict": "good"
}
```
