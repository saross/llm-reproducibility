# Variability Test Protocol

**Version:** 1.0
**Date:** 2025-12-01
**Purpose:** Document the automated protocol for testing extraction and assessment pipeline variability

---

## Overview

The variability test measures consistency of the research-assessor pipeline by running the full extraction and assessment workflow multiple times on the same papers. This tests whether the pipeline produces reliable, reproducible results.

### Key Questions

1. **Extraction consistency**: Do we extract the same items across runs?
2. **Assessment consistency**: Do we produce the same scores across runs?
3. **Propagation effects**: Does extraction variability affect assessment variability?

### Design

- **Papers**: 5 diverse papers (empirical, methodological, interpretive)
- **Runs per paper**: 5 independent extractions
- **Total runs**: 25
- **Context isolation**: Fresh session for each run (prevents contamination)

---

## Test Corpus

| Paper | Type | Approach | Context Flags | Status |
|-------|------|----------|---------------|--------|
| sobotkova-et-al-2024 | Empirical | Deductive | — | ✅ Complete |
| penske-et-al-2023 | Empirical | Inductive | — | 🔄 In Progress |
| ballsun-stanton-et-al-2018 | Methodological | — | 📦 🔧 | ⏳ Pending |
| ross-2005 | Empirical | Interpretive | 🔧 | ⏳ Pending |
| sobotkova-et-al-2016 | Empirical | Mixed | — | ⏳ Pending |

### Diversity Coverage

- 3 empirical papers (deductive, inductive, interpretive approaches)
- 1 methodological paper (software tool)
- 1 mixed-methods paper
- Context flag variants (📦 software, 🔧 non-standard methodology)

---

## Automation Components

### 1. Variability Queue (`input/variability-queue.yaml`)

Tracks all paper/run combinations with status:

```yaml
papers:
  - slug: penske-et-al-2023
    title: "Early contact between late farming..."
    source: input/sources/original-pdf/Penske et al...pdf
    paper_type: empirical
    research_approach: inductive
    status: in_progress
    runs:
      - id: run-01
        status: pending
      - id: run-02
        status: pending
      # ...
```

**Status values:**
- `pending` — Not yet started
- `in_progress` — Currently being processed (should not persist across sessions)
- `completed` — Run finished successfully
- `error` — Run failed (see notes)

**Tracked metadata (on completion):**
- `counts`: {evidence, claims, implicit_arguments}
- `aggregate_score`: Final credibility score (0-100)

### 2. Slash Command (`.claude/commands/variability-run.md`)

Automates a single run when invoked with `/variability-run`:

1. **Read queue** — Find next pending run
2. **Load skill** — Activate research-assessor
3. **Create output directory** — `outputs/variability-test/{paper}/{run}/`
4. **Execute extraction** — Passes 0-7 (evidence, claims, RDMAP, etc.)
5. **Execute assessment** — Passes 8-10 (classification, signals, report)
6. **Update queue** — Mark run complete, record metrics
7. **Run validation** — Check content uniqueness
8. **Report completion** — Summary for user

### 3. Validation Script (`scripts/validate-run-uniqueness.sh`)

Verifies runs have genuinely unique content (not copies):

```bash
./scripts/validate-run-uniqueness.sh outputs/variability-test/penske-et-al-2023
```

Checks MD5 hashes of evidence, claims, and implicit_arguments arrays across all runs.

### 4. Analysis Script (`scripts/analyse-extraction-variability.py`)

Computes variability metrics after runs complete:

```bash
python3 scripts/analyse-extraction-variability.py outputs/variability-test/penske-et-al-2023
```

**Metrics:**
- Count statistics (mean, stdev, CV%, range)
- Concept overlap (Jaccard similarity)
- Pairwise similarity matrices

---

## User Workflow

### Per-Run Protocol

```
┌─────────────────────────────────────────────────────────┐
│  1. Start fresh session (or /clear from previous)      │
│                                                         │
│  2. Run command:  /variability-run                      │
│                                                         │
│  3. Wait for completion (~30-60 minutes)                │
│     Claude will:                                        │
│     - Find next pending run from queue                  │
│     - Execute full pipeline autonomously                │
│     - Update queue with results                         │
│     - Report completion summary                         │
│                                                         │
│  4. Review output (optional)                            │
│                                                         │
│  5. Clear context:  /clear                              │
│                                                         │
│  6. Repeat from step 2                                  │
└─────────────────────────────────────────────────────────┘
```

