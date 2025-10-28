# Systematic Comparison: Implicit Arguments vs Implicit RDMAP Extraction

**Problem:** Implicit Arguments are being extracted successfully (6-7 items), but Implicit RDMAP items are not being extracted at all (0 items), despite both being in the prompts, skill, and schema.

**Purpose:** Identify structural differences causing complete failure to extract implicit RDMAP items.

---

## Part 1: Schema Requirements Comparison

### Implicit Arguments Schema (schema-guide.md:181-234)

**Object type:** `implicit_arguments` (separate array)

**Required fields:**
- `implicit_argument_id`: Pattern `IA###`
- `argument_text`: The unstated argument
- `type`: Type enum (logical_implication, unstated_assumption, bridging_claim, design_assumption, methodological_assumption)
- `trigger_text`: **REQUIRED** - Array of verbatim passages
- `trigger_locations`: **REQUIRED** - Array of locations (parallel)
- `inference_reasoning`: **REQUIRED** - Explanation

**Optional fields:**
- `supports_claims`: Array of claim IDs
- `disciplinary_context`: Domain
- `confidence_in_inference`: Strength
- `source_verification`: Pass 3 validation

**Key observation:** NO `implicit_metadata` object required, NO status field needed

---

### Implicit RDMAP Schema (schema-guide.md:329-445)

**Object types:** `research_designs`, `methods`, `protocols` (same arrays as explicit, distinguished by status field)

**Required fields for implicit RDMAP:**
- ID field: Pattern `RD###`, `M###`, or `P###`
- Text field: Description
- Type field: Enum for each type
- **Status field: `design_status`, `method_status`, or `protocol_status` = "implicit"**
- `trigger_text`: **REQUIRED** - Array of verbatim passages
- `trigger_locations`: **REQUIRED** - Array of locations (parallel)
- `inference_reasoning`: **REQUIRED** - Explanation
- **`implicit_metadata`: REQUIRED object with:**
  - `basis`: "mentioned_undocumented" | "inferred_from_results"
  - `transparency_gap`: Description of missing documentation
  - `assessability_impact`: Impact on assessment capability
  - `reconstruction_confidence`: "low" | "medium" | "high"

**Optional fields:**
- All the same optional fields as explicit RDMAP (cross-references, etc.)
- `source_verification`: Pass 3 validation

**Key observation:** Requires `implicit_metadata` object AND status field, making it MORE complex than implicit arguments

---

## Part 2: Prompt Instructions Comparison

### Prompt 01: Implicit Arguments (lines 156-255)

**Section title:** "4. Implicit Arguments (HIGH-PRIORITY claims only)"

**Positioning:** Integrated into main extraction workflow at Step 2.3

**Instructions structure:**
1. **Clear mandate:** "Extract implicit arguments for all core claims (REQUIRED systematic search)"
2. **Four-type taxonomy** with clear descriptions (lines 160-178)
3. **Embedded in workflow:** Step 2.3 of section-by-section extraction (lines 220-256)
4. **Systematic 4-type checklist** with specific questions (lines 223-235)
5. **Common pitfalls section** (lines 240-248) with specific mistakes to avoid
6. **Quality check requirement:** "Can you demonstrate you ran all 4 type scans?" (line 249)
7. **Mandatory if no implicit found:** "Document in extraction_notes why" (line 238)
8. **Two reference links** to detailed guidance (lines 251-255)
9. **Quality checklist includes:** "Systematic implicit argument search completed for all core claims" (line 312)

**Total coverage:** ~100 lines of guidance in main prompt

**Emphasis level:** HIGH - marked as "(HIGH-PRIORITY claims only)" in section title

---

### Prompt 03: Implicit RDMAP (lines 58-96, 251-253)

**Section title:** "🚨 CRITICAL: RDMAP Sourcing Requirements" (but covers both explicit and implicit)

**Positioning:** Separate from main extraction workflow, in "sourcing requirements" section

**Instructions structure:**
1. **Status field requirement** (lines 64-96): Decision rule for explicit vs implicit
2. **Basis classification** (lines 86-91): Two types (mentioned_undocumented, inferred_from_results)
3. **Note about transparency** (line 92-93): "Implicit status documents transparency gaps"
4. **Reference to fundamentals:** "For complete sourcing fundamentals" (line 94)
5. **Quality checklist:** Items 107-110 mention status fields and implicit metadata
6. **Pre-scan mention:** Step 0 has note about implicit patterns (line 249-253)

