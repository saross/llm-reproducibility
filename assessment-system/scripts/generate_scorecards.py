#!/usr/bin/env python3
"""
Scorecard Generator

Generates individual credibility metrics scorecards for each paper in the corpus,
with corpus-relative percentile rankings and detailed interpretations.

Usage:
    python3 generate_scorecards.py

Inputs:
    - outputs/credibility-metrics-dashboard.json (from batch_metrics.py)

Outputs:
    - outputs/{paper-id}/metrics-scorecard.md for each paper

Author: Claude Sonnet 4.5
Date: 2025-11-14
Version: 1.0
"""

import json
import statistics
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime


def load_dashboard(path: str = "outputs/credibility-metrics-dashboard.json") -> Dict[str, Any]:
    """Load the metrics dashboard JSON."""
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def calculate_percentile(value: float, all_values: List[float], reverse: bool = False) -> int:
    """
    Calculate percentile rank of value within all_values.

    Args:
        value: The value to rank
        all_values: List of all values in corpus
        reverse: If True, lower values get higher percentiles (for ESD)

    Returns:
        Percentile (0-100)
    """
    if reverse:
        # For ESD: lower is better, so reverse the ranking
        rank = sum(1 for v in all_values if v > value)
    else:
        # For other metrics: higher is better
        rank = sum(1 for v in all_values if v < value)

    percentile = int((rank / len(all_values)) * 100)
    return percentile


def get_percentile_description(percentile: int) -> str:
    """Get text description of percentile position."""
    if percentile >= 75:
        return "Top 25%"
    elif percentile >= 50:
        return "Above median"
    elif percentile >= 25:
        return "Below median"
    else:
        return "Bottom 25%"


def get_rating_stars(percentile: int) -> str:
    """Get star rating based on percentile."""
    if percentile >= 75:
        return "⭐⭐⭐⭐"
    elif percentile >= 50:
        return "⭐⭐⭐"
    elif percentile >= 25:
        return "⭐⭐"
    else:
        return "⭐"


def get_visual_indicator(score: float, max_score: float, filled_char: str = "●", empty_char: str = "○", total_circles: int = 5) -> str:
    """
    Generate visual indicator (filled/empty circles) for score.

    Args:
        score: Current score
        max_score: Maximum possible score
        filled_char: Character for filled positions
        empty_char: Character for empty positions
        total_circles: Total number of circles to display

    Returns:
        Visual indicator string (e.g., "●●●○○")
    """
    if max_score == 0:
        return empty_char * total_circles

    proportion = score / max_score
    filled_count = round(proportion * total_circles)
    filled_count = max(0, min(total_circles, filled_count))  # Clamp to 0-total_circles

    return (filled_char * filled_count) + (empty_char * (total_circles - filled_count))


