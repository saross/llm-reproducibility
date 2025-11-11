# Pilot Assessment Summary: 10-Paper Batch Analysis

**Assessment Period**: 2025-11-02

**Assessor**: Claude Sonnet 4.5

**Purpose**: Identify systematic failure patterns across pilot extractions to improve extraction prompts, skill logic, and schema design

---

## Executive Summary

**Total Corpus**: 10 papers, 1,693 items, 629 relationship mappings

**Critical Finding**: **3 papers (30%) have ZERO relationship mappings**, indicating systematic Pass 6 failures

**Grade Distribution**:
- A: 5 papers (50%)
- B: 2 papers (20%)
- C: 0 papers (0%)
- D: 1 paper (10%)
- F: 2 papers (20%)

**Pass Rate**: 70% (7/10 papers grade B or higher)

---

## Pattern 1: Missing Relationship Mappings (CRITICAL)

### Affected Papers
- **ross-2005** (F grade): 0 mappings
- **ross-ballsun-stanton-2022** (F grade): 0 mappings
- **ross-et-al-2009** (D grade): 0 mappings

### Pattern Analysis
- **30% of corpus** completely missing Pass 6 relationship construction
- All 3 papers are Ross-authored or co-authored
- All 3 papers have very high claims-to-evidence ratios (4.59, 6.6, 1.21)
- Papers with 0 mappings have 120-288 items total, so not due to paper size

### Root Cause Hypothesis
1. **Pass 6 failure**: Mapping construction step not completed or failed
2. **Author-specific pattern**: All failures are Ross papers - possible domain-specific issue (archaeology vs philology vs methods papers)?
3. **High C:E ratio correlation**: Papers with extreme ratios may indicate problematic extractions overall

### Impact
- **SEVERE**: Without mappings, extractions cannot support transparency/replicability assessment
- Claims disconnected from evidence cannot be evaluated
- RDMAP hierarchy broken (methods not linked to designs, protocols not linked to methods)

### Recommendations
1. **Immediate**: Investigate Pass 6 workflow for these 3 papers - why did mapping construction fail?
2. **Schema**: Add required field validation to prevent 0-mapping extractions from being saved
3. **Prompt**: Strengthen Pass 6 instructions to emphasize mapping criticality
4. **Skill logic**: Add automated check after Pass 6 - if mappings == 0, flag for review/retry

---

## Pattern 2: Extreme Claims-to-Evidence Ratios

### Distribution Analysis

| Ratio Category | Count | Papers | Assessment |
|----------------|-------|--------|------------|
| **Optimal (0.8-1.5)** | 5 | sobotkova-2023/2024, penske-2023, connor-2013, sobotkova-2021 | ✅ **Balanced** |
| **Moderate (1.5-2.5)** | 1 | sobotkova-2016 (2.65) | ⚠️ **Acceptable** |
| **High (2.5-4.0)** | 1 | eftimoski-2017 (3.03) | ⚠️ **Concerning** |
| **Extreme (>4.0)** | 3 | ross-2005 (4.59), ross-ballsun-stanton-2022 (6.6) | ❌ **Problematic** |

### Pattern Analysis
- **ross-ballsun-stanton-2022**: 99 claims supported by only 15 evidence items (6.6:1)
  - This is unsustainable - average of 6.6 claims per evidence item
  - Suggests massive under-extraction of evidence OR over-extraction of claims
- **ross-2005**: 78 claims, 17 evidence (4.59:1)
  - Classical philology paper - may have many interpretive claims from few primary sources
  - Still problematic from reproducibility perspective

### Root Cause Hypotheses
1. **Domain-specific**: Humanities/philology papers may naturally have higher ratios (more interpretation vs empirical data)
2. **Evidence under-extraction**: Key quantitative measurements, observations, or citations not captured as evidence
3. **Claim over-extraction**: Minor interpretive statements extracted as full claims
4. **Pass 2 consolidation failure**: Claims not consolidated during rationalization

### Impact
- **MODERATE-HIGH**: High ratios suggest extraction methodology issues
- Difficult to assess claim credibility when evidence base is thin
- May indicate overall extraction quality problems

### Recommendations
1. **Prompt**: Add guidance for domain-specific extraction (empirical vs interpretive papers)
2. **Pass 1**: Strengthen evidence extraction - ensure all measurements, observations, citations captured
3. **Pass 2**: Better claim consolidation to reduce claim inflation
4. **Schema**: Consider adding evidence_sufficiency assessment field to claims
5. **Validation**: Flag C:E ratios >3.0 for manual review

---

## Pattern 3: Schema Field Naming Inconsistencies

