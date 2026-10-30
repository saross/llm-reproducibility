# Reproduction Log

## Herskind and Riede 2024 (attempt 04)

**Paper:** Herskind, L.L.P. and Riede, F. (2024). A computational linguistic
methodology for assessing semiotic structure in prehistoric art and the
meaning of southern Scandinavian Mesolithic ornamentation. *Journal of
Archaeological Science* 165, 105969. <https://doi.org/10.1016/j.jas.2024.105969>

**Run:** gate-1-3-1-pilot-rerun-2026-10, attempt 4; launch commit
`6b1850554def6a563d82a5409dd821f56b4cb1d4`; executor: reproduction-executor
v1.7 (claude-opus-5-5, reasoning effort high).

### Timeline

All times UTC, 2026-10-17.

| Time | Activity | Duration |
|------|----------|----------|
| 05:16 | Approval verified: `reproduction-plan.json` sha256 `6837cf60...553d` equals the spawn hash and the approval record's `plan_sha256`; decision "approve" (2026-10-13). Instruments verified (verdicts-and-precision 1.1, coverage-rules 1.1, pipeline invariants 1.1) | 2 min |
| 05:18 | Zenodo record 10801706 metadata fetched; the four deposit files downloaded into `deposit/`; all md5s match Zenodo's published checksums | 1 min |
| 05:19 | Read the authors' S2.R and README in full; read the paper (9 pages) in full | 3 min |
| 05:20-05:28 | **Published values transcribed** into `published-values/` (Tables 1-3, named values; Fig. 3 labels by eye and bars by pixel measurement; Fig. 2 bars; Fig. 4 axis order and 290 boxes by pixel detection, checked by overlay; Fig. 5 pies). Completed before any build or run | 8 min |
| 05:28 | Dockerfile and `install-pins.R` written | 2 min |
| 05:29-05:34 | Image built through the lane (build-01): all seven pins at their supplied versions, 0 fallbacks | 4.5 min |
| 05:34-05:37 | `run-analysis.R`, `verification-aids.R`, `run.sh`, and `authors-code-manifest.json` written; `check-code` run (passes apart from "no run yet") | 3 min |
| 05:37 | run-01: the authors' script completed; the verification-aids process failed (`colSums` on a dfm without quanteda attached). Fixed in the aid (`Matrix::colSums`) | 10 s |
| 05:38 | run-02: complete. The T01 map aid found S1's coordinate columns are text ("-" marks an unknown location); fixed in the aid | 11 s |
| 05:39 | run-03: complete. The plan's T01 method names the ggplot layer data; the wrapper was extended to export it | 10 s |
| 05:40 | run-04: complete. The comparison showed 15-digit rounding in the exported matrix m (`write.csv`); the wrapper was changed to write m at 17 digits | 11 s |
| 05:43 | **run-05: complete (final, credited run)**; exit 0; only the declared line-27 tolerance fired | 12 s |
| 05:44-06:05 | Comparisons (`comparisons/compare.py` on run-05), comparison.json, report, environment.md, this log; `check-attempt` self-check | ~20 min |
| **Total** | | **~50 min** |

### Materials Acquired

