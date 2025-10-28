# Implementation Plan: Restoring Implicit RDMAP Extraction

**Problem:** Implicit RDMAP items are not being extracted (0 items consistently across multiple runs)
**Root Cause:** Workflow non-integration - implicit RDMAP scanning is not part of main extraction workflow
**Solution:** Mirror the successful implicit argument extraction structure for implicit RDMAP

**Related Analysis:** `planning/implicit-extraction-comparison-analysis.md`

---

## Implementation Priority

### Phase 1: Immediate Fixes (Before Next Extraction Run)

These fixes are critical and must be implemented before running another extraction:

1. **Fix 1:** Integrate implicit RDMAP into main workflow (Phase A/B structure)
2. **Fix 2:** Add explicit iteration instructions
3. **Fix 5:** Elevate priority level (HIGH-PRIORITY marker)
4. **Fix 8:** Add worked example

**Estimated time:** 2-3 hours
**Impact:** Should restore implicit RDMAP extraction capability

### Phase 2: Medium-Term Improvements

Implement after validating Phase 1 works:

5. **Fix 3:** Replace checkbox with quality gate
6. **Fix 4:** Reframe from transparency to content
7. **Fix 6:** Move recognition patterns to main prompt

**Estimated time:** 1-2 hours
**Impact:** Reinforces and strengthens Phase 1 changes

### Phase 3: Long-Term Enhancements

8. **Fix 7:** Add mid-section checkpoints with ratios

**Estimated time:** 1 hour
**Impact:** Process monitoring and self-correction

---

## Fix 1: Integrate Implicit RDMAP into Main Workflow

**File:** `extraction-system/prompts/03-rdmap_pass1_prompt.md`

### Step 1.1: Restructure Research Designs Extraction (Lines ~255-287)

**Current structure:**
```markdown
### Step 1: Identify Research Designs
- Scan Abstract, Introduction, Background, and Methods/Approach sections systematically. RDs appear where they appear - don't prioritize sections.

**Scan for design language:**
- Decision: "chose," "selected," "opted for," "decision to"
- Rationale: "because," "rationale," "reasoning"
[... 8 more bullet points ...]
- Determine explicit vs implicit status
- Populate verbatim_quote OR trigger_text appropriately
- **Liberal extraction:** Include "high-level" design elements - critical for transparency assessment
```

**Replace with:**
```markdown
### Step 1: Identify Research Designs

**Phase A: Extract Explicit Research Designs**

Scan Abstract, Introduction, Background, and Methods/Approach sections for documented strategic decisions:

**Look for design language:**
- Decision markers: "chose," "selected," "opted for," "decision to"
- Rationale markers: "because," "rationale," "reasoning"
- Purpose markers: "aimed to," "sought to," "designed to"
- Framework markers: "framework," "guided by," "informed by"
- Comparison markers: "compared," "evaluated," "tested whether"

**For each explicit design found:**
- Extract complete strategic decision with rationale
- Set `design_status = "explicit"`
- Extract `verbatim_quote` from paper
- Classify reasoning approach for each
- Extract theoretical frameworks as Research Designs
- Include meta-level framing (comparative evaluation, case study rationale, etc.)

⚠️ **Literature Review Warning:** Don't extract designs from descriptions of PRIOR work. If verbatim quote says "Smith et al. employed..." → Not current paper's design.

---

**Phase B: Scan for Implicit Research Designs (REQUIRED)**

After extracting explicit designs, systematically scan for implicit designs using 4-pattern recognition:

**For EACH major section (Abstract, Introduction, Methods, Results, Discussion):**

Run systematic 4-pattern implicit design scan:

1. **Pattern 1 - Mentioned Strategic Decision:**
   - Question: "Are strategic decisions or frameworks referenced but not explained?"
   - Look for: Framework names without rationale, approaches mentioned without justification
   - Example: "We employed comparative methodology" without stating WHY or comparison criteria
   - If found: Extract as implicit design with `design_status = "implicit"`

2. **Pattern 2 - Effects Implying Design Causes:**
   - Question: "Do outcomes or comparisons suggest design choices?"
   - Look for: Systematic comparisons throughout paper but design objective never stated
   - Example: Paper compares approach to ML alternatives throughout Discussion, but Introduction doesn't state this as design goal
   - If found: Extract as implicit design (comparative design choice inferred from systematic comparison)

3. **Pattern 3 - Frameworks Referenced Without Specification:**
   - Question: "Are theoretical frameworks or methodological traditions referenced but not described?"
   - Look for: "Building on previous work," "Following established approaches" without specifying what
   - Example: "Following GIS best practices" without identifying which practices or standards
   - If found: Extract as implicit design (methodological positioning without specification)

4. **Pattern 4 - Strategic Positioning Without Explicit Statement:**
   - Question: "Does paper position study relative to alternatives without stating this as design objective?"
   - Look for: Discussion positioning (efficiency thresholds, scalability boundaries, comparison baselines) without design rationale in Methods
   - Example: Paper establishes "optimal range of 10,000-60,000 features" but doesn't state threshold determination was a design objective
   - If found: Extract as implicit design (strategic boundary investigation inferred from analysis focus)

**For each implicit design found:**
- Extract `trigger_text` array (verbatim passages from paper that together imply design choice)
- Record `trigger_locations` (parallel array with location of each trigger passage)
- Set `design_status = "implicit"`
- Write `inference_reasoning` (explain how triggers imply this strategic decision)
- Populate `implicit_metadata`:
  - `basis`: "mentioned_undocumented" (referenced without rationale) OR "inferred_from_results" (implied by systematic analysis)
  - `transparency_gap`: What design information is missing (rationale, decision criteria, alternatives considered)
  - `assessability_impact`: How missing design documentation affects assessment (e.g., "Cannot assess whether comparative framing was pre-planned or post-hoc")
  - `reconstruction_confidence`: "low" | "medium" | "high" based on strength of inference

**Quality checkpoint:**
- [ ] Completed 4-pattern scan for EACH major section
- [ ] Documented implicit design scan in extraction_notes
- [ ] If zero implicit designs found: Documented in extraction_notes why (e.g., "All strategic decisions explicitly documented in Introduction and Methods with clear rationale")

⚠️ **If you find zero implicit designs after systematic scan:** This is unusual. Most papers have 1-3 implicit designs (strategic choices apparent from analysis but not stated as objectives). Document your scan methodology to demonstrate thorough searching.
```

