# Prompt-to-Skill Content Optimization Analysis

**Date**: 2025-10-27
**Analyzer**: skill-creator skill assessment
**Context**: After Phase 1-3 refactoring, analyze prompts for remaining content that should move to skill

---

## Executive Summary

**Overall Assessment**: Prompts contain **~350 lines of conceptual/framework content** that should move to skill references.

**Key Skill-Creator Principle Applied**:
> "Information should live in either SKILL.md or references files, not both. Prefer references files for detailed information unless it's truly core to the skill. Keep only essential procedural instructions and workflow guidance in SKILL.md; move detailed reference material, schemas, and examples to references files."

**Findings**:
- 🔴 **CRITICAL**: 3 duplications (~89 lines) - content exists in BOTH prompts AND skill
- 🟡 **HIGH PRIORITY**: 8 conceptual frameworks (~263 lines) - belong in skill references, not prompts
- 🟢 **OPTIONAL**: Pass-specific content that could be generalized (~50 lines)

**Estimated Impact**:
- Prompts: 2,426 → ~2,070 lines (15% reduction)
- New skill references: +400 lines (organized, reusable)
- Reduced duplication, improved maintainability

---

## Part 1: Critical Duplications

### DUPLICATION 1: Evidence vs Claims Distinction

**Location 1**: SKILL.md lines 148-160 (13 lines)
**Location 2**: Prompt 01 lines 106-122 (17 lines)

**Assessment**: FULL DUPLICATION
- Both define Evidence vs Claims with same test
- Prompt 01 has slightly more detail (examples)
- **Violates**: "Information should live in either SKILL.md or references files, not both"

**Recommendation**:
- Create `references/checklists/evidence-vs-claims-guide.md` (comprehensive version)
- Remove from SKILL.md (replace with pointer)
- Remove from Prompt 01 (replace with reference)

**Impact**: -30 lines total

---

### DUPLICATION 2: RDMAP Three-Tier Hierarchy (Decision Tree Form)

**Location 1**: tier-assignment-guide.md (full treatment, 193 lines)
**Location 2**: Prompt 03 lines 146-184 (39 lines)

**Assessment**: PARTIAL DUPLICATION
- tier-assignment-guide.md has comprehensive guidance
- Prompt 03 repeats basic decision tree and tier definitions
- Already removed from SKILL.md in Phase 1

**Recommendation**:
- Remove decision tree from Prompt 03
- Replace with: "See `references/checklists/tier-assignment-guide.md` for decision tree"

**Impact**: -39 lines

---

### DUPLICATION 3: Tier Assignment Verification (in Pass 2)

**Location 1**: tier-assignment-guide.md (tier definitions)
**Location 2**: Prompt 04 lines 199-223 (25 lines)

**Assessment**: PARTIAL DUPLICATION
- Prompt 04 repeats tier indicators for verification
- tier-assignment-guide.md already has this

**Recommendation**:
- Remove tier definitions from Prompt 04
- Replace with reference to tier-assignment-guide.md
- Keep verification workflow instructions

**Impact**: -20 lines

---

## Part 2: High Priority - Conceptual Frameworks Belong in Skill

### CANDIDATE 1: Claims Hierarchy (4-Level)

**Location**: Prompt 01 lines 139-160 (22 lines)

**Content**:
```markdown
**CORE claims** (typically 5-10 per paper)
- Main thesis, key findings, primary contributions

**INTERMEDIATE claims** (vary by paper)
- Support core claims
- May have their own supporting claims

**SUPPORTING claims**
- Directly supported by evidence
- Bottom layer of claim hierarchy

**EVIDENCE**
- Observations, measurements, data
```

**Assessment**: Conceptual framework, not pass-specific
- Defines claim hierarchy structure
- Needed for Pass 1 AND Pass 2
- Currently only in Prompt 01

**Recommendation**:
- Create `references/checklists/claims-hierarchy-guide.md`
- Include hierarchy levels, identification guidance, relationship mapping
- Reference from both Prompts 01 and 02

**Impact**: -22 lines from prompt, +60 lines in new reference

