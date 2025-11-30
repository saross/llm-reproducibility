# Credibility Assessment Report

**Paper:** FAIMS Mobile: Flexible, open-source software for field research  
**Authors:** Ballsun-Stanton, Ross, Sobotkova, Crook  
**DOI:** [10.1016/j.softx.2017.12.006](https://doi.org/10.1016/j.softx.2017.12.006)  
**Publication Year:** 2018 (SoftwareX)

**Assessment Date:** 2025-11-30  
**Assessor Version:** v1.0  
**Schema Version:** 1.0

---

## Executive Summary

> **Verdict:** Good | **Confidence:** HIGH
>
> This **methodological** software paper demonstrates excellent software transparency with full open source availability. Published in SoftwareX (2018, early adopter era), it exemplifies best practice for research software papers: GPLv3 code on GitHub, archival snapshot, and Google Play distribution.
>
> **Key Strengths:**
> - Full source code available (GitHub, GPLv3, archival snapshot)
> - Compiled application on Google Play for easy installation
> - Five years of iterative co-development with field researchers
>
> **Key Concerns:**
> - Limited comparison to alternative software approaches (typical for software papers)
>
> **Bottom Line:** An exemplary research software paper with excellent transparency and reproducibility, describing FAIMS as a solution for field data collection challenges.

---

## Verdict & Classification

| Aspect | Value |
|--------|-------|
| **Verdict Band** | Good |
| **Aggregate Score** | 72/100 (EXPERIMENTAL) |
| **Confidence Level** | HIGH |
| **Quality State** | HIGH |
| **Paper Type** | Methodological (software paper) |
| **Research Approach** | Methodological |
| **Framework Applied** | Methodological emphasis (Transparency, Reproducibility prioritised) |

---

## Signal Scores Dashboard

| # | Signal | Score | Band | Context |
|---|--------|-------|------|---------|
| 1 | Comprehensibility | 78 | Good | — |
| 2 | Transparency | 85 | Excellent | — |
| 3 | Plausibility | 74 | Good | — |
| 4 | Validity | 62 | Good | — |
| 5 | Robustness | 55 | Moderate | 📦 Software paper |
| 6 | Generalisability | 70 | Good | — |
| 7 | Reproducibility | 82 | Excellent | 🔧 Software paper |

**Aggregate:** 72/100 ⚠️ *EXPERIMENTAL — we are investigating what aggregate scores mean*

---

## Cluster Summaries

### Cluster 1: Foundational Clarity (Transparency Pillar)

**Rating:** Strong

The paper demonstrates strong foundational clarity with excellent software transparency and good architectural documentation. Source code is available on GitHub under GPLv3 with archival snapshot at ElsevierSoftwareX.

| Signal | Score | Band |
|--------|-------|------|
| Comprehensibility | 78 | Good |
| Transparency | 85 | Excellent |

**Key Strengths:**
- Full source code on GitHub (GPLv3)
- Archival snapshot provides permanent link
- Design rationale explicitly stated

**Key Weaknesses:**
- Some implementation details implicit
- Development methodology details in external docs

---

### Cluster 2: Evidential Strength (Credibility Pillar)

**Rating:** Adequate

The paper demonstrates adequate evidential strength, appropriate for a software description paper. Robustness is moderate (📦) reflecting genre expectations — software papers describe what exists rather than systematically comparing alternatives.

| Signal | Score | Band |
|--------|-------|------|
| Plausibility | 74 | Good |
| Validity | 62 | Good |
| Robustness | 55 | Moderate 📦 |
| Generalisability | 70 | Good |

**Key Strengths:**
- Design decisions consistent with software engineering practice
- Case studies cited (Sobotkova et al. 2016)
- Limitations honestly acknowledged
- Cross-disciplinary design documented

**Key Weaknesses:**
- Limited comparison to alternative software
- Case study details in cited paper, not here

---

### Cluster 3: Reproducibility (Reproducibility Pillar)

**Rating:** Strong

The software described is fully available for installation, use, and extension. This represents best practice for research software papers.

| Signal | Score | Band | Pathway |
|--------|-------|------|---------|
| Reproducibility | 82 | Excellent | Standard 🔧 |

**Key Strengths:**
- Compiled app on Google Play
- Source code under GPLv3
- User-to-Developer documentation
- Customisation module library

**Key Weaknesses:**
- Build environment details in external docs

**Execution Feasibility:** Ready — no barriers to use

---

## Era Context

**Publication Year:** 2018  
**Era:** Early adopter (2015-2020)  
**Era Label:** Early adopter era — reproducibility discussions emerging, data/code sharing becoming expected

**Interpretation:** Published in 2018, this paper exceeds era expectations. Full open source code with archival snapshot and Google Play distribution represents best practice even by 2024 standards. The SoftwareX venue specifically promotes software transparency, and this paper exemplifies journal standards.

---

## Context Flag Interpretation

### Robustness (55, Moderate) 📦

**Why this score:** Software and data papers describe artefacts rather than testing hypotheses. They do not typically include systematic comparisons to alternatives, sensitivity analyses, or robustness checks in the way empirical studies do. A Moderate Robustness score reflects these different genre expectations — it is not a criticism of the paper.

**What this means:** The paper describes FAIMS architecture, features, and use cases. It does not claim to have tested FAIMS against alternative approaches or demonstrated superiority through controlled comparison. This is appropriate: software papers in venues like SoftwareX are meant to document software, not conduct comparative evaluations.

**What readers should consider:** When deciding whether to adopt FAIMS (or any research software), readers should independently evaluate alternatives appropriate to their context. The paper provides the information needed to understand FAIMS; comparative assessment is the reader's responsibility.

**Generalisation:** Similar Robustness patterns should be expected for other software papers, data papers, and infrastructure descriptions. These genres prioritise Transparency and Reproducibility (can you access and use the artefact?) over Robustness (was it tested against alternatives?).

---

## Infrastructure & FAIR Summary

| Aspect | Status | Details |
|--------|--------|---------|
| **FAIR Score** | N/A | Software paper |
| **FAIR Rating** | N/A | Not applicable |
| **Code Availability** | Available | GitHub (active + archival), GPLv3 |
| **Data Availability** | N/A | Software paper |
| **Preregistration** | N/A | Software development |
| **PID Coverage** | Good | DOI, archival snapshot link |

**Infrastructure Strengths:**
- Full open source availability (GPLv3)
- Archival snapshot at ElsevierSoftwareX
- Google Play distribution
- User-to-Developer documentation

---

## Structured Output

```json
{
  "credibility_report": {
    "version": "1.0",
    "paper": {
      "slug": "ballsun-stanton-et-al-2018",
      "title": "FAIMS Mobile: Flexible, open-source software for field research",
      "doi": "10.1016/j.softx.2017.12.006",
      "publication_year": 2018
    },
    "classification": {
      "paper_type": "methodological",
      "paper_subtype": "software_paper",
      "approach": "methodological",
      "framework": "methodological_emphasis",
      "quality_state": "high",
      "classification_confidence": "high"
    },
    "verdict": {
      "band": "Good",
      "confidence": "HIGH",
      "aggregate_score": 72,
      "aggregate_experimental": true
    },
    "signals": {
      "comprehensibility": { "score": 78, "band": "Good" },
      "transparency": { "score": 85, "band": "Excellent" },
      "plausibility": { "score": 74, "band": "Good" },
      "validity": { "score": 62, "band": "Good" },
      "robustness": { "score": 55, "band": "Moderate", "context_flag": "software_paper" },
      "generalisability": { "score": 70, "band": "Good" },
      "reproducibility": { "score": 82, "band": "Excellent", "variant": "software_paper" }
    },
    "aggregates": {
      "cluster_1_rating": "Strong",
      "cluster_2_rating": "Adequate",
      "cluster_3_rating": "Strong"
    },
    "infrastructure": {
      "fair_score": null,
      "fair_rating": "not_applicable",
      "fair_maximum": null,
      "code_availability": "available",
      "data_availability": "not_applicable",
      "preregistration": "not_applicable"
    },
    "era_context": {
      "publication_year": 2018,
      "era": "early_adopter",
      "era_label": "Early adopter era — reproducibility discussions emerging",
      "expectations_note": "2018 paper exceeds era expectations with full open source and archival snapshot"
    },
    "assessment_metadata": {
      "assessment_date": "2025-11-30",
      "assessor_version": "v1.0",
      "schema_version": "1.0"
    }
  }
}
```

---

*Generated by Research Assessor v1.0 | Assessment Framework: Three Pillars (Transparency, Credibility, Reproducibility)*
