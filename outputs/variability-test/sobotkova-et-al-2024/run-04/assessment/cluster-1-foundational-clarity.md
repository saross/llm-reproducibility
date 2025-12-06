# Cluster 1: Foundational Clarity Assessment

**Paper:** sobotkova-et-al-2024
**Assessment Date:** 2025-12-05
**Assessor Version:** v1.0

**Quality State:** HIGH
**Research Approach:** Deductive (confidence: high)
**Paper Type:** Empirical

---

## Signal Scores Summary

| Signal | Score | Band | Approach Anchors |
|--------|-------|------|------------------|
| Comprehensibility | 78 | Good | Deductive |
| Transparency | 80 | Excellent | Deductive |

**Cluster Rating:** Strong

---

## Signal 1: Comprehensibility

**Score:** 78/100 (Good)

**Approach anchors applied:** Deductive

### Assessment

This paper demonstrates good comprehensibility for deductive hypothesis-testing research. While explicit formal hypotheses are not stated (e.g., "H1: CNN will detect ≥50% of mounds"), the implicit hypotheses are clearly framed and their testing is transparent. The research questions are operationally clear: Can a pre-trained CNN reliably detect burial mounds? Will curating training data improve performance?

Claims are explicit and precisely bounded. The core claims (C001-C003) articulate specific findings with quantified performance metrics. C001 states "The CNN model failed to reliably detect burial mounds when validated against field data, with very high false negative and false positive rates" - this is clear, bounded, and directly evaluable. Key terms like "false negative rate," "F1 score," and "true positive" are used consistently with standard ML definitions.

The logical structure follows a clear hypothesis-testing pattern: expectation (pre-trained CNN should detect mounds) → experimental test (two configurations) → validation against ground truth → quantified outcome → interpretation. The reasoning from test results to conclusions is transparent, particularly in how the authors explain the disconnect between internal metrics (F1=0.87) and external validation (95% false negatives).

One minor weakness is that hypotheses are implicit rather than formally stated. The paper would score higher on deductive anchors with explicit hypothesis specifications in the introduction. However, the implicit hypothesis-testing framework is sufficiently clear that readers can understand what was tested and on what basis conclusions were drawn.

### Evidence

**Strengths:**
- C001: "The CNN model failed to reliably detect burial mounds when validated against field data" — Clear core claim with explicit bounds
- C002: "Self-reported CNN performance metrics (F1 scores) were misleadingly high" — Precise claim about metric-reality gap
- RD001: "Comparative validation design testing CNN predictions against ground-truthed field data" — Explicit design statement
- RD002: "Experimental design with two treatment conditions" — Clear comparative framework

**Weaknesses:**
- No formally stated hypotheses (e.g., "H1: We hypothesise that...") — Hypotheses are implicit in the testing framework
- IA003: "Standard ML performance metrics adequately reflect real-world performance" — This implicit assumption could have been made explicit a priori

### Scoring Rationale

Score of 78 (Good band for deductive research) because: Hypotheses are stated implicitly through research design (60-79 criterion); all key terms operationally defined (60-79); logical structure of hypothesis testing is transparent (60-79); claims are unambiguous and testable (80-100); reasoning from test results to conclusions is clear (80-100). Falls short of 80-100 "Excellent" primarily because hypotheses are not explicitly stated and pre-registered. The 78 score reflects strong comprehensibility with minor room for improvement in explicit hypothesis specification.

---

## Signal 2: Transparency

**Score:** 80/100 (Excellent)

**Approach anchors applied:** Deductive

### Assessment

This paper demonstrates excellent methodological transparency for deductive empirical research. While not pre-registered, the research design is clearly documented with comprehensive methods and protocols. The paper provides exceptional code availability through three public GitHub repositories, enabling independent verification and reproduction of computational analyses.

Methods documentation is comprehensive. M001-M009 detail the CNN classification approach, field validation procedures, performance evaluation metrics, training data preparation, and literature review methodology. Each method is linked to implementing protocols (P001-P015) that specify technical details such as the 70:20:10 data split (P010), 60% probability threshold (P004), and spatial intersection validation procedure (P005).

Data accessibility presents a mixed picture. Code availability is excellent with three GitHub repositories (cnn-testing, burial-mounds, MoundDetection) covering all computational aspects. However, the underlying field survey data (773 GPS-located mounds) is not deposited in a public repository, limiting full reproducibility. The FAIR assessment scores 24/40 (60%), with code accessibility driving the score up while data inaccessibility limits it.

Limitations are explicitly acknowledged throughout. The authors document their failed expectations (IA002: "We believed that the volume of training data would offset other shortcomings"), the disconnect between internal and external validation (C056), and the specific technical choices that may have contributed to poor performance (C061: non-overlapping tiles, C045: small mound-to-tile ratio).

