# Reproduction verdicts, precision, and tolerances v1.0 — canonical file

**Status: FROZEN by OSF registration 2026-07-20 (DOI 10.17605/OSF.IO/DQNHG)** —
changes require the §8 regression gate + an erratum-log entry + an OSF amendment
before any affected analysis runs.
**Version:** 1.0 (composed 2026-07-24 from preregistration §7.2, §7.4, §7.5 and
the reproduction-assessor protocol v1.1 used in the pilot — the source the
registration's §7.2 "definitions as in" clause points to)
**Canonical home** per routing design §4. The reproduction-assessor `SKILL.md`
mirrors the discrepancy, verification-strategy, and scope-limitation tables
verbatim (machine-checked); the environment levels and verdict definitions are
registered here.
**Consumers:** `reproduction-executor` (pushed, with read receipt);
reproduction-assessor SKILL.md (verbatim table mirror, human lane); registered
in `manifest.yaml` `shared_content`.

---

## Verdict categories (preregistration §7.2)

- **SUCCESSFUL** — All (or nearly all) values reproduced within expected tolerances; conclusions confirmed
- **PARTIAL** — Some analyses reproduced, others could not (scope limitations, missing data, etc.)
- **FAILED** — Material discrepancies; reproduced results contradict published findings
- **BLOCKED** — Reproduction could not be attempted (missing code, inaccessible data, proprietary tools with no intermediates)

BLOCKED is an outcome, not an exclusion: availability claims that cannot be
fulfilled are recorded and the paper is retained with verdict BLOCKED
(preregistration §5.2).

## Precision categories (preregistration §7.4)

Exact = matches to machine precision; within tolerance = matches within
pre-stated per-analysis tolerances (e.g. within published highest posterior
density intervals for Markov chain Monte Carlo outputs), tolerances recorded in
each reproduction plan **before execution**; material discrepancy = outside
tolerance with potential to affect conclusions.

## Tolerance rules by analysis type

| Analysis Type | Strategy | Tolerance | Example |
|---------------|----------|-----------|---------|
| Deterministic | Exact match | 0 | Herskind (frequency counts), Dye (post-processing) |
| Stochastic (MCMC) | Within HPD intervals | Published confidence intervals | Crema (Bayesian posteriors) |
| Stochastic (bootstrap/permutation) | Within expected variance | ±2 SE or similar | — |
| GAM/regression | Coefficient comparison | Within reported precision | Marwick (minor p-value difference) |
| Proprietary upstream | Document scope limitation | N/A | Dye (OxCal not reproduced) |

Deterministic analyses: every value must match — differences indicate a bug in
the reproduction, not expected variation. Stochastic analyses: fresh runs
produce different point estimates; verify point estimates within published
HPD/CI intervals, qualitative conclusions unchanged, direction and magnitude of
effects consistent. Figure verification is visual (layout, patterns, relative
positions) — exact pixel matching is not expected; the scientific content must
match.

## Discrepancy classification

| Category | Definition | Verdict Impact |
|----------|-----------|----------------|
| EXACT_MATCH | Values identical to reported precision | SUCCESSFUL |
| WITHIN_PRECISION | Difference within rounding of reported precision | SUCCESSFUL |
| WITHIN_CONFIDENCE | Within published CI/HPD intervals (stochastic only) | SUCCESSFUL |
| MINOR_DISCREPANCY | Small difference, conclusions unchanged | SUCCESSFUL with note |
| MAJOR_DISCREPANCY | Substantive difference affecting conclusions | PARTIAL or FAILED |
| CANNOT_COMPARE | Value could not be computed (upstream data/preprocessing issue) | Context-dependent |

**CANNOT_COMPARE** covers cases where the reproduction cannot produce a value
because of upstream issues outside the analytical pipeline — for example, NaN
results from undocumented data preprocessing steps, missing input files, or
data formatting mismatches. Distinct from MAJOR_DISCREPANCY because the
algorithm is not wrong; the input conditions differ from those (often
undocumented) that produced the published result.

**Paper error handling:** when a reproduced value disagrees with a published
value but the reproduction is internally consistent and the paper's own
tabulated data supports the reproduced value, classify as PAPER_ERROR rather
than MAJOR_DISCREPANCY. To verify a suspected paper error: apply the published
formula to the paper's own input values and check whether the paper's reported
output is consistent. Document the verification in the comparison report.
PAPER_ERROR findings escalate for human confirmation before entering study
data (modernisation plan §4.4).

## Scope-limitation taxonomy

| Category | Description | FAIR Implication | Example |
|----------|-------------|------------------|---------|
| Proprietary upstream | Analysis depends on commercial/proprietary software | Not a FAIR failure — tool choice | Dye → OxCal MCMC generation |
| Data unavailability | Required data cannot be accessed | FAIR failure — data not accessible | Key → 10/13 datasets unavailable |
| Stochastic non-reproducibility | No random seed set; results will vary | Design limitation, not failure | Key → no `set.seed()` in mmc2/mmc3 |
| Publishing error | Supplement files empty, corrupted, or mislabelled | Journal process failure | Key → mmc4.csv header only (75 bytes) |

Verdict implications: proprietary upstream does not diminish a SUCCESSFUL
verdict for the reproducible components; data unavailability may require
PARTIAL if substantial analyses are affected; stochastic non-reproducibility
uses stochastic tolerances (exact match not expected); publishing errors are
documented, excluded from comparison, and flagged as FAIR findings.

## Environment-specification levels (preregistration §7.5, ordinal)

- **0** — none
- **1** — language version stated
- **2** — unpinned dependency list
- **3** — pinned lockfile
- **4** — container specification
- **5** — container plus pinned lockfile

---

Receipt-token: fe9bca3d3c95f931
