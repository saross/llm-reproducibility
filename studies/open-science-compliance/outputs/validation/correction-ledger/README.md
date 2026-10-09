# Correction ledger for the §8 regression gate — DRAFT

**Status: DRAFT, ruled in part (ledger 0.2.1-draft). Shawn ruled L1 to L4
and L6 to L16 on 2026-10-09; L5 and L17 are open. Not frozen and not
hashed.** No run may use any value here until every ruling is made, the
ruled copy is committed, and its sha256 is recorded in the gate's run
configuration (amendment 3 §9 and §10 step 3).

## What this is

Amendment 3 to the Open Science Framework (OSF) registration, lodged
2026-10-08, re-bases the registered §8 regression gate. An audit of the
pilots' executed code (2026-10-04) found that the gate's baseline, the five
pilots' attempt-01 artefacts, is not what the gate assumes. Three pilots
executed a reproducer's re-implementation rather than the authors' files, and
two executed a version other than the one the version-selection rule (AP-12)
picks. Matching the pilots exactly would reward a pipeline for reproducing
their errors. §9 therefore adds a versioned **correction ledger**. For each
pilot target it records the selected source version and checksum, the printed
value and tolerance, any corrected expected value with its evidence tier and
ruling, the pilot's recorded value and outcome, the repair class, credit
eligibility, and the coverage treatment. The amended gate passes against the
frozen ledger; the strict comparison against the pilot artefacts is still
reported.

## Files

| File | Role |
|---|---|
| `correction-ledger.json` | The ledger: the artefact to be ruled, frozen, and hashed |
| `correction-ledger.md` | Rendered review copy (`render-ledger.py`); never edit it by hand |
| `render-ledger.py` | Renders the JSON as Markdown |
| `check-printed-values.py` | Re-checks every printed value against its cited PDF page |
| `deposit-checksums/crema-v1.0.0.sha256` | sha256 of all 50 files in crema's v1.0.0 deposit |
| `evidence/l9-dye-section-07/` | Operator run of dye's section 5 and 7 code, byte-identical (L9) |

## How it was drafted

- **Target list.** No pilot attempt-01 has a locked target list: the pilots
  predate that instrument. The draft takes each attempt-01 comparison report's
  compared items, mapped to the paper's own display items (ruling L1), and
  lists every exclusion with its reason (L2).
- **Values.** Printed values come from the corpus store's PDFs and the
  selected deposits only. Four read-only Opus subagents transcribed them, and
  every value was then checked mechanically. `check-printed-values.py` finds
  239 of 239 text-layer values on their cited pages; the five figure labels
  drawn inside herskind's Fig. 3 raster were read on a 250 dpi render. The
  pilot values were checked against the pilot reports and output files by
  script.
- **Shakedown evidence.** The shakedown's attempt-02 results appear only as
  evidence that the authors' unmodified code yields a value, and are labelled
  so, as §9 requires.
- **Deposits fetched on 2026-10-09** (public, no login): crema v1.0.0 from
  Zenodo (sha256 and md5 match the audit and the published checksum) and
  marwick's rendered `paper.docx` at tag 1.3 from GitHub (git blob hash equals
  the tag's tree entry). A Zenodo re-download of marwick's 1.3 zip returned
  HTTP 504 and was not retried.

## Findings beyond the executed-code audit

1. **Marwick: the published Kendall's W is 0.64, not about 0.70.** The pilot
   recorded the published value as "~0.70 (moderate to strong)" and credited
   its 0.7 as an exact match. It also said PC1's variance is not printed (the
   paper prints 71 %). Version 1.3's own rendered `paper.docx` reads W 0.64,
   p = 2.67 × 10⁻⁶, and PC1 71 %, the printed values. So all three of the
   pilot's marwick differences trace to running post-1.3 code (audit MAR-1),
   and the "data revision" explanation is unsupported.
2. **Key: the two "paper errors" are the pilot's own transcription slip.**
   The paper prints Midland Thickness Extension % = 19.6 and Clovis Mass =
   3.1; the pilot's wrapper swapped them. Audit ruling Q5(ii), and the example
   in lodged amendment 3 §7(d), rest on the swap (ruling L16). The pilot also
   mis-recorded Olduvai Thickness Mean (42.3 for the printed 42.2), the
   paper's DOI, and its author list.
3. **Dye: three of the five "published" branching values are not printed.**
   0.83, Amethyst→Disc 0.87, and Cowrie→Disc 1.00 match the pilot's own
   output; the paper prints only Cowrie→Disc 0.87. The report lists 53
   comparisons, not 54, and leaves out six printed zeros. Its figure numbers
   (7 and 8) are the supplement's stale cross-references; the paper's are
   Figs 3 and 4. The corpus store's `vor.pdf` is the accepted manuscript.
4. **Crema: confirmed at source.** The printed Table 1 equals v1.0.0's
   `table1.csv` in all 24 cells. 18 of the pilot's 24 archived-posterior
   values differ from it. The pilot report swaps the labels of Figs 1 and 2
   and names the wrong journal.
