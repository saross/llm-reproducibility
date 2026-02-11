# Extraction Workflow QA/QI Assessment Prompt v3.0

**Purpose:** Systematic quality assurance (find errors) and quality improvement (optimize efficiency) for research-assessor extraction workflow

**Core Imperatives:**
1. **Consistency:** No contradictions across prompts, schema, skill, WORKFLOW.md
2. **Lean Prompts:** Optimal division (prompts minimal, skill comprehensive)
3. **Performance:** Comprehensive, high-quality, consistent extraction output

**Scope:** Schema, 5 prompts, skill package, WORKFLOW.md

---

## QUICK START

### 5-Minute Check (After Minor Changes)
```bash
# Run automated checks
bash qa-checks.sh quick

# Review output for CRITICAL/HIGH issues only
```

### 30-Minute Check (Before Deployment)
```bash
# Full automated checks + manual verification
bash qa-checks.sh full

# Complete PART 2 (QA) or PART 3 (QI) based on change type
# Run test extraction validation
```

---

## PART 1: AUTOMATED CHECKS (Run First)

### Check 0: File Sync Status

**Automated:**
```bash
# Verify skill directories synced
diff -r .claude/skills/research-assessor/ extraction-system/skill/research-assessor/

# Check for orphaned files
find extraction-system/prompts/ -name "*.md" -type f
find extraction-system/skill/research-assessor/references/ -name "*.md" -type f
```

**Manual:** Review diff output, sync any mismatches

---

### Check 1: Schema-Prompt Field Consistency

**Automated:**
```bash
# Extract all field names from prompts
grep -roh '[a-z_]*_quote\|[a-z_]*_text\|[a-z_]*_metadata\|[a-z_]*_status' extraction-system/prompts/*.md | sort -u > /tmp/prompt_fields.txt

# Extract schema field names
jq -r '.. | objects | keys[]' extraction-system/schema/extraction_schema.json | sort -u > /tmp/schema_fields.txt

# Find mismatches
comm -23 /tmp/prompt_fields.txt /tmp/schema_fields.txt
```

**Manual Verification:**
1. For each mismatch: Check if it's a typo or legitimate variation
2. Verify enum values match exactly (case-sensitive)
3. Check required fields are enforced in both places

**Critical Patterns:**
- `verbatim_quote` (not verbatim_text)
- `trigger_text` (not trigger_passages)
- `consolidated_from` (not source_items)
- Status: "explicit" / "implicit" (lowercase)

---

### Check 2: Skill Reference Accuracy

**Automated:**
```bash
# Extract all skill references from prompts
grep -roh 'references/[^) ]*\.md' extraction-system/prompts/ | sort -u > /tmp/refs.txt

# Check if files exist
while read ref; do
  test -f "extraction-system/skill/research-assessor/$ref" || echo "MISSING: $ref"
done < /tmp/refs.txt

# Check loaded skill has same files
while read ref; do
  test -f ".claude/skills/research-assessor/$ref" || echo "MISSING FROM LOADED: $ref"
done < /tmp/refs.txt
```

**Manual Verification:**
1. Verify section names match (if prompt says "See Section X", X exists)
2. Check examples referenced actually present
3. Confirm paths use correct format: `/mnt/skills/user/research-assessor/references/...` for skill context

---

### Check 3: Terminology Consistency

**Automated:**
```bash
# Check for terminology variations
echo "=== Checking for term variations ==="
echo "verbatim_quote variations:"
grep -r "verbatim_text\|verbatim_quote\|quote_text" extraction-system/ | grep -v ".git\|node_modules"

echo "consolidation variations:"
grep -r "source_items\|consolidated_from\|merged_from" extraction-system/ | grep -v ".git"

echo "Liberal extraction variations:"
grep -r "liberal\|over-extract\|comprehensive capture" extraction-system/prompts/ | wc -l

echo "Status case variations:"
grep -r '"Explicit"\|"Implicit"\|"explicit"\|"implicit"' extraction-system/ | grep -v ".git"
```

**Standard Terms (Use Everywhere):**
- Extraction approach: "liberal extraction" (not "over-extraction" or "comprehensive capture")
- Pass 2: "rationalisation" (not "consolidation" or "refinement")
- Explicit/Implicit: lowercase in JSON, capitalised in prose
- Source field: `consolidated_from` (not `source_items`)

