# Pass C: Mapping Assessment - Connor et al. 2013

## Assessment Overview

Evaluating relationship quality between:
1. Evidence → Claims (98 mappings)
2. Protocols → Methods (40 mappings)
3. Research Designs → Methods (7 mappings via supported_by_methods)

**Total Mappings:** 145

## Mapping Structure Analysis

### Evidence → Claims (supports_claims)
- 98 relationships total
- Embedded in evidence items as `supports_claims` array
- Most evidence supports 1-2 claims; some support 0 (methodological evidence)

### Protocols → Methods (implements_methods)
- 40 relationships total
- Embedded in protocol items as `implements_methods` array
- Most protocols implement 1 method; some implement 0 (preparatory protocols)

### Research Designs ← Methods (supported_by_methods)
- 7 relationships total
- Embedded in research_design items as `supported_by_methods` array
- Each design supported by 0-3 methods

## Evidence → Claims Mapping Assessment

### Overall: EXCELLENT (98.0%)

**Total Mappings:** 98
**Strong Mappings:** 96
**Weak Mappings:** 2
**Incorrect Mappings:** 0

### Strong Mapping Examples

#### Quantitative Claims Well-Supported
- **C075 ← E071:** Artemisia/Poaceae percentages → Cold steppe dominance claim
- **C079 ← E080, E081:** Concentration increases → Oak woods expansion claim
- **C067 ← E062:** Magnetic susceptibility values → Lithological correlation claim

#### Chronological Claims Well-Supported
- **C001 ← E001-E005:** Five vegetation phases → Temporal transition claim
- **C095 ← E093:** Age-depth model result → Pleistocene-Holocene boundary claim
- **C097 ← E096:** Dated pollen zone → Cold steppe chronology claim

#### Comparative Claims Well-Supported
- **C098 ← E097:** Tenaghi Philippon correlation → Regional pattern claim
- **C099 ← E098:** Ezero record comparison → Similar assemblage interpretation

### Weak Mapping Issues

#### Weak Mapping 1: C063 ← No Evidence
- **Claim:** "Age-depth model constructed using Markov chain Monte-Carlo analysis with Bayesian statistical approach in OxCal 4.1.7"
- **Evidence Support:** None listed
- **Issue:** This is duplicate of E056 content (flagged in Pass A and B)
- **Severity:** Low - E056 exists as evidence item, so claim is supported, just not via mapping
- **Assessment:** Weak support due to structural issue, not conceptual
- **Recommendation:** Remove C063 as claim (consolidate into E056)

#### Weak Mapping 2: C096 ← E094, E095
- **Claim:** "Pollen source-area of large sites (>100 ha) is dominated by regional pollen component, representing spatial area of ~10^4-10^5 km^2"
- **Evidence:** E094, E095 (methodological principles from Jacobson & Bradshaw 1981, Sugita 2007)
- **Issue:** Claim categorised as "methodological" but actually presents established theory being applied
- **Severity:** Low - Evidence matches claim, but claim miscategorised (flagged in Pass A as misattribution)
- **Assessment:** Support relationship correct, but claim should be "theoretical" type
- **Impact:** Mapping structurally sound, categorisation issue only

### Evidence Items Without Claim Mappings (Appropriate)

#### Methodological Evidence (No Claims) - 11 items
- **E029:** Sampling intervals
- **E030:** Sample storage
- **E042:** Additional cores collection
- **E043:** Canal core sampling
- **E049:** PC-Ord software
- **E054:** Pollen concentrate dating procedure
- **E055:** Organic residue pre-treatment
- **E056:** Age-depth model construction (consolidated methods, not claim)
- **E039:** Magnetic susceptibility measurements (detailed methods)
- **E044:** Data presentation with Psimpoll
- **E046:** European Pollen Database source

**Assessment:** APPROPRIATE - These are methodological details supporting protocols/methods, not claims

### Multiple Evidence Supporting Single Claims (Appropriate)

#### Examples of Strong Multi-Evidence Support
- **C001 ← E001, E002, E003, E004, E005:** Five vegetation phases support overall transition claim
- **C028 ← E018, E027, E028:** Site location/coordinates from multiple sources
- **C053 ← E045-E052:** Statistical methods supported by multiple procedural steps
- **C061 ← E053, E088:** Radiocarbon dating supported by sample count mentioned twice
- **C083 ← E076, E079, E080, E081:** Oak woods expansion supported by multiple measurements

**Assessment:** EXCELLENT - Multi-evidence mappings provide robust support chains

### Claims Without Evidence Mappings (Issues)

Examining claims with no evidence support:
- **C063:** Age-depth model construction
  - **Issue:** Should be supported by E056 or removed (duplicate)
  - **Severity:** Moderate structural issue

All other claims have appropriate evidence support.

### Mapping Score: 98.0%
- 96 strong mappings
- 2 weak mappings (both due to structural issues flagged elsewhere)
- 0 incorrect mappings
- Deduction: -2 points for weak mappings

