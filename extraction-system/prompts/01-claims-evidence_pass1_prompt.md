# Claims & Evidence Extraction Prompt - PASS 1: Liberal Extraction v2.5

**Version:** 2.5 Pass 1  
**Last Updated:** 2025-10-21  
**Workflow Stage:** Pass 1 - Liberal extraction with over-capture strategy  
**Update:** Added mandatory sourcing requirements (hallucination prevention)

---

## Your Task

Extract evidence, claims, and implicit arguments from a research paper section. This is **Pass 1: Liberal Extraction** - when uncertain, err on the side of inclusion. Pass 2 will consolidate and refine.

**Input:** JSON extraction document (schema v2.5)
- May be blank template (starting fresh)
- May be partially populated (if RDMAP or other sections already extracted)

**Your responsibility:** Populate these arrays:
- `evidence`
- `claims`
- `implicit_arguments`
- `project_metadata`

**Leave untouched:** 
- `research_designs`, `methods`, `protocols` (RDMAP arrays - extracted separately)
- Any other arrays already populated

**Output:** Same JSON document with evidence/claims/implicit arguments arrays populated

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

**For comprehensive guide:** `references/verbatim-quote-requirements.md`

**Non-negotiable rules for all `verbatim_quote` fields:**

1. **Complete sentences with full context** - Extract whole grammatical units that preserve the meaning and context of the claim/evidence
   - ✓ Include enough surrounding context to make the statement understandable
   - ✓ If a sentence references "this" or "these results", include the prior sentence for clarity
   - ✗ Never extract sentence fragments or clauses without their main clause
   - ✗ Never truncate sentences mid-way that lose essential context

2. **Exact text only** - Copy-paste from paper, never paraphrase or reconstruct
   - ✓ Whitespace normalisation acceptable (PDF conversion artefacts)
   - ✓ Line breaks within sentences can be removed
   - ✗ Never change words, add words, or rearrange text
   - ✗ Never paraphrase or summarise

3. **Verify before committing** - Ensure exact quote exists in paper before adding to JSON
   - Use find/search to locate the exact text string
   - If text can't be found with search, quote is wrong

4. **Single source only** - Never synthesise quotes from multiple locations
   - Each verbatim_quote must come from ONE contiguous passage
   - If combining information from multiple locations, use multiple evidence items

**Context completeness examples:**

❌ **Incomplete (missing context):**
> "These results support the hypothesis."

✓ **Complete (includes context):**
> "Radiocarbon dates from all three trenches cluster in the 12th-13th centuries CE. These results support the hypothesis that the settlement was occupied during the Medieval period."

❌ **Incomplete (fragmented sentence):**
> "significantly higher than control sites"

✓ **Complete (full sentence with context):**
> "Material density at the identified features was significantly higher than control sites (Mann-Whitney U test, p<0.001)."

**Self-check:** "Can I find this EXACT text string in the paper with simple search?"
- If YES → Extract it
- If NO → Quote is wrong; fix it or mark as implicit

**Context self-check:** "Does this quote make sense on its own without needing the previous sentence?"
- If YES → Context sufficient
- If NO → Expand quote to include necessary context

⚠️ **Failure to follow causes 40-50% validation failures in Pass 3.**
⚠️ **Incomplete quotes (missing context) identified as top systemic issue in cross-paper error analysis (29 instances, 2 papers).**

---

## 🚨 CRITICAL: Sourcing Requirements

**For complete fundamentals:** `references/extraction-fundamentals.md`

**MANDATORY for all extractions:**
**EVIDENCE & CLAIMS require:**
- `verbatim_quote` - Exact text from paper stating this content
- Precise location - Section, subsection, paragraph range
- If quote doesn't exist → DO NOT EXTRACT
**IMPLICIT ARGUMENTS require:**
- `trigger_text` array - Verbatim passages that imply (not state) the argument
- `trigger_locations` - Location of each trigger passage
- `inference_reasoning` - Explanation connecting triggers to argument
- If no trigger passages → DO NOT EXTRACT
**Quick test before extracting:**
- Evidence/Claims: "Can I point to the exact sentence that says this?"
- Implicit Arguments: "Can I point to specific passages that together imply this?"
- If NO → DO NOT EXTRACT
**For verification:** `references/verification-procedures.md`

---

## EXTRACTION PHILOSOPHY FOR PASS 1

**When uncertain whether something qualifies as evidence/claim: INCLUDE IT.**

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

### Application

- Better to over-extract and consolidate later than miss important content
- Preserve granularity - we will consolidate in Pass 2 rationalization
- Accept some over-extraction as expected and manageable
- Focus on comprehensive capture, not perfect classification

**You will NOT be penalized for:**
- Extracting too many items (Pass 2 consolidates)
- Being overly granular (Pass 2 lumps related items)
- Including marginal items (Pass 2 filters)

