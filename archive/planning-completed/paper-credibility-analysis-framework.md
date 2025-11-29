# Paper Credibility Analysis Framework
## Individual Paper Assessment with Research Approach Flexibility

**Document Purpose:** Framework for assessing individual paper credibility with approach-specific (inductive/deductive/abductive) criteria

**Date Created:** 2025-11-16 (reconstructed after VS Code crash)
**Status:** Planning phase - fundamental design decisions
**Phase:** Post-metrics implementation, pre-interpretation deployment

---

## Executive Summary: Fundamental Decisions Made

### Critical Design Decisions (Pre-Crash Discussion)

#### 1. Target of Evaluation: Individual Papers, Not Corpora ✅

**Decision:** Focus credibility assessment on **individual papers**, not corpus-level patterns.

**Rationale:**
- Credibility is paper-specific, not corpus-aggregate
- Individual assessments are actionable for authors
- Corpus patterns emerge from aggregating individual assessments (secondary analysis)
- Aligns with repliCATS approach (individual paper credibility estimates)

**Implication:** Primary output is **per-paper credibility report**, not corpus interpretation report

**Note:** This decision supersedes earlier planning in `corpus-interpretation-framework.md` (which focused on corpus-level patterns). Corpus interpretation becomes **secondary** analysis layer.

---

#### 2. Workflow Automation: Maximum Use of Claude Capabilities ✅

**Decision:** Leverage Claude Code's autonomous capabilities to maximum extent, not manual API scripting.

**Approach:**
- Bypass permissions enabled (CLAUDE.md autonomous work mode)
- Use file operations (Read, Write, Edit) extensively
- Use TodoWrite for task tracking and planning
- Use Skills (research-assessor) for domain knowledge
- Collaborative iteration on prompts and workflows
- In-context planning with file-based persistence

**Rationale:**
- Seamless collaboration on pipeline improvement
- Faster iteration cycles
- Better transparency (all planning/execution visible in files)
- Leverages Claude's multi-tool orchestration
- Reduces scripting overhead

**Implication:** Analysis workflow is **Claude-driven** with human oversight, not Python script automation

---

#### 3. Research Approach Flexibility: Inductive, Deductive, Abductive ✅

**Decision:** Credibility assessment criteria must **vary by research approach** (inductive/deductive/abductive).

**Approach-Specific Credibility Frameworks:**

| Research Approach | Primary Credibility Criteria | Assessment Focus |
|------------------|------------------------------|------------------|
| **Deductive** (hypothesis-testing) | Validity, Robustness, Replicability | Evidence sufficiency for claims, alternative explanations, reproducibility |
| **Inductive** (pattern-finding, exploratory) | Transparency, Comprehensibility, Generalisability | Research design clarity, scope constraints, pattern-data fit |
| **Abductive** (inference to best explanation) | Plausibility, Validity, Robustness | Explanatory coherence, alternative explanations, consilience |

**Mixed-Method Reality:**
- Many papers combine approaches (exploratory survey → confirmatory analysis)
- Assessment must be **flexible and adaptive**
- Not rigid classification, but **dominant approach with mixed elements**

**Who Decides Approach:**
- **Claude determines approach** during analysis (Pass 0 or early assessment)
- Use research designs, methods, explicit statements as evidence
- Flag mixed-method papers explicitly
- Iterate and refine classification heuristics over multiple papers

**Implication:** No single credibility rubric - need **approach-specific assessment frameworks**

---

#### 4. Incremental Reporting: 3-5 Page Summaries First ✅

**Decision:** Start with **concise 3-5 page summary reports** while refining analysis approach.

**Rationale:**
- Faster iteration on assessment framework
- Easier to review and validate
- Lower time investment per paper (allows testing on more papers quickly)
- Can expand to detailed 10+ page reports once framework validated

