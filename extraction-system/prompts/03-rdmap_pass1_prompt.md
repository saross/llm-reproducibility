# RDMAP Extraction Prompt - PASS 1: Liberal Extraction v2.5

**Version:** 2.5 Pass 1  
**Last Updated:** 2025-10-21  
**Workflow Stage:** Pass 1 of 3 - Liberal RDMAP extraction with over-capture strategy  
**Skill Context:** This prompt is part of the research-assessor skill  
**Schema Update:** Added mandatory sourcing (explicit/implicit distinction) to prevent hallucination

---

## Your Task

Extract Research Design, Methods, and Protocols (RDMAP) from research paper sections. This is **Pass 1: Liberal Extraction** - when uncertain about tier assignment or boundaries, err on the side of inclusion. Pass 2 will consolidate and rationalize.

**Input:** JSON extraction document (schema v2.5)
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

## 🚨 CRITICAL: Verbatim Quote Requirements

**Before extracting any item:**

Read if uncertain: `/mnt/skills/user/research-assessor/references/verbatim-quote-requirements.md`

**Non-negotiable rules for all `verbatim_quote` fields:**

1. **Complete sentences only** - Extract whole grammatical units, never mid-sentence fragments
2. **Exact text only** - Copy-paste from paper, never paraphrase or reconstruct from memory  
3. **Verify before committing** - Ensure exact quote exists in paper before adding to JSON
4. **Single source only** - Never synthesize quotes from multiple locations

**Self-check:** "Can I find this EXACT text string in the paper with simple search?"
- If YES → Extract it
- If NO → Quote is wrong; fix it or mark as implicit

⚠️ **Failure to follow these rules causes 40-50% validation failures in Pass 3.**

---

## 🚨 CRITICAL: RDMAP Sourcing Requirements

**READ FIRST:** `/mnt/skills/user/research-assessor/references/extraction-fundamentals.md`

The fundamentals document covers universal sourcing requirements that apply to all object types. **RDMAP items have the same sourcing discipline as Evidence and Claims.**

### RDMAP-Specific: Explicit vs Implicit Status

**EXPLICIT = Documented in Methods section**
- Procedural details provided with sufficient description
- Extract with `verbatim_quote` field
- Status: `design_status`, `method_status`, or `protocol_status` = `"explicit"`

**IMPLICIT = Not documented in Methods section**
- May be mentioned elsewhere without procedures (Results/Discussion)
- May be inferred from outcomes or comparisons
- Extract with `trigger_text` + `trigger_locations` + `inference_reasoning` + `implicit_metadata`
- Status: `design_status`, `method_status`, or `protocol_status` = `"implicit"`

**Decision rule:**
```
Is this RDMAP item described in the Methods section?
├─ YES → Status = "explicit", extract with verbatim_quote
└─ NO → Are there passages elsewhere that imply it existed?
    ├─ YES → Status = "implicit", extract with trigger_text
    └─ NO → DO NOT EXTRACT (absent, not implicit)
```

**Basis classification for implicit RDMAP:**
- **mentioned_undocumented**: Paper mentions item but doesn't describe procedures
  - Example: "Data were cleaned" but no cleaning procedure described
- **inferred_from_results**: Never mentioned but implied by outcomes
  - Example: Results show quality metrics but quality control never mentioned

**Note:** Implicit status documents transparency gaps for assessment. It does NOT mean "bad methodology" - many legitimate decisions may not be fully documented.

**For complete sourcing fundamentals:** → `references/extraction-fundamentals.md`  
**For detailed verification procedures:** → `references/verification-procedures.md`

---

## Quality Checklist for Pass 1

Use this checklist as your roadmap. Before finalizing:

- [ ] All research designs extracted (questions, hypotheses, study designs, frameworks)
- [ ] All methods extracted (data collection, sampling, analysis approaches)
- [ ] All protocols extracted (specific procedures, tools, parameters, configurations)
- [ ] Tier assignments marked (even if uncertain)
- [ ] **Status fields set for all RDMAP items (explicit or implicit)**
- [ ] **All explicit items have verbatim_quote populated**
- [ ] **All implicit items have trigger_text, trigger_locations, inference_reasoning**
- [ ] **All implicit items have complete implicit_metadata**
- [ ] Cross-references populated (`enables_methods`, `realized_through_protocols`, etc.)
- [ ] `expected_information_missing` flagged where appropriate
- [ ] `extraction_notes` document uncertainties and decisions
- [ ] Location tracking complete (section, page, paragraph)
- [ ] Reasoning approaches classified (where applicable)
- [ ] **No hallucinations - only extract what's sourced**
- [ ] Other arrays (claims/evidence) untouched

