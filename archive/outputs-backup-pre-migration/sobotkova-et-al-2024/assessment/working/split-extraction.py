#!/usr/bin/env python3
"""Split extraction.json into component files for assessment."""
import json

# Read extraction
with open('outputs/sobotkova-et-al-2024/extraction.json') as f:
    extraction = json.load(f)

# Split into components
components = {
    'evidence': extraction.get('evidence', []),
    'claims': extraction.get('claims', []),
    'methods': extraction.get('methods', []),
    'protocols': extraction.get('protocols', []),
    'research_designs': extraction.get('research_designs', [])
}

# Write component files
for component_name, component_data in components.items():
    output_path = f'outputs/sobotkova-et-al-2024/assessment/working/{component_name}.json'
    with open(output_path, 'w') as f:
        json.dump(component_data, f, indent=2)
    print(f"Wrote {len(component_data)} {component_name} to {output_path}")

# Summary
print(f"\nTotal items: {sum(len(c) for c in components.values())}")
for name, data in components.items():
    print(f"  {name}: {len(data)}")
