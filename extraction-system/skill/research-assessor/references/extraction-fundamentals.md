# Extraction Fundamentals - Universal Sourcing Requirements

**Last Updated:** 2025-10-28
**Schema Version:** 2.5+
**Applies to:** All extraction passes (Pass 1-5: Claims/Evidence and RDMAP extraction)
**Purpose:** Core sourcing requirements that apply across all object types

---

## 🚨 MANDATORY SOURCING REQUIREMENT

**Schema v2.5 introduced mandatory sourcing to prevent hallucination.**

Every extracted item must be traceable to specific passages in the paper. **No exceptions.**

### Universal Principle

**Before extracting ANY item, ask:**
- "Can I point to the exact text that states or implies this?"
- If NO → **DO NOT EXTRACT**

---

## Explicit vs Implicit Content

All extractable content falls into two categories:

### EXPLICIT CONTENT
**Definition:** Directly stated in the paper with clear procedural detail or assertion.

**Required fields:**
- `verbatim_quote` (string, required) - Exact text from paper
- `location` (object, required) - Section, subsection, paragraph
- Content must match what quote actually says

**Quick test:** "Is this directly stated in the paper?"
- If YES → Extract as explicit with verbatim_quote
- If NO → Check if implicit (below)

**Examples of explicit content:**
- Evidence: "We recorded 8,343 features"
- Claims: "The mobile platform was more efficient"
- Methods: "We used stratified random sampling with 30% coverage"
- Protocols: "GPS coordinates recorded using Trimble GeoXH 6000"

---

### IMPLICIT CONTENT
**Definition:** Not directly stated but can be reasonably inferred from available passages.

**Required fields:**
- `trigger_text` (array of strings, required) - Verbatim passages that imply the content
- `trigger_locations` (array of location objects, required) - Where each trigger found
- `inference_reasoning` (string, required) - Explanation connecting triggers to inferred content
- `implicit_metadata` (object, required for some types) - Basis, gaps, confidence

**Quick test:** "Can I point to passages that together imply this?"
- If YES → Extract as implicit with triggers
- If NO → DO NOT EXTRACT

**Examples of implicit content:**
- Implicit Arguments: Unstated assumptions, logical implications
- Implicit Methods: Procedures mentioned but not described
- Implicit Protocols: Implementation details inferred from results

---

## Implicit RDMAP Extraction in Section-by-Section Passes

### The Challenge

When extracting RDMAP section-by-section (Abstract+Intro, Methods, Results, Discussion),
each section must extract **BOTH explicit AND implicit** RDMAP items.

