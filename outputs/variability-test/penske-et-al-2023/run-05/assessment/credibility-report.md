# Credibility Assessment Report

**Paper:** penske-et-al-2023
**Title:** Early contact between late farming and pastoralist societies in southeastern Europe
**DOI:** 10.1038/s41586-023-06334-8
**Publication Year:** 2023

**Assessment Date:** 2025-12-02
**Assessor Version:** v1.0
**Schema Version:** 1.0

---

## Executive Summary

**Verdict:** GOOD | **Confidence:** HIGH

This empirical paper using inductive reasoning demonstrates strong foundational clarity and evidential strength. Published in 2023, it meets current era expectations for open science practices with excellent data archiving.

**Key Strengths:**

- Excellent data availability: DNA sequences deposited in ENA (PRJEB62503) with public access
- Comprehensive methods documentation with protocols.io references and detailed parameters
- Multi-proxy genetic analysis provides robust triangulation (autosomal, Y-chromosome, IBD, ROH)
- Pattern claims appropriately bounded to southeastern Europe, 5400-2400 BC

**Key Concerns:**

- No dedicated code repository; workflow reconstruction required from method descriptions

**Bottom Line:** High-quality inductive archaeogenomics study with strong transparency and credibility, meeting field standards for Nature publications. Reproducibility is good but would benefit from shared analysis scripts.

---

## Signal Scores Dashboard

| Signal | Score | Band | Notes |
|--------|-------|------|-------|
| Comprehensibility | 82 | Excellent | Clear research goals, bounded pattern claims |
| Transparency | 85 | Excellent | Comprehensive methods, data archived |
| Plausibility | 82 | Excellent | Consistent with established frameworks |
| Validity | 78 | Good | Sufficient evidence, systematic sampling |
| Robustness | 75 | Good | Multi-proxy triangulation |
| Generalisability | 72 | Good | Appropriately scoped claims |
| Reproducibility | 68 | Good | Data available; code reconstruction needed |

**Aggregate Score:** 77 (GOOD) — *EXPERIMENTAL*

*Note: Aggregate score is calculated as mean of all seven signals. We are still investigating what this aggregate means and how it should be interpreted.*

---

## Cluster Ratings

| Cluster | Rating | Pillar |
|---------|--------|--------|
| Cluster 1: Foundational Clarity | Strong | Transparency |
| Cluster 2: Evidential Strength | Strong | Credibility |
| Cluster 3: Reproducibility | Adequate | Reproducibility |

---

## Detailed Findings

### Cluster 1: Foundational Clarity — Strong

The paper demonstrates excellent comprehensibility and transparency for inductive archaeogenomic research. Research questions are explicit: characterising genetic variation in Chalcolithic southeastern Europe and understanding early farming-pastoralist contact. Pattern descriptions are clear and well-bounded. Methods are comprehensively documented with protocols.io references, software versions, and analytical parameters. Data is archived in ENA with public access.

**Key Strengths:**

- Explicit research goals and exploratory framing
- Clear, bounded pattern claims throughout
- Comprehensive methods with detailed parameter documentation
- Primary data archived in standardised repository (ENA)

**Key Weaknesses:**

- Some implicit interpretive steps in population history reconstruction

---

### Cluster 2: Evidential Strength — Strong

All four credibility signals perform well. Findings are highly plausible given established frameworks for European prehistory—genetic ancestry patterns align with archaeological evidence and previous archaeogenomic studies. Evidence is sufficient for the pattern claims made, with 135 individuals from 8 sites providing adequate coverage. Robustness is supported by multi-proxy triangulation across autosomal, Y-chromosome, kinship, and inbreeding analyses. Claims are appropriately scoped to the studied region and period.

**Key Strengths:**

- Patterns consistent with established Neolithic expansion and steppe-farmer interaction frameworks
- Multi-proxy genetic analysis provides convergent evidence
- Both distal and proximal qpAdm modelling frameworks tested
- Claims explicitly bounded to southeastern Europe, 5400-2400 BC

**Key Weaknesses:**

- Limited sample sizes at some individual sites
- No systematic sensitivity analysis of outgroup set choices
- Transfer conditions to adjacent regions not fully specified

---

### Cluster 3: Reproducibility — Adequate

**Pathway:** Standard (computational components present)