### Evidence

**From reproducibility_infrastructure:**
- Code availability: Present — Three public GitHub repositories with Python/R scripts
- Data availability: Not deposited — "Field survey data referenced to published TRAP project reports but not deposited in repository"
- Persistent identifiers: Paper DOI present (10.1108/JD-05-2022-0096); no code DOIs
- FAIR score: 24/40 (60%)

**From methods/protocols:**
- M002: "Field validation of model predictions using GPS-located ground-truthed mound locations" — Validation approach explicit
- P005: "Spatial intersection of CNN predictions with ground-truthed mound points" — Validation protocol clear and reproducible
- P010: "Data partitioning into training (70%), validation (20%), and test (10%) sets" — Standard protocol documented

**Strengths:**
- Three public GitHub repositories with complete computational workflow
- Clear validation methodology linking predictions to ground-truth
- Explicit documentation of analytical decisions and thresholds
- Comprehensive acknowledgement of limitations and failed expectations

**Weaknesses:**
- No pre-registration of study design or hypotheses
- Field survey data not deposited in public repository (references earlier publications only)
- No explicit data licence for code repositories
- Satellite imagery redistribution terms unclear

### Scoring Rationale

Score of 80 (Excellent band for deductive research) because: Clear research design and hypothesis specification (60-79); detailed methods with full protocol documentation (80-100); data availability stated with excellent code sharing but no data repository (60-79); workflow documented and executable via GitHub (80-100); major limitations explicitly acknowledged (80-100). The score reaches "Excellent" threshold due to exemplary code availability and comprehensive methods documentation. The lack of pre-registration and data deposit prevents a higher score within the band.

---

## Cluster Synthesis

**Overall Foundational Clarity:** Strong

This paper exhibits strong foundational clarity appropriate for deductive hypothesis-testing research. Both signals score in the upper ranges of their bands (Good-Excellent), indicating that readers can understand what was tested, how it was tested, and on what basis conclusions were drawn.

### Pattern Summary

The Comprehensibility and Transparency scores are consistent and mutually reinforcing. The paper's clear articulation of claims (Comprehensibility) is supported by detailed methodological documentation (Transparency). The logical hypothesis-testing structure evident in the claims is operationalised through explicit methods and protocols. The primary limitation across both signals is the implicit rather than explicit hypothesis specification and lack of pre-registration.

### Implications for Subsequent Assessment

- **For Cluster 2 (Evidential Strength):** Strong transparency enables confident assessment of evidence sufficiency. The explicit methods and validation protocols allow evaluation of whether evidence adequately tests the implicit hypotheses. The honest documentation of negative results supports validity assessment.

- **For Cluster 3 (Reproducibility):** Excellent code availability positions this paper well for reproducibility assessment. The computational workflow is fully documented in public repositories. However, the lack of deposited field data creates an asymmetric reproducibility profile where analytical reproduction is feasible but data verification is not.

---

## Structured Output

```yaml
cluster_1_foundational_clarity:
  paper_slug: "sobotkova-et-al-2024"
  assessment_date: "2025-12-05"
  quality_state: "high"
  research_approach: "deductive"

  comprehensibility:
    score: 78
    band: "good"
    strengths:
      - "Clear core claims with quantified performance metrics"
      - "Explicit research design with comparative validation framework"
      - "Logical hypothesis-testing structure transparent throughout"
      - "Key ML terms used consistently with standard definitions"
    weaknesses:
      - "Hypotheses implicit rather than formally stated"
      - "No pre-registered predictions"
    rationale: "Good comprehensibility for deductive research. Implicit hypotheses are clearly framed through research design, claims are precise and bounded, and reasoning from tests to conclusions is transparent. Falls short of excellent due to lack of explicit hypothesis statements."

  transparency:
    score: 80
    band: "excellent"
    strengths:
      - "Three public GitHub repositories with complete computational workflow"
      - "Comprehensive methods and protocols documentation"
      - "Explicit validation methodology"
      - "Thorough acknowledgement of limitations and failed expectations"
    weaknesses:
      - "No pre-registration"
      - "Field survey data not deposited in repository"
      - "No explicit licence for code"
    rationale: "Excellent transparency for deductive research. Comprehensive methods documentation, exemplary code availability, and explicit limitation acknowledgement. Lack of pre-registration and data deposit are the primary gaps."

  cluster_synthesis:
    overall_rating: "strong"
    pattern_summary: "Consistent high performance across both foundational signals. Clear claims supported by detailed methods documentation. Logical structure enables confident downstream assessment."
    consistency_check: "consistent"
    implications:
      cluster_2: "Strong transparency enables confident validity assessment. Negative results honestly documented."
      cluster_3: "Excellent code availability supports computational reproducibility. Asymmetric profile due to missing data deposit."
```
