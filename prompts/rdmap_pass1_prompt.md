# RDMAP Extraction Prompt - PASS 1: Liberal Extraction v2.4

**Version:** 2.4 Pass 1  
**Last Updated:** 2025-10-19  
**Workflow Stage:** Pass 1 of 3 - Liberal RDMAP extraction with over-capture strategy

---

## Your Task

Extract Research Design, Methods, and Protocols (RDMAP) from research paper sections. This is **Pass 1: Liberal Extraction** - when uncertain about tier assignment or boundaries, err on the side of inclusion. Pass 2 will consolidate and rationalize.

**Input:** JSON extraction document (schema v2.4)
- May be blank template (starting fresh)
- May be partially populated (if claims/evidence already extracted)

**Your responsibility:** Populate these arrays:
- `research_designs`
- `methods`
- `protocols`

**Leave untouched:**
- `evidence`, `claims`, `implicit_arguments` (extracted separately)
- Any other arrays already populated

**What you're extracting:**
- **Research Designs** - Strategic decisions about WHY research was framed this way
- **Methods** - Tactical approaches about WHAT was done at high level
- **Protocols** - Operational procedures about HOW specifically it was done

**Output:** Same JSON document with RDMAP arrays populated

---

## EXTRACTION PHILOSOPHY FOR PASS 1

**When uncertain about tier assignment, inclusion, or boundaries: INCLUDE IT.**

- Better to over-extract and consolidate later than miss important methodological information
- Preserve granularity - Pass 2 will consolidate appropriately
- Accept 40-50% over-extraction as expected and manageable
- Focus on comprehensive capture, not perfect classification

**You will NOT be penalized for:**
- Extracting too many items (Pass 2 consolidates)
- Being overly granular (Pass 2 lumps related items)
- Including items at multiple tiers when uncertain
- Marking uncertain boundaries

**You WILL be penalized for:**
- Missing important methodological information
- Under-extracting due to uncertainty
- Being too conservative about inclusion

---

## Core Extraction Principles

### 1. Three-Tier Hierarchy: Design → Methods → Protocols

**Research Design (Strategic Level - WHY)**
- Research questions and hypotheses
- Theoretical frameworks guiding interpretation
- Study design choices (survey, excavation, experimental, comparative, etc.)
- Scope definitions (spatial, temporal, thematic boundaries)
- Positionality and reflexivity statements

**Methods (Tactical Level - WHAT)**
- Data collection approaches (how data gathered generally)
- Sampling strategies (how units selected)
- Analysis approaches (how data analyzed broadly)
- Quality control methods (how quality ensured)
- Validation approaches (how findings checked)
- Temporal frameworks (field seasons, duration)

**Protocols (Operational Level - HOW)**
- Specific procedures with step-by-step detail
- Tools and equipment specifications
- Recording standards and formats
- Parameter values and configurations
- Measurement protocols with precision
- Safety and ethics protocols

**Decision Tree for Tier Assignment:**

```
Does this explain WHY research was framed/designed this way?
├─ YES → Research Design
└─ NO → Does this explain WHAT general approach was used?
    ├─ YES → Method
    └─ NO → Does this explain HOW specifically something was done?
        ├─ YES → Protocol
        └─ NO → Likely project context (metadata, not RDMAP)
```

**When uncertain:** Extract at BOTH levels and mark `extraction_notes` with "Tier assignment uncertain - may belong at [alternative tier]"

---

### 2. Description vs Argumentation Boundary

**CRITICAL DISTINCTION:**

**RDMAP objects** = Descriptions of what was done (methodological procedures)
- "We used stratified random sampling"
- "FAIMS Mobile platform was employed"
- "GPS accuracy was ±3cm"
- Reports methodology factually

**Claim objects** = Arguments about why approaches were appropriate (methodological arguments)
- "Stratified random sampling was appropriate because it ensured representation"
- "FAIMS Mobile enabled efficient data capture in field conditions"
- "±3cm GPS accuracy was sufficient for our research questions"
- Justifies or defends methodology

**Pattern Recognition:**

Extract as **RDMAP** if the text reports what was done:
- "We used X"
- "Y approach was employed"
- "Data collected using Z"
- "Protocol followed ABC steps"

Extract as **Claim** (type: methodological_argument) if the text argues appropriateness:
- "X was appropriate for..."
- "Y enabled us to..."
- "Z ensured that..."
- "This approach was chosen because..."