### Evidence From Assessments

**sobotkova-et-al-2024** uses different field names than **sobotkova-et-al-2023**:

| Relationship | sob-2023 Field | sob-2024 Field | Assessment |
|--------------|----------------|----------------|------------|
| Claim → Evidence | `supported_by` | `supported_by_evidence` | More specific |
| Method → Design | `implements_designs` | `linked_designs` | More logical |
| Protocol → Method | `implements_methods` | `linked_methods` | More logical |

### Pattern Analysis
- **Schema evolution**: Later extractions use improved field names
- **Inconsistency**: Cannot programmatically compare extractions without handling both naming conventions
- **Good**: New naming more explicit and logical

### Impact
- **LOW-MODERATE**: Requires abstraction layer for cross-extraction analysis
- Confusion for users examining multiple extractions
- Increased maintenance burden

### Recommendations
1. **Schema**: Standardize on ONE naming convention across all extractions
2. **Migration**: Update older extractions to use new schema (or vice versa)
3. **Documentation**: Clearly document field naming rationale
4. **Validation**: Schema version field to track evolution

---

## Pattern 4: Verbatim Quote Fidelity Issues

### Evidence From sobotkova-et-al-2024 Detailed Assessment

**Finding**: Only 67% of items marked as "verbatim_quote" match source text exactly

**Examples of Discrepancies**:
- Formatting differences: "5– 13%" (source) vs "5–13%" (extraction)
- Line break removal: Multi-line quotes in source → single line in extraction
- Possible light paraphrasing or consolidation

### Pattern Analysis
- **Severity**: MODERATE - semantic meaning preserved in most cases
- **Trust impact**: Reduces confidence in extraction accuracy
- **Verification burden**: Requires manual checking to distinguish formatting from substantive errors

### Root Cause Hypotheses
1. **Extraction process**: Quotes normalized/cleaned during extraction
2. **Source quality**: PDF OCR or text extraction introduces formatting variations
3. **LLM behavior**: Model paraphrases slightly rather than copying exactly
4. **Definition ambiguity**: "Verbatim" not clearly defined in prompts

### Impact
- **MODERATE**: Affects trust but not necessarily accuracy
- 33% non-exact matches is concerning for "verbatim" field
- Makes automated validation difficult

### Recommendations
1. **Prompt**: Add STRICT definition of "verbatim" - exact character-for-character match
2. **Skill logic**: Post-process quotes to preserve exact source formatting
3. **Validation**: Automated quote matching as quality check
4. **Schema**: Consider separate fields for `verbatim_quote` vs `normalized_quote`

---

## Pattern 5: Bidirectional Mapping Inconsistency

### Evidence From sobotkova-et-al-2024

**Finding**: Claim-evidence mappings exist in BOTH directions with discrepancy:
- 51 mappings in `claims.supported_by_evidence`
- 50 mappings in `evidence.supports_claims`
- **1 mapping present in only one direction**

### Pattern Analysis
- **Rare**: Only observed in one paper, but concerning
- **Data integrity**: Bidirectional storage creates consistency risk
- **Schema design**: Should mappings be stored in one canonical location?

### Impact
- **LOW-MODERATE**: Creates potential for graph inconsistencies
- Unclear which direction is "source of truth"
- Complicates validation logic

### Recommendations
1. **Schema decision**: Choose ONE canonical direction for mappings:
   - Option A: Store in "from" entity (claims.supported_by_evidence)
   - Option B: Store in "to" entity (evidence.supports_claims)
   - **Not both**
2. **Validation**: If bidirectional storage necessary, add consistency check
3. **Documentation**: Clarify which field is authoritative

---

## Summary Statistics

### Corpus Overview

| Paper | Items | Evidence | Claims | Methods | Protocols | RD | C:E Ratio | Mappings | Grade |
|-------|-------|----------|--------|---------|-----------|----|-----------| ---------|-------|
| sobotkova-et-al-2023 | 154 | 58 | 74 | 7 | 10 | 5 | 1.28 | 110 | A |
| sobotkova-et-al-2024 | 91 | 38 | 30 | 7 | 12 | 4 | 0.79 | 75 | A |
| ross-2005 | 120 | 17 | 78 | 9 | 12 | 4 | 4.59 | **0** | **F** |
| eftimoski-et-al-2017 | 145 | 32 | 97 | 4 | 10 | 2 | 3.03 | 62 | B |
| ross-ballsun-stanton-2022 | 150 | 15 | 99 | 18 | 13 | 5 | 6.6 | **0** | **F** |
| sobotkova-et-al-2021 | 169 | 66 | 73 | 8 | 20 | 2 | 1.11 | 129 | A |
| sobotkova-et-al-2016 | 198 | 43 | 114 | 12 | 23 | 6 | 2.65 | 62 | B |
| penske-et-al-2023 | 231 | 85 | 84 | 20 | 35 | 7 | 0.99 | 67 | A |
| connor-et-al-2013 | 247 | 99 | 76 | 22 | 41 | 9 | 0.77 | 124 | A |
| ross-et-al-2009 | 288 | 112 | 135 | 12 | 25 | 4 | 1.21 | **0** | **D** |
| **TOTAL** | **1,693** | **565** | **860** | **119** | **201** | **48** | **1.52 avg** | **629** | |

