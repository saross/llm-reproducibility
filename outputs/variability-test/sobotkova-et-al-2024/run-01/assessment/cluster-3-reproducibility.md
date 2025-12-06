# Cluster 3: Reproducibility Assessment

**Paper:** sobotkova-et-al-2024
**Assessment Date:** 2025-12-04
**Assessor Version:** v1.0

**Quality State:** HIGH
**Research Approach:** deductive (confidence: high)
**Paper Type:** empirical
**Assessment Pathway:** standard

---

## Signal Score Summary

| Signal | Score | Band | Pathway |
|--------|-------|------|---------|
| Reproducibility | 55 | Moderate | standard |

**Cluster Rating:** Adequate

---

## Signal 6: Reproducibility

**Score:** 55/100 (Moderate)

**Pathway:** standard
**Approach anchors applied:** deductive

### Assessment

This paper has computational components (CNN model training, transfer learning, image processing) that make the standard reproducibility pathway appropriate. The assessment reveals a mixed reproducibility profile: strong code availability but weak data availability and environment documentation.

**Code availability is strong.** Three GitHub repositories are provided:
1. `adivea/cnn-testing` - Training data preparation and model validation
2. `centre-for-humanities-computing/burial-mounds` - 2021 CNN model code
3. `centre-for-humanities-computing/MoundDetection` - 2022 CNN model code

These repositories cover the core analytical workflow. However, no persistent identifiers (DOIs via Zenodo) are provided, and licences are not specified in the paper.

**Data availability is weak.** No formal data availability statement is present. The field survey data (773 mound locations with dimensions) is not deposited in any repository - it is referenced to a prior publication (Sobotkova and Ross, 2018) but not directly accessible. The satellite imagery (IKONOS) is proprietary and not accessible. The training data cutouts generated from satellite imagery are not deposited.

**Environment documentation is minimal.** The paper mentions "UCloud interactive HPC system" at University of Southern Denmark but provides no software versions (Python version, TensorFlow/Keras version), GPU specifications, memory allocation, or container/environment specifications. Hyperparameters (learning rate, epochs, batch size) are not documented.

**Workflow documentation is partial.** The training data preparation process is described in the Methods section with some detail (150x150 pixel cutouts, class ratios), but specific implementation decisions and parameters are often implicit.

### Evidence

**From reproducibility_infrastructure:**
- Code availability: **YES** — 3 GitHub repositories with training data prep and model code
- Data availability: **NO** — No formal statement; field data referenced to prior publication; satellite imagery proprietary
- Persistent identifiers: Paper DOI only (10.1108/JD-05-2022-0096); no code DOIs, no data DOIs
- FAIR score: Partial findable, partial accessible, limited interoperable, limited reusable

**From methods/protocols:**
- M002: Training data preparation documented with cutout sizes and class ratios
- P-IMP-002: Hyperparameters identified as implicit - not documented
- P-IMP-004: Software environment identified as implicit - versions not documented

**Strengths:**
- Three functional code repositories covering the analytical workflow
- Training data preparation methodology described in detail
- CC BY 4.0 open access licence for the paper itself

**Weaknesses:**
- No formal data availability statement or data deposit
- Field data (773 mound locations) not accessible
- Satellite imagery proprietary (IKONOS via GeoEye grant)
- Training data cutouts not deposited
- Software versions and environment not documented
- Hyperparameters not documented

### Tool Assessment

| Aspect | Status | Tool Type | Impact |
|--------|--------|-----------|--------|
| Primary analysis (CNN) | Documented in code repos | open_scriptable (Python) | No demerit |
| HPC platform | Mentioned (UCloud) | HPC | Moderate demerit - environment not specified |
| Image processing | Implied in code | open_scriptable | No demerit |
| Field data collection | Described | Manual (GPS recording) | Not applicable - not computational |

### Scoring Rationale

Score: 55 (Moderate for deductive). Code partially shared with basic structure but incomplete documentation (40-59). Data partially available - referenced to prior publication but not deposited (40-59). Workflow partially documented - methods described but parameters missing (40-59). Some outputs reproducible - could run code but cannot fully replicate due to data unavailability (40-59). Partial FAIR compliance. The strong code availability (3 repos) lifts the score above 40, but weak data availability and missing environment documentation prevent Good rating.

---

## Reproducibility Readiness Checklist

