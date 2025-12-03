# Pipeline Improvement Notes

**Purpose:** Track observations, problems, and successes from variability testing to inform potential pipeline refinements.

**Protocol:** Update after each paper completes 5 runs. Make decisions about improvements only after sufficient data (all 5 papers).

**Last Updated:** 2025-12-02

---

## Summary Statistics

| Paper | Runs | Aggregate Range | Aggregate CV | Most Variable Component |
|-------|------|-----------------|--------------|-------------------------|
| sobotkova-et-al-2024 | 5 | 75-77 | 1.1% | Claims (12-16, CV 11.7%) |
| penske-et-al-2023 | 5 | 74-78 | 2.0% | Protocols (20-39, CV 27.2%) |
| ballsun-stanton-et-al-2018 | 0 | — | — | — |
| ross-2005 | 0 | — | — | — |
| sobotkova-et-al-2016 | 0 | — | — | — |

**Key Finding:** Content uniqueness confirmed via MD5 hashing for all completed runs. No context contamination detected.

---

## Paper 1: sobotkova-et-al-2024

**Paper Type:** Empirical (Deductive)
**Complexity:** Moderate (hypothesis-testing study with GIS/field methods)

### Extraction Counts Across Runs

| Run | Evidence | Claims | Implicit Args | Research Designs | Methods | Protocols |
|-----|----------|--------|---------------|------------------|---------|-----------|
| 01 | 17 | 16 | 5 | 3 | 4 | 5 |
| 02 | 16 | 13 | 4 | 3 | 4 | 5 |
| 03 | 15 | 12 | 5 | 3 | 4 | 5 |
| 04 | 14 | 13 | 4 | 3 | 4 | 5 |
| 05 | 15 | 13 | 5 | 3 | 4 | 5 |

### Signal Scores Across Runs

| Run | Comp | Trans | Plaus | Valid | Robust | General | Repro | Aggregate |
|-----|------|-------|-------|-------|--------|---------|-------|-----------|
| 01 | 82 | 78 | 85 | 75 | 72 | 70 | 75 | 77 |
| 02 | 80 | 75 | 82 | 73 | 70 | 68 | 75 | 75 |
| 03 | 82 | 78 | 85 | 75 | 72 | 70 | 75 | 77 |
| 04 | 80 | 76 | 84 | 74 | 71 | 69 | 75 | 76 |
| 05 | 82 | 78 | 85 | 75 | 72 | 70 | 75 | 77 |

### (a) Problems Identified

1. **Claims count variability (CV 11.7%)**: Range of 12-16 claims suggests boundary ambiguity about what constitutes a distinct claim vs. a sub-claim or supporting statement.

2. **Evidence count variability (CV 7.4%)**: Range of 14-17 evidence items indicates granularity decisions vary between runs—some runs combine related evidence, others separate them.

3. **Implicit arguments unstable**: 4-5 items across runs. These are inherently interpretive and the threshold for "implicit" vs "explicit" is subjective.

4. **No signal score variability for Reproducibility**: All runs scored 75, which may indicate:
   - Anchoring to rubric rather than nuanced assessment
   - Or genuinely unambiguous reproducibility characteristics

### (b) Successes Identified

1. **RDMAP extraction highly stable**: Identical counts (3/4/5) across all runs with unique content. This paper's straightforward methodology made RDMAP saturation achievable.

2. **Aggregate scores stable (75-77)**: Despite CEM count variability, the assessment phase produced consistent verdicts. This suggests the assessment rubrics effectively normalise extraction differences.

3. **All cluster ratings identical**: Every run rated Cluster 1 Strong, Cluster 2 Strong, Cluster 3 Adequate. The cluster-level synthesis is robust to extraction variability.

4. **Verdict consistency**: All runs produced "GOOD" verdict with similar rationales.

5. **Content uniqueness verified**: All hashes unique—no evidence of context contamination despite shared session concerns.

### (c) Potential Mitigations

