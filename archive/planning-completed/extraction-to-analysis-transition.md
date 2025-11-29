# From Extraction to Analysis: A Transition Framework
## Leveraging CEM Graphs for Credibility Assessment in HASS Research

**Document Purpose:** Guide the transition from successful extraction work (CEM graphs + RDMAP) to systematic credibility/reliability analysis

**Date:** 2 November 2025 (Updated: 3 November 2025)

**Project Phase:** Post-extraction, infrastructure enhancement, pre-assessment

**Author:** Discussion starter for analytical framework development

**Updates:** Added Part 9 documenting Pass 6 infrastructure extraction enhancement (PIDs, FAIR assessment, permits)

---

## Executive Summary: Where We Are and Where We're Going

### What We Have Built (Extraction Phase Complete)

You have successfully created:

- **10 complete CEM graph extractions** with 1,693 total items
- **629 relationship mappings** connecting claims to evidence, methods to designs, protocols to methods
- **Structured knowledge representations** in canonical schema v2.5 format
- **High-quality extractions** (70% grade B or higher based on structural assessment)
- **Systematic extraction methodology** with validated multi-pass workflow

### What We Need to Build (Analysis Phase Ahead)

The transition to analysis requires moving from:

- **Descriptive extraction** ("what does the paper say?") → **Evaluative assessment** ("how credible is what the paper says?")
- **Structural completeness** ("are all elements captured?") → **Epistemic adequacy** ("is the evidence sufficient for the claims?")
- **Individual paper graphs** → **Cross-paper pattern recognition** and **comparative credibility profiles**

### The Core Challenge You're Facing

> "I've spent so long on extraction details that I've lost sight of how we approach analysis"

This is a **natural and important transition point**. Extraction required intense focus on *accuracy* and *completeness*. Analysis requires shifting focus to *interpretation* and *assessment* of what you've extracted.

The good news: **The repliCATS Seven Signals framework provides a clear analytical structure**. The challenge: **Operationalising those signals against your CEM graph data**.

---

## Part 1: Connecting Extraction Outputs to Analytical Goals

### The Fundamental Question

Your overall goal is to assess:

> **"The reliability/credibility of papers in long-tail domains where reproducibility (in the narrow sense) may not be appropriate"**

This maps precisely to **repliCATS credibility assessment**, which intentionally broadens beyond reproducibility to encompass:

1. **Comprehensibility** - Can the argument be understood?
2. **Transparency** - Is the research process documented?
3. **Plausibility** - Does it fit with existing knowledge?
4. **Validity** - Is the evidence adequate for the claims?
5. **Robustness** - Would results hold under reasonable alternatives?
6. **Replicability** - Can analytical processes be reproduced? (Not field replication)
7. **Generalisability** - Are scope limitations explicit?

### What Your CEM Graphs Enable

Your extraction schema was **designed to feed these assessments**. Here's the direct mapping:

| Credibility Signal | Available from CEM Extraction | Assessment Approach |
|-------------------|------------------------------|---------------------|
| **Comprehensibility** | - Explicit vs implicit claims<br>- Claim scope qualifiers<br>- Logical claim→evidence links<br>- Term definitions in evidence | **Qualitative:** Review claim clarity, scope boundedness<br>**Quantitative:** % explicit claims, scope qualifier presence, term definition coverage |
| **Transparency** | - Research designs (exploratory/confirmatory)<br>- Methods documentation<br>- Protocol specifications<br>- RDMAP hierarchy completeness | **Qualitative:** Assess design rationale clarity<br>**Quantitative:** Design→method→protocol completeness score, RDMAP depth |
| **Plausibility** | - Domain context in evidence<br>- Chronological/geographic references<br>- Citations to comparanda<br>- Anomaly acknowledgment flags | **Qualitative:** Expert domain coherence review<br>**Quantitative:** Comparanda citation density, anomaly acknowledgment presence (currently not captured - enhancement needed) |
| **Validity** | - Evidence→claim mappings<br>- Claims-to-evidence ratio<br>- Alternative interpretations (if stated)<br>- Sampling limitation statements | **Qualitative:** Assess evidential sufficiency<br>**Quantitative:** C:E ratio, mapping density, alternative interpretation presence |
| **Robustness** | - Analytical workflow documentation<br>- Sensitivity analyses (if present)<br>- Multiple independent evidence lines<br>- Triangulation patterns | **Qualitative:** Assess convergent evidence<br>**Quantitative:** Evidence type diversity, sensitivity analysis presence, triangulation index |
| **Replicability** | - Data/code availability mentions<br>- Repository links (need to verify)<br>- Workflow documentation<br>- FAIR/CARE indicators | **Qualitative:** Assess data stewardship appropriateness<br>**Quantitative:** Repository link presence, link resolution rate, metadata completeness |
| **Generalisability** | - Claim scope declarations<br>- Explicit limitation statements<br>- Geographic/temporal bounds<br>- Over-generalisation flags | **Qualitative:** Review scope constraint appropriateness<br>**Quantitative:** Limitation statement density, scope-evidence alignment |

### The Critical Insight

**You already have the infrastructure for assessment**. What you need now is:

1. **Assessment rubrics** - Clear scoring criteria for each signal
2. **Assessment workflows** - Processes for applying rubrics to CEM graphs
3. **Analysis infrastructure** - Tools for querying graphs and aggregating scores
4. **Validation framework** - Methods for checking assessment reliability

---

## Part 2: Proposed Analysis Approaches (Qualitative + Quantitative)

### Approach A: Signal-by-Signal Assessment (Systematic Rubric Application)

**What:** Assess each paper against all seven signals using structured rubrics

**How:**

1. **Create detailed rubrics** for each signal (0-100 scale with clear anchors)
2. **Assess papers systematically** (either human or LLM-assisted)
3. **Generate signal profiles** showing strengths/weaknesses per paper
4. **Aggregate to credibility scores** with transparent provenance

**Example Rubric Structure (Validity Signal):**

