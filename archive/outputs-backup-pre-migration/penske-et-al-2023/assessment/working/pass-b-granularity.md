# Pass B: Granularity Assessment - Penske et al. (2023)

**Assessment Date:** 2025-11-02
**Assessor:** Claude Sonnet 4.5
**Items Assessed:** 231 (85 evidence, 84 claims, 20 methods, 35 protocols, 7 research designs)

## Assessment Methodology

Granularity assessment evaluates whether items are:
- **Appropriately scoped:** Single atomic fact/claim/method/protocol/design
- **Not over-split:** Related information kept together for functional usefulness
- **Not under-split:** Compound statements separated when needed for independent assessment
- **Consistently chunked:** Similar information has similar granularity across extraction

**Evaluation Criteria:**
1. **Atomic Principle:** Each item should capture one coherent unit
2. **Functional Usefulness:** Items should be independently assessable for replicability/transparency
3. **Consolidation Quality:** Pass 1 over-extraction appropriately consolidated in Pass 2+
4. **Internal Consistency:** Similar types of information chunked at similar granularity

## Pass B Results Summary

**Overall Granularity Score:** 98.7% (A)

**By Item Type:**

| Type | Total | Appropriate | Over-split | Under-split | Inconsistent | Score |
|------|-------|-------------|------------|-------------|--------------|-------|
| Evidence | 85 | 84 | 0 | 1 | 0 | 98.8% |
| Claims | 84 | 84 | 0 | 0 | 0 | 100.0% |
| Methods | 20 | 19 | 0 | 1 | 0 | 95.0% |
| Protocols | 35 | 34 | 0 | 1 | 0 | 97.1% |
| Research Designs | 7 | 7 | 0 | 0 | 0 | 100.0% |

**Total Issues:** 3 under-split items
**No over-splitting detected**

## Detailed Analysis by Type

### Evidence Granularity: 98.8% (A)

**Average Content Length:** 98 characters
**Content Length Range:** 32-221 characters
**Consolidated Items:** 8 (from 16 original Pass 1 items)

#### Consolidation Quality: **EXCELLENT**

All 8 consolidations appropriately reduce Pass 1 over-extraction:

**E009** - Tell sites (3→1)
- **Consolidated:** P1_E009, P1_E010, P1_E011
- **Type:** compound_finding
- **Assessment:** ✅ Appropriate - Three separate statements about tell sites (emergence, specific sites, occupation duration) combined into single coherent evidence about tell settlement pattern
- **Rationale:** All supported only C019, never independently assessed

**E019** - PIE039 genetic similarity (2→1)
- **Consolidated:** P1_E019, P1_E020
- **Type:** identical_support_pattern
- **Assessment:** ✅ Appropriate - PCA and f3 statistics both describe same individual's genetic similarity, consolidated into compound statement preserving both methods
- **Rationale:** Both support only C025, describe same finding with different statistical approaches

**E021** - SEE 1 genetic modelling (2→1)
- **Consolidated:** P1_E021, P1_E022
- **Type:** compound_finding
- **Assessment:** ✅ Appropriate - Symmetry test results and qpAdm modelling combined into single evidence statement
- **Rationale:** Compound statistical finding, functionally inseparable

**E023** - CA cluster formation (2→1)
- **Consolidated:** P1_E023, P1_E024
- **Type:** compound_finding
- **Assessment:** ✅ Appropriate - Cluster identification and geographic overlap combined
- **Rationale:** Single PCA observation with spatial interpretation

**E059** - MJ41 admixture dating (2→1)
- **Consolidated:** P1_E059, P1_E060
- **Type:** compound_finding
- **Assessment:** ✅ Appropriate - DATES estimate and curve interpretation combined
- **Rationale:** Compound admixture dating result

**E076** - Vertical stratification (2→1)
- **Consolidated:** P1_E076, P1_E077
- **Type:** compound_finding
- **Assessment:** ✅ Appropriate - Related individuals in burial combined with genetic similarity
- **Rationale:** Single burial observation with genetic confirmation

**E087** - mtDNA analysis (2→1)
- **Consolidated:** P1_E087, P1_E088
- **Type:** compound_finding
- **Assessment:** ✅ Appropriate - mtDNA capture method and haplogroup assignment combined
- **Rationale:** Methodological and results statement for same analysis

