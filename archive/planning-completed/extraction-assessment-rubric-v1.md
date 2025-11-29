# Extraction Assessment Rubric v1.0 - Accuracy & Granularity

**Date:** 2025-10-31
**Status:** Draft - Ready for Pilot Testing
**Scope:** Accuracy and Granularity assessment only (Completeness via multi-run comparison - see deferred tasks)
**Use Case:** Assess quality of completed extractions from research-assessor skill

---

## Overview

### Purpose

This rubric enables systematic assessment of extraction quality along two dimensions:
1. **Accuracy:** Are extracted items correct, properly interpreted, and free from hallucinations?
2. **Granularity:** Are items appropriately atomic and consistently detailed?

**Out of scope:** Completeness assessment (handled separately via multi-run comparison studies)

### Required Inputs

- Source paper (PDF or processed markdown)
- extraction.json output file
- Schema definitions (from extraction-system/schema/)
- This rubric

### Assessment Workflow

**Quick Assessment (30-45 min):**
- Accuracy check on 20 random items
- Granularity check on 20 random items
- Mapping accuracy spot-check on 10 pairs

**Medium Assessment (2-3 hours):**
- Accuracy check on 50 items (stratified by type)
- Granularity check on 50 items
- Full mapping verification for one section

**Deep Assessment (4-6 hours):**
- Accuracy check on all items (or representative sample if >150 items)
- Granularity check on all items
- Full mapping verification
- Inter-item consistency analysis

---

## Part 1: Category Definitions with Edge Cases

### 1.1 Claims

**Core Definition:**
An interpretation, conclusion, or assertion put forward by the paper's authors about their findings, methods, or theory.

**Include:**
- Interpretations of empirical results
- Methodological assertions and justifications
- Theoretical positions and arguments
- Empirical generalizations and patterns
- Comparative statements about findings
- Causal or correlational statements

**Exclude:**
- Background literature claims (unless actively evaluated/tested)
- Pure descriptions without interpretation
- Research questions or hypotheses (unless asserted as findings)
- Methodological descriptions (those are methods/protocols)
- Simple result statements without interpretation (those are evidence)

**Edge Cases:**

| Statement | Classification | Reasoning |
|-----------|---------------|-----------|
| "Smith (2015) argues X" | NOT a claim (usually) | Unless paper is testing/supporting/refuting Smith's argument |
| "We used method X because Y" | Claim (the "because Y" part) | The justification is a methodological claim |
| "Table 1 shows increased values over time" | Claim | Interpretation of pattern, not just data reporting |
| "Values increased from 10 to 15" | Evidence | Description of data without interpretation |
| "The increase suggests climate change" | Claim | Interpretation/conclusion |
| "We hypothesize that X causes Y" | NOT a claim | Hypothesis, not asserted finding (unless in Discussion restating as supported) |
| "Our results support the hypothesis that X causes Y" | Claim | Assertion based on findings |

**Examples from Corpus:**

**Good claim extraction:**
- "The genetic data indicate admixture between farming and pastoralist populations by 4500 BCE"
- Interpretation of genetic evidence, author's conclusion

**Miscategorized as claim (should be evidence):**
- "23 radiocarbon dates were obtained ranging from 4800-4200 BCE"
- Pure data description, no interpretation

**Miscategorized as claim (should be method):**
- "We used Bayesian chronological modelling to refine the dates"
- Methodological description, not assertion about findings

---

### 1.2 Evidence

**Core Definition:**
Data, observations, measurements, or results reported by the paper's authors that support claims.

**Include:**
- Quantitative data and measurements
- Qualitative observations
- Statistical results
- Visual/material evidence descriptions
- Comparative data
- Negative results (absence of expected findings)

**Exclude:**
- Interpretations of data (those are claims)
- Background/literature data (unless used as comparative evidence)
- Methodological procedures (those are methods/protocols)
- Data about methods (e.g., "95% of samples amplified") unless used as evidence for a claim

**Edge Cases:**

