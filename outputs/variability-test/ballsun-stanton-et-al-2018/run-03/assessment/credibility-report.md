# Credibility Assessment Report

**Paper:** FAIMS Mobile: Flexible, open-source software for field research
**DOI:** 10.1016/j.softx.2017.12.006
**Publication Year:** 2018 (Early Adopter Era)
**Assessment Date:** 2025-12-02
**Assessor Version:** v1.0

---

## Executive Summary

**Verdict:** Good | **Confidence:** HIGH

This **methodological (software tool)** paper using **inductive** reasoning demonstrates strong foundational clarity and excellent reproducibility infrastructure. Published in the early adopter era (2018), FAIMS Mobile represents exemplary practice for software publications.

**Key Strengths:**

- Complete open source code availability under GPLv3 with permanent GitHub repository
- Comprehensive technical documentation including architecture, dependencies, and multiple user guides
- Honest acknowledgment of limitations and technical debt

**Key Concerns:**

- One proprietary dependency (Nutiteq mapping library) limits fully open reproducibility
- Robustness assessment limited by software paper genre (comparative evaluation not expected)

**Bottom Line:** A well-documented open source software publication demonstrating excellent transparency and reproducibility practices for its era.

---

## Signal Scores Dashboard

| Signal | Score | Band | Context |
|--------|-------|------|---------|
| Comprehensibility | 85 | Excellent | — |
| Transparency | 90 | Excellent | — |
| Plausibility | 80 | Excellent | — |
| Validity | 75 | Good | — |
| Robustness | 55 | Moderate | 📦 Software paper |
| Generalisability | 70 | Good | — |
| Reproducibility | 85 | Excellent | 🔧 Software reproducibility |

**Aggregate Score:** 77/100 (Good) *EXPERIMENTAL*

---

## Cluster Ratings

| Cluster | Rating | Pillar |
|---------|--------|--------|
| Foundational Clarity | Strong | Transparency |
| Evidential Strength | Adequate-to-Strong | Credibility |
| Reproducibility | Strong | Reproducibility |

---

## Detailed Findings

### Cluster 1: Foundational Clarity — Strong

The paper demonstrates excellent comprehensibility with clear, bounded technical claims and explicit design rationale. Every major architectural decision is explained and justified. Technical specifications are precise with documented mechanisms (definition packets, DSL, Beanshell scripts).

Transparency is outstanding for a software publication. The Code metadata table provides comprehensive technical specification. Software architecture is documented with clear design decisions. Open source licensing (GPLv3) and permanent GitHub repository provide complete code access.

**Key Strengths:**

- Technical specifications clear and bounded with explicit mechanisms
- Design rationale explicit for all architectural decisions
- Multiple documentation resources for different user types

**Key Weaknesses:**

- Some evidence relies on external publication (Sobotkova et al., 2016)

---

### Cluster 2: Evidential Strength — Adequate-to-Strong

Plausibility and Validity are high, reflecting well-grounded claims with sufficient evidence. The paper's claims about software capabilities are plausible given established knowledge about mobile technology and field research. Evidence is sufficient: 40 customisations, 29 deployments, 300 users provide concrete metrics.

Robustness is moderate, appropriate for software paper genre. The paper describes what FAIMS does, not systematic comparisons with alternatives. This is genre-appropriate, not a deficiency.

Generalisability is good with claims appropriately bounded to demonstrated deployment contexts.

**Key Strengths:**

- Comprehensive deployment metrics support capability claims
- Honest acknowledgment of technical debt and limitations
- Cross-disciplinary adoption demonstrates pattern consistency

**Key Weaknesses:**

- No formal comparative evaluation against alternatives (genre-appropriate)
- User satisfaction based on qualitative feedback, not systematic measurement

---

### Cluster 3: Reproducibility — Strong

**Pathway:** Standard (software with computational components)

FAIMS demonstrates excellent software reproducibility. Complete source code is available under GPLv3 via permanent GitHub repository. All dependencies are documented in Code metadata table. Multiple documentation resources support installation and customisation.

