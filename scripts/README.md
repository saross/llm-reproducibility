# Project Scripts

Utility scripts for variability testing, validation, and analysis.

**Last Updated:** 2025-12-01

---

## Overview

This directory contains project-level utility scripts that support the variability testing workflow and extraction quality assurance. These are distinct from the extraction-system scripts which handle per-paper extraction workflows.

---

## Quick Reference

| Script | Purpose | When to Use |
|--------|---------|-------------|
| `analyse-extraction-variability.py` | Compute variability metrics across runs | After completing multiple runs of same paper |
| `validate-run-uniqueness.sh` | Verify runs have unique content (not copies) | After completing variability test runs |
| `batch-assess.py` | Rapid quality assessment across extractions | Batch validation, quality comparison |
| `install-git-hooks.sh` | Install pre-commit hooks | Initial setup, new clones |
| `quick_infrastructure_scan.py` | Scan codebase for infrastructure patterns | Exploratory analysis |

---

## Variability Testing Scripts

### analyse-extraction-variability.py

**Purpose:** Analyse extraction variability across multiple runs of the same paper. Computes count statistics, concept overlap, and pairwise similarity metrics.

**Usage:**

```bash
# Basic usage - console output
python3 scripts/analyse-extraction-variability.py outputs/variability-test/sobotkova-et-al-2024

# JSON output
python3 scripts/analyse-extraction-variability.py outputs/variability-test/sobotkova-et-al-2024 --json

# Custom similarity threshold (default: 0.5)
python3 scripts/analyse-extraction-variability.py outputs/variability-test/sobotkova-et-al-2024 --threshold 0.3

# Save to file
python3 scripts/analyse-extraction-variability.py outputs/variability-test/sobotkova-et-al-2024 --json --output analysis.json
```

**Metrics Computed:**

1. **Count Statistics** — For each extraction array (evidence, claims, implicit_arguments, methods, protocols, research_designs):
   - Mean, standard deviation, coefficient of variation (CV%)
   - Min, max, range across runs

2. **Concept Overlap** — Token-based Jaccard similarity:
   - Core agreement percentage (concepts in ALL runs)
   - Unmatched items in other runs
   - Uses first run as reference

3. **Pairwise Similarity** — Pooled vocabulary comparison:
   - Jaccard similarity between all run pairs
   - Average similarity across pairs

**Output Example:**

```text
======================================================================
EXTRACTION VARIABILITY ANALYSIS: sobotkova-et-al-2024
======================================================================
Runs analysed: 5 (run-01, run-02, run-03, run-04, run-05)

COUNT STATISTICS
----------------------------------------------------------------------
Array                    Mean   StdDev      CV%      Range
----------------------------------------------------------------------
evidence                 15.4     1.14     7.4%      14-17
claims                   13.4     1.52    11.3%      12-16
...
```

**Interpretation Guidelines:**

| CV% | Interpretation |
|-----|----------------|
| 0-5% | Very stable (structural elements like RDMAP) |
| 5-15% | Acceptable variability (typical for evidence/claims) |
| >15% | High variability (investigate cause) |

**Dependencies:** Standard library only (json, re, statistics, pathlib, argparse)

**Extension Points:** Script is designed to be extended with:
- Sentence embeddings for semantic similarity (sentence-transformers)
- Inter-rater reliability metrics (Krippendorff's alpha)
- Cluster analysis for concept grouping

---

### validate-run-uniqueness.sh

**Purpose:** Validate that all variability test runs have genuinely unique content (not copies of each other). Prevents the failure mode where runs are accidentally duplicated.

**Usage:**

```bash
./scripts/validate-run-uniqueness.sh outputs/variability-test/penske-et-al-2023
```

**Validation Checks:**

1. **Evidence array uniqueness** — MD5 hash of serialised evidence array
2. **Claims array uniqueness** — MD5 hash of serialised claims array
3. **Implicit arguments uniqueness** — MD5 hash of serialised implicit_arguments array

**Output Example:**

```text
Checking content uniqueness for: outputs/variability-test/penske-et-al-2023
Found 5 extraction files

=== Evidence Array ===
  run-01: faedad836e666e5e261d39c8f8202760
  run-02: 689f5ca8c973487c98278c63e4fa3ef1
  run-03: 102007e3176222ed3b9554d42e804bb7
  run-04: 309a3e315bec770c6a2f98391e33929d
  run-05: 7e975b6f29532b0d9a91c6fd535b18e9
  ✅ All 5 runs have unique evidence content
...

=== Summary ===
✅ All content arrays have unique values across all runs
```

**Exit Codes:**
- `0` — All runs have unique content
- `1` — Duplicate content detected (some runs may be copies)

**When to Use:**
- After completing variability test runs for a paper
- Before committing variability test outputs
- When investigating suspected copy errors

**Dependencies:** bash, jq, md5sum

---

## Other Scripts

### batch-assess.py

**Purpose:** Rapid quality assessment metrics across multiple extractions.

See `extraction-system/scripts/README.md` for detailed documentation.

### install-git-hooks.sh

**Purpose:** Install pre-commit hooks for the repository.

**Usage:**

```bash
./scripts/install-git-hooks.sh
```

**Installs:**
- Filename convention enforcement (lowercase-with-hyphens)
- Other project-specific hooks

### quick_infrastructure_scan.py

**Purpose:** Exploratory script for scanning codebase infrastructure patterns.

---

## Related Documentation

- **Extraction System Scripts:** [extraction-system/scripts/README.md](../extraction-system/scripts/README.md)
- **Variability Test Plan:** [planning/](../planning/) (see variability test planning documents)
- **Schema Reference:** [extraction-system/schema/README.md](../extraction-system/schema/README.md)

---

## Development Guidelines

Per project CLAUDE.md guidelines:

1. **Header blocks required** — Scripts need purpose, usage, author, date
2. **Function docstrings** — All functions need documentation
3. **Inline comments** — Complex logic needs explanation
4. **UK spelling** — Use British/Australian spelling throughout

### Adding New Scripts

```python
#!/usr/bin/env python3
"""
script-name.py

Brief description of purpose.

Usage:
    python3 scripts/script-name.py <arguments>

Example:
    python3 scripts/script-name.py outputs/paper-name

Author: [name]
Date: YYYY-MM-DD
"""
```

---

**Version:** 1.0
**Maintained by:** LLM Reproducibility Project
