# Cluster 2: Evidential Strength Assessment

**Paper:** marwick-2025
**Assessment Date:** 2026-01-14
**Assessor Version:** v1.0

**Quality State:** HIGH
**Research Approach:** inductive (confidence: high)
**Paper Type:** meta_research

---

## Signal Scores Summary

| Signal | Score | Band | Approach Anchors |
|--------|-------|------|------------------|
| Plausibility | 80 | excellent | inductive |
| Validity | 78 | good | inductive |
| Robustness | 68 | good | inductive |
| Generalisability | 75 | good | inductive |

**Cluster Rating:** Strong

---

## Signal 3: Plausibility

**Score:** 80/100 (excellent)

**Approach anchors applied:** inductive

### Assessment

The paper demonstrates excellent plausibility for inductive meta-research. Observed patterns are firmly grounded in established frameworks. The bibliometric component adopts the validated Fanelli & Glänzel (2013) framework for measuring field hardness/softness (RD002, C007). This framework has empirical support from prior research across 12 disciplines, providing strong theoretical grounding for the five bibliometric variables (author count, article length, title length, reference recency, reference diversity).

Patterns identified are consistent with known regional and disciplinary frameworks. The finding that archaeology sits between natural and social sciences (C001, C017) aligns with longstanding debates about archaeology's scientific status. The paper acknowledges this context explicitly: "these debates... have become a genre in archaeological writing" (C006). Individual variable results (E007-E010) position archaeology reasonably relative to established benchmarks from physics, social sciences, and humanities.

Anomalies are acknowledged and contextualised rather than ignored. The Journal of Cultural Heritage outlier is explained through its distinct focus on conservation science without engagement with "anthropological topics" (C024). The Journal of Archaeological Research's soft ranking is contextualised as predictable for review journals (C025). Mixed temporal trends (C019, C020) are reported transparently rather than cherry-picked for a single narrative.

One theoretical assumption warrants attention: IA001 notes that the link between bibliometric variables and "consensus" (the theoretical construct) is assumed rather than demonstrated. The paper follows Fanelli & Glänzel without independently validating that these specific bibliometric proxies capture consensus formation. This represents a moderate transparency gap for theoretical grounding, though it follows established meta-research practice.

### Evidence

**Strengths:**
- RD002: "Fanelli and Glänzel (2013)... examined the hardness and softness of 12 disciplines using scholarly publication parameters" - established framework provides theoretical grounding
- C024: Journal of Cultural Heritage outlier "typically do not engage in questions or debates about past human behavior or culture" - anomaly acknowledged and explained
- C022: "r-squared values are very low, demonstrating that much of the variability in these metrics is independent of time" - inconvenient finding reported transparently
- E007-E010: Comparative positioning across five variables provides convergent evidence for intermediate position

**Weaknesses:**
- IA001: "bibliometric variables accurately capture 'hardness/softness' as a meaningful scientific construct" - theoretical link assumed
- IA002: 28% reproducibility characterised as "low end" requires implicit threshold judgment
- Limited discussion of whether Fanelli & Glänzel disciplines are appropriate comparators for archaeology

### Scoring Rationale

Score of 80 (lower Excellent for inductive) reflects: observed patterns consistent with established frameworks (80-100 criterion met), classifications follow established conventions via Fanelli & Glänzel (80-100), anomalies acknowledged and contextualised (80-100), interpretations grounded in comparative data (80-100). Score at threshold of excellent band due to implicit assumption about bibliometric-consensus validity (IA001) and limited explicit theoretical defence of framework appropriateness for archaeology.

---

## Signal 4: Validity

**Score:** 78/100 (good)

**Approach anchors applied:** inductive

### Assessment

The paper demonstrates good validity for pattern claims in both components. Data are sufficient and representative for the bibliometric component. The sample of 9,697 papers from 20 journals over 50 years (E004) provides substantial coverage for identifying disciplinary patterns. The sampling is systematic with explicit criteria: Web of Science category "Archaeology", document type "article", filtered to top 25 journals by h-index, then to journals with ≥100 articles (M002, RD005).

