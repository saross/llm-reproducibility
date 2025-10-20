# Architecture Documentation

**Version:** 2.4  
**Last Updated:** 2025-10-20

This document explains the architectural design of the Research Assessor skill, including design principles, rationale, and tradeoffs.

---

## Table of Contents

1. [Core Architecture](#core-architecture)
2. [Design Principles](#design-principles)
3. [Skill + Runtime Prompts Model](#skill--runtime-prompts-model)
4. [Iterative Accumulation Workflow](#iterative-accumulation-workflow)
5. [Two-Pass Extraction Philosophy](#two-pass-extraction-philosophy)
6. [Object Type Hierarchy](#object-type-hierarchy)
7. [Cross-Reference System](#cross-reference-system)
8. [Schema Design](#schema-design)
9. [Controlled Vocabularies](#controlled-vocabularies)
10. [Tradeoffs and Limitations](#tradeoffs-and-limitations)

---

## Core Architecture

### System Overview

```
┌─────────────────────────────────────────────────────────────┐
│                      Research Assessor                       │
│                                                               │
│  ┌──────────────────┐         ┌─────────────────────────┐  │
│  │   Claude Skill   │         │   Extraction Prompts    │  │
│  │                  │         │    (Runtime Provided)    │  │
│  │  - Frameworks    │         │                          │  │
│  │  - Schema        │◄────────┤  - Pass 1: Liberal      │  │
│  │  - Examples      │         │  - Pass 2: Rationalize  │  │
│  │  - Checklists    │         │  - Pass 3: Validate     │  │
│  └──────────────────┘         └─────────────────────────┘  │
│                                                               │
└─────────────────────────────────────────────────────────────┘
                          │
                          ▼
         ┌────────────────────────────────────┐
         │     Single JSON Document            │
         │  (Accumulates Across Passes)        │
         │                                     │
         │  - evidence[]                       │
         │  - claims[]                         │
         │  - implicit_arguments[]             │
         │  - research_designs[]               │
         │  - methods[]                        │
         │  - protocols[]                      │
         └────────────────────────────────────┘
```

### Key Components

**1. Skill Package (Stable)**
- Decision frameworks
- Schema definitions
- Reference materials
- Examples

**2. Extraction Prompts (Evolving)**
- Detailed extraction instructions
- Pass-specific guidance
- Comprehensive examples
- Provided by user at runtime

**3. JSON Document (Accumulates)**
- Single source of truth
- Flows through all passes
- Arrays populated sequentially
- Complete provenance tracking

---

## Design Principles

### 1. Separation of Stable and Evolving Components

**Principle:** Framework (stable) and implementation (evolving) should be separate.

**Implementation:**
- Skill contains stable decision frameworks
- Prompts contain evolving extraction guidance
- User provides prompts at runtime

**Rationale:**
- Prompts refined through testing more frequently than core frameworks
- Skill repackaging expensive (user must reinstall)
- Separation enables experimentation without friction

**Tradeoff:** Requires user to manage prompts separately, but gains flexibility.

---

### 2. Progressive Disclosure

**Principle:** Load only what's needed when needed.

**Implementation:**
- Skill metadata always loaded (~100 tokens)
- SKILL.md loaded when skill triggers (~1,500 tokens)
- Reference files loaded only when Claude needs them (~1,000-2,000 tokens each)
- Extraction prompts provided when needed (~4,000-5,000 tokens each)

**Rationale:**
- Context window is a shared resource
- Most queries don't need full reference materials
- Load detailed guidance only for ambiguous cases

**Example:**
- Simple extraction: SKILL.md only (~1,500 tokens)
- Uncertain about tier: + tier-assignment-guide.md (~1,100 tokens)
- Need examples: + sobotkova-example.md (~1,400 tokens)

---

### 3. Iterative Refinement Over Perfect First-Pass

**Principle:** Two-pass extraction (liberal → rationalize) beats single perfect pass.

**Implementation:**
- Pass 1: Over-extract (40-50% more items)
- Pass 2: Consolidate (15-20% reduction)
- Each pass has clear, simple goal

**Rationale:**
- Missing items harder to find than consolidating extras
- Uncertainty better handled by inclusion than exclusion
- Rationalization catches false positives
- LLMs better at critique than generation

**Evidence:** RepliCATS project achieved ~80% accuracy with multi-pass approach.

---

### 4. Extraction vs. Assessment Separation

**Principle:** Extract what's there, don't judge quality during extraction.

**Implementation:**
- No quality scoring in extraction
- "Expected information missing" tracking, not "required information"
- Flag gaps, don't penalize
- Assessment happens post-extraction

**Rationale:**
- Extraction requires accuracy, not judgment
- Quality assessment requires domain expertise
- Mixing extraction and assessment creates bias
- Transparent extraction enables multiple assessment frameworks

**Example:** RDMAP extraction notes "TIDieR element 7 missing" but doesn't score paper lower.

---

### 5. Respect for Fieldwork Epistemology

**Principle:** Opportunistic adaptation is legitimate when transparent.

**Implementation:**
- Track "opportunistic_decisions" in methods/protocols
- Distinguish planned vs emergent research questions
- Capture "adaptive_procedures" with justification
- No penalty for post-hoc hypothesis formulation

**Rationale:**
- Fieldwork happens in uncontrolled settings
- Adaptation to field conditions is methodologically sound
- Transparency matters, not conformity to pre-registration
- Retrospective inference is the reality

**Contrast:** Clinical trial frameworks (CONSORT) assume pre-specification. We adapt for retrospective assessment.

---

## Skill + Runtime Prompts Model

### Why This Architecture?

**Problem:** Traditional skill design embeds all instructions in skill package.

**Issue:** Extraction prompts evolve rapidly through testing:
- v2.0: Initial design
- v2.1: Boundary refinements
- v2.2: Two-pass workflow
- v2.3: Consolidation metadata
- v2.4: RDMAP integration

Each change required skill repackaging and user reinstallation.

**Solution:** Separate stable framework from evolving prompts.

### What Goes Where?

**In Skill (Stable):**
- Core principles (evidence vs claims, tier logic)
- Schema definitions (object structures)
- Decision frameworks (when to consolidate, assign tiers)
- Worked examples (demonstrate principles)

**Runtime Prompts (Evolving):**
- Detailed extraction steps
- Pass-specific philosophy
- Comprehensive examples
- Quality checklists
- Output specifications

### Benefits

**For Development:**
- ✅ Rapid prompt iteration without skill repackaging
- ✅ A/B testing different prompt approaches
- ✅ Domain-specific prompt variations
- ✅ User can maintain prompt versions

**For Users:**
- ✅ No reinstallation for prompt updates
- ✅ Explicit control over prompt versions
- ✅ Can customize prompts for their needs
- ✅ Clear separation of framework and implementation

**For Context Management:**
- ✅ Prompts loaded only when needed
- ✅ Skill references loaded only when uncertain
- ✅ Efficient token usage
- ✅ Scales to longer papers

### Workflow Pattern

```
User's Action                 Claude's Response
────────────────────────────  ───────────────────────────────
1. Provides extraction        → Skill loaded (~1,500 tokens)
   prompt + source text       → Prompt in context (~4,000 tokens)
                              → Follows prompt instructions

2. Claude uncertain about     → Reads tier-assignment-guide.md
   tier assignment            → (~1,100 tokens additional)

3. Extraction complete        → Returns populated JSON
                              → Skill context released
```

---

## Iterative Accumulation Workflow

### Single Document Through All Passes

**Core Idea:** One JSON document flows through all passes, accumulating content.

```
┌─────────────────┐
│ Blank Template  │
│  - evidence: [] │
│  - claims: []   │
│  - RDMAP: []    │
└────────┬────────┘
         ↓
┌─────────────────────────────┐
│ Claims Pass 1 (Liberal)     │
│  Populates: evidence, claims│
│  Preserves: RDMAP[]         │
└────────┬────────────────────┘
         ↓
┌─────────────────────────────┐
│ Claims Pass 2 (Rationalize) │
│  Refines: evidence, claims  │
│  Preserves: RDMAP[]         │
└────────┬────────────────────┘
         ↓
┌─────────────────────────────┐
│ RDMAP Pass 1 (Liberal)      │
│  Populates: RDMAP           │
│  Preserves: evidence, claims│
└────────┬────────────────────┘
         ↓
┌─────────────────────────────┐
│ RDMAP Pass 2 (Rationalize)  │
│  Refines: RDMAP             │
│  Preserves: evidence, claims│
└────────┬────────────────────┘
         ↓
┌─────────────────────────────┐
│ Pass 3 (Validation)         │
│  Reads: All arrays          │
│  Modifies: Nothing          │
│  Produces: Validation report│
└─────────────────────────────┘
```

### Advantages

**For Production:**
- ✅ Single source of truth throughout
- ✅ No merging step required
- ✅ Cross-references can be validated early
- ✅ Complete provenance tracking
- ✅ Simpler pipeline architecture

**For Testing:**
- ✅ Can test any pass independently
- ✅ Can start with blank or partially-populated
- ✅ Can validate partial extractions
- ✅ Flexible debugging

**For Users:**
- ✅ One file to manage
- ✅ Clear state at each stage
- ✅ Easy to pause and resume
- ✅ Complete audit trail

### Array Boundaries

**Critical Rule:** Each pass has clear boundaries.

**Claims/Evidence Passes:**
- ✅ Touch: `evidence`, `claims`, `implicit_arguments`
- ❌ Don't touch: `research_designs`, `methods`, `protocols`

**RDMAP Passes:**
- ✅ Touch: `research_designs`, `methods`, `protocols`
- ❌ Don't touch: `evidence`, `claims`, `implicit_arguments`

**Validation Pass:**
- ✅ Read: All arrays
- ❌ Don't modify: Anything (produces separate report)

**Why strict boundaries?**
- Prevents accidental data loss
- Clear responsibility per pass
- Enables independent pass testing
- Reduces cognitive load

---

## Two-Pass Extraction Philosophy

### Pass 1: Liberal Extraction

**Goal:** Comprehensive capture, err on side of inclusion.

**Strategy:**
- Over-extract by 40-50%
- Preserve granularity
- Mark uncertainties
- Include borderline cases

**Rationale:**
- Missing items hard to discover later
- Consolidation easier than discovery
- Uncertainty best handled by inclusion
- Pass 2 will rationalize

**Example:**
```
Source: "GPS coordinates recorded with RTK correction for improved accuracy"

Pass 1 might extract:
- E042: "GPS coordinates recorded"
- E043: "RTK correction applied"
- E044: "Improved accuracy achieved"

Pass 2 will consolidate appropriately.
```

### Pass 2: Rationalization

**Goal:** Refine quality, reduce over-extraction by 15-20%.

**Operations:**
- CONSOLIDATE: Redundant items
- SPLIT: Over-consolidated items
- RECLASSIFY: Boundary errors
- VERIFY: Relationships
- DOCUMENT: All changes via consolidation metadata

**Rationale:**
- Quality improvement through review
- Granularity matching to assessment needs
- Traceability of decisions
- Second look catches errors

**Example:**
```
Pass 1 items (above):
- E042, E043, E044

Pass 2 consolidated:
- E042: "GPS coordinates recorded with RTK correction for improved accuracy"
  - consolidation_metadata: {
      consolidated_from: ["E042", "E043", "E044"],
      consolidation_type: "procedure_chain",
      rationale: "Related procedure elements assessed as unit"
    }
```

### Consolidation Decision Framework

**Acid Test:** "Would I assess these items TOGETHER or SEPARATELY?"

- Together → Consolidate
- Separately → Keep distinct

**Lumping Patterns:** (12 identified)
- Sequential procedures
- Instrument + configuration
- Measurement + unit
- And 9 more (see consolidation-patterns.md)

**Splitting Patterns:** (6 identified)
- Over-aggregation
- Multiple distinct claims in one
- Temporal progression separated
- And 3 more (see consolidation-patterns.md)

### Why Two Passes Works

**Cognitive Load:**
- Single task per pass (extract OR rationalize)
- Clear success criteria per pass
- Reduces decision paralysis

**Error Correction:**
- Pass 1 errors caught in Pass 2
- Review catches what generation missed
- Different mindset per pass

**LLM Strengths:**
- Generation benefits from permissiveness
- Critique benefits from standards
- Two passes leverage both modes

---

## Object Type Hierarchy

### Six Object Types in Three Categories

**Claims & Evidence:**
```
evidence          → Raw observations, measurements
claims           → Interpretations, generalizations
implicit_arguments → Unstated assumptions, logical implications
```

**RDMAP (Research Design, Methods, Protocols):**
```
research_designs  → Strategic decisions (WHY framed this way)
methods          → Tactical approaches (WHAT was done)
protocols        → Operational procedures (HOW specifically)
```

### Three-Tier RDMAP Hierarchy

**Design (Strategic):**
- Research questions and hypotheses
- Theoretical frameworks
- Study design choices
- Scope definitions
- Positionality statements

**Test:** "Is this about framing and rationale?"

**Methods (Tactical):**
- Data collection approaches
- Sampling strategies
- Analysis techniques
- Quality control approaches
- Temporal frameworks

**Test:** "Is this the general approach at high level?"

**Protocols (Operational):**
- Specific procedures
- Tool configurations
- Parameter specifications
- Step-by-step instructions
- Measurement details

**Test:** "Could someone replicate from this level of detail?"

### Why Three Tiers?

**Assessment Granularity:**
- Design: Assess appropriateness of framing
- Methods: Assess validity of approach
- Protocols: Assess replicability of execution

**Hierarchical Relationships:**
- Designs enable methods
- Methods realized through protocols
- Clear parent-child relationships

**Reporting Standards:**
- Maps to TIDieR, CONSORT, SPIRIT frameworks
- Matches how researchers think about methodology
- Supports structured assessment

### Boundary Cases

**Design vs. Method:**
- "Comparative survey design" → Design (strategic choice)
- "Survey data collection" → Method (tactical approach)
- **Test:** Could we execute THIS design with DIFFERENT methods? If yes → Design

**Method vs. Protocol:**
- "Total station survey" → Method (general approach)
- "Leica TS15 configured with 5mm precision" → Protocol (specific procedure)
- **Test:** Does THIS give enough detail to replicate? If not → Method, if yes → Protocol

---

## Cross-Reference System

### Simple String ID Arrays

**Design Choice:** Cross-references are arrays of string IDs.

```json
{
  "method_id": "M008",
  "implements_designs": ["RD001", "RD002"],
  "realized_through_protocols": ["P023", "P024", "P025"],
  "validated_by_evidence": ["E046", "E047"]
}
```

### Why Simple String Arrays?

**Alternatives Considered:**
1. **Nested objects:** `{"designs": [{nested design objects}]}`
2. **Relationship objects:** `[{from: "M008", to: "RD001", type: "implements"}]`
3. **Database-style foreign keys**

**Chosen:** Simple string ID arrays

**Rationale:**
- ✅ Minimal token overhead
- ✅ Human-readable
- ✅ Easy to validate
- ✅ Simple to manipulate
- ✅ Sufficient for assessment needs

**Tradeoff:** Requires ID dereferencing for full object, but that's acceptable.

### Bidirectional Consistency

**Rule:** All cross-references must be bidirectional.

**Example:**
```json
// Method M008 implements Design RD001
{
  "method_id": "M008",
  "implements_designs": ["RD001"]
}

// Design RD001 is implemented by Method M008
{
  "design_id": "RD001",
  "implemented_by_methods": ["M008"]
}
```

**Validation:** Pass 3 checks bidirectional consistency.

### Cross-Reference Types

**RDMAP Hierarchy:**
- Designs → Methods: `enables_methods` / `implements_designs`
- Methods → Protocols: `realized_through_protocols` / `implements_methods`

**RDMAP → Claims:**
- Designs → Claims: `informs_claims` / `supports_design`
- Methods → Claims: `justification_claim` / `supports_method`
- Protocols → Claims: `justification_claim` / `supports_protocol`

**Claims → Evidence:**
- Claims → Evidence: `supported_by_evidence` / `supports_claims`
- Claims → Claims: `supported_by_claim` (claim chains)

**Implicit Arguments → Everything:**
- Implicit Arguments → Designs: `supports_design`
- Implicit Arguments → Methods: `supports_method`
- Implicit Arguments → Protocols: `supports_protocol`
- Implicit Arguments → Claims: `enables_claim`

---

## Schema Design

### Core Schema Principles

**1. Required vs. Optional Fields**

**Always Required:**
- ID (primary key)
- Text (human-readable content)
- Type (controlled vocabulary)

**Often Optional:**
- Type-specific structures (depend on type value)
- Cross-references (not all objects relate to all others)
- Consolidation metadata (only for consolidated items)

**2. Type-Specific Conditional Structures**

```json
{
  "method_id": "M008",
  "method_type": "sampling",
  
  // Only populated if method_type = "sampling"
  "sampling_strategy": {
    "type": "stratified",
    "rationale": "...",
    "target_population": "..."
  }
}
```

**Rationale:** Avoids bloat for non-applicable structures.

**3. Standard Fields on All Objects**

```json
{
  "location": {"section": "...", "page": X, "paragraph": Y},
  "verbatim_quote": "...",
  "extraction_confidence": "high|medium|low",
  "extraction_notes": "...",
  "expected_information_missing": ["..."]
}
```

**Rationale:** Consistent traceability and transparency across all extractions.

### Schema Evolution Strategy

**Current State (v2.4):**
- Mix of controlled vocabularies (enums) and open text
- Empirical vocabulary building

**Future Direction:**
- Build controlled vocabularies from actual usage
- Start with archaeology (testing domain)
- Expand to other fieldwork domains
- Maintain "other (specify)" escape hatches

**Example Evolution:**
```
v2.4: study_design: "string" (open text)
v2.5: study_design: enum["comparative", "case_study", ...] + "other"
v3.0: Domain-specific enums per discipline
```

---

## Controlled Vocabularies

### Vocabulary Philosophy

**Principle:** Start open, formalize empirically.

**Current Approach:**
- Core types controlled (claim_type, reasoning_approach)
- Domain-specific terms open (study_design, sampling_strategy)
- Build vocabularies through usage
- Accept free text initially

**Rationale:**
- Unknown unknowns in new domains
- Premature formalization constrains discovery
- Real usage reveals actual patterns
- Always provide "other (specify)" option

### Core Controlled Vocabularies (v2.4)

**Claim Types:**
- `empirical` - About observed patterns
- `interpretation` - About meaning
- `methodological_argument` - Justifying method choices
- `theoretical` - About concepts

**Reasoning Approaches:**
- `inductive` - Pattern discovery
- `abductive` - Inference to best explanation
- `deductive` - Hypothesis testing
- `mixed` - Multiple approaches
- `unclear` - Not explicitly stated

**Extraction Confidence:**
- `high` - Clear and explicit in text
- `medium` - Requires inference
- `low` - Highly uncertain

### Evolving Open Vocabularies

**Research Designs:**
- study_design: "comparative", "case_study", "longitudinal", etc.
- Open list, domain-specific
- Build from archaeology first

**Methods:**
- data_collection approaches: "survey", "excavation", "interview", etc.
- sampling strategies: "stratified", "purposive", "convenience", etc.
- Open lists, empirically refined

**Protocols:**
- recording, measurement, analysis_procedure, etc.
- Very domain-specific
- Formalize later

---

## Tradeoffs and Limitations

### Current Limitations

**1. Optimized for Fieldwork Research**

**Strength:** Respects fieldwork epistemology, handles opportunistic adaptation
**Limitation:** May not suit controlled experiments or computational studies
**Mitigation:** Domain extensions planned (v2.5+)

**2. Archaeology-Focused Examples**

**Strength:** Deep understanding of one domain
**Limitation:** Other domains need adapted examples
**Mitigation:** Community contributions welcome

**3. English-Only**

**Strength:** Consistent processing
**Limitation:** Non-English papers need translation
**Mitigation:** Extraction supports any language, but prompts in English

**4. Manual Pass Management**

**Strength:** Full user control
**Limitation:** Requires multiple LLM calls
**Mitigation:** Automation possible later (outside skill scope)

**5. No Quality Scoring**

**Strength:** Separates extraction from assessment
**Limitation:** Users must develop own assessment frameworks
**Mitigation:** Assessment framework planned (v2.5)

### Architectural Tradeoffs

**Skill + Runtime Prompts:**
- ✅ Gains: Flexibility, iteration speed
- ❌ Loses: Self-contained skill
- **Verdict:** Worth it for development velocity

**Two-Pass Extraction:**
- ✅ Gains: Quality, error correction
- ❌ Loses: Requires two LLM calls
- **Verdict:** Worth it for accuracy

**Simple Cross-References:**
- ✅ Gains: Simplicity, token efficiency
- ❌ Loses: Rich relationship metadata
- **Verdict:** Sufficient for current needs

**Iterative Accumulation:**
- ✅ Gains: Single source of truth
- ❌ Loses: Parallel extraction capability
- **Verdict:** Worth it for provenance

---

## Future Architectural Directions

### Planned Enhancements (v2.5+)

**1. Assessment Framework**
- Scoring rubrics for transparency
- Replicability indicators
- Quality metrics
- Separate from extraction (maintains separation)

**2. Domain Extensions**
- Ecology-specific adaptations
- Ethnography-specific adaptations
- Biology field study adaptations
- Shared core, domain variants

**3. Automation Layer**
- Batch processing support
- Automated pass sequencing
- Progress tracking
- Outside skill, uses skill

**4. Validation Enhancement**
- Domain-specific validation rules
- Completeness patterns
- Temporal consistency checks
- Statistical validation

### Research Questions

**Architecture Research:**
- How does extraction quality scale to longer papers?
- What's optimal chunking strategy for papers >50 pages?
- Can we parallelize passes safely?
- How to handle multi-paper comparative analysis?

**Schema Research:**
- What controlled vocabularies emerge from usage?
- How do domains differ in RDMAP structure?
- What cross-reference patterns predict quality?
- How should temporal relationships be modeled?

---

**For implementation details, see:**
- [USAGE_GUIDE.md](USAGE_GUIDE.md) - How to use the architecture
- [PROMPT_REVISION_SUMMARY.md](PROMPT_REVISION_SUMMARY.md) - How architecture evolved
- [TESTING.md](TESTING.md) - How architecture was validated
