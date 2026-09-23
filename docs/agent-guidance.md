# Agent guidance — llm-reproducibility

Shared project policy for any AI agent working in this repository. It is
harness-neutral by construction: Claude Code reaches it from `CLAUDE.md`, and
Codex from `AGENTS.md`. Both entry points stay short and carry only
harness-specific mechanisms — tool names, skills, hooks, and commands.

Edit this file when project policy changes. Do not copy its rules into a
harness entry point, or the two will drift.

**Version:** 3.1 | **Schema:** v2.7 | **Workflow:** 8-pass session-per-pass
(v5.0.0) | **Reproduction:** v1.1
**Manifest:** see `manifest.yaml` for all component versions.

## Session continuity — fetch first

Run `git fetch` **first**, before reading anything or starting work, and report
ahead/behind. Then read `wiki/continuity.md` — cross-session state, pending
tasks, and the session log live there. Planning documents live in
`wiki/planning/`.

> **Why fetch first.** This repository is worked from several machines
> (amd-tower, zbook). `git status` and `git rev-list origin/main...HEAD` read
> the *local* `origin/main` ref and never contact the remote, so without a
> fetch they report "in sync" from a stale pointer — which looks exactly like
> genuinely being in sync. An agent harness's session-start git snapshot does
> not fetch either. On 2026-07-27 this cost a full duplicate build of the D5
> gate: the resumed session's check said `0 behind` while seven commits sat
> unfetched from three days earlier.

## Project purpose

Systematic extraction and assessment of evidence, claims, methods, and research
designs from academic papers. Evaluates transparency, replicability, and
credibility of fieldwork-based research.

## CRITICAL: session-per-pass execution mode

**This project uses a session-per-pass workflow that produces higher quality
extractions.**

Run comparison (crema-et-al-2024) demonstrated session-per-pass yields:

- +75% claims captured
- +100% research designs captured
- Better cross-references and methodological reasoning

### Session structure

Extraction is organised into 4 focused sessions:

| Session | Passes | Focus | Typical duration |
| ------- | ------ | ----- | ---------------- |
| **A** | Pass 0 + Pass 6 | Metadata + Infrastructure | 30-60 min |
| **B** | Pass 1-2 | Claims/Evidence extraction + rationalisation | 3-6 hours |
| **C** | Pass 3-5 | RDMAP extraction + implicit + rationalisation | 3-5 hours |
| **D** | Pass 7 + FAIR | Validation + FAIR assessment | 1-2 hours |

### Within-session execution rules

**Within each session**, work autonomously without stopping:

- ✅ **Never ask "Would you like me to continue?"** within a session
- ✅ **Never stop between section groups** within a pass
- ✅ **Complete all passes in the session** before stopping
- ✅ **Save to extraction.json** after each pass

### Between-session checkpoints

**At session end**, provide a handoff summary **and STOP**:

- ⛔ **Do NOT proceed to the next session without explicit user confirmation**
- The handoff summary signals completion; wait for the user to approve
  continuation

```text
Session [A/B/C/D] complete for {paper-slug}

Completed:
- Pass X: {summary}
- Pass Y: {summary}

Counts: {evidence}, {claims}, {research_designs}, {methods}, {protocols}

Next session: [B/C/D/Complete]
Ready to continue when you are.
```

### Session resumption

When starting a new session or resuming after context compaction:

1. **Read extraction.json** — understand current state
2. **Check queue.yaml** — verify paper status and checkpoint
3. **Read paper text if needed** — for extraction passes
4. **Continue from checkpoint** — do not re-extract completed passes

### Why session-per-pass works better

1. **Focused attention**: each session has a clear objective
2. **Fresh context**: new session = fresh context window for extraction
3. **Natural breaks**: allows review between major phases
4. **Better quality**: deeper extraction of methodological reasoning and
   cross-references

## Workflow reference

**Core workflow:** `input/workflow.md` — complete 8-pass extraction process
(Pass 0-7) with planning requirements

**Planning guidance:** `extraction-system/extraction-plan-unified-model.md` —
flexible planning model adapted for diverse paper types
(empirical/methodological/short/long/multi-proxy)

