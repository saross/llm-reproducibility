# Evidence vs Claims Decision Guide

**Purpose:** Comprehensive framework for distinguishing evidence from claims during extraction

**Critical for:** Pass 1 extraction, Pass 2 boundary verification, Pass 3 validation

---

## The Core Distinction

### Evidence

**Definition:** Raw observations, measurements, or data that require minimal interpretation

**Characteristics:**
- Direct measurements (e.g., "125.8 person-hours")
- Observations (e.g., "12 students owned smartphones")
- Data points (e.g., "95.7% accuracy")
- Captured verbatim from the paper
- Someone could verify by checking the source
- Minimal reasoning required to accept as fact

**Examples:**
- ✅ "The survey covered 22 ha"
- ✅ "8,343 features were digitized"
- ✅ "Inter-coder reliability Cohen's kappa = 0.87"
- ✅ "GPS accuracy ±3-5m"
- ✅ "3.9 person-hours of supervision required"

### Claims

**Definition:** Assertions that interpret, frame, or generalize from evidence

**Characteristics:**
- Require reasoning or expertise to assess
- Make inferences beyond direct observation
- Involve framing or definitional choices
- Connect evidence to broader patterns
- Judgment or interpretation involved

**Examples:**
- ✅ "The platform was efficient"
- ✅ "Data quality was high"
- ✅ "The approach reduced supervision requirements"
- ✅ "Results demonstrate feasibility"
- ✅ "The method proved superior to traditional approaches"

---

## The Primary Test

**Core Question:** "Does this require expertise to assess or just checking sources?"

- **Checking sources** → Evidence
  - "Did they really collect 8,343 features?" → Check paper → Yes/No

- **Expertise to assess** → Claim
  - "Was the platform efficient?" → Requires judgment about what "efficient" means

**Alternative Formulation:** "Could someone verify this by looking at the source, or does it require interpretation?"

- **Verify from source** → Evidence
- **Requires interpretation** → Claim

---

## Decision Framework

### Step 1: Identify the Statement Type

**Measurement/Observation:**
- Numbers, quantities, counts → Likely Evidence
- "X measurements were Y" → Evidence
- "Tool Z was used" → Evidence (if just stating fact)

**Judgment/Interpretation:**
- Quality assessments ("high," "low," "good," "poor") → Claim
- Effectiveness statements ("efficient," "successful," "feasible") → Claim
- Comparative judgments ("better than," "superior to") → Claim

### Step 2: Apply the Interpretation Test

**Minimal interpretation required** → Evidence
- "8,343 features digitized" (counting)
- "95.7% accuracy" (measurement)
- "3.9 hours supervision" (timing)

**Significant interpretation required** → Claim
- "High-quality dataset produced" (what constitutes "high quality"?)
- "Minimal supervision required" (what constitutes "minimal"?)
- "Approach was efficient" (what threshold defines "efficient"?)

### Step 3: Check for Definitional Dependence

**Does accepting this statement require agreeing with a definition?**

- **NO** → Evidence
  - "125.8 person-hours" (objective measurement)

- **YES** → Claim
  - "Minimal supervision" (depends on defining "minimal")
  - "High accuracy" (depends on defining "high")

---

## Common Boundary Cases

### Case 1: Professional Judgment Statements

**Pattern:** Statements requiring expertise to assess

**Example:** "These maps are accurate"

**Analysis:**
- Requires expertise to assess accuracy
- Professional judgment involved
- Not directly verifiable from source alone

**Classification:** **CLAIM** (interpretation claim)
- Extract as claim supported by implicit professional judgment
- NOT evidence

**Rule:** If it requires professional expertise to assess truthfulness → Claim

### Case 2: Quantified Quality Assessments

**Pattern:** Quality terms with quantitative grounding

**Example 1:** "High accuracy (95.7%)"
- "95.7%" → Evidence
- "High accuracy" → Claim (interpretation of 95.7% as "high")

**Example 2:** "Minimal supervision (3.9 hours)"
- "3.9 hours" → Evidence
- "Minimal" → Claim (interpretation of 3.9 hours as "minimal")

**Rule:** Separate the measurement (evidence) from the judgment (claim)

