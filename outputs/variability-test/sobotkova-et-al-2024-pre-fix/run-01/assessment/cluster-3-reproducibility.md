# Cluster 3: Reproducibility Assessment

**Paper:** sobotkova-et-al-2024
**Assessment Date:** 2025-11-30
**Assessor Version:** v1.0

**Quality State:** HIGH
**Research Approach:** Deductive (confidence: high)
**Paper Type:** Empirical
**Assessment Pathway:** Standard (computational components present)

---

## Signal Score Summary

| Signal | Score | Band | Pathway |
|--------|-------|------|---------|
| Reproducibility | 72 | Good | Standard |

**Cluster Rating:** Adequate

---

## Computational Component Assessment

### Pathway Determination

This paper has computational components requiring Standard Reproducibility assessment:
- Machine learning model training (CNN with transfer learning)
- Python scripts for model implementation
- R scripts for data processing and validation
- Computational workflows on HPC infrastructure

Assessment follows standard deductive anchors for computational reproducibility.

---

## Signal 7: Reproducibility

**Score:** 72/100 (Good)

**Approach anchors applied:** Deductive (Standard pathway)

### Assessment

This paper demonstrates good computational reproducibility for deductive research. The key strength is comprehensive code sharing through three public GitHub repositories covering the complete analytical pipeline: training data preparation, 2021 CNN classifier, and 2022 CNN classifier. This level of code sharing exceeds typical practice in archaeological remote sensing.

Code availability is excellent. The repositories are publicly accessible and organised by function. The separation of training data preparation, 2021 model, and 2022 model allows researchers to engage with specific components. The use of open scriptable tools (R, Python) rather than proprietary software maximises reproducibility.

However, data availability is the primary limitation. Satellite imagery (IKONOS) is commercial and not directly shareable. Field survey data is referenced to a prior publication (Ross et al. 2018) rather than directly deposited with PIDs. This means full analytical reproducibility requires: (1) purchasing IKONOS imagery, (2) obtaining field data through the reference publication. The computational workflow itself is reproducible; the inputs are not fully accessible.

Environment specification is partial. The paper mentions UCloud HPC and identifies R and Python as tools, but does not provide detailed dependency information (requirements.txt, conda environment, Docker container). This is a gap that would require some trial-and-error to resolve.

### Evidence from extraction.json

**Code availability (strong):**
- `reproducibility_infrastructure.code_availability.repositories[]`: Three public GitHub repositories
  - https://github.com/adivea/cnn-testing (validation scripts)
  - https://github.com/centre-for-humanities-computing/burial-mounds (2021 model)
  - https://github.com/centre-for-humanities-computing/MoundDetection (2022 model)
- Machine actionability rated "high" — GitHub URLs with clear purposes

**Data availability (limited):**
- `reproducibility_infrastructure.data_availability`: Statement present
- Field data: Referenced to Ross et al. 2018 publication (not directly deposited)
- Satellite imagery: Commercial IKONOS (not shareable)
- Machine actionability rated "medium" due to access barriers

**Environment specification (partial):**
- `reproducibility_infrastructure.computational_environment.documented`: true
- Details: "UCloud interactive HPC system at University of Southern Denmark; R and Python used"
- Gap: No detailed dependency specification (requirements.txt, environment.yml)

### Strengths

- **Excellent code sharing:** Three public repositories covering complete pipeline
- **Open tools:** R and Python (open scriptable) maximise reproducibility
- **Organised workflow:** Clear separation of training prep, 2021 model, 2022 model
- **Current era (2024):** Published when code sharing increasingly expected

### Weaknesses

- **Data access barriers:** Commercial imagery and reference-only field data
- **No environment specification:** Dependencies not formally documented
- **No containerisation:** No Docker/Singularity for environment reproducibility

### Scoring Rationale

Score of 72 (Good for deductive) reflects: code shared with basic documentation via GitHub (60-79); workflow documented through organised repositories (60-79); data partially available with barriers (60-79). Score is Good rather than Excellent because data access limitations and lack of formal environment specification prevent full reproducibility without additional effort. Would need full data deposit and environment specification for 80+ score.

