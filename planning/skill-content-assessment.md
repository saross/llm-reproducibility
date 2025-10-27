# Research Assessor Skill - Comprehensive Content Assessment

**Date**: 2025-10-27
**Assessor**: skill-creator skill analysis
**Skill Version**: 2.6.3
**Purpose**: Deep content review for optimal distribution, duplication, redundancy, and gaps

---

## Executive Summary

**Overall Assessment**: ⚠️ **GOOD with notable improvements needed**

The research-assessor skill has evolved organically over time, leading to:
- ✅ **Strengths**: Comprehensive coverage, well-organised structure, excellent individual file quality
- ⚠️ **Issues**: Significant content duplication between SKILL.md and references, suboptimal file distribution
- 🔧 **Recommendation**: Refactor to eliminate duplication, consolidate related content, redistribute according to skill-creator principles

**Key Skill-Creator Principle Violated**:
> "Avoid duplication: Information should live in either SKILL.md or references files, not both. Prefer references files for detailed information unless it's truly core to the skill—this keeps SKILL.md lean."

---

## Part 1: Content Duplication Analysis

### Critical Duplication: SKILL.md vs References

#### Issue 1: RDMAP Hierarchy Duplication

**Location 1**: SKILL.md lines 162-180 (19 lines)
```markdown
### RDMAP Three-Tier Hierarchy

**Research Designs** (Strategic - WHY)
- Research questions and hypotheses
- Theoretical frameworks
- Study design choices
- **Test:** "Is this about framing and rationale?"

**Methods** (Tactical - WHAT)
- Data collection approaches
- Sampling strategies
- Analysis techniques
- **Test:** "Is this the general approach at high level?"

**Protocols** (Operational - HOW)
- Specific procedures
- Tool configurations
- Parameter specifications
- **Test:** "Could someone replicate from this level of detail?"
```

**Location 2**: tier-assignment-guide.md lines 1-100+ (entire file, 193 lines)
- Same hierarchy definition (lines 1-8)
- Same core questions Q1/Q2/Q3 (lines 12-25)
- Same tier-specific indicators (lines 26-100+)
- Additional detail on granularity, keywords, worked examples

**Assessment**: FULL DUPLICATION of core concept + summary in SKILL.md
- SKILL.md has 19-line summary
- tier-assignment-guide.md has full 193-line treatment
- **Skill-creator violation**: Should only be in references, SKILL.md should just point to it

**Recommendation**: Remove from SKILL.md, replace with:
```markdown
### RDMAP Three-Tier Hierarchy

Research Designs (WHY), Methods (WHAT), Protocols (HOW).

**For complete guidance:** See `references/checklists/tier-assignment-guide.md`
```

---

#### Issue 2: Consolidation Algorithm Duplication

**Location 1**: SKILL.md lines 182-225 (44 lines)
```markdown
### Consolidation Logic

**PRIMARY: Empirical Graph Analysis (Identical Support Patterns)**

[Full algorithm with 5 steps]
[Example showing E032/E033 consolidation]
[Secondary test description]
```

**Location 2**: consolidation-patterns.md lines 14-133 (119+ lines)
- Same algorithm (lines 24-41)
- Same example (E032/E033) (lines 47-60)
- Many additional examples
- Full detailed guidance

**Assessment**: FULL DUPLICATION of algorithm + example
- SKILL.md has 44-line treatment with algorithm and one example
- consolidation-patterns.md has 120+ line treatment with same algorithm and many examples
- **Skill-creator violation**: Algorithm appears in BOTH places verbatim

**Recommendation**: Remove from SKILL.md, replace with:
```markdown
### Consolidation Logic

Use empirical graph analysis (identical support patterns) as primary method.

**For complete algorithm and examples:** See `references/checklists/consolidation-patterns.md`
```

---

#### Issue 3: Evidence vs Claims Distinction (Partial Duplication)

**Location 1**: SKILL.md lines 148-160 (13 lines)
```markdown
### Evidence vs. Claims

**Evidence** = Raw observations requiring minimal interpretation
- Direct measurements, observations, data points
- Someone could verify by checking the source
- Example: "125.8 person-hours"

**Claims** = Assertions that interpret or generalize
- Require reasoning or expertise to assess
- Make inferences beyond direct observation
- Example: "The platform was efficient"

**Test:** "Does this require expertise to assess or just checking sources?"
```

