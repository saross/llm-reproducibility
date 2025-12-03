# Cluster 3: Reproducibility Assessment

**Paper:** penske-et-al-2023
**Assessment Date:** 2025-12-01
**Assessor Version:** v1.0

**Quality State:** HIGH
**Research Approach:** empirical_quantitative (confidence: high)
**Paper Type:** research article
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
**Approach anchors applied:** deductive

### Assessment

The paper demonstrates good analytical reproducibility potential, with excellent data sharing but incomplete code documentation. This is a computational paper requiring standard reproducibility assessment: the analysis involves statistical methods (PCA, qpAdm, f-statistics) and computational workflows (EAGER pipeline, ADMIXTOOLS) that can in principle be re-executed.

**Input availability** is excellent. Raw sequence data are deposited in the European Nucleotide Archive (ENA) under accession PRJEB62503 with open access conditions. This enables complete technical reproduction of the data processing pipeline from raw reads. Additionally, genotype data are integrated into the Allen Ancient DNA Resource (AADR v44.3), facilitating comparison with published datasets using standard formats.

**Code availability** is the main gap. The paper specifies software versions (EAGER v1.92.56, ADMIXTOOLS v5.1, smartpca v16000, GLIMPSE v1.0.1, ancIBD v0.4, hapROH v0.64, DATES v753, HOPS v0.2) but does not provide a code repository with analysis scripts. This means that while the tools are known, the exact parameters, configurations, and workflow sequences used are not fully documented. Reproducing the analysis would require reconstructing the pipeline from the methods section.

**Environment specification** is partial. Software versions are listed, which is a significant positive for archaeogenetics where tool versions can substantially affect results. However, computational environment details (operating system, library versions, container specifications) are not provided.

**Output documentation** is good. Supplementary Tables A-Y provide detailed intermediate and final results, enabling verification of reproduced outputs against published values. The use of standard metrics (f-statistics, P-values) with documented thresholds facilitates comparison.

### Evidence

**From reproducibility_infrastructure:**
- Data availability: YES — ENA accession PRJEB62503, open access, raw sequences available
- Code availability: NO — No custom repository; standard tools with versions specified but no scripts
- Persistent identifiers: Paper DOI 10.1038/s41586-023-06334-8; 5 protocols.io DOIs for laboratory methods
- FAIR score: 35/40 (Findable 9/10, Accessible 10/10, Interoperable 8/10, Reusable 8/10)

**From methods/protocols:**
- M001: Laboratory procedures documented with facility identification (MPI-EVA Leipzig/Jena)
- M004: PCA methodology specified including reference dataset (1,253 modern West Eurasians)
- M005: qpAdm analysis documented with software version (ADMIXTOOLS v5.1) and acceptance threshold (P > 0.05)

**Strengths:**
- Raw sequence data publicly available with persistent identifier
- All software tools identified with specific version numbers
- Standard archaeogenetics tools enable method reproduction by experienced practitioners
- 5 protocols.io DOIs provide detailed laboratory procedure documentation
- AADR integration facilitates comparative analysis

**Weaknesses:**
- No analysis code repository provided
- Custom scripts and configurations not shared
- Computational environment not fully specified
- Pipeline workflow sequences must be inferred from text

### Tool Assessment

| Aspect | Status | Tool Type | Impact |
|--------|--------|-----------|--------|
| Sequencing pipeline | EAGER v1.92.56 | open_scriptable | Minimal demerit — standard tool |
| Population genetics | ADMIXTOOLS v5.1 | open_scriptable | Minimal demerit — standard tool |
| PCA | smartpca v16000 | open_scriptable | Minimal demerit — standard tool |
| Imputation | GLIMPSE v1.0.1 | open_scriptable | Minimal demerit — standard tool |
| IBD/ROH analysis | ancIBD/hapROH | open_scriptable | Minimal demerit — standard tools |
| Custom analysis scripts | Not available | none | Significant demerit — workflow reconstruction required |

### Scoring Rationale

Score of 68 (Good for deductive) reflects: data available via ENA with persistent identifier (strong positive); code not shared but standard tools with versions specified (moderate limitation); workflow partially documented but exact configurations unknown; most outputs reproducible using standard tools with effort; FAIR score 35/40. Does not reach 80-100 due to absence of code repository preventing immediate analytical reproduction. Above 60 due to excellent data sharing and use of well-documented standard tools.

---

## Reproducibility Readiness Checklist

