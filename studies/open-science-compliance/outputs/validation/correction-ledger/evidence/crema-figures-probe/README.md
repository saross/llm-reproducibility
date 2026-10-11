# Crema's figures probe (ruling L5 (c))

A local probe on amd-tower, run by Claude before the ledger freezes, as
ruling L5 (c) requires. It runs v1.0.0's `figures_and_tables/figures_main.R`
unmodified and compares the five main figures with the deposit's own PDFs.
The deposit's `figures_main.R` and `src/utility.R` match
`../../deposit-checksums/crema-v1.0.0.sha256`.

There are two environments. The first (2026-10-10) is a preliminary
diagnostic: it pinned only the attached packages. The second (v3,
2026-10-11) honours every package version the deposit supplies, as
amendment 3 §7(d) requires (Astra's B3). It reproduces the first probe's
results exactly, so the findings below hold in the compliant environment.

## Environment

The deposit has no Dockerfile or lockfile. Its README's session info is the
authors' environment specification: R 4.3.1 and 68 package versions, 11
attached and 57 loaded via a namespace. Under §7(d) each is a supplied pin,
judged per dependency, not by whether `library()` attached it.

### Compliant environment (v3)

`probe-v3.Dockerfile` builds on `rocker/r-ver:4.3.1` and runs
`install-pins.R` over `pins.csv`, the 68 versions parsed from the session
info. The script builds each pin from CRAN's own source tarball, in the
pinned versions' dependency order. If a pin cannot be retrieved or built,
the script records the failure and tries the immediately preceding release,
then the immediately following one (at most three attempts). It installs
dependencies the session info does not list at the release current at the
article's first online appearance (2024-03-16), from a Posit Package Manager
snapshot of that date. It then asserts the final inventory and fails on any
mismatch.

- **Inventory** (`pin-inventory.csv`): 67 supplied pins honoured, 1
  fallback, and 14 unspecified dependencies from the snapshot (82
  packages).
- **The fallback: nimbleCarbon 0.2.4.** It is unavailable in the checked
  release sources: CRAN's archive and current release hold 0.1.1, 0.1.2,
  0.2.1, 0.2.5, and 0.2.6, and the GitHub repository's tags are
  v0.1-beta.0, v0.1.1, and v0.2.5 (checked 2026-10-11). The search's first
  step, the preceding release 0.2.1, builds. `figures_main.R` only attaches
  the package; the figures call base graphics, rcarbon, and the deposit's
  `src/utility.R`. `pin-attempts.csv` logs every attempt.
- **An unspecified initial choice: rnaturalearthhires v1.0.0.** This is not
  a fallback. The package is absent from the session info and not on CRAN.
  The tag current at the article's first online appearance is v1.0.0,
  tagged 2023-12-12, so the Dockerfile installs that tag.
- **Build effort:** one version substitution (nimbleCarbon) and no
  build-repair events.

### Preliminary diagnostic (v1)

`probe.Dockerfile` pinned only the 11 attached packages, so it cannot show
pin compliance. It installed vctrs 0.6.4 and polyclip 1.10-6 where the
session info names 0.6.2 and 1.10-4, for example. v3 corrects this. Its
figures are pixel-identical to v1's (`v3-vs-run1.json`;
`curve-v3-vs-run1.json` at 220 dots per inch (dpi) for Fig. 2).

v2 was an unused intermediate build. Its install script read the release
history from the base image's default repository, a 2023-10-30 snapshot
with an incomplete archive index. It also took dependencies and build order
from the packages' 2024 versions, so rnaturalearth 0.3.3 was built before
`sp`, which it imports, and failed. v3 reads CRAN itself and each pinned
version's own DESCRIPTION.

## Results

| Target | Figure | v3 against the deposit's PDF |
|---|---|---|
| CREMA-T03 | Fig. 1 | pixel-identical |
| CREMA-T04 | Fig. 2 | panel a differs (below); panel b within one pixel row; panel c identical |
| CREMA-T05 | Fig. 3 | pixel-identical |
| CREMA-T06 | Fig. 4 | pixel-identical |
| CREMA-T07 | Fig. 5 | pixel-identical |

