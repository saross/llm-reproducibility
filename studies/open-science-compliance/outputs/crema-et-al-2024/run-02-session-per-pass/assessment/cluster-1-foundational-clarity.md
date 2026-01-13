# Cluster 1: Foundational Clarity Assessment

**Paper:** crema-et-al-2024
**Assessment Date:** 2026-01-13
**Assessor Version:** v1.0

**Quality State:** HIGH
**Research Approach:** deductive (confidence: high)
**Paper Type:** methodological

---

## Signal Scores Summary

| Signal | Score | Band | Approach Anchors |
|--------|-------|------|------------------|
| Comprehensibility | 88 | Excellent | methodological |
| Transparency | 92 | Excellent | methodological |

**Cluster Rating:** Strong

---

## Signal 1: Comprehensibility

**Score:** 88/100 (Excellent)

**Approach anchors applied:** methodological (inductive anchors with technical specification emphasis)

### Assessment

This methodological paper demonstrates exemplary comprehensibility. All central methodological claims are explicit, bounded, and technically precise. The core contribution — a novel Bayesian framework for inferring diffusion curves from radiocarbon data — is clearly stated in the abstract and consistently elaborated throughout.

The argument structure is transparent and traceable: the paper moves logically from (1) identifying limitations of existing SPD-based approaches, to (2) developing two complementary statistical models (hierarchical parametric and ICAR non-parametric), to (3) validating these models on simulated data with known parameters, to (4) applying the validated methods to three empirical case studies. This deductive validation structure is explicit from the outset.

Technical terms are operationally defined. The paper explains the k parameter for site-specific probability caps, the phi parameter for inter-site variation, the ICAR random walk model, and posterior predictive checking — all with precise mathematical notation (equations 2-8). The dual-model approach is explicitly justified: parametric for hypothesis testing with numerical estimates, non-parametric for exploratory visual characterisation (C011).

### Evidence

**Strengths:**
- C001: "This paper introduces a novel Bayesian framework for inferring the shape of diffusion curves using radiocarbon data associated with the presence/absence of a particular innovation." — Core claim explicit, bounded, and unambiguous
- C011: "The parametric model can provide numerical estimates such as diffusion rate (r) or average diffusion cap (mu)... the non-parametric ICAR solution provides a visual descriptive tool" — Clear differentiation of complementary approaches
- RD002: "Two complementary models developed for different purposes: parametric hierarchical for hypothesis testing, non-parametric ICAR for exploratory analysis" — Design rationale explicit
- M001: Full mathematical specification with equations 5-8, explaining k parameter with Beta distribution for inter-site variation

**Weaknesses:**
- IA003: "The k parameter absorbs multiple sources of variation without distinguishing their relative contributions" — The paper acknowledges this transparently, but it does represent a comprehensibility gap in terms of interpretive precision. However, this is a limitation of the method rather than unclear exposition.

### Scoring Rationale

Score of 88 (Excellent for methodological). Technical specification clarity is exemplary — all mathematical components are defined with equations. Design rationale is explicit throughout, explaining why two complementary approaches were developed and when each is appropriate. Feature descriptions are precisely bounded (e.g., C012 states posterior predictive checking is "robust if not conservative"). The paper meets all criteria for 80-100 band: research goals explicit, pattern descriptions clear and well-bounded, key terms defined, logical progression transparent.

---

## Signal 2: Transparency

**Score:** 92/100 (Excellent)

**Approach anchors applied:** methodological

### Assessment

This paper achieves exemplary transparency for a methodological paper, meeting or exceeding all criteria for the Excellent band. The statistical framework is fully documented with complete mathematical specification (equations 2-8), explicit prior specifications, MCMC settings, and validation procedures.

