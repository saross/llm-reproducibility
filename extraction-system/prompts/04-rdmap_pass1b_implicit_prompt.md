# RDMAP Extraction Prompt - PASS 1b: Implicit RDMAP Scanning v2.5

**Version:** 2.5 Pass 1b
**Last Updated:** 2025-10-28
**Workflow Stage:** Pass 1b of 4 - Implicit RDMAP extraction following explicit extraction
**Skill Context:** This prompt is part of the research-assessor skill
**Purpose:** Systematically scan for RDMAP items that are mentioned but undocumented, or inferred from Results/Discussion

---

## Your Task

You have already extracted **explicit RDMAP items** (documented in Methods section). Now systematically scan for **implicit RDMAP items**: strategic decisions, methods, and protocols that are:

1. **Mentioned but not documented** - Procedures referenced without description
2. **Inferred from results** - Effects implying methodological causes
3. **Operationally necessary but undocumented** - Tools/processes mentioned without specifications
4. **Strategic positioning without explicit statement** - Design choices apparent from analysis focus

**Input:** JSON extraction document with explicit RDMAP already populated

**Your responsibility:** Add implicit RDMAP items to existing arrays:
- `research_designs` (add items with `design_status = "implicit"`)
- `methods` (add items with `method_status = "implicit"`)
- `protocols` (add items with `protocol_status = "implicit"`)

**Leave untouched:**
- Existing explicit RDMAP items
- `evidence`, `claims`, `implicit_arguments` arrays

**Output:** Same JSON document with implicit RDMAP items added

---

## 🚨 CRITICAL: Why This Pass Matters

**Implicit RDMAP items are PRIMARY CONTENT with equal priority to explicit RDMAP items.**

These are not optional "transparency metadata"—they are core extraction targets. Many papers mention procedures without documenting them, or imply methods through results. These undocumented procedures are assessment-critical because they:

- **Transparency gaps:** Reveal what methodological information is missing from Methods documentation
- **Reproducibility barriers:** Identify procedures mentioned but cannot be replicated due to missing detail
- **Credibility concerns:** Highlight undocumented decisions affecting results without documented rationale
- **Assessment foundation:** Enable comparison between what WAS documented and what SHOULD BE documented

**Do not skip implicit scanning** because Methods section exists. Implicit items are found OUTSIDE Methods (Results/Discussion mentions without procedures).

**Expected outcome:** Most empirical papers have 20-40% implicit RDMAP items. Finding zero suggests either exceptional documentation (rare) or incomplete scanning (common).

---

## Systematic Scanning Process

For EACH major section (Abstract, Introduction, Methods, Results, Discussion), run systematic 4-pattern scans for each RDMAP tier.

### Step 1: Scan for Implicit Research Designs

**Pattern 1 - Mentioned Strategic Decision:**
- Question: "Are strategic decisions or frameworks referenced but not explained?"
- Look for: Framework names without rationale, approaches mentioned without justification

**Pattern 2 - Effects Implying Design Causes:**
- Question: "Do outcomes or comparisons suggest unstated design choices?"
- Look for: Systematic comparisons throughout paper but design objective never stated

**Pattern 3 - Frameworks Without Specification:**
- Question: "Are theoretical frameworks or methodological traditions referenced but not described?"
- Look for: "Building on previous work," "Following established approaches" without specifying what

**Pattern 4 - Strategic Positioning Without Explicit Statement:**
- Question: "Does paper position study relative to alternatives without stating this as design objective?"
- Look for: Discussion positioning (thresholds, boundaries, baselines) without design rationale in Methods

**For each implicit design found:**
- Extract `trigger_text` array (verbatim passages from paper implying design choice)
- Record `trigger_locations` (parallel array with section/page/paragraph for each trigger)
- Set `design_status = "implicit"`
- Write `inference_reasoning` (explain how triggers imply this strategic decision)
- Populate `implicit_metadata`:
  - `basis`: "mentioned_undocumented" OR "inferred_from_results"
  - `transparency_gap`: What design information is missing
  - `assessability_impact`: How missing documentation affects assessment
  - `reconstruction_confidence`: "low" | "medium" | "high"