| Statement | Classification | Reasoning |
|-----------|---------------|-----------|
| "Pollen assemblages show 60% arboreal taxa" | Evidence | Quantitative observation/measurement |
| "This indicates woodland environment" | Claim | Interpretation of the pollen data |
| "Sample amplification success was 85%" | Evidence (conditional) | Evidence IF used to support claim about preservation; otherwise method QC data |
| "We obtained 47 dates" | Evidence (count) | Quantitative result |
| "Dating precision averaged ±30 years" | Evidence (if supporting quality claim) OR Method (if describing process) | Context-dependent |
| "No artifacts were found in Layer 3" | Evidence | Negative result is still evidence |

**Examples from Corpus:**

**Good evidence extraction:**
- "qpAdm analysis yielded admixture coefficient of 0.23 (SE=0.04)"
- Quantitative result from analysis

**Miscategorized as evidence (should be claim):**
- "The admixture coefficient indicates gene flow occurred"
- Interpretation of the coefficient, not the coefficient itself

---

### 1.3 Methods

**Core Definition:**
Analytical techniques, procedures, or approaches used to generate or analyse evidence.

**Include:**
- Analytical techniques (radiocarbon dating, DNA sequencing, pollen analysis)
- Statistical methods (Bayesian modelling, PCA, regression)
- Field methods (excavation, survey, sampling)
- Laboratory procedures (at method level, not detailed protocol)
- Software/tools used for analysis
- Comparative/interpretive frameworks

**Exclude:**
- Detailed procedural steps (those are protocols - sub-components of methods)
- Equipment specifications alone (unless that defines the method)
- Citations to methods without usage (background only)

**Edge Cases:**

| Statement | Classification | Reasoning |
|-----------|---------------|-----------|
| "We used radiocarbon dating" | Method | High-level analytical technique |
| "Samples were pretreated with acid-alkali-acid" | Protocol | Detailed procedural step within dating method |
| "AMS dating was performed at Lab X using Model Y accelerator" | Method + Protocol OR just Protocol | Depends on granularity - see Part 4 |
| "We followed Smith (2015)" | Method (weak) | If that's all the detail provided, extract as method with note |
| "Pollen was counted to minimum 300 grains" | Protocol | Specific procedural parameter |

**Examples from Corpus:**

**Good method extraction:**
- "Genetic data analysed using qpAdm (Haak et al. 2015)"
- Clear analytical method with citation

**Over-granular (should be protocol or merged):**
- Extracting "qpAdm analysis", "ADMIXTOOLS implementation", and "reference population selection" as separate methods when they're all part of one analytical workflow

---

### 1.4 Protocols

**Core Definition:**
Specific procedural steps, parameters, or implementation details that operationalize a method.

**Include:**
- Sample preparation procedures
- Measurement parameters (counts, thresholds, replicates)
- Quality control steps
- Specific software parameters/settings
- Calibration procedures
- Detailed procedural steps

**Exclude:**
- High-level method names (those are methods)
- Results of protocol application (those are evidence)
- Justifications for protocol choices (those are claims)

**Edge Cases:**

| Statement | Classification | Reasoning |
|-----------|---------------|-----------|
| "Samples calibrated using IntCal20" | Protocol | Specific calibration procedure/dataset |
| "We used Bayesian chronological modelling" | Method | High-level technique |
| "Model run with 10,000 iterations, 1000 burn-in" | Protocol | Specific implementation parameters |
| "Poor preservation required extended DNA extraction times" | Claim (about preservation) + potentially Protocol (if details given) | Context-dependent |

---

### 1.5 Research Designs

**Core Definition:**
Overarching investigative strategies or frameworks that structure how the research was conducted.

**Include:**
- Study design types (comparative, longitudinal, case study, experimental)
- Sampling strategies (spatial, temporal, targeted vs systematic)
- Data integration approaches (multi-proxy, triangulation)
- Analytical frameworks (hypothesis testing, exploratory, Bayesian inference)
- Quality assurance frameworks

**Exclude:**
- Individual methods (those belong in Methods)
- Specific claims about design choices (those are claims)
- Procedural details (those are protocols)

**Edge Cases:**

