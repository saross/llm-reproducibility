# Cluster 3: Reproducibility Assessment

**Paper:** penske-et-al-2023
**Assessment Date:** 2025-12-02
**Assessor Version:** v1.0

**Quality State:** HIGH
**Research Approach:** inductive (confidence: high)
**Paper Type:** empirical
**Assessment Pathway:** standard

---

## Signal Score Summary

| Signal | Score | Band | Pathway |
|--------|-------|------|---------|
| Reproducibility | 68 | Good | standard |

**Cluster Rating:** Adequate

---

## Signal 6: Reproducibility

**Score:** 68/100 (Good)

**Pathway:** standard
**Approach anchors applied:** inductive

### Assessment

This archaeogenomic study has strong data archiving but lacks a dedicated code repository. The paper represents typical practice for Nature archaeogenomics publications: comprehensive data deposition with analytical workflows described in methods but without shared analysis scripts.

**Data availability is excellent.** All DNA sequences are deposited in the European Nucleotide Archive (ENA) under accession PRJEB62503 with public access. The data includes raw sequencing reads, allowing complete re-analysis from primary data. Machine actionability is high—the ENA accession enables programmatic data retrieval through standard bioinformatics APIs.

**Code availability is limited.** No dedicated code repository (e.g., GitHub, Zenodo) provides custom analysis scripts. The paper relies on established bioinformatics software packages (EAGER, ANGSD, ADMIXTOOLS/qpAdm, ancIBD, hapROH, GLIMPSE, DATES, HaploGrep, YMCA) with parameters documented in Methods and Supplementary Information. While this enables procedural reproduction, it requires researchers to implement workflows from method descriptions rather than execute shared scripts.

**Environment specification is partial.** Software versions are documented (e.g., EAGER v.1.92.37, GLIMPSE, ancIBD v.0.4, hapROH v.0.64), enabling environment reconstruction. However, no containerised environment (Docker, Singularity) or explicit dependency manifest is provided.

**Workflow documentation is good.** The Methods section and Supplementary Information provide detailed analytical parameters (e.g., DATES: binsize 0.001, maxdis 1, qbin 10, lovalfit 0.45; qpAdm rotating outgroups; IBD thresholds). A researcher with archaeogenomics expertise could reconstruct the analysis pipeline from these descriptions.

### Evidence

**From reproducibility_infrastructure:**

- Code availability: statement_present = false; no dedicated repository
- Data availability: statement_present = true; ENA PRJEB62503 (public access)
- Persistent identifiers: protocols.io references (bqd8ms9w, bqebmtan), GitHub stschiff/sequenceTools
- FAIR score: 14/16 (87.5%) - Findable: 4, Accessible: 4, Interoperable: 3, Reusable: 3

**From methods/protocols:**

- M001: "1,240,000 SNP capture enrichment" with documented parameters
- P001-P024: Detailed protocols for DNA extraction, sequencing, analysis
- Software versions documented throughout Methods section

**Strengths:**

- Primary data fully archived in ENA with public access
- Established software packages used with documented parameters
- Detailed methods enable procedural reconstruction
- protocols.io references for laboratory protocols

**Weaknesses:**

- No dedicated code repository for custom analysis scripts
- No containerised computational environment
- Workflow requires reconstruction from method descriptions

### Tool Assessment

| Aspect | Status | Tool Type | Impact |
|--------|--------|-----------|--------|
| DNA alignment | EAGER pipeline | open_scriptable | Positive - established open-source |
| Population genetics | ADMIXTOOLS/qpAdm | open_scriptable | Positive - established open-source |
| Statistical analysis | ANGSD, DATES | open_scriptable | Positive - established open-source |
| Kinship analysis | ancIBD, hapROH | open_scriptable | Positive - established open-source |
| Imputation | GLIMPSE | open_scriptable | Positive - established open-source |
| Custom scripts | Not shared | none | Negative - workflow reconstruction required |

### Scoring Rationale

Score of 68 reflects good reproducibility for inductive archaeogenomics. Data is archived with comprehensive documentation in ENA (meets 60-79 criterion for data archiving). Analysis workflow is documented with parameters (meets 60-79 for workflow documentation). Classification schemes (haplogroup assignment, ancestry modelling) are explicit (60-79). However, code is not shared—only parameter descriptions (prevents reaching 80-100 which requires analysis workflow documentation even if not automated). Raw observations (sequencing data) are accessible (60-79). Metadata is adequate (60-79). Does not reach Excellent band because custom scripts are not shared and workflow requires reconstruction.

---

## Reproducibility Readiness Checklist