### Case 3: Comparative Statements

**Pattern:** "X was better/worse/more/less than Y"

**Example:** "Mobile platform was faster than desktop GIS"

**Analysis:**
- Contains factual basis (timing comparison)
- Contains judgment ("faster" implies superiority in this context)

**Classification:** **CLAIM**
- The comparison itself is interpretive
- Supported by evidence (actual timing measurements)

**Rule:** Comparisons beyond direct measurement → Claim

### Case 4: Definitional Framing

**Pattern:** Statements that define or frame concepts

**Example:** "We define 'novice' as users with <1 week training"

**Analysis:**
- This is a definitional choice
- Not an observation of external reality
- Frames subsequent findings

**Classification:** **CLAIM** (definitional claim)
- Or potentially project_metadata if just methodological context

**Rule:** Definitions and framing choices → Claims or metadata, not evidence

### Case 5: Aggregated Measurements

**Pattern:** Summary statistics or aggregates

**Example 1:** "Mean accuracy was 95.7%"
- If calculated from reported data → Evidence
- If requires accepting aggregation method → Claim

**Example 2:** "Overall data quality was acceptable"
- "Acceptable" requires judgment → Claim
- Even if based on quantitative metrics

**Rule:** If aggregation requires methodological judgment → Claim; if straightforward summary → Evidence

---

## Edge Case Decision Trees

### Tree 1: Quality Assessments

```text
Does statement assess quality?
├─ NO → Check other trees
└─ YES → Is quality defined quantitatively?
    ├─ YES → Separate measurement (evidence) from judgment (claim)
    └─ NO → Claim (interpretation required)
```

### Tree 2: Measurements vs Interpretations

```text
Does statement contain numbers/measurements?
├─ NO → Check: Does it describe observation?
│   ├─ YES → Evidence (if minimal interpretation)
│   └─ NO → Claim
└─ YES → Is number presented alone or with interpretation?
    ├─ ALONE → Evidence ("8,343 features")
    └─ WITH INTERPRETATION → Split into evidence + claim
```

### Tree 3: Factual vs Judgment

```text
Could two people disagree about this statement's truth?
├─ NO, easily verified → Evidence
└─ YES, requires judgment → Claim
```

---

## Worked Examples

### Example 1: Output Claim

**Text:** "The mobile platform enabled collection of 8,343 features across 22 sites with minimal training and supervision."

**Analysis:**
- "8,343 features" → Evidence (E001)
- "22 sites" → Evidence (E002 or consolidated into E001)
- "minimal training" → Claim (C001) - requires defining "minimal"
- "minimal supervision" → Claim (C001 or C002) - requires defining "minimal"
- "enabled collection" → Claim (C003) - causal/effectiveness assertion

**Extraction:**
- **E001:** "8,343 features digitised across 22 sites"
- **C001:** "Platform enabled collection with minimal training and supervision"
- **Relationship:** C001 supported by E001

### Example 2: Quality Assessment

**Text:** "Data quality was high, with 95.7% positional accuracy and complete attribute coverage."

**Analysis:**
- "95.7% positional accuracy" → Evidence (E003)
- "complete attribute coverage" → Evidence (E004) if objectively verifiable, Claim if requires judgment
- "Data quality was high" → Claim (C004) - interpretation of metrics as "high quality"

**Extraction:**
- **E003:** "95.7% positional accuracy"
- **E004:** "Complete attribute coverage" (check if verifiable)
- **C004:** "Data quality was high"
- **Relationship:** C004 supported by E003, E004

### Example 3: Comparative Finding

**Text:** "Mobile platform supervision requirements (3.9 hours) were substantially lower than desktop GIS baseline (40 hours)."

**Analysis:**
- "3.9 hours" → Evidence (E005)
- "40 hours" → Evidence (E006)
- "substantially lower" → Claim (C005) - comparative judgment

**Extraction:**
- **E005:** "Mobile platform required 3.9 person-hours supervision"
- **E006:** "Desktop GIS required 40 person-hours supervision"
- **C005:** "Mobile platform supervision requirements substantially lower than desktop GIS baseline"
- **Relationship:** C005 supported by E005, E006

### Example 4: Professional Judgment

