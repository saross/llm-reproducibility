# Credibility Assessment Report

**Paper:** Sobotkova et al. 2016 — "Measure Twice, Cut Once: Cooperative Deployment of a Generalized Mobile Recording System"

**Assessment Date:** 2025-12-04
**Assessor Version:** v1.0
**Schema Version:** 1.0

---

## Executive Summary

**Verdict:** Good | **Confidence:** HIGH

This **methodological** paper using **inductive** reasoning demonstrates solid credibility appropriate for a software tool presentation. Publication year 2016 places this in the early adopter era — transparency expectations were lower than today, making the open source availability on GitHub notably progressive.

**Key Strengths:**

- Open source software on GitHub with explicit GPLv3 licence — exemplary for 2016
- Clear technical specifications with bounded definitions (four-level customisation hierarchy)
- Appropriate claim scoping — presents "observations" and "lessons learned" rather than universal principles
- Honest limitation acknowledgement (device constraints, support requirements, learning curves)

**Key Concerns:**

- Qualitative analysis methodology undocumented — theme identification and quote selection procedures implicit
- No archived software DOI — GitHub URL provides access but not stable citation for 2016 version

**Bottom Line:** A well-documented software tool paper that exceeds 2016 reproducibility norms, limited by undocumented qualitative methodology for case study synthesis.

---

## Signal Scores Dashboard

| Signal | Score | Band | Context Flag |
|--------|-------|------|--------------|
| Comprehensibility | 72 | Good | — |
| Transparency | 68 | Good | — |
| Plausibility | 75 | Good | — |
| Validity | 62 | Good | — |
| Robustness | 48 | Moderate | 📦 Software paper |
| Generalisability | 70 | Good | — |
| Reproducibility | 65 | Good | 🔧 Software transparency |

**Aggregate Score:** 66 (EXPERIMENTAL)
**Aggregate Band:** Good

---

## Classification Summary

| Attribute | Value |
|-----------|-------|
| Paper Type | methodological |
| Paper Subtype | software_tool |
| Approach | inductive |
| Framework | methodological paper |
| Quality State | HIGH |
| Classification Confidence | HIGH |

---

## Detailed Findings by Cluster

### Cluster 1: Foundational Clarity — Adequate

**Signals assessed:** Comprehensibility (72), Transparency (68)

The paper demonstrates adequate foundational clarity. Technical specifications for the FAIMS platform are clear and bounded — the four-level customisation hierarchy (core, approach, module, instance) is precisely defined. The co-development partnership model is articulated with explicit rationale.

However, the qualitative methodology for thematic synthesis is implicit. Readers understand WHAT themes were identified but not HOW they were derived from case study data. This creates an asymmetry: strong technical transparency, weak methodological transparency.

**Key Strengths:**

- Software architecture documented with design rationale
- Code publicly available on GitHub with explicit GPLv3 licence
- Logical progression from platform description to case studies to themes is traceable

**Key Weaknesses:**

- Theme identification methodology undocumented (M-IMP-001)
- Quote selection criteria unspecified (M-IMP-002)
- No archived software DOI (GitHub URL only)

---

### Cluster 2: Evidential Strength — Adequate

**Signals assessed:** Plausibility (75), Validity (62), Robustness (48), Generalisability (70)

The paper demonstrates adequate evidential strength with a profile typical of methodological/software papers. Claims align well with domain knowledge and show consistent patterns across three varied archaeological deployments. Claims are appropriately bounded and limitations acknowledged.

Validity is adequate for platform capability claims but weaker for thematic synthesis claims due to undocumented qualitative methodology. Robustness is moderate, which is genre-appropriate for software description papers.

**Key Strengths:**

- Claims consistent with established software engineering and archaeological computing literature
- 28 evidence items documenting deployment experiences across three projects
- Case studies span different archaeological research types (excavation, survey, regional)

**Key Weaknesses:**

- No comparison to alternative platforms (ODK, Fulcrum, etc.) — readers must evaluate alternatives independently
- Retrospective design limits causal inference
- Limited consideration of alternative interpretations for thematic claims

---

### Cluster 3: Reproducibility — Adequate

**Signal assessed:** Reproducibility (65)
**Pathway:** standard (has computational component)

The FAIMS software is openly available on GitHub under GPLv3 licence, providing strong code reproducibility. The platform can be examined, modified, and deployed. However, the case study analysis methodology cannot be reproduced due to documentation gaps.

**Key Strengths:**

- Complete source code on GitHub
- GPLv3 licence enables examination and modification
- Module definition documents provide replication examples

**Key Weaknesses:**

