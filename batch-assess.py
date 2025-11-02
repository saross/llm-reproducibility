#!/usr/bin/env python3
"""
Rapid batch assessment of all 10 extractions.
Focuses on structural patterns, schema compliance, and distribution metrics.
"""
import json
from pathlib import Path

papers = [
    'sobotkova-et-al-2023',
    'sobotkova-et-al-2024',
    'ross-2005',
    'eftimoski-et-al-2017',
    'ross-ballsun-stanton-2022',
    'sobotkova-et-al-2021',
    'sobotkova-et-al-2016',
    'penske-et-al-2023',
    'connor-et-al-2013',
    'ross-et-al-2009'
]

results = []

for paper_id in papers:
    extraction_path = f'outputs/{paper_id}/extraction.json'

    try:
        with open(extraction_path) as f:
            data = json.load(f)

        # Count items
        counts = {
            'evidence': len(data.get('evidence', [])),
            'claims': len(data.get('claims', [])),
            'methods': len(data.get('methods', [])),
            'protocols': len(data.get('protocols', [])),
            'research_designs': len(data.get('research_designs', []))
        }

        total = sum(counts.values())

        # Calculate ratios
        claims_to_evidence = counts['claims'] / counts['evidence'] if counts['evidence'] > 0 else 0
        rdmap_total = counts['methods'] + counts['protocols'] + counts['research_designs']

        # Check schema fields (sample from first items)
        schema_notes = []

        # Check if mappings exist
        mappings = {
            'claim_evidence': 0,
            'method_design': 0,
            'protocol_method': 0
        }

        # Count claim-evidence mappings (check multiple schema variants)
        # Variant 1: Mappings in claims (supported_by_evidence, supported_by, evidence_links)
        for c in data.get('claims', []):
            mappings['claim_evidence'] += len(
                c.get('supported_by_evidence',
                c.get('supported_by',
                c.get('evidence_links', [])))
            )

        # Variant 2: Mappings in evidence (supports_claims, linked_claims)
        for e in data.get('evidence', []):
            mappings['claim_evidence'] += len(
                e.get('supports_claims',
                e.get('linked_claims', []))
            )

        # Count method-design mappings (check schema variants)
        for m in data.get('methods', []):
            mappings['method_design'] += len(
                m.get('linked_designs',
                m.get('implements_designs', []))
            )

        # Count protocol-method mappings (check schema variants)
        for p in data.get('protocols', []):
            mappings['protocol_method'] += len(
                p.get('linked_methods',
                p.get('implements_methods', []))
            )

        total_mappings = sum(mappings.values())

        results.append({
            'paper_id': paper_id,
            'total_items': total,
            'counts': counts,
            'claims_to_evidence_ratio': round(claims_to_evidence, 2),
            'rdmap_items': rdmap_total,
            'total_mappings': total_mappings,
            'mappings': mappings
        })

    except FileNotFoundError:
        results.append({
            'paper_id': paper_id,
            'error': 'extraction.json not found'
        })
    except Exception as e:
        results.append({
            'paper_id': paper_id,
            'error': str(e)
        })

# Print results table
print("=" * 120)
print(f"{'Paper':<30} {'Total':<8} {'Ev':<6} {'Cl':<6} {'Me':<6} {'Pr':<6} {'RD':<6} {'C:E':<8} {'Maps':<8}")
print("=" * 120)

for r in results:
    if 'error' in r:
        print(f"{r['paper_id']:<30} ERROR: {r['error']}")
    else:
        print(f"{r['paper_id']:<30} "
              f"{r['total_items']:<8} "
              f"{r['counts']['evidence']:<6} "
              f"{r['counts']['claims']:<6} "
              f"{r['counts']['methods']:<6} "
              f"{r['counts']['protocols']:<6} "
              f"{r['counts']['research_designs']:<6} "
              f"{r['claims_to_evidence_ratio']:<8} "
              f"{r['total_mappings']:<8}")

print("=" * 120)

# Save detailed results
with open('outputs/batch-assessment-metrics.json', 'w') as f:
    json.dump(results, f, indent=2)

print("\nDetailed metrics saved to: outputs/batch-assessment-metrics.json")