5. **Herskind: the pilot's figure labels match none of the paper's figures.**
   Its frequency table silently differs from the printed Table 1, which has
   eight paper-error cells (shakedown ruling 3), and its "top PMI"
   (pointwise mutual information) values are not the global top five.
6. **Marwick: Fig. 2 cannot be redrawn from the deposit.** The published
   image comes from `supplement-GAMS-details.qmd`, whose model-fitting chunk
   is marked `eval: false` with the authors' note "this takes a few hours"
   (five brms models, 4 chains of 50,000 iterations each). Its saved fit,
   `results_brms.RData`, is not in the tag 1.3 tree. Found 2026-10-09 while
   applying ruling L11; it raises ruling L17.

**Astra's review (2026-10-09, at `9b66683`)** confirmed the key and marwick
printed-value findings independently and found two errors, both fixed in
ledger 0.2.1-draft:

- **B1. Two marwick figures were labelled unchanged though their content
  changes.** The pilot's Fig. 1 and Fig. 3, rendered from 652e542, differ
  from the version of record in the diversity panels and in Fig. 3's Borda
  ranking, not just in styling. MAR-T09 and MAR-T11 are now corrected, with
  the pilot figures kept as their historical baseline; marwick's unchanged
  set falls from eight to six. Fig. 5 (MAR-T13) was checked the same way
  and matches, so it stays unchanged.
- **B2. HER-T02 tightened the pilot's precision without a correction.**
  Amendment 3 §9 compares an unchanged deterministic target at the pilot
  table's precision, after the same rounding. HER-T02 now compares at 3 dp;
  the 4-dp figure labels stay with HER-T03 (corrected).

Shawn accepted L16's finding on 2026-10-09: the erratum log's Entry 7
records the key slip, and the public correction is queued for the next OSF
amendment.

## Sets and gate selection

| Paper | Testable unchanged targets | Corrected | Expected verdict (pilot) |
|---|---|---|---|
| crema | 0 (registered leg, Table 1 only) | 1 | SUCCESSFUL (SUCCESSFUL) |
| dye | 11 | 2 | PARTIAL (SUCCESSFUL) |
| herskind | 2, including the 1,601-cell S3 table | 2 | SUCCESSFUL (SUCCESSFUL) |
| key | 0; all nine targets untestable | 2 | BLOCKED (PARTIAL) |
| marwick | 6 | 7 | SUCCESSFUL, provisional on L17 (SUCCESSFUL) |

**Ruled (L6 (c), 2026-10-09): the gate runs dye, herskind, and marwick,**
plus crema's mandatory archived-posterior leg. Key is not a gate paper; its
record keeps the expected verdict for the strict comparison. Each paper's
agentic run passes the API review gate before it starts.

## Rulings (details in `correction-ledger.md`)

Ruled by Shawn on 2026-10-09:

- **L1 (a):** the de facto target list. **L2 (a):** exclusions listed with
  reasons. **L3 (a):** scope changes extend the target. **L4 (a):**
  "unchanged" ignores pilot credit eligibility. **L6 (c):** dye, herskind,
  and marwick. **L7 (a):** testable unchanged targets.
- **L8 (a):** styling-only differences count as reproduced. **L9 (b):** the
  two operator runs are admitted as tier-3 evidence. **L10 (a):** dye
  PARTIAL. **L11 (a):** a static include never counts. **L12 (a):**
  marwick's printed values stand. **L13 (a):** review counts kept, checked
  before freezing. **L14 (a):** key BLOCKED. **L15 (a):** freezing.
  **L16 (a):** erratum-log Entry 7; OSF note with the next amendment.

Open:

- **L5:** crema's figures. Recommendation revised to (c), all five figures
  in the leg, after Shawn asked whether they repeat Table 1 (they mostly do
  not: Figs 2 and 5 appear nowhere else).
- **L17:** marwick's Fig. 2, which only a multi-hour MCMC re-run can
  regenerate. Recommendation (a), outside the gate as a stated scope
  limit.

## Before freezing

- [x] 2026-10-09 Rule L1–L4 and L6–L16 and apply them to the JSON
      (ledger 0.2.0-draft, re-rendered).
- [ ] Rule L5 and L17 and apply them.
- [ ] Hold the crema v1.0.0 and herskind v1 deposits in the corpus store with
      manifest entries (audit Q10).
- [ ] Hash marwick's files inside the 1.3 zip; confirm review counts in
      `paper.qmd` at 1.3 (L13).
- [x] 2026-10-09 Operator runs for L9: dye's section 5 and 7 code
      byte-identical (`evidence/l9-dye-section-07/`); herskind's Fig. 4
      check already used the authors' function verbatim.
- [x] 2026-10-09 Admit the two runs as tier-3 evidence (L9 (b)).
- [ ] Commit the ruled copy as `correction-ledger-v1.0.json` and record its
      sha256 in the run configuration (L15).

## Re-running the checks

```bash
python3 check-printed-values.py      # needs pdftotext and the corpus store
python3 render-ledger.py             # regenerates correction-ledger.md
```