## Protocols → Methods Mapping Assessment

### Overall: EXCELLENT (97.5%)

**Total Mappings:** 40
**Strong Mappings:** 39
**Weak Mappings:** 1
**Incorrect Mappings:** 0

### Strong Mapping Examples

#### Pollen Analysis Chain
- **P009 → M001:** Pollen extraction → Pollen analysis
- **P010 → M001:** Pollen counting → Pollen analysis
- **P011 → M002:** NPP classification → NPP analysis

#### Charcoal Analysis Chain
- **P015 → M003:** Microscopic charcoal → Charcoal analysis
- **P016 → M003:** Macroscopic charcoal → Charcoal analysis

#### Magnetic Analysis Chain
- **P021 → M005:** Dual-frequency measurement → Magnetic susceptibility
- **P022 → M006:** VFTB analysis → Mineral magnetic analysis

#### Statistical Analysis Chain
- **P035 → M014:** DCA implementation → DCA method
- **P036 → M015:** Cluster analysis → Clustering method
- **P037 → M016:** Indicator species analysis → ISA method

### Weak Mapping Issue

#### P001 → M001: Weak Linkage
- **Protocol:** "Quarry trench excavation: 520 cm deep × 30 cm wide..."
- **Method:** "Pollen analysis using Lycopodium marker technique"
- **Issue:** P001 is field sampling that enables pollen analysis, but doesn't directly implement pollen analysis method
- **Severity:** Low - Conceptual link exists (sampling for pollen analysis), but "implements" may be too strong
- **Assessment:** Borderline weak - field sampling is prerequisite, not implementation
- **Recommendation:** Consider whether field sampling protocols should link to methods or to research designs instead
- **Alternative:** P001 could link to research design (RD003: sampling strategy) rather than method

### Protocols Without Method Mappings (Appropriate)

#### Preparatory Protocols (7 items)
- **P002:** Sampling intervals
- **P003:** Sample storage
- **P004-P008:** Additional cores and transects
- **P034:** Age-depth model construction calibration

**Assessment:** APPROPRIATE - These are preparatory or parameter-setting protocols that enable multiple methods

### Multiple Protocols Implementing Single Method (Appropriate)

Examples:
- **M001 (Pollen analysis) ← P009, P010:** Extraction + counting
- **M003 (Charcoal analysis) ← P015, P016, P017, P018:** Multiple quantification steps
- **M006 (Mineral magnetic analysis) ← P022-P028:** Multiple measurement types

**Assessment:** EXCELLENT - Multi-protocol mappings reflect complex multi-step methods

### Mapping Score: 97.5%
- 39 strong mappings
- 1 weak mapping (P001→M001 borderline field sampling relationship)
- 0 incorrect mappings
- Deduction: -1 point for weak mapping

## Research Designs ← Methods Mapping Assessment

### Overall: POOR (28.6%)

**Total Mappings:** 7
**Strong Mappings:** 2
**Weak Mappings:** 0
**Incorrect Mappings:** 0
**Missing Mappings:** SIGNIFICANT ISSUE

### Current Mappings

#### RD001: Multi-proxy palaeoenvironmental approach
- **supported_by_methods:** [] (EMPTY)
- **Expected:** M001 (Pollen), M002 (NPP), M003 (Charcoal), M005 (Magnetic susceptibility)
- **Issue:** Multi-proxy design has NO method mappings despite being core integration design
- **Severity:** CRITICAL

#### RD002: Regional comparative analysis
- **supported_by_methods:** [] (EMPTY)
- **Expected:** M014 (DCA), M015 (Cluster analysis), M017 (Comparative analysis)
- **Issue:** Comparative design has NO method mappings
- **Severity:** CRITICAL

#### RD003: High-resolution Quaternary chronology
- **supported_by_methods:** [M012, M013]
- **Mapping:** Age-depth modelling + Radiocarbon dating
- **Assessment:** STRONG - Appropriate methods support chronology design

#### RD004: Large-site pollen source-area considerations
- **supported_by_methods:** [] (EMPTY)
- **Expected:** M001 (Pollen analysis) or theoretical framework
- **Issue:** Design rationale has no method implementation
- **Severity:** MODERATE (this is more theoretical consideration than implemented design)

#### RD005: Integration of archaeological and palaeoenvironmental data
- **supported_by_methods:** [] (EMPTY)
- **Expected:** M001 (Pollen), M003 (Charcoal), M018 (Archaeological data integration)
- **Issue:** Integration design has NO method mappings
- **Severity:** CRITICAL

#### RD006: Magnetic susceptibility as environmental proxy
- **supported_by_methods:** [M005]
- **Mapping:** Magnetic susceptibility
- **Assessment:** STRONG - Appropriate method supports proxy design

