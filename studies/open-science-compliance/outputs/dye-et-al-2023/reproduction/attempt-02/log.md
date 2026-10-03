# Reproduction Log

## Dye, Buck, DiNapoli & Philippe 2023 — attempt 02

**Paper:** Dye, T.S., Buck, C.E., DiNapoli, R.J., & Philippe, A. (2023). Bayesian
chronology construction and substance time. *Journal of Archaeological Science*,
153, 105765. <https://doi.org/10.1016/j.jas.2023.105765>. Corpus copy: White Rose
accepted manuscript (`vor.pdf`, sha256 `3039d0cc…4e9`); supplement mmc1.pdf
(`supplement-1.pdf`, sha256 `9b497fc2…b71`). Both are referenced by path from the
corpus store and never copied here.

**Run:** `phase2-shakedown-2026-10`, attempt 2. Launch commit
`e5f35543c07d2a9314d1742ff34df40a12bd35fd`. Executor: reproduction-executor
v1.1 (model `claude-opus-5-5`, effort pinned high).

**Approval check (before any work):** `sha256sum reproduction-plan.json` gave
`7ff05a24d1342b84ebe5f61f2f0e7b15df040baf73ad1c67aa13c63ff49f0f35`. This equals
the hash in the spawn prompt and `plan_sha256` in `plan-approval.json`, whose
decision is `approve` (Shawn Ross, 2026-10-03T11:57:16Z).

### Timeline

Times are UTC on 2026-10-03.

| Time | Activity | Duration |
|------|----------|----------|
| 11:57 | Verified the plan hash and approval record; read the plan, schema, templates, and pulled references | 2 min |
| 11:59 | Fetched beads-1.csv, ArchaeoPhases 1.8, and mmc2.zip, each hashed (all match the plan); re-probed beads-0/2/3/4 (404) | 1 min |
| 12:01 | Docker build, iteration 1, succeeded first time | 7 min 24 s |
| 12:02 | Transcribed the supplement code (tool written, two parser fixes, see Modifications); checked against rendered PDF pp. 26 and 31-33 | ~8 min, during the build |
| 12:10 | Label check in Docker: 77/77 `pos` and 68/68 `bead_list` labels found; section 4 index 78 exceeds 77 columns | < 1 min |
| 12:11 | First full run of the authors' code (development run) | 2 min |
| 12:13 | Read paper pp. 7-22 and supplement pp. 47-49; high-resolution renders of Figs 2, 4, and 6 (scratch) | ~6 min |
| 12:16 | Fixed the tempo-plot output capture; wrote and ran the R1 verification aids | ~5 min |
| 12:21 | Wrote `comparisons/published-values.csv` and `scripts/compare.R`; first comparison run | ~3 min |
| 12:23 | Cleaned the development outputs; final clean pipeline run (`run-all.sh`, `--user` host uid) | 56 s |
| 12:25 | Documentation, comparison report, `comparison.json`, and self-check gate (pass at 12:30:41) | ~7 min |
| **Total** | | **about 35 min** (11:57-12:32) |

### Materials Acquired

