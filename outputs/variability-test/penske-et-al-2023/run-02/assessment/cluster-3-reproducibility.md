# Cluster 3: Reproducibility Assessment

**Paper:** penske-et-al-2023
**Run:** run-02 (variability test)
**Assessment Date:** 2025-12-02
**Assessor Version:** v1.0

**Quality State:** HIGH
**Research Approach:** Inductive (confidence: high)
**Paper Type:** Empirical
**Assessment Pathway:** Standard (computational components present)

---

## Signal Score Summary

| Signal | Score | Band | Pathway |
|--------|-------|------|---------|
| Reproducibility | 62 | Good | Standard |

**Cluster Rating:** Adequate

---

## Signal 6: Reproducibility

**Score:** 62/100 (Good)

**Pathway:** Standard (computational methods: PCA, f-statistics, qpAdm, IBD, ROH, imputation)
**Approach anchors applied:** Inductive

### Assessment

This archaeogenomics study has substantial computational components including: PCA projection, f-statistics (f3, f4) calculations, qpAdm admixture modelling, imputation using GLIMPSE, IBD analysis, and runs of homozygosity (ROH) analysis. The standard reproducibility pathway applies.

**Data availability is excellent.** Raw sequence data is deposited in the European Nucleotide Archive (ENA) under accession PRJEB62503 with open access. This is the primary input for all downstream analyses and meets field standards for data sharing.

**Code availability is absent.** No custom analysis code repository is provided despite substantial computational analysis. The paper uses standard published software packages (EAGER, ADMIXTOOLS, GLIMPSE, HaploGrep2, ANGSD, READ, hapROH) with version numbers documented in Methods, but the specific scripts combining these tools, the parameter files, and the exact commands used are not shared.

**Environment specification is partial.** Software versions are documented (EAGER v.1.92.56, BWA v.0.7.12, ADMIXTOOLS v.5.1, etc.) which enables tool-level reproduction, but no containerised environment (Docker, Singularity) or requirements file is provided. Dependencies between tools are implicit.

**Workflow documentation is good but incomplete.** The Methods section documents the analytical pipeline at a conceptual level, and supplementary tables provide parameters, but the exact workflow orchestration is not reproducible without reconstructing the analysis from descriptions.

### Evidence

**From reproducibility_infrastructure:**

- **Code availability:** Not present. "No code availability statement. Paper uses standard published software packages with version numbers documented in Methods, but no custom analysis code repository provided."
- **Data availability:** Present. ENA PRJEB62503, open access, domain-specific repository.
- **Persistent identifiers:** Paper DOI (10.1038/s41586-023-06334-8), data accession (PRJEB62503). No software DOIs for custom scripts.
- **FAIR score:** 12/16 (moderately_fair) — Findability 3/4, Accessibility 4/4, Interoperability 2/4, Reusable 3/4

**From methods/protocols:**

- M02: "All samples were enriched for a panel of 1.24 million single-nucleotide polymorphisms" — Standard input format
- P05: Sequence processing with documented software versions (EAGER, BWA, DeDup, pileupCaller)
- P10: qpAdm methodology documented with outgroup specification referenced to supplementary tables

**Strengths:**

- Complete data archiving in standard repository (ENA) with open access
- All primary software tools named with version numbers
- Detailed supplementary tables with parameters and outgroup specifications
- Standard field tools enable methodological reproduction even without scripts

**Weaknesses:**

- No code repository for analysis scripts
- Environment not containerised or formally specified
- Workflow orchestration not documented (how tools were combined)
- Machine-actionability low (manual integration required)

### Tool Assessment

| Aspect | Status | Tool Type | Impact |
|--------|--------|-----------|--------|
| Sequence processing | EAGER pipeline | Open scriptable | No demerit |
| Population genetics | ADMIXTOOLS (qpAdm, f-stats) | Open scriptable | No demerit |
| Imputation | GLIMPSE | Open scriptable | No demerit |
| Relatedness | READ | Open scriptable | No demerit |
| ROH analysis | hapROH | Open scriptable | No demerit |
| Haplogroup calling | HaploGrep2 | Open scriptable | No demerit |
| **Custom integration** | Not shared | — | **Significant demerit** |

All primary tools are open-source and scriptable (Python, R, C++), which is ideal for reproducibility. The significant gap is the absence of the custom scripts/workflow that orchestrated these tools.

### Scoring Rationale

Score of 62 falls in the Good band (60-79) for inductive research. Data is archived with documentation (60-79 criterion for "data archived with documentation"). Workflow is documented at the methodological level. Procedures are explicit for individual tools. Observations (genetic data) are accessible.

Does not reach Excellent (80-100) because:

1. No code repository — analysis workflow cannot be directly re-executed
2. Environment not formally specified
3. Machine-actionability is low

Does not fall to Moderate (40-59) because:

1. Primary data is fully archived and accessible
2. All tools are documented with versions
3. Supplementary tables provide parameters
4. Standard tools enable methodological (if not exact) reproduction

