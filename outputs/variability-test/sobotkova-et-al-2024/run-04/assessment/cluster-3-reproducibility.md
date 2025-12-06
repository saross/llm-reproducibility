# Cluster 3: Reproducibility Assessment

**Paper:** sobotkova-et-al-2024
**Assessment Date:** 2025-12-05
**Assessor Version:** v1.0

**Quality State:** HIGH
**Research Approach:** Deductive (confidence: high)
**Paper Type:** Empirical
**Assessment Pathway:** standard

---

## Signal Score Summary

| Signal | Score | Band | Pathway |
|--------|-------|------|---------|
| Reproducibility | 62 | Good | standard |

**Cluster Rating:** Adequate

---

## Signal 6: Reproducibility

**Score:** 62/100 (Good)

**Pathway:** standard
**Approach anchors applied:** Deductive

### Assessment

This paper demonstrates good computational reproducibility for deductive empirical research, with a notable asymmetry between code availability (excellent) and data availability (weak). The analytical workflow can be substantially reproduced, but full validation against ground-truth data requires access to the unpublished field survey dataset.

**Code availability is excellent.** Three public GitHub repositories (E038) provide comprehensive coverage of the computational workflow:
1. `cnn-testing` — Training data preparation and CNN prediction validation
2. `burial-mounds` — 2021 CNN classifier training and prediction
3. `MoundDetection` — 2022 CNN classifier training and prediction

These repositories cover the complete analytical pipeline from data preparation through model training to validation. The code uses open, scriptable tools (Python, TensorFlow 2, R) that support reproducibility.

**Data availability is weak.** The 773 ground-truthed mound locations (E007) are referenced to "published TRAP project reports" but are not deposited in a public repository. The satellite imagery was acquired via GeoEye Foundation grant with unclear redistribution terms. This creates a significant barrier to independent reproduction: while the analytical scripts are available, the inputs needed to run them are not publicly accessible.

**Workflow documentation is adequate.** The methods section (M001-M009) documents the analytical workflow at the protocol level, including data partitioning ratios (P010: 70:20:10), probability thresholds (P004: 60%), and tile specifications (P003: 150×150 pixels). However, no explicit environment specification (Python version, package versions, Docker container) is provided in the paper.

### Evidence

**From reproducibility_infrastructure:**
- Code availability: Present — Three public GitHub repositories with Python/R scripts
- Data availability: Not deposited — "Field survey data referenced to published TRAP project reports but not deposited in repository"
- Persistent identifiers: Paper DOI present (10.1108/JD-05-2022-0096); no code DOIs (GitHub URLs only)
- FAIR score: 24/40 (60%)

**From methods/protocols:**
- P001: "CNN model deployment using TensorFlow 2 in Python" — Open scriptable tool
- P010: "Data partitioning into training (70%), validation (20%), and test (10%) sets" — Protocol documented
- M002: "Field validation of model predictions using GPS-located ground-truthed mound locations" — Validation protocol clear but data not accessible

**Strengths:**
- Three public GitHub repositories covering complete computational workflow
- Open scriptable tools (Python, TensorFlow, R) used throughout
- Protocols documented with specific parameters (thresholds, ratios, tile sizes)
- Code structured across logical repositories matching workflow stages

**Weaknesses:**
- Field survey data (773 mound points) not deposited in public repository
- Satellite imagery access unclear (GeoEye Foundation grant terms)
- No explicit environment specification (Python/package versions)
- No code DOIs (GitHub URLs only, no Zenodo archival)
- No explicit licence for code repositories

### Tool Assessment

| Aspect | Status | Tool Type | Impact |
|--------|--------|-----------|--------|
| CNN training | TensorFlow 2, Python | open_scriptable | No demerit |
| Data preparation | R, Python scripts | open_scriptable | No demerit |
| Validation analysis | R scripts | open_scriptable | No demerit |
| GIS processing | Not specified | mixed | Minor demerit — tools not specified |
| HPC execution | UCloud (SDU) | cloud_platform | Minor demerit — platform-specific |

### Scoring Rationale

Score of 62 (Good band for deductive research) because: Data partially available—code shared but input data not deposited (40-59 to 60-79); code shared with basic documentation via GitHub (60-79); workflow documented at protocol level (60-79); some outputs reproducible given access to inputs (60-79); FAIR partially met at 60% (60-79). Score is at lower end of Good because the asymmetric code-data profile creates a significant barrier: analytical scripts can be examined but not executed without independent access to proprietary satellite imagery and unpublished field data. The excellent code availability lifts the score above Moderate, but absent data prevents reaching the upper Good band.

---

## Reproducibility Readiness Checklist