**Manual:** Fix any variations found to use standard terms

---

### Check 4: Critical Sourcing Requirements

**Automated:**
```bash
# Check extraction.json for hallucination patterns
echo "=== Checking for unsourced items ==="
jq '.evidence[] | select(.verbatim_quote == null or .verbatim_quote == "") | .evidence_id' outputs/*/extraction.json

jq '.implicit_arguments[] | select(.trigger_text == null or (.trigger_text | length) == 0) | .implicit_argument_id' outputs/*/extraction.json

# Check for hallucination language
echo "=== Checking for hallucination indicators ==="
grep -r "appears to\|seems to\|likely states\|probably" outputs/*/extraction.json
```

**Manual Verification:**
1. Verify all prompts enforce `verbatim_quote` for explicit items (MANDATORY language)
2. Verify all prompts enforce `trigger_text` + `trigger_locations` for implicit items
3. Check for "zero tolerance" enforcement language in prompts
4. Search prompts for: "CRITICAL:", "MANDATORY:", "DO NOT EXTRACT if"

**Required Patterns in ALL Pass 1 Prompts:**
- Verbatim quote requirements section (with complete sentences rule)
- Explicit/implicit decision tree
- "Can I point to exact text?" quick test
- NO EXCEPTIONS language

---

### Check 5: Liberal Extraction Emphasis

**Automated:**
```bash
# Count "INCLUDE IT" reminders
echo "=== Pass 1 Liberal Extraction Emphasis ==="
echo "01-claims-evidence:"
grep -c "INCLUDE IT\|when uncertain.*include\|err on the side" extraction-system/prompts/01-claims-evidence_pass1_prompt.md

echo "03-rdmap:"
grep -c "INCLUDE IT\|when uncertain.*include\|err on the side" extraction-system/prompts/03-rdmap_pass1_prompt.md

# Check philosophy sections present
grep -n "Extraction Philosophy\|EXTRACTION PHILOSOPHY" extraction-system/prompts/01-claims*.md extraction-system/prompts/03-rdmap*.md
```

**Expected Pattern:**
- Philosophy section: ~20 lines, "When uncertain: INCLUDE IT" header
- Workflow reminders: "When uncertain: INCLUDE IT" at each extraction step
- Minimum 3 mentions per Pass 1 prompt

**Manual:** If counts differ significantly (>50%), identify cause and align

---

### Check 6: Regression Watch - Known Issues

**Focus Areas (From Recent Fixes):**

**1. Tier Misclassification:**
```bash
# Check RD extraction guidance includes tactical decisions
grep -A5 "Platform.*selection\|Workflow.*architecture\|tool.*choice" extraction-system/prompts/03-rdmap_pass1_prompt.md
```
**Verify:** research-design-extraction-guide.md examples show platform/workflow as RD

**2. File Operation Safety:**
```bash
# Check WORKFLOW.md has safety rules
grep -n "NEVER.*partial.*Read\|Read.*limit.*Write\|data loss" extraction-system/WORKFLOW.md
```
**Verify:** Safety rules at lines ~98-144 present and unchanged

**3. Liberal Extraction Workflow Integration:**
```bash
# Verify reminders at Steps 2 & 3 in RDMAP prompt
sed -n '370,390p' extraction-system/prompts/03-rdmap_pass1_prompt.md | grep -c "INCLUDE IT"
```
**Expected:** 2 occurrences (Step 2 and Step 3)

---

## PART 2: MANUAL QA CHECKS (Find Errors & Inconsistencies)

### Check 7: Cross-Document Contradiction Scan

**Goal:** Ensure same concepts defined consistently across all files

**Procedure:**
1. **Pick 3 key concepts** (e.g., "explicit vs implicit", "tier hierarchy", "consolidation")
2. **Find all mentions** across prompts, schema, skill
   ```bash
   # Example: Check "explicit vs implicit" guidance
   grep -rn "explicit.*implicit\|Explicit.*Implicit" extraction-system/ --include="*.md" | head -20
   ```
3. **Verify consistency:** Same definition, same examples, same decision trees

**Common Contradictions:**
- Prompt says field required, schema makes it optional
- Different tier assignment criteria in different prompts
- Consolidation guidance conflicts between Pass 2 prompts
- Decision frameworks inconsistent across prompts