**E092** - Y-chromosome analysis (2→1)
- **Consolidated:** P1_E092, P1_E093
- **Type:** compound_finding
- **Assessment:** ✅ Appropriate - Y-SNP calling and haplogroup assignment combined
- **Rationale:** Methodological and results statement for same analysis

#### Issue E-B1: E015 - Potential Under-split
- **Severity:** Minor
- **Content:** "Tell settlements involved in proto-industrial exploitation of copper, gold and salt"
- **Issue:** Three distinct resource types (copper, gold, salt) combined
- **Analysis:** Could be split into separate evidence items for each resource type IF paper provides independent evidence for each
- **Assessment:** ⚠️ **Marginal** - Acceptable as consolidated economic pattern, but may under-split if paper discusses resources separately
- **Recommendation:** Verify against source - if resources discussed independently with separate evidence, consider splitting

### Claims Granularity: 100.0% (A+)

**Average Content Length:** 90 characters
**Content Length Range:** 40-182 characters
**Consolidated Items:** 1 (C019: P1_C019 + P1_C020)

#### Consolidation Quality: **EXCELLENT**

**C019** - Tell settlements interpretation (2→1)
- **Consolidated:** P1_C019, P1_C020
- **Type:** redundancy_elimination
- **Assessment:** ✅ Appropriate - C020 essentially restated C019 with same evidence
- **Rationale:** Pure redundancy from Pass 1 over-extraction

#### Granularity Consistency: **EXCELLENT**

Claims consistently scoped at appropriate level:
- **Background claims** (C001-C003): High-level synthesis statements (75-105 chars)
- **Genetic interpretation claims** (C025-C044): Specific population-level findings (80-120 chars)
- **Temporal claims** (C002, C003, C013): Date ranges and timing (70-95 chars)
- **Methodological claims** (C007-C009): Study design statements (80-110 chars)

No over-splitting detected. No under-splitting detected.

### Methods Granularity: 95.0% (A)

**Average Content Length:** 84 characters
**Content Length Range:** 43-154 characters
**Consolidated Items:** 0 (no consolidation metadata)

#### Issue M-B1: M002 - Potential Under-split
- **Severity:** Minor
- **Content:** "Generate genome-wide ancient DNA data from petrous bones and teeth"
- **Issue:** Two distinct sample types (petrous bones, teeth) combined in single method statement
- **Analysis:** Paper states "We processed 168 petrous bones and 129 teeth in total" - these are quantified separately
- **Protocol Level:** P003 appropriately handles both sampling procedures as compound protocol (petrous + teeth methods consolidated)
- **Assessment:** ⚠️ **Marginal** - At method level (strategic choice), consolidation is appropriate. At protocol level (execution detail), P003 handles tissue-specific procedures.
- **Recommendation:** Acceptable - RDMAP hierarchy appropriately places tissue-specific detail at protocol level, method level correctly describes overall data generation strategy

### Protocols Granularity: 97.1% (A)

**Average Content Length:** 89 characters
**Content Length Range:** 38-168 characters
**Consolidated Items:** 1 (P003: petrous + teeth sampling)

#### Consolidation Quality: **EXCELLENT**

**P003** - Tissue sampling procedures (2→1)
- **Consolidated:** P3_P003, P3_P004
- **Type:** compound_protocol
- **Assessment:** ✅ Appropriate - Petrous bone and teeth sampling procedures combined with clear differentiation preserved in content
- **Rationale:** "Two sampling procedures for different tissue types, always assessed as complete sampling protocol"

#### Issue P-B1: P008 - Potential Under-split
- **Severity:** Minor
- **Content:** "Calibrate radiocarbon dates using IntCal20 database and OxCal v.4.4.2"
- **Issue:** Two distinct elements (calibration curve database + software tool) combined
- **Analysis:** Calibration inherently requires both database and software - functionally inseparable
- **Assessment:** ⚠️ **Acceptable** - Database and software are standard paired components of calibration protocol, not independently assessable
- **Recommendation:** No action - appropriate consolidation of inseparable protocol components

### Research Designs Granularity: 100.0% (A+)

**Average Content Length:** 119 characters (designs appropriately more detailed)
**Content Length Range:** 81-183 characters
**Consolidated Items:** 1 (RD002: spatial + temporal scope)

#### Consolidation Quality: **EXCELLENT**