---

### Step 2: Scan for Implicit Methods

**Pattern 1 - Procedure Mentioned Without Description:**
- Question: "Are methodological approaches mentioned but not described?"
- Look for: "We quality-checked," "maps were selected," "performance was monitored" without methodology

**Pattern 2 - Results Implying Unstated Methodological Approach:**
- Question: "Do results or outcomes suggest methodological approaches not documented?"
- Look for: Error taxonomies, performance thresholds, quality metrics implying undocumented methods

**Pattern 3 - Tools/Approaches Referenced Without Specification:**
- Question: "Are analytical tools or approaches mentioned without methodological detail?"
- Look for: "Statistical analysis," "thematic coding," "spatial analysis" without specifying method

**Pattern 4 - Analysis Mentioned Without Method Documentation:**
- Question: "Are analytical procedures mentioned in Results but not documented in Methods?"
- Look for: Results describing categorisation, comparison, or evaluation without method specification

**For each implicit method found:**
- Extract `trigger_text` array (passages mentioning or implying method)
- Record `trigger_locations`
- Set `method_status = "implicit"`
- Write `inference_reasoning`
- Populate `implicit_metadata` (same structure as designs)

---

### Step 3: Scan for Implicit Protocols

**Pattern 1 - Operational Procedure Mentioned Without Details:**
- Question: "Are operational procedures referenced but not described?"
- Look for: "Maps were assigned," "data was exported," "devices were configured" without protocol

**Pattern 2 - Effects Implying Undocumented Operational Protocols:**
- Question: "Do operational effects suggest protocols not documented?"
- Look for: Performance thresholds suggesting monitoring, error rates suggesting QA, timing suggesting workflow protocols

**Pattern 3 - Equipment/Tools Mentioned Without Specifications:**
- Question: "Are tools, devices, or infrastructure mentioned without operational detail?"
- Look for: "Server configured," "devices used," "GPS recorded" without specifications

**Pattern 4 - Data Processing Mentioned Without Procedure:**
- Question: "Is data processing, cleaning, or transformation mentioned without protocol?"
- Look for: "Coordinates extracted," "errors corrected," "data aggregated" without procedure description

**For each implicit protocol found:**
- Extract `trigger_text` array (passages mentioning or implying protocol)
- Record `trigger_locations`
- Set `protocol_status = "implicit"`
- Write `inference_reasoning`
- Populate `implicit_metadata` (same structure as designs and methods)
- Record `procedure_steps` if inferable from context (even if incomplete)

---

## Quick Reference: 4-Pattern Implicit Recognition

Use these patterns to identify implicit RDMAP during systematic scanning:

**Pattern 1 - Mentioned Procedure Without Description:**
- **Question:** "Is procedure referenced but not described?"
- **Look for:** Verbs without methods—"cleaned," "validated," "checked," "assigned," "exported," "monitored"
- **Example:** "Data were cleaned prior to analysis" but no cleaning procedure described
- **Extract as:** Implicit method/protocol (basis: mentioned_undocumented)

**Pattern 2 - Effects Implying Undocumented Causes:**
- **Question:** "Do results/outcomes suggest procedures not documented in Methods?"
- **Look for:** Thresholds detected → monitoring, error rates → QA, accuracy metrics → validation
- **Example:** "Performance degraded after 2,500 records" implies monitoring but method not documented
- **Extract as:** Implicit protocol (basis: inferred_from_results)

**Pattern 3 - Tools/Processes Mentioned Without Specifications:**
- **Question:** "Are tools, equipment, or processes mentioned without operational detail?"
- **Look for:** "GPS used" (no specs), "server configured" (no details), "students assigned" (no method)
- **Example:** "Students assigned specific map tiles" but assignment procedure not described
- **Extract as:** Implicit protocol (basis: mentioned_undocumented)