| Statement | Classification | Reasoning |
|-----------|---------------|-----------|
| "Multi-proxy palaeoenvironmental reconstruction" | Research Design | Overarching integrative framework |
| "Pollen analysis combined with stable isotopes" | Could be Research Design OR two Methods | Depends if emphasizing integration (design) vs individual techniques (methods) |
| "Systematic spatial sampling every 10m" | Research Design (sampling strategy) | Structures data collection approach |
| "Samples collected every 10m" | Protocol | If just describing procedure without design rationale |

---

## Part 2: Accuracy Assessment

### 2.1 Verification Protocol

**Step 1: Locate the Quote**
1. Search for `verbatim_quote` text in source paper
2. If not found exactly, search for key phrases (light paraphrasing acceptable)
3. Verify `page` number matches quote location
4. Check `context_before` and `context_after` if provided

**Step 2: Verify Interpretation**
1. Read surrounding sentences (±2 paragraphs)
2. Does the context support the extracted interpretation?
3. Is this the author's own claim/evidence, or are they describing cited work?
4. Is the categorization appropriate for the quote's role in the paper?

**Step 3: Check Metadata**
1. Is `page` number correct?
2. Is `section_id` appropriate for where quote appears?
3. Are cross-references (`claim_id`, `evidence_id`, etc.) valid?

### 2.2 Error Categories

**HALLUCINATION (Critical Error)**
- Definition: Quote does not exist anywhere in the paper
- Example: Extraction claims "The authors state X" but X never appears in any form
- Scoring: -5 points per hallucination

**CONFABULATION (Major Error)**
- Definition: Quote exists but meaning is substantially misrepresented
- Example: Paper says "We found no evidence of X" → Extracted as "Evidence shows X occurred"
- Scoring: -3 points per confabulation

**MISATTRIBUTION (Major Error)**
- Definition: Quote exists but is from cited work, not paper's own claim/evidence/method
- Example: Paper says "Smith (2015) found X" → Extracted as paper's own evidence
- Scoring: -3 points per misattribution

**MISCATEGORIZATION (Moderate Error)**
- Definition: Item is accurately extracted but in wrong category
- Example: Claim extracted as evidence, or method extracted as protocol
- Scoring: -1 point per miscategorization (still correct content, wrong bucket)

**PAGE ERROR (Minor Error)**
- Definition: Quote exists with correct interpretation but wrong page number
- Example: Quote is on page 15 but extraction says page 12
- Scoring: -0.5 points per page error

**CONTEXT ERROR (Moderate Error)**
- Definition: Quote exists but important contextualizing information is omitted, changing meaning
- Example: Paper says "In the southern region, unlike the north, we found X" → Extracted as general claim without regional qualifier
- Scoring: -2 points per context error

### 2.3 Accuracy Scoring

**Formula:**
```
Accuracy Score = (Verified Correct Items - Error Penalties) / Total Items Assessed × 100%

Where:
Verified Correct = Items with no errors
Error Penalties = (Hallucinations × 5) + (Confabulations × 3) + (Misattributions × 3)
                  + (Miscategorizations × 1) + (Page Errors × 0.5) + (Context Errors × 2)
```

**Interpretation:**
- **95-100%:** Excellent accuracy, minimal corrections needed
- **85-94%:** Good accuracy, some minor errors to address
- **75-84%:** Acceptable accuracy, systematic errors should be investigated
- **65-74%:** Poor accuracy, significant problems with extraction process
- **<65%:** Unacceptable accuracy, extraction requires major revision

**Stratified Sampling for Efficiency:**
If extraction has >100 items, sample by type:
- 30% of claims
- 30% of evidence items
- 30% of methods
- 30% of protocols
- 100% of research designs (usually few items)

Random selection within each category.

---

## Part 3: Granularity Assessment

### 3.1 Granularity Principles

**Atomic Principle:** Each extracted item should represent ONE distinct thing
- One claim, one piece of evidence, one method, one protocol, one design
- Compound statements should be split if parts can be independently assessed
- BUT: Don't over-split naturally coupled information

**Consistency Principle:** Similar statements should be extracted at similar levels of detail
- If "qpAdm (Haak 2015)" is one method, then "pollen analysis (Faegri & Iversen 1989)" should also be one method
- If you split radiocarbon dating into "sample preparation" + "AMS measurement" + "calibration" protocols, do the same for other dating methods

