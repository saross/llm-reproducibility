# Reproduction Log

## Herskind and Riede 2024 (attempt 03)

**Paper:** Herskind, L.L.P., Riede, F., 2024. A computational linguistic
methodology for assessing semiotic structure in prehistoric art and the meaning
of southern Scandinavian Mesolithic ornamentation. *Journal of Archaeological
Science* 165, 105969. <https://doi.org/10.1016/j.jas.2024.105969>. Available
online 3 April 2024; CC BY 4.0.

**Run:** `gate-1-3-pilot-rerun-2026-10`, attempt 3; launch commit
`cd5d54ac890fafc9061547694c7d0fad9c065912`; executor reproduction-executor
v1.6, model `claude-opus-5-5`, reasoning effort high. Approved plan
`reproduction-plan.json` (sha256
`89f2c93784d4e962971fcd19b9ecdee43c9c82258f610e69b25f0d6b73df55b5`), approved
by Shawn Ross on 2026-10-11 (`plan-approval.json`, decision "approve"; the
plan's hash was checked against both the spawn brief and the approval record
before any work began).

### Timeline

All times are Coordinated Universal Time (UTC), 2026-10-11.

| Time | Activity | Duration |
|------|----------|----------|
| 11:20 | Approval verified (plan sha256 = brief = approval record); instruments v1.1 read; plan, schemas, preparation prompt, pulled references, and templates read | 2 min |
| 11:22 | Four Zenodo v2 deposit files fetched and checksummed (all md5 match) | 1 min |
| 11:23 | S2.R and README read; paper read in full; Tables 1-3 transcribed from the PDF text layer; Fig. 3 labels read at full zoom of the embedded 300 ppi image | 4 min |
| 11:26 | Dockerfile written; image built (one build, no failures) | 4.5 min |
| 11:27 | Wrapper (`run-analysis.R`), entry (`run-reproduction.sh`), comparison script, and authors' code manifest written; `check-code` run | 7 min |
| 11:34:59 | **run-01**: S2.R completed (0 untolerated errors); comparison script failed in T05 (plot aesthetics could not find `skipgram_order1`; see Modifications 4) | 9 s |
| 11:36:06 | **run-02**: complete; all targets compared; T01 discrepancy found | 10 s |
| 11:37 | Visual review of Figs 2, 3, 4, 5 against the published figures; Fig. 4 boxes found to cover co-occurrences of any frequency | 3 min |
| 11:39:52 | **run-03**: complete; T01 element count and paper-error evidence added; extended Fig. 4 aid | 10 s |
| 11:40 | Published Fig. 4 and Fig. 2 transcribed cell by cell and segment by segment with the reading tools; Fig. 5 pies read at 4x zoom | 6 min |
| 11:46:44 | **run-04** (final, credited): complete, exit 0; all 20 targets scored | 10 s |
| 11:47 | `check-attempt` (artefacts missing only); documents written | 15 min |
| **Total** | | **about 45 min** |

### Materials Acquired

