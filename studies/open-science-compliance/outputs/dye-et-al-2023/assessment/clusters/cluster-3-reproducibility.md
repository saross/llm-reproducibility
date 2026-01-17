# Cluster 3: Reproducibility (Reproducibility Pillar)

**Paper:** Dye et al. (2023) - Bayesian Chronology Construction and Substance Time

**Signal assessed:** Reproducibility

**Research approach:** Abductive (methodological paper)

**Note:** Reproducibility is a **primary signal** for methodological papers.

---

## Computational Component Assessment

### Does the paper have computational components?

**Yes.** The paper includes:

1. **Bayesian chronological modelling** using OxCal (proprietary but free software)
2. **MCMC sampling and validation** (5 independent runs)
3. **Probability calculations** for mode inference from posterior samples
4. **Tempo and occurrence plot generation** using R/ArchaeoPhases
5. **Analytical derivations** (mathematical, not computational, but documented)

The computational workflow is central to the methodological contribution.

---

## Signal 7: Reproducibility

### Score: 80/100 (Excellent)

### Assessment

Using **abductive research anchors** adapted for computational methodology:

**Strengths meeting 80-100 band criteria:**

1. **Evidence sources fully documented and accessible:**
   - Original data from Archaeological Data Service with DOI (10.5284/1018290)
   - Data comes from Hines & Bayliss (2013) published source
   - Bead type definitions traceable to published corpus

2. **Reasoning process explicitly traceable:**
   - Allen's interval algebra derivations fully documented
   - Mode inference logic clearly specified (M004)
   - Probability calculation procedure documented (P004)

3. **Theoretical framework clearly specified:**
   - Event time vs substance time distinction operationalised
   - Three modes of change mathematically specified
   - Allen relations for each mode derived and documented

4. **Code and software accessible:**
   - **ArchaeoPhases R package on CRAN** — stable, maintained, open source
   - OxCal model code in supplementary materials
   - R scripts for tempo and occurrence plots in supplement

5. **Workflow documented:**
   - 10 protocols document analytical procedures
   - P001: OxCal model implementation with version (4.4.2)
   - P002: MCMC validation protocol
   - P003-P007: Specific analytical procedures

6. **Interpretive decisions explained:**
   - Constraint removal rationale documented (P005)
   - Chi-squared test justification provided
   - Model assumptions explicit

**Limitations preventing higher score:**

1. **Supplement lacks independent DOI:**
   - OxCal model and R scripts attached to journal
   - Not archived in stable repository (Zenodo, OSF, etc.)
   - Long-term accessibility depends on journal infrastructure

2. **OxCal is proprietary (but free):**
   - Requires downloading OxCal software
   - Not fully open source, though freely available
   - Version dependency (4.4.2) may cause issues over time

3. **Three implicit protocols:**
   - P008: Similarity estimation procedure not fully specified
   - P009: Transformation inference less detailed than branching
   - P010: Reticulation inference conceptually described but not procedurally operationalised

4. **Environment specification partial:**
   - OxCal version specified (4.4.2)
   - IntCal20 calibration curve specified
   - ArchaeoPhases R package version not specified in paper
   - R version not specified

5. **No explicit licence for supplement code:**
   - ArchaeoPhases is GPL licensed
   - Supplement code reuse conditions unclear

### Justification

Reproducibility scored 80 (Excellent band for abductive/methodological research). The reasoning process is fully traceable through documented methods, protocols, and mathematical derivations. Core code is available through ArchaeoPhases (CRAN) and supplementary materials. Data sources are documented with DOI. The main limitations are: (1) supplement lacks independent DOI for long-term stability, (2) three protocols remain implicit, (3) OxCal is proprietary though free, and (4) environment specification is partial. Despite these limitations, an experienced researcher could reproduce the analysis with reasonable effort.

---

## Reproducibility Readiness Checklist

