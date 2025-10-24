# Research Extraction Workflow

**Version:** 2.6
**Skill:** research-assessor
**Updated:** 2025-10-24

---

## Overview

This workflow extracts research methodology, claims, and evidence from academic papers through a structured 5-pass process. Each paper undergoes systematic extraction that populates a standardized JSON schema and produces human-readable validation reports.

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

## Workflow Steps

### Pre-Flight
1. **Check queue**: Read `input/queue.yaml` to identify next paper with `status: pending`
2. **Load paper**: Read the PDF from the specified path
3. **Initialize schema**: Copy blank schema to `outputs/{paper-slug}/extraction.json`
4. **Update queue**: Set paper status to `in_progress`

### Pass 1: Claims & Evidence (Liberal)
- **Prompt**: `extraction-system/prompts/claims-evidence_pass1_prompt.md`
- **Action**: Extract all observations, measurements, claims, and arguments
- **Output**: Update `outputs/{paper-slug}/extraction.json` with claims/evidence entities
- **Goal**: Cast wide net; capture everything potentially relevant

### Pass 2: Claims & Evidence (Rationalization)
- **Prompt**: `extraction-system/prompts/claims-evidence_pass2_prompt.md`
- **Action**: Review Pass 1 results, refine, consolidate, remove false positives
- **Output**: Update same JSON file with refined claims/evidence
- **Goal**: Improve accuracy and specificity

### Pass 3: RDMAP (Research Designs, Methods, Protocols) - Liberal
- **Prompt**: `extraction-system/prompts/rdmap_pass1_prompt.md`
- **Action**: Extract research designs, methods, and protocols
- **Output**: Append RDMAP entities to JSON
- **Goal**: Comprehensive methodology extraction

### Pass 4: RDMAP Rationalization
- **Prompt**: `extraction-system/prompts/rdmap_pass2_prompt.md`
- **Action**: Refine RDMAP extraction, improve cross-references to claims/evidence
- **Output**: Update JSON with refined RDMAP data
- **Goal**: Ensure methodology connects to claims/evidence

### Pass 5: Validation & Reporting
- **Prompt**: `extraction-system/prompts/rdmap_pass3_prompt.md`
- **Action**: Verify structural integrity, check cross-references, assess completeness
- **Output**: Write `validation-pass3.md` (NO changes to JSON)
- **Goal**: Quality assurance and human-readable assessment

### Post-Processing
1. **Generate summary**: Create `summary.md` with key entities and metadata from final JSON
2. **Update queue**: Set paper status to `completed` in `queue.yaml`
3. **Report completion**: Notify user with output locations

## Session Continuity

If context limits are approached:
1. **Save state**: Ensure current pass results are written to JSON
2. **Document progress**: Note which pass was completed in queue.yaml notes
3. **Resume**: On restart, read JSON to determine where to continue

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
