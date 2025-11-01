#!/usr/bin/env python3
"""
Sample Extraction for Assessment

Performs stratified random sampling of extraction.json items for quality assessment.

Usage:
    python sample_extraction.py <extraction.json> --depth quick|medium|deep --output sample.json [--seed 42]

Sample sizes:
    - quick:  20 items (proportional stratified)
    - medium: 52 items (15 claims, 20 evidence, 10 methods, 5 protocols, 2 designs)
    - deep:   ALL items (no sampling)

Output: JSON file with sampled items formatted for LLM assessment
"""

import json
import random
import argparse
import sys
from pathlib import Path
from collections import defaultdict


def load_extraction(filepath):
    """Load extraction.json and parse item counts by type."""
    with open(filepath, 'r') as f:
        data = json.load(f)

    items_by_type = {
        'claims': data.get('claims', []),
        'evidence': data.get('evidence', []),
        'methods': data.get('methods', []),
        'protocols': data.get('protocols', []),
        'research_designs': data.get('research_designs', [])
    }

    return data, items_by_type


def calculate_sample_sizes(items_by_type, depth):
    """Calculate sample sizes for each item type based on depth."""
    counts = {k: len(v) for k, v in items_by_type.items()}
    total = sum(counts.values())

    if depth == 'deep':
        # All items
        return counts

    elif depth == 'medium':
        # Fixed stratified sample: 52 items
        target_sizes = {
            'claims': min(15, counts['claims']),
            'evidence': min(20, counts['evidence']),
            'methods': min(10, counts['methods']),
            'protocols': min(5, counts['protocols']),
            'research_designs': min(2, counts['research_designs'])
        }
        return target_sizes

    elif depth == 'quick':
        # 20 items, proportionally stratified
        target_total = 20

        if total <= target_total:
            # If extraction has fewer than 20 items, use all
            return counts

        # Proportional allocation
        sample_sizes = {}
        allocated = 0

        for item_type, count in counts.items():
            if count == 0:
                sample_sizes[item_type] = 0
                continue

            # Proportional share
            proportion = count / total
            size = max(1, round(target_total * proportion))  # Minimum 1 if type exists
            sample_sizes[item_type] = min(size, count)
            allocated += sample_sizes[item_type]

        # Adjust if we over-allocated (due to rounding)
        if allocated > target_total:
            # Remove from largest category first
            for item_type in sorted(sample_sizes.keys(), key=lambda k: sample_sizes[k], reverse=True):
                if sample_sizes[item_type] > 1 and allocated > target_total:
                    reduction = min(sample_sizes[item_type] - 1, allocated - target_total)
                    sample_sizes[item_type] -= reduction
                    allocated -= reduction
                if allocated <= target_total:
                    break

        return sample_sizes

    else:
        raise ValueError(f"Invalid depth: {depth}. Must be quick, medium, or deep.")


def sample_items(items_by_type, sample_sizes, seed=None):
    """Perform stratified random sampling."""
    if seed is not None:
        random.seed(seed)

    sampled = {}

    for item_type, items in items_by_type.items():
        sample_size = sample_sizes[item_type]

        if sample_size >= len(items):
            # Use all items if sample size >= population
            sampled[item_type] = items.copy()
        elif sample_size > 0:
            # Random sample
            sampled[item_type] = random.sample(items, sample_size)
        else:
            sampled[item_type] = []

    return sampled


def collect_mappings(sampled_items, depth):
    """Collect mappings to verify from sampled items."""
    mappings = []
    sampled_ids = set()

    # Collect all sampled item IDs
    for item_type, items in sampled_items.items():
        for item in items:
            sampled_ids.add(item['id'])

    # Collect mappings where both endpoints are in sample
    for item_type, items in sampled_items.items():
        for item in items:
            # Claim → Evidence links
            if item_type == 'claims' and 'evidence_links' in item:
                for evidence_id in item.get('evidence_links', []):
                    if evidence_id in sampled_ids:
                        mappings.append({
                            'item_a': item['id'],
                            'item_b': evidence_id,
                            'mapping_type': 'claim_to_evidence'
                        })

            # Protocol → Method links
            if item_type == 'protocols' and 'method_id' in item:
                method_id = item.get('method_id')
                if method_id and method_id in sampled_ids:
                    mappings.append({
                        'item_a': item['id'],
                        'item_b': method_id,
                        'mapping_type': 'protocol_to_method'
                    })

            # Method → Research Design links
            if item_type == 'methods' and 'research_design_id' in item:
                rd_id = item.get('research_design_id')
                if rd_id and rd_id in sampled_ids:
                    mappings.append({
                        'item_a': item['id'],
                        'item_b': rd_id,
                        'mapping_type': 'method_to_design'
                    })

    # For quick/medium, sample mappings if there are too many
    if depth == 'quick' and len(mappings) > 10:
        mappings = random.sample(mappings, 10)
    elif depth == 'medium' and len(mappings) > 25:
        mappings = random.sample(mappings, 25)

    return mappings