| Artefact | Source URL or DOI | Retrieved (UTC) | SHA-256 | Destination |
|----------|-------------------|-----------------|---------|-------------|
| `Herskind&Riede_S1.xlsx` | <https://zenodo.org/api/records/10801706/files/Herskind&Riede_S1.xlsx/content> (DOI 10.5281/zenodo.10801706, v2) | 2026-10-11T11:22:26Z | `d76b9d6328465658aa1582c5c8de0912f9167ff1f8c737bd7998d91fd5692030` | attempt dir, `materials/` (md5 `0bcde6d178b5a8f3da80a023a64ff510` = Zenodo) |
| `Herskind&Riede_S2.R` | <https://zenodo.org/api/records/10801706/files/Herskind&Riede_S2.R/content> | 2026-10-11T11:22:27Z | `487a00a09db92b484dac136f13a5745a3a2ac699c3a01cfccf528d4d550a8720` | attempt dir, `materials/` (md5 `6760ccb30ecc1de7c280bc1e0fa182e5` = Zenodo) |
| `Herskind&Riede_S3.xlsx` | <https://zenodo.org/api/records/10801706/files/Herskind&Riede_S3.xlsx/content> | 2026-10-11T11:22:28Z | `1199acac5d1edb916dc4528d5e994295e206e798cb132e91c3be59cc9e328eed` | attempt dir, `materials/` (md5 `812be5456d7e0e2adb97ecb5a975239e` = Zenodo) |
| `README.txt` | <https://zenodo.org/api/records/10801706/files/README.txt/content> | 2026-10-11T11:22:32Z | `cdaae0824c92137375537cc962c7016a6ce71eecdd2bb90dba7e604755786679` | attempt dir, `materials/` (md5 `8b5ef4c5a8c1f75c5d61ed25f799521b` = Zenodo) |
| `rocker/r-ver:4.3.2` | docker.io (pulled; already up to date) | 2026-10-11 | digest `sha256:4e32addfc4da3e660f6e0d05ce5e43d3eceb9db58a60b9a142e0dde9a654ead1` | local Docker store (pinned by digest in the Dockerfile) |
| `data.table_1.15.0.tar.gz` | <https://cloud.r-project.org/src/contrib/Archive/data.table/data.table_1.15.0.tar.gz> | 2026-10-11 (build) | `39b7db5dbc76fed91ac60bc351f37a0275a51f306120086b5cd92c1062241062` | image, `/opt/llmr/pins/` |
| `dplyr_1.1.4.tar.gz` | <https://cloud.r-project.org/src/contrib/Archive/dplyr/dplyr_1.1.4.tar.gz> | 2026-10-11 (build) | `cf730414d5d4ab387b4e9890a4b1df9d17a3903488e8da8df1cf2e11e44558cb` | image |
| `extrafont_0.19.tar.gz` | <https://cloud.r-project.org/src/contrib/Archive/extrafont/extrafont_0.19.tar.gz> | 2026-10-11 (build) | `4e8f90152df13fc5dee573222a26b4d66553493fdf6af1c7777e59521ccdab8d` | image |
| `forcats_1.0.0.tar.gz` | <https://cloud.r-project.org/src/contrib/Archive/forcats/forcats_1.0.0.tar.gz> | 2026-10-11 (build) | `c5bb157909d92e1e1a427c0dc5cb358ea00a43a14918a9088fa4f6630962254e` | image |
| `ggplot2_3.5.0.tar.gz` | <https://cloud.r-project.org/src/contrib/Archive/ggplot2/ggplot2_3.5.0.tar.gz> | 2026-10-11 (build) | `07fa1cd4e02d409ade32e69a9088d9209f864c6ddd70fa2f904769dec21090e2` | image |
| `quanteda_3.3.1.tar.gz` | <https://cloud.r-project.org/src/contrib/Archive/quanteda/quanteda_3.3.1.tar.gz> | 2026-10-11 (build) | `628542307d7ac45d4996fbc993a43ed5efcca73d97735ca74a10ccea401d4166` | image |
| `readxl_1.4.3.tar.gz` | <https://cloud.r-project.org/src/contrib/Archive/readxl/readxl_1.4.3.tar.gz> | 2026-10-11 (build) | `7efebbcdefeb8523633db62b3eeb6ea2e4e81e3d010d8b2adb134011c09a5948` | image |
| 44 unspecified dependencies | <https://packagemanager.posit.co/cran/__linux__/jammy/2024-04-03> (Ubuntu jammy binaries) | 2026-10-11 (build) | not hashed individually: installed by `install.packages()` inside the image build; names and versions recorded in `environment.md` and the sealed `package-inventory.csv` | image |
| Paper `vor.pdf` | corpus store `~/corpora/llm-reproducibility/herskind-riede-2024/vor.pdf` (publisher content; referenced, never copied) | already held | `5c60cc3d6fce9f297c44fc62384e0caada1251416066d872ea020feec145fad0` | corpus store |
| Embedded figure images (Figs 2-5), extracted with `pdfimages -j` | from `vor.pdf` pages 3, 5, 6, 7 (publisher content) | 2026-10-11 | Fig. 2 `f6d0c8504b710f4bd4e188b9f0aca916d206720d594d35f4accff2efed8e1434`; Fig. 3 `48ffa902ad0742345cf9d084b5ac955f02404e4fa680d2e94a8356b2f905f47a`; Fig. 4 `10a1d5a1551f7b3a90b74a1d7274fe4965058ee17d0f4d553957524a4e4fd44b`; Fig. 5 `783850e4d8f24e126be45ca5239c5128dac4fc0b948c3cf0c3889db287c1a9b3` | scratch only (`~/scratch/llmr-runs/.../executor/`), never in the repository |

Zenodo version 1 (10.5281/zenodo.10623550), cited in the paper's methods, and
the concept DOI were deliberately not used (AP-12: version 2 is the version of
record). The S2.R provenance anchor (and those of S1, S3, and README) verify
against the committed evidence pack
`corpus/evidence-packs/harvest-2026-10-04/herskind-riede-2024.json`, record
`zenodo:10.5281/zenodo.10801706` (gate `code_integrity.anchors`: all four
`verified`).

### Data availability (L-level)

Taxonomy v1.1 (assigned from actual retrieval attempts).