**Workflow integration:** NOT integrated into main Steps 1-3 extraction workflow

**No systematic extraction patterns in main prompt** - delegated to references:
- Line 249-253: "For systematic implicit RDMAP recognition patterns: → See references/extraction-fundamentals.md"

**Total coverage in main prompt:** ~40 lines (mostly schema requirements, not extraction guidance)

**Emphasis level:** MEDIUM - mentioned as part of sourcing requirements, not highlighted as high-priority

---

## Part 3: extraction-fundamentals.md Comparison

### Implicit Arguments Coverage (lines 161-316)

**Section title:** "Implicit Arguments Extraction in Claims-Evidence Passes"

**Subsections:**
1. "The Challenge" (lines 163-168) - explains why implicit arguments are easily missed
2. "Where Implicit Arguments Hide" (lines 170-191) - 4 types with concrete examples using ✓ checkmarks
3. "Section-by-Section Extraction Workflow" (lines 193-211) - specific steps for EACH section
4. "Recognition Patterns" (lines 213-248) - 6 detailed patterns with examples
5. "Quick Reference: Explicit vs Implicit Arguments" (lines 250-259) - comparison table
6. "Common Mistakes to Avoid" (lines 261-275) - 6 mistakes with ❌/✓ markers
7. "When NOT to Extract" (lines 277-291) - clear boundaries
8. "Cross-Section Synthesis Patterns" (lines 293-316) - Pass 2 considerations

**Total:** 155 lines of detailed guidance

**Key features:**
- Concrete examples with ✓ markers
- 6 recognition patterns explicitly numbered
- Decision trees and tables
- Common mistakes prominently highlighted
- When NOT to extract clearly specified

---

### Implicit RDMAP Coverage (lines 68-158)

**Section title:** "Implicit RDMAP Extraction in Section-by-Section Passes"

**Subsections:**
1. "The Challenge" (lines 70-77) - explains section-by-section implicit extraction
2. "Where Implicit RDMAP Items Hide" (lines 79-93) - 3 categories with ✓ examples
3. "Section-by-Section Extraction Workflow" (lines 95-112) - 3 steps for EACH section
4. "Recognition Patterns" (lines 114-137) - 4 patterns with examples
5. "Quick Reference: Explicit vs Implicit RDMAP" (lines 139-147) - comparison table
6. "Common Mistakes to Avoid" (lines 149-158) - 4 mistakes with ❌/✓ markers

**Total:** 90 lines of guidance

**Key features:**
- Similar structure to implicit arguments
- 4 recognition patterns explicitly numbered
- Table comparison
- Common mistakes highlighted

**CRITICAL DIFFERENCE:** No "When NOT to Extract" section (implicit arguments has this at lines 277-291)

---

## Part 4: Structural Differences Summary

### 1. **Prompt Integration Level**

| Aspect | Implicit Arguments | Implicit RDMAP |
|--------|-------------------|----------------|
| **Workflow integration** | Embedded in Step 2.3 | Mentioned in sourcing section only |
| **Systematic checklist** | 4-type scan with specific questions | No checklist in main workflow |
| **Quality gate** | "Can you demonstrate you ran scans?" | Status field checkboxes only |
| **Mandatory documentation** | "If none found, document why" | No equivalent requirement |
| **Emphasis** | "(HIGH-PRIORITY claims only)" | Part of general sourcing |
| **Lines in main prompt** | ~100 lines | ~40 lines |

**Diagnosis:** Implicit RDMAP is treated as a **sourcing option** rather than a **mandatory extraction task**

---

### 2. **Schema Complexity**

| Aspect | Implicit Arguments | Implicit RDMAP |
|--------|-------------------|----------------|
| **Object type** | Separate array | Same array as explicit (status-differentiated) |
| **Status field** | Not needed | REQUIRED (design_status/method_status/protocol_status) |
| **implicit_metadata** | Not required | REQUIRED (4 subfields) |
| **Complexity** | 6 required fields | 9+ required fields (base + status + metadata) |

**Diagnosis:** Implicit RDMAP has **higher cognitive load** - more fields, status management, metadata complexity

---

### 3. **Decision Boundaries**

