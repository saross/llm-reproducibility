# RDMAP Implementation Decisions: Adapting (Pre)Registration Frameworks for Retrospective Fieldwork Assessment

**Date:** 2025-10-19  
**Version:** 1.0  
**Status:** Final blueprint for schema v2.4 and prompt development  
**Purpose:** Document all design decisions for integrating Research Design-Methods-Protocols (RDMAP) extraction into unified schema

---

## Executive Summary

This document captures design decisions for RDMAP schema v2.4 development, drawing on comprehensive review of (pre)registration frameworks while adapting them for retrospective assessment of fieldwork-based research. Key insight: We borrow **patterns and frameworks** from 20+ years of clinical trial and psychology registration refinement, but adapt **terminology and implementation** for retrospective inference in disciplines without registration culture.

**Core challenge:** Adapting prospective registration frameworks (planning done before data) to retrospective assessment (inferring decisions from published papers after the fact) in fieldwork disciplines (archaeology, ethnography, field ecology, structural geology, field linguistics) where registration is uncommon (<10% of papers).

**Solution:** Extract what papers report about research design, methods, and protocols while explicitly tracking:
- What papers claim vs what we can infer
- Temporal sequence of decisions (when hypotheses formed relative to data)
- Completeness gaps (expected information missing)
- Adaptations and opportunistic decisions (fieldwork reality)
- Reasoning approaches (inductive/abductive/deductive)

**Outcome:** Schema v2.4 enables transparent extraction of methodological information to support future credibility assessment without premature quality judgments during extraction phase.

---

## What We Learned from (Pre)Registration Frameworks

### Comprehensive Survey Conducted

Reviewed 15+ major schemas including:
- **OSF Prereg** (psychology/social science standard)
- **CONSORT-SPI 2018** (social/psychological interventions - most applicable to our domains)
- **SPIRIT 2025** (clinical trial protocols)
- **ClinicalTrials.gov** (mature 20+ year registry, 51 database tables)
- **Qualitative Preregistration Template** (48-expert Delphi consensus)
- **Registered Reports** (journal-based pre-acceptance)
- **AsPredicted** (minimalist 9-question approach)
- **protocols.io** (maximum procedural detail, full machine-readable schemas)

### Key Patterns Identified

**1. Three-tier strategic/tactical/operational structure**
- **Strategic:** Research questions, hypotheses, study design, theoretical framework
- **Tactical:** Sampling strategies, data collection approaches, analysis plans
- **Operational:** Step-by-step protocols, equipment specifications, quality controls

**RDMAP adoption:** Validates our Design → Methods → Protocols hierarchy

---

**2. Confirmatory vs exploratory distinction**
- Critical for preventing HARKing (Hypothesizing After Results Known)
- OSF's five-level "existing data taxonomy" operationalizes this
- Separates when decisions made relative to data access

**RDMAP adaptation:** Can't determine registration levels retrospectively, but CAN infer reasoning approach (inductive/abductive/deductive) and hypothesis formulation timing from paper narrative

---

**3. Primary vs secondary outcomes**
- Universal across clinical, economics, education schemas
- Primary = powered for, drive sample size
- Secondary = additional evidence, exploratory

**RDMAP adaptation:** Terminology doesn't fit fieldwork (not "outcomes"), but pattern useful: distinguish planned vs emergent research questions/findings

---

**4. Comprehensive intervention documentation (TIDieR 12 elements)**
- Brief Name, Why (rationale), What (materials), What (procedures), Who Provided, How (mode), Where (setting), When/How Much, Tailoring, Modifications, Fidelity assessment

**RDMAP adaptation:** "Intervention" → "Method Documentation Framework." Elements apply beautifully to excavation, survey, interview methods. Use as expected information checklist.

---

**5. Measurement specification framework (CONSORT-Outcomes 2022)**
- Domain, Instrument, Metric, Aggregation, Time points, Reporter

**RDMAP adoption:** Directly applicable. Provides expected information checklist for any measurement protocol.

---

**6. Analysis population specifications (SPIRIT)**
- ITT (intention-to-treat), Per-protocol, As-treated, Complete case

**RDMAP adaptation:** Fieldwork equivalents: All collected data, Quality-filtered, Outliers excluded, Complete cases only. Critical for transparency about exclusions.

---

**7. Conditional decision rules**
- IF assumptions violated THEN alternative procedure
- Documents planned contingencies and adaptive procedures