---

### Step 1.2: Restructure Methods Extraction (Lines ~288-296)

**Current structure:**
```markdown
### Step 2: Identify Methods
- Look for data collection approaches
- Extract sampling strategies
- Identify analysis methods
- Note quality control and validation approaches
- Determine explicit vs implicit status for each method
- Populate verbatim_quote OR trigger_text + implicit_metadata
- Document expected missing information
- **When uncertain about tier or inclusion: INCLUDE IT**
```

**Replace with:**
```markdown
### Step 2: Identify Methods

**Phase A: Extract Explicit Methods**

Scan Methods/Approach section for documented tactical approaches:

**Look for method types:**
- Data collection approaches (recording, measurement, observation)
- Sampling strategies (systematic, random, purposive, stratified)
- Analysis methods (statistical tests, qualitative coding, spatial analysis)
- Quality control approaches (validation, verification, cross-checking)

**For each explicit method found:**
- Extract high-level approach with context
- Set `method_status = "explicit"`
- Extract `verbatim_quote` from Methods section
- Document expected missing information

---

**Phase B: Scan for Implicit Methods (REQUIRED)**

After extracting explicit methods, systematically scan for implicit methods using 4-pattern recognition:

**For EACH major section (Methods, Results, Discussion):**

Run systematic 4-pattern implicit method scan:

1. **Pattern 1 - Mentioned Procedure Without Description:**
   - Question: "Are methods named but procedures not described?"
   - Look for verbs: "cleaned," "validated," "checked," "filtered," "normalised," "corrected," "adjusted"
   - Example: "Data were cleaned prior to analysis" but no cleaning procedure described
   - If found: Extract as implicit method (mentioned_undocumented)

2. **Pattern 2 - Effects Implying Methodological Causes:**
   - Question: "Do results reveal methods not documented in Methods section?"
   - Look for: Error rates → QA method, accuracy metrics → validation method, threshold detection → monitoring method
   - Example: "Error rate of 5% was detected" but no error detection method described
   - If found: Extract as implicit method (inferred_from_results)

3. **Pattern 3 - Undocumented Quality Control:**
   - Question: "Are quality control activities mentioned without methods?"
   - Look for: "quality-checked," "validated against," "verified accuracy," "cross-referenced"
   - Example: "We validated digitised features against source maps" but no validation procedure described
   - If found: Extract as implicit method (quality control mentioned but undocumented)

4. **Pattern 4 - Analytical Steps Without Documentation:**
   - Question: "Do Results or Discussion reveal analytical steps not in Methods?"
   - Look for: Comparisons calculated, thresholds determined, subsets analysed, adjustments made
   - Example: Discussion calculates "payoff threshold of 3,400-4,300 features" but Methods doesn't describe threshold calculation methodology
   - If found: Extract as implicit method (analytical approach inferred from outcomes)

**For each implicit method found:**
- Extract `trigger_text` array (verbatim passages mentioning method)
- Record `trigger_locations` (location of each trigger passage)
- Set `method_status = "implicit"`
- Write `inference_reasoning` (explain how triggers imply method existed)
- Populate `implicit_metadata` (basis, transparency_gap, assessability_impact, reconstruction_confidence)

**Quality checkpoint:**
- [ ] Completed 4-pattern scan for Methods, Results, Discussion sections
- [ ] If zero implicit methods found: Documented why in extraction_notes

⚠️ **Most papers have 3-8 implicit methods** - procedures mentioned in Results/Discussion but not documented in Methods. Finding zero suggests incomplete scanning.
```

---

### Step 1.3: Restructure Protocols Extraction (Lines ~297-306)

