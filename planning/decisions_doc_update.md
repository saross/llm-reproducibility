# Claims Extraction Schema Development: Synopsis of Decisions
**Date:** October 18, 2025  
**Version:** 2.3  
**Context:** Developing methodology for extracting and assessing claims from research papers

**Version 2.3 Updates:**
- Added Multi-Dimensional Evidence Extraction principle and analytical view pattern
- Added consolidation metadata field for traceability
- Documented Results section test findings (2025-10-18)

---

## Core Conceptual Framework

### Evidence vs. Claims Distinction

**Decision:** Separate evidence (observations/measurements) from claims (interpretations/assertions)

**Rationale:** Different assessment approaches needed:
- **Evidence** assessed for: measurement quality, source reliability, transparency
- **Claims** assessed for: logical validity, evidence support, generalizability

**Implementation:**
- Evidence = minimal inference from raw data (observations, measurements, counts)
- Claims = require interpretive framing, categorization decisions, causal/instrumental assertions

**Example:**
- Evidence: "Students worked for 189.4 hours" (from timestamps)
- Claim: "The crowdsourcing approach produced 10,827 features with 57 staff-hours, yielding 190 features/staff-hour" (bundles evidence + boundary decisions + causal framing)

---

## NEW (v2.3): Multi-Dimensional Evidence Extraction

**Decision:** When evidence can be organized along multiple dimensions (phase, activity type, year, quality metric), create analytical view items for dimensions that support distinct claims

**Rationale:** Single evidence source may support multiple assessment questions requiring different organizational lenses. Rather than forcing single structure or duplicating content, create:
1. **Primary item:** Comprehensive data organized by dominant dimension
2. **Analytical view(s):** Extract/reorganize by secondary dimension(s) supporting distinct claims

**Date Added:** 2025-10-18  
**Trigger:** Results section test revealed inconsistency in handling time data organized by phase vs activity type

### The Problem Case

**Scenario:** Staff time data organized by project phase (pre-fieldwork 44h, during-fieldwork 7h) also contains supervision time component relevant to separate "minimal supervision" claim.

**Initial approaches tried:**
- ❌ Consolidate all time → loses supervision-specific support for "minimal supervision" claim
- ❌ Extract only training time → inconsistent (fieldwork supervision ignored)
- ✅ **Solution:** Primary item (time by phase) + analytical view (time by activity type)

### Implementation Pattern

**Primary Evidence Item:**
```json
{
  "evidence_id": "E001",
  "evidence_text": "Comprehensive breakdown organized by dominant dimension",
  "supports_claims": ["C001"],  // Claims about primary dimension
  "consolidation_metadata": {
    "consolidation_type": "phase_aggregation",
    "information_preserved": "lossy_granularity",
    "granularity_available": "Paper reports component-level detail..."
  },
  "extraction_notes": "For [activity-type] view, see E002"
}
```

**Analytical View Item:**
```json
{
  "evidence_id": "E002",
  "evidence_text": "Extracted/reorganized by secondary dimension",
  "supports_claims": ["C002"],  // Claims about secondary dimension
  "related_evidence": ["E001"],  // Links back to comprehensive item
  "consolidation_metadata": {
    "consolidation_type": "analytical_view",
    "information_preserved": "complete",
    "rationale": "Secondary dimension supports distinct claim requiring separate evidence"
  },
  "extraction_notes": "Analytical view extracting [activity type] from comprehensive breakdown (E001)"
}
```

### When to Apply

**✅ Create analytical view when:**
- Evidence organizeable by multiple dimensions (phase/activity, year/type, metric/source)
- Dimension 2 supports distinct claim requiring separate assessment
- Same underlying data, different analytical lenses
- Extractor can reorganize/extract without adding information

**❌ Do NOT create analytical view when:**
- Same dimension, different granularity levels → just consolidate appropriately
- Secondary dimension doesn't support distinct claim → keep in primary only
- Truly independent measurements → separate items, not views
- Would require inferring data not present → that's a claim, not view

### Examples from Results Section Test

