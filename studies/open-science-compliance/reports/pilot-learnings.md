# Open Science Compliance Study - Pilot Learnings

**Study:** Open Science Compliance Study - Phase 1 Pilot
**Started:** 2025-01-12
**Last Updated:** 2025-01-12

---

## Purpose

This document captures learnings (successes, failures, surprises) during the Phase 1 pilot study. Updated before each session clear to preserve insights across context boundaries.

---

## Session Log

### Session 1: Study Setup (2025-01-12)

**Objective:** Establish study infrastructure, select papers, obtain PDFs

**Successes:**
- [x] Created full study folder structure
- [x] Collaboratively selected 5 diverse pilot papers
- [x] Drafted comprehensive study protocol with FAIR assessment methodology
- [x] Obtained all 5 PDFs (2 automated, 3 manual download)
- [x] Committed protocol to git (d6f0126)

**Failures:**
- [ ] Automated PDF download failed for 3/5 papers (DNS resolution, ScienceDirect redirects)

**Surprises:**
- JAS has had mandatory reproducibility reviews since January 2024 (stronger than expected)
- Ben Marwick published 2025 meta-analysis of JAS reproducibility - highly relevant to our study

**Decisions:**
- Full pipeline run (no streamlining) to test generalisation
- Session-per-pass approach with quality gates
- No agents/parallelism for now (reconsider at API stage)
- Priority: quality over speed

**Technical Notes:**
- ScienceDirect returns HTML redirects for direct PDF URLs
- HAL Science and faculty pages work better for automated download
- Session logs accessible at `~/.claude/projects/-home-shawn-Code-llm-reproducibility/`

---

### Session 2: First Paper Extraction (2025-01-12)

**Objective:** Complete full extraction pipeline (Pass 0-7) on crema-et-al-2024

**Status:** Completed (extraction + FAIR assessment)

**Successes:**
- [x] PDF text extraction successful (874 lines)
- [x] Full 8-pass extraction completed in single session
- [x] Created comprehensive extraction.json with all fields populated
- [x] Created detailed FAIR assessment (fair-assessment.yaml)
- [x] Paper scores 15/15 (100%) on code FAIR - exemplary compliance

**Extraction Counts:**
- 10 evidence items (quantitative data, simulation results, parameter estimates)
- 8 claims (methodological and empirical)
- 2 implicit arguments
- 3 research designs (methods development, simulation validation, case study application)
- 4 methods (hierarchical Bayesian, ICAR, simulation-based validation, posterior predictive)
- 7 protocols (MCMC settings, priors, convergence diagnostics)

**Failures:**
- None in this session

**Surprises:**
- Ben Marwick reviewed the code for this paper (mentioned in acknowledgements) - this adds independent verification of reproducibility
- Paper has exemplary infrastructure: GitHub + Zenodo DOI archival, CC BY licence, full CRediT statement, 4 funding sources documented
- JAS reproducibility review policy is delivering visible benefits (code review by specialist)

**Technical Notes:**
- pdftotext -layout worked well for text extraction
- Methods paper structure (development → validation → application) maps cleanly to RDMAP hierarchy
- Simulation validation studies provide clear evidence-claim linkages

---

## Cumulative Insights

### What Works Well

1. Collaborative paper selection with clear rationale documentation
2. Comprehensive protocol writing before starting extraction
3. YAML queue with per-paper status tracking
4. Full extraction pipeline runs smoothly on well-structured methods papers
5. FAIR assessment framework captures key reproducibility infrastructure

### What Needs Improvement

1. PDF acquisition workflow (need better automated sources)
2. Consider adding random seed documentation to FAIR checklist

### Patterns Emerging

1. **JAS reproducibility policy impact visible**: Ben Marwick code review noted in crema-et-al-2024
2. **Methods papers have clean RDMAP structure**: Three-tier hierarchy (development → validation → application) maps naturally to research designs
3. **Zenodo DOI archival is the FAIR differentiator**: GitHub + Zenodo = highly FAIR; GitHub only = partially FAIR
4. **Secondary data analysis papers need different FAIR treatment**: Data FAIR is "not applicable", not "not fair"

---

## Questions to Investigate

- [ ] How does pipeline perform on papers where analyst wasn't co-author?
- [ ] Which passes are most time-consuming?
- [ ] What extraction items are hardest to get right?

---

## Version History

| Date | Session | Changes |
|------|---------|---------|
| 2025-01-12 | 1 | Initial document, study setup complete |
| 2025-01-12 | 2 | Completed crema-et-al-2024 extraction + FAIR assessment |
