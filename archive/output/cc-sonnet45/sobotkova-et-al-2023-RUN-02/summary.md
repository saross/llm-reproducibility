# Extraction Summary: Sobotkova et al. 2023

**Paper:** Creating large, high-quality geospatial datasets from historical maps using novice volunteers

**Authors:** Sobotkova, Ross, Nassif-Haynes, Ballsun-Stanton

**Extraction Date:** 2025-10-25

**Extractor:** Claude Sonnet 4.5 (research-assessor v2.6)

**Status:** ✅ COMPLETE - Ready for Assessment

---

## Executive Summary

Successfully completed 5-pass extraction yielding **112 items** comprehensively documenting claims, evidence, and methodology from this crowdsourcing case study.

**Key Finding:** Paper presents well-documented comparative evaluation of mobile crowdsourcing approach with explicit efficiency thresholds: most efficient for 10,000-60,000 features, with detailed time measurements enabling replication.

---

## Extraction Statistics

| Category | Count | Notes |
|---|---|---|
| **Evidence** | 33 | All quantitative measurements properly sourced |
| **Claims** | 46 | 10 core, mixed intermediate/supporting |
| **Implicit Arguments** | 7 | Systematic review of all core claims completed |
| **Research Designs** | 2 | Case study + comparative evaluation (both explicit) |
| **Methods** | 9 | 6 explicit, 3 implicit (67% transparency) |
| **Protocols** | 15 | 13 explicit, 2 implicit (87% transparency) |
| **TOTAL** | **112** | 100 explicit, 12 implicit items |

---

## Core Claims (Top 10)

1. **C001:** Crowdsourcing produced large, accurate, analysis-ready dataset
2. **C002:** Approach required little training/supervision
3. **C003:** Most efficient for 10,000–60,000 features (conservative estimate)
4. **C004:** Mobile field systems can be customized for participatory GIS
5. **C005:** Complements ML (less expertise/time/resources required)
6. **C039:** Threshold: worthwhile above ~4,500 features (vs expert) or ~10,000 (vs desktop GIS volunteers)
7. **C040:** Above 60,000 records, use ML (if expertise available)
8. **C042:** Crowdsourcing and ML are complementary
9. **C043:** Typical projects can deploy crowdsourcing but may not access ML
10. **C045:** Approach is readily transferable

---

## Methodological Overview

### Research Designs
- **RD001:** Case study design evaluating crowdsourced digitization (inductive)
- **RD002:** Comparative evaluation testing efficiency thresholds (deductive)

### Data Collection Methods
- **M001:** Crowdsourced digitization via FAIMS Mobile customization
- **M002:** Novice volunteer recruitment (field school students)
- **M003:** Map symbol extraction (burial/settlement mounds from Soviet maps)
- **M004:** Systematic time-on-task measurement
- **M005:** Random sampling for accuracy assessment (7% of maps)
- **M006:** Desktop GIS baseline comparison (2010)

### Analysis Methods
- **M007:** Comparative time-efficiency analysis (features/staff-hour)
- **M008:** Error rate calculation and characterization

### Implicit Methods (Transparency Gaps)
- **M009:** Map tile assignment to volunteers (mentioned but undocumented)

### Key Protocols (15 total)
- **System Setup:** 7-stage FAIMS customization workflow, server config, validation
- **Data Preparation:** Map tiling/pyramids, file transfer workflow
- **Training:** Minimal protocol (<30 min total per season)
- **Data Collection:** Point digitization, attribute entry with controlled vocabularies, offline sync
- **Quality Assurance:** Random sampling review, time logging, performance mitigation

---

## Quantitative Outputs

### Project Scale
- **10,827 features** digitized from 58 Soviet topographic maps
- **23,500 sq km** coverage
- **241 person-hours** total (57 staff, 184 volunteers)
- **54-92 seconds** per feature (2017 vs 2018)

### Quality Metrics
- **<6% error rate** (5.87% in random sample)
- **~94% accuracy** for processed maps
- **2.06% recoverable omissions** (mostly corrected via validation)

### Efficiency Comparisons
- **190 features/staff-hour** (crowdsourcing approach)
- **60-75 features/staff-hour** (expert desktop GIS)
- **130-180 features/staff-hour** (volunteer desktop GIS)