| Artefact | Source URL or DOI | Retrieved (UTC) | SHA-256 | Destination |
|----------|-------------------|-----------------|---------|-------------|
| `beads-1.csv` | <https://tsdye.online/AP/beads-1.csv> (HTTP 200, Last-Modified 2022-10-20 16:24:44 GMT, 3,688,071 bytes) | 2026-10-03 11:59 | `02cf52d4ace408b6329e69e7a0e4bd457084ae9605f2fa5eccc2abad20ab9051` (identical before and after the copy) | attempt-dir `data/beads-1.csv` (author-released data) |
| `beads-0.csv` | <https://tsdye.online/AP/beads-0.csv> | 2026-10-03 11:59 | not hashable: HTTP 404, no file received | none |
| `beads-2.csv` | <https://tsdye.online/AP/beads-2.csv> | 2026-10-03 11:59 | not hashable: HTTP 404, no file received | none |
| `beads-3.csv` | <https://tsdye.online/AP/beads-3.csv> | 2026-10-03 11:59 | not hashable: HTTP 404, no file received | none |
| `beads-4.csv` | <https://tsdye.online/AP/beads-4.csv> | 2026-10-03 11:59 | not hashable: HTTP 404, no file received | none |
| (directory probes) | <https://tsdye.online/AP/> (HTTP 403); <https://tsdye.online/AP/beads-0.csv.gz> (404); <https://tsdye.online/beads-0.csv> (404) | 2026-10-03 11:59 | not hashable: no file received | none |
| `ArchaeoPhases_1.8.tar.gz` | <https://cran.r-project.org/src/contrib/Archive/ArchaeoPhases/ArchaeoPhases_1.8.tar.gz> | 2026-10-03 11:59 | `728a0d0c3a487e8f90b8c550a977a7678855d0c355a0347629d4a4afd5a5a801` | attempt-dir `vendor/` (GPL-3 CRAN source; verified again inside the Docker build) |
| `mmc2.zip` (contains `beads.oxcal`, 19,123 bytes, dated 2023-03-23) | <https://ars.els-cdn.com/content/image/1-s2.0-S0305440323000432-mmc2.zip> | 2026-10-03 11:59 | `28133a3b1139b08d698982daea29b1042f9a51d2ca419b27ebd7233d6d6e20a7` | scratch only (publisher content; for provenance, not used by this attempt) |
| `rocker/r-ver:4.2.3` base image | Docker Hub `docker.io/rocker/r-ver:4.2.3` | 2026-10-03 12:01 | `sha256:6dff804fb051f7c38cf9ebcaf307b5102b46e5187ffe2ce921d760a26facd693` (image digest) | Docker build cache |
| CRAN dependencies (137 packages, Ubuntu jammy binaries) | <https://packagemanager.posit.co/cran/__linux__/jammy/2023-03-23> | 2026-10-03 12:01-12:08 | not hashed individually: `install.packages()` inside `docker build` does not expose per-file digests. The date-frozen snapshot URL is the identifier, and the versions are in `outputs/logs/session-info.txt` and `outputs/logs/docker-build.log` | Docker image layer |
| Paper (accepted manuscript) | corpus store `/home/shawn/corpora/llm-reproducibility/dye-et-al-2023/vor.pdf` (not fetched; local holding) | read 2026-10-03 | `3039d0ccb2e443855b082d65b50044f72da17afc3b06b9bb93398fd1c644e4a9` | corpus store (referenced by path only) |
| Supplement mmc1.pdf | corpus store `/home/shawn/corpora/llm-reproducibility/dye-et-al-2023/supplement-1.pdf` (not fetched; the plan records it as byte-identical to the journal mmc1.pdf) | read 2026-10-03 | `9b497fc23ef378621a03de6ef447a4309bc81be80b2cd882cfb48953f7018b71` | corpus store (referenced by path only) |

All five retrieval attempts for the four replicate runs failed, so those rows
carry no digest. Text extraction (`pdftotext -layout`) and page renders of the
two PDFs went to the scratch directory only.

### Modifications Required

Every change below alters *how* the code runs, never *what* it computes
(invariant 2). Each was checked against that rule; none changes a statistical
method, parameter, data filter, model specification, or analysis step.

1. **Transcription of printed code** (`tools/transcribe_supplement.py` builds
   `authors-code-raw/`):
   - The authors' R code exists only as listings in the supplement PDF
     (sections 3-10).
   - The tool keeps numbered listing lines, strips the line numbers, rejoins
     `↪` continuation lines with one space (the listings break only at
     whitespace), and replaces typographic quotes with ASCII quotes.
   - Two parser bugs were found and fixed before any use. (a) Python's
     `str.splitlines()` also splits on the form feeds pdftotext puts at page
     breaks, which shifted every section range; the tool now splits on `\n`
     only. (b) A listing line at the top of a page starts with a form feed and
     was missed, which dropped `pos <-` (section 3), `library()` (section 9),
     the `"BE1-Amethyst"` entry (section 10.3), and a comment (section 10.4).
     The tool now strips leading form feeds.
   - The result was checked by eye against rendered supplement pp. 26 and
     31-33, and by `scripts/check-labels.R`. All 77 section 3 `pos` labels
     (identical to the CSV column order) and all 68 distinct `bead_list` labels
     match `beads-1.csv` column names exactly (`outputs/checks/label-check.txt`).
   - Authors' quirks were kept verbatim: the duplicated
     `"SUERC-51539 (ERL G353)"` in section 5.32, the stale "Figure 7/8"
     numbering, and section 4's indices and x-limits.
