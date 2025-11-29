# Credibility Assessment Implementation Roadmap
## From Metrics to Individual Paper Credibility Reports

**Document Purpose:** Concrete implementation plan for building credibility assessment capability

**Date Created:** 2025-11-16
**Status:** Implementation-ready roadmap
**Estimated Total Effort:** 15-20 hours for initial capability

---

## Design Decisions Summary (Finalised)

### Fundamental Decisions ✅

1. **Target:** Individual papers (not corpus aggregates)
2. **Workflow:** Maximum Claude automation (autonomous, not scripted)
3. **Approach flexibility:** Inductive/deductive/abductive-specific criteria
4. **Report format:** 3-5 page summaries initially (expand to 10+ pages after validation)
5. **RepliCATS alignment:** Close enough to reproduce their analysis as external validation
6. **Two-track analysis:** Separate extraction quality (Track A) from paper credibility (Track B)
7. **Credibility definitions:** Approach-specific and domain-sensitive

### Classification Decisions ✅

- **Q1 Timing:** After extraction (Option B) - Pass 6.5 or early Pass 7
- **Q2 Method:** Contextual inference with expressed vs revealed comparison
- **Q3 Mixed-method:** Qualitative characterisation, avoid false precision percentages
- **Q4 Validation:** Iterative refinement across corpus, expert review where feasible

### Assessment Framework Decisions ✅

- **Q5 Weighting:** Narrative determines importance, experiment with percentage weights in notes
- **Q6 Rubrics:** Develop empirically - start universal, fork if needed (iterate across corpus)
- **Q7 Scope:** Assess all seven signals for repliCATS compatibility, mark N/A where appropriate

### Track A/B Workflow Decisions ✅

- **Q8 Track A approach:** Start with metric-based quality proxies + spot-checking
- **Q9 Transition:** Run both tracks in parallel with reducing Track A overhead over time
- **Q10 Quality threshold:** Already meet minimum - focus on continuous improvement

### RepliCATS Alignment Decisions ✅

- **Q11 Methodology:** Sufficient documentation in `docs/background-research/`
- **Q12 Corpus access:** Build complete tool on 10-11 papers first, then validate on repliCATS corpus
- **Q13 Adaptation:** Document divergences explicitly (HASS-specific adaptations)

---

## Implementation Phases

### Phase 1: Research Approach Classification (Week 1, 3-4 hours)

**Goal:** Build and test classifier for research approach (deductive/inductive/abductive)

**Tasks:**
1. ✅ Create classification framework document (COMPLETE)
2. Build classification workflow
   - Prompt template for expressed approach detection
   - Prompt template for revealed approach inference
   - Comparison and HARKing detection logic
   - Output schema (YAML in classification.json)
3. Test on 3 papers:
   - sobotkova-et-al-2024 (predicted: primarily inductive)
   - ballsun-stanton-et-al-2018 (predicted: mixed methodological)
   - penske-et-al-2023 (predicted: deductive)
4. Document classification patterns and refinements

**Outputs:**
- `/assessment-system/prompts/classify_research_approach.md` (prompt template)
- `/outputs/{paper-id}/classification.json` (per-paper classifications)
- `/planning/classification-testing-log.md` (refinement notes)

**Success criteria:**
- All 3 papers classified with high confidence
- Expressed vs revealed comparison working
- "None stated" cases handled appropriately
- Classification justifications reference specific extraction elements

---

### Phase 2: Universal Signal Rubrics (Week 1-2, 4-6 hours)

**Goal:** Create assessment rubrics for seven repliCATS signals, adapted for HASS

**Tasks:**
1. Draft seven universal rubrics:
   - Comprehensibility (claim clarity, scope, argument traceability)
   - Transparency (research design, methods documentation, repository links)
   - Plausibility (domain coherence, chronology, comparanda)
   - Validity (evidence adequacy, alternatives considered, limitations)
   - Robustness (sensitivity analyses, triangulation, analytical alternatives)
   - Replicability (analytic reproducibility, data/code availability, FAIR/CARE)
   - Generalisability (scope constraints, limitation statements, appropriate bounds)

