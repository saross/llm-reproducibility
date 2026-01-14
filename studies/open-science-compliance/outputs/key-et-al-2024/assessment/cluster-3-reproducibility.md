# Signal Cluster Assessment: Reproducibility

## Reproducibility Signal

## Paper: key-et-al-2024

**Assessment Date:** 2026-01-14
**Cluster:** 3 - Reproducibility (Reproducibility Pillar)
**Research Approach:** Deductive (methodological validation)
**Quality State:** HIGH

---

## Cluster Overview

This cluster assesses whether the computational aspects of the research can be independently re-executed. For HASS research, Reproducibility means **analytic or computational reproducibility**—can others reproduce the analytical outputs given the same inputs?—NOT beginning-to-end reproducibility or replication of the overall research.

For a methodological paper presenting computational analyses in R, this signal is particularly important. The paper's contribution is a method; reproducibility of that method is essential for adoption and verification.

**Signal prioritisation:** Reproducibility is a **primary signal** for this methodological paper per classification framework.

---

## Signal 7: Reproducibility

**Score:** 68/100
**Confidence:** High

### Signal Definition

Can others reproduce the analytical outputs given the same inputs? Are data and code available and complete? Are computational workflows documented?

### Assessment Summary

Key et al. (2024) demonstrates moderate-to-good computational reproducibility. R code for both validation and case study analyses is available in supplementary materials, the software version is specified (R 4.3.0), and analytical parameters are thoroughly documented in protocols. However, code and data are archived only in publisher supplementary materials without dedicated repository DOIs, package dependencies are not listed, and machine-actionability is low. For a 2024 methods paper, this represents adequate but not optimal reproducibility infrastructure.

### Key Strengths

- **Code available:** R scripts for validation and case study analyses provided in supplementary
- **Software version specified:** "All analyses were undertaken in R version 4.3.0" (P001)
- **Open source tool:** R is open, free, and scriptable—optimal tool choice for reproducibility
- **Detailed parameter documentation:** k-values, sample percentages, iteration counts all specified
- **Workflow traceable:** 12 protocols document analytical steps in detail
- **Open access:** CC BY licence enables code/data reuse

### Key Weaknesses

- **Supplementary-only distribution:** Code and data in publisher supplementary, not dedicated repository
- **No dedicated DOIs:** No persistent identifiers for code or data beyond paper DOI
- **Package dependencies unlisted:** R 4.3.0 specified but required packages not documented
- **No environment specification:** No lockfile, Docker container, or dependency management
- **Limited machine-actionability:** FAIR assessment rates machine-actionability as "low"
- **No CodeMeta:** No standardised software metadata

### Supporting Evidence from Extraction

**Code availability:**

