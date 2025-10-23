# RDMAP Pass 1 Extraction Summary Report

**Paper:** Creating large, high-quality geospatial datasets from historical maps using novice volunteers (Sobotkova et al., 2023)

**Extraction Date:** October 23, 2025  
**Extractor:** Claude Sonnet 4.5  
**Schema Version:** 2.5  
**Pass:** 1 of 3 (Liberal Extraction)

---

## Extraction Scope

**Complete paper coverage:**
- ✅ Abstract
- ✅ Section 1: Introduction (subsections 1.1-1.4)
- ✅ Section 2: Approach (subsections 2.1-2.5)
- ✅ Section 3: Results (subsections 3.1-3.5)
- ✅ Section 4: Discussion (subsections 4.1-4.3)
- ✅ Section 5: Conclusion

---

## Final RDMAP Counts

| Category | Count | Percentage |
|----------|-------|------------|
| **Research Designs** | 10 | 21% |
| **Methods** | 13 | 27% |
| **Protocols** | 25 | 52% |
| **TOTAL RDMAP** | **48** | **100%** |

**Status Classification:**
- **Explicit items:** 40 (83%)
- **Implicit items:** 8 (17%)
- **Uncertain classifications:** 0

**Other Arrays (Preserved from Pass 2):**
- Evidence: 37 items
- Claims: 58 items
- Implicit Arguments: 8 items

---

## Distribution by Section

```
Section                    RDs   Methods  Protocols  Total   Notes
────────────────────────────────────────────────────────────────────────
Abstract + Section 1        7      4         0        11    Study framing,
                                                             questions,
                                                             frameworks

Section 2 (Approach)        2      6        13        21    Core methods &
                                                             detailed protocols

Section 3 (Results)         0      1        10        11    Operational details,
                                                             time requirements

Sections 4-5 (Disc/Conc)    1      2         2         5    Comparative analysis,
                                                             future work
────────────────────────────────────────────────────────────────────────
TOTAL                      10     13        25        48
```

---

## Key Findings by Section

### Abstract + Section 1 (Introduction)
**Character:** Strategic framing and theoretical foundations

**Content:**
- Research questions and hypotheses (RD001, RD002, RD003, RD004)
- Theoretical frameworks (RD005: Utility-Usability; RD006: HCI principles)
- Study design decisions (RD007: Three-activity approach)
- High-level methods mentioned but not procedurally described (M001-M004: all implicit)

**Status:** 7/11 explicit (all Research Designs); 4/11 implicit (all Methods)

### Section 2 (Approach)
**Character:** Core methodological descriptions

**Content:**
- Platform selection rationale (RD008, RD009)
- Data collection methods (M005-M010)
- Detailed protocols:
  - Record structures (P001)
  - Platform capabilities (P002-P003)
  - Workflow implementation (P004-P007)
  - Automation features (P008-P011)
  - Time tracking (P012-P013)

**Status:** 21/21 explicit (Methods section provides full procedural detail)

**Note:** Richest section for RDMAP with comprehensive protocol-level documentation

### Section 3 (Results)
**Character:** Operational implementation and outcomes

**Content:**
- 2010 baseline comparison (M011: implicit - limited documentation)
- Time requirements across both field seasons (P014-P017)
- Quality assurance protocols (P018)
- Deployment specifics (P019-P020)
- Performance issues and solutions (P021-P022)

**Status:** 10/11 explicit; 1/11 implicit

**Note:** Detailed measurements of actual implementation with timestamps and resource tracking

### Sections 4-5 (Discussion/Conclusion)
**Character:** Analysis and future directions

**Content:**
- Future research plan (RD010: ML comparison)
- Comparative analysis methods (M012: payoff thresholds; M013: ML benchmarking - both implicit)
- Post-processing protocols (P024)
- Proposed error mitigation (P025: implicit)

**Status:** 2/5 explicit; 3/5 implicit

**Note:** Discussion contains analytical methods not fully specified; Conclusion proposes future strategies

---

## Quality Assurance

### ✅ Sourcing Discipline
**All 48 items properly sourced:**
- **Explicit items (40):** `verbatim_quote` + `location` populated
- **Implicit items (8):** `trigger_text` + `trigger_locations` + `inference_reasoning` + `implicit_metadata` populated

**No hallucinations:** Every extraction traceable to specific paper passages

### ✅ Tier Assignment
**Three-tier hierarchy maintained:**
- **Research Designs (WHY):** Strategic decisions, questions, frameworks
- **Methods (WHAT):** General approaches, data collection strategies
- **Protocols (HOW):** Operational procedures, specific implementations

**No uncertain classifications flagged**

### ✅ Gap Documentation
**Expected information missing:** Documented where relevant
- Example: P001 missing specific attribute field names
- Example: M011 (2010 baseline) missing detailed training protocols
- Example: M012 missing threshold calculation formulas

### ✅ Cross-References
**Populated throughout:**
- `implements_designs` (Methods → Designs)
- `enables_methods` (Designs → Methods)
- `realized_through_protocols` (Methods → Protocols)
- `implements_method` (Protocols → Methods)

