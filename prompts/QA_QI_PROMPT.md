# Extraction Workflow QA/QI Assessment Prompt

**Purpose:** Systematic quality assurance (find errors/inconsistencies/omissions) and quality improvement (identify optimization opportunities) for the research-assessor extraction workflow.

**Scope:** Schema, prompts (all 5), skill package (SKILL.md + references)

**Use:** Run this assessment after significant changes or periodically to maintain quality

---

## PART 1: QUALITY ASSURANCE (QA) - Find Problems

### Check 1: Schema-Prompt Consistency

**Goal:** Ensure prompts and schema are perfectly aligned

**Procedure:**
1. **Field Existence:** For every field referenced in prompts, verify it exists in schema
   - Check required fields match
   - Check enum values match
   - Check field names match exactly (case-sensitive)

2. **Field Requirements:** Verify required vs optional matches
   - If prompt says "REQUIRED", schema should not allow null
   - If prompt says "optional", schema should allow null
   - Check for mismatches

3. **Object Structure:** Verify object shapes match
   - Nested objects in schema match prompt descriptions
   - Array structures match
   - Cross-reference fields consistent

**Output for Check 1:**
- List of mismatches found
- Severity (CRITICAL, HIGH, MEDIUM, LOW)
- Specific location in prompt and schema
- Recommended fix

---

### Check 2: Prompt-Skill Reference Accuracy

**Goal:** Ensure all skill references in prompts are accurate and resolvable

**Procedure:**
1. **File Existence:** For every skill reference in prompts, verify file exists
   - Check path accuracy: `/mnt/skills/user/research-assessor/references/[file].md`
   - Verify file is actually in skill package
   - Check for broken references

2. **Content Accuracy:** Verify referenced content actually exists in skill file
   - If prompt says "See X in [file]", verify X is actually there
   - Check section names match
   - Verify examples referenced actually exist

3. **Version Compatibility:** Check for schema version mismatches
   - Prompts reference schema v2.5
   - Skill files reference schema v2.5
   - No outdated version references

**Output for Check 2:**
- List of broken references
- List of inaccurate references (points to wrong section)
- List of version mismatches
- Recommended fixes

---

### Check 3: Terminology Consistency

**Goal:** Ensure consistent terminology across all documents

**Procedure:**
1. **Field Names:** Check for name variations
   - `consolidated_from` vs `source_items`
   - `verbatim_quote` vs `verbatim_text` vs `quote`
   - `trigger_text` vs `trigger_passages`
   - Any other variations

2. **Concept Names:** Check for inconsistent concept naming
   - "Liberal extraction" vs "Over-extraction" vs "Comprehensive capture"
   - "Rationalization" vs "Consolidation" vs "Refinement"
   - "Validation" vs "Verification" vs "Quality checks"

3. **Status Values:** Check enum consistency
   - "explicit" vs "Explicit" (case)
   - "implicit" vs "Implicit"
   - Any other enum value variations

4. **Cross-Document Consistency:** Verify same term used same way everywhere
   - Schema uses term X
   - All prompts use term X
   - All skill files use term X

**Output for Check 3:**
- List of terminology inconsistencies
- Recommended standard term
- Locations to fix

---

### Check 4: Completeness Checks

**Goal:** Ensure no critical information is missing

**Procedure:**
1. **All Object Types Covered:**
   - Evidence: Pass 1, Pass 2, Pass 3 procedures ✓
   - Claims: Pass 1, Pass 2, Pass 3 procedures ✓
   - Implicit Arguments: Pass 1, Pass 2, Pass 3 procedures ✓
   - Research Designs: Pass 1, Pass 2, Pass 3 procedures ✓
   - Methods: Pass 1, Pass 2, Pass 3 procedures ✓
   - Protocols: Pass 1, Pass 2, Pass 3 procedures ✓

2. **All Required Fields Documented:**
   - Schema defines field
   - At least one prompt explains when/how to populate it
   - Skill reference documents it

