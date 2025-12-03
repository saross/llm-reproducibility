# Credibility Assessment Report

**Paper:** ballsun-stanton-et-al-2018
**Title:** FAIMS Mobile: Flexible, open-source software for field research
**Assessment Date:** 2025-12-02
**Run:** 01

---

## Executive Summary

This paper describes FAIMS Mobile, a native Android application for customisable field data collection across disciplines including archaeology, ecology, geoscience, and history. The software addresses a gap in purpose-built field research tools through deep customisation via XML-based definition packets. Impact is demonstrated through deployment statistics (40+ customisations, 29 field deployments, ~300 users, 20,000+ hours) and user-reported benefits.

**Overall Credibility:** Good (75/100)

---

## Quality Gating Result

**Quality State:** HIGH

- Extraction Confidence: HIGH
- Classification Confidence: HIGH
- Assessment Pathway: Standard (full assessment)

---

## Research Classification

**Paper Type:** Methodological (software_tool)
**Primary Approach:** Inductive (high confidence)
**Mixed Methods:** No
**Context Flags:** 📦 (infrastructure), 🔧 (tool)

Software publication describing artefact capabilities through case study demonstration and user feedback validation.

---

## Signal Scores

| Cluster | Signal | Score | Band |
|---------|--------|-------|------|
| Foundational Clarity | Comprehensibility | 82 | Excellent |
| Foundational Clarity | Transparency | 88 | Excellent |
| Evidential Strength | Plausibility | 78 | Good |
| Evidential Strength | Validity | 68 | Good |
| Evidential Strength | Robustness | 52 | Moderate (📦) |
| Evidential Strength | Generalisability | 72 | Good |
| Reproducibility | Reproducibility | 85 | Excellent |

**Aggregate Score:** 75/100 (Good)

---

## Cluster Summaries

### Cluster 1: Foundational Clarity (Strong)

Both signals reach Excellent band. Exceptional transparency through GPLv3 open-source licensing, multiple distribution channels (GitHub, Google Play, direct APK), and comprehensive documentation (Module Cookbook, API docs, User-to-Developer guide). Strong comprehensibility with explicit design rationale ("two fundamental requirements") and bounded technical specifications.

### Cluster 2: Evidential Strength (Adequate)

Plausibility and Generalisability in Good band with appropriate domain grounding and scope boundaries. Validity adequate but limited by reliance on self-reported user feedback. Robustness score (52) reflects 📦 software paper genre expectations—software papers describe artefacts, not test alternatives. This is appropriate, not a deficiency.

### Cluster 3: Reproducibility (Strong)

Excellent code availability with GPLv3 licence, 4 distribution channels, and comprehensive dependency documentation (18 technologies). External project customisations provide empirical validation of reproducibility infrastructure. Minor limitations: no software DOI, no containerised environment.

---

## Key Strengths

1. **Exceptional open-source availability** - GPLv3 licence with multiple distribution channels
2. **Comprehensive documentation** - Module Cookbook, Beanshell API, User-to-Developer guide
3. **Explicit design rationale** - Two fundamental requirements clearly articulated
4. **Honest limitation acknowledgement** - Customisation complexity and time reallocation challenges documented
5. **Cross-disciplinary validation** - Deployments across archaeology, ecology, geoscience, history

## Key Limitations

1. **Self-reported validation** - Impact claims based on user feedback without independent verification
2. **Team-authored case studies** - No independent third-party evaluation
3. **Geographic scope** - Primarily Australian deployments; international applicability not validated
4. **No systematic comparison** - Alternative tools described but not benchmarked

---

## Reproducibility Readiness

```yaml
reproducibility_readiness:
  inputs_available: "yes"
  code_available: "yes"
  environment_specified: "partial"
  execution_feasibility: "ready"
  publication_year: 2018
```

---

## Assessment Verdict

**Verdict:** Good

This paper demonstrates good credibility for a methodological software publication. The exceptional transparency (GPLv3, comprehensive documentation, explicit design rationale) and strong reproducibility infrastructure provide a solid foundation. Technical capability claims are fully supported by architectural documentation. Impact claims are appropriately scoped to available evidence but would benefit from independent validation. The moderate Robustness score reflects appropriate genre expectations for software papers. Overall, this is a well-documented software publication that meets community standards for infrastructure papers.

---

## Structured Output

```json
{
  "paper_id": "ballsun-stanton-et-al-2018",
  "assessment_date": "2025-12-02",
  "run": "01",
  "quality_state": "high",
  "research_approach": "inductive",
  "paper_type": "methodological",
  "paper_subtype": "software_tool",
  "context_flags": ["📦", "🔧"],
  "signals": {
    "comprehensibility": {"score": 82, "band": "excellent"},
    "transparency": {"score": 88, "band": "excellent"},
    "plausibility": {"score": 78, "band": "good"},
    "validity": {"score": 68, "band": "good"},
    "robustness": {"score": 52, "band": "moderate", "genre_appropriate": true},
    "generalisability": {"score": 72, "band": "good"},
    "reproducibility": {"score": 85, "band": "excellent"}
  },
  "aggregate_score": 75,
  "aggregate_band": "good",
  "verdict": "good"
}
```
