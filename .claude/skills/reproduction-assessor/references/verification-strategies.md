# Verification Strategies for Computational Reproductions

Reference document for the reproduction-assessor skill. Covers strategies for comparing
reproduced results against published values in computational research papers.

## Verification Philosophy

The goal of verification is to determine whether the reproduced analysis confirms the
published findings. This is not a binary pass/fail exercise — it requires structured,
transparent comparison across every reported result. Rigorous verification demands:

- **Identifying ALL verification targets** — every table, figure, and key statistic reported
  in the paper. Nothing should be silently omitted from the comparison.
- **Classifying each target as deterministic or stochastic** — because the appropriate
  comparison method differs fundamentally between the two.
- **Applying appropriate comparison tolerances** — exact match for deterministic outputs,
  interval-based or distributional checks for stochastic outputs.
- **Documenting scope limitations** — what was NOT reproduced and why. Scope limitations
  are informative, not failures.
- **Avoiding cherry-picking** — report all comparisons, not just the ones that match. A
  verification report that only shows successes is not trustworthy.

## Deterministic Comparison

For analyses with no random elements — frequency counts, proportions, logarithms,
algebraic transformations, post-processing of fixed inputs — the standard is exact match
to reported precision.

**Every value must match.** Any difference indicates a reproduction bug, an error in the
original paper, or a misunderstanding of the method. It does not indicate expected
variation, because there is no source of variation in a deterministic pipeline.

### Implementation

1. Extract all values from the reproduced output (programmatically where possible).
2. Extract all corresponding values from published tables and text.
3. Compare at the precision reported in the paper. If the paper reports two decimal
   places, compare to two decimal places.
4. **Rounding convention**: A value of 0.870 that rounds to 0.87 at two decimal places is
   an exact match to the published value 0.87.
5. **Machine epsilon**: Values that differ only at floating-point precision (e.g.,
   0.449999... vs 0.45) are classified as EXACT_MATCH. These arise from IEEE 754
   representation, not from analytical differences.

### Examples from Completed Reproductions

- **Herskind & Riede (2024)**: All 291 Pointwise Mutual Information (PMI) values matched
  exactly against published Table 2.
- **Dye & Allen (2023)**: All 54 algebraic probability values matched exactly against
  published tables.

## Stochastic Comparison: Markov chain Monte Carlo (MCMC) / Bayesian

For Bayesian analyses using MCMC sampling, fresh runs produce different posterior draws
and therefore different point estimates. This is expected behaviour, not a reproduction
failure.

### Verification Approach

The appropriate check is whether reproduced values fall within the published confidence
or Highest Posterior Density (HPD) intervals.

**HPD interval checking procedure:**

1. Extract published HPD intervals from paper tables (typically 90% or 95%).
2. Compute point estimates (mean, median) from the fresh MCMC output.
3. Verify each reproduced estimate falls within the corresponding published interval.
4. If a reproduced estimate falls outside the published interval, check whether the
   qualitative conclusion is unchanged (e.g., the direction and approximate magnitude
   of the effect are preserved).

### Convergence Checks

Before comparing values, verify that MCMC diagnostics are acceptable:

- **Rhat** (potential scale reduction factor): should be close to 1.0 (typically < 1.05).
- **ESS** (effective sample size): should be large enough for stable posterior summaries
  (typically > 400 for point estimates, > 400 for tail quantiles).

Poor convergence invalidates comparison — the reproduced values are not reliable
estimates of the posterior.

### Important Nuance

Pre-computed results derived from the same MCMC run are deterministic. If you load saved
posterior draws and recompute summaries, the results should match exactly (same draws
produce the same summaries). The stochastic comparison framework applies only when fresh
MCMC sampling is performed.

### Example

- **Crema et al. (2024)**: All fresh point estimates fell within the published 90% HPD
  intervals, confirming the reproduction.

## Stochastic Comparison: Other Methods

For bootstrap, permutation tests, cross-validation, and other resampling-based methods,
point estimates vary between runs due to random resampling.

### Comparison Criteria

- **Direction of effect**: Does the reproduced estimate point the same way?
- **Approximate magnitude**: Is the reproduced estimate in the same ballpark?
- **Significance level**: Does the reproduced p-value lead to the same statistical
  conclusion (e.g., both significant at alpha = 0.05)?
- **Tolerance**: Typically within plus or minus two standard errors, or a similar
  method-appropriate tolerance.

### When Seeds Are Set

If a random seed is set and documented in the original code, reproduced results should
be exact. Seed-controlled stochastic analyses are effectively deterministic for
verification purposes.

## Regression and Generalised Additive Model (GAM) Comparison

For fitted statistical models, different components have different sensitivity to minor
variations in data or implementation.

### What to Compare

- **Coefficient estimates**: Compare values and standard errors. Small differences may
  arise from optimiser tolerance or library version differences.
- **P-values**: Compare significance level rather than exact value. P-values are highly
  sensitive to minor perturbations — a shift from 0.048 to 0.052 may cross a threshold
  but does not represent a substantive difference.
