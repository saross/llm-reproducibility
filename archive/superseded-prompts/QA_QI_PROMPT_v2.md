# Extraction Workflow QA/QI Assessment Prompt v2.0

**Purpose:** Systematic quality assurance for research-assessor extraction workflow

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

# Complete Checks 1-3 manually (consistency deep-dive)
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
- Pass 2: "rationalization" (not "consolidation" or "refinement")
- Explicit/Implicit: lowercase in JSON, capitalized in prose
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

## PART 2: MANUAL CHECKS (Consistency Deep-Dive)

### Check 7: Cross-Document Contradiction Scan

**Procedure:**
1. **Pick 3 key concepts** (e.g., "explicit vs implicit", "tier hierarchy", "consolidation")
2. **Find all mentions** across prompts, schema, skill
3. **Verify consistency:** Same definition, same examples, same decision trees

**Method:**
```bash
# Example: Check "explicit vs implicit" guidance
grep -rn "explicit.*implicit\|Explicit.*Implicit" extraction-system/ --include="*.md" | head -20

# Read each occurrence, verify consistent definition
```

**Common Contradictions:**
- Prompt says field required, schema makes it optional
- Different tier assignment criteria in different prompts
- Consolidation guidance conflicts between Pass 2 prompts

---

### Check 8: Prompt-Skill Division Optimization

**Goal:** Prompts should be lean, skill should be comprehensive

**Scan Pattern:**

**For each Pass 1 prompt:**
1. **Find sections >30 lines** with detailed procedures/examples
2. **Check:** Does equivalent content exist in skill references?
3. **If yes:** Compress to 5-10 line summary + pointer to skill
4. **If no:** Decide: Keep in prompt (essential) or move to skill (reference material)

**For each skill reference:**
1. **Check:** Is this referenced by any prompt?
2. **If no:** Add reference to relevant prompt OR remove if unused

**Red Flags:**
- Detailed examples in prompts (>50 lines) - should be in skill
- Comprehensive procedures in prompts - should be in skill with prompt summary
- Skill content not referenced by any prompt - may be orphaned

**Target:** Each prompt ≤600 lines, skill references ≤500 lines each

---

### Check 9: Output Consistency Factors

**Goal:** Identify factors causing run-to-run variation

**Procedure:**

1. **Check for ambiguous language** in prompts:
```bash
grep -n "may\|might\|could\|consider\|optionally" extraction-system/prompts/*.md | wc -l
```
Ambiguity → inconsistency. Verify ambiguous language is intentional.

2. **Check for clear decision criteria:**
- Evidence vs Claims: Test provided?
- Explicit vs Implicit: Decision tree provided?
- Tier assignment: WHY/WHAT/HOW test provided?
- Consolidate vs Keep: Assessment compatibility test provided?

3. **Check for examples showing edge cases:**
- Implicit arguments: 4 types with examples
- Research designs: Meta-level framing examples
- Consolidation: Temporal comparison (never consolidate) examples

4. **Verify quantitative guidance:**
- Pass 1: "40-50% over-extraction expected"
- Pass 2: "15-20% reduction target"
- Research Designs: "4-6 items expected" (not 1-2)

**If missing:** Add clear criteria to reduce interpretive variance

---

## PART 3: EXTRACTION VALIDATION TEST

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
- Research Designs <3: Under-extraction, tier misclassification
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

## PART 4: AUTOMATED QA SCRIPT

**Create:** `extraction-system/qa-checks.sh`

