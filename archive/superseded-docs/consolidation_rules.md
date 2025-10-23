# Consolidation Rules v1.0

**Version:** 1.0  
**Created:** 2025-10-17  
**Purpose:** Quick reference for Pass 2 rationalization decisions  
**Source:** Empirically derived from Methods section rationalization

---

## The Acid Test

**"Would I assess the credibility of these statements TOGETHER or SEPARATELY?"**

- **Together** → LUMP (consolidate)
- **Separately** → SPLIT (keep distinct)

This is your primary decision criterion. When in doubt, apply the test.

---

## When to LUMP (Consolidate)

### 1. Multiple observations specify the same entity

**Pattern:** Descriptive details about one thing scattered across multiple items

**Example:**
- Before: E001 (map scale 1:5000), E005 (digitized from paper), E007 (1920s source date)
- After: E001-CONSOLIDATED "Historical maps at 1:5000 scale, digitized from 1920s paper sources"

**Rationale:** Specifications belong together for assessment

### 2. Multiple interpretations form a single compound claim

**Pattern:** Professional judgment components that are assessed as one unit

**Example:**
- Before: E002 "Maps are accurate", E003 "Represent pre-modern landscapes"
- After: C002-NEW "Maps accurately represent pre-modern landscapes"

**Rationale:** Both require same expertise to assess; assessed together

### 3. Technical features that jointly support one capability claim

**Pattern:** Individual features less important than overall capability

**Example:**
- Before: 8 separate automation features (feature selection, validation, workflow management, etc.)
- After: E-PLATFORM "Platform provides comprehensive automation (8 specific capabilities)" + count as detail

**Rationale:** Overall capability matters for claims, not individual feature granularity

### 4. Process steps that form a single workflow

**Pattern:** Multiple tasks that constitute one role or responsibility

**Example:**
- Before: Multiple staff preparation tasks (data cleaning, format conversion, quality checks)
- After: E-STAFF "Staff handled geospatial data preparation and quality control"

**Rationale:** Division of labor principle matters, not individual task efficiency

---

## When to SPLIT (Keep Separate)

### 1. Different observations support different claims

**Pattern:** Each item supports a distinct assessment question

**Example:**
- Keep separate: E011 (student hours worked) vs E012 (features generated)
- Rationale: One supports efficiency claim, other supports output claim

**Assessment questions differ:**
- "How efficient was the process?" (hours)
- "What was the output?" (features)

### 2. Claims have different assessment requirements

**Pattern:** Independent quality dimensions needing separate evaluation

**Example:**
- Keep separate: Accuracy (95.7%) vs Completeness (83%)
- Rationale: Different quality dimensions, independent credibility assessments

**Can't assess one from the other:**
- High accuracy doesn't imply high completeness
- Each requires different validation approach

### 3. Evidence comes from different sources or methods

**Pattern:** Confidence basis differs, requires separate tracking

**Example:**
- Keep separate: Direct measurement vs professional judgment
- Rationale: Different evidence strength, different credibility basis

**Assessment differs:**
- Measurement: Check precision, calibration, error margins
- Judgment: Check expertise, explanation, alternative views

### 4. Alternative limitations address different concerns

**Pattern:** Each limitation supports different part of rejection argument

**Example:**
- Keep separate: ArcGIS connectivity requirement vs multi-app architecture complexity
- Rationale: Different reasons why alternative inadequate

**Support different rejection criteria:**
- Connectivity: Field practicality concern
- Architecture: Usability concern

---

## Category-Specific Patterns

### Maps/Source Materials

**Common over-extraction:** Scale, source type, date, coverage, digitization as separate items

**Consolidate to:**
- ONE evidence item: Source specifications
- ONE claim (if applicable): Quality/accuracy assessment

**When to split:**
- If different map sources support different claims
- If quality varies across map sets

### Platform/Tool Features

**Common over-extraction:** Each individual feature as separate evidence

**Consolidate to:**
- Overall capabilities as evidence
- Feature count as supporting detail
- Implicit claim about capability if generalized

**When to split:**
- If specific features support different claims
- If some features validated, others not

### Participant Data

**Usually keep separate when:**
- Different dimensions (time, output, device usage)
- Support different claims (efficiency vs preference)
- Different metrics requiring independent assessment

**Example - DON'T consolidate:**
- E011: Student hours (efficiency)
- E012: Features generated (output)
- E018: Device ownership (preference)

### Validation Results

**Always keep separate:**
- Different quality dimensions (accuracy vs completeness)
- Different validation approaches (automated vs manual)
- Different metrics (precision vs recall)

**Rationale:** Independent quality assessments needed

---

## Consolidation Operations

### REMOVE → project_metadata

**Move these to project_metadata:**
- Timeline (field seasons, project phases)
- Location context (sites, work settings)
- Resource constraints (equipment, budget)
- Track record (prior uses of method)
- Organizational details (team structure)

**Test:** "Would removing this cause a claim to lose evidential support?"
- NO → Project metadata
- YES → Keep as evidence

### CONSOLIDATE → Single item

**Apply lumping heuristics:**
1. Same entity specifications → One specification item
2. Compound professional judgment → One claim
3. Joint technical capabilities → One capability statement
4. Single workflow steps → One process description

**Document in change log:**
- Which items consolidated
- Result ID
- Rationale (which heuristic applied)
- Verify no information lost

### SPLIT → Multiple items

**Rare in Pass 2** (Pass 1 should be granular), but watch for:
- Multiple quality dimensions bundled inappropriately
- Different evidence sources conflated
- Distinct claims merged prematurely

