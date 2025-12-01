#!/usr/bin/env python3
"""
analyse-extraction-variability.py

Analyses variability across multiple extraction runs of the same paper.
Computes count statistics, concept overlap, and agreement metrics.

Usage:
    python scripts/analyse-extraction-variability.py <paper-directory>

Example:
    python scripts/analyse-extraction-variability.py outputs/variability-test/sobotkova-et-al-2024

Output:
    - Console summary
    - Optional JSON report (--json flag)

Author: Claude Code
Date: 2025-12-01
"""

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path
from statistics import mean, stdev
from typing import Any


# -----------------------------------------------------------------------------
# Configuration
# -----------------------------------------------------------------------------

# Arrays to analyse from extraction.json
# These correspond to the main extraction output arrays defined in schema v2.6
# RDMAP arrays (methods, protocols, research_designs) typically show low variability
# while evidence/claims/implicit_arguments show moderate variability
EXTRACTION_ARRAYS = [
    'evidence',
    'claims',
    'implicit_arguments',
    'methods',
    'protocols',
    'research_designs'
]

# Text fields to use for semantic comparison (in order of preference)
# Schema field names vary slightly across versions, so we try multiple names
# First matching field is used for text extraction
TEXT_FIELDS = {
    'evidence': ['evidence_text', 'text', 'content'],
    'claims': ['claim_text', 'text', 'content'],
    'implicit_arguments': ['argument_text', 'content', 'text'],
    'methods': ['method_text', 'text', 'content'],
    'protocols': ['protocol_text', 'text', 'content'],
    'research_designs': ['design_text', 'text', 'content']
}


# -----------------------------------------------------------------------------
# Data Loading
# -----------------------------------------------------------------------------

def load_extractions(paper_dir: Path) -> dict[str, dict]:
    """
    Load all extraction.json files from run directories.

    Returns:
        Dictionary mapping run_id to extraction data
    """
    extractions = {}

    for run_dir in sorted(paper_dir.glob('run-*')):
        extraction_file = run_dir / 'extraction.json'
        if extraction_file.exists():
            with open(extraction_file, 'r', encoding='utf-8') as f:
                extractions[run_dir.name] = json.load(f)

    return extractions


def get_text_content(item: dict, array_type: str) -> str:
    """Extract text content from an item, trying multiple field names."""
    for field in TEXT_FIELDS.get(array_type, ['text', 'content']):
        if field in item and item[field]:
            return str(item[field])
    return ''


# -----------------------------------------------------------------------------
# Count Statistics
# -----------------------------------------------------------------------------

def compute_count_statistics(extractions: dict[str, dict]) -> dict[str, dict]:
    """
    Compute count statistics for each array type across runs.

    Calculates mean, standard deviation, coefficient of variation (CV%), and range
    for the number of items extracted in each array type across all runs.

    CV% is the primary variability metric:
    - 0-5%: Very stable (typical for RDMAP elements)
    - 5-15%: Acceptable variability (typical for evidence/claims)
    - >15%: High variability (investigate cause)

    Args:
        extractions: Dictionary mapping run_id to extraction data

    Returns:
        Dictionary with statistics for each array type
    """
    stats = {}

    for array_type in EXTRACTION_ARRAYS:
        # Collect item counts from each run
        counts = []
        for run_id, data in extractions.items():
            array = data.get(array_type, [])
            counts.append(len(array))

        if counts:
            n = len(counts)
            avg = mean(counts)
            # Standard deviation requires at least 2 data points
            std = stdev(counts) if n > 1 else 0
            # Coefficient of variation: relative measure of dispersion
            # Expressed as percentage for easier interpretation
            cv = (std / avg * 100) if avg > 0 else 0

            stats[array_type] = {
                'counts': counts,
                'n_runs': n,
                'mean': round(avg, 2),
                'stdev': round(std, 2),
                'cv_percent': round(cv, 1),
                'min': min(counts),
                'max': max(counts),
                'range': max(counts) - min(counts)
            }

    return stats


# -----------------------------------------------------------------------------
# Text Similarity (Lightweight)
# -----------------------------------------------------------------------------

def tokenise(text: str) -> set[str]:
    """Simple tokenisation: lowercase, alphanumeric tokens."""
    return set(re.findall(r'\b[a-z0-9]+\b', text.lower()))


def jaccard_similarity(set_a: set, set_b: set) -> float:
    """
    Compute Jaccard similarity coefficient between two sets.

    Jaccard index = |A ∩ B| / |A ∪ B|
    Range: 0.0 (no overlap) to 1.0 (identical sets)

    This is a simple but effective measure for comparing token sets.
    For more sophisticated semantic comparison, consider sentence embeddings.
    """
    # Edge case: both empty sets are considered identical
    if not set_a and not set_b:
        return 1.0
    # Edge case: one empty, one non-empty = no similarity
    if not set_a or not set_b:
        return 0.0
    intersection = len(set_a & set_b)
    union = len(set_a | set_b)
    return intersection / union if union > 0 else 0.0