**Common failure mode**: Only extracting explicit items (what's documented in Methods),
missing implicit items (procedures mentioned but not described).

### Where Implicit RDMAP Items Hide

**Implicit Methods** - Procedures mentioned but not described:
- ✓ Results: "We cleaned the data" → Data cleaning method (implicit if procedure not in Methods)
- ✓ Discussion: "We validated against external datasets" → Validation method (implicit)
- ✓ Results: "Error checking revealed..." → QA method (implicit if process not described)

**Implicit Protocols** - Implementation details inferred from execution:
- ✓ Results: "2,500 records per device caused performance degradation" → Load threshold monitoring protocol
- ✓ Results: "Students were assigned specific map tiles" → Map assignment protocol
- ✓ Results: "We corrected spatial omissions by re-extracting coordinates" → Error correction protocol

**Implicit Research Designs** - Strategic decisions apparent but unstated:
- ✓ Introduction: Positioning study relative to other approaches (if framing not in Methods)
- ✓ Discussion: Threshold analysis framework (if decision criteria not explicitly designed)

### Section-by-Section Extraction Workflow

**For EACH section (Abstract+Intro, Methods, Results, Discussion):**

1. **First**: Extract explicit RDMAP
   - Items documented in Methods section OR clearly stated in current section
   - Use `*_status = "explicit"` with `verbatim_quote`

2. **Then**: Scan for implicit RDMAP
   - Look for **VERBS without procedures**: cleaned, validated, checked, assigned, corrected
   - Look for **EFFECTS implying causes**: "performance degraded at 2,500 records" → monitoring
   - Look for **MENTIONS without descriptions**: "assigned maps" → assignment protocol

3. **For each implicit item**:
   - Extract `trigger_text` array (verbatim passages mentioning the procedure)
   - Record `trigger_locations` (where each trigger found)
   - Write `inference_reasoning` (explain how triggers imply the RDMAP item)
   - Add `implicit_metadata` with basis and assessment_implication

### Recognition Patterns

**Pattern 1: Mentioned Procedure**
- Trigger: Paper mentions doing something but doesn't describe how
- Example: "We quality-checked digitised features"
- Extract: Implicit protocol for QA procedure
- Reasoning: "Paper states QA occurred but provides no procedural details"

**Pattern 2: Inferred from Results**
- Trigger: Results section reveals operational detail not in Methods
- Example: "Performance degraded after ~2,500 records per device"
- Extract: Implicit protocol for load monitoring
- Reasoning: "Precise threshold detection implies monitoring, but monitoring method undocumented"

**Pattern 3: Undocumented Assignment**
- Trigger: References to "assigned" tasks without assignment method
- Example: "Students assigned specific map tiles"
- Extract: Implicit protocol for task assignment
- Reasoning: "Assignment mentioned multiple times but allocation method never described"

**Pattern 4: Implied Strategic Decision**
- Trigger: Discussion positions study but framing not in Methods
- Example: Paper compares approach to ML without stating this was design goal
- Extract: Implicit research design for comparative positioning
- Reasoning: "Systematic comparison implies design choice, but not stated as objective"

### Quick Reference: Explicit vs Implicit RDMAP

| Aspect | Explicit | Implicit |
|--------|----------|----------|
| **Location** | Documented in Methods OR clearly stated | Mentioned/inferred from Results/Discussion |
| **Test** | "Is procedure described?" | "Is procedure mentioned but not described?" |
| **Status field** | `"explicit"` | `"implicit"` |
| **Source field** | `verbatim_quote` | `trigger_text` array |
| **Reasoning** | Not required | `inference_reasoning` required |

### Common Mistakes to Avoid

❌ **Assuming implicit = absent**: If paper never mentions a procedure, it's absent (don't extract). Implicit means mentioned but undocumented.

❌ **Extracting standard practices**: Don't infer "they must have done X" from domain knowledge. Only extract what paper mentions.

❌ **Marking Methods section items as implicit**: Items documented in Methods section are explicit, even if terse.

✓ **Correct approach**: Implicit items have textual triggers (mentions) but lack procedural detail.

---

## Implicit Arguments Extraction in Claims-Evidence Passes

### The Challenge

When extracting claims and evidence, implicit arguments are easily overlooked because they're definitionally unstated. Each core claim requires systematic search for 4 types of implicit arguments.

**Common failure mode**: Only extracting obvious logical implications (Type 1), missing deeper assumptions (Types 2-4) that are often more assessment-critical.

### Where Implicit Arguments Hide

**Type 1: Logical Implications** - Unstated steps in reasoning chain:
- ✓ Discussion: "Method is accurate" → implies adequate calibration/validation occurred
- ✓ Results: "Complete dataset" → implies no systematic exclusions occurred
- ✓ Claims about platform "efficiency" → implies comparison baseline exists

**Type 2: Unstated Assumptions** - Prerequisites assumed without acknowledgment:
- ✓ Introduction: Spatial analysis assumes GPS accuracy adequate for research scale
- ✓ Methods: Sample representativeness assumes no systematic bias in selection
- ✓ Claims: Quality judgments assume evaluator competence and consistent criteria

**Type 3: Bridging Claims** - Missing links between evidence and conclusions:
- ✓ Evidence: "8,343 features collected" → Claim: "Comprehensive coverage"
  Missing bridge: What makes 8,343 "comprehensive"? (comparison to target/expectations)