```yaml
reproducibility_readiness:
  applies: true
  pathway: "standard"
  if_not_applicable_reason: ""

  inputs_available:
    status: "partial"
    details: "Field survey data (773 mound GPS points with attributes) referenced to TRAP project reports but not deposited. Satellite imagery (IKONOS) acquired via GeoEye Foundation grant with unclear redistribution terms. Training cutouts and model weights not deposited."

  code_available:
    status: "yes"
    tool_type: "open_scriptable"
    details: "Three public GitHub repositories: (1) cnn-testing for training data preparation and validation; (2) burial-mounds for 2021 CNN; (3) MoundDetection for 2022 CNN. Python/TensorFlow for ML, R for analysis. No DOIs or Zenodo archival."

  environment_specified:
    status: "partial"
    details: "TensorFlow 2 and Python stated. UCloud HPC platform mentioned. No explicit Python version, package versions, or Docker/conda environment provided. Requirements.txt status unknown without repository inspection."

  outputs_documented:
    status: "partial"
    details: "Model performance metrics (F1, precision, recall) documented. Validation results (confusion matrix, detection rates) documented. Intermediate outputs (predictions, tile classifications) implied but not archived."

  execution_feasibility: "needs_work"
  feasibility_rationale: "Analytical code is available and uses standard open tools. However, execution requires: (1) access to 773 ground-truth mound points (not deposited); (2) access to IKONOS satellite imagery (proprietary, GeoEye grant); (3) environment setup (not specified). A researcher could examine and understand the workflow, but could not execute it end-to-end without independent data acquisition."

  publication_year: 2024
  adoption_context: "early_majority"
```

---

## Cluster Synthesis

**Overall Reproducibility:** Adequate

This paper demonstrates adequate reproducibility with a characteristic asymmetric profile: excellent code transparency but weak data accessibility. This pattern is increasingly common in research where computational workflows are shareable but underlying data has access restrictions (proprietary imagery, unpublished primary datasets).

The three GitHub repositories represent exemplary practice for code sharing in digital archaeology. The workflow from training data preparation through model training to validation is fully represented in public code. A researcher could:
1. **Examine** the complete analytical workflow
2. **Understand** all methodological decisions at the code level
3. **Adapt** the approach to their own data
4. **Verify** the logic of validation calculations

However, a researcher could **not** reproduce the specific results without:
1. Access to the 773 ground-truth mound locations (unpublished TRAP data)
2. Access to the IKONOS satellite imagery (proprietary, grant-dependent)
3. Sufficient computational resources (HPC was used)

### Chronological Context

Publication year 2024 places this paper in the **early_majority** era of reproducibility adoption. By 2024 standards, code sharing is expected and data sharing is increasingly expected. The excellent code availability meets 2024 norms. The absent data deposit is a gap relative to current best practice, though understandable given the proprietary satellite imagery and the field data deriving from a separate project (TRAP 2009-2011).

### Gateway Assessment

**Execution Feasibility:** needs_work

This paper could be queued for **partial reproduction** with the following considerations:

**What can be reproduced:**
- Analytical workflow inspection and understanding
- Method adaptation for other datasets
- Validation logic verification

**What would be needed for full reproduction:**
- Field survey data: Contact authors or access TRAP project archives
- Satellite imagery: GeoEye Foundation grant or alternative imagery source
- Environment: Set up Python/TensorFlow environment (should be straightforward given standard tools)

**Recommendation:** This paper is suitable for "analytical transparency assessment" rather than "full reproduction attempt." The code repositories enable verification that the reported methods match the implemented methods. Independent validation would require securing comparable inputs.

---

## Structured Output

```yaml
cluster_3_reproducibility:
  paper_slug: "sobotkova-et-al-2024"
  assessment_date: "2025-12-05"
  quality_state: "high"
  research_approach: "deductive"
  pathway: "standard"
  experimental: false

  reproducibility:
    score: 62
    band: "good"
    strengths:
      - "Three public GitHub repositories covering complete computational workflow"
      - "Open scriptable tools (Python, TensorFlow, R) support reproducibility"
      - "Protocols documented with specific parameters"
      - "Code structured logically across repositories"
    weaknesses:
      - "Field survey data not deposited in public repository"
      - "Satellite imagery access unclear (proprietary)"
      - "No explicit environment specification"
      - "No code DOIs or archival (GitHub URLs only)"
    rationale: "Good reproducibility with asymmetric profile. Excellent code availability enables workflow examination and adaptation. Absent data deposit prevents full execution. Lower Good band due to code-data asymmetry."
    tool_assessment:
      primary_tool_type: "open_scriptable"
      tool_impact: "No demerit — Python, TensorFlow, R are ideal for reproducibility"

  reproducibility_readiness:
    applies: true
    pathway: "standard"
    inputs_available:
      status: "partial"
      details: "Field data and satellite imagery not deposited. Training cutouts not archived."
    code_available:
      status: "yes"
      tool_type: "open_scriptable"
      details: "Three GitHub repositories with Python/R scripts. No DOIs."
    environment_specified:
      status: "partial"
      details: "TensorFlow 2, Python stated. No version specifications or container."
    outputs_documented:
      status: "partial"
      details: "Metrics documented. Intermediate outputs not archived."
    execution_feasibility: "needs_work"
    feasibility_rationale: "Code available but input data requires independent acquisition."
    publication_year: 2024
    adoption_context: "early_majority"

  cluster_synthesis:
    overall_rating: "adequate"
    chronological_interpretation: "2024 publication in early_majority era. Code sharing meets current norms; absent data deposit is gap relative to best practice but understandable given data provenance."
    gateway_recommendation: "Suitable for analytical transparency assessment. Full reproduction requires independent data acquisition. Code enables workflow verification and method adaptation."
```
