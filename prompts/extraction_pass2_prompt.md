# Claims Extraction Prompt - PASS 2: Rationalization v2.3

**Version:** 2.3 Pass 2  
**Last Updated:** 2025-10-18  
**Workflow Stage:** Pass 2 of 2 - Consolidate and refine Pass 1 extraction

**Changes in v2.3:**
- Added multi-dimensional evidence extraction principle
- Added consolidation_metadata field usage
- Added analytical view pattern for cross-referenced evidence

---

## Your Task

Review the Pass 1 extraction and apply consolidation principles to produce a rationalized, high-quality extraction. Pass 1 intentionally over-extracted (~40-50% more items than needed). Your job is to consolidate, correct, and verify.

---

## RATIONALIZATION PHILOSOPHY FOR PASS 2

**Goals:**
- Reduce over-extraction to appropriate granularity
- Correct evidence/claim boundary errors
- Remove items that don't support claims (move to project_metadata)
- Consolidate redundant or over-granular items
- Add missing implicit generalizations
- Verify all relationships are accurate

**You have access to:**
1. Pass 1 extraction JSON (may be over-extracted and over-granular)
2. Original section text (for verification and fact-checking)

**Expected outcome:**
- 15-20% reduction in total items (may be higher for measurement-heavy Results sections)
- Better evidence/claim boundaries
- Appropriate consolidation without loss of information
- All claims have clear evidential support
- Accurate citations and no hallucinations
- Complete consolidation traceability via metadata

---

## Core Consolidation Principles

### The Lumping/Splitting Decision Framework

**PRIMARY PRINCIPLE: Match Evidence Granularity to Claim Granularity**

Evidence should be at the same level of detail as the claims they support:
- If claim assesses components **together** → consolidate evidence into compound finding
- If claim assesses components **separately** → keep evidence items separate
- If claims need both views → consider analytical view pattern (see below)

**ACID TEST:** "Would I assess the credibility of these statements TOGETHER or SEPARATELY?"
- Together → LUMP (consolidate)
- Separately → SPLIT (keep distinct)

### Anchor Numbers Principle (Strategic Duplication)

**Rule:** Claims can include key quantitative values that provide necessary context, even if these numbers appear in evidence. This is acceptable strategic duplication that makes claims interpretable.

**When to include anchor numbers in claims:**
- Numbers are central to understanding the claim's meaning
- Omitting them makes claim too vague or abstract
- They provide concrete grounding for the assertion
- They're brief and selective (not full evidence reproduction)

**Examples:**
- ✅ "Produced 8,343 features at 54s per feature" (anchor numbers make productivity claim concrete)
- ✅ "Overall data quality was good (>94% accuracy)" (anchor contextualizes "good")
- ❌ Full verbatim reproduction of entire evidence text
- ❌ Including every detail when claim is high-level synthesis

**Rationale:** Claims should be interpretable without constantly cross-referencing evidence. Strategic anchor numbers balance this readability need with avoiding excessive duplication. The claim-evidence graph structure still provides full traceability.

### When to LUMP (Consolidate)

**1. Multiple observations specify the same entity**
- Example: Map scale (1:5000) + digitized from paper maps + source date (1920s) → Single "map specifications" evidence
- Rationale: Descriptive details about one thing belong together
- **Consolidation type:** `granularity_reduction`

**2. Multiple interpretations form a single compound claim**
- Example: "Maps are accurate" + "represent pre-modern landscapes" → Single claim: "Maps accurately represent pre-modern landscapes"
- Rationale: Professional judgment components assessed together
- **Consolidation type:** `compound_interpretation`

**3. Technical features that jointly support one capability claim**
- Example: Multiple automation features → Single "automation capabilities" evidence
- Rationale: Individual features matter less than overall capability they enable
- **Consolidation type:** `profile_consolidation`

**4. Process steps that form a single workflow**
- Example: Multiple staff preparation tasks → Single "staff handled geospatial preparation" evidence
- Rationale: Division of labor principle matters, not individual task granularity
- **Consolidation type:** `phase_aggregation`

**IMPORTANT DISTINCTION: Profile Dimensions vs Comparison Dimensions**

**Consolidate profile/characteristic dimensions:**
- Multiple characteristics of same phenomenon (error types, quality metrics, component features)
- Example: False negatives + double-marking + classification errors → error profile
- Rationale: Characteristics assessed together as complete description

**Keep separate comparison dimensions:**
- Temporal progressions (year-over-year, before/after, baseline vs treatment)
- Controlled comparisons (mobile vs desktop, concentrated vs sporadic)
- Example: 2017 omissions vs 2018 omissions → keep separate for improvement claim
- Rationale: Comparison IS the claim, requires separate measurements