| Dataset | Route | Steps | Outcome |
|---------|-------|-------|---------|
| S1.xlsx (sole analysis input to all 20 targets) | DOI 10.5281/zenodo.10801706 → Zenodo REST API file endpoint | One unauthenticated HTTPS GET; md5 compared with the record's published checksum | Retrieved, md5 match, 483 objects |
| S3.xlsx (published-values reference for T08; not an input) | same record | One unauthenticated HTTPS GET; md5 check | Retrieved, md5 match |
| Płonka (2003) printed catalogue | cited as upstream source | none: provenance only, no target requires it (L2 counting unit) | not attempted; not counted |

**Assigned level: L1 (open-complete).** The one dataset the targets require
is machine-retrievable through a resolving persistent identifier with no
authentication.

### Modifications Required

No authors' file was edited: S2.R ran byte-identical (md5
`6760ccb30ecc1de7c280bc1e0fa182e5` before and after the run, stdout.log lines
2 and 439; gate `code_integrity.status = identical`). Every mechanic below sits
in the reproducer's own files and changes how the code runs, not what it
computes (invariant 2).

1. **Dockerfile construction** (1 build, 0 failures):
   - The authors supplied R 4.3.2 and seven exact package versions (README),
     with no container or lockfile.
   - Base `rocker/r-ver:4.3.2`, pinned by digest. The image's own repository
     date (2024-02-28) was overridden: pins were built from CRAN Archive source
     tarballs; unspecified dependencies came from the P3M snapshot of
     2024-04-03 (first online appearance).
   - The plan named `remotes::install_version` for the pins; base
     `install.packages(<archive tarball URL>, repos = NULL, type = "source")`
     was used instead, which installs the same CRAN Archive release without
     adding a build-time package. Build failures were promoted from warnings to
     errors, and installed versions asserted.
   - `extrafontdb` made writable (non-root run user); DejaVu fonts and
     fontconfig added.
   - Nothing is copied into the image and no R start-up file is edited (the
     lane mounts the checked work copy).
2. **Script adaptation** (`run-analysis.R`, wrapper):
   - S1.xlsx is copied into `authors-run/`, the working directory S2.R expects
     (it reads `"Herskind&Riede_S1.xlsx"` relatively and writes its PNGs and
     CSVs there).
   - S2.R is parsed once with `parse(file = ..., encoding = "UTF-8",
     keep.source = TRUE)`. `keep.source` is used only to read line numbers. Its
     133 top-level expressions are evaluated in order in the global
     environment, as Rscript would, and visible values are printed (Tables 1
     and 2 are hand-copied from this printed output in the paper). Nothing is
     skipped, re-ordered, or altered.
   - All wrapper state lives in `local()`, outside the global environment.
     S2.R line 642 runs its own `for (i in ...)` loop at the top level, which
     would otherwise overwrite a global wrapper index.
   - Warnings and messages are routed to stdout with the expression index
     (output capture). There is per-expression error capture; the only
     declared tolerance is the font registration on S2.R line 27 (below).
   - Read-only captures: `bigrams` immediately before S2.R line 633 (Part 7
     overwrites the full-corpus table), the finished session (`save()` of the
     global environment), `sessionInfo()`, and the image's package inventory.
3. **Display device** (wrapper): S2.R auto-prints ggplot objects at the top
   level (lines 70, 411, 432, 607-612, 690), as in the authors' interactive
   session. Rscript's default `pdf()` device would error on the unregistered
   family "Gill Sans MT"; a cairo PNG device (`authors-run/screen-device-NN.png`)
   stands in for the screen. The authors' own `ggsave()` calls are unaffected.
4. **Comparison script** (`compare-results.R`, comparison role): its first
   version (run-01) loaded the saved session into a private environment.
   The plots' aesthetic quosures refer to the global environment, which
   `save()` keeps only by reference, so building them failed (object
   `skipgram_order1` not found). From run-02 the session is restored into
   the global environment, as it was when S2.R ended, and every comparison
   variable lives in `local()`. Later edits (runs 03-04) added the T01
   element count and paper-error evidence, the any-frequency Fig. 4 lookup,
   and scoring of T04, T06, and T07 against the transcriptions. Accumulators
   use environments rather than `<<-`, to avoid the gate's in-memory-patching
   heuristic.
5. **Entry** (`run-reproduction.sh`): runs the wrapper, then the comparison
   in a separate R process only if the wrapper exits 0; both consoles are
   teed to `wrapper-captures/`. From run-02 the comparison's stderr is
   captured too.
