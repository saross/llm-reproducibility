# Claims Extraction Schema Development: Synopsis of Decisions
**Date:** October 16, 2025  
**Version:** 2.0  
**Context:** Developing methodology for extracting and assessing claims from research papers

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

### Dual-Layer Uncertainty Tracking

**Decision:** Track both author-declared uncertainty AND assessor uncertainty, supporting diverse uncertainty types

**Rationale:** 
- Authors may not acknowledge limitations (transparency issue)
- External assessors need to flag missing information
- Insider knowledge problem: authors may know about limitations they don't document
- Different fields use different uncertainty conventions (radiometric ±, stylistic ranges, confidence intervals)

**Implementation:**
- **Layer 1 (Author - "declared_uncertainty")**: What paper states about confidence, ranges, limitations
  - Supports: bounded ranges ("800-600 BC"), error margins ("2567 BP ±87"), hedging language ("ca.", "approximately"), confidence intervals ("95% CI")
- **Layer 2 (Assessor - "expected_uncertainty")**: Uncertainty that SHOULD have been declared but wasn't
  - Flags: missing error margins on dates, false precision, absent bounded ranges
  - Documents: why we expect uncertainty that wasn't provided

**Examples:**
```json
// Well-documented radiometric date
"declared_uncertainty": {
  "uncertainty_type": "error_margin",
  "point_estimate_with_error": "2567 BP ±87"
}

// Stylistic date with appropriate range
"declared_uncertainty": {
  "uncertainty_type": "stylistic_range",
  "bounded_range": "800-600 BC",
  "hedging_language": ["ca."]
}

// Problematic: radiometric date WITHOUT error
"declared_uncertainty": {
  "uncertainty_type": "none_stated"
},
"expected_uncertainty": {
  "should_have_error_margin": true,
  "missing_uncertainty_types": ["statistical error for radiometric date"],
  "assessor_notes": "C14 date reported as '2567 BP' without ± - all radiocarbon dates have measurement error"
}

// Problematic: stylistic date with false precision
"declared_uncertainty": {
  "uncertainty_type": "none_stated"
},
"expected_uncertainty": {
  "should_have_range": true,
  "false_precision_flag": true,
  "assessor_notes": "Pottery dated to '725 BC' based on style - stylistic dating cannot achieve single-year precision"
}
```

### Claim Hierarchy

**Decision:** Organize claims hierarchically with explicit relationships - FOUR LEVELS

**Rationale:**
- Not all claims equally important to paper's argument
- Evidence quality propagates up hierarchy
- Core claims need most scrutiny
- Complex papers need intermediate layer between core and supporting

**Implementation:**
Four-tier hierarchy:
1. **Core claims** (5-10): Main thesis arguments (highest priority)
2. **Intermediate claims** (10-15): Major supporting arguments that build toward core
3. **Supporting claims** (15-25): Specific interpretations and findings
4. **Evidence claims** (30-50): Observations, measurements, data points

Plus additional roles:
- **Background claims**: Context-setting (assessed via citations)
- **Methodological claims**: About methods (assessed differently)
- **Transitional claims**: Narrative scaffolding (low priority)

**Note:** Start with four levels, reduce to three if intermediate layer proves unnecessary.

### Claim Composition Structure

**Decision:** Explicitly decompose claims into constituent parts

**Rationale:**
- Reveals interpretive moves
- Identifies boundary decisions
- Makes implicit framing explicit
- Enables assessment of each component

**Implementation:**
```json
"composed_of": {
  "evidence": ["E001", "E002"],  // Raw observations
  "calculations": ["190 = 10827 / 57"],  // Arithmetic
  "boundary_decisions": ["Programmer time counted as staff time"],  // Definitional choices
  "causal_framing": "Staff investment *enabled* student digitization"  // Instrumental claim
}
```

## Key Classification Decisions

### Claim Types
- **EMPIRICAL**: Observations, measurements, data
- **INTERPRETATION**: Inferences drawn from empirical data
- **METHODOLOGICAL**: About methods/procedures
- **THEORETICAL**: Conceptual/theoretical assertions

### Claim Roles
- **core**: Central to paper's argument (high assessment priority)
- **supporting**: Build toward core arguments (medium priority)
- **background**: Context/literature (assessed via citations)
- **transitional**: Narrative connections (low priority)
- **methodological**: Method descriptions (special assessment)