3. **All Workflows Covered:**
   - Pass 1: Liberal extraction workflow ✓
   - Pass 2: Rationalization workflow ✓
   - Pass 3: Validation workflow ✓
   - Each has clear steps

4. **All Decision Points Covered:**
   - Evidence vs Claims: Decision framework provided ✓
   - Explicit vs Implicit: Decision framework provided ✓
   - Design vs Method vs Protocol: Decision framework provided ✓
   - Consolidate vs Keep Separate: Decision framework provided ✓

**Output for Check 4:**
- List of gaps (object type not covered, field not documented, etc.)
- Missing decision frameworks
- Incomplete workflows
- Recommended additions

---

### Check 5: Internal Consistency Within Prompts

**Goal:** Ensure each prompt is internally consistent

**Procedure:**
1. **Example Consistency:** Check examples match current schema
   - Examples show v2.5 structure
   - Examples include all required fields
   - Examples don't show deprecated fields

2. **Instruction Consistency:** Check for contradictions
   - One section says "always X"
   - Another section says "sometimes not-X"
   - Flag contradictions

3. **Quality Checklist Alignment:** Verify checklist matches instructions
   - If instructions emphasize X, checklist includes X
   - No checklist items for things not in instructions
   - Checklist is comprehensive

**Output for Check 5:**
- List of contradictions found
- Outdated examples
- Checklist gaps or misalignments
- Recommended fixes

---

### Check 6: Critical Sourcing Requirements

**Goal:** Verify hallucination prevention is enforced throughout

**Procedure:**
1. **Explicit Items:** Verify all prompts enforce verbatim_quote requirement
   - Evidence must have verbatim_quote
   - Claims must have verbatim_quote
   - Explicit RDMAP must have verbatim_quote
   - No exceptions allowed

2. **Implicit Items:** Verify all prompts enforce trigger infrastructure
   - Implicit Arguments need trigger_text + trigger_locations + inference_reasoning
   - Implicit RDMAP needs same plus implicit_metadata
   - No exceptions allowed

3. **Quick Tests:** Verify decision questions present
   - "Can I point to exact text?" → explicit
   - "Can I point to passages that imply this?" → implicit
   - "If no" → DO NOT EXTRACT

4. **Zero Tolerance Language:** Check for enforcement language
   - Prompts use phrases like "MANDATORY", "NO EXCEPTIONS", "DO NOT EXTRACT"
   - Consequences clear for violations
   - No hedging or softening of requirements

**Output for Check 6:**
- Any weakening of sourcing requirements
- Missing quick tests
- Unclear enforcement
- Locations to strengthen

---

### Check 7: Cross-Reference Architecture

**Goal:** Ensure cross-reference system is consistent and complete

**Procedure:**
1. **Bidirectional Consistency:** Check all cross-reference instructions
   - If A references B, B should reference A
   - Instructions for maintaining bidirectionality
   - Validation checks for broken references

2. **Array Naming:** Verify consistent array names
   - `supports_claims` vs `supported_by_claims`
   - `implements_designs` vs `enabled_by_designs`
   - All variations documented

3. **Cross-Type References:** Check complex reference support
   - Methods can reference Claims ✓
   - Protocols can reference Evidence ✓
   - All cross-type patterns documented

**Output for Check 7:**
- Inconsistent array naming
- Missing bidirectionality instructions
- Undocumented cross-type patterns
- Recommended fixes

---

## PART 2: QUALITY IMPROVEMENT (QI) - Optimize

### Optimization 1: Duplication Analysis

**Goal:** Find content duplicated across multiple documents

**Procedure:**
1. **Identify Duplication:**
   - Content in multiple prompts
   - Content in both prompts and skill files
   - Content in multiple skill files

2. **Assess Appropriateness:**
   - Is duplication intentional (brief reminders)?
   - Or wasteful (same detailed explanation multiple places)?

