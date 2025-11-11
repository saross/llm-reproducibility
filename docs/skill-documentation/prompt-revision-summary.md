# Prompt Revision Summary

**Version:** 2.4  
**Development Period:** 2025-10-16 to 2025-10-20  
**Status:** Complete and Production Ready

This document chronicles the development of the five extraction prompts (~4,400 lines total) from initial concept through empirical testing to production release.

---

## Executive Summary

**What We Built:**
- Five extraction prompts for systematic research methodology assessment
- Two-pass workflow (liberal → rationalize) with validation
- Three-tier RDMAP hierarchy (Design → Method → Protocol)
- Complete cross-reference architecture across six object types

**How We Built It:**
- Iterative empirical testing on real research paper (Sobotkova et al. 2023)
- Evidence-driven refinement based on extraction quality
- Consolidation patterns discovered through rationalization practice
- Architectural decisions informed by RepliCATS and registration frameworks

**Key Achievements:**
- 15-20% reduction through Pass 2 rationalization (target met)
- Complete traceability via consolidation metadata
- Three-tier hierarchy working correctly
- Cross-reference integrity maintained
- Expected information tracking functional

---

## Development Timeline

### Phase 1: Initial Concept (v2.0) - October 16

**Goal:** Proof of concept for claims/evidence extraction.

**Delivered:**
- Single extraction prompt (~400 lines)
- Basic schema (evidence, claims, implicit_arguments)
- Simple cross-references

**Testing:**
- Sobotkova Results section extraction
- Established baseline extraction approach

**Outcome:**  ✅ Concept validated, but over-extraction problematic

---

### Phase 2: Two-Pass Workflow (v2.2) - October 17

**Goal:** Address over-extraction through rationalization.

**Key Decision:** Liberal Pass 1 + Rationalization Pass 2

**Rationale:**
- LLMs better at generation with permissiveness
- Critique (Pass 2) catches what generation (Pass 1) missed
- Missing items harder to discover than consolidating extras
- Inspired by RepliCATS multi-pass success

**Delivered:**
- Claims/Evidence Pass 1 prompt (~800 lines)
- Claims/Evidence Pass 2 prompt (~850 lines)
- Consolidation decision framework
- 12 lumping patterns + 6 splitting patterns

**Testing:**
- Sobotkova Methods section
- Pass 1: 46 evidence, 32 claims (comprehensive)
- Pass 2: 37 evidence, 26 claims (15-20% reduction ✓)

**Outcome:** ✅ Two-pass workflow successful

---

### Phase 3: Consolidation Metadata (v2.3) - October 18

**Goal:** Complete traceability of rationalization decisions.

**Problem Discovered:**
- Consolidations in Pass 2 lacked explanation
- Couldn't verify information preservation
- Assessment unclear which items were combined

**Solution:** Consolidation metadata on all consolidated items.

**Structure:**
```json
"consolidation_metadata": {
  "consolidated_from": ["E042", "E043", "E044"],
  "consolidation_type": "procedure_chain",
  "information_preserved": "All GPS procedure steps maintained",
  "rationale": "Sequential procedure elements assessed as unit"
}
```

**Additional Enhancement:** Multi-dimensional evidence pattern.

**Testing:**
- Validated on Sobotkova Results section
- Confirmed information preservation
- Clear consolidation rationale

**Outcome:** ✅ Complete traceability achieved

---

### Phase 4: RDMAP Integration (v2.4) - October 19-20

**Goal:** Systematic methodology extraction (Research Design, Methods, Protocols).

**Challenge:** Three-tier hierarchy needs clear boundaries.

**Solution Development:**

**Step 1: Vocabulary Decisions**
- Reasoning: inductive/abductive/deductive (NOT exploratory/confirmatory)
  - Why: Aligns with philosophical tradition, clearer than vague "exploratory"
- Research questions vs hypotheses: Separate tracking
  - Why: Fieldwork often has emergent RQs, not pre-specified hypotheses
- Study designs: Open list
  - Why: Domain-specific, build empirically

**Step 2: Expected Information Frameworks**
- Adapted TIDieR for methods (10 elements)
- Adapted CONSORT-Outcomes for protocols (8 elements)
- Created sampling strategy checklist (7 elements)
- Created analysis methods checklist (7 elements)

**Step 3: Fieldwork-Specific Adaptations**
- Opportunistic decisions tracking (legitimate in fieldwork)
- Contingency plans (planned vs actual)
- Adaptive procedures with justification
- Emergent discoveries documentation

**Delivered:**
- RDMAP Pass 1 prompt (~1,000 lines)
  - 6 comprehensive archaeology examples
  - Three-tier decision framework
  - Expected information checklists
  - Liberal extraction philosophy
  
