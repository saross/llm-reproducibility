# Adversarial Review Report

## Paper: Key et al. 2024 — Identifying accurate artefact morphological ranges using optimal linear estimation

## Date: 2026-02-10

## Reviewer context: Fresh session (no reproduction context)

### Artefacts Reviewed

- `comparisons/comparison-report.md` — Quantitative comparison with PARTIAL verdict
- `log.md` — Reproduction timeline and modifications
- `environment.md` — Software specification
- `Dockerfile` — Environment definition
- `run-analysis.R` — Wrapper script (314 lines)
- `outputs/table-5-olduvai-results.csv` — Table 5 reproduction output
- `outputs/table-6-paleoindian-results.csv` — Table 6 reproduction output
- `outputs/run.log` — Console output from Docker execution
- `scripts/Morphology OLE Script _spl_Main_spl_ Supplementary Information.r` — Original mmc1 script
- Paper PDF pages 12-13 (Tables 5, 6, 7)

---

### Dimension 1: Provenance Audit

**Verdict: PASS**

**Question:** Did the reproduced values genuinely come from the Docker run?

**Checks performed:**

- [x] **run.log timestamp consistency**: run.log shows "Date: 2026-02-10
  07:26:16 UTC". The UTC timezone confirms execution inside a Docker
  container (host is in a local timezone). Consistent with log.md timeline.
- [x] **Dockerfile completeness**: Complete and functional — FROM clause,
  COPY for script and data, CMD for Rscript execution. Not a stub.
- [x] **Output file sizes**: table-5-olduvai-results.csv (409 B, 6 data
  rows), table-6-paleoindian-results.csv (1.2 KB, 16 data rows), run.log
  (6.7 KB, 138 lines). All non-empty and plausible for the analyses
  described.
- [x] **Traceability**: Every "Reproduced" value in the comparison report
  can be traced to a specific cell in the CSV output files. Verified by
  spot-check (see Dimension 2).
- [x] **Deterministic analysis / exact match consistency**: The OLE.test
  function involves no stochastic components (no rnorm, no sample, no
  set.seed). Exact match claims for this function are appropriate.
- [x] **No evidence of manual value insertion**: The comparison report's
  "Reproduced" column values match CSV file contents exactly. No values
  present in the report that are absent from output files.