3. **Recommend Consolidation:**
   - Where should canonical version live?
   - How should other locations reference it?
   - What stays as brief reminder?

**Output for Optimization 1:**
- List of duplications found
- Assessment (appropriate or wasteful)
- Consolidation recommendations
- Estimated line savings

---

### Optimization 2: Streamlining Opportunities

**Goal:** Identify verbose sections that could be more concise

**Procedure:**
1. **Identify Verbose Sections:**
   - Sections >50 lines
   - Extensive examples
   - Detailed procedures that are in skill files

2. **Assess Information Density:**
   - How much new information per line?
   - Could examples be reduced?
   - Could procedures be referenced instead of reproduced?

3. **Recommend Compression:**
   - Keep essential concept (10-20 lines)
   - Add pointer to comprehensive version
   - Estimated line savings

**Output for Optimization 2:**
- List of verbose sections
- Information density assessment
- Compression recommendations
- Estimated line savings

---

### Optimization 3: Progressive Disclosure Assessment

**Goal:** Verify proper use of skill architecture for progressive disclosure

**Procedure:**
1. **Check Pattern Compliance:**
   - SKILL.md is lean (<500 lines)
   - Detailed procedures in references/ files
   - Prompts reference rather than reproduce

2. **Identify Violations:**
   - Detailed procedures in prompts (should be in skill)
   - Comprehensive examples in prompts (should be in skill)
   - Missing references to existing skill content

3. **Recommend Improvements:**
   - Move content to skill references
   - Add pointers from prompts
   - Strengthen READ FIRST statements

**Output for Optimization 3:**
- Progressive disclosure violations
- Content that should move to skill
- Missing pointer opportunities
- Architectural improvements

---

### Optimization 4: Skill Reference Enhancement

**Goal:** Improve effectiveness of skill references

**Procedure:**
1. **Assess Current References:**
   - Are they prominent enough?
   - Do they explain WHY to read the file?
   - Do they explain WHAT'S in the file?

2. **Check Reference Pattern:**
   - First mention: `**READ FIRST:** /full/path` ✓
   - Subsequent: `→ See references/file.md` ✓
   - Brief description of content ✓

3. **Identify Improvements:**
   - References that need prominence
   - References that need better description
   - Missing references to available content

**Output for Optimization 4:**
- Under-prominent references
- Poorly described references
- Missing reference opportunities
- Enhancement recommendations

---

### Optimization 5: Checklist Standardization

**Goal:** Ensure quality checklists are consistent and optimally structured

**Procedure:**
1. **Compare Checklist Structures:**
   - Pass 1: Checklists have same structure?
   - Pass 2: Checklists have same structure?
   - Pass 3: Checklists have same structure?

2. **Check Recommended Structure:**
   - Sourcing verified (always first)
   - Content completeness
   - Relationships correct
   - Expected information flagged
   - Other arrays untouched (always last)

3. **Identify Improvements:**
   - Reorder for consistency
   - Add missing items
   - Remove redundant items

**Output for Optimization 5:**
- Checklist structure inconsistencies
- Recommended standard structure
- Items to add/remove/reorder

---

### Optimization 6: Example Quality

**Goal:** Ensure examples are helpful and current

**Procedure:**
1. **Check Example Currency:**
   - Examples show v2.5 structure
   - Examples include all required fields
   - Examples reflect current best practices

2. **Assess Example Quantity:**
   - Too many examples (overwhelming)?
   - Too few examples (unclear)?
   - Right balance (2-3 per concept)?

3. **Evaluate Example Clarity:**
   - Examples demonstrate key points clearly
   - Examples show both good and bad patterns
   - Examples are realistic

**Output for Optimization 6:**
- Outdated examples to update
- Excess examples to remove
- Missing examples to add
- Clarity improvements

---

### Optimization 7: Token Efficiency

**Goal:** Maximize information density per token

**Procedure:**
1. **Identify Low-Density Sections:**
   - Repetitive phrasing
   - Unnecessary verbosity
   - Redundant explanations

