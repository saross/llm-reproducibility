# Research Extraction Workflow

**Version:** 2.7.0
**Skill:** research-assessor
**Updated:** 2025-10-28

---

## Overview

This workflow extracts research methodology, claims, and evidence from academic papers through a structured 6-pass process. Each paper undergoes systematic extraction that populates a standardised JSON schema and produces human-readable validation reports.

## Input/Output Structure

```
Input:
  - PDF paper: As specified in input/queue.yaml
  - Blank schema: extraction-system/schema/extraction_schema.json

Output (for each paper):
  outputs/{paper-slug}/
    ├── extraction.json         # Final populated schema
    ├── validation-pass3.md     # Human-readable validation report
    └── summary.md             # Key findings summary
```

## Extraction Methodology: Section-by-Section Approach

**IMPORTANT**: Liberal extraction passes (prompt 01; prompt 03) should be executed **section-by-section**, not on the entire paper at once. This approach has been tested and found significantly more effective for:
- Maintaining focus and thoroughness
- Ensuring proper sourcing and verbatim quotes
- Managing cognitive load
- Producing higher-quality extractions

### Required Section Grouping (Pass 1 & Pass 3 ONLY)

**Flexible section-by-section extraction for liberal passes (01, 03):**

Execute by processing section groups in order, adapting to paper structure:

1. **Abstract + following section** - Combined as ONE unit (save to JSON after)
2. **Middle sections** - Each major section as ONE unit (save to JSON after)
3. **Conclusion + preceding section** - Combined as ONE unit (save to JSON after)

**Section size limits:** Target ~1000 words, maximum 1500 words. If section exceeds 1500 words, divide into roughly equal chunks at natural breaks (subsections > topic shifts > paragraph boundaries).

**Papers without sections:** Process in ~1000-word chunks using paragraph/thematic boundaries.

**Track chunking decisions:** Document section grouping and word counts in `extraction_notes.section_extracted` for quality review.

**For detailed section handling guidance:** See "Section Handling" in prompts 01 and 03.

**For rationalisation passes (02, 05) and validation (06):**
- Review all extractions across entire paper
- No section-by-section processing required

**For implicit RDMAP pass (04):**
- Scan across entire paper
- No section-by-section processing required

### File Management for Section-by-Section Extraction

**IMPORTANT - Direct writes only:**

For section-by-section extraction (Pass 1 and Pass 3):
- **DO**: Update `extraction.json` directly using Write or Edit tool after each section group
- **DO NOT**: Create intermediate files (e.g., `claims_pass1_methods.json`, `rdmap_pass3_results.json`)

**Rationale:**
- ✅ Simpler workflow with fewer files to manage
- ✅ `extraction.json` serves as the checkpoint/audit trail
- ✅ Git history provides version control if needed
- ✅ Cleaner output directory
- ✅ No cleanup needed after extraction completes

**Example of correct approach:**
```
1. Extract from Abstract + Introduction
2. Write to extraction.json (replaces entire file with updated content)
3. Extract from Methods section
4. Write to extraction.json (replaces entire file with updated content including previous extractions)
... continue for all section groups
```

**Incorrect approach (DO NOT do this):**
```
❌ Write to claims_pass1_abstract.json
❌ Write to claims_pass1_methods.json
❌ Merge intermediate files into extraction.json
```

---

### File Operation Safety Rules (CRITICAL)

**⚠️ CRITICAL: Preventing Data Loss**

A file operation bug in a previous run caused catastrophic data loss: a partial `Read(file, limit=14)` followed by `Write(file)` overwrote the entire 750+ line extraction.json, destroying all claims and implicit arguments (367 lines deleted, never recovered).

**MANDATORY SAFETY RULES - Follow Without Exception:**

#### Rule 1: NEVER Partial Read Before Full Write

```
❌ FORBIDDEN PATTERN (causes data loss):
Read(extraction.json, limit=14)    # Reads only first 14 lines
... modify in memory ...
Write(extraction.json, content)     # Overwrites ENTIRE file with partial context
→ RESULT: 367 line deletion, complete data loss
```

```
✅ REQUIRED PATTERN (safe):
Read(extraction.json)               # Read FULL file (no limit parameter)
... modify in memory ...
Write(extraction.json, content)     # Write complete updated file
→ RESULT: All data preserved
```

**Absolute requirement:** Before ANY `Write(extraction.json)`, you MUST `Read(extraction.json)` with **NO limit parameter**.

#### Rule 2: Prefer Edit Tool for Incremental Updates

For adding items to existing arrays:
```
✅ PREFERRED: Edit(file, old_string, new_string)
✅ ACCEPTABLE: Read(file) [full] → modify → Write(file)
❌ FORBIDDEN: Read(file, limit=N) → Write(file)
```

