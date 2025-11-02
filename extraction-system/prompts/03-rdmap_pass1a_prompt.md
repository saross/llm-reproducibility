# RDMAP Extraction Prompt - PASS 1: Explicit Extraction v2.5

**Version:** 2.5 Pass 1
**Last Updated:** 2025-10-28
**Workflow Stage:** Pass 1 of 4 - Explicit RDMAP extraction (implicit extraction in Pass 1b)
**Skill Context:** This prompt is part of the research-assessor skill
**Schema Update:** Added mandatory sourcing to prevent hallucination

---

## Your Task

Extract **explicit RDMAP items** from research paper Methods/Approach sections: strategic decisions, methods, and protocols that are documented with procedural details.

**This is Pass 1: Liberal Extraction** - when uncertain about tier assignment or boundaries, err on the side of inclusion. Pass 2 will consolidate and rationalise.

**Input:** JSON extraction document (schema v2.5)
- May be blank template (starting fresh)
- May be partially populated (if claims/evidence already extracted)

**Your responsibility:** Populate these arrays with EXPLICIT items:
- `research_designs` (set `design_status = "explicit"`)
- `methods` (set `method_status = "explicit"`)
- `protocols` (set `protocol_status = "explicit"`)

**Leave untouched:**
- `evidence`, `claims`, `implicit_arguments` (extracted separately)
- Any other arrays already populated

**What you're extracting:**
- **Research Designs** - Strategic decisions about WHY research was framed this way
- **Methods** - Tactical approaches about WHAT was done at high level
- **Protocols** - Operational procedures about HOW specifically it was done

**Note:** Implicit RDMAP items (mentioned but undocumented, or inferred from Results/Discussion) will be extracted in Pass 1b (separate prompt). This pass focuses solely on documented methodology in Methods section.

**Output:** Same JSON document with explicit RDMAP arrays populated

---

## Section Handling

**Extract section-by-section using flexible grouping based on the paper's structure.**

### Default Grouping

1. **Abstract + following section** - Combined as one unit (save to JSON after)
2. **Middle sections** - Each major section as one unit, combining subsections (save after each)
3. **Conclusion + preceding section** - Combined as one unit (save to JSON after)

**Adapt to what the paper gives you.** If Methods is called "Approach" or a section is thematic like "Landscape and Memory," treat it as a middle section.

### Section Size Limits

**Target ~1000 words per section. Maximum 1500 words.**

If any section exceeds 1500 words, divide into roughly equal chunks using natural breaks:
1. Subsection boundaries (3.1, 3.2, etc.) closest to midpoint/thirds
2. Topic shifts or conceptual paragraph boundaries closest to equal division
3. Any paragraph boundary closest to equal chunk sizes

**Aim for 1000 ± 500 words per chunk** - never >1500 words.

### Papers Without Formal Sections

If the paper lacks section headings:
1. **Abstract** - Usually labelled even without sections (combine with next ~1000 words)
2. **Middle content** - Process in ~1000-word chunks using paragraph/thematic boundaries
3. **Conclusion** - Recognisable by concluding language (combine with previous ~1000 words)

If no Abstract/Conclusion identifiable: Process entire paper in ~1000-word chunks.

### Tracking Section Decisions

Document your section grouping decisions in `extraction_notes.section_extracted` after each section group:
- Which sections were combined
- **Word count of the section/chunk**
- Where splits occurred and why (word count, break type used)
- Any unusual structural features

This enables prompt refinement and extraction performance analysis.

---

## 🚨 CRITICAL: Verbatim Quote Requirements

**Before extracting any item:**

Read if uncertain: `references/verbatim-quote-requirements.md`

**Non-negotiable rules for all `verbatim_quote` fields:**

1. **Complete sentences with full context** - Extract whole grammatical units that preserve the meaning and context of the RDMAP item
   - ✓ Include enough surrounding context to make the methodological description understandable
   - ✓ If a sentence references "this approach" or "these methods", include the prior sentence for clarity
   - ✗ Never extract sentence fragments or clauses without their main clause
   - ✗ Never truncate sentences mid-way that lose essential methodological context

2. **Exact text only** - Copy-paste from paper, never paraphrase or reconstruct from memory
   - ✓ Whitespace normalisation acceptable (PDF conversion artefacts)
   - ✓ Line breaks within sentences can be removed
   - ✗ Never change words, add words, or rearrange text
   - ✗ Never paraphrase or summarise