**Launch prompt:** `input/extraction-launch.md` — brief primer for starting new
extractions

**Queue:** `input/queue.yaml` — paper processing queue with checkpoint/resume
support

## Reproduction workflow

**Planning guide:** `reproduction-system/reproduction-plan-guide.md` — flexible
model for paper-specific adaptation

**Launch prompt:** `reproduction-system/reproduction-launch.md` — quick-start
primer for reproductions

**Prompts:** `reproduction-system/prompts/` — session-specific prompts (00-03)

**Queue:** `studies/open-science-compliance/corpus/queue.yaml` — paper queue
with reproduction status

### Reproduction session structure

- **R-Plan** — `00-reproduction-plan.md`: paper analysis, type
  classification, plan. 30-60 min.
- **R-A** — `01-preparation.md`: materials, Docker, script adaptation.
  30-90 min.
- **R-B** — `02-execution-and-verification.md`: execution, comparison,
  documentation. 30 min to hours.
- **R-C** — `03-adversarial-review.md`: 5-dimension sceptical audit, in a
  fresh context. 30-60 min.

### Reproduction artefact set

Each reproduction produces artefacts in
`outputs/{paper-slug}/reproduction/attempt-{NN}/`:

- `Dockerfile` — reproducible environment
- `run-analysis.R` — batch-executable script
- `environment.md` — software versions and dependencies
- `log.md` — timeline and modifications
- `comparisons/comparison-report.md` — quantitative results and verdict
- `outputs/` — generated analysis outputs

### Verdict categories

- **SUCCESSFUL** — all (or nearly all) values reproduced within tolerances
- **PARTIAL** — some analyses reproduced, others could not
- **FAILED** — material discrepancies affecting conclusions
- **BLOCKED** — reproduction could not be attempted

## File operations safety

**CRITICAL**: always read a file in full before writing it. A partial read
followed by a write truncates the file and loses data. This applies to every
harness; the specific parameter that causes it differs per tool, so see the
harness entry point for the local hazard.

`extraction.json` is the file this most often destroys.

**Always validate counts after writes:**

```bash
jq '{evidence: (.evidence|length), claims: (.claims|length)}' extraction.json
```

## PDF handling

**CRITICAL**: always prefer reading PDFs directly over reading extracted text.

**Paper sources live in the out-of-tree corpus store** (2026-07-24):
`~/corpora/llm-reproducibility/<slug>/` — `vor.pdf`, `preprint.pdf`,
`supplement-*.pdf`, `extracted.txt`. Entry point and manifests:
`corpus/README.md`. The gitignored symlink `corpus/store/<slug>/` reaches the
same files from inside the repo. Legacy in-repo copies
(`studies/*/corpus/pdfs/`, `input/sources/`) remain transitionally but the
store is canonical; **never add third-party PDFs or extracted article text to
git** (a pre-commit corpus gate enforces this).

**Tested finding** (Key et al. 2024 comparison): text extraction achieves 91.5%
of PDF extraction counts. PDF is preferred because it performs equally well
while preserving additional context.

- ✅ **Read PDFs directly** — extraction quality is equivalent or slightly
  better
- ✅ **Preserve visual context** — page numbers, tables, figures, and
  formatting are captured
- ⚠️ **Only extract text as a last resort** — when a PDF genuinely exceeds
  context limits

**Why PDF is preferred despite context compactions:**

- Context compaction maintains continuity well across sessions
- PDF preserves page numbers essential for `location` fields
- Maintains table structure and figure captions
- No text extraction artefacts or errors
- RDMAP extraction quality is equivalent between formats

## Filename convention enforcement

**CRITICAL**: a git pre-commit hook enforces lowercase-with-hyphens filenames
and automatically blocks commits with ALL CAPS filenames.

**Allowed:**

- ✅ `my-document.md` (lowercase-with-hyphens)
- ✅ `README.md` (standard exception)
- ✅ `CONTRIBUTING.md` (standard exception)

**Blocked:**

- ❌ `MY_DOCUMENT.md` (ALL CAPS)
- ❌ `My_Document.md` (mixed case/underscores)
- ❌ `ANALYSIS_REPORT.md` (ALL CAPS)

