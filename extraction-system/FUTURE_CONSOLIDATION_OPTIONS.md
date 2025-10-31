# Future Consolidation Options for Pass 1 Prompt

**Created:** 2025-10-30
**Context:** Prompt refactoring to manage length while maintaining extraction performance

---

## Completed Consolidation (Phases 1-2, 3.3)

**Total savings: 100 lines (20% reduction from 509 to ~409 lines)**

### Phase 1.1: Literary/Historical Section ✅ COMPLETED
- **Lines saved:** 66 lines (91 → 32 lines)
- **Risk level:** VERY LOW
- **Approach:** Moved detailed citation formats, verification protocol, and worked examples to skill
- **Maintained:** Core decision rule, procedural steps, reference to comprehensive guidance
- **Location:** Lines 253-284 (new numbering after edits)

### Phase 1.2: Verbatim Requirements ✅ COMPLETED
- **Lines saved:** 4 lines (20 → 16 lines)
- **Risk level:** VERY LOW (conservative approach)
- **Approach:** Minimal wording tightening, added reference to comprehensive guide
- **Maintained:** All 4 critical rules, self-check test, failure warning
- **Location:** Lines 76-91 (new numbering after edits)

### Phase 1.3: Sourcing Requirements ✅ COMPLETED
- **Lines saved:** 8 lines (28 → 20 lines)
- **Risk level:** VERY LOW (conservative approach)
- **Approach:** Condensed formatting, removed duplicate references, tightened blank lines
- **Maintained:** All requirements for evidence/claims/implicit arguments, quick tests, all warnings
- **Location:** Lines 95-115 (new numbering after edits)

### Phase 3.3: Output Format ✅ COMPLETED
- **Lines saved:** 22 lines (37 → 15 lines)
- **Risk level:** LOW
- **Approach:** Replaced full JSON example with concise bullet-point description
- **Maintained:** Key instruction (return same JSON, populate these arrays), reference to schema-guide.md
- **Location:** Lines 372-386 (new numbering after edits)

---

## Deferred Options (Pending Testing)

### Phase 3.1: Consolidate Extraction Philosophy

**Current state:** Lines 117-155 (39 lines)

**Potential savings:** 12 lines → 27 lines target

**Risk level:** LOW-MEDIUM

**Rationale for deferral:**
- Pass 1 philosophy is critical to over-extraction strategy
- "When uncertain: INCLUDE IT" mental model needs reinforcement
- Want to verify current refactoring maintains performance before further changes

**Proposed approach:**

Condense lines 124-162 from 39 lines to ~27 lines by:

1. **Keep unchanged (essential):**
   - Section title and lead statement
   - Liberal extraction mental model (Pass 1 = CAPTURE, Pass 2 = CONSOLIDATE)
   - Active rules checklist (✓ When uncertain: EXTRACT IT, etc.)
   - Penalty framework (will NOT be penalized for / WILL be penalized for)

2. **Condense:**
   - "Never think during Pass 1" examples (reduce from 3 to 2 examples)
   - Application paragraph (tighten from 4 bullets to 3)
   - Remove one example from penalty sections

3. **Move to skill (if needed):**
   - Detailed worked examples of over-extraction scenarios
   - Extended rationale for liberal extraction approach

**Implementation guidance:**
```markdown
## EXTRACTION PHILOSOPHY FOR PASS 1

**When uncertain whether something qualifies as evidence/claim: INCLUDE IT.**

### Liberal Extraction Mental Model

**Pass 1 job:** CAPTURE (comprehensively)
**Pass 2 job:** CONSOLIDATE (rationally)

**Active rules during Pass 1:**
- ✓ When uncertain: EXTRACT IT
- ✓ When granular: KEEP IT SEPARATE
- ✓ When related items: DON'T CONSOLIDATE YET

**Never think during Pass 1:**
- ✗ "This seems too detailed for final output"
- ✗ "These should probably merge"

**Remember:** Pass 2 can merge. Pass 1 cannot recover missed items.

### Application

- Better to over-extract and consolidate later than miss important content
- Accept some over-extraction as expected and manageable
- Focus on comprehensive capture, not perfect classification

**You will NOT be penalised for:**
- Extracting too many items (Pass 2 consolidates)
- Being overly granular (Pass 2 lumps related items)

**You WILL be penalised for:**
- Missing important claims or evidence
- Under-extracting due to uncertainty
- **Extracting items without proper sourcing (verbatim_quote OR trigger_text)**
```

**Testing requirements:**
- Run on next 2 papers
- Verify over-extraction behaviour maintained
- Confirm no false conservatism in extraction decisions

---

### Phase 3.2: Condense Implicit Arguments

**Current state:** Lines 219-367 (149 lines)

**Potential savings:** 8 lines → 141 lines target

**Risk level:** MEDIUM

**Rationale for deferral:**
- Implicit argument extraction most challenging aspect
- Recent performance improvements (systematic search, 4-type framework)
- Want to verify current refactoring maintains quality before further changes
- Higher risk due to complexity of the task

**Proposed approach:**

Condense lines 219-367 from 149 lines to ~141 lines by:

1. **Keep unchanged (essential):**
   - Section title and priority statement
   - 4-type framework with definitions and test questions
   - REQUIRED systematic search instruction for all core claims
   - Common pitfalls checklist
   - Quality check requirements
   - References to detailed guidance

2. **Condense:**
   - Type definitions: reduce examples from 2 per type to 1 per type (save 4 lines)
   - Common pitfalls: reduce from 6 items to 4 items (save 4 lines)

3. **Consider moving to skill (if further consolidation needed):**
   - Extended worked examples for each type
   - Detailed recognition patterns
   - Cross-section assumption guidance

**Implementation guidance:**
```markdown
### 4. Implicit Arguments (HIGH-PRIORITY claims only)

**Extract implicit arguments for all core claims (REQUIRED systematic search) and key intermediate claims (as applicable).**

**Four types:**

**Type 1: Logical Implications** - Unstated steps in reasoning chain
- IF the explicit claims are true, THEN X must also be true
- Example: "Method is accurate" implies "Equipment was calibrated"

**Type 2: Unstated Assumptions** - Prerequisites assumed without acknowledgement
- Authors assume X is true without stating or justifying it
- Example: Spatial analysis assumes GPS accuracy adequate

**Type 3: Bridging Claims** - Missing links between evidence and conclusions
- Evidence → ??? → Claim (what's the ???)
- Example: "Complete data" → "High quality data" needs bridging argument

**Type 4: Disciplinary Assumptions** - Field-specific taken-for-granted knowledge
- Domain experts assume X without stating it
- Example: Archaeologists assume surface visibility relates to artifact presence

[... rest of section continues with systematic search workflow ...]

**Common Pitfalls When Extracting Implicit Arguments:**
- ❌ Superficial scan instead of systematic 4-type review per core claim
- ❌ Missing cross-section assumptions (note for Pass 2)
- ❌ No trigger_text (your inference without textual basis = hallucination)
- ❌ Treating all domain knowledge as implicit (only extract if paper's reasoning relies on it)

[... quality check and references ...]
```

**Testing requirements:**
- Run on next 3 papers (need more samples due to higher risk)
- Verify systematic search still occurring
- Confirm all 4 types still being identified
- Check trigger_text quality remains high
- Ensure cross-section assumptions still noted

---

## Testing Protocol

**Before implementing Phase 3.1 or 3.2:**

1. **Baseline performance verification:**
   - Run extraction on next paper using current (~409 line) prompt
   - Document: evidence count, claims count, implicit arguments count
   - Note: any sourcing failures, any under-extraction indicators

2. **Implement deferred phase:**
   - Choose either 3.1 or 3.2 (recommend 3.1 first due to lower risk)
   - Apply changes as documented above
   - Commit with clear message indicating experimental status

3. **Performance testing:**
   - Run extraction on 2-3 papers (type depends on risk level)
   - Compare metrics against baseline
   - Check for:
     - Over-extraction maintained (Pass 1 philosophy)
     - Systematic search occurring (implicit arguments)
     - Sourcing quality unchanged
     - No false conservatism

4. **Decision:**
   - If performance maintained → Keep changes, proceed to next phase
   - If performance degraded → Revert, document why, consider alternative approach

---

## Additional Opportunities (Lower Priority)

### Other sections that could be further optimised:

**Section-by-section extraction workflow (lines 305-376):**
- Currently 72 lines
- Could potentially save 5-10 lines by condensing step descriptions
- Risk: MEDIUM (workflow clarity is important)
- Priority: LOW (current length acceptable)

**Quality Checklist (lines 410-434):**
- Currently 25 lines
- Could potentially save 3-5 lines by tightening formatting
- Risk: LOW (checklist format allows scanning)
- Priority: LOW (checklists benefit from explicit formatting)

**Core Extraction Principles (lines 165-282):**
- Currently 118 lines across 6 subsections
- Evidence vs Claims distinction: Could reference guide more
- Could potentially save 10-15 lines across all subsections
- Risk: MEDIUM (principles are foundational)
- Priority: MEDIUM (consider if need further reduction)

---

## Progressive Disclosure Principle

**Reminder:** Per skill-creator guidance:

- **Prompts should contain:** Procedural workflow, decision rules, critical warnings
- **Skills should contain:** Detailed examples, edge cases, comprehensive frameworks

**Good signs current refactoring follows this:**
- ✅ Critical rules remain in prompt (verbatim, sourcing, 4-type framework)
- ✅ Detailed examples moved to skill (citation formats, boundary cases)
- ✅ References clearly signpost where to find detail
- ✅ Prompt remains scannable and procedural

**Watch for:**
- ❌ Prompt becoming too sparse (losing procedural clarity)
- ❌ Over-reliance on external references (breaking workflow)
- ❌ Moving critical decision rules to skill (should stay in prompt)

---

## Maintenance Notes

**When updating this document:**
- Mark phases as COMPLETED when implemented and tested
- Add new phases as opportunities identified
- Document actual line savings vs estimates
- Note any performance impacts observed
- Update testing protocol based on lessons learned

**When updating prompts or skills:**
- Check this document for deferred consolidation opportunities
- Consider whether new content could live in skill instead of prompt
- Maintain the progressive disclosure principle
- Test thoroughly before considering additional consolidation
