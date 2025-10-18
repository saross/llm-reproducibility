# Claims Extraction Prompt - PASS 2: Rationalization v2.4

**Version:** 2.4 Pass 2  
**Last Updated:** 2025-10-18  
**Workflow Stage:** Pass 2 of 2 - Consolidate and refine Pass 1 extraction

**Changes in v2.4:**
- Reorganized for clarity: priority hierarchy, decision trees, boxed references
- 15% length reduction through consolidation and example compression
- All v2.3 patterns and distinctions preserved

---

## Your Task

Review the Pass 1 extraction and apply consolidation principles to produce a rationalized, high-quality extraction. Pass 1 intentionally over-extracted (~40-50% more items than needed). Your job is to consolidate, correct, and verify.

**Expected outcome:**
- 15-20% reduction in total items (may be higher for measurement-heavy sections)
- Better evidence/claim boundaries
- Appropriate consolidation without loss of information
- All claims have clear evidential support
- Accurate citations and no hallucinations
- Complete consolidation traceability via metadata

---

## PATTERN PRIORITY HIERARCHY

### ⭐⭐⭐ CRITICAL PATTERNS (Never Miss These)

**1. Profile vs Comparison Dimensions**
- **LUMP:** Profile/characteristic dimensions (error types, quality metrics, component features)
- **SPLIT:** Comparison dimensions (year-over-year, before/after, treatment/control)
- **Why critical:** Merging temporal comparisons destroys the comparison claim

**2. Multi-Dimensional Evidence → Analytical Views**
- When evidence serves multiple dimensions AND dimension 2 supports distinct claim
- Create primary item + analytical view(s), cross-reference via `related_evidence`
- **Why critical:** Enables one dataset, multiple assessment perspectives

**3. The Acid Test**
- "Would I assess the credibility of these statements TOGETHER or SEPARATELY?"
- Together → LUMP | Separately → SPLIT
- **Why critical:** Primary consolidation decision criterion

### ⭐⭐ SECONDARY PATTERNS (Apply When Recognized)

**4. Three High-Value Addition Patterns**
- Implicit comparisons (contrastive framing without explicit statement)
- Overlooked explicit content (recommendations, forward-looking statements)
- Cross-subsection synthesis (overarching messages spanning subsections)

**5. Anchor Numbers in Claims**
- Include key quantitative values that make claims interpretable
- Strategic duplication for readability vs full evidence reproduction

**6. Calculation Claims vs Evidence**
- Straightforward arithmetic → evidence
- Interpretation/comparison beyond arithmetic → claims

### 📋 REFERENCE INFORMATION (Consult as Needed)

- Consolidation_metadata field structure (see Reference Box A)
- Consolidation type taxonomy (see Reference Box B)
- Expected information checklists (inherited from Pass 1)

---

## CORE CONSOLIDATION PRINCIPLES

### Match Evidence Granularity to Claim Granularity

Evidence should be at the same level of detail as the claims they support:
- If claim assesses components **together** → consolidate evidence
- If claim assesses components **separately** → keep evidence separate
- If claims need both views → consider analytical view pattern

### Lumping/Splitting Decision Framework

```
Apply ACID TEST: "Assess together or separately?"
│
├─ TOGETHER → Check lumping patterns:
│  ├─ Multiple specs for same entity? → LUMP (specifications)
│  ├─ Compound professional judgment? → LUMP (interpretation)
│  ├─ Joint technical capabilities? → LUMP (capability profile)
│  └─ Single workflow steps? → LUMP (process aggregation)
│
└─ SEPARATELY → Check splitting requirements:
   ├─ Different observations support different claims? → SPLIT
   ├─ Different assessment requirements? → SPLIT
   ├─ Different sources or methods? → SPLIT
   ├─ Temporal comparison IS the claim? → SPLIT (critical)
   └─ Multi-dimensional with different supported claims? → ANALYTICAL VIEW
```