**You WILL be penalized for:**
- Missing important claims or evidence
- Under-extracting due to uncertainty
- Being too conservative
- **Extracting items without proper sourcing (verbatim_quote OR trigger_text)**

---

## Core Extraction Principles

### 1. Evidence vs. Claims Distinction

**EVIDENCE** = Raw observations, measurements, or data requiring minimal interpretation

**CLAIMS** = Assertions that interpret, frame, or generalize from evidence

**Test:** "Does this require expertise to assess or just checking sources?"

**Professional Judgment Boundary:** Statements requiring expertise to assess (e.g., "these maps are accurate") are **CLAIMS** supported by implicit professional judgment, not evidence.

**For complete decision framework with examples, edge cases, and worked examples:**
→ See `references/checklists/evidence-vs-claims-guide.md`

---

### 2. Evidence Must Support Claims

Extract observations only if they support specific claims. Context that doesn't support claims → `project_metadata`.

**Test question:** "Would removing this item cause a claim to lose evidential support?"
- If YES → Evidence
- If NO → Project metadata (timeline, location, resources, track record)

**Track Record = Context, Not Evidence:** "Method X worked before" justifies attempting the approach but doesn't support current project claims. Move to `project_metadata`, not evidence.

---

### 3. Four-Level Hierarchy (Claims)

**CORE claims** (typically 5-10 per paper)
- Main thesis, key findings, primary contributions
- What authors want you to remember
- Top of argument structure

**INTERMEDIATE claims** (vary by paper)
- Support core claims
- May have their own supporting claims
- Middle layers of argument

**SUPPORTING claims** 
- Directly supported by evidence
- Bottom layer of claim hierarchy
- Connect evidence to higher claims

**EVIDENCE**
- Observations, measurements, data
- Support claims but aren't claims themselves

---

### 4. Implicit Arguments (HIGH-PRIORITY claims only)

**Extract implicit arguments for all core claims (REQUIRED systematic search) and key intermediate claims (as applicable).**

**Four types:**

**Type 1: Logical Implications** - Unstated steps in reasoning chain
- IF the explicit claims are true, THEN X must also be true
- Example: "Method is accurate" implies "Equipment was calibrated"

**Type 2: Unstated Assumptions** - Prerequisites assumed without acknowledgment
- Authors assume X is true without stating or justifying it
- Example: Spatial analysis assumes GPS accuracy adequate

