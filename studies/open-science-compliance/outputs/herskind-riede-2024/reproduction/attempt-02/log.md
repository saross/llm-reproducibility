# Reproduction Log

## Herskind and Riede 2024 — attempt 02

**Paper:** Herskind, L.L.P., Riede, F., 2024. A computational linguistic
methodology for assessing semiotic structure in prehistoric art and the meaning
of southern Scandinavian Mesolithic ornamentation. *Journal of Archaeological
Science* 165, 105969. <https://doi.org/10.1016/j.jas.2024.105969> (CC BY 4.0).

**Run:** `phase2-shakedown-2026-10`, attempt 2. Executor
`reproduction-executor v1.1` (`claude-opus-5-5`, effort high). Launch commit
`e5f35543c07d2a9314d1742ff34df40a12bd35fd`.

### Timeline

All times are UTC on 2026-10-03.

| Time | Activity | Duration |
|------|----------|----------|
| 11:58 | Read the injected instruments (verdicts-and-precision, coverage-rules, and pipeline-invariants, all v1.0). Verified the approval: plan sha256 `5cdc8071…abaf63` equals the spawn hash and the approval record's `plan_sha256`; decision `approve`. | 2 min |
| 11:59 | Read the plan, comparison-record schema, templates, pulled references, and preparation/execution prompts | 1 min |
| 12:00 | Fetched Zenodo v2 record metadata and four files; all published md5 checksums matched; sha256 recorded | 1 min |
| 12:01 | Read S2.R (759 lines, 8 parts) and README in full; wrote the Dockerfile | 1 min |
| 12:02 | `docker build` iteration 1 — succeeded; all README pins asserted | 2.5 min |
| 12:05 | Probed S1/S3 structure in the container (read-only); wrote `run-analysis.R` | 1.5 min |
| 12:06 | Run 1 in Docker (exit 0, ~6 s); outputs root-owned | <1 min |
| 12:07 | Read the paper (PDF, corpus store) and transcribed the published values; rendered 400 dpi crops of pp. 3–7 into scratch only | 6 min |
| 12:13 | Wrote `comparisons/published-values/*.csv` and `comparisons/compare.R` | 2 min |
| 12:15 | Run 2 in Docker as the host user (final outputs); byte-identical to run 1 except timestamps | <1 min |
| 12:16 | Ran `compare.R` in Docker. Fixed two defects in my own aid script: a T04 totals merge, and the T12–T14 site-name join (see Modifications 4) | 3 min |
| 12:19 | Visual comparisons (Figs 2–5); added the T04 occurrence cross-check; wrote the documentation and `comparison.json` | ~15 min |
| **Total** | | **~40 min** |

### Materials Acquired

| Artefact | Source URL or DOI | Retrieved (UTC) | SHA-256 | Destination |
|----------|-------------------|-----------------|---------|-------------|
| `Herskind&Riede_S1.xlsx` | <https://zenodo.org/api/records/10801706/files/Herskind&Riede_S1.xlsx/content> (DOI 10.5281/zenodo.10801706, v2) | 2026-10-03 | `d76b9d6328465658aa1582c5c8de0912f9167ff1f8c737bd7998d91fd5692030` | attempt-dir `data/` (md5 `0bcde6d178b5a8f3da80a023a64ff510` = published) |
| `Herskind&Riede_S2.R` | <https://zenodo.org/api/records/10801706/files/Herskind&Riede_S2.R/content> | 2026-10-03 | `487a00a09db92b484dac136f13a5745a3a2ac699c3a01cfccf528d4d550a8720` | attempt-dir `data/` (md5 `6760ccb30ecc1de7c280bc1e0fa182e5` = published) |
| `Herskind&Riede_S3.xlsx` | <https://zenodo.org/api/records/10801706/files/Herskind&Riede_S3.xlsx/content> | 2026-10-03 | `1199acac5d1edb916dc4528d5e994295e206e798cb132e91c3be59cc9e328eed` | attempt-dir `data/` (md5 `812be5456d7e0e2adb97ecb5a975239e` = published) |
| `README.txt` | <https://zenodo.org/api/records/10801706/files/README.txt/content> | 2026-10-03 | `cdaae0824c92137375537cc962c7016a6ce71eecdd2bb90dba7e604755786679` | attempt-dir `data/` (md5 `8b5ef4c5a8c1f75c5d61ed25f799521b` = published) |
| Zenodo record metadata `record.json` | <https://zenodo.org/api/records/10801706> | 2026-10-03 | not hashed (a metadata response used only to read the file list and checksums; discarded) | scratch |
| `rocker/r-ver:4.3.2` | Docker Hub | 2026-10-03 | `sha256:4e32addfc4da3e660f6e0d05ce5e43d3eceb9db58a60b9a142e0dde9a654ead1` (repo digest) | local Docker |
| Paper PDF (version of record) | `/home/shawn/corpora/llm-reproducibility/herskind-riede-2024/vor.pdf` (corpus store; publisher content) | already held | `5c60cc3d6fce9f297c44fc62384e0caada1251416066d872ea020feec145fad0` | corpus store only — read in place, never copied into the attempt directory. 400 dpi page renders were made in scratch for reading figure labels. |