**Execution Feasibility:** Ready for reproduction attempt with documented resources.

**Key Strengths:**

- Complete source code under permissive open source license
- Comprehensive dependency documentation
- Open scriptable tool chain (Java, Beanshell, XML)

**Key Weaknesses:**

- One proprietary dependency (Nutiteq)
- Some dependency versions not fully specified

---

## Contextual Interpretation

### Robustness (55, Moderate) 📦

**Why this score:** Software papers describe artefacts rather than testing hypotheses. They do not typically include systematic comparisons, sensitivity analyses, or robustness checks. A Moderate Robustness score reflects genre expectations — it is not a criticism.

**What this means:** FAIMS Mobile paper describes what the software does and demonstrates through deployment evidence. It does not compare FAIMS against ARK, Heurist, Kora, or ODK in systematic benchmark testing. This comparative assessment is the reader's responsibility.

**What readers should consider:** Evaluate alternative field data collection tools independently based on your specific requirements (offline capability, customisation needs, platform constraints, support availability).

---

### Reproducibility (85, Excellent) 🔧

**Why this score:** For software papers, "reproducibility" means: can users install, customise, and deploy the software? FAIMS provides comprehensive support: open source code, documented dependencies, multiple user guides, and community resources.

**What this means:** Users can reproduce the software environment described in the paper. The GitHub repository provides complete source code. Documentation supports the full user journey from installation through customisation.

**What readers should consider:** Some system administration expertise required for server setup. One proprietary dependency (Nutiteq) may require licensing consideration.

---

## Infrastructure & FAIR Summary

| Dimension | Status | Details |
|-----------|--------|---------|
| Code availability | Available | GPLv3, GitHub repository (permanent link) |
| Data availability | Not applicable | Software paper, no research data |
| Preregistration | Not applicable | Software development, not empirical research |
| FAIR score | Not calculated | Software publication (FAIR designed for research data) |

**PID Coverage:**

- Paper DOI: 10.1016/j.softx.2017.12.006
- Software repository: https://github.com/ElsevierSoftwareX/SOFTX-D-17-00021
- No ORCID identifiers in source document

**Infrastructure Gaps:**

- No formal data DOI (not applicable for software paper)
- No ORCID author identifiers

---

## Era Context

**Publication Year:** 2018
**Era:** Early Adopter
**Era Label:** Early adopter era — reproducibility discussions emerging, data/code sharing becoming expected

**Expectations Note:** In 2018, software reproducibility practices were emerging but not yet standard. FAIMS demonstrates exemplary practice for its era: open source licensing, GitHub repository, comprehensive dependency documentation, and multiple documentation resources. This paper would score well even against mainstream (post-2025) expectations.

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
      "paper_subtype": "software_tool",
      "approach": "inductive",
      "framework": "methodological_paper",
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
      "comprehensibility": { "score": 85, "band": "excellent" },
      "transparency": { "score": 90, "band": "excellent" },
      "plausibility": { "score": 80, "band": "excellent" },
      "validity": { "score": 75, "band": "good" },
      "robustness": { "score": 55, "band": "moderate", "context_flag": "software_paper" },
      "generalisability": { "score": 70, "band": "good" },
      "reproducibility": { "score": 85, "band": "excellent", "variant": "standard" }
    },
    "aggregates": {
      "cluster_1_rating": "strong",
      "cluster_2_rating": "adequate_to_strong",
      "cluster_3_rating": "strong"
    },
    "infrastructure": {
      "fair_score": null,
      "fair_rating": "not_applicable",
      "fair_maximum": 40,
      "code_availability": "available",
      "data_availability": "not_applicable",
      "preregistration": "not_applicable"
    },
    "era_context": {
      "publication_year": 2018,
      "era": "early_adopter",
      "era_label": "Early adopter era",
      "expectations_note": "Reproducibility practices emerging; FAIMS demonstrates exemplary practice for era"
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

**End of Credibility Assessment Report**
