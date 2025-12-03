# Credibility Assessment Report

**Paper:** FAIMS Mobile: Flexible, open-source software for field research
**DOI:** [10.1016/j.softx.2017.12.006](https://doi.org/10.1016/j.softx.2017.12.006)
**Publication Year:** 2018
**Assessment Date:** 2025-12-03

---

## Executive Summary

**Verdict:** Good | **Confidence:** HIGH

This methodological software paper using inductive reasoning demonstrates strong foundational clarity and excellent reproducibility infrastructure. Published in 2018 during the early adopter era of open science, this paper exceeds contemporary expectations for software publication practice.

**Key Strengths:**

- Exceptional transparency: GPLv3 open source code with multiple distribution channels (GitHub, Google Play, direct download) and comprehensive documentation
- Clear technical specification: Software architecture, design rationale, and feature descriptions are explicit and well-bounded
- Strong reproducibility infrastructure: FAIR score of 93.75%, permanent archived links, version-controlled repositories

**Key Concerns:**

- Genre-appropriate moderate Robustness (📦 flag): Software papers describe artefacts rather than test alternatives — this is expected, not a deficiency

**Bottom Line:** A well-executed software publication that demonstrates best practices for open-source research software documentation and distribution.

---

## Signal Scores Dashboard

| Signal | Score | Band | Context Flag |
|--------|-------|------|--------------|
| Comprehensibility | 88 | Excellent | — |
| Transparency | 92 | Excellent | — |
| Plausibility | 82 | Excellent | — |
| Validity | 75 | Good | — |
| Robustness | 55 | Moderate | 📦 |
| Generalisability | 72 | Good | — |
| Reproducibility | 90 | Excellent | 🔧 |

**Aggregate Score:** 79 (Good) — *EXPERIMENTAL*

---

## Detailed Cluster Findings

### Cluster 1: Foundational Clarity — **Strong**

The paper achieves exemplary comprehensibility and transparency for a software publication. Technical specifications are explicit and bounded, with a clear logical structure from motivation (Section 1) through architecture (2.1), functionalities (2.2), examples (3), impact (4), to conclusions (5).

**Key Strengths:**

- Design rationale explicit: "We developed this architecture to meet two fundamental requirements..."
- Feature descriptions bounded and precise: 23 capabilities enumerated with clear specifications
- Comprehensive documentation: Module Cookbook, Beanshell API, Developer docs, User-to-Developer pathway

**Key Weaknesses:**

- Some implicit assumptions about field research contexts remain unstated (minor, appropriate for venue)

---

### Cluster 2: Evidential Strength — **Adequate-to-Strong**

Evidence is well-grounded with strong theoretical basis and appropriate validation for a software description paper. Plausibility is high due to grounding in established field research challenges. Validity is good with technical specifications and adoption metrics supporting claims.

**Key Strengths:**

- Strong theoretical grounding in field research literature (Borgman, Kintigh, Snow et al.)
- Honest acknowledgement of trade-offs: "customisation is more entailed" than alternatives
- Adoption metrics provide quantitative validation (40+ customisations, 29 deployments, ~300 users, 20,000+ hours)

**Key Weaknesses:**

- Efficiency claims based on qualitative case study reports rather than systematic measurement
- No systematic benchmark comparison with alternatives (appropriate for genre)

---

### Cluster 3: Reproducibility — **Strong**

**Pathway:** Methodological Transparency Variant

The software itself is the reproducible artefact, and it is exceptionally accessible. Multiple redundant distribution channels, open source licensing, and comprehensive documentation ensure long-term availability and usability.

**Key Strengths:**

- Multiple distribution channels: GitHub (archive + active), Google Play, direct APK, server installer
- Open source licence (GPLv3) ensures perpetual reusability
- Comprehensive documentation with permanent archived links (perma.cc)
- Active project with support infrastructure

**Key Weaknesses:**

- Optional proprietary dependency (Nutiteq for non-watermarked GIS)
- No containerisation (not standard practice in 2017)

---

## Contextual Interpretation

### Robustness (55, Moderate) 📦

**Why this score:** This is a software paper describing an artefact (FAIMS Mobile). Software papers document what tools do; they do not perform systematic comparative evaluation against alternatives. A Moderate Robustness score reflects genre expectations, not a deficiency.

**What this means:** The paper describes FAIMS Mobile's features, architecture, and adoption. It honestly documents trade-offs (customisation complexity vs capability) and limitations (time front-loading). Comparative assessment is the reader's responsibility.

**What readers should consider:** Evaluate alternative field data collection tools (ODK, ARK, Heurist, Kora) independently. Consider project requirements against documented FAIMS features. The paper provides comparison guidance but not systematic evaluation.

**Generalisation:** Similar patterns are expected for other software, data, infrastructure, protocol, and resource papers. These papers describe artefacts; systematic comparison is a different paper type.

---

### Reproducibility (90, Excellent) 🔧

**Why this score:** For software papers, reproducibility means: Can users install, use, and extend the software? FAIMS Mobile excels on all dimensions: multiple installation pathways, open source code, comprehensive documentation, and active community support.

**What this means:** The software can be downloaded and installed immediately. Android app available on Google Play. Server installation documented with Puppet script. Module customisation supported with extensive tutorials.

**What readers should consider:** Server installation may need updating for current Ubuntu versions (16.04 now EOL). Nutiteq licence required for non-watermarked GIS (optional). Active project with support available at support@fedarch.org.

---

## Infrastructure & FAIR Summary

**FAIR Score:** 15/16 (93.75%) — Excellent

| Dimension | Score | Notes |
|-----------|-------|-------|
| Findable | 4/4 | DOI, multiple repository links, permanent archived URLs |
| Accessible | 4/4 | Open access publication, GPLv3 code, multiple channels |
| Interoperable | 3/4 | Standard formats (XML, SQL, shapefiles, GeoJSON), linked data support |
| Reusable | 4/4 | Extensive documentation, open licence, explicit versioning |

**Code Availability:** ✅ Available — GPLv3, GitHub (Elsevier archive + FAIMS Project), Google Play, direct APK

**Data Availability:** Not applicable — software publication

**Preregistration:** Not applicable — software publication

**PID Coverage:**

- Paper DOI: ✅ 10.1016/j.softx.2017.12.006
- Software PIDs: ✅ GitHub repository (archived), perma.cc links
- Author ORCIDs: ❌ Not captured (predates widespread adoption)

**Infrastructure Gaps:** None significant. Minor: Optional proprietary dependency (Nutiteq), no containerisation.

---

## Era Context

**Publication Year:** 2018
**Era:** Early adopter
**Era Label:** Early adopter era — reproducibility discussions emerging, data/code sharing becoming expected

**Expectations Note:** In 2018, comprehensive open-source documentation with permanent archived links exceeded contemporary standards. This paper demonstrates leading-edge practice for its era.

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
      "aggregate_score": 79,
      "aggregate_experimental": true
    },
    "signals": {
      "comprehensibility": { "score": 88, "band": "excellent" },
      "transparency": { "score": 92, "band": "excellent" },
      "plausibility": { "score": 82, "band": "excellent" },
      "validity": { "score": 75, "band": "good" },
      "robustness": { "score": 55, "band": "moderate", "context_flag": "📦" },
      "generalisability": { "score": 72, "band": "good" },
      "reproducibility": { "score": 90, "band": "excellent", "variant": "methodological_transparency" }
    },
    "aggregates": {
      "cluster_1_rating": "strong",
      "cluster_2_rating": "adequate-to-strong",
      "cluster_3_rating": "strong"
    },
    "infrastructure": {
      "fair_score": 15,
      "fair_rating": "excellent",
      "fair_maximum": 16,
      "code_availability": "available",
      "data_availability": "not_applicable",
      "preregistration": "not_applicable"
    },
    "era_context": {
      "publication_year": 2018,
      "era": "early_adopter",
      "era_label": "Early adopter era — reproducibility discussions emerging, data/code sharing becoming expected",
      "expectations_note": "Exceeds contemporary standards for software publication practice"
    },
    "assessment_metadata": {
      "assessment_date": "2025-12-03",
      "assessor_version": "v1.0",
      "schema_version": "1.0",
      "extractor": "claude-opus-4-5-20251101",
      "run_id": "run-05"
    }
  }
}
```

---

## Assessment Quality Notes

**Quality State:** HIGH

- Extraction confidence: High (47 evidence, 61 claims, 18 RDMAP items)
- Classification confidence: High (unambiguous software publication)
- All bidirectional mappings validated

**Assessment Precision:** Full (±5 point precision on all scores)

---

*Report generated using research-assessor v1.0*
*Schema version: 1.0*
*Extraction schema: v2.6*
