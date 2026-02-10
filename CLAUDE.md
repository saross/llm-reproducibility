# LLM Reproducibility Project - Research Paper Extraction

**Version:** 2.8 | **Schema:** v2.6 | **Workflow:** 8-pass session-per-pass (v5.0.0) | **Reproduction:** v1.0
**Manifest:** See `manifest.yaml` for all component versions

## Project Purpose

Systematic extraction and assessment of evidence, claims, methods, and research designs from academic papers using the `research-assessor` skill. Evaluates transparency, replicability, and credibility of fieldwork-based research.

## CRITICAL: Session-per-Pass Execution Mode

**This project uses a session-per-pass workflow that produces higher quality extractions.**

Run comparison (crema-et-al-2024) demonstrated session-per-pass yields:
- +75% claims captured
- +100% research designs captured
- Better cross-references and methodological reasoning

### Session Structure

Extraction is organised into 4 focused sessions:

| Session | Passes | Focus | Typical Duration |
|---------|--------|-------|------------------|
| **A** | Pass 0 + Pass 6 | Metadata + Infrastructure | 30-60 min |
| **B** | Pass 1-2 | Claims/Evidence extraction + rationalisation | 3-6 hours |
| **C** | Pass 3-5 | RDMAP extraction + implicit + rationalisation | 3-5 hours |
| **D** | Pass 7 + FAIR | Validation + FAIR assessment | 1-2 hours |

### Within-Session Execution Rules

**Within each session**, work autonomously without stopping:

- ✅ **Never ask "Would you like me to continue?"** within a session
- ✅ **Never stop between section groups** within a pass
- ✅ **Complete all passes in the session** before stopping
- ✅ **Save to extraction.json** after each pass

### Between-Session Checkpoints

**At session end**, provide a handoff summary **and STOP**:

- ⛔ **Do NOT proceed to the next session without explicit user confirmation**
- The handoff summary signals completion; wait for the user to approve continuation

```text
Session [A/B/C/D] complete for {paper-slug}

Completed:
- Pass X: {summary}
- Pass Y: {summary}

Counts: {evidence}, {claims}, {research_designs}, {methods}, {protocols}

Next session: [B/C/D/Complete]
Ready to continue when you are.
```

### Session Resumption

When starting a new session or resuming after context compaction:

1. **Read extraction.json** - understand current state
2. **Check queue.yaml** - verify paper status and checkpoint
3. **Read paper text if needed** - for extraction passes
4. **Continue from checkpoint** - don't re-extract completed passes

### Why Session-per-Pass Works Better

1. **Focused attention**: Each session has a clear objective
2. **Fresh context**: New session = fresh context window for extraction
3. **Natural breaks**: Allows review between major phases
4. **Better quality**: Deeper extraction of methodological reasoning and cross-references

## Workflow Reference

**Core workflow:** `input/workflow.md` - Complete 8-pass extraction process (Pass 0-7) with planning requirements

**Planning guidance:** `extraction-system/extraction-plan-unified-model.md` - Flexible planning model adapted for diverse paper types (empirical/methodological/short/long/multi-proxy)

**Launch prompt:** `input/extraction-launch.md` - Brief primer for starting new extractions

**Queue:** `input/queue.yaml` - Paper processing queue with checkpoint/resume support

## Reproduction Workflow

**Skill:** `reproduction-assessor` — Docker-based reproduction, verification, and adversarial review

**Planning guide:** `reproduction-system/reproduction-plan-guide.md` — Flexible model for paper-specific adaptation

**Launch prompt:** `reproduction-system/reproduction-launch.md` — Quick-start primer for reproductions

**Prompts:** `reproduction-system/prompts/` — Session-specific prompts (00-03)

**Queue:** `studies/open-science-compliance/corpus/queue.yaml` — Paper queue with reproduction status

### Reproduction Session Structure

| Session | Prompt | Focus | Duration |
|---------|--------|-------|----------|
| **R-Plan** | `00-reproduction-plan.md` | Paper analysis, type classification, plan | 30-60 min |
| **R-A** | `01-preparation.md` | Materials + Docker + script adaptation | 30-90 min |
| **R-B** | `02-execution-and-verification.md` | Execution + comparison + documentation | 30 min - hours |
| **R-C** | `03-adversarial-review.md` | 5-dimension sceptical audit (fresh context) | 30-60 min |

### Reproduction Artefact Set

Each reproduction produces artefacts in `outputs/{paper-slug}/reproduction/attempt-{NN}/`:

- `Dockerfile` — Reproducible environment
- `run-analysis.R` — Batch-executable script
- `environment.md` — Software versions and dependencies
- `log.md` — Timeline and modifications
- `comparisons/comparison-report.md` — Quantitative results and verdict
- `outputs/` — Generated analysis outputs