- **Statement:** "The script used to run all validation analyses is available in the supplementary information... The script used to run all case study tests is available in the supplementary information." (pages 4, 6)
- **Format:** R scripts
- **Access:** Publisher supplementary (https://doi.org/10.1016/j.jas.2023.105921)
- **Licence:** CC BY 4.0 (implied from paper licence)

**Data availability:**

- **Statement:** "Supplementary data to this article can be found online at [DOI]" (page 18)
- **Format:** Supplementary tables and datasets
- **Access:** Publisher supplementary

**Environment specification:**

- **Language:** R
- **Version:** 4.3.0
- **Packages:** Not specified
- **System requirements:** Not specified

**FAIR assessment (from Pass 6):**

| FAIR Dimension | Score | Notes |
|----------------|-------|-------|
| Findable | 2/4 | Paper DOI only, no code/data DOIs |
| Accessible | 4/4 | Open access CC BY |
| Interoperable | 0/3 | No formal schemas |
| Reusable | 3/4 | Provenance documented, no CodeMeta |
| **Total** | **9/15 (60%)** | Moderately FAIR |

**Machine-actionability:** Low
- Rationale: "Code and data in publisher supplementary materials. No dedicated repository, no separate DOIs, limited metadata."

### Scoring Justification

Scored 68 (Good Reproducibility for deductive research). This paper meets 60-79 anchor criteria:
- ✅ "Data available (may have minor gaps)" - Supplementary data accessible
- ✅ "Code shared with basic documentation" - R scripts provided
- ✅ "Workflow documented" - Detailed protocols specify analytical steps
- ✅ "Most outputs reproducible" - With effort, analyses should be reproducible

Does not reach 80-100 because:
- ❌ "Complete raw data publicly available with persistent identifiers" - No separate DOIs
- ❌ "Computational environment specified (versions, dependencies)" - Packages not listed
- ❌ "FAIR principles met" - Only 60% FAIR compliance

**Publication era context:** For a 2024 methods paper, dedicated repository archiving (GitHub + Zenodo) with DOIs would be expected for Excellent reproducibility. Supplementary-only provision is adequate but represents 2015-era practices rather than 2024 best practices.

### Approach-Specific Context

**Research Approach:** Deductive (methodological validation)

For deductive research with computational components, Reproducibility emphasises code/data sharing and environment specification. This paper's validation analyses are entirely computational—reproducibility is essential for verification. The code is available but infrastructure falls short of current standards for methods papers.

**Tool-based assessment:**
- **Tool type:** Open scriptable (R) - Ideal for reproducibility
- **Code portability:** Good (R scripts are portable)
- **Dependency tracking:** Poor (packages not specified)
- **Environment isolation:** None (no containers or lockfiles)

### Reproducibility Readiness Assessment

This structured assessment supports potential future automated reproduction attempts:

```yaml
reproducibility_readiness:
  applies: true
  pathway: standard
  if_not_applicable_reason: ""

  inputs_available:
    status: "partial"
    details: "Validation replica assemblage data and case study morphometric data available in supplementary. Some case study data from published sources - availability varies."

  code_available:
    status: "yes"
    tool_type: "open_scriptable"
    details: "R scripts for validation and case study analyses in supplementary materials. Language: R. No dedicated repository."

  environment_specified:
    status: "partial"
    details: "R version 4.3.0 specified. Required packages not listed. No lockfile or container."

  outputs_documented:
    status: "yes"
    details: "Validation results (accuracy, CI coverage) and case study results (range extensions) documented in Results section and supplementary tables."

  execution_feasibility: "needs_work"
  feasibility_rationale: "Code is available and analyses should be reproducible with effort. However, package dependencies would need to be inferred from code inspection. Some case study input data may need to be sourced from original publications."

  publication_year: 2024
  adoption_context: "early_majority"
```

### Recommendations for Improvement

1. **Archive code in dedicated repository:** GitHub with Zenodo integration for DOI
2. **Document dependencies:** Include renv.lock or requirements list
3. **Add CodeMeta metadata:** Software citation and discovery
4. **Create reproducibility container:** Docker image with R environment
5. **Separate data archive:** Dataset with own DOI in domain repository

---

## Cross-Signal Coherence Check

**Single-signal cluster:** No cross-signal coherence check required for Cluster 3.

**Coherence with other clusters:**

Reproducibility (68) is lower than Transparency (78), which is coherent:
- Transparency assesses documentation completeness (excellent protocols)
- Reproducibility assesses practical re-execution capability (infrastructure gaps)

A paper can be highly transparent (well-documented) but only moderately reproducible (infrastructure limitations). This is exactly the pattern here: exceptional methods documentation but supplementary-only code sharing.

---

## Cluster Summary

**Overall Assessment:** Reproducibility is moderate-to-good

**Primary Strengths:**

1. R code for all analyses provided
2. Open source tool (R) enables verification
3. Detailed workflow documentation in 12 protocols
4. Open access licence permits reuse

**Primary Weaknesses:**

1. Supplementary-only distribution limits machine-actionability
2. No package dependency documentation
3. No persistent identifiers for code/data
4. Falls short of 2024 methods paper standards

**Implications for Overall Credibility:**

Moderate reproducibility is a notable limitation for a methods paper. While the validation analyses are theoretically reproducible, practical re-execution would require effort to infer dependencies and potentially source case study input data. This doesn't undermine the paper's validity claims (validation evidence is strong), but it does limit the ease of method adoption and verification.

**Execution feasibility:** "Needs work" - Reproducible with effort, but not ready for automated reproduction.

---

## Assessment Metadata

**Assessor:** research-assessor skill v2.1
**Assessment Date:** 2026-01-14
**Approach-Specific Anchors Applied:** Yes (deductive research anchors)
**Quality State:** HIGH