**Current structure:**
```markdown
### Step 3: Identify Protocols
- Find specific procedures with implementation detail
- Extract tool specifications and configurations
- Capture parameter settings and values
- Document recording standards and decision rules
- Note measurement protocols
- Determine explicit vs implicit status for each protocol
- Populate verbatim_quote OR trigger_text + implicit_metadata
- **When uncertain: INCLUDE IT**
```

**Replace with:**
```markdown
### Step 3: Identify Protocols

**Phase A: Extract Explicit Protocols**

Scan Methods/Approach section for documented operational procedures:

**Look for protocol types:**
- Specific procedures with implementation steps
- Tool specifications (equipment models, software versions, configurations)
- Parameter settings (thresholds, tolerances, measurement units)
- Recording standards (data formats, precision levels, naming conventions)
- Decision rules (when to include/exclude, how to categorise, stopping criteria)

**For each explicit protocol found:**
- Extract detailed procedure with parameters
- Set `protocol_status = "explicit"`
- Extract `verbatim_quote` from Methods section
- Document expected missing information (parameter justifications, tool specifications, etc.)

---

**Phase B: Scan for Implicit Protocols (REQUIRED)**

After extracting explicit protocols, systematically scan for implicit protocols using 4-pattern recognition:

**For EACH major section (Methods, Results, Discussion):**

Run systematic 4-pattern implicit protocol scan:

1. **Pattern 1 - Mentioned Implementation Without Details:**
   - Question: "Are specific procedures mentioned without implementation details?"
   - Look for: "Students were assigned maps," "Coordinates were recorded," "Features were digitised"
   - Example: "Students assigned specific map tiles" but assignment procedure not described
   - If found: Extract as implicit protocol (task mentioned, procedure undocumented)

2. **Pattern 2 - Effects Implying Operational Protocols:**
   - Question: "Do results reveal operational thresholds or procedures?"
   - Look for: Performance limits detected, load thresholds observed, timing patterns reported
   - Example: "Performance degraded after ~2,500 records per device" implies monitoring protocol
   - If found: Extract as implicit protocol (monitoring/detection implied by threshold knowledge)

3. **Pattern 3 - Tool/Equipment Mentioned Without Specifications:**
   - Question: "Are tools named without specifications or configuration details?"
   - Look for: "GPS units used," "Mobile devices deployed," "Software customised"
   - Example: "GPS coordinates recorded" but no GPS model, accuracy specs, or configuration described
   - If found: Extract as implicit protocol (equipment mentioned, specs undocumented)

4. **Pattern 4 - Undocumented Data Processing:**
   - Question: "Are data processing or quality control steps mentioned?"
   - Look for: "corrected," "post-processed," "synchronised," "exported," "converted"
   - Example: "Data were exported to GIS format" but export procedure and format specifications not described
   - If found: Extract as implicit protocol (processing step mentioned, procedure undocumented)

**For each implicit protocol found:**
- Extract `trigger_text` array (verbatim passages mentioning protocol)
- Record `trigger_locations` (location of each trigger passage)
- Set `protocol_status = "implicit"`
- Write `inference_reasoning` (explain how triggers imply protocol existed)
- Populate `implicit_metadata` (basis, transparency_gap, assessability_impact, reconstruction_confidence)

**Quality checkpoint:**
- [ ] Completed 4-pattern scan for Methods, Results, Discussion sections
- [ ] If zero implicit protocols found: Documented why in extraction_notes

⚠️ **Most papers have 8-15 implicit protocols** - specific procedures mentioned but not documented. Results sections often reveal operational details (assignments, thresholds, processing steps) not in Methods. Finding zero suggests incomplete scanning.
```

---

## Fix 2: Add Explicit Iteration Instructions

**File:** `extraction-system/prompts/03-rdmap_pass1_prompt.md`

### Step 2.1: Add Section-Level Iteration Reminder

**Location:** After Step 3 (Protocols), before Step 4 (Cross-Reference) - approximately line 307

**Insert:**
```markdown

---

### Critical Reminder: Implicit RDMAP Extraction

**Between extracting explicit and implicit RDMAP for each step above:**

You must systematically scan EACH major section using the 4-pattern recognition checklist.

**Systematic scanning means:**
- ✅ Read through Results section looking for verb phrases ("cleaned," "assigned," "monitored")
- ✅ Read through Discussion looking for procedure mentions ("quality-checked," "validated")
- ✅ Read through Results looking for operational details (thresholds, assignments, processing steps)
- ✅ Document your scan in extraction_notes if finding no implicit items in a section

**Do NOT:**
- ❌ Assume "if it's not in Methods section, it doesn't exist"
- ❌ Skip sections because they "don't usually have methods"
- ❌ Mark all items as "explicit" without considering implicit items

**Expected outcome:** 20-40% of RDMAP items are typically implicit. If you find zero implicit items across all sections, document your systematic scan methodology in extraction_notes to demonstrate thorough searching.

---
```

---

## Fix 5: Elevate Priority Level