- ✓ Evidence: "95% accuracy" → Claim: "High quality"
  Missing bridge: What threshold defines "high"? (disciplinary norms or requirements)

**Type 4: Disciplinary Assumptions** - Field-specific taken-for-granted knowledge:
- ✓ Archaeology: Surface visibility relates to artifact presence (not stated in paper)
- ✓ GIS: Coordinate precision adequate for analysis scale (assumed without verification)
- ✓ Digital Humanities: Manual digitisation quality assumptions (expert = accurate)

### Section-by-Section Extraction Workflow

**For EACH section (Abstract, Introduction, Methods, Results, Discussion):**

1. **First**: Extract explicit claims and evidence
   - Direct statements requiring minimal interpretation
   - Use `*_status = "explicit"` with `verbatim_quote`

2. **Then**: For each CORE claim, run systematic 4-type implicit argument scan
   - **Type 1 scan**: "If this claim is true, what MUST also be true?"
   - **Type 2 scan**: "What must be true for this claim to hold?"
   - **Type 3 scan**: "How do they get from evidence to this claim?"
   - **Type 4 scan**: "What field-specific knowledge is taken for granted?"

3. **For each implicit argument found**:
   - Extract `trigger_text` array (verbatim passages implying the argument)
   - Record `trigger_locations` (where each trigger found)
   - Write `inference_reasoning` (explain how triggers imply argument)
   - Add `implicit_metadata` with basis and assessment_implication

### Recognition Patterns

**Pattern 1: Undefended Quality Judgments**
- Trigger: Claims use evaluative terms without criteria or comparison
- Example: "Data quality was high" without defining "high" or comparison baseline
- Extract: Implicit assumption about quality thresholds or adequacy criteria
- Reasoning: "Paper asserts 'high quality' but never specifies criteria, threshold, or comparison baseline that justifies 'high'"

**Pattern 2: Comparison Without Baseline**
- Trigger: Efficiency/performance claims without stated comparison point
- Example: "Platform was efficient" without stating "compared to what?"
- Extract: Implicit comparison assumption (expectations, alternatives, or prior experience)
- Reasoning: "Efficiency is inherently relative—claim implies unstated baseline or expectations"

**Pattern 3: Capability Assumptions**
- Trigger: Methods rely on technical capabilities without verification discussion
- Example: GPS-based spatial analysis with no accuracy/precision discussion
- Extract: Implicit adequacy assumption about technical capability
- Reasoning: "Spatial analysis assumes GPS precision adequate for research scale, but adequacy never verified or discussed"

**Pattern 4: Inferential Leaps**
- Trigger: Large gap between evidence granularity and claim scope/generality
- Example: Evidence: "3 volunteers had issues" → Claim: "Supervision challenges exist"
- Extract: Bridging argument about representativeness or pattern significance
- Reasoning: "Leap from 3 specific cases to general pattern needs bridging claim about whether sample is representative or significant"

**Pattern 5: Definitional Assumptions**
- Trigger: Terms used with assumed meaning without definition
- Example: "Comprehensive survey" without defining comprehensiveness criteria
- Extract: Implicit definition or threshold assumption
- Reasoning: "Comprehensiveness requires criteria (spatial coverage? feature types? completeness threshold?) but none stated"

**Pattern 6: Causal Assumptions**
- Trigger: Causal language without mechanism or alternative exclusion
- Example: "Mobile platform caused efficiency gains" without mechanism or confound discussion
- Extract: Implicit causal mechanism or alternative exclusion argument
- Reasoning: "Causal claim requires mechanism and alternative exclusion, but neither discussed"

### Quick Reference: Explicit vs Implicit Arguments