def format_output(extraction_data, sampled_items, mappings, depth, sample_sizes):
    """Format sampled items and mappings for LLM assessment."""

    output = {
        'assessment_metadata': {
            'paper_slug': extraction_data.get('project_metadata', {}).get('paper_slug', 'unknown'),
            'assessment_depth': depth,
            'extraction_timestamp': extraction_data.get('extraction_timestamp', ''),
            'total_items_in_extraction': sum(len(extraction_data.get(k, [])) for k in ['claims', 'evidence', 'methods', 'protocols', 'research_designs']),
            'sample_sizes': sample_sizes,
            'total_sampled': sum(len(v) for v in sampled_items.values()),
            'mappings_to_verify': len(mappings)
        },

        'sampled_items': {},
        'mappings': mappings
    }

    # Format items by type for easy LLM processing
    for item_type, items in sampled_items.items():
        formatted_items = []

        for item in items:
            formatted_item = {
                'id': item['id'],
                'type': item_type.rstrip('s'),  # 'claims' → 'claim'
                'content': item.get('content', ''),
                'verbatim_quote': item.get('verbatim_quote', ''),
                'page_number': item.get('page_number', item.get('page', '')),
                'context': item.get('context', ''),
            }

            # Add type-specific fields
            if item_type == 'claims':
                formatted_item['claim_type'] = item.get('claim_type', '')
                formatted_item['evidence_links'] = item.get('evidence_links', [])
            elif item_type == 'evidence':
                formatted_item['evidence_type'] = item.get('evidence_type', '')
            elif item_type == 'methods':
                formatted_item['method_type'] = item.get('method_type', '')
                formatted_item['research_design_id'] = item.get('research_design_id', '')
            elif item_type == 'protocols':
                formatted_item['protocol_type'] = item.get('protocol_type', '')
                formatted_item['method_id'] = item.get('method_id', '')
            elif item_type == 'research_designs':
                formatted_item['design_type'] = item.get('design_type', '')

            formatted_items.append(formatted_item)

        output['sampled_items'][item_type] = formatted_items

    return output


def main():
    parser = argparse.ArgumentParser(
        description='Sample extraction items for quality assessment',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Sample sizes:
  quick:  20 items (proportional stratified)
  medium: 52 items (15 claims, 20 evidence, 10 methods, 5 protocols, 2 designs)
  deep:   ALL items (no sampling)

Examples:
  python sample_extraction.py outputs/paper/extraction.json --depth medium --output sample.json
  python sample_extraction.py outputs/paper/extraction.json --depth quick --output sample.json --seed 42
        """
    )

    parser.add_argument('extraction', type=Path, help='Path to extraction.json')
    parser.add_argument('--depth', required=True, choices=['quick', 'medium', 'deep'], help='Assessment depth')
    parser.add_argument('--output', type=Path, required=True, help='Output path for sample.json')
    parser.add_argument('--seed', type=int, help='Random seed for reproducibility (optional)')

    args = parser.parse_args()

    # Validate input file
    if not args.extraction.exists():
        print(f"Error: Extraction file not found: {args.extraction}", file=sys.stderr)
        sys.exit(1)

    # Load extraction
    print(f"Loading extraction from {args.extraction}...")
    extraction_data, items_by_type = load_extraction(args.extraction)

    # Print counts
    print(f"\nExtraction totals:")
    for item_type, items in items_by_type.items():
        print(f"  {item_type}: {len(items)}")
    print(f"  Total: {sum(len(items) for items in items_by_type.values())}")

    # Calculate sample sizes
    sample_sizes = calculate_sample_sizes(items_by_type, args.depth)
    print(f"\nSample sizes for '{args.depth}' assessment:")
    for item_type, size in sample_sizes.items():
        print(f"  {item_type}: {size}")
    print(f"  Total: {sum(sample_sizes.values())}")

    # Perform sampling
    if args.depth == 'deep':
        print("\nDeep assessment: Using all items (no sampling)")
        sampled_items = items_by_type
    else:
        print(f"\nPerforming stratified random sampling (seed: {args.seed})...")
        sampled_items = sample_items(items_by_type, sample_sizes, args.seed)

    # Collect mappings
    print("\nCollecting mappings to verify...")
    mappings = collect_mappings(sampled_items, args.depth)
    print(f"  Mappings to verify: {len(mappings)}")

    # Format output
    print("\nFormatting output...")
    output = format_output(extraction_data, sampled_items, mappings, args.depth, sample_sizes)

    # Write output
    print(f"Writing sample to {args.output}...")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with open(args.output, 'w') as f:
        json.dump(output, f, indent=2)

    print(f"\n✓ Sample created successfully!")
    print(f"  Items sampled: {output['assessment_metadata']['total_sampled']}")
    print(f"  Mappings to verify: {len(mappings)}")
    print(f"  Output: {args.output}")


if __name__ == '__main__':
    main()