**Type 3: Bridging Claims** - Missing links between evidence and conclusions
- Evidence → ??? → Claim (what's the ???)
- Example: "Complete data" → "High quality data" needs bridging argument about what makes data "high quality"

**Type 4: Disciplinary Assumptions** - Field-specific taken-for-granted knowledge
- Domain experts assume X without stating it
- May be invisible to practitioners but crucial for outsiders
- Example: Archaeologists assume surface visibility relates to artifact presence

---

### 5. Expected Information Checklists

**For comprehensive checklists by claim type and domain:**  
→ See `references/checklists/expected-information.md`

**Flag missing expected information** in `expected_information_missing` field.

**Quick examples:** Method specified? Error margins? Sample size? Comparison basis? Causal mechanisms? Alternative explanations?

### 6. Literary/Historical Source Papers: Evidence Extraction Adaptation

**When analysing ancient/historical texts:**

**DECISION RULE:** "When paper references primary source text → create evidence item"

**Extraction steps:**

1. **Scan for all primary source citations:**
   - Citation patterns: Il. X.Y, Hdt. X.Y, Gen X:Y, Republic 510b
   - Include both extensively analysed passages AND inline references
   - Capture paraphrases with citations

2. **Create evidence item for each citation:**
   - `evidence_type`: "primary_source_textual"
   - `source`: Use author's citation format ("Homer, Iliad 2.802-6" or "Il. 2.802-6")
   - `verbatim_quote`: Extract author's English translation/paraphrase from body text
   - `notes`: Document if bundled with other citations

3. **Handle bundled citations** (e.g., "See Il. 2.802-6, 4.433-38"):
   - Create separate evidence items for each citation
   - Cross-reference via `related_evidence` array

**Target:** 20-30 evidence items for literary/philological papers (vs 40-60 empirical)

**For comprehensive guidance:**
→ `references/checklists/expected-information.md` (Literary Studies / Philology section)
  - Citation format patterns by discipline (Greco-Roman, Biblical, Medieval, Philosophical, Legal)
  - Evidence type classification (primary vs secondary textual, archaeological, inscriptional)
  - Boundary cases (what to include/exclude)
  - Bundled citation handling details
  - Post-extraction verification protocol with grep patterns

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

### STEP 1: Initial Scan
- Read abstract and conclusion
- Identify 5-10 CORE claims (main thesis)
- Note paper's structure
- Check for any COI declarations

### STEP 2: Section-by-Section Extraction

For each section:

1. **Identify Evidence First**
   - Look for observations, measurements, data points
   - Check for declared uncertainty (ranges, errors, hedging)
   - Note missing uncertainty that should be present
   - Extract source and confidence information
   - Apply evidence test: does it support a claim?
   - **When uncertain: INCLUDE IT**

2. **Then Identify Claims**
   - Look for assertions that interpret/frame evidence
   - Classify by role (core/intermediate/supporting)
   - Identify what evidence supports each claim
   - Check for composed claims (bundles of evidence + framing)
   - Watch for single-case generalizations
   - **When uncertain: INCLUDE IT**

3. **Extract Implicit Arguments** (REQUIRED systematic search for all core claims)

   For EACH core claim, run the 4-type checklist:

   **Type 1 - Logical Implications:** "If this claim is true, what MUST also be true?"
   - Look for unstated logical consequences

   **Type 2 - Unstated Assumptions:** "What must be true for this claim to hold?"
   - Look for prerequisites not acknowledged

   **Type 3 - Bridging Claims:** "How do they get from evidence to this claim?"
   - Look for missing argumentative steps

   **Type 4 - Disciplinary Assumptions:** "What field-specific knowledge is taken for granted?"
   - Look for insider assumptions invisible to outsiders

   Document trigger passages for each implicit argument found.

   **If no implicit arguments found after systematic search:** Document in extraction_notes why (e.g., "All reasoning explicit in this section"). Skipping the search is not acceptable.

   **Common Pitfalls When Extracting Implicit Arguments:**

   - ❌ Only scanning for Type 1 (logical implications), neglecting Types 2-4 which are often more assessment-critical
   - ❌ Superficial scan instead of systematic 4-type review per core claim
   - ❌ Missing cross-section assumptions (visible only when seeing full argument arc—note for Pass 2)
   - ❌ Extracting your own critique (what they SHOULD have considered) vs what their reasoning depends on
   - ❌ No trigger_text (your inference without textual basis = hallucination)
   - ❌ Treating all domain knowledge as implicit (only extract if paper's reasoning relies on it)

   **Quality Check:** For each core claim, can you demonstrate you ran all 4 type scans? Document scan methodology in extraction_notes if needed.

   **For detailed recognition patterns and common mistakes:**
   → See `references/extraction-fundamentals.md` (Implicit Arguments Extraction section)

   **For concrete examples with proper sourcing structure:**
   → See `extraction-system/scripts/extraction/section_implicit_arguments_template.py` (4 worked examples, one per type)

4. **Map Relationships**
   - Which claims support which other claims?
   - Are there alternatives or qualifications?
   - Does this contradict prior literature?

5. **Apply Expected Information Checklists**
   - Flag missing expected information
   - Don't penalize, just document

---

## Output Format

**Return the same JSON document you received, with these arrays populated:**
- `evidence` - All evidence items extracted
- `claims` - All claim items extracted (core, intermediate, supporting)
- `implicit_arguments` - All implicit arguments extracted
- `project_metadata` - Timeline, location, resources, track record context

**Leave unchanged:** `research_designs`, `methods`, `protocols` (RDMAP arrays extracted separately)

**Update:** `extraction_notes` with pass number, section extracted, strategy, uncertainties

**→ For complete object structure and field definitions, see `references/schema/schema-guide.md`**

---

## Quality Checklist for Pass 1

Use this checklist as your roadmap. Before finalizing:

- [ ] All potentially relevant evidence captured?
- [ ] All claims identified (core, intermediate, supporting)?
- [ ] **Systematic implicit argument search completed for all core claims**
- [ ] **All implicit arguments have trigger_text, trigger_locations, inference_reasoning**
- [ ] **If no implicit arguments found: documented in extraction_notes with rationale**
- [ ] **All evidence items have verbatim_quote populated**
- [ ] **All claims have verbatim_quote populated**
- [ ] Evidence-claim support relationships mapped?
- [ ] Expected information gaps flagged?
- [ ] Project metadata separated from evidence?
- [ ] All items have location tracking?
- [ ] Uncertain items marked in extraction_notes?
- [ ] **No hallucinations - only extract what's sourced**
- [ ] Other arrays (RDMAP) left unchanged?

---

## Remember

**Pass 1 is about COMPREHENSIVE CAPTURE, not perfect classification.**

- Over-extract rather than under-extract
- Preserve granularity
- Mark uncertainties
- Let Pass 2 consolidate and rationalize
- **All items must be properly sourced** (see extraction-fundamentals.md)
- **Don't touch RDMAP arrays** - those are extracted separately

**Your goal:** Ensure nothing important is missed. Pass 2 will refine.