| Aspect | Explicit Claims | Implicit Arguments |
|--------|----------------|-------------------|
| **Location** | Directly stated in paper | Implied by reasoning structure |
| **Test** | "Does paper say this?" | "Does reasoning require this unstated step?" |
| **Status field** | `"explicit"` (claims) | `"implicit"` (arguments) |
| **Source field** | `verbatim_quote` | `trigger_text` array |
| **Reasoning** | Not required | `inference_reasoning` required |
| **Object type** | claims array | implicit_arguments array |

### Common Mistakes to Avoid

❌ **Assuming implicit = unimportant**: Implicit arguments are often the most assessment-critical items. They reveal unacknowledged assumptions that affect credibility.

❌ **Only extracting Type 1 (logical implications)**: Type 1 is easiest to spot, so extractions can become Type 1-heavy. Types 2-4 require deeper analysis but are often more significant for assessment.

❌ **Treating "domain knowledge" as implicit**: If paper never references or relies on a concept, it's absent (don't extract). Implicit means the AUTHORS' reasoning requires it even though unstated.

❌ **Extracting from YOUR reasoning**: Only extract implicit arguments the AUTHORS' reasoning depends on, not what YOU think they should have considered (that's your critique, not their argument).

❌ **Superficial scanning**: "Looked for implicit arguments, found none" without demonstrating systematic 4-type scan per core claim is inadequate. Document your scan methodology.

❌ **No trigger passages**: Implicit arguments need verbatim trigger_text showing where reasoning implies the unstated step. "I inferred this" without textual basis is hallucination.

✓ **Correct approach**: Systematic 4-type scan for EACH core claim, documenting verbatim trigger passages that show why authors' reasoning depends on this implicit step, with clear inference_reasoning connecting triggers to argument.

### When NOT to Extract Implicit Arguments