**When to LUMP:**
1. **Same entity specifications** - Map scale + source + date → "Historical maps at 1:5000 scale from 1920s paper sources"
2. **Compound interpretation** - "Accurate" + "Pre-modern" → "Maps accurately represent pre-modern landscapes"
3. **Joint capabilities** - 8 automation features → "Platform provides comprehensive automation"
4. **Single workflow** - Multiple prep tasks → "Staff handled geospatial preparation"

**When to SPLIT:**
1. **Different claims** - Hours worked (efficiency) vs features generated (output)
2. **Different assessments** - Accuracy 95.7% vs Completeness 83% (independent quality dimensions)
3. **Different sources** - Direct measurement vs professional judgment
4. **Temporal comparisons** - 2017 vs 2018 (comparison IS the claim - never merge)
5. **Multi-dimensional** - Time by phase vs time by activity type (see analytical view pattern)

---

## MULTI-DIMENSIONAL EVIDENCE: ANALYTICAL VIEW PATTERN

### Decision Tree

```
Does evidence serve multiple analytical dimensions?
├─ NO → Create single item, organized by dominant dimension
└─ YES → Does dimension 2 support a distinct claim?
    ├─ NO → Keep in primary item only
    └─ YES → CREATE ANALYTICAL VIEW
        ├─ Primary item (dimension 1, comprehensive)
        ├─ Analytical view item (dimension 2, extracted/reorganized)
        ├─ Cross-reference via related_evidence
        └─ Document in consolidation_metadata
```

### Example Pattern

**Primary Item (E001):** Time by phase (comprehensive)
- Supports claim about total investment
- Organized chronologically

**Analytical View (E002):** Time by activity type (supervision extracted)
- Supports claim about minimal supervision
- Extracted from primary, different lens
- `related_evidence: ["E001"]`
- `consolidation_type: "analytical_view"`

**Key principle:** Same underlying data, different analytical perspectives for different claims.

---

## STRATEGIC DECISIONS

### Anchor Numbers Principle

Claims can include key quantitative values for interpretability, even if numbers appear in evidence.

**Include anchor numbers when:**
- Numbers are central to claim meaning
- Omitting makes claim too vague
- Provides concrete grounding

**Example:**
- ✅ "Produced 8,343 features at 54s per feature"
- ✅ "Overall quality was good (>94% accuracy)"
- ❌ Full verbatim reproduction of evidence text

### Calculation Claims vs Evidence

**Test:** "Does this require reasoning beyond arithmetic?"
- **NO** → Evidence (e.g., "63s per record" from total÷count)
- **YES** → Claim (e.g., "2018 was slower" requires comparative judgment)

**Remove redundant calculation claims:** If claim merely restates calculation in evidence without interpretation.

### Strategic Verbosity in Claims

**Balance:** Readable and interpretable vs requiring excessive graph navigation

**Good verbosity:**
- "Overall data quality was good (>94% accuracy), with low recoverable omissions"
- Connects to subclaims, includes anchor numbers, interpretable standalone

**Bad verbosity:**
- Reproducing full evidence text
- Losing clarity in excessive qualification

---

## PASS 2 OPERATIONS

### STEP 1: Review Pass 1 Extraction
- Read all items against source text
- Identify consolidation opportunities
- Flag boundary errors
- Check for missing implicit content

### STEP 2: Apply Operations

**CONSOLIDATE** redundant/over-granular items
- Apply lumping patterns
- Use appropriate consolidation_type
- Document via consolidation_metadata

**CREATE ANALYTICAL VIEWS** for multi-dimensional evidence
- Primary item + view(s) for dimensions supporting different claims
- Cross-reference via related_evidence

**SPLIT** over-consolidated items (rare)
- When Pass 1 merged items needing separate assessment

**RECLASSIFY** boundary errors
- Professional judgment → claims
- Direct measurements → evidence

**ADD** missing content (three high-value patterns)
- **Implicit comparisons:** Contrastive framing → explicit comparison claim
- **Overlooked explicit:** Recommendations, forward-looking statements
- **Cross-subsection synthesis:** Overarching messages spanning findings

