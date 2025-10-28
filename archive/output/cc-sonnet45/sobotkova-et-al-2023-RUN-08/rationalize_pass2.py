#!/usr/bin/env python3
"""
Pass 2 Rationalization Script for sobotkova-et-al-2023 extraction.

This script safely loads the full extraction.json, performs Pass 2 rationalization
on claims/evidence/implicit_arguments arrays, and writes back the complete file.

Safety features:
- Loads entire JSON into memory before modifications
- Preserves all RDMAP arrays untouched
- Validates counts before and after
- Creates backup before writing
"""

import json
import shutil
from datetime import datetime
from pathlib import Path

def load_extraction(filepath):
    """Load the full extraction JSON."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_extraction(data, filepath):
    """Save the rationalized extraction JSON."""
    # Create backup first
    backup_path = filepath.parent / f"{filepath.stem}_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    shutil.copy2(filepath, backup_path)
    print(f"Backup created: {backup_path}")

    # Write updated file
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Updated file written: {filepath}")

def print_counts(data, label):
    """Print array counts for validation."""
    print(f"\n{label}:")
    print(f"  Evidence: {len(data.get('evidence', []))}")
    print(f"  Claims: {len(data.get('claims', []))}")
    print(f"  Implicit Arguments: {len(data.get('implicit_arguments', []))}")
    print(f"  Research Designs: {len(data.get('research_designs', []))}")
    print(f"  Methods: {len(data.get('methods', []))}")
    print(f"  Protocols: {len(data.get('protocols', []))}")

def main():
    # Load extraction
    extraction_path = Path("/home/shawn/Code/llm-reproducibility/outputs/sobotkova-et-al-2023/extraction.json")
    print("Loading extraction.json...")
    data = load_extraction(extraction_path)

    # Print before counts
    print_counts(data, "BEFORE Rationalization")

    items_before = len(data['evidence']) + len(data['claims']) + len(data['implicit_arguments'])

    # === RATIONALIZATION LOGIC WILL GO HERE ===
    # This script provides the safe framework
    # The actual rationalization will be done by Claude in the next step

    print("\n⚠️  Script framework ready. Rationalization logic to be implemented.")
    print("Current status: No modifications made (safe test run)")

    # Print after counts (should be same for now)
    print_counts(data, "AFTER Rationalization")

    # Calculate statistics
    items_after = len(data['evidence']) + len(data['claims']) + len(data['implicit_arguments'])
    reduction_pct = ((items_before - items_after) / items_before * 100) if items_before > 0 else 0

    print(f"\nReduction: {items_before} → {items_after} ({reduction_pct:.1f}%)")
    print(f"Target: 15-20% reduction")

if __name__ == "__main__":
    main()