```yaml
reproducibility_readiness:
  applies: true
  pathway: "standard"
  if_not_applicable_reason: ""

  inputs_available:
    status: "partial"
    details: "Field survey mound locations (773 points) referenced to Sobotkova and Ross 2018 but not directly deposited. Satellite imagery proprietary (IKONOS via GeoEye grant, 2009). Training data cutouts not deposited. Code repositories available but require recreating or obtaining input data."

  code_available:
    status: "yes"
    tool_type: "open_scriptable"
    details: "Three GitHub repositories provided: (1) adivea/cnn-testing for training data prep and validation, (2) centre-for-humanities-computing/burial-mounds for 2021 model, (3) centre-for-humanities-computing/MoundDetection for 2022 model. Python-based using CNN/transfer learning. Licences not specified in paper."

  environment_specified:
    status: "partial"
    details: "UCloud HPC system at University of Southern Denmark mentioned. Python implied by code repos. No software versions documented (Python version, TensorFlow/Keras version, GPU type, memory). No containerisation (Docker/Singularity) or requirements.txt referenced in paper."

  outputs_documented:
    status: "partial"
    details: "Expected outputs described: F1 scores, prediction tiles, confusion matrices. Results reported in paper (F1=0.87 for 2021, F1=0.62 for 2022, validation metrics). Model prediction maps shown in figures. However, trained model weights not deposited, and exact expected outputs for verification not provided."

  execution_feasibility: "needs_work"
  feasibility_rationale: "Reproduction would require: (1) obtaining comparable satellite imagery (IKONOS scenes or similar), (2) obtaining or recreating field survey data (773 mound locations), (3) determining software versions and hyperparameters not documented in paper, (4) setting up computational environment. Code is available but inputs and environment prevent immediate execution."

  publication_year: 2024
  adoption_context: "early_majority"
```

---

## Cluster Synthesis

**Overall Reproducibility:** Adequate

The paper demonstrates adequate reproducibility infrastructure overall. The three code repositories represent genuine commitment to sharing analytical workflows - this exceeds many ML papers in the archaeological literature. However, the reproducibility profile is asymmetric: computational code is shared, but the data inputs required to use that code are not available.

### Chronological Context

Publication year 2024 places this paper in the **early_majority** era of reproducibility adoption. By 2024 standards, code sharing is increasingly expected and the three repositories meet this expectation. Data sharing is also increasingly expected but remains inconsistent across disciplines. The absence of a formal data availability statement and the lack of data deposit is a gap relative to current best practice, though not uncommon for archaeological research involving proprietary satellite imagery.

### Gateway Assessment

**Execution Feasibility:** needs_work

To attempt reproduction, the following gaps would need to be addressed:

1. **Data acquisition**: Obtain comparable satellite imagery (IKONOS or similar high-resolution multispectral). Original imagery was acquired via GeoEye Foundation grant in 2009 - licensing/access unclear.

2. **Field data access**: Contact authors or access prior publication (Sobotkova and Ross, 2018) to obtain 773 mound coordinates.

3. **Environment specification**: Determine Python version, deep learning framework version, and hardware specifications through code inspection or author contact.

4. **Hyperparameter determination**: Determine learning rate, epochs, batch size through code inspection or author contact.

Given these requirements, this paper would be classified as "needs work" rather than "ready" for actual reproduction attempt. The code sharing represents a foundation that could enable reproduction with additional effort.

---

## Structured Output

```yaml
cluster_3_reproducibility:
  paper_slug: "sobotkova-et-al-2024"
  assessment_date: "2025-12-04"
  quality_state: "high"
  research_approach: "deductive"
  pathway: "standard"
  experimental: false

  reproducibility:
    score: 55
    band: "moderate"
    strengths:
      - "Three GitHub repositories cover core analytical workflow"
      - "Training data preparation methodology documented"
      - "Open scriptable tools (Python/CNN)"
    weaknesses:
      - "No formal data availability statement or data deposit"
      - "Field data (773 mound locations) not accessible"
      - "Satellite imagery proprietary"
      - "Software versions and hyperparameters not documented"
    rationale: "Moderate for deductive research. Code availability strong (3 repos), but data availability weak (not deposited), environment documentation minimal (no versions), and workflow documentation partial (no hyperparameters). Asymmetric profile - computational code shared but inputs not available."
    tool_assessment:
      primary_tool_type: "open_scriptable"
      tool_impact: "No demerit for Python/CNN approach; moderate demerit for undocumented environment"

  reproducibility_readiness:
    applies: true
    pathway: "standard"
    inputs_available:
      status: "partial"
      details: "Field data referenced to prior publication; satellite imagery proprietary; training cutouts not deposited"
    code_available:
      status: "yes"
      tool_type: "open_scriptable"
      details: "Three GitHub repositories provided covering training, 2021 model, 2022 model"
    environment_specified:
      status: "partial"
      details: "UCloud HPC mentioned; no software versions, GPU specs, or hyperparameters"
    outputs_documented:
      status: "partial"
      details: "Results reported in paper but trained model weights and verification outputs not deposited"
    execution_feasibility: "needs_work"
    feasibility_rationale: "Code available but inputs (data, imagery) and environment (versions, hyperparameters) would need to be obtained/determined before reproduction attempt"
    publication_year: 2024
    adoption_context: "early_majority"

  cluster_synthesis:
    overall_rating: "adequate"
    chronological_interpretation: "2024 early_majority era: code sharing meets current expectations; data sharing gap below emerging best practice but common in archaeology with proprietary imagery"
    gateway_recommendation: "Needs work - code available but data acquisition and environment specification required before reproduction attempt"
```
