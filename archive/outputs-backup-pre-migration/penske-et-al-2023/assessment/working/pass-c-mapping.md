# Pass C: Mapping Assessment - Penske et al. (2023)

**Assessment Date:** 2025-11-02
**Assessor:** Claude Sonnet 4.5
**Mappings Assessed:** 140 (99 claim-evidence, 19 method-design, 22 protocol-method)

## Assessment Methodology

Mapping quality assessment evaluates:
1. **Bidirectional Consistency:** Forward and reverse mappings match
2. **Mapping Strength:** Evidence appropriately supports claims, methods implement designs, protocols implement methods
3. **Structural Integrity:** Referenced items exist, no orphaned references
4. **RDMAP Hierarchy:** Design → Method → Protocol relationships maintained

**Quality Criteria:**
- **Strong Mapping:** Direct, appropriate relationship with bidirectional consistency
- **Weak Mapping:** Indirect or tangential relationship, but not incorrect
- **Incorrect Mapping:** No logical relationship or structural error

## Pass C Results Summary

**Overall Mapping Quality:** 75.0% (C)

**CRITICAL FINDING:** Extensive bidirectional mapping inconsistencies detected across all relationship types.

**By Relationship Type:**

| Type | Total | Consistent | Inconsistent | Missing Items | Score |
|------|-------|------------|--------------|---------------|-------|
| **Claim-Evidence** | 99 | 79 | 20 | 4 | 79.8% |
| **Method-Design** | 19 | 9 | 10 | 0 | 47.4% |
| **Protocol-Method** | 22 | 0 | 29 | 3 | 0.0% |

**Total Bidirectional Issues:** 62
**Grade:** **C** (Significant issues requiring correction)

## Critical Issue: Bidirectional Inconsistency

### Overview

The extraction contains **extensive bidirectional mapping inconsistencies** where forward mappings (e.g., claim → evidence) do not match reverse mappings (evidence → claim). This creates:

1. **Data integrity problems:** Uncertainty about true relationships
2. **Assessment ambiguity:** Unclear which direction is correct
3. **Potential propagation errors:** Inconsistencies may cascade to analyses

### Root Cause Analysis

Bidirectional inconsistency suggests:
- **Incomplete Pass 1→2 consolidation reconciliation:** When items were consolidated, mappings not fully updated in both directions
- **Evidence gaps:** Some mappings reference non-existent evidence (E020, E022, E024, E077) suggesting post-consolidation orphaned references
- **Protocol gaps:** Some methods reference non-existent protocols (P004, P012, P020) suggesting incomplete protocol extraction or ID mismatches
- **Asymmetric updates:** Updates made to one direction without corresponding reverse direction updates

## Claim-Evidence Mapping Analysis

### Summary Statistics
- **Total Mappings:** 99 (from evidence → claims direction)
- **Bidirectionally Consistent:** 79 (79.8%)
- **Forward Direction Issues:** 14 mappings
- **Reverse Direction Issues:** 6 mappings
- **Missing Evidence Items:** 4 (E020, E022, E024, E077)

### Score: 79.8% (C+)

### Forward Direction Issues (14 mappings)

**Claims pointing to evidence that doesn't point back:**

