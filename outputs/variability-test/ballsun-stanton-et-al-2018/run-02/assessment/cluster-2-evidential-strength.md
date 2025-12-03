# Cluster 2: Evidential Strength Assessment

**Paper:** Ballsun-Stanton et al. (2018) - FAIMS Mobile
**Run:** run-02
**Assessment Date:** 2025-12-02
**Paper Type:** Methodological (Software Publication)

## Overview

This cluster assesses the quality and strength of evidence supporting the paper's claims. For software publications, this includes adoption evidence, impact metrics, and feature effectiveness claims.

## Signal 2.1: Evidence Quality

### Assessment

| Criterion | Rating | Evidence |
|-----------|--------|----------|
| Evidence type diversity | **Strong** | Quantitative metrics, case study references, feature documentation |
| Source credibility | **Strong** | Self-reported but verifiable (open repositories) |
| Evidence-claim alignment | **Strong** | Claims well-supported by presented evidence |
| Quantification | **Moderate** | Key metrics provided; some areas lack quantification |

### Key Quantitative Evidence

| Metric | Value | Source |
|--------|-------|--------|
| Project modules created | 45 | Direct reporting |
| Module definitions (public wiki) | 24 | Verifiable |
| Researchers trained | 80+ | Direct reporting |
| Records from 3 projects | 30,000+ | Direct reporting |
| Customisation reduction | 90%+ | Claim with partial evidence |
| Development duration | 5 years | Direct reporting |

**Score: 4/5**

## Signal 2.2: Claim-Evidence Linkage

### Assessment

| Claim Type | Evidence Strength | Notes |
|------------|-------------------|-------|
| Feature capabilities | **Strong** | Technical specifications verifiable in repository |
| Adoption claims | **Moderate** | Self-reported metrics; partial verification possible |
| Impact claims | **Moderate** | Referenced case studies; direct evidence limited |
| Efficiency claims | **Limited** | 90% reduction claim lacks detailed quantification |

### Evidence Chain Analysis

**Strongest chains:**
- Problem → Feature → Implementation: Well-documented with technical specifications
- Adoption metrics: Concrete numbers with verifiable wiki

**Weakest chains:**
- Efficiency claims: "90%+ reduction in customisation" lacks baseline comparison
- User satisfaction: No formal evaluation metrics

**Score: 3.5/5**

## Signal 2.3: Methodological Rigour for Evidence Collection

### Assessment

| Criterion | Rating | Evidence |
|-----------|--------|----------|
| Systematic collection | **Limited** | Evidence appears opportunistically collected |
| Bias mitigation | **Limited** | Self-reported by development team |
| Validation | **Moderate** | Some claims verifiable via public resources |
| Completeness | **Moderate** | Key areas covered; gaps in user experience data |

### Evidence Collection Approach

The paper follows software publication conventions where evidence is typically drawn from:
- Development experience (documented)
- Deployment statistics (provided)
- User adoption metrics (partially provided)
- Comparative analysis (limited)

**Score: 3/5**

## Signal 2.4: Counter-Evidence Handling

### Assessment

| Criterion | Rating | Evidence |
|-----------|--------|----------|
| Limitations acknowledged | **Strong** | Explicitly notes sustainability, server requirements |
| Alternative approaches discussed | **Limited** | Minimal comparison with alternatives |
| Failure modes addressed | **Moderate** | Technical limitations noted (server requirement) |
| Uncertainty communication | **Moderate** | Some qualifying language used |

### Acknowledged Limitations

> "FAIMS infrastructure is grant-funded and therefore its long-term sustainability is uncertain"

> "FAIMS Mobile requires a Linux server... data management and any additional analyses require a separate desktop GIS and/or database application"

**Score: 3.5/5**

## Cluster 2 Summary

| Signal | Score | Weight | Weighted |
|--------|-------|--------|----------|
| 2.1 Evidence Quality | 4.0/5 | 0.30 | 1.20 |
| 2.2 Claim-Evidence Linkage | 3.5/5 | 0.30 | 1.05 |
| 2.3 Methodological Rigour | 3.0/5 | 0.20 | 0.60 |
| 2.4 Counter-Evidence | 3.5/5 | 0.20 | 0.70 |
| **Cluster Total** | | | **3.55/5** |

## Qualitative Assessment

### Strengths

1. **Concrete metrics:** Specific adoption numbers (45 modules, 80+ researchers, 30,000 records)
2. **Verifiable claims:** Open-source repository allows independent verification
3. **Honest limitations:** Clear acknowledgment of sustainability challenges
4. **Case study references:** Points to Sobotkova et al. (2016) for detailed deployment analysis

### Limitations

1. **Self-reported data:** Metrics from development team without independent validation
2. **Missing baselines:** Efficiency claims lack comparative baselines
3. **No formal evaluation:** No user studies or systematic impact assessment
4. **Selection bias:** Reported deployments may represent successful cases

### Evidence Gaps

| Gap | Impact | Mitigation |
|-----|--------|------------|
| User satisfaction data | Moderate | Case study references |
| Comparative performance | High | Limited mitigation |
| Long-term usage patterns | Moderate | 5-year development span suggests sustainability |
| Failure case analysis | Moderate | Some limitations acknowledged |

---

*Cluster 2 Assessment completed: 2025-12-02*
*Overall Score: 3.55/5 (Moderate-Strong)*
