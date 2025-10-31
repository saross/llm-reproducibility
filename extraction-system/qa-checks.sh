#!/bin/bash
# Automated QA checks for extraction system
# Usage: ./qa-checks.sh [quick|full]

MODE=${1:-full}

echo "=== EXTRACTION SYSTEM QA CHECKS ==="
echo "Mode: $MODE"
echo "Date: $(date +%Y-%m-%d)"
echo ""

CHECKS_PASSED=0
CHECKS_FAILED=0
CHECKS_WARN=0

# Helper function for status
check_status() {
  local status=$1
  local message=$2

  if [ "$status" = "PASS" ]; then
    echo "✅ PASS - $message"
    CHECKS_PASSED=$((CHECKS_PASSED + 1))
  elif [ "$status" = "FAIL" ]; then
    echo "⛔ FAIL - $message"
    CHECKS_FAILED=$((CHECKS_FAILED + 1))
  else
    echo "⚠️  WARN - $message"
    CHECKS_WARN=$((CHECKS_WARN + 1))
  fi
}

# Check 0: File Sync
echo "CHECK 0: File Sync Status"
DIFF_OUT=$(diff -qr .claude/skills/research-assessor/ extraction-system/skill/research-assessor/ 2>&1 | grep -v "\.git")
if [ -z "$DIFF_OUT" ]; then
  check_status "PASS" "Skills directories synced"
else
  check_status "FAIL" "Skills out of sync"
  echo "$DIFF_OUT" | head -5
fi
echo ""

# Check 1: Schema-Prompt Fields
echo "CHECK 1: Schema-Prompt Field Consistency"
# Scan only extraction prompts (0*.md, readme.md), exclude QA documentation
grep -roE '\b[a-z_]+_(quote|text|metadata|status)\b' extraction-system/prompts/0*.md extraction-system/prompts/readme.md 2>/dev/null | cut -d: -f2 | sort -u > /tmp/prompt_fields.txt
jq -r '.. | objects | keys[]' extraction-system/schema/extraction_schema.json 2>/dev/null | sort -u > /tmp/schema_fields.txt
# Filter out known validation report fields (legitimate, but not in extraction schema)
MISMATCHES=$(comm -23 /tmp/prompt_fields.txt /tmp/schema_fields.txt | grep -v "^$" | grep -v "overall_status\|validation_status")
if [ -z "$MISMATCHES" ]; then
  check_status "PASS" "All prompt fields exist in schema"
else
  check_status "WARN" "Potential field mismatches found"
  echo "  Mismatches: $(echo "$MISMATCHES" | tr '\n' ' ')"
fi
echo ""

# Check 2: Skill References
echo "CHECK 2: Skill Reference Accuracy"
grep -roh 'references/[^) ]*\.md' extraction-system/prompts/ 2>/dev/null | grep -v "\[file\]\|/file\.md" | sort -u > /tmp/refs.txt
MISSING_COUNT=0
MISSING_FILES=""
while read ref; do
  if [ ! -f "extraction-system/skill/research-assessor/$ref" ]; then
    MISSING_FILES="$MISSING_FILES\n  - $ref"
    MISSING_COUNT=$((MISSING_COUNT + 1))
  fi
done < /tmp/refs.txt

if [ $MISSING_COUNT -eq 0 ]; then
  check_status "PASS" "All $(wc -l < /tmp/refs.txt) referenced files exist"
else
  check_status "FAIL" "$MISSING_COUNT missing files"
  echo -e "$MISSING_FILES"
fi
echo ""

# Check 3: Terminology Consistency
echo "CHECK 3: Terminology Consistency"
WRONG_VERBATIM=$(grep -r "verbatim_text" extraction-system/prompts/0*.md extraction-system/prompts/readme.md extraction-system/skill/ 2>/dev/null | wc -l)
WRONG_SOURCE=$(grep -r "source_items" extraction-system/prompts/0*.md extraction-system/prompts/readme.md extraction-system/skill/ 2>/dev/null | wc -l)

if [ $WRONG_VERBATIM -eq 0 ] && [ $WRONG_SOURCE -eq 0 ]; then
  check_status "PASS" "Terminology consistent"
else
  check_status "WARN" "Non-standard terminology: verbatim_text ($WRONG_VERBATIM), source_items ($WRONG_SOURCE)"
fi
echo ""

