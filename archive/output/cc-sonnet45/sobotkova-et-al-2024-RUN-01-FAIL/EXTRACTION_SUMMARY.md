# Extraction Summary: Sobotkova et al. 2024

**Paper:** Validating predictions of burial mounds with field data: the promise and reality of machine learning  
**Authors:** Adela Sobotkova, Ross Deans Kristensen-McLachlan, Orla Mallon, Shawn Adrian Ross  
**Year:** 2024  
**Journal:** Journal of Documentation  
**Extraction Date:** 2025-10-29  
**Extractor:** Claude Code (Claude Sonnet 4.5) - research-assessor skill

---

## Extraction Statistics

### Total Items Extracted: 85

**Claims & Evidence (58 items):**
- Evidence: 17 items
- Claims: 34 items
- Implicit Arguments: 7 items

**RDMAP - Research Designs, Methods, Protocols (27 items):**
- Research Designs: 3 items (all explicit)
- Methods: 10 items (6 explicit, 4 implicit)
- Protocols: 14 items (10 explicit, 4 implicit)

### RDMAP Status Distribution

**Explicit RDMAP:** 19 items (70.4%)
**Implicit RDMAP:** 8 items (29.6%)

Implicit ratio within expected 20-40% range for empirical papers, indicating appropriate balance between documented and undocumented methodology.

---

## Workflow Summary

### Pass 1: Claims & Evidence (Liberal Extraction)
- **Sections processed:** 6 section groups using flexible chunking (~1000 words per group)
- **Items extracted:** 72 items (24 evidence, 41 claims, 7 implicit arguments)
- **Strategy:** Liberal over-capture with systematic 4-type implicit argument scanning
- **Key findings:** Dense quantitative validation paper with extensive performance metrics

### Pass 2: Claims & Evidence (Rationalization)
- **Consolidations:** 10 consolidations using empirical graph analysis
- **Reduction:** 19.4% (72 → 58 items)
- **Primary method:** Identical support pattern consolidation
- **Quality:** All consolidations maintain complete information with proper sourcing

### Pass 3: RDMAP Explicit Extraction
- **Items extracted:** 19 items (3 designs, 6 methods, 10 protocols)
- **Focus:** Documented methodology in Data and Methods sections
- **Coverage:** Transfer learning approach, CNN training, validation methodology

### Pass 4: RDMAP Implicit Scanning
- **Items found:** 8 implicit items (0 designs, 4 methods, 4 protocols)
- **Pattern distribution:**
  - Mentioned-but-undocumented: 7 items
  - Inferred-from-results: 1 item
- **Key gaps:** Visual examination methodology, visibility assessment protocol, model selection experimentation

### Pass 5: RDMAP Rationalization
- **Consolidations:** 1 consolidation (duplicate mosaicking procedure)
- **Reduction:** 3.6% (28 → 27 items)
- **Rationale:** Modest reduction reflects genuinely detailed methodology rather than over-extraction
- **Tier corrections:** 0 (all assignments verified correct)

### Pass 6: Validation & Quality Assurance
- **Sourcing completeness:** 100%
  - All evidence items: verbatim_quote present
  - All claims: verbatim_quote present
  - All implicit arguments: trigger_text present
- **Cross-references:** Validated and bidirectional
- **Expected information gaps:** Comprehensively flagged
- **Status:** PASS

---

## Paper Characteristics

### Methodological Transparency
**High documentation quality in explicit methodology:**
- Transfer learning rationale clearly stated with three justifications
- CNN architecture and parameters documented
- Training data preparation procedures detailed
- Validation methodology explicit

**Transparency gaps in implicit methodology:**
- Visual examination procedures undocumented (M-IMP-001)
- Visibility assessment criteria not specified (M-IMP-002)
- Model selection experimentation not detailed (M-IMP-003)
- GPS recording specifications incomplete (P-IMP-002)
- Preservation status assessment protocol undefined (P-IMP-003)

### Research Focus
Paper reports **FAILURE** of machine learning approach for burial mound detection:
- 95-96% false negative rates at 60% probability threshold
- 87-95% false positive rates
- Second run with curated training data performed worse than first run
- Systematic analysis of why CNN approach failed in heterogeneous landscape

### Assessment-Critical Features
1. **Comparative experimental design** - Two model runs testing curation effect
2. **External validation** - Field data validation essential to revealing internal metric inadequacy
3. **Quantitative performance metrics** - Extensive F1, precision, recall, TP/FP/FN rates
4. **Failure analysis** - Diagnostic investigation of model limitations
5. **Resource reporting** - 135 person-hours documented for development cost

---

## Extraction Quality Indicators

### Strengths
✓ 100% sourcing completeness (v2.5 hallucination prevention)  
✓ Systematic implicit argument scanning (7 arguments across 4 types)  
✓ Comprehensive RDMAP extraction (29.6% implicit ratio)  
✓ Complete consolidation traceability  
✓ All expected information gaps flagged  

### Characteristics
- Dense quantitative validation data requiring careful evidence/claim boundary management
- Negative results paper requiring precise framing of failure claims vs diagnostic evidence
- Implicit RDMAP primarily operational/assessment procedures rather than strategic design gaps
- Liberal extraction appropriate for detailed methodology section

---

## Notable Extraction Challenges

1. **Implicit argument complexity:** Paper's core finding (internal metrics misleading) required extracting unstated assumptions about metric validity (IA001)

2. **Consolidation granularity:** Performance metrics presented across multiple dimensions (TP, FP, FN rates) requiring assessment compatibility test to determine consolidation vs separation

3. **RDMAP boundary maintenance:** Distinguishing methodological descriptions (RDMAP) from effectiveness claims about methodology

4. **Negative results framing:** Extracting failure claims without mischaracterizing as author error vs legitimate exploration of approach limitations

---

## Files Generated

- `extraction.json` - Complete extraction (85 items, 15,456 lines)
- `EXTRACTION_SUMMARY.md` - This summary document

---

## Next Steps

This extraction demonstrates research-assessor skill performance on quantitative validation paper with negative results. Paper now available for:

1. Reproducibility assessment (RDMAP completeness analysis)
2. Transparency evaluation (implicit methodology gap analysis)
3. Claims-evidence relationship validation
4. Cross-paper comparison (variation testing vs sobotkova-et-al-2023 re-extraction)

**Queue Status:** Paper 2 of 8 complete. Ready to proceed to paper 3 (sobotkova-et-al-2021).

---

**Extraction Schema:** v2.5  
**Workflow Version:** 2.7.0  
**Extraction Complete:** 2025-10-29