| Aspect | Implicit Arguments | Implicit RDMAP |
|--------|-------------------|----------------|
| **When NOT to extract** | Explicit section (5 conditions) | Not specified in fundamentals |
| **When TO extract** | 4 conditions specified | Only by negation (not in Methods) |
| **Boundary clarity** | HIGH - multiple decision rules | MEDIUM - single location test |

**Diagnosis:** Implicit RDMAP has **weaker decision boundaries** - unclear when extraction is appropriate

---

### 4. **Recognition Patterns Detail**

| Aspect | Implicit Arguments | Implicit RDMAP |
|--------|-------------------|----------------|
| **Pattern count** | 6 recognition patterns | 4 recognition patterns |
| **Pattern names** | Named and numbered | Named and numbered |
| **Examples per pattern** | 1-2 concrete examples each | 1 example each |
| **Trigger examples** | ✓ Extensive trigger text examples | ✓ Some trigger text examples |

**Diagnosis:** Recognition patterns similar, but implicit arguments has more examples

---

### 5. **Execution Instructions**

| Aspect | Implicit Arguments | Implicit RDMAP |
|--------|-------------------|----------------|
| **In-workflow prompt** | "For EACH core claim, run 4-type checklist" | No equivalent in Steps 1-3 |
| **Delegation to references** | 2 references for detail only | Main guidance delegated to references |
| **Self-check questions** | 4 specific questions in prompt | No questions in main workflow |
| **Quality checkpoint** | In Pass 1 quality checklist (line 312) | In Pass 1 quality checklist (lines 107-110) |

**Diagnosis:** Implicit arguments has **explicit in-workflow execution instructions**, implicit RDMAP relies on **external references**

---

## Part 5: Root Cause Analysis

### Primary Failure Mode: **Workflow Invisibility**

**Implicit Arguments:**
- ✅ Integrated into Step 2.3 of main extraction workflow
- ✅ "For EACH core claim, run the 4-type checklist" - explicit iteration instruction
- ✅ Impossible to complete Step 2.3 without considering implicit arguments
- ✅ Quality gate: "Can you demonstrate you ran all 4 type scans?"

**Implicit RDMAP:**
- ❌ NOT integrated into Steps 1-3 of main extraction workflow
- ❌ No iteration instruction ("For each RDMAP item, scan for implicit items")
- ❌ Easy to complete Steps 1-3 while ignoring implicit RDMAP entirely
- ❌ Only appears as status checkbox in quality checklist, not workflow gate

**Result:** Executor follows Steps 1-3, extracts explicit RDMAP, checks status boxes, moves on. Implicit RDMAP never enters the extraction process.

---

### Secondary Failure Mode: **Complexity Overhead**

**Implicit Arguments:**
- 6 required fields (ID, text, type, trigger_text, trigger_locations, inference_reasoning)
- No status field management
- No mandatory metadata object
- Same array regardless of implicit/explicit status

**Implicit RDMAP:**
- 9+ required fields (ID, text, type, STATUS, trigger_text, trigger_locations, inference_reasoning, implicit_metadata with 4 subfields)
- Must set correct status field (design_status vs method_status vs protocol_status)
- Must populate implicit_metadata with 4 distinct fields
- Mixed array (explicit + implicit) requires status management

**Result:** Even when considering implicit RDMAP, cognitive overhead makes extraction feel burdensome. Easier to mark items as "explicit" and move on.

---

### Tertiary Failure Mode: **Framing as Transparency Gap vs Content**

**Implicit Arguments:**
- Framed as **content extraction task**: "Unstated assumptions, logical implications, bridging claims"
- Value proposition: Reveals reasoning structure, assessment-critical
- Line 156: "(HIGH-PRIORITY claims only)"
- Emphasis: Extract these because they're important for analysis

**Implicit RDMAP:**
- Framed as **transparency documentation**: "Implicit status documents transparency gaps for assessment" (line 92-93)
- Value proposition: Records missing documentation, enables assessment
- No "HIGH-PRIORITY" marker
- Emphasis: Mark status correctly for transparency evaluation

**Result:** Implicit arguments feel like **required extraction** (find the reasoning), implicit RDMAP feels like **optional metadata** (note the gaps).

---

### Quaternary Failure Mode: **Reference Delegation Without Reinforcement**

**Implicit Arguments:**
- Main prompt has 100 lines of guidance
- References provide additional detail and examples
- Executor can complete task with prompt alone
- References = depth, not discovery