def find_best_match(item_tokens: set, candidate_items: list[tuple[str, set]],
                    threshold: float = 0.5) -> tuple[str | None, float]:
    """
    Find best matching item from candidates based on token Jaccard.

    Returns:
        (best_match_id, similarity_score) or (None, 0) if no match above threshold
    """
    best_id = None
    best_score = 0.0

    for item_id, tokens in candidate_items:
        score = jaccard_similarity(item_tokens, tokens)
        if score > best_score:
            best_score = score
            best_id = item_id

    if best_score >= threshold:
        return best_id, best_score
    return None, 0.0


# -----------------------------------------------------------------------------
# Concept Overlap Analysis
# -----------------------------------------------------------------------------

def analyse_concept_overlap(extractions: dict[str, dict],
                            array_type: str,
                            similarity_threshold: float = 0.5) -> dict[str, Any]:
    """
    Analyse concept overlap across runs using token-based similarity.

    Approach:
    1. Use first run as reference
    2. For each item in reference, find best match in other runs
    3. Track which concepts appear in all runs vs. some runs

    Returns:
        Dictionary with overlap statistics
    """
    run_ids = list(extractions.keys())
    if len(run_ids) < 2:
        return {'error': 'Need at least 2 runs for comparison'}

    # Build tokenised representations for all items in all runs
    run_items = {}
    for run_id, data in extractions.items():
        items = data.get(array_type, [])
        run_items[run_id] = []
        for item in items:
            text = get_text_content(item, array_type)
            item_id = item.get(f'{array_type[:-1]}_id', item.get('id', ''))
            tokens = tokenise(text)
            if tokens:  # Only include items with extractable text
                run_items[run_id].append((item_id, tokens, text[:100]))

    # Use first run as reference, find matches in other runs
    reference_run = run_ids[0]
    reference_items = run_items[reference_run]

    concept_presence = []  # List of (concept_summary, [runs_present])

    for ref_id, ref_tokens, ref_text in reference_items:
        runs_with_match = [reference_run]

        for other_run in run_ids[1:]:
            other_items = [(item_id, tokens) for item_id, tokens, _ in run_items[other_run]]
            match_id, score = find_best_match(ref_tokens, other_items, similarity_threshold)
            if match_id:
                runs_with_match.append(other_run)

        concept_presence.append({
            'reference_id': ref_id,
            'text_preview': ref_text,
            'runs_present': len(runs_with_match),
            'in_all_runs': len(runs_with_match) == len(run_ids)
        })

    # Compute summary statistics
    n_concepts = len(concept_presence)
    n_in_all = sum(1 for c in concept_presence if c['in_all_runs'])

    # Also check for items in other runs not matched to reference
    unmatched_in_other_runs = 0
    for other_run in run_ids[1:]:
        other_items = run_items[other_run]
        ref_token_sets = [tokens for _, tokens, _ in reference_items]
        for item_id, tokens, _ in other_items:
            matched = False
            for ref_tokens in ref_token_sets:
                if jaccard_similarity(tokens, ref_tokens) >= similarity_threshold:
                    matched = True
                    break
            if not matched:
                unmatched_in_other_runs += 1

    return {
        'reference_run': reference_run,
        'n_reference_concepts': n_concepts,
        'n_in_all_runs': n_in_all,
        'core_agreement_percent': round(n_in_all / n_concepts * 100, 1) if n_concepts > 0 else 0,
        'unmatched_in_other_runs': unmatched_in_other_runs,
        'similarity_threshold': similarity_threshold,
        'concepts': concept_presence  # For detailed inspection
    }


# -----------------------------------------------------------------------------
# Pairwise Similarity Matrix
# -----------------------------------------------------------------------------

def compute_pairwise_similarity(extractions: dict[str, dict],
                                array_type: str) -> dict[str, Any]:
    """
    Compute pairwise Jaccard similarity between all run pairs.

    Uses pooled tokens from all items in each run.
    """
    run_ids = list(extractions.keys())

    # Pool all tokens per run
    run_token_pools = {}
    for run_id, data in extractions.items():
        items = data.get(array_type, [])
        all_tokens = set()
        for item in items:
            text = get_text_content(item, array_type)
            all_tokens |= tokenise(text)
        run_token_pools[run_id] = all_tokens

    # Compute pairwise similarities
    similarities = {}
    for i, run_a in enumerate(run_ids):
        for run_b in run_ids[i+1:]:
            sim = jaccard_similarity(run_token_pools[run_a], run_token_pools[run_b])
            similarities[f'{run_a}_vs_{run_b}'] = round(sim, 3)

    # Compute average
    if similarities:
        avg_sim = mean(similarities.values())
    else:
        avg_sim = 0

    return {
        'pairwise_similarities': similarities,
        'average_similarity': round(avg_sim, 3),
        'n_pairs': len(similarities)
    }


# -----------------------------------------------------------------------------
# Main Analysis
# -----------------------------------------------------------------------------