**Functional Principle:** Granularity should serve assessment goals
- Too coarse: Can't assess credibility of individual components
- Too fine: Creates noise, obscures patterns, makes assessment tedious

### 3.2 Over-Splitting (Too Fine)

**Red Flags:**
- Adjacent items that are always used together
- Components of a single procedure extracted separately without clear benefit
- Splitting purely for word count rather than conceptual distinction

**Examples:**

**Claims - Over-Split:**
```
❌ WRONG:
C001: "Genetic diversity was high"
C002: "This indicates large population size"

✓ BETTER:
C001: "Genetic diversity was high, indicating large population size"
```
*Reasoning:* These form one interpretive statement. The second is justification for the first, not an independent claim.

**But compare:**
```
✓ CORRECT to keep separate:
C001: "Genetic diversity was high, indicating large population size"
C002: "Large population size likely resulted from immigration rather than natural growth"
```
*Reasoning:* Second claim adds a distinct causal interpretation beyond the first.

**Evidence - Over-Split:**
```
❌ WRONG:
E001: "23 radiocarbon dates were obtained"
E002: "Dates ranged from 4800-4200 BCE"
E003: "Mean date was 4450 BCE"

✓ BETTER:
E001: "23 radiocarbon dates ranged from 4800-4200 BCE (mean 4450 BCE)"
```
*Reasoning:* These are all facets of one dataset description.

**Methods - Over-Split:**
```
❌ WRONG:
M001: "We used qpAdm"
M002: "qpAdm implemented in ADMIXTOOLS"
M003: "ADMIXTOOLS version 7.0"

✓ BETTER:
M001: "Genetic admixture analysed using qpAdm (Haak et al. 2015) implemented in ADMIXTOOLS v7.0"
```
*Reasoning:* These are all describing one analytical method.

**But compare:**
```
✓ CORRECT to keep separate:
M001: "Genetic admixture analysed using qpAdm (Haak et al. 2015)"
M002: "Population structure assessed using ADMIXTURE (Alexander et al. 2009)"
```
*Reasoning:* Two distinct analytical methods, even if from same software suite.

### 3.3 Under-Splitting (Too Coarse)

**Red Flags:**
- Multiple distinct ideas compressed into one item
- "And" statements that join separable components
- Items that mix categories (claim + evidence in one item)

**Examples:**

**Claims - Under-Split:**
```
❌ WRONG:
C001: "Genetic diversity was high indicating large population size, which likely resulted from immigration based on isotope data showing non-local origins for 40% of individuals"

✓ BETTER:
C001: "Genetic diversity was high, indicating large population size"
C002: "Large population size likely resulted from immigration"
C003: "40% of individuals show non-local isotopic signatures"
```
*Reasoning:* Three distinct interpretive statements that can be independently assessed.

**Evidence - Under-Split:**
```
❌ WRONG:
E001: "Radiocarbon dating, stable isotope analysis, and DNA sequencing were performed, yielding 23 dates (4800-4200 BCE), δ13C values of -21±2‰, and 15 genetic sequences with 89% endogenous content"

✓ BETTER:
E001: "23 radiocarbon dates ranged from 4800-4200 BCE"
E002: "Stable isotope analysis yielded δ13C values of -21±2‰"
E003: "DNA sequencing produced 15 genetic sequences with 89% endogenous content"
```
*Reasoning:* Three distinct datasets from different methods, each assessable separately.

**Methods - Under-Split:**
```
❌ WRONG:
M001: "We used radiocarbon dating and stable isotope analysis"

✓ BETTER:
M001: "Radiocarbon dating"
M002: "Stable isotope analysis"
```
*Reasoning:* Two distinct analytical methods that should be separately extractable.

**But compare:**
```
✓ ACCEPTABLE to keep merged:
M001: "Multi-proxy palaeoenvironmental reconstruction combining pollen, charcoal, and phytolith analysis"
```
*Reasoning:* If paper presents this as integrated approach (research design level), keep merged. If paper describes each proxy separately with different protocols, split.

### 3.4 Granularity Consistency Check

**Procedure:**
1. Select 10 items of same type (e.g., 10 claims)
2. Compare level of detail across items
3. Identify outliers (much more or less detailed than others)
4. Assess if variation is justified (complex vs simple claims) or inconsistent

