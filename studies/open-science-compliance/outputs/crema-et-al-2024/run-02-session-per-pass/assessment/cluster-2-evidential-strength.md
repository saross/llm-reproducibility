# Cluster 2: Evidential Strength Assessment

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
| Plausibility | 82 | Excellent | deductive |
| Validity | 85 | Excellent | deductive |
| Robustness | 75 | Good | deductive |
| Generalisability | 78 | Good | deductive |

**Cluster Rating:** Strong

---

## Signal 3: Plausibility

**Score:** 82/100 (Excellent)

**Approach anchors applied:** deductive

### Assessment

The methodological framework demonstrates excellent plausibility. The paper is grounded in established diffusion of innovation theory and addresses well-known limitations of existing SPD-based approaches to radiocarbon proportion modelling. The statistical foundation — hierarchical Bayesian modelling with site-specific probability parameters — follows from coherent statistical theory.

The three empirical case studies are drawn from well-established research contexts: rice diffusion in Japan and the spread of agriculture in Britain are among the most intensively studied episodes in archaeological radiocarbon research. The theoretical motivation for the dual-model approach (parametric for hypothesis testing, non-parametric for exploration) is coherent with statistical practice.

Anomalous results are handled appropriately. When posterior predictive checks revealed poor fit for the Japanese and British agriculture datasets (C005), the paper interprets these deviations rather than dismissing them. The Japanese double s-shape is explained by documented regional accelerations and slowdowns in rice dispersal (C006). British deviations are connected to established research showing temporary shifts to pastoralism (C007). The cremation case study reveals unexpected two-cycle pattern that the paper contextualises within Late Neolithic and Bronze Age mortuary practices (C008, C009).

### Evidence

**Strengths:**
- C002: "Our solution overcomes several problems that affect current approaches based on SPDs, including sampling error, calibration-based artefacts, and overdispersion" — Addresses established methodological problems
- RD004: Shift from proportion-based to probability-based framework explicitly grounded in statistical theory for small samples
- C006: Double s-shape in Japan explained by "episodes of significant regional accelerations and slowdowns" — Anomaly contextualised within established literature
- C008: Cremation decline "pre-dates Beaker inhumation practices in Britain by several centuries, suggesting... endogenous factors" — Unexpected finding interpreted cautiously

**Weaknesses:**
- IA002: "Direct dating of domesticates is an adequate proxy for farming practice adoption" — Acknowledged proxy assumption that seed presence equals farming adoption; potential bias from differential preservation
- IA003: The k parameter absorbs multiple sources of variation (taphonomy, sampling, behaviour) without distinguishing their relative contributions — limits interpretive precision

### Scoring Rationale

Score of 82 (Excellent for deductive). Hypotheses are grounded in established statistical theory and archaeological research (80-100 criterion). Predictions are consistent with domain knowledge — the case studies draw from well-researched contexts. Anomalous results are explicitly acknowledged and explained with reference to established literature (80-100 criterion). The theoretical framework is coherent, following standard Bayesian hierarchical modelling practice. The paper falls short of higher scores because the proxy assumptions (IA002) and conflation of variation sources (IA003), while acknowledged, do represent auxiliary assumptions that affect certainty of interpretation.

---

## Signal 4: Validity

**Score:** 85/100 (Excellent)

**Approach anchors applied:** deductive (validation approach for methodological paper)

### Assessment

The validation strategy is exemplary. The paper employs pre-specified simulation testing with known parameters to establish method validity before empirical application — a paradigmatic deductive validation approach.

Evidence directly addresses the methodological hypotheses. The simulation validation (M004, RD003) tests whether the models can accurately recover known parameter values (r, m, mu, phi) when dealing with sample sizes comparable to the empirical case studies. This directly tests the core methodological claims: C003 states "Our hierarchical approach was able to accurately recover the shape of the diffusion curve in both simulated datasets, with the 'true' curve within the 95% posterior fitted range." C004 confirms the ICAR model "successfully recovered the 'true' time-sequence."