**Output:**
- List contradictions found with locations (file:line)
- Severity (CRITICAL if affects behaviour, HIGH if affects consistency)
- Recommended fix (which version is correct, where to propagate)

---

### Check 8: Checklist Standardisation

**Goal:** Ensure quality checklists across prompts follow consistent structure

**Procedure:**
1. **Extract all checklists:**
   ```bash
   # Find checklist sections in all prompts
   grep -A 30 "## Quality Checklist\|### Quality Checks" extraction-system/prompts/*.md
   ```

2. **Compare structures across pass types:**
   - Pass 1 prompts (01, 03): Should have same checklist order
   - Pass 2 prompts (02, 04): Should have same checklist order
   - Pass 3 prompt (05): Unique validation-focused structure OK

3. **Verify standard order (Pass 1 & 2):**
   - Sourcing verified (always first)
   - Content completeness
   - Relationships correct
   - Expected missing information flagged
   - Other arrays untouched (always last)

4. **Check count expectations:**
   - Research Designs: Check mentions "4-6 items expected" (not "1-2")
   - Methods: Liberal extraction emphasis present
   - Protocols: Liberal extraction emphasis present

**Output:**
- Structural inconsistencies (different order, missing items)
- Count expectation mismatches
- Recommended standard structure
- Where to align

---

### Check 9: Example Currency & Correctness

**Goal:** Ensure all examples show current schema and correct patterns

**Procedure:**
1. **Find all examples:**
   ```bash
   # Extract code blocks that look like JSON examples
   grep -A 15 '```json\|```javascript' extraction-system/prompts/*.md
   ```

2. **Check schema version:**
   - All examples show v2.5 structure (current version)
   - No examples with deprecated fields (`source_items`, `verbatim_text`)
   - Required fields present in all examples

3. **Check pattern correctness:**
   - Evidence examples: `verbatim_quote` populated with complete sentences
   - Implicit examples: `trigger_text` + `trigger_locations` + `inference_reasoning` present
   - Cross-reference examples: Bidirectional arrays correct
   - Consolidated items: `consolidated_from` array populated

4. **Assess example quality:**
   - Examples demonstrate key distinctions (evidence vs claim, explicit vs implicit)
   - Examples realistic (drawn from actual papers, not contrived)
   - Examples show both correct and incorrect patterns where helpful

**Output:**
- Outdated examples (v2.4, v2.3 structures)
- Incorrect examples (wrong patterns, missing fields)
- Missing examples (concepts explained but not demonstrated)
- Recommended fixes/additions

---

## PART 3: MANUAL QI OPTIMISATIONS (Reduce Bloat & Increase Clarity)

### Optimisation 1: Duplication Analysis

**Goal:** Find and eliminate duplicated content across files

**Procedure:**
1. **Identify duplication (>20 lines):**
   ```bash
   # Find potentially duplicated sections
   for file in extraction-system/prompts/*.md; do
     echo "=== $file ==="
     awk '/^##/ {section=$0} {print section ":" $0}' "$file" | sort
   done | uniq -c | sort -rn | head -20
   ```

2. **Assess each duplication:**
   - **Intentional reminder:** Brief (5-10 lines), different context, acceptable
   - **Wasteful reproduction:** Full procedure (30+ lines), identical content, should consolidate

3. **Determine canonical location:**
   - Detailed procedures → skill references
   - Core philosophy → each Pass 1 prompt (intentional duplication)
   - Examples → skill references
   - Decision frameworks → skill references with brief prompt summary

4. **Recommend consolidation:**
   - Where should full version live?
   - How should prompts reference it?
   - What stays as brief reminder (1-3 lines)?

**Output:**
- List of duplications (content, length, locations)
- Assessment (intentional vs wasteful)
- Consolidation plan (canonical location + reference pattern)
- Estimated line savings

---

### Optimisation 2: Streamlining Opportunities

**Goal:** Identify verbose sections and compress without information loss

**Procedure:**
1. **Find verbose sections (>50 lines):**
   ```bash
   # Show section lengths
   for file in extraction-system/prompts/*.md; do
     awk '/^##/ {if (section) print length_count " " prev_section; section=$0; prev_section=$0; length_count=0} {length_count++} END {print length_count " " section}' "$file"
   done | sort -rn
   ```

