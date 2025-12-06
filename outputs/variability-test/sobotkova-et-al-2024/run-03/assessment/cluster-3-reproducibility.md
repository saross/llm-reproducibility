# Cluster 3: Reproducibility Assessment

**Paper:** sobotkova-et-al-2024
**Assessment Date:** 2025-12-05
**Assessor Version:** v1.0

**Quality State:** HIGH
**Research Approach:** deductive (confidence: high)
**Paper Type:** empirical
**Assessment Pathway:** standard

---

## Signal Score Summary

| Signal | Score | Band | Pathway |
|--------|-------|------|---------|
| Reproducibility | 65 | Good | standard |

**Cluster Rating:** Adequate

---

## Signal 7: Reproducibility

**Score:** 65/100 (Good)

**Pathway:** standard
**Approach anchors applied:** deductive

### Assessment

This paper demonstrates a reproducibility profile with asymmetric strengths: excellent code availability but limited data accessibility. Three public GitHub repositories provide complete analytical code for CNN training, prediction, and validation. However, the 773-mound field dataset (the critical validation benchmark) is not deposited in a public repository, and the IKONOS satellite imagery is proprietary.

For deductive hypothesis-testing research, the key reproducibility question is: can someone else run the analysis and verify the results? The answer is: **partially**. The computational workflow is fully documented and executable, but reproducing the core validation requires access to data that isn't publicly available.

Code availability is strong:
- `github.com/adivea/cnn-testing` — Training data preparation and validation scripts
- `github.com/centre-for-humanities-computing/burial-mounds` — 2021 CNN classifier training
- `github.com/centre-for-humanities-computing/MoundDetection` — 2022 CNN classifier training

Environment specification is adequate: TensorFlow 2, Python, ResNet-50 with 25.6m trainable parameters, UCloud HPC. However, exact package versions and environment files (requirements.txt, environment.yaml) are not mentioned in the paper.

The methodological documentation is exemplary: protocols specify training/validation/test splits (70:20:10), data augmentation procedures, probability thresholds (60%), and validation methodology. This enables analytical reproducibility even where data access is constrained.

### Evidence

**From reproducibility_infrastructure:**

- Code availability: **YES** — Three public GitHub repositories with Python and R scripts
- Data availability: **PARTIAL** — Field data (773 mounds) referenced but not publicly deposited; satellite imagery proprietary
- Persistent identifiers: Paper DOI present (10.1108/JD-05-2022-0096); no data DOIs; software URLs but no software DOIs
- FAIR score: 20/40 (50%) — Findable/Accessible good for code, limited for data

**From methods/protocols:**

- P01 (Image Cutout Generation): 150×150m polygons, EPSG:32635, detailed specifications
- P02 (Data Split): 70:20:10 ratio, 1:2 positive:negative ratio documented
- P03 (CNN Training): ResNet-50, TensorFlow 2, augmentation procedures specified
- P05 (Field Validation): 60% probability threshold, spatial intersection method

**Strengths:**
- Three public GitHub repositories with complete analytical code
- Comprehensive protocol documentation enables methodological reproduction
- Technical specifications fully documented (model architecture, parameters, procedures)
- Open scriptable tools (Python, R) — ideal for reproducibility
- Resource requirements reported (135 person-hours) — rare transparency

**Weaknesses:**
- Field survey data (773 mounds) not deposited in public repository
- Satellite imagery proprietary (IKONOS via GeoEye Foundation grant)
- No explicit environment specification (package versions, dependencies)
- No data DOIs or persistent identifiers for datasets

### Tool Assessment

| Aspect | Status | Tool Type | Impact |
|--------|--------|-----------|--------|
| CNN model training | TensorFlow 2 / Python | open_scriptable | No demerit |
| Data preparation | Python scripts | open_scriptable | No demerit |
| Validation analysis | R scripts | open_scriptable | No demerit |
| GIS processing | QGIS implied | open_scriptable | No demerit |

All computational tools are open-source and scriptable, representing ideal reproducibility practice.

### Scoring Rationale

Score: 65 (Good for deductive). Code shared with documentation through three GitHub repositories (meets 60-79 "code shared with basic documentation"). Data availability has gaps — field data not publicly deposited, imagery proprietary (60-79 "Data available with minor gaps" — gaps are significant but not total). Workflow documented through comprehensive protocols (meets 60-79 "workflow documented"). Most analytical outputs reproducible if data were available. FAIR score 50% reflects partial compliance.

Falls short of Excellent (80-100) because: data not publicly available with PIDs, no environment specification files, no explicit FAIR principles statement. The asymmetric profile (excellent code, limited data) is characteristic of papers using legacy fieldwork data and proprietary imagery.

---

## Reproducibility Readiness Checklist