---

### CANDIDATE 2: Multi-Dimensional Evidence Pattern

**Location**: Prompt 02 lines 134-168 (35 lines)

**Content**: Detailed pattern for handling evidence with multiple analytical dimensions

**Assessment**: Consolidation decision framework
- Not Pass 2 specific - applies to any consolidation decision
- Conceptual pattern with decision criteria
- Belongs with other consolidation patterns

**Recommendation**:
- Move to `references/checklists/consolidation-patterns.md`
- Add as new section after existing patterns
- Reference from Prompt 02

**Impact**: -35 lines from prompt, +40 lines to consolidation-patterns.md

---

### CANDIDATE 3: Description vs Argumentation Boundary

**Location**: Prompt 03 lines 189-205 (17 lines)

**Content**:
```markdown
**RDMAP = Methodological Descriptions (what was done)**
**Claims/Evidence = Argumentation (assertions about what worked)**
**Test:** "Is this describing HOW research was done, or ARGUING about how well it worked?"
```

**Assessment**: Core decision framework
- Needed for RDMAP Pass 1 AND Pass 2
- Boundary distinction, not pass-specific
- Conceptual knowledge

**Recommendation**:
- Add to `references/checklists/tier-assignment-guide.md` as new section
- Or create new `references/checklists/rdmap-vs-claims-guide.md`
- Reference from Prompts 03 and 04

**Impact**: -17 lines from prompt, +25 lines to reference

---

### CANDIDATE 4: Reasoning Approach Classification

**Location**: Prompt 03 lines 207-235 (29 lines)

**Content**:
```markdown
**Inductive** - Data to patterns to theory
**Abductive** - Anomaly to best explanation
**Deductive** - Theory to predictions to test
**Mixed** - Genuine combination
**Unclear** - Insufficient information
```

**Assessment**: Research Design classification framework
- Applies to Research Design extraction and verification
- Needed in Pass 1 and Pass 2
- Domain knowledge, not workflow

**Recommendation**:
- Move to `references/research-design-operational-guide.md` as new section
- Include indicators, timing inference, confidence assessment
- Reference from Prompts 03 and 04

**Impact**: -29 lines from prompt, +40 lines to reference

---

### CANDIDATE 5: Research Questions vs Hypotheses

**Location**: Prompt 03 lines 237-257 (21 lines)

**Content**: Distinction between RQs and hypotheses, timing inference

**Assessment**: Research Design classification knowledge
- Conceptual framework
- Needed for extraction and verification
- Domain knowledge

**Recommendation**:
- Move to `references/research-design-operational-guide.md` with Candidate 4
- Include timing basis, confidence assessment
- Reference from Prompt 03

**Impact**: -21 lines from prompt, +30 lines to reference

---

### CANDIDATE 6: Fieldwork-Specific Considerations

**Location**: Prompt 03 lines 289-308 (20 lines)

**Content**: Opportunistic decisions, contingency plans, emergent discoveries

**Assessment**: Domain-specific patterns
- Applies to fieldwork-based research generally
- Not Pass 1 specific
- Domain knowledge

**Recommendation**:
- Move to `references/research-design-operational-guide.md`
- Or new `references/fieldwork-patterns.md` if more content needed
- Reference from Prompt 03

**Impact**: -20 lines from prompt, +30 lines to reference

---

### CANDIDATE 7: RDMAP-Specific Consolidation Patterns (6 Patterns)

**Location**: Prompt 04 lines 150-194 (45 lines)

**Content**:
```markdown
Pattern 1: Design Rationale Synthesis
Pattern 2: Scope Definition Consolidation
Pattern 3: Workflow Method Aggregation
Pattern 4: Validation Chain Consolidation
Pattern 5: Protocol Specification Consolidation
Pattern 6: Parameter Aggregation
```

**Assessment**: Consolidation decision frameworks
- RDMAP-specific but not Pass 2 specific
- Belongs with other consolidation patterns
- Conceptual patterns

