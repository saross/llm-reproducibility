# Extraction Summary: sobotkova-et-al-2016

**Paper:** "Measure Twice, Cut Once: Cooperative Deployment of a Generalised, Archaeology-Specific Field Data Collection System"
**Authors:** Adela Sobotkova, Brian Ballsun-Stanton, Shawn Ross, Penny Crook
**Extraction Date:** 2025-10-31
**Extraction Status:** ✓ Complete
**Schema Version:** 2.5

---

## Extraction Overview

**Total Items Extracted:** 218

### Claims-Evidence Framework

| Type | Count | Notes |
|------|-------|-------|
| **Evidence** | 43 | Reduced from 46 after Pass 2 (3 consolidations) |
| **Claims** | 114 | No consolidation - well-differentiated analytical roles |
| **Implicit Arguments** | 20 | Underlying methodological assumptions and theoretical framing |

### Research Design and Methods Assessment Protocol (RDMAP)

| Tier | Explicit | Implicit | Total | Notes |
|------|----------|----------|-------|-------|
| **Research Designs** | 4 | 2 | 6 | Strategic positioning, co-development model, sustainability designs |
| **Methods** | 8 | 4 | 12 | Module customisation, testing, support, assessment methods |
| **Protocols** | 18 | 5 | 23 | Customisation pathways, testing procedures, deployment protocols |
| **Total RDMAP** | 30 | 11 | 41 | 26.8% implicit (within 20-40% target) |

---

## Pass-by-Pass Summary

### Pass 1: Liberal Claims-Evidence Extraction

- **Sections:** 8 groups (Abstract through Conclusions)
- **Items Extracted:** 180 (46 E, 114 C, 20 IA)
- **Approach:** Liberal extraction across all sections
- **Issue Resolved:** Fixed null page numbers via section-to-PDF mapping

### Pass 2: Claims-Evidence Rationalization

- **Before:** 180 items (46 E, 114 C, 20 IA)
- **After:** 177 items (43 E, 114 C, 20 IA)
- **Reduction:** 3 items (1.7%)
- **Consolidations:** 3 evidence groups (E007+E008, E017+E018, E042+E043)
- **Rationale:** Pass 1 extraction was well-bounded, not over-extracted. Conservative consolidation appropriate.

### Pass 3: Liberal RDMAP Extraction

- **Sections:** Same 8 groups as Pass 1
- **Items Extracted:** 30 RDMAP (4 RD, 8 M, 18 P)
- **Group 1 (Intro sections):** 4 research designs, 3 methods, 8 protocols
- **Groups 2-8 (Case studies):** 5 methods, 10 protocols
- **Key Finding:** Research designs concentrated in introductory/positioning sections; methods/protocols in case study sections

### Pass 4: Implicit RDMAP Extraction

- **Items Extracted:** 11 implicit RDMAP (2 RD, 4 M, 5 P)
- **Implicit Ratio:** 11/41 = 26.8% (within 20-40% target)
- **Key Findings:**
  - Comparative digital vs paper evaluation pervades paper but never stated as design objective
  - Multiple measurement methodologies (performance, time-on-task, cost-benefit) mentioned but not documented
  - Post-project questionnaire is primary data source but methodology invisible
  - Operational protocols (seed assignment, live updates, concatenation) mentioned without specification

### Pass 5: RDMAP Rationalization

- **Before:** 42 RDMAP (6 RD, 13 M, 23 P)
- **After:** 41 RDMAP (6 RD, 12 M, 23 P)
- **Reduction:** 1 item (2.4%)
- **Consolidation:** M-IMP-003 + M-IMP-004 (assessment methodology unified)
- **Rationale:** Assessment compatibility test showed minimal consolidation appropriate. RDMAP items represent genuine procedural diversity in co-development study.

### Pass 6: Validation and Cross-Reference Repair

