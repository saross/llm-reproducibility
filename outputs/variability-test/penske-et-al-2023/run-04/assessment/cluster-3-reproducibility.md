# Cluster 3: Reproducibility Assessment

**Paper:** penske-et-al-2023
**Assessment Date:** 2025-12-02
**Run:** run-04 (variability test)
**Assessor Version:** v1.0

**Quality State:** HIGH
**Research Approach:** inductive (confidence: high)
**Paper Type:** empirical
**Assessment Pathway:** standard

---

## Signal Score Summary

| Signal | Score | Band | Pathway |
|--------|-------|------|---------|
| Reproducibility | 73 | Good | standard |

**Cluster Rating:** Adequate

---

## Signal 6: Reproducibility

**Score:** 73/100 (Good)

**Pathway:** standard
**Approach anchors applied:** inductive

### Assessment

This archaeogenomics paper has substantial computational components warranting standard reproducibility assessment. The analytical workflow encompasses DNA sequence processing, quality filtering, SNP calling, and multiple population genetics analyses (PCA, f-statistics, qpAdm ancestry modelling, IBD detection, ROH analysis).

**Data availability** is excellent. Raw DNA sequences are deposited in the European Nucleotide Archive (ENA) under accession PRJEB62503 with open access. This domain-specific repository provides structured metadata, programmatic API access, and persistent identifiers. The FAIR assessment score of 14/15 (93.3%) reflects strong compliance with open science standards.

**Code availability** is limited. No custom code repository is provided. However, all analyses employ established published software packages with version numbers documented in Methods: EAGER pipeline for ancient DNA processing, EIGENSOFT for PCA, ADMIXTOOLS for f-statistics and qpAdm, ancIBD for Identity-by-Descent analysis, and hapROH for Runs of Homozygosity. These packages are open-source and well-documented, enabling analytical pipeline reconstruction.

**Environment specification** is partial. Software versions are mentioned throughout Methods and Supplementary Information, but complete computational environment details (operating system, library dependencies, hardware specifications) are not provided. The analysis likely requires High Performance Computing (HPC) resources for sequence processing.

**Workflow documentation** is thorough in Methods and Supplementary Information but not automated as a reproducible pipeline (e.g., Snakemake, Nextflow). Parameter specifications appear in protocol descriptions (P01-P24).

### Evidence

**From reproducibility_infrastructure:**
- Data availability: statement_present = true; ENA PRJEB62503 (open access)
- Code availability: statement_present = false; relies on published software packages
- FAIR score: 14/15 (93.3%) — highly_fair rating
- PID connectivity: moderate (2/6) — paper DOI and dataset accession present

**From methods/protocols:**
- P18: "EAGER pipeline for ancient DNA sequence processing" — documented bioinformatics workflow
- M03: "PCA projection using EIGENSOFT" — standard tool with parameters
- M04-M05: "qpAdm ancestry modelling with ADMIXTOOLS" — version specified
- P19-P22: DNA extraction and library preparation protocols with references

**Strengths:**
- Data archived in major domain repository (ENA) with open access
- All primary analytical software packages are open source
- Software versions specified throughout Methods section
- FAIR compliance excellent (93.3%)
- Supplementary tables provide detailed parameter documentation

**Weaknesses:**
- No custom code repository or analysis scripts provided
- Computational environment specification incomplete
- Workflow not automated as reproducible pipeline
- Reference dataset assembly process not fully documented

### Tool Assessment

| Aspect | Software | Tool Type | Impact |
|--------|----------|-----------|--------|
| DNA processing | EAGER pipeline | open_scriptable | No demerit |
| PCA | EIGENSOFT/smartpca | open_scriptable | No demerit |
| f-statistics | ADMIXTOOLS | open_scriptable | No demerit |
| qpAdm modelling | ADMIXTOOLS | open_scriptable | No demerit |
| IBD detection | ancIBD | open_scriptable | No demerit |
| ROH analysis | hapROH | open_scriptable | No demerit |
| DATES | DATES | open_scriptable | No demerit |

### Scoring Rationale

Score: 73 (Good for inductive). Data archived in domain repository with excellent documentation (60-79 criterion met). Workflow documented in Methods but not automated (60-79). Procedures explicit through detailed protocol descriptions (60-79). Raw data accessible via ENA with open access (60-79). Metadata comprehensive through supplementary tables (60-79). FAIR score 93.3% meets high standard (60-79). Would require automated pipeline and complete environment specification for 80-100 band.

---

## Reproducibility Readiness Checklist