### Verdict Categories

- **SUCCESSFUL** — All (or nearly all) values reproduced within tolerances
- **PARTIAL** — Some analyses reproduced, others could not
- **FAILED** — Material discrepancies affecting conclusions
- **BLOCKED** — Reproduction could not be attempted

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

## PDF Handling

**CRITICAL**: Always prefer reading PDFs directly using the Read tool.

**Tested finding** (Key et al. 2024 comparison): Text extraction achieves 91.5% of PDF extraction counts. PDF is preferred because it performs equally well while preserving additional context.

- ✅ **Read PDFs directly** - Extraction quality is equivalent or slightly better
- ✅ **Preserve visual context** - Page numbers, tables, figures, and formatting are captured
- ⚠️ **Only extract text as last resort** - When PDF genuinely exceeds context limits

```python
# ✅ PREFERRED - Read PDF directly
paper = Read("corpus/pdfs/paper-slug.pdf")

# ⚠️ FALLBACK ONLY - When PDF doesn't fit in context
# Text extraction is viable (91.5% capture rate) but loses:
# - Page numbers for location references
# - Table structure and figure captions
# - Section formatting that aids extraction
```

**Why PDF is preferred despite context compactions:**
- Context compaction maintains continuity well across sessions
- PDF preserves page numbers essential for `location` fields
- Maintains table structure and figure captions
- No text extraction artefacts or errors
- RDMAP extraction quality is equivalent between formats

## Filename Convention Enforcement

**CRITICAL**: Pre-commit hook enforces lowercase-with-hyphens filenames

A git pre-commit hook automatically blocks commits with ALL CAPS filenames.

**Allowed:**
- ✅ `my-document.md` (lowercase-with-hyphens)
- ✅ `README.md` (standard exception)
- ✅ `CONTRIBUTING.md` (standard exception)

**Blocked:**
- ❌ `MY_DOCUMENT.md` (ALL CAPS)
- ❌ `My_Document.md` (mixed case/underscores)
- ❌ `ANALYSIS_REPORT.md` (ALL CAPS)

**Standard exceptions only:** README, CHANGELOG, CONTRIBUTING, CODE_OF_CONDUCT, CLAUDE, SKILL, LICENSE, CITATION

**If hook blocks your commit:**
1. Rename the file to lowercase-with-hyphens
2. Re-stage and commit
3. Never use `--no-verify` unless absolutely necessary

**Installing hook in new clones:**
```bash
./scripts/install-git-hooks.sh
```

## Project-Specific Acronyms

Expand on first usage in each file:
- **RDMAP**: Research Design and Methods Assessment Protocol
- **CEM**: Claims-Evidence-Methods framework
- **CWTS**: Centre for Science and Technology Studies (Leiden)
- **repliCATS**: Collaborative Assessments for Trustworthy Science
- **HASS**: Humanities, Arts, and Social Sciences

## Key Files and Structure

```text
manifest.yaml              # Component version manifest (source of truth)

input/
├── queue.yaml             # Paper processing queue (checkpoint/resume)
├── workflow.md            # Complete 8-pass extraction workflow
└── extraction-launch.md   # Quick-start primer for new extractions

outputs/
└── {paper-slug}/
    ├── extraction.json    # Primary extraction output
    ├── {paper-slug}.txt   # Extracted plain text
    └── reproduction/      # Reproduction artefacts
        └── attempt-{NN}/

extraction-system/
├── prompts/               # Pass-specific extraction prompts (00-07)
├── schema/                # JSON schema definitions (v2.6)
└── extraction-plan-unified-model.md  # Flexible planning guidance

reproduction-system/
├── prompts/               # Session-specific reproduction prompts (00-03)
├── templates/             # Document templates for artefacts
├── reproduction-plan-guide.md  # Flexible planning model
└── reproduction-launch.md      # Quick-start primer

assessment-system/
└── prompts/               # Assessment prompts (Pass 8-9, in development)
```

## Skills Used

- `research-assessor` — Primary extraction and assessment skill
- `reproduction-assessor` — Docker-based reproduction, verification, and adversarial review

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

**Issue**: Lower extraction counts than expected
**Solution**: Use session-per-pass approach (4 sessions, not single autonomous run)

**Issue**: Extraction counts don't match after write
**Solution**: Always Read() full file without limit parameter

**Issue**: Session auto-compacts mid-session
**Solution**: Check queue.yaml checkpoint, resume from last completed pass

**Issue**: Can't find paper text
**Solution**: Check `outputs/{paper-slug}/{paper-slug}.txt` exists

**Issue**: Unclear which session to run next
**Solution**: Check `extraction_notes.passes_completed` in extraction.json