**RD002** - Spatiotemporal scope (2→1)
- **Consolidated:** P3_RD002, P3_RD003
- **Type:** compound_design
- **Assessment:** ✅ Excellent - Spatial and temporal scope are inseparable facets of single strategic scoping decision
- **Rationale:** "Spatial and temporal scope are inseparable facets of single scoping decision. Always assessed together"

#### Granularity Consistency: **EXCELLENT**

Design items appropriately scoped at strategic level:
- **RD001** (research_question): Overall motivating question
- **RD002** (scope_definition): Spatiotemporal boundaries as unified design choice
- **RD004** (approach_justification): Genome-wide data as strategic approach
- **RD005** (site_selection_strategy): Emblematic site focus
- **RD006** (methodological_triangulation): Multi-method analytical strategy
- **RD007** (hypothesis_testing): Pathogen screening as design element
- **RD008** (reference_framework_selection): Cornerstone population choice (implicit)

All designs capture strategic-level choices, appropriately abstracted from method-level implementation.

## Cross-Type Consistency Analysis

### Consistency Pattern 1: RDMAP Hierarchy Granularity
**Assessment:** ✅ **EXCELLENT**

Clear granularity differentiation across hierarchy:
- **Designs** (avg 119 chars): Strategic-level decisions, rationale-rich
- **Methods** (avg 84 chars): Implementation-level approaches
- **Protocols** (avg 89 chars): Execution-level procedures with technical detail

Example hierarchy:
- **RD006** (design): "Use multiple complementary genetic analysis methods to characterize ancestries"
- **M005** (method): "Principal Component Analysis (PCA) to visualize genetic structure"
- **P010** (protocol): "Project ancient samples onto PCA space using smartPCA with lsqproject:YES and shrinkmode:YES"

Granularity appropriately increases in specificity: Design → Method → Protocol

### Consistency Pattern 2: Genetic Evidence Granularity
**Assessment:** ✅ **EXCELLENT**

Genetic evidence consistently chunked at observation/statistic level:
- **PCA observations** (E023, E026, E031): Individual observation per evidence item
- **f-statistics** (E029, E032): Individual statistical test per evidence item
- **qpAdm models** (E021, E027, E030): Individual modelling result per evidence item
- **DATES estimates** (E034, E059): Individual dating estimate per evidence item

Similar information types chunked at similar granularity throughout.

### Consistency Pattern 3: Archaeological Evidence Granularity
**Assessment:** ✅ **EXCELLENT**

Archaeological evidence consistently chunked at observation/pattern level:
- **Site identifications** (E006, E008, E009): Individual site or site pattern per evidence
- **Material culture** (E007, E014, E017): Individual material culture observation per evidence
- **Temporal patterns** (E013): Individual temporal pattern per evidence

### Consistency Pattern 4: Claims Granularity
**Assessment:** ✅ **EXCELLENT**

Claims consistently scoped at interpretation/finding level:
- **Genetic interpretations** (C010, C011, C025-C044): Single population-level genetic finding per claim
- **Temporal associations** (C002, C003, C013): Single timing relationship per claim
- **Cultural interpretations** (C015, C017, C018): Single cultural assessment per claim

No arbitrary splitting of compound interpretations. No inappropriate consolidation of distinct findings.

## Consolidation Strategy Assessment

**Overall Consolidation Approach:** ✅ **CONSERVATIVE AND APPROPRIATE**

**Consolidation Statistics:**
- **Evidence:** 8/85 items consolidated (9.4%) - 16 original items → 8 consolidated
- **Claims:** 1/84 items consolidated (1.2%) - 2 original items → 1 consolidated
- **Protocols:** 1/35 items consolidated (2.9%) - 2 original items → 1 consolidated
- **Research Designs:** 1/7 items consolidated (14.3%) - 2 original items → 1 consolidated

**Consolidation Principles Applied:**
1. **Compound findings:** Related observations using different methods (E019, E021, E023)
2. **Identical support patterns:** Items never independently assessed (E009)
3. **Functionally inseparable:** Components always used together (P003, RD002)
4. **Redundancy elimination:** Pure duplication (C019)

**What Was NOT Consolidated (Appropriately):**
- Separate genetic populations even from same analysis
- Distinct archaeological sites even from same region
- Different statistical tests even on same samples
- Different interpretive claims even from same evidence

**Assessment:** Strong editorial judgment balancing atomic principle with functional usefulness.