### Claim Functions (in argument chain)
- **premise**: Establishes starting points (check literature acceptance)
- **finding**: Results/outcomes (check evidence support)
- **conclusion**: Interpretations (check logical validity)
- **recommendation**: Prescriptive claims (check warrant)

### Claim Scope (generalizability)
- **project**: Project-specific (evidence from this work sufficient)
- **domain**: Domain-bounded (need evidence generalizes within field)
- **general**: Universal claims (need cross-domain evidence or hedging)

**Assessment approach:** Check whether evidence matches claimed scope. Higher expectations for broader claims (project < domain < general).

### Claim Function Structure

**Decision:** Hierarchical structure (primary/secondary) to capture multiple roles

**Rationale:** Some claims serve multiple functions in argument (e.g., both premise AND finding from literature)

**Implementation:**
```json
"claim_function": {
  "primary_function": "premise",
  "secondary_function": "finding"
}
```

**Can revert to:** Multi-tag array if hierarchical proves overkill

## Handling Special Cases

### Missing vs. Implicit Evidence

**Decision:** Flag when methodological claims lack verification evidence, but distinguish missing from implicit

**Types:**
1. **Missing evidence**: No basis provided at all
2. **Implicit unexplained evidence**: Evidence exists (author observation, professional judgment) but isn't documented
3. **Documented evidence**: Proper verification provided

**Example:** "UI allowed students to begin after only minutes"
- Not *missing* evidence (authors observed this)
- But implicit and unexplained (no training time measurements)
- Flag: `IMPLICIT_EVIDENCE_UNEXPLAINED`

### Quantitative vs. Qualitative

**Decision:** Start with rich categorization, pare down if unused

**Initial implementation:**
```json
"quantitative_details": {
  "source": "measurement | calculation | estimate | statistical",
  "confidence_basis": "...",
  "bounded_range": "...",
  "arithmetic_verifiable": true/false
}
```

**Rationale:** Different quantitative sources need different assessment. Can collapse later if distinction proves unhelpful.

### Fuzzy Data vs. Boundary Decisions

**Decision:** Tag both explicitly

