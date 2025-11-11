#!/usr/bin/env python3
"""
Quick infrastructure scan of extraction.json files to identify reproducibility markers.

Usage: python3 quick_infrastructure_scan.py <extraction.json>
"""

import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Any

def scan_for_patterns(data: Any, patterns: Dict[str, List[str]], context_size: int = 150) -> Dict[str, List[str]]:
    """
    Recursively scan JSON data for text patterns.
    Returns matches with surrounding context.
    """
    results = {key: [] for key in patterns.keys()}

    def recurse(obj, path=""):
        if isinstance(obj, dict):
            for key, value in obj.items():
                recurse(value, f"{path}.{key}" if path else key)
        elif isinstance(obj, list):
            for i, item in enumerate(obj):
                recurse(item, f"{path}[{i}]")
        elif isinstance(obj, str):
            # Check each pattern category
            for category, pattern_list in patterns.items():
                for pattern in pattern_list:
                    if re.search(pattern, obj, re.IGNORECASE):
                        # Extract context
                        match_pos = re.search(pattern, obj, re.IGNORECASE).start()
                        start = max(0, match_pos - context_size)
                        end = min(len(obj), match_pos + context_size)
                        context = obj[start:end]
                        results[category].append({
                            "path": path,
                            "context": context.strip(),
                            "full_text": obj
                        })
                        break  # Only match once per string

    recurse(data)
    return results

def main():
    # Define search patterns
    patterns = {
        "funding": [
            r"\b(fund(?:ed|ing)?|grant|support(?:ed)?|sponsor|acknowledge?ment)\b",
            r"\b(project\s+(?:number|id|code)|award\s+(?:number|no))\b",
            r"\b(erc|nsf|nih|arc|esrc|ahrc|leverhulme|wellcome)\b"
        ],
        "data_repository": [
            r"\b(zenodo|figshare|dryad|osf|github|gitlab|bitbucket)\b",
            r"\b(doi\s*:?\s*10\.\d+)",
            r"\b(data\s+(?:available|archived|deposited))\b",
            r"\b(repository|repos)\b",
            r"\b(open\s+context|tdar|ariadne)\b"
        ],
        "code_repository": [
            r"\b(github|gitlab|bitbucket)\.(?:com|org)",
            r"\b(code\s+(?:available|archived|deposited))\b",
            r"\b(software\s+(?:available|repository))\b",
            r"\b(jupyter|notebook|script|analysis\s+code)\b"
        ],
        "conflict_of_interest": [
            r"\b(conflict(?:s)?\s+of\s+interest)\b",
            r"\b(competing\s+interest(?:s)?)\b",
            r"\b(no\s+competing)\b",
            r"\b(declare(?:s)?.*interest)\b"
        ],
        "ethics": [
            r"\b(ethics?\s+(?:approval|committee|review|statement))\b",
            r"\b(institutional\s+review\s+board)\b",
            r"\b(irb\s+(?:approval|number))\b",
            r"\b(informed\s+consent)\b",
            r"\b(human\s+(?:subjects?|participants?))\b"
        ],
        "author_contributions": [
            r"\b(author(?:s)?\s+contribution(?:s)?)\b",
            r"\b(credit\s+statement)\b",
            r"\b(contribution(?:s)?\s+statement)\b",
            r"\b(?:conceived|designed|performed|analysed|wrote)\s+(?:the\s+)?(?:study|experiments|manuscript)\b"
        ],
        "preregistration": [
            r"\b(pre-?register(?:ed|ation)?)\b",
            r"\b(register(?:ed)?\s+(?:report|protocol))\b",
            r"\b(osf\.io/\w+)\b",
            r"\b(clinicaltrials\.gov)\b",
            r"\b(aspredicted\.org)\b"
        ],
        "open_science_badges": [
            r"\b(open\s+(?:data|materials|code))\b",
            r"\b(badge(?:s)?)\b",
            r"\b(preregister(?:ed)?\s+badge)\b"
        ],
        "power_analysis": [
            r"\b(power\s+analysis)\b",
            r"\b(sample\s+size\s+(?:calculation|determination|justification))\b",
            r"\b(statistical\s+power)\b",
            r"\b(effect\s+size.*detect)\b"
        ],
        "uncertainty": [
            r"\b(uncertain(?:ty)?|confidence\s+interval|standard\s+error|margin\s+of\s+error)\b",
            r"\b(±|plus-minus|\+/-)\b",
            r"\b(\d+%\s+(?:ci|confidence))\b"
        ]
    }

    # Read extraction file
    if len(sys.argv) < 2:
        print("Usage: python3 quick_infrastructure_scan.py <extraction.json>", file=sys.stderr)
        sys.exit(1)

    extraction_file = Path(sys.argv[1])
    if not extraction_file.exists():
        print(f"Error: File {extraction_file} not found", file=sys.stderr)
        sys.exit(1)

    with open(extraction_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Scan for patterns
    results = scan_for_patterns(data, patterns)

    # Print results
    paper_name = extraction_file.parent.name
    print(f"\n{'='*80}")
    print(f"REPRODUCIBILITY INFRASTRUCTURE SCAN: {paper_name}")
    print(f"{'='*80}\n")

    for category, matches in results.items():
        print(f"\n{category.upper().replace('_', ' ')} ({len(matches)} matches)")
        print("-" * 60)
        if matches:
            for i, match in enumerate(matches[:5], 1):  # Show max 5 per category
                print(f"\n  [{i}] Path: {match['path']}")
                print(f"      Context: ...{match['context']}...")
            if len(matches) > 5:
                print(f"\n  ... and {len(matches) - 5} more matches")
        else:
            print("  (none found)")

    # Summary statistics
    print(f"\n\n{'='*80}")
    print("SUMMARY")
    print(f"{'='*80}")
    total_matches = sum(len(matches) for matches in results.values())
    print(f"Total matches across all categories: {total_matches}")
    print(f"\nCategories with matches:")
    for category, matches in results.items():
        if matches:
            print(f"  - {category.replace('_', ' ').title()}: {len(matches)}")

if __name__ == "__main__":
    main()
