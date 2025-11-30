# Cluster 3: Reproducibility Assessment

**Paper:** penske-et-al-2023
**Assessment Date:** 2025-11-30
**Assessor Version:** v1.0

**Quality State:** HIGH
**Research Approach:** Inductive (confidence: medium)
**Paper Type:** Empirical
**Assessment Pathway:** Standard

---

## Signal Score Summary

| Signal | Score | Band | Pathway |
|--------|-------|------|---------|
| Reproducibility | 72 | Good | Standard |

**Cluster Rating:** Adequate

---

## Signal 6: Reproducibility

**Score:** 72/100 (Good)

**Pathway:** Standard
**Approach anchors applied:** Inductive

### Assessment

This paper demonstrates good computational reproducibility with excellent data archiving but missing code availability. The analytical workflow involves substantial computational analysis: ancient DNA processing, population genetic statistics, and admixture modelling - all reproducible in principle but dependent on accessing or recreating analytical scripts.

**Data archiving** is exemplary. DNA sequences are deposited in the European Nucleotide Archive (PRJEB62503) with open access. The Allen Ancient DNA Resource (AADR) provides comparative genotype data in standardised formats. Machine actionability is rated "high" for data - ENA provides API access and structured metadata.

**Code availability** is absent. No code repository is mentioned despite extensive computational analysis. The paper lists software tools (EAGER, AdapterRemoval, BWA, DeDup, mapDamage, ADMIXTOOLS, etc.) but custom analysis scripts - which would be needed to exactly reproduce the specific analyses - are not shared. This represents the key reproducibility gap.

**Workflow documentation** is comprehensive. The 35 protocols document analytical procedures in detail, enabling a skilled practitioner to approximate the analysis using the identified tools. However, exact reproduction would require either obtaining scripts from authors or recreating them from protocol descriptions.

### Evidence

**From reproducibility_infrastructure:**
- Code availability: **No** — No repository, software tools listed but scripts not shared
- Data availability: **Yes** — ENA (PRJEB62503), open access, machine-actionable
- Persistent identifiers: Paper DOI, ENA accession
- FAIR score: 13/16 (81%) — highly FAIR

**From methods/protocols:**
- P010: "smartpca from EIGENSOFT package" - tool identified but parameters would need extraction
- P034: "mergeit to merge datasets" - standard tool but specific parameters not preserved
- 35 protocols provide substantial procedural detail

**Strengths:**
- Excellent data archiving (ENA PRJEB62503)
- AADR reference data accessible
- FAIR score of 81%
- 35 protocols document analytical procedures
- Standard tools identified (ADMIXTOOLS, EIGENSOFT, etc.)

**Weaknesses:**
- No code repository
- Custom analysis scripts not shared
- Exact parameters for analyses may require author contact
- Environment specification implicit in tool versions

### Tool Assessment

| Aspect | Status | Tool Type | Impact |
|--------|--------|-----------|--------|
| DNA processing | EAGER, AdapterRemoval, BWA | open_scriptable | Ideal |
| Population genetics | ADMIXTOOLS, EIGENSOFT | open_scriptable | Ideal |
| Custom analysis | Not shared | unknown | Significant gap |
| Visualisation | Not specified | unknown | Minor gap |

### Scoring Rationale

Score of 72 (Good) reflects: data archived with comprehensive documentation (80-100 for data); workflow documented through 35 protocols (60-79); procedures explicit and could be approximated; raw data accessible. Gap from Excellent due to: no code repository, custom scripts not shared, exact reproduction requires author contact or script recreation.

---

## Reproducibility Readiness Checklist