**Don't extract when:**
- Paper explicitly states the assumption/implication (then it's an explicit claim, not implicit argument)
- No textual triggers exist (that's your own inference, not theirs)
- Claim is trivial with no assessment implications
- It's about what they SHOULD have done (your critique, not their reasoning dependency)
- The "gap" is standard for the discipline (e.g., every paper assumes basic math works)

**Do extract when:**
- Authors' reasoning chain requires it even though unstated
- Multiple triggers in paper imply the assumption
- Assessment implications exist (affects transparency, credibility, reproducibility)
- It's not obvious to readers outside the discipline
- The unstated step affects interpretation of claims

### Cross-Section Synthesis Patterns (Pass 2 Focus)

With full-paper context, certain implicit arguments become visible that weren't apparent in section-by-section extraction:

**Threshold Criteria Used Throughout**
- Paper applies quality threshold judgments in multiple sections
- But never states threshold criteria
- Extract: Implicit threshold definition used consistently

**Comparative Framing**
- Discussion positions study relative to alternatives throughout
- But never explicitly states this was a design objective
- Extract: Implicit comparative research framing

**Methodological Adequacy Assumptions**
- Multiple claims depend on method adequacy
- But adequacy criteria never discussed
- Extract: Implicit adequacy assumptions spanning methods and findings

**Generalisability Claims**
- Results stated, then discussed as if generalisable
- But generalisability conditions never specified
- Extract: Implicit generalisability assumptions

---

## Hallucination Prevention

**Critical rules:**

1. **No guessing** - If you cannot find source text, DO NOT extract the item
2. **No inferring from knowledge** - Only extract what paper actually says or clearly implies
3. **No combining unstated ideas** - Don't create synthetic claims from disparate observations
4. **Verbatim quotes required** - For explicit items, quote must be exact
5. **Trigger text required** - For implicit items, triggers must be verbatim passages

**Common hallucination risks:**
- Inferring methods that "must have been used" without textual support
- Creating claims that seem implied but have no trigger passages
- Assuming standard practices without paper mentioning them
- Over-interpreting vague statements

---

## Verbatim Quote Requirements

**CRITICAL:** For detailed guidance on creating proper verbatim quotes, see:  
→ **`references/verbatim-quote-requirements.md`**

**Key rules (full details in reference file):**
1. Extract **complete sentences** only (whole grammatical units)
2. Copy-paste **exact text** from paper (no paraphrasing)
3. **Verify quote exists** in paper before extracting
4. Use **single source location** per quote (no synthesis)
5. Character normalization allowed: hyphens, line breaks, whitespace

**Common failures to avoid:**
- ❌ Mid-sentence fragments ("volunteers required extensive support")
- ❌ Paraphrased reconstruction ("In 2010, we attempted to...")
- ❌ Synthesized multi-source quotes (combining separate statements)

**When uncertain:** Read the detailed requirements file before extracting.

---

## Field Requirements Summary

### For ALL Explicit Items
```json
{
  "*_id": "string",
  "*_text": "string", 
  "*_status": "explicit",
  "verbatim_quote": "Exact text from paper (REQUIRED)",
  "location": {
    "section": "string (REQUIRED)",
    "subsection": "string or null",
    "paragraph": "integer or null"
  }
}
```

### For ALL Implicit Items
```json
{
  "*_id": "string",
  "*_text": "string",
  "*_status": "implicit",
  "trigger_text": [
    "Verbatim passage 1 that implies content",
    "Verbatim passage 2 that implies content"
  ],
  "trigger_locations": [
    {"section": "string", "subsection": "string", "paragraph": 1},
    {"section": "string", "subsection": "string", "paragraph": 3}
  ],
  "inference_reasoning": "Explanation of how triggers support inference (REQUIRED)",
  "location": {
    "section": "Primary location (REQUIRED)",
    "subsection": "string or null", 
    "paragraph": "integer or null"
  }
}
```

*Note: Some object types (RDMAP, Implicit Arguments) require additional `implicit_metadata` fields. See object-specific prompts for details.*

---

## Source Verification (Pass 6)

All extracted items are verified in Pass 6 (Validation) using `source_verification` object:

### Explicit Items Verification
- `location_verified`: Stated location exists and discusses topic
- `quote_verified`: verbatim_quote found at stated location
- `content_aligned`: Item content matches what quote actually says

### Implicit Items Verification
- `trigger_locations_verified`: All trigger locations exist and accessible
- `trigger_quotes_verified`: All trigger_text found at stated locations  
- `inference_reasonable`: inference_reasoning is logical given triggers

**Quality threshold:** >95% pass rate expected across all items

---

## Quick Reference: Decision Tree

```
Can you point to text that states or implies this content?
├─ NO → DO NOT EXTRACT (item absent, not implicit)
└─ YES → Is it directly stated?
    ├─ YES → EXPLICIT
    │   ├─ Extract verbatim_quote
    │   ├─ Set *_status = "explicit"
    │   └─ Record location
    └─ NO, but implied → IMPLICIT
        ├─ Extract trigger_text array (verbatim passages)
        ├─ Set *_status = "implicit"
        ├─ Record trigger_locations
        ├─ Explain inference_reasoning
        └─ Complete implicit_metadata (if required)
```

---

## Additional Resources

**For detailed verification procedures:**
→ `/mnt/skills/user/research-assessor/references/verification-procedures.md`
- Complete verification protocols for each object type
- Decision trees for each verification step
- Worked examples (passes and fails)
- Red flags for hallucination detection
- Edge cases and troubleshooting

**For object-specific guidance:**
→ Pass 1 prompts (claims-evidence_pass1_prompt, rdmap_pass1_prompt)
- Object-specific decision trees (e.g., "Is it in Methods section?" for RDMAP)
- Object-specific field requirements
- Object-specific examples

**For schema details:**
→ `/mnt/skills/user/research-assessor/references/schema/schema-guide.md`
- Complete field definitions
- Required vs optional fields
- Enum values and constraints

---

## Remember

**Sourcing discipline is non-negotiable in schema v2.5.**

Every item must have:
- Explicit items: verbatim_quote pointing to source
- Implicit items: trigger_text array pointing to passages

**If you cannot source it, do not extract it.**

This requirement protects against hallucination and ensures all extractions are verifiable by checking against the source paper.
