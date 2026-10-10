# Crema's figures: pilot against deposit v1.0.0

Evidence for the correction sets of CREMA-T03 to T07, recorded 2026-10-10
when ruling L5 (c) brought crema's five main figures into the registered
archived-posterior leg.

Under ruling L4 (a), a target stays "unchanged" only if its expected outcome
and value both equal the pilot's. The pilot drew its figures from version
2.0.0's archived results; the gate draws them from version 1.0.0's.
`compare-figures.py` rasterises the pilot's PDFs and the deposit's own
v1.0.0 PDFs at 110 dpi and compares them pixel by pixel. The deposit PDFs'
sha256 digests match `../../deposit-checksums/crema-v1.0.0.sha256`.

| Target | Figure | Result | Differing pixels |
|---|---|---|---|
| CREMA-T03 | Fig. 1, site maps | pixel-identical | 0 |
| CREMA-T04 | Fig. 2, simulation fits | content differs | 1.158 % |
| CREMA-T05 | Fig. 3, Japan posterior predictive check | content differs | 0.730 % |
| CREMA-T06 | Fig. 4, Britain posterior predictive check | content differs | 1.258 % |
| CREMA-T07 | Fig. 5, cremation proportions | pixel-identical | 0 |

The differences lie inside the plotted bands, not in axes, labels, or
legends. In Fig. 2, panels a and b (simulations 1a and 1b) place the 95 %
highest posterior density (HPD) band and the posterior mean slightly
differently, and panel c matches. In Figs 3 and 4, the edges of the 90 %
prediction envelope differ. The figure code's only random call,
`plot.fitted()`'s `sample()` in `src/utility.R`, permutes all the draws and
leaves the plotted means and quantiles unchanged, and two runs of v1.0.0's
script give pixel-identical figures (`../crema-figures-probe/`). So the
differences come from version 2.0.0's archived inputs or plotting
functions, not from the run. (Corrected 2026-10-10: the first version of
this note said `figures_main.R` draws no random numbers, having searched
that file only.)

Visual inspection of side-by-side renders, made the same day, agrees.
Those renders are not kept here, since they reproduce third-party figures.

```bash
python3 compare-figures.py \
  ../../../../crema-et-al-2024/reproduction/attempt-01/outputs/figures-from-precomputed \
  <unzipped v1.0.0 deposit>/figures_and_tables results.json
```
