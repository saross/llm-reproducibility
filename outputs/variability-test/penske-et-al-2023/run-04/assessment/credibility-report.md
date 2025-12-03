# Credibility Assessment Report

**Paper:** Penske et al. (2023) — Ancient DNA reveals early contact between farming and pastoralist societies in southeastern Europe
**Publication:** Nature (2023)
**DOI:** 10.1038/s41586-023-06334-8
**Assessment Date:** 2025-12-02
**Run:** run-04 (variability test)
**Assessor Version:** v1.0

---

## Executive Summary

This Nature archaeogenomics paper presents genome-wide ancient DNA analysis from 135 individuals across southeastern Europe and the northwestern Black Sea region (ca. 5400-2400 BC), revealing that genetic contact between farming and pastoralist societies occurred approximately 1000 years earlier than archaeological evidence suggested.

**Overall Credibility Rating:** STRONG

| Cluster | Rating | Scores |
|---------|--------|--------|
| C1: Foundational Clarity | Strong | Comprehensibility 83, Transparency 85 |
| C2: Evidential Strength | Strong | Plausibility 77, Validity 81, Robustness 74, Generalisability 73 |
| C3: Reproducibility | Adequate | Reproducibility 73 |

**Composite Score:** 78/100 (Strong)

---

## Quality Gate Summary

**Quality State:** HIGH

- **Extraction Confidence:** HIGH — 64 evidence items, 63 claims, 10 implicit arguments, 47 RDMAP items
- **Classification Confidence:** HIGH — Empirical/inductive with expressed-revealed match
- **Infrastructure Confidence:** HIGH — FAIR score 93.3%, data at ENA PRJEB62503

---

## Research Approach

**Primary Classification:** Inductive (confidence: high)

This is clearly inductive empirical research. The paper adopts an exploratory framework to address a temporal-spatial "sampling gap" in archaeogenomics of southeastern Europe. No hypotheses are pre-specified; the study characterises genetic variation across 135 individuals from 8 sites spanning approximately 3000 years, identifies ancestry patterns, and reconstructs population history from genomic data.

**Framework Applied:** inductive_emphasis

**Primary Signals:** Transparency, Comprehensibility, Generalisability
**Secondary Signals:** Validity, Reproducibility, Plausibility

---

## Signal Scores

### Cluster 1: Foundational Clarity

| Signal | Score | Band |
|--------|-------|------|
| Comprehensibility | 83 | Excellent |
| Transparency | 85 | Excellent |

**Cluster Rating:** Strong

**Summary:** Research goals explicitly stated as exploratory archaeogenomic investigation. Pattern descriptions clear and well-bounded with quantitative precision. Methods thoroughly documented (19 methods, 24 protocols). Data archived in ENA with accession PRJEB62503.

### Cluster 2: Evidential Strength

| Signal | Score | Band |
|--------|-------|------|
| Plausibility | 77 | Good |
| Validity | 81 | Excellent |
| Robustness | 74 | Good |
| Generalisability | 73 | Good |

**Cluster Rating:** Strong

**Summary:** Substantial evidence base (135 individuals, 8 sites). Multi-proxy methodological triangulation (PCA, f-statistics, qpAdm, IBD, ROH). Patterns consistent with established frameworks while refining temporal understanding. Claims appropriately bounded to southeastern Europe/Black Sea region.

### Cluster 3: Reproducibility

| Signal | Score | Band |
|--------|-------|------|
| Reproducibility | 73 | Good |

**Cluster Rating:** Adequate

**Summary:** Data openly available through ENA PRJEB62503. All primary software packages open-source with versions documented. FAIR score 93.3%. Limitation: no custom code repository; workflow documented but not automated.

---

## Key Findings

### Major Contributions

1. **Early contact timing:** Genetic contact between farming and pastoralist groups occurred approximately 1000 years earlier than archaeological evidence suggested
2. **Genetic continuity:** Substantial continuity between Neolithic and Copper Age populations in southeastern Europe
3. **Complex admixture:** Multiple sources of steppe-related ancestry (EHG-enriched vs full steppe) with distinct chronological patterns
4. **Regional variation:** Site-specific ancestry patterns (Yagodna, Pietrele showing different dynamics than other sites)

### Strengths

- **Exceptional methodological documentation:** 19 explicit methods, 24 protocols captured
- **Multi-proxy analytical approach:** Convergent evidence from PCA, f-statistics, qpAdm, IBD, ROH
- **Exemplary data sharing:** DNA sequences in ENA with open access (FAIR 93.3%)
- **Appropriate claim scoping:** Geographic and temporal boundaries clearly stated
- **High publication venue:** Nature standards ensure rigorous peer review

### Limitations