#### RD007: Dual magnetic frequency analysis
- **supported_by_methods:** [] (EMPTY)
- **Expected:** M005 (Magnetic susceptibility - dual frequency)
- **Issue:** Specific design for dual-frequency approach has no method mapping
- **Severity:** MODERATE

#### RD008: Multi-location coring strategy
- **supported_by_methods:** [] (EMPTY)
- **Expected:** M007 (Field sampling) or spatial methods
- **Issue:** Spatial design has no method implementation
- **Severity:** MODERATE

#### RD009: Statistical validation framework
- **supported_by_methods:** [] (EMPTY)
- **Expected:** M014 (DCA), M015 (Cluster), M016 (Indicator species)
- **Issue:** Validation design has NO method mappings
- **Severity:** CRITICAL

### Critical Missing Mappings

The majority of research designs (7 out of 9) have EMPTY `supported_by_methods` arrays. This represents a systematic mapping failure in the RDMAP hierarchy.

#### Expected vs. Actual

| Design | Expected Methods | Actual | Missing |
|--------|-----------------|--------|---------|
| RD001 | M001, M002, M003, M005 | 0 | 4 |
| RD002 | M014, M015, M017 | 0 | 3 |
| RD003 | M012, M013 | 2 | 0 ✓ |
| RD004 | M001 or none | 0 | 0-1 |
| RD005 | M001, M003, M018 | 0 | 3 |
| RD006 | M005 | 1 | 0 ✓ |
| RD007 | M005 | 0 | 1 |
| RD008 | M007 or field methods | 0 | 1 |
| RD009 | M014, M015, M016 | 0 | 3 |
| **TOTAL** | **~16-20** | **2** | **14-18** |

### Mapping Score: 28.6%
- Only 2 of 7 expected design→method relationships present
- Critical systematic gap in RDMAP hierarchy
- Deduction: -71.4 points (massive structural failure)

### Severity Assessment
This is the MOST SIGNIFICANT issue identified across all three passes. The RDMAP hierarchy is broken at the Design-Method level. While methods and protocols are well-extracted and accurately mapped to each other, they are almost entirely disconnected from research designs.

### Recommendation
URGENT: Populate `supported_by_methods` arrays in research designs to establish proper RDMAP hierarchy. This should be straightforward as the methods exist and are well-extracted - only the linkages are missing.

## Summary Statistics

| Relationship Type | Total | Strong | Weak | Incorrect | Missing | Score % |
|-------------------|-------|--------|------|-----------|---------|---------|
| Evidence → Claims | 98 | 96 | 2 | 0 | 1* | 98.0% |
| Protocols → Methods | 40 | 39 | 1 | 0 | 0 | 97.5% |
| Designs ← Methods | 7 | 2 | 0 | 0 | ~15** | 28.6% |
| **TOTAL** | **145** | **137** | **3** | **0** | **~16** | **94.5%*** |

*C063 has no evidence support (duplicate issue)
**Estimated 15 missing design→method relationships
***Weighted by relationship count; heavily impacted by design-method gap

## Pass C Overall Grade: B (94.5% overall, but D for RDMAP hierarchy)

### Key Findings

1. **Evidence-Claims mapping excellent:** 98% with only structural issues from duplicate claims
2. **Protocol-Method mapping excellent:** 97.5% with only one borderline weak link
3. **CRITICAL FAILURE: Design-Method mapping incomplete:** Only 28.6% of expected relationships present
4. **No incorrect mappings:** All existing mappings are conceptually appropriate
5. **Structural issues, not conceptual:** Missing mappings are systematic gaps, not errors

### Mapping Patterns

#### Strengths
- Quantitative claims consistently supported by measurement evidence
- Multi-evidence support chains provide robust claim backing
- Protocol-method chains correctly represent multi-step analytical workflows
- No hallucinated or incorrect relationships

#### Weaknesses
- RDMAP hierarchy broken at design-method level
- Most research designs have empty `supported_by_methods` arrays
- Multi-proxy integration design (RD001) disconnected from proxy methods
- Statistical validation design (RD009) disconnected from statistical methods

### Impact on Usability

- **Transparency assessment:** Partially compromised - cannot trace from design through method to protocol
- **Replicability assessment:** Methods and protocols traceable, but strategic design rationale disconnected
- **Credibility assessment:** Evidence-claims chain intact, but RDMAP chain broken
- **Research design evaluation:** SEVERELY compromised - cannot assess design implementation

### Overall Assessment

The extraction shows excellent work on evidence-claims relationships and good protocol-method linkages, but CRITICAL systematic failure in establishing design-method relationships. This represents incomplete implementation of the RDMAP framework. The issue is straightforward to fix (methods exist, just need linking), but severely impacts the utility of research design extraction for evaluating study design quality and coherence.

### Priority Correction

**HIGHEST PRIORITY:** Populate `supported_by_methods` arrays in all 9 research designs. Recommend adding approximately 15-18 method relationships to complete RDMAP hierarchy.