---

## Reproducibility Readiness Checklist

```yaml
reproducibility_readiness:
  applies: true
  pathway: "standard"
  if_not_applicable_reason: ""

  inputs_available:
    status: "yes"
    details: "Raw sequence data in ENA (PRJEB62503) with open access. 1240K SNP-enriched ancient DNA data for 135 individuals."

  code_available:
    status: "no"
    tool_type: "open_scriptable"
    details: "No custom code repository. Uses standard tools (ADMIXTOOLS, EAGER, GLIMPSE, hapROH) with versions documented but integration scripts not shared."

  environment_specified:
    status: "partial"
    details: "Software versions documented (EAGER v.1.92.56, ADMIXTOOLS v.5.1, etc.) but no containerised environment or requirements file."

  outputs_documented:
    status: "partial"
    details: "Key results in supplementary tables (qpAdm models, f-statistics). Expected intermediate outputs not explicitly documented."

  execution_feasibility: "needs_work"
  feasibility_rationale: "Data available, standard tools identifiable, but analysis would require reconstructing the computational workflow from Methods descriptions. Experienced archaeogenomics researcher could reproduce with effort; exact reproduction not possible without original scripts."

  publication_year: 2023
  adoption_context: "early_majority"
```

---

## Cluster Synthesis

**Overall Reproducibility:** Adequate

The paper achieves adequate reproducibility for a 2023 archaeogenomics study. Data availability is excellent (ENA open access), meeting the critical requirement for computational reproduction. However, the absence of a code repository means the specific analytical workflow cannot be directly re-executed. An experienced archaeogenomics researcher familiar with ADMIXTOOLS and EAGER could reproduce the analyses methodologically using the documented parameters, but exact reproduction is not guaranteed.

### Chronological Context

Publication year 2023 places this paper in the **early_majority** era of reproducibility adoption (2020-2025). In this context, a score of 62 reflects:

- **Above-average data sharing:** ENA deposition with open access exceeds minimum expectations
- **Below-average code sharing:** Code repositories are increasingly expected for computational papers in Nature journals
- **Standard for archaeogenomics:** Many comparable papers similarly provide data but not code

The field of archaeogenomics has strong data sharing norms (driven by ENA/AADR infrastructure) but weaker code sharing practices compared to computational genetics or bioinformatics.

### Gateway Assessment

**Execution Feasibility:** needs_work

This paper could be queued for a reproduction attempt with the following considerations:

**What would be needed:**

1. Download data from ENA (PRJEB62503)
2. Reconstruct bioinformatic pipeline using documented tools and versions
3. Reconstruct qpAdm model specifications from supplementary tables
4. Run analyses using standard archaeogenomics workflows

**Gaps to address:**

- Exact script parameters for workflow orchestration
- Intermediate file formats and naming conventions
- Environment configuration details

**Estimated effort:** High — would require archaeogenomics expertise and substantial workflow reconstruction. Results would be "methodologically reproducible" but possibly not exactly identical due to undocumented analysis choices.

---

## Structured Output

```yaml
cluster_3_reproducibility:
  paper_slug: "penske-et-al-2023"
  run: "run-02"
  assessment_date: "2025-12-02"
  quality_state: "high"
  research_approach: "inductive"
  pathway: "standard"
  experimental: false

  reproducibility:
    score: 62
    band: "good"
    strengths:
      - "Complete data archiving in ENA with open access"
      - "All software tools documented with versions"
      - "Supplementary tables provide analytical parameters"
      - "Standard open-source tools enable methodological reproduction"
    weaknesses:
      - "No code repository for analysis scripts"
      - "Environment not containerised or formally specified"
      - "Workflow orchestration not documented"
      - "Low machine-actionability"
    rationale: "Good for inductive. Data archived and accessible, workflow documented at method level. Below Excellent due to missing code and environment specification."
    tool_assessment:
      primary_tool_type: "open_scriptable"
      tool_impact: "All primary tools open-source; significant demerit only for absent custom integration scripts"

  reproducibility_readiness:
    applies: true
    pathway: "standard"
    inputs_available:
      status: "yes"
      details: "ENA PRJEB62503 with open access"
    code_available:
      status: "no"
      tool_type: "open_scriptable"
      details: "Standard tools documented, custom scripts not shared"
    environment_specified:
      status: "partial"
      details: "Software versions documented, no container/requirements"
    outputs_documented:
      status: "partial"
      details: "Results in supplementary tables, intermediates not documented"
    execution_feasibility: "needs_work"
    feasibility_rationale: "Data available, tools identifiable, workflow requires reconstruction"
    publication_year: 2023
    adoption_context: "early_majority"

  cluster_synthesis:
    overall_rating: "adequate"
    chronological_interpretation: "Above-average for data sharing, below-average for code sharing relative to 2023 expectations. Standard for archaeogenomics field."
    gateway_recommendation: "Methodological reproduction possible with archaeogenomics expertise; exact reproduction not feasible without original scripts."
```