**Report Structure (Summary Version):**
1. Paper metadata and research approach classification (0.5 pages)
2. Metric scorecard with visualisation (0.5 pages)
3. Signal-by-signal brief assessment (1-2 pages)
4. Key strengths and weaknesses (0.5 pages)
5. Actionable recommendations (0.5 pages)
6. Overall credibility estimate with uncertainty (0.5 pages)

**Transition to Detailed Reports:**
- After 5-10 summary reports validated
- Expand with detailed justifications, CEM graph citations, evidence excerpts
- Target: 10-15 page comprehensive credibility assessment

---

#### 5. RepliCATS Alignment: Close Enough to Reproduce Their Analysis ✅

**Decision:** Follow repliCATS Seven Signals framework **closely enough to reproduce their analysis** on their corpus.

**Rationale:**
- External validation benchmark
- Can compare our automated assessments to their human expert panels
- Tests whether extraction → credibility pipeline works
- Credible evaluation of our methodology

**Alignment Requirements:**
- Use same seven signals (Comprehensibility, Transparency, Plausibility, Validity, Robustness, Replicability, Generalisability)
- Similar scoring scale (0-100 with uncertainty bounds)
- Comparable assessment criteria (adapt rubrics to match their guidance)
- Report format compatible with their scorecard structure

**Validation Test:**
- Identify papers assessed by repliCATS (public dataset available?)
- Run our extraction + assessment pipeline on same papers
- Compare scores signal-by-signal
- Calculate inter-rater reliability (our system vs repliCATS human panel)
- Document systematic differences and refine

**Implication:** Need to research repliCATS assessment methodology in detail (rubrics, training materials, scoring guidance)

---

#### 6. TWO-TRACK ANALYSIS: Extraction Quality vs Paper Credibility ✅ CRITICAL

**Decision:** **Separate** (a) extraction/metrics quality assessment from (b) paper credibility assessment.

**Track A: Extraction and Metrics Quality Assessment**
- **Purpose:** Evaluate our extraction and metrics system
- **Questions:**
  - Are extractions accurate and complete?
  - Do metrics discriminate between papers appropriately?
  - Are metrics reliable and valid?
  - Which metrics have most/least utility?
  - Are there systematic extraction biases?
- **Outputs:**
  - Extraction quality reports
  - Metric validation studies
  - Inter-rater reliability (human vs extraction)
  - Discriminative validity analysis
- **Audience:** Us (system developers)

**Track B: Paper Credibility Assessment**
- **Purpose:** Evaluate research papers' credibility
- **Questions:**
  - How credible is this paper's research?
  - What are its strengths and weaknesses?
  - Should this research be trusted?
  - How could the research be improved?
- **Outputs:**
  - Individual paper credibility reports
  - Signal scorecards
  - Recommendations for authors
- **Audience:** Researchers, reviewers, readers

**Critical Distinction:**
- Track A is **formative** (improving our system)
- Track B is **summative** (judging research quality)
- Track A informs Track B (better extraction → better credibility assessment)
- Must not conflate: "Low metric score" ≠ "Low credibility" if metric is invalid

**Implication:** Need **two distinct workflows and report types**

---

#### 7. Domain and Approach Variation in Credibility Definition ✅

**Decision:** "Credibility" must be **defined differently** for different research approaches and potentially domains.

**Approach-Specific Credibility Definitions:**

**Deductive/Confirmatory Research:**
- Credibility = Evidence adequacy for claims + robustness to alternatives + replicability
- Focus: Internal validity, statistical power, control of confounds
- RepliCATS signals emphasised: Validity, Robustness, Replicability

**Inductive/Exploratory Research:**
- Credibility = Transparency of process + pattern-data fit + scope discipline + plausibility
- Focus: Research design clarity, systematic observation, appropriate generalisation
- RepliCATS signals emphasised: Transparency, Comprehensibility, Generalisability

**Abductive/Explanatory Research:**
- Credibility = Explanatory coherence + consilience + plausibility + alternative consideration
- Focus: Inference quality, explanatory breadth, theoretical grounding
- RepliCATS signals emphasised: Plausibility, Validity, Robustness