**File:** `extraction-system/prompts/03-rdmap_pass1_prompt.md`

### Step 5.1: Add HIGH-PRIORITY Section

**Location:** After "Your Task" section (line 10-34), before "🚨 CRITICAL: Verbatim Quote Requirements"

**Insert:**
```markdown

---

## 🚨 HIGH-PRIORITY: Extract Both Explicit AND Implicit RDMAP

**This pass extracts TWO equally important types of RDMAP:**

1. **Explicit RDMAP (documented)** - Strategic decisions, methods, and protocols documented in Methods section with procedural details
   - Source: Methods/Approach section
   - Required: `verbatim_quote` field
   - Status: `*_status = "explicit"`

2. **Implicit RDMAP (undocumented)** - Strategic decisions, methods, and protocols mentioned but not documented, OR inferred from Results/Discussion
   - Source: Results/Discussion sections (mentions without procedures), OR implicit strategic positioning
   - Required: `trigger_text`, `trigger_locations`, `inference_reasoning`, `implicit_metadata`
   - Status: `*_status = "implicit"`

**BOTH are mandatory extraction targets with equal priority.**

### Why Implicit RDMAP Matters

Implicit RDMAP items are assessment-critical because they reveal:
- **Transparency gaps:** What methodological information is missing from documentation
- **Reproducibility barriers:** Procedures that cannot be replicated due to missing detail
- **Credibility concerns:** Undocumented decisions or procedures that affect results
- **Assessment foundation:** Enables evaluating what WAS documented vs what SHOULD BE documented

### Expected Outcomes

**Typical distribution for empirical papers:**
- Explicit RDMAP: 60-80% of total RDMAP items (documented in Methods)
- Implicit RDMAP: 20-40% of total RDMAP items (mentioned elsewhere or inferred)

**If you find zero implicit RDMAP items:** This indicates either:
- Exceptionally thorough Methods documentation (very rare)
- Incomplete implicit RDMAP scanning (common executor error)

Document your systematic implicit scan methodology in extraction_notes to demonstrate which case applies.

**Red flag:** Finding zero implicit RDMAP items without documented systematic scanning suggests extraction failure.

---
```

---

## Fix 8: Add Worked Example

**File:** `extraction-system/prompts/03-rdmap_pass1_prompt.md`

### Step 8.1: Add Comprehensive Implicit RDMAP Example

**Location:** After Example 4 (Implicit Protocol inferred_from_results), before "Output Format" section - approximately line 457

