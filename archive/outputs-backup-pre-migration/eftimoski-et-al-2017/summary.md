# Extraction Summary: Eftimoski et al. 2017

**Paper:** The impact of land use and depopulation on burial mounds in the Kazanlak Valley, Bulgaria: An ordered logit predictive model
**Authors:** Martin Eftimoski, Shawn A. Ross, Adela Sobotkova
**Journal:** Journal of Cultural Heritage (2017)
**DOI:** 10.1016/j.culher.2016.10.002

## Extraction Overview

**Extraction Date:** 2025-10-29
**Schema Version:** 2.5
**Extraction Status:** COMPLETE ✓
**Validation Status:** PASS ✓

### Total Items Extracted: 153

| Category | Count | Breakdown |
|----------|-------|-----------|
| **Evidence** | 32 | All explicit |
| **Claims** | 97 | All explicit |
| **Implicit Arguments** | 8 | All implicit |
| **Research Designs** | 2 | 2 explicit, 0 implicit |
| **Methods** | 4 | 4 explicit, 0 implicit |
| **Protocols** | 10 | 7 explicit, 3 implicit (30%) |
| **RDMAP Total** | 16 | 13 explicit, 3 implicit (18.75%) |

## Paper Characteristics

**Paper Type:** Quantitative predictive modelling study
**Discipline:** Archaeological heritage management / landscape archaeology
**Methods Transparency:** High (technical paper with detailed methodology)
**RDMAP Density:** Moderate (16 RDMAP items appropriate for modelling study)

## Key Findings

### Research Designs (2)

1. **RD001:** Ordered logit vulnerability assessment model - uses logistic regression to assess mound vulnerability by modeling current condition-circumstance relationships and simulating probable outcomes under changed circumstances
2. **RD002:** Perceptive risk assessment approach - selects risk factors based on field researchers' observations about principal threats, then tests hypotheses quantitatively

### Methods (4)

1. **M001:** Hypothesis-driven factor selection based on three field-informed hypotheses about threats
2. **M002:** Large-scale systematic pedestrian survey (n=773 mounds, trained personnel, standardised recording)
3. **M003:** GIS-based spatial variable derivation (elevation from DEM, distances using qGIS)
4. **M004:** Ordered logit model estimation and simulation using maximum likelihood

### Protocols (10)

**Explicit Protocols (7):**
- P001: Variable selection for model (explanatory variables + four simulation scenarios)
- P002: Standardised mound recording (GPS, dimensions, land-use, condition)
- P003: Elevation extraction from ASTER DEM
- P004: Distance calculation using qGIS Distance Matrix plugin
- P005: Ordered logit coefficient estimation
- P006: Simulation procedure for changed circumstances
- P007: Graphical representation of simulation results (probability density functions)

**Implicit Protocols (3):**
- IP001: Personnel training procedure (mentioned: "trained personnel" but not documented)
- IP002: Land-use classification criteria (categories defined but decision rules not specified)
- IP003: Condition assessment procedure (Likert scale described but diagnostic criteria not detailed)

### Major Empirical Findings

**Land Use Impact:**
- Pasture→annual agriculture conversion: 30.16% decrease in well-preserved mounds (C059, supported by E024)
- Effect likely due to aggressive ploughing, harrowing, stone clearing (C068)

**Remoteness/Depopulation Impact:**
- 673m urban boundary retreat: 8.59% decline in well-preserved mounds (C061, supported by E025)
- Counterintuitive finding: remoteness increases damage (C013)
- Mechanism: reduced surveillance enables looting/agricultural damage (C069, IA004)

**Size/Elevation Effects:**
- Larger mounds in better condition (C074, C063): agricultural damage to small mounds outweighs looting of large mounds (C077)
- Higher elevation associated with more damage (C062), likely erosion or indirect relationships (C078)

## Rationalization Summary

### Pass 2 (Claims/Evidence)
- **Items before:** 99 claims, 32 evidence, 8 implicit arguments
- **Items after:** 97 claims, 32 evidence, 8 implicit arguments
- **Reduction:** 2.0% (2 claim consolidations)
- **Note:** Conservative reduction appropriate for well-differentiated technical paper

**Consolidations:**
1. C042+C043 → C042 (logit superiority over linear regression)
2. C073+C087 → C073 (depopulation threatens heritage)

### Pass 5 (RDMAP)
- **Items before/after:** 16 RDMAP items (no changes)
- **Reduction:** 0%
- **Note:** All RDMAP items describe distinct procedures; no consolidation opportunities

## Validation Results

**Overall Status:** PASS ✓
**Total Items Validated:** 153

