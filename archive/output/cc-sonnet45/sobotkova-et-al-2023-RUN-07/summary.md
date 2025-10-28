# Extraction Summary: Sobotkova et al. (2023)

**Paper:** Creating large, high-quality geospatial datasets from historical maps using novice volunteers
**Journal:** Applied Geography 155 (2023) 102967
**DOI:** 10.1016/j.apgeog.2023.102967

## Extraction Overview

**Completed:** 2025-10-27
**Extractor:** Claude Sonnet 4.5
**Workflow:** 5-pass autonomous extraction
**Status:** ✅ Complete and validated

## Final Item Counts

| Category | Count |
|----------|-------|
| Evidence | 10 |
| Claims | 19 |
| Implicit Arguments | 7 |
| Research Designs | 2 |
| Methods | 4 |
| Protocols | 6 |
| **Total** | **48** |

## Key Findings

### Core Claims (8 items)
The paper makes 8 core claims about crowdsourced map digitisation:
1. Optimal efficiency range: 10,000-60,000 features (C001)
2. May offer advantages for datasets as small as few hundred records (C002)
3. Mobile field data collection systems can be profitably customised for participatory GIS (C003)
4. Crowdsourcing scales better than desktop GIS but requires platform adaptation (C004)
5. Complements ML by requiring less expertise and resources (C008)
6. Suitable for small-mid sized datasets not warranting ML investment (C009)
7. Payoff threshold vs staff digitisation: 3,400-4,300 features (C017)
8. Above 60,000 records, ML becomes more appropriate (C018)

### Methodological Transparency

**Research Designs:**
- Comparative evaluation design (vs desktop GIS and ML)
- Usability-driven framework adapting field HCI principles

**Methods:**
- FAIMS Mobile platform customisation
- Volunteer crowdsourcing with novice undergraduates
- Time-on-task measurement for comparison
- Streamlined GIS interface design

**Protocols:**
- System customisation via definition files
- Map preparation (tiling, pyramids)
- Offline collection with opportunistic sync
- Automated metadata capture
- Minimal training protocol
- Random sampling QA (7% of maps)

### Implicit Assumptions

7 key implicit arguments identified, including:
- Efficiency measured by staff time rather than total time (IA001)
- Generalisability beyond specific Bulgarian mound symbology (IA002)
- Conditional viability for small datasets depends on staff constraints (IA003)
- HCI principles transfer from kinetic to deskbound work (IA004)
- Comparison baseline is failed 2010 desktop GIS attempt (IA005)

## Assessment Readiness

**Transparency:** High - All RDMAP items explicit/documented
**Replicability:** Good - Key procedures specified, some technical details could be more granular
**Credibility:** Strong - Systematic evaluation with error rates, multiple comparison baselines

**Suitable for:**
- Comparative method assessments
- Transparency/reproducibility studies
- Cost-benefit analysis
- Scaling decisions for similar projects

## Notes

- Paper demonstrates good methodological documentation (all RDMAP explicit)
- Systematic comparative evaluation across three approaches
- Quantitative thresholds provided for decision-making
- Well-suited for informing digital humanities infrastructure choices