```bash
#!/bin/bash
# Automated QA checks for extraction system

MODE=${1:-full}

echo "=== EXTRACTION SYSTEM QA CHECKS ==="
echo "Mode: $MODE"
echo ""

# Check 0: File Sync
echo "CHECK 0: File Sync Status"
DIFF_OUT=$(diff -qr .claude/skills/research-assessor/ extraction-system/skill/research-assessor/ 2>&1)
if [ -z "$DIFF_OUT" ]; then
  echo "✅ PASS - Skills directories synced"
else
  echo "⛔ FAIL - Skills out of sync:"
  echo "$DIFF_OUT"
fi
echo ""

# Check 1: Schema-Prompt Fields
echo "CHECK 1: Schema-Prompt Field Consistency"
grep -roh '[a-z_]*_quote\|[a-z_]*_text\|[a-z_]*_metadata\|[a-z_]*_status' extraction-system/prompts/*.md | sort -u > /tmp/prompt_fields.txt
jq -r '.. | objects | keys[]' extraction-system/schema/extraction_schema.json | sort -u > /tmp/schema_fields.txt
MISMATCHES=$(comm -23 /tmp/prompt_fields.txt /tmp/schema_fields.txt)
if [ -z "$MISMATCHES" ]; then
  echo "✅ PASS - All prompt fields exist in schema"
else
  echo "⚠️  WARN - Potential mismatches:"
  echo "$MISMATCHES"
fi
echo ""

# Check 2: Skill References
echo "CHECK 2: Skill Reference Accuracy"
grep -roh 'references/[^) ]*\.md' extraction-system/prompts/ | sort -u > /tmp/refs.txt
MISSING=""
while read ref; do
  if [ ! -f "extraction-system/skill/research-assessor/$ref" ]; then
    MISSING="$MISSING\n  - $ref"
  fi
done < /tmp/refs.txt
if [ -z "$MISSING" ]; then
  echo "✅ PASS - All referenced files exist"
else
  echo "⛔ FAIL - Missing files:$MISSING"
fi
echo ""

# Check 3: Terminology Consistency
echo "CHECK 3: Terminology Consistency"
TERM_ISSUES=0
WRONG_TERMS=$(grep -r "verbatim_text\|source_items" extraction-system/ --include="*.md" 2>/dev/null | grep -v ".git")
if [ ! -z "$WRONG_TERMS" ]; then
  echo "⚠️  WARN - Non-standard terminology found"
  TERM_ISSUES=1
fi

if [ $TERM_ISSUES -eq 0 ]; then
  echo "✅ PASS - Terminology consistent"
fi
echo ""

# Check 5: Liberal Extraction Emphasis
echo "CHECK 5: Liberal Extraction Emphasis"
COUNT_01=$(grep -c "INCLUDE IT\|when uncertain.*include" extraction-system/prompts/01-claims-evidence_pass1_prompt.md 2>/dev/null || echo 0)
COUNT_03=$(grep -c "INCLUDE IT\|when uncertain.*include" extraction-system/prompts/03-rdmap_pass1_prompt.md 2>/dev/null || echo 0)
echo "  01-claims-evidence: $COUNT_01 mentions"
echo "  03-rdmap: $COUNT_03 mentions"
if [ $COUNT_01 -ge 3 ] && [ $COUNT_03 -ge 3 ]; then
  echo "✅ PASS - Liberal extraction emphasized"
else
  echo "⚠️  WARN - Liberal extraction may be under-emphasized"
fi
echo ""

# Check 6: Regression Watch
if [ "$MODE" = "full" ]; then
  echo "CHECK 6: Regression Watch"

  # File safety rules
  if grep -q "NEVER.*partial.*Read\|Read.*limit.*Write" extraction-system/WORKFLOW.md; then
    echo "✅ PASS - File safety rules present"
  else
    echo "⛔ FAIL - File safety rules missing"
  fi

  # RDMAP liberal reminders
  RDMAP_REMINDERS=$(sed -n '370,390p' extraction-system/prompts/03-rdmap_pass1_prompt.md | grep -c "INCLUDE IT")
  if [ $RDMAP_REMINDERS -eq 2 ]; then
    echo "✅ PASS - RDMAP workflow reminders present"
  else
    echo "⛔ FAIL - RDMAP workflow reminders missing (found $RDMAP_REMINDERS, expected 2)"
  fi
  echo ""
fi

echo "=== QA CHECKS COMPLETE ==="
```

**Make executable:**
```bash
chmod +x extraction-system/qa-checks.sh
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

1. **[Optimization]** - Benefit: [description]

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

# 2. Complete Checks 7-9 manually (30 min)

# 3. Run test extraction (Part 3)

# 4. Generate QA report
```

**Monthly maintenance:**
```bash
# Quick automated check + spot-check one manual area
./extraction-system/qa-checks.sh quick
# Manual Check 8 (prompt-skill division)
```

---

## CRITICAL SUCCESS FACTORS

1. **Automate first** - Run automated checks before manual work
2. **Focus on imperatives** - Consistency, lean prompts, performance
3. **Test with real extraction** - Counts validate better than reading
4. **Document findings** - Use QA report template
5. **Prioritize fixes** - Critical → High → Medium → Low

---

**This streamlined QA/QI prompt focuses on core imperatives with automation for efficiency. Run automated checks first (5 min), then targeted manual verification (25 min) for comprehensive quality assurance in 30 minutes total.**
