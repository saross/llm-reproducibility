#!/usr/bin/env python3
"""
Batch Metrics Calculator

Runs quantitative credibility metrics on all papers in the outputs/ directory
and generates corpus-wide statistics and reports.

Usage:
    python3 batch_metrics.py [--output-dir DIR]

Outputs:
    - outputs/credibility-metrics-dashboard.json: Full metrics for all papers
    - outputs/credibility-metrics-summary.md: Human-readable summary report

Author: Claude Sonnet 4.5
Date: 2025-11-14
Version: 1.0
"""

import json
import sys
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime
import statistics

# Import analysis toolkit
from analysis_toolkit import (
    load_extraction,
    calculate_all_metrics,
    get_paper_metadata,
    summarise_extraction
)


def find_extraction_files(base_dir: str = "outputs") -> List[Path]:
    """
    Find all extraction.json files in the outputs directory.

    Args:
        base_dir: Base directory to search (default: outputs)

    Returns:
        List of Path objects pointing to extraction.json files
    """
    base_path = Path(base_dir)

    if not base_path.exists():
        print(f"Error: Directory '{base_dir}' does not exist")
        return []

    # Find all extraction.json files
    extraction_files = list(base_path.glob("*/extraction.json"))

    return sorted(extraction_files)


def calculate_corpus_statistics(all_metrics: Dict[str, Dict]) -> Dict[str, Any]:
    """
    Calculate corpus-wide statistics for each metric.

    Args:
        all_metrics: Dictionary mapping paper_id to metrics

    Returns:
        Dictionary with corpus statistics
    """
    stats = {}

    # Get all metric keys from first paper
    if not all_metrics:
        return stats

    first_paper = next(iter(all_metrics.values()))
    metric_keys = first_paper.keys()

    for metric_key in metric_keys:
        # Collect scores for this metric across all papers
        scores = []
        for paper_metrics in all_metrics.values():
            metric_data = paper_metrics.get(metric_key, {})
            score = metric_data.get('score')
            if score is not None and score != float('inf'):
                scores.append(score)

        if not scores:
            continue

        # Calculate statistics
        stats[metric_key] = {
            'mean': round(statistics.mean(scores), 2),
            'median': round(statistics.median(scores), 2),
            'stdev': round(statistics.stdev(scores), 2) if len(scores) > 1 else 0,
            'min': round(min(scores), 2),
            'max': round(max(scores), 2),
            'count': len(scores)
        }

    return stats


def generate_dashboard(papers_data: List[Dict[str, Any]],
                       corpus_stats: Dict[str, Any]) -> Dict[str, Any]:
    """
    Generate JSON dashboard with all metrics and statistics.

    Args:
        papers_data: List of paper data with metadata and metrics
        corpus_stats: Corpus-wide statistics

    Returns:
        Complete dashboard dictionary
    """
    return {
        'generated_at': datetime.now().isoformat(),
        'corpus_size': len(papers_data),
        'corpus_statistics': corpus_stats,
        'papers': papers_data
    }


def generate_summary_report(papers_data: List[Dict[str, Any]],
                           corpus_stats: Dict[str, Any]) -> str:
    """
    Generate markdown summary report.

    Args:
        papers_data: List of paper data
        corpus_stats: Corpus statistics

    Returns:
        Markdown-formatted summary string
    """
    lines = []

    lines.append("# Credibility Metrics Summary Report")
    lines.append("")
    lines.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append(f"**Corpus Size:** {len(papers_data)} papers")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Corpus statistics
    lines.append("## Corpus Statistics")
    lines.append("")
    lines.append("| Metric | Mean | Median | StDev | Min | Max |")
    lines.append("|--------|------|--------|-------|-----|-----|")

    metric_names = {
        'esd': 'ESD (Evidential Support Density)',
        'tci': 'TCI (Transparency Completeness)',
        'scs': 'SCS (Scope Constraints)',
        'rti': 'RTI (Robustness Triangulation)',
        'ris': 'RIS (Replicability Infrastructure)',
        'pgcs': 'PGCS (PID Connectivity)',
        'fcs': 'FCS (FAIR Compliance)',
        'mdd': 'MDD (Methods Documentation)'
    }

    for metric_key, metric_name in metric_names.items():
        if metric_key in corpus_stats:
            stats = corpus_stats[metric_key]
            lines.append(
                f"| {metric_name} | {stats['mean']} | {stats['median']} | "
                f"{stats['stdev']} | {stats['min']} | {stats['max']} |"
            )

    lines.append("")
    lines.append("---")
    lines.append("")

    # Individual papers
    lines.append("## Individual Paper Scores")
    lines.append("")

    for paper in papers_data:
        metadata = paper['metadata']
        metrics = paper['metrics']

        lines.append(f"### {metadata['title']}")
        lines.append("")
        lines.append(f"**Authors:** {', '.join(metadata['authors'][:3])}" +
                    (" et al." if len(metadata['authors']) > 3 else ""))
        lines.append(f"**Year:** {metadata['year']}")
        if metadata.get('doi'):
            lines.append(f"**DOI:** {metadata['doi']}")
        lines.append("")

        lines.append("| Metric | Score | Interpretation |")
        lines.append("|--------|-------|----------------|")

        for metric_key, metric_name in metric_names.items():
            if metric_key in metrics:
                metric_data = metrics[metric_key]
                score = metric_data.get('score', 'N/A')
                interp = metric_data.get('interpretation', '')
                lines.append(f"| {metric_name} | {score} | {interp} |")

        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("## Metric Definitions")
    lines.append("")
    lines.append("**ESD (Evidential Support Density):** Claims:Evidence ratio. Lower is better (more evidence per claim).")
    lines.append("")
    lines.append("**TCI (Transparency Completeness Index):** RDMAP coverage (0-1 scale). Higher is better.")
    lines.append("")
    lines.append("**SCS (Scope Constraint Score):** Count of limitation statements. Higher is better.")
    lines.append("")
    lines.append("**RTI (Robustness Triangulation Index):** Shannon diversity of evidence types (0-3 typical). Higher is better.")
    lines.append("")
    lines.append("**RIS (Replicability Infrastructure Score):** PIDs and sharing statements (0-10 scale). Higher is better.")
    lines.append("")
    lines.append("**PGCS (PID Graph Connectivity Score):** Connectivity between PIDs. Higher is better.")
    lines.append("")
    lines.append("**FCS (FAIR Compliance Score):** Aggregate FAIR assessment (0-15 scale). Higher is better.")
    lines.append("")
    lines.append("**MDD (Methods Documentation Density):** Mean characters per RDMAP item. Higher is better.")
    lines.append("")

    return "\n".join(lines)


