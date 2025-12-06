# Cluster 3: Reproducibility Assessment

**Paper:** sobotkova-et-al-2024
**Assessment Date:** 2025-12-06
**Assessor Version:** v1.0

**Quality State:** HIGH
**Research Approach:** Deductive (confidence: high)
**Paper Type:** Empirical
**Assessment Pathway:** standard

---

## Signal Score Summary

| Signal | Score | Band | Pathway |
|--------|-------|------|---------|
| Reproducibility | 58 | Moderate | Standard |

**Cluster Rating:** Adequate

---

## Signal 6: Reproducibility

**Score:** 58/100 (Moderate)

**Pathway:** standard
**Approach anchors applied:** Deductive

### Assessment

This paper has clear computational components: CNN transfer learning with ResNet-50, satellite imagery preprocessing (pan-sharpening), training data augmentation, and spatial validation against ground-truth data. These computational aspects constitute the core analytical workflow that could potentially be reproduced.

The paper demonstrates an asymmetric reproducibility profile. Code availability is strong—three GitHub repositories are mentioned, and the TRAP project has a documented history of open data practices. However, several critical components for full reproducibility are missing or under-documented.

**Key reproducibility enablers:**
1. GitHub repositories mentioned for TRAP project data processing
2. CNN model architecture specified (ResNet-50, 25.6m parameters)
3. Training parameters partially documented (70:20:10 split, 1:2 positive:negative ratio)
4. Validation methodology clearly specified (60% probability threshold, spatial overlap detection)

**Key reproducibility barriers:**
1. No persistent identifiers (DOIs) for code repositories
2. IKONOS satellite imagery obtained through 2009 GeoEye Foundation grant—not publicly available
3. Field survey data (773 mounds) availability not specified
4. Hyperparameter tuning details not documented
5. Software versions and computational environment not specified
6. Pan-sharpening algorithm and GIS software not named

The fundamental barrier is data availability: while the analytical workflow is reasonably documented, the primary inputs (IKONOS imagery, mound GPS coordinates) are not deposited in accessible repositories with persistent identifiers.

### Evidence

**From extraction.json methods and protocols:**
- M02: "ResNet-50 seemed to perform best for our data. This model is one of the smaller pre-trained CNNs available, with only around 25.6m trainable parameters" — Model specification clear
- P04: "cutouts were divided into training, validation, and test sets following a 70:20:10 ratio" — Training protocol specified
- P05: "All of the training images were augmented using vertical and horizontal flip and random rotation" — Augmentation stated but incomplete (rotation angles, library not specified)
- P08: "mound-probability exceeded 0.599" — Threshold specified but rationale not documented
- M05: "fused the panchromatic and multispectral bands" — Process described but algorithm/software not named

**Inferred from paper content:**
- GitHub repositories referenced for TRAP project
- No formal data availability statement
- No code DOI or persistent identifier

**Strengths:**
- Clear CNN model architecture specification (ResNet-50)
- Training/validation/test split documented
- Validation methodology explicit with threshold
- Two-run comparison provides some workflow transparency
- GitHub presence for TRAP project

**Weaknesses:**
- Primary data (IKONOS imagery) not publicly available
- Field survey data repository not specified
- No persistent identifiers for code or data
- Hyperparameters and software versions not documented
- Pan-sharpening and GIS tools not named
- Data augmentation parameters incomplete

### Tool Assessment

| Aspect | Status | Tool Type | Impact |
|--------|--------|-----------|--------|
| CNN model training | ResNet-50 transfer learning | open_scriptable (Python/TensorFlow implied) | Positive — reproducible if code shared |
| Satellite imagery preprocessing | Pan-sharpening fusion | Unknown (software not specified) | Moderate negative — may require consultation |
| Spatial validation | GIS overlap detection | Unknown (software not specified) | Moderate negative — procedure clear but tool unknown |
| Data augmentation | Flip/rotation | open_scriptable (library not specified) | Minor negative — parameters incomplete |

### Scoring Rationale

Score of 58 (Moderate for deductive) reflects: data partially available (some code through GitHub, but primary imagery and survey data not deposited); some code shared but may be incomplete and lacks documentation of versions/environments; workflow partially documented (training split, threshold, validation method clear, but hyperparameters and software specifics missing); some outputs reproducible in principle but data access barriers prevent verification. Falls short of Good (60-79) primarily due to: no persistent identifiers, no formal data deposit, incomplete environment specification, and key tool gaps (GIS, pan-sharpening software).

---

## Reproducibility Readiness Checklist