**Insert:**
```markdown

---

### Example 5: Systematic Implicit RDMAP Scan (Complete Workflow)

This example demonstrates the Phase A → Phase B workflow for a Methods section that documents some items but leaves others implicit.

---

**Methods Section Text:**

> "We deployed FAIMS Mobile to digitise archaeological features from Soviet-era military maps. Undergraduate students volunteered during summer fieldwork. The platform enabled offline data collection with opportunistic synchronisation. Time-on-task was measured by comparing staff hours to volunteer hours."

**Results Section Text:**

> "Students were assigned specific map tiles based on fieldwork location. Performance degraded after approximately 2,500 records per device, requiring data transfer. Quality checking was performed on 7% of maps selected randomly."

---

**Phase A: Explicit RDMAP Extraction**

Scanning Methods section finds:

**Explicit Methods (3 items):**
- M001: FAIMS Mobile platform for data collection (explicit)
  - verbatim_quote: "We deployed FAIMS Mobile to digitise archaeological features from Soviet-era military maps"
  - method_type: "data_collection"

- M002: Volunteer crowdsourcing with undergraduate students (explicit)
  - verbatim_quote: "Undergraduate students volunteered during summer fieldwork"
  - method_type: "data_collection"

- M003: Time-on-task comparison measurement (explicit)
  - verbatim_quote: "Time-on-task was measured by comparing staff hours to volunteer hours"
  - method_type: "measurement"

**Explicit Protocols (2 items):**
- P001: Offline data collection with opportunistic sync (explicit)
  - verbatim_quote: "The platform enabled offline data collection with opportunistic synchronisation"
  - protocol_type: "data_management"

- P002: Staff-volunteer time comparison (explicit)
  - verbatim_quote: "Time-on-task was measured by comparing staff hours to volunteer hours"
  - protocol_type: "measurement"

**Phase A Result:** 5 explicit RDMAP items (3 methods, 2 protocols, 0 designs)

---

**Phase B: Systematic Implicit RDMAP Scan**

Now scan Methods AND Results sections for implicit RDMAP using 4-pattern recognition:

---

**Scan 1 - Mentioned Procedures Without Description:**

✓ **Found in Results:** "Students were assigned specific map tiles"
- Trigger: Assignment mentioned but allocation method not described
- Question: How were tiles assigned? Random? By location? By skill level?
- **Extract:** P-IMP-001 (Map tile assignment protocol, implicit)

```json
{
  "protocol_id": "P015",
  "protocol_text": "Map tile assignment procedure for distributing work among volunteer students",
  "protocol_type": "task_allocation",
  "protocol_status": "implicit",
  "trigger_text": [
    "Students were assigned specific map tiles based on fieldwork location"
  ],
  "trigger_locations": [
    {"section": "Results", "subsection": "3.1", "paragraph": 1}
  ],
  "inference_reasoning": "Results states students were assigned specific tiles, and assignment was based on fieldwork location, but Methods section provides no description of the assignment procedure, criteria, or who performed assignments. Procedure must have existed but was not documented.",
  "implicit_metadata": {
    "basis": "mentioned_undocumented",
    "transparency_gap": "No documentation of: assignment procedure, allocation criteria, whether assignment was by staff or self-selected, how location determined assignment, or whether workload was balanced",
    "assessability_impact": "Cannot assess fairness of task distribution, whether assignment method might introduce bias in coverage, or how location-based assignment was operationalised",
    "reconstruction_confidence": "low"
  },
  "implements_methods": ["M002"],
  "location": {"section": "Results", "subsection": "3.1", "paragraph": 1}
}
```

✓ **Found in Results:** "Quality checking was performed on 7% of maps"
- Trigger: QA mentioned but checking procedure not described
- Question: How were maps selected? What did checking involve? Who performed it?
- **Extract:** M-IMP-001 (Quality assurance method, implicit)

```json
{
  "method_id": "M018",
  "method_text": "Quality assurance method involving checking 7% of maps",
  "method_type": "quality_control",
  "method_status": "implicit",
  "trigger_text": [
    "Quality checking was performed on 7% of maps selected randomly"
  ],
  "trigger_locations": [
    {"section": "Results", "subsection": "3.2", "paragraph": 3}
  ],
  "inference_reasoning": "Results mentions quality checking on 7% of maps with random selection, but Methods provides no description of QA procedure, checking criteria, who performed checks, or how random selection was operationalised. QA method clearly existed but was not documented.",
  "implicit_metadata": {
    "basis": "mentioned_undocumented",
    "transparency_gap": "No documentation of: QA procedure steps, checking criteria or checklist, personnel who performed QA, how random 7% was selected, or what actions were taken when errors were found",
    "assessability_impact": "Cannot assess rigor of QA procedures, appropriateness of 7% sampling rate, or whether checking criteria were objective and consistently applied",
    "reconstruction_confidence": "low"
  },
  "realized_through_protocols": ["P-IMP-002"],
  "location": {"section": "Results", "subsection": "3.2", "paragraph": 3}
}
```

---

**Scan 2 - Effects Implying Operational Protocols:**

✓ **Found in Results:** "Performance degraded after approximately 2,500 records per device"
- Trigger: Specific threshold implies monitoring
- Question: How was this threshold detected? Was performance monitored systematically?
- **Extract:** P-IMP-003 (Performance monitoring protocol, implicit)

```json
{
  "protocol_id": "P023",
  "protocol_text": "Device performance monitoring protocol that detected degradation threshold at ~2,500 records",
  "protocol_type": "monitoring",
  "protocol_status": "implicit",
  "trigger_text": [
    "Performance degraded after approximately 2,500 records per device, requiring data transfer"
  ],
  "trigger_locations": [
    {"section": "Results", "subsection": "3.1", "paragraph": 2}
  ],
  "inference_reasoning": "Results reports specific threshold of ~2,500 records at which performance degraded. Detection of this precise threshold implies systematic monitoring of device performance and record counts. Methods section has no description of performance monitoring procedures, suggesting monitoring protocol existed but was not documented.",
  "implicit_metadata": {
    "basis": "inferred_from_results",
    "transparency_gap": "No documentation of: how performance was monitored, whether monitoring was proactive or reactive, how 2,500-record threshold was determined, what performance metrics were tracked, or who monitored devices",
    "assessability_impact": "Cannot assess whether threshold is empirically robust, whether monitoring was systematic or anecdotal, or whether degradation was consistent across devices",
    "reconstruction_confidence": "medium"
  },
  "implements_methods": ["M001"],
  "location": {"section": "Results", "subsection": "3.1", "paragraph": 2}
}
```

---

**Scan 3 - Tools/Equipment Mentioned Without Specifications:**

✓ **Found in Methods:** "FAIMS Mobile" mentioned but no version, configuration, or technical specs
- Trigger: Platform named but specifications not provided
- Question: Which FAIMS Mobile version? What configuration? What customisation?
- **Extract:** P-IMP-004 (FAIMS Mobile configuration protocol, implicit)

```json
{
  "protocol_id": "P003",
  "protocol_text": "FAIMS Mobile platform configuration for archaeological map digitisation",
  "protocol_type": "tool_configuration",
  "protocol_status": "implicit",
  "trigger_text": [
    "We deployed FAIMS Mobile to digitise archaeological features from Soviet-era military maps"
  ],
  "trigger_locations": [
    {"section": "Methods", "subsection": "2.1", "paragraph": 1}
  ],
  "inference_reasoning": "Methods mentions FAIMS Mobile deployment but provides no technical specifications: version number, module configuration, customisation for map digitisation task, or device requirements. Platform must have been configured for this specific use case, but configuration protocol is not documented.",
  "implicit_metadata": {
    "basis": "mentioned_undocumented",
    "transparency_gap": "No documentation of: FAIMS Mobile version, whether customised module was created, configuration settings, device hardware requirements, or map display/digitisation interface design",
    "assessability_impact": "Cannot assess platform capabilities, whether configuration was appropriate for task, or replicate technical setup",
    "reconstruction_confidence": "low"
  },
  "implements_methods": ["M001"],
  "location": {"section": "Methods", "subsection": "2.1", "paragraph": 1}
}
```

---

**Scan 4 - Undocumented Data Processing:**

✓ **Found in Results:** "requiring data transfer" (implies transfer procedure)
- Trigger: Data transfer mentioned but procedure not described
- Question: How were data transferred? What format? How handled synchronisation?
- **Extract:** P-IMP-005 (Data transfer protocol, implicit)

```json
{
  "protocol_id": "P024",
  "protocol_text": "Data transfer protocol when device reached record threshold",
  "protocol_type": "data_management",
  "protocol_status": "implicit",
  "trigger_text": [
    "Performance degraded after approximately 2,500 records per device, requiring data transfer"
  ],
  "trigger_locations": [
    {"section": "Results", "subsection": "3.1", "paragraph": 2}
  ],
  "inference_reasoning": "Results states performance degradation required data transfer, implying procedure existed for transferring data from devices when threshold reached. Methods describes opportunistic sync but not threshold-triggered transfer procedure. Transfer protocol existed but details not documented.",
  "implicit_metadata": {
    "basis": "mentioned_undocumented",
    "transparency_gap": "No documentation of: how transfer was triggered, who performed transfers, whether data were cleared from device after transfer, data integrity verification, or how transferred data were integrated",
    "assessability_impact": "Cannot assess data integrity procedures, whether transfer process might introduce errors or data loss, or how threshold-triggered transfer related to opportunistic sync",
    "reconstruction_confidence": "low"
  },
  "implements_methods": ["M001"],
  "location": {"section": "Results", "subsection": "3.1", "paragraph": 2}
}
```

---

**Phase B Result:** 5 implicit RDMAP items found (1 implicit method, 4 implicit protocols)

---

**Combined Extraction Result:**

- **Explicit RDMAP:** 5 items (3 methods, 2 protocols)
- **Implicit RDMAP:** 5 items (1 method, 4 protocols)
- **Total RDMAP:** 10 items
- **Implicit ratio:** 50% (5/10)

**This is typical.** Methods section documents high-level approaches but leaves operational details implicit. Results section reveals procedures that weren't documented.

**Key lesson:** Phase A extraction is the starting point. Phase B systematic scanning doubles the extraction count by finding undocumented procedures mentioned in Results/Discussion.

---
```