The four author files are byte-identical copies of the downloads: the sha256
was taken before and after copying. They are released as supplementary
material under the article's CC BY 4.0 licence. No publisher supplements were
fetched; per the run note they are byte-identical to Zenodo v2.

#### Data retrieval log (per dataset)

| Dataset | Route | Steps | Outcome |
|---------|-------|-------|---------|
| S1 motif data (the only dataset in the data availability statement and methods) | DOI 10.5281/zenodo.10801706 → Zenodo files API | One unauthenticated HTTPS GET; md5 verified | Retrieved, complete (483 objects). **L1** |
| Płonka (2003) catalogue (upstream source of S1) | Printed monograph | Not attempted: transcription is outside the computational scope (plan) | Not retrieved. Not counted in the L-level. |
| Fig. 2 / Fig. 5 base maps; Fig. 5 motif-extent patches | None stated | None possible | No route. A scope limitation for T02 (base map, not scored) and T14 (patches → CANNOT_COMPARE). |

**Data-availability level: L1 (open-complete).** All analysis data were
machine-retrievable by persistent identifier with no authentication.

### Modifications Required

Each modification was tested against the wrapper cardinal rule (pipeline
invariant 2). None changes what is computed.

1. **Dockerfile construction** (1 iteration):
   - The deposit provides R and package versions only (README).
   - Built from `rocker/r-ver:4.3.2`. Its frozen P3M snapshot (2024-02-28)
     resolved every README pin, and a build-time assertion enforces them.
   - Locale set to C.UTF-8. Added fontconfig with a "Gill Sans MT" → DejaVu
     Sans alias, plus cairo libraries.

2. **Script adaptation — wrapper `run-analysis.R`:**
   - S2.R is read verbatim and evaluated statement by statement in its own
     order. The wrapper splits evaluation at the script's own `#PART n:`
     headers and saves copies of existing objects to `outputs/capture-*.csv`
     between parts. No authors' statement is edited, removed, added, or
     reordered.
   - **Working directory:** S2.R runs from `outputs/`, with a temporary
     symbolic link `Herskind&Riede_S1.xlsx` → `../data/…`, so the authors'
     relative read and write paths resolve unchanged. The link is removed at
     the end.
   - **Font import:** `font_import(pattern = "GIL", prompt = FALSE)` is the
     only error-tolerant statement. It failed with "arguments imply differing
     number of rows: 0, 1" because no Gill Sans files exist. The authors' own
     comment says it errors on their machine too. The call only registers
     fonts and computes nothing.
   - **Screen rendering:** auto-printed plots are routed to a cairo PDF
     (`console-plots.pdf`), because Rscript's default `pdf()` device cannot
     resolve the "Gill Sans MT" family. The authors' `ggsave()` calls are
     untouched.
   - **Fig. 3 objects:** the per-panel objects that S2.R overwrites
     (`skipgramsFreq`/`skipgramsPMI`, `summary_freq`/`summary_pmi`) are copied
     read-only from the authors' own ggplot objects (`$data` and the label
     layer's data). No authors' block was split.

3. **Container user:** run 2 (the final outputs) used `--user $(id -u):$(id -g)`
   so host files are not root-owned. Run 1 outputs were hashed to scratch and
   deleted; both runs are byte-identical apart from timestamps.