**Example Consistency Issue:**

```
C001: "Admixture occurred between farming and pastoralist populations by 4500 BCE in the Carpathian Basin"
[Very detailed: what, when, where]

C015: "Climate changed"
[Too vague: what kind of change, when, where?]

C032: "Economic strategies diversified"
[Medium detail: what happened, but not when/where specified]
```

**Assessment:** Inconsistent granularity. Either C001 is too detailed, or C015/C032 are too vague. Check paper context:
- If paper provides detail for all three, extract all at high detail
- If paper only provides detail for C001, then variation is appropriate

### 3.5 Granularity Scoring

**Formula:**
```
Granularity Score = (Items at Appropriate Level) / (Total Items Assessed) × 100%

Where:
Items at Appropriate Level = Total - Over-Split Items - Under-Split Items - Inconsistent Items
```

**Calibration Guidance:**

For each item, assess:
- **Appropriate (1 point):** Item is atomic, functionally useful, consistent with similar items
- **Over-Split (-0.5 points):** Should be merged with adjacent item(s)
- **Under-Split (-0.5 points):** Should be split into 2+ items
- **Inconsistent (-0.25 points):** Granularity doesn't match similar items (too detailed or too vague)

**Interpretation:**
- **90-100%:** Excellent consistency, appropriate granularity throughout
- **80-89%:** Good consistency, minor adjustments needed
- **70-79%:** Acceptable consistency, some systematic issues
- **60-69%:** Poor consistency, significant variation in granularity
- **<60%:** Unacceptable consistency, major revision needed

---

## Part 4: Mapping Accuracy Assessment

**Scope:** Assess accuracy of existing mappings only (NOT completeness of mappings - that requires re-extraction)

### 4.1 Mapping Types

**Claim → Evidence Links**
- Does the evidence actually support the claim as stated?
- Is the link semantically valid?

**Protocol → Method Links**
- Is the protocol actually a component/implementation of the method?

**Method → Research Design Links**
- Is the method part of the research design framework?

**Evidence → Method Links**
- Was the evidence generated/analysed using this method?

### 4.2 Correct vs Incorrect Mappings

**Correct Mapping Example:**
```
C001: "Population increased after 2000 BCE"
→ linked to →
E005: "Settlement count increased from 12 (2500-2000 BCE) to 47 (2000-1500 BCE)"
```
*Assessment:* ✓ Evidence directly supports claim

**Incorrect Mapping Example:**
```
C001: "Climate was warm during the Bronze Age"
→ linked to →
E008: "Pottery styles changed from red to black ware"
```
*Assessment:* ✗ No logical connection between pottery styles and climate

**Missing Context (Questionable Mapping):**
```
C015: "Migration occurred from the steppe"
→ linked to →
E023: "Genetic admixture coefficient 0.23"
```
*Assessment:* ? Coefficient alone doesn't indicate direction. Need additional evidence about source populations. Mark as "weak mapping" if inference chain is unclear.

### 4.3 Mapping Verification Protocol

**For each mapped pair:**

1. **Read both items** (claim + evidence, or protocol + method)
2. **Check logical connection:**
   - Does B actually support/implement/relate to A?
   - Is the connection explicit in the paper or inferred?
   - Is the inference chain clear?
3. **Categorize:**
   - **Strong mapping:** Direct, explicit connection in paper
   - **Weak mapping:** Connection requires inference, may be valid but uncertain
   - **Incorrect mapping:** No logical connection, or misinterprets relationship
4. **Note errors:**
   - If incorrect, explain why
   - If weak, note what would strengthen it

### 4.4 Mapping Accuracy Scoring

**Formula:**
```
Mapping Accuracy = (Strong Mappings + 0.5 × Weak Mappings) / (Total Mappings Assessed) × 100%
```

**Interpretation:**
- **90-100%:** Excellent mapping accuracy
- **80-89%:** Good mapping accuracy, some weak links
- **70-79%:** Acceptable, significant weak or questionable mappings
- **60-69%:** Poor, many incorrect or weak mappings
- **<60%:** Unacceptable mapping quality

