#!/bin/bash
# -----------------------------------------------------------------------------
# validate-run-uniqueness.sh
# -----------------------------------------------------------------------------
# Validates that all variability test runs have unique content (not copies).
#
# This script addresses a specific failure mode observed during variability
# testing: runs being accidentally created as copies of previous runs rather
# than independent extractions. This can happen due to context contamination
# when multiple runs are performed in the same session.
#
# The script computes MD5 hashes of the serialised JSON arrays (evidence,
# claims, implicit_arguments) and verifies that all hashes are unique across
# runs. Identical hashes indicate duplicate content.
#
# Usage:
#   ./scripts/validate-run-uniqueness.sh <paper-directory>
#
# Example:
#   ./scripts/validate-run-uniqueness.sh outputs/variability-test/penske-et-al-2023
#
# Exit codes:
#   0 - All runs have unique content
#   1 - Duplicate content detected (investigate and re-extract)
#
# Dependencies: bash, jq, md5sum
#
# Author: Claude Code
# Date: 2025-12-01
# -----------------------------------------------------------------------------

set -e  # Exit on error

PAPER_DIR="${1:-.}"

# Verify directory exists
if [ ! -d "$PAPER_DIR" ]; then
    echo "❌ Error: Directory not found: $PAPER_DIR"
    exit 1
fi

# Check for extraction.json files
RUN_COUNT=$(find "$PAPER_DIR" -maxdepth 2 -name "extraction.json" -path "*/run-*/extraction.json" | wc -l)
if [ "$RUN_COUNT" -eq 0 ]; then
    echo "❌ Error: No extraction.json files found in $PAPER_DIR/run-*/"
    exit 1
fi

echo "Checking content uniqueness for: $PAPER_DIR"
echo "Found $RUN_COUNT extraction files"
echo ""

# -----------------------------------------------------------------------------
# check_field_uniqueness - Validate uniqueness for a specific JSON array field
# -----------------------------------------------------------------------------
# Args:
#   $1 - Field name (e.g., "evidence", "claims", "implicit_arguments")
#
# Returns:
#   0 if all runs have unique content for this field
#   1 if duplicates detected
#
# Method:
#   1. For each extraction.json, serialise the specified array with jq -c
#   2. Compute MD5 hash of serialised JSON
#   3. Compare hashes across all runs
#   4. Report duplicates if found
# -----------------------------------------------------------------------------
check_field_uniqueness() {
    local field=$1
    local hashes=""

    # Iterate through all extraction.json files in run directories
    for run in "$PAPER_DIR"/run-*/extraction.json; do
        run_name=$(basename "$(dirname "$run")")
        # Serialise array to compact JSON and compute MD5 hash
        # The "// []" provides empty array fallback if field missing
        hash=$(jq -c ".$field // []" "$run" 2>/dev/null | md5sum | cut -d' ' -f1)
        hashes="$hashes$hash\n"
        echo "  $run_name: $hash"
    done

    # Count unique vs total hashes to detect duplicates
    unique_count=$(echo -e "$hashes" | sort | uniq | grep -c . || true)
    total_count=$(echo -e "$hashes" | grep -c . || true)

    if [ "$unique_count" -eq "$total_count" ]; then
        echo "  ✅ All $total_count runs have unique $field content"
        return 0
    else
        echo "  ⚠️ Only $unique_count/$total_count runs have unique $field content"
        # Show which hashes are duplicated (appear more than once)
        echo "  Duplicate hashes:"
        echo -e "$hashes" | sort | uniq -d | while read -r dup; do
            echo "    $dup"
        done
        return 1
    fi
}

# -----------------------------------------------------------------------------
# Main validation logic
# -----------------------------------------------------------------------------
# Check the three key arrays that should show variability across runs.
# RDMAP arrays (methods, protocols, research_designs) are expected to be
# more stable, so we focus on evidence, claims, and implicit_arguments.
# -----------------------------------------------------------------------------

# Track overall result across all field checks
all_passed=true

echo "=== Evidence Array ==="
if ! check_field_uniqueness "evidence"; then
    all_passed=false
fi
echo ""

echo "=== Claims Array ==="
if ! check_field_uniqueness "claims"; then
    all_passed=false
fi
echo ""

echo "=== Implicit Arguments Array ==="
if ! check_field_uniqueness "implicit_arguments"; then
    all_passed=false
fi
echo ""

# Summary
echo "=== Summary ==="
if $all_passed; then
    echo "✅ All content arrays have unique values across all runs"
    exit 0
else
    echo "⚠️ Duplicate content detected - some runs may be copies"
    exit 1
fi