2. **Assess information density:**
   - Count unique concepts per 10 lines
   - Identify repetitive phrasing (same point made multiple times)
   - Check for verbose examples that could be compressed
   - Look for paragraph text that could be bullet points

3. **Identify compression strategies:**
   - **Prose → bullets:** Paragraph explanations → concise bullet lists
   - **Long examples → tables:** 20-line examples → 5-line table
   - **Procedures → skill:** Detailed step-by-step → summary + skill reference
   - **Repetition removal:** Same concept explained in 3 places → 1 place

4. **Estimate compression potential:**
   - Can section be 50% shorter without information loss?
   - Can formatting change improve density?
   - Should content move to skill instead?

**Output:**
- Verbose sections (location, length, density assessment)
- Compression recommendations (specific strategy per section)
- Estimated line savings
- Priority (high = low-density + long section)

---

### Optimisation 3: Prompt-Skill Division

**Goal:** Optimal division with prompts lean, skill comprehensive

**Procedure:**
1. **Scan prompts for content that should be in skill:**
   - Detailed procedures (>30 lines)
   - Comprehensive examples (>15 lines per example)
   - Background theory/rationale
   - Edge case catalogues
   - Extended decision trees

2. **Check if equivalent content exists in skill:**
   ```bash
   # List skill reference files
   ls -lh extraction-system/skill/research-assessor/references/

   # Check which are referenced by prompts
   grep -roh 'references/[^)]*\.md' extraction-system/prompts/
   ```

3. **Assess each potential move:**
   - **Essential for execution:** Keep in prompt (even if detailed)
   - **Reference material:** Move to skill, add pointer from prompt
   - **Already in skill:** Just add/strengthen prompt reference

4. **Check current targets:**
   - Each prompt ≤600 lines ✓
   - Each skill reference ≤500 lines ✓
   - Prompts focused on workflow, skill focused on knowledge ✓