- **Code availability gap:** No custom analysis scripts or automated pipeline shared
- **Temporal sampling bias:** Copper Age overrepresented (n≈95) vs Neolithic (n=1)
- **Implicit theoretical assumptions:** Population continuity and replacement models not fully articulated
- **Sensitivity analysis limited:** Reference population effects on ancestry estimates not systematically tested

---

## Reproducibility Assessment

**Execution Feasibility:** needs_work

### Reproducibility Readiness

| Component | Status | Details |
|-----------|--------|---------|
| Inputs | Available | ENA PRJEB62503, supplementary tables |
| Code | Partial | Published packages with versions; no custom repo |
| Environment | Partial | Software versions documented; dependencies not specified |
| Outputs | Documented | Results, figures, supplementary tables |

### Gateway Recommendation

This paper could be queued for analytical reproducibility verification with moderate preparation effort. Requirements:
1. Download sequences from ENA
2. Install documented open-source software packages
3. Reconstruct pipeline from Methods documentation
4. Execute analyses with specified parameters
5. Compare outputs to published results

Estimated effort: Substantial but feasible for experienced archaeogenomicist with HPC access.

---

## Chronological Context

**Publication Year:** 2023
**Adoption Context:** early_majority

By 2023 standards:
- Data sharing in repositories: **Excellent** (exceeds standard)
- Code sharing: **Below emerging expectation** (gap)
- FAIR compliance: **Excellent** (93.3%)
- Automated pipelines: **Not implemented** (emerging practice)

The 78/100 composite score reflects strong overall practice with identified improvement opportunities.

---

## Recommendations

### For Verification

1. **Priority reproduction target:** qpAdm ancestry proportion estimates (C01 claim about early contact)
2. **Independent verification:** f-statistics testing affinity relationships
3. **Sensitivity test:** Alternative reference population compositions

### For Future Work

1. **Code deposition:** Publish analysis scripts to Zenodo or similar repository
2. **Pipeline automation:** Convert workflow to Snakemake/Nextflow for reproducibility
3. **Sensitivity analysis:** Document reference population effects on estimates
4. **Environment specification:** Provide complete computational environment details

### For Field

This paper exemplifies good archaeogenomics practice for its era. The combination of Nature publication standards, comprehensive supplementary documentation, and ENA data deposition provides a strong foundation for verification. The absence of code sharing represents an opportunity for the field to strengthen reproducibility norms.

---

## Structured Output

```yaml
credibility_report:
  paper_slug: "penske-et-al-2023"
  run: "run-04"
  assessment_date: "2025-12-02"
  assessor_version: "v1.0"

  quality_state: "high"
  research_approach: "inductive"
  framework: "inductive_emphasis"

  overall_rating: "strong"
  composite_score: 78

  cluster_scores:
    foundational_clarity:
      rating: "strong"
      comprehensibility: 83
      transparency: 85
    evidential_strength:
      rating: "strong"
      plausibility: 77
      validity: 81
      robustness: 74
      generalisability: 73
    reproducibility:
      rating: "adequate"
      reproducibility: 73

  signal_summary:
    highest: "transparency (85)"
    lowest: "generalisability (73)"
    mean: 78
    range: 12

  key_strengths:
    - "Exemplary data sharing (ENA PRJEB62503, FAIR 93.3%)"
    - "Comprehensive methodological documentation"
    - "Multi-proxy analytical triangulation"
    - "Appropriate claim scoping"

  key_limitations:
    - "No custom code repository"
    - "Limited sensitivity analysis"
    - "Uneven temporal sampling"

  reproducibility_gateway:
    feasibility: "needs_work"
    data_accessible: true
    code_accessible: "partial"
    effort_level: "moderate"
    hpc_required: true

  recommendations:
    verification:
      - "Priority: qpAdm ancestry estimates for early contact claim"
      - "Sensitivity: test alternative reference populations"
    improvement:
      - "Deposit analysis scripts to repository"
      - "Automate pipeline (Snakemake/Nextflow)"
      - "Document complete computational environment"

  chronological_context:
    publication_year: 2023
    adoption_era: "early_majority"
    field_comparison: "Good practice; exceeds data sharing norms, below emerging code sharing expectations"
```

---

## Assessment Metadata

- **Extraction counts:** 64 evidence, 63 claims, 10 implicit arguments, 4 research designs, 19 methods, 24 protocols
- **Classification:** empirical/inductive (high confidence, expressed-revealed matched)
- **Quality state:** HIGH (all confidence dimensions HIGH)
- **FAIR score:** 14/15 (93.3%)
- **Schema version:** v2.6
- **Assessor model:** claude-opus-4-5-20251101

---

*Assessment generated as part of variability test (run-04 of 5)*