Sample adequacy is established through simulation design. The simulation datasets were generated with "sample sizes and time-windows equivalent to each observed dataset" (IA001). This doesn't fully capture real-world complexity (taphonomy, sampling bias) but does establish internal consistency.

Methods are appropriate for the research questions. The hierarchical Bayesian approach (M001) addresses inter-site variation through site-specific k parameters. The ICAR approach (M002) provides model-free estimation for complex dynamics. Posterior predictive checking (M003) provides conservative detection of model-data mismatch.

### Evidence

**Strengths:**
- RD003: "Simulation-based validation to establish method robustness before empirical application" — Pre-specified validation sequence
- C003: "Our hierarchical approach was able to accurately recover the shape of the diffusion curve" — Evidence directly addresses methodological hypothesis
- P010: Simulation parameters pre-specified (r=0.01, m=2900 BP, mu=0.65, phi=50; r=0.008, m=4500 BP, mu=0.8, phi=40) — Known-truth testing
- C012: "This approach makes the posterior predictive check a reasonably robust, if not conservative, solution" — Conservative model assessment

**Weaknesses:**
- IA001: "Sample sizes validated in simulation are adequate for empirical inference despite real-world complexities" — Simulation validation establishes internal consistency but cannot capture archaeological realities (taphonomy, sampling bias)
- The parametric model's assumption of s-shaped diffusion is tested and shown to fail in both agricultural case studies — while this is correctly identified through posterior predictive checking, it means the parametric model's parameter estimates should be interpreted cautiously

### Scoring Rationale

Score of 85 (Excellent for deductive). Evidence directly addresses methodological hypotheses through simulation testing with pre-specified parameters (80-100 criterion). Sample adequacy is established for model testing purposes through matched simulation design. Methods are appropriate — hierarchical Bayesian for overdispersion, ICAR for model-free exploration, posterior predictive for conservative validation. Alternative approaches are tested through the dual-model design. Limitations are explicitly stated (IA001-IA003). Score reflects that simulation validation, while rigorous, doesn't fully capture archaeological complexity — this is acknowledged and appropriate.

---

## Signal 5: Robustness

**Score:** 75/100 (Good)

**Approach anchors applied:** deductive

### Assessment

The paper demonstrates good robustness through methodological triangulation and systematic validation, though without comprehensive sensitivity analysis across all analytical choices.

The dual-model approach (M001 parametric, M002 ICAR non-parametric) provides methodological triangulation. Results are interpreted through both lenses: parametric estimates provide numerical values for hypothesis testing, while ICAR provides visual exploration without imposing sigmoid assumptions. This complementary approach guards against single-method dependency.

Simulation validation (M004) tests parameter recovery under known conditions. The hierarchical model accurately recovered diffusion curve shape in both simulations (C003), and ICAR successfully recovered the time-sequence (C004). This establishes that the methods function as intended under controlled conditions.

Convergence diagnostics (P006) include Gelman-Rubin statistics for parameter mixing and agreement indices for individual date posteriors. MCMC settings (P001, P004) specify sufficient iterations (4 chains × 1M iterations for hierarchical; 4 × 100K for ICAR) with appropriate burn-in and thinning.

However, comprehensive sensitivity analysis to analytical choices is not documented. The paper doesn't systematically vary prior specifications, time-block widths, or probability thresholds to assess result sensitivity. The filtering thresholds (0.5 for seeds, 0.99 for burials) are stated but alternatives aren't tested.

### Evidence

**Strengths:**
- RD002: "Two complementary models developed for different purposes" — Dual-model triangulation guards against single-method dependency
- M004: Simulation-based validation establishes parameter recovery under known conditions
- P006: "Gelman-Rubin statistic... agreement indices" — Convergence diagnostics documented
- C003, C004: Both models recover known parameters in simulation — internal validity established

**Weaknesses:**
- No systematic sensitivity analysis varying prior specifications (P002)
- Time-block width (100 years for ICAR) not tested against alternatives
- Filtering threshold choices (0.5, 0.99) stated but not sensitivity-tested

