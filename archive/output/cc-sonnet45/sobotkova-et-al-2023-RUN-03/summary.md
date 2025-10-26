# Extraction Summary: Sobotkova et al. 2023

**Paper:** Creating large, high-quality geospatial datasets from historical maps using novice volunteers  
**Authors:** Adela Sobotkova, Shawn A. Ross, Christian Nassif-Haynes, Brian Ballsun-Stanton  
**Year:** 2023  
**Journal:** Applied Geography  
**DOI:** 10.1016/j.apgeog.2023.102967

**Extraction Date:** 2025-10-26  
**Extractor:** Claude Code (Sonnet 4.5) - Autonomous 5-Pass Workflow  
**Schema Version:** 2.5  
**Skill:** research-assessor v2.6

---

## Extraction Statistics

### Final Counts
| Category | Count | Details |
|----------|-------|---------|
| **Evidence** | 63 | Quantitative measurements, observations, qualitative data |
| **Claims** | 26 | Core, intermediate, and supporting claims |
| **Research Designs** | 6 | Research framing, study design choices |
| **Methods** | 6 | Data collection, evaluation, quality control approaches |
| **Protocols** | 8 | Specific procedures, configurations, standards |
| **TOTAL** | **109** | Complete extraction |

### Workflow Progression
- **Pass 1 (Liberal Extraction):** 70 evidence, 26 claims → Liberal over-capture
- **Pass 2 (Rationalization):** 63 evidence, 26 claims → 10% reduction, 6 consolidations
- **Pass 3 (RDMAP Extraction):** 6 designs, 6 methods, 8 protocols → Complete methodology extraction
- **Pass 4 (RDMAP Rationalization):** No changes → Items already well-scoped
- **Pass 5 (Validation):** 100% source verification pass rate → Assessment-ready

---

## Key Research Content

### Core Claims (3 major findings)
1. **Efficiency Thresholds:** Crowdsourcing most efficient for 10,000-60,000 feature datasets
2. **Platform Transferability:** Field data collection systems can serve as participatory geospatial platforms
3. **Quality Achievement:** Large (>10k features), high-quality (<6% error) dataset with reasonable resource demands

### Research Designs (Strategic Framework)
1. Mobile crowdsourcing feasibility assessment
2. Case study design in archaeological context
3. Comparative evaluation framework
4. Efficiency threshold hypothesis testing
5. Mobile platform selection for usability
6. Novice volunteer strategy for generalizability

### Methods (Tactical Approaches)
1. Crowdsourcing with field school participants
2. Customized mobile GIS (FAIMS Mobile)
3. Time-on-task measurement for efficiency evaluation
4. Random sampling quality assurance
5. On-device validation
6. Comparative analysis with desktop GIS and ML

### Key Evidence Highlights
- 10,827 features digitized in 241 person-hours (63s/record average)
- Error rate: 5.87% overall (2.8% excluding outlier)
- Setup: 51 hours total (36h programmer, 15h staff)
- 2017: 125.8h, 8,343 features, 54s/feature
- 2018: 63.6h, 2,484 features, 92s/feature

---

## Quality Metrics

### Source Verification
- **Evidence:** 100% (63/63) sourced with verbatim quotes
- **Claims:** 100% (26/26) sourced with verbatim quotes  
- **RDMAP:** 100% (20/20) sourced with verbatim quotes
- **Overall:** 100% pass rate (109/109 items)

### Consolidation Discipline
- **Pass 2:** 6 consolidations applied with full metadata
  - E002-004: Person-hours breakdown
  - E009-010: TRAP prior work
  - E043-044: Recoverable omissions
  - E041-042: Performance degradation
  - E051+057: Error patterns
  - E022+027: Customization time
- **Pass 4:** 0 consolidations (RDMAP well-scoped from Pass 3)

### Cross-Reference Integrity
- ✅ All claim-evidence relationships valid
- ✅ All design-method-protocol chains complete
- ✅ No broken references
- ✅ No orphaned items

---

## Extraction Highlights

### Methodological Completeness
- **6 Research Designs** (target: 4-6) ✅
  - Research framing: 2 items
  - Study design choices: 4 items
- **Complete RDMAP hierarchy** documented
- **All three tiers represented** (WHY → WHAT → HOW)

### Evidence Quality
- Quantitative measurements: 45+ items with precision metadata
- Temporal comparisons preserved (2017 vs 2018 not consolidated)
- Speed-accuracy correlations documented
- Setup/operational costs fully quantified

### Claim Structure
- Core claims: Clear efficiency thresholds and transferability findings
- Supporting claims: Quality metrics, usability outcomes, scalability
- All claims evidence-supported (no unsourced assertions)

---

## Assessment Readiness

This extraction is **READY FOR ASSESSMENT** with:

✅ **Complete sourcing:** Every item traceable to paper  
✅ **Structural integrity:** All relationships verified  
✅ **Consolidation transparency:** Full metadata for all merges  
✅ **Appropriate granularity:** Conservative consolidation preserves detail  
✅ **Methodological completeness:** Research designs, methods, protocols fully extracted  

### Use Cases
- **Transparency assessment:** All RDMAP items explicit with clear sourcing
- **Replicability evaluation:** Protocols documented with sufficient detail
- **Credibility analysis:** Evidence-claim relationships mapped
- **Methodological rigor:** Research design choices and rationales captured

---

## Files Generated

- `extraction.json` (primary output, 109 items)
- `validation-pass5.md` (this summary's companion)
- `extraction_continue.json` (Pass 1 continuation, archived)
- `extraction_backup.json` (safety backup, can be removed)

---

## Autonomous Workflow Success

This extraction demonstrates successful autonomous 5-pass workflow execution across multiple sessions:

1. ✅ Session continuity maintained through queue.yaml and extraction.json
2. ✅ All 5 passes completed without user intervention
3. ✅ Quality preserved through conservative consolidation
4. ✅ 100% source verification achieved
5. ✅ Assessment-ready output delivered

**Completion Time:** Single extended session  
**Auto-Compact Events:** 0 (maintained within token budget)  
**User Interventions:** 0 (fully autonomous after initial instruction)

---

**Generated:** 2025-10-26T07:49:32.995312  
**Status:** COMPLETE - VALIDATED - ASSESSMENT-READY