- **R-squared / deviance explained**: Compare approximate values. Small differences in
  the third decimal place are typically immaterial.
- **Qualitative conclusions**: Do the reproduced model results support the same
  interpretations as the published analysis?

### Example

- **Marwick (2025)**: Kendall's tau p-value reproduced as 4.08 x 10^-7 versus the
  published 2.67 x 10^-6. Both are highly significant (p << 0.001), so this was
  classified as MINOR_DISCREPANCY — the statistical conclusion is identical despite
  the numerical difference.

## Figure Verification

Visual outputs require a different comparison approach than numerical values. The
question is not pixel-level identity but scientific equivalence.

### What to Compare

- **Layout**: Same axes, scales, and orientation.
- **Patterns**: Same trends, clusters, and distributions.
- **Relative positions**: Same ordering of elements and spatial relationships.

### What is NOT Expected to Match

- Exact colours (theme and device differences between plotting environments).
- Font rendering and text positioning.
- Pixel-level differences in anti-aliasing or rasterisation.
- Minor layout shifts from different output device dimensions.

### Guiding Principle

**Does the figure communicate the same scientific content?** If a reader would draw the
same conclusions from both figures, the reproduction is successful.

### Figure Comparison Checklist

For each figure, work through this structured comparison:

1. **Identify figure type:** Statistical plot, map, diagram, photograph, composite panel
2. **Check data equivalence:** Can the underlying data be extracted and compared
   numerically? If so, verify data first — visual comparison is secondary
3. **Compare structural elements:**
   - Axis labels, ranges, and scales (linear vs log, inverted)
   - Legend content and positioning
   - Number of data points, bars, lines, or panels
4. **Compare scientific content:**
   - Do trends, peaks, and inflection points appear at the same positions?
   - Are relative magnitudes preserved (tallest bar, densest cluster)?
   - Are categorical orderings the same?
5. **Note acceptable differences:**
   - Colour palette and theme styling
   - Font family and text rendering
   - Anti-aliasing and rasterisation artefacts
   - Minor layout shifts from different output dimensions
6. **Document verdict per figure:** Match / Minor visual differences / Substantive
   difference

### Special Cases

- **Computationally generated figures**: The underlying data should match; visual
  rendering is secondary. Verify the data, then confirm the figure looks equivalent.
- **Manually post-processed figures** (e.g., GIMP-edited heatmaps, Inkscape-annotated
  plots): Computational values should match, but exact visual reproduction requires
  replicating the same manual editing steps. Document the manual steps as a scope
  limitation if they cannot be automated.
- **Multi-panel figures**: Compare each panel separately. Panels may be generated by
  different code sections — verify that all panels are reproduced, not just the first.

## Scope Limitation Documentation

Not everything in a paper can always be reproduced. The key is to document what was
excluded and why, rather than treating omissions as failures. Each scope limitation
should be classified by category.

### Scope Limitation Taxonomy

| Category | Description | FAIR Implication | Verdict Impact |
|----------|-------------|------------------|----------------|
| **Proprietary upstream** | Analysis depends on commercial/proprietary software | Not a FAIR failure — tool choice | Does not diminish SUCCESSFUL for open components |
| **Data unavailability** | Required data cannot be accessed | FAIR failure — data not accessible | May require PARTIAL if substantial analyses affected |
| **Stochastic non-reproducibility** | No random seed set; results vary between runs | Design limitation | Use stochastic tolerances; exact match not expected |
| **Publishing error** | Supplement files empty, corrupted, or mislabelled | Journal process failure | Document and exclude; flag as FAIR finding |
| **Compute constraints** | Pipeline too expensive for verification scope | Not a FAIR failure | Document and scope to feasible subset |

### Documentation Per Category

**Proprietary upstream:** Document which tool is proprietary, what outputs it produces,
and how pre-computed outputs from the original authors were used as inputs to the
reproducible pipeline instead. Example: Dye et al. 2023 — OxCal MCMC generation not
reproduced; ArchaeoPhases post-processing fully verified using pre-computed MCMC draws.

**Data unavailability:** Document what data is missing, why, and the impact on
verification scope. Use the data access level taxonomy (Level 0-4) from the reproduction
plan guide. Quantify the impact: what percentage of analyses, datasets, or records cannot
be reproduced. Example: Key et al. 2024 — 10/13 datasets at Level 3-4, limiting
reproduction to 42.6% of records.

**Stochastic non-reproducibility:** Document the absence of `set.seed()` or equivalent.
Note whether the paper's stochastic analyses can still be verified using distributional
checks (HPD intervals, effect directions, significance levels). Example: Key et al. 2024
— mmc2 and mmc3 use stochastic methods without fixed seeds; exact reproduction of
randomised analyses is not possible.

**Publishing error:** Document the specific error (empty file, corrupted data, wrong
format), the evidence that it is a publishing error rather than an intentional omission,
and any alternative sources for the missing content. Example: Key et al. 2024 — mmc4.csv
contains only a header row (75 bytes); likely a publishing error since the paper
references data that should be in this file.