### Strategic Verbosity in Claims

**Principle:** Err toward slightly more verbose claims that contextualize findings over terse claims that require excessive graph navigation to understand.

**Good verbosity (adds meaningful context):**
- "Overall data quality was good (>94% accuracy), with low recoverable omissions and correctable error patterns"
- Connects to supporting subclaims
- Includes anchor numbers for concreteness
- Makes claim interpretable standalone

**Bad verbosity (unwieldy detail):**
- Reproducing full evidence text
- Listing every minor detail
- Losing clarity in excessive qualification

**Balance:** Claims should be readable and interpretable while maintaining traceability through claim-evidence links. Use anchor numbers and contextual phrases to enhance rather than obscure meaning.

### When to SPLIT (Keep Separate)

**1. Different observations support different claims**
- Example: Student hours (efficiency dimension) vs features generated (output dimension)
- Rationale: Different assessment questions require different evidence

**2. Claims have different assessment requirements**
- Example: Accuracy (95.7%) vs completeness (83%) - different quality dimensions
- Rationale: Independent credibility assessments needed

**3. Evidence comes from different sources or methods**
- Example: Direct measurement vs professional judgment
- Rationale: Confidence basis differs, requires separate tracking

**4. Temporal progressions where comparison is the claim**
- Example: 2017 omissions (2.3%) vs 2018 omissions (0.52%) - year-over-year improvement
- Rationale: Comparison claims (before/after, treatment/control, year-over-year) require separate measurements for each time point
- **Key principle:** Don't consolidate temporal comparisons - they're naturally separate measurements, not reorganizations
- **Applies to claims too:** Keep aggregate claims separate from year-over-year comparison claims

**5. Different dimensions support different claims**
- Example: Time by phase (total investment claim) vs time by activity type (supervision claim)
- Rationale: Multi-dimensional evidence needs analytical views (see below)

### Calculation Claims vs Evidence Distinction

**Rule:** Straightforward arithmetic calculations without interpretation belong in **evidence**, not claims. Claims should add reasoning, framing, or comparative judgment beyond arithmetic.

**Test question:** "Does this require reasoning beyond arithmetic?"
- **NO** → Include calculation in evidence (e.g., "63s per record" from total time / total records)
- **YES** → Extract as claim (e.g., "rate improved" requires comparative judgment)

**Examples:**
- ✅ Evidence: "10,827 features in 189.4 hours (63s per record)" - arithmetic calculation
- ✅ Claim: "2018 was slower than 2017 (92s vs 54s per feature)" - comparative interpretation
- ❌ Redundant claim: Restating calculation already in evidence without adding interpretation

**When to remove calculation claims:** If a claim merely repeats an arithmetic calculation already present in evidence without adding framing, comparison, or judgment, remove it as redundant.

---

## NEW: Multi-Dimensional Evidence Extraction Principle

**Problem:** Evidence can be organized along multiple dimensions (phase, activity type, year, quality metric), and different dimensions may support different claims requiring separate assessment.

**Solution:** Create **analytical view** items that extract/reorganize data from a comprehensive primary item.

### When to Create Analytical Views

**Trigger:** When evidence serves multiple analytical dimensions AND dimension 2 supports a distinct claim.

**Pattern:**
1. **Create primary item** organized by dominant dimension (usually chronological/hierarchical)
2. **Create analytical view item(s)** for secondary dimensions that support distinct claims
3. **Cross-reference** using `related_evidence` field
4. **Document** extraction/reorganization in `consolidation_metadata`

### Example: Time by Phase vs Time by Activity Type

**Primary Item (E001) - Time by Phase:**
```json
{
  "evidence_id": "E001",
  "evidence_text": "Across both seasons, customisation, setup, and supervision took about 51 h total, including 36 h from the programmer and 15 h from project staff. Of this, initial customisation and setup before fieldwork was 44 h, while time during fieldwork (map preparation, distribution, and supervision) was 7 h.",
  "evidence_type": "Time measurement - comprehensive by phase",
  "supports_claims": ["C001"],
  "consolidation_metadata": {
    "consolidation_performed": true,
    "source_items": ["P1_E001", "P1_E002", "P1_E003", "P1_E004", "P1_E006", "P1_E007", "P1_E008", "P1_E009", "P1_E012", "P1_E013"],
    "consolidation_type": "phase_aggregation",
    "information_preserved": "lossy_granularity",
    "granularity_available": "Paper reports 11 discrete component times (programmer 35h customisation, staff 3h server setup, 1.5h map prep, 2.5h file monitoring, etc.)",
    "rationale": "Individual task times less relevant than phase totals for assessing total investment"
  },
  "extraction_notes": "Comprehensive time breakdown organized by project phase; includes all activities. For supervision-specific view, see E002."
}
```