---

## Part 5: Overall Scoring Framework

### 5.1 Component Weights

```
Overall Quality Score = (Accuracy × 0.50) + (Granularity × 0.30) + (Mapping Accuracy × 0.20)
```

**Rationale:**
- **Accuracy (50%):** Most critical - hallucinations/confabulations undermine entire extraction
- **Granularity (30%):** Important for usability and assessment, but less critical than correctness
- **Mapping (20%):** Useful but secondary - can be fixed post-hoc more easily than accuracy errors

### 5.2 Grade Interpretation

**A Grade (90-100%):**
- Minimal corrections needed
- Suitable for assessment framework use with confidence
- May have minor granularity inconsistencies or weak mappings

**B Grade (80-89%):**
- Good quality, some corrections needed
- Usable for assessment with awareness of limitations
- Likely has some miscategorizations or granularity issues

**C Grade (70-79%):**
- Acceptable quality, systematic corrections needed
- Usable for assessment but requires significant review
- May have accuracy concerns in specific sections or item types

**D Grade (60-69%):**
- Poor quality, major revision needed
- Not suitable for assessment without substantial corrections
- Likely has hallucinations, confabulations, or systematic miscategorizations

**F Grade (<60%):**
- Unacceptable quality
- Re-extraction recommended rather than correction
- Fundamental problems with extraction process

### 5.3 Reporting Template

```markdown
## Extraction Assessment Report

**Paper:** [Title, Authors, Year]
**Extraction File:** [path/to/extraction.json]
**Assessor:** [Human or LLM model]
**Assessment Date:** [YYYY-MM-DD]
**Assessment Depth:** [Quick / Medium / Deep]

---

### Summary Scores

| Dimension | Score | Grade | Status |
|-----------|-------|-------|--------|
| Accuracy | 92% | A | Excellent |
| Granularity | 85% | B | Good |
| Mapping Accuracy | 88% | B | Good |
| **Overall** | **89%** | **B** | **Good** |

---

### Accuracy Assessment

**Items Assessed:** 50 / 247 total (stratified sample)
- Claims: 15 assessed
- Evidence: 20 assessed
- Methods: 10 assessed
- Protocols: 5 assessed

**Errors Found:**
- Hallucinations: 0
- Confabulations: 1 (C023 - misinterpreted context)
- Misattributions: 2 (E015, E027 - cited work not paper's own data)
- Miscategorizations: 3 (see details below)
- Page Errors: 2 (minor)

**Notable Issues:**
- C023: States "population declined" but paper says "no evidence of decline" - confabulation
- E015, E027: Attributed to paper but actually from Smith (2015) comparison
- M003, M007, P012: Miscategorized (methods as protocols, protocol as method)

---

### Granularity Assessment

**Items Assessed:** 50 (same sample as accuracy)

**Issues Found:**
- Over-split items: 3 (C001+C002 should merge, E034+E035 should merge, M008+M009 should merge)
- Under-split items: 2 (C015 contains 3 distinct claims, E045 mixes two datasets)
- Inconsistent items: 5 (varying detail levels without clear justification)

**Patterns:**
- Generally consistent granularity for evidence items
- Claims show some inconsistency (high detail for genetic claims, low detail for environmental claims)
- Methods appropriately atomic

---

### Mapping Assessment

**Mappings Assessed:** 25 claim→evidence links

**Results:**
- Strong mappings: 20 (80%)
- Weak mappings: 3 (12%) - C008→E019, C015→E032, C024→E051
- Incorrect mappings: 2 (8%) - C012→E028 (no logical connection), C019→E041 (misinterpreted relationship)

**Notable Issues:**
- C012→E028: Claim about climate linked to pottery evidence with no explanation
- C019→E041: Claim about migration direction but evidence is non-directional admixture coefficient

---

### Recommendations

1. **Priority:** Fix confabulation in C023 and misattributions in E015, E027
2. **Granularity:** Merge over-split items, split C015 and E045
3. **Mappings:** Remove or justify C012→E028 and C019→E041 links
4. **Quality:** Overall B-grade quality suitable for assessment use with noted corrections

---

### Assessor Notes

[Any additional observations, patterns, concerns, or praise]
```

