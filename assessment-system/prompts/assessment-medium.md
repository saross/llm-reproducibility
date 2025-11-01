# Medium Depth Extraction Assessment Prompt

**Version:** 1.0
**Last Updated:** 2025-10-31
**Assessment Depth:** Medium (2-3 hours)
**Based on:** planning/extraction-assessment-rubric-v1.md

---

## Your Task

Assess the quality of a research paper extraction along two dimensions:
1. **Accuracy** - Are extracted items correct, properly interpreted, and free from hallucinations?
2. **Granularity** - Are items appropriately atomic and consistently detailed?

**NOT assessed:** Completeness (requires re-extraction, handled separately via multi-run comparison)

---

## Input Provided

You will receive:

1. **Source paper** (full text in markdown)
2. **Extraction sample** (52 stratified items from extraction.json):
   - 15 claims (random sample)
   - 20 evidence items (random sample)
   - 10 methods (random sample)
   - 5 protocols (random sample)
   - 2 research designs (random sample)
3. **Mapping pairs** (subset to verify)
4. **Relevant rubric sections** (category definitions, verification protocols)

---

## Assessment Workflow - Multi-Pass

### Pass A: Accuracy Assessment

For each item in the sample, verify accuracy using this protocol:

#### Step 1: Locate the Quote
1. Search for the `verbatim_quote` text in the source paper
2. If not found exactly, search for key phrases (light paraphrasing is acceptable)
3. Verify the `page_number` matches the quote location
4. Check `context` fields if provided

#### Step 2: Verify Interpretation
1. Read surrounding sentences (±2 paragraphs for context)
2. Does the context support the extracted interpretation in `content`?
3. Is this the author's own claim/evidence/method, or are they describing cited work?
4. Is the item correctly categorized (claim vs evidence vs method vs protocol vs research design)?

#### Step 3: Categorize Errors

**Error Types and Penalties:**

- **HALLUCINATION (-5 points):** Quote does not exist anywhere in the paper
  - Example: Extraction claims "The authors state X" but X never appears

- **CONFABULATION (-3 points):** Quote exists but meaning is substantially misrepresented
  - Example: Paper says "We found no evidence of X" → Extracted as "Evidence shows X occurred"

- **MISATTRIBUTION (-3 points):** Quote exists but is from cited work, not paper's own claim/evidence/method
  - Example: Paper says "Smith (2015) found X" → Extracted as paper's own evidence

- **MISCATEGORIZATION (-1 point):** Item is accurately extracted but in wrong category
  - Example: Claim extracted as evidence, or method extracted as protocol
  - Still correct content, wrong bucket

- **PAGE ERROR (-0.5 points):** Quote exists with correct interpretation but wrong page number

- **CONTEXT ERROR (-2 points):** Quote exists but important contextualising information is omitted, changing meaning
  - Example: Paper says "In the southern region, unlike the north, we found X" → Extracted as general claim without regional qualifier

#### Output for Pass A:
For each item, record:
```json
{
  "item_id": "C001",
  "item_type": "claim",
  "accuracy_status": "verified_correct|has_errors",
  "errors": [
    {
      "error_type": "confabulation|hallucination|misattribution|miscategorization|page_error|context_error",
      "description": "Specific description of the error",
      "penalty_points": 3
    }
  ],
  "notes": "Any additional observations"
}
```

---

### Pass B: Granularity Assessment

For each item in the sample, assess granularity:

#### Granularity Principles

**Atomic Principle:** Each item should represent ONE distinct thing
- One claim, one piece of evidence, one method, one protocol, one design
- Compound statements should be split if parts can be independently assessed
- BUT: Don't over-split naturally coupled information

**Consistency Principle:** Similar statements should be extracted at similar levels of detail
- If "qpAdm (Haak 2015)" is one method, then "pollen analysis (Faegri & Iversen 1989)" should also be one method
- If you split radiocarbon dating into multiple protocols, do the same for other dating methods