**Minor note:** The run.log contains hardcoded "Published Table 5 values"
comparison text (lines 23-29 of run.log) with an incorrect Length
Extension% value (27.5% instead of the paper's actual 18.1%). This is a
transcription error in the cat() statements of run-analysis.R — it does
NOT affect the CSV outputs or the comparison report, which correctly uses
18.1%. The log.md documents this error in Discrepancy Note #5. However,
a reader examining only run.log could be misled by the incorrect reference
values embedded in the console output.

---

### Dimension 2: Quantitative Claims Audit

**Verdict: PASS**

**Question:** Are the numerical comparisons in the report accurate?

**Spot-check procedure:** Selected 6 values spanning both tables, multiple
classification types, and both exact and discrepant results.

**Spot-check 1: Table 5, Olduvai Breadth OLE Maximum**

- Paper Table 5 (p.12): Olduvai row, Breadth, OLE Maximum = **126.8**
- CSV (table-5-olduvai-results.csv): "Breadth",134,...,126.8,... → Max_TE = **126.8**
- Report: Published 126.8, Reproduced 126.8, EXACT_MATCH
- **Verified: correct** ✓

**Spot-check 2: Table 6, Folsom Mass OLE Minimum**

- Paper Table 6 (p.13): Folsom, Mass, OLE Minimum = **-0.4**
- CSV (table-6): "Mass_g","Folsom",...,-0.4,...  → Min_TE = **-0.4**
- Report: Published -0.4, Reproduced -0.4, EXACT_MATCH
- **Verified: correct** ✓

**Spot-check 3: Table 5, Mass Minimum (WITHIN_PRECISION)**

- Paper Table 5 (p.12): Olduvai, Mass, Minimum = **252**
- CSV (table-5): "Mass",134,588.3,**251.5**,... → Minimum = 251.5
- Report: Published 252, Reproduced 251.5, WITHIN_PRECISION
- Difference: 0.5 (explained by decigram-to-gram conversion precision)
- **Verified: classification correct** ✓

**Spot-check 4: Table 6, E. Clovis Breadth OLE Maximum**

- Paper Table 6 (p.13): E. Clovis, Breadth, OLE Maximum = **46.7**
- CSV (table-6): "Breadth_mm","Eastern Clovis",...,46.7,... → Max_TE = **46.7**
- Report: Published 46.7, Reproduced 46.7, EXACT_MATCH
- **Verified: correct** ✓

**Spot-check 5: Table 6, Midland Thickness Extension % (MAJOR_DISCREPANCY)**

- Paper Table 6 (p.13): Midland, Thickness, Extension % = **3.1**
- CSV (table-6): "Thickness_mm","Midland",...,21.2 → Range_Ext_TE_Pct = **21.2**
- Report: Published 3.1, Reproduced 21.2, MAJOR_DISCREPANCY
- Independent formula check: paper's own values give
  ((6.5 − 2.9)/(6.0 − 3.0) − 1) × 100 = **20.0%**, not 3.1%.
  The 21.2% from full-precision intermediates is plausible; the paper's
  3.1% is inconsistent with its own OLE Min/Max values.
- **Verified: classification correct — paper error confirmed** ✓

**Spot-check 6: Table 6, Clovis Mass Extension % (MAJOR_DISCREPANCY)**

- Paper Table 6 (p.13): Clovis, Mass, Extension % = **19.6**
- CSV (table-6): "Mass_g","Clovis",...,3.1 → Range_Ext_TE_Pct = **3.1**
- Report: Published 19.6, Reproduced 3.1, MAJOR_DISCREPANCY
- Independent formula check: paper's own values give
  ((201.8 − 1.4)/(196.2 − 1.9) − 1) × 100 = **3.1%**, not 19.6%.
  The reproduction's 3.1% matches the formula; the paper's 19.6% is
  inconsistent with its own OLE Min/Max values.
- **Verified: classification correct — paper error confirmed** ✓

**Arithmetic verification of combined summary:**

- EXACT_MATCH: 24 (T5) + 65 (T6) = 89 ✓
- WITHIN_PRECISION: 6 (T5) + 21 (T6) = 27 ✓
- CANNOT_COMPARE: 0 (T5) + 8 (T6) = 8 ✓
- MAJOR_DISCREPANCY: 0 (T5) + 2 (T6) = 2 ✓
- Total: 30 + 96 = 126 ✓
- Comparable: 126 − 8 = 118 ✓
- Confirmed: 89 + 27 = 116 ✓
- 116/118 = 98.3% ✓

**Table 6 row count verification:** 4 types × 4 variables = 16 rows ×
6 metrics = 96 values ✓

**No omissions detected.** All Table 5 Olduvai rows and all Table 6 rows
are present in the comparison. No silent skipping of values.

---

### Dimension 3: Scope Completeness Audit

**Verdict: PASS**

**Question:** What was NOT reproduced, and is the omission justified?

**Paper contents inventory:**

| Element | Status | Justification |
|---------|--------|---------------|
| Table 1 | N/A | Descriptive table (assemblage descriptions), no quantitative results |
| Tables 2-3 | Not reproduced | Validation with replica assemblages — data Level 3-4 (PhD theses, never published) |
| Table 4 | Not reproduced | Summarises Tables 2-3 results — dependent on unavailable data |
| Table 5 (Olduvai row) | **Reproduced** | 30 values compared |
| Table 5 (8 other rows) | Not reproduced | Data Level 3 (co-author-held, monographs, closed-access theses) |
| Table 6 (all 4 types) | **Reproduced** | 96 values compared |
| Table 7 | Not reproduced | Morphometric data not in public GitHub repos; additionally uses mmc2 (no set.seed) |
| Figures 1-4 | Not reproduced | Require Tables 2-3 validation data |
| Figure 5 | Not reproduced | Requires full validation dataset |
| Figure 6 | Not reproduced | Requires complete Tables 5-7 results |

**Scope limitation assessment:**

1. **Tables 2-4** (validation): Genuinely external — replica handaxe data
   is from a closed-access PhD thesis (Kempe 2020), and Early Archaic point
   data was never published (Level 4). No workaround possible.
2. **Table 5 other rows**: 8 datasets held by co-authors or in monographs.
   The data-availability-inventory.md documents each dataset's access
   status. No workaround without author contact.
3. **Table 7**: Two barriers — (a) public GitHub repos contain
   classification data, not morphometric measurements, and (b) the
   Randomised OLE script (mmc2) lacks set.seed(), making exact reproduction
   impossible even with correct data. Both barriers are genuine.
4. **Figures**: All depend on unreproducible tables. No figures could have
   been generated from available data alone.

**Selective reproduction check:** The reproduction covers everything
possible with available data. No accessible analyses were skipped to
produce favourable results. The 2 MAJOR_DISCREPANCY values (both paper
errors) were reported transparently rather than hidden.

---

### Dimension 4: Confirmation Bias Check

**Verdict: PASS**

**Question:** Were ambiguous results interpreted too favourably?

**Judgment calls identified in the comparison report:**

1. **6 WITHIN_PRECISION values in Table 5**: All explained by data
   precision differences (decigram conversion) and rounding order
   (Extension % from rounded vs unrounded intermediates). These
   explanations are plausible and specific. A sceptic could argue these
   indicate "different input data" rather than "same data, different
   precision," but the magnitude of differences (0.1-0.5) is consistent
   with rounding, not with fundamentally different data.

2. **21 WITHIN_PRECISION values in Table 6**: Pattern is consistent —
   small descriptive statistic rounding (e.g., 16.65 → 16.7) and
   Extension % computation order differences. All within 1 unit of the
   last reported decimal place. Classification is appropriate.

3. **2 MAJOR_DISCREPANCY classified as "paper errors"**: This is
   independently verifiable. Applying the Extension % formula
   ((OLE Max − OLE Min)/(Max − Min) − 1) × 100 to the paper's own
   tabulated OLE values produces values inconsistent with the paper's
   stated Extension %. The claim of "paper error" is justified by
   arithmetic, not interpretation.

4. **8 CANNOT_COMPARE values**: Classified as NaN from undocumented
   duplicate handling. The technical explanation is verified — the OLE.test
   function does produce NaN when the k-window contains duplicates (log of
   zero in v parameter). This is a genuine limitation, not an excuse.

**Challenge test — arguing for FAILED:**
"Only 2 of 13 datasets were reproduced. The Mass values differ (251.5 vs
252). The 8 NaN values could be hiding mismatches. The paper's OLE
algorithm might have been applied differently for the 10 inaccessible
datasets."