---

## Fix 3: Replace Checkbox with Quality Gate

**File:** `extraction-system/prompts/03-rdmap_pass1_prompt.md`

### Step 3.1: Update Quality Checklist

**Location:** Lines 99-118 (Quality Checklist for Pass 1)

**Current text:**
```markdown
- [ ] All research designs extracted (questions, hypotheses, study designs, frameworks)
- [ ] All methods extracted (data collection, sampling, analysis approaches)
- [ ] All protocols extracted (specific procedures, tools, parameters, configurations)
- [ ] Tier assignments marked (even if uncertain)
- [ ] **Status fields set for all RDMAP items (explicit or implicit)**
- [ ] **All explicit items have verbatim_quote populated**
- [ ] **All implicit items have trigger_text, trigger_locations, inference_reasoning**
- [ ] **All implicit items have complete implicit_metadata**
```

**Replace with:**
```markdown
- [ ] All research designs extracted (questions, hypotheses, study designs, frameworks)
- [ ] All methods extracted (data collection, sampling, analysis approaches)
- [ ] All protocols extracted (specific procedures, tools, parameters, configurations)
- [ ] Tier assignments marked (even if uncertain)
- [ ] **Systematic implicit RDMAP scan completed for EACH major section (Abstract, Intro, Methods, Results, Discussion)**
- [ ] **For each section, documented implicit scan methodology in extraction_notes OR implicit items found**
- [ ] **All implicit RDMAP items have trigger_text, trigger_locations, inference_reasoning, implicit_metadata**
- [ ] **If zero implicit RDMAP items across all sections: extraction_notes explains why** (e.g., "Exceptionally well-documented Methods section with all strategic decisions, methods, and protocols explicit. Systematic scan of Results/Discussion found no undocumented procedure mentions.")
- [ ] **All explicit items have verbatim_quote populated**
- [ ] **Status fields set for all RDMAP items based on documentation location**
```

---

## Fix 4: Reframe from Transparency to Content

**File:** `extraction-system/prompts/03-rdmap_pass1_prompt.md`

### Step 4.1: Update Framing Language

**Location:** Lines 86-96 (RDMAP Sourcing Requirements section)