**Implicit RDMAP:**
- Main prompt has 40 lines (mostly schema)
- Extraction guidance delegated to references: "See extraction-fundamentals.md" (line 249-253)
- Executor cannot complete task with prompt alone
- References = required reading, but easy to skip

**Result:** Executor might not read external references if they seem optional. Implicit RDMAP guidance never reaches execution.

---

## Part 6: Evidence from Extraction Outcomes

### Current Extraction (2025-10-28)

**Implicit Arguments:** 7 items extracted
- IA001: Efficiency measured by staff time (unstated assumption)
- IA002: Generalisability beyond Bulgarian mounds (unstated assumption)
- IA003: Conditional viability depends on staff constraints (unstated assumption)
- IA004: HCI principles transfer to deskbound work (disciplinary assumption)
- IA005: Comparison baseline is 2010 failed attempt (bridging claim)
- IA006: ML would require specialized expertise (logical implication)
- IA007: Crowdsourcing scalability has upper bound (logical implication)

**Implicit RDMAP:** 0 items extracted
- All 12 RDMAP items marked as `"explicit"`
- Validation report line: "All RDMAP items were explicit (well-documented in Methods/Approach sections)"

**Analysis:** The paper states that implicit arguments exist and were found (7 items). But for RDMAP, the extraction concluded all items were explicit. This is implausible - if the reasoning has unstated assumptions, the methodology almost certainly has undocumented procedures.

---

### RUN-05 Extraction (2025-10-27, archive)

**Implicit Arguments:** 6 items extracted
- Similar pattern to current run

**Implicit RDMAP:** 0 items extracted
- Checked: `jq '.research_designs[] | select(.design_status == "implicit")` → 0 items
- Checked: `jq '.methods[] | select(.method_status == "implicit")` → 0 items
- Checked: `jq '.protocols[] | select(.protocol_status == "implicit")` → 0 items
- **All 84 RDMAP items marked as explicit**

**Critical finding:** This is NOT a regression. Even the "comprehensive" RUN-05 extraction (275 total items) had ZERO implicit RDMAP items. The problem is systemic and predates the current run.

---

### Early Test Run (Sonnet 4.5 chatbot, pre-migration)

**User statement:** "An early test run in the Sonnet 4.5 chatbot successfully captured implicit RDMAP items"

**Implication:** The framework is capable of extracting implicit RDMAP when properly triggered. The migration to Claude Code introduced structural changes that broke this capability.

**Hypothesis:** Early test run may have had:
- Direct instructions to extract implicit RDMAP in user message
- Fewer competing priorities (simpler prompt structure)
- Interactive session allowing course correction
- Different emphasis in prompts (before recent revisions)

---

## Part 7: Smoking Gun Evidence

### The "All Explicit" Pattern

Both extractions concluded that **all RDMAP items were explicit**. This is implausible for several reasons:

1. **Implicit arguments exist (6-7 found)** - If reasoning has unstated assumptions, methodology almost certainly has undocumented procedures

2. **Paper structure** - Results and Discussion sections mention procedures not documented in Methods:
   - "Students were assigned specific map tiles" (assignment method not described)
   - "We quality-checked digitised features" (QC procedure not described)
   - "Performance degraded at ~2,500 records" (monitoring method not described)

3. **Domain knowledge** - Archaeology/GIS papers routinely have implicit protocols:
   - GPS accuracy assumptions without verification procedures
   - Data cleaning procedures mentioned but not documented
   - Quality control mentioned but methods not specified

4. **Transparency assessment purpose** - The entire point of explicit/implicit distinction is to flag missing documentation. Finding "all explicit" defeats this purpose.

**Conclusion:** Executor is not scanning for implicit RDMAP items at all. The "all explicit" conclusion is the default when implicit extraction is skipped.

---

## Part 8: Why Implicit Arguments Succeed

### Critical Success Factors

**1. Workflow Integration**

Implicit argument extraction is **impossible to skip**:

```markdown
### Step 2: Section-by-Section Extraction
...
3. **Extract Implicit Arguments** (REQUIRED systematic search for all core claims)

   For EACH core claim, run the 4-type checklist:

   **Type 1 - Logical Implications:** "If this claim is true, what MUST also be true?"
   **Type 2 - Unstated Assumptions:** "What must be true for this claim to hold?"
   **Type 3 - Bridging Claims:** "How do they get from evidence to this claim?"
   **Type 4 - Disciplinary Assumptions:** "What field-specific knowledge is taken for granted?"
```