- RDMAP Pass 2 prompt (~900 lines)
  - Tier-specific consolidation patterns
  - Cross-reference formalization
  - Hierarchy validation
  - Completeness assessment

- Validation Pass 3 prompt (~600 lines)
  - Unified validation across all six object types
  - Cross-reference integrity checks
  - Hierarchy validation
  - Schema compliance verification
  - Flexible validation (adapts to partial extractions)

**Testing:**
- Sobotkova Methods section full extraction
- Three-tier hierarchy validated
- Cross-references working
- Expected information gaps identified

**Outcome:** ✅ Complete RDMAP framework functional

---

## Prompt Statistics

### Line Counts by Version

| Version | Claims P1 | Claims P2 | RDMAP P1 | RDMAP P2 | Valid P3 | Total  |
|---------|-----------|-----------|----------|----------|----------|--------|
| v2.0    | 400*      | -         | -        | -        | -        | 400    |
| v2.2    | 800       | 850       | -        | -        | -        | 1,650  |
| v2.3    | 800       | 900       | -        | -        | -        | 1,700  |
| v2.4    | 830       | 920       | 1,000    | 900      | 600      | 4,250  |

*Single prompt pre-two-pass split

### Reduction Through Rationalization

**Target:** 15-20% reduction from Pass 1 to Pass 2

**Achieved:**

| Test | Pass 1 Items | Pass 2 Items | Reduction | Status |
|------|--------------|--------------|-----------|--------|
| Sobotkova Methods (v2.2) | 78 | 63 | 19% | ✓ |
| Sobotkova Results (v2.3) | 85 | 68 | 20% | ✓ |
| Sobotkova Methods RDMAP (v2.4) | 68 | 55 | 19% | ✓ |

**Conclusion:** Rationalization consistently achieves target reduction.

---

## Key Design Decisions

### Decision 1: Skill + Runtime Prompts Architecture

**When:** v2.4 development

**Problem:** Prompts evolved rapidly (v2.0 → v2.4 in 4 days). Each change required:
1. Repackaging skill
2. User reinstallation
3. Version management friction

**Solution:** Separate skill (stable framework) from prompts (evolving guidance).

**Tradeoff:**
- ✅ Gains: Rapid iteration, user control, experimentation
- ❌ Loses: Self-contained skill

**Verdict:** Worth it for development velocity.

---

### Decision 2: Iterative Accumulation Workflow

**When:** v2.4 RDMAP integration

**Alternatives Considered:**
1. Separate JSONs for claims/RDMAP, merge at end
2. Nested extraction with claims inside RDMAP
3. Parallel extraction with merge step

**Chosen:** Single JSON flows through all passes.

**Rationale:**
- Single source of truth
- No merge complexity
- Easier provenance tracking
- Cross-references work naturally

**Tradeoff:**
- ✅ Gains: Simplicity, traceability
- ❌ Loses: Parallel extraction capability

**Verdict:** Worth it for provenance.

---

### Decision 3: Simple String ID Cross-References

**When:** v2.0 initial design

**Alternatives Considered:**
1. Nested objects: `{"designs": [{full design object}]}`
2. Relationship objects: `[{from: "M008", to: "RD001", type: "implements"}]`
3. Graph database approach

**Chosen:** Simple string arrays: `"implements_designs": ["RD001", "RD002"]`

**Rationale:**
- Minimal tokens
- Human-readable
- Easy to validate
- Sufficient for assessment

**Tradeoff:**
- ✅ Gains: Simplicity, efficiency
- ❌ Loses: Rich relationship metadata

**Verdict:** Sufficient for current needs, can enhance later if needed.

---

### Decision 4: Open vs. Controlled Vocabularies

**When:** v2.4 RDMAP development

**Approach:** Start open, formalize empirically.

**Controlled (v2.4):**
- Reasoning approaches (5 values)
- Extraction confidence (3 values)
- Claim types (4 values)

**Open (v2.4):**
- Study designs (domain-specific)
- Sampling strategies (context-dependent)
- Method types (evolving)

**Rationale:**
- Unknown unknowns in new domains
- Premature formalization constrains
- Real usage reveals patterns
- Always provide "other (specify)"

**Plan:** Build v2.5 controlled vocabularies from v2.4 usage.

---

### Decision 5: Expected Information ≠ Required Information

**When:** v2.4 RDMAP development

**Key Insight:** "Expected" is descriptive, "Required" is prescriptive.

**Implementation:**
- Track gaps as `expected_information_missing`
- Flag missing elements
- Don't penalize during extraction
- Assessment happens later

**Rationale:**
- Extraction accuracy vs. quality judgment
- Different domains have different standards
- Transparency about gaps matters, not scoring
- Enables multiple assessment frameworks

---

## Consolidation Patterns Discovered

### Through Empirical Testing