```yaml
reproducibility_readiness:
  applies: true
  if_not_applicable_reason: null

  inputs_available:
    status: "yes"
    details: "Data from ADS (DOI: 10.5284/1018290) and Hines & Bayliss (2013). Bead type definitions from published corpus."

  code_available:
    status: "yes"
    tool_type: "mixed"
    details: |
      - ArchaeoPhases R package on CRAN (open source, GPL)
      - OxCal model code in supplement (proprietary software, free)
      - R scripts for plots in supplement
      - Mathematical derivations in paper text

  environment_specified:
    status: "partial"
    details: |
      - OxCal version: 4.4.2
      - Calibration curve: IntCal20
      - ArchaeoPhases: CRAN version (not specified)
      - R version: not specified

  outputs_documented:
    status: "yes"
    details: |
      - Tempo plots presented in figures
      - Occurrence plots presented
      - Mode probability estimates reported
      - Allen relation classifications documented

  execution_feasibility: "ready"
  feasibility_rationale: |
    Reproduction is feasible with reasonable effort:
    1. Install OxCal (free download)
    2. Install R and ArchaeoPhases from CRAN
    3. Obtain supplement materials from journal
    4. Run OxCal model
    5. Process output with ArchaeoPhases
    Main challenge: Three implicit protocols (P008-P010) may require author clarification.

  publication_year: 2023
  adoption_context: "late_early_adopter"
  adoption_notes: |
    Published 2023, during period of growing reproducibility expectations.
    Code sharing reflects contemporary standards for archaeological methodology papers.
    Package on CRAN is excellent practice.
    Supplement without DOI is below emerging best practice.
```

---

## FAIR Assessment Integration

From Pass 6 infrastructure extraction:

| FAIR Dimension | Score | Notes |
|----------------|-------|-------|
| Findable | 7/10 | Paper DOI, author ORCIDs (100%), ArchaeoPhases on CRAN, but supplement lacks DOI |
| Accessible | 7/10 | Open access, CRAN package, supplement via journal |
| Interoperable | 6/10 | Standard formats (R, OxCal), uses ADS dataset, no formal data schema |
| Reusable | 6/10 | CC-BY-NC-ND paper licence, ArchaeoPhases GPL, supplement licence unclear |
| **Total** | **26/40 (65%)** | Moderately FAIR |

### FAIR-Reproducibility Alignment

- FAIR score of 65% aligns with Reproducibility score of 80
- FAIR captures infrastructure aspects (DOIs, licences)
- Reproducibility score captures practical re-execution feasibility
- Both indicate moderate-to-good reproducibility infrastructure with specific gaps (supplement DOI, licence clarity)

---

## Cluster 3 Summary

| Signal | Score | Band | Priority |
|--------|-------|------|----------|
| Reproducibility | 80 | Excellent (80-100) | Primary |

### Reproducibility Assessment

The paper demonstrates **excellent reproducibility** for a methodological paper. Core analytical components are accessible through ArchaeoPhases (CRAN) and supplementary materials. Data sources are documented with DOI. The reasoning process is traceable through documented protocols and mathematical derivations. Execution is feasible with standard archaeological computing resources (R, OxCal).

### Primary Signal Assessment (for Methodological Paper)

As a methodological paper, Reproducibility is a **primary signal**. The score of 80 indicates the method can be implemented by others with documented procedures and available tools. The main improvement opportunity is archiving supplement materials with independent DOI for long-term accessibility.

### Reproduction Attempt Recommendation

**Priority:** HIGH (for pilot study reproduction queue)

**Feasibility:** Ready

**Recommended approach:**
1. Obtain OxCal model from supplement
2. Install ArchaeoPhases from CRAN
3. Run OxCal with IntCal20 calibration
4. Validate MCMC (compare with published 5-run results)
5. Generate tempo and occurrence plots
6. Compute mode probabilities and compare with published values

**Expected challenges:**
- OxCal version compatibility (4.4.2 vs current)
- Implicit protocol details (P008-P010) may need clarification
- Exact figure reproduction may require specific R package version