**Compute constraints:** Document the estimated runtime and why it exceeds the
verification scope. Identify whether a representative subset can be reproduced instead.
Example: week-long MCMC runs may be scoped to a subset of chains or iterations.

### Key Principle

Distinguish between **the paper's analytical contribution** (what the authors actually
did that constitutes their research) and **upstream preprocessing** (data acquisition,
calibration by external tools, or data cleaning steps that precede the analysis). Scope
limitations in upstream preprocessing do not diminish a successful reproduction of the
core analytical pipeline.

## Discrepancy Classification Reference

Use these categories consistently across all verification reports.

| Category | Definition | Example |
|----------|-----------|---------|
| EXACT_MATCH | Identical to reported precision | 0.87 = 0.87 |
| WITHIN_PRECISION | Differs only at unreported decimal places | 0.870 vs 0.871 (reported as 0.87) |
| WITHIN_CONFIDENCE | Within published CI/HPD interval (stochastic only) | Estimate 45.2, HPD [40.1, 50.8] |
| MINOR_DISCREPANCY | Small difference, conclusions unchanged | p = 4.08 x 10^-7 vs 2.67 x 10^-6 |
| MAJOR_DISCREPANCY | Substantive difference, conclusions affected | Coefficient sign reversal |
| CANNOT_COMPARE | Value could not be computed (upstream issue) | NaN from undocumented duplicate removal |
| PAPER_ERROR | Paper's own value is internally inconsistent | Extension% contradicts tabulated min/max |

### Notes on Classification

- EXACT_MATCH and WITHIN_PRECISION are both considered successful reproduction for
  deterministic analyses.
- WITHIN_CONFIDENCE is the expected outcome for stochastic analyses with fresh runs.
- MINOR_DISCREPANCY requires explanation (e.g., library version difference, floating-point
  accumulation) but does not undermine the reproduction.
- MAJOR_DISCREPANCY requires investigation and may indicate a genuine problem with either
  the reproduction or the original analysis.
- CANNOT_COMPARE applies when the reproduction pipeline cannot produce a value because
  upstream conditions differ from the (often undocumented) conditions that produced the
  published result. Common causes: undocumented data preprocessing (duplicate removal,
  outlier filtering), missing input files, or data format mismatches. This is distinct
  from MAJOR_DISCREPANCY — the algorithm is correct but the inputs are not comparable.
- PAPER_ERROR applies when the reproduced value is internally consistent but disagrees
  with the paper's reported value, AND independent verification confirms the paper's
  value is wrong. To verify: apply the published formula to the paper's own tabulated
  input values and check whether the paper's output is consistent. PAPER_ERROR
  strengthens confidence in the reproduction (the algorithm detected a genuine error).

### Handling Paper Errors

When a suspected paper error is identified:

1. **Independent verification:** Apply the paper's stated formula to its own tabulated
   values. If the formula produces the reproduced value (not the published value), the
   paper contains an error.
2. **Cross-reference:** Check whether the same error appears in other rows or tables
   (errors in derived columns like percentages may be systematic).
3. **Document explicitly:** In the comparison report, present both the published value and
   the independently verified correct value, with the formula used for verification.
4. **Classify as PAPER_ERROR:** Do not classify as MAJOR_DISCREPANCY — the reproduction
   is correct and the paper is wrong.
5. **Verdict impact:** PAPER_ERROR values should not count against the reproduction's
   match rate. They are evidence of reproduction quality, not reproduction failure.

## Verification Reporting

The comparison report is the primary output of the verification phase. It must be
comprehensive, honest, and structured.

### Required Components

1. **Methodology section**: How the comparison was conducted — what tools were used, how
   values were extracted, what precision was applied.
2. **Complete comparison table**: List EVERY value compared, not just matches. Use a
   consistent format:

   | Item | Published | Reproduced | Category |
   |------|-----------|------------|----------|
   | Table 1, Row 1 | 0.87 | 0.87 | EXACT_MATCH |
   | Table 1, Row 2 | 0.45 | 0.44 | MINOR_DISCREPANCY |

3. **Summary counts**: Total values compared and category breakdown (e.g., "289/291
   EXACT_MATCH, 2/291 WITHIN_PRECISION").
4. **Scope section**: What was and was not reproduced, with justification for any
   exclusions.
5. **Verdict**: State the overall outcome clearly using one of:
   - **SUCCESSFUL** — All or nearly all values match within appropriate tolerances;
     conclusions fully confirmed.
   - **PARTIAL** — Some results reproduced, others could not be verified (typically due
     to scope limitations rather than discrepancies).
   - **FAILED** — Substantive discrepancies that undermine the published conclusions.
   - **BLOCKED** — Reproduction could not proceed due to missing data, inaccessible
     software, or other barriers outside the analyst's control.

### Reporting Principles

- **Transparency over advocacy**: The report should enable a reader to form their own
  judgement, not argue for a particular conclusion.
- **Quantify everything**: Counts, percentages, and specific values — not vague language
  like "most results matched."
- **Distinguish reproduction quality from paper quality**: A successful reproduction
  confirms that the computational pipeline works as described. It does not validate the
  research design, theoretical framework, or interpretation of results.