**Distinction:**
- **Fuzzy data** = measurement uncertainty (inherent to method)
  - Example: "180-195h student time" (don't know exactly)
  - Assessment: How much uncertainty? Does it propagate to conclusions?
  
- **Boundary decisions** = definitional choices (author decisions)
  - Example: "Programmer hours count as 'staff time'"
  - Assessment: Are choices reasonable? Would alternatives change conclusions?

### Methodological Claims

**Decision:** Extract as claims (not methods) when paper argues for their effectiveness

**Rationale:** Methods papers argue that methodological choices were successful/optimal, making these argumentative claims, not just descriptions

**Example:** "UI allowed students to begin after only minutes" is both describing the system AND claiming it was successful

### Information Gaps as Data

**Decision:** Systematically record what should be present but isn't

**Rationale:** Absence is signal for transparency assessment

**Implementation:**
```json
"information_gaps": [
  "No bounded range despite proxy measurement",
  "No discussion of timestamp limitations",
  "Precision (189.4h) suggests false certainty"
]
```

### Expected Information Checklists

**Decision:** Create standard checklists of expected information for each claim type

**Rationale:** 
- Systematic identification of missing information
- Useful for automation (e.g., Claude Code)
- Consistent assessment across papers
- Turns absence into measurable transparency metric

**Implementation:**
Pre-defined checklists for:
- **Quantitative claims**: measurement method, instrument specs, error margins, sample size, bounded ranges, precision justification, units
- **Comparative claims**: comparison basis, what held constant, alternative explanations, fairness justification
- **Methodological claims**: justification for choices, limitations acknowledged, alternatives considered, verification evidence, replicability
- **Causal claims**: mechanism explained, confounds addressed, temporal precedence, alternatives ruled out, appropriate causal language
- **Generalizability claims**: scope explicit, evidence supports scope, boundary conditions, population/domain defined

**Assessment approach:** For each claim, check which expected information is present vs. absent. Missing information becomes transparency score input.

**Evolution:** Start with preliminary checklists, refine empirically as we see what actually matters for assessment.

## Relationship Tracking

### Beyond Hierarchy

**Decision:** Track multiple relationship types

**Types:**
- **supports/supported_by**: Hierarchical evidential support
- **alternatives**: Different scenarios (C095 vs C096 vs C097)
- **qualifications**: Claims that bound/qualify others
- **contradicts**: Challenges to prior literature (flag for extra scrutiny)

**Rationale:** Different relationships imply different assessment strategies

## Extraction vs. Assessment Boundary

**Decision:** Extraction phase gathers information needed for assessment; assessment phase evaluates

**Extraction captures:**
- What paper explicitly states
- What we can directly infer from text
- What's missing (information gaps)
- Structure/relationships

**Deferred to assessment:**
- Omitted caveats (unless glaringly obvious)
- Negative claims (what's NOT argued)
- Deep evaluation of evidence quality
- Final credibility scoring

## Principles Guiding Design

1. **Better to include too much than miss things** (at this exploratory stage)

2. **Tag distinctions that change assessment approach** (only pragmatically useful categories)

3. **Transparency is assessable** (missing information matters as much as present information)

4. **Uncertainty is normal** (capture both expressed and unexpressed uncertainty)

5. **Iterate empirically** (test schema, refine based on what actually helps)

6. **Evidence quality propagates** (weak evidence → weak claims, track chain)

## Finalized Decisions Summary

1. ✅ **Uncertainty handling**: Accommodates diverse types (radiometric ±, stylistic ranges, confidence intervals); tracks both declared and expected uncertainty
2. ✅ **Implicit arguments**: Type 1 and Type 2 for high-priority claims; flag Type 3; calibrate before full extraction
3. ✅ **Claim function**: Hierarchical (primary/secondary); can revert to multi-tag if overkill
4. ✅ **Missing evidence**: Flag when lacking, but distinguish from implicit unexplained evidence
5. ✅ **Claim scope**: Tag explicitly (project/domain/general); use in assessment
6. ✅ **Hierarchy depth**: Four levels (core → intermediate → supporting → evidence); reduce if unnecessary
7. ✅ **Extraction/assessment boundary**: Clear for now; monitor and adjust
8. ✅ **Expected information checklists**: Created preliminary versions; refine empirically
9. ✅ **Calibration approach**: Focused implicit argument extraction and review before full extraction; may need new chat

## Remaining Open Questions

## Remaining Open Questions

1. **Implicit argument extraction reliability**: How consistently can Type 1 and Type 2 be identified? (Requires calibration round)

2. **Four-level hierarchy utility**: Do papers actually need intermediate layer, or is three levels sufficient? (Will test empirically)

3. **Expected information checklist coverage**: Are the preliminary checklists comprehensive? What's missing? (Refine through use)

4. **Tag utility in practice**: Which classifications actually affect assessment decisions? (May pare down unused tags)

5. **Claim scope granularity**: Is project/domain/general sufficient, or need finer distinctions? (Test during assessment)

6. **Completeness assessment**: How do we know when we've captured all important claims? (Develop through careful iteration)

7. **Uncertainty generalization** (Critical for cross-domain work):
   - **Current state**: Schema handles specific uncertainty types well (error margins, bounded ranges, time estimates, radiometric/stylistic dates)
   - **Need**: Generalize across diverse claim types and domains through empirical observation
   - **Examples of uncovered patterns**: 
     - Qualitative assessments ("likely", "possibly", "appears to")
     - Model predictions with confidence bounds
     - Historical interpretations with competing evidence
     - Taxonomic classifications with uncertain attributions
     - Geospatial coordinates with positional accuracy
     - Sample representativeness questions
     - Causal mechanisms with incomplete understanding
   - **Approach**: 
     - Start with current extensible structure (uncertainty_type always included)
     - During each extraction, note uncertainty patterns that don't fit cleanly
     - Accumulate examples across papers from different domains
     - Periodically refine schema based on observed patterns
     - Build comprehensive cross-domain uncertainty taxonomy over time
   - **Action**: Explicitly document uncertainty edge cases during early extractions for later schema refinement

## Next Steps (Updated)

1. **Create extraction prompt** - Comprehensive prompt incorporating all schema elements
2. **Calibration round for implicit arguments** - Extract from Discussion section, user reviews, refine
3. **Test schema on one section** - Full extraction of Discussion or Results to validate approach
4. **Assess tag utility** - Which distinctions actually matter during assessment?
5. **Refine checklists** - Update expected information based on actual papers
6. **Document assessment criteria** - How to assess each claim type/role/function
7. **Full extraction trial** - One complete paper end-to-end
8. **Iterate** - Refine based on what works/doesn't work

**Note:** May need new chat for calibration round due to context limits

## Evolution Strategy

**Philosophy:** Err toward granularity now, pare back later. Past experience (Sonnet 3.5-3.7) suggests Claude can follow complex rubrics reliably when working with single sources. Build system empirically, not theoretically perfect from start.