**Pattern 4 - Strategic Positioning Without Explicit Statement:**
- **Question:** "Does paper position work relative to alternatives without stating as design objective?"
- **Look for:** Systematic comparisons in Discussion without design rationale in Methods/Introduction
- **Example:** Compares to ML alternatives throughout but doesn't state comparative evaluation as design goal
- **Extract as:** Implicit research design (basis: inferred_from_results)

**For detailed examples and troubleshooting:**
→ See `references/extraction-fundamentals.md` (Implicit RDMAP section, lines 68-158)

---

## Sourcing Requirements for Implicit RDMAP

**Every implicit RDMAP item MUST have:**

1. **trigger_text** (array of strings)
   - Verbatim passages from paper that together trigger your inference
   - Minimum 1 trigger, typically 2-4 triggers that together build the case
   - Each trigger must be exact quote from paper

2. **trigger_locations** (array of objects, parallel to trigger_text)
   - For each trigger passage, record: `{"section": "...", "subsection": "...", "page": N, "start_paragraph": N, "end_paragraph": N}`
   - Enables reader to find and verify each trigger

3. **inference_reasoning** (string)
   - Explain how trigger passages together imply this RDMAP item
   - What information is present? What is missing? Why do you infer this item exists?
   - Be explicit about your reasoning chain

4. **implicit_metadata** (object)
   - `basis`: Why you're inferring this exists
     - "mentioned_undocumented" - Procedure referenced but not described
     - "inferred_from_results" - Results/outcomes imply methodological cause
   - `transparency_gap`: What information is missing that should be documented
   - `assessability_impact`: How does missing information affect assessment?
   - `reconstruction_confidence`: "low" | "medium" | "high" - How confident reconstruction is possible

**Anti-hallucination discipline:**
- No inference without textual trigger
- No trigger without exact location
- No implicit item without explaining reasoning

---

## Liberal Extraction Philosophy

**Pass 1b still follows liberal extraction:**

- When uncertain whether something qualifies as implicit RDMAP: **INCLUDE IT**
- When uncertain about tier (design vs method vs protocol): **INCLUDE IT** (Pass 2 will rationalize)
- When uncertain about confidence level: **Include it with "low" confidence**
- Better to over-extract and consolidate in Pass 2 than miss assessment-critical gaps

**Red flags indicating conservative extraction:**
- Zero implicit RDMAP items found (very unusual)
- Only obvious/confident items included
- Skipping sections because "nothing seems implicit"

**Expected:** Pass 2 will consolidate 15-20% of Pass 1 items. If Pass 2 finds nothing to consolidate, Pass 1 was too conservative.

---

## Quality Checkpoints

Before completing extraction, verify:

- [ ] Completed 4-pattern scan for EACH RDMAP tier (designs, methods, protocols) across EACH major section (Abstract, Intro, Methods, Results, Discussion)
- [ ] Documented scan methodology in extraction_notes for each section scanned, OR extracted implicit items found
- [ ] All implicit RDMAP items have complete sourcing: trigger_text, trigger_locations, inference_reasoning, implicit_metadata
- [ ] No duplication with explicit RDMAP items (compared against existing extraction)
- [ ] **If zero implicit RDMAP found across all sections:** extraction_notes explains systematic scan methodology and why none found (e.g., "Exceptionally thorough Methods section with all strategic decisions, methods, and protocols documented with procedural details. Systematic Results/Discussion scan found no procedure mentions without descriptions.")

**⚠️ Most papers have 20-40% implicit RDMAP.** Finding zero suggests either exceptional documentation (rare) or incomplete scanning (common). Document scan methodology to demonstrate which.

---

## Common Implicit RDMAP Examples

**Implicit Designs:**
- Paper systematically compares to alternative approaches throughout Discussion, but Introduction doesn't state comparative evaluation as design objective
- Paper establishes threshold ranges (e.g., "optimal for 10,000-60,000 records"), but doesn't state threshold determination was a design goal
- Paper references methodological tradition (e.g., "following citizen science principles") without specifying which principles or why chosen

**Implicit Methods:**
- Results mention "quality assurance by project staff" but Methods doesn't describe QA methodology
- Error taxonomy presented in Results (false positives, false negatives, classification errors) but error categorisation method not documented
- Performance monitoring implied by specific thresholds (e.g., "degraded after 2,500 records") but monitoring method not described