**Note:** Bidirectional consistency will be validated in Pass 3

---

## Notable Extraction Decisions

### 1. Abstract/Introduction Methods as Implicit
**Decision:** Methods M001-M004 extracted as implicit
**Rationale:** Mentioned in Introduction but not procedurally described. Full descriptions appear in Methods section (Section 2).
**Status:** `method_status = "implicit"` with `basis = "mentioned_undocumented"`

### 2. 2010 ArcGIS Comparison as Implicit
**Decision:** Method M011 extracted as implicit
**Rationale:** Results section mentions 2010 effort for comparison but lacks full methodological detail
**Evidence:** "Although we did not maintain detailed volunteer time-on-task records..."
**Transparency gap:** Limited detail about training procedures, support mechanisms

### 3. Discussion Analysis Methods as Implicit
**Decision:** Methods M012-M013 extracted as implicit
**Rationale:** Comparative calculations presented without full procedural protocols
**Gap:** How rates measured, threshold calculation formulas, uncertainty estimation methods not specified

### 4. Proposed Strategies vs Implemented Protocols
**Decision:** P025 (error mitigation) extracted as implicit with note "Proposed strategy, not implemented protocol"
**Rationale:** Paper mentions redundant digitization/peer review as possibilities, not as implemented procedures
**Trigger phrases:** "would likely eliminate", "would be easily mitigated by"

---

## Liberal Extraction Strategy

### Pass 1 Philosophy: "When in doubt, include it"
**Achieved:**
- ✅ Comprehensive capture across all sections
- ✅ Granular protocol extraction (25 protocols)
- ✅ Preserved uncertainty through documentation
- ✅ Over-extraction expected and acceptable

**Target:** 40-50% over-extraction relative to final Pass 2 output
**Actual:** 48 items extracted → expect ~38-41 items after Pass 2 rationalization (~15-20% reduction)

---

## Technical Notes

### Token Efficiency
- **Total tokens used:** ~95,000
- **Context window remaining:** ~95,000
- **Extraction completed section-by-section** to manage context

### Data Integrity
- ✅ Evidence, Claims, Implicit Arguments arrays untouched (37, 58, 8 items respectively)
- ✅ No data loss or corruption
- ✅ Duplicate entries identified and removed during merge

### Extraction Workflow
1. Abstract + Section 1 → 11 items (7 RDs, 4 Ms)
2. Section 2 → +21 items (2 RDs, 6 Ms, 13 Ps)
3. Section 3 → +11 items (1 M, 10 Ps)
4. Sections 4-5 → +5 items (1 RD, 2 Ms, 2 Ps)

**Total:** 48 RDMAP items

---

## Next Steps: Pass 2 Rationalization

### Objectives
1. **Consolidate related items** (target 15-20% reduction)
2. **Verify cross-references** (bidirectional consistency)
3. **Document consolidations** (metadata tracking)
4. **Flag remaining uncertainties**

### Expected Outcomes
- **Target count:** ~38-41 items (after consolidation)
- **Explicit/implicit ratio:** Likely unchanged (~83% explicit)
- **Quality improvement:** Better granularity matching assessment needs

### Consolidation Candidates
- **Methods M001-M004:** May consolidate if they reference same underlying approach
- **Protocols P014-P017:** Time requirement protocols may consolidate by season
- **Protocols P019-P020:** Deployment protocols may consolidate
- **Research Designs RD003-RD004:** TRAP aims may consolidate if addressing together

### Decision Principle (Pass 2)
**"Would I assess these items TOGETHER or SEPARATELY?"**
- Together → Consolidate
- Separately → Keep distinct

---

## Output Files

**Complete extraction:** `sobotkova_extraction_rdmap_pass1_COMPLETE.json`

**Section checkpoints:**
- `sobotkova_extraction_rdmap_pass1_section1.json`
- `sobotkova_extraction_rdmap_pass1_section2.json`
- `sobotkova_extraction_rdmap_pass1_section3.json`

---

## Extractor Notes

### Strengths of This Paper for RDMAP Extraction
1. **Excellent Methods section (Section 2):** Comprehensive procedural detail
2. **Results quantification (Section 3):** Detailed time tracking and measurements
3. **Transparent about gaps:** Authors acknowledge limited 2010 documentation
4. **FAIR principles:** Explicit attention to reproducibility

### Challenges Encountered
1. **Implicit methods in Introduction:** Required careful distinction between "mentioned" vs "described"
2. **Discussion analysis methods:** Calculations presented without full methodology
3. **Proposed vs implemented:** Required careful reading of verb tenses and modal auxiliaries

### Lessons for Future Extractions
- Methods sections contain most explicit protocols
- Introduction often contains implicit methods (mentioned but not described)
- Results contain operational details (time, measurements, outcomes)
- Discussion may contain analytical methods not fully specified

---

**Extraction Status:** ✅ RDMAP Pass 1 Complete  
**Ready for:** Pass 2 Rationalization  
**Estimated Pass 2 duration:** ~60-90 minutes