**Rebuttal:** The FAILED verdict requires "material discrepancies affecting
conclusions." The 2 discrepancies are demonstrably paper errors (verified
by formula). The Mass difference is 0.5g on a 1017g range (0.05%).
The NaN values come from a documented code limitation, not a mysterious
failure. The scope limitation is due to data access, not methodology. The
core finding — that the OLE algorithm produces the reported estimates — is
confirmed.

**Challenge test — arguing for SUCCESSFUL:**
"98.3% match rate is excellent. The 2 discrepancies are paper errors, not
reproduction failures. The method is fully verified."

**Rebuttal:** SUCCESSFUL requires "all or nearly all values reproduced."
With only 2/13 datasets accessible and 3/6 tables untestable, "nearly all"
does not apply. The method is verified within a narrow scope, but the
majority of the paper's results remain unconfirmed. PARTIAL correctly
reflects this.

**Conclusion:** The PARTIAL verdict is appropriately calibrated. Neither
the FAILED nor SUCCESSFUL counter-arguments are strong enough to overturn
it.

---

### Dimension 5: Methodological Soundness Audit

**Verdict: PASS**

**Question:** Was the reproduction methodology itself sound?

**OLE.test function verification:**

Compared run-analysis.R lines 41-60 against original mmc1 lines 26-45
character by character. The function body is **identical** — only trailing
whitespace differs (non-functional). Confirmed verbatim.

**run_ole helper function verification:**

Compared run-analysis.R lines 67-124 against mmc1 for-loop (lines 48-61):

| mmc1 Operation | Wrapper Operation | Match |
|----------------|-------------------|-------|
| `data.i <- sort(datalist[,i])` | `data.i <- sort(values)` | ✓ (parameterised) |
| `rev(sort(data.i))[1:k.size]` | `rev(sort(data.i))[1:k.size]` | ✓ identical |
| `sort(data.i)[1:k.size]` | `sort(data.i)[1:k.size]` | ✓ identical |
| `max(min.range.data) - min.range.data` | `max(min.range.data) - min.range.data` | ✓ identical |
| `max.range.data - min(max.range.data)` | `max.range.data - min(max.range.data)` | ✓ identical |
| `max(min.range.data) - OLE.test(...)` | `max(min.range.data) - OLE.test(...)` | ✓ identical |
| `min(max.range.data) + OLE.test(...)` | `min(max.range.data) + OLE.test(...)` | ✓ identical |
| `OLE.min[[1]], OLE.min[[2]]` | `min_te <- OLE.min[[1]], min_ci <- OLE.min[[2]]` | ✓ (named) |
| `OLE.max[[1]], OLE.max[[2]]` | `max_te <- OLE.max[[1]], max_ci <- OLE.max[[2]]` | ✓ (named) |