**Example 1: Time by Phase vs Activity Type**
- Primary (E001): Time by phase (44h pre-fieldwork, 7h during fieldwork) → supports total investment claim
- Analytical view (E002): Supervision time (≤30min training + portion of 7h) → supports minimal supervision claim
- Same data, two lenses

**Example 2: Season Productivity (kept separate, not analytical view)**
- E004: 2017 productivity (time + output + rate)
- E006: 2018 productivity (time + output + rate)
- NOT analytical views because: different years = independent measurements, not reorganizations

**Example 3: Error Types (consolidated, not split)**
- False negatives + double-marking + classification errors → Single error profile
- NOT split into views because: error profile assessed as unit, not separately by type

### Heuristic for Consolidation vs Analytical View

**Question 1:** "Is this the same underlying data organized differently?"
- YES → Consider analytical view
- NO → Separate items (not views)

**Question 2:** "Does dimension 2 support a distinct claim?"
- YES → Create analytical view
- NO → Keep dimension 2 in primary item only

**Question 3:** "Would I assess these dimensions together or separately?"
- Together → Consolidate into single item
- Separately → Analytical view pattern

### Prompt Addition (Pass 2 v2.3)

Added ~400 words to Pass 2 prompt:
- Multi-Dimensional Evidence Extraction Principle section
- When to create analytical views
- Example pattern with E001/E002
- When NOT to use pattern
- Cross-referencing via `related_evidence` field

---

## NEW (v2.3): Consolidation Metadata for Traceability

**Decision:** Add `consolidation_metadata` field to evidence, claims, and implicit arguments to document all consolidation operations performed in Pass 2

**Rationale:** 
- Makes consolidation decisions explicit and auditable
- Enables systematic analysis of consolidation patterns
- Documents information preservation (complete vs lossy)
- Records available granularity in source for future reference
- Creates basis for learning/refining consolidation rules

**Date Added:** 2025-10-18  
**Trigger:** Results section test revealed need to document aggressive evidence consolidation (58% reduction) and justify granularity loss

### Schema Structure

```json
"consolidation_metadata": {
  "consolidation_performed": true/false,
  "source_items": ["P1_E001", "P1_E002", ...],
  "consolidation_type": "granularity_reduction | compound_finding | analytical_view | phase_aggregation | profile_consolidation | redundancy_elimination | narrative_consolidation | compound_interpretation | synthesis",
  "information_preserved": "complete | lossy_granularity | lossy_redundancy",
  "granularity_available": "Description of additional detail in source",
  "rationale": "Brief explanation"
}
```

### Consolidation Type Taxonomy

**For Evidence:**
- **granularity_reduction:** Fine measurements → aggregate (task times → phase totals)
- **compound_finding:** Multiple measurements → single finding (time + output = productivity)
- **analytical_view:** Reorganize by different dimension (see above)
- **phase_aggregation:** Sequential/temporal combination (2017 + 2018 → total)
- **profile_consolidation:** Multiple characteristics → complete profile (error rate + types)
- **redundancy_elimination:** Overlapping items merged (rare)

**For Claims:**
- **narrative_consolidation:** Problem + cause + solution → story
- **compound_interpretation:** Multiple judgments → integrated assessment
- **synthesis:** Cross-subsection integration → overarching conclusion

### Information Preservation Levels

- **complete:** No information lost, just reorganized
- **lossy_granularity:** Component-level detail exists in source but not extracted
- **lossy_redundancy:** Redundant measurements consolidated (no unique information lost)

### Usage Requirements

**Pass 2 rationalization MUST:**
1. Populate consolidation_metadata for ALL items created by merging Pass 1 items
2. List all source_items (Pass 1 IDs) that were consolidated
3. Select appropriate consolidation_type
4. Specify information_preserved level
5. If lossy_granularity: document what detail is available in source via granularity_available
6. Provide brief rationale for consolidation decision

