# Cluster 3: Reproducibility Assessment

**Paper:** sobotkova-et-al-2016
**Assessment Date:** 2025-12-04
**Assessor Version:** v1.0

**Quality State:** HIGH
**Research Approach:** inductive (confidence: high)
**Paper Type:** methodological
**Assessment Pathway:** methodological_transparency_variant

**⚠️ EXPERIMENTAL:** Using Methodological Transparency alternate anchors. This paper is a software description/case study without computational analysis of data. The methodological transparency variant assesses whether methods are documented clearly enough that someone could apply the same approach to different data/contexts.

---

## Signal Score Summary

| Signal | Score | Band | Pathway |
|--------|-------|------|---------|
| Reproducibility | 62 | Good | methodological_transparency_variant |

**Cluster Rating:** Adequate

---

## Signal 6: Reproducibility

**Score:** 62/100 (Good)

**Pathway:** methodological_transparency_variant
**Approach anchors applied:** inductive/methodological

### Assessment

This paper describes FAIMS mobile platform deployment experiences rather than presenting computational analyses of data. There are no statistical analyses, computational workflows, or quantitative modelling to reproduce. The reproducibility question therefore shifts from "can someone re-run the code?" to "can someone apply the same methodological approach?"

The methodological approach (case study documentation with thematic analysis) is well-documented at the high level. Research design (RD001) explicitly states the case study methodology. Data collection methods (M001-M002) specify questionnaires and project communications as sources. The thematic analysis approach (M003) is identified, and cost-benefit analysis methods (M004) are described.

However, reproducibility of the analytical process is limited by implicit protocols. P004 (theme derivation) notes that coding procedures are not documented - another researcher could not precisely replicate the thematic analysis. P005 (cost calculations) notes that methodology for time/cost comparisons is not specified. These are typical limitations for case study research but affect methodological reproducibility.

A significant strength is the **software reproducibility**: FAIMS itself is fully open-source (GPLv3), documented on GitHub, and available for redeployment. While the case study evaluation cannot be precisely reproduced, the software being evaluated can be independently examined and deployed.

### Evidence

**From reproducibility_infrastructure:**
- Code availability: **YES** — GitHub repository (FAIMS), GPLv3 licence, comprehensive documentation
- Data availability: **PARTIAL** — Questionnaires referenced in supplementary materials but not directly archived
- Persistent identifiers: **LIMITED** — No DOIs for specific software versions; no formal data DOI
- FAIR score: 8/16 (50%, "minimally_fair")

**From methods/protocols:**
- M001: "Post-deployment questionnaires completed by project directors" — Data collection method specified
- M003: "Thematic analysis approach for synthesis across case studies" — Analytical method stated
- P004 (implicit): "Theme derivation process and coding procedures not documented" — Reproducibility gap
- P005 (implicit): "Calculation methodology for time/cost comparisons not specified" — Cannot verify quantitative claims

**Strengths:**
- Software fully open-source and redeployable (GitHub, GPLv3)
- Case study methodology explicitly stated (RD001)
- Data collection methods documented (questionnaires, communications)
- Supplementary materials provide access to questionnaire data

**Weaknesses:**
- Thematic analysis procedures implicit - cannot precisely replicate coding
- Cost calculation methodology not documented
- No formal data archiving with PIDs
- Inter-coder reliability not assessed

### Tool Assessment

| Aspect | Status | Tool Type | Impact |
|--------|--------|-----------|--------|
| Primary software | FAIMS Mobile | open_scriptable | No demerit - fully open source |
| Data collection | Questionnaires | gui_based | Moderate demerit - manual process |
| Analysis | Thematic coding | gui_based | Significant demerit - implicit procedures |
| Cost calculations | Unknown | unknown | Significant demerit - methodology not specified |

### Scoring Rationale

Score of 62 (Good for methodological transparency variant) reflects: most methods clear (60-79), some tacit knowledge required for thematic analysis, generally reproducible approach at high level. The software itself is exemplary (open source, documented), but the case study evaluation methodology has typical qualitative research limitations. An experienced researcher could approximate the approach but could not precisely replicate the thematic analysis without documented coding procedures.

---

## Reproducibility Readiness Checklist