**Functional Principle:** Granularity should serve assessment goals
- Too coarse: Can't assess credibility of individual components
- Too fine: Creates noise, obscures patterns

#### Check for Over-Splitting (Too Fine)

**Red flags:**
- Adjacent items that are always used together
- Components of a single procedure extracted separately without clear benefit

**Examples:**

Claims - Over-Split:
```
❌ WRONG:
C001: "Genetic diversity was high"
C002: "This indicates large population size"

✓ BETTER:
C001: "Genetic diversity was high, indicating large population size"
```
*Second is justification for first, not independent claim*

Evidence - Over-Split:
```
❌ WRONG:
E001: "23 radiocarbon dates were obtained"
E002: "Dates ranged from 4800-4200 BCE"

✓ BETTER:
E001: "23 radiocarbon dates ranged from 4800-4200 BCE"
```
*All facets of one dataset description*

Methods - Over-Split:
```
❌ WRONG:
M001: "We used qpAdm"
M002: "qpAdm implemented in ADMIXTOOLS"

✓ BETTER:
M001: "Genetic admixture analysed using qpAdm (Haak et al. 2015) implemented in ADMIXTOOLS"
```

#### Check for Under-Splitting (Too Coarse)

**Red flags:**
- Multiple distinct ideas compressed into one item
- "And" statements that join separable components
- Items that mix categories

**Examples:**

Claims - Under-Split:
```
❌ WRONG:
C001: "Genetic diversity was high indicating large population size, which likely resulted from immigration based on isotope data showing non-local origins for 40% of individuals"

✓ BETTER:
C001: "Genetic diversity was high, indicating large population size"
C002: "Large population size likely resulted from immigration"
C003: "40% of individuals show non-local isotopic signatures"
```
*Three distinct interpretive statements*

Evidence - Under-Split:
```
❌ WRONG:
E001: "Radiocarbon dating, stable isotope analysis, and DNA sequencing were performed, yielding 23 dates (4800-4200 BCE), δ13C values of -21±2‰, and 15 genetic sequences"

✓ BETTER:
E001: "23 radiocarbon dates ranged from 4800-4200 BCE"
E002: "Stable isotope analysis yielded δ13C values of -21±2‰"
E003: "DNA sequencing produced 15 genetic sequences"
```
*Three distinct datasets*

#### Check for Consistency

- Select 5-10 items of same type
- Compare level of detail
- Identify outliers (much more or less detailed than others)
- Assess if variation is justified or inconsistent

#### Output for Pass B:
For each item, record:
```json
{
  "item_id": "C001",
  "item_type": "claim",
  "granularity_status": "appropriate|over_split|under_split|inconsistent",
  "issue_description": "If not appropriate, explain why",
  "suggested_action": "merge_with: [C002]|split_into: 2-3 items|increase_detail|reduce_detail",
  "consistency_notes": "How this compares to similar items"
}
```

---

### Pass C: Mapping Accuracy Assessment

For each mapping pair provided, verify the link accuracy:

#### Mapping Types

- **Claim → Evidence:** Does the evidence actually support the claim?
- **Protocol → Method:** Is the protocol a component/implementation of the method?
- **Method → Research Design:** Is the method part of the design framework?
- **Evidence → Method:** Was the evidence generated/analysed using this method?

#### Verification Protocol

For each mapped pair:
1. Read both items (claim + evidence, or protocol + method, etc.)
2. Check logical connection:
   - Does B actually support/implement/relate to A?
   - Is the connection explicit in the paper or inferred?
   - Is the inference chain clear?
3. Categorize mapping strength

#### Mapping Categories

**Strong Mapping:**
- Direct, explicit connection in paper
- Evidence directly supports claim
- Protocol clearly implements method
- Example: C001 "Population increased after 2000 BCE" → E005 "Settlement count increased from 12 to 47"

