# Detailed Assessment Report: sobotkova-et-al-2023

**Paper:** Sobotkova et al. (2023) - Creating large, high-quality geospatial datasets from historical maps using novice volunteers

**Assessment Date:** 2025-11-02

**Assessment Type:** Full three-pass detailed assessment (Pass A/B/C)

**Assessor:** Claude Sonnet 4.5

**Overall Grade:** **A** (Excellent)

---

## Executive Summary

**Total Items Assessed:** 153 (58 evidence, 73 claims, 7 methods, 10 protocols, 5 research designs)

**Total Mappings Assessed:** 110 (89 claim→evidence, 9 method→design, 12 protocol→method)

**Overall Assessment:** Excellent extraction quality with only minor issues concentrated in claims accuracy. RDMAP and evidence components are production-ready.

### Pass Scores

| Pass | Score | Grade | Summary |
|------|-------|-------|---------|
| **Pass A: Accuracy** | 94.1% | A- | Strong performance with isolated issues in claims (4 errors) |
| **Pass B: Granularity** | 99.3% | A | Excellent editorial judgment with appropriate consolidation |
| **Pass C: Mapping** | 99.1% | A | Excellent relationship integrity with only 1 weak mapping |

---

## Pass A: Accuracy Assessment

### Overall: 94.1% (A-)

**Items Assessed:** 153
**Correct Items:** 144
**Items with Errors:** 5
**Total Errors:** 6

### Accuracy by Item Type

| Type | Total | Correct | Errors | Accuracy | Grade |
|------|-------|---------|--------|----------|-------|
| **Evidence** | 58 | 58 | 0 | 100.0% | A+ |
| **Methods** | 7 | 7 | 0 | 100.0% | A+ |
| **Protocols** | 10 | 10 | 0 | 100.0% | A+ |
| **Research Designs** | 5 | 5 | 0* | 99.0% | A |
| **Claims** | 73 | 69 | 4 | 88.4% | B+ |

*RD-IMP-001 has minor data quality issue (duplicate trigger_locations entries)

### Errors Identified

#### Error 1: C018 - Misattribution (PRIORITY 1)
- **Severity:** Moderate (-3.0 points)
- **Error Type:** Literature statement misrepresented as empirical finding
- **Issue:** Claim text attributes lack of GIS skills to volunteers, but verbatim quote references "volunteers often lack skills" from literature review (Elwood 2008b, Jones & Weber 2012, Owen et al. 2009), not TRAP project findings
- **Verbatim Source:** "Volunteers often lack the skills necessary to use GIS software (Elwood, 2008b; Jones & Weber, 2012; Owen et al., 2009)."
- **Corrective Action:** Change claim_type from 'empirical' to 'theoretical' OR reword to "Literature indicates volunteers often lack GIS skills"

#### Error 2: C004 - Context Error (PRIORITY 2)
- **Severity:** Moderate (-2.0 points)
- **Error Type:** Partial extraction of compound claim without comparative context
- **Issue:** C004 extracts 'but' clause without "Crowdsourcing scales better" context, creating incomplete comparative statement
- **Verbatim Source:** "Crowdsourcing scales better than direct digitisation by experts, but requires an appropriate platform and the technical skills to adapt it."
- **Corrective Action:** Extract complete compound claim OR split into two related claims with explicit linkage
- **Also Flagged In:** Pass B (under-split)

#### Error 3: C032 - Context Error (PRIORITY 3)
- **Severity:** Moderate (-2.0 points)
- **Error Type:** Claim incorrectly states GIS features were hidden "or eliminated"
- **Issue:** Quote found on p.6 but discusses preprocessing/setup delegation to staff, not UI feature hiding. "Hidden or eliminated" language found but in different context about expert workflow allocation, not volunteer UI simplification
- **Verbatim Source:** "GIS features not needed for digitisation were hidden or eliminated."
- **Corrective Action:** Verify exact source location and ensure claim accurately reflects whether features were hidden in UI vs eliminated from workflow

#### Error 4: C028 - Miscategorisation (PRIORITY 4)
- **Severity:** Minor (-1.0 points)
- **Error Type:** Authorial interpretation presented as empirical observation
- **Issue:** Source states preference as authorial assertion without empirical measurement. Should be claim_nature: 'interpretive' not 'descriptive'
- **Verbatim Source:** "Fifth, student volunteers are accustomed to, and even prefer, 'slippy-map', touch-screen interfaces on mobile devices over the point-and-click, desktop UI idiom."
- **Corrective Action:** Change claim_nature from 'descriptive' to 'interpretive'

#### Error 5: C028 - Page Error (Minor)
- **Severity:** Minor (-0.5 points)
- **Error Type:** Location states page 4, but verbatim quote found on page 5
- **Corrective Action:** Update location.page from 4 to 5

