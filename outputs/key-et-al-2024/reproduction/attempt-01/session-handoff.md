# Session Handoff: Key et al. 2024 Reproduction

**Session:** R-Plan (Planning)
**Date:** 2026-02-10
**Status:** R-Plan COMPLETE — data availability audit done, plan approved

---

## What Was Accomplished

1. **Paper analysis:** Read full 20-page paper, all 3 supplementary R scripts,
   empty CSV template, and supplementary document (mmc5.docx)
2. **Classification:** Type C (interactive scripts, no Dockerfile, no renv)
3. **Comprehensive data search:** 10 parallel search agents traced all 13
   source datasets across Zenodo, Figshare, GitHub, Springer ESM, UCL
   Discovery, PLoS ONE, Nature, PIDBA, tDAR, OSF, and institutional repos
4. **Data retrieved:** 3 of 13 datasets downloaded and verified (Olduvai
   cleavers, Paleoindian points, geometric microliths)
5. **Inventory written:** `data-availability-inventory.md` with full access
   levels, record counts, provenance chains, and reproducibility metrics

## Key Findings

- **Record-weighted data availability: 42.6%** (2,149 of 5,042 artefacts)
- **Dataset-count availability: 23.1%** (3 of 13 datasets at Level 0)
- **9 datasets Level 3** (exist but inaccessible — co-author-held or in monographs)
- **1 dataset Level 4** (replica archaic points — never published)
- **mmc4.csv is empty** (header only, 75 bytes) — probable publishing error
- **No `set.seed()` in any stochastic script** — separate reproducibility problem
- **Co-author-held data universally inaccessible** — strongest predictor of
  data availability was independent publication under data-sharing mandate

## Methodological Innovation: Data Provenance Protocol

This session developed a working protocol for papers that aggregate external
datasets (rules of engagement agreed with user):

- Machine does comprehensive search; user retrieves what machine finds but
  can't download; user does NOT do independent search
- 5-level access taxonomy (Level 0-4)
- Dual metrics: dataset-count AND record-weighted availability
- Citation-chain depth tracking
- Effort cost annotation
- Projected vs actual reproducibility comparison (feedback to research-assessor)

## Downloaded Data Locations

Data files are in `/tmp/key-et-al-data/` (EPHEMERAL — needs copying to
permanent location before next session):

- `olduvai-cleavers/olduvai-cleavers-key-et-al-2024.csv` (134 records, verified)
- `paleoindian-points/key-et-al-2024-paleoindian-points.csv` (1,281 records, verified)
- `geometric-microliths/` (7 CSV files from 3 GitHub repos, partially verified)
- `replica-assemblages/` (search reports, no data)
- `sibudu-cores/` (summary stats only)
- `capuchin-flakes/` (summary stats only)
- `copper-tang-points/` (search reports, no data)
- `boxgrove-handaxes/` (Clark et al. n=30 alternative only)
- `ceramics/` (search report, no data)

Supplementary R scripts are in `/tmp/key-et-al-supp/extracted/`.

## Next Steps (Options)

1. **R-A with available data:** Build Docker, write wrapper, reproduce Tables
   5 (Olduvai rows), 6 (all Paleoindian), and 7 (microliths) using the 3
   downloaded datasets. Verdict would be PARTIAL.
2. **Write-up:** Incorporate data availability findings into the open science
   compliance study narrative. The finding that data availability is a bigger
   bottleneck than computational reproducibility (for these papers) is the
   headline result.
3. **Copy data to permanent location:** Move `/tmp/key-et-al-data/` to
   `outputs/key-et-al-2024/reproduction/attempt-01/source-data/` before
   the temp directory is cleaned.
4. **Update queue.yaml** with reproduction status and findings.

## Queue Status

The paper's reproduction status should be updated to reflect:
- `reproduction_attempted: true`
- `verdict: partial` (or `blocked` depending on framing)
- Data availability is the limiting factor, not code or compute