**Implicit Protocols:**
- Results mention "participants assigned to specific maps" but assignment protocol not described
- Methods mention "data exported and aggregated" but export/aggregation procedure not specified
- Infrastructure mentioned (e.g., "server configured") but configuration protocol not documented
- Data cleaning mentioned (e.g., "errors corrected," "coordinates re-extracted") but correction procedure not specified

---

## Integration with Explicit RDMAP

**Use already-extracted explicit RDMAP as seed list:**

1. For each explicit method → scan for undocumented protocols realising that method
2. For each explicit design → scan for unstated strategic positioning related to that design
3. For each explicit protocol → scan for parameter specifications or operational details mentioned elsewhere

**Avoid duplication:**
- If explicit item already captures the information, don't extract as implicit
- Implicit items reveal NEW information not in explicit extraction
- Use cross-references (`implements_methods`, `implements_designs`) to link implicit items to explicit items

---

## Output Format

**Return the same JSON document with implicit RDMAP items ADDED to existing arrays.**

Preserve all existing content. Only add new items with:
- `design_id` / `method_id` / `protocol_id` following existing numbering (use IMP prefix: "RD-IMP-001", "M-IMP-001", "P-IMP-001")
- `*_status = "implicit"` for all new items
- Complete sourcing (trigger_text, trigger_locations, inference_reasoning, implicit_metadata)

**Update extraction_notes:**
- Increment pass number if tracking
- Document implicit scan methodology
- Note implicit RDMAP ratio: `(implicit items / total RDMAP items) × 100%`
- Document any unusual findings (e.g., zero implicit items and why)

---

## Reference Materials

**For detailed implicit RDMAP recognition patterns:**
→ See `references/extraction-fundamentals.md` (Section: Implicit RDMAP Extraction Patterns)

**For schema field definitions:**
→ See `references/schema/schema-guide.md`

**For tier assignment guidance:**
→ See `references/checklists/tier-assignment-guide.md`

---

## Example: Worked Implicit RDMAP Scan

**Scenario:** Paper on crowdsourced map digitisation. Explicit extraction found:
- 2 research designs (explicit)
- 4 methods (explicit)
- 6 protocols (explicit)

**Now running implicit scan:**

**Results section states:** "Performance would degrade once approximately 3,000-6,000 records had been created."

→ Implicit Protocol: "Performance load monitoring protocol"
- trigger_text: ["Performance would degrade once approximately 3,000-6,000 records had been created"]
- basis: "inferred_from_results" (specific threshold implies monitoring)
- transparency_gap: "Monitoring methodology not documented - unknown how performance was measured, frequency of monitoring, or criteria for detecting degradation"

**Results section states:** "Finally, project staff reviewed randomly selected digitisation work completed by volunteers to characterise errors."

→ Implicit Method: "Quality assurance methodology"
- trigger_text: ["project staff reviewed randomly selected digitisation work completed by volunteers to characterise errors"]
- basis: "mentioned_undocumented" (QA mentioned but method not described)
- transparency_gap: "QA methodology not specified - unknown review criteria, error definitions, inter-rater reliability, or systematic procedure"

**Discussion systematically compares approach to ML alternatives with threshold calculations, but Introduction doesn't state ML comparison as design objective.**

→ Implicit Design: "Comparative positioning relative to machine learning approaches"
- trigger_text: ["It complements Machine Learning and other automated approaches...", "A minimum threshold for automation can be extrapolated..."]
- basis: "inferred_from_results" (systematic positioning throughout but not stated as design goal)
- transparency_gap: "ML comparison design objective not stated in Methods - unknown if pre-planned comparison or post-hoc positioning"

**Result:** 3 implicit items added. New totals: 2 designs + 1 implicit = 3 designs, 4 methods + 1 implicit = 5 methods, 6 protocols + 1 implicit = 7 protocols. Implicit ratio: 3/15 = 20% (typical range).

---

**End of Prompt 04**