The reproducibility review component has a smaller but adequate sample. 47 reviews of 25 manuscripts (E002) is sufficient to identify common failure modes, though limited for precise rate estimation. The paper acknowledges different denominators produce different rates (28% of eligible, 63% of submitting, 7% of all articles), providing appropriate context for interpretation.

Methods are appropriate for pattern-finding in meta-research. Bibliometric variables follow established operationalisations (M001, P002-P009). Statistical methods include Bayesian GAMs for temporal trends (M003), PCA for comparative positioning (M005), and Kendall's W for concordance (E015). These are appropriate for exploratory description.

Some limitations are acknowledged but incompletely. Low r-squared values are reported transparently (E013, C21-C22), appropriately tempering trend claims. However, IA004 notes that h-index journal selection may systematically exclude non-Anglophone, regional, or innovative work, which could affect representativeness claims. The single-reviewer protocol for reproducibility reviews (IA003) is not discussed as a potential validity threat.

### Evidence

**Strengths:**
- E004: "9697 papers published during 1975–2025" - substantial sample for pattern claims
- M002: Systematic WoS query with explicit filtering criteria
- E015: "Kendall's coefficient of concordance (Wt) value of 0.64" - statistical validation of variable agreement
- C021-C022: Low r-squared values reported transparently, tempering over-interpretation

**Weaknesses:**
- IA003: Single reviewer reproducibility reviews with no inter-rater reliability assessment
- IA004: H-index selection may exclude innovative/regional work from sample
- E002: Only 25 manuscripts for reproducibility review component
- No formal sampling frame for which papers receive reproducibility review (self-selected by author submission)

### Scoring Rationale

Score of 78 (Good for inductive) reflects: data sufficient for main patterns (60-79 criterion fully met, approaching 80-100), sampling systematic with documented criteria (60-79+), coverage adequate for disciplinary claims (60-79), some alternatives considered (C024, C025 discuss outliers). Score in upper Good band because systematic sampling is well-documented, but single-reviewer reproducibility assessment and potential h-index selection bias limit validity for some claims.

---

## Signal 5: Robustness

**Score:** 68/100 (good)

**Approach anchors applied:** inductive

### Assessment

The paper demonstrates good robustness for the bibliometric component but limited robustness evidence for the reproducibility component. The five bibliometric variables provide methodological triangulation, with patterns converging from multiple indicators (E007-E010). Kendall's coefficient of concordance (Wt = 0.64) demonstrates that variables agree in ranking journals on the hard-soft spectrum (E015). This represents meaningful convergent evidence.

Multiple statistical approaches are used. Bayesian GAMs assess temporal trends (M003), PCA visualises journal positioning (M005), and concordance statistics assess variable agreement. The low r-squared values (E013) are reported rather than hidden, demonstrating that temporal trends explain little variance. This represents appropriate robustness acknowledgment.

Pattern identification uses multiple classification schemes. Journal rankings are assessed by individual variables (Figure 3 panels A-E) and by consensus ranking (Figure 3F). PCA reveals distinct communities of practice (C026). However, no formal sensitivity analysis tests whether patterns change under different analytical choices (e.g., different journal selection thresholds, different time periods).

The reproducibility review component has limited robustness evidence. Issue categorisation was performed by a single reviewer with no documented inter-coder reliability (RD007 implicit, M-IMP-001). Category definitions (incomplete compendium, dependencies, path errors, function errors) are not operationally defined. Success criteria distinguishing "first attempt" from "required additional input" are not specified (P-IMP-001). This reduces confidence in the reproducibility failure taxonomy.

### Evidence

**Strengths:**
- E015: Wt = 0.64 concordance demonstrates variable agreement
- E007-E010: Five variables provide convergent evidence for intermediate positioning
- E013: Low r-squared values transparently reported
- M003, M005: Multiple statistical approaches (GAMs, PCA, concordance)

**Weaknesses:**
- RD007: Issue taxonomy development methodology undocumented
- IA003: Single-reviewer reproducibility assessment with no reliability check
- P-IMP-001: Success criteria for "first attempt" vs "required input" not defined
- No formal sensitivity analysis for journal selection threshold or time period choices

