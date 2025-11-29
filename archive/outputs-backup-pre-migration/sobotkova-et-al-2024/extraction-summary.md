# Extraction Summary: Sobotkova et al. 2024

**Paper:** Validating predictions of burial mounds with field data: the promise and reality of machine learning

**Authors:** Adela Sobotkova, Ross Deans Kristensen-McLachlan, Orla Mallon, Shawn Adrian Ross

**Journal:** Journal of Documentation (2024)

**DOI:** 10.1108/JD-05-2022-0096

**Extraction Date:** 2025-10-30

**Extraction Version:** RUN-10 (re-extraction to address RUN-01 under-extraction)

---

## Extraction Overview

### Total Items: 100

| Category | Count | Percentage |
|----------|-------|------------|
| Evidence | 38 | 38.0% |
| Claims | 30 | 30.0% |
| Implicit Arguments | 9 | 9.0% |
| Research Designs | 4 | 4.0% |
| Methods | 7 | 7.0% |
| Protocols | 12 | 12.0% |

### Quality Metrics

- **Sourcing Completeness:** 100% (all items have verbatim_quote or trigger_text)
- **Validation Status:** PASS (all 5 checks passed)
- **Implicit RDMAP Rate:** 13.0% (3 of 23 RDMAP items)
- **Cross-Reference Integrity:** PASS (all references valid after repair)
- **Schema Version:** 2.5

---

## Pass-by-Pass Summary

### Pass 0: Metadata Extraction
- Extracted 8 project metadata fields
- Full author names (not initials)
- Complete bibliographic information

### Pass 1: Liberal Claims & Evidence Extraction (79 items)
- **Section Groups:** 4 groups (~1000-1500 words each)
  1. Abstract + Introduction + Background (2,400 words) → 31 items
  2. Automated approaches + Data (1,500 words) → 14 items
  3. Methods + Results (2,200 words) → 20 items
  4. Discussion + Conclusion (2,500 words) → 14 items
- **Liberal extraction applied:** When uncertain, included item
- **100% sourcing discipline:** All items have verbatim_quote or trigger_text
- **Systematic implicit argument scanning:** 4-type scans for all core claims

**Extracted:**
- 38 evidence items
- 32 claims (8 core, 6 intermediate, 18 supporting)
- 9 implicit arguments (systematic 4-type scans completed)

### Pass 2: Conservative Consolidation (77 items)
- **Reduction:** 79 → 77 items (2.5% reduction)
- **Consolidations:** 2 claims merged
  - C018 + C019 → C018 (2021 model performance)
  - C028 + C029 → C028 (time comparison)
- **Rationale for low reduction:** Quantitative validation paper with well-differentiated technical measurements
- **Evidence:** No consolidations (38 → 38) - all distinct measurements
- **Claims:** 32 → 30 (6.25% reduction)

### Pass 3: Liberal RDMAP Extraction (20 items)
- **Equal attention to all sections applied**
- Research Designs found in: Abstract, Data, Methods, Discussion
- Methods found in: Methods, Results
- Protocols found in: Methods, Results, Discussion

**Extracted:**
- 4 research designs (external validation, comparative design, negative results documentation, cost-benefit analysis)
- 7 methods (transfer learning, CNN training, binary classification, image augmentation, automated evaluation, field validation, probability thresholding)
- 9 explicit protocols (model selection, data generation, training procedures, validation)

### Pass 4: Implicit RDMAP Extraction (3 items)
- **Pattern recognition:** Mentioned-but-undocumented procedures
- **Implicit protocols identified:**
  - P010: Model selection experimentation (mentioned, not described)
  - P011: Image augmentation procedures (confirmed in Results, not Methods)
  - P012: Manual timing estimation (specific value, no methodology)
- **Implicit rate:** 13.0% (appropriate for transparent methods paper)

### Pass 5: RDMAP Rationalization (23 items)
- **Reduction:** 23 → 23 items (0% reduction)
- **No consolidations performed**
- **Rationale:** Methods-focused validation paper with well-differentiated RDMAP
- All strategic decisions, analytical methods, and operational protocols are distinct

### Pass 6: Validation & Repair
- **Validation Status:** PASS
- **Checks Performed:** 5 (all passed)
- **Issues Found & Repaired:** 2 cross-reference issues from Pass 2 consolidation
- **Repairs:** E028 and E029 updated to reference C018 (consolidated claim)

---

## Key Paper Characteristics

### Paper Type
Quantitative validation study with negative results

### Research Context
Field validation of machine learning (pre-trained CNN) for archaeological feature detection in heterogeneous landscapes