### Scoring Rationale

Score of 75 (Good for deductive). Some sensitivity analysis is present through simulation validation and convergence diagnostics (60-79 criterion). Results appear robust across the two alternative approaches (60-79 criterion). Assumptions are stated with mathematical precision (60-79 criterion met, would need testing for 80-100). Dependencies documented via MCMC settings and prior specifications. The dual-model approach provides robustness evidence through triangulation. Score reflects that while validation is rigorous, comprehensive sensitivity analysis varying analytical choices is not systematically documented.

---

## Signal 7: Generalisability

**Score:** 78/100 (Good)

**Approach anchors applied:** deductive (methodological paper)

### Assessment

The paper demonstrates good generalisability with clear scope boundaries and appropriate qualification of both methodological and empirical claims.

Scope boundaries are explicit. The method is designed for "inferring the shape of diffusion curves using radiocarbon data associated with the presence/absence of a particular innovation" — a bounded methodological scope. Case studies are explicitly bounded: Japan (4000-1700 cal BP, excluding Hokkaido and Ryukyu islands, P007), British seeds (7000-3000 cal BP, P008), British burials (5500-2000 cal BP, P009).

Transfer conditions for the method are specified. The R implementation is publicly available, documented for use with different datasets. The paper states when each model is appropriate: "parametric model can provide numerical estimates... to evaluate specific hypotheses... non-parametric ICAR solution provides a visual descriptive tool that may be used to characterise more complex diffusion dynamics" (C011).

Limitations are acknowledged. IA001 notes simulation validation doesn't fully capture real-world complexity. IA002 notes the proxy assumption linking seed dates to farming practice. IA003 notes the k parameter absorbs multiple variation sources without distinguishing them. The parametric model's sigmoid assumption is shown to be violated in both agricultural case studies — this limitation is documented through posterior predictive checking.

### Evidence

**Strengths:**
- RD001: Method designed for specific scope — "diffusion of innovation curves from radiocarbon data"
- C011: Transfer conditions specified — parametric for hypothesis testing, non-parametric for exploration
- P007-P009: Case study boundaries explicit (temporal windows, geographic exclusions)
- IA001-IA003: Methodological limitations acknowledged

**Weaknesses:**
- Empirical interpretations (C006-C009) draw on established literature but the findings themselves are specific to these case studies
- Method assumes binary classification of samples (x=1 domesticate, x=0 wild) — may not generalise to all innovation diffusion scenarios

### Scoring Rationale

Score of 78 (Good for deductive). Scope of methodological contribution is clearly bounded (60-79 criterion met). Limitations to external validity are stated through the implicit arguments (60-79 criterion). Population, context, and temporal bounds are clear for each case study (60-79 criterion met). Extrapolations are qualified — the paper doesn't overclaim generality from the case studies. Transfer conditions are specified through documentation and code availability (60-79 criterion). Score reflects good but not exhaustive generalisability discussion — the method's applicability to other innovation types beyond the binary presence/absence framework isn't fully explored.

---

## Cluster Synthesis

**Overall Evidential Strength:** Strong

The paper demonstrates strong evidential strength across all four signals. Plausibility (82) and Validity (85) score in the Excellent band, reflecting the paper's rigorous theoretical grounding and principled validation strategy. Robustness (75) and Generalisability (78) score in the Good band, indicating solid but not exceptional performance in these areas.

The signal pattern reveals a coherent credibility profile appropriate for a methodological paper with deductive validation. The strengths cluster around what methodological papers should excel at: theoretical coherence (Plausibility), pre-specified validation (Validity), and appropriate scope claims (Generalisability). The slightly lower Robustness score reflects the common trade-off in methodological papers between demonstrating that a new method works and exhaustively testing sensitivity to all choices.

### Pattern Summary

The four signals show consistent performance in the Good-to-Excellent range (75-85), with no weak signals. The pattern indicates:

1. **Theoretical foundation is sound** — method addresses known SPD limitations using established statistical theory
2. **Validation strategy is rigorous** — simulation with known parameters before empirical application represents best practice
3. **Analytical robustness is demonstrated but not exhaustively** — dual-model triangulation provides evidence, but sensitivity analysis to prior choices is limited
4. **Scope claims are appropriately bounded** — both method and case studies are clearly delimited with acknowledged limitations

### Implications for Cluster 3

- **For Reproducibility:** Strong evidential strength supports high reproducibility expectations. The validation strategy with pre-specified simulation parameters means reproduction attempts have clear targets — can the published results be regenerated? The dual-model approach provides multiple outputs that could be checked (parametric parameter estimates and ICAR probability sequences). The explicit MCMC settings, convergence diagnostics, and filtering criteria provide a roadmap for reproduction.

---

## Structured Output

```yaml
cluster_2_evidential_strength:
  paper_slug: "crema-et-al-2024"
  assessment_date: "2026-01-13"
  quality_state: "high"
  research_approach: "deductive"

  plausibility:
    score: 82
    band: "excellent"
    strengths:
      - "Grounded in established diffusion theory and addresses known SPD limitations"
      - "Case studies in well-researched contexts (Japan rice, Britain agriculture/burials)"
      - "Anomalous results acknowledged and explained (C005-C009)"
      - "Theoretical framework coherent with statistical practice"
    weaknesses:
      - "Proxy assumption (seed dates = farming practice) acknowledged but not quantified (IA002)"
      - "k parameter conflates multiple variation sources (IA003)"
    rationale: "Hypotheses grounded in established theory. Predictions consistent with domain knowledge. Anomalies explicitly acknowledged and contextualised. Framework coherent."

  validity:
    score: 85
    band: "excellent"
    strengths:
      - "Pre-specified simulation validation with known parameters (RD003, P010)"
      - "Evidence directly addresses methodological hypotheses (C003, C004)"
      - "Methods appropriate — hierarchical for overdispersion, ICAR for model-free exploration"
      - "Posterior predictive checking provides conservative model assessment (C012)"
    weaknesses:
      - "Simulation validation captures internal consistency, not archaeological complexity (IA001)"
      - "Parametric model's sigmoid assumption fails in both agricultural cases"
    rationale: "Evidence directly addresses methodological hypotheses through simulation testing. Sample adequacy established for model testing. Methods appropriate. Limitations stated."

  robustness:
    score: 75
    band: "good"
    strengths:
      - "Dual-model approach provides methodological triangulation"
      - "Simulation validation establishes parameter recovery"
      - "Convergence diagnostics documented (Gelman-Rubin, agreement indices)"
    weaknesses:
      - "No systematic sensitivity analysis varying prior specifications"
      - "Time-block width and filtering thresholds not sensitivity-tested"
    rationale: "Some sensitivity analysis through simulation and convergence diagnostics. Results appear robust across dual approaches. Comprehensive sensitivity to analytical choices not documented."

  generalisability:
    score: 78
    band: "good"
    strengths:
      - "Method scope clearly bounded to radiocarbon proportion modelling"
      - "Case study boundaries explicit (temporal windows, geographic exclusions)"
      - "Transfer conditions specified through documentation and code"
      - "Limitations acknowledged (IA001-IA003)"
    weaknesses:
      - "Method applicability beyond binary presence/absence not explored"
      - "Empirical findings specific to case studies"
    rationale: "Scope boundaries clear. Limitations stated. Transfer conditions documented. Extrapolations qualified. Not exhaustive generalisability discussion."

  cluster_synthesis:
    overall_rating: "strong"
    pattern_summary: "Consistent Good-to-Excellent performance (75-85) across all signals. Strengths in theoretical foundation and validation strategy appropriate for methodological paper. Robustness slightly lower reflecting common methodological paper trade-off."
    consistency_check: "consistent"
    implications:
      cluster_3: "Strong evidential strength supports high reproducibility expectations. Pre-specified validation parameters provide clear reproduction targets. Dual-model outputs enable multiple verification points."
```