The executor **cannot complete Step 2.3** without at least considering implicit arguments. Even if they find none, they must document why.

**2. Explicit Iteration Instruction**

"For EACH core claim, run the 4-type checklist" - this forces systematic scanning. The executor must:
- Identify core claims (Step 2.2)
- For each one, run 4 separate scans
- Document if none found

**3. Quality Gate**

Line 249-250: "Quality Check: For each core claim, can you demonstrate you ran all 4 type scans? Document scan methodology in extraction_notes if needed."

This creates accountability - cannot claim completion without evidence of scanning.

**4. High-Priority Framing**

Line 156: "### 4. Implicit Arguments (HIGH-PRIORITY claims only)"

Signals that this is not optional or peripheral.

---

## Part 9: Why Implicit RDMAP Fails

### Critical Failure Factors

**1. Workflow Non-Integration**

Implicit RDMAP is **easy to skip**:

```markdown
### Step 1: Identify Research Designs
- Scan for design language
- Identify each distinct strategic decision point
- Extract theoretical frameworks
- Determine explicit vs implicit status
- Populate verbatim_quote OR trigger_text appropriately
- Liberal extraction
```

"Determine explicit vs implicit status" is a **single checklist item** among many. No iteration instruction, no systematic scan, no separate step. Easy to interpret as "note the status" rather than "actively scan for implicit items".

**2. No Iteration Instruction**

Implicit arguments: "For EACH core claim, run the 4-type checklist"
Implicit RDMAP: ~~No equivalent~~

There's no "For each section, scan for implicit RDMAP" or "For each method, check if procedures are documented" instruction in the main workflow.

**3. No Quality Gate**

Quality checklist line 107: "- [ ] Status fields set for all RDMAP items (explicit or implicit)"

This is a **checkbox about field population**, not a gate requiring evidence of systematic scanning. Executor can check this box by setting all items to "explicit" without considering whether implicit items exist.

**4. Transparency Framing Instead of Content Framing**

Line 92-93: "Note: Implicit status documents transparency gaps for assessment. It does NOT mean 'bad methodology' - many legitimate decisions may not be fully documented."

This frames implicit RDMAP as **meta-documentation** (noting gaps) rather than **content extraction** (finding undocumented procedures). It sounds like an optional annotation rather than a core extraction task.

**5. Reference Delegation**

Line 249-253: "For systematic implicit RDMAP recognition patterns: → See references/extraction-fundamentals.md"

Main extraction guidance is **delegated to external references** that may not be consulted. Implicit arguments has 100 lines of guidance IN the main prompt; implicit RDMAP says "see external reference".

---

## Part 10: Proposed Fixes

### Fix 1: Integrate Implicit RDMAP into Main Workflow (HIGH PRIORITY)

**Current (Step 1 in prompt 03):**
```markdown
### Step 1: Identify Research Designs
- Scan for design language
- [8 bullet points]
- Determine explicit vs implicit status
- Populate verbatim_quote OR trigger_text appropriately
```

**Proposed:**
```markdown
### Step 1: Identify Research Designs

**Phase A: Extract Explicit Research Designs**
- Scan Abstract, Introduction, Methods for design language
- Extract strategic decisions documented with rationale
- Set design_status = "explicit"
- Populate verbatim_quote

**Phase B: Scan for Implicit Research Designs (REQUIRED)**

For EACH major section (Abstract, Introduction, Methods, Results, Discussion):

Run 4-pattern implicit RDMAP scan:
1. **Mentioned Procedure:** Strategic decisions referenced but not explained?
2. **Effects Implying Causes:** Outcomes suggesting design choices?
3. **Mentions Without Descriptions:** Frameworks referenced but not specified?
4. **Strategic Positioning:** Comparative framing without explicit design statement?

Document scan in extraction_notes. If no implicit designs found: state why.

For each implicit design found:
- Extract trigger_text from passages
- Set design_status = "implicit"
- Populate implicit_metadata (basis, transparency_gap, assessability_impact, reconstruction_confidence)
```

**Apply same structure to Steps 2 (Methods) and 3 (Protocols).**

---

### Fix 2: Add Explicit Iteration Instructions