**Domain Variation (Secondary):**
- HASS archaeology: Lower replicability expectations (field context uniqueness), higher transparency/generalisability
- Computational archaeology: Higher replicability expectations, code/data sharing norms
- Paleoecology: High robustness expectations (proxy validation), methodological triangulation

**Implication:** Cannot use single "overall credibility score" - need **approach-specific credibility profiles**

---

## Area 1: Research Approach Classification ✅ DECIDED

**What we decided:**
- Claude determines approach during analysis
- Flexibility for mixed-method papers
- Iterate classification heuristics

**Decisions made:**

### Q1: Classification Trigger Point ✅

**Decision: Option B - After extraction complete (Pass 6.5 or early Pass 7)**

**Rationale:**
- Full evidence available from extraction (RDMAP, claims, methods, evidence)
- Can compare stated approach (from introduction) vs revealed approach (from actual research)
- Doesn't add cognitive load to extraction passes
- Clean separation: extract → classify → assess
- Optimal balance of evidence availability and workflow clarity

**Implementation:** Add classification step between Pass 6 (infrastructure) and Pass 7 (validation), or integrate as first step of credibility assessment in Pass 7.

---

### Q2: Classification Evidence and Method ✅

**Decision: Contextual inference using Claude's NLP capabilities**

**Approach:**
- **Primary:** Claude reads research designs, methods, claims and infers approach contextually
- **Supporting:** Use classification rubric as guidance, not rigid rules
- **Critical addition:** Distinguish **expressed approach** (what paper says) vs **revealed approach** (what paper actually does)
- **HARKing detection:** Flag mismatches between expressed and revealed approaches
- **"None stated" significance:** If no methodological approach is stated, document this explicitly as indicator of methodological naivete/weak research design

**Evidence sources:**
- Explicit statements (research design declarations)
- Research designs extracted in RDMAP
- Methods characteristics and application
- Claims structure (hypothesis-framed, pattern-descriptive, explanatory)
- Evidence-claim relationships

**Special handling:** "No expressed method" is **significant information**, not something to strain to find. Document absence explicitly and note transparency implications.

---

### Q3: Mixed-Method Handling ✅

**Decision: Qualitative characterisation, avoid false precision**

**Approach:**
- Use "primary + secondary" labelling with qualitative descriptions
- **Example:** "Primarily inductive exploratory survey with confirmatory statistical analysis of observed patterns"
- Avoid percentage precision (e.g., "60% inductive") - implies false precision
- Provide qualifications and specifications as needed
- Work out representation iteratively across corpus

**Format:**
```yaml
primary_approach: "inductive"
qualifications:
  - "Overall inductive survey design"
  - "Includes reproducible statistical analysis of observed patterns"
  - "Statistical tests are post-hoc validation, not a priori hypotheses"
```

**Rationale:** Archaeological research often genuinely mixed; rigid categorisation inappropriate; qualitative description more accurate and honest.

---

### Q4: Approach Classification Validation ✅

**Decision: Iterative empirical validation across corpus**