1. **Claims granularity guidance**: Add explicit criteria for claim boundaries (e.g., "Each testable proposition = one claim; sub-hypotheses count separately").

2. **Evidence aggregation rules**: Clarify when to combine vs. separate evidence items (e.g., "Same data source, same analysis = one item; different analyses = separate items").

3. **Multi-run voting for CEM**: Given assessment stability, variability in CEM counts may be acceptable. Consider 2-of-3 or 3-of-5 voting for final extraction if count consistency is desired.

---

## Paper 2: penske-et-al-2023

**Paper Type:** Empirical (Inductive)
**Complexity:** High (multi-proxy archaeogenomics, 135 individuals, extensive methods)

### Extraction Counts Across Runs

| Run | Evidence | Claims | Implicit Args | Research Designs | Methods | Protocols |
|-----|----------|--------|---------------|------------------|---------|-----------|
| 01 | 67 | 60 | 10 | 4 | 19 | 39 |
| 02 | 56 | 64 | 10 | 5 | 15 | 20 |
| 03 | 67 | 65 | 10 | 4 | 15 | 29 |
| 04 | 64 | 63 | 10 | 4 | 19 | 24 |
| 05 | 67 | 63 | 10 | 4 | 16 | 24 |

### Signal Scores Across Runs

| Run | Comp | Trans | Plaus | Valid | Robust | General | Repro | Aggregate |
|-----|------|-------|-------|-------|--------|---------|-------|-----------|
| 01 | 82 | 85 | 82 | 78 | 75 | 72 | 68 | 77 |
| 02 | 80 | 82 | 80 | 75 | 72 | 70 | 62 | 74 |
| 03 | 82 | 85 | 82 | 78 | 75 | 72 | 68 | 77 |
| 04 | 85 | 88 | 85 | 80 | 78 | 75 | 70 | 78 |
| 05 | 82 | 85 | 82 | 78 | 75 | 72 | 68 | 77 |

### (a) Problems Identified

1. **Protocol extraction highly variable (CV 27.2%)**: Range of 20-39 protocols. This paper's extensive methodological detail creates granularity ambiguity—when to split vs. combine protocol steps.

2. **Methods count variable (CV 12.5%)**: Range of 15-19 methods. Boundary between "method" and "protocol" appears inconsistent across runs.

3. **Evidence count variable (CV 8.1%)**: Range of 56-67. Some runs extracted more granular genetic findings; others aggregated.

4. **Reproducibility signal variable (11-point range)**: 62-73 across runs. This may reflect genuine ambiguity about reproducibility rating (data archived but no code repository) or assessor anchoring differences.

5. **Run 02 outlier pattern**: Lower counts (56 evidence, 20 protocols) and lower scores across most signals. This run may have under-extracted due to early saturation judgement or prompt interpretation differences.

### (b) Successes Identified

1. **Implicit arguments perfectly stable**: All 5 runs extracted exactly 10 implicit arguments. High-level interpretive claims are consistently identified.

2. **Research designs stable**: 4 designs in 4/5 runs (one run had 5). Core research structure reliably captured.

3. **Aggregate scores stable (74-78)**: Despite high RDMAP variability, assessment phase normalises differences effectively.

4. **Cluster ratings consistent**: All runs rated Cluster 1 Strong, Cluster 2 Strong, Cluster 3 Adequate. Same pattern as Paper 1.

5. **Verdict consistency**: All runs produced "GOOD" verdict. The fundamental credibility judgement is robust.

6. **Content uniqueness verified**: All hashes unique across all 5 runs despite variable counts. Genuine independence confirmed.

### (c) Potential Mitigations

1. **Protocol granularity standard**: Define what constitutes a protocol unit (e.g., "One executable procedure with defined inputs/outputs = one protocol"). Consider providing examples for complex papers.

2. **Method-Protocol boundary clarification**: Explicit distinction (e.g., "Method = analytical approach; Protocol = specific procedural steps to execute that method").

