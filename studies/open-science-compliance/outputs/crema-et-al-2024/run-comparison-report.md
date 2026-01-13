# Run Comparison Report: crema-et-al-2024

**Paper:** Crema et al. (2024) "Modelling diffusion of innovation curves using radiocarbon data"
**Journal:** Journal of Archaeological Science, Vol. 165, Article 105962
**DOI:** 10.1016/j.jas.2024.105962
**Comparison Date:** 2026-01-13

## Extraction Approaches Compared

| Aspect | Run-01 | Run-02 |
|--------|--------|--------|
| Approach | Autonomous (single session) | Session-per-Pass |
| Schema | v2.5 | v2.6 |
| Sessions | 1 | 4 (A: Pass 0+6, B: Pass 1-2, C: Pass 3-5, D: Pass 7+FAIR) |

## Quantitative Summary

| Component | Run-01 (Autonomous) | Run-02 (Session-per-Pass) | Difference |
|-----------|---------------------|---------------------------|------------|
| Evidence items | 10 | 12 | +2 (+20%) |
| Claims | 8 | 14 | +6 (+75%) |
| Implicit arguments | 2 | 3 | +1 (+50%) |
| Research designs | 3 | 6 | +3 (+100%) |
| Methods | 4 | 6 | +2 (+50%) |
| Protocols | 7 | 10 | +3 (+43%) |

## Qualitative Differences

### 1. Evidence Extraction

Run-02 added two items Run-01 missed:

- **E011**: Japanese model deviations (overestimated 800-500 BCE, underestimated post-200 BCE)
- **E012**: British model deviations (negative 3700-2300 BCE, positive post-1600 BCE)

These are posterior predictive check findings — key diagnostic outputs that directly support interpretation claims. Run-01 captured the narrative conclusions but missed the specific diagnostic details.

### 2. Claims Extraction

Run-02 captured 6 additional claims:

- **C010**: Probabilistic equations 2-3 better suited to archaeological samples
- **C011**: Parametric vs non-parametric model complementarity
- **C012**: Posterior predictive check robustness/conservatism
- **C013**: Method accurately recovers temporal dynamics (conclusions claim)
- **C014**: Non-parametric model provides independent assessment

These are methodological claims that strengthen the argument chain. Run-01 focused on empirical findings and missed supporting methodological justifications.

### 3. Research Designs

Run-02 identified double the research designs:

- **RD004**: Theoretical shift from proportion-based to probability-based framework
- **RD005**: Japan/Britain case study selection rationale
- **RD006**: Direct dating strategy design choice

Run-01 captured the three main designs (development, simulation, application) but missed the embedded design decisions that justify methodological choices.

### 4. Methods and Protocols

Run-02 added:

- **M005**: Radiocarbon date filtering by cumulative probability
- **M006**: Binary classification of dates (domesticate vs non-domesticate)
- **P007-P010**: Region-specific filtering protocols and simulation parameters

These are operational details essential for reproduction — exactly what matters for FAIR assessment.

### 5. Structural Quality

Run-02 improvements:

- **Metadata**: Full author affiliations extracted (Run-01 had none)
- **Locations**: Structured `{section, subsection, page}` objects vs string locations
- **Cross-references**: More complete linkages between evidence→claims→RDMAP
- **Implicit arguments**: Added `assessment_implication` field explaining why each matters

## Interpretation

The session-per-pass approach yielded substantially richer extraction:

1. **Depth over breadth**: Run-02 didn't just find more items — it found the *connecting tissue* between items (methodological justifications, design rationales, operational protocols)

2. **Reproduction-relevant detail**: The additional protocols (P007-P010) and methods (M005-M006) are exactly what someone would need to replicate the analysis

3. **Structured metadata**: Run-02's attention to location structure and cross-references enables better validation and citation

4. **Implicit argument quality**: Run-02's `assessment_implication` field connects assumptions to assessment consequences — directly useful for credibility analysis

## Conclusion

For a methodological paper like this, the session-per-pass approach produced notably better extraction quality. The 75% increase in claims and 100% increase in research designs aren't just quantity gains — they represent capturing the methodological reasoning that makes the paper's argument coherent and its methods reproducible.

**Recommendation**: Session-per-pass is preferred for complex methodological papers. The added session overhead is justified by extraction quality gains.

## Files

- Run-01: `run-01-autonomous/extraction.json`
- Run-02: `run-02-session-per-pass/extraction.json`
- Paper text: `crema-et-al-2024.txt`