**Approach:**
- Develop and refine classification heuristics iteratively as we classify more papers
- Document classification patterns and edge cases
- Compare to authors' stated approach when available (but don't assume author is correct)
- Expert review where feasible (but acknowledge we're testing our system, not deferring to authority)
- Build empirical understanding through corpus application

**Validation strategy:**
- Work it out iteratively across 10-11 paper corpus
- Document difficult cases and resolution logic
- Refine classification framework based on empirical experience
- Accept that classification involves interpretation and judgment

**Note:** We'll see what's relevant and what works as we apply the framework - empirical development preferred over theoretical specification.

---

## Area 2: Approach-Specific Assessment Frameworks ✅ DECIDED

**What we decided:**
- Different credibility criteria for different approaches
- Seven signals weighted differently by approach
- Flexible definitions of credibility

**Decisions made:**

### Q5: Signal Weighting by Approach ✅

**Decision: Narrative determines importance + experimental percentage weights**

**Approach:**
- **Primary:** Let narrative assessment determine signal importance naturally
- **Guidance:** Include qualitative emphasis in prompts (e.g., "For deductive research, validity and robustness are particularly critical")
- **Experimental:** Track/document percentage weightings in planning notes to see if patterns emerge
- **No enforcement:** Don't enforce numeric weights in actual assessment
- **Flexibility:** Allows edge case handling and nuanced judgment

**Rationale:**
- Avoids premature precision
- Provides data to evaluate whether explicit weights would help
- Maintains flexibility for complex cases
- Can discover natural weightings empirically

**Implementation:** Assessment prompts include emphasis guidance, but scores determined by evidence, not formula.

---

### Q6: Approach-Specific Rubrics ✅

**Decision: Develop empirically - start with 7 universal rubrics, fork if needed**

**Approach:**
- **Initial:** Create 7 universal rubrics (one per signal)
- **Include:** Approach-specific interpretation notes within each rubric
- **Monitor:** Track where approach-specific assessment substantially differs
- **Fork if needed:** Create separate rubrics only if distinctions become systematic and substantial
- **Iterate:** Work this out across corpus over multiple papers

**Rationale:**
- Avoid over-engineering upfront
- Discover genuine needs through application
- Start simple, add complexity only when empirically justified
- 7 rubrics more maintainable than 21

**Tracking mechanism:** Use planning docs to note "Validity assessment differed substantially for inductive vs deductive - consider separate rubrics after 5 more papers"

---

### Q7: Assessment Comprehensiveness ✅

**Decision: Assess all seven signals for repliCATS compatibility**

**Approach:**
- **Always assess all seven signals** (maintaining cross-paper comparability)
- **Mark N/A where appropriate** (e.g., replicability N/A for purely theoretical papers)
- **De-emphasise** non-primary signals in narrative (but still score them)
- **Maintain repliCATS structure** to enable future validation against their corpus

**Rationale:**
- Enables repliCATS validation (our key external benchmark)
- Maintains comparability across papers in corpus
- Allows empirical discovery of which signals matter for which approaches
- Future flexibility - can fork to HASS-specific subset later if needed
- Building system "robust enough for repliCATS but extensible beyond" (architectural principle)

**Note:** Goal is to replicate repliCATS analysis on their corpus as test of our system, so need structural compatibility.

---

## Area 3: Two-Track Analysis Workflow ✅ DECIDED

**What we decided:**
- Separate extraction quality assessment from paper credibility assessment
- Track A (system evaluation) informs Track B (paper evaluation)

**Decisions made:**

### Q8: Track A Workflow ✅

**Decision: Metric-based quality proxies + spot-checking, built into workflow as self-assessment**

**Approach:**
- **Primary:** Use existing credibility metrics as quality indicators (relationship density, completeness scores as proxies)
- **Secondary:** Manual spot-checking for high-stakes papers or when uncertainty flagged
- **Integration:** Build self-assessment into credibility assessment workflow (not separate step)
- **Continuous improvement:** Track A runs alongside Track B, providing ongoing quality monitoring
- **Audience:** Track A analysis is for us (system developers), not external reporting

**Implementation:**
- Include Track A quality notes in each credibility report
- Track extraction confidence, metric-assessment alignment, areas of uncertainty
- Document improvement opportunities

**Rationale:**
- Efficient - uses data we already have
- Integrated - doesn't require separate validation passes
- Practical - acknowledges we can't do extensive validation on every paper
- Improvement-focused - identifies concrete refinement opportunities

---

### Q9: Track A → Track B Transition ✅

**Decision: Run both tracks in parallel with reducing overhead over time**

**Approach:**
- **No hard transition:** Both tracks run continuously, not sequential phases
- **Variable intensity:**
  - First 3-5 papers: Heavy Track A validation and monitoring
  - Papers 6-10: Reduced Track A (spot-checking, metric monitoring)
  - Beyond 10 papers: Minimal routine quality monitoring, Track A on new paper types only
- **Feedback loop:** Track A findings inform extraction improvements, which improve Track B quality
- **Continuous improvement:** Always monitoring, always refining, intensity varies

**Rationale:**
- Parallel tracks enable continuous feedback and improvement
- Reducing overhead over time as confidence builds
- Never fully "trusting" - always monitoring quality
- Pragmatic balance between validation rigour and practical efficiency

---

### Q10: Track B Quality Dependencies ✅

**Decision: Already meet minimum threshold - focus on continuous improvement**

**Quality requirements:**
- **Must-have (for Track B):** Claims, evidence, major RDMAP elements accurate
- **Tolerable errors:** Minor granularity differences, some relationship mapping gaps
- **Deal-breakers:** Missing entire sections, misclassified items, fabricated content

**Current status assessment:**
- **Schema v2.5 is mature** - extractions generally high quality
- **10-paper corpus complete** - demonstrated extraction capability
- **Validation tools in place** - bidirectional mapping, schema validation, completeness checks
- **Assessment:** We meet minimum threshold for credibility assessment

**Going forward:**
- Focus on **improvement**, not validation for permission to proceed
- Track quality issues as they arise
- Refine extraction where Track B assessment reveals weaknesses
- Work towards higher quality, not waiting for perfect quality

**Note:** Track B credibility assessment itself will reveal extraction quality issues - we learn by doing, not by extensive pre-validation.

---

## Area 4: RepliCATS Alignment and Validation ✅ DECIDED

**What we decided:**
- Follow repliCATS closely enough to reproduce their analysis
- Use their corpus as external validation benchmark

**Decisions made:**

### Q11: RepliCATS Methodology Research ✅

**Decision: Sufficient documentation available in background-research/**

**Resources available:**
- **`docs/background-research/replicats-report.md`** - Comprehensive overview of repliCATS IDEA protocol, process, performance
- **`docs/background-research/replicats-seven-signals-hass-adaptation.md`** - Detailed signal definitions, HASS adaptations, assessment guidance

**Methodology elements documented:**
- Seven-signal framework with definitions
- IDEA protocol (Investigate → Discuss → Estimate → Aggregate)
- Multi-expert deliberation approach
- Uncertainty quantification (interval scores: lower/best/upper)
- Performance benchmarks (73-84% accuracy, AUC > 0.75)
- HASS-specific adaptations (analytic reproducibility, CARE principles, interpretive research handling)

**Assessment:** Documentation is sufficient for implementation. Additional detail may be available in published papers if needed during refinement.

**Action:** Proceed with implementation using available documentation; consult published papers if specific methodological questions arise.

---

### Q12: RepliCATS Corpus Identification ✅

**Decision: Build complete tool first, then validate on repliCATS corpus**

**Approach:**
- **Now:** Build and test credibility assessment on our 10-11 paper archaeological corpus
- **Later:** After tool is complete and validated on our corpus, seek access to repliCATS assessed papers for external validation
- **Rationale:** Avoid inadvertent fitting to their specific corpus; build genuinely independent system, then test as true external validation

**Timeline:**
- Complete credibility assessment capability on current corpus (Phases 1-5)
- After 5-10 credibility reports generated and validated
- Then seek repliCATS corpus for comparison

**Benefits of delayed access:**
- Tests whether our system generalises
- Provides genuine external validation (not circular development)
- Avoids over-fitting to their corpus characteristics

---

### Q13: Adaptation Requirements ✅

**Decision: Document divergences explicitly**

**Approach:**
- **Transparency:** Explicitly document where we diverge from repliCATS and why
- **HASS adaptations:**
  - Replicability = analytic reproducibility (not field replication)
  - CARE principles alongside FAIR (Indigenous/community data governance)
  - Approach-specific assessment (inductive/deductive/abductive if repliCATS didn't distinguish)
  - Lower replicability expectations, higher context-dependence for field research
- **Documentation location:** In rubrics, assessment reports, and methodology documentation

**Format:**
```markdown
## Divergence from RepliCATS: [Signal Name]

**RepliCATS approach:** [Original definition/scoring]
**Our adaptation:** [How we've modified it]
**Rationale:** [Why HASS research requires this adaptation]
**Compatibility:** [How to map our scores to repliCATS scores for comparison]
```

**Rationale:**
- Explicit divergences aid interpretation and validation
- Enables mapping between our scores and repliCATS scores
- Documents methodological decisions for transparency
- Allows assessment of whether divergences were necessary/beneficial

---

## Area 5: Report Structure and Output Format (PARTIAL - TO BE REFINED)

**What we decided:**
- 3-5 page summary reports initially
- Expand to 10+ page detailed reports after validation

**Questions for further discussion:**

### Q14: Summary Report Template

**Proposed 6-section structure** (from Decision 4):
1. Paper metadata and research approach classification (0.5 pages)
2. Metric scorecard with visualisation (0.5 pages)
3. Signal-by-signal brief assessment (1-2 pages, ~200 words per signal)
4. Key strengths and weaknesses (0.5 pages)
5. Actionable recommendations (0.5 pages)
6. Overall credibility profile with uncertainty (0.5 pages)

**Status:** To be validated during Phase 3 (pilot assessment)

**Likely refinements needed:**
- Track A quality notes integration (extraction confidence)
- Expressed vs revealed approach comparison (if mismatch)
- Approach-specific emphasis (which signals prioritised)

---

### Q15: Visualisation in Reports

**Status:** TO BE DETERMINED during implementation

**Options under consideration:**
- Radar chart (seven signals) - classic repliCATS visualisation
- Metric scorecard table - structured numeric summary
- Strengths/weaknesses visual summary
- Uncertainty representation (error bars, intervals)

**Decision point:** Phase 3 (pilot report generation) - test what's useful vs distracting

**Principle:** Start text-heavy, add visualisation incrementally if it aids comprehension

---

### Q16: Report Audience Framing

**Status:** TO BE DETERMINED during implementation

**Candidate audiences:**
- Paper authors (formative feedback on improving credibility)
- Peer reviewers (decision support for accept/revise/reject)
- Researchers evaluating literature (trust indicators for citation decisions)
- Us (system validation and refinement)

**Initial approach:** Reports primarily for us (Track A + Track B combined), then adapt for external audiences after validation

**Future consideration:** Audience-specific versions if needed (detailed for authors, summary for reviewers, etc.)

---

## Area 6: Implementation Strategy (QUESTIONS FOR DISCUSSION)

**What we decided:**
- Use Claude's autonomous capabilities maximally
- Iterative development over multiple papers
- File-based planning and execution

**Questions remaining for your input:**

### Q17: First Implementation Target

**Question:** Which capability should we build first?
- **Option A:** Research approach classifier (foundational - informs all assessments)
- **Option B:** Single-signal assessment (prove concept end-to-end on one signal)
- **Option C:** Summary report generator (work backwards from target output)
- **Option D:** Track A extraction quality assessment (validate before assessing)

**My recommendation:** Option A (classifier) - foundational for all subsequent assessment

**Your input needed:** Confirm or suggest alternative sequencing?

---

### Q18: Iteration Corpus Selection

**Question:** Which papers should we test on first (3-5 papers)?

**Candidates from 10-paper corpus:**
- sobotkova-et-al-2024 (well-extracted, inductive survey, 2024)
- ballsun-stanton-et-al-2018 (software/methods paper, mixed approach, 2018)
- penske-et-al-2023 (genomics, deductive, high FAIR, 2023)
- ross-ballsun-stanton-2022 (field data collection, 2022)
- sobotkova-et-al-2016 (book chapter, pre-FAIR, 2016)

**Selection criteria:**
- Diverse research approaches (inductive, deductive, abductive, mixed)
- Well-extracted vs problematic extractions (test robustness)
- Different quality levels (high, medium credibility expected)
- Different domains/types (survey, methods, genomics, field collection, book chapter)

**My recommendation:** Start with sobotkova-et-al-2024 (well-extracted, inductive), ballsun-stanton-et-al-2018 (mixed methods), penske-et-al-2023 (deductive, high quality)

**Your input needed:** Confirm selection or suggest alternatives?

---

### Q19: Prompt Development Strategy

**Question:** How should we architect assessment prompts?

**Options:**
- **Option A:** Single comprehensive prompt (all seven signals assessed in one pass)
  - *Pros:* Holistic assessment, signals inform each other, efficient
  - *Cons:* Complex prompt, harder to refine individual signals
- **Option B:** Seven separate prompts (one per signal, sequential)
  - *Pros:* Modular, easier to refine, focused attention per signal
  - *Cons:* More passes, potential redundancy, signals assessed in isolation
- **Option C:** Iterative multi-turn dialogue (conversational assessment)
  - *Pros:* Natural, adaptive, can drill down where needed
  - *Cons:* Less structured, harder to standardise, longer execution

**My recommendation:** Start with Option B (separate prompts per signal) for development, potentially consolidate to Option A once refined

**Your input needed:** Confirm or suggest alternative approach?

---

### Q20: Skill Integration

**Question:** How should we leverage the research-assessor skill during assessment?

**Current skill capabilities:**
- CEM extraction guidance
- RDMAP framework
- Infrastructure assessment (Pass 6)
- Schema definitions
- Reference materials (evidence-vs-claims-guide, checklists, etc.)

**Integration options:**
- Load skill at assessment start (skill context available throughout)
- Reference specific skill files in assessment prompts
- Extend skill with assessment rubrics and guidance (add to .claude/skills/research-assessor/)
- Use skill as-is (sufficient for extraction, assessment separate)

**My recommendation:** Load skill at start, reference relevant files (schema, guides), consider extending with rubrics if they become complex

**Your input needed:** Preferences for skill integration approach?

---

## Immediate Planning Priorities

Based on reconstructed discussion, here are the **critical path questions** we need to resolve:

### Priority 1: Research Approach Classification (Questions 1-4)
**Why critical:** Determines assessment framework for each paper
**Decisions needed:**
- When to classify (Q1)
- Classification evidence (Q2)
- Mixed-method representation (Q3)
- Validation strategy (Q4)

### Priority 2: Approach-Specific Frameworks (Questions 5-7)
**Why critical:** Core assessment methodology
**Decisions needed:**
- Signal weighting approach (Q5)
- Rubric granularity (Q6)
- Assessment scope (Q7)

### Priority 3: Two-Track Workflow (Questions 8-10)
**Why critical:** Separates system validation from paper assessment
**Decisions needed:**
- Track A methodology (Q8)
- Transition criteria (Q9)
- Quality thresholds (Q10)

### Priority 4: RepliCATS Alignment (Questions 11-13)
**Why critical:** External validation benchmark
**Decisions needed:**
- Methodology research plan (Q11)
- Corpus identification (Q12)
- Adaptation documentation (Q13)

### Priority 5: Implementation (Questions 17-20)
**Why critical:** Execution strategy
**Decisions needed:**
- First implementation target (Q17)
- Test corpus (Q18)
- Prompt architecture (Q19)
- Skill integration (Q20)

---

## Proposed Next Steps

### Immediate Action: Answer Critical Path Questions

**Suggested approach:**
1. You answer Priority 1-2 questions (research approach and frameworks) - domain expertise required
2. We collaborate on Priority 3-4 (workflows and validation) - methodological decisions
3. I propose answers for Priority 5 (implementation) - technical execution

**Then:**
4. Create detailed implementation plan based on decisions
5. Build first prototype capability (approach classifier or single-signal assessor)
6. Test on 1-2 papers
7. Iterate and refine

---

## Questions for You (To Continue Planning)

### Priority 1: Research Approach Classification

**Q1:** When should Claude classify research approach?
- During extraction (Pass 0)?
- After extraction (before assessment)?
- During assessment (first step)?

**Q2:** Should we develop an explicit classification rubric or let Claude infer approach from context using research designs + methods + claims?

**Q3:** For mixed-method papers, prefer "primary + secondary" labelling or something else?

**Q4:** How important is validating approach classifications? (Expert review? Author confirmation?)

### Priority 2: Approach-Specific Frameworks

**Q5:** Signal weighting: Explicit numeric weights or qualitative emphasis?

**Q6:** Rubric granularity: 7 universal rubrics (one per signal) or 21 approach-specific rubrics (7 signals × 3 approaches)?

**Q7:** Should we always assess all seven signals (with some de-emphasised) or only assess relevant signals per approach?

---

---

## Decision Summary (Ready for Implementation)

### Decisions Finalised ✅ (13/20 questions answered)

**Research Approach Classification (Q1-Q4):**
- ✅ Q1: After extraction (Pass 6.5 or early Pass 7)
- ✅ Q2: Contextual inference with expressed vs revealed comparison
- ✅ Q3: Qualitative mixed-method characterisation
- ✅ Q4: Iterative empirical validation

**Assessment Frameworks (Q5-Q7):**
- ✅ Q5: Narrative importance + experimental weights
- ✅ Q6: 7 universal rubrics, fork if needed
- ✅ Q7: Assess all seven signals (repliCATS compatibility)

**Track A/B Workflow (Q8-Q10):**
- ✅ Q8: Metric-based + spot-checking, integrated self-assessment
- ✅ Q9: Parallel tracks with reducing overhead
- ✅ Q10: Already meet threshold, focus on improvement

**RepliCATS Alignment (Q11-Q13):**
- ✅ Q11: Sufficient documentation available
- ✅ Q12: Build tool first, validate later
- ✅ Q13: Document divergences explicitly

### Questions Awaiting Your Input (4/20 remaining)

**Report Structure (Q14-Q16):** To be refined during implementation
- Q14: Validate 6-section report structure
- Q15: Visualisation approach (text vs charts)
- Q16: Audience framing (internal vs external)

**Implementation Strategy (Q17-Q20):** ✅ DECIDED
- ✅ **Q17:** Build research approach classifier first (foundational)
- ✅ **Q18:** Test on sobotkova-2024, ballsun-stanton-2018, penske-2023; expand to all 10 once working
- ✅ **Q19:** One prompt per signal (7 signal prompts) + classifier prompt + quality assessment prompt(s). Heuristic: discrete tasks = separate prompts; interacting tasks = same prompt
- ✅ **Q20:** Leverage research-assessor skill, extend as needed for classification/assessment. Use skill-creator skill to help determine prompt/skill boundaries

---

## Next Actions

### Immediate (After Q17-Q20 Answered)

1. **Update implementation roadmap** with your answers
2. **Begin Phase 1** (research approach classification)
3. **Test classifier** on 3 selected papers
4. **Draft first rubric** (transparency)
5. **Pilot end-to-end** (classify + assess one signal on one paper)

### Documentation Status

**Completed planning documents:**
- ✅ This framework (fundamental decisions)
- ✅ `planning/research-approach-classification-framework.md` (detailed classification spec)
- ✅ `planning/credibility-assessment-implementation-roadmap.md` (5-phase plan)

**Ready for implementation:** Awaiting answers to Q17-Q20

---

**Document Status:** v2.0 - Decisions documented (13/20 complete, 4 awaiting input, 3 deferred)
**Last Updated:** 2025-11-16
**Next Update:** After Q17-Q20 answered and Phase 1 begins

**Related Documents:**
- `planning/research-approach-classification-framework.md` (classification detailed spec)
- `planning/credibility-assessment-implementation-roadmap.md` (5-phase implementation plan)
- `planning/extraction-to-analysis-transition.md` (comprehensive background context)
- `planning/active-todo-list.md` (Task 10.2 implementation tracking)
- `docs/background-research/replicats-report.md` (repliCATS methodology)
- `docs/background-research/replicats-seven-signals-hass-adaptation.md` (signal definitions)