4. **Comparison script `comparisons/compare.R`** (verification aids, ruling R1;
   separate from the authors' code). Two defects in my own script were found
   and fixed before scoring:
   - A merge produced duplicate `total` column names, which crashed the T04
     totals step.
   - The T12–T14 S1 lookup joined on site name only. "Korsør, Glasværk" (and
     other sites) occur on several S1 rows, so `match()` picked a different
     object. The join now takes, among rows with the published site name, the
     unique row bearing at least two of the five cluster motifs. The Figure
     field is deliberately not used as a key because it is a compared field.
     Each resolved S1 row number is written in `results/t12-table3.csv`.
   - Added after the first full comparison: a read-only occurrence check for
     T04. Σ C(m, 2) and Σ C(m, 3) over the S1 `Total` column are compared with
     the occurrences implied by Table 1, as part of the PAPER_ERROR
     verification protocol.

### Outputs Generated

| File | Description | Size |
|------|-------------|------|
| `outputs/artefact_type_chronology.png` | Fig. 2 bar panel (authors' ggsave) | 45,764 B |
| `outputs/bigramsBYfrequency.png`, `bigramsBYpmi.png`, `trigramsBYfrequency.png`, `trigramsBYpmi.png`, `quadrigramsBYfrequency.png`, `quadrigramsBYpmi.png` | Fig. 3 panels a–f (authors' ggsave) | 162–211 kB each |
| `outputs/heatmapPMI.png` | Fig. 4 skeleton (authors' ggsave) | 181,274 B |
| `outputs/Bigrams.csv`, `Trigrams.csv`, `Quadrigrams.csv` | S3 tables (authors' fwrite) | 8,288 / 6,063 / 1,377 B |
| `outputs/run-console.log` | Echoed console of the full run (Table 1 `table()`/`length()`, Table 2 `summary()`) | 33,608 B |
| `outputs/capture-*.csv` | Wrapper copies of intermediate objects (Table 1/2 values, Fig. 2 counts, Fig. 3 bars, labels, and axis order, Fig. 4 cells, full skipgram tables) | 52 B – 744 kB |
| `outputs/console-plots.pdf` | Screen renders of auto-printed plots | 64,751 B |
| `outputs/session-info.txt` | `sessionInfo()` | 1,621 B |
| `comparisons/results/*.csv` | Value-level comparisons per target | — |
| `comparisons/aids/*.png` | Verification-aid figures (Fig. 2 map points, Fig. 4 boxes, Fig. 5 positions) | — |

### Findability, Accessibility, Interoperability, and Reusability (FAIR) / Machine-Actionability Findings

1. **Data and code access:** the materials are fully open and DOI-versioned
   (Zenodo), with published md5 checksums. All four files retrieved by API
   without authentication.
2. **Version ambiguity:** the methods (p. 3) cite version 1
   (10.5281/zenodo.10623550), while the data availability statement cites
   version 2. Resolved by run note AP-12 (version 2 is the version of record).
3. **Environment specification:** the README gives exact package versions and
   R 4.3.2, but the paper says R 4.2.2. There is no lockfile, container, or
   `sessionInfo()` (level 2).
4. **Interactive-only outputs:** Tables 1 and 2 exist only as console output,
   hand-copied into Word. Figs 3 and 4 were finished in GIMP. Fig. 2 (map) and
   Fig. 5 have no code or layers. Table 3's selection rule is unstated, though
   S1 shows it equals "objects bearing at least two of C4/C5/C12/C13/D7".
5. **Proprietary font:** every plot requests Gill Sans MT, and
   `font_import(pattern = "GIL")` errors where it is absent. This was
   tolerated in the wrapper.
6. **Method statement:** the paper gives PMI = log2(observed/expected)
   (p. 3), but S2.R uses natural `log()`. All published PMI values are
   natural-log values: for example, I5–I13 = ln(3/0.0497925) = 4.0985 in both
   S3 and Fig. 3b, whereas log2 would give 5.913. This is a documented finding
   and not scored (approval ruling 3).

### Blinding note

A directory listing of `.claude/skills/reproduction-assessor/references/`
(12:00) printed the names of the blinded file `verification-strategies.md` and
subdirectory `examples` as bare entries. Neither was opened, read, searched, or
listed further.

A repository-wide `git status --porcelain` (about 12:23 UTC, run to confirm
that this attempt wrote nothing outside its directory) printed the untracked
paths of another paper's concurrent attempt directory (`dye-et-al-2023`,
attempt-02: top-level file and directory names only). Nothing under that path
was opened, read, listed, searched, or modified. The exposure was limited to
the path names in the status output and has no bearing on any result here,
because all comparisons were complete and the gate had passed. No other
blinded path was accessed.