```
VALIDITY ASSESSMENT RUBRIC (Evidential Adequacy)

Score 80-100 (Excellent):
- All major claims supported by multiple independent evidence items
- Alternative interpretations explicitly considered
- Sampling limitations clearly stated
- Evidence sufficient and representative for claim scope
- No over-generalisation from limited data

Score 60-79 (Good):
- Most claims supported by adequate evidence
- Some alternative interpretations considered
- Sampling strategy documented
- Minor scope-evidence mismatches
- Generally appropriate generalisation

Score 40-59 (Moderate):
- Claims have some evidentiary support
- Alternative interpretations rarely mentioned
- Sampling limitations not fully addressed
- Some over-generalisation present
- Evidence adequate for core claims but weak for broader ones

Score 20-39 (Poor):
- Many claims weakly supported
- No alternative interpretations considered
- Sampling strategy unclear or absent
- Significant over-generalisation
- Evidence-claim scope mismatch

Score 0-19 (Very Poor):
- Claims largely unsupported by evidence
- No engagement with alternatives
- No acknowledgment of limitations
- Extreme over-generalisation
- Evidence inadequate for claims made

ASSESSMENT PROCESS:
1. Review all claims and their linked evidence
2. Calculate C:E ratio and mapping density
3. Check for alternative interpretation statements
4. Check for limitation/sampling statements
5. Assess scope alignment
6. Assign score with written justification
```

**Outputs:**
- Per-paper credibility scorecards
- Signal distribution charts
- Cross-paper comparative profiles
- Detailed justifications with CEM graph references

**Effort:** Moderate (can be partially automated with LLM assessors)

---

### Approach B: Pattern-Based Analysis (Cross-Paper Learning)

**What:** Identify recurrent patterns across papers that indicate credibility strengths/weaknesses

**How:**

1. **Structural pattern mining:**
   - Papers with zero mappings → systematic transparency failure
   - High C:E ratios (>3.0) → validity concerns
   - Missing RDMAP elements → transparency/replicability issues

2. **Content pattern analysis:**
   - Consistent absence of alternative interpretations
   - Lack of limitation statements
   - Repository link presence/absence patterns

3. **Domain-specific patterns:**
   - Do certain research types have characteristic credibility profiles?
   - Are there field-specific credibility strengths (e.g., archaeology strong on contextualisation, weak on replicability)?

**Example Patterns Already Identified:**

From your batch assessment:
- **Missing mappings pattern** (30% of papers): Pass 6 failures indicating severe transparency problems
- **Extreme C:E ratio pattern** (40% >2.5): Possible evidence under-extraction or claim inflation
- **Schema inconsistency pattern**: Field naming evolution affecting cross-paper analysis

**Outputs:**
- Pattern catalogue with credibility implications
- Paper clustering by credibility profile
- Failure mode taxonomy
- Domain-specific credibility baselines

**Effort:** Moderate (mostly automated with human interpretation)

---

### Approach C: Graph-Based Credibility Metrics (Quantitative Structure Analysis)

**What:** Derive credibility indicators from CEM graph structure itself

**Proposed Metrics:**

#### 1. Evidential Support Density
```
ESD = (total evidence→claim mappings) / (total claims)

Interpretation:
- ESD < 0.5: Weak evidential support (many claims unsupported)
- ESD 0.5-1.0: Moderate support (most claims have some evidence)
- ESD 1.0-2.0: Good support (claims have multiple evidence items)
- ESD > 2.0: Strong support (extensive triangulation)
```

#### 2. Transparency Completeness Index
```
TCI = weighted sum of:
  - Research designs declared (0-25 points)
  - Design→method mappings (0-25 points)
  - Method→protocol mappings (0-25 points)
  - Protocol detail sufficiency (0-25 points)

Interpretation:
- TCI < 40: Poor transparency
- TCI 40-60: Moderate transparency
- TCI 60-80: Good transparency
- TCI > 80: Excellent transparency
```

#### 3. Scope Constraint Score
```
SCS = % of claims with:
  - Explicit temporal bounds
  - Explicit spatial bounds
  - Explicit population/domain bounds
  - Limitation statements linked

Interpretation:
- SCS < 30%: Poor scope discipline
- SCS 30-60%: Moderate constraint
- SCS 60-85%: Good constraint
- SCS > 85%: Excellent scope discipline
```

#### 4. Robustness Triangulation Index
```
RTI = measures:
  - Evidence type diversity (how many different evidence types support claims?)
  - Convergent evidence patterns (do multiple independent evidence streams support same claims?)
  - Sensitivity analysis presence
  - Alternative interpretation engagement

Composite score 0-100
```

#### 5. Replicability Infrastructure Score
```
RIS = presence + verification of:
  - Data repository links (0-30 points)
  - Code repository links (0-20 points)
  - Protocol documentation (0-20 points)
  - Workflow specifications (0-15 points)
  - FAIR/CARE compliance (0-15 points)

Interpretation:
- RIS < 30: Minimal replicability
- RIS 30-60: Partial replicability
- RIS 60-85: Good replicability
- RIS > 85: Excellent replicability
```

**Outputs:**
- Quantitative credibility profiles per paper
- Comparative metric distributions across corpus
- Correlation analyses (which metrics cluster together?)
- Credibility benchmarks for domain

**Effort:** Low (highly automated once metrics defined)

---

### Approach D: LLM-Assisted Multi-Agent Assessment (repliCATS IDEA Adaptation)

**What:** Use multiple independent LLM agents to assess papers, following repliCATS deliberation model

**Process:**

**Stage 1: Independent Assessment (Investigate)**
- Deploy 3-5 independently seeded LLM agents
- Each agent receives:
  - Full CEM graph for paper
  - Relevant text excerpts
  - Assessment rubric for one signal
- Each agent produces:
  - Score (0-100) with lower/best/upper bounds
  - 3-5 sentence justification
  - Citations to specific CEM graph elements (evidence IDs, claim IDs)