```yaml
reproducibility_readiness:
  applies: true
  pathway: "standard"
  if_not_applicable_reason: ""

  inputs_available:
    status: "yes"
    details: "DNA sequences archived in ENA PRJEB62503 with public access. Raw sequencing reads enable complete re-analysis from primary data."

  code_available:
    status: "partial"
    tool_type: "open_scriptable"
    details: "Established software packages documented with versions and parameters. No custom analysis scripts shared. Workflow reconstruction required from method descriptions."

  environment_specified:
    status: "partial"
    details: "Software versions documented (EAGER v.1.92.37, ancIBD v.0.4, hapROH v.0.64, etc.). No containerised environment or dependency manifest provided."

  outputs_documented:
    status: "yes"
    details: "Expected outputs documented in figures, supplementary tables, and text. PCA coordinates, qpAdm coefficients, f-statistics, IBD segments, ROH tracts all specified."

  execution_feasibility: "needs_work"
  feasibility_rationale: "Data fully available for reproduction. Analytical workflow must be reconstructed from method descriptions and parameter specifications. Experienced archaeogenomicist could reproduce analyses, but requires significant implementation effort."

  publication_year: 2023
  adoption_context: "early_majority"
```

---

## Cluster Synthesis

**Overall Reproducibility:** Adequate

The paper demonstrates adequate reproducibility infrastructure for 2023 archaeogenomics. Data archiving in ENA is excellent and represents best practice for the field. The absence of a dedicated code repository is the primary limitation, placing this paper in the majority of archaeogenomic publications that document analytical workflows in methods sections rather than sharing executable scripts. This is not a deficiency relative to field norms but does limit reproducibility compared to emerging best practices.

### Chronological Context

Publication year 2023 places this paper in the **early_majority** era of reproducibility adoption. Data sharing in domain repositories (ENA for sequence data) is established practice. Code sharing is emerging but not yet standard for Nature archaeogenomics papers. The paper meets field expectations for its publication venue and era.

### Gateway Assessment

**Execution Feasibility:** needs_work

This paper could be queued for reproduction with preparation:

**What would be needed:**

1. Download data from ENA PRJEB62503
2. Install documented software packages (EAGER, ADMIXTOOLS, ANGSD, ancIBD, hapROH, GLIMPSE, DATES)
3. Reconstruct analysis pipeline from Methods and Supplementary Information
4. Apply documented parameters to each analytical step
5. Compare outputs to published figures and supplementary tables

**Estimated effort:** Moderate-to-high. Experienced archaeogenomicist (familiar with standard tools) could reproduce core analyses in 2-4 weeks. Population genetics analyses (qpAdm, f-statistics) are most tractable; kinship and admixture timing analyses require more parameter matching.

**Not feasible without:** Access to 1000 Genomes reference panel for GLIMPSE imputation; computational resources for large-scale population genetics analysis.

---

## Structured Output

```yaml
cluster_3_reproducibility:
  paper_slug: "penske-et-al-2023"
  assessment_date: "2025-12-02"
  quality_state: "high"
  research_approach: "inductive"
  pathway: "standard"
  experimental: false

  reproducibility:
    score: 68
    band: "good"
    strengths:
      - "Primary data fully archived in ENA (PRJEB62503) with public access"
      - "Established open-source software packages used throughout"
      - "Detailed parameter documentation in Methods and Supplementary Information"
      - "protocols.io references for laboratory protocols"
    weaknesses:
      - "No dedicated code repository for custom analysis scripts"
      - "No containerised computational environment"
      - "Workflow requires reconstruction from method descriptions"
    rationale: "Good reproducibility for inductive archaeogenomics. Data archived with documentation, workflow documented with parameters, but code not shared. Meets field norms but does not reach best practices for computational reproducibility."
    tool_assessment:
      primary_tool_type: "open_scriptable"
      tool_impact: "Positive - all core tools are open-source (EAGER, ADMIXTOOLS, ANGSD, ancIBD, hapROH). Impact reduced by absence of shared analysis scripts."

  reproducibility_readiness:
    applies: true
    pathway: "standard"
    inputs_available:
      status: "yes"
      details: "DNA sequences in ENA PRJEB62503, public access, machine actionable"
    code_available:
      status: "partial"
      tool_type: "open_scriptable"
      details: "Established packages documented; no custom scripts shared"
    environment_specified:
      status: "partial"
      details: "Software versions documented; no containerised environment"
    outputs_documented:
      status: "yes"
      details: "Results documented in figures, tables, and supplementary materials"
    execution_feasibility: "needs_work"
    feasibility_rationale: "Data available; workflow reconstruction required from method descriptions"
    publication_year: 2023
    adoption_context: "early_majority"

  cluster_synthesis:
    overall_rating: "adequate"
    chronological_interpretation: "Meets 2023 field expectations for Nature archaeogenomics. Data sharing excellent; code sharing not yet standard practice."
    gateway_recommendation: "Reproducible with effort. Experienced archaeogenomicist could reproduce core analyses in 2-4 weeks by reconstructing pipeline from documented parameters."
```