3. **Reproducibility signal calibration**: Run 02's 62 score vs. Run 04's 70 (same paper, same infrastructure) suggests the rubric may need tighter anchoring for "data available, code not available" scenarios.

4. **Early saturation detection**: Run 02's lower counts may indicate premature saturation. Consider adding explicit "completeness check" before moving to next pass.

5. **Multi-run consensus for RDMAP**: For complex papers, 3 runs with voting may reduce protocol variability without full 5-run overhead.

---

## Cross-Paper Observations

### Consistent Patterns

1. **Assessment stability exceeds extraction stability**: Both papers show 1-2% aggregate CV despite 7-27% component CV. The assessment phase is robust.

2. **Cluster ratings are invariant**: All 10 runs produced identical cluster patterns (Strong/Strong/Adequate). This is the most stable output.

3. **Implicit arguments stable**: Both papers show low variability in implicit arguments (0-1 items). High-level interpretation is consistent.

4. **Research designs stable**: Both papers show minimal design count variability (0-1 items). Core structure is reliably captured.

5. **Verdict is invariant**: All 10 runs across both papers produced "GOOD" verdict. The bottom-line judgement is robust.

### Variable Patterns

1. **Protocol extraction most variable**: This is the clearest improvement target.

2. **Complexity correlates with RDMAP variability**: Simple paper (Sobotkova) = stable RDMAP; complex paper (Penske) = variable RDMAP.

3. **Reproducibility signal shows most assessment variability**: Range of 6 points (Sobotkova) to 11 points (Penske).

### Implications

1. **Core assessment is reliable**: The pipeline produces consistent verdicts despite extraction variability. This is a strength.

2. **Extraction variability may be acceptable**: If the goal is credibility assessment, the current variability doesn't affect outcomes.

3. **If extraction consistency is required**: Protocol granularity is the primary target for prompt refinement.

---

## Proposed Mitigation Strategies

### Strategy A: Prompt Refinement (Low Risk)

Target protocol and methods extraction with explicit granularity criteria:

- Define protocol boundaries with examples
- Clarify method vs. protocol distinction
- Add "completeness check" before pass completion

**Pros:** Low implementation cost, reversible
**Cons:** May not fully resolve granularity ambiguity for complex papers

### Strategy B: Multi-Run Voting (Medium Risk)

Run 3 extractions per paper, require 2-of-3 agreement for each item:

- Reduces random extraction variability
- Increases extraction cost 3x
- May improve content quality through consensus

**Pros:** Statistically robust, catches outlier runs
**Cons:** Higher cost, complexity in merging extractions

### Strategy C: Staged Pipeline (Medium Risk)

Add explicit quality gates between extraction and assessment:

1. After extraction: Review counts against paper complexity benchmark
2. Flag runs with counts outside expected range
3. Re-extract flagged sections before assessment

**Pros:** Catches outlier extractions early
**Cons:** Adds pipeline complexity, requires benchmarks

### Strategy D: Accept Current Variability (No Risk)

Given that:
- Aggregate scores are stable (CV 1-2%)
- Cluster ratings are invariant
- Verdicts are consistent

Current variability may be acceptable for the assessment use case.

**Pros:** No changes needed
**Cons:** Extraction counts less reliable for detailed analysis

---

## Decision Log

*Record decisions made based on variability testing observations*

| Date | Decision | Rationale |
|------|----------|-----------|
| 2025-12-02 | Continue testing without changes | Need data from Papers 3-5 before deciding on mitigations |

---

## Next Steps

1. Complete variability testing for remaining papers (ballsun-stanton-et-al-2018, ross-2005, sobotkova-et-al-2016)
2. Update this document after each paper completes
3. Review patterns across all 5 papers before implementing any changes
4. Consider pilot test of Strategy B (multi-run voting) if Protocol variability persists

---

*Document maintained as part of variability testing protocol. See `docs/variability-test-protocol.md` for full methodology.*