**When statements combine both:** 
- Extract the description as RDMAP object
- Extract the justification as separate claim object
- Link them: RDMAP `justification_claim: "C###"`, Claim `supports_method: "M###"`

**Example:**
"We used stratified random sampling to ensure adequate representation across site types" contains:
- Method: "stratified random sampling" (what was done)
- Claim: "ensured adequate representation across site types" (why it was appropriate)

---

### 3. Reasoning Approach Framework

**Extract both explicit statements AND inferred reasoning approach with confidence.**

**Reasoning Approach Types:**

**Inductive (Pattern → Theory)**
- Observations → patterns → generalizations
- "We identified patterns in the data that suggest..."
- "Repeated instances of X led us to propose..."
- Generates theory from observations
- Common in exploratory, grounded theory research

**Abductive (Anomaly → Best Explanation)**
- Surprising observation → inference to best explanation
- "The unexpected finding of X suggests..."
- "This pattern is best explained by..."
- Generates hypotheses to explain anomalies
- Common in interpretive, theory-building research

**Deductive (Theory → Prediction → Test)**
- Theory → hypothesis → test against data
- "We hypothesized that X would correlate with Y"
- "If theory Z is correct, we expect to observe..."
- Tests predictions from existing theory
- Common in hypothesis-testing research

**Mixed**
- Genuine combination of approaches (NOT a dumping ground)
- Multiple reasoning pathways clearly articulated
- Different phases using different approaches
- Example: "Exploratory analysis revealed patterns (inductive), which we then tested with hypotheses (deductive)"

**Unclear**
- Insufficient information to classify
- Ambiguous or contradictory indicators
- Use only when genuinely uncertain

**What to extract:**
- Explicit statements about reasoning approach
- Inferred approach based on paper structure and language
- Confidence in inference (high/medium/low)
- Linguistic markers and structural patterns supporting inference

**Confidence indicators:**
- **High:** Explicit statement of approach OR very clear structural pattern
- **Medium:** Strong indicators but no explicit statement
- **Low:** Weak or ambiguous indicators

---

### 4. Research Questions vs Hypotheses

**Extract separately and track formulation timing - CRITICAL for HARKing detection.**

**Research Questions:**
- Open-ended questions guiding investigation
- Do not predict specific outcomes
- Common in exploratory research
- Example: "How do mobile platforms affect data quality?"

**Hypotheses:**
- Specific, testable predictions
- Predict relationships or outcomes
- Common in confirmatory research
- Example: "Mobile platforms will reduce recording errors compared to paper methods"

**Formulation Timing (CRITICAL):**

**Pre-data:**
- Stated in introduction or methods before results
- Clear indication formulated before data collection/analysis
- Explicit preregistration statement (rare in unregistered papers)

**Post-data:**
- First appears in results or discussion section
- Appears after presenting findings
- Reframed after seeing patterns

**Unclear:**
- Timing cannot be determined from paper structure
- Ambiguous presentation
- Restructured narrative obscures timing

**How to infer timing from paper structure:**
1. Check introduction/background - hypothesis stated here → likely pre-data
2. Check methods section - hypothesis stated here → likely pre-data
3. Check results section - first mention here → likely post-data
4. Check discussion - formulated here → definitely post-data
5. Look for phrases: "We hypothesized..." (intro) vs "These findings suggest..." (results/discussion)

**Emergent findings:**
- Unexpected patterns or discoveries not anticipated
- Track separately as emergent (not pre-formulated)
- Note if later presented as if anticipated

---

### 5. Expected Information Checklists

**Use these as GUIDES, not REQUIREMENTS. Flag what's missing, don't penalize papers for gaps.**

#### Method Documentation Checklist (Adapted from TIDieR)

For major data collection methods, look for:

1. **Rationale (Why)** - Why this method chosen, theoretical/practical justification
2. **Materials (What - physical)** - Equipment, tools, instruments, platforms, specifications
3. **Procedures (What - actions)** - Step-by-step process, order of operations
4. **Personnel (Who)** - Team composition, training, expertise, roles
5. **Mode (How)** - Approach to execution, technique details
6. **Setting (Where)** - Location specifics, environmental context, spatial framework
7. **Schedule (When/How Much)** - Duration, timing, frequency, intensity
8. **Tailoring (Planned adaptations)** - Built-in flexibility, context-specific modifications
9. **Modifications (Actual changes)** - What changed during execution, why, impact
10. **Fidelity (Quality assurance)** - How adherence monitored, quality control, validation