3. **Verify before committing** - Ensure exact quote exists in paper before adding to JSON
   - Use find/search to locate the exact text string
   - If text can't be found with search, quote is wrong

4. **Single source only** - Never synthesise quotes from multiple locations
   - Each verbatim_quote must come from ONE contiguous passage
   - If combining information from multiple locations, use multiple RDMAP items

**Context completeness examples for RDMAP:**

❌ **Incomplete (missing methodological context):**
> "This approach was used to ensure reliability."

✓ **Complete (includes method context):**
> "Systematic transect surveys at 20m intervals were conducted across the study area. This approach was used to ensure reliability and comparability with the 2015 baseline survey."

❌ **Incomplete (fragmented protocol):**
> "using the ATLAS.ti software package"

✓ **Complete (full protocol sentence):**
> "Qualitative coding was performed using the ATLAS.ti software package (v9.1) with a grounded theory approach to identify emergent themes."

**Self-check:** "Can I find this EXACT text string in the paper with simple search?"
- If YES → Extract it
- If NO → Quote is wrong; fix it or skip (will be captured in Pass 1b if implicit)

**Context self-check:** "Does this quote make sense on its own without needing the previous sentence?"
- If YES → Context sufficient
- If NO → Expand quote to include necessary methodological context

⚠️ **Failure to follow these rules causes 40-50% validation failures in Pass 3.**
⚠️ **Incomplete quotes (missing context) identified as top systemic issue in cross-paper error analysis (29 instances, 2 papers).**

---

## 🚨 CRITICAL: Explicit RDMAP Sourcing

**READ FIRST:** `references/extraction-fundamentals.md`

The fundamentals document covers universal sourcing requirements that apply to all object types. **RDMAP items have the same sourcing discipline as Evidence and Claims.**

### Explicit RDMAP Definition

**EXPLICIT = Documented in Methods section with procedural details**
- Strategic decisions described with rationale
- Methods described with approach specifications
- Protocols described with operational steps
- Extract with `verbatim_quote` field from Methods/Approach section
- Status: `design_status`, `method_status`, or `protocol_status` = `"explicit"`

**Decision rule for this pass:**
```
Is this RDMAP item described in the Methods section with procedural details?
├─ YES → Extract as explicit (this pass)
└─ NO → Skip (will be extracted in Pass 1b if implicit)
```

**For complete sourcing fundamentals:** → `references/extraction-fundamentals.md`
**For detailed verification procedures:** → `references/verification-procedures.md`

---

## Quality Checklist for Pass 1

Use this checklist as your roadmap. Before finalising:

- [ ] All explicit research designs extracted (questions, hypotheses, study designs, frameworks)
- [ ] All explicit methods extracted (data collection, sampling, analysis approaches)
- [ ] All explicit protocols extracted (specific procedures, tools, parameters, configurations)
- [ ] Tier assignments marked (even if uncertain)
- [ ] Status fields set to "explicit" for all RDMAP items
- [ ] All items have verbatim_quote populated
- [ ] Expected missing information documented for each item
- [ ] Liberal extraction applied (when uncertain, include it)

---

## RDMAP Tier Hierarchy

Research Designs → Methods → Protocols (strategic → tactical → operational)

**Research Designs** are strategic decisions answering "WHY this approach?"
- Research questions and hypotheses
- Study designs (comparative evaluation, case study, experimental design)
- Theoretical frameworks guiding the research
- Sampling frames (WHAT to sample from)

**Methods** are tactical approaches answering "WHAT was done?"
- Data collection approaches (observation, measurement, recording)
- Sampling strategies (HOW to sample)
- Analysis methods (statistical tests, qualitative coding, spatial analysis)
- Validation and quality control approaches

**Protocols** are operational procedures answering "HOW SPECIFICALLY was it done?"
- Step-by-step procedures
- Tool configurations and parameters
- Recording and data capture procedures
- Processing and transformation procedures

**See:** `references/checklists/tier-assignment-guide.md` for complete classification guidance

---

## Liberal Extraction Philosophy

This is Pass 1: **LIBERAL EXTRACTION**

### Liberal Extraction Mental Model

**Pass 1 job:** CAPTURE (comprehensively)
**Pass 2 job:** CONSOLIDATE (rationally)

**Active rules during Pass 1:**
- ✓ When uncertain: EXTRACT IT
- ✓ When granular: KEEP IT SEPARATE
- ✓ When related items: DON'T CONSOLIDATE YET

