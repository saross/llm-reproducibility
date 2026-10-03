# herskind-riede-2024 — Zenodo v1 versus v2 input-drift check

**Date:** 2026-10-03, run while stage 2 was executing. The executor never
reads this file, because it sits on a blinded path.
**Method:** `input-drift-check.py` (this directory). It downloads both
versions' S1.xlsx and S3.xlsx, verifies each against Zenodo's published md5,
and compares every cell value. Full report: `input-drift-herskind.json`.

## Result

| File / sheet | v1 cells | v2 cells | Changed | Added | Removed |
|---|---|---|---|---|---|
| S1.xlsx `Data` | 134,020 | 134,020 | 0 | 0 | 0 |
| S1.xlsx `Legend` | 9 | 9 | 2 | 0 | 0 |
| S3.xlsx `bigrams` | 1,165 | 1,165 | 0 | 0 | 0 |
| S3.xlsx `trigrams` | 966 | 966 | 0 | 0 | 0 |
| S3.xlsx `quadrigrams` | 234 | 234 | 0 | 0 | 0 |

The analysis data and the authors' precomputed reference tables are
**cell-identical** between versions. The two changed cells are
documentation in the Legend sheet: A1 changed from "…for the MA
dissertation of Lasse Lukas Platz Herskind" to "…'Supplementary
Information S1' document for the article…", and A2 had a wording edit.
The file-size differences (S1 442,501 → 442,983 bytes; S3 31,384 → 31,598)
are therefore formatting or metadata, not data.

**Code is different.** S2.R grew from 18,707 to 33,834 bytes. Stripped of
comments, it has 220 lines in v1 and 405 in v2. v2 adds the Fig. 2 bar-panel
code (Part 2) and restructures the n-gram parts: v1 was a single-n
interactive script, re-run by hand with changed parameters. The visible
expected-frequency and PMI formulas match. This is an approximate,
comment-stripped comparison; `#` inside strings, such as hex colours, was
also stripped.

## Consequence for the regression criterion

- **Explained input drift (data):** none possible. No analysis-data or
  reference-table cell changed, so an attempt-01 to attempt-02 value
  difference cannot be explained as data drift.
- **Code-version drift:** possible in principle, not expected in values.
  S3, the authors' reference output, is identical across versions. The
  criterion v1.0 and its D1 clarification do not pre-classify a difference
  traced to the v1→v2 code restructure. If one arises, it goes to the
  registrant for a ruling rather than being labelled automatically.