---

## Extraction Philosophy

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
- **Extracting RDMAP items without proper sourcing (verbatim_quote OR trigger_text)**

---

## Core Decision Framework

### 1. Three-Tier Hierarchy: Design → Methods → Protocols

**Quick Decision Tree:**
```
Does this explain WHY research was framed/designed this way?
├─ YES → Research Design
└─ NO → Does this explain WHAT general approach was used?
    ├─ YES → Method
    └─ NO → Does this explain HOW specifically something was done?
        ├─ YES → Protocol
        └─ NO → Likely project context (metadata, not RDMAP)
```

**Research Design (Strategic - WHY)**
- Research questions and hypotheses
- Theoretical frameworks
- Study design choices and rationale
- Scope definitions
- Positionality statements

**Methods (Tactical - WHAT)**
- Data collection approaches
- Sampling strategies
- Analysis approaches
- Quality control methods
- Validation approaches

**Protocols (Operational - HOW)**
- Specific procedures with detail
- Tools and equipment specifications
- Recording standards and formats
- Parameter values and configurations
- Measurement protocols with precision

**When uncertain:** Extract at BOTH levels and mark `extraction_notes` with "Tier assignment uncertain - may belong at [alternative tier]"

**For detailed tier assignment guidance and examples:**  
→ See `references/checklists/tier-assignment-guide.md`

---

### 2. Description vs Argumentation Boundary

**RDMAP = Methodological Descriptions (what was done)**
- Research designs, data collection methods, analysis procedures
- Extract as neutral descriptions
- Example: "Used stratified random sampling with 30% coverage"

**Claims/Evidence = Argumentation (assertions about what worked)**
- Effectiveness claims, quality assessments, comparisons
- Extract separately in claims/evidence arrays
- Example: "Stratified sampling proved more efficient than previous approaches"

**Test:** "Is this describing HOW research was done, or ARGUING about how well it worked?"
- Describing → RDMAP
- Arguing → Claims/Evidence

**If combined:** Extract description in RDMAP, assertion in claims, cross-reference them

---

### 3. Reasoning Approach Classification

**For Research Designs, classify reasoning approach:**

**Inductive** - Data to patterns to theory
- Exploratory, pattern discovery, grounded theory
- Indicator: "emerged from", "patterns suggested", "we observed"

**Abductive** - Anomaly to best explanation
- Puzzle-solving, inference to best explanation
- Indicator: "surprising finding", "best explained by", "accounts for"

**Deductive** - Theory to predictions to test
- Hypothesis testing, theory verification
- Indicator: "we hypothesized", "predicted", "tested whether"

**Mixed** - Genuine combination (NOT default)
- Explicit integration of approaches
- Must show both exploratory AND confirmatory phases
- Example: "Exploratory phase identified patterns, confirmatory phase tested hypotheses"

**Unclear** - Insufficient information
- Use when approach not stated or inferable

**Important:** 
- Look for explicit statements about approach
- Check hypothesis timing (pre-data vs post-data)
- Document confidence level
- Don't default to "mixed" - be specific when possible

---

### 4. Research Questions vs Hypotheses

**Research Questions** - Open-ended inquiry
- "How does X affect Y?"
- "What is the relationship between X and Y?"
- No prediction, exploratory stance

**Hypotheses** - Specific predictions
- "X will increase Y"
- "X is positively correlated with Y"
- Testable prediction, confirmatory stance

**Critical distinction: Timing**
- **Pre-data:** Stated before/during data collection
- **Post-data:** Formulated after seeing patterns
- Document timing basis and confidence

**If unclear:** Flag in `extraction_notes` and document reasoning

---

### 5. Expected Information & Missing Elements

For each RDMAP item, consider what information SHOULD be present but is MISSING.

**Use the `expected_information_missing` field to document gaps:**
- Don't penalize - just document
- Helps assess transparency and replicability
- Context-dependent (archaeology ≠ biology ≠ ethnography)

**For comprehensive checklists covering:**
- Method documentation (TIDieR-adapted)
- Measurement specifications (CONSORT-adapted)
- Sampling strategies
- Analysis methods
- Domain-specific expectations (archaeology, biology, ethnography)

**→ See `references/checklists/expected-information.md`**

**Common missing elements to watch for:**
- Sample size justification
- Tool/equipment specifications
- Parameter settings
- Quality control procedures
- Alternative methods considered
- Stopping rules for sampling

