# Cluster 3: Reproducibility Assessment

**Paper:** sobotkova-et-al-2024
**Assessment Date:** 2025-11-30
**Assessor Version:** v1.0

**Quality State:** HIGH
**Research Approach:** Deductive (confidence: high)
**Paper Type:** Empirical
**Assessment Pathway:** Standard

---

## Signal Score Summary

| Signal | Score | Band | Pathway |
|--------|-------|------|---------|
| Reproducibility | 71 | Good | Standard |

**Cluster Rating:** Adequate

---

## Signal 6: Reproducibility

**Score:** 71/100 (Good)

**Pathway:** Standard
**Approach anchors applied:** Deductive

### Assessment

This paper demonstrates good computational reproducibility, with excellent code sharing offset by incomplete data availability. The analytical workflow involves CNN training and validation using Python and R, all of which are open-source scriptable tools ideal for reproducibility.

**Code availability** is exemplary. Three distinct GitHub repositories document the complete analytical workflow:
1. `adivea/cnn-testing` - Training data preparation and CNN prediction validation
2. `centre-for-humanities-computing/burial-mounds` - 2021 CNN classifier
3. `centre-for-humanities-computing/MoundDetection` - 2022 CNN classifier

The code availability statement is explicit and machine-actionable with direct URLs. Machine actionability is rated "high" in the extraction.

**Data availability** is the key gap. No explicit data availability statement is present. The historical field survey data from TRAP (773 mounds, 2009-2011) is not deposited in a public repository. Training data (satellite imagery cutouts) availability is unclear - presumably available via GitHub but not explicitly stated. The satellite imagery itself was from GeoEye Foundation grants and may have access restrictions.

**Environment specification** is not detailed in the paper. No requirements.txt, environment.yml, or explicit version pinning is mentioned. The paper states "R and Python" but doesn't specify versions or package dependencies. This creates a moderate reproducibility barrier.

**Workflow documentation** is good through the methods and protocols sections. 12 protocols document specific steps (P001-P012) including model selection, training cutout generation, data composition, and training/validation splits.

### Evidence

**From reproducibility_infrastructure:**
- Code availability: **Yes** — "Scripts are available in public repositories" with 3 GitHub URLs
- Data availability: **Partial** — No explicit statement; field data not deposited; training data unclear
- Persistent identifiers: Paper DOI + 3 GitHub URLs (no code DOIs)
- FAIR score: 75% (12/16) — "highly_fair" rating

**From methods/protocols:**
- P001: "ResNet-50 CNN model selection with ~25.6m trainable parameters" - implementation details
- P002: "Training cutout generation: 150x150m square polygons" - reproducible spatial parameters
- P004: "Training data composition: 1:2 positive to negative ratio" - documented class balance
- P006: "70:20:10 train/validation/test split" - reproducible data partition

**Strengths:**
- Excellent code availability (3 repositories, explicit statement, machine-actionable)
- Open-source tools (Python, R) - ideal for reproducibility
- Detailed protocols document analytical workflow
- FAIR score of 75% indicates good overall compliance

**Weaknesses:**
- No explicit data availability statement
- Historical field data (773 mounds) not deposited
- Training data availability unclear
- No environment specification (Python/R versions, package dependencies)
- No code DOIs (Zenodo integration would improve)

### Tool Assessment

| Aspect | Status | Tool Type | Impact |
|--------|--------|-----------|--------|
| CNN training | Python | open_scriptable | Ideal - no demerit |
| Data preparation | Python/R | open_scriptable | Ideal - no demerit |
| GIS processing | GIS (unspecified) | mixed | Minor demerit - tool not specified |
| Validation | Python | open_scriptable | Ideal - no demerit |

### Scoring Rationale

Score of 71 (Good) reflects: data available with gaps (field data not deposited) (60-79); code shared with basic documentation (60-79); workflow documented through protocols; most computational outputs reproducible; FAIR mostly met (75%). Gap from Excellent due to: incomplete data sharing, missing environment specification, and no pre-registration (though appropriate for retrospective study). The excellent code sharing raises score within Good band.

---

## Reproducibility Readiness Checklist

