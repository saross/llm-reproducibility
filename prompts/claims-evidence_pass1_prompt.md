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

## 🚨 CRITICAL SOURCING REQUIREMENT 🚨

**READ FIRST - BEFORE ANY EXTRACTION:**
`/mnt/skills/user/research-assessor/verification-procedures.md`

The verification procedures document contains:
- Complete verification protocols for evidence/claims and implicit arguments
- Decision trees for each verification step
- Worked examples (passes and fails)
- Red flags for hallucination detection
- Edge cases and troubleshooting

**MANDATORY for all extractions:**

**EVIDENCE & CLAIMS require:**
1. `verbatim_quote` - Exact text from paper stating this content
2. Precise location - Section, subsection, paragraph
3. Faithful extraction - Extract ONLY what quote explicitly states
4. If quote doesn't exist → DO NOT EXTRACT

**IMPLICIT ARGUMENTS require:**
1. `trigger_text` array - Verbatim passages that imply (not state) the argument
2. `trigger_locations` - Location of each trigger passage
3. `inference_reasoning` - Explanation connecting triggers to argument
4. If no trigger passages → DO NOT EXTRACT

**Quick test before extracting:**
- Evidence/Claims: "Can I point to the exact sentence that says this?"
- Implicit Arguments: "Can I point to specific passages that together imply this?"
- If NO → DO NOT EXTRACT

See verification-procedures.md for complete guidance.

---

## EXTRACTION PHILOSOPHY FOR PASS 1

**When uncertain whether something qualifies as evidence/claim: INCLUDE IT.**

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

---

## Core Extraction Principles

### 1. Evidence vs. Claims Distinction

**EVIDENCE** = Raw observations, measurements, or data that require minimal interpretation
- Direct measurements (e.g., "125.8 person-hours")
- Observations (e.g., "12 students owned smartphones")
- Data points (e.g., "95.7% accuracy")
- Captured verbatim from the paper
- Someone could verify by checking the source

**CLAIMS** = Assertions that interpret, frame, or generalize from evidence
- Require reasoning or expertise to assess
- Make inferences beyond direct observation
- Involve framing or definitional choices
- Connect evidence to broader patterns

**Professional Judgment Boundary:** Statements requiring expertise to assess (e.g., "these maps are accurate") are **CLAIMS** supported by implicit professional judgment, not evidence. Extract as INTERPRETATION claims, not observations.

**→ For detailed decision framework, see `references/checklists/tier-assignment-guide.md`**

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

**Extract implicit arguments ONLY for core and key intermediate claims.**

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

**For Quantitative Claims:**
- Method specified?
- Error margins/confidence intervals?
- Sample size reported?
- Precision justified?

**For Comparative Claims:**
- Basis of comparison explicit?
- What was held constant?
- Alternative explanations considered?

**For Causal Claims:**
- Mechanism proposed?
- Alternative causes ruled out?
- Temporal sequence established?

**Flag missing expected information** in `expected_information_missing` field.

**→ For comprehensive checklists by domain, see `references/checklists/expected-information.md`**

---

## Extraction Workflow

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

3. **Check for Implicit Arguments** (high-priority claims only)
   - What logical implications are unstated?
   - What assumptions must be true?
   - Are there bridging claims missing?
   - What disciplinary assumptions frame the argument?

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

```json
{
  "schema_version": "2.5",
  "extraction_timestamp": "ISO 8601",
  "extractor": "Claude Sonnet 4.5",
  
  "evidence": [evidence_object],
  "claims": [claim_object],
  "implicit_arguments": [implicit_argument_object],
  "project_metadata": {
    "timeline": {...},
    "location": {...},
    "resources": {...},
    "track_record": {...}
  },
  
  // These arrays remain unchanged if already populated:
  "research_designs": [...],  // Leave untouched
  "methods": [...],           // Leave untouched
  "protocols": [...],         // Leave untouched
  
  "extraction_notes": {
    "pass": 1,
    "section_extracted": "string",
    "extraction_strategy": "Liberal extraction with over-capture",
    "known_uncertainties": ["string"]
  }
}
```

**→ For complete object structure and field definitions, see `references/schema/schema-guide.md`**

---

## Quality Checklist for Pass 1

Before finalizing extraction:

- [ ] All potentially relevant evidence captured?
- [ ] All claims identified (core, intermediate, supporting)?
- [ ] Implicit arguments extracted for high-priority claims?
- [ ] Evidence-claim support relationships mapped?
- [ ] Expected information gaps flagged?
- [ ] Project metadata separated from evidence?
- [ ] All items have location tracking?
- [ ] Uncertain items marked in extraction_notes?
- [ ] Other arrays (RDMAP) left unchanged?

---

## Remember

**Pass 1 is about COMPREHENSIVE CAPTURE, not perfect classification.**

- Over-extract rather than under-extract
- Preserve granularity
- Mark uncertainties
- Let Pass 2 consolidate and rationalize
- **Don't touch RDMAP arrays** - those are extracted separately

**Your goal:** Ensure nothing important is missed. Pass 2 will refine.