2. **Path-only edits** (`authors-code/`, each marked inline `LLMR-PATH:`):
   - `read_oxcal("https://tsdye.online/AP/beads-1.csv")` becomes
     `read_oxcal("data/beads-1.csv")`, the verified local copy with the same
     sha256 (sections 4 and 6-10, except 10.4).
   - In section 10.4, the author-local
     `"/home/dk/Projects/hierarchical-sequence-prior/phyletic-seriation/project_source/lakenheath/beads-1.csv"`
     becomes `"data/beads-1.csv"`.
   - In section 3, the placeholders `/path/to/beads-N.csv` become
     `data/beads-N.csv`. The section is not executed because four inputs are
     missing.
   - Output files `all-burials.pdf` and `test-bead-tempos.pdf` are written to
     `outputs/`.
3. **Batch wrapper** (`run-analysis.R`):
   - Sources each section into one global environment, in supplement order,
     with section 5 before sections 6-10, as the supplement instructs.
   - `tryCatch` per section records an error and continues to the remaining
     independent blocks.
   - Results are captured (`res$observed` unrounded and rounded to 2 dp, the
     tempo and occurrence plot data, and `bead_list`), and a null default
     device absorbs the `dev.new()` previews.
   - Section 6 (tempo plot) runs after sections 7-10 rather than between 5
     and 7. It only reads `bead_list`, `bead_names`, and the MCMC file, and
     sections 7-10 do not depend on it, so no value can change; the reordering
     is recorded here as a deviation from plan step 4.
   - One capture fix after the development run: the `tempo_plot()` return
     value is a list of 23 per-type data frames, not an object with `$x`, so
     the CSV writer was corrected to stack them.
4. **Dockerfile construction** (1 iteration): `rocker/r-ver:4.2.3`, PPM
   2023-03-23 snapshot, system libraries for proj4, igraph, and Cairo, and
   ArchaeoPhases 1.8 from the vendored archive tarball with an in-build sha256
   check. The image built on the first attempt.