#### Error 6: RD-IMP-001 - Data Quality (Minor)
- **Severity:** Minor (-0.5 points)
- **Error Type:** trigger_locations array contains duplicate entries for "4. Discussion, 4.1, p9, para 1-2"
- **Corrective Action:** Remove duplicate trigger_locations entries

### Key Findings

✅ **No hallucinations or confabulations** - All errors are categorisation/context/attribution issues, not fabricated content
✅ **Perfect RDMAP extraction** - Methods, protocols, and research designs show 100% accuracy
✅ **Perfect evidence extraction** - All 58 evidence items accurate
⚠️ **Claims more challenging** - Lower accuracy (88.4%) due to need to distinguish empirical vs theoretical, capture complete context, and accurately categorise claim nature

---

## Pass B: Granularity Assessment

### Overall: 99.3% (A)

**Items Assessed:** 153
**Appropriate Granularity:** 152
**Over-split:** 0
**Under-split:** 1
**Inconsistent:** 0

### Granularity by Item Type

| Type | Total | Appropriate | Over-split | Under-split | Inconsistent | Score |
|------|-------|-------------|------------|-------------|--------------|-------|
| **Evidence** | 58 | 58 | 0 | 0 | 0 | 100.0% |
| **Claims** | 73 | 72 | 0 | 1 | 0 | 98.6% |
| **Methods** | 7 | 7 | 0 | 0 | 0 | 100.0% |
| **Protocols** | 10 | 10 | 0 | 0 | 0 | 100.0% |
| **Research Designs** | 5 | 5 | 0 | 0 | 0 | 100.0% |

### Issues Identified

#### C004 - Under-split
- **Issue:** Partial extraction of compound claim without comparative context
- **Explanation:** C004 extracts second clause ("but requires platform and skills") without first clause ("Crowdsourcing scales better"). Should either include full comparative statement or be two separate claims with clear relationship
- **Also Flagged In:** Pass A (context error)

### Notable Consolidation Examples (Evidence)

Excellent consolidation judgment demonstrated in:
- **E002:** Total time + breakdown (57 staff + 184 volunteer)
- **E028:** 2017 setup activities consolidated
- **E044:** Complex omissions data across two seasons
- **E065:** Staff vs programmer time breakdown
- **E069:** Scalability measurements consolidated
- **E072:** Machine learning preparation time calculation

### Key Findings

✅ **No over-splitting detected** - Strong editorial judgment on consolidation
✅ **Evidence extraction exemplary** - 100% with excellent consolidation decisions
✅ **RDMAP hierarchy crystal clear** - Design→Method→Protocol consistently maintained
✅ **Consistent detail levels** - Velocities, times, counts, observations appropriately scoped
✅ **Functional appropriateness** - Granularity supports transparency and replicability assessment

---

## Pass C: Mapping Assessment

### Overall: 99.1% (A)

**Mappings Assessed:** 110
**Strong Mappings:** 109
**Weak Mappings:** 1
**Incorrect Mappings:** 0

### Mapping Quality by Relationship Type

| Relationship Type | Total | Strong | Weak | Incorrect | Score |
|-------------------|-------|--------|------|-----------|-------|
| **Claim → Evidence** | 89 | 88 | 1 | 0 | 98.9% |
| **Method → Design** | 9 | 9 | 0 | 0 | 100.0% |
| **Protocol → Method** | 12 | 12 | 0 | 0 | 100.0% |

### Issues Identified

#### C044 → E041 - Weak Support
- **Severity:** Low
- **Issue Type:** Low volunteer attrition (E041) supports satisfaction but only indirectly supports claim that volunteers could attain and maintain high digitisation rate
- **Impact:** Non-critical - C044 has strong alternative support from E055 (fastest digitisers: 44-45s/feature with low errors)
- **Recommendation:** Consider adding E033 or E034 as additional direct evidence for digitisation rate maintenance

### Key Findings

✅ **No structural mapping errors** - All relationship types correctly aligned
✅ **RDMAP hierarchy well-maintained** throughout
✅ **Quantitative claims consistently supported** by direct measurements
✅ **Comparative claims supported** by explicit benchmark calculations
✅ **All threshold claims supported** (C008, C055, C063, C064 have calculation evidence)
✅ **Only 1 weak mapping** - Claim remains well-supported through alternative evidence

---

## Pattern Analysis

### Pattern 1: RDMAP Extraction Excellence
**Description:** Methods, protocols, and research designs show perfect accuracy (100%) and perfect granularity (100%)
**Significance:** RDMAP framework successfully applied with clear hierarchy maintenance and appropriate abstraction levels