---

## Part 6: Practical Assessment Workflows

### 6.1 Quick Assessment (30-45 minutes)

**Goal:** Rapid quality check, catch major problems

**Procedure:**
1. Random sample 20 items (mixed types)
2. Verify accuracy for all 20
3. Assess granularity for all 20
4. Check 10 random mappings
5. Calculate scores
6. Report major issues only

**When to Use:**
- Initial quality check on new extraction
- Triage for deeper assessment
- Periodic spot-checks across multiple extractions

**Limitations:**
- May miss systematic errors in specific sections
- Small sample size limits confidence
- Not suitable for formal quality certification

---

### 6.2 Medium Assessment (2-3 hours)

**Goal:** Thorough assessment with reasonable effort

**Procedure:**
1. **Stratified sample 50 items:**
   - 15 claims (random across all claims)
   - 20 evidence (random across all evidence)
   - 10 methods (random)
   - 5 protocols (random)
   - All research designs (usually <10)

2. **Accuracy assessment:**
   - Full verification protocol for all 50 items
   - Categorize errors
   - Note patterns (e.g., confabulations concentrated in Discussion section?)

3. **Granularity assessment:**
   - Assess all 50 for appropriate atomicity
   - Check 10 similar items for consistency
   - Note systematic issues

4. **Mapping assessment:**
   - Select one complete section
   - Verify all mappings in that section
   - Assess strong/weak/incorrect

5. **Score and report**

**When to Use:**
- Standard assessment for pilot extractions
- Quality certification for corpus inclusion
- Diagnosing systematic extraction issues

---

### 6.3 Deep Assessment (4-6 hours)

**Goal:** Comprehensive quality evaluation

**Procedure:**
1. **Full or large-sample accuracy check:**
   - If <150 items: assess all
   - If >150 items: stratified sample of 100 items

2. **Full granularity assessment:**
   - All items assessed for atomicity
   - Systematic consistency checks across item types
   - Document patterns and outliers

3. **Full mapping verification:**
   - All mappings assessed
   - Cross-check for logical coherence
   - Identify systematic mapping issues

4. **Inter-item analysis:**
   - Check for duplicate items (same claim extracted twice)
   - Check for contradictory items
   - Assess coverage balance (are all sections equally detailed?)

5. **Comprehensive report with recommendations**

**When to Use:**
- Gold standard extraction for method validation
- Problematic extractions requiring diagnosis
- Training dataset quality assurance
- Pre-publication quality certification

---

## Part 7: LLM Assessor Guidance

### 7.1 Prompting Strategy for LLM Assessment

**Required Inputs:**
1. Source paper (full text)
2. extraction.json file contents
3. Schema definitions
4. Relevant sections of this rubric

**Suggested Prompt Structure:**

```
You are assessing the quality of an automated extraction from a research paper.

# Your Task
Assess the accuracy and granularity of extracted items according to the provided rubric.

# Inputs Provided
1. Source paper: [paper text or path]
2. Extraction output: [extraction.json contents]
3. Assessment rubric: [relevant rubric sections]

# Assessment Procedure

## Step 1: Accuracy Assessment
For each item in the extraction (or specified sample):
1. Locate the verbatim_quote in the source paper
2. Verify the page number is correct
3. Read the surrounding context
4. Categorize any errors according to the rubric:
   - Hallucination (quote doesn't exist)
   - Confabulation (quote exists but misrepresented)
   - Misattribution (from cited work, not paper's claim)
   - Miscategorization (wrong category)
   - Page error (wrong page number)
   - Context error (missing important context)

## Step 2: Granularity Assessment
For each item:
1. Determine if item is appropriately atomic (one thing)
2. Identify over-split items (should be merged)
3. Identify under-split items (should be split)
4. Check consistency with similar items

## Step 3: Mapping Assessment
For specified mappings:
1. Read both linked items
2. Assess if link is logical and supported by paper
3. Categorize as Strong / Weak / Incorrect

## Output Format
Provide a structured assessment report following the template in Section 5.3 of the rubric.

# Examples
[Provide 2-3 worked examples of accuracy and granularity assessment]

# Begin Assessment
[Specify which items to assess, or "assess random sample of 20 items"]
```

