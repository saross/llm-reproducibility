# Signal Cluster Assessment: Reproducibility

## Reproducibility

## Paper: herskind-riede-2024

**Assessment Date:** 2026-01-17
**Cluster:** 3 - Reproducibility (Reproducibility Pillar)
**Research Approach:** Inductive (methodological paper with case study demonstration)
**Quality State:** HIGH

---

## Cluster Overview

This cluster assesses whether the research can be computationally or analytically reproduced. **Reproducibility** in HASS (Humanities, Arts, and Social Sciences) means analytic or computational reproducibility — can others reproduce the analytical outputs given the same inputs? For computational methodology papers, this is a **primary assessment signal**.

This is distinct from replicability (conducting the entire study again from scratch), which is often impossible or inappropriate in HASS contexts.

**For this methodological paper:** Reproducibility focuses on whether the computational pipeline (skipgram generation → PMI calculation → frequency/chronological analysis) can be reproduced from the archived data and code.

---

## Signal 7: Reproducibility

**Score:** 80/100
**Confidence:** High

### Signal Definition

Can others reproduce the analytical outputs given the same inputs? Are data, code, and workflow sufficiently documented for independent verification?

### Assessment Summary

Excellent reproducibility for a computational methodology paper. Data and code are openly archived in Zenodo repositories with DOIs. The R version and primary package dependency are documented. The analytical workflow is clearly described in the paper text. The main gaps are: no computational environment containerisation, incomplete dependency specification, and no explicit licence for deposited materials. For a 2024 publication, this represents strong open science practice.

### Key Strengths

- **Data openly available:** Corpus data in Zenodo (DOI: 10.5281/zenodo.10623550) and supplementary information (DOI: 10.5281/zenodo.10801706)
- **Code openly available:** R scripts for skipgram analysis deposited in same Zenodo repository
- **R version documented:** R v4.2.2 explicitly stated (E007)
- **Primary package documented:** Quanteda (Benoit et al., 2018) identified as main analysis package
- **Workflow described:** Data transformation → skipgram generation → PMI calculation → frequency analysis → chronological comparison pipeline clear
- **Persistent identifiers:** Two Zenodo DOIs provide stable access points

### Key Weaknesses

- **No computational environment containerisation:** No Docker image or similar encapsulation of full environment
- **Incomplete dependency specification:** Only R version and Quanteda mentioned; full package list not provided
- **No explicit licence for deposited materials:** Zenodo deposits lack stated licence in paper text
- **Missing ORCIDs:** Authors lack persistent identifiers, limiting author disambiguation
- **Custom classification not machine-actionable:** Płonka's motif classification scheme not linked to controlled vocabulary

### Supporting Evidence from Extraction

**Data availability (from reproducibility_infrastructure):**

```
data_availability:
  statement_present: true
  statement_type: "available_with_accession"
  repositories:
    - name: "Zenodo"
      url: "https://zenodo.org/records/10623550"
      access_conditions: "open"
    - name: "Zenodo"
      url: "https://zenodo.org/records/10801706"
      access_conditions: "open"
  datasets:
    - "South Scandinavian Mesolithic ornamentation dataset" (Supplementary S1)
    - "R code for skipgram analysis" (Supplementary S2)
    - "Complete data tables" (Supplementary S3)
```

**Code availability (from reproducibility_infrastructure):**

```
code_availability:
  statement_present: true
  statement_type: "available_with_accession"
  repositories:
    - name: "Zenodo"
      url: "https://zenodo.org/records/10623550"
  software_dependencies:
    - name: "R", version: "4.2.2"
    - name: "Quanteda", version: null
```

**FAIR assessment:**

- Findable: 3/4 (missing domain-specific indexing)
- Accessible: 3/4 (Zenodo persistence unclear)
- Interoperable: 2/4 (custom classification, no controlled vocabulary)
- Reusable: 2/4 (missing licence, community standards)
- **Total: 10/16 (62.5%, "moderately_fair")**

**PID graph connectivity:** 3/6 (moderate)

- Paper DOI: Present ✓
- Author ORCIDs: None ✗
- Dataset DOIs: 2 Zenodo DOIs ✓
- Software DOIs: None (no separate software publication)
- Sample PIDs: N/A
- Vocabulary DOIs: None ✗

### Reproducibility Readiness Assessment

**Pathway:** Standard (computational methodology paper)

| Component | Status | Details |
|-----------|--------|---------|
| **Inputs available** | Yes | Corpus data in Zenodo S1, metadata documented |
| **Code available** | Yes | R scripts in Zenodo S2 |
| **Environment specified** | Partial | R 4.2.2 + Quanteda noted, full dependencies not listed |
| **Outputs documented** | Yes | Tables 1-2, Figures 3-5 provide expected outputs |
| **Execution feasibility** | Ready | Standard R environment, open data, straightforward pipeline |