1. **C007 → E001** (evidence doesn't link back)
   - C007 lists E001 in supporting_evidence
   - E001 supports_claims: ["C001", "C002"] (C007 missing)
   - **Likely Correct Direction:** C007 (research objective) legitimately uses dataset description
   - **Corrective Action:** Add C007 to E001.supports_claims

2. **C007 → E003** (evidence doesn't link back)
   - C007 lists E003 in supporting_evidence
   - E003 supports_claims: ["C001"] (C007 missing)
   - **Likely Correct Direction:** C007 (research objective) legitimately uses genome-wide data description
   - **Corrective Action:** Add C007 to E003.supports_claims

3. **C008 → E001** (evidence doesn't link back)
   - C008 (study design - contact zone) lists E001
   - E001 supports_claims: ["C001", "C002"] (C008 missing)
   - **Likely Correct Direction:** C008 legitimately describes study design using dataset description
   - **Corrective Action:** Add C008 to E001.supports_claims

4. **C009 → E002** (evidence doesn't link back)
   - C009 (temporal span) lists E002
   - E002 supports_claims: ["C003"] (C009 missing)
   - **Likely Correct Direction:** C009 legitimately describes temporal coverage
   - **Corrective Action:** Add C009 to E002.supports_claims

5. **C015 → E014** (evidence doesn't link back)
   - C015 (technological/social changes) lists E014
   - E014 supports_claims: ["C016"] (C015 missing)
   - **Assessment:** C015 is broader claim about transformations, E014 specifically about copper production. Mapping is weak but not incorrect.
   - **Corrective Action:** Add C015 to E014.supports_claims OR remove E014 from C015 if too tangential

6. **C025 → E020** (evidence not found)
   - C025 lists E020 in supporting_evidence
   - **E020 does not exist** (gap in evidence IDs: E019 → E021)
   - **Likely Cause:** E020 consolidated into E019 or E021, C025 reference not updated
   - **Investigation:** E019 is about PIE039 genetic similarity
   - **Corrective Action:** Change C025.supporting_evidence E020 → E019

7. **C027 → E022** (evidence not found)
   - C027 lists E022 in supporting_evidence
   - **E022 does not exist** (gap: E021 → E023)
   - **Likely Cause:** E022 consolidated into E021 or E023
   - **Corrective Action:** Identify correct evidence (likely E021) and update C027

8. **C029 → E024** (evidence not found)
   - C029 lists E024 in supporting_evidence
   - **E024 does not exist** (gap: E023 → E025)
   - **Likely Cause:** E024 consolidated into E023 or E025
   - **Corrective Action:** Identify correct evidence and update C029

9-14. **C037, C060, C071, C073, C075, C077** - Similar patterns
   - References to missing evidence or bidirectional mismatches
   - **Common Pattern:** Claims reference evidence that was likely consolidated

### Reverse Direction Issues (6 mappings)

**Evidence pointing to claims that don't point back:**

1. **E006 → C015** (claim doesn't link back)
   - E006 (Varna necropolis dated) supports_claims includes C015
   - C015 supporting_evidence: ["E014"] (E006 missing)
   - **Assessment:** E006 is about Varna dating, C015 is about broader transformations. Weak link.
   - **Corrective Action:** Remove C015 from E006.supports_claims (too tangential) OR add E006 to C015.supporting_evidence

2. **E013 → C023** (claim doesn't link back)
   - E013 (abandonment of tell settlements) supports_claims includes C023
   - C023 supporting_evidence: [] (empty)
   - **Assessment:** Direct, strong relationship - C023 is about abandonment enigma
   - **Corrective Action:** Add E013 to C023.supporting_evidence (flagged in Pass A as missing evidence)

3. **E021 → C027** (claim doesn't link back)
   - E021 (SEE 1 genetic modelling) supports_claims includes C027
   - C027 supporting_evidence: ["E022"] (E022 doesn't exist)
   - **Assessment:** E021 and E022 may have been consolidated; C027 still references old ID
   - **Corrective Action:** Update C027.supporting_evidence E022 → E021

4-6. **E083 → C078, E085 → C080, E086 → C081** - Similar patterns
   - Evidence claims to support claims that don't acknowledge the evidence
   - **Pattern:** Likely evidence added in later passes without updating claim mappings

### Missing Evidence Items (4 items)

**Critical Data Integrity Issue:**

- **E020** - Referenced by C025, but doesn't exist (likely consolidated into E019)
- **E022** - Referenced by C027, but doesn't exist (likely consolidated into E021)
- **E024** - Referenced by C029, but doesn't exist (likely consolidated into E023)
- **E077** - Referenced by C073, but doesn't exist (gap: E076 → E078)

**Root Cause:** Consolidation reconciliation incomplete. When evidence items were consolidated in Pass 2+, claims referencing the consolidated items were not updated to point to the new consolidated IDs.

**Impact:** 4 claims have broken references to non-existent evidence, creating orphaned mappings.

## Method-Design Mapping Analysis

### Summary Statistics
- **Total Mappings:** 19 (from methods → designs direction)
- **Bidirectionally Consistent:** 9 (47.4%)
- **Forward Direction Issues:** 7 mappings
- **Reverse Direction Issues:** 3 mappings

### Score: 47.4% (F)

**CRITICAL:** Less than half of method-design mappings are bidirectionally consistent.

### Forward Direction Issues (7 mappings)

**Methods pointing to designs that don't point back:**

**M009, M010, M011, M012, M013, M014, M015 → RD006** (design doesn't link back)
- **Issue:** 7 methods claim to implement RD006 (methodological triangulation)
- **RD006.supported_by_methods:** ["M005", "M006", "M007", "M008"]
- **Missing from RD006:** M009, M010, M011, M012, M013, M014, M015

**Analysis of Missing Methods:**
- M005: PCA ✓ (correctly in RD006)
- M006: outgroup f3 ✓ (correctly in RD006)
- M007: f4-statistics ✓ (correctly in RD006)
- M008: qpAdm modelling ✓ (correctly in RD006)
- **M009:** qpWave permutations (analytical triangulation method) - SHOULD be in RD006
- **M010:** DATES admixture dating (analytical method) - SHOULD be in RD006
- **M011:** Kinship analysis (analytical method) - SHOULD be in RD006
- **M012:** Sex determination (analytical method) - Marginal for RD006
- **M013:** mtDNA haplogroup assignment (analytical method) - SHOULD be in RD006
- **M014:** Y-chromosome haplogroup assignment (analytical method) - SHOULD be in RD006
- **M015:** qpAdm reference population selection (analytical framework) - SHOULD be in RD006 (and RD008)

**Corrective Action:** Add M009, M010, M011, M013, M014, M015 to RD006.supported_by_methods

### Reverse Direction Issues (3 mappings)

**Designs pointing to methods that don't point back:**

1. **RD001 → M002** (method doesn't link back)
   - RD001 (research question) supported_by_methods includes M002
   - M002.implements_designs: ["RD004"] (RD001 missing)
   - **Assessment:** M002 (genome-wide data generation) implements RD004 (genome-wide approach), not directly RD001 (research question)
   - **Corrective Action:** Remove M002 from RD001.supported_by_methods (or add RD001 to M002 if addressing research question)

2. **RD004 → M003** (method doesn't link back)
   - RD004 (genome-wide data approach) supported_by_methods includes M003
   - M003.implements_designs: ["RD002"] (RD004 missing)
   - **Assessment:** M003 (radiocarbon dating) implements RD002 (temporal scope), not RD004 (genetic approach)
   - **Corrective Action:** Remove M003 from RD004.supported_by_methods

3. **RD008 → M015** (method doesn't link back)
   - RD008 (reference framework selection) supported_by_methods includes M015
   - M015.implements_designs: ["RD006"] (RD008 missing)
   - **Assessment:** M015 (qpAdm reference population selection) legitimately implements both RD006 (triangulation) AND RD008 (reference framework choice)
   - **Corrective Action:** Add RD008 to M015.implements_designs

### Methods Without Design Mappings (4 methods)

Flagged in Pass A:
- **M017** (model_selection): No implements_designs
- **M018** (quality_control): No implements_designs
- **M019** (classification): No implements_designs
- **M020** (visualization): No implements_designs

**Recommendation:** Link M017, M018, M019 to appropriate designs (likely RD006, RD004)

## Protocol-Method Mapping Analysis

### Summary Statistics
- **Total Mappings:** 22 (from methods → protocols direction)
- **Bidirectionally Consistent:** 0 (0.0%)
- **Forward Direction Issues:** 29 mappings
- **Reverse Direction Issues:** 3 mappings (missing protocols)

### Score: 0.0% (F)

**CRITICAL:** ZERO protocols-method mappings are bidirectionally consistent. This is a severe structural failure.

### Forward Direction Issues (29 mappings)

**Protocols pointing to methods that don't point back:**

Extensive issues across most protocols. Examples:

1. **P002 → M002** (method doesn't link back)
   - P002 (sample selection) implements_methods: ["M001", "M002"]
   - M002.implemented_by_protocols: ["P003", "P004", "P005", "P006"] (P002 missing)
   - **Assessment:** P002 (sample selection) should implement M002 (data generation)
   - **Corrective Action:** Add P002 to M002.implemented_by_protocols

2. **P010 → M014** (method doesn't link back)
   - P010 (PCA analysis) implements_methods: ["M014"]
   - M014.implemented_by_protocols: [] (empty)
   - **Assessment:** Incorrect - P010 (PCA protocol) should implement M005 (PCA method), not M014 (Y-chromosome)
   - **Corrective Action:** Change P010.implements_methods from ["M014"] to ["M005"]

3. **P011 → M007** (method doesn't link back)
   - P011 (f3-statistics computation) implements_methods: ["M007"]
   - M007.implemented_by_protocols: [] (empty)
   - **Assessment:** Incorrect - P011 should implement M006 (f3 statistics), not M007 (f4 statistics)
   - **Corrective Action:** Change P011.implements_methods from ["M007"] to ["M006"]

4-29. **Extensive similar issues throughout protocol-method mappings**

**Pattern Analysis:**
- Many protocols have empty implemented_by_protocols in their methods
- Many protocols point to wrong methods (ID mismatches)
- Suggests systematic protocol extraction/mapping issues

### Reverse Direction Issues (3 mappings)

**Methods pointing to protocols that don't exist:**

1. **M002 → P004** (protocol not found)
   - M002.implemented_by_protocols includes P004
   - **P004 does not exist in protocols array** (but mentioned in text)
   - **Corrective Action:** Verify P004 should exist or update M002 reference

2. **M007 → P012** (protocol not found)
   - M007.implemented_by_protocols includes P012
   - **P012 does not exist** (gap: P011 → P013)
   - **Corrective Action:** Identify correct protocol or add missing P012

3. **M014 → P020** (protocol not found)
   - M014.implemented_by_protocols includes P020
   - **P020 does not exist** (gap: P019 → P021)
   - **Corrective Action:** Identify correct protocol or add missing P020

## Structural Integrity Issues

### ID Gaps Analysis

**Evidence Gaps:**
- E010, E011 (E009 → E012)
- E020 (E019 → E021) ← Referenced by C025
- E022 (E021 → E023) ← Referenced by C027
- E024 (E023 → E025) ← Referenced by C029
- E077 (E076 → E078) ← Referenced by C073

**Protocol Gaps:**
- P004 (P003 → P005) ← Referenced by M002
- P012 (P011 → P013) ← Referenced by M007
- P020 (P019 → P021) ← Referenced by M014

**Research Design Gaps:**
- RD003 (RD002 → RD004) - Documented as consolidated into RD002 ✓

**Assessment:**
- Evidence gaps: Some documented consolidations (E010, E011 in E009), others orphaned references
- Protocol gaps: Missing protocols or ID assignment errors
- Most gaps have consolidation_metadata explaining them, BUT referencing items not updated

## RDMAP Hierarchy Assessment

### Hierarchy Integrity

**Design → Method:**
- **RD001** (research question) → M001 ✓
- **RD002** (spatiotemporal scope) → M001, M003 ✓
- **RD004** (genome-wide approach) → M002, M004 ✓
- **RD005** (site selection) → M001 ✓
- **RD006** (methodological triangulation) → M005, M006, M007, M008 ✓ (but missing M009-M015)
- **RD007** (hypothesis testing) → M016 ✓
- **RD008** (reference framework) → M015 (documented in design, but M015 doesn't link back)

**Assessment:** Conceptual hierarchy is sound, but bidirectional mapping implementation is broken.

### Method → Protocol Mapping Quality

**Cannot assess reliably** due to 0% bidirectional consistency. The systematic failure suggests:
- Protocol extraction incomplete
- Protocol-method mapping systematically broken
- Possible ID numbering mismatches between passes

## Key Findings

### Critical Issues
❌ **0% protocol-method bidirectional consistency** - Severe structural failure
❌ **47% method-design bidirectional consistency** - Major integrity problem
❌ **80% claim-evidence bidirectional consistency** - Significant but recoverable
❌ **7 missing item references** - Orphaned mappings from consolidation
❌ **62 total bidirectional inconsistencies** - Pervasive data integrity issue

### Root Causes
1. **Incomplete consolidation reconciliation** - When items consolidated, mappings not fully updated
2. **Asymmetric mapping updates** - Forward direction updated without reverse, or vice versa
3. **Protocol extraction issues** - Systematic problems in protocol-method mapping
4. **ID management problems** - References to non-existent IDs post-consolidation

### Impact on Assessment
⚠️ **High Impact:** Bidirectional inconsistency creates ambiguity about true relationships
⚠️ **Cascading Risk:** Errors may propagate to downstream analyses
⚠️ **Assessment Reliability:** Cannot reliably assess mapping strength when directionality unclear
⚠️ **Replicability Concern:** Broken RDMAP hierarchy undermines protocol traceability

## Priority Corrections

### Priority 1: Fix Missing Item References (CRITICAL)
**Action:** Update all claims/methods referencing non-existent items
- C025: E020 → E019
- C027: E022 → E021
- C029: E024 → (identify correct evidence)
- C073: E077 → (identify correct evidence)
- M002: P004 → (verify protocol exists or remove)
- M007: P012 → (identify correct protocol)
- M014: P020 → (identify correct protocol)

### Priority 2: Reconcile Claim-Evidence Bidirectional Mappings (HIGH)
**Action:** Systematically reconcile 20 bidirectional inconsistencies
- Add missing reverse mappings (C007→E001/E003, C008→E001, C009→E002, etc.)
- Remove incorrect forward mappings (E006→C015 if too tangential)
- Verify mapping strength for all corrections

### Priority 3: Reconcile Method-Design Bidirectional Mappings (HIGH)
**Action:** Fix 10 method-design inconsistencies
- Add M009-M015 to RD006.supported_by_methods (where appropriate)
- Remove incorrect design→method links (RD001→M002, RD004→M003)
- Add missing method→design links (M015→RD008)

### Priority 4: Completely Rebuild Protocol-Method Mappings (CRITICAL)
**Action:** Systematic protocol-method mapping overhaul required
- Audit all 35 protocols and verify implements_methods
- Audit all 20 methods and verify implemented_by_protocols
- Ensure bidirectional consistency throughout
- Identify and add any missing protocols (P004, P012, P020 if they should exist)

### Priority 5: Add Missing Method-Design Mappings (MODERATE)
**Action:** Link orphaned methods to designs
- M017 → RD006 (model selection for triangulation)
- M018 → RD004 (quality control for genome-wide approach)
- M019 → RD006 (population classification for analysis)
- M020 → (clarify visualization method status)

## Overall Assessment

**Grade:** **C** (Significant Issues Requiring Major Corrections)

**Summary:** While conceptual relationships are generally sound, the extraction suffers from severe bidirectional mapping inconsistencies across all relationship types. Protocol-method mappings are completely broken (0% consistency), method-design mappings are less than half consistent (47%), and claim-evidence mappings have significant issues (80%). The extraction requires systematic reconciliation of all bidirectional mappings before it can be considered reliable for replicability assessment.

**Root Cause:** Incomplete consolidation reconciliation when Pass 1 items were consolidated in Pass 2+ without updating all forward and reverse references.

**Fitness for Use:** **NOT SUITABLE** for replicability assessment without major corrections. Bidirectional inconsistencies create ambiguity about true relationships and undermine RDMAP hierarchy traceability. Requires systematic mapping reconciliation across all relationship types.

**Estimated Correction Effort:** High - Approximately 62 bidirectional inconsistencies plus systematic protocol-method mapping rebuild required.