**Example:**
```json
{
  "evidence_id": "E001",
  "consolidation_metadata": {
    "consolidation_performed": true,
    "source_items": ["P1_E001", "P1_E002", "P1_E003", "P1_E004", "P1_E006", "P1_E007", "P1_E008", "P1_E009", "P1_E012", "P1_E013"],
    "consolidation_type": "phase_aggregation",
    "information_preserved": "lossy_granularity",
    "granularity_available": "Paper reports 11 discrete component times: programmer 35h customisation, staff 3h server setup, 1.5h map prep, 2.5h file monitoring, 1h validation dev, 1h field setup, 30min map prep, 1.5h file prep per season",
    "rationale": "Individual task times less relevant than phase totals for assessing total investment; all details preserved in source for verification"
  }
}
```

### Schema Version Update

- **v2.2 → v2.3** added:
  - `consolidation_metadata` object to evidence, claim, and implicit_argument definitions
  - `related_evidence` array to evidence definition (for analytical view cross-referencing)
  - `synthesis` as claim_role enum value (for cross-subsection integration claims)

---

## Empirical Findings from Two-Pass Workflow Tests

### Methods Section Test (2025-10-17)
- Pass 1: 85 items → Pass 2: 69 items (19% reduction)
- Evidence/claim boundaries: High accuracy
- Consolidation: Appropriate for specification-heavy content
- Pattern: Specification redundancy (same entity described multiple ways)

### Results Section Test (2025-10-18)
- Pass 1: 80 items (43 evidence, 29 claims, 8 IAs) → Pass 2: 49 items (18 evidence, 22 claims, 9 IAs)
- Total reduction: 38.8% (exceeds 15-20% target but defensible)
- Evidence reduction: 58.1% (very high)
- Claims reduction: 24.1% (within target)
- IA change: +1 (added missing generalization)

**Key Findings:**

1. **Section-specific consolidation rates:** Results sections (measurement-heavy) consolidate more aggressively than Methods sections (specification-heavy)
   - Results: Time measurements at multiple levels (task → phase → season → total)
   - Methods: Specifications generally not redundant
   - Conclusion: Target 15-20% is appropriate for Methods, 20-40% for Results

2. **Evidence/claim boundary accuracy:** Pass 1 achieved 100% accuracy in Results test
   - No reclassifications needed in Pass 2
   - Professional judgments correctly classified as claims
   - Direct measurements correctly classified as evidence
   - Speed-accuracy correlations kept as evidence (comparative analysis, not interpretation)

3. **Multi-dimensional evidence discovered:** Time data organized by phase needed supervision-specific view
   - Revealed need for analytical view pattern (now implemented in v2.3)
   - Primary item + analytical view solves organizational tension

4. **Items added in Pass 2:** Both tests added 3-4 items
   - Implicit comparisons missed in Pass 1
   - Cross-subsection synthesis claims
   - Missing implicit generalizations from single cases
   - Pattern: Pass 1 under-extracts synthesis/integration claims

5. **Type 3 implicit arguments:** Successfully extracted in both tests
   - Methods: Several disciplinary assumptions about platform/technical choices
   - Results: 1 disciplinary assumption about dataset value
   - Pattern: More conceptually dense sections (Methods, Discussion) contain more Type 3 IAs

6. **Consolidation metadata necessity:** Results test highlighted need for documenting granularity loss
   - 58% evidence reduction required justification
   - Assessors need to know what detail is available in source
   - Led to v2.3 consolidation_metadata addition

---

## Dual-Layer Uncertainty Tracking

**Decision:** Track both author-declared uncertainty AND assessor uncertainty, supporting diverse uncertainty types

**Rationale:** 
- Authors may not acknowledge limitations (transparency issue)
- External assessors need to flag missing information
- Insider knowledge problem: authors may know about limitations they don't document
- Different fields use different uncertainty conventions

**Implementation:**
- **Layer 1 (Author - "declared_uncertainty")**: What paper states
- **Layer 2 (Assessor - "expected_uncertainty")**: What SHOULD have been declared but wasn't

---

## Four-Level Hierarchical Claim Structure

**Decision:** Core → Intermediate → Supporting → Evidence (with optional Synthesis)

**Rationale:** Papers build arguments hierarchically; assessment requires understanding claim roles

**Update (v2.3):** Added "synthesis" as claim_role for cross-subsection integration claims
- Example: "The mobile system successfully produced large, high-quality datasets with low supervision demands"
- Integrates findings from multiple Results subsections
- Discovered in Results section test (2025-10-18)