**Output:**
- Content to move from prompts to skill (with rationale)
- Orphaned skill content (in skill but not referenced by any prompt)
- Missing references (content in skill but prompt doesn't point to it)
- Estimated line savings from moves
- Current prompt/skill lengths vs targets

---

### Optimisation 4: Output Consistency Factors

**Goal:** Identify factors causing run-to-run variation

**Procedure:**
1. **Check for ambiguous language:**
   ```bash
   grep -n "may\|might\|could\|consider\|optionally" extraction-system/prompts/*.md | wc -l
   ```
   - Ambiguity → inconsistency
   - Verify ambiguous language is intentional (e.g., "may be explicit or implicit" is OK)
   - Flag unintentional ambiguity (e.g., "you might want to extract this")

2. **Check for clear decision criteria:**
   - Evidence vs Claims: Test provided? ("supports or refutes" = claim)
   - Explicit vs Implicit: Decision tree provided? ("Can I point to text" test)
   - Tier assignment: WHY/WHAT/HOW test provided?
   - Consolidate vs Keep: Assessment compatibility test provided?

3. **Check for edge case guidance:**
   - Implicit arguments: 4 types with examples present?
   - Research designs: Meta-level framing examples present?
   - Consolidation: Temporal comparison examples (when NOT to consolidate)?

4. **Verify quantitative guidance:**
   - Pass 1: "40-50% over-extraction expected" present?
   - Pass 2: "15-20% reduction target" present?
   - Research Designs: "4-6 items expected" (not 1-2) present?

**Output:**
- Ambiguous instructions (location + suggested clarification)
- Missing decision criteria (concept + needed framework)
- Missing edge case examples (type + suggested addition)
- Inconsistent quantitative guidance (current vs recommended)

---

## PART 4: EXTRACTION VALIDATION TEST

### Test Extraction on Known Baseline

**Setup:**
```bash
# Use Sobotkova et al. 2023 as test paper (known baseline)
PAPER="sobotkova-et-al-2023"
```

**Run Extraction:**
1. Clear previous output: `rm -rf outputs/$PAPER/`
2. Run full 5-pass extraction following WORKFLOW.md
3. Generate validation report

**Validate Output:**
```bash
# Check entity counts
jq '{
  evidence: (.evidence | length),
  claims: (.claims | length),
  implicit_arguments: (.implicit_arguments | length),
  research_designs: (.research_designs | length),
  methods: (.methods | length),
  protocols: (.protocols | length)
}' outputs/$PAPER/extraction.json
```

**Expected Ranges (Sobotkova Baseline):**
- Evidence: 40-110
- Claims: 60-90 (Core: 10-15, Intermediate: 25-35, Supporting: 40-60)
- Implicit Arguments: 4-8
- Research Designs: 4-6 (NOT 1-2) ← **Key regression watch**
- Methods: 5-10
- Protocols: 11-15

**Red Flags:**
- Research Designs <3: Under-extraction or tier misclassification
- Methods <4: Under-extraction
- Any category = 0: Critical failure

**Validation Report:**
```bash
# Check validation passed
jq '.summary.validation_status' outputs/$PAPER/validation_report.json
# Expected: "PASSED"

# Check warnings acceptable
jq '.summary.total_warnings' outputs/$PAPER/validation_report.json
# Expected: ≤10
```

---

## PART 5: AUTOMATED QA SCRIPT

**Location:** `extraction-system/qa-checks.sh` (executable)

**Usage:**
```bash
# Quick check (5 minutes) - Automated checks only
./extraction-system/qa-checks.sh quick

# Full check (30 minutes) - Automated + regression watch
./extraction-system/qa-checks.sh full
```

**What It Checks:**
- Check 0: File sync status
- Check 1: Schema-prompt field consistency
- Check 2: Skill reference accuracy
- Check 3: Terminology consistency
- Check 5: Liberal extraction emphasis
- Check 6: Regression watch (full mode only)

**Output Format:**
```
=== EXTRACTION SYSTEM QA CHECKS ===
Mode: [quick|full]

CHECK 0: File Sync Status
✅ PASS / ⚠️ WARN / ⛔ FAIL

[... for each check ...]

=== QA CHECKS COMPLETE ===
```

---

## OUTPUT FORMAT

### QA Report Template

**File:** `outputs/qa-reports/$(date +%Y-%m-%d)-qa-report.md`

```markdown
# QA Report: YYYY-MM-DD

## Status: ✅ PASS / ⚠️ MINOR / ⛔ CRITICAL

## Automated Checks

[Paste bash output here]

## Critical Issues (Must Fix)

1. **[Issue]** - Location: [file:line] - Fix: [action]

## High Priority (Should Fix)

1. **[Issue]** - Location: [file:line] - Fix: [action]

## Medium Priority (Good to Have)

1. **[Optimisation]** - Benefit: [description]

## Test Extraction Results

- Entity counts: [JSON output]
- Validation status: PASSED/FAILED
- Warnings: [count]

## Recommendations

1. [Action item with priority and effort estimate]
```

---

## USAGE

**After minor prompt edits:**
```bash
./extraction-system/qa-checks.sh quick
```

**Before deployment/significant changes:**
```bash
# 1. Run automated checks
./extraction-system/qa-checks.sh full

# 2. Complete PART 2 (QA) manually (15 min)
#    - Check 7: Cross-document contradictions
#    - Check 8: Checklist standardisation
#    - Check 9: Example currency

# 3. Run test extraction (PART 4) (10 min)

# 4. Generate QA report
```

**Monthly optimisation:**
```bash
# 1. Quick automated check
./extraction-system/qa-checks.sh quick

# 2. Complete PART 3 (QI) manually (20 min)
#    - Optimisation 1: Duplication analysis
#    - Optimisation 2: Streamlining opportunities
#    - Optimisation 3: Prompt-skill division
#    - Optimisation 4: Output consistency

# 3. Generate optimisation plan with line savings estimates
```

---

## CRITICAL SUCCESS FACTORS

1. **Automate first** - Run automated checks before manual work
2. **Separate QA from QI** - Fix errors first, optimise second
3. **Focus on imperatives** - Consistency, lean prompts, performance
4. **Test with real extraction** - Counts validate better than reading
5. **Document findings** - Use QA report template
6. **Prioritise fixes** - Critical → High → Medium → Low

---

**This streamlined QA/QI prompt separates error-finding (QA) from optimisation (QI) while maintaining focus on core imperatives. Run automated checks first (5 min), then targeted manual verification (15-25 min) for comprehensive quality assurance in 20-30 minutes total.**