**Current text:**
```markdown
**Basis classification for implicit RDMAP:**
- **mentioned_undocumented**: Paper mentions item but doesn't describe procedures
  - Example: "Data were cleaned" but no cleaning procedure described
- **inferred_from_results**: Never mentioned but implied by outcomes
  - Example: Results show quality metrics but quality control never mentioned

**Note:** Implicit status documents transparency gaps for assessment. It does NOT mean "bad methodology" - many legitimate decisions may not be fully documented.
```

**Replace with:**
```markdown
**Basis classification for implicit RDMAP:**
- **mentioned_undocumented**: Paper mentions item but doesn't describe procedures
  - Example: "Data were cleaned" but no cleaning procedure described
- **inferred_from_results**: Never mentioned but implied by outcomes
  - Example: Results show quality metrics but quality control never mentioned

**CRITICAL:** Implicit RDMAP extraction is as important as explicit RDMAP extraction. These are PRIMARY CONTENT, not optional metadata. Many papers mention procedures without documenting them, or imply methods through results. These undocumented procedures are assessment-critical because they:
- Reveal transparency gaps (what's missing from Methods)
- Affect reproducibility (procedures that cannot be replicated)
- Impact credibility assessment (undocumented decisions affecting results)

Extract implicit RDMAP items systematically. Do not skip implicit scanning because Methods section exists.
```

---

## Fix 6: Move Recognition Patterns to Main Prompt

**File:** `extraction-system/prompts/03-rdmap_pass1_prompt.md`

### Step 6.1: Embed Recognition Patterns

**Location:** Currently the Step 0 (Pre-Scan) section at lines 236-254 has a reference to external patterns.

**Current text (line 249-253):**
```markdown
**For systematic implicit RDMAP recognition patterns:**
→ See `references/extraction-fundamentals.md` (Implicit RDMAP Extraction section)
- Covers 4 recognition patterns: Mentioned Procedure, Effects Implying Causes, Mentions Without Descriptions, Strategic Decisions
- Section-by-section extraction workflow for finding implicit RDMAP items
- Common mistakes to avoid
```

**Replace with embedded patterns:**
```markdown
**Systematic implicit RDMAP recognition patterns:**

These 4 patterns help identify implicit RDMAP items during Phase B scanning:

**Pattern 1 - Mentioned Procedure:**
- Paper states procedure occurred but doesn't describe HOW
- Look for verbs without procedures: "cleaned", "validated", "checked", "assigned"
- Example: "Data were cleaned" → implicit data cleaning method
- Basis: mentioned_undocumented

**Pattern 2 - Effects Implying Causes:**
- Results or outcomes imply procedures that weren't documented
- Look for: thresholds detected → monitoring, accuracy metrics → validation, error rates → QA
- Example: "Performance degraded at 2,500 records" → implicit monitoring protocol
- Basis: inferred_from_results

**Pattern 3 - Mentions Without Descriptions:**
- Tools, assignments, or processes mentioned without detail
- Look for: "GPS used" (no specs), "students assigned" (no allocation method), "maps prepared" (no preparation process)
- Example: "Students assigned specific tiles" → implicit assignment protocol
- Basis: mentioned_undocumented

**Pattern 4 - Strategic Positioning:**
- Paper positions work relative to alternatives but doesn't state this as design objective
- Look for: systematic comparisons throughout Discussion without design statement
- Example: Paper compares to ML alternatives throughout but Introduction doesn't state comparative evaluation as objective → implicit comparative design
- Basis: inferred_from_results

**For detailed examples and common mistakes:**
→ See `references/extraction-fundamentals.md` (Implicit RDMAP Extraction section)
```

---

## Fix 7: Add Mid-Section Checkpoints

**File:** `extraction-system/prompts/03-rdmap_pass1_prompt.md`

### Step 7.1: Add Checkpoint Template

**Location:** After the main Extraction Workflow section (after Step 5: Flag Missing Information), before Key Examples section - approximately line 326

**Insert:**
```markdown

---

## Mid-Section Extraction Checkpoints

**After completing RDMAP extraction for each section group:**

Use this checkpoint to verify implicit RDMAP scanning is working:

```bash
# Count extraction progress
jq '{
  explicit_designs: [.research_designs[] | select(.design_status == "explicit")] | length,
  implicit_designs: [.research_designs[] | select(.design_status == "implicit")] | length,
  explicit_methods: [.methods[] | select(.method_status == "explicit")] | length,
  implicit_methods: [.methods[] | select(.method_status == "implicit")] | length,
  explicit_protocols: [.protocols[] | select(.protocol_status == "explicit")] | length,
  implicit_protocols: [.protocols[] | select(.protocol_status == "implicit")] | length
}' outputs/{paper-slug}/extraction.json
```

**Calculate implicit ratio:**
- Implicit RDMAP items / Total RDMAP items = Implicit ratio
- Expected ratio: 20-40% for most papers

**Self-check questions:**

1. **If implicit ratio < 10%:**
   - Did I systematically scan Results/Discussion sections?
   - Did I look for procedure verbs without methods?
   - Did I check for operational details revealed in Results?
   - Action: Review remaining sections with increased attention to implicit items

2. **If implicit ratio = 0% after completing 2+ section groups:**
   - Did I run the 4-pattern recognition scan for each section?
   - Can I point to extraction_notes showing my scan methodology?
   - Is Methods documentation truly exceptional?
   - Action: Document scan methodology if exceptional; otherwise review Phase B scanning

3. **If implicit ratio > 40%:**
   - This is acceptable - some papers have extensive undocumented procedures
   - Verify implicit items meet sourcing requirements (trigger_text, implicit_metadata)
   - Action: Continue, high implicit ratio is better than zero

**Document checkpoint results** in extraction_notes for each section group.

---
```