```yaml
reproducibility_readiness:
  applies: true
  pathway: "standard"
  if_not_applicable_reason: ""

  inputs_available:
    status: "partial"
    details: "IKONOS satellite imagery acquired through 2009 GeoEye Foundation grant—not publicly available. Field survey data (773 mounds) from TRAP 2009-2011—availability not specified. GitHub repositories mentioned for TRAP project but specific data deposits not confirmed."

  code_available:
    status: "partial"
    tool_type: "open_scriptable"
    details: "GitHub repositories mentioned for TRAP project data processing. CNN implementation implied to be Python-based (ResNet-50 transfer learning). Specific repository URLs not provided in paper. No DOIs for code. Model training code completeness unknown."

  environment_specified:
    status: "no"
    details: "No software versions specified. Python/TensorFlow implied but not stated. GIS software not named. Pan-sharpening algorithm not specified. No containerisation or environment files mentioned."

  outputs_documented:
    status: "partial"
    details: "F1 scores, detection rates, and validation metrics fully documented. Predicted tiles with probabilities described. But no intermediate outputs (trained model weights, prediction files) deposited for verification."

  execution_feasibility: "needs_work"
  feasibility_rationale: "Conceptual workflow is clear and methodology well-documented, but reproduction attempt would be blocked by: (1) IKONOS imagery access requiring separate licensing/acquisition, (2) field survey data requiring direct author contact, (3) software environment requiring reconstruction from implicit clues. With author cooperation and imagery licensing, reproduction could be feasible."

  publication_year: 2024
  adoption_context: "early_majority"
```

---

## Cluster Synthesis

**Overall Reproducibility:** Adequate

The paper demonstrates adequate reproducibility for a 2024 publication—a period when data and code sharing are increasingly expected. The computational workflow is clearly described at the conceptual level, with specific parameters documented for training splits, validation thresholds, and model architecture. GitHub repositories for the TRAP project suggest a commitment to open practices.

However, the paper falls short of current best practices in several ways. No persistent identifiers are provided for data or code. The primary data inputs (IKONOS imagery, field survey coordinates) are not deposited in accessible repositories. Key software tools (GIS, pan-sharpening algorithm) are not named. Computational environment is not specified. These gaps create significant barriers to independent reproduction, even though the analytical logic is transparent.

### Chronological Context

Publication year 2024 places this paper in the **early_majority** era of reproducibility adoption. By this period, data availability statements and code repositories with DOIs are increasingly expected, particularly for computational research. The paper's GitHub presence is consistent with era expectations, but the absence of persistent identifiers, formal data deposits, and environment specification falls below emerging norms for ML-based research.

### Gateway Assessment

**Execution Feasibility:** needs_work

This paper is **not ready** for immediate reproduction attempt but could become feasible with targeted effort:

**What would be needed to attempt reproduction:**
1. **Data access:** Contact authors or TRAP project for field survey data; negotiate IKONOS imagery access or obtain equivalent satellite imagery
2. **Code location:** Identify specific GitHub repository containing CNN training code
3. **Environment reconstruction:** Determine Python version, TensorFlow/PyTorch version, and dependencies from code inspection
4. **Software identification:** Clarify GIS tool used for spatial validation, pan-sharpening algorithm

**Feasibility with cooperation:** High. The methodology is clearly documented at the procedural level, and the authors' institutional context (digital archaeology, open data advocacy) suggests likely cooperation with reproduction requests.

---

## Structured Output

```yaml
cluster_3_reproducibility:
  paper_slug: "sobotkova-et-al-2024"
  assessment_date: "2025-12-06"
  quality_state: "high"
  research_approach: "deductive"
  pathway: "standard"
  experimental: false

  reproducibility:
    score: 58
    band: "moderate"
    strengths:
      - "Clear CNN model architecture specification (ResNet-50 with 25.6m parameters)"
      - "Training/validation/test split documented (70:20:10)"
      - "Validation methodology explicit with stated threshold (60%)"
      - "GitHub presence for TRAP project"
      - "Two-run comparison provides workflow transparency"
    weaknesses:
      - "Primary data (IKONOS imagery) not publicly available"
      - "Field survey data repository not specified"
      - "No persistent identifiers for code or data"
      - "Hyperparameters and software versions not documented"
      - "GIS and pan-sharpening tools not named"
    rationale: "Meets Moderate criteria (40-59): data partially available through project GitHub, some code shared but incomplete documentation, workflow partially documented, some outputs reproducible in principle. Falls short of Good (60-79) due to no persistent identifiers, incomplete environment specification, and data access barriers."
    tool_assessment:
      primary_tool_type: "open_scriptable"
      tool_impact: "Positive for reproducibility if code fully shared; current gaps in environment specification and tool naming create moderate barriers"

  reproducibility_readiness:
    applies: true
    pathway: "standard"
    inputs_available:
      status: "partial"
      details: "IKONOS imagery not public; field survey data availability unspecified; GitHub repos mentioned"
    code_available:
      status: "partial"
      tool_type: "open_scriptable"
      details: "GitHub repos for TRAP project; specific CNN code completeness unknown; no DOIs"
    environment_specified:
      status: "no"
      details: "No software versions, no GIS tool named, no containerisation"
    outputs_documented:
      status: "partial"
      details: "Performance metrics documented but no intermediate outputs deposited"
    execution_feasibility: "needs_work"
    feasibility_rationale: "Clear conceptual workflow but blocked by data access and environment gaps; feasible with author cooperation"
    publication_year: 2024
    adoption_context: "early_majority"

  cluster_synthesis:
    overall_rating: "adequate"
    chronological_interpretation: "2024 publication in early_majority era; GitHub presence meets era norms but absence of persistent identifiers and formal data deposits falls below emerging best practices for ML research"
    gateway_recommendation: "Not ready for immediate reproduction; could become feasible with author cooperation for data access and code clarification"
```