- No DOI for archived software version
- Qualitative analysis methodology undocumented
- Data collection instruments not provided

**Execution Feasibility:** needs_work — Software deployable with effort; qualitative analysis not reproducible

---

## Contextual Interpretation

### Robustness (48, Moderate) 📦

**Why this score:** This is a software description paper, not a hypothesis-testing study. Software papers describe artefacts rather than testing them against alternatives. A Moderate Robustness score reflects genre expectations — it is not a criticism of the paper.

**What this means:** The paper describes the FAIMS platform and its deployment experiences. It does not claim to prove FAIMS is superior to alternatives. Comparative evaluation is a different paper type.

**What readers should consider:** Evaluate alternative mobile data collection platforms (ODK, Fulcrum, commercial solutions) independently when deciding on tools for your project. This paper provides evidence that FAIMS works, not that it works better than alternatives.

**Generalisation:** Similar patterns expected for other software, data, infrastructure, protocol, and resource papers.

---

### Reproducibility (65, Good) 🔧

**Why this score:** For software papers, reproducibility means: Can users install, use, and extend the software? FAIMS meets this criterion well through open source availability on GitHub.

**What this means:** The software itself is highly reproducible. The case study analysis is not — theme identification methodology is undocumented.

**What readers should consider:** The software can be examined and deployed. If you want to replicate the case study analysis, you would need to develop your own methodology for synthesising deployment experiences.

---

## Infrastructure & FAIR Summary

| Metric | Value | Notes |
|--------|-------|-------|
| FAIR Score | 9/16 | 56.25% — moderately_fair |
| Code Availability | available | GitHub (https://github.com/FAIMS), GPLv3 |
| Data Availability | implicit_reference | Supplementary materials referenced, access unclear |
| Preregistration | not_applicable | Not expected for methodological paper |
| Paper DOI | none | Book chapter — no individual chapter DOI |
| Author ORCIDs | 0/6 | None found (typical for 2016) |
| Software DOI | none | GitHub URL only |

**Infrastructure Strengths:**

- Open source code with explicit licence
- Funding sources documented with grant numbers
- Two major grants acknowledged (NeCTAR RT043, ARC LE140100151)

**Infrastructure Gaps:**

- No archived software version with DOI
- Supplementary materials access unclear
- No author contribution or conflict of interest statements

---

## Era Context

**Publication Year:** 2016
**Era:** Early adopter (2015-2020)
**Expectations Note:** In 2016, open source availability on GitHub was progressive for archaeological computing. DOIs for software were rare, and FAIR principles had not yet been widely adopted in HASS. The score of 66 is above expectations for this era.

---

## JSON Output

```json
{
  "credibility_report": {
    "version": "1.0",
    "paper": {
      "slug": "sobotkova-et-al-2016",
      "title": "Measure Twice, Cut Once: Cooperative Deployment of a Generalized Mobile Recording System",
      "doi": null,
      "publication_year": 2016
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
      "aggregate_score": 66,
      "aggregate_experimental": true
    },
    "signals": {
      "comprehensibility": { "score": 72, "band": "good" },
      "transparency": { "score": 68, "band": "good" },
      "plausibility": { "score": 75, "band": "good" },
      "validity": { "score": 62, "band": "good" },
      "robustness": { "score": 48, "band": "moderate", "context_flag": "software_paper" },
      "generalisability": { "score": 70, "band": "good" },
      "reproducibility": { "score": 65, "band": "good", "variant": "standard" }
    },
    "aggregates": {
      "cluster_1_rating": "adequate",
      "cluster_2_rating": "adequate",
      "cluster_3_rating": "adequate"
    },
    "infrastructure": {
      "fair_score": 9,
      "fair_rating": "moderately_fair",
      "fair_maximum": 16,
      "code_availability": "available",
      "data_availability": "implicit_reference",
      "preregistration": "not_applicable"
    },
    "era_context": {
      "publication_year": 2016,
      "era": "early_adopter",
      "era_label": "Early adopter era — reproducibility discussions emerging, data/code sharing becoming expected",
      "expectations_note": "Score of 66 exceeds 2016 era expectations for HASS software papers"
    },
    "assessment_metadata": {
      "assessment_date": "2025-12-04",
      "assessor_version": "v1.0",
      "schema_version": "1.0"
    }
  }
}
```

---

## Assessment Quality Notes

**Quality State:** HIGH
**Extraction Confidence:** HIGH
**Classification Confidence:** HIGH

This assessment was conducted with full precision (±5 point scores). No caveats apply.

---

**End of Credibility Assessment Report**
