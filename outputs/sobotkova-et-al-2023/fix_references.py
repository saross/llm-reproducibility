#!/usr/bin/env python3
"""
Fix broken cross-references from Pass 2 consolidation.
E020 was consolidated but claims still reference it.
"""

import json
from pathlib import Path

def load_extraction():
    path = Path("/home/shawn/Code/llm-reproducibility/outputs/sobotkova-et-al-2023/extraction.json")
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_extraction(data, filepath):
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def main():
    data = load_extraction()

    # Remove E020 references (E020 was consolidated in Pass 2)
    fixed_count = 0
    for claim in data['claims']:
        if 'E020' in claim.get('supported_by_evidence', []):
            claim['supported_by_evidence'].remove('E020')
            fixed_count += 1
            print(f"Fixed {claim['claim_id']}: removed E020 reference")

    print(f"\nTotal fixes: {fixed_count}")

    extraction_path = Path("/home/shawn/Code/llm-reproducibility/outputs/sobotkova-et-al-2023/extraction.json")
    save_extraction(data, extraction_path)
    print(f"Updated extraction.json")

if __name__ == "__main__":
    main()