---

## Reproducibility Readiness Checklist

```yaml
reproducibility_readiness:
  # Pathway determination
  applies: true
  pathway: "standard"
  if_not_applicable_reason: ""

  # Input availability
  inputs_available:
    status: "partial"
    details: "Code available. Field survey data referenced to publication (Ross et al. 2018) but not directly deposited. Satellite imagery commercial (IKONOS) - requires purchase. Training data preparation scripts allow recreation of cutouts if imagery obtained."

  # Code availability
  code_available:
    status: "yes"
    tool_type: "open_scriptable"
    details: "Three public GitHub repositories: (1) cnn-testing (validation scripts, R), (2) burial-mounds (2021 CNN, Python), (3) MoundDetection (2022 CNN, Python). All open source, publicly accessible."

  # Environment specification
  environment_specified:
    status: "partial"
    details: "UCloud HPC environment mentioned. R and Python identified. No requirements.txt, conda environment file, or Docker container provided. Some trial-and-error may be needed for dependency resolution."

  # Output documentation
  outputs_documented:
    status: "partial"
    details: "Results tables in paper provide expected outputs (detection rates, false positive/negative rates). No formal verification files or expected output datasets in repositories."

  # Overall feasibility
  execution_feasibility: "needs_work"
  feasibility_rationale: "Code is available and well-organised. Main barriers: (1) obtain commercial satellite imagery or substitute data, (2) resolve computational dependencies through trial-and-error. Computational workflow reproducible if inputs available."

  # Chronological context
  publication_year: 2024
  adoption_context: "early_majority"
```

---

## Cluster Synthesis

**Overall Reproducibility:** Adequate

### Assessment Summary

This paper demonstrates adequate reproducibility with notable strengths and limitations. Code sharing is exemplary — three organised public repositories cover the complete analytical pipeline. This reflects good practice for 2024 publication in the early majority era of reproducibility adoption.

The primary limitation is data access. Commercial satellite imagery and reference-only field data create barriers to full analytical reproduction. This is a common challenge for archaeological remote sensing research where imagery licensing constraints limit data sharing.

### Implications for Reproduction Attempts

Researchers wishing to reproduce this analysis would need to:
1. Obtain IKONOS satellite imagery (commercial purchase) or substitute data
2. Access field survey data through Ross et al. 2018 reference
3. Resolve R and Python dependencies (no formal environment specification)
4. Use provided training data preparation scripts to recreate cutouts
5. Run CNN training and validation using provided model code

**Feasibility:** Moderate effort required. Code infrastructure is solid; data acquisition is the main hurdle.

---

## Structured Output

```yaml
cluster_3_reproducibility:
  paper_slug: "sobotkova-et-al-2024"
  assessment_date: "2025-11-30"
  quality_state: "high"
  research_approach: "deductive"
  pathway: "standard"

  reproducibility:
    score: 72
    band: "good"
    strengths:
      - "Three public GitHub repositories covering complete pipeline"
      - "Open scriptable tools (R, Python)"
      - "Well-organised workflow separation"
    weaknesses:
      - "Commercial satellite imagery not shareable"
      - "Field data reference-only, not directly deposited"
      - "No formal environment specification"
    rationale: "Good for deductive. Code shared with documentation, workflow documented, but data access limitations and no environment specification prevent Excellent rating."

  reproducibility_readiness:
    inputs_available: "partial"
    code_available: "yes"
    environment_specified: "partial"
    outputs_documented: "partial"
    execution_feasibility: "needs_work"
    publication_year: 2024
    adoption_context: "early_majority"

  cluster_synthesis:
    overall_rating: "adequate"
    pattern_summary: "Strong code sharing, limited data access. Computational workflow reproducible if inputs obtained."
    implications: "Reproduction requires commercial imagery acquisition and dependency resolution. Code infrastructure supports reproduction attempt."
```