### 7.2 LLM Reliability Considerations

**Strengths of LLM assessment:**
- Fast verification of quote existence and page numbers
- Good at identifying obvious miscategorizations
- Can process large samples efficiently
- Consistent application of rubric criteria

**Weaknesses of LLM assessment:**
- May struggle with subtle context errors
- Can miss edge cases in categorization
- May be overly literal in quote matching (miss light paraphrasing)
- Less reliable for granularity consistency judgments

**Recommended approach:**
- **Use LLM for:** Quick and medium assessments, accuracy verification, bulk processing
- **Use human for:** Deep assessments, edge case adjudication, granularity consistency, final quality certification

**Validation protocol:**
- Run LLM assessment on sample
- Human spot-check 20% of LLM assessments
- If agreement >90%, trust LLM
- If agreement <90%, investigate LLM systematic errors

### 7.3 Multi-LLM Comparison

**For critical extractions, consider cross-validation:**
1. Run same assessment with 2-3 different LLMs (e.g., Claude 3.7 Sonnet, GPT-4.5, Gemini 2.5 Pro)
2. Compare assessments
3. Items flagged by multiple LLMs → high confidence errors
4. Items flagged by one LLM only → human review needed

---

## Part 8: Using Assessment Results

### 8.1 Interpreting Score Patterns

**High Accuracy, Low Granularity:**
- Extraction is correct but inconsistently detailed
- Fix: Review extraction prompts for granularity guidance
- May indicate over-splitting or under-splitting in specific sections

**Low Accuracy, High Granularity:**
- Extraction is consistently detailed but contains errors
- Fix: Investigate hallucination/confabulation sources
- May indicate prompt pushing for over-extraction, or context window issues

**Both Low:**
- Systematic extraction failure
- Consider re-extraction with revised prompts or different approach

**Both High:**
- Excellent extraction quality
- Use as exemplar for future extractions

### 8.2 Section-Level Patterns

If assessment reveals section-specific issues:
- **Methods over-extracted, Results under-extracted:** Confirms "Methods bias" concern
- **Discussion section confabulations:** May indicate interpretive over-reach
- **Introduction miscategorizations:** Background lit being extracted as paper's claims

### 8.3 Feeding Back to Extraction Process

Assessment results inform:
1. **Prompt refinement:** Address systematic errors
2. **Skill tuning:** Adjust research-assessor skill guidance
3. **Workflow validation:** Confirm multi-pass approach is working
4. **Corpus quality standards:** Set thresholds for inclusion

---

## Appendices

### Appendix A: Edge Case Decision Tree

```
Is this a Claim or Evidence?
├─ Does it interpret/conclude something? → Claim
├─ Does it report data/observation? → Evidence
└─ Does it do both? → Split into Claim + Evidence

Is this a Method or Protocol?
├─ High-level technique/approach? → Method
├─ Specific procedural step? → Protocol
└─ Unclear? → Check: could you assess credibility of the technique (Method) separately from how it was implemented (Protocol)?

Is this too coarse or too fine?
├─ Can components be independently assessed? → Should be split
├─ Are components always used together? → Should be merged
└─ Unclear? → Check consistency with similar items
```

### Appendix B: Common Extraction Errors by Type

**Claims:**
- Most common error: Extracting background lit as claims
- Second most common: Confabulating interpretations not stated by authors
- Watch for: Hypotheses extracted as findings

**Evidence:**
- Most common error: Extracting interpretations as evidence
- Second most common: Over-splitting related measurements
- Watch for: Method QC data extracted as evidence when not used to support claims

**Methods:**
- Most common error: Extracting protocols as methods (too granular)
- Second most common: Under-splitting method combinations
- Watch for: Citations to methods without actual usage

**Protocols:**
- Most common error: Extracting methods as protocols (not detailed enough)
- Second most common: Over-splitting sequential steps
- Watch for: Parameters vs procedures (both are protocols but different kinds)

---

## Changelog

**v1.0 (2025-10-31):**
- Initial draft
- Accuracy and Granularity assessment only
- Completeness deferred to multi-run comparison protocol
- Ready for pilot testing on 10-paper corpus