**RDMAP adoption:** Perfect for fieldwork serendipity. Capture both planned contingencies and actual opportunistic adaptations.

---

**8. Controlled vocabularies**
- Study designs, sampling strategies, intervention types, masking levels
- Enable comparison and aggregation across studies

**RDMAP adaptation:** Adopt core patterns but build vocabularies empirically for fieldwork contexts. Start with open lists, refine as we process papers.

---

### What Doesn't Transfer

**Registration-specific elements we're NOT adopting:**
- Registration timestamps and unique identifiers
- Deviations from preregistered protocol (papers aren't registered)
- Prospective power calculations (rare in fieldwork)
- Trial registration requirements (FDAAA, ICMJE)
- Ethics approval tracking (different system in our domains)

**Over-complex structures we're avoiding:**
- protocols.io's 26+ step component types (lab-specific)
- ClinicalTrials.gov's 51 database tables (implementation overkill)
- AsPredicted's PDF-only approach (need machine-readable)

---

## Borrowing Patterns vs Implementations

### What We're Borrowing

**Structural patterns:**
- Three-tier hierarchy (strategic/tactical/operational)
- Planned vs actual documentation (protocols vs adaptations)
- Expected information frameworks (comprehensive checklists)
- Conditional decision rules (IF-THEN contingencies)
- Cross-reference structures (hierarchical implementation chains)

**Conceptual frameworks:**
- Confirmatory vs exploratory reasoning (adapted to inductive/abductive/deductive)
- Hypothesis formulation timing (pre-data, post-data)
- Measurement specification (what, how, precision)
- Exclusion transparency (what data removed, why)
- Method documentation completeness (TIDieR elements)

**Controlled vocabularies (adapted):**
- Study design types (adding fieldwork-specific)
- Sampling strategies (probability, purposive, opportunistic)
- Analysis populations (all data → quality-filtered → complete cases)

---

### What We're Adapting

**Terminology changes:**
- "Intervention" → "Method" (fieldwork doesn't intervene)
- "Primary/secondary outcomes" → "Planned/emergent research questions"
- "Exploratory/confirmatory" → "Inductive/abductive/deductive"
- Clinical population terms → Fieldwork equivalents

**Epistemological reframing:**
- Prospective planning → Retrospective inference
- Registration compliance → Methodological transparency
- Hypothesis preregistration → Hypothesis formulation timing
- Protocol deviation → Adaptive procedures and opportunistic decisions

**Uncertainty acknowledgment:**
- Can't know actual temporal sequence, only infer from narrative
- Must track confidence in inferences
- Distinguish explicit statements from implicit assumptions
- Document when information genuinely unclear vs missing

---

## RDMAP Adaptations for Retrospective Assessment

### The Fundamental Challenge

**Registration frameworks assume:**
- Researchers document plans BEFORE data collection/analysis
- Temporal sequence is certain (registration timestamp)
- Deviations from protocol are transparent
- Can distinguish pre-specified from post-hoc analyses

**Retrospective assessment must:**
- Infer what was planned vs opportunistic from published narrative
- Accept uncertainty about decision timing
- Work with incomplete reporting (papers omit details)
- Detect when claimed sequence (hypothesis first) contradicts evidence (pattern appears post-hoc)

**Our approach:** Extract what papers report while explicitly tracking:
1. **What papers claim** (explicit statements)
2. **What we can infer** (from narrative flow, section structure, language)
3. **Our confidence** in inferences (high/medium/low)
4. **What's unclear or missing** (expected information gaps)

---

### Key Adaptations

**1. Reasoning Approach Instead of Registration Status**

**Don't use:** OSF's five-level existing data taxonomy (registration prior to: 1. data creation, 2. observation, 3. access, 4. analysis, 5. preliminary analysis)

**Do use:** Inductive/abductive/deductive reasoning approach with hypothesis formulation timing

**Rationale:** Can't determine registration levels from unregistered papers, but CAN infer reasoning patterns from:
- Whether hypotheses stated before results
- Whether predictions tested or patterns described
- Whether theory guides data collection or emerges from it

---

**2. Planned vs Emergent Research Focus**

**Don't use:** "Primary outcomes" (powered for) vs "Secondary outcomes" (additional)

**Do use:** "Planned research questions" vs "Emergent findings"

**Rationale:** Fieldwork often doesn't have formal power calculations or single primary outcome. But researchers DO have main research focus vs additional discoveries. Can infer from:
- Questions stated in introduction/methods
- "Additional findings" or "unexpected patterns" in discussion
- Whether analysis systematic (planned) or opportunistic (emergent)

---

**3. Method Documentation Framework**

**Don't use:** "Intervention" terminology (TIDieR framework as-is)

**Do use:** Method documentation completeness checklist

**Elements (adapted from TIDieR):**
- **Why:** Rationale for method choice
- **What (materials):** Equipment, tools, platforms, instruments
- **What (procedures):** Step-by-step process
- **Who:** Team composition, training, expertise
- **How:** Mode of execution, approach
- **Where:** Setting, location specifics, spatial context
- **When/How Much:** Duration, frequency, intensity, timing
- **Tailoring:** Adaptation to conditions, contexts, participants
- **Modifications:** Changes during execution
- **Fidelity:** Quality control, adherence monitoring

**Rationale:** These elements are universal for method transparency. Archaeological excavation example:
- Why: Stratigraphic excavation chosen for depositional sequence
- What: Marshalltown trowels, total station, FAIMS mobile
- What: Single-context recording, photography, drawing
- Who: 5-person team, 2 experienced + 3 trained students
- How: Trowel and mattock excavation
- Where: Site X, Units 1-4, north area
- When: 6-week season, 8 hours/day
- Tailoring: Increased sieving in midden contexts
- Modifications: Shifted to shovel-scraping in rocky hardpan
- Fidelity: Daily supervisor review of context sheets

---

**4. Opportunistic Decisions and Adaptations**

**Unique to fieldwork:** Things NEVER go as planned
- Weather prevents access → extend season
- Unexpected feature exposed → expand excavation
- Key informant unavailable → adapt interview schedule
- Equipment failure → switch recording method

**What we need to capture:**
- **Planned contingencies** (if documented): "IF weather prevents access THEN extend season"
- **Actual adaptations** (what happened): "Heavy rains week 3 made site inaccessible; we extended season 4 days"
- **Decision rationale** (why justified): "Needed to complete Unit 2 excavation to maintain stratigraphic integrity"
- **Impact assessment** (consequences): "Maintained systematic coverage; no effect on comparability"

**Critical distinction:**
- **Systematic deviation with justification** = legitimate adaptation
- **Silent changes** = methodological opacity (red flag)

---

**5. Exclusion Transparency**

**Borrow from SPIRIT:** Analysis population specifications

**Adapt for fieldwork:**
- All collected data (equivalent to ITT)
- Quality-filtered data (equivalent to per-protocol)
- Outliers excluded (equivalent to as-treated)
- Complete cases only (no missing data)

**What we extract:**
- "547 features recorded; 523 analyzed after 24 excluded for poor preservation"
- "All interviews transcribed; 3 excluded from coding due to incomplete data"

**Critical for assessment:** Transparency about what data was removed and why. Basis for detecting selective reporting.

---

## Vocabulary Decisions

### 1. Reasoning Approach: Inductive/Abductive/Deductive

**Terms used:**
- **`inductive`** - Pattern-seeking and hypothesis-generating from data
- **`abductive`** - Inference to best explanation with testable implications  
- **`deductive`** - Hypothesis-testing with predictions tested against data
- **`mixed`** - Intentional combination of reasoning modes (not just confused)
- **`unclear`** - Cannot determine from paper

**Rationale:** These are the appropriate terms for fieldwork epistemology, reflecting actual inference patterns rather than just temporal sequence. Registration frameworks use "exploratory/confirmatory" focused on timing; we need richer distinction for retrospective assessment.

**Definitions (for schema self-documentation):**

```
inductive: "Data → patterns → generalizations. Researchers collect data and identify 
patterns to generate new hypotheses. Goal is hypothesis generation, not testing. 
Example: 'We excavated 47 sites and observed ceramic density increases near water 
sources across all periods.'"

abductive: "Observations → inference to best explanation → testable predictions. 
Researchers propose explanatory frameworks that account for observed patterns and 
generate testable implications. Dominant mode in fieldwork. Example: 'Ceramic 
density near water [observation] is best explained by ritual water access practices 
[abduction], which predicts we should find votive deposits and specialized vessel 
forms near springs [testable implications].'"

deductive: "Theory/hypothesis → predictions → empirical test. Researchers state 
hypotheses derived from theory before data collection, then systematically test 
predictions. Example: 'If ritual water access was practiced [hypothesis], then we 
should find [specific predictions]. We test this by [systematic data collection].'"

mixed: "Genuine combination of reasoning modes (not confusion). Research intentionally 
combines inductive exploration, abductive explanation, and deductive testing in 
transparent sequence. Example: 'We inductively identified ceramic-water pattern, 
abductively proposed ritual explanation, then deductively tested predictions about 
votive deposits.'"

unclear: "Cannot determine reasoning approach from paper. May be poor reporting, 
may be genuinely confused methodology."
```

**Extraction guidance:**

**Inductive indicators:**
- "Patterns emerged from the data"
- "We conducted exploratory analysis"
- "We identified trends"
- No a priori predictions stated
- Generates new hypotheses as output

**Abductive indicators:**
- "This pattern is best explained by..."
- "We propose that X accounts for Y"
- Builds explanatory framework from observations
- Generates testable predictions as output
- Theory-building language

**Deductive indicators:**
- "We hypothesized that..."
- "Based on theory X, we predicted..."
- Clear a priori predictions stated in intro/methods
- Systematic testing language
- Hypothesis as input, evidence as test

**Mixed indicators:**
- Explicit combination: "We first explored patterns inductively, then tested..."
- Multi-phase research with different modes at different stages
- NOT just confused—actually combining approaches systematically

**Critical guidance:** Use "mixed" only when paper explicitly combines modes. Default to dominant single mode if unclear. Don't let "mixed" become dumping ground for uncertain classifications.

---

### 2. Research Questions vs Hypotheses

**Distinction matters:** These require different treatment and enable different kinds of science.

**Research Questions:**
- Open-ended inquiries: "What is the distribution of X?" "How do communities Y?"
- Addressed through systematic but exploratory investigation
- Common in qualitative research, surveys, initial studies
- Appropriate for inductive/abductive work
- Generate hypotheses as output

**Hypotheses:**
- Specific, testable predictions: "X will correlate with Y" "Sites will cluster near water"
- Should precede data collection/analysis for deductive testing
- Derived from theory or prior research
- Require systematic testing against evidence
- Falsifiable predictions

**Critical assessment need:** Detecting HARKing (Hypothesizing After Results Known)

**What we must capture:**
1. What papers claim (research questions OR hypotheses)
2. When formulated (pre-data, post-data, unclear)
3. How addressed/tested (systematic investigation, post-hoc pattern matching)
4. Whether emergent findings are honestly labeled or misrepresented as predictions

**Structure captures:**
- Separate arrays for research_questions and hypotheses
- Formulation timing for both
- How hypotheses actually tested (systematic vs post-hoc)
- Emergent findings with explicit framing (unexpected discovery vs claimed prediction)

---

### 3. Study Design Vocabulary

**Approach:** Open list, build empirically

**Starting controlled types:**
- `survey` - Archaeological/ecological survey, not questionnaire
- `excavation` - Archaeological excavation
- `ethnographic` - Ethnographic fieldwork (participant observation, interviews)
- `experimental` - Controlled experiments (rare in fieldwork but exist)
- `comparative` - Cross-site, temporal, regional comparisons
- `longitudinal` - Multi-season, repeated visits over time
- `case_study` - In-depth single case
- `mixed_methods` - Explicit combination of approaches

**Not included (clinical terms that don't apply):**
- "Observational" - Everything in fieldwork is observational
- "Interventional" - Fieldwork doesn't intervene in clinical sense

**Implementation:**
- Free text `design_type` field
- Suggested controlled types list
- Allow expansion as we encounter new patterns
- Use `design_description` for specifics

**Rationale:** Study designs vary widely across archaeology, ethnography, field ecology, structural geology, field linguistics. Can't anticipate all types. Build vocabulary empirically from actual papers.

---

### 4. Sampling Vocabulary

**Approach:** Open list, context-dependent, build empirically

**Challenge:** Sampling varies by:
- **What's sampled:** Survey areas, excavation units, artifacts, interview participants, ecological plots
- **Scale:** Regional, site, unit, object level
- **Discipline:** Survey design in archaeology vs participant recruitment in ethnography

**Starting controlled types:**

**Probability sampling:**
- `simple_random` - Every unit has equal probability
- `stratified_random` - Random within defined strata
- `systematic_random` - Regular intervals with random start
- `cluster` - Random selection of groups

**Non-probability sampling:**
- `purposive` - Deliberate selection for characteristics (multiple subtypes)
- `convenience` - Based on accessibility
- `theoretical` - Based on emerging theory (grounded theory)
- `snowball` - Referral-based recruitment
- `quota` - Fill predetermined categories
- `judgmental` - Expert selection

**Archaeological-specific (examples):**
- `total_collection` - All artifacts collected
- `grab_sample` - Non-systematic sample

**Coverage:**
- `total_coverage` - Complete census
- `census` - All units examined

**Implementation:**
- Free text `sampling_type` field
- Common types list (will expand)
- `sampling_context` field (what was sampled)
- `sampling_rationale` (why this approach)

**Rationale:** Sampling terminology varies across disciplines and contexts. Need flexible structure that can accommodate discipline-specific terms while building toward controlled vocabulary.

**Future priority (LATER):** Systematic review of sampling terminology across fieldwork disciplines to build comprehensive controlled vocabulary and formal ontology (following OBI patterns).

---

### 5. Analysis Population / Exclusions

**Borrow from SPIRIT, adapt terminology:**

**Analysis population types:**
- `all_collected` - All data collected (equivalent to ITT)
- `quality_filtered` - Data meeting quality standards (equivalent to per-protocol)
- `outliers_excluded` - Statistical outliers removed (equivalent to as-treated)
- `complete_cases_only` - Only cases with no missing data

**What we capture:**
- Type of analysis population
- Definition used
- Number excluded (if reported)
- Exclusion criteria
- Justification for exclusions

**Critical for assessment:** Transparency about data removals. Enables detection of:
- Selective reporting (only favorable data)
- Post-hoc exclusions (removing inconvenient cases)
- Appropriate quality control (justified removals)

---

## Schema Mapping: Registration Frameworks → RDMAP

### Sources and Adaptations Table

| Registration Source | Element | RDMAP Location | Adaptation |
|---------------------|---------|----------------|------------|
| OSF 5-level taxonomy | Data knowledge status | research_design.confirmatory_stance | Reframed as reasoning approach inference, not registration level |
| OSF Prereg | Primary/secondary outcomes | research_design.research_framing | Terminology changed to planned/emergent research questions |
| CONSORT-SPI TIDieR | Intervention documentation | method expected information checklist | "Intervention" → "Method," applied broadly to data collection |
| CONSORT-Outcomes 2022 | Measurement specification | protocol expected information checklist | Applied to any measurement/observation protocol |
| ClinicalTrials.gov | Study design controlled vocabulary | research_design.study_design.design_type | Extended with fieldwork designs, open list |
| ClinicalTrials.gov | Masking/blinding | method.blinding (conditional) | For experimental designs only |
| SPIRIT | Analysis population | method.analysis_population | Terminology adapted for fieldwork contexts |
| OSF Prereg | Conditional decision rules | protocol.decision_rules | Extended to capture actual adaptations, not just plans |
| Qualitative Template | Theoretical paradigm | research_design.theoretical_framework | Directly adopted |
| Qualitative Template | Sampling strategies | method.sampling_strategy | Integrated purposive and opportunistic types |
| Qualitative Template | Stopping rules | method.sampling_strategy.stopping_rule | Added data saturation concepts |
| Qualitative Template | Positionality | research_design.positionality | Directly adopted for interpretive research |
| Qualitative Template | Credibility strategies | method.quality_control (conditional) | Adapted to qualitative QC approaches |

---

## Expected Information Framework

### Core Principle

Registration frameworks excel at defining **what should be documented** for transparency and replicability. We adopt these comprehensive checklists as "expected information" - what we look for during extraction, what we flag as missing.

**Critical distinction:** Expected information ≠ Required information
- Papers won't have everything
- Gaps are data points, not failures
- We document what's expected but missing
- Assessment phase evaluates gap severity

---

### Method Documentation Checklist (Adapted from TIDieR)

**For major data collection methods, expect:**

1. **Rationale (Why)**
   - Why this method chosen
   - Theoretical or practical justification
   - Alternatives considered (if any)

2. **Materials (What - physical)**
   - Equipment, tools, instruments
   - Platforms, software
   - Specifications where relevant

3. **Procedures (What - actions)**
   - Step-by-step process
   - Order of operations
   - Decision points

4. **Personnel (Who)**
   - Team composition
   - Training and expertise
   - Roles and responsibilities

5. **Mode (How)**
   - Approach to execution
   - Technique details
   - Quality control during execution

6. **Setting (Where)**
   - Location specifics
   - Environmental context
   - Spatial framework

7. **Schedule (When/How Much)**
   - Duration and timing
   - Frequency and intensity
   - Temporal framework

8. **Tailoring (Adaptation plans)**
   - Planned adaptations to contexts
   - Flexibility built into design
   - Personalization approaches

9. **Modifications (Actual changes)**
   - What changed during execution
   - Why changes were made
   - Impact on comparability

10. **Fidelity (Quality assurance)**
    - How adherence monitored
    - Quality control procedures
    - Validation approaches

**Domain-specific versions:**
- Archaeological survey checklist
- Excavation methods checklist
- Interview/ethnographic methods checklist
- Ecological sampling checklist
- Artifact analysis checklist

*(Detailed domain checklists developed in prompt phase)*

---

### Measurement Specification Checklist (Adapted from CONSORT-Outcomes)

**For measurement and observation protocols, expect:**

1. **Domain**
   - What construct/phenomenon measured
   - Conceptual definition

2. **Instrument**
   - Specific tool, method, or approach
   - Equipment specifications

3. **Metric**
   - How measurement expressed
   - Units and scale

4. **Aggregation**
   - How individual measurements combined
   - Statistical summary method

5. **Time points**
   - When measurements taken
   - Temporal sampling

6. **Reporter/Observer**
   - Who made observations
   - Observer training and expertise

7. **Precision**
   - Measurement error
   - Resolution and accuracy

8. **Quality control**
   - Inter-observer reliability
   - Validation procedures

---

### Sampling Strategy Checklist

**For any sampling approach, expect:**

1. **Sampling type**
   - Probability, purposive, opportunistic, coverage

2. **Target population**
   - What universe being sampled
   - Boundaries and scope

3. **Sampling rationale**
   - Why this approach appropriate
   - How it addresses research questions

4. **Sample size**
   - Planned or target size
   - Actual size achieved

5. **Selection procedure**
   - How units selected
   - Specific selection criteria

6. **Stopping rule**
   - How sample size determined
   - Data saturation, predetermined N, resource constraints

7. **Inclusion/exclusion criteria**
   - What qualifies for inclusion
   - What excluded and why

---

### Analysis Methods Checklist

**For analysis approaches, expect:**

1. **Analytical approach**
   - Overall strategy (statistical, interpretive, comparative)
   - Specific techniques

2. **Software/tools**
   - Programs used
   - Versions where relevant

3. **Analysis population**
   - What data included
   - What excluded

4. **Preprocessing**
   - Data transformations
   - Cleaning procedures

5. **Assumptions**
   - Statistical assumptions checked
   - Interpretive framework stated

6. **Decision rules**
   - How analytical choices made
   - Contingency plans

7. **Quality control**
   - Validation procedures
   - Sensitivity analyses

8. **Multiple comparisons**
   - How handled (if applicable)

---

## Phasing: NOW / SOON / LATER

### NOW Phase (Schema v2.4 + Extraction Prompts)

**Include for extraction quality:**

1. ✅ **Reasoning approach framework**
   - Inductive/abductive/deductive/mixed/unclear
   - Clear definitions in schema
   - Extraction guidance in prompts

2. ✅ **Hypothesis formulation timing**
   - Pre-data, during-data, post-data, unclear
   - Basis for determination
   - Confidence in inference

3. ✅ **Research questions vs hypotheses distinction**
   - Separate tracking
   - Formulation timing
   - How addressed/tested
   - Emergent findings documentation

4. ✅ **Method documentation framework** (adapted TIDieR)
   - Expected information checklist
   - Domain-specific versions
   - Gap documentation

5. ✅ **Measurement specification framework** (adapted CONSORT-Outcomes)
   - Expected information checklist
   - Applied to all measurement protocols

6. ✅ **Controlled vocabularies** (open lists, build empirically)
   - Study designs
   - Sampling strategies
   - Analysis populations

7. ✅ **Exclusion transparency**
   - Analysis populations
   - What excluded and why
   - Justification documentation

8. ✅ **Decision rules and contingency plans**
   - Planned contingencies (IF-THEN)
   - Actual adaptations
   - Rationale and impact

9. ✅ **Opportunistic decisions tracking**
   - Field condition triggers
   - Responses and rationale
   - Impact on comparability

**Rationale:** These enhance extraction by providing:
- Clear categorization frameworks
- Comprehensive expected information checklists
- Systematic capture of fieldwork adaptations
- Structure for detecting methodological issues (HARKing, selective reporting)

**Output:** Schema v2.4 + Pass 1/2/3 prompts

---

### SOON Phase (Initial Assessment Framework)

**Enable basic assessment:**

1. **Method completeness scoring**
   - Does documentation include TIDieR elements?
   - Scale: comprehensive / adequate / minimal / inadequate

2. **Exclusion transparency assessment**
   - Are exclusions reported? Quantified? Justified?
   - Red flags for selective reporting

3. **Adaptation transparency assessment**
   - Are field adaptations documented? Justified?
   - Distinguish legitimate flexibility from methodological sloppiness

4. **Confirmatory/exploratory clarity**
   - Is reasoning approach explicit or inferable?
   - Confidence in classification
   - Flags for potential HARKing

5. **Expected information completeness**
   - What proportion of expected elements present?
   - Critical gaps (assessment blockers) vs nice-to-have

**Rationale:** These require scoring rubrics, decision trees, domain-specific guidance developed after extraction is refined.

**Output:** Assessment prompts and scoring frameworks

---

### LATER Phase (Advanced Assessment)

**Comprehensive quality evaluation:**

1. **Bias risk assessment** (following Cochrane patterns)
2. **Fidelity to protocol** (if protocol exists or can be inferred)
3. **Cross-paper comparison metrics**
4. **Aggregation across studies**
5. **Domain-specific quality standards**

**Rationale:** These require extensive empirical testing, validation studies, domain consensus.

**Output:** Validated assessment protocols

---

## Critical Gaps RDMAP Addresses

The preregistration framework review explicitly identified gaps that **validate our RDMAP scope**:

1. ✅ **"No formal ontology for sampling strategies"**
   - RDMAP building sampling vocabulary empirically
   - Future: Formal OWL ontology following OBI patterns

2. ✅ **"Limited infrastructure for mixed methods preregistration"**
   - RDMAP accommodates via type-specific structures
   - Explicit mixed-methods study design type

3. ✅ **"Minimal formal ontologies for social science methods"**
   - RDMAP developing controlled vocabularies
   - Fieldwork-specific method taxonomies

4. ✅ **"No widely-adopted schema for implementation documentation in field research"**
   - RDMAP's entire focus
   - Adaptation, opportunism, field reality

5. ✅ **"Theory of change and mechanism documentation underdeveloped"**
   - RDMAP captures via theoretical_framework
   - Abductive reasoning framework

**Positioning:** RDMAP as infrastructure advancing transparency, reproducibility, and rigor across fieldwork disciplines.

---

## Domain-Specific Guidance Notes

### Primary Focus: Archaeology

**Rationale:** User expertise, test case availability (Sobotkova et al.), well-developed but under-served domain.

**Archaeological-specific elements:**
- Site designation and coordinates
- Survey methodologies (systematic, opportunistic)
- Excavation approaches (stratigraphic, arbitrary levels, single-context)
- Recording protocols (total station, GPS, photogrammetry)
- Artifact processing chains
- Dating sample selection
- Curation and repository information

**Examples in prompts will emphasize:** Survey design, excavation methods, artifact analysis, site formation processes.

---

### Expansion Domains (Ready for Testing)

**Ethnography:**
- Participant recruitment, informed consent
- Interview protocols and guides
- Recording methods (audio, video, field notes)
- Transcription procedures
- Coding frameworks
- Member checking and validation
- Anonymization procedures
- Community permissions

**Field Ecology:**
- Plot/transect specifications
- Sampling intensity and intervals
- Species identification methods
- Measurement protocols
- Replication structure
- Temporal sampling design
- Environmental variable documentation

**Structural Geology:**
- Outcrop selection criteria
- Measurement protocols (strike/dip, etc.)
- Sample collection procedures
- Scale of observation
- Stereographic projection methods
- Field mapping protocols

**Field Linguistics:**
- Speaker recruitment and selection
- Elicitation protocols
- Recording specifications
- Transcription conventions (IPA)
- Grammatical analysis framework
- Community language documentation standards

---

## Potential Publications List

**Based on RDMAP development, potential contributions to field:**

1. **RDMAP Methodology Paper**
   - "Retrospective Assessment of Methodological Transparency in Fieldwork-Based Research: The RDMAP Framework"
   - Target: *PLOS ONE*, *eLife*, *Royal Society Open Science*

2. **Sampling Strategies Ontology**
   - "A Formal Ontology of Sampling Strategies in Fieldwork Research"
   - Systematic review across archaeology, ethnography, ecology
   - OWL ontology following OBI patterns
   - Target: *Scientific Data*, *Journal of Archaeological Method and Theory*

3. **HARKing Detection in Fieldwork Research**
   - "Distinguishing Hypothesis-Testing from Hypothesis-Generating Research: Patterns and Prevalence in Archaeological Literature"
   - Apply RDMAP extraction at scale
   - Target: *Advances in Archaeological Practice*, *American Antiquity*

4. **Adaptation and Opportunism in Field Research**
   - "Systematic Flexibility: Documenting Adaptive Procedures in Field-Based Science"
   - Transparency framework for field conditions
   - Target: *Field Methods*, *Nature Methods*

5. **Assessment Framework Validation**
   - "Assessing Methodological Transparency: Validation of the RDMAP Framework Across Fieldwork Disciplines"
   - After extensive testing
   - Target: *Meta-Psychology*, *Collabra: Psychology*

6. **Cross-Domain Comparison**
   - "Methodological Transparency Across Fieldwork Sciences: A Comparative Analysis"
   - Archaeology vs Ethnography vs Ecology
   - Target: *Research Synthesis Methods*, *Scientometrics*

---

## Implementation Plan Summary

### Deliverables Status

**✅ COMPLETED (This Chat - 2025-10-19):**
1. ✅ **Implementation Decision Document** - Complete blueprint documenting all design decisions, vocabulary choices, adaptations from (pre)registration frameworks, and expected information checklists
2. ✅ **Schema v2.4** - Complete unified JSON schema (~1000 lines) integrating RDMAP with claims/evidence extraction. Includes:
   - All v2.3 objects (evidence, claims, implicit arguments) with v2.4 enhancements
   - research_design_object with reasoning approach framework, research questions vs hypotheses, confirmatory stance
   - method_object with TIDieR-adapted checklists, sampling strategies, analysis populations, contingency plans
   - protocol_object with procedures, tools, parameters, decision rules, ethics
   - Self-documenting reasoning approach definitions
   - Open vocabularies for study designs and sampling strategies
   - Cross-reference structures across all object types

**NEXT CHAT - Prompt Development:**
3. **Pass 1 Prompt** - Liberal RDMAP extraction (~400 lines)
4. **Pass 2 Prompt** - Rationalization and consolidation (~400 lines)
5. **Pass 3 Validation Prompt** - Cross-reference integrity checks (~200 lines)

**SUBSEQUENT CHAT - Testing & Refinement:**
6. **Test Extraction** - Sobotkova Methods section using all three passes
7. **Refinement** - Iterative improvements based on test results
8. **Integration** - Coordinate with claims/evidence extraction workflow

---

### Key Resources for Crosswalk Documentation

**Add to project crosswalk:**
- This implementation document
- Preregistration framework survey (in project knowledge)
- MDAR Framework (Macleod et al. 2021)
- CONSORT-SPI 2018 (Grant et al.)
- SPIRIT 2025 (Chan et al.)
- Qualitative Preregistration Template (Haven & Van Grootel 2019)
- TIDieR Checklist (Hoffmann et al. 2014)
- CONSORT-Outcomes 2022 (Butcher et al.)

---

## Conclusion

This implementation plan balances:
- **Learning from mature frameworks** (20+ years of clinical trial refinement)
- **Adapting for fieldwork context** (terminology, epistemology, field reality)
- **Retrospective inference reality** (working from published papers, not registrations)
- **Pragmatic complexity** (comprehensive but not overwhelming)
- **Future assessment enablement** (extract now, assess later)

**Core philosophy:** Borrow proven patterns and frameworks while adapting terminology, acknowledging uncertainty, and respecting fieldwork epistemology. Result: Schema and prompts that enable transparent extraction of methodological information to support credible assessment without premature quality judgments.

**Ready for implementation:** Schema v2.4 development can proceed with confidence in design decisions.

---

**Document Status:** Complete blueprint for schema v2.4 and prompt development  
**Version:** 1.0 Final  
**Date:** 2025-10-19  
**Next Step:** Schema v2.4 development