**Add to each RDMAP extraction step:**

```markdown
### Systematic Implicit RDMAP Scan

After extracting explicit items, FOR EACH SECTION (Abstract, Intro, Methods, Results, Discussion):

1. **Scan for verb phrases without procedures:**
   - "cleaned", "validated", "checked", "assigned", "corrected", "filtered"
   - If found: Extract as implicit method/protocol

2. **Scan for effects implying causes:**
   - Performance thresholds → monitoring protocols
   - Error rates → QA methods
   - Assignment patterns → allocation protocols
   - If found: Extract as implicit protocol

3. **Scan for mentions without descriptions:**
   - "Students assigned maps" → assignment protocol
   - "Data quality-checked" → QA method
   - "GPS accuracy adequate" → accuracy verification protocol
   - If found: Extract as implicit method/protocol

4. **Document scan:** Add to extraction_notes if no implicit items found in section
```

---

### Fix 3: Add Quality Gate (Not Checkbox)

**Current quality checklist:**
```markdown
- [ ] Status fields set for all RDMAP items (explicit or implicit)
```

**Proposed quality checklist:**
```markdown
- [ ] Systematic implicit RDMAP scan completed for EACH major section
- [ ] For each section, documented implicit scan methodology OR implicit items found
- [ ] All implicit RDMAP items have trigger_text, trigger_locations, inference_reasoning, implicit_metadata
- [ ] If zero implicit RDMAP items: extraction_notes explains why (e.g., "Exceptionally well-documented Methods section with all procedures explicit")
- [ ] Status fields set for all RDMAP items based on documentation location
```

---

### Fix 4: Reframe from Transparency to Content

**Current framing (line 92-93):**
> "Note: Implicit status documents transparency gaps for assessment. It does NOT mean 'bad methodology' - many legitimate decisions may not be fully documented."

**Proposed framing:**
> "CRITICAL: Implicit RDMAP extraction is as important as explicit RDMAP extraction. Many papers mention procedures without documenting them, or imply methods through results. These undocumented procedures are assessment-critical because they reveal transparency gaps and affect reproducibility. Extract implicit RDMAP items as PRIMARY CONTENT, not optional metadata."

---

### Fix 5: Elevate Priority Level

**Add to prompt 03 after line 13:**

```markdown
## 🚨 HIGH-PRIORITY: Extract Both Explicit AND Implicit RDMAP

**This pass extracts TWO equally important types of RDMAP:**

1. **Explicit RDMAP** - Documented in Methods (verbatim_quote)
2. **Implicit RDMAP** - Mentioned but undocumented, or inferred from Results/Discussion (trigger_text)

**BOTH are mandatory extraction targets.**

Implicit RDMAP items are assessment-critical because they reveal:
- Transparency gaps (what's missing from Methods documentation)
- Reproducibility barriers (procedures that cannot be replicated)
- Credibility concerns (undocumented decisions affecting results)

**Expected outcome:** Most papers have 20-40% of RDMAP items implicit. Finding zero implicit items indicates incomplete extraction or exceptional documentation (rare).
```

---

### Fix 6: Move Recognition Patterns to Main Prompt

**Current:** Recognition patterns delegated to extraction-fundamentals.md (line 249-253)

**Proposed:** Copy the 4 recognition patterns from extraction-fundamentals.md:115-137 directly into prompt 03 main workflow, similar to how implicit argument patterns are in prompt 01.

This ensures executor sees the patterns without needing to consult external references.

---

### Fix 7: Add Mid-Section Implicit Extraction Checkpoint

**Add after each section group in workflow:**

```markdown
**After extracting from [Section]:**

1. Count explicit RDMAP items extracted: __
2. Count implicit RDMAP items extracted: __
3. Implicit extraction ratio: __ / (__ + __) = __%

**Self-check:**
- If implicit ratio < 10%: Review section for undocumented procedures mentioned in Results/Discussion
- If implicit ratio = 0%: Document in extraction_notes why no implicit items found

Expected: 20-40% of RDMAP items typically implicit in most papers.
```

---

### Fix 8: Add Worked Examples to Main Prompt

**Add to prompt 03 Examples section (lines 329-457):**

