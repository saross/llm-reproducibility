# RDMAP Extraction Prompt - PASS 1: Liberal Extraction v2.4

**Version:** 2.4 Pass 1  
**Last Updated:** 2025-10-20  
**Workflow Stage:** Pass 1 of 3 - Liberal RDMAP extraction with over-capture strategy  
**Skill Context:** This prompt is part of the research-assessor skill

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

## Quality Checklist for Pass 1

Use this checklist as your roadmap. Before finalizing:

- [ ] All research designs extracted (questions, hypotheses, study designs, frameworks)
- [ ] All methods extracted (data collection, sampling, analysis approaches)
- [ ] All protocols extracted (specific procedures, tools, parameters, configurations)
- [ ] Tier assignments marked (even if uncertain)
- [ ] Cross-references populated (`enables_methods`, `realized_through_protocols`, etc.)
- [ ] `expected_information_missing` flagged where appropriate
- [ ] `extraction_notes` document uncertainties and decisions
- [ ] Location tracking complete (section, page, paragraph)
- [ ] Reasoning approaches classified (where applicable)
- [ ] No hallucinations - only extract what's actually stated
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
- Methods `realized_through_protocols` → Protocols `implements_method`
- Methods `supports_claims` ← Claims `supported_by_evidence`

**Don't over-reference:** Only link if there's a clear relationship

**Complete in Step 4** of workflow (after extracting all RDMAP items)

---

## Extraction Workflow

### Step 1: Identify Research Designs
- Scan for research questions, hypotheses, theoretical frameworks
- Extract study design choices and rationale
- Classify reasoning approach
- Track location information

### Step 2: Identify Methods
- Look for data collection approaches
- Extract sampling strategies
- Identify analysis methods
- Note quality control and validation approaches
- Document expected missing information

### Step 3: Identify Protocols
- Find specific procedures with implementation detail
- Extract tool specifications and configurations
- Capture parameter settings and values
- Document recording standards and decision rules
- Note measurement protocols

### Step 4: Cross-Reference
- Link designs to methods they enable
- Link methods to protocols they use
- Verify bidirectional consistency
- Update `implements_designs` and `implements_method` fields

### Step 5: Flag Missing Information
- Review each RDMAP item against expected information
- Populate `expected_information_missing` arrays
- Document in `extraction_notes` if significant gaps
- Don't penalize - just document for transparency

---

## Boundary Cases and Decisions

### When Description and Argumentation are Combined

**Pattern:** "We used [method] which was [assessment/claim]"

**Solution:** Split into RDMAP + Claim
- RDMAP: "We used [method]" 
- Claim: "[Method] was [assessment]"
- Cross-reference them

**Example:**
- Text: "We used mobile platform which proved more efficient than paper"
- Method: "Mobile platform for data recording"
- Claim: "Mobile platform was more efficient than paper"
- Cross-reference: Method supports Claim

---

### When Tier Assignment is Ambiguous

**Pattern:** Statement could fit multiple tiers

**Solution:** Include at primary tier, note alternative in `extraction_notes`

**Example:**
- "GPS points collected at 5m accuracy"
- Could be: Method (general GPS approach) OR Protocol (specific 5m setting)
- Decision: Protocol (specific parameter value)
- Note: "Could also be considered method-level description of GPS approach"

**When genuinely uncertain:** Extract at BOTH tiers with cross-reference

---

### When Reasoning Approach is Mixed

**Don't default to "mixed"** - requires evidence of BOTH approaches

**Genuine mixed:**
- Explicit exploratory phase THEN confirmatory phase
- Both inductive and deductive elements documented
- Example: "Exploratory analysis identified patterns, then tested via hypothesis"

**Not mixed:**
- Just unclear approach → `unclear`
- Only one approach evident → classify specifically
- No information → `unclear`

---

### When Hypothesis Timing is Ambiguous

**Pre-data indicators:**
- Stated in Introduction/Methods before results
- Uses future tense ("We will test")
- Called "hypothesis" or "prediction" a priori

**Post-data indicators:**
- First mentioned in Results/Discussion
- Formed after seeing patterns
- Called "emerged" or "suggested by"

**Document:**
- Timing basis (where/when stated)
- Confidence level (high/medium/low)
- Mark `emergent: true` if post-data

---

## Key Examples

### Example 1: Research Design with Reasoning Approach

**Text:** "We hypothesized that mobile platforms would be more efficient than paper-based recording. We also conducted exploratory analysis to identify usage patterns."

**Extract as:**
```json
{
  "design_id": "RD001",
  "design_type": "research_question",
  "hypotheses": [{
    "hypothesis": "Mobile platforms would be more efficient than paper-based recording",
    "formulation_timing": "pre-data",
    "timing_basis": "Stated in introduction before methods"
  }],
  "reasoning_approach": {
    "approach": "mixed",
    "reasoning_confidence": "high",
    "indicators": ["Explicit hypothesis (deductive)", "Exploratory analysis (inductive)"]
  }
}
```

---

### Example 2: Method with Opportunistic Decision

**Text:** "Survey used systematic transects. Due to unexpectedly high artifact density in western section, survey coverage was increased from 20% to 40% in that area."

**Extract as:**
```json
{
  "method_id": "M003",
  "method_text": "Systematic transect survey with adaptive coverage",
  "sampling_strategy": {
    "sampling_type": "systematic",
    "planned_coverage": "20%",
    "actual_coverage": "20% overall, 40% in western section"
  },
  "opportunistic": true,
  "opportunistic_notes": "Coverage increased in western section due to high artifact density",
  "expected_information_missing": ["Stopping rule for increased coverage", "Criteria for 'high density'"]
}
```

---

### Example 3: Protocol with Tool Specification

**Text:** "GPS coordinates recorded using Trimble GeoXH 6000 with real-time SBAS correction, accuracy target 1m horizontal."

**Extract as:**
```json
{
  "protocol_id": "P012",
  "protocol_text": "GPS coordinate recording with real-time correction",
  "tools_equipment": ["Trimble GeoXH 6000"],
  "parameters": {
    "correction_type": "real-time SBAS",
    "accuracy_target": "1m horizontal"
  },
  "expected_information_missing": ["Actual accuracy achieved", "Number of satellites required"]
}
```

---

### Example 4: Combined Description + Claim (Split)

**Text:** "We used stratified random sampling which proved more representative than our previous convenience sampling."

**Extract as RDMAP:**
```json
{
  "method_id": "M007",
  "method_text": "Stratified random sampling",
  "sampling_strategy": {
    "sampling_type": "stratified_random"
  },
  "supports_claims": ["C045"]
}
```

**Extract as Claim (in claims array):**
```json
{
  "claim_id": "C045",
  "claim_text": "Stratified random sampling proved more representative than previous convenience sampling",
  "supported_by_evidence": ["M007"]
}
```

---

## Output Format

**Return the same JSON document with RDMAP arrays populated:**

```json
{
  "schema_version": "2.4",
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
- Tier assignments made (even if uncertain)
- Expected information gaps flagged
- Cross-references populated
- Ready for rationalization (Pass 2)