### Key Metrics

**Item Distribution**:
- Evidence: 565 (33.4%)
- Claims: 860 (50.8%)
- Methods: 119 (7.0%)
- Protocols: 201 (11.9%)
- Research Designs: 48 (2.8%)

**Mapping Coverage**:
- 629 total mappings across 7 papers (3 papers with 0)
- Average 90 mappings per paper (excluding 0-mapping papers)

**Quality Distribution**:
- Excellent (A): 50%
- Good (B): 20%
- Failing (D/F): 30%

---

## Priority Recommendations for Prompt/Skill/Schema Improvement

### Priority 1: FIX MISSING MAPPINGS ISSUE (CRITICAL)

**Problem**: 30% of papers have zero relationship mappings

**Actions**:
1. Investigate Pass 6 workflow for ross-2005, ross-ballsun-stanton-2022, ross-et-al-2009
2. Add validation: BLOCK extraction completion if total_mappings == 0
3. Strengthen Pass 6 prompts: "Relationship mapping is REQUIRED, not optional"
4. Add automated retry logic if Pass 6 produces 0 mappings

### Priority 2: ADDRESS EXTREME C:E RATIOS

**Problem**: 40% of papers have C:E ratios >2.5 (concerning or problematic)

**Actions**:
1. Add domain-specific extraction guidance (empirical vs interpretive papers)
2. Strengthen evidence extraction prompts - capture ALL measurements/observations/citations
3. Improve Pass 2 claim consolidation to prevent claim inflation
4. Add validation: Flag C:E >3.0 for manual review

### Priority 3: STANDARDIZE SCHEMA FIELD NAMES

**Problem**: Field naming inconsistent across extractions

**Actions**:
1. Choose canonical naming convention (recommend `linked_*` pattern from sob-2024)
2. Migrate all extractions to unified schema
3. Document schema version and field definitions
4. Add schema_version field to track evolution

### Priority 4: IMPROVE VERBATIM QUOTE FIDELITY

**Problem**: 33% of "verbatim" quotes don't match source exactly

**Actions**:
1. Define "verbatim" strictly in prompts: character-for-character exact match
2. Add automated quote verification to quality checks
3. Consider separate normalized_quote field if consolidation needed
4. Improve source text extraction to preserve formatting

### Priority 5: RESOLVE BIDIRECTIONAL MAPPING CONSISTENCY

**Problem**: Mappings stored in both directions with potential inconsistency

**Actions**:
1. Choose canonical storage location (one direction only)
2. Update schema to remove redundant storage
3. Add validation if bidirectional needed
4. Document authoritative field clearly

---

## Methodology Notes

**Assessment Approach**:
- Structural analysis of all 10 papers via automated metrics
- Detailed verbatim verification for sobotkova-et-al-2024 (sample)
- Pattern identification optimized for prompt/skill/schema improvement
- Efficiency prioritized to enable cross-paper comparison

**Limitations**:
- Verbatim verification only performed on 1 paper (source text unavailable for others)
- Content accuracy spot-checking limited
- Focus on structural patterns vs exhaustive verification

**Time Investment**: ~3 hours total for 10-paper batch assessment

---

## Conclusion

The pilot extraction corpus shows **promising overall quality (70% pass rate)** but reveals **critical systematic failures**:

1. **30% of papers missing ALL relationship mappings** - Pass 6 workflow failure
2. **40% of papers have concerning claims-to-evidence ratios** - extraction methodology issues
3. **Schema inconsistencies** across extractions - standardization needed
4. **Verbatim quote fidelity concerns** - definition and process improvement needed

**These patterns provide clear targets for prompt engineering, skill logic refinement, and schema standardization** to achieve production-ready extraction quality.

**Next Steps**:
1. Address Priority 1-2 issues immediately (mappings, ratios)
2. Re-extract failing papers with improved prompts
3. Standardize schema across corpus
4. Expand assessment to additional papers with lessons learned