def generate_scorecard(paper_data: Dict[str, Any],
                       corpus_data: List[Dict[str, Any]],
                       corpus_stats: Dict[str, Any],
                       template_path: str = "assessment-system/templates/metrics-scorecard.md") -> str:
    """
    Generate scorecard for a single paper.

    Args:
        paper_data: Paper's data from dashboard
        corpus_data: All papers' data for percentile calculation
        corpus_stats: Corpus statistics
        template_path: Path to scorecard template

    Returns:
        Filled scorecard markdown
    """
    # Read template
    with open(template_path, 'r', encoding='utf-8') as f:
        template = f.read()

    # Extract data
    paper_id = paper_data['paper_id']
    metadata = paper_data['metadata']
    metrics = paper_data['metrics']
    summary = paper_data['summary']

    # Calculate percentiles for each metric
    all_metrics = {key: [] for key in metrics.keys()}
    for paper in corpus_data:
        for metric_key in metrics.keys():
            score = paper['metrics'][metric_key].get('score')
            if score is not None and score != float('inf'):
                all_metrics[metric_key].append(score)

    percentiles = {}
    for metric_key in metrics.keys():
        score = metrics[metric_key].get('score')
        if score is not None and score != float('inf'):
            # ESD: lower is better (reverse percentile)
            reverse = (metric_key == 'esd')
            percentiles[metric_key] = calculate_percentile(score, all_metrics[metric_key], reverse=reverse)
        else:
            percentiles[metric_key] = 0

    # Calculate corpus percentile summary
    avg_percentile = statistics.mean(percentiles.values())
    percentile_summary = f"{avg_percentile:.0f}th percentile overall"

    # Format authors
    authors_list = metadata.get('authors', [])
    if len(authors_list) > 3:
        authors_str = ', '.join(authors_list[:3]) + ' et al.'
    else:
        authors_str = ', '.join(authors_list)

    # Build replacement dictionary
    replacements = {
        'paper_id': paper_id,
        'assessment_date': datetime.now().strftime('%Y-%m-%d'),
        'corpus_size': str(len(corpus_data)),
        'title': metadata.get('title', 'Unknown'),
        'authors': authors_str,
        'publication_year': str(metadata.get('year', 'Unknown')),
        'doi': metadata.get('doi', 'Not available'),
        'percentile_summary': percentile_summary,
        'generation_timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    }

    # ESD
    esd = metrics['esd']
    replacements.update({
        'esd_score': f"{esd['score']:.2f}",
        'esd_percentile': f"{percentiles['esd']}%",
        'esd_percentile_description': get_percentile_description(percentiles['esd']),
        'esd_rating': get_rating_stars(percentiles['esd']),
        'esd_visual': get_visual_indicator(100 - percentiles['esd'], 100),  # Reverse for ESD
        'claims_count': str(esd.get('claims_count', 0)),
        'evidence_count': str(esd.get('evidence_count', 0)),
        'esd_ratio': f"{esd['score']:.2f}",
        'esd_corpus_mean': f"{corpus_stats['esd']['mean']:.2f}",
        'esd_corpus_median': f"{corpus_stats['esd']['median']:.2f}",
        'esd_corpus_min': f"{corpus_stats['esd']['min']:.2f}",
        'esd_corpus_max': f"{corpus_stats['esd']['max']:.2f}",
    })

    # ESD interpretation
    if esd['score'] == 0:
        esd_interp = "No explicit claims extracted. This may indicate a descriptive/methodological paper, or an extraction issue."
    elif esd['score'] < 0.5:
        esd_interp = "Strong evidential support: More than 2 evidence items per claim."
    elif esd['score'] < 1.0:
        esd_interp = "Good evidential support: More evidence than claims."
    elif esd['score'] == 1.0:
        esd_interp = "Balanced: Equal claims and evidence items."
    elif esd['score'] < 2.0:
        esd_interp = "Moderate support: Fewer evidence items than claims. May warrant review."
    else:
        esd_interp = "Limited support: Many claims per evidence item. Flag for review of claim support."
    replacements['esd_interpretation'] = esd_interp

    # TCI
    tci = metrics['tci']
    replacements.update({
        'tci_score': f"{tci['score']:.2f}",
        'tci_percentile': f"{percentiles['tci']}%",
        'tci_percentile_description': get_percentile_description(percentiles['tci']),
        'tci_rating': get_rating_stars(percentiles['tci']),
        'tci_visual': get_visual_indicator(tci['score'], 1.0),
        'rd_count': str(tci.get('rd_count', 0)),
        'rd_expected': str(tci.get('expected_rd', 2)),
        'methods_count': str(tci.get('methods_count', 0)),
        'methods_expected': str(tci.get('expected_methods', 5)),
        'protocols_count': str(tci.get('protocols_count', 0)),
        'protocols_expected': str(tci.get('expected_protocols', 8)),
        'rdmap_total': str(tci.get('actual_total', 0)),
        'rdmap_expected': str(tci.get('expected_total', 15)),
        'tci_corpus_mean': f"{corpus_stats['tci']['mean']:.2f}",
        'tci_corpus_median': f"{corpus_stats['tci']['median']:.2f}",
        'tci_corpus_min': f"{corpus_stats['tci']['min']:.2f}",
        'tci_corpus_max': f"{corpus_stats['tci']['max']:.2f}",
    })

    # TCI interpretation
    if tci['score'] >= 1.0:
        tci_interp = "Excellent: Meets or exceeds expected RDMAP coverage."
    elif tci['score'] >= 0.8:
        tci_interp = "Strong: Most expected RDMAP components documented."
    elif tci['score'] >= 0.5:
        tci_interp = "Moderate: Partial RDMAP coverage. Some methods detail may be missing."
    else:
        tci_interp = "Sparse: Significant RDMAP gaps. Review methods documentation."
    replacements['tci_interpretation'] = tci_interp

    # SCS
    scs = metrics['scs']
    replacements.update({
        'scs_score': str(scs['score']),
        'scs_percentile': f"{percentiles['scs']}%",
        'scs_percentile_description': get_percentile_description(percentiles['scs']),
        'scs_rating': get_rating_stars(percentiles['scs']),
        'scs_visual': get_visual_indicator(scs['score'], corpus_stats['scs']['max']),
        'limitations_count': str(scs['score']),
        'scs_corpus_mean': f"{corpus_stats['scs']['mean']:.1f}",
        'scs_corpus_median': f"{corpus_stats['scs']['median']:.1f}",
        'scs_corpus_min': str(corpus_stats['scs']['min']),
        'scs_corpus_max': str(corpus_stats['scs']['max']),
    })

    # SCS interpretation
    if scs['score'] == 0:
        scs_interp = "No explicit limitations extracted. Review paper for implicit limitations discussion or extraction issues."
    elif scs['score'] <= 3:
        scs_interp = "Few limitations acknowledged. Typical for this corpus (median = 0.5)."
    elif scs['score'] <= 8:
        scs_interp = "Moderate limitation discussion. Above corpus median."
    else:
        scs_interp = f"Extensive limitation discussion ({scs['score']} items). Review for quality vs quantity."
    replacements['scs_interpretation'] = scs_interp

    # RTI
    rti = metrics['rti']
    replacements.update({
        'rti_score': f"{rti['score']:.2f}",
        'rti_percentile': f"{percentiles['rti']}%",
        'rti_percentile_description': get_percentile_description(percentiles['rti']),
        'rti_rating': get_rating_stars(percentiles['rti']),
        'rti_visual': get_visual_indicator(rti['score'], 3.5),  # Shannon H typical max ~3.5
        'evidence_types_count': str(rti.get('type_count', 0)),
        'rti_corpus_mean': f"{corpus_stats['rti']['mean']:.2f}",
        'rti_corpus_median': f"{corpus_stats['rti']['median']:.2f}",
        'rti_corpus_min': f"{corpus_stats['rti']['min']:.2f}",
        'rti_corpus_max': f"{corpus_stats['rti']['max']:.2f}",
    })

    # Top evidence types
    type_counts = rti.get('type_counts', {})
    if type_counts:
        top_types = sorted(type_counts.items(), key=lambda x: x[1], reverse=True)[:3]
        top_types_str = ', '.join([f"{t[0]} (n={t[1]})" for t in top_types])
    else:
        top_types_str = "No evidence types extracted"
    replacements['top_evidence_types'] = top_types_str

    # RTI interpretation
    if rti['score'] < 0.5:
        rti_interp = "Low diversity: Mono-method or single evidence type dominates."
    elif rti['score'] < 1.5:
        rti_interp = "Moderate-low diversity: 1-2 dominant evidence types."
    elif rti['score'] < 2.5:
        rti_interp = "Moderate diversity: Multiple evidence types, some dominant."
    elif rti['score'] < 3.5:
        rti_interp = "High diversity: Many evidence types with balanced distribution."
    else:
        rti_interp = "Very high diversity: Extensive triangulation across many evidence types."
    replacements['rti_interpretation'] = rti_interp

    # RIS
    ris = metrics['ris']
    replacements.update({
        'ris_score': str(ris['score']),
        'ris_percentile': f"{percentiles['ris']}%",
        'ris_percentile_description': get_percentile_description(percentiles['ris']),
        'ris_rating': get_rating_stars(percentiles['ris']),
        'ris_visual': get_visual_indicator(ris['score'], 10),
        'ris_paper_doi': "✓" if ris['components']['paper_doi'] > 0 else "✗",
        'ris_author_orcids': "✓" if ris['components']['author_orcids'] > 0 else "✗",
        'ris_dataset_pids': "✓" if ris['components']['dataset_pids'] > 0 else "✗",
        'ris_software_pids': "✓" if ris['components']['software_pids'] > 0 else "✗",
        'ris_data_statement': "✓" if ris['components']['data_statement'] > 0 else "✗",
        'ris_code_statement': "✓" if ris['components']['code_statement'] > 0 else "✗",
        'ris_supplementary': "✓" if ris['components']['supplementary_materials'] > 0 else "✗",
        'ris_preregistration': "✓" if ris['components']['preregistration'] > 0 else "✗",
        'ris_corpus_mean': f"{corpus_stats['ris']['mean']:.1f}",
        'ris_corpus_median': f"{corpus_stats['ris']['median']:.1f}",
        'ris_corpus_min': str(corpus_stats['ris']['min']),
        'ris_corpus_max': str(corpus_stats['ris']['max']),
    })

    # RIS interpretation
    if ris['score'] == 0:
        ris_interp = "No replicability infrastructure. Consider archiving data/code and obtaining PIDs."
    elif ris['score'] <= 3:
        ris_interp = "Minimal infrastructure: Paper DOI and/or ORCIDs only. Data/code sharing absent."
    elif ris['score'] <= 6:
        ris_interp = "Moderate infrastructure: Some PIDs and sharing statements present."
    elif ris['score'] <= 9:
        ris_interp = "Strong infrastructure: Comprehensive PIDs and sharing practices."
    else:
        ris_interp = "Exemplary infrastructure: All replicability components present."
    replacements['ris_interpretation'] = ris_interp

    # PGCS
    pgcs = metrics['pgcs']
    replacements.update({
        'pgcs_score': str(pgcs['score']),
        'pgcs_percentile': f"{percentiles['pgcs']}%",
        'pgcs_percentile_description': get_percentile_description(percentiles['pgcs']),
        'pgcs_rating': get_rating_stars(percentiles['pgcs']),
        'pgcs_rating_label': pgcs.get('rating', 'unknown'),
        'pgcs_visual': get_visual_indicator(pgcs['score'], 10),
        'pgcs_total_pids': str(pgcs.get('total_pids', 0)),
        'pgcs_paper_doi': str(pgcs['pid_counts']['paper_doi']),
        'pgcs_author_orcids': str(pgcs['pid_counts']['author_orcids']),
        'pgcs_dataset_pids': str(pgcs['pid_counts']['dataset_pids']),
        'pgcs_software_pids': str(pgcs['pid_counts']['software_pids']),
        'pgcs_sample_pids': str(pgcs['pid_counts']['sample_pids']),
        'pgcs_project_pid': str(pgcs['pid_counts']['project_pid']),
        'pgcs_vocabulary_pids': str(pgcs['pid_counts']['vocabulary_pids']),
        'pgcs_rationale': pgcs.get('rationale', 'No rationale provided'),
        'pgcs_corpus_mean': f"{corpus_stats['pgcs']['mean']:.1f}",
        'pgcs_corpus_median': f"{corpus_stats['pgcs']['median']:.1f}",
        'pgcs_corpus_min': str(corpus_stats['pgcs']['min']),
        'pgcs_corpus_max': str(corpus_stats['pgcs']['max']),
    })

    # PGCS interpretation
    pgcs_rating = pgcs.get('rating', 'none')
    if pgcs_rating == 'exemplary':
        pgcs_interp = "Exemplary PID connectivity: Rich PID graph with comprehensive linkages."
    elif pgcs_rating == 'strong':
        pgcs_interp = "Strong PID connectivity: Well-connected PID infrastructure."
    elif pgcs_rating == 'moderate':
        pgcs_interp = "Moderate PID connectivity: Some PIDs connected."
    elif pgcs_rating == 'minimal':
        pgcs_interp = "Minimal PID connectivity: Few PIDs, limited connections."
    else:
        pgcs_interp = "No PID connectivity: Isolated or absent PIDs."
    replacements['pgcs_interpretation'] = pgcs_interp

    # FCS
    fcs = metrics['fcs']
    if fcs.get('assessed', True):
        replacements.update({
            'fcs_score': str(fcs['score']),
            'fcs_percentile': f"{percentiles['fcs']}%",
            'fcs_percentile_description': get_percentile_description(percentiles['fcs']),
            'fcs_rating': get_rating_stars(percentiles['fcs']),
            'fcs_visual': get_visual_indicator(fcs['score'], 15),
            'fcs_findable_score': str(fcs['breakdown']['findable']['score']),
            'fcs_findable_rationale': fcs['breakdown']['findable'].get('rationale', 'No rationale'),
            'fcs_accessible_score': str(fcs['breakdown']['accessible']['score']),
            'fcs_accessible_rationale': fcs['breakdown']['accessible'].get('rationale', 'No rationale'),
            'fcs_interoperable_score': str(fcs['breakdown']['interoperable']['score']),
            'fcs_interoperable_rationale': fcs['breakdown']['interoperable'].get('rationale', 'No rationale'),
            'fcs_reusable_score': str(fcs['breakdown']['reusable']['score']),
            'fcs_reusable_rationale': fcs['breakdown']['reusable'].get('rationale', 'No rationale'),
            'fcs_corpus_mean': f"{corpus_stats['fcs']['mean']:.1f}",
            'fcs_corpus_median': f"{corpus_stats['fcs']['median']:.1f}",
            'fcs_corpus_min': str(corpus_stats['fcs']['min']),
            'fcs_corpus_max': str(corpus_stats['fcs']['max']),
        })

        # FCS interpretation
        percentage = (fcs['score'] / 15) * 100
        if percentage >= 90:
            fcs_interp = "Exemplary FAIR compliance: Nearly perfect or perfect alignment."
        elif percentage >= 75:
            fcs_interp = "Strong FAIR compliance: Most FAIR principles satisfied."
        elif percentage >= 50:
            fcs_interp = "Moderate FAIR compliance: Some FAIR components present."
        else:
            fcs_interp = "Low FAIR compliance: Limited alignment with FAIR principles."
        replacements['fcs_interpretation'] = fcs_interp
    else:
        # FAIR not assessed
        replacements.update({
            'fcs_score': "N/A",
            'fcs_percentile': "N/A",
            'fcs_percentile_description': "Not assessed",
            'fcs_rating': "N/A",
            'fcs_visual': "○○○○○",
            'fcs_findable_score': "N/A",
            'fcs_findable_rationale': "FAIR assessment not conducted",
            'fcs_accessible_score': "N/A",
            'fcs_accessible_rationale': "FAIR assessment not conducted",
            'fcs_interoperable_score': "N/A",
            'fcs_interoperable_rationale': "FAIR assessment not conducted",
            'fcs_reusable_score': "N/A",
            'fcs_reusable_rationale': "FAIR assessment not conducted",
            'fcs_corpus_mean': f"{corpus_stats['fcs']['mean']:.1f}",
            'fcs_corpus_median': f"{corpus_stats['fcs']['median']:.1f}",
            'fcs_corpus_min': str(corpus_stats['fcs']['min']),
            'fcs_corpus_max': str(corpus_stats['fcs']['max']),
            'fcs_interpretation': "FAIR assessment not conducted for this paper.",
        })

    # MDD
    mdd = metrics['mdd']
    replacements.update({
        'mdd_score': f"{mdd['score']:.1f}",
        'mdd_percentile': f"{percentiles['mdd']}%",
        'mdd_percentile_description': get_percentile_description(percentiles['mdd']),
        'mdd_rating': get_rating_stars(percentiles['mdd']),
        'mdd_visual': get_visual_indicator(mdd['score'], 400),  # Assume ~400 as reasonable max
        'mdd_total_items': str(mdd.get('total_rdmap_items', 0)),
        'mdd_rd_count': str(mdd['breakdown']['research_designs']['count']),
        'mdd_rd_mean': f"{mdd['breakdown']['research_designs']['mean_length']:.1f}",
        'mdd_methods_count': str(mdd['breakdown']['methods']['count']),
        'mdd_methods_mean': f"{mdd['breakdown']['methods']['mean_length']:.1f}",
        'mdd_protocols_count': str(mdd['breakdown']['protocols']['count']),
        'mdd_protocols_mean': f"{mdd['breakdown']['protocols']['mean_length']:.1f}",
        'mdd_corpus_mean': f"{corpus_stats['mdd']['mean']:.1f}",
        'mdd_corpus_median': f"{corpus_stats['mdd']['median']:.1f}",
        'mdd_corpus_min': f"{corpus_stats['mdd']['min']:.1f}",
        'mdd_corpus_max': f"{corpus_stats['mdd']['max']:.1f}",
    })

    # MDD interpretation
    if mdd['score'] < 100:
        mdd_interp = "Sparse documentation: Terse RDMAP descriptions (< 100 chars/item)."
    elif mdd['score'] < 200:
        mdd_interp = "Moderate documentation: Paragraph-length RDMAP descriptions."
    elif mdd['score'] < 300:
        mdd_interp = "Detailed documentation: Multi-paragraph RDMAP descriptions."
    else:
        mdd_interp = "Extensive documentation: Very detailed RDMAP descriptions (> 300 chars/item)."
    replacements['mdd_interpretation'] = mdd_interp

    # Calculate corpus quartile distribution for appendix
    def percentile(values: List[float], p: float) -> float:
        """Calculate percentile without numpy."""
        if not values:
            return 0.0
        sorted_values = sorted(values)
        k = (len(sorted_values) - 1) * (p / 100)
        f = int(k)
        c = k - f
        if f + 1 < len(sorted_values):
            return sorted_values[f] + c * (sorted_values[f + 1] - sorted_values[f])
        else:
            return sorted_values[f]

    for metric_key in all_metrics.keys():
        values = all_metrics[metric_key]
        if values:
            replacements[f"{metric_key}_p25"] = f"{percentile(values, 25):.2f}"
            replacements[f"{metric_key}_p50"] = f"{percentile(values, 50):.2f}"
            replacements[f"{metric_key}_p75"] = f"{percentile(values, 75):.2f}"
        else:
            replacements[f"{metric_key}_p25"] = "N/A"
            replacements[f"{metric_key}_p50"] = "N/A"
            replacements[f"{metric_key}_p75"] = "N/A"

    # Summary assessment
    top_quartile = [k.upper() for k, v in percentiles.items() if v >= 75]
    bottom_quartile = [k.upper() for k, v in percentiles.items() if v < 25]

    replacements['top_quartile_metrics'] = ', '.join(top_quartile) if top_quartile else "None"
    replacements['bottom_quartile_metrics'] = ', '.join(bottom_quartile) if bottom_quartile else "None"

    # Overall ranking
    avg_percentile = statistics.mean(percentiles.values())
    if avg_percentile >= 75:
        rank_desc = "Top quartile overall"
    elif avg_percentile >= 50:
        rank_desc = "Above median overall"
    elif avg_percentile >= 25:
        rank_desc = "Below median overall"
    else:
        rank_desc = "Bottom quartile overall"
    replacements['overall_ranking'] = rank_desc

    # Strengths
    strengths = []
    if percentiles.get('fcs', 0) >= 75:
        strengths.append("- Exemplary FAIR compliance (top quartile)")
    if percentiles.get('tci', 0) >= 75:
        strengths.append("- Comprehensive RDMAP documentation (top quartile)")
    if percentiles.get('rti', 0) >= 75:
        strengths.append("- High evidence diversity/triangulation (top quartile)")
    if percentiles.get('ris', 0) >= 75:
        strengths.append("- Strong replicability infrastructure (top quartile)")
    if percentiles.get('mdd', 0) >= 75:
        strengths.append("- Detailed methodological documentation (top quartile)")
    if not strengths:
        strengths.append("- Metrics indicate areas for improvement across most dimensions")
    replacements['strengths_list'] = '\n'.join(strengths)

    # Improvements
    improvements = []
    if percentiles.get('esd', 0) < 25:
        improvements.append("- Consider increasing evidential support for claims (high claims:evidence ratio)")
    if percentiles.get('tci', 0) < 25:
        improvements.append("- Expand RDMAP documentation (sparse methods/protocols)")
    if percentiles.get('scs', 0) < 25 or scs['score'] == 0:
        improvements.append("- Explicitly acknowledge limitations and scope constraints")
    if percentiles.get('rti', 0) < 25:
        improvements.append("- Consider triangulation with additional evidence types")
    if percentiles.get('ris', 0) < 25:
        improvements.append("- Improve replicability infrastructure (PIDs, data/code sharing)")
    if percentiles.get('pgcs', 0) < 25:
        improvements.append("- Strengthen PID connectivity (link PIDs in infrastructure)")
    if percentiles.get('fcs', 0) < 25:
        improvements.append("- Enhance FAIR compliance (metadata, accessibility, licensing)")
    if percentiles.get('mdd', 0) < 25:
        improvements.append("- Provide more detailed methodological descriptions")
    if not improvements:
        improvements.append("- No major areas for improvement identified (strong performance overall)")
    replacements['improvements_list'] = '\n'.join(improvements)

    # Flags
    flags = []
    if esd['score'] == 0 or esd['score'] == float('inf'):
        flags.append("⚠️ ESD edge case (0 or inf): Review claims and evidence extraction")
    if scs['score'] == 0:
        flags.append("⚠️ No limitations extracted: Check for implicit limitations or extraction issue")
    if ris['score'] == 0:
        flags.append("⚠️ No replicability infrastructure: Critical concern for reproducibility")
    if tci['score'] < 0.5:
        flags.append("⚠️ Sparse RDMAP coverage: Insufficient methodological documentation")
    if not flags:
        flags.append("No critical flags")
    replacements['flags_and_notes'] = '\n'.join(flags)

    # Recommendations
    recommendations_authors = []
    if ris['score'] < 6:
        recommendations_authors.append("- Archive data and code in repositories with PIDs (e.g., Zenodo, OSF)")
    if fcs['score'] < 12:
        recommendations_authors.append("- Enhance FAIR compliance: add rich metadata, clear licences, standard formats")
    if scs['score'] < 3:
        recommendations_authors.append("- Explicitly discuss limitations, scope constraints, and assumptions")
    if not recommendations_authors:
        recommendations_authors.append("- Continue current practices; strong performance across metrics")
    replacements['recommendations_authors'] = '\n'.join(recommendations_authors)

    recommendations_reviewers = []
    if esd['score'] > 2.0:
        recommendations_reviewers.append("- Review whether claims are adequately supported by evidence")
    if rti['score'] < 1.0:
        recommendations_reviewers.append("- Consider whether mono-method approach is appropriate for research question")
    if scs['score'] == 0:
        recommendations_reviewers.append("- Request explicit limitations discussion")
    if not recommendations_reviewers:
        recommendations_reviewers.append("- Metrics suggest solid methodological foundation; focus on qualitative assessment")
    replacements['recommendations_reviewers'] = '\n'.join(recommendations_reviewers)

    recommendations_replication = []
    if ris['score'] < 4:
        recommendations_replication.append("- Contact authors for data/code (not publicly available)")
    if mdd['score'] < 150:
        recommendations_replication.append("- Expect to need additional methodological clarification from authors")
    if fcs['score'] < 10:
        recommendations_replication.append("- Data may not be accessible or in standard formats; prepare for preprocessing")
    if not recommendations_replication:
        recommendations_replication.append("- Good infrastructure and documentation; replication attempt should be feasible")
    replacements['recommendations_replication'] = '\n'.join(recommendations_replication)

    # Fill template
    scorecard = template
    for key, value in replacements.items():
        scorecard = scorecard.replace('{' + key + '}', str(value))

    return scorecard


def main():
    """Main execution function."""
    print("=" * 60)
    print("SCORECARD GENERATOR")
    print("=" * 60)
    print()

    # Load dashboard
    print("Loading dashboard...")
    dashboard = load_dashboard()

    corpus_data = dashboard['papers']
    corpus_stats = dashboard['corpus_statistics']

    print(f"Found {len(corpus_data)} papers in dashboard")
    print()

    # Generate scorecards
    print("Generating scorecards...")
    print()

    for paper_data in corpus_data:
        paper_id = paper_data['paper_id']
        title = paper_data['metadata']['title']

        print(f"Processing: {paper_id}")
        print(f"  Title: {title[:60]}...")

        try:
            # Generate scorecard
            scorecard = generate_scorecard(paper_data, corpus_data, corpus_stats)

            # Save to outputs/{paper-id}/metrics-scorecard.md
            output_dir = Path(f"outputs/{paper_id}")
            output_dir.mkdir(parents=True, exist_ok=True)

            output_path = output_dir / "metrics-scorecard.md"
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(scorecard)

            print(f"  ✓ Saved: {output_path}")

        except Exception as e:
            import traceback
            print(f"  ✗ Error: {e}")
            traceback.print_exc()
            continue

        print()

    print("=" * 60)
    print("COMPLETE!")
    print("=" * 60)
    print()
    print(f"Generated {len(corpus_data)} scorecards in outputs/{{paper-id}}/metrics-scorecard.md")
    print()


if __name__ == '__main__':
    main()