```yaml
reproducibility_readiness:
  applies: true
  pathway: "standard"
  if_not_applicable_reason: ""

  inputs_available:
    status: "yes"
    details: "DNA sequences in ENA (PRJEB62503), open access. AADR reference data available. Raw sequence data sufficient for complete analytical reproduction."

  code_available:
    status: "no"
    tool_type: "open_scriptable"
    details: "Software tools identified (ADMIXTOOLS, EIGENSOFT, EAGER) but custom analysis scripts not shared. No code repository. Would need to recreate scripts from protocol descriptions or contact authors."

  environment_specified:
    status: "partial"
    details: "Tool names and versions partially specified. No environment file (conda, docker). Reproducers would need to infer compatible versions."

  outputs_documented:
    status: "yes"
    details: "PCA coordinates, f-statistics, qpAdm coefficients, ROH values all documented. Tables in supplementary materials provide expected outputs for verification."

  execution_feasibility: "needs_work"
  feasibility_rationale: "Data fully available and accessible. Analytical reproduction feasible but requires recreating analysis scripts from protocol descriptions. A skilled ancient DNA analyst could reproduce main findings using documented methods and available data. Exact reproduction blocked by missing code."

  publication_year: 2023
  adoption_context: "early_majority"
```

---

## Cluster Synthesis

**Overall Reproducibility:** Adequate

The paper demonstrates adequate reproducibility with asymmetric infrastructure: excellent data archiving but no code sharing. This pattern is common in archaeogenetics where domain-specific repositories (ENA) are well-established for data but code sharing practices are less consistent.

The data availability meets the highest standards: ENA deposit with standardised formats, open access, and machine-actionable metadata. Any researcher with access to standard ancient DNA analysis tools could work with this data.

However, exact computational reproduction is limited by the code gap. While the 35 protocols provide sufficient detail for an expert to approximate the analysis, recreating specific scripts would require substantial effort. The paper identifies all software tools used, but specific parameter choices and custom processing steps are not preserved in shareable code form.

### Chronological Context

Publication year 2023 places this paper in the **early majority** era of reproducibility adoption. For a Nature paper, data sharing meets contemporary expectations (ENA deposit is standard). Code sharing is increasingly expected in 2023 but not yet universal in archaeogenetics. The absence of a code repository is a gap relative to emerging best practice but reflects current field norms.

### Gateway Assessment

**Execution Feasibility:** needs_work

This paper could be queued for analytical reproduction with the following prerequisites:

**Available now:**
- Raw sequence data (ENA PRJEB62503)
- Reference panel (AADR)
- Comprehensive protocol documentation (35 protocols)
- Expected outputs for verification (supplementary tables)

**Gaps to address:**
1. **Critical:** Analysis scripts - would need recreation from protocols or author contact
2. **Moderate:** Exact software versions - would need to infer compatible environments
3. **Minor:** Visualisation code - could recreate from figure descriptions

**Recommendation:** Suitable for data-level reproduction and approximated analytical reproduction by domain experts. Not suitable for exact computational reproduction without additional materials from authors.

---

## Structured Output

```yaml
cluster_3_reproducibility:
  paper_slug: "penske-et-al-2023"
  assessment_date: "2025-11-30"
  quality_state: "high"
  research_approach: "inductive"
  pathway: "standard"
  experimental: false

  reproducibility:
    score: 72
    band: "good"
    strengths:
      - "Excellent data archiving (ENA PRJEB62503)"
      - "FAIR score 81%"
      - "35 protocols document analytical procedures"
      - "Standard tools identified"
    weaknesses:
      - "No code repository"
      - "Custom analysis scripts not shared"
      - "Exact parameters require author contact"
    rationale: "Good reproducibility with excellent data but missing code. Gap from Excellent due to code availability."
    tool_assessment:
      primary_tool_type: "open_scriptable"
      tool_impact: "Ideal tools used but scripts not shared"

  reproducibility_readiness:
    applies: true
    pathway: "standard"
    inputs_available:
      status: "yes"
      details: "ENA PRJEB62503, AADR reference data"
    code_available:
      status: "no"
      tool_type: "open_scriptable"
      details: "Tools identified but scripts not shared"
    environment_specified:
      status: "partial"
      details: "Tool versions partially specified, no environment file"
    outputs_documented:
      status: "yes"
      details: "Supplementary tables provide expected outputs"
    execution_feasibility: "needs_work"
    feasibility_rationale: "Data available; analytical reproduction requires script recreation"
    publication_year: 2023
    adoption_context: "early_majority"

  cluster_synthesis:
    overall_rating: "adequate"
    chronological_interpretation: "2023 Nature paper meets data sharing expectations; code gap reflects field norms"
    gateway_recommendation: "Suitable for approximated reproduction by domain experts; exact reproduction blocked by code gap"
```