2. For each rubric:
   - Scoring scale (0-100) with anchors (0-19, 20-39, 40-59, 60-79, 80-100)
   - Assessment questions (5-7 key questions per signal)
   - Automated feature detection (what from extraction informs this signal?)
   - Approach-specific interpretation notes (how does this signal apply to inductive vs deductive research?)
   - Example red flags (low scores) and green flags (high scores)

3. Document approach-specific emphasis:
   - Deductive: PRIMARY = Validity, Robustness, Replicability
   - Inductive: PRIMARY = Transparency, Comprehensibility, Generalisability
   - Abductive: PRIMARY = Plausibility, Validity, Robustness

**Outputs:**
- `/assessment-system/rubrics/comprehensibility-rubric.md`
- `/assessment-system/rubrics/transparency-rubric.md`
- `/assessment-system/rubrics/plausibility-rubric.md`
- `/assessment-system/rubrics/validity-rubric.md`
- `/assessment-system/rubrics/robustness-rubric.md`
- `/assessment-system/rubrics/replicability-rubric.md`
- `/assessment-system/rubrics/generalisability-rubric.md`
- `/assessment-system/rubrics/README.md` (rubric index with approach-specific guidance)

**Success criteria:**
- All seven rubrics complete with scoring anchors
- Assessment questions clearly stated
- Approach-specific notes included
- Rubrics reference repliCATS guidance from background-research/

---

### Phase 3: Pilot Single-Paper Assessment (Week 2, 4-5 hours)

**Goal:** Generate first complete credibility assessment report with integrated quality tracking

**Tasks:**
1. Select well-extracted paper (sobotkova-et-al-2024 recommended)
2. Run full assessment workflow:
   - **Step 0:** Load research-assessor skill
   - **Step 1:** Classify research approach (from Phase 1)
   - **Step 2:** Assess all seven signals using rubrics (from Phase 2)
   - **Step 3:** Track extraction quality (Track A) during assessment
   - **Step 4:** Generate 3-5 page summary report
3. Report structure:
   - Paper metadata & approach classification (0.5 pages)
   - Metric scorecard (from Phase 6 metrics) (0.5 pages)
   - Seven-signal assessment (1-2 pages, ~200 words per signal)
   - Key strengths & weaknesses (0.5 pages)
   - Actionable recommendations (0.5 pages)
   - Overall credibility profile (0.5 pages)
   - Track A quality notes (extraction confidence, areas of uncertainty)
4. Generate report markdown file
5. Review and refine

**Outputs:**
- `/outputs/sobotkova-et-al-2024/assessment/credibility-report-v1.md` (first pilot report)
- `/planning/pilot-assessment-refinements.md` (notes on what to improve)
- Updated rubrics based on application experience

**Success criteria:**
- Complete 3-5 page report generated
- All seven signals assessed with scores and justifications
- Approach-specific emphasis applied appropriately
- Track A quality tracking integrated
- Report references specific extraction elements (claim IDs, evidence IDs, etc.)
- Identifies concrete improvement recommendations

---

### Phase 4: Iterative Refinement (Week 2-3, 4-6 hours)

**Goal:** Test assessment on 2-3 more diverse papers, refine rubrics and workflow

**Tasks:**
1. Select 2-3 additional papers:
   - Different research approaches (ensure inductive, deductive, abductive represented)
   - Different quality levels (high, medium credibility)
   - Different domains if available (archaeology, ecology, computational)
2. Run assessment on each:
   - Classify approach
   - Assess seven signals
   - Generate 3-5 page reports
   - Track quality and refinement needs
3. Cross-paper analysis:
   - Are rubrics working consistently?
   - Do approach-specific frameworks make sense?
   - Are scores discriminating appropriately?
   - What patterns emerge?
4. Refine:
   - Update rubrics based on empirical use
   - Adjust approach-specific guidance
   - Improve report template
   - Document classification heuristics

**Outputs:**
- 2-3 additional credibility reports
- Updated rubrics (v1.1)
- `/planning/cross-paper-assessment-patterns.md` (empirical findings)
- Refined classification heuristics

**Success criteria:**
- Consistent application of rubrics across papers
- Approach-specific assessments feel appropriate
- Reports provide actionable insights
- Beginning to see credibility patterns across corpus

---

### Phase 5: Documentation and Workflow Integration (Week 3-4, 2-3 hours)