**Stage 2: Synthetic Aggregation (Discuss & Estimate)**
- Synthesiser agent receives all assessments
- Identifies agreement/disagreement patterns
- Produces aggregated score (trimmed mean)
- Flags high-variance cases for human review
- Generates summary justification citing specific graph elements

**Stage 3: Validation (Aggregate)**
- Compare LLM assessments to human expert panel (subsample)
- Calculate inter-rater reliability (Gwet's AC1)
- Compute calibration metrics (Brier scores)
- Identify systematic biases
- Refine prompts/thresholds

**Example Agent Prompt (Validity Signal):**

```
You are assessing the VALIDITY (evidential adequacy) of a research paper.

INPUT DATA:
- CEM graph with {N} claims, {M} evidence items, {K} mappings
- Full text excerpts for context

YOUR TASK:
1. Review all claims and their supporting evidence
2. Assess whether evidence is sufficient and representative for claims made
3. Check for alternative interpretations
4. Check for sampling limitation statements
5. Assess scope-evidence alignment

OUTPUT REQUIRED:
{
  "signal": "validity",
  "score_lower": <pessimistic score 0-100>,
  "score_best": <most likely score 0-100>,
  "score_upper": <optimistic score 0-100>,
  "justification": "<2-4 sentences explaining score>",
  "evidence_refs": ["<claim_id>", "<evidence_id>", ...],
  "key_strengths": ["<strength 1>", "<strength 2>"],
  "key_weaknesses": ["<weakness 1>", "<weakness 2>"]
}
```

**Outputs:**
- Per-paper credibility scorecards with uncertainty bounds
- Agent agreement metrics (identifies controversial papers)
- Justification corpus for pattern mining
- Calibrated probability estimates

**Effort:** Moderate-High (requires prompt engineering, validation)

---

### Approach E: Targeted Quality Indicators (Minimum Viable Assessment)

**What:** Focus on a small set of high-signal indicators for rapid assessment

**Proposed Minimal Indicator Set:**

1. **Has structured research design?** (Yes/No) → Transparency
2. **Claims-to-evidence ratio** (0.5-1.5 = good) → Validity
3. **Has repository links?** (Yes/No) → Replicability
4. **Has limitation statements?** (Yes/No) → Generalisability
5. **Has alternative interpretations?** (Yes/No) → Validity/Robustness
6. **RDMAP completeness** (Design→Method→Protocol chain intact?) → Transparency

**Simple Scoring:**
- Each indicator: 0 (absent), 50 (partial), 100 (present)
- Average across indicators = overall credibility score
- Traffic light system: <40 red, 40-70 yellow, >70 green

**Outputs:**
- Quick credibility flags per paper
- Prioritisation for detailed assessment
- Baseline credibility distribution

**Effort:** Low (can be fully automated)

---

## Part 3: Recommended Phased Implementation

### Phase 1: Foundation (Weeks 1-2)
**Goal:** Establish assessment infrastructure

**Tasks:**
1. Define detailed rubrics for all seven signals (adapt from repliCATS guidance)
2. Develop graph query utilities (Python/jq scripts to extract specific patterns from extraction.json)
3. Create assessment templates (standardised formats for scorecards)
4. Pilot test: Manually assess 2-3 papers using rubrics to validate feasibility

**Outputs:**
- Complete rubric document (seven signals)
- Graph analysis toolkit
- Assessment template library
- Pilot assessment reports

---

### Phase 2: Quantitative Baseline (Weeks 3-4)
**Goal:** Generate quantitative credibility metrics for full corpus

**Tasks:**
1. Implement Approach C metrics (ESD, TCI, SCS, RTI, RIS)
2. Run metric calculations on all 10 papers
3. Generate comparative distributions
4. Identify outliers and patterns
5. Correlate metrics with existing structural grades

**Outputs:**
- Quantitative credibility profiles (10 papers)
- Metric correlation matrix
- Outlier identification report
- Credibility benchmark document

---

### Phase 3: Qualitative Deep Dive (Weeks 5-6)
**Goal:** Perform systematic signal-by-signal assessment on subset

**Tasks:**
1. Select 3 diverse papers (high/medium/low structural grades)
2. Apply Approach A (full rubric assessment) to each
3. Generate detailed scorecards with justifications
4. Compare qualitative assessments to quantitative metrics
5. Refine rubrics based on application experience

**Outputs:**
- 3 complete credibility scorecards
- Rubric refinement notes
- Qualitative-quantitative alignment analysis

---

### Phase 4: LLM Assessment Prototype (Weeks 7-9)
**Goal:** Automate assessment using multi-agent LLM approach

**Tasks:**
1. Develop agent prompts for each signal (based on refined rubrics)
2. Implement multi-agent assessment workflow
3. Run on 5 papers with 3-agent ensembles per signal
4. Compare LLM assessments to Phase 3 human assessments
5. Compute inter-rater reliability and calibration metrics
6. Identify systematic LLM biases or errors

**Outputs:**
- LLM assessment pipeline (code)
- 5 LLM-generated scorecards
- Human-LLM comparison analysis
- Bias/error taxonomy
- Calibration report

---

### Phase 5: Full Corpus Assessment (Weeks 10-12)
**Goal:** Complete credibility assessment of all 10 papers

**Tasks:**
1. Deploy validated LLM assessment pipeline to all 10 papers
2. Flag high-uncertainty cases for human review
3. Generate comprehensive credibility database
4. Perform cross-paper pattern analysis (Approach B)
5. Create visualisations and summary reports
6. Document methodology and limitations

**Outputs:**
- Complete credibility database (10 papers × 7 signals)
- Cross-paper pattern catalogue
- Visual credibility dashboards
- Methodology documentation
- Limitations and future work report

---

## Part 4: Infrastructure and Tooling Needs

### Analysis Scripts Required

#### 1. CEM Graph Query Library
```python
# Extract specific patterns from extraction.json

def get_claims_to_evidence_ratio(extraction):
    """Calculate C:E ratio"""

def get_unsupported_claims(extraction):
    """Find claims with no evidence mappings"""

def get_evidence_type_distribution(extraction):
    """Analyse evidence type diversity"""

def get_rdmap_completeness(extraction):
    """Check Design→Method→Protocol chain integrity"""

def get_scope_constraint_coverage(extraction):
    """Count claims with explicit bounds"""

def get_repository_links(extraction):
    """Extract data/code repository mentions"""
```

#### 2. Metric Calculation Pipeline
```python
# Compute credibility metrics

def calculate_evidential_support_density(extraction):
    """ESD metric"""

def calculate_transparency_completeness_index(extraction):
    """TCI metric"""

def calculate_scope_constraint_score(extraction):
    """SCS metric"""

def calculate_robustness_triangulation_index(extraction):
    """RTI metric"""

def calculate_replicability_infrastructure_score(extraction):
    """RIS metric"""
```

#### 3. Assessment Workflow Manager
```python
# Orchestrate multi-agent LLM assessment

def run_multi_agent_assessment(paper_id, signal, n_agents=3):
    """Deploy N independent agents for signal assessment"""

def aggregate_agent_scores(agent_outputs):
    """Combine scores with uncertainty quantification"""

def flag_for_human_review(aggregated_score, variance_threshold):
    """Identify high-uncertainty cases"""

def generate_scorecard(paper_id, all_signal_scores):
    """Create comprehensive credibility report"""
```

#### 4. Visualisation and Reporting
```python
# Generate analysis outputs

def create_signal_radar_chart(scorecard):
    """7-signal radar plot"""

def create_credibility_matrix_heatmap(corpus_scores):
    """Papers × signals heatmap"""

def create_metric_correlation_plot(metric_data):
    """Correlation matrix visualisation"""

def generate_markdown_scorecard(paper_id, scores, justifications):
    """Human-readable report"""
```

### Data Structures Needed

#### Credibility Scorecard Schema
```json
{
  "paper_id": "sobotkova-et-al-2024",
  "assessment_date": "2025-11-05",
  "assessor_type": "multi_agent_llm",
  "signals": {
    "comprehensibility": {
      "score": 85,
      "score_lower": 80,
      "score_upper": 90,
      "justification": "Claims are explicit and well-scoped...",
      "evidence_refs": ["C001", "C005", "E023"],
      "key_strengths": ["Clear scope bounds", "Term definitions present"],
      "key_weaknesses": ["Some implicit assumptions"]
    },
    "transparency": { ... },
    "plausibility": { ... },
    "validity": { ... },
    "robustness": { ... },
    "replicability": { ... },
    "generalisability": { ... }
  },
  "overall_credibility": 72,
  "confidence_interval": [68, 76],
  "priority_improvements": [
    "Add repository links for data",
    "Include sensitivity analyses"
  ]
}
```

---

## Part 5: Key Considerations and Decisions Needed

### Decision 1: Assessment Philosophy

**Question:** Should assessment be **descriptive** (documenting what's present) or **normative** (judging against ideal standards)?

**Options:**
- **Descriptive:** "This paper has X mappings, Y limitation statements, Z repository links" → Neutral reporting
- **Normative:** "This paper scores 60/100 on validity because..." → Evaluative judgment

**Recommendation:** **Hybrid approach**
- Use descriptive metrics as foundation (objective, reproducible)
- Add normative assessment for complex signals (validity, robustness) that require judgment
- Clearly separate descriptive facts from evaluative judgments in reports

---

### Decision 2: Domain-Specific Calibration

**Question:** Should credibility standards vary by research type?

**Context:** Your corpus includes:
- Empirical fieldwork papers (surveys, excavations)
- Methodological papers (testing techniques)
- Synthetic/theoretical papers

**Recommendation:** **Differentiated profiles, common framework**
- Use same seven signals for all papers
- Mark signals as "not applicable" where inappropriate (e.g., replicability N/A for theoretical papers)
- Establish domain-specific baselines (what's "good" for survey archaeology may differ from philology)
- Document research type in scorecard for context

---

### Decision 3: Human Validation Strategy

**Question:** How much human validation is needed?

**Options:**
1. **Minimal:** Spot-check LLM assessments, trust automation
2. **Moderate:** Expert panel assesses 20-30% of corpus, calibrate LLMs
3. **Extensive:** Full parallel human/LLM assessment, deep comparison

**Recommendation:** **Moderate validation** (Option 2)
- Expert panel (3-5 researchers) independently assesses 3 papers
- Compare expert vs LLM scores (inter-rater reliability)
- Use discrepancies to refine prompts and rubrics
- Document where LLMs systematically diverge from experts
- Reserve full human assessment for high-stakes or controversial cases

---

### Decision 4: Uncertainty Representation

**Question:** How should we represent uncertainty in assessments?

**Options:**
1. **Point scores:** Single number (0-100)
2. **Interval scores:** Range (lower-upper)
3. **Distributional:** Full probability distribution

**Recommendation:** **Interval scores** (Option 2)
- Lower bound = pessimistic but defensible assessment
- Best estimate = most likely score
- Upper bound = optimistic but defensible assessment
- Width of interval indicates confidence
- Follows repliCATS IDEA protocol
- Balances precision with honesty about uncertainty

---

### Decision 5: Public Reporting Sensitivity

**Question:** How should credibility assessments be communicated?

**Context:** You're assessing real papers by real researchers. Negative assessments could be sensitive.

**Recommendation:** **Constructive, anonymous aggregate reporting**
- Individual scorecards: Private, shared only with authors if they request
- Aggregate patterns: Anonymised reporting ("30% of papers lacked repository links")
- Focus on improvement: Frame weaknesses as opportunities ("adding data repositories would strengthen replicability")
- Pilot phase: Treat as formative assessment to refine methodology, not summative judgment

---

## Part 6: Success Metrics for Analysis Phase

### How will you know the analysis phase is working?

#### Metric 1: Assessment Reliability
**Target:** Inter-rater reliability (human-human or human-LLM) > 0.70 (Gwet's AC1)

**Why:** Indicates assessments are consistent and not arbitrary

**How to measure:** Expert panel independently scores 3 papers, compute agreement

---

#### Metric 2: Discriminative Validity
**Target:** Credibility scores should correlate with known quality indicators

**Why:** Validates that scores capture actual credibility differences

**How to measure:**
- Papers with repository links should score higher on replicability
- Papers with clear RDMAP should score higher on transparency
- Papers with high C:E ratios should score lower on validity

---

#### Metric 3: Actionable Insights
**Target:** Every low-scoring signal should have clear improvement recommendations

**Why:** Assessments should be formative, not just summative

**How to measure:** Review scorecards - can authors identify specific actions to improve?

---

#### Metric 4: Pattern Coherence
**Target:** Cross-paper patterns should make domain sense

**Why:** Validates that patterns reflect real phenomena, not artefacts

**How to measure:** Do identified patterns align with expert intuitions about field practices?

---

#### Metric 5: Transparency of Provenance
**Target:** Every score should trace to specific CEM graph elements

**Why:** Ensures assessments are auditable and contestable

**How to measure:** Can you trace any score back to specific evidence/claim/method IDs?

---

## Part 7: Risks and Mitigations

### Risk 1: Assessment Subjectivity

**Problem:** Different assessors may score same paper differently

**Mitigation:**
- Detailed rubrics with clear anchors
- Multi-agent ensembles to reduce individual biases
- Calibration against expert panel
- Document assessment methodology transparently

---

### Risk 2: Domain Knowledge Gaps

**Problem:** LLMs (or human assessors) may lack domain expertise to judge plausibility

**Mitigation:**
- Focus on structural signals (transparency, validity) where expertise matters less
- Mark plausibility signal as "requires domain expert review"
- Build domain knowledge bases for RAG (gazetteers, chronologies, typologies)
- Reserve domain-heavy assessments for expert panel

---

### Risk 3: Overfitting to Corpus

**Problem:** Rubrics/metrics optimised for 10 papers may not generalise

**Mitigation:**
- Keep rubrics general (based on repliCATS principles, not corpus idiosyncrasies)
- Test on held-out papers when expanding corpus
- Document corpus characteristics that may affect generalisation
- Regularly revisit and refine rubrics as corpus grows

---

### Risk 4: Automation Bias

**Problem:** Over-reliance on LLM assessments without critical human review

**Mitigation:**
- Always flag high-variance or extreme scores for human review
- Maintain human validation cadence (assess subset regularly)
- Document LLM limitations and systematic errors
- Treat LLM assessments as "first pass" requiring verification

---

### Risk 5: Perceived Criticism of Colleagues

**Problem:** Credibility assessment could be seen as attacking researchers' work

**Mitigation:**
- Frame as methodology improvement, not researcher judgment
- Anonymise aggregate reporting
- Share individual scorecards privately with constructive framing
- Emphasise formative assessment (identify improvement opportunities)
- Acknowledge systemic issues (infrastructure gaps, field norms) vs individual failings

---

## Part 8: Immediate Next Steps (Week 1 Action Items)

### 1. Define Rubrics (Priority: High)

**Task:** Create detailed scoring rubrics for all seven signals

**Why:** Foundation for all assessment approaches

**Output:** `planning/CREDIBILITY_ASSESSMENT_RUBRICS_V1.md`

**Effort:** 8-12 hours

---

### 2. Build Graph Query Toolkit (Priority: High)

**Task:** Write Python/jq scripts to extract key patterns from extraction.json

**Why:** Enables all quantitative approaches

**Output:** `assessment-system/analysis_toolkit.py`

**Effort:** 6-10 hours

---

### 3. Pilot Manual Assessment (Priority: High)

**Task:** Manually assess 1-2 papers using rubrics to validate approach

**Why:** Tests rubric clarity and feasibility before automation

**Output:** `outputs/{paper-id}/assessment/PILOT_SCORECARD.md`

**Effort:** 4-6 hours per paper

---

### 4. Design Scorecard Template (Priority: Medium)

**Task:** Create standardised format for credibility reports

**Why:** Ensures consistency and completeness

**Output:** `assessment-system/templates/scorecard_template.md`

**Effort:** 2-3 hours

---

### 5. Literature Review: Validation Methods (Priority: Medium)

**Task:** Review repliCATS validation methodology and inter-rater reliability best practices

**Why:** Ensures rigorous validation approach

**Output:** `docs/background-research/ASSESSMENT_VALIDATION_METHODS.md`

**Effort:** 4-5 hours

---

### 6. Stakeholder Consultation (Priority: Low-Medium)

**Task:** Discuss assessment approach with 1-2 domain experts

**Why:** Validates that approach will be seen as credible and useful by field

**Output:** Notes on feedback and adjustments

**Effort:** 2-3 hours meetings + revisions

---

## Part 9: Infrastructure Extraction Enhancement (November 2025 Update)

**Date Added:** 3 November 2025

**Status:** Schema defined, awaiting Pass 6 prompt development

### The Gap Identified

During transition planning, analysis of current extractions revealed a **critical gap**: CEM graphs (Passes 0-5) capture *intrinsic research content* (claims, evidence, methods, protocols) but miss *extrinsic reproducibility infrastructure* — the persistent identifiers, data repositories, permits, and FAIR compliance markers that enable transparency assessment.

**Evidence:**
- Infrastructure scans of three papers found **zero genuine reproducibility markers** in extraction.json
- All matches were false positives from metadata fields and consolidation notes
- Transparency and Replicability signals cannot be fully assessed without this infrastructure

### Solution: Pass 6 - Reproducibility Infrastructure Extraction

**Decision:** Insert new Pass 6 (infrastructure extraction) before Pass 7 (comprehensive validation)

**Rationale:**
- Infrastructure is independent of research content relationships
- Can be extracted in parallel with validation workflow
- Directly supports Transparency and Replicability signal assessment

**New workflow:**
```
Pass 0: Section identification + planning
Pass 1: Evidence extraction
Pass 2: Claims extraction + rationalization
Pass 3: Methods extraction
Pass 4: Protocols extraction
Pass 5: Research designs extraction
Pass 6: Infrastructure extraction ← NEW
Pass 7: Comprehensive validation (relationships + infrastructure)
```

---

### Comprehensive Schema Design (v2.0)

**Complete specification:** `planning/REPRODUCIBILITY_INFRASTRUCTURE_SCHEMA.md`

**Background research:** `docs/background-research/FAIR_and_PIDs_for_HASS_reproducibility.md`

#### 13 Infrastructure Sections

1. **Persistent Identifiers (PIDs)** ← Major addition
   - Paper DOI
   - Author ORCIDs (with coverage tracking: none/corresponding/partial/all)
   - Dataset PIDs (DOIs, accession numbers)
   - Software PIDs (Zenodo, Software Heritage, GitHub)
   - Sample PIDs (IGSN for physical samples - archaeology/palaeoecology)
   - Project PIDs (RAiD for research activities - emerging 2025-2028)
   - Vocabulary PIDs (controlled vocabularies, gazetteers: PeriodO, Pleiades, AAT)
   - **PID graph connectivity score** (0-6 scale measuring research object interconnection)

2. **Funding**
   - Funder name, grant number, recipients
   - Structured metadata: ROR, funder jurisdiction
   - Verbatim acknowledgement text with location

3. **Data Availability**
   - Repository type (domain-specific, institutional, general)
   - Persistent identifiers (DOI, accession, URL)
   - Access conditions (open, restricted, embargoed, closed)
   - Licence (CC-BY, CC0, etc.)
   - Machine-readable format assessment (API, structured export vs PDF)
   - Ethical considerations (CARE principles, Indigenous data sovereignty)

4. **Code Availability**
   - Repository type (GitHub, GitLab, Zenodo)
   - Persistent identifier (DOI for archived snapshots)
   - Executable assessment (dependencies documented, environment specified)
   - Archived snapshot vs live repository
   - Licence (MIT, Apache, GPL, etc.)
   - Software tools used (GIS, statistical packages, domain tools)

5. **Author Contributions**
   - Format (CReDIT taxonomy, narrative, equal contribution)
   - Parsed contributions by CReDIT role if structured
   - Cross-reference with ORCIDs

6. **Conflicts of Interest**
   - Declaration type (none declared, conflicts declared, not stated)
   - Specific conflicts if present

7. **Ethics Approval**
   - Institutional ethics committee approval
   - Community consent (Indigenous research agreements)
   - Informed consent status
   - CARE principles applied (Boolean)
   - Approval numbers and jurisdictions

8. **Permits and Authorisations** ← Major addition (fieldwork-specific)
   - Excavation permits (archaeological/palaeontological)
   - Land access agreements (Traditional Owner permissions, private land)
   - Sampling permits (protected areas, national parks)
   - Heritage consents (work near/on heritage sites)
   - Export/import permits (CITES, biosecurity)
   - Collection permits (museum/repository access)
   - Diving permits (underwater archaeology)
   - 10 permit types defined with CARE principle integration

9. **Preregistration**
   - Preregistration present (Boolean)
   - Registered report (Boolean)
   - Registration platform links (OSF, AsPredicted, clinicaltrials.gov)
   - **Note:** Rare in HASS archaeology/palaeoecology (exploratory/inductive research)

10. **Supplementary Materials**
    - Type (document, data, code, video, interactive)
    - Format (PDF, CSV, XLSX, R, Python)
    - Persistent identifier if present
    - Machine-readable assessment

11. **References Completeness**
    - In-text citations count vs bibliography entries
    - Missing references identified
    - **Note:** May be difficult to assess; consider low priority

12. **FAIR Assessment** ← Major addition
    - Structured scoring (0-4 per dimension):
      - **Findable** (PIDs present, metadata rich, registered in repositories)
      - **Accessible** (PIDs resolve, protocols open, metadata persistent)
      - **Interoperable** (structured formats, controlled vocabularies, typed relationships)
      - **Reusable** (clear licence, provenance documented, community standards)
    - Total score 0-16 with rating scale:
      - 0-4: Not FAIR
      - 5-8: Minimally FAIR
      - 9-12: Moderately FAIR
      - 13-16: Highly FAIR
    - Machine-actionability assessment (critical distinction from "available")
    - PID graph completeness evaluation
    - Context-dependent assessment (publication year, discipline, research type)
    - CARE-compliant restrictions marked as POSITIVE signal
    - Recommendations for improvement

13. **Extraction Metadata**
    - Sections examined
    - Validation performed
    - Schema version (2.0)

---

### FAIR Principles Integration

**Foundation:** GO-FAIR 15 principles emphasise **machine-actionability** — computational systems must be able to find, access, interoperate with, and reuse data with minimal human intervention.

**Critical distinction:** "Available" ≠ FAIR
- ❌ PDF supplementary materials with tables as images
- ❌ "Data available upon request"
- ❌ URLs without PIDs (link rot)
- ✅ Dataset with DOI + machine-readable metadata (JSON-LD)
- ✅ Data in structured format (CSV, NetCDF) with documented schema
- ✅ API access for programmatic retrieval

**HASS Context:**
- ORCID adoption: 91-93% (natural sciences) vs 17-24% (humanities)
- Timeline: FAIR principles published 2016; expect adoption 2020+
- Assessment adjusted by publication year and discipline baseline
- Restricted access with ethical justification = POSITIVE FAIR signal (A1.2 + CARE)

**PID Systems Status (2024-2025):**
- **DOI:** 391 million registrations (2025); universal for papers, growing for datasets/software
- **ORCID:** US federal requirement by end 2025; patchy HASS adoption
- **RAiD:** Pilot phase (Europe, US, Finland, Australia); launch 2025-2028
- **IGSN:** Rebranded to International Generic Sample Number; explicitly includes archaeology; very low current adoption but emerging interest

---

### Direct Enhancement of repliCATS Signals

| Signal | Infrastructure Support | Schema Fields |
|--------|----------------------|---------------|
| **Transparency** | **PRIMARY** (direct measurement) | All fields; especially PIDs, data/code availability, funding, permits, author contributions |
| **Replicability (Analytic)** | **PRIMARY** (direct measurement) | Code availability + executable environment + data PIDs + software version PIDs |
| **Validity** | **MODERATE** (supporting evidence) | Sample PIDs (traceability), ethics approval (procedural), permits (regulatory) |
| **Robustness** | **MODERATE** (supporting evidence) | Supplementary materials DOIs, sensitivity analyses archived |
| **Generalisability** | **MINIMAL** (enables reanalysis) | Data availability enables testing in new contexts |
| **Comprehensibility** | **MINIMAL** (metadata richness) | Rich metadata (FAIR R1) supports understanding |
| **Plausibility** | **MINIMAL** (vocabulary support) | Vocabulary PIDs aid checks (standardised terminology) |

**Transparency signal enhancement formula:**

**Transparency = Intrinsic Transparency (RDMAP) + Extrinsic Transparency (Infrastructure)**

| Intrinsic | Infrastructure | Overall Transparency |
|-----------|----------------|---------------------|
| High | High FAIR (13-16) | **EXEMPLARY** |
| High | Moderate FAIR (9-12) | **GOOD** |
| High | Low FAIR (5-8) | **MODERATE** (well-documented but not FAIR) |
| Low | High FAIR (13-16) | **MODERATE** (FAIR but opaque) |
| Low | Low FAIR (0-8) | **POOR** |

**Replicability Infrastructure Score (RIS)** — new quantitative metric:
```
RIS = presence + verification of:
  - Data repository links (0-30 points)
  - Code repository links (0-20 points)
  - Protocol documentation (0-20 points)
  - Workflow specifications (0-15 points)
  - FAIR/CARE compliance (0-15 points)

Interpretation:
- RIS < 30: Minimal replicability
- RIS 30-60: Partial replicability
- RIS 60-85: Good replicability
- RIS > 85: Excellent replicability
```

---

### Updated Quantitative Credibility Metrics (Approach C)

**Original five metrics** remain:
1. Evidential Support Density (ESD)
2. Transparency Completeness Index (TCI)
3. Scope Constraint Score (SCS)
4. Robustness Triangulation Index (RTI)
5. Replicability Infrastructure Score (RIS)

**New infrastructure-derived metrics:**
6. **PID Graph Connectivity Score (PGCS)** — 0-6 scale
   - +1 for paper DOI
   - +1 for authors with ORCIDs (any)
   - +1 for dataset PIDs
   - +1 for software PIDs
   - +1 for sample PIDs
   - +1 for project PID or vocabulary PIDs

7. **FAIR Compliance Score (FCS)** — 0-16 scale
   - Findable: 0-4
   - Accessible: 0-4
   - Interoperable: 0-4
   - Reusable: 0-4

8. **Machine-Actionability Index (MAI)** — Boolean + qualitative
   - Machine-readable metadata present
   - Structured data format (not PDF)
   - API access available
   - Typed relationships documented
   - Rating: none / low / moderate / high

---

### Implementation Status

**Completed:**
- ✅ Infrastructure scans (Connor et al 2013, Eftimoski et al 2017, Penske et al 2023)
- ✅ FAIR principles research (GO-FAIR, WorldFAIR, PID systems)
- ✅ Background research report (28 pages documenting FAIR framework, PID adoption, assessment methods)
- ✅ Schema v2.0 complete (13 sections, 13,000+ lines)
- ✅ Permits addition (fieldwork-specific, CARE-integrated)
- ✅ FAIR assessment framework (4D scoring, machine-actionability, PID graph)

**Pending:**
- ⏳ User confirmation of schema scope and assessment depth
- ⏳ Pass 6 prompt development (infrastructure extraction with lightweight self-validation)
- ⏳ Test Pass 6 on Penske et al 2023 (most recent paper, likely best infrastructure)
- ⏳ Schema validation and refinement
- ⏳ Batch extraction: Run Pass 6 on all 10 pilot papers
- ⏳ Update WORKFLOW.md to document Pass 6
- ⏳ Enhance Pass 7 validation to include infrastructure checks

**Timeline estimate:** 1-2 weeks to complete Pass 6 development and pilot testing; 1 week for batch extraction of 10 papers

---

### Critical Design Decisions

#### 1. FAIR Assessment Depth

**Options:**
- **A (Lightweight):** Extract PIDs, note presence/absence, basic FAIR score in Pass 6
- **B (Detailed):** Full 4D FAIR assessment with rationale in Pass 6
- **C (Deferred):** Extract infrastructure in Pass 6, assess FAIR in Pass 7 validation

**Recommendation:** Option A — lightweight in Pass 6, detailed in Pass 7
- Keeps Pass 6 focused and fast (5-10 minutes per paper)
- Pass 7 validation can add depth (link resolution, API checks)
- Separation of concerns: extraction vs assessment

#### 2. PID Verification Approach

**Options:**
- **A (Immediate):** Extract + verify resolution in Pass 6
- **B (Deferred):** Extract in Pass 6, verify in Pass 7
- **C (Automated):** Extract in Pass 6, post-processing script verifies in batch

**Recommendation:** Option C — separation with automated batch verification
- Pass 6 remains extraction-focused
- Batch verification more efficient (single API call per paper)
- Enables retry logic for transient failures

#### 3. Assessment Philosophy

**Confirmed approach:**
- **Descriptive + context-dependent normative**
- Adjust expectations by publication year (pre-2016 vs 2020+), discipline (HASS vs natural sciences), research type (exploratory vs confirmatory)
- CARE-compliant restrictions = POSITIVE signal (ethical compliance, not penalty)
- PID graph completeness as key metric (interconnection, not just presence)
- Machine-actionability emphasized over human-readability

#### 4. Permits Integration with CARE Principles

**Rationale:** Permits demonstrate:
- Regulatory compliance (excavation, sampling, export/import)
- Ethical practice (Indigenous agreements, community consent)
- Respect for jurisdictions (protected areas, heritage sites)
- Methodological legitimacy (authorised research)

**CARE Connection:**
- Land access agreements = Authority to Control (A)
- Community research agreements = Collective benefit (C) + Ethics (E)
- Permit documentation = Responsibility (R)

**Transparency benefit:** Proper permitting visible in papers enhances procedural validity and trustworthiness

---

### Integration with Original Analysis Plan

**Original Approach C (Graph-Based Credibility Metrics)** is now **significantly enhanced**:

**Was (original plan):**
- 5 metrics (ESD, TCI, SCS, RTI, RIS)
- Replicability Infrastructure Score estimated from mentions

**Now (with Pass 6 infrastructure):**
- 8 metrics (added PGCS, FCS, MAI)
- Replicability Infrastructure Score **directly measured** from structured extraction
- Transparency Completeness Index **augmented** with funding, permits, contributions
- Machine-actionability **quantified** rather than estimated

**Original Approach D (LLM Multi-Agent Assessment)** is also enhanced:
- Agents can reference structured infrastructure (not just text mentions)
- FAIR scores provide objective baseline for Transparency/Replicability assessment
- PID graph connectivity gives verifiable metric (not just judgment)

---

### Cross-Paper Infrastructure Analysis (Pattern-Based)

**From batch structural assessment (STRUCTURAL_SUMMARY.md):**
- 30% of papers missing ALL relationship mappings (Pass 6 failure) — **will be fixed by renumbering to Pass 7 validation**
- 0% of papers have PID infrastructure in current extractions — **will be fixed by new Pass 6**

**New pattern analysis enabled by Pass 6:**
- PID adoption rates by publication year (temporal trends)
- FAIR score distribution across corpus (field baseline)
- Repository preferences (Zenodo vs domain-specific vs institutional)
- Permit documentation patterns (which countries/regions require explicit permits?)
- ORCID adoption by author position (corresponding vs all authors)
- Machine-actionability gaps (what prevents FAIR compliance?)

---

### Updated Week 1 Action Items

**Original:**
1. Define credibility assessment rubrics
2. Build graph query toolkit
3. Pilot manual assessment

**Now (revised):**
1. **Confirm Pass 6 schema** (scope, FAIR depth, verification approach)
2. **Draft Pass 6 prompt** (infrastructure extraction with self-validation)
3. **Test Pass 6 on Penske et al 2023** (validate schema, refine prompt)
4. Define credibility assessment rubrics (**enhanced with infrastructure metrics**)
5. Build graph query toolkit (**augmented with PID/FAIR extractors**)
6. Pilot manual assessment (**using enhanced rubrics**)

---

### Conclusion of Infrastructure Enhancement

The addition of Pass 6 (Reproducibility Infrastructure) is not scope creep — it's **completing the extraction phase** by capturing the extrinsic markers that enable full Transparency and Replicability assessment.

**Impact:**
- Transparency signal: From partially assessed (RDMAP only) to **fully assessed** (RDMAP + PIDs + FAIR)
- Replicability signal: From anecdotally mentioned to **systematically measured** (RIS + FCS + MAI)
- Cross-paper analysis: From structural patterns to **infrastructure trends** (PID adoption, FAIR compliance, permitting practices)
- Field impact: From extraction to **actionable improvement recommendations** (which infrastructure is missing, how to become more FAIR)

**Alignment with repliCATS:** The repliCATS Seven Signals assumed Transparency and Replicability could be assessed from "paper descriptions." Pass 6 operationalises this by **extracting those descriptions structurally** (not just reading them impressionistically).

**Next milestone:** Pass 6 prompt development and pilot testing (est. 1 week), then batch extraction across 10-paper corpus (est. 1-2 days).

---

## Conclusion: From Extraction Excellence to Assessment Impact

You have built an **exceptional extraction system** that captures the argumentative and procedural structure of research papers with unprecedented detail. The CEM graphs you've created are **precisely what repliCATS assumed would be done manually** - the structured knowledge needed for credibility assessment.

The transition to analysis is not a new project; it's **activating the second half of the system you've designed**. The extraction phase answered "What does the paper say?" The analysis phase answers "How credible is what it says?"

### The Core Insight

**Credibility assessment is not a mystery** - you have:
- ✅ **A proven framework** (repliCATS Seven Signals)
- ✅ **The necessary data** (CEM graphs with all elements)
- ✅ **A clear mapping** (signals → graph features)
- ✅ **Multiple approach options** (qualitative, quantitative, hybrid)

What you need to build is **the bridge** from your CEM graphs to credibility scores. This document proposes:

1. **Five complementary approaches** (rubric-based, pattern-based, metric-based, LLM-assisted, minimal indicators)
2. **A phased implementation plan** (12 weeks to full corpus assessment)
3. **Practical infrastructure** (scripts, templates, workflows)
4. **Clear success metrics** (reliability, validity, actionability)
5. **Risk mitigations** (subjectivity, domain gaps, automation bias)

### Your Immediate Path Forward

**This week:**
- Define detailed rubrics for all seven signals
- Build graph query toolkit for metric extraction
- Pilot assess 1-2 papers manually to validate rubrics

**Next 2-4 weeks:**
- Generate quantitative metrics for full corpus
- Perform deep qualitative assessment on diverse subset
- Compare quantitative and qualitative approaches

**Weeks 5-12:**
- Develop and validate LLM assessment pipeline
- Complete full corpus assessment
- Document methodology and generate comparative analyses

### The Opportunity

You are building something genuinely novel: **Automated, transparent, content-based credibility assessment for HASS research at scale**. The extraction work was hard because it was foundational. The analysis work will be rewarding because it's where the **scientific impact** emerges - moving research evaluation beyond citation counts to **actual epistemic quality**.

The repliCATS team proved this works with human assessors. You're building the system that makes it **scalable, transparent, and practical** for long-tail domains where traditional reproducibility metrics don't apply.

---

**Document Status:** Discussion framework v1.0
**Next Update:** After rubric definition and pilot assessment
**Feedback Welcome:** This is meant to start a conversation, not end it
