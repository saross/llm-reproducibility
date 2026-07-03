# Open Science Compliance Study

**Status:** Phase 1 (Exploratory Pilot) — COMPLETE (2026-02-12). Phase 2 (Confirmatory) not yet started; OSF preregistration pending.
**Target Journal:** Journal of Archaeological Science (JAS)
**Corpus Size:** 5 papers (Phase 1), 15-25 papers (Phase 2)

## Research Goals

**(a) Publication:** Empirical study of open science/FAIR compliance in Q1 archaeology journal articles

**(b) Reproduction Feasibility:** Test whether papers with good open science apparatus can have results semi-automatically reproduced

## Study Design

### Phase 1: Exploratory Pilot (5 papers)

- No preregistered hypotheses
- Document methodology and generate descriptive findings
- Identify patterns for hypothesis development
- Output: Pilot findings report + hypothesis candidates

### Phase 2: Confirmatory Study (15-25 papers)

- Preregister hypotheses on OSF (based on Phase 1 observations)
- Test on fresh corpus (no overlap with Phase 1)
- Statistical analysis for publication

## Directory Structure

```text
studies/open-science-compliance/
├── README.md                    # This file
├── protocol/
│   ├── study-protocol.md        # Full methodology
│   ├── preregistration.md       # Preregistered hypotheses (Phase 2)
│   └── selection-criteria.md    # Corpus inclusion/exclusion
├── corpus/
│   ├── queue.yaml               # Paper processing queue
│   ├── pilot-papers.md          # Phase 1 paper list + rationale
│   └── confirmatory-papers.md   # Phase 2 paper list
├── outputs/
│   └── {paper-slug}/            # Per-paper extraction outputs
├── analysis/
│   ├── fair-summary.md          # FAIR compliance results
│   └── reproduction-summary.md  # Reproduction attempt results
└── reports/
    ├── pilot-findings.md        # Phase 1 report
    └── manuscript-draft.md      # Publication draft
```

## Selection Criteria

Papers must be:

1. Published 2023-2025 (post-reproducibility-policy for JAS)
2. Open Access (gold OA or green OA available)
3. Computational component (code + data mentioned)
4. English language

## Timeline

- [x] Phase 1 corpus selection (2026-01-09)
- [x] Phase 1 protocol commit (timestamped) (2026-01-09, commit d6f0126)
- [x] Phase 1 extractions (5 papers) — full pipeline including assessment and reproduction (completed by 2026-02-11)
- [x] Phase 1 findings report (2026-02-11, commit afab8f6; FAIR scores standardised 2026-02-12)
- [ ] Phase 2 hypothesis development (5 candidates drafted in pilot findings report §"Hypothesis Candidates")
- [ ] Phase 2 OSF preregistration
- [ ] Phase 2 corpus selection
- [ ] Phase 2 extractions
- [ ] Manuscript draft

## Related Files

- Plan: `~/.claude/plans/flickering-zooming-abelson.md`
- Main project: `/home/shawn/Code/llm-reproducibility/`