**Goal:** Formalise workflow, create user documentation, integrate with existing system

**Tasks:**
1. Create assessment workflow documentation:
   - Update WORKFLOW.md to include credibility assessment phase
   - Document inputs (extraction.json, metrics) and outputs (credibility report)
   - Describe integration points with existing passes
2. Create user guide:
   - How to run credibility assessment
   - How to interpret credibility reports
   - How to use reports for improvement
3. Integration with existing tools:
   - Update batch-assess.py to optionally trigger credibility assessment
   - Create assessment-system/scripts/ directory structure
   - Document Track A / Track B separation

**Outputs:**
- Updated `input/WORKFLOW.md` (include credibility assessment phase)
- `/docs/assessment-guide/how-to-assess-credibility.md` (user guide)
- `/docs/assessment-guide/interpreting-credibility-reports.md` (interpretation guide)
- `/assessment-system/README.md` (assessment system overview)

**Success criteria:**
- Clear workflow documentation
- Assessment process reproducible by following docs
- Integration with existing extraction workflow documented

---

## Phase Summary & Timeline

| Phase | Effort | Timeline | Status |
|-------|--------|----------|--------|
| 1. Research Approach Classification | 3-4 hours | Week 1 | Framework complete, implementation pending |
| 2. Universal Signal Rubrics | 4-6 hours | Week 1-2 | Pending |
| 3. Pilot Single-Paper Assessment | 4-5 hours | Week 2 | Pending |
| 4. Iterative Refinement | 4-6 hours | Week 2-3 | Pending |
| 5. Documentation & Integration | 2-3 hours | Week 3-4 | Pending |
| **TOTAL** | **17-24 hours** | **3-4 weeks** | **Planning complete** |

---

## Immediate Next Steps (This Week)

### Priority 1: Complete Phase 1 (Research Approach Classification)

**Action items:**
1. Create `/assessment-system/prompts/classify_research_approach.md`
2. Build classification workflow (Claude autonomous)
3. Test on sobotkova-et-al-2024, ballsun-stanton-et-al-2018, penske-et-al-2023
4. Generate classification.json for each
5. Document patterns in `/planning/classification-testing-log.md`

**Estimated time:** 3-4 hours
**Outcome:** Research approach classifier working on 3 diverse papers

---

### Priority 2: Draft First Rubric (Transparency)

**Action items:**
1. Create `/assessment-system/rubrics/` directory
2. Draft `/assessment-system/rubrics/transparency-rubric.md` (most critical for HASS)
3. Include:
   - 0-100 scoring scale with five anchors
   - 5-7 assessment questions
   - Automated features (what from extraction informs this?)
   - Approach-specific notes
   - Examples (low/high scores)

**Estimated time:** 1 hour
**Outcome:** First rubric ready for testing

---

### Priority 3: Test Classification + Transparency Assessment

**Action items:**
1. Run combined workflow on sobotkova-et-al-2024:
   - Classify approach
   - Assess transparency signal
   - Generate mini-report (just transparency section)
2. Validate output quality
3. Refine prompt and rubric

**Estimated time:** 1-2 hours
**Outcome:** End-to-end proof of concept (classification → assessment → report)

---

## Track A Integration (Continuous Quality Monitoring)

### Track A Questions to Monitor Throughout

1. **Extraction Accuracy:**
   - Are extracted claims/evidence/RDMAP accurate?
   - Are there obvious omissions?
   - Are granularity levels appropriate?

2. **Metric Validity:**
   - Do metric scores align with qualitative assessment?
   - Are there metric-assessment mismatches?
   - Which metrics are most/least useful?

3. **Classification Quality:**
   - Does research approach classification feel correct?
   - Are expressed vs revealed comparisons accurate?
   - Are mixed-method characterisations appropriate?

4. **Assessment Consistency:**
   - Are rubrics being applied consistently?
   - Do scores discriminate appropriately?
   - Are justifications well-grounded in extraction?

### Track A Output Format

For each assessed paper, include Track A notes:

```markdown
## Track A: Extraction & Assessment Quality Notes

### Extraction Confidence
- **Overall:** High|Medium|Low
- **Claims extraction:** [notes on accuracy, completeness]
- **Evidence extraction:** [notes on accuracy, completeness]
- **RDMAP extraction:** [notes on accuracy, completeness]
- **Infrastructure extraction:** [notes on accuracy, completeness]

### Metric Validity
- **Metrics align with qualitative assessment:** Yes|Partial|No
- **Discrepancies noted:** [any metrics that don't match intuitive assessment]
- **Most useful metrics:** [which metrics most informative]
- **Least useful metrics:** [which metrics least informative]

### Classification Quality
- **Approach classification confidence:** High|Medium|Low
- **Classification notes:** [any uncertainty or ambiguity]

### Assessment Quality
- **Rubric application consistency:** [any difficulties applying rubrics]
- **Score confidence:** [confidence in assigned scores]
- **Areas of uncertainty:** [aspects of assessment that need validation]

### Improvement Opportunities
- [Specific suggestions for extraction improvement]
- [Specific suggestions for metric refinement]
- [Specific suggestions for rubric refinement]
```

---

## Success Criteria (Phase 1-5 Complete)

### Technical Success ✓
- Research approach classifier working on 10+ papers
- Seven signal rubrics validated through application
- 5-10 complete credibility reports generated
- Track A quality monitoring integrated
- Workflow documented and reproducible

### Methodological Success ✓
- Approach-specific assessment working (inductive/deductive/abductive)
- Expressed vs revealed comparison detecting methodological issues
- RepliCATS seven signals appropriately adapted for HASS
- Two-track analysis (extraction quality vs paper credibility) clearly separated

### Output Quality ✓
- 3-5 page reports are readable and actionable
- Scores discriminate between high/medium/low credibility papers
- Justifications reference specific extraction elements
- Recommendations are concrete and implementable
- Track A notes identify genuine improvement opportunities

---

## Future Enhancements (Post Phase 5)

### After Initial Capability Validated:

1. **Expand to 10+ page detailed reports** (add detailed justifications, CEM graph citations, evidence excerpts)
2. **RepliCATS corpus validation** (test on their papers, compare scores to their human panels)
3. **Multi-agent assessment** (following IDEA protocol with ensemble scoring)
4. **Corpus-level interpretation** (secondary analysis of credibility patterns)
5. **Interactive dashboards** (HTML visualisation of credibility profiles)
6. **Longitudinal tracking** (credibility trends over time, across disciplines)

---

## Questions & Decisions Log

### Decisions Made (2025-11-16)

1. ✅ Individual papers as assessment target
2. ✅ Maximum Claude automation
3. ✅ Approach-specific credibility frameworks
4. ✅ 3-5 page summary reports initially
5. ✅ RepliCATS alignment for validation
6. ✅ Two-track analysis (Track A: quality, Track B: credibility)
7. ✅ Option B for classification timing (after extraction)
8. ✅ Contextual inference for approach classification
9. ✅ Qualitative mixed-method characterisation
10. ✅ Narrative importance weighting
11. ✅ Empirical rubric development
12. ✅ Assess all seven signals
13. ✅ Parallel Track A/B with reducing overhead
14. ✅ Already meet quality threshold, focus on improvement
15. ✅ Build complete tool before repliCATS corpus validation

### Open Questions (To Be Resolved During Implementation)

1. Report visualisation: Radar charts? Tables? Text only?
2. Score representation: Point scores? Intervals? Distributions?
3. Uncertainty quantification: How to represent assessment confidence?
4. Audience framing: Single report or audience-specific versions?
5. Rubric evolution: When to fork universal rubrics into approach-specific versions?

---

## Document Status

**Version:** 1.0 (implementation-ready)
**Last Updated:** 2025-11-16
**Next Update:** After Phase 1 complete (classification tested)

**Related Documents:**
- `/planning/paper-credibility-analysis-framework.md` (fundamental design decisions)
- `/planning/research-approach-classification-framework.md` (classification detailed spec)
- `/planning/active-todo-list.md` (Task 10.2 tracking)
- `/docs/background-research/replicats-report.md` (repliCATS methodology)
- `/docs/background-research/replicats-seven-signals-hass-adaptation.md` (signal definitions)

**Implementation Priority:** HIGH (foundational for credibility assessment capability)
