# Synthesis: External Feedback Analysis
## Critical Response to GPT-5.1 Review

**Document Purpose:** Analyse GPT-5.1 feedback, identify genuine improvements vs areas where our design is sound

**Date:** 2025-11-16
**Reviewers:** Claude (original plan author) + Shawn (project lead)

---

## Overall Assessment of the Review

**Grade for the review itself: A-**

GPT-5.1 provided thoughtful, structured, domain-aware critique that identifies genuine weaknesses while respecting our design context. The review demonstrates understanding of HASS research characteristics and spots real architectural risks.

**Key strengths of the review:**
- Identifies holistic vs fragmented reasoning tension (Major Concern #1)
- Correctly identifies Track A as "operationally toothless" (Major Concern #2)
- Spots validation under-specification (Major Concern #4)
- Provides concrete, actionable recommendations

**Limitations of the review:**
- Some recommendations may over-correct toward experimental psychology norms
- Doesn't fully appreciate iterative empirical development philosophy
- May underestimate maintenance burden of consolidated prompts

---

## Analysis by Category

### MAJOR CONCERNS (5 issues)

---

#### MC#1: Fragmented Prompt Architecture vs Holistic Judgement

**GPT-5.1's critique:**
> 7 separate signal prompts risk cross-signal incoherence, loss of shared context, higher variance

**Our critical analysis:**

**AGREE** that this is a genuine risk. The critique correctly identifies that signals are conceptually interacting.

**However, we PARTIALLY CHALLENGE the severity:**
- RepliCATS itself assesses signals independently in IDEA protocol
- Our "discrete tasks = separate prompts" heuristic comes from empirical extraction workflow success
- Consolidated prompts create different risks: overwhelming context, harder to refine individual signals, all-or-nothing failures

**MIDDLE GROUND - Phased approach:**
1. **Phase 1 (Pilot):** Build 1-2 signals as separate prompts to test modularity
2. **Empirical test:** Does separation create incoherence in practice?
3. **Phase 2 decision:** Based on evidence, either:
   - Keep separate (if coherence maintained)
   - Consolidate into 2-3 clustered prompts (if incoherence appears)
   - Try single integrated prompt (if severe issues)

**Action item:**
- [ ] **ACCEPT** concern as valid risk to monitor
- [ ] **DEFER** consolidation decision to after Phase 1 empirical testing
- [ ] **ADD** cross-signal consistency checking to validation checkpoints

**Specific improvement:**
Add to Checkpoint 4 (All Seven Signals Working):
```markdown
**Cross-signal coherence check:**
- Manual review: Do signal assessments contradict each other?
- Example: High Transparency but low Replicability (check if explained)
- Example: Low Comprehensibility but high Plausibility (suspicious)
- Decision gate: If >3 incoherent pairs across 3 papers → consolidate prompts
```

**VERDICT:** Valid concern, adopt monitoring approach, defer architectural decision to empirical evidence.

---

#### MC#2: Track A Is Operationally Toothless

**GPT-5.1's critique:**
> Track A quality monitoring doesn't mechanically affect Track B outputs; no gating rules defined

**Our critical analysis:**

**STRONGLY AGREE.** This is the single strongest critique in the review. GPT-5.1 is absolutely right that Track A is currently "introspective commentary, not control logic."

**Our original design flaw:**
- We described Track A as "parallel" to Track B
- No specification of what happens when quality is low
- No integration of quality findings into report caveats

**GPT-5.1's recommendation is excellent:**
> Introduce explicit gating: {OK → Full report}, {Caution → Caveated report}, {Fail → No report}

**Action item:**
- [ ] **FULLY ACCEPT** this critique
- [ ] **IMPLEMENT** quality gating in revised plan

**Specific improvement:**

Add new section to implementation plan:

```markdown
### Track A Quality Gating (Pre-Assessment Decision Logic)

**Quality assessment produces one of three states:**

**STATE 1: HIGH QUALITY (Proceed with full assessment)**
- Extraction confidence: High
- Metric-assessment alignment: Yes
- Classification confidence: High or Medium
- **Action:** Run all 7 signals, generate full 3-5 page report

**STATE 2: MODERATE QUALITY (Proceed with caveats)**
- Extraction confidence: Medium
- OR metric-assessment alignment: Partial
- OR classification confidence: Low
- **Action:**
  - Run all 7 signals
  - Generate report with prominent "Assessment Limitations" section at top
  - Constrain scoring to 20-point bands (not precise scores)
  - All signal files include bold caveat header

**STATE 3: LOW QUALITY (Abort credibility assessment)**
- Extraction confidence: Low
- OR major extraction errors identified in Track A
- OR classification completely ambiguous
- **Action:**
  - Generate Track A quality report only
  - Create brief "assessment-not-viable.md" explaining why
  - Flag paper for re-extraction or manual review

**Implementation:**
- Track A prompt must output explicit quality state: `quality_state: "high|moderate|low"`
- Report generation prompt enforces state-dependent behaviour
- File naming reflects state: `credibility-report-v1-CAVEATED.md`
```

**VERDICT:** Excellent catch. Fully adopt recommendation with concrete gating rules.

---

#### MC#3: Approach-Specific Assessment Is Mechanically Vague

**GPT-5.1's critique:**
> Plan says "apply approach-specific emphasis" but doesn't specify HOW mechanically

**Our critical analysis:**

**AGREE** this is under-specified. GPT-5.1 correctly identifies ambiguity.

**GPT-5.1's recommendations are good:**
- Define approach-specific anchor descriptions for scoring bands
- Output both raw score and approach-normalised rating
- Extend classification JSON with explicit textual guidance

**However, we CHALLENGE one aspect:**
> "Without explicit rules, there is danger of hidden normative bias: model may internalise implicit 'deductive default'"

**Our counter-argument:**
- LLMs don't have stable "defaults" in this sense (they follow instructions)
- Risk is actually: *inconsistent application*, not *hidden bias toward deduction*
- Real risk: Approach context doesn't actually influence scoring, just adds narrative fluff

**Better framing:**
The problem is **operationalization**, not bias. We need scoring to demonstrably vary by approach.

**Action item:**
- [ ] **ACCEPT** need for mechanical specification
- [ ] **IMPLEMENT** approach-specific scoring anchors
- [ ] **ADD** validation check: Do approach types show score profile differences?

**Specific improvement:**

Add to signal rubric structure:

```markdown
## Approach-Specific Scoring Anchors (Example: Replicability)

### Deductive Research (Hypothesis-Testing)
**80-100:** Pre-registered analysis plan + public data + documented code + versioned software
**60-79:** Public data + analysis code + software versions documented
**40-59:** Public data OR analysis code (not both), some documentation gaps
**20-39:** Data/code availability stated but not accessible, minimal documentation
**0-19:** No data/code sharing, no replication materials

### Inductive Research (Exploratory)
**80-100:** Data archived + analysis workflow documented + sampling documented + classifications reproducible
**60-79:** Data accessible + workflow description + sufficient documentation for analytical replication
**40-59:** Data partially available OR workflow documented (gaps in one or both)
**20-39:** Minimal data/workflow documentation, analytic replication not feasible
**0-19:** No documentation of analytical process, data unavailable

### Abductive Research (Interpretive)
**80-100:** Theoretical framework explicit + evidence fully documented + alternative interpretations considered + reasoning traceable
**60-79:** Framework stated + evidence accessible + reasoning documented
**40-59:** Implicit framework + partial evidence documentation
**20-39:** Vague framework + minimal evidence accessibility
**0-19:** No theoretical transparency, interpretation not traceable
```

**Add to validation (Checkpoint 4):**
```markdown
**Approach-specific scoring check:**
- Compare mean Replicability scores: Deductive vs Inductive papers
- Expected: Deductive papers score higher (stricter standards)
- If no difference → approach anchors not being applied → revise prompts
```

**VERDICT:** Valid critique. Adopt approach-specific anchors. Challenge "bias" framing, reframe as operationalization.

---

#### MC#4: Validation Strategy Is Under-Powered

**GPT-5.1's critique:**
> Validation relies on manual "does this make sense?" checks; lacks test-retest reliability, inter-rater agreement; defers repliCATS too late

**Our critical analysis:**

**LARGELY AGREE.** This is a strong critique with excellent recommendations.

**GPT-5.1 is right that:**
- We need quantitative reliability baselines
- Test-retest (multiple runs) is easy to implement and valuable
- Early repliCATS pilot would catch structural misalignment before full build

**However, we PARTIALLY CHALLENGE the framing:**
> "You may invest substantial effort... only to discover later that behaviour is structurally misaligned"

**Our counter:**
- We're building for 10-paper HASS corpus FIRST, repliCATS validation is secondary
- RepliCATS corpus is psychology-focused; structural alignment is not guaranteed goal
- Early repliCATS test assumes we have access to papers + expert scores (unclear)

**Better framing:**
- Reliability checks (test-retest, variance) are **essential** → adopt fully
- Early repliCATS pilot is **desirable if feasible** → investigate access
- RepliCATS is **external validation target**, not **calibration corpus**

**Action items:**
- [ ] **FULLY ACCEPT** need for quantitative reliability checks
- [ ] **IMPLEMENT** test-retest validation in Phase 1
- [ ] **INVESTIGATE** repliCATS corpus access for early pilot (ask Shawn)
- [ ] **CLARIFY** repliCATS role: validation, not calibration

**Specific improvements:**

**Add to Checkpoint 1 (Classifier Working):**
```markdown
**Test-retest reliability check:**
- Run classification 3x on sobotkova-et-al-2024 (identical inputs, different invocations)
- Measure:
  - Expressed approach consistency (should be identical)
  - Revealed approach consistency (acceptable: all 3 agree OR 2/3 agree if third is "mixed")
  - HARKing flag consistency (should be identical if high confidence)
- **Threshold:** <2 classification changes across 3 runs = acceptable
- **If fails:** Classification prompt insufficiently constrained → revise
```

**Add to Checkpoint 2 (Transparency Rubric Working):**
```markdown
**Score variance check:**
- Run transparency assessment 3x on sobotkova-et-al-2024
- Measure: Mean score ± SD
- **Threshold:** SD < 10 points = acceptable reliability
- **If SD > 10:** Rubric insufficiently anchored OR evidence ambiguous → investigate

**Metric-signal correlation check:**
- Compare TCI (Transparency & Completeness Index) to Transparency signal score
- Expected correlation: r > 0.6 (positive relationship)
- **If r < 0.4:** Metric and signal measuring different things → investigate divergence
```

**Add Phase 1.5 (Conditional on Access):**
```markdown
### Phase 1.5: Early RepliCATS Pilot (OPTIONAL - if corpus accessible)

**Goal:** Validate that our approach produces structurally similar assessments to repliCATS expert panels

**Actions:**
1. Identify 1-2 papers in repliCATS corpus that we can access (check with Shawn)
2. Run classifier + transparency assessment on repliCATS papers
3. Compare our scores to repliCATS expert judgments (if available)
4. **NOT calibrating** - just checking for structural sanity
5. **Threshold:** Our ranking should not invert repliCATS ranking (if we assess 2 papers)

**Effort:** 1-2 hours (if corpus accessible)

**Decision gate:** If major misalignment → discuss with Shawn before proceeding to all 7 signals
```

**VERDICT:** Strong critique. Fully adopt reliability checks. Conditionally adopt early repliCATS pilot pending access investigation.

---

#### MC#5: Skill Boundary Creep and Single-Skill Overload

**GPT-5.1's critique:**
> Extending research-assessor skill violates separation of concerns; extraction vs assessment are different tasks

**Our critical analysis:**

**PARTIALLY AGREE.** GPT-5.1 makes valid points about separation of concerns and future reuse.

**Strong arguments FOR separation (GPT-5.1 is right):**
- Extraction and assessment are conceptually distinct
- Independent versioning more flexible
- Clearer boundaries for maintenance

**Strong arguments AGAINST separation (our original reasoning):**
- Credibility assessment **depends directly** on extraction schema understanding
- Many references overlap (HASS adaptations, RDMAP interpretation, infrastructure)
- Skills can be compartmentalized internally (references/credibility/ vs references/extraction/)
- User burden: loading 2 skills vs 1

**This is a DESIGN TRADE-OFF, not a clear right/wrong.**

**Action item:**
- [ ] **ACKNOWLEDGE** valid concern
- [ ] **ASK SHAWN** for preference (this affects workflow ergonomics)
- [ ] **PREPARE** arguments for both options

**Question for Shawn:**

> **Skill architecture decision: Extend research-assessor vs create separate credibility-assessor skill**
>
> **Option A: Extend research-assessor (original plan)**
> - Pros: Single skill load, shared references, integrated workflow
> - Cons: Skill complexity increases, mixing extraction + assessment concerns
>
> **Option B: Separate credibility-assessor skill (GPT-5.1 recommendation)**
> - Pros: Clear separation of concerns, independent versioning, better reuse
> - Cons: Need to load 2 skills, some reference duplication, coordination overhead
>
> **Option C: Hybrid (new idea)**
> - Keep research-assessor focused on extraction
> - Create lightweight credibility-assessor that REFERENCES research-assessor schemas
> - Share infrastructure via cross-skill references (if Claude Code supports this)
>
> **Your preference?**

**VERDICT:** Legitimate design choice. Need Shawn's input on workflow preference.

---

### MEDIUM CONCERNS (5 issues)

---

#### MedC#1: Ambiguous Handling of Low-Confidence Classification

**GPT-5.1's critique:**
> Plan doesn't specify what happens when classification confidence is low or approach is ambiguous

**Our analysis:**

**FULLY AGREE.** This meshes with MC#2 (Track A gating). Low classification confidence should trigger Moderate Quality state.

**Action item:**
- [ ] **ACCEPT** and integrate with Track A gating

**Specific improvement:**

Add to Track A gating rules (STATE 2):
```markdown
**Moderate quality triggers include:**
- Classification confidence: Low
- Expressed vs revealed: Mismatched with unclear type
- Research approach: "Mixed" with high ambiguity

**Result:** Assess all signals but with approach-generic rubrics (no approach-specific anchors)
Report includes: "Classification ambiguous; assessment uses generic HASS criteria"
```

**VERDICT:** Valid. Integrate with Track A gating.

---

#### MedC#2: File Format Choices and Downstream Automation

**GPT-5.1's critique:**
> Mixing JSON, YAML, Markdown creates parsing fragility; embedding YAML in .json is confusing

**Our analysis:**

**PARTIALLY AGREE.** GPT-5.1 is right about "YAML in .json" being confusing.

**However, we CHALLENGE the assumption that consistency is paramount:**
- Markdown for narrative reports (human-readable) is correct choice
- JSON for structured data (machine-readable) is correct choice
- Mixed formats serve different purposes

**The real issue:** Our plan showed YAML format in a .json file - that's just documentation confusion.

**Action item:**
- [ ] **ACCEPT** need for format clarity
- [ ] **CLARIFY** in plan: .json files contain JSON, .md files contain Markdown

**Specific improvement:**

**Standardize file formats:**
```markdown
**Structured data (machine-readable):**
- classification.json - JSON format (not YAML)
- metrics/metrics.json - JSON format
- Future: assessment-summary.json - JSON format (all signals + Track A in one object)

**Narrative reports (human-readable):**
- track-a-quality.md - Markdown
- signals/*.md - Markdown
- credibility-report.md - Markdown

**Rationale:** JSON for parsing/analysis, Markdown for reading/sharing
```

**Consider GPT-5.1's "Opportunity #1" (canonical assessment.json):**
- Good idea for corpus analysis
- Generate from individual files after assessment complete
- Enables cross-paper statistics

**VERDICT:** Accept need for format clarity. Adopt canonical assessment.json as post-processing step.

---

#### MedC#3: Normative Stance on "No Expressed Method"

**GPT-5.1's critique:**
> Treating "no expressed method" as naivete may penalize genre conventions, historical scholarship, non-Anglophone norms

**Our analysis:**

**PARTIALLY AGREE - Important caveat.** GPT-5.1 raises legitimate concern about cultural/temporal/genre bias.

**However, we note:**
- Our corpus is contemporary (2013-2024), mostly Anglophone, post-"methodology section" norm
- For OUR corpus, "no expressed method" likely IS a transparency weakness
- But GPT-5.1 is right that this shouldn't be universal rule

**Action item:**
- [ ] **ACCEPT** need for context-sensitivity
- [ ] **IMPLEMENT** defeasible interpretation (as GPT-5.1 suggests)

**Specific improvement:**

Update classification handling:
```markdown
**When `expressed_approach: "none_stated"`:**

**Default interpretation:**
"No explicit methodological framework stated. This may indicate:
1. Methodological naivete or weak research design (common for contemporary papers)
2. Disciplinary genre conventions (some subfields, historical periods)
3. Methodological commitments expressed through narrative rather than explicit section"

**Track A check:**
Monitor whether "none_stated" correlates with:
- Publication year (older papers more likely?)
- Journal/discipline (some fields don't use methodology sections?)
- Language/region (non-Anglophone traditions?)

**If pattern emerges:** Adjust interpretation for specific contexts
**Otherwise:** Treat as transparency weakness per contemporary norms
```

**VERDICT:** Valid concern. Adopt defeasible interpretation with empirical monitoring.

---

#### MedC#4: Report Length and Rhetorical Authority

**GPT-5.1's critique:**
> 3-5 page reports from experimental system risk over-interpretation; start with 1-2 pages

**Our analysis:**

**DISAGREE - This recommendation doesn't fit our context.**

**Reasons:**
1. **We explicitly decided** on 3-5 pages in planning (not arbitrary)
2. **Audience is us** (Shawn + Claude), not external stakeholders
3. **Purpose is development**, not publication
4. **Shorter reports sacrifice detail** needed for empirical refinement

**GPT-5.1's concern is valid for:**
- Public-facing assessments
- High-stakes decisions
- Untested systems presented to naive users

**But our use case is:**
- Internal development and iteration
- Expert users (Shawn knows system is experimental)
- Reports inform rubric refinement

**However, GPT-5.1's "experimental system" warning is good:**

**Action item:**
- [ ] **REJECT** 1-2 page reduction
- [ ] **ACCEPT** prominent experimental disclaimer

**Specific improvement:**

Add to every credibility report:
```markdown
# Credibility Assessment Report
## {Paper Title}

> **EXPERIMENTAL SYSTEM - DEVELOPMENT PHASE**
>
> This assessment was generated by an experimental LLM-based credibility evaluation system
> currently under development. Scores and interpretations should be treated as provisional
> and subject to revision as the system is refined. Do not use for high-stakes decisions.
>
> System version: v0.1-alpha | Assessment date: {date} | Assessor: Claude (research-assessor skill)
```

**VERDICT:** Reject page reduction. Accept experimental disclaimer.

---

#### MedC#5: Metrics–Signals Integration Is Lightly Specified

**GPT-5.1's critique:**
> Mapping from 8 metrics to signal judgments is implicit; model may ignore or overfit

**Our analysis:**

**PARTIALLY AGREE.** This is under-specified, but GPT-5.1's recommendation is too prescriptive.

**GPT-5.1 suggests:**
> "Define rules like: If ESD < X, then Validity cannot exceed Y"

**We CHALLENGE this:**
- This creates rigid heuristics that may not generalize
- Defeats purpose of LLM flexible interpretation
- Metrics are **inputs**, not **determinants** of signals

**Better approach:**
- Metrics provide **evidence** for signal assessment
- Signals should **reference** metrics in justification
- Track A monitors **metric-signal divergence**

**Action item:**
- [ ] **ACCEPT** need for clearer integration
- [ ] **REJECT** hard rules (ESD < X → Validity < Y)
- [ ] **IMPLEMENT** soft guidance + divergence monitoring

**Specific improvement:**

Add to each signal prompt:
```markdown
## Relevant Metrics (Inputs)

**Primary metrics for Validity assessment:**
- **ESD (Evidence Sufficiency Density):** Higher ESD suggests more evidence per claim
  - Use as starting point: ESD > 2.0 is positive signal
  - But: Low ESD may be justified for synthetic/review claims
- **RTI (Research Traceability Index):** Higher RTI suggests better evidence-claim linkage
  - Use as corroboration: High RTI + High ESD = strong validity foundation

**Assessment process:**
1. Review metric scores
2. Review extracted evidence and claims
3. Assess validity qualitatively
4. **If metric and qualitative assessment diverge significantly, explain why in justification**

**Example divergence to explain:**
"ESD is low (1.2) but Validity scored high (75) because claims are primarily synthetic
integrations of established findings, not novel empirical assertions requiring dense evidence."
```

Add to Track A monitoring:
```markdown
**Metric-signal divergence log:**
- For each paper, note cases where metric suggests one score band but signal assessment differs by >20 points
- Investigate patterns: Are divergences explained? Systematic? Random?
- Use to refine either metrics or signal rubrics
```

**VERDICT:** Accept need for integration guidance. Reject rigid rules. Adopt soft guidance + monitoring.

---

### OPPORTUNITIES (3 suggestions)

---

#### Opp#1: Single Canonical Assessment Object

**GPT-5.1's suggestion:**
> Create assessment.json containing classification + signals + Track A + metrics for easier analysis

**Our analysis:**

**EXCELLENT IDEA.** This is genuinely valuable for corpus-level analysis.

**Action item:**
- [ ] **FULLY ADOPT** as post-processing step

**Specific improvement:**

Add to Phase 3 (after report generation):
```markdown
### Step: Generate Canonical Assessment Object

**After all individual files created, consolidate into assessment.json:**

```json
{
  "paper_id": "sobotkova-et-al-2024",
  "assessment_date": "2025-11-16",
  "system_version": "v0.1-alpha",

  "classification": { ... },

  "track_a": {
    "quality_state": "high|moderate|low",
    "extraction_confidence": "...",
    "metric_signal_alignment": "...",
    ...
  },

  "signals": [
    {
      "signal_name": "comprehensibility",
      "signal_number": 1,
      "score": 75,
      "confidence": "high",
      "summary": "...",
      "strengths": [...],
      "weaknesses": [...],
      "justification": "..."
    },
    ... (7 signals)
  ],

  "metrics": { ... },

  "report_path": "assessment/credibility-report-v1.md"
}
```

**Benefits:**
- Corpus-level statistics easy to compute
- Cross-paper comparisons straightforward
- Downstream tooling (dashboards, visualizations) simplified
```

**VERDICT:** Excellent suggestion. Fully adopt.

---

#### Opp#2: Cross-Model Ensembles for Reliability

**GPT-5.1's suggestion:**
> Run same assessment with different seeds or different models (Claude vs GPT) to measure disagreement

**Our analysis:**

**INTERESTING BUT PREMATURE.** This adds significant complexity for uncertain benefit at current stage.

**Concerns:**
- Running assessments 3x already tests single-model reliability (test-retest)
- Cross-model comparison requires maintaining parallel prompt versions for different APIs
- Disagreement between models is hard to interpret (which is right?)
- Substantial additional cost and time

**Better timing:**
- Phase 1-3: Single-model test-retest reliability
- Phase 4-5: If reliability is poor, THEN consider cross-model ensemble
- Later: For high-stakes or contested papers, run with multiple models

**Action item:**
- [ ] **DEFER** to post-Phase 3
- [ ] **NOTE** as future enhancement option

**VERDICT:** Interesting idea. Defer as future enhancement, not Phase 1 priority.

---

#### Opp#3: Early "Gold Standard" Micro-Corpus

**GPT-5.1's suggestion:**
> Create 3-5 papers with human-authored signal assessments as regression tests

**Our analysis:**

**GOOD IDEA, but resource-intensive.** This would be valuable but requires substantial expert time.

**Trade-off:**
- **Benefit:** Human baseline for comparing LLM assessments
- **Cost:** Shawn (or collaborator) must manually assess 3-5 papers using rubrics (~10-15 hours)
- **Timing:** Better AFTER Phase 1-2 (once rubrics stable enough to use for human assessment)

**Action item:**
- [ ] **ACCEPT** as valuable Phase 4 enhancement
- [ ] **ASK SHAWN** if feasible and desirable

**Question for Shawn:**

> **Gold standard micro-corpus: Desirable?**
>
> GPT-5.1 suggests creating 3-5 papers with your own manual signal assessments to use as
> regression tests. This would help validate LLM assessments against human judgment.
>
> **Effort required:** ~2-3 hours per paper × 3-5 papers = 6-15 hours of your time
> **Timing:** After Phase 2 (once rubrics refined enough for you to use)
> **Value:** Concrete benchmark for LLM assessment quality
>
> **Is this worth the time investment, or should we rely on test-retest + repliCATS validation?**

**VERDICT:** Good idea. Ask Shawn about feasibility. If yes, schedule for Phase 4.

---

## Summary: Recommendations Categorized

### FULLY ADOPT (Implement in revised plan)

1. ✅ **Track A quality gating** (MC#2) - Add explicit state machine with behavioral rules
2. ✅ **Approach-specific scoring anchors** (MC#3) - Define concrete scoring bands per approach
3. ✅ **Test-retest reliability checks** (MC#4) - Run assessments 3x, measure variance
4. ✅ **Metric-signal divergence monitoring** (MC#4) - Log and investigate misalignments
5. ✅ **Low-confidence classification handling** (MedC#1) - Integrate with Track A gating
6. ✅ **File format standardization** (MedC#2) - JSON for data, Markdown for narrative
7. ✅ **Canonical assessment.json** (Opp#1) - Post-processing consolidation for corpus analysis
8. ✅ **Experimental system disclaimer** (MedC#4) - Add to all reports
9. ✅ **Defeasible "no method" interpretation** (MedC#3) - Context-sensitive, not universal penalty
10. ✅ **Metrics-signals soft guidance** (MedC#5) - Reference metrics, explain divergences

### CONDITIONALLY ADOPT (Pending investigation/decision)

11. 🔍 **Early repliCATS pilot** (MC#4) - **IF corpus accessible** → add Phase 1.5
12. 🔍 **Skill separation decision** (MC#5) - **ASK SHAWN** for preference (extend vs separate)
13. 🔍 **Gold standard micro-corpus** (Opp#3) - **ASK SHAWN** if feasible for Phase 4

### DEFER TO EMPIRICAL EVIDENCE (Test in Phase 1, decide in Phase 2)

14. ⏸️ **Prompt consolidation** (MC#1) - Monitor for incoherence, consolidate if needed
15. ⏸️ **Cross-model ensembles** (Opp#2) - Defer to post-Phase 3 if reliability poor

### RESPECTFULLY DECLINE

16. ❌ **Reduce report to 1-2 pages** (MedC#4) - Our use case requires 3-5 pages for development
17. ❌ **Hard metric-signal rules** (MedC#5) - Too rigid, defeats LLM flexibility

---

## Questions for Shawn

### Q1: Skill Architecture (High Priority)

**Should we extend research-assessor skill or create separate credibility-assessor skill?**

- **Option A:** Extend research-assessor (original plan)
- **Option B:** Separate credibility-assessor skill (GPT-5.1 recommendation)
- **Option C:** Hybrid with cross-skill references

**Your preference based on workflow ergonomics?**

### Q2: RepliCATS Corpus Access (Medium Priority)

**Do we have access to repliCATS corpus papers with expert assessment scores?**

- If YES → Add Phase 1.5 early validation pilot
- If NO → Defer repliCATS validation to Phase 5+

### Q3: Gold Standard Micro-Corpus (Lower Priority)

**Would you be willing to manually assess 3-5 papers (6-15 hours) to create human baseline?**

- Timing: After Phase 2 (once rubrics stable)
- Value: Concrete benchmark for LLM quality
- Alternative: Rely on test-retest + eventual repliCATS validation

---

## Next Steps

1. **Shawn answers questions** → Design decisions finalized
2. **Claude revises implementation plan** → Incorporate fully adopted + conditionally adopted recommendations
3. **Create revised plan v2.0** → Ready for Phase 1 execution

---

**Analysis Status:** Complete
**Synthesis Grade:** A (GPT-5.1 provided genuinely valuable feedback; most recommendations sound)
**Action Required:** Shawn input on 3 questions, then revise plan