---

## Implicit Argument Taxonomy

**Decision:** Three types with different extraction intensities

**Types:**
1. **Type 1 (Logical Implications):** Unstated but necessarily implied by explicit claims
2. **Type 2 (Unstated Assumptions):** Assumed premises that make arguments work
3. **Type 3 (Disciplinary Assumptions):** Deep assumptions shared by field, rarely acknowledged

**Extraction Strategy:**
- Type 1 & 2: Extract for high-priority claims (core and key intermediate)
- Type 3: Flag when recognized, formalize cautiously (requires domain knowledge)

**Validation:** Discussion section test achieved 95% author confirmation (20/21 items)

**Update from Results test (2025-10-18):**
- Successfully extracted 1 Type 3 IA: "Large systematic datasets inherently valuable"
- Archaeological disciplinary assumption distinguishable from project-specific assumptions
- Pattern validated: Type 3 extraction reliable when framed carefully

---

## Extraction vs. Assessment Boundary

**Decision:** Extraction phase gathers information; assessment phase evaluates

**Extraction captures:**
- What paper explicitly states
- What we can directly infer
- What's missing (information gaps)
- Structure/relationships
- Consolidation operations and traceability (v2.3)

**Deferred to assessment:**
- Credibility scoring
- Deep evaluation of evidence quality
- Final transparency/validity/robustness ratings

**Update (v2.3):** Consolidation metadata bridges extraction and assessment
- Documents what was consolidated and why
- Notes available granularity for assessors needing more detail
- Makes consolidation decisions auditable

---

## Relationship Tracking

**Decision:** Track multiple relationship types

**Types:**
- **supports/supported_by**: Hierarchical evidential support
- **related_evidence** (v2.3): Links analytical views to primary items
- **alternatives**: Different scenarios
- **qualifications**: Claims that bound/qualify others
- **contradicts**: Challenges to prior literature

**Update (v2.3):** Added `related_evidence` field for analytical view pattern
- Cross-references analytical views to comprehensive items
- Documents same-data-different-lens relationships
- Enables tracing extraction decisions

---

## Principles Guiding Design

1. **Better to include too much than miss things** (Pass 1 philosophy)
2. **Consolidate systematically with traceability** (Pass 2 philosophy, v2.3)
3. **Tag distinctions that change assessment approach**
4. **Transparency is assessable** (missing information matters)
5. **Uncertainty is normal** (capture expressed and unexpressed)
6. **Evidence quality propagates** (track chains)
7. **Iterate empirically** (test and refine)
8. **Document consolidation decisions** (v2.3: enable learning and audit)
9. **Multi-dimensional evidence needs multiple views** (v2.3: analytical view pattern)

---

## Version History

- **v2.0 (2025-10-16):** Initial comprehensive schema
- **v2.1 (2025-10-16):** Post-calibration refinements, Type 3 formalization
- **v2.2 (2025-10-17):** Extraction/assessment separation, credibility structure
- **v2.3 (2025-10-18):** Multi-dimensional evidence + consolidation metadata

---

## Open Questions for Future Refinement

1. **Consolidation rate targets:** Should vary by section type?
   - Current finding: 15-20% for Methods, 20-40% for Results
   - Needs testing on Discussion/Introduction sections

2. **Analytical view frequency:** How common is multi-dimensional evidence?
   - Discovered in Results time data
   - May appear in other contexts (quality metrics, participant characteristics)
   - Monitor frequency to assess if pattern is common enough to warrant complexity

3. **Synthesis claim extraction:** Pass 1 consistently under-extracts cross-subsection integration
   - Should Pass 1 prompt emphasize synthesis claims more?
   - Or is Pass 2 addition the right place to catch these?

4. **Consolidation metadata overhead:** Does benefit justify the effort?
   - Enables traceability and learning
   - Creates systematic record
   - Monitor whether assessors actually use granularity_available field

---

**Last Updated:** 2025-10-18  
**Status:** Active development, empirically refined through multi-section testing  
**Next Test:** Discussion or Introduction section to validate across full paper structure