**Document what's present in method object fields. Flag missing elements in `expected_information_missing`.**

---

#### Measurement Specification Checklist (Adapted from CONSORT-Outcomes)

For measurement and observation protocols, look for:

1. **Domain** - What construct/phenomenon measured, conceptual definition
2. **Instrument** - Specific tool/method/approach, equipment specifications
3. **Metric** - How measurement expressed, units and scale
4. **Aggregation** - How individual measurements combined, statistical summary
5. **Time points** - When measurements taken, temporal sampling
6. **Reporter/Observer** - Who made observations, training and expertise
7. **Precision** - Measurement error, resolution, accuracy specifications
8. **Quality control** - Inter-observer reliability, validation procedures

**Document what's present in protocol object fields. Flag missing elements in `expected_information_missing`.**

---

#### Sampling Strategy Checklist

For any sampling approach, look for:

1. **Sampling type** - Probability/purposive/opportunistic/coverage
2. **Target population** - What universe being sampled, boundaries and scope
3. **Sampling rationale** - Why this approach appropriate, how it addresses research questions
4. **Sample size** - Planned or target size, actual size achieved
5. **Selection procedure** - How units selected, specific criteria
6. **Stopping rule** - How sample size determined (data saturation, predetermined N, resources)
7. **Inclusion/exclusion criteria** - What qualifies, what excluded and why

**Document in method.sampling_strategy. Flag missing elements in `expected_information_missing`.**

---

#### Analysis Methods Checklist

For analysis approaches, look for:

1. **Analytical approach** - Overall strategy, specific techniques
2. **Software/tools** - Programs used, versions where relevant
3. **Analysis population** - What data included/excluded
4. **Preprocessing** - Data transformations, cleaning procedures
5. **Assumptions** - Statistical assumptions checked, interpretive framework
6. **Decision rules** - How analytical choices made, contingency plans
7. **Quality control** - Validation procedures, sensitivity analyses

**Document in method.analytical_approach. Flag missing elements in `expected_information_missing`.**

---

### 6. Controlled Vocabularies (Open Lists)

**These are SUGGESTIONS, not strict requirements. Accept free text and build vocabulary empirically.**

#### Reasoning Approaches (CLOSED list):
- `inductive` - pattern to theory
- `abductive` - anomaly to best explanation
- `deductive` - theory to test
- `mixed` - genuine combination (NOT dumping ground)
- `unclear` - insufficient information

#### Study Designs (OPEN list - starting vocabulary):
- `survey` - systematic examination of area/population
- `excavation` - systematic excavation and recording
- `ethnographic` - participant observation and cultural study
- `experimental` - controlled manipulation and observation
- `comparative` - systematic comparison across cases
- `longitudinal` - repeated observations over time
- `case_study` - in-depth examination of specific case(s)
- `mixed_methods` - integration of multiple approaches
- **Accept free text** - many domain-specific designs

#### Sampling Types (OPEN list - starting vocabulary):

**Probability sampling:**
- `simple_random` - equal probability
- `stratified_random` - random within strata
- `systematic_random` - regular intervals
- `cluster` - random groups

**Non-probability sampling:**
- `purposive` - deliberate selection
- `convenience` - accessibility-based
- `theoretical` - theory-driven (grounded theory)
- `snowball` - referral-based
- `judgmental` - expert selection
- `quota` - predetermined categories

**Archaeological-specific:**
- `total_collection` - all artifacts
- `total_coverage` - complete census
- **Accept free text** - many context-specific strategies

#### Analysis Populations (ADAPTED from SPIRIT):
- `all_collected` - all data collected (equivalent to ITT)
- `quality_filtered` - meeting quality standards
- `outliers_excluded` - statistical outliers removed
- `complete_cases_only` - no missing data

---

### 7. Fieldwork-Specific Guidance

#### Opportunistic Decisions
Fieldwork involves legitimate adaptations to field conditions. Capture systematically:

**What to extract:**
- Field condition triggers (weather, access, discoveries)
- Original plan (what was intended)
- Adaptation made (what was actually done)
- Rationale (why adaptation was necessary)
- Impact on comparability (how it affected results)
- Whether maintained methodological rigor