**Additions in wrapper (non-algorithmic):**

- NA removal: `vals <- vals[!is.na(vals)]` (line 155, 220) — necessary for
  mass columns with missing values. Does not change analytical logic.
- Duplicate counting: `n_unique`, `n_dups` (lines 72-73) — diagnostic
  only, not used in OLE computation.
- Extension % calculation (lines 101-108) — derived metric not in mmc1,
  computed from OLE outputs. Correctly implements the formula.
- `round(..., 1)` on output values (lines 114-122) — presentation
  rounding, applied after all computation.
- `write.csv()` and `sink()` — output capture only.

**No prohibited modifications found:**

- [x] No changes to statistical methods or parameters
- [x] No changes to data filtering or subsetting logic
- [x] No changes to model specifications
- [x] No added or removed analysis steps
- [x] alpha = 0.05, k.size = 10 match mmc1 defaults

**Docker isolation:**

- Dockerfile COPYs data and script into container
- Docker run uses `-v $(pwd)/outputs:/analysis/outputs` for output
- run.log shows UTC timezone (container), confirming in-container execution
- No host R installation dependency

**Data version:**

- Olduvai: n=134 matches paper's stated sample size
- Paleoindian: n=810 Clovis, n=228 E. Clovis, n=179 Folsom, n=64 Midland
  — all match paper's Table 6 caption
- Mass sample sizes (n=101, 63, 125, 64) match paper's stated exceptions

**Minor observation:** The run-analysis.R comment on line 103 reads "Using
CI values (which extend further than TE values)" but the code computes
both CI and TE Extension %. The comparison report correctly uses TE values
(Range_Ext_TE_Pct), matching the paper's reported TE estimates. The
misleading comment does not affect the analysis.

---

### Overall Assessment

**Verdict: CONFIRMED**

| Dimension | Verdict | Key Finding |
|-----------|---------|-------------|
| 1. Provenance | PASS | All values traceable to Docker-generated CSV outputs |
| 2. Quantitative Claims | PASS | 6/6 spot-checks verified; arithmetic confirmed |
| 3. Scope Completeness | PASS | All accessible analyses reproduced; omissions genuine |
| 4. Confirmation Bias | PASS | PARTIAL verdict correctly calibrated; challenge tests rebutted |
| 5. Methodological Soundness | PASS | OLE.test verbatim; wrapper modifications non-algorithmic |

All 5 dimensions PASS. The reproduction's PARTIAL verdict is well-supported
by the evidence: the OLE algorithm is verified within the available scope,
and the scope limitations are genuine external barriers (data access), not
methodological shortcuts.

The two MAJOR_DISCREPANCY values are independently confirmed as paper
calculation errors by applying the Extension % formula to the paper's own
tabulated OLE values. The 8 CANNOT_COMPARE values result from a documented
code limitation (duplicate handling) that is an inherent property of the
original OLE script.

---

### Recommendations

1. **Fix hardcoded comparison values in run-analysis.R**: Lines 175 and
   249-264 contain reference values transcribed from the paper for visual
   comparison during execution. Line 175 has an incorrect Length Extension %
   (27.5% instead of 18.1%, copied from the wrong Table 5 row). While this
   does not affect the CSV outputs, it creates a misleading artefact in
   run.log. Consider correcting or removing these cat() statements.

2. **Clarify comment on line 103**: The comment "Using CI values" is
   misleading — the code computes both CI and TE Extension %. The
   comparison uses TE. Suggest revising to "Computing Extension % from
   both TE and CI values."

3. **Document the Extension % computation order**: The comparison report
   notes that WITHIN_PRECISION differences in Extension % arise from
   computing with full-precision vs rounded intermediates. This could be
   made more explicit by adding a note to environment.md or the wrapper
   script explaining that the reproduction computes Extension % before
   rounding, which may differ from the paper's apparent approach.

4. **Consider contacting authors about duplicate handling**: The 8 NaN
   values could potentially be resolved by learning the authors'
   pre-processing steps. This would allow verification of the remaining
   CANNOT_COMPARE cells and might resolve the Midland Thickness / Clovis
   Mass Extension % discrepancies if the authors used a different
   intermediate computation.