```markdown
### Example 5: Systematic Implicit RDMAP Scan (Methods Section)

**Explicit extraction finds:**
- M001: FAIMS Mobile platform for data collection (explicit)
- M002: Volunteer crowdsourcing approach (explicit)
- M003: Time-on-task measurement (explicit)

**Then run implicit RDMAP scan:**

**Scan 1 - Verb phrases without procedures:**
- ✓ Found: "Students were assigned specific map tiles"
  → Extract: P-IMP-001 (Map assignment protocol, implicit - mentioned_undocumented)

- ✓ Found: "We quality-checked digitised features"
  → Extract: M-IMP-001 (QA method, implicit - mentioned_undocumented)

**Scan 2 - Effects implying causes:**
- ✓ Found: "Performance degraded after ~2,500 records per device"
  → Extract: P-IMP-002 (Load monitoring protocol, implicit - inferred_from_results)

**Scan 3 - Mentions without descriptions:**
- ✓ Found: "GPS coordinates recorded" but no accuracy specs
  → Extract: P-IMP-003 (GPS recording protocol, implicit - mentioned_undocumented)

**Result:** 3 explicit methods → scan finds 1 implicit method, 3 implicit protocols

This is typical. Explicit items are starting point for implicit scanning.
```

---

## Part 11: Implementation Priority

### Immediate (before next extraction run):

1. **Fix 1:** Integrate implicit RDMAP into main workflow with Phase A/Phase B structure
2. **Fix 2:** Add explicit iteration instructions ("For EACH section, run 4-pattern scan")
3. **Fix 5:** Elevate priority level (HIGH-PRIORITY marker)
4. **Fix 8:** Add worked example showing systematic implicit scan

### Medium-term (next prompt revision):

5. **Fix 3:** Replace checkbox with quality gate requiring scan evidence
6. **Fix 4:** Reframe from transparency metadata to primary content
7. **Fix 6:** Move recognition patterns to main prompt

### Long-term (structural improvements):

8. **Fix 7:** Add mid-section checkpoints with implicit extraction ratios

---

## Part 12: Testing the Fixes

### Validation Criteria

After implementing fixes, re-extract Sobotkova et al. 2023 and verify:

**Success indicators:**
- [ ] Implicit RDMAP items > 0 (10-20 expected)
- [ ] Implicit RDMAP ratio 20-40% of total RDMAP items
- [ ] Extraction notes document implicit RDMAP scan methodology
- [ ] Examples of all 4 recognition patterns found:
  - [ ] Mentioned procedure (e.g., "assigned maps" without allocation method)
  - [ ] Effects implying causes (e.g., performance threshold → monitoring)
  - [ ] Mentions without descriptions (e.g., "GPS used" without specs)
  - [ ] Strategic positioning (e.g., comparative framing without explicit design)

**Failure indicators:**
- Implicit RDMAP items = 0
- All RDMAP marked as "explicit"
- No implicit scan documented in extraction_notes

**Specific items expected from Sobotkova paper:**
1. Map assignment protocol (implicit - "students assigned tiles" but method not described)
2. Load monitoring protocol (implicit - threshold detection implies monitoring)
3. QA method (implicit - "quality-checked" mentioned without procedure)
4. GPS accuracy protocol (implicit - coordinates recorded but accuracy not specified)
5. Volunteer training protocol (implicit - training mentioned but content not described)
6. Comparative positioning design (implicit - paper compares to ML without stating as design objective)

---

## Summary: Root Cause Diagnosis

**Why implicit arguments succeed:**
- ✅ Integrated into mandatory workflow step
- ✅ Explicit iteration instruction ("For EACH core claim")
- ✅ Quality gate requiring scan evidence
- ✅ HIGH-PRIORITY framing
- ✅ 100 lines of guidance in main prompt

**Why implicit RDMAP fails:**
- ❌ NOT integrated into workflow (buried in sourcing section)
- ❌ No iteration instruction ("For each section, scan for...")
- ❌ Checkbox quality check (no scan evidence required)
- ❌ Transparency framing (optional metadata, not primary content)
- ❌ 40 lines in main prompt, guidance delegated to external references

**The fix:** Mirror the implicit argument extraction structure for implicit RDMAP. Make it a mandatory, high-priority workflow step with explicit iteration instructions and quality gates.

---

**Version:** 1.0
**Date:** 2025-10-28
**Status:** Diagnostic complete, fixes proposed
**Next:** Implement Fixes 1, 2, 5, 8 before next extraction run
