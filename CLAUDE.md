# LLM Reproducibility Project - Research Paper Extraction

## Project Purpose

Systematic extraction and assessment of evidence, claims, methods, and research designs from academic papers using the `research-assessor` skill. Evaluates transparency, replicability, and credibility of fieldwork-based research.

## CRITICAL: Autonomous Execution Mode

**This project uses fully autonomous multi-pass workflows triggered by WORKFLOW.md.**

### Execution Rules - Never Stop Between Steps

You MUST work continuously without asking permission:

- ✅ **Never ask "Would you like me to continue?"**
- ✅ **Never ask "Should I proceed to the next section?"**
- ✅ **Never stop between passes (0→1→2→3→4→5→6)**
- ✅ **Never stop between section groups**
- ✅ **Work until all 7 passes complete**

### Continue Automatically After

- Completing a section group (Abstract+Intro, Methods, Results, Discussion)
- Completing any pass
- Saving to extraction.json
- Updating queue.yaml
- Validation checks
- Any intermediate workflow step

### Only Stop If

- ✅ All 7 passes complete (extraction done)
- ✅ Error requires user intervention (document in queue.yaml)
- ✅ Structural problem with input files

### Session Resumption

- **Auto-compact happens naturally** - resume from queue.yaml checkpoint when it does
- **Don't ask before resuming** - check queue.yaml and continue
- **Don't summarise progress between steps** - just do the work
- **Treat workflow as single continuous job**

## Workflow Reference

**Core workflow:** `input/WORKFLOW.md` - Complete 7-pass extraction process (Pass 0-6) with planning requirements

**Planning guidance:** `extraction-system/EXTRACTION_PLAN_UNIFIED_MODEL.md` - Flexible planning model adapted for diverse paper types (empirical/methodological/short/long/multi-proxy)

**Launch prompt:** `input/EXTRACTION_LAUNCH.md` - Brief primer for starting new extractions

## File Operations Safety

**CRITICAL**: Always read full files before writing to prevent data loss.
```python
# ✅ CORRECT
data = Read("outputs/paper-name/extraction.json")  # No limit
# ... modify data ...
Write("outputs/paper-name/extraction.json", data)

# ❌ WRONG - Will truncate file
data = Read("outputs/paper-name/extraction.json", limit=5000)  # Dangerous!
Write("outputs/paper-name/extraction.json", data)  # Loses data
```

**Always validate counts after writes:**
```bash
jq '{evidence: (.evidence|length), claims: (.claims|length)}' extraction.json
```

## Project-Specific Acronyms

Expand on first usage in each file:
- **RDMAP**: Research Design and Methods Assessment Protocol
- **CEM**: Claims-Evidence-Methods framework
- **CWTS**: Centre for Science and Technology Studies (Leiden)
- **repliCATS**: Collaborative Assessments for Trustworthy Science
- **HASS**: Humanities, Arts, and Social Sciences

## Key Files and Structure
```
input/
├── queue.yaml              # Paper processing queue (checkpoint/resume)
├── WORKFLOW.md            # Complete 5-pass extraction workflow
└── papers/                # PDF papers to process

outputs/
└── {paper-slug}/
    ├── extraction.json    # Primary extraction output
    └── {paper-slug}.txt   # Extracted plain text

extraction-system/
├── prompts/              # Pass-specific extraction prompts
└── schema/              # JSON schema definitions
```

## Skills Used

- `research-assessor` - Primary extraction and assessment skill
- Loads automatically from project knowledge and `/mnt/project/` files

## Validation Checks

After each section extraction, verify:
```bash
# Item counts
jq '.evidence | length' extraction.json
jq '.claims | length' extraction.json

# Required fields present
jq '.extraction_notes.section_extracted' extraction.json
jq '.extraction_timestamp' extraction.json
```

## Common Issues and Solutions

**Issue**: Claude stops between passes  
**Solution**: Check this CLAUDE.md - autonomous mode enabled

**Issue**: Extraction counts don't match  
**Solution**: Always Read() full file without limit parameter

**Issue**: Session auto-compacts mid-extraction  
**Solution**: Check queue.yaml, resume from checkpoint automatically

**Issue**: Can't find paper text  
**Solution**: Check `outputs/{paper-slug}/{paper-slug}.txt` exists