**REMOVE** items not supporting claims
- Move to project_metadata (timeline, location, resources, track record)

**VERIFY** relationships
- Update supports_claims arrays
- Check support chains
- Maintain hierarchy

### STEP 3: Quality Checks

- Citation accuracy (no hallucinations)
- Support chain integrity (no broken links)
- Consolidation traceability (complete metadata)
- Information preservation (verify via verbatim_quotes)

---

## OUTPUT REQUIREMENTS

**1. Rationalized JSON** (schema v2.4)
- All items properly consolidated
- Consolidation_metadata complete
- Analytical views cross-referenced
- Relationships verified

**2. Change Log:**
```json
{
  "operation": "CONSOLIDATE | ADD | REMOVE | SPLIT | RECLASSIFY | ANALYTICAL_VIEW",
  "items": "What was affected",
  "rationale": "Why this operation was performed",
  "acid_test": "For consolidations: 'together' or 'separately'?"
}
```

**3. Summary Statistics:**
- Pass 1 vs Pass 2 item counts
- Reduction percentages
- Operations breakdown

---

## QUALITY CRITERIA

**Good rationalization demonstrates:**
- ✅ Appropriate consolidation (15-20% reduction without information loss)
- ✅ Boundary accuracy (evidence/claim classifications correct)
- ✅ Relationship integrity (all support chains valid)
- ✅ Citation accuracy (no hallucinations)
- ✅ Completeness (no important content missed)
- ✅ Granularity match (items at appropriate level for assessment)
- ✅ Consolidation traceability (complete metadata)
- ✅ Analytical views used appropriately

**Common mistakes to avoid:**
- Over-consolidation (merging items needing separate assessment)
- Consolidating temporal comparisons (year-over-year, before/after must stay separate)
- Breaking support chains (consolidating evidence without updating claims)
- Citation errors (inaccuracies during text merging)
- Missing analytical views (consolidating multi-dimensional evidence inappropriately)
- Incomplete metadata (not documenting consolidation operations)
- Hallucination (adding content not in source)

---

## REMEMBER

- **Acid test is primary criterion** for lumping/splitting
- **Profile dimensions consolidate, comparison dimensions split**
- **Multi-dimensional evidence** gets analytical views when dimensions support different claims
- **Document everything** via consolidation_metadata
- **When uncertain, keep separate** - splitting beats over-lumping
- **Every claim needs support** - verify relationships after consolidation
- **Check against source** - no hallucinations
- **Project context ≠ Evidence** - move non-supportive items to metadata

---

## REFERENCE BOX A: Consolidation Metadata Structure

**Populate for EVERY consolidated item:**

```json
"consolidation_metadata": {
  "consolidation_performed": true,
  "source_items": ["P1_E001", "P1_E002", ...],
  "consolidation_type": "[see Reference Box B]",
  "information_preserved": "complete | lossy_granularity | lossy_redundancy",
  "granularity_available": "Description of additional detail in source",
  "rationale": "Why this consolidation was appropriate"
}
```

---

## REFERENCE BOX B: Consolidation Type Taxonomy

**For Evidence:**
- `granularity_reduction`: Fine-grain → aggregate (task times → phase totals)
- `compound_finding`: Multiple measurements → single finding (time + output → productivity)
- `analytical_view`: Reorganize by different dimension (supervision from phase breakdown)
- `phase_aggregation`: Sequential/temporal items combined (2017 + 2018 → total)
- `profile_consolidation`: Multiple characteristics → complete profile (error types)
- `redundancy_elimination`: Overlapping items merged (rare in Pass 1)

**For Claims:**
- `narrative_consolidation`: Problem + cause + solution → story
- `compound_interpretation`: Multiple judgments → integrated assessment
- `synthesis`: Cross-subsection integration → overarching conclusion

**For Implicit Arguments:**
- Same types as claims when consolidating multiple IAs

---

**Version:** 2.4  
**Schema:** v2.4 (with consolidation_metadata)  
**Length:** ~410 lines (15% reduction from v2.3)  
**Date:** 2025-10-18