**12 Lumping Patterns Identified:**

1. **Sequential procedures** - GPS → RTK correction → Accuracy check
2. **Measurement + precision** - "Total station survey at 5mm precision"
3. **Instrument + configuration** - "Leica TS15 with 1" angular accuracy"
4. **Method + rationale** - Combining approach and justification
5. **Protocol + validation** - Procedure and its verification
6. **Temporal sequence** - Events in chronological order
7. **Compound measurements** - Multi-dimensional observations
8. **Causal chain** - Cause → Mechanism → Effect
9. **Hierarchical relationship** - Parent with immediate children
10. **Validation chain** - Primary → Secondary → Tertiary validation
11. **Spatial unit + measurement** - Location and its properties
12. **Tool + output** - Instrument and what it produces

**6 Splitting Patterns Identified:**

1. **Over-aggregation** - Multiple distinct concepts forced together
2. **Temporal progression** - Changes over time need separation
3. **Different assessment purposes** - Assessed independently not together
4. **Multi-claim lumping** - Multiple interpretations in single item
5. **Causality mixed with description** - Separate observation from explanation
6. **Professional judgment buried** - Expertise claim hidden in data

**Impact:** Pass 2 prompts incorporate these patterns for consistent consolidation.

---

## Errors Caught and Fixed

### Error 1: Factual Inaccuracies in Rationalization

**Discovered:** Pass 2 introduced factual errors (wrong student count, wrong year).

**Root Cause:** Source text not provided to rationalization pass.

**Fix:** Always provide source section text to Pass 2.

**Lesson:** Context management critical for accuracy.

---

### Error 2: Array Boundary Violations

**Discovered:** Early v2.4 RDMAP prompts modified claims/evidence arrays.

**Root Cause:** Unclear instructions about array boundaries.

**Fix:** Explicit "touch these, don't touch those" instructions in every prompt.

**Lesson:** Make boundaries unmistakably clear.

---

### Error 3: Cross-Reference Orphans

**Discovered:** Some cross-references pointed to non-existent IDs.

**Root Cause:** Consolidation updated items but not references to them.

**Fix:**
- Pass 2 prompts explicitly require updating all references
- Pass 3 validation checks bidirectional consistency
- Example consolidation metadata shows reference updates

**Lesson:** Cross-reference updates must be explicit in rationalization.

---

### Error 4: Over-Consolidation Losing Detail

**Discovered:** Some Pass 2 consolidations lost critical details.

**Root Cause:** Unclear guidance on information preservation.

**Fix:**
- `information_preserved` field in consolidation metadata
- Explicit examples showing preservation
- Splitting patterns for over-consolidation

**Lesson:** Preservation verification as important as consolidation decision.

---

## Testing Insights

### From Sobotkova et al. (2023)

**Why This Paper:**
- Representative fieldwork complexity
- Multi-method archaeological survey
- Well-documented methodology
- Opportunistic adaptations present
- Published and peer-reviewed

**What We Learned:**

**1. Liberal Extraction Works**
- 40-50% over-extraction acceptable
- Rationalization catches false positives
- Missing items hard to find later

**2. Tier Assignment Needs Practice**
- Design vs. Method boundary subtle
- Examples essential for calibration
- "Why/What/How" test mostly works

**3. Expected Information Valuable**
- TIDieR/CONSORT-Outcomes adapted well
- Gaps reveal transparency issues
- Different domains need different checklists

**4. Cross-References Essential**
- Enable traceability
- Support assessment
- Bidirectional consistency critical

**5. Consolidation is an Art**
- No perfect algorithm
- Domain expertise helps
- Acid test ("assess together?") works well

---

## Prompt Engineering Lessons

### What Works

**1. Clear Structure**
- Numbered sections
- "Remember" boxes at end
- Quality checklists
- Comprehensive examples

**2. Decision Trees**
- Tests at decision points
- "If X then Y" guidance
- Clear criteria

**3. Progressive Detail**
- High-level philosophy first
- Then specific guidance
- Then examples
- Then edge cases

**4. Explicit Boundaries**
- "Touch these arrays"
- "Don't touch those arrays"
- Clear pass responsibilities

**5. Consolidation Metadata**
- Forces explanation
- Enables review
- Complete traceability

### What Doesn't Work

**1. Implicit Instructions**
- "Be careful about..." → Ignored
- "Consider whether..." → Skipped
- **Better:** Explicit steps with verification

**2. Ambiguous Criteria**
- "Extract important..." → What's important?
- "When relevant..." → Always relevant?
- **Better:** Clear tests and examples

**3. Verbose Explanations**
- Long philosophical discussions → Skimmed
- **Better:** Concise principles + examples

**4. Nested Complexity**
- "If X and Y but not Z unless W" → Confusing
- **Better:** Decision trees, simple tests