**Note:** Expected information is separate from implicit status. An explicit (documented) method can still be missing expected details. Implicit methods automatically have higher expected information gaps since they're not documented at all.

---

### 6. Fieldwork-Specific Considerations

**Opportunistic Decisions**
- Unplanned adaptations during fieldwork
- Response to field conditions
- Mark as `opportunistic: true` in relevant RDMAP item
- Example: "Extended survey due to high artifact density"

**Contingency Plans**
- Pre-planned IF-THEN responses
- Extract as protocols with `contingent: true`
- Example: "If GPS unavailable, use total station"

**Emergent Discoveries**
- Patterns discovered during analysis
- Hypotheses formulated post-data
- Mark timing in research questions/hypotheses
- Document emergence in `extraction_notes`

---

### 7. Cross-Referencing

**Populate bidirectional links:**
- Research Designs `enables_methods` → Methods `implements_designs`
- Methods `realized_through_protocols` → Protocols `implements_methods`
- Methods `supports_claims` ← Claims `supported_by_evidence`

**Don't over-reference:** Only link if there's a clear relationship

**Complete in Step 4** of workflow (after extracting all RDMAP items)

---

## Extraction Workflow

### Step 1: Identify Research Designs
- Scan Abstract, Introduction, Background carefully (RDs commonly appear here; also check Methods sections, especially those with design-oriented framing)
- Scan for design language keywords (see tier-assignment-guide.md)
- **Identify each distinct strategic decision point** (separate rationales = separate designs)
- Extract theoretical frameworks as Research Designs
- Classify reasoning approach for each
- Determine explicit vs implicit status
- Populate verbatim_quote OR trigger_text appropriately
- **Liberal extraction:** Include "high-level" design elements - critical for transparency assessment

### Step 2: Identify Methods
- Look for data collection approaches
- Extract sampling strategies
- Identify analysis methods
- Note quality control and validation approaches
- Determine explicit vs implicit status for each method
- Populate verbatim_quote OR trigger_text + implicit_metadata
- Document expected missing information

### Step 3: Identify Protocols
- Find specific procedures with implementation detail
- Extract tool specifications and configurations
- Capture parameter settings and values
- Document recording standards and decision rules
- Note measurement protocols
- Determine explicit vs implicit status for each protocol
- Populate verbatim_quote OR trigger_text + implicit_metadata

### Step 4: Cross-Reference
- Link designs to methods they enable
- Link methods to protocols they use
- Verify bidirectional consistency
- Update `implements_designs` and `implements_methods` fields

**Protocol-method linking (CRITICAL):**
- `implements_methods` is an ARRAY of method IDs (plural, not singular)
- Protocol implements ONE method: `"implements_methods": ["M001"]`
- Protocol implements MULTIPLE methods: `"implements_methods": ["M001", "M002"]`
- All protocols should link to at least one method (prevents orphaned protocols)

### Step 5: Flag Missing Information
- Review each RDMAP item against expected information
- Populate `expected_information_missing` arrays
- Document in `extraction_notes` if significant gaps
- Don't penalize - just document for transparency

---

## Key Examples

### Example 1: Explicit Research Design

**Text (from Methods):** "We hypothesized that mobile platforms would be more efficient than paper-based recording. We also conducted exploratory analysis to identify usage patterns."

**Extract as:**
```json
{
  "design_id": "RD001",
  "design_type": "research_question",
  "design_status": "explicit",
  "verbatim_quote": "We hypothesized that mobile platforms would be more efficient than paper-based recording. We also conducted exploratory analysis to identify usage patterns.",
  "hypotheses": [{
    "hypothesis": "Mobile platforms would be more efficient than paper-based recording",
    "formulation_timing": "pre-data",
    "timing_basis": "Stated in introduction before methods"
  }],
  "reasoning_approach": {
    "approach": "mixed",
    "reasoning_confidence": "high",
    "indicators": ["Explicit hypothesis (deductive)", "Exploratory analysis (inductive)"]
  },
  "location": {"section": "Methods", "subsection": "2.1 Study Design", "paragraph": 1}
}
```

---

### Example 2: Explicit Method

**Text (from Methods):** "Survey used systematic transects with 20% coverage. Due to high artifact density in western section, coverage was increased to 40% in that area."

