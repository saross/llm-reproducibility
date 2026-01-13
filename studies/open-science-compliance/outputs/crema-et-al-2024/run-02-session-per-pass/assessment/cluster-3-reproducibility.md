# Cluster 3: Reproducibility Assessment

**Paper:** crema-et-al-2024
**Assessment Date:** 2026-01-13
**Assessor Version:** v1.0

**Quality State:** HIGH
**Research Approach:** deductive (confidence: high)
**Paper Type:** methodological
**Assessment Pathway:** standard

---

## Signal Score Summary

| Signal | Score | Band | Pathway |
|--------|-------|------|---------|
| Reproducibility | 90 | Excellent | standard |

**Cluster Rating:** Strong

---

## Signal 6: Reproducibility

**Score:** 90/100 (Excellent)

**Pathway:** standard
**Approach anchors applied:** deductive

### Assessment

This paper achieves exemplary reproducibility, representing best practice for computational archaeology. All code and data are publicly available through dual archival (GitHub + Zenodo with DOI), the computational workflow is fully documented, and the code has been independently reviewed.

**Input availability** is complete. All radiocarbon data used in the three case studies are available in the GitHub repository and permanently archived on Zenodo (DOI: 10.5281/zenodo.10782942). The data availability statement explicitly confirms this: "All data and R scripts are available on https://github.com/ercrema/diffusionCurve and permanently archived on https://doi.org/10.5281/zenodo.10782942."

**Code availability** is comprehensive. R scripts for all analyses are shared with the same dual archival. The code implements both the hierarchical Bayesian sigmoid model (M001) and the ICAR non-parametric model (M002). Critically, the code was independently reviewed by Ben Marwick, the Journal of Archaeological Science's Reproducibility Specialist, who is acknowledged for "reviewing the computational code and providing suggestions to improve its reproducibility."

**Environment specification** is good but not exhaustive. The language (R) and calibration curve (IntCal20) are specified. MCMC settings are fully documented (P001, P004). However, specific R package dependencies and versions are not explicitly listed in the paper text — these would need to be checked in the repository documentation.

**Workflow documentation** is excellent. The paper provides complete specification of the analytical workflow: MCMC chains, iterations, burn-in, and thinning (P001, P004); prior distributions for all parameters (P002); calibration curve (P003); filtering criteria for each dataset (P007-P009); and simulation parameters (P010). This enables reproduction of the entire analytical pipeline.

**Output documentation** enables verification. Table 1 provides parameter estimates (r, m, mu, phi) with 90% HPD intervals for each case study, giving clear targets for reproduction comparison. The figures show posterior predictions and simulation envelopes that could be regenerated.

### Evidence

**From reproducibility_infrastructure:**
- Code availability: statement_present = true; repositories = [GitHub, Zenodo]; access_conditions = open; language = R
- Data availability: statement_present = true; repositories = [GitHub, Zenodo]; persistent_archive = DOI 10.5281/zenodo.10782942
- Persistent identifiers: code_doi = 10.5281/zenodo.10782942; paper_doi = 10.1016/j.jas.2024.105962
- Code review: Ben Marwick reviewed computational code (acknowledged)

**From methods/protocols:**
- P001: "four chains, each with 1 million iterations (half discarded as burn-in) and with thinning set to 50" — MCMC settings explicit
- P002: Prior specifications (r ~ Exponential(100); mu ~ Beta(2,2); phi ~ Gamma(5,0.1)) — reproducible statistical specification
- P003: IntCal20 calibration curve specified
- P010: Simulation parameters explicit (r=0.01, m=2900 BP, mu=0.65, phi=50 for simulation 1a)

**Strengths:**
- Dual archival (GitHub + Zenodo DOI) provides both working repository and permanent archive
- Independent code review by JAS Reproducibility Specialist (Ben Marwick)
- Complete MCMC specification enables exact reproduction
- Pre-specified simulation parameters enable validation reproduction
- Table 1 parameter estimates provide clear verification targets

**Weaknesses:**
- R package dependencies and versions not explicitly listed in paper (may be in repository)
- No containerised environment (Docker) for full environment specification

### Tool Assessment

| Aspect | Status | Tool Type | Impact |
|--------|--------|-----------|--------|
| Primary analysis | R scripts | open_scriptable | Ideal — no demerit |
| Bayesian inference | nimble/rstan (presumed) | open_scriptable | Ideal |
| Calibration | IntCal20 | standard curve | Standard — reproducible |
| Visualisation | R | open_scriptable | Ideal |

### Scoring Rationale

Score of 90 (Excellent for deductive). Complete data publicly available with PIDs (DOI for Zenodo archive) — meets 80-100 criterion. All code shared with documentation and independent code review — meets and exceeds 80-100 criterion (code review is exceptional). Environment partially specified (R language, IntCal20, MCMC settings explicit; package versions not in paper text) — minor gap from 80-100 ideal. Workflow fully documented and executable — meets 80-100 criterion. Outputs documented for verification (Table 1, figures) — meets 80-100 criterion. FAIR principles substantially met with persistent identifiers for code, data, and paper. Score reflects exemplary practice with minor gap on environment specification (package versions/dependencies).

---

## Reproducibility Readiness Checklist