**5. Mixed Concerns**
- Extraction + assessment combined → Bias
- **Better:** Strict separation

---

## Architectural Evolution

### v2.0 → v2.2: Two-Pass Workflow

**Why:** Single-pass over-extraction problematic.

**How:** Split into liberal Pass 1 + rationalization Pass 2.

**Result:** Consistent 15-20% reduction, better quality.

---

### v2.2 → v2.3: Consolidation Metadata

**Why:** Rationalization decisions opaque.

**How:** Added consolidation metadata to all consolidated items.

**Result:** Complete traceability, verifiable preservation.

---

### v2.3 → v2.4: RDMAP Integration

**Why:** Methodology extraction as important as claims.

**How:** Three-tier hierarchy + cross-references + iterative accumulation.

**Result:** Unified extraction framework for complete assessment.

---

### v2.4: Skill + Runtime Prompts

**Why:** Prompt evolution faster than skill packaging.

**How:** Separate stable framework (skill) from evolving guidance (prompts).

**Result:** Rapid iteration without installation friction.

---

## Future Directions

### Prompt Enhancements (v2.5+)

**1. Domain-Specific Prompts**
- Ecology variant (different expected information)
- Ethnography variant (different methods)
- Biology variant (different protocols)

**2. Controlled Vocabularies**
- Build from v2.4 usage
- Standardize study designs
- Formalize sampling strategies

**3. Validation Rules**
- Domain-specific checks
- Completeness patterns
- Temporal consistency

**4. Assessment Integration**
- Transparency scoring
- Replicability indicators
- Quality metrics

### Research Questions

**About Prompts:**
- How does extraction quality vary by domain?
- What prompt length is optimal?
- How many examples are enough?
- Can we auto-generate examples?

**About Architecture:**
- Can we parallelize passes safely?
- How to handle >50 page papers?
- What's optimal chunking strategy?
- Can we automate pass sequencing?

**About Usage:**
- What are common failure modes?
- Where do users get stuck?
- What documentation gaps exist?
- How to improve onboarding?

---

## Lessons for Future Skill Development

### 1. Test Early, Test Often

Start testing with real content immediately, not after "perfect" design.

### 2. Iterate Based on Evidence

Every design decision informed by actual extraction quality, not theory.

### 3. Separate Stable and Evolving

Framework (slow) and implementation (fast) have different change rates.

### 4. Progressive Disclosure

Load what's needed when needed, minimize context bloat.

### 5. Two-Pass Better Than One

Liberal generation + careful critique beats trying for perfect first-pass.

### 6. Traceability Non-Negotiable

Consolidation metadata, location tracking, verbatim quotes essential.

### 7. Examples Trump Explanation

Show don't tell, comprehensive examples more valuable than long explanations.

### 8. Domain Expertise Helps

Subject matter knowledge improves extraction quality significantly.

### 9. Start Permissive, Formalize Later

Open vocabularies then controlled after usage patterns emerge.

### 10. Test on Real Papers

Synthetic examples miss real complexity, use published papers.

---

## Acknowledgments

**Frameworks Adapted:**
- TIDieR (Template for Intervention Description and Replication)
- CONSORT-Outcomes (Consolidated Standards of Reporting Trials)
- SPIRIT (Standard Protocol Items: Recommendations for Interventional Trials)

**Inspired By:**
- RepliCATS project (multi-pass assessment)
- Open Science Framework (transparency emphasis)
- Registered Reports (pre-specification principles, adapted for retrospective)

**Tested On:**
- Sobotkova et al. (2023) "Arbitrary Offline Data Capture on All of Your Androids: The FAIMS Mobile Platform"

**Tools:**
- Claude Sonnet 4.5 (Anthropic) for all extractions
- JSON schema validation
- Iterative empirical testing methodology

---

## Conclusion

From initial concept (v2.0) to production system (v2.4), prompt development was driven by empirical testing and evidence-based refinement. The five prompts (~4,400 lines) represent distilled insights from multiple extraction cycles, error correction, and architectural evolution.

Key achievements:
- ✅ Two-pass workflow achieving 15-20% reduction consistently
- ✅ Complete traceability via consolidation metadata
- ✅ Three-tier RDMAP hierarchy working correctly
- ✅ Cross-reference integrity maintained
- ✅ Expected information tracking functional
- ✅ Skill + runtime prompts architecture enabling rapid iteration

The prompts are production-ready but continue to evolve based on usage, domain expansion, and community feedback.

**For technical details, see [ARCHITECTURE.md](ARCHITECTURE.md)**  
**For usage instructions, see [USAGE_GUIDE.md](USAGE_GUIDE.md)**  
**For testing procedures, see [TESTING.md](TESTING.md)**
