# Execution and Verification Prompt — Session R-B

**Version:** 1.0
**Last Updated:** 2026-02-10
**Session:** R-B (Execution and Verification)
**Skill:** reproduction-assessor
**Prerequisite:** Successful Docker build and script adaptation from Session R-A

---

## Your Task

Execute the analysis in Docker, quantitatively compare all results against published values, and write the three documentation artefacts (environment.md, log.md, comparison-report.md). By the end of this session, the reproduction has a verdict.

**Input:** Working Docker image, adapted scripts, data files, approved reproduction plan with verification targets

**Output:** Generated analysis outputs, quantitative comparison report with verdict, environment specification, reproduction log

---

## Critical Rules

1. **Execute in Docker.** The analysis must run inside the Docker container, not on the host. This is the whole point of isolated reproduction.
2. **Capture all output.** Plots to PDF/PNG, tables to CSV, statistics to text files. Nothing should exist only in console output.
3. **Compare EVERY verification target.** The plan identified specific tables, figures, and statistics. Compare all of them. Do not skip any.
4. **Use the correct classification.** Deterministic targets get exact-match comparison. Stochastic targets get HPD/CI interval comparison.
5. **Report honestly.** If something does not match, report it. Do not round, reinterpret, or reclassify to make it look better.
6. **Work autonomously within the session.** Complete execution, comparison, and documentation without stopping.

---

## Procedure

### Phase 1: Execute the Analysis

#### 1.1 Local Execution (< 1 hour)

```bash
# Run in container with volume mount for outputs
docker run --rm \
  -v $(pwd)/outputs/{paper-slug}/reproduction/attempt-{NN}/outputs:/project/outputs \
  reproduction-{slug} \
  Rscript run-analysis.R 2>&1 | tee outputs/{paper-slug}/reproduction/attempt-{NN}/outputs/run.log
```

#### 1.2 Sapphire Execution (> 1 hour)

```bash
# Build on sapphire
ssh sapphire "cd ~/cc-scratch/{project} && docker build -t reproduction-{slug} ."

# Launch detached container
ssh sapphire "docker run -d --name repro-{slug} \
  -v ~/cc-scratch/{project}/outputs:/project/outputs \
  reproduction-{slug} \
  Rscript run-analysis.R"

# Monitor
ssh sapphire "docker logs -f repro-{slug}"
```

#### 1.3 Parallel MCMC (Multiple Independent Runs)

For analyses with multiple independent model runs:

1. Create separate working directories per run (prevent write conflicts)
2. Launch each in a detached container
3. Monitor with `docker stats --no-stream`
4. Wait for all to complete before comparison

#### 1.4 Execution Verification

After execution completes:

- Check exit code (0 = success)
- Verify expected output files exist
- Check output file sizes (not empty, plausible sizes)
- Review run.log for errors or warnings

### Phase 2: Quantitative Comparison

Follow the Verification Strategy framework from the skill (§C).

#### 2.1 Deterministic Results

For each deterministic verification target:

1. Extract the published value from the paper (table, text, supplement)
2. Extract the reproduced value from the output files
3. Compare at the precision reported in the paper
4. Classify: EXACT_MATCH, WITHIN_PRECISION, or DISCREPANCY

**Transcription accuracy is critical.** Double-check both published and reproduced values. Transposed digits are the most common comparison error.

#### 2.2 Stochastic Results (MCMC/Bayesian)

For each stochastic verification target:

1. Extract published point estimate AND confidence/HPD interval
2. Extract reproduced point estimate from fresh output
3. Check: does reproduced value fall within the published interval?
4. Check: is the qualitative conclusion unchanged?
5. Classify: WITHIN_CONFIDENCE, MINOR_DISCREPANCY, or MAJOR_DISCREPANCY

#### 2.3 Figure Comparison

For each figure verification target:

1. Generate the reproduced figure (PDF or PNG)
2. Compare visually with the published figure:
   - Same axes, scales, orientation?
   - Same trends, clusters, distributions?
   - Same relative positions of elements?
3. Note: exact pixel matching not expected (rendering differences)
4. Focus: does the figure communicate the same scientific content?

#### 2.4 Stress-Testing

Actively search for failure modes that are hardest to detect:

- Check values that the reproduction "almost" gets right — are they truly within tolerance?
- Look for off-by-one errors in table comparisons (wrong row or column)
- Verify that reported "exact matches" are genuinely exact, not rounded matches
- Check whether any verification targets were silently skipped

**For complete verification strategies and discrepancy classification:**
→ Consult `references/verification-strategies.md`

### Phase 3: Documentation

Write the three required documentation artefacts. Use the templates from the skill references.

#### 3.1 Environment Specification

**File:** `outputs/{paper-slug}/reproduction/attempt-{NN}/environment.md`

**Template:** `references/templates/environment-template.md`

Contents:

- Software versions (R, key packages, Docker base)
- System dependencies added to Docker
- R package dependencies (significant transitive deps)
- Data source(s) with provenance
- Upstream software (if applicable — what was not reproduced)
- Notes (version selection rationale, determinism properties)

#### 3.2 Reproduction Log

**File:** `outputs/{paper-slug}/reproduction/attempt-{NN}/log.md`

**Template:** `references/templates/log-template.md`

Contents:

- Timeline (activities with approximate durations)
- Modifications required (Dockerfile, script adaptation, data, indices)
- Outputs generated (filenames, descriptions, sizes)
- FAIR/machine-actionability findings

#### 3.3 Comparison Report

**File:** `outputs/{paper-slug}/reproduction/attempt-{NN}/comparisons/comparison-report.md`

**Template:** `references/templates/comparison-report-template.md`

Contents:

- Verdict (SUCCESSFUL / PARTIAL / FAILED / BLOCKED)
- Quantitative results (ALL values compared, with tables)
- Qualitative results (figure descriptions)
- Methodology (environment, data, analysis type, comparison approach)
- Why the observed match level is expected
- Scope limitations (if applicable)
- Verdict justification (2-3 sentences connecting evidence to verdict)

### Phase 4: Queue Update

Update `studies/open-science-compliance/corpus/queue.yaml`:

- Set `reproduction_attempted: true`
- Add `reproduction:` section with date, verdict, details
- Update notes

---

## Handoff

```text
Session R-B complete for {paper-slug}

Completed:
- Execution: {runtime, resource used}
- Verification: {N/M values matched, category breakdown}
- Documentation: environment.md, log.md, comparison-report.md written
- Queue: updated

Verdict: {SUCCESSFUL / PARTIAL / FAILED / BLOCKED}
Justification: {1-2 sentence summary}

Next session: R-C (Adversarial Review)
Ready to continue when you are.
```

---

## Common Pitfalls

- **Running on host instead of Docker.** The analysis must run inside the container. Volume mounts persist results to the host filesystem.
- **Incomplete comparison.** Checking only the "headline" results and skipping supplementary tables or inline statistics.
- **Transcription errors.** Wrong row, wrong column, transposed digits when extracting published values.
- **Rounding to hide discrepancies.** Compare at the precision the paper reports. Do not round further.
- **Favourable interpretation of ambiguous results.** If a value is borderline, flag it rather than rounding towards "match".
- **Forgetting the log.** Timeline and modification details are essential for the adversarial review session.

---

## Decision Framework References

- **SKILL.md** §C — Verification Strategy (deterministic vs stochastic)
- **SKILL.md** §D — Compute Resource Allocation
- **SKILL.md** §E — Discrepancy Classification
- **references/verification-strategies.md** — HPD interval checking, figure assessment
- **references/templates/** — Document structure templates