```yaml
reproducibility_readiness:
  applies: true
  pathway: "standard"
  if_not_applicable_reason: ""

  inputs_available:
    status: "yes"
    details: "All radiocarbon data for three case studies available on GitHub and permanently archived on Zenodo (DOI: 10.5281/zenodo.10782942). Data availability statement confirms open access."

  code_available:
    status: "yes"
    tool_type: "open_scriptable"
    details: "R scripts for all analyses available on GitHub and Zenodo. Implements both hierarchical Bayesian (M001) and ICAR (M002) models. Code independently reviewed by Ben Marwick (JAS Reproducibility Specialist)."

  environment_specified:
    status: "partial"
    details: "R language specified. IntCal20 calibration curve documented (P003). MCMC settings explicit (P001, P004). Package dependencies and versions not listed in paper text — would need to check repository for DESCRIPTION/renv.lock files."

  outputs_documented:
    status: "yes"
    details: "Table 1 provides parameter estimates (r, m, mu, phi) with 90% HPD intervals for all models. Figures show posterior predictions and simulation envelopes. Simulation ground-truth parameters documented (P010) enabling recovery validation."

  execution_feasibility: "ready"
  feasibility_rationale: "All components present for reproduction attempt. Data accessible, code available and reviewed, workflow documented. Minor gap: would need to identify exact R package versions from repository. Priority 1 candidate for reproduction in Open Science Compliance Study."

  publication_year: 2024
  adoption_context: "early_majority"
```

---

## Cluster Synthesis

**Overall Reproducibility:** Strong

This paper achieves exemplary reproducibility, scoring 90/100 (Excellent band) on the standard pathway. It represents best practice for computational archaeology and could serve as a template for reproducible methodological papers.

The paper's reproducibility apparatus is notable for several reasons:

1. **Dual archival strategy** — GitHub provides a working repository for ongoing use and updates, while Zenodo provides permanent archival with DOI. This addresses both usability and preservation concerns.

2. **Independent code review** — The code was reviewed by Ben Marwick, demonstrating JAS's reproducibility review process in action. This adds confidence that the code actually runs and produces the claimed outputs.

3. **Pre-specified validation parameters** — The simulation validation (P010) specifies exact data-generating parameters, enabling reproduction to verify not just "does the code run?" but "does the code recover known parameters correctly?"

4. **Complete workflow documentation** — MCMC settings, prior specifications, calibration curve, and filtering criteria are fully documented, enabling step-by-step reproduction.

### Chronological Context

Publication year 2024 places this paper in the **early_majority** era of reproducibility adoption (2020-2025). In this era, data and code sharing are increasingly expected but not yet universal, and sophisticated reproducibility infrastructure (containerisation, automated workflows) is emerging. This paper exceeds era expectations by providing independent code review and dual archival — practices that will likely become standard in the mainstream era (post-2025).

### Gateway Assessment

**Execution Feasibility:** ready

This paper is **Priority 1 for reproduction attempt** in the Open Science Compliance Study. All components required for reproduction are present:

- **To attempt reproduction:**
  1. Clone repository from GitHub (or download Zenodo archive)
  2. Install R and required packages (identify from repository documentation)
  3. Download IntCal20 calibration curve
  4. Run simulation validation scripts — compare to P010 ground-truth parameters
  5. Run case study analyses — compare parameter estimates to Table 1
  6. Generate posterior predictive checks — compare to Figures 3-4
  7. Run ICAR analysis — compare cremation probability sequence to Figure 5

- **Expected effort:** Low-to-moderate. Code reviewed by expert, documentation comprehensive. Main uncertainty: package dependency resolution.

- **Verification targets:** Table 1 parameter estimates (r, m, mu, phi with HPD intervals); simulation parameter recovery (C003, C004 claims); posterior predictive check patterns.

---

## Structured Output

```yaml
cluster_3_reproducibility:
  paper_slug: "crema-et-al-2024"
  assessment_date: "2026-01-13"
  quality_state: "high"
  research_approach: "deductive"
  pathway: "standard"
  experimental: false

  reproducibility:
    score: 90
    band: "excellent"
    strengths:
      - "Dual archival (GitHub + Zenodo DOI) for working code and permanent preservation"
      - "Independent code review by Ben Marwick (JAS Reproducibility Specialist)"
      - "Complete MCMC specification enables exact reproduction"
      - "Pre-specified simulation parameters enable validation reproduction"
      - "Table 1 provides clear verification targets"
    weaknesses:
      - "R package dependencies/versions not explicitly listed in paper text"
      - "No containerised environment (Docker) for full environment specification"
    rationale: "Exemplary reproducibility. Complete data and code with DOIs. Independent code review. Workflow fully documented. FAIR principles substantially met. Minor gap on package version specification."
    tool_assessment:
      primary_tool_type: "open_scriptable"
      tool_impact: "Ideal — R scripts enable full reproduction"

  reproducibility_readiness:
    applies: true
    pathway: "standard"
    inputs_available:
      status: "yes"
      details: "All data on GitHub and Zenodo (DOI: 10.5281/zenodo.10782942)"
    code_available:
      status: "yes"
      tool_type: "open_scriptable"
      details: "R scripts available, independently reviewed by Ben Marwick"
    environment_specified:
      status: "partial"
      details: "R language and IntCal20 specified. MCMC settings explicit. Package versions need repository check."
    outputs_documented:
      status: "yes"
      details: "Table 1 parameter estimates with HPD intervals. Figures show expected outputs."
    execution_feasibility: "ready"
    feasibility_rationale: "All components present. Priority 1 for reproduction attempt."
    publication_year: 2024
    adoption_context: "early_majority"

  cluster_synthesis:
    overall_rating: "strong"
    chronological_interpretation: "Exceeds early_majority era expectations with independent code review and dual archival. Practices that will likely become standard in mainstream era."
    gateway_recommendation: "Priority 1 for reproduction attempt. Expected effort: low-to-moderate. Clear verification targets available."
```