**Analytical View Item (E002) - Time by Activity Type:**
```json
{
  "evidence_id": "E002",
  "evidence_text": "Training and supervision of students took no more than half an hour of staff time per season (≤30 min in 2017, 30 min in 2018). Additional supervision was included in the 7h of fieldwork activities.",
  "evidence_type": "Time measurement - supervision-specific analytical view",
  "supports_claims": ["C002"],
  "related_evidence": ["E001"],
  "consolidation_metadata": {
    "consolidation_performed": true,
    "source_items": ["P1_E005", "P1_E010", "extracted from P1_E013"],
    "consolidation_type": "analytical_view",
    "information_preserved": "complete",
    "rationale": "Supervision time supports separate claim (C002 'minimal supervision') requiring distinct evidence item despite being subset of total time (E001). Extracts supervision-specific figures from comprehensive phase breakdown."
  },
  "extraction_notes": "Analytical view extracting supervision-specific time from comprehensive time breakdown (E001). Paper does not separate supervision from other fieldwork activities within the 7h figure."
}
```

**Key Features:**
- E001 = comprehensive (by phase)
- E002 = analytical view (by activity type)
- `related_evidence` links them
- Both reference same underlying data, different lenses
- `consolidation_type: "analytical_view"` marks the pattern
- E002 supports C002 (minimal supervision), E001 supports C001 (total investment)

### When NOT to Create Analytical Views

- ❌ Same dimension, just different levels of granularity → consolidate to appropriate level
- ❌ Secondary dimension doesn't support distinct claim → keep in primary only
- ❌ Truly independent measurements (not reorganizations) → separate evidence items without analytical view relationship

---

## Consolidation Metadata Requirements

**For EVERY item created by consolidation**, populate the `consolidation_metadata` field:

```json
"consolidation_metadata": {
  "consolidation_performed": true,
  "source_items": ["P1_E001", "P1_E002", ...],
  "consolidation_type": "granularity_reduction | compound_finding | analytical_view | phase_aggregation | profile_consolidation | redundancy_elimination | narrative_consolidation | compound_interpretation | synthesis",
  "information_preserved": "complete | lossy_granularity | lossy_redundancy",
  "granularity_available": "Description of additional detail in source paper",
  "rationale": "Why this consolidation was appropriate"
}
```

**Consolidation Type Definitions:**

**For Evidence:**
- `granularity_reduction`: Fine-grain measurements → aggregate (task times → phase totals)
- `compound_finding`: Multiple measurements → single finding (time + output → productivity)
- `analytical_view`: Reorganize by different dimension (supervision extracted from phase breakdown)
- `phase_aggregation`: Sequential/temporal items combined (2017 + 2018 → total)
- `profile_consolidation`: Multiple characteristics → complete profile (error rate + types)
- `redundancy_elimination`: Overlapping items merged (rare if Pass 1 done well)

**For Claims:**
- `narrative_consolidation`: Problem + cause + solution → story (omissions narrative)
- `compound_interpretation`: Multiple judgments → integrated assessment
- `synthesis`: Cross-subsection integration → overarching conclusion

**For Implicit Arguments:**
- Same types as claims when consolidating multiple IAs

---

## Pass 2 Operations

### STEP 1: Review Pass 1 Extraction
- Read all evidence, claims, and implicit arguments
- Check Pass 1 extraction against source text
- Identify consolidation opportunities
- Flag boundary errors

### STEP 2: Apply Consolidation Operations

**REMOVE:** Items that don't support claims
- Move to project_metadata (timeline, location, resources, track record)
- Document what was removed and why

**CONSOLIDATE:** Redundant or over-granular items
- Apply lumping heuristics
- Use appropriate consolidation_type
- Document source_items and rationale
- Note granularity_available if lossy

**CREATE ANALYTICAL VIEWS:** Multi-dimensional evidence
- Identify when different dimensions support different claims
- Create primary item + analytical view(s)
- Link via related_evidence
- Document extraction in consolidation_metadata

**SPLIT:** Over-consolidated items (rare)
- When Pass 1 merged items needing separate assessment
- Document split rationale

**RECLASSIFY:** Evidence/claim boundary errors
- Professional judgment → claims
- Direct measurements → evidence
- Document reclassification

**ADD:** Missing content
- Implicit generalizations from single cases
- Overlooked comparative claims
- Cross-subsection synthesis claims
- Missing implicit arguments

**Three High-Value Addition Patterns:**