**Extract as:**
```json
{
  "method_id": "M003",
  "method_text": "Systematic transect survey with adaptive coverage",
  "method_status": "explicit",
  "verbatim_quote": "Survey used systematic transects with 20% coverage. Due to high artifact density in western section, coverage was increased to 40% in that area.",
  "sampling_strategy": {
    "sampling_type": "systematic",
    "planned_coverage": "20%",
    "actual_coverage": "20% overall, 40% in western section"
  },
  "opportunistic": true,
  "opportunistic_notes": "Coverage increased in western section due to high artifact density",
  "expected_information_missing": ["Stopping rule for increased coverage", "Criteria for 'high density'"],
  "location": {"section": "Methods", "subsection": "2.3 Field Survey", "paragraph": 2}
}
```

---

### Example 3: Implicit Method (mentioned_undocumented)

**Text (from Discussion):** "Desktop quality control procedures ensured data consistency in 2010 season."

**Methods section check:** No description of quality control procedures found.

**Extract as:**
```json
{
  "method_id": "M018",
  "method_text": "Desktop quality control procedures for 2010 season data consistency",
  "method_status": "implicit",
  "trigger_text": [
    "Desktop quality control procedures ensured data consistency in 2010 season"
  ],
  "trigger_locations": [
    {"section": "Discussion", "subsection": "4.2", "paragraph": 3}
  ],
  "inference_reasoning": "Discussion mentions quality control procedures for 2010 data, but Methods contains no description. Procedures were used but not documented.",
  "implicit_metadata": {
    "basis": "mentioned_undocumented",
    "transparency_gap": "No description of QC procedures, criteria, or personnel",
    "assessability_impact": "Cannot assess rigor or appropriateness of QC for 2010 data",
    "reconstruction_confidence": "low"
  },
  "expected_information_missing": [
    "QC procedure description",
    "QC criteria and thresholds",
    "Personnel who performed QC"
  ],
  "location": {"section": "Discussion", "subsection": "4.2", "paragraph": 3}
}
```

---

### Example 4: Implicit Protocol (inferred_from_results)

**Text (from Results):** "After removing GPS points with accuracy >10m, mean accuracy was 2.3m (SD = 1.1m, n = 1,247)."

**Methods section check:** No mention of GPS point filtering.

**Extract as:**
```json
{
  "protocol_id": "P025",
  "protocol_text": "GPS point filtering procedure based on 10m accuracy threshold",
  "protocol_status": "implicit",
  "trigger_text": [
    "After removing GPS points with accuracy >10m, mean accuracy was 2.3m"
  ],
  "trigger_locations": [
    {"section": "Results", "subsection": "3.1", "paragraph": 2}
  ],
  "inference_reasoning": "Results state GPS points >10m were removed before analysis. Methods has no description of this filtering. Protocol must have been applied but wasn't documented.",
  "implicit_metadata": {
    "basis": "inferred_from_results",
    "transparency_gap": "No description of filtering: how accuracy measured, when applied, automated vs manual",
    "assessability_impact": "Cannot verify appropriateness of 10m threshold or assess impact on coverage",
    "reconstruction_confidence": "medium"
  },
  "parameters": {
    "accuracy_threshold": "10m"
  },
  "expected_information_missing": [
    "How accuracy measured",
    "Filtering stage",
    "Number of points removed",
    "Justification for 10m threshold"
  ],
  "location": {"section": "Results", "subsection": "3.1", "paragraph": 2}
}
```

---

## Output Format

**Return the same JSON document with RDMAP arrays populated:**

```json
{
  "schema_version": "2.5",
  "extraction_timestamp": "ISO 8601",
  "extractor": "Claude Sonnet 4.5",
  
  // Populate these arrays:
  "research_designs": [design_object],    
  "methods": [method_object],             
  "protocols": [protocol_object],         
  
  // Leave these untouched:
  "evidence": [...],                      
  "claims": [...],                        
  "implicit_arguments": [...],            
  
  "extraction_notes": {
    "pass": 1,
    "section_extracted": "string",
    "total_rdmap_items": 47,
    "designs": 8,
    "methods": 23,
    "protocols": 16,
    "explicit_items": 38,
    "implicit_items": 9,
    "uncertain_classifications": 3
  }
}
```

**For complete object structure and field definitions:**  
→ See `references/schema/schema-guide.md`

---

## Pass 1 Goal

Produce comprehensive RDMAP extraction with:
- All methodological information captured (over-extraction OK)
- All items properly sourced (explicit with verbatim_quote OR implicit with trigger_text)
- Tier assignments made (even if uncertain)
- Status fields set (explicit or implicit)
- Expected information gaps flagged
- Cross-references populated
- Ready for rationalization (Pass 2)