**Distinction:**
- **Legitimate adaptation:** Transparent, justified, maintains rigor
  - "Heavy rain prevented surface survey; we extended excavation season instead"
- **Methodological opacity:** Silent changes, unexplained deviations
  - "Some data excluded" (no explanation)

**Extract both planned contingencies and actual adaptations.**

---

#### Contingency Plans
IF-THEN decision rules documented in advance:

**Planned contingencies:** "If weather prevents survey, excavation will continue"
**Actual responses:** "Due to heavy rain days 4-7, we extended excavation and shortened survey"

**Extract:**
- Condition triggers
- Planned responses
- Actual responses (if different)
- Rationale for deviations

---

#### Emergent Discoveries
Serendipitous findings that change research scope or direction:

**Examples:**
- Unexpected artifact types prompting new research questions
- Site extent larger than anticipated requiring scope adjustment
- Chance discovery of new site types

**Extract:**
- What was discovered
- How it changed research approach
- New questions or hypotheses generated
- How integrated into overall design

**Distinguish:** Legitimate scientific response to discovery vs HARKing (claiming you predicted it)

---

### 8. Cross-Reference Patterns

**Use simple string ID arrays. Keep references liberal in Pass 1.**

**Research Design cross-references:**
- `enables_methods: ["M003", "M007"]` - which methods implement this design
- `informs_claims: ["C089"]` - which claims this design supports
- `implicit_assumptions: ["IA001"]` - unstated design assumptions

**Method cross-references:**
- `implements_designs: ["RD001"]` - which designs this method realizes
- `realized_through_protocols: ["P011", "P012"]` - which protocols implement this method
- `validated_by_evidence: ["E046"]` - which evidence validates this method
- `justification_claim: "C027"` - claim arguing this method was appropriate
- `implicit_assumptions: ["IA002"]` - unstated methodological assumptions

**Protocol cross-references:**
- `implements_methods: ["M003"]` - which methods this protocol operationalizes
- `produces_evidence: ["E045"]` - which evidence this protocol generated
- `adapted_from: "P010"` - source protocol if this is adaptation

**When uncertain about cross-references in Pass 1:**
- Include potential references with note in `extraction_notes`
- Example: "May implement RD001, verify in Pass 2"
- Pass 2 will validate and finalize

---

### 9. Location Tracking

**Precise location tracking enables verification and assessment.**

Required for all RDMAP objects:
```json
"location": {
  "section": "Methods",
  "page": 5,
  "paragraph": 3,
  "sentence_start": 2,
  "sentence_end": 4
}
```

**Section types:**
- "Abstract", "Introduction", "Methods", "Results", "Discussion", "Conclusion"
- For multi-section papers, be specific: "Methods - Data Collection", "Results - Survey Findings"

---

## Extraction Workflow

### Step 1: Identify Research Designs
- Read introduction and methods for strategic framing
- Look for: research questions, hypotheses, study design, theoretical framework, scope, positionality
- Extract reasoning approach (explicit and inferred)
- Track hypothesis formulation timing

### Step 2: Identify Methods
- Read methods section for tactical approaches
- Look for: data collection, sampling, analysis, quality control, validation, temporal framework
- Apply expected information checklists
- Note opportunistic decisions and contingency plans
- Track exclusions and analysis populations

### Step 3: Identify Protocols
- Read methods for operational detail
- Look for: procedures, tools, parameters, recording standards, precision, safety/ethics
- Apply measurement specification checklist
- Note adaptations and modifications
- Track decision rules and quality control

### Step 4: Cross-Reference
- Link protocols → methods → designs
- Link methods → evidence validation
- Link methods → methodological argument claims
- Link designs/methods → implicit assumptions
- Mark uncertain references for Pass 2

### Step 5: Flag Missing Information
- Apply expected information checklists
- Note gaps in `expected_information_missing` arrays
- Don't penalize papers, just document
- Distinguish critical gaps from nice-to-have

---

## Boundary Cases and Decisions

### When Description and Argumentation are Combined

**Example:** "We used stratified random sampling to ensure adequate representation across site types"

**Extract as:**
1. **Method object:** "Stratified random sampling"
   - `sampling_strategy.type: "stratified_random"`
   - `justification_claim: "C027"`
   
2. **Claim object (C027):** "Stratified sampling ensured adequate representation"
   - `claim_type: "methodological_argument"`
   - `supports_method: "M003"`