**Standard exceptions only:** README, CHANGELOG, CONTRIBUTING, CODE_OF_CONDUCT,
CLAUDE, AGENTS, SKILL, LICENSE, CITATION

**If the hook blocks your commit:**

1. Rename the file to lowercase-with-hyphens
2. Re-stage and commit
3. Never use `--no-verify` unless absolutely necessary

**Installing the hook in new clones:**

```bash
./scripts/install-git-hooks.sh
```

⚠ An admitted Codex clone is created with hooks disabled, so this gate does not
run there. Check filenames explicitly before committing from a lane, and review
the installer's compatibility with the admission validator before running it.

## Project-specific acronyms

Expand on first usage in each file:

- **RDMAP**: Research Design and Methods Assessment Protocol
- **CEM**: Claims-Evidence-Methods framework
- **CWTS**: Centre for Science and Technology Studies (Leiden)
- **repliCATS**: Collaborative Assessments for Trustworthy Science
- **HASS**: Humanities, Arts, and Social Sciences

## Key files and structure

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
├── schema/                # JSON schema definitions (v2.7; v2.6 retained
│                          #   for pilots)
└── extraction-plan-unified-model.md  # Flexible planning guidance

reproduction-system/
├── prompts/               # Session-specific reproduction prompts (00-03)
├── templates/             # Document templates for artefacts
├── reproduction-plan-guide.md  # Flexible planning model
└── reproduction-launch.md      # Quick-start primer

assessment-system/
└── prompts/               # Assessment prompts (Pass 8-9, in development)

docs/                      # This file and project documentation
wiki/                      # Continuity, planning, working notes, registers
```

**Study papers** live under `studies/{study-name}/outputs/{paper-slug}/` with
the same per-paper layout (extraction.json, assessment/, reproduction/). The
paper's queue entry `output_dir` field is authoritative for determining the
correct output path. Non-study papers use the default `outputs/{paper-slug}/`
location.

## Validation checks

After each section extraction, verify:

```bash
# Item counts
jq '.evidence | length' extraction.json
jq '.claims | length' extraction.json

# Required fields present
jq '.extraction_notes.section_extracted' extraction.json
jq '.extraction_timestamp' extraction.json
```

## Common issues and solutions

**Issue**: lower extraction counts than expected
**Solution**: use the session-per-pass approach (4 sessions, not a single
autonomous run)

**Issue**: extraction counts do not match after write
**Solution**: always read the full file before writing it

**Issue**: session auto-compacts mid-session
**Solution**: check the `queue.yaml` checkpoint, resume from the last completed
pass

**Issue**: cannot find paper text
**Solution**: check `outputs/{paper-slug}/{paper-slug}.txt` exists

**Issue**: unclear which session to run next
**Solution**: check `extraction_notes.passes_completed` in `extraction.json`

## Agent ownership in this repository

The reciprocal boundary is set by
`~/personal-assistant/global-agent-guidance/ownership.toml` and the plan at
`~/personal-assistant/wiki/planning/gpt-in-codex-integration.md`. Here:

- **Claude-owned, read-only to Codex:** `CLAUDE.md`, `.claude/` (a real,
  partly tracked directory in this repository — agents, commands, hooks,
  skills), and `wiki/claude-observations.md`.
- **Codex-owned, read-only to Claude:** `AGENTS.md`, `AGENTS.override.md`, and
  `.codex/`.
- **Shawn-gated:** `wiki/user-observations.md`. Either agent may draft a
  labelled candidate; Shawn decides its final status.
- **Shared:** this file, `wiki/continuity.md`, `wiki/working-notes.md`, and all
  extraction, reproduction, assessment, corpus, script, and study material.

A blocked path is not a dead end. Draft the exact change and hand it to the
owning agent or to Shawn, through agent mail (`Project: llm-reproducibility`),
a shared planning document, or the current conversation.

Cross-agent work never shares a checkout. Codex works only in its admitted
independent clone at `~/worktrees/llm-reproducibility/sol-repro-entry`; a
directory name confers nothing, the `ownership.toml` admission does.