- **Overall Status:** PASS_WITH_ISSUES
- **Critical Issues:** 0 (after fixes)
- **Important Issues:** 1 (protocol-method linking at 56.5%, expected for system-level protocols)
- **RDMAP Source Verification:** 100% pass rate (explicit and implicit)
- **Fixes Applied:** 1 broken cross-reference repaired (RD-IMP-002 → M-IMP-003 after consolidation)

---

## Key Methodological Findings

### Extraction Characteristics

1. **Well-Bounded Initial Extraction:** Both Pass 1 (claims/evidence) and Pass 3 (RDMAP) were well-differentiated, resulting in below-target rationalization percentages (1.7% and 2.4% vs 15-20% target). This reflects appropriate liberal extraction, not over-extraction.

2. **Implicit Content Substantial:** 28.6% implicit RDMAP ratio indicates significant transparency gaps. Many procedural details mentioned but not documented (questionnaires, measurement methodologies, operational protocols).

3. **Research Design Positioning:** Strategic design decisions concentrated in introductory sections (positioning, partnership model, sustainability), while operational methods/protocols found in case study sections.

4. **Assessment Method Consolidation:** Post-fieldwork assessment methodology appropriately unified - questionnaire is vehicle for impact assessment, evaluated as single evaluation approach.

### Paper-Specific Observations

1. **Co-Development Study:** Paper documents three case studies of FAIMS mobile platform deployment, with rich procedural detail in case study sections but strategic framing in introduction.

2. **Comparative Framing Implicit:** Systematic digital vs paper comparison pervades paper but never explicitly stated as design objective - identified as implicit research design (RD-IMP-001).

3. **Reproducibility Focus Emergent:** Reproducibility and transparency language in Discussion/Conclusions but not stated as a priori design goal - identified as implicit research design (RD-IMP-002).

4. **Measurement Gaps:** Multiple quantitative claims (performance thresholds, cost savings, time measurements) but measurement methodologies largely undocumented - identified as implicit methods.

5. **Operational Protocols Mentioned:** Several technical protocols (seed assignment, identifier concatenation, live updates, VM installation) referenced but procedures not specified - identified as implicit protocols.

---

## Validation Quality Metrics

| Metric | Value | Status |
|--------|-------|--------|
| **Cross-Reference Integrity** | 0 broken references | ✓ Pass |
| **Orphaned Objects** | 0 orphaned methods | ✓ Pass |
| **RDMAP Explicit Source Verification** | 100% pass rate | ✓ Pass |
| **RDMAP Implicit Source Verification** | 100% pass rate | ✓ Pass |
| **Protocol-Method Linking** | 56.5% | ⚠ Below 80%, but appropriate for system-level protocols |
| **Missing Required Fields** | 0 | ✓ Pass |
| **ID Format Errors** | 0 | ✓ Pass |

---

## Files Generated

- `extraction.json` - Complete extraction (218 items)
- `validation_report.json` - Pass 6 validation results
- `pass2_rationalization.py` - Claims/evidence consolidation script
- `pass2_consolidation_analysis.py` - Claims/evidence analysis
- `pass2_analysis_report.txt` - Consolidation analysis report
- `pass3_rdmap_extraction_group1.py` - RDMAP extraction (intro sections)
- `pass3_rdmap_extraction_groups2to8.py` - RDMAP extraction (case studies)
- `pass4_implicit_rdmap.py` - Implicit RDMAP extraction
- `pass5_rdmap_analysis.py` - RDMAP consolidation analysis
- `pass5_rdmap_rationalization.py` - RDMAP consolidation
- `pass6_validation.py` - Validation checks
- `pass6_fixes.py` - Cross-reference repairs

---

## Extraction Complete

All 6 passes completed successfully. Extraction ready for transparency and reproducibility assessment.

**Final Item Counts:**
- **Claims-Evidence:** 177 items (43 E, 114 C, 20 IA)
- **RDMAP:** 41 items (6 RD, 12 M, 23 P)
- **Total:** 218 items
- **Validation:** PASS_WITH_ISSUES (0 critical, 1 minor)