---

### When Tier Assignment is Ambiguous

**Example:** "Survey transects spaced at 10m intervals"

Could be:
- **Method:** Sampling strategy (tactical)
- **Protocol:** Specific spacing parameter (operational)

**Pass 1 approach:**
- Extract at BOTH levels if uncertain
- Mark in `extraction_notes`: "Tier assignment uncertain - transect spacing could be method-level sampling strategy OR protocol-level parameter"
- Pass 2 will rationalize

---

### When Reasoning Approach is Mixed

**Example:** "We conducted exploratory analysis to identify patterns (clustering of artifact types by elevation), then tested specific hypotheses about elevation effects on site distribution"

**Extract as:**
- `reasoning_approach: "mixed"`
- `reasoning_details: "Initial inductive pattern identification followed by deductive hypothesis testing"`
- `reasoning_confidence: "high"`

**NOT mixed:** Simply unclear or ambiguous reasoning. Use `unclear` for that.

---

### When Hypothesis Timing is Ambiguous

**Example:** Hypothesis mentioned in introduction but phrasing suggests post-hoc formulation

**Extract as:**
- `formulation_timing: "unclear"`
- `timing_basis: "Stated in introduction but phrasing ('we found that...') suggests post-hoc formulation"`
- `timing_confidence: "low"`
- Note in `extraction_notes` for human review

---

## Examples (Archaeology Focus)

### Example 1: Research Design - Study Design

```json
{
  "design_id": "RD001",
  "design_text": "Comparative assessment of mobile platform (FAIMS) versus traditional paper-based recording for archaeological survey",
  "design_type": "study_design",
  "study_design": {
    "design_type": "comparative",
    "rationale": "Direct comparison enables assessment of mobile platform effectiveness in field conditions",
    "alternatives_considered": ["Single-method study", "Meta-analysis of existing studies"]
  },
  "reasoning_approach": {
    "approach": "mixed",
    "explicit_statement": "Exploratory analysis of usage patterns combined with confirmatory comparison of data quality metrics",
    "inferred_approach": "mixed",
    "reasoning_confidence": "high",
    "indicators": ["Explicitly states exploratory and confirmatory phases", "Introduction presents hypotheses, results show exploratory patterns"]
  },
  "enables_methods": ["M003", "M008", "M015"],
  "expected_information_missing": ["Sample size justification", "Power analysis"],
  "extraction_notes": "Clear comparative design with explicit mixed reasoning approach",
  "extraction_confidence": "high",
  "location": {"section": "Introduction", "page": 2, "paragraph": 4}
}
```

---

### Example 2: Research Design - Research Question vs Hypothesis

```json
{
  "design_id": "RD002",
  "design_text": "Research questions and hypotheses guiding the study",
  "design_type": "research_question",
  "research_questions": [
    {
      "question": "How does mobile platform use affect data recording efficiency in archaeological field survey?",
      "formulation_timing": "pre-data",
      "timing_basis": "Stated in introduction before methods section",
      "timing_confidence": "high",
      "how_addressed": "Measured via recording time per artifact"
    }
  ],
  "hypotheses": [
    {
      "hypothesis": "Mobile platform recording will be faster than paper-based recording",
      "formulation_timing": "pre-data",
      "timing_basis": "Stated in introduction as a priori expectation",
      "timing_confidence": "high",
      "how_tested": "Systematic time measurement comparison between platforms"
    },
    {
      "hypothesis": "Data completeness will correlate with recorder experience",
      "formulation_timing": "post-data",
      "timing_basis": "First mentioned in results section after presenting completeness findings",
      "timing_confidence": "medium",
      "how_tested": "Post-hoc correlation analysis",
      "emergent": true,
      "emergent_notes": "Pattern emerged during exploratory analysis, then tested"
    }
  ],
  "expected_information_missing": [],
  "extraction_notes": "Clear distinction between pre-registered RQ/H and emergent post-hoc hypothesis",
  "extraction_confidence": "high",
  "location": {"section": "Introduction", "page": 3, "paragraph": 2}
}
```

---

### Example 3: Method - Data Collection with Opportunistic Decisions