```yaml
reproducibility_readiness:
  applies: true
  pathway: "methodological_transparency_variant"
  if_not_applicable_reason: ""

  inputs_available:
    status: "partial"
    details: "Questionnaire responses referenced in supplementary materials but not formally archived. Case study communications (emails, chat) summarised but not raw data. Software source code fully available."

  code_available:
    status: "yes"
    tool_type: "open_scriptable"
    details: "FAIMS software fully open source (GPLv3) on GitHub. No analysis code exists - paper is descriptive case study without computational analysis."

  environment_specified:
    status: "partial"
    details: "FAIMS deployment requirements documented (Android devices, server infrastructure). No computational environment for analysis (none exists - qualitative case study)."

  outputs_documented:
    status: "partial"
    details: "Three themes and supporting findings documented. Specific cost figures provided but calculation methodology not documented."

  execution_feasibility: "needs_work"
  feasibility_rationale: "Software can be independently examined and deployed. Case study methodology can be approximated but not precisely reproduced without documented thematic coding procedures and raw questionnaire data."

  publication_year: 2016
  adoption_context: "early_adopter"
```

---

## Cluster Synthesis

**Overall Reproducibility:** Adequate

The paper demonstrates adequate reproducibility for a methodological case study from the early-adopter era. The software being described (FAIMS) is exemplary in its openness - fully open-source, well-documented, and redeployable. However, the case study evaluation methodology has typical qualitative research limitations: thematic analysis procedures are implicit, and raw data is not formally archived.

The dichotomy is instructive: **software reproducibility is strong** (anyone can deploy FAIMS), but **analytical reproducibility is limited** (another researcher could not precisely replicate the thematic analysis). This is appropriate for the paper's contribution - readers should evaluate the software directly rather than replicating the case study findings.

### Chronological Context

Publication year 2016 places this paper in the **early_adopter** era of reproducibility adoption. At this time, open-source software release was emerging as good practice but formal data archiving with DOIs was not yet standard. The paper's commitment to open-source software (GPLv3, GitHub) represents strong practice for its era. The lack of formal data archiving and documented analytical procedures reflects typical practices at the time rather than a deficiency relative to contemporaries.

### Gateway Assessment

**Execution Feasibility:** needs_work

This paper could not be queued for precise analytical reproduction without:

1. **Raw questionnaire data**: Access to original project director responses
2. **Thematic coding scheme**: Documented procedures for theme derivation
3. **Cost calculation methodology**: Specification of how time/cost figures were derived

However, the **software itself is ready for independent evaluation**: FAIMS can be downloaded, deployed, and assessed without any additional materials. Readers interested in the paper's claims about FAIMS capabilities can verify them directly.

---

## Structured Output

```yaml
cluster_3_reproducibility:
  paper_slug: "sobotkova-et-al-2016"
  assessment_date: "2025-12-04"
  quality_state: "high"
  research_approach: "inductive"
  pathway: "methodological_transparency_variant"
  experimental: true

  reproducibility:
    score: 62
    band: "good"
    strengths:
      - "Software fully open-source (GPLv3) and redeployable"
      - "Case study methodology explicitly stated"
      - "Data collection methods documented"
      - "Supplementary materials provide questionnaire access"
    weaknesses:
      - "Thematic analysis procedures implicit - cannot precisely replicate coding"
      - "Cost calculation methodology not documented"
      - "No formal data archiving with PIDs"
    rationale: "Good methodological transparency for qualitative case study. Software exemplary (open source). Analytical procedures have typical qualitative research limitations."
    tool_assessment:
      primary_tool_type: "open_scriptable (software) + gui_based (analysis)"
      tool_impact: "Software: no demerit. Analysis: significant demerit due to implicit procedures."

  reproducibility_readiness:
    applies: true
    pathway: "methodological_transparency_variant"
    inputs_available:
      status: "partial"
      details: "Questionnaire data referenced but not formally archived. Software fully available."
    code_available:
      status: "yes"
      tool_type: "open_scriptable"
      details: "FAIMS software open source on GitHub. No analysis code (descriptive case study)."
    environment_specified:
      status: "partial"
      details: "FAIMS deployment requirements documented. No computational analysis environment."
    outputs_documented:
      status: "partial"
      details: "Themes and cost figures documented but calculation methodology not specified."
    execution_feasibility: "needs_work"
    feasibility_rationale: "Software reproducible. Case study methodology can be approximated but not precisely reproduced."
    publication_year: 2016
    adoption_context: "early_adopter"

  cluster_synthesis:
    overall_rating: "adequate"
    chronological_interpretation: "Strong software transparency for 2016 (open source, GitHub). Typical qualitative research limitations in analytical documentation."
    gateway_recommendation: "Software ready for independent evaluation. Case study evaluation not precisely reproducible without raw data and coding procedures."
```