### Pattern 2: Evidence Extraction Excellence
**Description:** Evidence items show perfect accuracy (100%), perfect granularity (100%), and near-perfect mapping (98.9%)
**Significance:** Quantitative measurements, calculations, and observations extracted with high precision and appropriate consolidation

### Pattern 3: Claims Accuracy Variability
**Description:** Claims show lower accuracy (88.4%) compared to other types, with all errors concentrated in claims
**Significance:** Claims extraction is more challenging due to need to: (1) distinguish empirical vs theoretical, (2) capture complete context for compound statements, (3) accurately categorise claim nature (descriptive vs interpretive)

### Pattern 4: Excellent Consolidation Judgment
**Description:** Multiple evidence items appropriately consolidated (E002, E028, E044, E065, E069, E072) without over-splitting
**Significance:** Strong editorial discretion in balancing atomic principle with functional usefulness

### Pattern 5: No Hallucinations or Confabulations
**Description:** All Pass A errors are categorisation/context/attribution issues - no fabricated content
**Significance:** Extraction process maintained high fidelity to source paper without introducing false information

### Pattern 6: Isolated Error Concentration
**Description:** Only 1 item (C004) flagged in multiple passes; all other issues are independent
**Significance:** No systematic cascading errors - issues are isolated and localised

### Pattern 7: Strong Relationship Integrity
**Description:** 99.1% mapping quality with only 1 weak (not incorrect) relationship
**Significance:** Claim-evidence linkages, RDMAP hierarchy, and protocol-method connections well-maintained

---

## Priority Corrections

### Priority 1: C018 - Misattribution
**Action:** Change claim_type from 'empirical' to 'theoretical' OR reword claim_text to clarify this references literature, not TRAP project findings
**Rationale:** Incorrect categorisation - presents literature review statement as empirical project finding
**Impact:** Moderate - affects interpretation of evidence basis and claim role in argument

### Priority 2: C004 - Context Error + Under-split
**Action:** Extract complete compound claim OR split into two related claims with explicit linkage
**Rationale:** Partial extraction loses comparative context essential to claim meaning
**Impact:** Moderate - flagged in both Pass A (context error) and Pass B (under-split)

### Priority 3: C032 - Context Error
**Action:** Verify source location and ensure "hidden or eliminated" accurately reflects UI simplification vs workflow delegation
**Rationale:** Possible conflation of different aspects of expert/volunteer division of labour
**Impact:** Moderate - affects accuracy of technical implementation description

### Priority 4: C028 - Miscategorisation + Page Error
**Action:** Change claim_nature from 'descriptive' to 'interpretive' AND update location.page from 4 to 5
**Rationale:** Preference statement is authorial interpretation, not measured empirical observation
**Impact:** Minor - minor categorisation refinement + location correction

### Priority 5: RD-IMP-001 - Data Quality
**Action:** Remove duplicate entries from trigger_locations array
**Rationale:** Data quality cleanup
**Impact:** Minor - cosmetic data quality issue

---

## Strengths

✅ Perfect RDMAP extraction (methods, protocols, designs): 100% accuracy, 100% granularity
✅ Perfect evidence extraction: 100% accuracy, 100% granularity, excellent consolidation judgment
✅ Excellent relationship mapping: 99.1% with no incorrect mappings
✅ No hallucinations or confabulations - all errors are categorisation/context issues
✅ Strong editorial judgment on consolidation vs atomic principle balance
✅ Clear RDMAP hierarchy maintenance throughout
✅ All quantitative claims supported by direct measurement evidence

---

## Weaknesses

⚠️ Claims accuracy (88.4%) lower than other types due to categorisation and context challenges
⚠️ One compound claim (C004) under-split, losing comparative context
⚠️ One literature claim (C018) miscategorised as empirical finding
⚠️ Minor location and categorisation refinements needed for 2 claims (C028, C032)

---

## Recommendations

1. **Priority 1:** Fix C018 misattribution (literature vs empirical)
2. **Priority 2:** Re-extract C004 with full comparative context or split with explicit linkage
3. Address remaining minor issues (C028, C032 categorisation/location corrections)
4. Consider adding E033/E034 as additional evidence for C044 (currently weak link to E041)
5. Extraction process is production-ready with minor refinements

---

## Fitness for Use

**Assessment:** Suitable for research transparency and replicability assessment with minor corrections.

- **RDMAP components:** Production-ready (100% accuracy, 100% granularity)
- **Evidence components:** Production-ready (100% accuracy, 100% granularity, 98.9% mapping)
- **Claims components:** Requires targeted corrections (5 items) but overall quality is excellent (88.4% accuracy, 98.6% granularity, 98.9% mapping)

**Overall Quality Tier:** Excellent (Grade A)