| Check | Status | Details |
|-------|--------|---------|
| Cross-reference integrity | PASS ✓ | 0 broken references (1 fixed: E006 C24→C024) |
| Hierarchy validation | PASS ✓ | 100% RDMAP linking rate |
| Schema compliance | PASS ✓ | All required fields present |
| Source verification | PASS ✓ | 100% sourcing completeness |
| Type consistency | PASS ✓ | Status fields match sourcing |

**Issues Found:** 0 critical, 0 important, 0 minor, 0 warnings

## Expected Information Gaps

**Total gaps documented:** 15 transparency gaps in 3 implicit protocols

**Common gaps (Pattern 1: mentioned undocumented):**
- Personnel training content and duration (IP001)
- Land-use classification decision rules (IP002)
- Condition assessment diagnostic criteria (IP003)
- Software specifications for statistical analysis (P005)
- Model diagnostics and convergence criteria (P005)

These gaps represent documentation limitations (procedures mentioned but not detailed), not extraction errors. Appropriately captured as implicit protocols or expected_information_missing fields.

## Extraction Quality Metrics

### Sourcing Discipline
- **Evidence:** 32/32 with verbatim_quote (100%)
- **Claims:** 97/97 with verbatim_quote (100%)
- **Implicit Arguments:** 8/8 with trigger infrastructure (100%)
- **Explicit RDMAP:** 13/13 with verbatim_quote (100%)
- **Implicit RDMAP:** 3/3 with trigger infrastructure (100%)

### RDMAP Hierarchy Completeness
- **Designs:** 2 items, both with child methods
- **Methods:** 4 items, all linked to designs (100%)
- **Protocols:** 10 items, all linked to methods (100%)
- **Full chain coverage:** 100% of protocols trace to designs through methods

## Notable Extraction Decisions

1. **Conservative rationalization:** Accepted 2% reduction (below 15-20% target) as appropriate for technical paper where each claim provides distinct information

2. **Methodological claims preservation:** Kept detailed methodological justification claims (C042-C055) separate as they document distinct decision points in model selection process

3. **Implicit protocol extraction:** Extracted 3 implicit protocols for undocumented but essential procedures (training, classification criteria, assessment procedures)

4. **Counterintuitive findings emphasis:** Extracted multiple claims about unexpected remoteness-damage relationship (C003, C013, C060, C061, C069, C073) as this is paper's key contribution

## Assessment Readiness

**Ready for credibility assessment:** YES ✓

**Strengths:**
- 100% sourcing completeness prevents hallucination
- Complete RDMAP hierarchy enables systematic assessment
- High methods transparency in technical paper
- Well-documented quantitative findings with effect sizes
- Clear causal interpretations with mechanistic explanations

**Considerations for assessment:**
- 18.75% implicit RDMAP (3/16) indicates some transparency gaps in operational procedures
- Training and assessment procedures have low reconstruction confidence
- Model diagnostics and software specifications not provided
- Temporal limitations acknowledged (snapshot approach, no timeframe specification)

## Files Generated

- `extraction.json` - Complete extraction (153 items)
- `validation_report.json` - Detailed validation results
- `pass1_section1_abstract_intro.py` - Pass 1 Section 1 extraction
- `pass1_section2_methodology_part1.py` - Pass 1 Section 2 extraction
- `pass1_section3_methodology_part2.py` - Pass 1 Section 3 extraction
- `pass1_section4_results.py` - Pass 1 Section 4 extraction
- `pass1_section5_discussion_part1.py` - Pass 1 Section 5 extraction
- `pass1_section6_discussion_conclusion.py` - Pass 1 Section 6 extraction
- `pass2_rationalization.py` - Pass 2 consolidation script
- `pass3_rdmap_extraction.py` - Pass 3 RDMAP extraction
- `pass4_implicit_rdmap.py` - Pass 4 implicit RDMAP extraction
- `pass5_rdmap_rationalization.py` - Pass 5 RDMAP consolidation
- `pass6_validation.py` - Pass 6 validation script
- `pass6_fix_crossref.py` - Cross-reference fix
- `summary.md` - This summary document

## Recommendations for Future Extractions

1. **Technical modelling papers:** Expect well-differentiated claims with limited consolidation opportunities (each claim documents distinct aspect of methodology or findings)

2. **Quantitative findings:** Extract both aggregate findings and specific effect sizes as separate claims to preserve interpretive hierarchy

3. **Counterintuitive findings:** Papers emphasizing unexpected results may have multiple restatements across sections - consolidate carefully to preserve emphasis

4. **Implicit procedures:** Field data collection papers often have implicit training, classification, and assessment procedures - systematically extract as implicit protocols

---

**Extraction completed:** 2025-10-29
**Extractor:** Claude Code + research-assessor skill
**Schema version:** 2.5