**Recommendation**:
- Move to `references/checklists/consolidation-patterns.md`
- Add as "RDMAP Consolidation Patterns" section
- Already referenced in Prompt 04 (just needs content there)

**Impact**: -45 lines from prompt, +60 lines to consolidation-patterns.md

---

### CANDIDATE 8: Reasoning Approach Consistency (Verification)

**Location**: Prompt 04 lines 269-283 (15 lines)

**Content**: Verification of reasoning approach classifications

**Assessment**: Related to Candidate 4
- Verification guidance for reasoning approaches
- Should be with reasoning approach classification

**Recommendation**:
- Move to same location as Candidate 4 (research-design-operational-guide.md)
- Add as "Verification" subsection
- Reference from Prompt 04

**Impact**: -15 lines from prompt, +20 lines to reference

---

## Part 3: Optional - Pass-Specific Content That Could Be Generalized

### OPTIONAL 1: Strategic Verbosity in Claims

**Location**: Prompt 02 lines 207-220 (14 lines)

**Assessment**: Pass 2 specific guidance
- About how to write consolidated claims
- Could be generalized to "good claim writing"

**Recommendation**: KEEP IN PROMPT
- Pass 2 specific context
- Not worth moving

---

### OPTIONAL 2: Calculation Claims vs Evidence

**Location**: Prompt 02 lines 222-241 (20 lines)

**Assessment**: Specific type of over-extraction to remove
- Pass 2 rationalization pattern
- Could generalize to "redundancy patterns"

**Recommendation**: Consider moving to consolidation-patterns.md
- As "Common Over-Extraction Patterns" section
- Low priority

**Impact**: -20 lines from prompt, +25 lines to reference

---

### OPTIONAL 3: Pass 2 Addition Patterns

**Location**: Prompt 02 lines 243-265 (23 lines)

**Assessment**: Pass 2 specific
- About what to ADD in Pass 2
- Workflow guidance, not conceptual

**Recommendation**: KEEP IN PROMPT
- Pass 2 specific orchestration

---

## Part 4: Summary of Recommendations

### Priority 1: Critical Duplications (Remove Immediately)

| Content | Lines | From | To | Impact |
|---------|-------|------|-----|--------|
| Evidence vs Claims | 30 | SKILL.md + P01 | New reference | -30 prompt |
| RDMAP Hierarchy (decision tree) | 39 | P03 | tier-assignment-guide.md | -39 prompt |
| Tier definitions (verification) | 20 | P04 | tier-assignment-guide.md | -20 prompt |
| **TOTAL P1** | **89** | | | **-89 prompt** |

### Priority 2: High-Value Moves (Significant Benefit)

| Content | Lines | From | To | Impact |
|---------|-------|------|-----|--------|
| Claims Hierarchy | 22 | P01 | New claims-hierarchy-guide.md | -22 prompt |
| Multi-Dimensional Evidence | 35 | P02 | consolidation-patterns.md | -35 prompt |
| Description vs Argumentation | 17 | P03 | tier-assignment-guide.md | -17 prompt |
| Reasoning Approach Classification | 29 | P03 | research-design-operational-guide.md | -29 prompt |
| Research Questions vs Hypotheses | 21 | P03 | research-design-operational-guide.md | -21 prompt |
| Fieldwork Considerations | 20 | P03 | research-design-operational-guide.md | -20 prompt |
| RDMAP Consolidation Patterns | 45 | P04 | consolidation-patterns.md | -45 prompt |
| Reasoning Verification | 15 | P04 | research-design-operational-guide.md | -15 prompt |
| **TOTAL P2** | **204** | | | **-204 prompt** |

### Priority 3: Optional (Nice-to-Have)

| Content | Lines | From | To | Impact |
|---------|-------|------|-----|--------|
| Calculation Claims Pattern | 20 | P02 | consolidation-patterns.md | -20 prompt |
| **TOTAL P3** | **20** | | | **-20 prompt** |

### Overall Impact Summary

**If implementing ALL recommendations:**