**Document in change log:**
- Original item ID
- New item IDs created
- Rationale for splitting
- How support relationships updated

### RECLASSIFY → Change type

**Evidence → Claim when:**
- Requires expertise to assess
- Involves professional judgment
- Makes inference beyond observation
- Generalizes from specific observation

**Claim → Evidence when:**
- Direct observation misclassified
- Verifiable without expertise
- No interpretive framing involved

**Document in change log:**
- Old classification
- New classification
- Rationale (which criterion triggered change)

### ADD → Missing implicit generalizations

**Pattern to detect:** Project observation supports domain claim but generalization not extracted

**Process:**
1. Identify single-case observation (e.g., "12/12 students owned smartphones")
2. Extract implicit generalization as claim (e.g., "Volunteers prefer mobile devices")
3. Mark `claim_status: "implicit"`
4. Set `extraction_flags.generalization_from_single_case: true`
5. Link observation → implicit claim → broader claim

**Document in change log:**
- New claim ID
- What observation prompted it
- Why it's implicit

### VERIFY → Quality checks

**Relationship verification:**
- Every claim has evidential support (claim IDs or evidence IDs)
- Support chains are logical (evidence → supporting → intermediate → core)
- No orphaned items (everything connected)

**Citation accuracy:**
- Verbatim quotes match source text exactly
- Page numbers correct
- No hallucinated content
- Consolidated text preserves meaning

**Boundary clarity:**
- Evidence/claim classifications defensible
- Uncertain items flagged `boundary_ambiguous`
- Professional judgment identified

**Completeness:**
- No important content from source text missed
- Implicit generalizations surfaced
- Project metadata properly separated

---

## Red Flags (Quality Issues to Watch For)

### Over-consolidation Warning Signs

- Merging items that need different expertise to assess
- Combining distinct quality dimensions
- Bundling claims with different scopes (project vs domain)
- Lumping evidence from different sources

**When in doubt:** Keep separate. Splitting beats over-lumping.

### Under-consolidation Warning Signs

- Multiple items describing same entity (map specs scattered)
- Excessive granularity without assessment benefit
- Compound judgments split artificially
- Related workflow steps kept apart

**When in doubt:** Apply acid test. Assess together or separately?

### Reclassification Errors

- Professional judgment left as evidence
- Direct observations classified as claims
- Implicit generalizations not flagged
- Boundary ambiguity not noted

**When in doubt:** Default to claim if expertise needed to assess

### Relationship Errors

- Claims without evidential support
- Orphaned items (no links)
- Circular support chains
- Broken links after consolidation

**When in doubt:** Every claim must have support path to evidence

---

## Decision Framework

```
1. Read item(s) being considered
   ↓
2. Apply ACID TEST: "Assess together or separately?"
   ↓
3. If TOGETHER:
   - Check: Same entity? Compound judgment? Joint capability? Single workflow?
   - YES → LUMP using appropriate heuristic
   - NO → Check for over-consolidation risk
   ↓
4. If SEPARATELY:
   - Check: Different claims? Different assessments? Different sources? Different concerns?
   - YES → SPLIT or keep separate
   - NO → Reconsider consolidation
   ↓
5. Document decision in change log
   ↓
6. Verify relationships updated correctly
```

---

## Quick Reference: Common Decisions

| Situation | Decision | Rationale |
|-----------|----------|-----------|
| Map scale + source + date | LUMP | Same entity specifications |
| "Accurate" + "Complete" statements | LUMP if both about same dataset | Compound quality judgment |
| Hours worked + Features produced | SPLIT | Different efficiency dimensions |
| Accuracy % + Completeness % | SPLIT | Independent quality dimensions |
| 5 automation features | LUMP | Joint capability |
| Staff task 1 + Staff task 2 + Staff task 3 | LUMP | Single workflow |
| Student device observation | SPLIT + ADD | Keep observation, add implicit claim |
| "Method X worked before" | REMOVE | Track record → project metadata |
| Timeline/phases | REMOVE | Context → project metadata |
| "Maps are accurate" | RECLASSIFY | Evidence → Claim (requires expertise) |

---

## Expected Outcomes

### Typical Pass 2 Reductions

**Target:** 15-20% reduction from Pass 1

**Breakdown:**
- ~10% moved to project_metadata (context items)
- ~5-10% consolidated (over-granular items)
- ~0-2% split (over-consolidated items)
- ~0-5% reclassified (boundary corrections)
- ~0-5% added (implicit generalizations)

**Example from Methods section:**
- Pass 1: 85 items
- Pass 2: 69 items (19% reduction)
- Operations: 27 consolidated, 10 moved to metadata, 3 added (implicit)

### Quality Indicators

**Good rationalization:**
- All major content preserved
- Appropriate granularity for assessment
- Clear support chains
- No hallucinations
- Defensible classifications
- Useful change log

**Poor rationalization:**
- Information lost
- Over-consolidated items need splitting later
- Weak/broken relationships
- Inconsistent classifications
- Unexplained decisions

---

## Remember

1. **Acid test is primary criterion** - Use it liberally
2. **Document everything** - Change log enables learning
3. **Preserve information** - Consolidate text, don't summarize
4. **When uncertain, keep separate** - Splitting beats over-lumping
5. **Every claim needs support** - Verify relationships after consolidation
6. **Check against source** - Don't hallucinate during consolidation
7. **Project context ≠ Evidence** - Move non-supportive items to metadata

---

**Document Status:** v1.0  
**Last Updated:** 2025-10-17  
**For use with:** extraction_prompt_pass2_v2.2.md  
**Full details in:** Pass 2 prompt (comprehensive version)