**Weak Mapping:**
- Connection requires inference, may be valid but uncertain
- Inference chain not fully clear
- Example: C015 "Migration occurred" → E023 "Admixture coefficient 0.23" (doesn't indicate direction alone)

**Incorrect Mapping:**
- No logical connection
- Misinterprets relationship
- Example: C001 "Climate was warm" → E008 "Pottery styles changed" (no connection)

#### Output for Pass C:
For each mapping, record:
```json
{
  "mapping_id": "C001→E005",
  "item_a": "C001",
  "item_b": "E005",
  "mapping_type": "claim_to_evidence",
  "strength": "strong|weak|incorrect",
  "explanation": "Why this mapping is strong/weak/incorrect",
  "action": "keep|flag_for_review|remove"
}
```

---

## Final Output Format

Provide your assessment as structured JSON:

```json
{
  "assessment_metadata": {
    "paper": "paper-slug",
    "assessor": "claude-3.7-sonnet|gemini-2.5-pro|gpt-4.5|human",
    "assessment_date": "YYYY-MM-DD",
    "assessment_depth": "medium",
    "sample_size": 52,
    "total_items_in_extraction": 176
  },

  "accuracy_assessment": {
    "items_assessed": 52,
    "items_by_type": {
      "claims": 15,
      "evidence": 20,
      "methods": 10,
      "protocols": 5,
      "research_designs": 2
    },
    "verified_correct": 48,
    "items_with_errors": 4,
    "errors_by_type": {
      "hallucinations": 0,
      "confabulations": 1,
      "misattributions": 2,
      "miscategorizations": 3,
      "page_errors": 2,
      "context_errors": 0
    },
    "error_details": [
      {
        "item_id": "C023",
        "error_type": "confabulation",
        "description": "States 'population declined' but paper says 'no evidence of decline'",
        "penalty_points": 3
      }
    ],
    "raw_score": 48,
    "total_penalties": 8.5,
    "accuracy_score": 92.3,
    "grade": "A"
  },

  "granularity_assessment": {
    "items_assessed": 52,
    "appropriate_granularity": 45,
    "over_split_items": 3,
    "under_split_items": 2,
    "inconsistent_items": 2,
    "issue_details": [
      {
        "item_id": "C001",
        "issue": "over_split",
        "description": "Should be merged with C002 - second is justification not independent claim",
        "suggested_action": "merge_with: [C002]"
      }
    ],
    "granularity_score": 86.5,
    "grade": "B"
  },

  "mapping_assessment": {
    "mappings_assessed": 25,
    "strong_mappings": 20,
    "weak_mappings": 3,
    "incorrect_mappings": 2,
    "mapping_details": [
      {
        "mapping_id": "C012→E028",
        "strength": "incorrect",
        "explanation": "Claim about climate linked to pottery evidence with no logical connection",
        "action": "remove"
      }
    ],
    "mapping_score": 88.0,
    "grade": "B"
  },

  "overall_assessment": {
    "weighted_score": 89.2,
    "grade": "B",
    "calculation": "(92.3 × 0.50) + (86.5 × 0.30) + (88.0 × 0.20) = 89.2",
    "interpretation": "Good quality, some corrections needed",
    "recommendation": "Usable for assessment with awareness of limitations"
  },

  "priority_corrections": [
    "Fix confabulation in C023",
    "Fix misattributions in E015, E027",
    "Merge over-split items: C001+C002, E034+E035",
    "Remove incorrect mappings: C012→E028, C019→E041"
  ],

  "assessor_notes": "Generally consistent extraction. Claims show some granularity inconsistency (high detail for genetic claims, low detail for environmental claims). Methodological paper profile as expected (heavy claims, light evidence)."
}
```

---

## Category Definitions Reference

### Claims
**Core:** Interpretation, conclusion, or assertion by the paper's authors

**Include:**
- Interpretations of empirical results
- Methodological assertions and justifications
- Theoretical positions and arguments
- Empirical generalisations
- Comparative statements

**Exclude:**
- Background literature claims (unless actively evaluated/tested)
- Pure descriptions without interpretation
- Research questions/hypotheses (unless asserted as findings)

**Edge Cases:**
- "We used method X because Y" → The "because Y" is a claim (justification)
- "Table 1 shows increased values" → Claim (interpretation)
- "Values increased from 10 to 15" → Evidence (description)

### Evidence
**Core:** Data, observations, measurements, or results reported by authors

**Include:**
- Quantitative data and measurements
- Qualitative observations
- Statistical results
- Visual/material evidence descriptions
- Negative results

**Exclude:**
- Interpretations of data (those are claims)
- Background/literature data (unless comparative evidence)
- Methodological procedures

**Edge Cases:**
- "Pollen assemblages show 60% arboreal taxa" → Evidence
- "This indicates woodland environment" → Claim
- "No artefacts found in Layer 3" → Evidence (negative result)

### Methods
**Core:** Analytical techniques, procedures, or approaches used to generate/analyse evidence

**Include:**
- Analytical techniques (radiocarbon dating, DNA sequencing, etc.)
- Statistical methods (Bayesian modelling, PCA, etc.)
- Field methods (excavation, survey, sampling)
- Software/tools used for analysis

**Exclude:**
- Detailed procedural steps (those are protocols)
- Equipment specifications alone

**Edge Cases:**
- "We used radiocarbon dating" → Method
- "Samples pretreated with acid-alkali-acid" → Protocol

### Protocols
**Core:** Specific procedural steps, parameters, or implementation details

**Include:**
- Sample preparation procedures
- Measurement parameters
- Quality control steps
- Software parameters/settings
- Calibration procedures

**Exclude:**
- High-level method names (those are methods)
- Results of protocol application (those are evidence)

### Research Designs
**Core:** Overarching investigative strategies or frameworks

**Include:**
- Study design types (comparative, longitudinal, case study)
- Sampling strategies (spatial, temporal, systematic vs targeted)
- Data integration approaches (multi-proxy, triangulation)
- Analytical frameworks (hypothesis testing, exploratory)

**Exclude:**
- Individual methods
- Procedural details

---

## Scoring Formulas

### Accuracy Score
```
Accuracy = (Verified Correct Items - Error Penalties) / Total Items × 100%

Error Penalties = (Hallucinations × 5) + (Confabulations × 3) + (Misattributions × 3)
                + (Miscategorisations × 1) + (Page Errors × 0.5) + (Context Errors × 2)
```

### Granularity Score
```
Granularity = (Items at Appropriate Level) / Total Items × 100%

Appropriate Level = Total - Over-Split - Under-Split - Inconsistent
```

### Mapping Score
```
Mapping = (Strong Mappings + 0.5 × Weak Mappings) / Total Mappings × 100%
```

### Overall Score
```
Overall = (Accuracy × 0.50) + (Granularity × 0.30) + (Mapping × 0.20)
```

### Grade Interpretation
- **95-100% (A):** Excellent, minimal corrections needed
- **85-94% (B):** Good, some minor errors to address
- **75-84% (C):** Acceptable, systematic errors should be investigated
- **65-74% (D):** Poor, significant problems
- **<65% (F):** Unacceptable, requires major revision

---

## Important Notes

1. **Be thorough but efficient:** You're assessing a sample, not the full extraction. Focus on systematic patterns.

2. **Document ambiguity:** If an item is borderline (could be claim or evidence, over-split or appropriate), note it. These edge cases inform rubric refinement.

3. **Assess extraction quality, not paper quality:** A paper can make weak claims or have sparse evidence - assess whether the extraction correctly captured what the paper said, not whether the paper is good.

4. **Statistical extrapolation:** Your assessment of 52 items will be extrapolated to estimate full extraction quality (176 items in this example). Focus on identifying systematic patterns.

5. **Context matters:** Always read surrounding paragraphs when verifying quotes. Isolated sentences can be misleading.

---

## Begin Assessment

Proceed through Pass A (Accuracy) → Pass B (Granularity) → Pass C (Mapping), then compile the final JSON output.