```yaml
reproducibility_readiness:
  applies: true
  pathway: "standard"
  if_not_applicable_reason: ""

  inputs_available:
    status: "yes"
    details: "Raw sequence data deposited in ENA (PRJEB62503) with open access. Genotype data in AADR v44.3. 113 radiocarbon dates in supplementary materials."

  code_available:
    status: "partial"
    tool_type: "open_scriptable"
    details: "Standard archaeogenetics tools specified with versions (EAGER, ADMIXTOOLS, smartpca, GLIMPSE, ancIBD, hapROH, DATES, HOPS). No custom analysis scripts or configuration files shared."

  environment_specified:
    status: "partial"
    details: "Software versions specified. Computational facility identified (MPI-EVA). No container/environment files, OS details, or library dependencies documented."

  outputs_documented:
    status: "yes"
    details: "Supplementary Tables A-Y contain sample statistics, ancestry proportions, f-statistics, dates, and other intermediate/final outputs. Standard metrics with documented thresholds enable verification."

  execution_feasibility: "needs_work"
  feasibility_rationale: "Data fully available. Standard tools documented with versions. However, reproducing the analysis requires: (1) reconstructing pipeline workflow from methods text, (2) inferring qpAdm parameters and reference population configurations, (3) recreating quality filtering steps. Experienced archaeogeneticist could reproduce with moderate effort."

  publication_year: 2023
  adoption_context: "early_majority"
```

---

## Cluster Synthesis

**Overall Reproducibility:** Adequate

The paper demonstrates adequate reproducibility, with a score in the "Good" band but below the threshold for "Strong" cluster rating due to the code availability gap. The combination of excellent data sharing and incomplete code documentation is a common pattern in archaeogenetics publications.

### Chronological Context

Publication year 2023 places this paper in the **early_majority** era of reproducibility adoption. In this context, the reproducibility practices demonstrated are typical for high-impact archaeogenetics publications: comprehensive data deposition is now expected, but code sharing remains inconsistent. The paper meets disciplinary standards but does not exceed them.

By current (2023-2025) best practices, the absence of a code repository is a notable gap. However, the extensive use of standard, well-documented tools (ADMIXTOOLS, EAGER) partially mitigates this limitation, as experienced practitioners can reconstruct the analysis workflow.

### Gateway Assessment

**Execution Feasibility:** needs_work

This paper could potentially be queued for a reproduction attempt, but would require preparatory work:

**What would be needed:**
1. **Pipeline reconstruction:** Create analysis workflow from methods section, supplementary materials, and archaeogenetics conventions
2. **Parameter inference:** Determine qpAdm reference population sets and quality thresholds from supplementary tables
3. **Environment setup:** Configure computational environment with specified software versions
4. **Validation:** Use supplementary table outputs as verification checkpoints

**Estimated effort:** Moderate (experienced archaeogeneticist: 2-4 weeks; non-specialist: substantial additional learning)

**Confidence in reproduction success:** Moderate-high for main findings. The use of standard tools and availability of intermediate outputs suggest that principal results could be reproduced, though exact numerical values may vary with parameter choices.

---

## Structured Output

```yaml
cluster_3_reproducibility:
  paper_slug: "penske-et-al-2023"
  assessment_date: "2025-12-01"
  quality_state: "HIGH"
  research_approach: "empirical_quantitative"
  pathway: "standard"
  experimental: false

  reproducibility:
    score: 68
    band: "good"
    strengths:
      - "Raw data available in ENA with persistent identifier (PRJEB62503)"
      - "All software tools specified with version numbers"
      - "Standard archaeogenetics tools enable reproduction by practitioners"
      - "Supplementary outputs enable verification"
      - "FAIR score 35/40"
    weaknesses:
      - "No code repository for analysis scripts"
      - "Pipeline configurations must be inferred"
      - "Computational environment not fully specified"
    rationale: "Score of 68 reflects excellent data sharing with code availability gap; standard tools documented but workflow reconstruction required for reproduction."
    tool_assessment:
      primary_tool_type: "open_scriptable"
      tool_impact: "Minimal demerit for standard tools; significant demerit for absent custom scripts"

  reproducibility_readiness:
    applies: true
    pathway: "standard"
    inputs_available:
      status: "yes"
      details: "ENA PRJEB62503 open access; AADR v44.3 integration"
    code_available:
      status: "partial"
      tool_type: "open_scriptable"
      details: "Standard tools with versions; no custom scripts"
    environment_specified:
      status: "partial"
      details: "Software versions listed; no environment files"
    outputs_documented:
      status: "yes"
      details: "Supplementary Tables A-Y with intermediate outputs"
    execution_feasibility: "needs_work"
    feasibility_rationale: "Pipeline reconstruction required; moderate effort for experienced practitioner"
    publication_year: 2023
    adoption_context: "early_majority"

  cluster_synthesis:
    overall_rating: "adequate"
    chronological_interpretation: "Meets 2023 archaeogenetics standards for data sharing; code sharing gap reflects field norms rather than paper-specific deficiency"
    gateway_recommendation: "Reproduction feasible with moderate preparatory work; prioritise if validation of archaeogenetics workflows is a research goal"
```