```yaml
reproducibility_readiness:
  applies: true
  pathway: "standard"
  if_not_applicable_reason: ""

  inputs_available:
    status: "yes"
    details: "Raw DNA sequences deposited in ENA under PRJEB62503 with open access. Supplementary tables provide sample metadata, archaeological context, radiocarbon dates, and analytical parameters. 1.24M SNP panel data available."

  code_available:
    status: "partial"
    tool_type: "open_scriptable"
    details: "No custom code repository provided. Analysis uses published open-source packages (EAGER, EIGENSOFT, ADMIXTOOLS, ancIBD, hapROH) with versions specified. Pipeline reconstruction possible from Methods and Supplementary Information."

  environment_specified:
    status: "partial"
    details: "Software versions mentioned but complete computational environment not documented. Operating system, library dependencies, and hardware specifications not provided. Analysis likely requires HPC resources."

  outputs_documented:
    status: "yes"
    details: "Expected outputs documented in Results, Figures 1-4, Extended Data Figures 1-9, and Supplementary Tables A-Y. PCA coordinates, f-statistics, qpAdm ancestry proportions, IBD segments, and ROH lengths reported with values."

  execution_feasibility: "needs_work"
  feasibility_rationale: "Data accessible and methods comprehensively documented. Would require reconstructing analytical pipeline from Methods text and supplementary materials. All software packages available and open-source. Reproducibility achievable with moderate effort by experienced archaeogenomicist with HPC access."

  publication_year: 2023
  adoption_context: "early_majority"
```

---

## Cluster Synthesis

**Overall Reproducibility:** Adequate

The paper demonstrates good reproducibility infrastructure for a 2023 Nature archaeogenomics publication. Data sharing through ENA is exemplary and meets current genomics community standards. The primary limitation is absence of a custom code repository, which is increasingly expected but not yet mandatory.

### Chronological Context

Publication year 2023 places this paper in the **early_majority** era of reproducibility adoption in genomics. By 2023:
- Data deposition in domain repositories (ENA, SRA) is standard practice — reflected in excellent data availability
- Code sharing is increasingly expected but not universally implemented — reflected in code availability gap
- FAIR principles are well-established — reflected in 93.3% FAIR score
- Automated reproducible pipelines (Snakemake, Nextflow) are emerging best practice — gap present

The 73/100 score reflects good-but-not-exemplary practice for this publication era. The paper exceeds minimum requirements while falling short of emerging best practices.

### Gateway Assessment

**Execution Feasibility:** needs_work

This paper could be queued for analytical reproducibility verification with moderate preparation effort.

**What would be needed:**
1. Download raw sequences from ENA PRJEB62503 (publicly accessible)
2. Obtain reference population data (Allen Ancient DNA Resource, published datasets)
3. Install documented software packages (EAGER, EIGENSOFT, ADMIXTOOLS, ancIBD, hapROH)
4. Reconstruct analytical pipeline from Methods and Supplementary Information
5. Process sequences through alignment, quality filtering, and SNP calling
6. Execute population genetics analyses with documented parameters
7. Compare outputs to published results (PCA positions, f-statistics, qpAdm proportions)

**Gaps requiring attention:**
- No automated pipeline — requires manual workflow reconstruction
- Environment specification incomplete — may require dependency troubleshooting
- Reference dataset assembly not fully documented — would need consultation of cited publications
- HPC resources needed for sequence processing

**Estimated effort:** Substantial but feasible for experienced archaeogenomicist or bioinformatician with access to HPC infrastructure and familiarity with ancient DNA analysis pipelines.

---

## Structured Output

```yaml
cluster_3_reproducibility:
  paper_slug: "penske-et-al-2023"
  run: "run-04"
  assessment_date: "2025-12-02"
  quality_state: "high"
  research_approach: "inductive"
  pathway: "standard"
  experimental: false

  reproducibility:
    score: 73
    band: "good"
    strengths:
      - "Data archived in ENA with open access (PRJEB62503)"
      - "All primary analytical packages are open source"
      - "Software versions documented throughout Methods"
      - "FAIR score 93.3% (14/15) — highly FAIR"
      - "Comprehensive supplementary documentation"
    weaknesses:
      - "No custom code repository provided"
      - "Computational environment specification incomplete"
      - "Workflow not automated as reproducible pipeline"
    rationale: "Good for inductive. Data archived and accessible, workflow documented but not automated, all tools open-source. Would need code repository and environment spec for excellent."
    tool_assessment:
      primary_tool_type: "open_scriptable"
      tool_impact: "No demerit — all primary tools are open source"

  reproducibility_readiness:
    applies: true
    pathway: "standard"
    inputs_available:
      status: "yes"
      details: "ENA PRJEB62503 with open access; comprehensive supplementary metadata"
    code_available:
      status: "partial"
      tool_type: "open_scriptable"
      details: "No custom repository; published packages with documented versions"
    environment_specified:
      status: "partial"
      details: "Software versions mentioned; complete environment not documented"
    outputs_documented:
      status: "yes"
      details: "Results, figures, extended data, supplementary tables document expected outputs"
    execution_feasibility: "needs_work"
    feasibility_rationale: "Data accessible, methods documented, pipeline reconstruction required"
    publication_year: 2023
    adoption_context: "early_majority"

  cluster_synthesis:
    overall_rating: "adequate"
    chronological_interpretation: "Good practice for 2023 early_majority era. Data sharing exemplary; code sharing gap reflects evolving field norms."
    gateway_recommendation: "Queuing for reproduction feasible with moderate preparation. Requires pipeline reconstruction from Methods."
```