#### Rule 3: Pre-Write Validation Checklist

Before every `Write(extraction.json)`, verify:

1. ✅ **Full context loaded**: Did you `Read()` the complete file (no limit)?
2. ✅ **Preserving existing data**: Does your write include ALL previously extracted items?
3. ✅ **Array integrity**: Are all six arrays present (evidence, claims, implicit_arguments, research_designs, methods, protocols)?
4. ✅ **No accidental deletion**: Did you verify array counts before writing?

**If you cannot answer YES to all four questions: STOP. Read the full file first.**

#### Rule 4: Post-Write Validation (MANDATORY)

After EVERY `Write(extraction.json)`, immediately run validation:

```bash
# Count items in each array
jq '{
  evidence: (.evidence | length),
  claims: (.claims | length),
  implicit_arguments: (.implicit_arguments | length),
  research_designs: (.research_designs | length),
  methods: (.methods | length),
  protocols: (.protocols | length)
}' outputs/{paper-slug}/extraction.json
```

**Validation checks:**

- ✅ **Pass 1 complete?** Claims array should be non-empty (typically 15-50 items)
- ✅ **Pass 1 complete?** Evidence array should be non-empty (typically 30-80 items)
- ✅ **Pass 3 complete?** RDMAP arrays should be non-empty (typically 2-6 designs, 5-10 methods, 8-20 protocols)
- ⚠️ **ALERT if zero:** If any array is unexpectedly empty after its pass completes, DATA LOSS may have occurred

**Example validation output:**
```json
{
  "evidence": 40,
  "claims": 26,
  "implicit_arguments": 4,
  "research_designs": 0,    // ← OK if before Pass 3
  "methods": 0,             // ← OK if before Pass 3
  "protocols": 0            // ← OK if before Pass 3
}
```

If you see **unexpected zeros** (e.g., claims=0 after Pass 1 section writes), **STOP IMMEDIATELY** and investigate. This indicates data loss.

#### Emergency Recovery Procedure

If validation reveals data loss:

1. **STOP WORK** - Do not continue extraction
2. **Check git history**: `git diff HEAD extraction.json` to see what was lost
3. **Restore if possible**: `git checkout HEAD -- outputs/{paper-slug}/extraction.json`
4. **Report to user**: Document what happened and request guidance
5. **Review file operations**: Identify the bad Read→Write pattern
6. **Retry with full Read**: Ensure complete file context before Write

---

### Example: Complete Pass 1 Execution

```
Pass 1 execution (continuous, no stopping):
1. Read prompt: 01-claims-evidence_pass1_prompt.md
2. Extract from: Abstract + Introduction (ALL subsections) → save to extraction.json
3. Extract from: Methods (ALL subsections) → save to extraction.json
4. Extract from: Results (ALL subsections) → save to extraction.json
5. Extract from: Discussion + Conclusion (together) → save to extraction.json
6. Update queue.yaml: Mark Pass 1 complete
7. Immediately proceed to Pass 2 (no user confirmation needed)

Pass 2 execution (continuous, no stopping):
1. Read prompt: 02-claims-evidence_pass2_prompt.md
2. Review and rationalize all claims/evidence across full paper
3. Save consolidated extraction.json
4. Update queue.yaml: Mark Pass 2 complete
5. Immediately proceed to Pass 3 (no user confirmation needed)

Continue through all 6 passes autonomously...
```

## Autonomous Execution

**IMPORTANT:** This workflow is designed for fully autonomous multi-pass execution across multiple sessions.

### Continuous Operation

**After completing each section group:**
- Save progress to `extraction.json`
- Update `queue.yaml` notes with current status
- Immediately proceed to next section group
- **DO NOT stop** for user confirmation

**After completing each pass:**
- Update `queue.yaml` with pass completion status
- Immediately proceed to next pass
- **DO NOT stop** for user confirmation

**Work continues across auto-compact sessions** using saved state as memory.

### Session Continuity After Auto-Compact

When resuming after context reset (auto-compact):

1. **Check current state:**
   - Read `queue.yaml` to determine current paper and progress
   - Read `extraction.json` to see what's been extracted

2. **Identify checkpoint:**
   - Which pass are we on? (Pass 1-6)
   - Which section group is next? (Abstract+Intro, Methods, Results, Discussion+Conclusion)
   - Or is this pass complete? (proceed to next pass)

3. **Resume work:**
   - Load appropriate prompt for current pass
   - Continue from documented checkpoint
   - Update `queue.yaml` notes as you progress

4. **Maintain continuity:**
   - Use JSON cross-references to understand existing extractions
   - Build on previous work, don't duplicate
   - Preserve established ID sequences (E001, C001, M001, etc.)

### Stopping Conditions