| Artefact | Source URL or DOI | Retrieved (UTC) | SHA-256 | Destination |
|----------|-------------------|-----------------|---------|-------------|
| `Herskind&Riede_S1.xlsx` | <https://zenodo.org/api/records/10801706/files/Herskind&Riede_S1.xlsx/content> (DOI 10.5281/zenodo.10801706) | 2026-10-17T05:18:48Z | `d76b9d6328465658aa1582c5c8de0912f9167ff1f8c737bd7998d91fd5692030` | attempt-dir `deposit/` (md5 `0bcde6d178b5a8f3da80a023a64ff510` = Zenodo's) |
| `Herskind&Riede_S2.R` | <https://zenodo.org/api/records/10801706/files/Herskind&Riede_S2.R/content> | 2026-10-17T05:18:49Z | `487a00a09db92b484dac136f13a5745a3a2ac699c3a01cfccf528d4d550a8720` | attempt-dir `deposit/` (md5 `6760ccb30ecc1de7c280bc1e0fa182e5` = Zenodo's) |
| `Herskind&Riede_S3.xlsx` | <https://zenodo.org/api/records/10801706/files/Herskind&Riede_S3.xlsx/content> | 2026-10-17T05:18:51Z | `1199acac5d1edb916dc4528d5e994295e206e798cb132e91c3be59cc9e328eed` | attempt-dir `deposit/` (md5 `812be5456d7e0e2adb97ecb5a975239e` = Zenodo's) |
| `README.txt` | <https://zenodo.org/api/records/10801706/files/README.txt/content> | 2026-10-17T05:18:52Z | `cdaae0824c92137375537cc962c7016a6ce71eecdd2bb90dba7e604755786679` | attempt-dir `deposit/` (md5 `8b5ef4c5a8c1f75c5d61ed25f799521b` = Zenodo's) |
| Zenodo record metadata (record-10801706.json) | <https://zenodo.org/api/records/10801706> | 2026-10-17T05:18:34Z | Not kept as an artefact (API response used only to read file keys and checksums; the committed evidence pack holds the same checksums) | scratch |
| Paper PDF (version of record) | corpus store `~/corpora/llm-reproducibility/herskind-riede-2024/vor.pdf` (not fetched; publisher content) | already held | `5c60cc3d6fce9f297c44fc62384e0caada1251416066d872ea020feec145fad0` | corpus store; figure images extracted into scratch only |
| R packages (7 pins, 44 unspecified) | CRAN archive tarballs; Posit Package Manager snapshot 2024-04-03 | 2026-10-17 (build-01) | Not hashed individually; build log `lane-records/build-01/build.log` (sha256 `4438e4dcbf6a498551ef1dc3e534ad24d41248aa1b4589b6601eda51adfd04d0`) records every URL | Docker image |
| Base image `rocker/r-ver:4.3.2` | Docker Hub | previously pulled to the host | local image id `f0b4e058dcfa` | Docker |

Data retrieval (per dataset, for the L-level):

- **S1 analysis dataset.** Route: the data availability statement's Zenodo
  record 10801706. Steps: one unauthenticated HTTPS GET of the file's
  content link; md5 checked against Zenodo's published value. Outcome:
  retrieved, identical to the published checksum. No registration or
  permission needed. **L1 (open-complete).** No other dataset is required by
  any target (Plonka 2003 is upstream provenance; S3 is a published-values
  reference, retrieved by the same route).

### Modifications Required

No line of the authors' code was edited. `deposit/Herskind&Riede_S2.R` ran
byte-identical (sha256 checked by the wrapper at run time and by the gate
from the run records). Every mechanic is in a declared wrapper.

1. **Dockerfile construction** (1 build, 0 failures):
   - The authors give R and package versions in the README but no container
     or lockfile.
   - Built `rocker/r-ver:4.3.2` with a UTF-8 locale, compilers, ICU/libxml2,
     and cairo/fontconfig/fonts; `install-pins.R` installed the seven pins
     from CRAN tarballs and their unspecified dependencies from the
     2024-04-03 Posit snapshot, with the capped version search (not needed:
     every pin built first time) and an asserted inventory.
   - Departure from the plan's wording (environment only, nothing computed):
     the plan's step 3 mentions `remotes::install_version`; the build used
     the reproducer's own script reading CRAN's archive directly, as
     `dockerfile-patterns.md` ("Package repository dates") prescribes, so
     `remotes` was not installed.
2. **Script adaptation** (wrapper `run-analysis.R`, entry `run.sh`):
   - Working directory set to `deposit/`, where S2.R reads
     "Herskind&Riede_S1.xlsx" and writes its outputs. The plan's step 4 said
     the wrapper would copy S1 and S2 into a working directory; running them
     in place in the lane's private work copy does the same without making a
     second code file.
   - S2.R run statement by statement with the lane's evaluator,
     `getOption("lane.hook")$run_file("Herskind&Riede_S2.R", tolerate = 27L,
     encoding = "UTF-8")`. **Declared tolerance, line 27**
     (`font_import(pattern = "GIL", prompt = FALSE)`): **it fired** in every
     run ("arguments imply differing number of rows: 0, 1"; no Gill Sans
     font in the image). It registers fonts and computes nothing that enters
     a result. No other statement errored (the run's EVAL records).
   - Default graphics device set to a cairo PNG device
     (`options(device = ...)`). S2.R prints its ggplot objects (lines 70,
     411, 432, 607-612, 690); in the authors' RStudio session these went to
     the on-screen device. Under Rscript the default `pdf()` device has no
     "Gill Sans MT" family. The PNG device only receives those prints
     (`Rplot001-010.png`); every figure the paper uses is written by the
     authors' own `ggsave()` calls, which open their own device.
   - Output capture after the script ends: the authors' objects (the four
     Table 1 frequency tables and lengths, the three Table 2 summaries, the
     six Fig. 3 plots' data and drawn labels, the Fig. 2 plot's built layer
     data, the matrix m, and objects for the aids) written under `captured/`
     without recomputation. Per-section error capture was not needed.