### Scoring Rationale

Score of 68 (Good for inductive) reflects: some methodological triangulation present (60-79 criterion met), main patterns appear robust across bibliometric variables (60-79), some reliability evidence via concordance statistic (60-79). Score in middle of Good band because five-variable convergence and concordance provide meaningful robustness evidence, but single-reviewer reproducibility categorisation without reliability assessment represents significant robustness gap for that component.

---

## Signal 7: Generalisability

**Score:** 75/100 (good)

**Approach anchors applied:** inductive

### Assessment

The paper demonstrates good generalisability through explicit scope boundaries and prominent limitation acknowledgments. Pattern claims are explicitly bounded to sampled journals and time periods. The bibliometric sample is bounded to "top-ranking 25 journals according to their h-indices" (RD005), with explicit filtering to 20 journals with ≥100 articles. Temporal bounds are explicit (1975-2025). These constraints are prominently stated in Methods.

The paper provides thoughtful discussion of reproducibility applicability limits. Section 7 explicitly addresses "What about qualitative research in archaeology?" (C063-C068), acknowledging that computational reproducibility is not universally applicable. The paper distinguishes between reproducibility (same data/code) and replication (new data/methods), noting that qualitative research is oriented toward the latter (C067). C076 explicitly states: "Computational reproducibility is not a panacea; it should not be used as a universally accepted criterion for research quality."

Sampling limitations are partially acknowledged. IA004 identifies that h-index selection may exclude "innovative, regional, or non-Anglophone work" that is "less cited but still represents archaeological practice." However, this limitation is implicit rather than prominently discussed in the paper's limitations section. The paper focuses on mainstream Anglophone archaeology without explicitly noting the scope constraint.

Extrapolations are generally qualified. Core claims about archaeology's position (C001, C017, C070) are bounded to "on average" and qualified by acknowledging within-field variation (C069, C071). Recommendations for reproducibility practices (C048-C062) are framed as applicable to quantitative research specifically.

### Evidence

**Strengths:**
- RD005: Explicit journal selection criteria with bounded scope
- C076: "Computational reproducibility is not a panacea" - explicit limitation
- C063-C068: Extensive discussion of qualitative research applicability
- C070: "On average we generally behave as social scientists" - appropriately qualified

**Weaknesses:**
- IA004: H-index selection bias not prominently discussed as limitation
- No explicit discussion of non-Anglophone archaeology exclusion
- Reproducibility rates from single journal (JAS) may not generalise
- Regional/sub-disciplinary variation not systematically addressed

### Scoring Rationale

Score of 75 (Good for inductive) reflects: pattern claims bounded by geography/temporal scope (60-79 criterion met, approaching 80-100 for explicit time bounds), sampling limitations acknowledged via qualitative research discussion (60-79+), scope generally matched to coverage (60-79), extrapolations qualified (60-79). Score in upper Good band due to explicit Section 7 discussion of applicability limits and qualified core claims, but not Excellent due to insufficient discussion of Anglophone/h-index scope constraints.

---

## Cluster Synthesis

**Overall Evidential Strength:** Strong

This paper demonstrates strong evidential strength across the Credibility pillar. All four signals score in the Good-to-Excellent range (68-80), with no weak signals that would undermine overall credibility. The pattern is internally consistent: stronger scores for theoretical grounding (Plausibility 80) than for methodological robustness of the reproducibility component (Robustness 68).

The two-component structure creates natural variation in signal strength. The bibliometric component is methodologically stronger: established framework, large sample, multiple variables providing triangulation, systematic sampling. The reproducibility review component is smaller and less methodologically rigorous: single reviewer, undocumented categorisation, self-selected sample. This asymmetry is reflected in the Robustness score (68), which is constrained by the weaker component.

The paper's self-awareness about limitations is a credibility strength. Explicit acknowledgment that reproducibility is "not a panacea" (C076), extensive discussion of qualitative research applicability (Section 7), and transparent reporting of weak temporal effects (C21-C22) demonstrate appropriate epistemic humility for inductive research.