**Never think during Pass 1:**
- ✗ "This seems too detailed for final output"
- ✗ "These should probably merge"
- ✗ "I'm over-extracting"

**Remember:** Pass 2 can merge. Pass 1 cannot recover missed items.

### Application to RDMAP

**When uncertain:**
- About tier (design vs method vs protocol): **INCLUDE IT** (Pass 2 will rationalise)
- About boundaries (one item or two): **EXTRACT BOTH** (Pass 2 will consolidate)
- About whether it qualifies as RDMAP: **INCLUDE IT** (Pass 2 will review)

**Accept 40-50% over-extraction:**
- Pass 1 should over-capture
- Pass 2 consolidates and rationalises
- Better to extract too much than miss assessment-critical information

**When to extract "high-level" or "obvious" designs:**
- "Comparative evaluation of X vs Y" feels obvious? → EXTRACT IT (it's a strategic choice)
- "Case study to demonstrate Z" feels obvious? → EXTRACT IT (case study is a design decision)
- Meta-level framing that shapes entire paper → EXTRACT IT (these are Research Designs)

---

## Extraction Workflow

### STEP 0: MANDATORY Pre-Extraction (DO THIS FIRST)

Before extraction begins, you MUST:

1. **Read extraction fundamentals:**
   - File: `references/extraction-fundamentals.md`
   - Focus: Internalise the sourcing test: "Can I point to exact text?"

2. **Acknowledge understanding:**
   - State: "I have read extraction fundamentals and understand the sourcing discipline"

3. **Only then proceed to extraction**

**WITHOUT completing Step 0, extraction will fail sourcing requirements.**

---

## STEP 1: Pre-Scan for Research Designs

Before extracting RDMAP, quickly scan Abstract, Introduction, Background, and Methods/Approach sections for design elements:
- Mark decision language ("chose," "selected," "because")
- Mark frameworks ("guided by," "framework," "informed by")
- Mark meta-level framing (comparative evaluation, case study rationale, efficiency hypothesis)

See: `references/research-design-operational-guide.md` for detailed pre-scan checklist.

⚠️ **Pre-Scan Mindset:** If a design element feels "too obvious" or "everyone knows this" → Mark it anyway. Meta-level designs (comparative evaluation, case study rationale) feel obvious because they frame the entire paper - that's exactly why they're Research Designs.

---

## STEP 2: Extract Explicit Research Designs

⚠️ **Literature Review Warning:** Don't extract Research Designs from descriptions of PRIOR work.
- If verbatim quote says "Smith et al. employed..." → Not current paper's design
- If quote says "We build on comparative approaches..." → Check: Do they explain WHY they chose it for THIS study?
- Test: Does this explain a strategic choice the AUTHORS made, or describe what others did?

**Scan Abstract, Introduction, Background, and Methods/Approach sections for documented strategic decisions:**

**Look for design language:**
- Decision markers: "chose," "selected," "opted for," "decision to"
- Rationale markers: "because," "rationale," "reasoning"
- Purpose markers: "aimed to," "sought to," "designed to"
- Framework markers: "framework," "guided by," "informed by"
- Comparison markers: "compared," "evaluated," "tested whether"

See `references/checklists/tier-assignment-guide.md` for full patterns.

**For each explicit design found:**
- Extract complete strategic decision with rationale
- Set `design_status = "explicit"`
- Extract `verbatim_quote` from paper
- Classify reasoning approach for each
- **Identify each distinct strategic decision point** (separate rationales = separate designs)
- Extract theoretical frameworks as Research Designs

**Meta-level framing:** Papers often have strategic designs that frame entire research:
- "Comparative evaluation of X" → Design (comparison AS strategic choice)
- "Case study to demonstrate Y" → Design (case study AS deliberate decision)

Extract these even though they seem "obvious" - they're strategic choices requiring independent justification.

**Systematically check:** For each major section, ask: questions stated? hypotheses stated? frameworks referenced? design rationale explained? See `references/research-design-operational-guide.md` for complete checklist.

**Liberal extraction:** Include "high-level" design elements - critical for transparency assessment.

---

## STEP 3: Extract Explicit Methods

**Scan Methods/Approach section for documented tactical approaches:**

**Look for method types:**
- Data collection approaches (recording, measurement, observation)
- Sampling strategies (systematic, random, purposive, stratified)
- Analysis methods (statistical tests, qualitative coding, spatial analysis)
- Quality control approaches (validation, verification, cross-checking)

**For each explicit method found:**
- Extract high-level approach with context
- Set `method_status = "explicit"`
- Extract `verbatim_quote` from Methods section
- Document expected missing information
- When uncertain about tier: **INCLUDE IT** (Pass 2 will consolidate)

**Systematically check:** For each subsection of Methods, ask: data collection described? sampling described? analysis approach described? quality control described?

**Liberal extraction:** Include borderline items (might be method or protocol) - Pass 2 will rationalise tier assignments.

---

## STEP 4: Extract Explicit Protocols

**Scan Methods/Approach section for documented operational procedures:**

**Look for protocol types:**
- Recording procedures (how data was captured)
- Measurement procedures (how observations were made)
- Processing procedures (how data was cleaned, transformed, aggregated)
- Validation procedures (how quality was checked)
- Configuration procedures (how tools/equipment were set up)

**For each explicit protocol found:**
- Extract specific operational procedure
- Set `protocol_status = "explicit"`
- Extract `verbatim_quote` from Methods section
- Record procedure steps if specified
- Document parameters if specified
- Note expected missing information

**Protocol characteristics:**
- More specific than methods (implementation detail)
- Often includes parameters, settings, or step sequences
- Answers "how specifically" rather than "what approach"

**Systematically check:** For each method extracted, ask: are implementation procedures described? Are tool configurations specified? Are parameters documented?

**Liberal extraction:** Include procedural details even if incomplete - captures what WAS documented for transparency assessment.

---

## Relationship Mapping

**After extracting RDMAP items, map relationships:**

**Designs → Methods:**
- Which methods implement/realise which research designs?
- Use `implements_designs` field in methods

**Methods → Protocols:**
- Which protocols implement/realise which methods?
- Use `implements_methods` field in protocols

**Protocols → Methods:**
- Reverse reference from protocol perspective
- Use `realized_through_protocols` field in methods

**Cross-tier connections:**
- Research Designs may directly connect to protocols
- Some designs validate specific claims
- Document these relationships in appropriate fields

**Liberal approach:** When uncertain about relationships, include them. Pass 2 will review.

---

## Expected Missing Information

**For EVERY RDMAP item, document what's missing:**

This is assessment-critical. Use `expected_information_missing` arrays to note:

**For Research Designs:**
- Missing rationale or justification
- Alternatives not discussed
- Theoretical framework not specified

**For Methods:**
- Missing procedural details
- Sample size not justified
- Quality control not described

**For Protocols:**
- Parameters not specified
- Tool configurations not documented
- Validation procedures missing

**This information feeds transparency assessment.** Be thorough about documenting gaps.

---

## Output Format

**Return the same JSON document you received, with these arrays populated:**

```json
{
  "schema_version": "2.5",
  "extraction_timestamp": "ISO 8601",
  "extractor": "Claude Sonnet 4.5",

  "research_designs": [design_object],
  "methods": [method_object],
  "protocols": [protocol_object],

  "extraction_notes": {
    "pass": 1,
    "section_extracted": "RDMAP Pass 1: Explicit extraction complete. Implicit extraction pending (Pass 1b).",
    "extraction_strategy": "Liberal explicit RDMAP extraction from Methods/Approach sections...",
    "known_uncertainties": ["List any ambiguities, uncertain tier assignments, or items you're unsure about"]
  }
}
```

**IMPORTANT: Update extraction_notes:**
- Set pass number
- Document extraction strategy
- Note any uncertainties or ambiguities
- Document liberal extraction philosophy applied

---

## Reference Materials

**For detailed RDMAP extraction fundamentals:**
→ See `references/extraction-fundamentals.md` (Explicit RDMAP Extraction section)

**For tier assignment guidance:**
→ See `references/checklists/tier-assignment-guide.md`

**For research design operational guide:**
→ See `references/research-design-operational-guide.md`

**For schema field definitions:**
→ See `references/schema/schema-guide.md`

**For verification procedures:**
→ See `references/verification-procedures.md`

**For implicit RDMAP extraction:**
→ This will be handled in Pass 1b (Prompt 04) after explicit extraction is complete

---

## Examples

See `references/examples/` for:
- Worked RDMAP extraction examples
- Tier assignment examples
- Relationship mapping examples
- Expected missing information examples

---

**End of Prompt 03**
