# Marwick's Fig. 2 probe (ruling L17 (c))

A local probe, run by Claude on 2026-10-10 and 11 before the ledger freezes,
as ruling L17 (c) requires. The image was built on amd-tower and the run
took place on zbook; sapphire is held for a memory fault. The probe checks
the operator step that L17 (c) names for MAR-T10. It runs the code of the
supplement's switched-off fitting chunk verbatim from a wrapper, renders the
supplement unchanged, and compares the redrawn Fig. 2 with the published
one.

The source is compendium version 1.3 (Zenodo 10.5281/zenodo.15603267). Its
zip's sha256, `7cf98aa5…63bb85`, matches the ledger's `selected_deposit`
record.

## What the probe runs

`analysis/paper/supplement-GAMS-details.qmd` has one `eval: false` chunk
(lines 164 to 249, the authors' note: "this takes a few hours"). It fits five
brms models, each with 4 chains of 50,000 iterations (5,000 warm-up),
`cores = 4`, `adapt_delta = 0.99999`, and `seed = 123`, and saves
`analysis/data/results_brms.RData`.

`probe-run.R` reads the chunks from the .qmd at run time and logs each
chunk's text hash; the switched-off chunk's is `833dc050…`
(`probe-run-output.log`). It runs the three chunks before it, then that
chunk's code verbatim. Then it calls `rmarkdown::render()` on the supplement
unchanged. The supplement's unconditional `readRDS()` loads the saved fit,
and its `fig-smooth-plots-paper` chunk redraws the figure with `ggsave()` to
`analysis/figures/fig-smooth-plots-paper.png`. That is the file `paper.qmd`
includes as Fig. 2 (line 507). No authors' file is edited.

## Environment

The authors' `Dockerfile` (sha256 `93dd7ffd…`) and `renv.lock`
(`4cbafb58…`), built as supplied on 2026-10-10, fail at `renv::restore()`.
The current binary of rstan 2.32.7 cannot load against the lockfile's
RcppParallel 5.1.10: an undefined Threading Building Blocks (TBB) symbol
(`build-authors-dockerfile.log`, line 731).

`probe.Dockerfile` repeats the authors' steps in a wrapper. It builds
StanHeaders 2.32.10 and rstan 2.32.7 from CRAN source at their lockfile
pins (9.5 s and 1.6 min; `build-probe.log`, lines 568 and 569). It then
restores the rest of the lockfile and renders `paper.qmd` as the authors'
build does. Its comments were reworded on 2026-10-11 to use the
build-effort terms below; its instructions are as built.

- **Build effort:** no version substitutions, one build-repair event (the
  failed binary restore, repaired by a source build at the same pins), and
  two components affected (StanHeaders and rstan).
- **Inventory:** all 152 lockfile packages are installed at their locked
  versions (`verify-lockfile.R`, `lockfile-inventory.csv`,
  `verify-lockfile-output.log`).
- **R runtime: the supplied specifications conflict.** The authors'
  Dockerfile builds on `rocker/verse:4.4.1`; their lockfile records R
  4.5.0. That is the only issue `renv::status()` reports. Amendment 3
  §7(d) sets no precedence between conflicting supplied specifications.
  The probe follows the Dockerfile, the authors' executable recipe, so it
  honours the Dockerfile's runtime and does not follow the lockfile's. No
  R 4.5.0 build was attempted, so this is not a fallback under the
  version-search cap. Ruling L20 (a), 2026-10-11: the gate does the same,
  and reports the conflict beside the verdict as a minor discrepancy in
  the deposit.

## Run

The image (`sha256:40d3f29a…`) is the same on both machines. The container
ran with a 24 GiB memory limit and exited 0.

| Step | Time |
|---|---|
| Recency of references | 9.37 h |
| Diversity of references | 1.64 h |
| Relative title length (ln) | 0.82 h |
| N. of authors | 4.06 h |
| N. of pages | 3.30 h |
| **Fitting chunk** | **19.19 h** |
| Supplement render | 3.04 min |

This is far inside the study's 168-hour cap. Memory peaked at 5.6 GiB
during fitting and 19.6 GiB during the render (`resource-usage.log`, one
sample a minute). A gate run needs a memory limit above the render's peak.

### Sampler diagnostics

The run completed, but its sampler diagnostics are not clean, and they
differ from the authors'. The fit warned of divergent transitions
(`probe-run-output.log`, lines 119 to 126). The rendered supplements'
diagnostics tables (Table 1, "num_divergent") read:

| Model | Probe | Authors' deposited supplement |
|---|---|---|
| Recency of references | 3 | 6 |
| Diversity of references | 0 | 0 |
| Relative title length (ln) | 4 | 0 |
| N. of authors | 0 | 0 |
| N. of pages | 0 | 0 |

The minimum effective sample sizes differ too. So the probe's fit is not
identical to the authors', despite the same seed (123); a different R
version or machine is enough to change a sampler's path. All R-hat values
are 1 in both. The probe reports this as found and does not change the
authors' model.

## Comparison

The probe's figure is compared with the authors' deposited image
`analysis/figures/fig-smooth-plots-paper.png` (sha256 `dc03e1be…`).
`paper.qmd` includes that image as Fig. 2. The version of record, p. 4,
shows the same figure with the same five Pseudo R² labels.

`compare-trend.py` compares the two images (both 5,000 by 3,000 pixels at
1,000 dots per inch) (`trend-comparison.json`):

- **Trend lines.** In every column of all five panels, the purple line's
  top and bottom edges agree to within one pixel, on a line about 59
  pixels thick. One pixel is 0.001 inch.
- **Data points.** No strong point discrepancies were detected outside the
  excluded marks: all 47,235 pixels that differ by 60 or more grey levels
  lie within four pixels of text, a frame, a tick, or a trend line. This
  does not prove every point identical. The check ignores weaker
  differences, and points under the excluded marks. The empty sixth cell
  is identical.
- **Text.** Glyph edges differ throughout, as the same text was rasterised
  differently.
- **Pseudo R² labels**, read by eye:

  | Panel | Probe | Deposited image and version of record |
  |---|---|---|
  | Recency of references | 0.0129 | 0.0129 |
  | Diversity of references | 0.0456 | 0.0456 |
  | Relative title length (ln) | 0.0329 | 0.0328 |
  | N. of authors | 0.0827 | 0.0826 |
  | N. of pages | 0.0103 | 0.0103 |

  The labels come from `brms::bayes_R2(model, ndraws = 10000)`. brms picks
  those 10,000 draws with `sample()`, and the supplement's only seed is
  the fit's, so the labels can change between renders of the same fit.
  The fit itself also differs from the authors' (above). The differences
  are therefore consistent with stochastic variation, from the fit, the
  subsample, or both; this comparison does not separate the two. The
  authors' deposited supplement (Table 3, Bayesian R-squared) gives 95 %
  intervals of 0.03 to 0.04 for title length and 0.07 to 0.09 for
  authors, at two decimals, so both differences lie well within them. The
  paper's reading of the figure is unchanged: number of authors has the
  highest R², and every trend keeps its direction.

## Result

The operator step works as the approved plan will name it, and the redrawn
figure matches the published one in scientific content. The differences
are rasterisation and the last printed digit of two stochastic labels. This
supports L17 (c)'s expected outcome for MAR-T10, REPRODUCED_VISUAL.

The gate is not held to the probe's own agreement, since its fit may vary
further. Ruling L19 (a), 2026-10-11: the gate's figure must match the
authors' deposited image (sha256 `dc03e1be…`) in content, and each Pseudo
R² label must fall within its model's 95 % interval in the authors'
deposited supplement (sha256 `5b84fe31…`), read at the table's two
decimals.

## Files

| File | Content |
|---|---|
| `probe.Dockerfile` | The probe environment (one build repair, no substitution) |
| `build-authors-dockerfile.log`, `build-probe.log` | The authors' Dockerfile failing as supplied, and the probe build |
| `verify-lockfile.R`, `lockfile-inventory.csv`, `verify-lockfile-output.log` | The full lockfile inventory against the installed library |
| `probe-run.R` | The wrapper: chunk hashes, the switched-off chunk verbatim, the unchanged render |
| `probe-run-output.log` | The run's log, with chunk hashes and timings |
| `session-info.log` | `sessionInfo()` after the fit |
| `resource-usage.log` | CPU and memory once a minute through the run |
| `compare-trend.py`, `trend-comparison.json` | The figure comparison |

Captured logs have trailing whitespace and carriage returns stripped. The
renders, the rendered supplement, and the 1.7 GB saved fit are not kept
here, as they reproduce third-party material. Their sha256s are
`bdafd17a…` (the probe's figure) and `c76e9ee0…` (the supplement). The fit
stays in the stopped container on zbook.