The paper has strong data archiving but lacks a dedicated code repository. DNA sequences are deposited in ENA (PRJEB62503) with public access, enabling complete re-analysis from primary data. However, custom analysis scripts are not shared—the paper relies on established software packages with documented parameters. A researcher with archaeogenomics expertise could reconstruct the analysis pipeline from method descriptions, but this requires significant implementation effort.

**Key Strengths:**

- Primary data fully archived in ENA with machine-actionable access
- Established open-source software packages used throughout
- Detailed parameter documentation enables procedural reconstruction

**Key Weaknesses:**

- No dedicated code repository for custom analysis scripts
- No containerised computational environment
- Workflow requires reconstruction from method descriptions

---

## Infrastructure & FAIR Summary

| Aspect | Status |
|--------|--------|
| **FAIR Score** | 14/16 (87.5%) |
| **Code Availability** | Not available (relies on established packages) |
| **Data Availability** | Available (ENA PRJEB62503, public access) |
| **Preregistration** | Not preregistered (not expected for inductive research) |
| **PID Coverage** | Paper DOI present; protocols.io DOIs for lab protocols |

**Infrastructure Gaps:**

- No code repository for custom analysis scripts
- No author ORCIDs documented in extraction
- No containerised environment specification

---

## Contextual Interpretation

### Reproducibility (68, Good)

**Why this score:** This score reflects typical practice for Nature archaeogenomics publications in 2023. Data sharing in domain repositories is standard; code sharing is emerging but not yet expected.

**What this means:** The paper's analytical outputs can be reproduced by an experienced researcher who reconstructs the workflow from documented methods and parameters. This is workable but requires more effort than executing shared scripts.

**What readers should consider:** If attempting reproduction, plan for pipeline reconstruction. All core tools are open-source (EAGER, ADMIXTOOLS, ANGSD, ancIBD, hapROH). Parameter documentation is sufficient for experienced practitioners.

---

## Era Context

**Publication Year:** 2023
**Era:** Current (2020-present)
**Era Label:** Current era — FAIR and open science expectations established

**Expectations Note:** Papers from 2023 are expected to share data in domain repositories (met) and increasingly to share code (partially met). The paper meets field standards for Nature archaeogenomics publications.

---

## Structured Output

```json
{
  "credibility_report": {
    "version": "1.0",
    "paper": {
      "slug": "penske-et-al-2023",
      "title": "Early contact between late farming and pastoralist societies in southeastern Europe",
      "doi": "10.1038/s41586-023-06334-8",
      "publication_year": 2023
    },
    "classification": {
      "paper_type": "empirical",
      "paper_subtype": "archaeogenomics",
      "approach": "inductive",
      "framework": "inductive_emphasis",
      "quality_state": "high",
      "classification_confidence": "high"
    },
    "verdict": {
      "band": "good",
      "confidence": "high",
      "aggregate_score": 77,
      "aggregate_experimental": true
    },
    "signals": {
      "comprehensibility": { "score": 82, "band": "excellent" },
      "transparency": { "score": 85, "band": "excellent" },
      "plausibility": { "score": 82, "band": "excellent" },
      "validity": { "score": 78, "band": "good" },
      "robustness": { "score": 75, "band": "good" },
      "generalisability": { "score": 72, "band": "good" },
      "reproducibility": { "score": 68, "band": "good", "variant": "standard" }
    },
    "aggregates": {
      "cluster_1_rating": "strong",
      "cluster_2_rating": "strong",
      "cluster_3_rating": "adequate"
    },
    "infrastructure": {
      "fair_score": 14,
      "fair_rating": "high",
      "fair_maximum": 16,
      "code_availability": "not_available",
      "data_availability": "available",
      "preregistration": "not_applicable"
    },
    "era_context": {
      "publication_year": 2023,
      "era": "current",
      "era_label": "Current era — FAIR and open science expectations established",
      "expectations_note": "Data sharing in domain repositories expected and met. Code sharing increasingly expected but not yet standard for field."
    },
    "assessment_metadata": {
      "assessment_date": "2025-12-02",
      "assessor_version": "v1.0",
      "schema_version": "1.0"
    }
  }
}
```

---

## Assessment Limitations

None. Quality state is HIGH with high extraction and classification confidence.

---

*Report generated by research-assessor skill v1.0*
