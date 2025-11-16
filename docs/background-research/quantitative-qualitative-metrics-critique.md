# Critical Discussion: Quantitative vs Qualitative Credibility Metrics

**Document Type:** Methodological Reflection
**Date:** 2025-11-14
**Version:** 1.0
**Status:** Living document - will be updated as empirical validation proceeds

---

## Overview

This document captures a critical discussion of the hybrid quantitative-qualitative approach to research credibility assessment developed for this project. It presents both the rationale for the chosen metrics and a rigorous devil's advocate critique, establishing the epistemological foundations and limitations of the assessment framework.

**Key Question:** What is the value of quantitative metrics (counts, ratios, indices) versus qualitative LLM-based assessment, given LLMs' powerful natural language understanding capabilities?

---

## Table of Contents

1. [The Eight Quantitative Metrics](#the-eight-quantitative-metrics)
2. [Sources and Inspirations](#sources-and-inspirations)
3. [Devil's Advocate Critique](#devils-advocate-critique)
4. [Defense: What Quantitative Metrics Do Well](#defense-what-quantitative-metrics-do-well)
5. [What Qualitative LLM Assessment Does Well](#what-qualitative-llm-assessment-does-well)
6. [Complementary Architecture](#complementary-architecture)
7. [Design Decisions and Future Directions](#design-decisions-and-future-directions)
8. [References](#references)

---

## The Eight Quantitative Metrics

### Implemented (Phase 1, Session 1)

**1. ESD (Evidential Support Density)**
- **Calculation:** Claims ÷ Evidence ratio by section
- **Purpose:** Detect under-supported claims
- **Interpretation:** Lower is better (more evidence per claim)
- **Example:** sobotkova-et-al-2023 scored 1.28 (1.28 claims per evidence item)

**2. TCI (Transparency Completeness Index)**
- **Calculation:** RDMAP coverage against expected minimums (2 RD, 5 methods, 8 protocols), weighted average
- **Purpose:** Assess methods documentation completeness
- **Interpretation:** Higher is better (0-1 scale)
- **Weights:** Research Designs (0.2), Methods (0.3), Protocols (0.5)
- **Example:** sobotkova-et-al-2023 scored 1.0 (exceeded all baselines)

**3. SCS (Scope Constraint Score)**
- **Calculation:** Count claims containing scope/limitation keywords
- **Purpose:** Detect whether authors acknowledge limitations
- **Interpretation:** Higher is better (absolute count)
- **Keywords:** limitation, constraint, scope, boundary, caveat, restricted to, limited to, only, not claim, cannot, does not extend, preliminary, exploratory, pilot
- **Example:** sobotkova-et-al-2023 scored 8 scope constraints

**4. RTI (Robustness Triangulation Index)**
- **Calculation:** Shannon diversity index (H) of evidence types
- **Purpose:** Assess evidence type diversity (single vs multiple sources)
- **Interpretation:** Higher is better (typical range 0-3)
- **Formula:** H = -Σ(p_i × ln(p_i)), where p_i = proportion of evidence type i
- **Effective types:** e^H (interpretable as "number of equally-common types")
- **Example:** sobotkova-et-al-2023 scored RTI=3.26 (effectively 3.26 distinct evidence types)

### Planned (Phase 1, Session 2)

**5. RIS (Replicability Infrastructure Score)**
- **Calculation:** Count PIDs for data/code/materials + assess sharing statements
- **Purpose:** Assess data/code/materials availability
- **Data source:** `reproducibility_infrastructure.persistent_identifiers`

**6. PGCS (PID Graph Connectivity Score)**
- **Calculation:** Assess how many PIDs are linked (e.g., DOI→dataset DOI→software)
- **Purpose:** Evaluate FAIR infrastructure integration
- **Data source:** Cross-reference PID relationships

**7. FCS (FAIR Compliance Score)**
- **Calculation:** Aggregate Pass 6 FAIR assessment (0-15 scale)
- **Purpose:** Direct measure of Findable, Accessible, Interoperable, Reusable compliance
- **Data source:** `reproducibility_infrastructure.fair_assessment`

**8. MDD (Methods Documentation Density)**
- **Calculation:** Average verbatim quote length for RDMAP items
- **Purpose:** Assess level of methodological detail
- **Interpretation:** Longer quotes = more detail
- **Data source:** `research_designs`, `methods`, `protocols` text fields

---

## Sources and Inspirations

### Not Directly from repliCATS

**Important caveat:** None of these specific quantitative metrics come directly from the repliCATS framework. The repliCATS methodology uses **qualitative rubrics** for their seven credibility signals (Comprehensibility, Transparency, Plausibility, Validity, Robustness, Replicability, Generalisability), scored through expert elicitation panels, not automated calculation.

### Design Rationale

These metrics were **created de novo** (November 2025) to serve as an **automated foundation layer** before applying repliCATS-style qualitative assessment. Design influences:

**1. Research Transparency Literature (General Principles)**
- **ESD:** Inspired by evidential reasoning frameworks - claims require empirical support
- **TCI:** Inspired by reporting guidelines (CONSORT, TIDieR, SPIRIT) specifying minimum reporting elements
- **SCS:** Inspired by metascience work on overconfidence and scope constraints
- **RTI:** Shannon diversity index (from ecology/information theory) applied to evidence triangulation

**2. CEM/RDMAP Extraction Schema (Opportunistic)**
- Metrics exploit structured graph data already being extracted
- Designed to be calculable automatically from `extraction.json`
- No additional extraction burden

**3. Project's Hybrid Architecture (Architectural)**
- Quantitative metrics = objective, fast, scalable
- Qualitative rubrics (Phase 2) = nuanced, contextual, LLM-assisted
- Together they approximate repliCATS signals for HASS fieldwork

### Conceptual Mapping to repliCATS Signals

| **Metric** | **repliCATS Signal(s)** | **Relationship** |
|------------|------------------------|------------------|
| **ESD** | Validity, Robustness | Proxy for empirical adequacy |
| **TCI** | Comprehensibility, Transparency | Proxy for methods reporting |
| **SCS** | Transparency, Generalisability | Proxy for scope acknowledgment |
| **RTI** | Robustness | Proxy for triangulation/convergent evidence |
| **RIS** | Replicability | Proxy for data/code availability |
| **PGCS** | Replicability | Proxy for FAIR infrastructure |
| **FCS** | Replicability | Direct use of Pass 6 FAIR scores |
| **MDD** | Transparency, Comprehensibility | Proxy for methods detail |

**Key Point:** These are **proxies and approximations**, not direct implementations of repliCATS signals. Validation required.

---

## Devil's Advocate Critique

### 1. Fundamental Validity Issues

#### **Confusing Extraction Quality with Research Quality**

**Most damning critique:** These metrics measure how well we extracted, not how good the research is.

**Evidence:**

- **ESD (Claims:Evidence ratio):**
  - Poorly written paper with few explicit claims but verbose description scores "well" (low ratio)
  - Theoretically sophisticated paper with nuanced interpretations scores "poorly" (high ratio)
  - **We reward verbose description over analytical insight**

- **TCI (RDMAP completeness):**
  - Papers that spell everything out score well
  - Papers where methods are standard and referenced (e.g., "standard archaeological survey, see Banning 2002") score poorly
  - **We reward explicitness over domain-appropriate brevity**

- **RTI (Evidence diversity):**
  - Focused study using one method rigorously (e.g., pure dendrochronology) scores poorly
  - Scattershot study mentioning multiple methods superficially scores well
  - **We reward breadth over depth**

**Underlying problem:** Measuring **textual explicitness**, not **actual transparency or quality**.

---

#### **Campbell's Law: Gaming the Metrics**

"When a measure becomes a target, it ceases to be a good measure."

If these metrics became known, authors could optimize artificially:

- **ESD:** Add trivial descriptive "evidence" (e.g., "The pottery was red. The pottery was ceramic. The pottery had a rim.") to lower ratio without adding information

- **SCS:** Add boilerplate limitations ("This study is limited to the archaeological record" - true but meaningless) to boost score

- **TCI:** Inflate protocol count by atomising procedures ("Step 1: Pick up trowel. Step 2: Insert trowel into soil...")

**Result:** Extraction-valid but scientifically worthless content.

---

#### **Domain/Genre Bias**

Different paper types are structurally incomparable:

| **Paper Type** | **Structural Features** | **Metric Bias** |
|---------------|------------------------|-----------------|
| **Theoretical papers** | Few evidence items (thought experiments), many claims | ESD always "poor" |
| **Data papers** | Mostly descriptive evidence, few interpretive claims | ESD always "good" |
| **Review papers** | Evidence is citations, not observations | Schema doesn't capture this |
| **Book chapters** | Narrative structure, fewer explicit methods | TCI penalises genre |
| **Methodological papers** | Many protocols, fewer empirical claims | TCI inflated |

**Problem:** Comparing apples to oranges to theoretical frameworks.

---

#### **Missing the Human Element**

None of these metrics capture what repliCATS actually measures:

- **Plausibility:** Is the interpretation reasonable given the evidence? (Requires domain expertise)
- **Generalisability:** Can findings transfer to other contexts? (Requires understanding scope and theory)
- **Robustness:** Would results hold under different analytical choices? (Requires counterfactual reasoning)

**We measure surface features (counts, ratios) and hope they correlate with deep qualities (soundness, credibility).**

**That correlation is assumed, not validated.**

---

### 2. The "More Is Better" Fallacy

Several metrics assume quantity = quality:

- **TCI:** More protocols = better? Or just more verbose/pedantic?
- **RTI:** More evidence types = better? Or unfocused kitchen-sink approach?
- **SCS:** More limitations = better? Or catastrophically flawed study trying to hedge?

**Example - SCS nuance problem:**

Consider two papers:

**Paper A:**
- "This study is limited to the archaeological record"
- "We cannot eliminate all possible confounds"
- "Future research is needed"
- "Sample size constrains generalisability"
- **SCS = 4**

**Paper B:**
- "Post-depositional taphonomic processes may have selectively preserved certain ceramic forms while destroying others, fundamentally limiting our ability to reconstruct vessel assemblages and by extension household consumption patterns"
- **SCS = 1**

**Paper B has one serious, substantive limitation. Paper A has four trivial hedges.**

**The metric rewards Paper A.**

**Related problem:** Papers that recognise limitations only to claim they've solved them:

> "A potential limitation is sampling bias, however our stratified random sampling protocol mitigates this concern."

- Quantitative SCS: Contains "limitation" → +1 point (paper gets credit)
- Reality: Performative limitation acknowledgment, immediately dismissed without evidence

**We're counting when we should be weighing.**

---

### 3. Extraction Granularity Dependency

**Critical issue:** Inter-rater reliability problem.

Metrics are highly sensitive to extraction decisions:

**Example 1 - Methods granularity:**
- Extraction A: "We conducted survey" = ONE method
- Extraction B: "We conducted pedestrian survey using 10m transects with 5m spacing" = THREE protocols
- **TCI changes radically**

**Example 2 - Evidence splitting:**
- Extraction A: "GIS analysis showed clustering (p<0.05)" = ONE evidence item
- Extraction B: "GIS analysis showed clustering" + "Statistical significance p<0.05" = TWO evidence items
- **ESD changes**

**The metrics measure our extraction decisions as much as the paper's content.**

**Without strict extraction guidelines and inter-rater reliability testing, these metrics are noise.**

---

### 4. Statistical Issues

**Sample Size:**
11 papers is far too small to:
- Establish meaningful percentile ranks
- Detect true score distributions
- Validate metric stability
- Control for domain/method/genre confounds

**No Ground Truth:**
We don't have expert-rated papers to validate against. Building metrics without criterion validity.

**No Reliability Testing:**
Haven't run:
- Test-retest (same paper, different extractions)
- Inter-rater (multiple extractors, same paper)
- Multi-model (Claude vs GPT vs Gemini)

**Implication:** Cannot distinguish signal from noise.

---

### 5. Philosophical Issues: Epistemological Mismatch

**HASS fieldwork epistemology:**
- **Abductive:** Emergent discovery, not hypothesis testing
- **Opportunistic:** Adapting to what's found in the field
- **Interpretive:** Hermeneutic, not falsificationist

**Our metrics assume a positivist structure:**
- Evidence → Claims (but what about the hermeneutic circle?)
- Pre-specified methods (but what about emergent adaptation?)
- Scope constraints (but what about productive ambiguity in theory-building?)

**Question:** Are we imposing a scientific structure on humanities scholarship inappropriately?

---

### 6. The Transparency Paradox

**Highly transparent papers might score worse.**

**Example:**

**Paper A (Transparent):**
> "We initially attempted transect survey (2016 season) but encountered dense vegetation. We then tried geophysical survey (2017) but soil conditions were unsuitable. Finally we adopted aerial photogrammetry (2018) which successfully identified features."

- **TCI:** Failed methods = incomplete protocols (only final method fully documented)
- **SCS:** Multiple acknowledged failures = high limitation count
- **Perception:** Honest about trial-and-error

**Paper B (Selective):**
> "We conducted aerial photogrammetry survey in 2018, acquiring 500 images at 100m altitude with 80% overlap using DJI Phantom 4 Pro..."

- **TCI:** Complete protocol for successful method
- **SCS:** No mention of failures = low limitation count
- **Perception:** Clean, complete methods

**We might be rewarding selective reporting over transparency.**

---

### 7. Actionability Problem

**What does a "bad" score mean?**

If a paper gets:
- Low TCI (incomplete methods)
- High ESD (many unsupported claims)
- Low RTI (single evidence type)

Is it:
- **A.** A bad paper?
- **B.** A preliminary paper (appropriately scoped)?
- **C.** A theoretical paper (different genre)?
- **D.** A badly extracted paper?

**The metrics don't tell us - and we can't act on them without knowing.**

---

### 8. Most Serious Critique: Psychometric Validation Absent

**We're building a psychometric instrument (credibility assessment) without psychometric validation:**

- **No construct validity:** Do metrics measure what we claim?
- **No criterion validity:** Do they correlate with expert judgment?
- **No reliability:** Consistent across extractors/models/time?
- **No sensitivity analysis:** How robust to extraction choices?
- **No benchmarking:** What's good/bad on absolute scale?

**We're essentially saying "trust us, these numbers mean something."**

**But we haven't proven they do.**

---

## Defense: What Quantitative Metrics Do Well

Despite the critiques above, quantitative metrics provide essential capabilities that qualitative LLM assessment cannot match.

### 1. Objectivity and Auditability

**Quantitative metrics are transparent and reproducible:**

- `ESD = 1.28` means exactly: 120 claims ÷ 94 evidence items
- Anyone can verify by counting extraction.json objects
- No prompt sensitivity, no temperature variance, no model drift
- Auditable: "Why this score?" → "Here's the formula and counts"

**LLM qualitative assessment is opaque:**

- "This paper has moderate transparency" - why? How reproducible across runs?
- Temperature=0 helps but doesn't eliminate variance
- Prompt engineering affects outputs significantly
- Hard to audit: "Why this rating?" → "Because the model said so"

**Value:** Quantitative metrics provide a **defensible foundation** that doesn't rely on trusting an LLM's black-box judgment.

**Use case:** When assessment is challenged (funding decisions, editorial decisions), can point to objective counts.

---

### 2. Consistency Across Corpus

**Quantitative metrics apply the same standard to all papers:**

- Paper A: ESD=0.8, Paper B: ESD=2.1 - directly comparable
- Percentile ranking: "This paper is 75th percentile for evidence density"
- Distribution analysis: "Most papers cluster 0.5-1.5, outliers flag for investigation"

**LLM assessments drift:**

- Early papers in batch judged differently than later ones (context effects)
- Different prompts for different domains introduce incomparability
- "Moderate transparency" for Paper A vs Paper B - same threshold?

**Value:** Enables **systematic corpus-level analysis** (trends, comparisons, outlier detection) that qualitative ratings struggle with.

**Use case:** "How has methodological transparency changed in archaeology 2005-2025?" requires consistent measurement.

---

### 3. Computational Efficiency

**Quantitative metrics are fast and cheap:**

- Calculate all 8 metrics for all 11 papers: seconds, pennies
- Rerun entire corpus after schema changes: trivial
- Scale to 1000 papers: still fast

**LLM assessment is slow and expensive:**

- 7 rubric assessments × 11 papers = 77 LLM calls
- Each call: 5-10K tokens context (full extraction.json), 500-1K tokens output
- Time: minutes per paper
- Cost: dollars for full corpus
- Scale to 1000 papers: hours, hundreds of dollars

**Value:** Enables **rapid iteration and large-scale screening** before investing in expensive qualitative analysis.

**Use case:** "Which 20 of these 200 papers warrant deep assessment?" - quantitative metrics triage quickly.

---

### 4. Failure Mode Transparency

**When quantitative metrics fail, you know why:**

- TCI = 0.0 → "Zero protocols extracted" → extraction problem, not paper problem
- ESD = infinity → "Zero evidence items" → extraction failure or genuinely non-empirical paper
- Schema change breaks metric → immediately obvious, fixable

**When LLMs fail, it's subtle:**

- Hallucinated limitations that aren't in the text
- Inconsistent standards between papers
- Misunderstanding domain context (rating archaeological "evidence" by clinical trial standards)
- Silent failures: produces plausible-sounding ratings that are wrong

**Value:** Quantitative metrics have **predictable, debuggable failure modes**.

**Use case:** Quality control - metrics flag extraction problems before qualitative assessment.

---

### 5. What LLMs Can't Do Reliably

Despite their power, LLMs:

- **Can't count reliably:** Ask LLM "how many evidence items?" vs `jq '.evidence | length'` - they make errors
- **Can't compare precisely:** "Is Paper A more transparent than Paper B?" gets inconsistent answers across runs
- **Can't do corpus statistics:** "What's the 75th percentile?" requires actual calculation
- **Hallucinate when uncertain:** Might invent limitations or miss them

**Quantitative metrics do these things perfectly.**

---

### 6. Scientific Standards for Instrument Validation

If this assessment system is used for research (evaluating FAIR compliance, transparency trends), **validated instruments are essential**.

**Quantitative metrics are easier to validate:**

- **Test-retest reliability:** Do we get the same ESD extracting the paper twice?
- **Inter-rater reliability:** Do two extractors get similar TCI scores?
- **Criterion validity:** Does ESD correlate with expert ratings of evidential adequacy?

**LLM qualitative assessments are harder to validate:**

- Require expert panels, larger samples, more complex statistical models
- Harder to isolate what the LLM is measuring

**Quantitative metrics provide a validated foundation that qualitative assessment builds on.**

---

## What Qualitative LLM Assessment Does Well

Qualitative LLM assessment provides essential capabilities that quantitative metrics cannot achieve.

### 1. Contextual Judgment: Understanding Meaning, Not Just Counts

**Example - SCS (Scope Constraints):**

**Quantitative approach (counts keywords):**
- "This study is limited to the archaeological record" → 1 point
- "We cannot rule out post-depositional disturbance" → 1 point
- **Score: 2 constraints**

**Qualitative LLM assessment:**
- First statement: *"Trivial/tautological - all archaeology is limited to material record"*
- Second statement: *"Substantive - acknowledges specific inferential limitation affecting interpretation"*
- **Rating: Moderate scope awareness (1 substantive limitation, 1 trivial)**

**The LLM understands which limitations matter.**

---

### 2. Domain-Appropriate Standards: Applying Different Yardsticks

**Example - RTI (Evidence Diversity):**

**Quantitative:**
- Pure dendrochronology paper: RTI = 0.0 (single evidence type)
- Mixed-method survey: RTI = 2.8 (multiple types)
- **Implication: Dendro paper scores "poorly"**

**Qualitative LLM:**
- Dendro paper: *"Appropriately focused - tree-ring dating requires depth not breadth. Multiple cores from multiple contexts provides adequate triangulation within method."*
- Mixed-method: *"Broad evidence base, but integration unclear - pottery, radiocarbon, and survey treated separately rather than triangulated."*
- **Rating: Both receive similar robustness scores for different reasons**

**The LLM understands disciplinary norms and research design logic.**

---

### 3. Detecting Subtle Red Flags: Rhetorical Moves and Self-Contradiction

**Example - "Limitations we've solved" problem:**

Paper text:
> "A potential limitation is sampling bias, however our stratified random sampling protocol mitigates this concern."

**Quantitative SCS:**
- Contains "limitation" → +1 point
- **Score increases** (paper gets credit)

**Qualitative LLM:**
- *"Author raises limitation only to immediately dismiss it - suggests defensiveness rather than genuine reflexivity. Claims mitigation but provides no evidence that bias was actually eliminated."*
- **Rating: Low scope awareness** (performative rather than substantive)

**The LLM detects rhetorical strategy and evaluates sincerity.**

---

### 4. Holistic Integration: Assessing Relationships and Coherence

**Example - Evidential adequacy beyond counts:**

**Quantitative ESD:**
- 50 claims, 100 evidence items = ESD of 0.5 (good!)

**Qualitative LLM assessment:**
- *"Most evidence items are descriptive observations (pottery counts, site locations). Claims include complex social interpretations (migration patterns, trade networks). Evidence is abundant but often not directly relevant to specific claims - mismatch between granularity levels."*
- **Rating: Moderate evidential adequacy** (quantity present but mapping quality poor)

**The LLM evaluates claim-evidence fit, not just counts.**

---

### 5. Genre and Context Adaptation

**LLMs can adjust standards appropriately:**

- **Theoretical papers:** Expect logical argumentation, not empirical evidence
- **Book chapters:** Expect narrative synthesis, not full methods reproduction
- **Preliminary reports:** Expect scope constraints, adjust expectations
- **Methodological papers:** Expect detailed protocols, fewer empirical claims

**Quantitative metrics apply same formula regardless of genre.**

---

## Complementary Architecture

### Two-Stage Filtering Model

```text
Stage 1: Quantitative Screening (Fast, Cheap, Objective)
├─ Flag outliers (ESD > 3.0 = many unsupported claims)
├─ Flag gaps (TCI < 0.3 = minimal methods documentation)
├─ Flag strengths (RTI > 2.5 = diverse evidence base)
├─ Corpus distribution (percentile rankings)
└─ Extraction quality control (TCI=0 → extraction failed)
         ↓
Stage 2: Qualitative Deep Dive (Slow, Expensive, Contextual)
├─ Investigate flagged papers (why is ESD so high?)
├─ Nuanced judgment (is low RTI appropriate for this design?)
├─ Substantive assessment (are limitations meaningful?)
├─ Domain-appropriate standards (adjust for genre/discipline)
└─ Final credibility rating (7 repliCATS signals)
```

---

### Value Propositions of Hybrid Architecture

**1. Triage**
- Don't waste LLM calls on obviously incomplete extractions
- TCI=0 means extraction failed, not paper bad
- Flag before expensive qualitative processing

**2. Calibration**
- Quantitative metrics help calibrate LLM assessments
- "This paper is 90th percentile for evidence density - don't judge harshly for missing evidence"
- Corpus context informs individual assessment

**3. Validation**
- If LLM says "poor transparency" but TCI=0.9, investigate discrepancy
- Is it extraction quality vs reporting quality?
- Metrics provide reality check on LLM judgments

**4. Efficiency**
- Quantitative metrics identify which papers need deep qualitative dive
- Which are straightforward/complete vs complex/problematic?
- Allocate expensive LLM resources strategically

**5. Explainability**
- "This paper rated poorly because:"
  - "ESD=3.2 (under-evidenced claims - see quantitative metric)"
  - "Scope awareness low (see qualitative rubric assessment)"
- Hybrid explanation is more convincing than either alone

**6. Corpus Characterisation**
- Use quantitative metrics to characterise paper corpora
- "This is a high-RDMAP corpus (TCI median=0.85) from methods-focused journals"
- Ground qualitative assessment in corpus context
- Enable within-corpus comparisons (is this paper above/below average for this domain?)

---

### Analogy: Academic Peer Review

Think of hybrid architecture like journal peer review:

| **Stage** | **Function** | **Equivalent** |
|-----------|-------------|----------------|
| **Quantitative metrics** | Desk reject | Incomplete submission, missing required sections |
| **Qualitative LLM** | Reviewer comments | Substantive assessment of contribution, rigour, validity |

**You wouldn't:**
- Skip desk reject and send everything to reviewers (expensive, slow)
- *Only* do desk reject without substantive review (misses quality issues)

**You need both.**

---

### The LLM Capability Paradox

*Because LLMs are so powerful at qualitative judgment, we need quantitative metrics as guardrails.*

**Three reasons:**

**1. Trust and Verification**

Research assessment has high stakes (funding, reputation, career impact). Need:
- Explainable scores (not "the AI said so")
- Auditable decisions (show your working)
- Dispute mechanisms (challenge the rating)

Quantitative metrics provide **hard evidence** grounding LLM judgments.

When challenged:
- "Transparency rating based on: TCI=0.4 (only 3/8 expected protocol elements) + methods clarity rubric=2/5 (LLM comprehensibility assessment)"
- Can debate the rubric, but **the count is the count**

---

**2. LLM Limitations We Often Forget**

Despite power, LLMs still:
- Can't count reliably
- Can't compare precisely across runs
- Can't do corpus statistics
- Hallucinate when uncertain

Quantitative metrics do these perfectly.

---

**3. Scientific Standards for Instrument Validation**

If assessment system is used for research, need **validated instruments**.

Quantitative metrics easier to validate:
- Test-retest, inter-rater, criterion validity
- Clear measurement properties

LLM assessments harder to validate (need expert panels, larger samples).

**Quantitative metrics provide validated foundation for qualitative assessment.**

---

## Design Decisions and Future Directions

### Why These Metrics Are Defensible (Despite Critiques)

The metrics are defensible **as a starting point for empirical investigation**, not as validated instruments, because:

**1. Treating Them Correctly**
- **Exploratory, not confirmatory:** Testing empirically, not assuming they work
- **Iterative refinement:** Expect to modify based on validation
- **Complementary to qualitative:** Screening tools, not final judgments
- **Transparent about limitations:** Documenting assumptions and constraints

**2. Clear Value Proposition**
- Ground qualitative assessment in objective measures
- Enable rapid screening before deep analysis
- Provide auditable, reproducible components
- Catch what LLMs miss (counts, distributions, trends)

**3. Empirical Validation Plan**
- User (domain expert) validates on 11-paper corpus first
- Calibrate thresholds to actual distribution
- Refine metrics based on observed performance
- External validation (Aaron, repliCATS) on larger corpus
- Iterative improvement based on empirical data

---

### Limitations Acknowledged and Mitigation Strategies

| **Limitation** | **Mitigation Strategy** | **Timeline** |
|---------------|------------------------|--------------|
| **Fixed thresholds** (e.g., 2 RD, 5 methods) | Shift to corpus-relative percentiles after empirical data | Phase 1, Session 3 |
| **Extraction granularity dependency** | Develop extraction guidelines, measure inter-rater reliability | Phase 2 |
| **Genre/domain bias** | Add domain/genre flags, report metrics by category | Phase 3 |
| **"More is better" fallacy** | Complement with qualitative rubrics (Phase 2), investigate outliers | Phase 2 |
| **Limitations quality vs count** | Qualitative rubric for substantive vs trivial limitations | Phase 2 |
| **Small sample size** (11 papers) | Expand to larger corpus with Aaron's validation | Phase 4-5 |
| **No ground truth** | Expert validation (user first, Aaron second) | Phase 1-5 ongoing |
| **No reliability testing** | Test-retest, inter-rater studies | Phase 3 |

---

### Adaptive Yardsticks: Future Directions

**Current approach (Phase 1):** Fixed thresholds for bootstrapping
- Expected 2 RD, 5 methods, 8 protocols
- Enables initial calculation and testing

**Near-term evolution (Phase 1, Session 3):** Corpus-relative percentiles
- "This paper is 75th percentile for RDMAP completeness"
- See if paper is above/below average for corpus under study
- Characterise corpus: "High-RDMAP corpus (median TCI=0.85)"

**Medium-term evolution (Phase 2-3):** Domain/genre-specific benchmarks
- Archaeology vs ethnography vs palaeoenvironmental
- Empirical vs theoretical vs methodological papers
- Book chapters vs journal articles vs reports

**Long-term evolution (Phase 4-5):** Evidence-based thresholds
- Benchmarking exercise on high-quality papers
- Correlation with expert judgments
- Validated cut-offs for "good"/"adequate"/"poor"

**Critical question to monitor:** Are we capturing quality or just breadth/narrowness?
- More RDs/methods/protocols = broader scope, not necessarily better
- Need qualitative assessment to distinguish appropriate scope from inadequate detail
- Metrics identify patterns, rubrics assess appropriateness

---

### Absolute vs Relative Metrics: Clarity Needed

| **Metric** | **Current Interpretation** | **Absolute or Relative?** | **Future Direction** |
|-----------|---------------------------|---------------------------|---------------------|
| **ESD** | Lower is better | Relative (corpus-dependent) | Report percentile + raw ratio |
| **TCI** | Higher is better (0-1) | Mixed (thresholds absolute, but should be relative) | Shift to corpus percentile |
| **SCS** | Higher is better (count) | Absolute, but problematic | Add qualitative substantiveness rating |
| **RTI** | Higher is better (Shannon H) | Relative (corpus-dependent) | Report percentile + effective types |
| **RIS** | Higher is better (count) | Absolute (PIDs present/absent) | Could add corpus comparison |
| **PGCS** | Higher is better | Absolute (connectivity measured) | Could add corpus comparison |
| **FCS** | 0-15 scale | Absolute (FAIR principles) | Likely stays absolute, may add corpus context |
| **MDD** | Higher is better (quote length) | Relative (corpus-dependent) | Report percentile + mean length |

**Recommendation:** Report both raw scores and corpus percentiles for all metrics.

---

### Extraction Consistency: Critical Dependency

**Several metrics highly sensitive to extraction granularity:**

- **ESD:** Evidence count vs claims count - how granular is "one evidence item"?
- **TCI:** How granular is "one protocol"? (atomic step vs procedure)
- **MDD:** Quote length depends on what we extract as unit

**Needed for validation:**

1. **Extraction guidelines** (in progress):
   - Define granularity for evidence items
   - Define protocol vs method boundary
   - Define when to split vs combine

2. **Inter-rater reliability testing** (Phase 3):
   - Same paper extracted by multiple extractors
   - Compare metric scores
   - Identify sources of variance

3. **Multi-run stability** (Phase 3):
   - Same paper extracted multiple times (LLM variance)
   - Quantify score variability
   - Establish confidence intervals

**Until this is done, metrics are exploratory only.**

---

### Qualitative Nuance: Essential Complement

**Quantitative metrics identify patterns. Qualitative rubrics assess appropriateness.**

**Examples where qualitative assessment is essential:**

1. **Low RTI (single evidence type):**
   - Quantitative: Flags as potential concern
   - Qualitative: "Appropriately focused for dendrochronology study" OR "Problematic - survey study should triangulate"

2. **High SCS (many limitations):**
   - Quantitative: Looks good (acknowledging constraints)
   - Qualitative: "Substantive reflexivity" OR "Trivial hedging" OR "Catastrophically flawed study"

3. **High ESD (low evidence per claim):**
   - Quantitative: Flags under-evidenced claims
   - Qualitative: "Theoretical paper with logical arguments" OR "Speculation without support"

**The hybrid architecture works because:**
- Metrics flag patterns (outliers, gaps, strengths)
- Rubrics assess meaning (appropriate or problematic?)
- Together approximate expert judgment

---

### Learning Feedback to Extraction Phase

**User raised important concern:** Papers that acknowledge limitations only to dismiss them.

**Example:**
> "A potential limitation is sampling bias, however our stratified random sampling protocol mitigates this concern."

**Current extraction:** Would capture as claim with limitation keyword → SCS +1

**Problem:** Performative limitation acknowledgment, not genuine reflexivity

**Solution:** Feed learnings back to extraction phase

**Potential extraction refinement (Pass 1-2):**
- Capture limitation acknowledgments with modifier field:
  - `limitation_type: "acknowledged_mitigated"` vs `"acknowledged_unresolved"`
- Enable SCS to weight appropriately

**Workflow:**
1. Phase 1-2: Use current metrics, identify problematic patterns
2. Phase 3: Refine extraction schema based on assessment learnings
3. Phase 4: Re-extract corpus with refined schema
4. Phase 5: Recalculate metrics with improved data

**This is iterative development working as intended.**

---

## References

### Frameworks and Methodologies

**repliCATS (Collaborative Assessments for Trustworthy Science):**
- Focuses on lab science replication
- Seven credibility signals assessed by expert panels
- Qualitative rubrics, not quantitative metrics
- This project adapts approach to HASS fieldwork

**Reporting Guidelines:**
- CONSORT (Consolidated Standards of Reporting Trials)
- TIDieR (Template for Intervention Description and Replication)
- SPIRIT (Standard Protocol Items: Recommendations for Interventional Trials)
- Specify minimum reporting elements for clinical research

**FAIR Principles:**
- Findable, Accessible, Interoperable, Reusable
- Data and software sharing standards
- Assessed in Pass 6 (Infrastructure extraction)
- FCS metric uses Pass 6 FAIR scores

### Quantitative Methods

**Shannon Diversity Index:**
- Originally from information theory (Shannon 1948)
- Applied in ecology to measure species diversity
- Formula: H = -Σ(p_i × ln(p_i))
- Used in RTI to measure evidence type diversity

**Evidential Reasoning:**
- Philosophical framework for evaluating claim support
- Claims require empirical grounding
- Inspiration for ESD metric

**Metascience Literature:**
- Research on research quality, transparency, reproducibility
- Overconfidence and scope constraints
- Inspiration for SCS metric

### Project-Specific Documents

- `planning/assessment-implementation-plan.md` - Complete 5-phase plan
- `docs/background-research/replicats-seven-signals-hass-adaptation.md` - repliCATS adaptation
- `planning/extraction-to-analysis-transition.md` - Assessment framework overview
- `extraction-system/schema/reproducibility-infrastructure-schema-v2.6.yaml` - Pass 6 schema
- `assessment-system/scripts/analysis_toolkit.py` - Metric implementations

---

## Document Status and Evolution

**Version 1.0 (2025-11-14):** Initial critical discussion capturing methodological foundations

**Expected Evolution:**

- **Phase 1, Session 3:** Add empirical validation results from 11-paper corpus
- **Phase 2:** Update with qualitative rubric integration learnings
- **Phase 3:** Add inter-rater reliability findings, extraction guideline refinements
- **Phase 4-5:** Add external validation (Aaron/repliCATS) results, final metric specifications

**Living Document:** Will be updated as empirical validation informs refinements.

---

## Conclusion

The quantitative metrics developed for this project are **experimental instruments** requiring empirical validation. They are defensible as:

1. **Exploratory tools** for pattern detection, not validated assessments
2. **Complementary to qualitative LLM judgment**, not replacements
3. **Grounded in research transparency principles**, even if not directly from repliCATS
4. **Designed for iterative refinement** based on empirical data

**Key Strengths:**
- Objective, auditable, reproducible
- Fast, scalable, corpus-comparable
- Predictable failure modes
- Enable systematic analysis

**Key Limitations:**
- Measure textual explicitness, not necessarily quality
- Sensitive to extraction granularity
- Assume quantity = quality (often false)
- Small sample, no ground truth validation yet
- May not match HASS epistemology

**The hybrid quantitative-qualitative architecture is justified because:**
- Metrics ground LLM judgment (objectivity)
- LLMs provide nuance metrics lack (contextual understanding)
- Together they approximate expert human assessment
- Two-stage filtering is efficient and explainable

**Critical next step:** Empirical validation on 11-paper corpus will determine whether these metrics actually work in practice.

---

**Navigation:** [Main README](../../README.md) | [Assessment Plan](../../planning/assessment-implementation-plan.md) | [Background Research Index](../background-research/)