5. **Verification aids and comparison** (`scripts/verification-aids.R` and
   `scripts/compare.R`; ruling R1; separate from the authors' code):
   - The aids only call documented exports, `allen_illustrate()` and
     `allen_observe()`, and make read-only lookups in `beads-1.csv` and in the
     authors'-code outputs.
   - Display-only arguments (`plot_title`, `file_name`) are passed through the
     documented `...`.
   - Supplement Figure 3's left panel uses `allen_illustrate("transform")`, the
     composition m∘m, which renders exactly the published set {p}.
6. **Output ownership:** the development runs ran as root inside the container
   and left root-owned files. These were removed through the container, and the
   final run used `--user $(id -u):$(id -g)`.

### Outputs Generated

| File | Description | Size |
|------|-------------|------|
| `outputs/test-bead-tempos.pdf` | Paper Figure 4 (tempo plots, 23 bead types), from the authors' section 6 code | 104 KB |
| `outputs/authors/section-0{7,8,9}-observed*.{csv,rds}` | Sections 7-9 `allen_observe_frequency` matrices (oFD, oFD, oFDm), unrounded and rounded to 2 dp | ~12 KB each |
| `outputs/authors/section-10-{1..9}-observed*.{csv,rds}` | Section 10 rows 1-9 ('p') matrices (Supplement Tables 2-10) | ~12 KB each |
| `outputs/authors/section-06-tempo-data.csv`, `section-06-tempo-plot-object.rds` | Tempo plot data (23 types, 10,800 rows) | 668 KB, 128 KB |
| `outputs/authors/section-05-bead-list.rds` | `bead_list` and `bead_names` after sections 5.1-5.38 | 12 KB |
| `outputs/aids/` | R1 aid outputs: Fig 2 lattices (6 PDFs plus CSV), Supp Figs 1 and 3 lattices (PDFs plus CSV), the 54 relations, histogram bins, and the Supp Fig 2 PDF | 352 KB |
| `outputs/checks/label-check.txt`, `section-04-index-check.txt` | Transcription and label check | < 4 KB |
| `outputs/logs/` | `run-all-console.txt`, `run-analysis-transcript.txt`, `section-status.csv`, `session-info.txt`, `docker-build.log`, `input-checksum.txt`, `output-checksums.txt` | 272 KB |
| `comparisons/values/T01-…csv` to `T34-…csv` | Value-level comparison per locked target (36 files) | 440 KB |

No `all-burials.pdf` was produced: section 4 stops with an error (see the
findings below).

### Findings during execution

1. **Section 4 (paper Fig 3) cannot run on the published data.**
   `burial.dates <- c(3:5, 7, 9, 12:78)` indexes column 78, but
   `read_oxcal()` (ArchaeoPhases 1.8) drops the `Pass` and empty trailing
   fields, leaving 77 columns. `occurrence_plot()` therefore stops with
   "undefined columns selected". The code also sets `x_min = 500, x_max = 700`,
   while the published axis spans about 400-800. Together these suggest the
   published figure came from a different file layout or package version than
   the published code and data. Correcting the indices would change the data
   selection, so it was not done (invariant 2).
2. **Suspected paper error (T06).** The paper (p.16 l.374-376) gives
   BE1-Cowrie(oFD)BE1-Disc = 0.87. The authors' section 7 code on the
   published data gives 0.99967 (2 dp: 1.00). The value 0.87 does appear in
   the same matrix, as BE1-Amethyst(oFD)BE1-Disc = 0.86717. Matrix orientation
   (row = ancestor) is confirmed by T05: BE3-Amber(oFD)BE1-Amethyst = 1 and the
   converse = 0. All 54 tabulated values in Supplement Tables 2-10 reproduce
   exactly with the same inputs and code. This is escalated for human
   confirmation.
3. **Internal inconsistency (approver ruling: record as a finding, not a
   target).** Supplement section 10.5 says "The nine Earlier(p)Later relations"
   (p.42), while the same subsection says "Each of the six relations" (p.41).
   Table 6 has 6 cells, and the reproduction gives 6.
4. **Typo in the supplement prose:** "weere" (section 10.9, p.45) has no
   analytical effect.
5. **Blinding note:** one host directory listing of
   `.claude/skills/reproduction-assessor/references/`, made to locate the two
   pulled references, displayed the names of two blinded entries in that
   directory. Neither was opened, read, searched, or listed further.

### Findability, Accessibility, Interoperability, and Reusability (FAIR) / Machine-Actionability Findings

1. **Code only as printed PDF listings:** the authors' R code is typeset in the
   supplement PDF, with no script file. Line wrapping breaks string literals,
   and page breaks interleave prose, so a transcription tool plus a label check
   were needed before the code could run in batch.
2. **Data persistence:** the one published MCMC output is served from a
   personal server (`tsdye.online`) without a persistent identifier. The
   directory index returns 403. The file was unchanged since 2022-10-20 and
   matched the planner's hash.
3. **Unfulfilled availability claim:** "Data and materials are available in the
   Supplement" does not cover the four further OxCal runs (`beads-0/2/3/4.csv`)
   needed for Supplement Table 1. The supplement code uses `/path/to/`
   placeholders, and the server returns 404. Paper-level data availability is
   L6 under the plan's two-dataset enumeration (see `environment.md` for the
   sensitivity note).
4. **Author-local path in published code:** section 10.4 reads
   `/home/dk/Projects/…/beads-1.csv`.
5. **Environment specification:** no R version, no package versions, no
   `sessionInfo()`, no lockfile, and no container: level 0. The code depends on
   ArchaeoPhases functions removed after version 1.8.
6. **Code-data drift:** section 4's column indices do not fit the published
   `beads-1.csv` (finding 1).
