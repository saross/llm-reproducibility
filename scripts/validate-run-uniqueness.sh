#!/bin/bash
# validate-run-uniqueness.sh
# Validates that all variability test runs have unique content (not copies)
#
# Usage: ./scripts/validate-run-uniqueness.sh <paper-directory>
# Example: ./scripts/validate-run-uniqueness.sh outputs/variability-test/penske-et-al-2023
#
# Exit codes:
#   0 - All runs have unique content
#   1 - Duplicate content detected

set -e

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

# Function to check uniqueness for an array field
check_field_uniqueness() {
    local field=$1
    local hashes=""

    for run in "$PAPER_DIR"/run-*/extraction.json; do
        run_name=$(basename "$(dirname "$run")")
        hash=$(jq -c ".$field // []" "$run" 2>/dev/null | md5sum | cut -d' ' -f1)
        hashes="$hashes$hash\n"
        echo "  $run_name: $hash"
    done

    unique_count=$(echo -e "$hashes" | sort | uniq | grep -c . || true)
    total_count=$(echo -e "$hashes" | grep -c . || true)

    if [ "$unique_count" -eq "$total_count" ]; then
        echo "  ✅ All $total_count runs have unique $field content"
        return 0
    else
        echo "  ⚠️ Only $unique_count/$total_count runs have unique $field content"
        echo "  Duplicate hashes:"
        echo -e "$hashes" | sort | uniq -d | while read -r dup; do
            echo "    $dup"
        done
        return 1
    fi
}

# Track overall result
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
