# Architecture Documentation

**Version:** 2.6
**Last Updated:** 2025-11-13

This document explains the architectural design of the Research Assessor skill, including design principles, rationale, and tradeoffs.

---

## Table of Contents

1. [Core Architecture](#core-architecture)
2. [Design Principles](#design-principles)
3. [Skill + Runtime Prompts Model](#skill--runtime-prompts-model)
4. [Seven-Pass Workflow](#seven-pass-workflow)
5. [Liberal-Consolidate Philosophy](#liberal-consolidate-philosophy)
6. [Object Type Hierarchy](#object-type-hierarchy)
7. [Cross-Reference System](#cross-reference-system)
8. [Infrastructure Assessment](#infrastructure-assessment)
9. [Schema Design](#schema-design)
10. [Tradeoffs and Limitations](#tradeoffs-and-limitations)

---

## Core Architecture

### System Overview

```
┌──────────────────────────────────────────────────────────────┐
│                     Research Assessor v2.6                    │
│                                                                │
│  ┌──────────────────┐         ┌──────────────────────────┐  │
│  │   Claude Skill   │         │   Extraction Prompts     │  │
│  │                  │         │   (Runtime Provided)     │  │
│  │  - Frameworks    │         │                          │  │
│  │  - Schema        │◄────────┤  - Pass 0: Metadata      │  │
│  │  - Examples      │         │  - Pass 1: C&E Liberal   │  │
│  │  - Checklists    │         │  - Pass 2: C&E Consol    │  │
│  │  - Infrastructure│         │  - Pass 3: RDMAP Expl    │  │
│  │                  │         │  - Pass 4: RDMAP Impl    │  │
│  │                  │         │  - Pass 5: RDMAP Consol  │  │
│  │                  │         │  - Pass 6: Infrastructure│  │
│  │                  │         │  - Pass 7: Validation    │  │
│  └──────────────────┘         └──────────────────────────┘  │
│                                                                │
└────────────────────────────────────────────────────────────────┘
                          │
                          ▼
         ┌────────────────────────────────────────┐
         │     Single JSON Document                │
         │   (Accumulates Across Passes)           │
         │                                         │
         │  - paper_metadata                       │
         │  - evidence[]                           │
         │  - claims[]                             │
         │  - implicit_arguments[]                 │
         │  - research_designs[]                   │
         │  - methods[]                            │
         │  - protocols[]                          │
         │  - infrastructure{}                     │
         └────────────────────────────────────────┘
```

### Key Components

**1. Skill Package (Stable)**
- Decision frameworks (evidence vs claims, tier assignment, consolidation patterns)
- Schema definitions (object structures, field requirements)
- Reference materials (checklists, expected information guides)
- Infrastructure guides (PIDs, FAIR principles, permits, funding)
- Examples (worked extractions)

**2. Extraction Prompts (Evolving)**
- Detailed extraction instructions (8 passes, ~6,000 lines total)
- Pass-specific philosophy and guidance
- Comprehensive examples
- Quality checklists
- Output specifications
- Provided by user at runtime from `extraction-system/prompts/`

**3. JSON Document (Accumulates)**
- Single source of truth
- Flows through all passes (0→1→2→3→4→5→6→7)
- Arrays/objects populated sequentially
- Complete provenance tracking
- Consolidation metadata for all merges
- Infrastructure assessment in dedicated object

---

## Design Principles

### 1. Separation of Stable and Evolving Components

**Principle:** Framework (stable) and implementation (evolving) should be separate.

**Implementation:**
- Skill contains stable decision frameworks (evidence-vs-claims, tier-assignment, PID-systems)
- Prompts contain evolving extraction guidance (updated through empirical testing)
- User provides prompts at runtime (from `extraction-system/prompts/`)

**Rationale:**
- Prompts refined through testing more frequently than core frameworks
- Skill repackaging expensive (stored in `.claude/skills/`)
- Separation enables experimentation without friction
- Infrastructure guidance updated independently (Phase 2 enhancements)

**Tradeoff:** Requires user to manage prompts separately, but gains flexibility and rapid iteration.

---

### 2. Progressive Disclosure

**Principle:** Load only what's needed when needed.

**Implementation:**
- Skill metadata always loaded (~100 tokens)
- SKILL.md loaded when skill triggers (~2,000 tokens v2.6)
- Reference files loaded only when Claude needs them:
  - `evidence-vs-claims-guide.md` (~2,500 tokens)
  - `tier-assignment-guide.md` (~1,100 tokens)
  - `pid-systems-guide.md` (~3,500 tokens)
  - `fair-principles-guide.md` (~4,000 tokens)
- Extraction prompts provided when needed (~400-1,200 tokens each)

**Rationale:**
- Context window is shared resource
- Most queries don't need full reference materials
- Load detailed guidance only for ambiguous cases
- Infrastructure guides loaded during Pass 6 only

**Example:**
- Simple C&E extraction: SKILL.md only (~2,000 tokens)
- Uncertain about compound claim: + evidence-vs-claims-guide.md Case 6 (~2,500 tokens)
- Infrastructure assessment: + pid-systems-guide.md + fair-principles-guide.md (~7,500 tokens)

---

### 3. Iterative Refinement Over Perfect First-Pass

**Principle:** Multi-pass extraction (liberal → consolidate) beats single perfect pass.

**Implementation:**
- **Liberal passes (1, 3, 4):** Over-extract (40-50% above final expected)
- **Consolidation passes (2, 5):** Refine (15-20% reduction target)
- Each pass has clear, simple goal
- Consolidation metadata documents ALL merges

**Rationale:**
- Missing items harder to find than consolidating extras
- Uncertainty better handled by inclusion than exclusion
- Rationalisation catches false positives
- LLMs better at critique than generation
- Empirically validated: RUN-08 achieved balanced extraction (159 items, ranked #3 of 7 runs)

**Evidence:** RepliCATS project achieved ~80% accuracy with multi-pass approach. Our testing shows 81% evidence mapping, 57% claim coverage with liberal-consolidate workflow.

---

### 4. Extraction vs. Assessment Separation

**Principle:** Extract what's there, don't judge quality during extraction.

**Implementation:**
- No quality scoring in extraction
- "Expected information missing" tracking, not "required information"
- Flag gaps, don't penalise
- Assessment happens post-extraction
- Infrastructure assessment scores (PID connectivity, FAIR compliance) based on presence/absence, not quality judgement

**Rationale:**
- Extraction requires accuracy, not judgement
- Quality assessment requires domain expertise
- Mixing extraction and assessment creates bias
- Transparent extraction enables multiple assessment frameworks
- Historical context matters (pre-2016 papers expected to score 0 FAIR)

**Example:** RDMAP extraction notes "TIDieR element 7 missing" but doesn't score paper lower. Infrastructure assessment notes "data availability statement missing" with historical context, scores FAIR F1 as 0/1.

---

### 5. Respect for Fieldwork Epistemology

**Principle:** Opportunistic adaptation is legitimate when transparently documented.

**Implementation:**
- Track "opportunistic_decisions" in methods/protocols
- Distinguish planned vs emergent research questions
- Capture "adaptive_procedures" with justification
- No penalty for post-hoc hypothesis formulation
- CARE principles assessment for Indigenous data contexts

**Rationale:**
- Fieldwork happens in uncontrolled settings
- Adaptation to field conditions is methodologically sound
- Transparency matters, not conformity to pre-registration
- Retrospective inference is the reality
- Indigenous data governance requires culturally appropriate protocols

**Contrast:** Clinical trial frameworks (CONSORT) assume pre-specification. We adapt for retrospective assessment of fieldwork-based research.

---

## Skill + Runtime Prompts Model

### Why This Architecture?

**Problem:** Traditional skill design embeds all instructions in skill package.

**Issue:** Extraction prompts evolve rapidly through testing:
- v2.0: Initial claims/evidence extraction
- v2.1: Boundary refinements
- v2.2: Two-pass workflow
- v2.3: Consolidation metadata
- v2.4: RDMAP integration (5-pass workflow)
- v2.5: Schema field name standardisation, bidirectional validation
- v2.6: Infrastructure assessment, 7-pass workflow

Each change would require skill repackaging and user reinstallation if prompts were embedded.

**Solution:** Separate stable framework from evolving prompts.

### What Goes Where?

**In Skill (Stable - `.claude/skills/research-assessor/`):**
- Core principles (evidence vs claims, tier logic, PID types)
- Schema definitions (object structures, canonical field names)
- Decision frameworks (consolidation patterns, tier assignment tests, FAIR scoring)
- Infrastructure guides (PID systems, FAIR principles, permits, funding)
- Worked examples (demonstrate principles, Case 6 compound claims)

**Runtime Prompts (Evolving - `extraction-system/prompts/`):**
- Detailed extraction steps (8 passes)
- Pass-specific philosophy (liberal vs consolidation mindset)
- Comprehensive examples (from diverse corpus)
- Quality checklists
- Output specifications
- Historical context guidance (pre-FAIR baseline)

### Benefits

**For Development:**
- ✅ Rapid prompt iteration without skill repackaging
- ✅ A/B testing different prompt approaches (e.g., Pass 6 decision trees)
- ✅ Domain-specific prompt variations (HASS vs STEM)
- ✅ User can maintain prompt versions
- ✅ Phase 2 infrastructure enhancements deployed without skill update

**For Users:**
- ✅ No reinstallation for prompt updates
- ✅ Explicit control over prompt versions (workflow specifies prompt files)
- ✅ Can customise prompts for specific needs
- ✅ Clear separation of framework and implementation
- ✅ Infrastructure guidance updates independent of core skill

**For Context Management:**
- ✅ Prompts loaded only when needed (per-pass)
- ✅ Skill references loaded only when uncertain
- ✅ Efficient token usage (~15,000-25,000 tokens per pass vs ~40,000 if all embedded)
- ✅ Scales to longer papers

### Workflow Pattern

```
User's Action                  Claude's Response
─────────────────────────────  ────────────────────────────────
1. Provides Pass 1 prompt      → Skill loaded (~2,000 tokens)
   + source text               → Prompt in context (~800 tokens)
                               → Follows liberal extraction guidance

2. Claude uncertain about      → Reads evidence-vs-claims-guide.md
   compound claim              → Case 6 guidance (~2,500 tokens)

3. Pass 1 complete            → Returns populated JSON
                               → Skill context released

4. Provides Pass 6 prompt      → Skill + infrastructure guides loaded
   + full paper                → (~9,500 tokens: skill + PID + FAIR)
                               → Assesses infrastructure

5. Extraction complete         → Returns complete JSON
                               → Skill context released
```

---

## Seven-Pass Workflow

### Pass Sequence and Responsibilities

```
Pass 0: Metadata
├─ Input: Paper front matter (title, authors, abstract, DOI)
├─ Output: paper_metadata populated
├─ Modifies: metadata only
└─ Leaves alone: All arrays

Pass 1: Claims/Evidence Liberal
├─ Input: Results/Discussion sections + Pass 0 JSON
├─ Output: evidence[], claims[], implicit_arguments[] populated
├─ Modifies: C&E arrays only
├─ Leaves alone: RDMAP arrays, infrastructure
└─ Philosophy: Over-capture (40-50% above final)

Pass 2: Claims/Evidence Consolidation
├─ Input: Pass 1 JSON + original source text
├─ Output: Refined C&E (15-20% reduction)
├─ Modifies: C&E arrays only
├─ Leaves alone: RDMAP arrays, infrastructure
└─ Philosophy: Consolidate when assessment impact identical

Pass 3: RDMAP Explicit
├─ Input: Methods section + Pass 2 JSON
├─ Output: research_designs[], methods[], protocols[] populated (explicit only)
├─ Modifies: RDMAP arrays only
├─ Leaves alone: C&E arrays, infrastructure
└─ Philosophy: Extract visible methodology statements

Pass 4: RDMAP Implicit
├─ Input: All sections + Pass 3 JSON
├─ Output: Additional RDMAP items (implied decisions)
├─ Modifies: RDMAP arrays only (adds to Pass 3)
├─ Leaves alone: C&E arrays, infrastructure
└─ Philosophy: Identify unstated but evident decisions

Pass 5: RDMAP Consolidation
├─ Input: Pass 3-4 combined JSON + source text
├─ Output: Refined RDMAP (15-20% reduction)
├─ Modifies: RDMAP arrays only
├─ Leaves alone: C&E arrays, infrastructure
└─ Philosophy: Consolidate, verify hierarchy, formalise relationships

Pass 6: Infrastructure Assessment
├─ Input: Full paper (data availability, funding, ethics, code) + Pass 5 JSON
├─ Output: infrastructure{} populated (PIDs, FAIR, reproducibility, permits, funding)
├─ Modifies: infrastructure object only
├─ Leaves alone: All arrays
└─ Philosophy: Assess reproducibility infrastructure, distinguish missing vs negative

Pass 7: Validation
├─ Input: Complete extraction (Passes 0-6)
├─ Output: Validation report (separate or embedded in extraction_notes)
├─ Modifies: Nothing (read-only)
├─ Leaves alone: All sections
└─ Philosophy: Verify integrity, flag issues by severity (CRITICAL/IMPORTANT/MINOR)
```

### Array Boundary Protection

**Critical invariant:** Each pass modifies ONLY its designated section.

**Implementation:**
- Pass 1-2: Modify `evidence`, `claims`, `implicit_arguments` ONLY
- Pass 3-5: Modify `research_designs`, `methods`, `protocols` ONLY
- Pass 6: Modify `infrastructure` ONLY
- Pass 7: Modify nothing (read-only validation)

**Rationale:**
- Prevents accidental overwrites
- Clear mental model for each pass
- Easy to verify correctness (count arrays before/after)
- Supports flexible pass ordering within stages

**Verification pattern:**
```bash
# Before Pass 3
jq '.research_designs | length' extraction.json  # Should be 0
# After Pass 3
jq '.research_designs | length' extraction.json  # Should be >0
jq '.evidence | length' extraction.json          # Should be UNCHANGED from Pass 2
```

---

## Liberal-Consolidate Philosophy

### The Two-Stage Pattern

**Stage 1: Liberal Extraction (Passes 1, 3, 4)**

**Mental model:** "When uncertain → extract"

**Implementation:**
- Over-capture by 40-50% (expected vs final)
- Preserve granularity (split rather than lump)
- Include borderline cases
- Mark extraction_confidence: low when uncertain
- Document uncertainties in extraction_notes

**Rationale:**
- Missing items harder to find post-extraction
- False positives cheaper than false negatives
- Pass 2/5 consolidation will refine
- Comprehensive coverage more important than precision in Pass 1

**Evidence:** RUN-08 Pass 1 extracted 62 RDMAP items, Pass 2 refined to 53 (14.5% reduction), demonstrating effective liberal-consolidate pattern.

---

**Stage 2: Consolidation (Passes 2, 5)**

**Mental model:** "Consolidate only when assessment impact identical"

**Acid test:** "Would I assess these items together or separately?"

**Implementation:**
- Review all Pass 1 items systematically
- Consolidate redundant/overlapping items (target 15-20% reduction)
- Refine boundaries (evidence vs claims, tier assignments)
- Verify/formalise cross-references
- Document ALL consolidations via consolidation_metadata

**Consolidation metadata structure:**
```json
"consolidation_metadata": {
  "consolidated_from": ["E042", "E043", "E044"],
  "consolidation_type": "temporal_sequence",
  "rationale": "Three observations of same phenomenon at different time points, assess together",
  "information_preserved": "All three time points and measurements retained in verbatim_quote"
}
```

**Rationale:**
- Reduces item count without losing information
- Improves structural coherence
- Provides complete traceability
- Supports quality assessment (can review consolidation decisions)

**Quality check:** 15-20% reduction typical. <10% suggests under-consolidation, >30% suggests information loss risk.

---

### Why Not Single-Pass Extraction?

**Alternative considered:** Single pass with perfect granularity.

**Problems:**
1. **Uncertainty paralysis:** When uncertain, must decide immediately (extract or skip)
2. **Asymmetric costs:** Missing items expensive, false positives cheap
3. **Granularity inconsistency:** Different extractors make different split/lump decisions
4. **No traceability:** Can't review what wasn't extracted

**Evidence against:** Single-pass extraction in preliminary testing showed ~30% lower recall, inconsistent granularity.

**Liberal-consolidate advantages:**
- Systematic review of ALL candidate items
- Consolidation decisions documented and reviewable
- Consistent granularity (consolidation pass standardises)
- Complete provenance (know what was merged and why)

---

## Object Type Hierarchy

### Claims & Evidence Hierarchy

```
Evidence (Minimally Interpreted)
    ├─ Observations
    ├─ Measurements
    ├─ Data points
    └─ Raw findings

Claims (Interpretations)
    ├─ Inferences from evidence
    ├─ Generalisations
    ├─ Causal assertions
    └─ Theoretical positions

Implicit Arguments (Unstated Assumptions)
    ├─ Logical implications
    ├─ Background assumptions
    ├─ Inferential leaps
    └─ Reasoning bridges
```

**Boundary principle:** Evidence becomes claim when interpretation added.

**Tier tests:**
- Evidence: "Could this be wrong without interpretation being invalid?" → YES = evidence
- Claim: "Does this interpret/generalise?" → YES = claim
- Implicit argument: "Is this stated explicitly?" → NO = implicit

---

### RDMAP Three-Tier Hierarchy

```
Research Designs (Strategic WHY)
    ├─ Research questions
    ├─ Theoretical frameworks
    ├─ Study scope decisions
    ├─ Reasoning approach (inductive/deductive/abductive)
    └─ Sampling strategy rationale
    │
    ↓ (implemented_by_methods)
    │
Methods (Tactical WHAT)
    ├─ Data collection approaches
    ├─ Sampling procedures
    ├─ Analysis methods
    ├─ Quality control
    └─ Triangulation strategies
    │
    ↓ (realized_through_protocols)
    │
Protocols (Operational HOW)
    ├─ Specific tools/instruments
    ├─ Parameter settings
    ├─ Step-by-step procedures
    ├─ Quality checks
    └─ Data recording formats
```

**Tier assignment tests:**
- WHY framed this way? → Research Design
- WHAT was done? → Method
- HOW specifically implemented? → Protocol

**Hierarchy relationships:**
- Designs enable Methods (`research_designs.implemented_by_methods[]` ↔ `methods.implements_designs[]`)
- Methods enable Protocols (`methods.realized_through_protocols[]` ↔ `protocols.realizes_methods[]`)
- Bidirectional consistency enforced in Pass 7 validation

---

## Cross-Reference System

### Reference Types

**1. Evidence → Claims**
- `evidence.supports_claims[]` → claim IDs
- `claims.supported_by_evidence[]` → evidence IDs
- Bidirectional (Pass 7 validates consistency)

**2. RDMAP Hierarchy**
- `research_designs.implemented_by_methods[]` → method IDs
- `methods.implements_designs[]` → design IDs
- `methods.realized_through_protocols[]` → protocol IDs
- `protocols.realizes_methods[]` → method IDs
- Bidirectional (Pass 7 validates)

**3. RDMAP → Claims/Evidence**
- `methods.generates_evidence[]` → evidence IDs
- `methods.tests_claims[]` → claim IDs
- Unidirectional (methods reference C&E, not vice versa)

**4. Infrastructure → All Objects**
- `infrastructure.pid_graph.*.references_objects[]` → any object IDs
- Unidirectional (PIDs reference objects, not vice versa)

### Cross-Reference Principles

**Simplicity:** String ID arrays only (no nested objects)

**Example:**
```json
"supported_by_evidence": ["E023", "E024", "E025"]
```

**NOT:**
```json
"supported_by_evidence": [
  {"evidence_id": "E023", "relationship_type": "direct"},
  {"evidence_id": "E024", "relationship_type": "indirect"}
]
```

**Rationale:**
- Simple structure easier to validate
- Relationship type often ambiguous in practice
- Can add relationship metadata later if needed
- Reduces schema complexity

**Bidirectional consistency:**
- If A references B, B must reference A (where applicable)
- Pass 7 validation checks all bidirectional pairs
- Auto-correction scripts available (`scripts/fix_references.py`)

---

## Infrastructure Assessment

### Four-Component Framework

**1. Persistent Identifiers (PIDs)**

**Types tracked:**
- Paper DOIs (primary publication)
- Data DOIs (datasets archived)
- Code DOIs (software/analysis scripts)
- Author ORCIDs (researcher identifiers)
- Funder PIDs (grant DOIs, Crossref Funder IDs)
- Vocabulary PIDs (controlled vocabularies, ontologies)

**PID connectivity score:** 0-6 (sum of 6 binary components)
- 0 = pre-FAIR baseline (typical 2005-2015)
- 1-2 = minimal adoption (paper DOI only)
- 3-4 = moderate (paper + data/code + ORCIDs)
- 5-6 = exemplary (comprehensive PID graph)

**PID graph structure:**
```json
"pid_graph": {
  "paper": {"doi": "10.1234/example", "references_objects": []},
  "datasets": [{"doi": "10.5281/zenodo.123", "references_objects": ["E001", "E002"]}],
  "code_repositories": [{"doi": "10.5281/zenodo.456", "github_url": "...", "references_objects": ["M010"]}],
  "author_identifiers": [{"orcid": "0000-0001-2345-6789", "author_name": "Smith, J."}],
  "funding": [{"funder_id": "10.13039/501100000923", "grant_number": "...", "grant_doi": null}],
  "controlled_vocabularies": []
}
```

---

**2. FAIR Principles Assessment**

**15-principle framework:**
- **Findable (F1-F4):** Metadata, identifiers, searchability, registration
- **Accessible (A1-A2):** Retrieval, long-term preservation
- **Interoperable (I1-I3):** Open formats, vocabularies, cross-references
- **Reusable (R1-R4):** Licences, provenance, standards, usability

**Scoring:** Each principle 0 (not met) or 1 (met) → 0-15 overall score

**Example scoring:**
```json
"fair_assessment": {
  "overall_score": 13,
  "detailed_scores": {
    "findable": {"F1": 1, "F2": 1, "F3": 1, "F4": 1},
    "accessible": {"A1": 1, "A2": 1},
    "interoperable": {"I1": 1, "I2": 1, "I3": 1},
    "reusable": {"R1": 1, "R2": 1, "R3": 1, "R4": 0}
  },
  "scoring_rationale": [
    "F1: Data DOI present (10.5281/zenodo.123)",
    "R4: No formal data reuse policy documented"
  ]
}
```

**Historical context:** Pre-2016 papers expected to score 0-3 (FAIR principles published 2016).

---

**3. Computational Reproducibility**

**5-level spectrum:**
- **Level 0:** None (no code/data mentioned)
- **Level 1:** Code only (GitHub link, no dependencies documented)
- **Level 2:** Code + dependencies (requirements.txt, environment.yml)
- **Level 3:** Containerised (Docker, Singularity)
- **Level 4:** Fully reproducible (Binder, Code Ocean, complete workflow)

**Assessment dimensions:**
- Environment specification (dependencies documented?)
- Analysis transparency (random seeds, parameters?)
- Workflow documentation (steps reproducible?)
- Alternative approaches explored?

**Example:**
```json
"computational_reproducibility": {
  "level": 2,
  "code_availability": {
    "available": true,
    "location": "https://github.com/example/repo",
    "archived": true,
    "archive_location": "https://doi.org/10.5281/zenodo.456"
  },
  "environment_specification": {
    "dependencies_documented": true,
    "format": "requirements.txt",
    "version_pinning": "partial"
  }
}
```

---

**4. Permits and Ethics**

**Components:**
- IRB/ethics approval numbers
- Fieldwork permits (archaeological, ecological)
- Indigenous data governance (CARE principles)
- Ancient DNA ethics (regional variation)

**CARE principles (Indigenous data):**
- **C**ollective benefit
- **A**uthority to control
- **R**esponsibility
- **E**thics

**Regional variation:** Ancient DNA ethics requirements vary (Australia > Europe).

**Example:**
```json
"permits_ethics": {
  "irb_approval": {"status": "approved", "number": "IRB-2023-456"},
  "fieldwork_permits": [{"type": "archaeological_excavation", "issuing_authority": "..."}],
  "care_principles_assessment": {
    "indigenous_data_present": true,
    "collective_benefit": "documented",
    "authority_to_control": "documented",
    "responsibility": "documented",
    "ethics": "documented"
  }
}
```

---

### Infrastructure Assessment Principles

**1. Distinguish missing from negative**
- Missing statement ≠ absence of practice
- Pre-FAIR papers: missing statements expected
- Document "not stated in paper" vs "explicitly stated as absent"

**2. Use specific examples**
- Every FAIR score justified with quote/reference
- PID connectivity: list all DOIs found
- Code availability: exact GitHub URL + archive DOI

**3. Consider historical context**
- Pre-2016: FAIR principles not yet published (0-3 score expected)
- 2016-2020: Transition era (increasing awareness)
- 2020+: FAIR widely adopted in funding requirements

**4. GitHub-only vs archived**
- GitHub-only: Scores FAIR A1 (basic access) but NOT A2 (preservation)
- Zenodo/Software Heritage: Scores both A1 and A2
- Penalty for non-archived code: -1 on A2

---

## Schema Design

### Canonical Field Names (v2.5+)

**Standardised across all objects:**
- `implemented_by_methods` (NOT child_methods, enables_methods)
- `implements_designs` (reverse reference)
- `realized_through_protocols` (NOT child_protocols)
- `implements_methods` plural (NOT implements_method singular)
- `supported_by` (NOT supported_by_evidence - field name implies type)

**Migration:** Schema v2.5 standardisation (2025-11-02) updated 376 field names across 7 papers.

---

### Required vs Optional Fields

**Always required:**
- `id` - Unique identifier (E001, C001, RD001, M001, P001)
- `location` - Where in paper this was extracted
- `extraction_confidence` - high/medium/low

**Often required:**
- `verbatim_quote` - Direct quote from paper (evidence, claims, RDMAP)
- Cross-reference arrays (bidirectional pairs required for validation)

**Optional:**
- `consolidation_metadata` - Only if item was consolidated in Pass 2/5
- `expected_information_missing` - Only if gaps identified
- `extraction_notes` - Only if uncertainties to document

---

### Schema Versioning

**Current:** v2.6

**Version history:**
- v2.0-2.1: Initial claims/evidence
- v2.2-2.3: Consolidation metadata, multi-dimensional evidence
- v2.4: RDMAP integration, 5-pass workflow
- v2.5: Field name standardisation, bidirectional validation
- v2.6: Infrastructure object, 7-pass workflow

**Breaking changes documented:** `archive/planning-completed/migration-log.md`

---

## Tradeoffs and Limitations

### Tradeoff 1: Liberal Extraction Cost

**Decision:** Over-extract by 40-50% in Pass 1/3/4.

**Cost:**
- Longer extraction time (~30% more vs single-pass)
- More items to review in Pass 2/5
- Higher initial item counts may seem excessive

**Benefit:**
- Higher recall (80%+ vs ~50% single-pass in testing)
- Systematic review ensures nothing missed
- Documented consolidation provides traceability

**Verdict:** Cost justified by recall improvement and traceability.

---

### Tradeoff 2: Simple Cross-References

**Decision:** String ID arrays only, no relationship metadata.

**Cost:**
- Can't distinguish "direct" vs "indirect" support
- No strength-of-relationship tracking
- Limited to binary present/absent

**Benefit:**
- Simple to validate (no nested object complexity)
- Easy to update (just add/remove IDs)
- Relationship nuance often ambiguous anyway

**Verdict:** Simplicity wins. Can enhance later if needed.

---

### Tradeoff 3: Skill + Runtime Prompts Architecture

**Decision:** Separate framework (skill) from instructions (prompts).

**Cost:**
- User must manage prompts separately
- More complex setup (8 prompt files)
- Risk of prompt/skill version mismatch

**Benefit:**
- Rapid prompt iteration without skill repackaging
- Explicit version control
- Efficient context usage
- Domain-specific customisation possible

**Verdict:** Flexibility and iteration speed outweigh setup complexity.

---

### Tradeoff 4: Infrastructure Assessment Scope

**Decision:** Assess PIDs, FAIR, reproducibility, permits (Pass 6).

**Cost:**
- Additional extraction time (~30 minutes)
- Requires full paper context (not section-by-section)
- FAIR scoring complexity (15 principles, historical context)

**Benefit:**
- Comprehensive reproducibility assessment
- Cross-paper comparisons (PID adoption trends)
- Policy-relevant metrics (FAIR compliance)
- Historical baseline (pre-FAIR era documentation)

**Verdict:** Infrastructure assessment critical for reproducibility research, cost justified.

---

### Limitation 1: Single Extractor Subjectivity

**Issue:** One extractor's interpretation, not inter-rater agreement.

**Mitigation:**
- Consolidation metadata documents decisions (reviewable)
- Liberal extraction captures borderline cases
- Validation pass flags quality issues
- Multi-run comparison study possible (Section 7 in active-todo-list.md)

**Future work:** Multi-extractor comparison to quantify variability.

---

### Limitation 2: Fieldwork Domain Specificity

**Issue:** Framework designed for fieldwork-based research (archaeology, ecology, ethnography).

**Domain assumptions:**
- Opportunistic adaptation legitimate
- Post-hoc hypothesis formulation acceptable
- Retrospective assessment common

**Generalisability:** May need adaptation for:
- Clinical trials (pre-registration expected)
- Laboratory experiments (controlled conditions)
- Computational modelling (reproducibility different standards)

**Mitigation:** RDMAP framework and infrastructure assessment generalise well. Claims/evidence framework universal.

---

### Limitation 3: Infrastructure Assessment Temporal Coverage

**Issue:** Can only assess what's documented in paper.

**Gaps:**
- Data/code deposited after publication (not visible)
- Institutional repositories not mentioned
- ORCIDs adopted retrospectively
- Grant DOIs added later

**Mitigation:**
- Document as "not stated in paper"
- Distinguish missing statements from negative assessments
- Historical context consideration (pre-FAIR baseline)

**Future work:** Supplement with external checks (DataCite API, ORCID API, repository searches).

---

### Limitation 4: Consolidation Subjectivity

**Issue:** "Assess together or separately?" judgement call.

**Mitigation:**
- Consolidation_metadata.rationale documents reasoning
- Acid test provides decision framework
- Pass 7 validation can flag aggressive consolidation (>30% reduction)
- Multi-run study (planned) will quantify variability

**Acceptance:** Some subjectivity inevitable in qualitative assessment. Traceability more important than perfect consistency.

---

## Future Directions

**Planned enhancements:**
1. Multi-run extraction comparison (quantify variability)
2. Software documentation structure (Pass 6 Phase 2)
3. Supplementary materials tracking (Pass 6 Phase 2)
4. Cross-paper PID adoption trend analysis
5. Automated cross-reference validation scripts
6. Domain-specific prompt variants (ecology, ethnography)

**Research questions:**
1. What is typical PID connectivity score by discipline and year?
2. How has FAIR compliance evolved in HASS fields (2005-2024)?
3. What consolidation rate indicates optimal granularity?
4. How much extraction variability is acceptable?
5. Can we predict replicability from extraction patterns?

**See planning/active-todo-list.md for detailed roadmap.**
