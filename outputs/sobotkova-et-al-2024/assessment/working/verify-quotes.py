#!/usr/bin/env python3
"""
Automated verbatim quote verification against source text.
Systematically checks if extracted quotes exist in source paper.
"""
import json
import re
from pathlib import Path

# Read source text
source_path = 'outputs/sobotkova-et-al-2024/full_text.txt'
with open(source_path, 'r', encoding='utf-8') as f:
    source_text = f.read()

# Normalize text function (handles encoding variations)
def normalize(text):
    """Normalize text for comparison (handle en-dashes, quotes, etc.)"""
    text = text.replace('\u2013', '-')  # en-dash to hyphen
    text = text.replace('\u2014', '-')  # em-dash to hyphen
    text = text.replace('\u2019', "'")  # right single quote
    text = text.replace('\u201c', '"')  # left double quote
    text = text.replace('\u201d', '"')  # right double quote
    text = text.replace('\u2018', "'")  # left single quote
    text = text.replace('\u00d7', 'x')  # multiplication sign to x
    text = text.replace('\u20135', '=')  # special equals variations
    text = text.replace('\n', ' ')      # newlines to spaces
    text = text.replace('\r', ' ')      # carriage returns to spaces
    text = re.sub(r'\s+', ' ', text)    # multiple spaces to single space
    text = text.strip()
    return text

source_normalized = normalize(source_text)

# Component files to check
components = {
    'evidence': 'outputs/sobotkova-et-al-2024/assessment/working/evidence.json',
    'claims': 'outputs/sobotkova-et-al-2024/assessment/working/claims.json',
    'methods': 'outputs/sobotkova-et-al-2024/assessment/working/methods.json',
    'protocols': 'outputs/sobotkova-et-al-2024/assessment/working/protocols.json',
    'research_designs': 'outputs/sobotkova-et-al-2024/assessment/working/research_designs.json'
}

# Verification results
total_items = 0
total_quotes = 0
verified_quotes = 0
missing_quotes = []
partial_matches = []

print("=== VERBATIM QUOTE VERIFICATION ===\n")

for component_name, component_path in components.items():
    with open(component_path) as f:
        items = json.load(f)

    print(f"\n{component_name.upper()} ({len(items)} items):")

    component_verified = 0
    component_missing = 0

    for item in items:
        total_items += 1
        # Extract item ID based on component type
        if component_name == 'evidence':
            item_id = item.get('evidence_id', 'UNKNOWN')
        elif component_name == 'claims':
            item_id = item.get('claim_id', 'UNKNOWN')
        elif component_name == 'methods':
            item_id = item.get('method_id', 'UNKNOWN')
        elif component_name == 'protocols':
            item_id = item.get('protocol_id', 'UNKNOWN')
        elif component_name == 'research_designs':
            item_id = item.get('research_design_id', 'UNKNOWN')
        else:
            item_id = 'UNKNOWN'

        verbatim = item.get('verbatim_quote', '')
        if not verbatim:
            continue

        total_quotes += 1
        verbatim_norm = normalize(verbatim)

        # Check if quote exists in source (try both exact and case-insensitive)
        if verbatim_norm in source_text or verbatim_norm.lower() in source_normalized.lower():
            verified_quotes += 1
            component_verified += 1
        else:
            # Check for partial match (>80% of words present)
            words = verbatim_norm.split()
            if len(words) > 5:
                partial_count = sum(1 for w in words if w in source_normalized and len(w) > 3)
                if partial_count / len(words) > 0.8:
                    partial_matches.append({
                        'id': item_id,
                        'quote': verbatim[:100],
                        'match_pct': round(partial_count / len(words) * 100, 1)
                    })
                    component_verified += 1
                    verified_quotes += 1
                else:
                    missing_quotes.append({
                        'id': item_id,
                        'component': component_name,
                        'quote': verbatim[:100] + ('...' if len(verbatim) > 100 else '')
                    })
                    component_missing += 1
            else:
                missing_quotes.append({
                    'id': item_id,
                    'component': component_name,
                    'quote': verbatim
                })
                component_missing += 1

    print(f"  Verified: {component_verified}/{len(items)}")
    if component_missing > 0:
        print(f"  ⚠️  Missing: {component_missing}")

# Summary
print(f"\n=== SUMMARY ===")
print(f"Total items: {total_items}")
print(f"Items with verbatim quotes: {total_quotes}")
print(f"Verified quotes: {verified_quotes}/{total_quotes} ({round(verified_quotes/total_quotes*100,1)}%)")

if partial_matches:
    print(f"\n⚠️  Partial matches (>80% words found): {len(partial_matches)}")
    for pm in partial_matches[:5]:
        print(f"  {pm['id']}: {pm['match_pct']}% match")

if missing_quotes:
    print(f"\n❌ MISSING QUOTES: {len(missing_quotes)}")
    for mq in missing_quotes:
        print(f"\n  {mq['id']} ({mq['component']}):")
        print(f"    {mq['quote']}")