### Pattern Summary

All four signals cluster in the Good-to-Excellent range, indicating consistent credibility across dimensions. Plausibility (80) is highest, reflecting strong theoretical grounding in established frameworks. Robustness (68) is lowest, reflecting the single-reviewer reproducibility component. Validity (78) and Generalisability (75) are solidly Good, reflecting systematic methods with acknowledged scope constraints. The pattern suggests credible meta-research with stronger bibliometric component and weaker but adequate reproducibility review component.

### Implications for Cluster 3

- **For Reproducibility:** Strong foundational infrastructure (93.75% FAIR from Cluster 1) combined with Good-Excellent evidential strength suggests high potential for computational reproduction. The paper's own research compendium exemplifies the practices it advocates. However, the single-reviewer protocol identified in Robustness assessment (IA003) suggests that reproducibility assessment is a human judgment process that may vary across reviewers. This affects interpretation of the reproducibility signal: the paper's own code should be reproducible, but the reproducibility review findings reflect one expert's judgment.

---

## Structured Output

```yaml
cluster_2_evidential_strength:
  paper_slug: "marwick-2025"
  assessment_date: "2026-01-14"
  quality_state: "high"
  research_approach: "inductive"

  plausibility:
    score: 80
    band: "excellent"
    strengths:
      - "Established Fanelli & Glänzel (2013) framework provides theoretical grounding"
      - "Anomalies acknowledged and contextualised (C024, C025)"
      - "Inconvenient findings reported transparently (C021-C022)"
    weaknesses:
      - "Bibliometric-consensus link assumed not validated (IA001)"
      - "28% threshold characterisation implicit (IA002)"
    rationale: "Patterns consistent with established frameworks; anomalies explained; interpretations grounded in comparative data. Score at excellent threshold due to implicit theoretical assumptions."

  validity:
    score: 78
    band: "good"
    strengths:
      - "Large bibliometric sample (9,697 papers, 50 years, 20 journals)"
      - "Systematic WoS query with explicit criteria"
      - "Multiple statistical approaches (GAMs, PCA, concordance)"
    weaknesses:
      - "Single-reviewer reproducibility assessment (IA003)"
      - "H-index selection may exclude regional/innovative work (IA004)"
      - "Small reproducibility sample (25 manuscripts)"
    rationale: "Data sufficient for main patterns; sampling systematic; coverage adequate. Upper Good band due to systematic documentation offset by single-reviewer limitation."

  robustness:
    score: 68
    band: "good"
    strengths:
      - "Five bibliometric variables provide triangulation"
      - "Concordance statistic (Wt=0.64) validates variable agreement"
      - "Low r-squared values transparently reported"
    weaknesses:
      - "No inter-rater reliability for reproducibility categorisation"
      - "Issue taxonomy methodology undocumented"
      - "No formal sensitivity analysis"
    rationale: "Bibliometric component robust via triangulation; reproducibility component lacks reliability evidence. Middle Good band reflects asymmetric component robustness."

  generalisability:
    score: 75
    band: "good"
    strengths:
      - "Explicit scope boundaries (h-index journals, 1975-2025)"
      - "Extensive applicability discussion (Section 7 on qualitative research)"
      - "Claims appropriately qualified ('on average')"
    weaknesses:
      - "H-index selection bias not prominently discussed"
      - "Anglophone focus not explicitly acknowledged"
      - "JAS-only reproducibility rates may not generalise"
    rationale: "Pattern claims bounded; sampling limitations partially acknowledged; extrapolations qualified. Upper Good band due to explicit applicability discussion."

  cluster_synthesis:
    overall_rating: "strong"
    pattern_summary: "All signals Good-to-Excellent (68-80). Bibliometric component methodologically stronger than reproducibility review. Appropriate epistemic humility demonstrated."
    consistency_check: "consistent"
    implications:
      cluster_3: "Strong FAIR infrastructure + Good evidential strength = high reproduction potential. Single-reviewer protocol affects interpretation of reproducibility findings."
```