| Metric | Before | After | Change |
|--------|--------|-------|--------|
| **Total Prompt Lines** | 2,426 | 2,113 | -313 (-13%) |
| **Prompt 01** | 343 | 289 | -54 (-16%) |
| **Prompt 02** | 425 | 335 | -90 (-21%) |
| **Prompt 03** | 595 | 469 | -126 (-21%) |
| **Prompt 04** | 557 | 472 | -85 (-15%) |
| **Prompt 05** | 506 | 506 | 0 (0%) |

**New/Enhanced Skill References:**

| File | Action | Lines Added |
|------|--------|-------------|
| evidence-vs-claims-guide.md | CREATE | +30 |
| claims-hierarchy-guide.md | CREATE | +60 |
| consolidation-patterns.md | ENHANCE | +125 |
| tier-assignment-guide.md | ENHANCE | +62 |
| research-design-operational-guide.md | ENHANCE | +105 |
| **Total Skill Growth** | | **+382** |

**Net Effect:**
- Prompts: -313 lines (leaner, more focused on workflow)
- Skill: +382 lines (more comprehensive, reusable)
- Reduction in duplication: -89 lines
- Better separation of concerns

---

## Part 5: Implementation Strategy

### Phase A: Quick Wins (Priority 1 - Critical Duplications)

**Effort**: 1-2 hours
**Risk**: LOW (just removal + pointers)

1. Create `references/checklists/evidence-vs-claims-guide.md`
2. Remove Evidence vs Claims from SKILL.md and Prompt 01
3. Remove RDMAP decision tree from Prompt 03
4. Remove tier definitions from Prompt 04
5. Test: Verify references resolve correctly

**Deliverable**: -89 prompt lines, +30 skill lines, zero duplication

### Phase B: High-Value Moves (Priority 2 - Conceptual Frameworks)

**Effort**: 3-4 hours
**Risk**: MEDIUM (requires careful content migration)

1. Create `references/checklists/claims-hierarchy-guide.md`
2. Enhance `consolidation-patterns.md` with:
   - Multi-Dimensional Evidence Pattern section
   - RDMAP Consolidation Patterns section
3. Enhance `tier-assignment-guide.md` with:
   - Description vs Argumentation Boundary section
4. Enhance `research-design-operational-guide.md` with:
   - Reasoning Approach Classification section
   - Research Questions vs Hypotheses section
   - Fieldwork Considerations section
   - Reasoning Verification section
5. Update all prompt references
6. Test: Full extraction run to verify nothing broken

**Deliverable**: -204 prompt lines, +352 skill lines, better organization

### Phase C: Optional Polish (Priority 3)

**Effort**: 1 hour
**Risk**: LOW

1. Add Calculation Claims Pattern to consolidation-patterns.md
2. Update Prompt 02 reference

**Deliverable**: -20 prompt lines, +25 skill lines

---

## Part 6: File Structure After Optimization

### New Reference Files

```
references/
├── checklists/
│   ├── consolidation-patterns.md        # ENHANCED (+125 lines)
│   ├── tier-assignment-guide.md         # ENHANCED (+62 lines)
│   ├── evidence-vs-claims-guide.md      # NEW (+30 lines)
│   ├── claims-hierarchy-guide.md        # NEW (+60 lines)
│   └── expected-information.md          # UNCHANGED
├── research-design-operational-guide.md # ENHANCED (+105 lines)
├── extraction-fundamentals.md           # UNCHANGED
├── verbatim-quote-requirements.md       # UNCHANGED
└── verification-procedures.md           # UNCHANGED
```

### Skill Navigation Update (SKILL.md)

```markdown
**Decision Frameworks:**
- `references/checklists/evidence-vs-claims-guide.md` - Evidence vs Claims boundary (with examples and edge cases)
- `references/checklists/claims-hierarchy-guide.md` - 4-level claims hierarchy (Core/Intermediate/Supporting/Evidence)
- `references/checklists/tier-assignment-guide.md` - RDMAP tier decisions (Design/Method/Protocol) + Description vs Argumentation boundary
- `references/research-design-operational-guide.md` - Research Design patterns: reasoning approaches, RQ vs hypotheses, fieldwork considerations
- `references/checklists/consolidation-patterns.md` - Consolidation patterns including multi-dimensional evidence and RDMAP-specific patterns
- `references/checklists/expected-information.md` - Domain-specific completeness checklists
```