**Pattern 1: Implicit Comparisons**
- **Trigger:** Paper frames contrast but doesn't explicitly state comparison
- **Look for:** Contrastive language (concentrated vs sporadic, faster vs slower, better vs worse)
- **Example:** Separate 2017 and 2018 findings framed as "concentrated" vs "sporadic" → add explicit "concentrated was more productive" comparison claim
- **Test:** "Does the paper's language suggest comparison even without stating it?"

**Pattern 2: Overlooked Explicit Content**
- **Trigger:** Explicit recommendations, implications, or forward-looking statements missed in Pass 1
- **Look for:** "Should," "would likely," "future work," "recommendations" language
- **Example:** Final paragraph recommendation about QA methods overlooked in Pass 1
- **Test:** "Did I capture all explicit recommendations and forward-looking statements?"

**Pattern 3: Cross-Subsection Synthesis**
- **Trigger:** Pass 1 focuses on local claims, misses global integration
- **Look for:** Overarching messages that span multiple subsections
- **Example:** "System produced large, high-quality datasets with low supervision" integrates output + quality + efficiency findings
- **Test:** "What's the overall takeaway message integrating findings across this section?"

**When to add:** Always check for these three patterns in Pass 2, especially in Results and Discussion sections.

**VERIFY:** Relationships
- Update all supports_claims arrays after consolidation
- Check supported_by_evidence links
- Verify hierarchical claim structure

### STEP 3: Quality Checks

**Citation accuracy:**
- No hallucinations
- All verbatim_quotes verified against source
- Consolidated text accurately represents merged items

**Support chain integrity:**
- Every claim has supporting evidence or claims
- No broken links after consolidation
- Hierarchical structure maintained

**Consolidation traceability:**
- All consolidated items have complete consolidation_metadata
- Rationales documented
- Granularity loss noted

**Information preservation:**
- Check no important content lost
- Verify verbatim_quotes preserve details
- Confirm granularity_available documents what's in source

---

## Output Requirements

Produce:

1. **Rationalized JSON** following schema v2.3
   - All items properly consolidated
   - Consolidation_metadata complete for all merged items
   - Analytical views properly cross-referenced
   - All relationships verified

2. **Change Log** documenting all operations:
```json
{
  "operation": "CONSOLIDATE | ADD | REMOVE | SPLIT | RECLASSIFY | ANALYTICAL_VIEW",
  "items": "What was affected",
  "rationale": "Why this operation was performed",
  "acid_test": "For consolidations: answer to 'assess together or separately?'"
}
```

3. **Summary Statistics:**
   - Pass 1 item counts (evidence/claims/IAs)
   - Pass 2 item counts
   - Reduction percentages
   - Operations breakdown

---

## Quality Criteria for Pass 2

**Good rationalization demonstrates:**
- ✅ Appropriate consolidation (15-20% reduction without information loss, may be higher for measurement-heavy sections)
- ✅ Boundary accuracy (evidence/claim classifications correct)
- ✅ Relationship integrity (all support chains valid)
- ✅ Citation accuracy (no hallucinations)
- ✅ Completeness (no important content missed)
- ✅ Granularity match (items at appropriate level for assessment)
- ✅ Consolidation traceability (complete metadata)
- ✅ Analytical views used appropriately (multi-dimensional evidence handled correctly)

---

## Common Rationalization Mistakes to Avoid

1. **Over-consolidation:** Merging items that need separate assessment
2. **Consolidating temporal comparisons:** Merging year-over-year, before/after, or treatment/control measurements - these must remain separate for comparison claims
3. **Under-consolidation:** Not lumping clearly related specifications
4. **Breaking support chains:** Consolidating evidence but not updating claim links
5. **Citation errors:** Introducing inaccuracies when merging text
6. **Losing implicit content:** Not surfacing single-case generalizations
7. **Removing too much:** Moving supportive evidence to metadata
8. **Hallucination:** Adding content not in source text
9. **Missing analytical views:** Consolidating multi-dimensional evidence without extracting dimensions that support different claims
10. **Incomplete metadata:** Not documenting consolidation operations
11. **Ignoring granularity loss:** Not noting when source has more detail
12. **Mismatched granularity:** Evidence more detailed or coarse than claims it supports

---

## Remember

- **Acid test is primary criterion** for lumping/splitting
- **Multi-dimensional evidence** gets analytical views when dimensions support different claims
- **Document everything** via consolidation_metadata
- **Preserve information** - consolidate text, don't summarize
- **When uncertain, keep separate** - splitting beats over-lumping
- **Every claim needs support** - verify relationships after consolidation
- **Check against source** - no hallucinations
- **Project context ≠ Evidence** - move non-supportive items to metadata
- **Analytical views** enable one dataset, multiple assessment perspectives

---

**Version:** 2.3  
**Schema:** v2.3 (with consolidation_metadata)  
**Date:** 2025-10-18