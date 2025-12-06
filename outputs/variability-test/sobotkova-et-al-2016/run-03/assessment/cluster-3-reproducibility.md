# Cluster 3: Reproducibility Assessment

**Paper:** sobotkova-et-al-2016
**Assessment Date:** 2025-12-04
**Assessor Version:** v1.0

**Quality State:** HIGH
**Research Approach:** inductive (confidence: high)
**Paper Type:** methodological (software_tool)
**Assessment Pathway:** standard

---

## Signal Score Summary

| Signal | Score | Band | Pathway |
|--------|-------|------|---------|
| Reproducibility | 65 | Good | standard |

**Cluster Rating:** Adequate

---

## Signal 6: Reproducibility

**Score:** 65/100 (Good)

**Pathway:** standard
**Approach anchors applied:** inductive/methodological

### Assessment

The paper has a computational component (FAIMS mobile software platform) that enables standard reproducibility assessment. The software is the primary contribution, and its reproducibility is the key assessment target.

**Software Reproducibility (Primary Target):**

The FAIMS software is openly available on GitHub (https://github.com/FAIMS) under GPLv3 licence. This enables:

- **Code access:** Complete source code publicly available
- **Modification rights:** Open source licence permits examination, modification, redistribution
- **Module examples:** Example module definitions available for review

However, reproducibility is limited by:

- **No archived version:** No DOI for specific software version cited in paper
- **No environment specification:** Dependencies and build requirements not comprehensively documented in paper (though GitHub may have setup instructions)
- **Platform evolution:** Software has evolved since 2016 — current GitHub version differs from 2016 deployment

**Case Study Reproducibility (Secondary Target):**

The case study analysis methodology is not reproducible:

- Post-project questionnaire instrument not provided (P001 mentions questionnaire but doesn't include it)
- Communication log analysis procedure undocumented (M002)
- Theme identification methodology undocumented (M-IMP-001)
- Quote selection criteria unspecified (M-IMP-002)

This limits reproducibility of the thematic synthesis, though the software capability demonstrations could be replicated with new deployments.

### Evidence

**From reproducibility_infrastructure:**

- Code availability: **present** — GitHub repository (https://github.com/FAIMS), GPLv3 licence
- Data availability: **implicit_reference** — Supplementary materials referenced but access unclear
- Persistent identifiers: Software URL only (no DOI)
- FAIR score: 9/16 (56.25%)

**From methods/protocols:**

- P003: Module forking procedure documented — Enables replication of customisation workflow
- P007: Version control workflow documented — GitHub-based collaboration process clear
- M001: Post-project questionnaire mentioned but instrument not provided
- M-IMP-001, M-IMP-002: Qualitative analysis methodology undocumented

**Strengths:**

- Open source software fully available on GitHub
- GPLv3 licence enables examination and modification
- Module definition documents provide replication examples
- Funding acknowledged with grant numbers (aids provenance)

**Weaknesses:**

- No DOI for archived software version
- Data collection instruments not provided
- Qualitative analysis methodology undocumented
- Supplementary materials access unclear

### Tool Assessment

| Aspect | Status | Tool Type | Impact |
|--------|--------|-----------|--------|
| FAIMS platform | Open source on GitHub | open_scriptable | No demerit — ideal for reproducibility |
| Module definitions | XML-based configuration | open_scriptable | No demerit — structured, parseable format |
| Data collection | Questionnaire + communication logs | gui_based (email) | Moderate demerit — data collection process manual |
| Qualitative analysis | Thematic synthesis | manual | Significant demerit — process undocumented |

### Scoring Rationale

Score of 65 (Good for inductive/methodological). Code shared with documentation on GitHub (60-79 criterion), analysis workflow partially documented (60-79), data accessibility partially addressed (60-79). Not Excellent because no archived software DOI (would need persistent identifier for 80-100), qualitative analysis methodology undocumented (would need complete workflow documentation for 80-100), and data collection instruments not fully shared (would need comprehensive data documentation for 80-100).

---

## Reproducibility Readiness Checklist

```yaml
reproducibility_readiness:
  applies: true
  pathway: "standard"
  if_not_applicable_reason: ""

  inputs_available:
    status: "partial"
    details: "FAIMS source code available on GitHub. Module definition documents available as supplementary materials (access mechanism unclear). Case study questionnaire and communication log data not provided."

  code_available:
    status: "yes"
    tool_type: "open_scriptable"
    details: "Complete FAIMS platform source code on GitHub (https://github.com/FAIMS). GPLv3 licence. Module definition documents (XML-based) available."

  environment_specified:
    status: "partial"
    details: "Platform is Android-based with server component. Specific version and dependency requirements not documented in paper. GitHub repository may contain setup instructions but not cited in paper."

  outputs_documented:
    status: "partial"
    details: "Expected software behaviours described (offline data capture, sync, export). Case study outcomes documented. No formal output verification criteria or test cases."

  execution_feasibility: "needs_work"
  feasibility_rationale: "Software could be deployed and tested with effort. Would need to: (1) Identify correct 2016 software version, (2) Set up Android development environment, (3) Configure server component. Case study reproduction would require: (4) Deploying module to archaeological project, (5) Collecting comparable deployment experience data. Qualitative analysis reproduction not feasible due to methodology gaps."

  publication_year: 2016
  adoption_context: "early_adopter"
```

---

## Cluster Synthesis

**Overall Reproducibility:** Adequate

The paper demonstrates adequate reproducibility for its primary contribution (FAIMS software) but limited reproducibility for its secondary contribution (thematic synthesis from case studies). The open source availability on GitHub is a significant strength — the software can be examined, modified, and deployed. The GPLv3 licence explicitly enables reproduction and derivative work.

The score of 65 reflects a paper that exceeds baseline expectations for 2016 HASS methodology publication but falls short of ideal reproducibility practices. The key gap is the absence of archived, versioned software with DOI — the GitHub URL provides access but not the stable citation required for precise reproduction of 2016 functionality.

### Chronological Context

Publication year 2016 places this paper in the **early_adopter** era of reproducibility adoption. In 2016, open source availability on GitHub was progressive for archaeological computing. DOIs for software were rare, and FAIR principles had not yet been widely adopted in HASS. The score of 65 is above expectations for this era — many 2016 HASS methodology papers had no code sharing at all.

### Gateway Assessment

**Execution Feasibility:** needs_work

This paper could be queued for software reproduction attempt, but gaps need to be addressed:

**What would be needed to attempt reproduction:**

1. **Version identification:** Determine which GitHub commit corresponds to 2016 paper
2. **Environment setup:** Configure Android development environment and server component
3. **Module deployment:** Deploy sample module following documented procedures
4. **Functionality verification:** Test claimed features (offline capture, sync, customisation)

**Gaps to address:**

- Archived software version not identified (would need GitHub archaeology or author contact)
- Server setup procedure not documented in paper
- Test criteria not specified (what counts as successful reproduction?)

**Not feasible:**

- Reproducing qualitative thematic analysis — methodology undocumented
- Verifying specific case study claims — primary data not available

---

## Structured Output

```yaml
cluster_3_reproducibility:
  paper_slug: "sobotkova-et-al-2016"
  assessment_date: "2025-12-04"
  quality_state: "high"
  research_approach: "inductive"
  pathway: "standard"
  experimental: false

  reproducibility:
    score: 65
    band: "good"
    strengths:
      - "Open source software available on GitHub"
      - "GPLv3 licence enables examination and modification"
      - "Module definition documents provide replication examples"
    weaknesses:
      - "No DOI for archived software version"
      - "Qualitative analysis methodology undocumented"
      - "Data collection instruments not provided"
    rationale: "Good for inductive/methodological. Strong code availability (GitHub, open source). Not Excellent due to missing archived DOI and undocumented qualitative methodology."
    tool_assessment:
      primary_tool_type: "open_scriptable"
      tool_impact: "Ideal — no reproducibility demerit for software"

  reproducibility_readiness:
    applies: true
    pathway: "standard"
    inputs_available:
      status: "partial"
      details: "Source code available. Case study data not provided."
    code_available:
      status: "yes"
      tool_type: "open_scriptable"
      details: "GitHub repository, GPLv3 licence"
    environment_specified:
      status: "partial"
      details: "Android-based platform. Specific dependencies not documented in paper."
    outputs_documented:
      status: "partial"
      details: "Expected behaviours described. No formal verification criteria."
    execution_feasibility: "needs_work"
    feasibility_rationale: "Software deployable with effort. Would need version identification and environment setup. Qualitative analysis not reproducible."
    publication_year: 2016
    adoption_context: "early_adopter"

  cluster_synthesis:
    overall_rating: "adequate"
    chronological_interpretation: "Score of 65 exceeds 2016 early_adopter era expectations. Open source GitHub availability was progressive for archaeological computing."
    gateway_recommendation: "Software reproduction feasible with effort. Qualitative analysis reproduction not feasible. Queue for partial reproduction attempt if resources available."
```