---

## Part 7: Benefits Analysis

### For Prompts (Leaner, More Focused)

**Before Optimization:**
- Prompts contain mixture of workflow + conceptual frameworks
- Repeated concepts across prompts (duplication)
- Hard to update (change concept → update multiple prompts)
- Context-heavy (2,426 lines total)

**After Optimization:**
- Prompts focus on workflow orchestration ("DO this, THEN that")
- Conceptual frameworks referenced, not repeated
- Easy to update (change concept → update one reference file)
- Lighter context (2,113 lines total)

### For Skill (More Comprehensive, Reusable)

**Before Optimization:**
- Some frameworks missing from skill entirely
- Scattered knowledge (some in SKILL.md, some in prompts)
- Limited reusability

**After Optimization:**
- All decision frameworks centralized in skill
- Organized by topic (claims, consolidation, RDMAP, etc.)
- Reusable across passes and use cases
- Progressive disclosure works better

### For Maintenance

**Before Optimization:**
- Update framework → find all prompt locations
- Risk of inconsistency
- Duplication between SKILL.md and prompts

**After Optimization:**
- Update framework → edit one reference file
- Single source of truth
- Zero duplication

### For Users/Claude

**Before Optimization:**
- Must read full prompts to understand frameworks
- Frameworks buried in workflow instructions
- No central reference for "how do I decide X?"

**After Optimization:**
- Reference files provide comprehensive guidance
- Prompts provide workflow with pointers to details
- Clear separation: "what to do" (prompt) vs "how to decide" (skill)

---

## Part 8: Risks and Mitigations

### Risk 1: Breaking Existing Workflows

**Concern**: Removing content from prompts breaks extraction

**Mitigation**:
- Test with full extraction after each phase
- Keep prompts functional (replace removed content with clear references)
- Verify all references resolve correctly

### Risk 2: Over-Abstracting

**Concern**: Moving too much makes prompts too abstract

**Mitigation**:
- Keep workflow orchestration in prompts
- Move only conceptual/framework content
- Prompts remain self-contained for "what to do when"

### Risk 3: Increasing Context Load

**Concern**: More skill references → more reading

**Mitigation**:
- Progressive disclosure: read only when uncertain
- Well-named files make it clear when to read
- Comprehensive table of contents in SKILL.md

---

## Part 9: Recommended Next Steps

### Immediate (User Decision Needed)

1. **Review this analysis** - Confirm approach and priorities
2. **Approve Phase A** - Quick wins (critical duplications)
3. **Approve Phase B** - High-value moves (conceptual frameworks)
4. **Decide on Phase C** - Optional polish

### After Approval

1. **Implement Phase A** (1-2 hours)
   - Create evidence-vs-claims-guide.md
   - Remove duplications
   - Test

2. **Implement Phase B** (3-4 hours)
   - Create claims-hierarchy-guide.md
   - Enhance consolidation-patterns.md
   - Enhance tier-assignment-guide.md
   - Enhance research-design-operational-guide.md
   - Update all prompt references
   - Full extraction test

3. **Implement Phase C** (optional, 1 hour)
   - Add calculation claims pattern
   - Test

4. **Documentation**
   - Update SKILL_README.md with new reference files
   - Git commit with detailed message
   - Archive old prompts for reference

---

## Conclusion

The prompts currently contain **~313 lines of conceptual/framework content** that belongs in skill references according to skill-creator principles. Moving this content will:

- ✅ Eliminate 89 lines of duplication
- ✅ Reduce prompt size by 13% (2,426 → 2,113 lines)
- ✅ Centralize decision frameworks in skill
- ✅ Improve maintainability (single source of truth)
- ✅ Better separation of concerns (workflow vs concepts)
- ✅ Enable reuse across passes

**Recommendation**: Implement Phases A and B (Priority 1 and 2) for maximum benefit with acceptable effort/risk ratio.