**Location 2**: No dedicated reference file for this distinction!
- Mentioned briefly in extraction-fundamentals.md (implicit arguments section)
- Mentioned in schema-guide.md (object definitions)
- NOT a standalone decision framework in checklists/

**Assessment**: PARTIAL DUPLICATION / MISSING FILE
- SKILL.md has concise summary (appropriate)
- BUT there's no dedicated reference file for "evidence-vs-claims-guide.md"
- Claims extraction prompts must repeat this guidance (potential duplication there)

**Recommendation**:
- Option A: Keep in SKILL.md as core principle (it's lean enough)
- Option B: Create `references/checklists/evidence-vs-claims-guide.md` with full treatment, reduce SKILL.md to pointer

---

### Duplication Summary Table

| Content | SKILL.md Lines | Reference File Lines | Duplication Severity | Action Needed |
|---------|---------------|---------------------|---------------------|---------------|
| RDMAP Hierarchy | 19 (lines 162-180) | tier-assignment-guide.md (193 total) | 🔴 FULL | Remove from SKILL.md |
| Consolidation Algorithm | 44 (lines 182-225) | consolidation-patterns.md (529 total) | 🔴 FULL | Remove from SKILL.md |
| Evidence vs Claims | 13 (lines 148-160) | None (missing file) | 🟡 PARTIAL | Create reference OR keep in SKILL.md |

**Total Duplication in SKILL.md**: ~76 lines (28% of SKILL.md content) should be in references instead

---

## Part 2: Suboptimal Content Distribution

### Issue 4: Research Design Guidance Split Across Two Files

**File 1**: `references/checklists/tier-assignment-guide.md` (193 lines)
- Purpose: How to distinguish Design vs Method vs Protocol
- Content: Tier hierarchy, decision tree, indicators, granularity principle
- Audience: Anyone extracting RDMAP

**File 2**: `references/research-design-extraction-guide.md` (346 lines)
- Purpose: Operational guidance for finding 4-6 Research Designs (vs under-extracting 1-2)
- Content: 10 successful practices, pre-scan checklist, design types, meta-level patterns, worked example, quality checks
- Audience: Anyone extracting Research Designs specifically

**Problem**: Content overlap and unclear navigation
- Both files address "what is a Research Design"
- Both files have worked examples
- Both files have quality checks
- User must read BOTH to fully understand Research Design extraction
- SKILL.md references tier-assignment-guide.md but not research-design-extraction-guide.md (line 109)

**Assessment**: SUBOPTIMAL DISTRIBUTION
- tier-assignment-guide.md should be about tier decisions (Design vs Method vs Protocol)
- research-design-extraction-guide.md has valuable operational content but it's separate

**Options**:
1. **Merge**: Combine into single `research-design-guide.md` (~500 lines)
   - Pro: One-stop reference
   - Con: Very long file

2. **Keep separate but restructure**:
   - tier-assignment-guide.md → Remains focused on tier decisions (Design vs Method vs Protocol)
   - research-design-extraction-guide.md → Rename to `research-design-operational-guide.md`, focus on finding all designs
   - Add both to SKILL.md navigation

3. **Subsume into extraction-fundamentals.md**:
   - extraction-fundamentals.md already has implicit RDMAP section
   - Add Research Design recognition patterns there
   - Keep tier-assignment-guide.md for tier decisions only

**Recommendation**: Option 2 - Keep separate but improve navigation
- Rename research-design-extraction-guide.md → `research-design-operational-guide.md` for clarity
- Add to SKILL.md navigation explicitly
- Clarify scope: tier-assignment = "which tier?", operational-guide = "how to find all?"

---

### Issue 5: Missing Parallel: No Claims/Evidence Operational Guide

**Observation**:
- Research Designs have TWO files:
  - tier-assignment-guide.md (tier decisions)
  - research-design-extraction-guide.md (operational guidance for finding all)
- Claims/Evidence have NO operational guide beyond what's in prompts

**Gap**:
- No `claims-evidence-operational-guide.md` equivalent
- Operational guidance lives in prompts (evolving separately from skill)
- No persistent reference for "how to find all claims" or "how to find all implicit arguments"

**Assessment**: MISSING CONTENT (not critical, but asymmetric)
- Research Designs get special operational guide
- Claims/Evidence rely entirely on prompts
- May explain why implicit arguments were fragile (guidance not in skill)

**Recommendation**: Consider creating `references/claims-evidence-operational-guide.md`
- Parallel to research-design operational guide
- Persistent operational patterns for finding claims, evidence, implicit arguments
- Reduces reliance on prompt evolution

---

### Issue 6: Schema Split: In Skill vs Out of Skill

**Current State**:
- `references/schema/schema-guide.md` (human-readable, 19KB, in skill)
- `extraction-system/schema/extraction_schema.json` (JSON schema, NOT in skill)

**SKILL.md says** (line 106):
```markdown
**Schema & Structure:**
- `references/schema/schema-guide.md` - Complete object definitions
- `references/schema/examples/` - JSON examples from real extractions
```

**Problem**:
- `references/schema/examples/` directory DOES NOT EXIST in skill
- JSON schema lives outside skill (extraction-system/schema/)
- Creates confusion about source of truth

**Assessment**: SUBOPTIMAL / INCOMPLETE
- Schema-guide.md is excellent human-readable version
- But canonical JSON schema not in skill (OK per architecture, but confusing)
- Examples directory referenced but doesn't exist

**Options**:
1. Move `extraction_schema.json` into skill at `references/schema/`
   - Pro: Single source of truth
   - Con: Schema evolves with prompts, creates versioning issue

2. Remove `schema/examples/` reference from SKILL.md (doesn't exist)
   - Pro: Accurate
   - Con: Examples would be useful

3. Create `references/schema/examples/` with real extraction snippets
   - Pro: Very helpful for learning
   - Con: Adds maintenance burden

**Recommendation**: Option 2 + 3
- Remove non-existent directory reference
- Consider adding small example snippets to schema-guide.md inline (not separate files)

---

## Part 3: Redundancy Across Files

### Issue 7: Explicit vs Implicit Explained Multiple Times

**Locations**:
1. extraction-fundamentals.md (lines 24-66) - Full treatment
2. extraction-fundamentals.md (lines 68-158) - Implicit RDMAP specific
3. extraction-fundamentals.md (lines 161-315) - Implicit Arguments specific
4. schema-guide.md - Field definitions
5. verbatim-quote-requirements.md - Sourcing context
6. Multiple prompts (not in skill)

**Assessment**: ACCEPTABLE REDUNDANCY
- extraction-fundamentals.md is the canonical source
- Other files reference or apply the concept
- Not harmful duplication (concept application vs definition)

**No action needed** - this is appropriate layered explanation

---

### Issue 8: Consolidation Mentioned in Multiple Contexts

**Locations**:
1. SKILL.md (lines 182-225) - Algorithm ← DUPLICATION
2. consolidation-patterns.md (lines 1-529) - Full guide
3. Cross-reference repair in consolidation-patterns.md (lines 411-520) - New section
4. extraction-fundamentals.md - Brief mentions
5. Multiple prompts (not in skill)

**Assessment**: DUPLICATION (addressed in Issue 2)
- consolidation-patterns.md is canonical
- SKILL.md duplication should be removed
- Other mentions are references (acceptable)

**Action needed**: Remove from SKILL.md per Issue 2

---

## Part 4: Missing Crucial Content

### Gap 1: No "Getting Started" or "Quick Start" Guide

**Observation**:
- SKILL.md explains workflow but assumes user knows what passes are
- No file explaining "first time using research-assessor? start here"
- New users must piece together workflow from SKILL.md + prompts

**Impact**: MINOR (skill is for Claude, not end users)
- Claude can infer workflow from SKILL.md
- Human users have prompts to guide them

**Recommendation**: NOT NEEDED (skill is for Claude consumption)

---

### Gap 2: No Troubleshooting or FAQ

**Observation**:
- No file addressing common extraction problems
- No "what if verification fails?" guidance beyond verification-procedures.md
- No "validation pass failed - now what?" guide

**Impact**: MINOR
- verification-procedures.md covers validation
- Troubleshooting lives in operational usage, not skill

**Recommendation**: CONSIDER for future version
- Could add `references/troubleshooting.md` with common failure modes
- Not critical for current version

---

### Gap 3: Version/Changelog in Skill

**Observation**:
- SKILL_README.md (outside skill) documents versions
- No version tracking in skill itself
- extraction-fundamentals.md has "Last Updated: 2025-10-21" but no version number

**Impact**: MINOR
- Skill versions tracked externally (acceptable)
- Individual files have last-updated dates

**Recommendation**: OPTIONAL
- Consider adding version tag to SKILL.md metadata
- Not required by skill-creator guidance

---

## Part 5: File-by-File Quality Assessment

### SKILL.md (268 lines)

**Purpose**: Main skill file with workflow and navigation

**Content Quality**: ⭐⭐⭐⭐ (4/5)
- Well-structured
- Clear workflow
- Good navigation to references

**Issues**:
- 🔴 Contains duplicated content (76 lines should move to references)
- 🟡 Slightly over skill-creator "lean" guidance once duplication removed

**Size After Cleanup**: ~192 lines (acceptable, under 5k words)

---

### extraction-fundamentals.md (474 lines)

**Purpose**: Universal sourcing requirements + implicit patterns

**Content Quality**: ⭐⭐⭐⭐⭐ (5/5)
- Comprehensive
- Well-organised with recent improvements
- Excellent recognition patterns for implicit RDMAP and Arguments

**Issues**:
- None significant
- File is large (474 lines) but justified by comprehensive coverage

**Recommendation**: NO CHANGES NEEDED

---

### consolidation-patterns.md (529 lines)

**Purpose**: Consolidation decision framework + cross-reference repair

**Content Quality**: ⭐⭐⭐⭐⭐ (5/5)
- Comprehensive with excellent examples
- Recent cross-reference repair addition is critical
- Clear decision trees

**Issues**:
- None significant
- Algorithm duplicated in SKILL.md (addressed in Issue 2)

**Recommendation**: NO CHANGES to this file (remove duplication from SKILL.md instead)

---

### tier-assignment-guide.md (193 lines)

**Purpose**: Design vs Method vs Protocol tier decisions

**Content Quality**: ⭐⭐⭐⭐⭐ (5/5)
- Clear decision framework
- Good examples
- Granularity principle well-explained

**Issues**:
- Content overlap with research-design-extraction-guide.md (addressed in Issue 4)
- Hierarchy duplicated in SKILL.md (addressed in Issue 1)

**Recommendation**: Keep as-is, clarify relationship with research-design-extraction-guide.md

---

### research-design-extraction-guide.md (346 lines)

**Purpose**: Operational guidance for finding all Research Designs

**Content Quality**: ⭐⭐⭐⭐ (4/5)
- Excellent operational content
- 10 practices are valuable
- Worked example helpful

**Issues**:
- 🟡 File name not in SKILL.md navigation (line 109 only mentions tier-assignment-guide.md)
- 🟡 Relationship with tier-assignment-guide.md unclear
- 🟡 Feels like "special case" (no parallel for Claims/Evidence)

**Recommendation**:
- Rename to `research-design-operational-guide.md` for clarity
- Add explicit navigation in SKILL.md
- Consider creating parallel for Claims/Evidence

---

### expected-information.md (208 lines)

**Purpose**: Completeness checklists

**Content Quality**: ⭐⭐⭐⭐⭐ (5/5)
- Comprehensive domain checklists
- Well-organised by claim type and domain
- Valuable reference

**Issues**: None

**Recommendation**: NO CHANGES NEEDED

---

### verbatim-quote-requirements.md (438 lines)

**Purpose**: Strict verbatim quote rules

**Content Quality**: ⭐⭐⭐⭐⭐ (5/5)
- Critical for preventing validation failures
- Clear examples
- Comprehensive guidance

**Issues**: None

**Recommendation**: NO CHANGES NEEDED

---

### verification-procedures.md (1519 lines)

**Purpose**: Pass 3 validation procedures

**Content Quality**: ⭐⭐⭐⭐⭐ (5/5)
- Comprehensive validation guidance
- Decision trees
- Complete coverage

**Issues**:
- Very large file (1519 lines)
- But justified by comprehensive validation coverage

**Recommendation**: NO CHANGES NEEDED (size is appropriate for complexity)

---

### schema-guide.md (19,957 bytes / ~600 lines)

**Purpose**: Human-readable schema documentation

**Content Quality**: ⭐⭐⭐⭐⭐ (5/5)
- Complete object definitions
- Field requirements clear
- Well-organised

**Issues**:
- references/schema/examples/ directory doesn't exist (mentioned in SKILL.md)

**Recommendation**: Remove examples/ reference from SKILL.md or create directory

---

### sobotkova-example.md (6528 bytes / ~200 lines)

**Purpose**: Worked extraction example

**Content Quality**: ⭐⭐⭐⭐ (4/5)
- Good real-world example
- Helpful for learning

**Issues**:
- Only one example (could use more)
- File name mentioned in SKILL.md is "sobotkova-methods.md" but actual file is "sobotkova-example.md"

**Recommendation**: Fix filename reference in SKILL.md line 114

---

## Part 6: Overall Recommendations

### Priority 1: Eliminate Duplication from SKILL.md 🔴 CRITICAL

**Action**: Remove duplicated content from SKILL.md
- Remove RDMAP Hierarchy section (lines 162-180) → Replace with pointer
- Remove Consolidation Logic section (lines 182-225) → Replace with pointer
- Keeps SKILL.md lean (<200 lines after cleanup)

**Impact**: Reduces SKILL.md from 268 → ~192 lines, eliminates 76 lines of duplication

**Skill-Creator Principle**: "Information should live in either SKILL.md or references files, not both"

---

### Priority 2: Fix Content Distribution Issues 🟡 IMPORTANT

**Action 1**: Clarify Research Design guidance structure
- Keep tier-assignment-guide.md and research-design-extraction-guide.md separate
- Rename research-design-extraction-guide.md → research-design-operational-guide.md
- Add both to SKILL.md navigation explicitly

**Action 2**: Fix schema examples reference
- Remove `references/schema/examples/` from SKILL.md (doesn't exist)
- OR create directory with small JSON snippets

**Action 3**: Fix filename mismatch
- SKILL.md line 114 says "sobotkova-methods.md"
- Actual file is "sobotkova-example.md"
- Update SKILL.md reference

---

### Priority 3: Consider Symmetry Improvements 🟢 OPTIONAL

**Action 1**: Create claims-evidence-operational-guide.md
- Parallel to research-design-operational-guide.md
- Operational patterns for finding claims, evidence, implicit arguments
- Reduces reliance on prompt evolution

**Action 2**: Consider Evidence vs Claims reference file
- Currently only in SKILL.md (13 lines)
- Could create references/checklists/evidence-vs-claims-guide.md
- OR keep in SKILL.md as core principle (it's lean enough)

---

## Summary Table

| Issue | Type | Severity | Lines Affected | Priority |
|-------|------|----------|----------------|----------|
| RDMAP Hierarchy Duplication | Duplication | 🔴 Critical | SKILL.md 19 lines | P1 |
| Consolidation Algorithm Duplication | Duplication | 🔴 Critical | SKILL.md 44 lines | P1 |
| Evidence vs Claims (no ref file) | Gap/Partial Dup | 🟡 Medium | SKILL.md 13 lines | P3 |
| Research Design split across 2 files | Distribution | 🟡 Medium | 2 files, 539 lines | P2 |
| No Claims/Evidence operational guide | Gap | 🟢 Low | N/A (missing) | P3 |
| Schema examples/ doesn't exist | Incomplete | 🟡 Medium | SKILL.md 1 line | P2 |
| Filename mismatch (sobotkova) | Error | 🟡 Medium | SKILL.md 1 line | P2 |

---

## Proposed Refactored SKILL.md (excerpt)

```markdown
## Core Decision Frameworks

### Evidence vs. Claims

**Evidence** = Raw observations requiring minimal interpretation (direct measurements, data points)
**Claims** = Assertions that interpret or generalize (require reasoning or expertise)

**Test:** "Does this require expertise to assess or just checking sources?"

### RDMAP Three-Tier Hierarchy

**Research Designs** (WHY), **Methods** (WHAT), **Protocols** (HOW)

**For complete tier assignment guidance:**
→ See `references/checklists/tier-assignment-guide.md`

**For operational guidance on finding all Research Designs:**
→ See `references/research-design-operational-guide.md`

### Consolidation Logic

Evidence items with **identical claim support patterns** that are **never cited independently** should be consolidated.

**For complete algorithm, examples, and cross-reference repair:**
→ See `references/checklists/consolidation-patterns.md`
```

---

## Conclusion

The research-assessor skill is **high-quality and comprehensive** but has evolved to contain **significant duplication** between SKILL.md and reference files (76 lines, 28% of SKILL.md).

**Key Improvements**:
1. **Remove duplication from SKILL.md** (Priority 1 - Critical)
2. **Fix distribution and navigation issues** (Priority 2 - Important)
3. **Consider symmetry improvements** (Priority 3 - Optional)

**After refactoring**, the skill will be:
- ✅ 100% skill-creator compliant (no duplication)
- ✅ Leaner SKILL.md (~192 lines vs 268)
- ✅ Better navigation (all reference files properly listed)
- ✅ Fixed inconsistencies (filenames, missing directories)

**Estimated effort**: 1-2 hours to implement Priority 1 and 2 changes

**Risk**: LOW - changes are additive/removal only, no content modification needed