```yaml
reproducibility_readiness:
  applies: true
  pathway: "standard"
  if_not_applicable_reason: ""

  inputs_available:
    status: "partial"
    details: "Code and methods available. Satellite imagery source documented (IKONOS via GeoEye Foundation). Field survey ground truth (773 mounds) NOT deposited - critical gap for validation reproduction. Training data cutouts availability unclear."

  code_available:
    status: "yes"
    tool_type: "open_scriptable"
    details: "Three GitHub repositories: cnn-testing (validation), burial-mounds (2021 classifier), MoundDetection (2022 classifier). Python and R scripts. Open access. Machine actionability rated high."

  environment_specified:
    status: "partial"
    details: "Tools stated (Python, R, ResNet-50) but no version pinning. No requirements.txt or environment.yml mentioned. UCloud HPC platform noted but not configuration. Would need to inspect repositories for dependency information."

  outputs_documented:
    status: "yes"
    details: "Expected outputs documented: model predictions, F1 scores, precision/recall rates, tile classifications. Quantitative performance metrics explicitly reported (12.8% precision, 95.7% false negatives). Outputs could be verified against reported values."

  execution_feasibility: "needs_work"
  feasibility_rationale: "Code is available and well-documented. CNN training likely reproducible with appropriate environment setup. However, complete reproduction blocked by: (1) field survey ground truth data not deposited - cannot validate against same 773 mounds, (2) original satellite imagery may require separate access from GeoEye/Maxar, (3) environment dependencies need extraction from repositories."

  publication_year: 2024
  adoption_context: "early_majority"
```

---

## Cluster Synthesis

**Overall Reproducibility:** Adequate

The paper demonstrates adequate reproducibility with asymmetric infrastructure: excellent code sharing but incomplete data archiving. This pattern reflects common challenges in computational archaeology where legacy field data precedes current open data norms.

The three GitHub repositories provide a strong foundation for computational reproduction. The CNN training workflow, validation procedures, and analysis scripts are publicly accessible. An independent researcher could likely reproduce the model training process given appropriate satellite imagery inputs.

However, complete reproduction is limited by the field survey data gap. The 773 mound locations serving as ground truth for validation are not deposited. Without this data, an independent researcher could train similar models but could not replicate the specific external validation that is the core contribution of the paper.

### Chronological Context

Publication year 2024 places this paper in the **early majority** era of reproducibility adoption. Code sharing via GitHub is now expected for computational papers, and this paper meets that expectation admirably with three repositories. Data sharing expectations are also high in 2024, making the absent data availability statement a notable gap. For a 2024 paper in a methodological journal, the code sharing is exemplary but data sharing falls short of current best practice.

### Gateway Assessment

**Execution Feasibility:** needs_work

This paper could potentially be queued for reproduction with the following prerequisites:

**Available now:**
- CNN training code (3 repositories)
- Model architecture specifications
- Workflow documentation

**Gaps to address:**
1. **Critical:** Access to satellite imagery (IKONOS) - would need separate acquisition or equivalent source
2. **Critical for validation:** Field survey data (773 mound locations) - not available; could only reproduce training, not validation
3. **Moderate:** Environment specification - would need to inspect repositories for dependencies
4. **Minor:** Code DOIs for versioning

**Recommendation:** Suitable for partial reproduction (CNN training and workflow testing) but not complete reproduction (external validation against field data). Authors could be contacted for field survey data access.

---

## Structured Output

```yaml
cluster_3_reproducibility:
  paper_slug: "sobotkova-et-al-2024"
  assessment_date: "2025-11-30"
  quality_state: "high"
  research_approach: "deductive"
  pathway: "standard"
  experimental: false

  reproducibility:
    score: 71
    band: "good"
    strengths:
      - "Excellent code availability (3 GitHub repositories)"
      - "Open-source tools (Python, R) ideal for reproducibility"
      - "Detailed workflow documentation in protocols"
      - "FAIR score 75% (highly fair)"
    weaknesses:
      - "No explicit data availability statement"
      - "Field survey ground truth not deposited"
      - "Training data availability unclear"
      - "No environment specification"
    rationale: "Good computational reproducibility with excellent code sharing offset by incomplete data availability. Gap from Excellent due to data sharing gaps and missing environment specification."
    tool_assessment:
      primary_tool_type: "open_scriptable"
      tool_impact: "Ideal - Python/R enable full reproducibility of code components"

  reproducibility_readiness:
    applies: true
    pathway: "standard"
    inputs_available:
      status: "partial"
      details: "Code available; satellite imagery source documented but needs separate access; field survey data NOT deposited"
    code_available:
      status: "yes"
      tool_type: "open_scriptable"
      details: "3 GitHub repositories with R and Python scripts"
    environment_specified:
      status: "partial"
      details: "Tools stated but no version pinning or requirements files mentioned"
    outputs_documented:
      status: "yes"
      details: "Quantitative performance metrics documented for verification"
    execution_feasibility: "needs_work"
    feasibility_rationale: "Code reproducible; complete validation blocked by field data gap"
    publication_year: 2024
    adoption_context: "early_majority"

  cluster_synthesis:
    overall_rating: "adequate"
    chronological_interpretation: "2024 paper meets code sharing expectations but falls short on data sharing for current era"
    gateway_recommendation: "Suitable for partial reproduction (CNN training); complete validation reproduction blocked by field data access"
```