# Check 4: Critical Sourcing (if extraction files exist)
if [ "$MODE" = "full" ] && [ -d "outputs" ]; then
  echo "CHECK 4: Critical Sourcing Requirements"

  # Find most recent extraction
  LATEST_EXTRACTION=$(find outputs -name "extraction.json" -type f -printf '%T@ %p\n' 2>/dev/null | sort -rn | head -1 | cut -d' ' -f2)

  if [ ! -z "$LATEST_EXTRACTION" ]; then
    # Check for unsourced evidence
    UNSOURCED_EVIDENCE=$(jq -r '.evidence[]? | select(.verbatim_quote == null or .verbatim_quote == "") | .evidence_id' "$LATEST_EXTRACTION" 2>/dev/null)

    # Check for unsourced implicit arguments
    UNSOURCED_IA=$(jq -r '.implicit_arguments[]? | select(.trigger_text == null or (.trigger_text | length) == 0) | .implicit_argument_id' "$LATEST_EXTRACTION" 2>/dev/null)

    if [ -z "$UNSOURCED_EVIDENCE" ] && [ -z "$UNSOURCED_IA" ]; then
      check_status "PASS" "All items properly sourced"
    else
      check_status "FAIL" "Unsourced items found"
      [ ! -z "$UNSOURCED_EVIDENCE" ] && echo "  Unsourced evidence: $UNSOURCED_EVIDENCE"
      [ ! -z "$UNSOURCED_IA" ] && echo "  Unsourced implicit arguments: $UNSOURCED_IA"
    fi
  else
    check_status "WARN" "No extraction files found to check"
  fi
  echo ""
fi

# Check 5: Liberal Extraction Emphasis
echo "CHECK 5: Liberal Extraction Emphasis"
COUNT_01=$(grep -c "INCLUDE IT\|when uncertain.*include" extraction-system/prompts/01-claims-evidence_pass1_prompt.md 2>/dev/null || echo 0)
COUNT_03=$(grep -c "INCLUDE IT\|when uncertain.*include" extraction-system/prompts/03-rdmap_pass1_prompt.md 2>/dev/null || echo 0)

echo "  Claims-Evidence (01): $COUNT_01 mentions"
echo "  RDMAP (03): $COUNT_03 mentions"

if [ $COUNT_01 -ge 3 ] && [ $COUNT_03 -ge 3 ]; then
  check_status "PASS" "Liberal extraction emphasized (≥3 mentions each)"
else
  check_status "WARN" "Liberal extraction may be under-emphasized"
fi
echo ""

# Check 6: Regression Watch
if [ "$MODE" = "full" ]; then
  echo "CHECK 6: Regression Watch - Known Issues"

  # File safety rules
  if grep -q "NEVER.*partial.*Read\|NEVER Partial Read Before Full Write" input/WORKFLOW.md 2>/dev/null; then
    check_status "PASS" "File safety rules present in WORKFLOW.md"
  else
    check_status "FAIL" "File safety rules missing from WORKFLOW.md"
  fi

  # RDMAP liberal reminders (should be at Steps 2 & 3)
  RDMAP_REMINDERS=$(sed -n '370,390p' extraction-system/prompts/03-rdmap_pass1_prompt.md 2>/dev/null | grep -c "INCLUDE IT" || echo 0)
  if [ $RDMAP_REMINDERS -eq 2 ]; then
    check_status "PASS" "RDMAP workflow reminders present (Steps 2 & 3)"
  else
    check_status "WARN" "RDMAP workflow reminders count: $RDMAP_REMINDERS (expected 2)"
  fi

  # Research design guide exists
  if [ -f "extraction-system/skill/research-assessor/references/research-design-extraction-guide.md" ]; then
    check_status "PASS" "Research design extraction guide present"
  else
    check_status "FAIL" "Research design extraction guide missing"
  fi

  echo ""
fi

# Summary
echo "=== QA CHECKS SUMMARY ==="
echo "✅ Passed: $CHECKS_PASSED"
echo "⚠️  Warnings: $CHECKS_WARN"
echo "⛔ Failed: $CHECKS_FAILED"
echo ""

if [ $CHECKS_FAILED -gt 0 ]; then
  echo "STATUS: ⛔ CRITICAL - Fix failed checks before deployment"
  exit 1
elif [ $CHECKS_WARN -gt 0 ]; then
  echo "STATUS: ⚠️  MINOR ISSUES - Review warnings"
  exit 0
else
  echo "STATUS: ✅ PASS - All checks passed"
  exit 0
fi