---

## Implementation Checklist

### Before Starting

- [ ] Read diagnostic document: `planning/implicit-extraction-comparison-analysis.md`
- [ ] Back up current prompt: `cp 03-rdmap_pass1_prompt.md 03-rdmap_pass1_prompt.md.backup`
- [ ] Create git branch for changes: `git checkout -b fix-implicit-rdmap-extraction`

### Phase 1: Immediate Fixes

- [ ] **Fix 1:** Restructure Steps 1-3 with Phase A/Phase B structure
  - [ ] Step 1: Research Designs (lines ~255-287)
  - [ ] Step 2: Methods (lines ~288-296)
  - [ ] Step 3: Protocols (lines ~297-306)
- [ ] **Fix 2:** Add iteration reminder after Step 3 (line ~307)
- [ ] **Fix 5:** Add HIGH-PRIORITY section after "Your Task" (line ~35)
- [ ] **Fix 8:** Add Example 5 (Systematic Implicit RDMAP Scan) after Example 4 (line ~457)

### Phase 2: Medium-Term Improvements

- [ ] **Fix 3:** Update Quality Checklist (lines 99-118)
- [ ] **Fix 4:** Update framing language (lines 86-96)
- [ ] **Fix 6:** Embed recognition patterns in main prompt (lines 249-253)

### Phase 3: Long-Term Enhancements

- [ ] **Fix 7:** Add mid-section checkpoints after Step 5 (line ~326)

### After Implementation

- [ ] Validate prompt syntax (no markdown errors)
- [ ] Check line length stays reasonable (< 120 chars where possible)
- [ ] Verify all cross-references to line numbers still valid
- [ ] Commit changes: `git commit -am "Fix implicit RDMAP extraction failure - integrate into main workflow"`

### Testing

- [ ] Re-extract Sobotkova et al. 2023 using updated prompt
- [ ] Verify implicit RDMAP items > 0 (expect 10-20 items)
- [ ] Check implicit ratio 20-40%
- [ ] Verify extraction_notes documents implicit scan methodology
- [ ] Confirm specific expected items found:
  - [ ] Map assignment protocol
  - [ ] Load monitoring protocol
  - [ ] QA method
  - [ ] GPS accuracy protocol
  - [ ] FAIMS Mobile configuration protocol
  - [ ] Data transfer protocol

### Success Criteria

- [ ] Implicit RDMAP items extracted (not zero)
- [ ] Implicit ratio within 20-40% range
- [ ] extraction_notes documents systematic implicit scanning
- [ ] All 4 recognition patterns represented in findings
- [ ] trigger_text and implicit_metadata properly populated

---

## Rollback Plan

If changes cause issues:

```bash
# Restore backup
cp 03-rdmap_pass1_prompt.md.backup 03-rdmap_pass1_prompt.md

# Or use git
git checkout main -- extraction-system/prompts/03-rdmap_pass1_prompt.md
```

---

## Notes for Implementation

### Key Principles

1. **Mirror implicit arguments structure:** The implicit argument extraction works because it's integrated into the main workflow with explicit iteration instructions. Apply the same structure to implicit RDMAP.

2. **Phase A/Phase B separation:** Make explicit and implicit extraction two distinct phases within each step, not mixed together.

3. **Systematic scanning emphasis:** Repeatedly emphasize systematic 4-pattern scanning for EACH section. Use checklists and iteration language.

4. **Quality gates, not checkboxes:** Require evidence of scanning (extraction_notes documentation), not just field population.

5. **Expected outcomes:** Set clear expectations (20-40% implicit ratio) so executor knows zero is a failure signal.

### Estimated Impact

**Before fixes:**
- Implicit RDMAP: 0 items
- Implicit ratio: 0%
- Extraction completeness: ~50-60% (missing all implicit procedures)

**After fixes (projected):**
- Implicit RDMAP: 10-20 items (for Sobotkova paper)
- Implicit ratio: 20-40%
- Extraction completeness: 80-95% (capturing both explicit and implicit)

**Validation:** Re-extract same paper and compare counts.

---

**Version:** 1.0
**Date:** 2025-10-28
**Status:** Ready for implementation
**Related:** `planning/implicit-extraction-comparison-analysis.md` (diagnostic)
