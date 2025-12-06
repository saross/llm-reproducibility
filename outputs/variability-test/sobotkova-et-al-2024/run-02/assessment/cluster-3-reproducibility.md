# Cluster 3: Reproducibility & Scope Assessment

**Paper:** sobotkova-et-al-2024
**Assessment Date:** 2025-12-05
**Assessor Version:** v1.0

**Quality State:** HIGH
**Research Approach:** deductive
**Paper Type:** empirical

---

## Signal Scores Summary

| Signal | Score | Band | Approach Anchors |
|--------|-------|------|------------------|
| Reproducibility | 62 | Good | deductive |

**Cluster Rating:** Adequate

---

## Signal 7: Reproducibility

**Score:** 62/100 (Good)

**Approach anchors applied:** deductive

### Assessment

The paper demonstrates asymmetric reproducibility - excellent computational workflow transparency but significant data accessibility gaps. This pattern is characteristic of field-science research where data dependencies complicate full reproducibility.

**Computational Reproducibility (Strong):**
Three GitHub repositories provide comprehensive code coverage: `cnn-testing` (data preparation, validation), `burial-mounds` (2021 CNN training), and `MoundDetection` (2022 CNN training). Implementation uses documented frameworks (TensorFlow 2, Python) on documented infrastructure (UCloud HPC at University of Southern Denmark). The code enables understanding of the computational workflow and, in principle, re-execution with appropriate data.

**Data Reproducibility (Weak):**
No formal data availability statement exists. Field survey data (773 mound locations from TRAP 2009-2011) is not deposited in a public repository. IKONOS satellite imagery was acquired through GeoEye Foundation grant and is not publicly available. Training data cutouts, ground-truth coordinates, and trained model weights are not shared. FAIR score of 62.5% (10/16) reflects this gap.

**Replication Path:**
A researcher could: (1) understand the methodology from the paper, (2) examine the code to understand implementation, (3) NOT re-run the analysis without obtaining equivalent data independently. The paper is methodologically transparent but not computationally reproducible without data access.

### Evidence from extraction.json

**Code Availability (reproducibility_infrastructure.code_availability):**
- `statement_present`: true
- 3 repositories documented:
  - `cnn-testing`: https://github.com/adivea/cnn-testing (R, Python)
  - `burial-mounds`: https://github.com/centre-for-humanities-computing/burial-mounds (Python)
  - `MoundDetection`: https://github.com/centre-for-humanities-computing/MoundDetection (Python)
- `machine_actionability.rating`: "high"

**Data Availability (reproducibility_infrastructure.data_availability):**
- `statement_present`: false
- No repositories documented
- `access_conditions`: "No formal data availability statement. Field survey data (773 mounds) from TRAP 2009-2011 is referenced but not deposited..."
- `machine_actionability.rating`: "low"

**Computational Environment (reproducibility_infrastructure.computational_environment):**
- `documented`: true
- UCloud HPC at University of Southern Denmark
- TensorFlow 2, Python specified
- Random seeds and exact versions NOT documented

**FAIR Assessment (reproducibility_infrastructure.fair_assessment):**
- Findable: 3/4 (DOI, repos linked)
- Accessible: 2/4 (code yes, data no)
- Interoperable: 3/4 (standard formats)
- Reusable: 2/4 (code available, data/models missing)
- Total: 10/16 (62.5%)

### Reproducibility Dimensions Assessment

| Dimension | Score | Notes |
|-----------|-------|-------|
| Code availability | 85 | 3 GitHub repos, comprehensive coverage |
| Data availability | 25 | No deposit, no access statement |
| Environment documentation | 60 | HPC documented, versions partial |
| Protocol documentation | 75 | 14 protocols, 2 implicit |
| Pre-registration | 0 | Not pre-registered |

**Weighted Assessment:** The asymmetric profile (code 85, data 25) averages to ~62, which accurately reflects the paper's reproducibility state.

### Strengths

- **Comprehensive code sharing:** Three repositories covering all computational components
- **Platform documentation:** UCloud HPC explicitly named with institutional affiliation
- **Framework transparency:** TensorFlow 2, Python specified
- **Methodological reproducibility:** Detailed protocols enable understanding of approach

### Weaknesses

- **No data deposit:** 773 mound coordinates not archived
- **Satellite imagery inaccessible:** Commercial imagery not shareable
- **Trained models not shared:** CNN weights not deposited
- **Random seeds undocumented:** Exact reproducibility limited
- **Dependency versions incomplete:** Specific library versions not documented

### Scoring Rationale

Score of 62 reflects Good reproducibility at lower end of band: excellent code availability (3 repos) balanced against significant data gap (no deposit, no access statement). The score appropriately captures asymmetric reproducibility profile - computational workflow is transparent and could theoretically be re-executed, but data dependencies prevent practical replication. For deductive empirical research, this represents adequate but not excellent reproducibility. Score would be higher (75+) with data archiving, lower (45-55) without code repositories.

---

## Cluster Synthesis

**Overall Reproducibility & Scope:** Adequate

The paper demonstrates the characteristic tension in computational archaeology between code transparency (achievable) and data accessibility (constrained by commercial imagery rights and legacy fieldwork data). The asymmetric profile is common but limits full reproducibility.

### Pattern Summary

Strong computational transparency (3 GitHub repos, HPC documentation) with weak data accessibility (no deposit, commercial imagery) produces moderate overall reproducibility. This pattern is common in field sciences with data dependencies but represents a limitation for verification and replication.

### Implications for Final Report

- **Reproducibility verdict:** Partial - methodology and code reproducible, data dependencies block full replication
- **FAIR compliance:** Moderate (62.5%) - findable and interoperable strengths, accessible and reusable weaknesses
- **Recommendation:** Future work should archive ground-truth coordinates (even if satellite imagery cannot be shared)

---

## Structured Output

```yaml
cluster_3_reproducibility:
  paper_slug: "sobotkova-et-al-2024"
  assessment_date: "2025-12-05"
  quality_state: "high"
  research_approach: "deductive"

  reproducibility:
    score: 62
    band: "good"
    strengths:
      - "Three GitHub repositories with comprehensive code"
      - "HPC environment documented (UCloud)"
      - "Standard frameworks (TensorFlow 2, Python)"
      - "Detailed methodological protocols"
    weaknesses:
      - "No data repository deposit"
      - "Satellite imagery inaccessible (commercial)"
      - "Trained model weights not shared"
      - "Random seeds and versions undocumented"
    rationale: "Good reproducibility at lower end of band due to asymmetric profile: excellent code availability (85) balanced against poor data accessibility (25). Computational workflow transparent but not practically reproducible without data."

  fair_assessment:
    findable: 3
    accessible: 2
    interoperable: 3
    reusable: 2
    total: 10
    percentage: 62.5

  cluster_synthesis:
    overall_rating: "adequate"
    pattern_summary: "Asymmetric reproducibility profile typical of computational field science - strong code transparency, weak data accessibility."
    implications:
      final_report: "Partial reproducibility - methodology reproducible, data dependencies block full replication"
      recommendations: "Future work should archive ground-truth coordinates even if imagery cannot be shared"
```
