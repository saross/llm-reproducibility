# Crema's figures probe (ruling L5 (c))

A local probe on amd-tower, run by Claude on 2026-10-10 before the ledger
freezes, as ruling L5 (c) requires. It runs v1.0.0's `figures_and_tables/figures_main.R`
unmodified, in an environment built the way the lane's preparation guide
builds one, and compares the five main figures with the deposit's own PDFs.
The deposit's `figures_main.R` and `src/utility.R` match
`../../deposit-checksums/crema-v1.0.0.sha256`.

## Environment

`probe.Dockerfile` follows `reproduction-system/prompts/01-preparation.md`
§2.2, since the deposit has no Dockerfile. The base is `rocker/r-ver:4.3.1`,
from the README's session info, and the attached packages are pinned to its
versions. Two fallbacks are logged, both under amendment 3 §7(d):

- **nimbleCarbon.** The session info's 0.2.4 was never released: the CRAN
  archive has 0.1.1, 0.1.2, 0.2.1, and 0.2.5, and GitHub tags v0.1.1 and
  v0.2.5. The version search tries the preceding release, 0.2.1, which
  builds. `figures_main.R` only attaches the package; the figures call base
  graphics, rcarbon, and the deposit's `src/utility.R`.
- **rnaturalearthhires.** It is not on CRAN, so it is pinned to the tagged
  release current at publication (available online 2024-03-16): v1.0.0,
  tagged 2023-12-12.

## Results

| Target | Figure | Probe against the deposit's PDF |
|---|---|---|
| CREMA-T03 | Fig. 1 | pixel-identical |
| CREMA-T04 | Fig. 2 | panel a differs (below); panel b by edge pixels; panel c identical |
| CREMA-T05 | Fig. 3 | pixel-identical |
| CREMA-T06 | Fig. 4 | pixel-identical |
| CREMA-T07 | Fig. 5 | pixel-identical |

A second run gives pixel-identical figures (`run2-vs-run1.json`). The
scripts' only random call is `plot.fitted()`'s `sample()` in
`src/utility.R`, which permutes all the draws. That leaves the plotted means
and quantiles unchanged.

**Fig. 2 panel a: v1.0.0 does not hold the posterior behind its own figure.**
Panel a plots simulation 1a's fitted sigmoid, whose plateau is the parameter
`mu_k`.

- v1.0.0's archived posterior (`sim/results/post_sim1a.RData`, matching the
  deposit checksum) gives `mu_k` a median of 0.660 (95 % interval 0.591 to
  0.734); the simulated true value is 0.65 (`posterior-plateau-output.log`).
- `measure-band.py` reads the 95 % band at the curve's late end, calibrated
  on the panel frame (`band-measurement.json`):

  | Image | Band |
  |---|---|
  | Probe, from v1.0.0's archive | 0.592 to 0.729 |
  | The deposit's own `figure2.pdf` | 0.570 to 0.693 |
  | The pilot's render, from v2.0.0's archive | 0.565 to 0.693 |
  | Version of record, p. 6 (vector graphics) | 0.567 to 0.691 |

  The probe's reading agrees with its computed band (0.591 to 0.734) to
  within a pixel, which checks the calibration.
- Panel c is pixel-identical. Panel b differs from the deposit's PDF only
  by edge pixels along the rising curve, and its late-end band is the same
  in all three renders.

So the published panel a was drawn from a posterior that v2.0.0 archives and
v1.0.0 does not. Both bands contain the true value, which is the figure's
point, so the figure's conclusion is unchanged. The expected outcome is
ruling L18.

## Files

| File | Content |
|---|---|
| `probe.Dockerfile` | The probe environment, with both fallbacks commented |
| `probe-vs-deposit.json` | `../crema-figures-content/compare-figures.py`, probe against the deposit's PDFs |
| `run2-vs-run1.json` | The same script, second run against the first |
| `posterior-plateau.R`, `posterior-plateau-output.log` | `mu_k` and the band at 1700 BP from v1.0.0's posterior |
| `measure-band.py`, `band-measurement.json` | Panel a's band edges in the three renders and the version of record |

The renders themselves are not kept here, since they reproduce third-party
figures.
