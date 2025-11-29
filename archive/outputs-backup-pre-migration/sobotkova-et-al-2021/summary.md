# Extraction Summary: Sobotkova et al. 2021

**Paper:** Deploying an Offline, Multi-User, Mobile System for Digital Recording in the Perachora Peninsula, Greece
**Authors:** Adela Sobotkova, Shawn A. Ross, Petra Hermankova, Susan Lupack, Christian Nassif-Haynes, Brian Ballsun-Stanton, Panagiota Kasimi
**Journal:** Journal of Field Archaeology (2021)
**DOI:** 10.1080/00934690.2021.1969837

## Extraction Overview

**Extraction Date:** 2025-10-29
**Schema Version:** 2.5
**Extraction Status:** COMPLETE ✓
**Validation Status:** PASS ✓

### Total Items Extracted: 175

| Category | Count | Breakdown |
|----------|-------|-----------|
| **Evidence** | 66 | All explicit |
| **Claims** | 73 | All explicit |
| **Implicit Arguments** | 6 | All implicit |
| **Research Designs** | 2 | 2 explicit, 0 implicit |
| **Methods** | 8 | 6 explicit, 2 implicit (25%) |
| **Protocols** | 20 | 13 explicit, 7 implicit (35%) |
| **RDMAP Total** | 30 | 21 explicit, 9 implicit (30%) |

## Paper Characteristics

**Paper Type:** System implementation and field deployment case study
**Discipline:** Archaeological field informatics
**Methods Transparency:** High (technical implementation paper with detailed workflows)
**RDMAP Density:** Very high (30 RDMAP items for technical paper)

## Key Findings

### Research Designs (2)

1. **RD001:** Comparative case study design evaluating FAIMS Mobile platform against requirements for field data recording and open research principles
2. **RD002:** Requirements-driven approach for software selection and customisation based on project constraints

### Methods (8)

**Explicit Methods (6):**
- M001: Module reuse strategy (adapting existing FAIMS modules)
- M002: Dual parallel workflow management (Feature Recording + Gridded Survey)
- M003: Offline-first data management with bi-directional synchronisation
- M004: XML-based software customisation approach
- M005: Controlled vocabulary implementation for data quality
- M006: Daily data review for quality control

**Implicit Methods (2):**
- IM001: Student volunteer training method (mentioned as main project aim but procedures not documented)
- IM002: Retrospective efficiency comparison method (comparing FAIMS workflow to 2008-2011 hybrid approach)

### Protocols (20)

**Explicit Protocols (13):**
- System deployment and configuration protocols (P003, P004, P005, P007, P008)
- Field data collection workflows (P011 Feature Recording, P012 Gridded Survey)
- Data management and synchronisation (P003, P010, P013, P014)
- Quality control (P009)

**Implicit Protocols (7):**
- IP001: Device malfunction recovery protocol
- IP002: Bluetooth GPS troubleshooting protocol
- IP003: Diagnostic artefact collection and labelling
- IP004: Server-side validation protocol
- IP005: Automated backup protocol
- IP006: Digital camera photo tracking protocol
- IP008: Server hardware configuration protocol

### RDMAP Consolidations (Pass 5)

**2 consolidations executed (6.25% reduction):**

1. **P001 → P011:** Feature recording methodology subsumed into daily workflow
2. **P002 → P012:** Gridded survey methodology subsumed into daily workflow

Both consolidations used workflow integration pattern where detailed operational workflows (P011, P012) fully encompassed core methodology descriptions (P001, P002).

### Implicit RDMAP Patterns

**Total implicit RDMAP:** 9 items (30% of total)

**Extraction patterns:**
- Pattern 1 (mentioned undocumented): 7 items (78%)
- Pattern 2 (effects implying causes): 1 item (11%)
- Pattern 3 (tools without specs): 1 item (11%)
- Pattern 4 (strategic positioning): 0 items

**Implicit basis distribution:**
- mentioned_undocumented: 8 items (89%)
- inferred_from_results: 1 item (11%)

### Validation Results

**Overall Status:** PASS ✓
**Sourcing Completeness:** 100%

| Check | Status | Details |
|-------|--------|---------|
| Cross-reference integrity | PASS ✓ | 0 broken references |
| Hierarchy validation | PASS ✓ | 100% RDMAP linking rate |
| Schema compliance | PASS ✓ | All required fields present |
| Source verification | PASS ✓ | 100% sourcing completeness |
| Consolidation metadata | PASS ✓ | 2 consolidations properly documented |
| Type consistency | PASS ✓ | Status fields match sourcing |