def main():
    """Main execution function."""

    print("="*60)
    print("BATCH CREDIBILITY METRICS CALCULATOR")
    print("="*60)
    print()

    # Find all extraction files
    print("Searching for extraction files...")
    extraction_files = find_extraction_files()

    if not extraction_files:
        print("No extraction.json files found in outputs/ directory")
        sys.exit(1)

    print(f"Found {len(extraction_files)} extraction files")
    print()

    # Process each paper
    papers_data = []
    all_metrics = {}

    for filepath in extraction_files:
        paper_id = filepath.parent.name

        print(f"Processing: {paper_id}")

        try:
            # Load extraction
            extraction = load_extraction(str(filepath))

            # Get metadata
            metadata = get_paper_metadata(extraction)

            # Get summary
            summary = summarise_extraction(extraction)

            # Calculate metrics
            metrics = calculate_all_metrics(extraction)

            # Store data
            paper_data = {
                'paper_id': paper_id,
                'metadata': metadata,
                'summary': summary,
                'metrics': metrics
            }

            papers_data.append(paper_data)
            all_metrics[paper_id] = metrics

            # Print brief results
            print(f"  ✓ {metadata['title'][:60]}...")
            print(f"    ESD={metrics['esd']['score']}, TCI={metrics['tci']['score']}, "
                  f"FCS={metrics['fcs']['score']}/15")

        except Exception as e:
            import traceback
            print(f"  ✗ Error processing {paper_id}: {e}")
            print(f"     Traceback:")
            traceback.print_exc()
            continue

    print()
    print(f"Successfully processed {len(papers_data)} papers")
    print()

    # Calculate corpus statistics
    print("Calculating corpus statistics...")
    corpus_stats = calculate_corpus_statistics(all_metrics)

    # Generate dashboard
    print("Generating dashboard JSON...")
    dashboard = generate_dashboard(papers_data, corpus_stats)

    dashboard_path = Path("outputs/credibility-metrics-dashboard.json")
    with open(dashboard_path, 'w', encoding='utf-8') as f:
        json.dump(dashboard, f, indent=2, ensure_ascii=False)

    print(f"  ✓ Saved: {dashboard_path}")

    # Generate summary report
    print("Generating summary report...")
    summary_md = generate_summary_report(papers_data, corpus_stats)

    summary_path = Path("outputs/credibility-metrics-summary.md")
    with open(summary_path, 'w', encoding='utf-8') as f:
        f.write(summary_md)

    print(f"  ✓ Saved: {summary_path}")

    # Generate corpus profile
    print("Generating corpus profile...")
    from generate_corpus_profile import generate_corpus_profile

    profile_md = generate_corpus_profile(dashboard)

    # Save with timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d-%H%M")
    profile_path = Path(f"outputs/corpus-profile-{timestamp}.md")
    with open(profile_path, 'w', encoding='utf-8') as f:
        f.write(profile_md)

    print(f"  ✓ Saved: {profile_path}")

    print()
    print("="*60)
    print("CORPUS STATISTICS SUMMARY")
    print("="*60)
    print()

    metric_names = {
        'esd': 'ESD',
        'tci': 'TCI',
        'scs': 'SCS',
        'rti': 'RTI',
        'ris': 'RIS',
        'pgcs': 'PGCS',
        'fcs': 'FCS',
        'mdd': 'MDD'
    }

    for metric_key, metric_abbr in metric_names.items():
        if metric_key in corpus_stats:
            stats = corpus_stats[metric_key]
            print(f"{metric_abbr:6s}: Mean={stats['mean']:6.2f}  "
                  f"Median={stats['median']:6.2f}  "
                  f"Range=[{stats['min']:.2f}, {stats['max']:.2f}]")

    print()
    print("="*60)
    print("COMPLETE!")
    print("="*60)
    print()
    print("Generated files:")
    print(f"  - {dashboard_path}")
    print(f"  - {summary_path}")
    print(f"  - {profile_path}")


if __name__ == '__main__':
    main()