The code and data are publicly available through dual archival: GitHub repository (https://github.com/ercrema/diffusionCurve) and permanently archived on Zenodo with DOI (10.5281/zenodo.10782942). Crucially, the computational code was independently reviewed by Ben Marwick, the Journal of Archaeological Science's Reproducibility Specialist, adding an unusual layer of verification.

All design decisions are documented with rationale. The paper explains why probabilistic equations 2-3 are preferred over equation 1 for archaeological small samples (C010, RD004). Protocol documentation is comprehensive: MCMC settings specify chains, iterations, burn-in, thinning (P001, P004); prior specifications are explicit (P002); calibration curve is documented (P003 - IntCal20); simulation parameters are pre-specified with exact values (P010). Case study filtering criteria are transparent with probability thresholds for each dataset (P007-P009).

### Evidence

**From reproducibility_infrastructure:**
- Code availability: statement_present = true; repository = GitHub + Zenodo; access_conditions = open; code_reviewed = true (Ben Marwick)
- Data availability: statement_present = true; repository = GitHub + Zenodo; persistent_archive = DOI 10.5281/zenodo.10782942
- Persistent identifiers: code_doi = 10.5281/zenodo.10782942; paper_doi = 10.1016/j.jas.2024.105962

**Strengths:**
- P002: "r ~ Exponential(100) ... mu ~ Beta(2, 2) ... phi ~ Gamma(5, 0.1)" — Prior specifications fully documented
- P001: "four chains, each with 1 million iterations (half discarded as burn-in) and with thinning set to 50" — MCMC settings explicit
- P010: "r = 0.01, m = 2900 BP, mu = 0.65, phi = 50" — Simulation parameters pre-specified with exact data-generating values
- P006: Convergence diagnostics documented (Gelman-Rubin statistic, agreement indices)
- Code review: "Ben Marwick for reviewing the computational code and providing suggestions to improve its reproducibility" (Acknowledgements)

**Weaknesses:**
- No author ORCIDs visible (journal display limitation, not author choice — noted in pid_graph)
- Infrastructure section notes funder ROR IDs and institution ROR IDs not present, reducing PID graph connectivity (3/6)

### Scoring Rationale

Score of 92 (Excellent for methodological). Paper meets all criteria for 80-100 band: software/method architecture fully documented with mathematical specification; design decisions explained with clear rationale (why two complementary approaches, why probability-based over proportion-based); code publicly available with open source licence (CC BY) and independent code review; validation approach explicit with simulation-based testing before empirical application; dependencies documented (R implementation, IntCal20 calibration curve). Minor deduction for PID graph incompleteness (no author ORCIDs or funder RORs), which is largely outside author control.

---

## Cluster Synthesis

**Overall Foundational Clarity:** Strong

Both Comprehensibility (88) and Transparency (92) score in the Excellent band, indicating exemplary foundational clarity. This paper represents best practice for methodological paper documentation in computational archaeology.

The high scores are consistent and mutually reinforcing: clear technical specification enables transparency about what the methods do, and comprehensive documentation enables others to understand both the conceptual framework and the implementation details. The paper's transparency is not merely compliant with open science requirements but genuinely informative — readers can trace the complete pathway from theoretical motivation through mathematical formulation to implementation details and validation results.

### Pattern Summary

The paper exhibits a coherent pattern of methodological transparency. Both signals indicate that:
1. The research goals are explicit and achievable
2. The approach is well-justified with clear rationale
3. The technical details are fully documented
4. The validation strategy is principled and pre-specified
5. The materials are accessible for independent verification

The implicit arguments extracted (IA001-IA003) represent methodological acknowledgements rather than transparency gaps — the paper explicitly states the limitations these represent.

### Implications for Subsequent Assessment

- **For Cluster 2 (Evidential Strength):** High foundational clarity enables confident evaluation of evidential strength. The clear claim structure allows precise assessment of evidence-claim relationships. The deductive validation approach (simulation testing with known parameters before empirical application) provides strong basis for validity assessment.

- **For Cluster 3 (Reproducibility):** Exceptional transparency directly supports reproducibility. With GitHub+Zenodo archival, independent code review, full MCMC specification, and explicit simulation parameters, this paper is an ideal candidate for reproduction attempt. The Standard Reproducibility pathway is appropriate (computational paper with accessible code+data).

---

## Structured Output

```yaml
cluster_1_foundational_clarity:
  paper_slug: "crema-et-al-2024"
  assessment_date: "2026-01-13"
  quality_state: "high"
  research_approach: "deductive"

  comprehensibility:
    score: 88
    band: "excellent"
    strengths:
      - "Core methodological claims explicit and bounded (C001, C002)"
      - "Technical terms operationally defined with equations (k parameter, ICAR, posterior predictive)"
      - "Clear argument structure: limitation identification → method development → validation → application"
      - "Dual-model rationale explicit (C011 - parametric for hypothesis testing, non-parametric for exploration)"
    weaknesses:
      - "k parameter absorbs multiple variation sources without distinguishing them (acknowledged limitation, not unclear exposition)"
    rationale: "Exemplary technical specification clarity. All mathematical components defined with equations. Design rationale explicit throughout. Meets all 80-100 band criteria for methodological paper."

  transparency:
    score: 92
    band: "excellent"
    strengths:
      - "Full mathematical specification (equations 2-8)"
      - "Code publicly available with dual archival (GitHub + Zenodo DOI)"
      - "Independent code review by Ben Marwick (JAS Reproducibility Specialist)"
      - "MCMC settings, prior specifications, simulation parameters all explicit (P001, P002, P010)"
      - "Validation approach pre-specified (simulation testing before empirical application)"
    weaknesses:
      - "PID graph incomplete (no ORCIDs, no funder RORs) - largely outside author control"
    rationale: "Meets all 80-100 band criteria for methodological paper. Architecture documented, design decisions explained, code available and reviewed, validation explicit, dependencies documented."

  cluster_synthesis:
    overall_rating: "strong"
    pattern_summary: "Coherent pattern of exemplary methodological transparency. Clear technical specification enables transparency about methods; comprehensive documentation enables understanding of both framework and implementation."
    consistency_check: "consistent"
    implications:
      cluster_2: "High foundational clarity enables confident evidential strength evaluation. Clear claim structure supports evidence-claim relationship assessment."
      cluster_3: "Exceptional transparency directly supports reproducibility. Ideal candidate for reproduction attempt with accessible code+data and pre-specified validation parameters."
```