```json
{
  "method_id": "M008",
  "method_text": "Archaeological pedestrian survey using mobile data collection platform (FAIMS Mobile)",
  "method_type": "data_collection",
  "data_collection_approach": {
    "approach": "survey",
    "domain_specific_type": "pedestrian archaeological survey",
    "rationale": "Enables systematic artifact documentation with structured data capture"
  },
  "temporal_framework": {
    "field_seasons": ["Summer 2019"],
    "duration": "6 weeks",
    "frequency": "Daily survey weather permitting"
  },
  "opportunistic_decisions": [
    {
      "trigger": "Heavy rainfall days 12-14 prevented surface survey",
      "original_plan": "Complete survey of northern transects",
      "adaptation": "Extended survey period by 3 days and prioritized high-density areas",
      "justification": "Maintain planned sample coverage despite weather delays",
      "impact_on_comparability": "Maintained spatial coverage, no methodological impact",
      "maintained_rigor": true
    }
  ],
  "implements_designs": ["RD001"],
  "realized_through_protocols": ["P023", "P024", "P025"],
  "validated_by_evidence": ["E046"],
  "justification_claim": "C027",
  "expected_information_missing": ["Surveyor training details", "Inter-surveyor reliability"],
  "extraction_notes": "Clear opportunistic adaptation with transparent rationale",
  "extraction_confidence": "high",
  "location": {"section": "Methods", "page": 4, "paragraph": 2}
}
```

---

### Example 4: Method - Sampling Strategy

```json
{
  "method_id": "M010",
  "method_text": "Stratified random sampling of survey transects across site zones",
  "method_type": "sampling",
  "sampling_strategy": {
    "type": "stratified_random",
    "target_population": "Total site area of 45 hectares divided into 4 zones based on surface artifact density",
    "rationale": "Ensures proportional representation across zones with different artifact densities",
    "sample_size_planned": "20% of each zone (9 hectares total)",
    "sample_size_actual": "8.7 hectares (19.3% - weather prevented completion of Zone 3)",
    "selection_procedure": "Random selection of 10m x 10m survey units within each zone using random number generator",
    "stopping_rule": "Predetermined sample size based on available field time and crew size",
    "inclusion_criteria": ["Accessible terrain", "Vegetation clearance feasible"],
    "exclusion_criteria": ["Private property without access permission", "Active agricultural fields"]
  },
  "analysis_population": {
    "type": "quality_filtered",
    "definition": "Survey units with >50% surface visibility",
    "n_excluded": 12,
    "exclusion_criteria": ["Dense vegetation obscuring surface", "Heavy erosion"],
    "exclusion_justification": "Cannot assess artifact presence with <50% visibility"
  },
  "implements_designs": ["RD001"],
  "realized_through_protocols": ["P026"],
  "expected_information_missing": ["Power analysis for sample size", "Pilot test results"],
  "extraction_notes": "Comprehensive sampling documentation with clear exclusion transparency",
  "extraction_confidence": "high",
  "location": {"section": "Methods", "page": 5, "paragraph": 1}
}
```

---

### Example 5: Protocol - Tool Specification

```json
{
  "protocol_id": "P023",
  "protocol_text": "FAIMS Mobile v2.6 configured with custom archaeological survey module",
  "protocol_type": "recording",
  "tools": [
    {
      "tool_name": "FAIMS Mobile",
      "tool_type": "software",
      "version": "2.6",
      "configuration": "Custom module with artifact attribute vocabulary, photo linking, GPS integration",
      "specifications": {
        "platform": "Android 7.0+",
        "offline_capable": true,
        "database": "SQLite local storage",
        "sync_method": "Manual sync to server via WiFi"
      }
    },
    {
      "tool_name": "Samsung Galaxy Tab A",
      "tool_type": "equipment",
      "specifications": {
        "screen_size": "10.1 inch",
        "ruggedness": "IP67 rated case",
        "battery_life": "10 hours field use"
      }
    }
  ],
  "recording_standards": {
    "format": "Structured database records with controlled vocabulary",
    "precision": "GPS coordinates to 5 decimal places (±1m)",
    "metadata_captured": ["Timestamp", "Recorder ID", "Weather conditions", "Surface visibility"],
    "quality_checks": ["Required field validation", "Photo linked to record", "GPS coordinate within survey bounds"]
  },
  "implements_methods": ["M008"],
  "produces_evidence": ["E045", "E046"],
  "expected_information_missing": ["Software validation testing", "Data backup procedures"],
  "extraction_notes": "Comprehensive tool specification with recording standards",
  "extraction_confidence": "high",
  "location": {"section": "Methods", "page": 5, "paragraph": 3}
}
```