**Issues Found:** 0 critical, 0 important, 0 minor, 0 warnings

### Expected Information Gaps

**Total unique gaps:** 100
**Total gap instances:** 105

**Most common transparency gaps:**
- Validation rule specifications (2×)
- Error correction procedures (2×)
- Conflict resolution procedures (2×)
- Error handling procedures (2×)
- Backup verification procedures (2×)

These gaps represent documentation limitations in the source paper (procedures mentioned but not detailed), not extraction errors. They are appropriately captured as implicit RDMAP items where identifiable.

## Extraction Quality Metrics

### Sourcing Discipline

- **Evidence:** 66/66 with verbatim_quote (100%)
- **Claims:** 73/73 with verbatim_quote (100%)
- **Implicit Arguments:** 6/6 with trigger infrastructure (100%)
- **Explicit RDMAP:** 21/21 with verbatim_quote (100%)
- **Implicit RDMAP:** 9/9 with trigger infrastructure (100%)

### RDMAP Hierarchy Completeness

- **Designs:** 2 items, all with child methods
- **Methods:** 8 items, all linked to designs (100%)
- **Protocols:** 20 items, all linked to methods (100%)
- **Full chain coverage:** 100% of protocols trace to designs through methods

## Notable Extraction Decisions

1. **Conservative RDMAP consolidation:** Accepted 6.25% reduction (below 15-20% target) as appropriate for technical paper where each protocol describes distinct operational procedure

2. **Workflow integration pattern:** P011/P012 daily workflows subsumed P001/P002 methodology descriptions as they describe the same procedures at different levels of detail

3. **Implicit method extraction:** Training (IM001) extracted despite minimal documentation because explicitly identified as "main project aim" with multiple trigger passages

4. **Troubleshooting protocols:** Device recovery (IP001) and GPS troubleshooting (IP002) extracted as implicit protocols based on Results section descriptions of problems and solutions

## Assessment Readiness

**Ready for credibility assessment:** YES ✓

**Strengths:**
- 100% sourcing completeness prevents hallucination
- Complete RDMAP hierarchy enables systematic assessment
- High methods transparency facilitates evaluation
- Well-documented consolidations preserve source integrity

**Considerations for assessment:**
- 30% implicit RDMAP indicates transparency gaps in procedures
- System implementation paper with detailed workflows but less emphasis on scientific methods
- Training method (IM001) has low reconstruction confidence
- Multiple troubleshooting/recovery protocols inferred from Results section

## Files Generated

- `extraction.json` - Complete extraction (175 items)
- `validation_report.json` - Detailed validation results
- `pass1_claims_evidence.py` - Pass 1 extraction script
- `pass2_rationalization.py` - Pass 2 consolidation script
- `pass3_rdmap_extract.py` - Pass 3 initial RDMAP extraction
- `pass3_rdmap_continue.py` - Pass 3 system requirements extraction
- `pass3_rdmap_workflows.py` - Pass 3 detailed workflows extraction
- `pass3_rdmap_finalize.py` - Pass 3 completion script
- `pass4_implicit_rdmap.py` - Pass 4 Pattern 1 implicit extraction
- `pass4_implicit_continue.py` - Pass 4 Patterns 2-4 implicit extraction
- `pass5_rdmap_analysis.py` - Pass 5 consolidation analysis
- `pass5_rdmap_consolidate.py` - Pass 5 consolidation execution
- `pass6_validation.py` - Pass 6 validation script
- `pass6_fix_design_context.py` - Pass 6 hierarchy fix
- `summary.md` - This summary document

## Recommendations for Future Extractions

1. **Ensure design_context from start:** Add design_context references during Pass 3 extraction rather than fixing in Pass 6
2. **System implementation papers:** Expect high protocol counts and detailed workflows suitable for workflow integration consolidations
3. **Troubleshooting procedures:** Watch for implicit protocols in Results sections describing system problems and solutions
4. **Training methods:** Even when mentioned as important goals, training procedures often undocumented (extract as implicit with low confidence)

---

**Extraction completed:** 2025-10-29
**Extractor:** Claude Code + research-assessor skill
**Schema version:** 2.5