## Notable Granularity Examples

### Excellent Granularity Examples

**E021** (genetic_modelling): "Hungary_LN_Sopot and Malak Preslavets N most symmetrically related to PIE039 (|Z| ≤ 1), combined into SEE 1 group for proximal qpAdm modelling (P = 0.41)"
- ✅ Appropriately consolidates symmetry test + qpAdm grouping + P-value
- Single compound finding, functionally inseparable
- Preserves all quantitative detail (Z ≤ 1, P = 0.41)

**P010** (pca_analysis): "Project ancient samples onto PCA space using smartPCA with lsqproject:YES and shrinkmode:YES"
- ✅ Appropriately detailed protocol with specific parameters
- Single analytical procedure
- Replicable from this description

**RD002** (scope_definition): "Focus on spatiotemporal contact zone: southeastern Europe to northwestern Black Sea region spanning critical period 7000-3300 BC"
- ✅ Appropriately consolidates spatial + temporal scope
- Single strategic design decision
- Rationale metadata explains: "Spatial and temporal scope are inseparable facets"

### Marginal Cases (All Acceptable)

**E015** (economic_activity): "Tell settlements involved in proto-industrial exploitation of copper, gold and salt"
- ⚠️ Three resources combined - marginal
- **Assessment:** Acceptable as economic pattern unless paper discusses resources independently
- Could be split if independent evidence exists for each resource

**M002** (data_generation): "Generate genome-wide ancient DNA data from petrous bones and teeth"
- ⚠️ Two tissue types combined at method level
- **Assessment:** Acceptable - tissue-specific detail appropriately delegated to protocol level (P003)
- RDMAP hierarchy appropriately places variation at protocol level

**P008** (calibration): "Calibrate radiocarbon dates using IntCal20 database and OxCal v.4.4.2"
- ⚠️ Database + software combined
- **Assessment:** Acceptable - functionally inseparable components of calibration protocol
- Cannot assess database choice independently of software implementation

## Key Findings

### Strengths
✅ **Excellent consolidation quality** - 11 consolidations, all appropriate with clear metadata
✅ **No over-splitting** - No unnecessarily fragmented information
✅ **Strong RDMAP hierarchy** - Clear granularity differentiation across Design → Method → Protocol
✅ **Internal consistency** - Similar information types chunked at similar granularity
✅ **Conservative approach** - Avoids inappropriate consolidation of distinct findings
✅ **Well-documented consolidation** - All consolidations have metadata with rationale
✅ **Functional usefulness maintained** - Items independently assessable for replicability

### Weaknesses
⚠️ **Minor potential under-splits** - 3 items marginally under-split (E015, M002, P008)
⚠️ **All marginal cases acceptable** - No clear under-splitting requiring correction

### Patterns
- **Consolidation concentrated in evidence** - Most consolidation in genetic evidence (compound statistical findings)
- **Minimal claim consolidation** - Only 1 claim consolidated (redundancy elimination)
- **Strategic design consolidation** - 1 design consolidated (spatiotemporal scope inseparability)
- **Protocol-level tissue differentiation** - Tissue-specific procedures at protocol level, consolidated at method level

## Priority Actions

### No Critical Actions Required

All granularity issues are marginal and acceptable. Items flagged for review:

**Review Item 1: E015** (Low Priority)
- **Action:** Verify against source paper - if copper, gold, salt discussed independently with separate evidence, consider splitting
- **If separate:** Split into E015a (copper), E015b (gold), E015c (salt)
- **If consolidated:** Accept current granularity (economic pattern)

**Review Item 2: M002** (No Action)
- **Decision:** Accept current granularity - tissue-specific detail appropriately at protocol level

**Review Item 3: P008** (No Action)
- **Decision:** Accept current granularity - database and software functionally inseparable

## Overall Assessment

**Grade:** **A** (Excellent)

**Summary:** Excellent granularity with strong consolidation quality and no over-splitting. Pass 1 over-extraction appropriately consolidated using clear principles and well-documented rationale. RDMAP hierarchy shows appropriate granularity differentiation. Internal consistency excellent across item types. Only 3 marginal under-split cases, all functionally acceptable.

**Fitness for Use:** Granularity appropriate for transparency and replicability assessment. Items independently assessable while avoiding unnecessary fragmentation. Strong editorial judgment throughout.