**Only stop execution if:**
- ✅ **All extraction complete**: All 6 passes done, summary.md generated, queue.yaml status set to `completed`
- ❌ **Error encountered**: Issue requires user intervention (document in queue.yaml notes)

**Do NOT stop for:**
- Context limits (auto-compact will occur, then resume autonomously)
- Uncertainty about extraction (document in extraction_notes, continue)
- Long sections (take breaks between section groups via auto-compact, but keep going)

## Workflow Steps

### Pre-Flight
1. **Check queue**: Read `input/queue.yaml` to identify next paper with `status: pending`
2. **Load paper**: Read the PDF from the specified path
3. **Initialize schema**: Copy blank schema to `outputs/{paper-slug}/extraction.json`
4. **Update queue**: Set paper status to `in_progress`

### Pass 1: Claims & Evidence (Liberal)
- **Prompt**: `extraction-system/prompts/01-claims-evidence_pass1_prompt.md`
- **Action**: Extract all observations, measurements, claims, and arguments **section-by-section**
- **Output**: Update `outputs/{paper-slug}/extraction.json` with claims/evidence entities after each section
- **Goal**: Cast wide net; capture everything potentially relevant
- **Approach**: Abstract+Intro → Methods → Results → Discussion+Conclusion

### Pass 2: Claims & Evidence (Rationalization)
- **Prompt**: `extraction-system/prompts/02-claims-evidence_pass2_prompt.md`
- **Action**: Review Pass 1 results across entire paper, refine, consolidate, remove false positives
- **Output**: Update same JSON file with refined claims/evidence
- **Goal**: Improve accuracy and specificity
- **Approach**: Review all extractions, refer back to entire paper as needed

### Pass 3: RDMAP Explicit Extraction (Liberal)
- **Prompt**: `extraction-system/prompts/03-rdmap_pass1_prompt.md`
- **Action**: Extract explicit research designs, methods, and protocols from Methods section **section-by-section**
- **Output**: Append explicit RDMAP entities to JSON after each section
- **Goal**: Liberal extraction of documented methodology
- **Approach**: Abstract+Intro → Methods → Results → Discussion+Conclusion

### Pass 4: RDMAP Implicit Extraction
- **Prompt**: `extraction-system/prompts/04-rdmap_pass1b_implicit_prompt.md`
- **Action**: Systematically scan for implicit RDMAP items (mentioned but undocumented, or inferred from Results/Discussion)
- **Output**: Add implicit RDMAP entities to existing arrays in JSON
- **Goal**: Identify transparency gaps and undocumented procedures
- **Approach**: Scan across entire paper using 4-pattern recognition for each tier
- **Note**: Uses already-extracted explicit RDMAP as seed list

### Pass 5: RDMAP Rationalisation
- **Prompt**: `extraction-system/prompts/05-rdmap_pass2_prompt.md`
- **Action**: Review Pass 3 & 4 results across entire paper, refine RDMAP extraction, improve cross-references to claims/evidence
- **Output**: Update JSON with refined RDMAP data
- **Goal**: Ensure methodology connects to claims/evidence, consolidate over-extracted items
- **Approach**: Review all extractions, refer back to entire paper as needed

### Pass 6: Validation & Reporting
- **Prompt**: `extraction-system/prompts/06-validation_prompt.md`
- **Action**: Verify structural integrity, check cross-references, assess completeness (whole paper)
- **Output**: Write `validation-pass3.md` (NO changes to JSON)
- **Goal**: Quality assurance and human-readable assessment
- **Note**: Pass 6 is the only pass that reviews the entire paper at once

### Post-Processing
1. **Generate summary**: Create `summary.md` with key entities and metadata from final JSON
2. **Update queue**: Set paper status to `completed` in `queue.yaml`
3. **Report completion**: Notify user with output locations

## Error Handling

- **Incomplete extraction**: Keep status as `in_progress`, create note in queue.yaml
- **Prompt errors**: Document in validation report, continue workflow
- **JSON corruption**: Revert to last good version (use git history if needed)

## Quality Checks

After each pass:
- ✓ JSON validates against schema
- ✓ All required fields populated
- ✓ Cross-references use valid entity IDs
- ✓ No duplicate entities

## Invocation

To start the workflow:
```
Process the next paper in the queue using the research-assessor workflow.
```

To resume after interruption:
```
Continue the research extraction for [paper-slug].
```

To process a specific paper:
```
Extract research from [paper-path] using the research-assessor workflow.
```

---

## Technical Details

**Token Budget**: ~70-85K tokens per paper (well within 200K limit)

**Persistence**: JSON schema provides state between passes and sessions

**Parallelization**: Not applicable (sequential passes build on previous results)

**Validation**: Each pass validates JSON before proceeding to next pass