### Why Context Clearing?

Context clearing between runs prevents **contamination** — a failure mode where the LLM, having seen previous extractions, produces outputs that are:
- Copies of previous runs (identical content)
- Deliberately different (artificial variation)

Neither represents genuine independent extraction. Fresh context ensures each run is a true independent read of the source paper.

### Checking Progress

View queue status:
```bash
cat input/variability-queue.yaml | grep -A2 "status:"
```

Or check output directories:
```bash
ls outputs/variability-test/*/run-*/extraction.json
```

---

## Output Structure

```
outputs/variability-test/
├── {paper-slug}/
│   ├── run-01/
│   │   ├── extraction.json          # Full extraction output
│   │   └── assessment/
│   │       ├── classification.json  # Paper type, approach
│   │       ├── track-a-quality.md   # Quality gating
│   │       ├── cluster-1-foundational-clarity.md
│   │       ├── cluster-2-evidential-strength.md
│   │       ├── cluster-3-reproducibility.md
│   │       └── credibility-report.md  # Final assessment
│   ├── run-02/
│   │   └── ...
│   ├── run-03/
│   ├── run-04/
│   ├── run-05/
│   └── variability-analysis.json    # Analysis output (after all runs)
```

---

## Success Criteria

| Metric | Target | Rationale |
|--------|--------|-----------|
| Runs completed | 25/25 | All papers × all runs |
| Verdict consistency | ≥80% same band | Users get consistent guidance |
| Signal score CV | <15% for most signals | Acceptable measurement noise |
| Classification consistency | 100% same type/approach | Structural properties stable |
| Context flag consistency | 100% same flags | Binary decisions should be deterministic |

---

## Analysis Phase

After all 25 runs complete:

### 1. Per-Paper Analysis

```bash
python3 scripts/analyse-extraction-variability.py outputs/variability-test/{paper}
```

Generates:
- Count statistics table
- Concept overlap percentages
- Pairwise similarity matrix

### 2. Cross-Paper Comparison

Compare variability patterns across paper types:
- Do empirical papers show different variability than methodological?
- Does research approach affect extraction consistency?
- Which signals show most/least variability?

### 3. Final Report

`outputs/variability-test/variability-test-summary.md`:
- Executive summary of findings
- Most/least stable signals
- Extraction → assessment correlation
- Recommendations for pipeline refinement

---

## Troubleshooting

### Run Appears to be Copy of Previous

**Symptom:** `validate-run-uniqueness.sh` reports duplicate hashes

**Cause:** Context not cleared between runs

**Solution:** Delete affected runs, ensure `/clear` between each run

### Queue Not Updating

**Symptom:** Same run keeps being selected

**Cause:** Queue file not saved after run completion

**Solution:** Check for write errors, manually update queue if needed

### Run Takes Too Long

**Symptom:** Run exceeds 90 minutes

**Cause:** Large paper or complex extraction

**Solution:** This is expected for some papers (e.g., 58-page book chapters). Let it complete.

### Assessment Scores Vary Wildly

**Symptom:** Same paper gets scores ranging 50-90

**Cause:** Likely extraction quality issue, not assessment issue

**Solution:** Check extraction counts — high count variance suggests extraction instability

---

## Lessons Learned

### From Paper 1 (sobotkova-et-al-2024)

- **RDMAP elements perfectly stable** (0% CV) — Methods, Protocols, Research Designs extracted identically across runs
- **Evidence/Claims show moderate variability** (7-12% CV) — Expected, reflects granularity decisions
- **Assessment scores very stable** (SD ~0.8 points) — Different extractions yield nearly identical assessments
- **Quote selection varies more than concepts** — Same facts cited from different passages

### From Paper 2 Initial Attempt

- **Context contamination is real** — Runs 03-05 were copies when done in same session
- **Context clearing essential** — Each run must be independent session

---

## References

- Variability queue: `input/variability-queue.yaml`
- Slash command: `.claude/commands/variability-run.md`
- Validation script: `scripts/validate-run-uniqueness.sh`
- Analysis script: `scripts/analyse-extraction-variability.py`
- Scripts README: `scripts/README.md`

---

**Maintained by:** LLM Reproducibility Project
**Last Updated:** 2025-12-01