### Time Investments
- **44 hours** pre-field customization
- **7 hours** in-field setup/support across both seasons
- **6 hours** post-field quality assurance

---

## Transparency Assessment

### Well-Documented Aspects (88% explicit)
✅ Complete workflow documentation (7 stages)
✅ Detailed time measurements enabling replication
✅ Explicit quality assessment methodology
✅ System configuration comprehensively described
✅ Comparative baselines documented (2010 desktop GIS, ML benchmarks)

### Transparency Gaps (12% implicit)
⚠️ **M009:** Map assignment procedures undocumented
⚠️ **P010:** 2010 baseline protocol details missing
⚠️ **P011:** Symbol identification decision rules not explicit

### Expected Information Gaps Flagged
- 13 of 15 protocols have missing expected information documented
- Common gaps: parameter values, software versions, decision criteria
- Gaps documented for transparency, not as criticism

---

## Implicit Arguments Identified

All core claims systematically reviewed using 4-type framework:

1. **IA001:** Quality of volunteer data can match expert data with appropriate tools (bridging claim)
2. **IA002:** Technical complexity can be hidden through interface design (design assumption)
3. **IA003:** Staff time is primary constraint (unstated assumption underlying all analysis)
4. **IA004:** Mobile devices reduce participation barriers via familiarity (bridging claim)
5. **IA005:** ML expertise less accessible than digitization time for small projects (unstated assumption)
6. **IA006:** Thresholds generalizable despite single-case basis (unstated assumption)
7. **IA007:** ML training data effort constitutes digitization project (logical implication)

---

## Notable Methodological Features

### Strengths
- **Systematic comparative design** with multiple baselines
- **Detailed temporal tracking** (2017 vs 2018 preserved separately)
- **Complete workflow documentation** from setup through QA
- **Explicit efficiency thresholds** with quantitative basis
- **Open replication materials** (GitHub repository)

### Innovations
- **Mobile platform repurposing** for deskbound digitization
- **Minimal training approach** (minutes instead of hours)
- **Offline-first design** for field conditions
- **Performance mitigation protocol** (database resets)

### Limitations Acknowledged
- Single case study (explicitly noted as "single data point")
- Conservative thresholds (authors use qualifying language)
- Context-specific (density, obtrusiveness, complexity)
- Need for more comparative data

---

## Consolidation Summary

### Pass 2 (Claims/Evidence)
- **Before:** 101 items (40E, 46C, 7IA, 8 context)
- **After:** 86 items (33E, 46C, 7IA)
- **Reduction:** 17.5%
- **Consolidations:** 7 (mostly evidence, 5 moved to metadata, 2 evidence pairs)

### Pass 4 (RDMAP)
- **Before:** 26 items (2RD, 9M, 15P)
- **After:** 26 items (no consolidation)
- **Rationale:** Already at appropriate granularity, all items assessed separately
- **Cross-reference fixes:** 8 bidirectionality corrections

---

## Validation Results

✅ **PASSED** - All validation checks successful

- **Structural Completeness:** 112/112 items complete
- **Sourcing Integrity:** 100% compliance (zero hallucinations)
- **Relationship Integrity:** Zero broken links
- **Cross-Reference Validity:** All bidirectional links verified
- **Consolidation Integrity:** All 7 consolidations properly documented

---

## Files Generated

- `extraction.json` - Complete extraction (112 items, 542 lines)
- `validation-pass5.md` - Comprehensive validation report
- `summary.md` - This document
- `PASS1_COMPLETE.md` - Pass 1 checkpoint
- `PASS3_COMPLETE.md` - Pass 3 checkpoint

---

## Recommended Next Steps

### For Assessment
1. Evaluate transparency using documented RDMAP (88% explicit rate)
2. Assess replicability using time measurements and workflow documentation
3. Review credibility of efficiency threshold claims (C003, C039, C040)
4. Examine single-case generalization assumptions (IA006)

### For Comparison
- Time measurements enable direct comparison with other crowdsourcing studies
- Efficiency thresholds provide decision framework for approach selection
- Error rate data supports quality assessment discussions

### For Replication
- Complete workflow documented (RD → M → P chain)
- GitHub repository available for FAIMS customization
- Quantitative thresholds provided for approach selection

---

**Extraction Status:** COMPLETE ✅

**Ready for:** Research transparency and reproducibility assessment