2. **Assess Compression Potential:**
   - Can section be 50% shorter without information loss?
   - Can bullet points replace paragraphs?
   - Can tables replace long lists?

3. **Recommend Improvements:**
   - Specific compressions
   - Format changes
   - Information reorganization

**Output for Optimization 7:**
- Low-density sections
- Compression recommendations
- Format improvements
- Estimated token savings

---

## PART 3: ASSESSMENT OUTPUT FORMAT

For each check/optimization, provide:

```markdown
## [Check/Optimization Name]

### Status
- ✅ PASS - No issues found
- ⚠️ MINOR - Non-critical issues found
- ⛔ CRITICAL - Blocking issues found

### Issues Found
[List each issue with:]
- **Location:** [File name, line numbers, section]
- **Issue:** [Clear description]
- **Impact:** [Critical/High/Medium/Low]
- **Evidence:** [Specific quote or example showing the issue]

### Recommendations
[For each issue:]
- **Recommended Fix:** [Specific action to take]
- **Effort:** [Minutes/Hours estimate]
- **Priority:** [Must fix/Should fix/Nice to have]

### Estimated Improvements
- **Line savings:** [If applicable]
- **Token savings:** [If applicable]
- **Quality improvement:** [Description]
```

---

## PART 4: PRIORITIZED ACTION PLAN

After completing all checks, create prioritized action plan:

### Critical Issues (Must Fix Before Deployment)
1. [Issue with location and fix]
2. [Issue with location and fix]
...

### High-Priority Improvements (Should Fix Soon)
1. [Issue with location and fix]
2. [Issue with location and fix]
...

### Medium-Priority Optimizations (Good to Have)
1. [Optimization with estimated benefit]
2. [Optimization with estimated benefit]
...

### Low-Priority Polish (When Time Permits)
1. [Minor improvement]
2. [Minor improvement]
...

---

## USAGE INSTRUCTIONS

### Full Assessment (All Checks)
Use when:
- After major changes to prompts or schema
- Before significant deployment
- Periodic comprehensive review (every 3-6 months)

**Time required:** 4-6 hours
**Benefits:** Complete quality assurance + optimization

---

### Quick QA Check (Part 1 Only)
Use when:
- After minor prompt edits
- After schema field additions
- Regular maintenance (monthly)

**Time required:** 1-2 hours
**Benefits:** Catch errors and inconsistencies

---

### Optimization Review (Part 2 Only)
Use when:
- Prompts feel too long
- Context window concerns
- Seeking efficiency improvements

**Time required:** 2-3 hours
**Benefits:** Streamlining and token efficiency

---

### Targeted Check (Specific Checks)
Use when:
- Specific concern (e.g., "are all my references accurate?")
- Focused improvement area
- Quick validation of specific change

**Time required:** 30 minutes - 1 hour per check
**Benefits:** Focused, efficient review

---

## CRITICAL SUCCESS FACTORS

1. **Be Systematic:** Complete each check thoroughly, don't skip steps
2. **Provide Evidence:** Always show specific examples of issues found
3. **Be Specific:** "Line 45 uses 'source_items', schema uses 'consolidated_from'" not "field names inconsistent"
4. **Prioritize:** Not all issues are equal, indicate severity clearly
5. **Be Actionable:** Every issue should have clear recommended fix
6. **Estimate Impact:** Indicate line/token savings or quality improvement

---

## ASSESSMENT CHECKLIST

Before submitting assessment:
- [ ] All applicable checks completed
- [ ] Each issue has location, evidence, recommendation
- [ ] Severity/priority assigned to each issue
- [ ] Action plan prioritized by criticality
- [ ] Estimated effort for each fix
- [ ] Estimated benefits quantified where possible
- [ ] Output format followed consistently

---

**This QA/QI assessment prompt provides systematic, comprehensive evaluation of the extraction workflow. Use regularly to maintain quality and identify optimization opportunities.**