6. **Transcription tools** (`tools/`, tooling role, host-side, never run by
   the lane): `read-published-fig2.py` measures the published Fig. 2 bar
   segments; `read-published-fig4.py` reads every published Fig. 4 cell's box
   and centre colour. They read only the publisher's figure images (extracted
   to scratch) and compute nothing from the data. Their outputs, and the
   by-eye transcriptions, are under `published-values/` (method table in its
   README).

**Declared error tolerance and whether it fired:**
`font_import(pattern = "GIL", prompt = FALSE)` (S2.R line 27) raised "arguments
imply differing number of rows: 0, 1" (no font file matches "GIL"), and the
tolerance **fired** (stdout.log lines 46 and 436;
`wrapper-captures/expression-log.csv`, expression 8). It registers fonts and
computes nothing that enters a result. No other expression raised an error (0
untolerated errors, stdout.log line 438).

**Version-search attempts:** none needed. Every pin built at its supplied
version first time.

**Gate review obligations expected** (for the adversarial reviewer):

- *dynamic evaluation in `run-analysis.R`*: the `parse` and `eval` of S2.R
  itself.
- *dynamic evaluation in the `Dockerfile`*: `Rscript -e` install steps.
- *107 run-time texts*: these are the authors' own `parse(text =
  filter_condition)` calls in `createResultTable()` (S2.R lines 367-368),
  inside a dplyr `filter()` data mask, building conditions such as
  `"A1 == 1 & C1 == 1"` for each plotted skipgram.
- *wrapper semantics*.

### Outputs Generated

Sealed by the lane in `outputs/run-04/` (the credited run; runs 01-03 are kept
as earlier sealed runs).

| File | Description | Size |
|------|-------------|------|
| `stdout.log` | Full console of the run (S2.R printed output, wrapper and comparison logs) | 667 lines |
| `files/authors-run/artefact_type_chronology.png` | Fig. 2 bar chart (authors' ggsave) | 46 kB |
| `files/authors-run/{bigrams,trigrams,quadrigrams}BY{frequency,pmi}.png` | The six Fig. 3 panels (authors' ggsave) | 162-211 kB each |
| `files/authors-run/heatmapPMI.png` | Fig. 4 skeleton (authors' ggsave) | 181 kB |
| `files/authors-run/{Bigrams,Trigrams,Quadrigrams}.csv` | S3 tables (authors' fwrite) | 8.3, 6.1, 1.4 kB |
| `files/authors-run/screen-device-01..10.png` | the authors' top-level plot prints (display only) | 13-67 kB |
| `files/wrapper-captures/expression-log.csv` | Status of all 133 S2.R expressions | small |
| `files/wrapper-captures/authors-session.RData`, `bigrams-before-part7.rds` | Read-only captures | |
| `files/wrapper-captures/session-info.txt`, `package-inventory.csv` | Environment record | |
| `files/wrapper-captures/analysis-console.txt`, `compare-console.txt` | Teed consoles | |
| `files/comparison-out/*.csv`, `aid-plots/*.png` | Value-level comparisons and R1 aid plots (copied byte-identical to `comparisons/values/`) | |

### Findability, Accessibility, Interoperability, and Reusability (FAIR) / Machine-Actionability Findings

1. **Deposit access**: excellent. A versioned Zenodo DOI, an unauthenticated
   REST API, published md5 checksums, and a CC BY 4.0 licence. Data, code,
   and output tables are all deposited.
2. **Version citation**: the paper's methods (p. 3) cite version 1
   (10.5281/zenodo.10623550), while its data-availability statement (p. 8)
   cites version 2. A reader following the methods gets the earlier version.
3. **Environment specification**: the README pins the R and package versions
   (level 2), which built first time. The paper text says R 4.2.2 and the
   README says 4.3.2: a documentation inconsistency.
4. **Method text versus code**: the paper's PMI formula is written
   log2(observed/expected), but S2.R uses the natural log (`log()`), and every
   published value (Fig. 3 labels, Table 2, S3) is natural-log (e.g. I5-I13:
   ln(3 / 0.0498) = 4.0985). This is a documentation finding (approved plan,
   approver question 5), not a target.
5. **Hand-transcribed outputs**: Tables 1 and 2 were copied by hand from the
   console into Word, and Fig. 2 (bar order), Fig. 4 (box annotations), and
   Fig. 5 were finished or made in GIMP. The two paper-side inconsistencies
   this reproduction found (T01, T06) sit in these manual steps.
6. **Script portability**: S2.R runs end to end under a wrapper, but it was
   written for interactive use. It needs a proprietary font, and its
   `font_import()` call errors, which stops Rscript unless tolerated. It
   reads its data by a relative path containing an ampersand, and it is a
   CRLF UTF-8 file with a non-ASCII identifier.