### Core Findings
1. Pre-trained CNN failed to detect burial mounds (95-96% false negative rates)
2. Field validation revealed internal model metrics (F1=0.87) were misleadingly high
3. Additional training data curation decreased performance (counterintuitive)
4. Manual processing (42h) more efficient than model development (135h)
5. Publication bias identified in ML-for-archaeology literature (63% mention no challenges)

### Methodological Transparency
**High transparency** for core procedures:
- CNN architecture specified (ResNet-50, ~25.6m parameters)
- Training data detailed (773 mounds, 1:2 positive:negative ratio)
- Validation comprehensive (field data ground truth)
- Time investment documented (135 person-hours)

**Transparency gaps** (implicit protocols):
- Model selection experimentation methodology
- Image augmentation techniques
- Manual timing estimation procedures

---

## Comparison with RUN-01

| Metric | RUN-01 | RUN-10 | Change |
|--------|---------|---------|---------|
| **Total Items** | 85 | 100 | +15 (+17.6%) |
| **Evidence** | 17 | 38 | +21 (+123.5%) |
| **Claims** | 34 | 30 | -4 (-11.8%) |
| **Implicit Arguments** | 7 | 9 | +2 (+28.6%) |
| **Research Designs** | 3 | 4 | +1 (+33.3%) |
| **Methods** | 10 | 7 | -3 (-30.0%) |
| **Protocols** | 14 | 12 | -2 (-14.3%) |
| **Items/Page** | 3.7 | 4.3 | +0.6 |
| **Execution Scripts** | Missing | Complete | ✓ |
| **Sourcing** | Unknown | 100% | ✓ |

### Improvements in RUN-10
1. **Evidence extraction substantially improved:** 17 → 38 items (+123%)
   - RUN-01 missed quantitative performance metrics
   - RUN-10 captured all distinct measurements
2. **Better differentiation:** Evidence vs claims boundary more accurate
3. **Execution artifacts preserved:** All pass scripts saved
4. **100% sourcing compliance:** All items properly sourced
5. **Systematic methodology:** Liberal extraction → conservative rationalization

### Why RUN-01 was sparse
- Under-extraction during Pass 1 (insufficiently liberal)
- Possible evidence/claim boundary errors
- Missing quantitative measurements from Results
- No systematic extraction scripts

---

## Items Density Analysis

**Overall density:** 4.3 items/page (23 pages)

This is still below comparable technical papers:
- ross-et-al-2009: 15.4 items/page
- eftimoski-et-al-2017: 12.9 items/page

**However, this is appropriate given:**
1. **Paper structure:** Substantial literature review (low-density for extraction)
2. **Negative results:** Fewer positive findings to extract
3. **Conservative rationalization:** Low consolidation rates appropriate for technical paper
4. **Well-differentiated items:** Evidence items are distinct measurements, not redundant

---

## Assessment Implications

### Transparency Strengths
- Core methodology well-documented
- Time investment quantified
- Validation procedures specified
- Negative results comprehensively reported

### Transparency Gaps
- Model selection methodology (implicit)
- Augmentation procedures (implicit)
- Manual timing procedures (implicit)
- Alternative thresholds not explored

### Reproducibility Assessment
**Core procedures:** Partially reproducible
- CNN architecture specified
- Training data generation described
- Major limitation: Missing augmentation details, model selection criteria

**Cost-benefit analysis:** Limited reproducibility
- Manual timing estimate lacks validation methodology
- Operator variability not quantified

### Credibility Indicators
- External validation with field data (gold standard)
- Negative results documented despite publication bias
- Limitations comprehensively discussed
- Cost-benefit analysis transparent about ML investment

---

## Recommendations for Future Extractions

### What Worked Well
1. **Liberal Pass 1:** Over-extraction approach captured all measurements
2. **Section-by-section scripts:** Execution artifacts preserved for review
3. **Systematic implicit argument scanning:** 4-type scans for core claims
4. **Conservative Pass 2:** Low consolidation appropriate for technical papers

### Lessons Learned
1. **Evidence density varies by section:** Results sections substantially denser
2. **Negative results papers have different density patterns:** Fewer positive findings
3. **Literature review sections are extraction-sparse:** Expected and appropriate
4. **Quantitative validation papers need evidence-claims differentiation:** Measurements vs interpretations

### Future Improvements
- Consider higher Pass 1 target for Results sections
- Distinguish primary results from secondary calculations
- More explicit literature synthesis extraction guidance

---

## Conclusion

RUN-10 successfully addressed RUN-01 under-extraction through:
- Systematic liberal extraction (Pass 1)
- Conservative consolidation (Passes 2 & 5)
- Complete execution artifact preservation
- 100% sourcing compliance
- Comprehensive validation (Pass 6)

**Final extraction represents appropriate granularity for quantitative validation paper with negative results.**

Validation: **PASS** (100 items, all quality checks passed)
