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
| Reproducibility | 72 | Good | standard |

**Cluster Rating:** Adequate

---

## Signal 6: Reproducibility

**Score:** 72/100 (Good)

**Pathway:** standard
**Approach anchors applied:** inductive

### Assessment

This paper has substantial computational components (PCA, f-statistics, qpAdm modelling, IBD analysis, ROH analysis) making standard reproducibility assessment appropriate. Data availability is excellent: raw DNA sequences are deposited in the European Nucleotide Archive under accession PRJEB62503 with open access.

Code availability is limited: no custom code repository is provided. However, all analyses use established published software packages with version numbers specified in the Methods section. The primary analytical tools (EAGER pipeline, ANGSD, EIGENSOFT, ADMIXTOOLS) are open-source and well-documented. This means analytical reproducibility is achievable through reconstructing the pipeline from documented parameters.

Environment specification is partial: software versions are mentioned (e.g., EAGER v2, ANGSD, EIGENSOFT) but complete computational environment (operating system, dependencies) is not provided. Workflow documentation is detailed in Methods and Supplementary Information but not automated as a reproducible pipeline.

FAIR assessment: 35/40 (87.5%) reflecting strong findability, accessibility, interoperability, and reusability. The main gap is absence of custom code DOI.

### Evidence

**From reproducibility_infrastructure:**
- Code availability: statement_present = false; no custom repository
- Data availability: statement_present = true; ENA PRJEB62503 (open access)
- Persistent identifiers: paper DOI 10.1038/s41586-023-06334-8; project ID PRJEB62503
- FAIR score: 35/40 (87.5%)

**From methods/protocols:**
- P007: "EIGENSOFT smartpca version 16000" — software version specified
- P001-P004: DNA extraction and library preparation protocols referenced
- M003-M010: Statistical methods documented with parameters

**Strengths:**
- Data archived in major repository (ENA) with open access
- All primary software packages are open source
- Software versions specified throughout Methods
- FAIR compliance strong (87.5%)

**Weaknesses:**
- No custom code repository or analysis scripts
- Environment specification incomplete
- Workflow not automated as reproducible pipeline

### Tool Assessment

| Aspect | Status | Tool Type | Impact |
|--------|--------|-----------|--------|
| DNA processing | EAGER pipeline | open_scriptable | No demerit |
| PCA | EIGENSOFT | open_scriptable | No demerit |
| f-statistics | ADMIXTOOLS | open_scriptable | No demerit |
| qpAdm | ADMIXTOOLS | open_scriptable | No demerit |
| IBD analysis | Published packages | open_scriptable | No demerit |

### Scoring Rationale

Score: 72 (Good for inductive). Data archived with documentation (60-79). Workflow documented but not automated (60-79). Procedures explicit through Methods section (60-79). Raw data accessible via ENA (60-79). Metadata adequate through supplementary tables. FAIR mostly met (87.5%). Would need automated pipeline and complete environment specification for 80-100.

---

## Reproducibility Readiness Checklist

```yaml
reproducibility_readiness:
  applies: true
  pathway: "standard"
  if_not_applicable_reason: ""

  inputs_available:
    status: "yes"
    details: "Raw DNA sequences deposited in ENA under PRJEB62503 with open access. Supplementary tables provide sample metadata, archaeological context, and analytical parameters."

  code_available:
    status: "partial"
    tool_type: "open_scriptable"
    details: "No custom code repository. Analysis uses published open-source packages (EAGER, EIGENSOFT, ADMIXTOOLS) with versions specified. Pipeline reconstruction possible from Methods documentation."

  environment_specified:
    status: "partial"
    details: "Software versions mentioned but complete computational environment not documented. Operating system and dependency versions not specified."

  outputs_documented:
    status: "yes"
    details: "Expected outputs documented in Results, figures, and supplementary tables. PCA coordinates, f-statistics, qpAdm proportions, and IBD segments reported with values."

  execution_feasibility: "needs_work"
  feasibility_rationale: "Data accessible and methods documented, but would require reconstructing analytical pipeline from Methods text. Software packages available. Reproducibility achievable with moderate effort by experienced archaeogenomicist."

  publication_year: 2023
  adoption_context: "early_majority"
```

---

## Cluster Synthesis

**Overall Reproducibility:** Adequate

The paper demonstrates good reproducibility infrastructure for a 2023 archaeogenomics publication. Data sharing in ENA is exemplary. The main limitation is absence of a custom code repository, which is increasingly expected but not yet universal in the field.

### Chronological Context

Publication year 2023 places this paper in the **early_majority** era of reproducibility adoption. By 2023, data sharing in repositories is well-established in genomics (reflected in ENA deposition). Code sharing is increasingly expected but not yet mandatory at Nature. The 72/100 score reflects good-but-not-exemplary practice for this era.

### Gateway Assessment

**Execution Feasibility:** needs_work

This paper could be queued for analytical reproducibility verification with moderate preparation effort:

**What would be needed:**
1. Download raw sequences from ENA PRJEB62503
2. Install documented software packages (EAGER, EIGENSOFT, ADMIXTOOLS)
3. Reconstruct analytical pipeline from Methods section
4. Process data through DNA alignment and SNP calling
5. Run population genetics analyses with documented parameters
6. Compare outputs to published results

**Gaps to address:**
- No automated pipeline script — would need manual reconstruction
- Environment specification incomplete — may require version troubleshooting
- Reference dataset preparation not fully documented

**Estimated effort:** Substantial but feasible for experienced archaeogenomicist with access to HPC resources for sequence processing.

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
    score: 72
    band: "good"
    strengths:
      - "Data archived in ENA with open access (PRJEB62503)"
      - "All primary software packages are open source"
      - "Software versions specified in Methods"
      - "FAIR score 87.5% (35/40)"
    weaknesses:
      - "No custom code repository"
      - "Environment specification incomplete"
      - "Pipeline not automated"
    rationale: "Good for inductive. Data archived and accessible, workflow documented but not automated, open-source tools used. Would need code repository for excellent."
    tool_assessment:
      primary_tool_type: "open_scriptable"
      tool_impact: "No demerit — all primary tools are open source"

  reproducibility_readiness:
    applies: true
    pathway: "standard"
    inputs_available:
      status: "yes"
      details: "ENA PRJEB62503 with open access; supplementary metadata"
    code_available:
      status: "partial"
      tool_type: "open_scriptable"
      details: "No custom repository; uses published packages with versions"
    environment_specified:
      status: "partial"
      details: "Software versions mentioned; complete environment not documented"
    outputs_documented:
      status: "yes"
      details: "Results, figures, supplementary tables document expected outputs"
    execution_feasibility: "needs_work"
    feasibility_rationale: "Data accessible, methods documented, pipeline reconstruction required"
    publication_year: 2023
    adoption_context: "early_majority"

  cluster_synthesis:
    overall_rating: "adequate"
    chronological_interpretation: "Good practice for 2023 early_majority era. Data sharing exemplary; code sharing gap reflects evolving norms."
    gateway_recommendation: "Queuing for reproduction feasible with moderate preparation. Requires pipeline reconstruction from Methods."
```