def analyse_paper(paper_dir: Path, similarity_threshold: float = 0.5) -> dict[str, Any]:
    """
    Run full variability analysis on a paper's extraction runs.
    """
    extractions = load_extractions(paper_dir)

    if not extractions:
        return {'error': f'No extraction files found in {paper_dir}'}

    results = {
        'paper_directory': str(paper_dir),
        'paper_id': paper_dir.name,
        'n_runs': len(extractions),
        'run_ids': list(extractions.keys()),
        'count_statistics': {},
        'concept_overlap': {},
        'pairwise_similarity': {}
    }

    # Compute statistics for each array type
    results['count_statistics'] = compute_count_statistics(extractions)

    # Compute concept overlap for main arrays
    for array_type in ['evidence', 'claims', 'implicit_arguments']:
        results['concept_overlap'][array_type] = analyse_concept_overlap(
            extractions, array_type, similarity_threshold
        )
        results['pairwise_similarity'][array_type] = compute_pairwise_similarity(
            extractions, array_type
        )

    return results


def format_report(results: dict[str, Any]) -> str:
    """Format results as human-readable report."""
    lines = []
    lines.append('=' * 70)
    lines.append(f"EXTRACTION VARIABILITY ANALYSIS: {results['paper_id']}")
    lines.append('=' * 70)
    lines.append(f"Runs analysed: {results['n_runs']} ({', '.join(results['run_ids'])})")
    lines.append('')

    # Count statistics
    lines.append('COUNT STATISTICS')
    lines.append('-' * 70)
    lines.append(f"{'Array':<20} {'Mean':>8} {'StdDev':>8} {'CV%':>8} {'Range':>10}")
    lines.append('-' * 70)

    for array_type, stats in results['count_statistics'].items():
        range_str = f"{stats['min']}-{stats['max']}"
        lines.append(
            f"{array_type:<20} {stats['mean']:>8.1f} {stats['stdev']:>8.2f} "
            f"{stats['cv_percent']:>7.1f}% {range_str:>10}"
        )
    lines.append('')

    # Concept overlap
    lines.append('CONCEPT OVERLAP (token-based Jaccard similarity)')
    lines.append('-' * 70)

    for array_type in ['evidence', 'claims', 'implicit_arguments']:
        overlap = results['concept_overlap'].get(array_type, {})
        if 'error' in overlap:
            continue

        lines.append(f"\n{array_type.upper()}:")
        lines.append(f"  Reference run: {overlap['reference_run']}")
        lines.append(f"  Concepts in reference: {overlap['n_reference_concepts']}")
        lines.append(f"  Concepts in ALL runs: {overlap['n_in_all_runs']}")
        lines.append(f"  Core agreement: {overlap['core_agreement_percent']}%")
        lines.append(f"  Unmatched in other runs: {overlap['unmatched_in_other_runs']}")

    lines.append('')

    # Pairwise similarity
    lines.append('PAIRWISE SIMILARITY (pooled token Jaccard)')
    lines.append('-' * 70)

    for array_type in ['evidence', 'claims', 'implicit_arguments']:
        pairwise = results['pairwise_similarity'].get(array_type, {})
        if not pairwise:
            continue

        lines.append(f"\n{array_type.upper()}: avg = {pairwise['average_similarity']:.3f}")
        for pair, sim in pairwise['pairwise_similarities'].items():
            lines.append(f"  {pair}: {sim:.3f}")

    lines.append('')
    lines.append('=' * 70)

    return '\n'.join(lines)


# -----------------------------------------------------------------------------
# CLI
# -----------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description='Analyse extraction variability across multiple runs'
    )
    parser.add_argument(
        'paper_dir',
        type=Path,
        help='Path to paper directory containing run-XX subdirectories'
    )
    parser.add_argument(
        '--json',
        action='store_true',
        help='Output results as JSON instead of formatted report'
    )
    parser.add_argument(
        '--threshold',
        type=float,
        default=0.5,
        help='Similarity threshold for concept matching (default: 0.5)'
    )
    parser.add_argument(
        '--output',
        type=Path,
        help='Write output to file instead of stdout'
    )

    args = parser.parse_args()

    if not args.paper_dir.exists():
        print(f"Error: Directory not found: {args.paper_dir}", file=sys.stderr)
        sys.exit(1)

    results = analyse_paper(args.paper_dir, args.threshold)

    if 'error' in results:
        print(f"Error: {results['error']}", file=sys.stderr)
        sys.exit(1)

    if args.json:
        # Remove detailed concepts list for cleaner JSON output
        for array_type in results['concept_overlap']:
            if 'concepts' in results['concept_overlap'][array_type]:
                del results['concept_overlap'][array_type]['concepts']
        output = json.dumps(results, indent=2)
    else:
        output = format_report(results)

    if args.output:
        args.output.write_text(output)
        print(f"Output written to {args.output}")
    else:
        print(output)


if __name__ == '__main__':
    main()