```yaml
reproducibility_readiness:
  applies: true
  pathway: "standard"
  if_not_applicable_reason: ""

  inputs_available:
    status: "partial"
    details: "Field survey data (773 mounds GPS coordinates, attributes) not publicly deposited — available through author contact or TRAP project. IKONOS satellite imagery proprietary — acquired through GeoEye Foundation grant, not shareable."

  code_available:
    status: "yes"
    tool_type: "open_scriptable"
    details: "Three public GitHub repositories: cnn-testing (data preparation, validation), burial-mounds (2021 CNN training), MoundDetection (2022 CNN training). Python and R scripts with TensorFlow 2."

  environment_specified:
    status: "partial"
    details: "Paper specifies: TensorFlow 2, Python, ResNet-50 (25.6m parameters), UCloud HPC. No requirements.txt, environment.yaml, or Docker container. Package versions not specified."

  outputs_documented:
    status: "yes"
    details: "Expected outputs well-documented: F1 scores, false positive/negative rates, tile-based detection rates. Tables in paper provide verification benchmarks."

  execution_feasibility: "needs_work"
  feasibility_rationale: "Code is executable but data access requires author coordination. Full reproduction needs: (1) access to TRAP field data or comparable ground-truth dataset; (2) satellite imagery with comparable specifications; (3) environment setup from repository documentation."

  publication_year: 2024
  adoption_context: "early_majority"
```

---

## Cluster Synthesis

**Overall Reproducibility:** Adequate

This paper demonstrates an asymmetric reproducibility profile that is common in archaeological research using legacy fieldwork data and proprietary remote sensing imagery. The computational components are exemplary: three public GitHub repositories with complete Python and R code for the full analytical workflow (data preparation, CNN training, prediction, validation). Protocol documentation enables methodological reproduction even where data access is constrained.

The limitation is data accessibility. The 773-mound ground-truth dataset — which is the critical validation benchmark — is not deposited in a public repository. The IKONOS satellite imagery is proprietary. This creates a "computation reproducible, validation not" scenario: someone could retrain the CNN model with different data, but cannot verify the specific false positive/negative rates reported without access to the original data.

### Chronological Context

Publication year 2024 places this paper in the **early_majority** era of reproducibility adoption. By 2024 standards, the code availability is exemplary (three public repositories) while data availability lags expectations. The authors acknowledge this implicitly — the field data comes from 2009-2011 TRAP fieldwork predating current data deposit norms.

The 65/100 score should be interpreted in context: this represents good practice for computational archaeology with legacy data constraints. The code transparency is ahead of field norms; the data gap reflects common limitations when using pre-existing fieldwork.

### Gateway Assessment

**Execution Feasibility:** needs_work

This paper is **not ready** for immediate execution-based reproduction but **could be queued** with coordination:

**What would be needed:**
1. **Data access:** Contact authors or TRAP project for field survey data (773 mounds with GPS coordinates and attributes)
2. **Alternative imagery:** Substitute IKONOS with comparable satellite imagery (e.g., Sentinel-2, Planet Labs) — would test transferability but not reproduce exact results
3. **Environment setup:** Install TensorFlow 2, clone GitHub repositories, configure Python environment from repository documentation

**Partial reproduction possible:**
- CNN training pipeline can be run with substitute data
- Validation methodology can be replicated with different ground-truth datasets
- Core finding (high false negative rates for "low-touch" transfer learning) could be tested in different contexts

**Full reproduction barriers:**
- Original IKONOS imagery not shareable
- Field data requires author coordination
- Without exact data, can only test methodology, not verify specific metrics

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
    score: 65
    band: "good"
    strengths:
      - "Three public GitHub repositories with complete analytical code"
      - "Comprehensive protocol documentation (training, validation, data preparation)"
      - "Open scriptable tools (Python, R, TensorFlow 2)"
      - "Resource requirements transparently reported (135 person-hours)"
    weaknesses:
      - "Field survey data (773 mounds) not deposited in public repository"
      - "Satellite imagery proprietary (IKONOS via GeoEye Foundation)"
      - "No environment specification files (requirements.txt, Docker)"
      - "No persistent identifiers for datasets"
    rationale: "Asymmetric reproducibility: excellent code availability, limited data accessibility. Computational workflow fully documented and executable, but core validation requires data not publicly available."
    tool_assessment:
      primary_tool_type: "open_scriptable"
      tool_impact: "no_demerit"

  reproducibility_readiness:
    applies: true
    pathway: "standard"
    inputs_available:
      status: "partial"
      details: "Field data (773 mounds) not publicly deposited. IKONOS imagery proprietary."
    code_available:
      status: "yes"
      tool_type: "open_scriptable"
      details: "Three GitHub repos: cnn-testing, burial-mounds, MoundDetection"
    environment_specified:
      status: "partial"
      details: "TensorFlow 2, Python, ResNet-50 specified. No environment files."
    outputs_documented:
      status: "yes"
      details: "F1 scores, detection rates, confusion matrices documented as verification benchmarks"
    execution_feasibility: "needs_work"
    feasibility_rationale: "Code executable but data requires author coordination. Partial reproduction possible with substitute datasets."
    publication_year: 2024
    adoption_context: "early_majority"

  cluster_synthesis:
    overall_rating: "adequate"
    chronological_interpretation: "2024 publication shows exemplary code practice, data availability reflects legacy fieldwork constraints. 65/100 represents good practice for computational archaeology with pre-existing data."
    gateway_recommendation: "Queue for partial reproduction with coordination. Full reproduction requires data access arrangement."
```