---

### Example 6: Protocol - Measurement with Decision Rules

```json
{
  "protocol_id": "P027",
  "protocol_text": "GPS coordinate collection protocol with accuracy requirements and decision rules",
  "protocol_type": "measurement",
  "procedure": {
    "steps": [
      "Power on GPS unit and allow satellite acquisition (minimum 4 satellites)",
      "Wait for HDOP <2.0 before recording",
      "Record coordinates at artifact location",
      "If HDOP >2.0 for >5 minutes, flag location for resurvey",
      "Record accuracy estimate with each coordinate"
    ],
    "step_order_critical": true,
    "decision_points": ["HDOP threshold", "Resurvey flag"]
  },
  "parameters": {
    "hdop_threshold": {
      "value": 2.0,
      "unit": "dimensionless",
      "justification": "Ensures ~5m horizontal accuracy adequate for site-level analysis",
      "criticality": "high"
    },
    "satellite_minimum": {
      "value": 4,
      "unit": "count",
      "justification": "Minimum for 3D position fix",
      "criticality": "high"
    }
  },
  "decision_rules": [
    {
      "condition": "HDOP >2.0 for >5 minutes",
      "action_planned": "Flag location, continue survey, resurvey later",
      "action_actual": "Applied as planned for 23 locations, all successfully resurveyed",
      "rationale": "Prevents survey delays while maintaining accuracy requirements"
    }
  ],
  "measurement_specification": {
    "domain": "Spatial location",
    "instrument": "Garmin GPSMAP 64s",
    "metric": "WGS84 decimal degrees",
    "precision": "±3-5m horizontal accuracy at HDOP <2.0",
    "time_points": "Point-in-time at artifact observation",
    "observer": "Survey team member (trained in GPS use)",
    "quality_control": ["HDOP monitoring", "Satellite count check", "Resurvey of flagged points"]
  },
  "implements_methods": ["M008"],
  "produces_evidence": ["E047"],
  "expected_information_missing": ["GPS unit calibration procedures", "Accuracy validation against known points"],
  "extraction_notes": "Excellent protocol specification with clear decision rules and quality control",
  "extraction_confidence": "high",
  "location": {"section": "Methods", "page": 6, "paragraph": 2}
}
```

---

## Output Format

**Return the same JSON document you received, with RDMAP arrays populated:**

```json
{
  "schema_version": "2.4",
  "extraction_timestamp": "ISO 8601",
  "extractor": "Claude Sonnet 4.5",
  
  // These arrays remain unchanged if already populated:
  "evidence": [...],           // Leave untouched
  "claims": [...],             // Leave untouched
  "implicit_arguments": [...], // Leave untouched
  
  "research_designs": [research_design_object],  // Your work
  "methods": [method_object],                    // Your work
  "protocols": [protocol_object],                // Your work
  
  "extraction_notes": {
    "pass": 1,
    "section_extracted": "string",
    "extraction_strategy": "Liberal extraction with over-capture",
    "known_uncertainties": ["string"],
    "items_needing_pass2_review": ["RD###", "M###", "P###"]
  }
}
```

---

## Quality Checklist for Pass 1

Before finalizing extraction:

- [ ] All research designs extracted (questions, hypotheses, study design, framework, scope, positionality)?
- [ ] All major methods extracted (data collection, sampling, analysis, QC, validation)?
- [ ] All documented protocols extracted (procedures, tools, parameters, standards)?
- [ ] Reasoning approach classified with confidence?
- [ ] Hypothesis formulation timing inferred?
- [ ] Expected information checklists applied?
- [ ] Opportunistic decisions and contingency plans captured?
- [ ] Cross-references marked (even if tentative)?
- [ ] Location tracking complete and accurate?
- [ ] Missing information flagged appropriately?
- [ ] Uncertain items marked in extraction_notes?
- [ ] Other arrays (claims/evidence) left unchanged?

---

## Remember

**Pass 1 is about COMPREHENSIVE CAPTURE, not perfect classification.**

- Over-extract rather than under-extract
- Preserve granularity
- Mark uncertainties
- Let Pass 2 consolidate and rationalize
- **Don't touch claims/evidence arrays** - those are extracted separately

**Your goal:** Ensure nothing important is missed. Pass 2 will refine.