`v3-vs-deposit.json` holds the comparison; `probe-vs-deposit.json` is v1's,
with the same result. A second v1 run gave pixel-identical figures
(`run2-vs-run1.json`). The scripts' only random call is `plot.fitted()`'s
`sample()` in `src/utility.R`, which permutes all the draws. That leaves the
plotted means and quantiles unchanged.

## Fig. 2 panel a: v1.0.0's inputs do not regenerate it

Panel a plots simulation 1a's fitted sigmoid, whose plateau is the parameter
`mu_k`. The figure is regenerated from v1.0.0's archived posterior
(`sim/results/post_sim1a.RData`, matching the deposit checksum) by v1.0.0's
unmodified code.

- **Plateau.** The archived posterior gives `mu_k` a median of 0.660 (95 %
  interval 0.591 to 0.734); the simulated true value is 0.65
  (`posterior-plateau-output.log`). `measure-band.py` reads the 95 % band at
  the curve's late end, calibrated on the panel frame
  (`band-measurement.json`):

  | Image | Band |
  |---|---|
  | Probe, from v1.0.0's archive | 0.592 to 0.729 |
  | The deposit's own `figure2.pdf` | 0.570 to 0.693 |
  | The pilot's render, from v2.0.0's archive | 0.565 to 0.693 |
  | Version of record, p. 6 (vector graphics) | 0.567 to 0.691 |

  The probe's reading agrees with its computed band (0.591 to 0.734) to
  within a pixel, which checks the calibration.
- **Whole curve.** `compare-curve.py` compares the band edges column by
  column at 220 dpi, where one pixel row is 0.0046 in proportion
  (`curve-comparison.json`). In panel a, the probe's band is lower than the
  deposit's by up to 0.082 on the rising limb. The edges cross fixed values
  between 50 years earlier and 90 years later. In panel b, the edges agree
  within 0.005, one pixel row. Panel c is pixel-identical.
- **Containment.** `curve-containment.R` checks the true curve against the
  95 % band from v1.0.0's posteriors at every year
  (`curve-containment-output.log`). In panel a, the curve is inside the band
  at all 2,301 years; in panel b, at all 4,001. Where the true proportion
  exceeds 0.05, the smallest margins are 0.026 (at 3148 BP) and 0.028 (at
  4838 BP).

So v1.0.0's inputs and code do not regenerate the published panel a, while
the pilot's render from v2.0.0's archive closely matches it. The images do
not identify the posterior the authors used, or show that no file in v1.0.0
holds it; the band measurements are consistent with that inference but do
not prove it. The regenerated bands contain the true curve throughout
panels a and b, so the recovery claim the figure supports (§5.1, p. 7) holds
under v1.0.0's archive. The expected outcome is ruling L18.

## Files

| File | Content |
|---|---|
| `probe-v3.Dockerfile`, `install-pins.R`, `pins.csv` | The compliant environment and its install rules |
| `pin-inventory.csv`, `pin-attempts.csv` | v3's final inventory and every install attempt |
| `v3-vs-deposit.json`, `v3-vs-run1.json` | `../crema-figures-content/compare-figures.py`, v3 against the deposit's PDFs and against v1 |
| `curve-v3-vs-run1.json` | `compare-curve.py`, v3's Fig. 2 against v1's |
| `probe.Dockerfile` | v1, the preliminary diagnostic (attached pins only) |
| `probe-vs-deposit.json`, `run2-vs-run1.json` | v1 against the deposit's PDFs, and v1's second run against its first |
| `posterior-plateau.R`, `posterior-plateau-output.log` | `mu_k` and the band at 1700 BP from v1.0.0's posterior |
| `measure-band.py`, `band-measurement.json` | Panel a's late-end band in the three renders and the version of record |
| `compare-curve.py`, `curve-comparison.json` | Panels a and b compared column by column; panel c pixel by pixel |
| `curve-containment.R`, `curve-containment-output.log` | The true curve against the 95 % band at every year, panels a and b |

The R scripts' outputs are the same in v1 and v3. The renders themselves
are not kept here, since they reproduce third-party figures.