**Text:** "The digitised historical maps show acceptable geometric accuracy for archaeological purposes."

**Analysis:**
- No quantitative measurement provided
- "acceptable" requires professional judgment
- "for archaeological purposes" adds domain-specific framing

**Classification:** **CLAIM** (professional judgment)

**Extraction:**
- **C006:** "Digitised historical maps show acceptable geometric accuracy for archaeological purposes"
- **Supporting evidence:** May be implicit professional assessment or based on unstated measurements

---

## Common Mistakes to Avoid

### Mistake 1: Treating Quality Terms as Evidence

**Wrong:**
- E001: "High data quality" → This is interpretation, not observation

**Right:**
- E001: "95.7% positional accuracy"
- C001: "Data quality was high" (supported by E001)

### Mistake 2: Treating All Numbers as Evidence

**Wrong:**
- E002: "3.9 hours of minimal supervision"

**Right:**
- E002: "3.9 person-hours supervision"
- C002: "Supervision requirements were minimal" (supported by E002)

### Mistake 3: Missing Implicit Claims

**Wrong:**
- Extract only: E003: "8,343 features collected"
- Miss the implicit claim about capability/success

**Right:**
- E003: "8,343 features collected"
- C003: "Platform successfully enabled large-scale feature collection" (supported by E003)

### Mistake 4: Over-Splitting Integrated Statements

**Wrong:**
- E004a: "8,343"
- E004b: "features"
- E004c: "collected"

**Right:**
- E004: "8,343 features collected"
- Keep measurement integrated

### Mistake 5: Confusing Methodology with Evidence

**Wrong:**
- E005: "We used stratified random sampling" → This is methodology (RDMAP), not evidence

**Right:**
- This goes to methods array, not evidence array
- Evidence would be results/observations FROM the sampling

---

## Integration with Claims Hierarchy

### Supporting Evidence (Bottom Layer)

Evidence directly supports SUPPORTING claims (lowest tier of claims hierarchy)

```text
Evidence → Supporting Claim → Intermediate Claim → Core Claim
```

**Example:**
- E001: "8,343 features digitised"
- Supporting Claim: "Large dataset produced"
- Intermediate Claim: "Platform enabled efficient data collection"
- Core Claim: "Mobile crowdsourcing viable for archaeological georeferencing"

### Evidence-Claim Granularity Matching

**Principle:** Evidence granularity should match claim granularity

**Fine-grained claim** → Fine-grained evidence:
- Claim: "Point collection was rapid (54 seconds per feature)"
- Evidence: "54 seconds per feature collection time"

**High-level claim** → May aggregate multiple evidence items:
- Claim: "Platform demonstrated efficiency across multiple metrics"
- Evidence: E001 (collection time), E002 (supervision time), E003 (output volume)

---

## Validation Checklist

Use this checklist during Pass 2 boundary verification or Pass 3 validation:

### For Each Evidence Item:

- [ ] Does this item require expertise to assess?
  - If YES → Reclassify as claim

- [ ] Does this contain interpretation/judgment language?
  - If YES → Separate measurement (evidence) from judgment (claim)

- [ ] Could someone verify this by checking the source?
  - If NO → Reclassify as claim

### For Each Claim Item:

- [ ] Is this just a direct observation/measurement?
  - If YES → Reclassify as evidence

- [ ] Does this make an inference or interpretation?
  - If NO → Consider if it belongs in evidence or project_metadata

- [ ] Is this supported by evidence?
  - If NO → Flag for review (defensive extraction or missing evidence)

---

## Quick Reference

**Evidence = Observations requiring minimal interpretation**
- Measurements, counts, observations
- Verifiable from source
- Minimal reasoning required

**Claims = Assertions requiring interpretation**
- Quality assessments, effectiveness judgments
- Comparative evaluations
- Require expertise or definitional agreement

**Primary Test:** "Expertise to assess OR just check sources?"

**Common Patterns:**
- Numbers alone → Evidence
- Numbers + quality term → Separate (evidence + claim)
- Comparisons → Claim (supported by evidence)
- Professional judgment → Claim
- Definitions/framing → Claim or metadata

**When uncertain:** Extract at both levels in Pass 1, resolve in Pass 2