3. **Verification aids** (`verification-aids.R`, a separate R process,
   labelled under ruling R1): read-only S1 lookups and documented
   quanteda/readxl/ggplot2 calls for the targets with no authors' code.
   Mechanical fixes during the runs: `Matrix::colSums` for a dfm (run-01),
   and reading S1's text coordinate columns as numbers with "-" as missing
   (run-02). Neither touches the authors' code or computation.
4. **Comparison-method deviation (T13)**, declared in `comparison.json`: the
   plan's source object `token_freqs` is local to the authors' function and
   cannot be captured; the aid computes the same quantity with the same
   quanteda calls on the authors' corpus, cross-checked with the authors'
   global `freqs`.

### Published-values transcription timing

All files in `published-values/` were written between 05:20 and 05:28 UTC,
before the image build (05:29) and the first `run-container` call (05:37).
Nothing was transcribed late. Two transcription aids
(`published-values/measure_fig3_bars.py`, `detect_fig4_boxes.py`) were run
on the host against the published figure images only; they are declared
tooling.

### Outputs Generated

Final credited run: `outputs/run-05/` (sealed in `lane-records/run-05/`).

| File | Description | Size |
|------|-------------|------|
| `outputs/run-05/files/deposit/artefact_type_chronology.png` | Fig. 2 bar panel (authors' ggsave) | 45,711 B |
| `outputs/run-05/files/deposit/bigramsBYfrequency.png`, `bigramsBYpmi.png`, `trigramsBYfrequency.png`, `trigramsBYpmi.png`, `quadrigramsBYfrequency.png`, `quadrigramsBYpmi.png` | Fig. 3 panels a-f (authors' ggsave) | 163-211 kB each |
| `outputs/run-05/files/deposit/heatmapPMI.png` | Fig. 4 skeleton (authors' ggsave) | 181,151 B |
| `outputs/run-05/files/deposit/Bigrams.csv`, `Trigrams.csv`, `Quadrigrams.csv` | S3 tables (authors' fwrite) | 8,288 / 6,063 / 1,377 B |
| `outputs/run-05/files/deposit/Rplot001-010.png` | The script's interactive prints (wrapper's default device) | 13-59 kB each |
| `outputs/run-05/stdout.log` | Console: head() prints, Table 1 tables (lines 50-69), Table 2 summaries (lines 112-117) | 5,877 B |
| `outputs/run-05/files/captured/table1-*.csv`, `table2-reproduced.csv`, `*_ksngram_subset.csv` | Table 1 and 2 values from the authors' objects | small |
| `outputs/run-05/files/captured/fig2-*.csv`, `fig3-reproduced.csv`, `fig4-matrix-m.csv` | Plot data and matrix m | 0.5-16 kB |
| `outputs/run-05/files/captured/aid-*.csv`, `aid-*.png` | Verification aids (ruling R1) | small |
| `outputs/run-05/files/captured/session-info.txt`, `package-inventory.csv`, `pin-attempts.csv`, `runtime-notes.txt` | Environment record | small |
| `outputs/run-05/files/captured/authors-objects.rds` | The authors' corpus, tokens, k, t, and frequency objects, for the aids | 21,353 B |

Runs 01-04 are superseded (kept by the lane as evidence; not credited).

### Findability, Accessibility, Interoperability, and Reusability (FAIR) / Machine-Actionability Findings

1. **Data and code access:** all supplementary files are on Zenodo under
   CC-BY-4.0, with persistent identifiers and published checksums, and
   download without authentication (L1).
2. **Version ambiguity:** the methods cite Zenodo record 10623550 and the
   data availability statement cites 10801706; the concept DOI holds four
   records, and the S1 data differ between 10623550 and 10801706 (md5 and
   size in the evidence pack). Table 1 appears to reflect a different data
   state from the deposited S3 (see the comparison report, T05).
3. **Environment specification:** R and package versions are given in the
   README (level 2), and they disagree with the paper's R 4.2.2; no lockfile
   or container. All pins still build from CRAN's archive.
4. **Code batch-readiness:** S2.R runs top to bottom without interaction
   once the working directory is set; it depends on a proprietary font only
   for appearance, and its `font_import()` call fails harmlessly.
5. **Unscripted outputs:** the Fig. 2 and Fig. 5 maps, Table 3, and the
   GIMP annotations on Figs 3 and 4 have no code; their criteria (the
   Fig. 4 box rule, the Fig. 5 extent patches) are unpublished.
6. **Data format:** S1 records unknown coordinates as "-", so its coordinate
   columns read as text rather than numbers.