**Feasibility rationale:** A researcher with R programming experience could plausibly reproduce the analysis. The key pipeline steps (data loading → sentence transformation → skipgram generation → PMI calculation) are documented, and the Quanteda package is well-maintained open-source software. The main risk is package version incompatibility over time, as specific versions are not pinned.

### Scoring Justification

Scored 80 (Excellent Reproducibility band for inductive research). This paper meets 80-100 anchor criteria:

- ✓ "Data openly archived with documentation" — Zenodo repositories with DOIs
- ✓ "Code openly archived" — R scripts in Zenodo
- ✓ "Computational workflow documented in paper" — Clear pipeline description
- ✓ "Key software versions noted" — R 4.2.2, Quanteda package
- ✓ "Expected outputs documented for verification" — Tables and figures provide comparison points

Does not reach higher scores (85+) because:

- No containerisation (Docker, etc.) for full environment encapsulation
- Incomplete dependency specification (only R and Quanteda, not full package list)
- No explicit licence for deposited materials
- Missing ORCIDs reduce author disambiguation

### Approach-Specific Context

**Research Approach:** Inductive (methodological paper)

For inductive research, reproducibility emphasises data archiving and workflow documentation. For a computational methodology paper, the anchors note:

> "For methods papers emphasising computational analysis, reproducibility expectations include code sharing and environment documentation."

This paper meets these expectations well. The open availability of both data and code enables verification of the computational pipeline. The pipeline (R + Quanteda) uses widely available open-source tools, reducing barriers to reproduction.

**CARE Principles:** Not applicable — this paper uses published archaeological catalogue data, not indigenous or community data requiring special ethical considerations.

### Adoption Context

**Publication year:** 2024
**Adoption context:** Early Majority (post-2020)

**Contextual interpretation:** For a 2024 archaeology publication, this represents strong open science practice. The discipline has made progress on data/code sharing, particularly for computational work, though practices vary. This paper exceeds typical practices by providing both data and code with DOIs. Gaps (ORCIDs, licences, containerisation) reflect areas where adoption is still maturing.

**Note:** Adoption context is metadata for interpretation — scores are not adjusted for publication era.

### Relevant Metrics

- **FAIR score:** 10/16 (62.5%)
- **PID graph connectivity:** 3/6 (moderate)
- **Data availability:** Open (Zenodo)
- **Code availability:** Open (Zenodo)
- **Machine actionability:** Moderate (data accessible via DOI, no formal API)

---

## Cross-Signal Coherence Check

**Does Reproducibility cohere with Transparency?**

Yes, strong coherence between Reproducibility (80) and Transparency (82):

| Signal | Score | Key Criterion |
|--------|-------|---------------|
| Transparency | 82 | Workflow documented, limitations acknowledged |
| Reproducibility | 80 | Data/code archived, environment partially specified |

The similar scores reflect that good methodological documentation (Transparency) supports computational reproducibility (Reproducibility). The slightly higher Transparency score reflects comprehensive limitation acknowledgement, while Reproducibility has minor gaps in environment specification.

**Unexplained tensions:** None.

---

## Cluster Summary

**Overall Assessment:** Reproducibility is **excellent**.

**Primary Strengths:**

- Data and code openly archived in Zenodo with DOIs
- R version and primary package dependency documented
- Clear computational workflow described in paper
- Standard open-source tools (R, Quanteda) reduce barriers
- Expected outputs documented for verification

**Primary Weaknesses:**

- No computational environment containerisation
- Incomplete dependency specification
- Missing licence for deposited materials
- No ORCIDs for author disambiguation

**Reproducibility Readiness:**

- **Execution feasibility:** Ready
- **Estimated effort:** Low-to-moderate (standard R environment setup)
- **Main risk:** Package version incompatibility over time

**Implications for Overall Credibility:**

Excellent reproducibility strongly supports the paper's credibility as a methodological contribution. Researchers can verify the computational pipeline, attempt reproduction, and potentially extend the method to other corpora. The open availability of data and code demonstrates commitment to transparent science and enables the research community to build on this work.

For a methodological paper, reproducibility is a primary assessment criterion — the method's credibility depends on others being able to apply it. This paper meets that standard well.

---

## Assessment Metadata

**Assessor:** research-assessor skill v0.2-alpha
**Assessment Date:** 2026-01-17
**Approach-Specific Anchors Applied:** Yes (inductive research anchors, with Reproducibility emphasised for methodological papers)
**Quality State:** HIGH
