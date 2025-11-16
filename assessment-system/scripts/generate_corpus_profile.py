#!/usr/bin/env python3
"""
Corpus Profile Generator

Generates a corpus-specific profile document with statistics, examples, and
observations for a given set of papers.

Usage:
    python3 generate_corpus_profile.py

Inputs:
    - outputs/credibility-metrics-dashboard.json (from batch_metrics.py)

Outputs:
    - outputs/corpus-profile-YYYY-MM-DD-HHMM.md

Author: Claude Sonnet 4.5
Date: 2025-11-14
Version: 1.0
"""

import json
import statistics
from pathlib import Path
from typing import Dict, List, Any
from datetime import datetime
from collections import Counter


def load_dashboard(path: str = "outputs/credibility-metrics-dashboard.json") -> Dict[str, Any]:
    """Load the metrics dashboard JSON."""
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def calculate_percentile(value: float, all_values: List[float]) -> float:
    """Calculate percentile of value within all_values."""
    if not all_values:
        return 0.0
    sorted_values = sorted(all_values)
    k = (len(sorted_values) - 1) * 0.25
    f = int(k)
    c = k - f
    if f + 1 < len(sorted_values):
        p25 = sorted_values[f] + c * (sorted_values[f + 1] - sorted_values[f])
    else:
        p25 = sorted_values[f]

    k = (len(sorted_values) - 1) * 0.50
    f = int(k)
    c = k - f
    if f + 1 < len(sorted_values):
        p50 = sorted_values[f] + c * (sorted_values[f + 1] - sorted_values[f])
    else:
        p50 = sorted_values[f]

    k = (len(sorted_values) - 1) * 0.75
    f = int(k)
    c = k - f
    if f + 1 < len(sorted_values):
        p75 = sorted_values[f] + c * (sorted_values[f + 1] - sorted_values[f])
    else:
        p75 = sorted_values[f]

    return p25, p50, p75


def find_example_papers(papers_data: List[Dict], metric_key: str, reverse: bool = False) -> Dict[str, str]:
    """
    Find example papers at low, moderate, and high levels for a metric.

    Args:
        papers_data: List of paper data
        metric_key: Metric to find examples for
        reverse: If True, lower is better (for ESD)

    Returns:
        Dict with 'low', 'moderate', 'high' paper examples
    """
    scores = []
    for paper in papers_data:
        score = paper['metrics'][metric_key].get('score')
        if score is not None and score != float('inf'):
            scores.append((score, paper))

    if not scores:
        return {'low': 'None', 'moderate': 'None', 'high': 'None'}

    scores.sort(key=lambda x: x[0], reverse=reverse)

    # Get examples
    low_paper = scores[0][1]
    mid_idx = len(scores) // 2
    moderate_paper = scores[mid_idx][1]
    high_paper = scores[-1][1]

    def format_paper(paper_tuple):
        score, paper = paper_tuple if isinstance(paper_tuple, tuple) else (None, paper_tuple)
        title = paper['metadata']['title']
        year = paper['metadata']['year']
        score_val = paper['metrics'][metric_key]['score']
        return f"{title[:50]}... ({year}, score={score_val})"

    return {
        'low': format_paper((scores[0][0], low_paper)),
        'moderate': format_paper((scores[mid_idx][0], moderate_paper)),
        'high': format_paper((scores[-1][0], high_paper))
    }


def generate_corpus_profile(dashboard: Dict[str, Any]) -> str:
    """
    Generate corpus profile markdown.

    Args:
        dashboard: Dashboard data from JSON

    Returns:
        Markdown-formatted corpus profile
    """
    papers_data = dashboard['papers']
    corpus_stats = dashboard['corpus_statistics']
    corpus_size = dashboard['corpus_size']
    generated_at = dashboard['generated_at']

    lines = []

    # Header
    lines.append("# Corpus Assessment Profile")
    lines.append("")
    lines.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append(f"**Corpus Size:** {corpus_size} papers")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Corpus Description
    lines.append("## Corpus Description")
    lines.append("")

    # Extract year range
    years = [p['metadata']['year'] for p in papers_data if p['metadata']['year'] != 'Unknown']
    if years:
        min_year = min([y for y in years if isinstance(y, int)])
        max_year = max([y for y in years if isinstance(y, int)])
        lines.append(f"**Publication years:** {min_year}-{max_year}")

    # List papers
    lines.append("")
    lines.append("**Papers in corpus:**")
    lines.append("")
    for i, paper in enumerate(papers_data, 1):
        title = paper['metadata']['title']
        authors = paper['metadata']['authors']
        year = paper['metadata']['year']
        first_author = authors[0] if authors else "Unknown"
        lines.append(f"{i}. {first_author} et al. ({year}): {title}")

    lines.append("")
    lines.append("---")
    lines.append("")

    # Corpus Statistics
    lines.append("## Corpus-Wide Metric Statistics")
    lines.append("")
    lines.append("| Metric | Mean | Median | StDev | Min | Max | Range |")
    lines.append("|--------|------|--------|-------|-----|-----|-------|")

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
            range_val = stats['max'] - stats['min']
            lines.append(
                f"| {metric_name} | {stats['mean']:.2f} | {stats['median']:.2f} | "
                f"{stats['stdev']:.2f} | {stats['min']:.2f} | {stats['max']:.2f} | {range_val:.2f} |"
            )

    lines.append("")
    lines.append("---")
    lines.append("")

    # Detailed Metric Analysis
    lines.append("## Detailed Metric Analysis")
    lines.append("")

    # ESD
    lines.append("### ESD: Evidential Support Density")
    lines.append("")
    lines.append(f"**Corpus mean:** {corpus_stats['esd']['mean']:.2f}")
    lines.append(f"**Corpus median:** {corpus_stats['esd']['median']:.2f}")
    lines.append(f"**Standard deviation:** {corpus_stats['esd']['stdev']:.2f}")
    lines.append(f"**Range:** {corpus_stats['esd']['min']:.2f} - {corpus_stats['esd']['max']:.2f}")
    lines.append("")

    # Distribution interpretation
    mean_median_diff = corpus_stats['esd']['mean'] - corpus_stats['esd']['median']
    if mean_median_diff > 0.5:
        lines.append("**Distribution:** Right-skewed (mean > median). Most papers have low ESD, with some high-ESD outliers.")
    elif mean_median_diff < -0.5:
        lines.append("**Distribution:** Left-skewed (mean < median). Most papers have high ESD, with some low-ESD outliers.")
    else:
        lines.append("**Distribution:** Roughly symmetric (mean ≈ median).")

    lines.append("")

    # Definition and corpus interpretation
    lines.append("**ESD measures:** Ratio of claims to evidence items (lower is better, more evidence per claim).")
    lines.append("")

    # Corpus-specific interpretation
    esd_mean = corpus_stats['esd']['mean']
    esd_range = corpus_stats['esd']['max'] - corpus_stats['esd']['min']
    if esd_mean < 1.0:
        interpretation = f"The mean of {esd_mean:.2f} indicates this corpus has more evidence than claims on average (good empirical support)."
    elif esd_mean < 2.0:
        interpretation = f"The mean of {esd_mean:.2f} indicates roughly balanced claims and evidence across the corpus."
    else:
        interpretation = f"The mean of {esd_mean:.2f} indicates more claims than evidence on average, suggesting some papers may need stronger empirical support."

    if esd_range > 3.0:
        interpretation += f" The wide range ({corpus_stats['esd']['min']:.2f}-{corpus_stats['esd']['max']:.2f}) shows substantial variation between papers, providing good discriminating power for this metric."
    else:
        interpretation += f" The narrow range ({corpus_stats['esd']['min']:.2f}-{corpus_stats['esd']['max']:.2f}) indicates papers are relatively similar in claims-to-evidence ratios."

    lines.append(f"**Corpus-specific interpretation:** {interpretation}")
    lines.append("")

    # Example papers
    examples = find_example_papers(papers_data, 'esd', reverse=True)  # Lower is better for ESD
    lines.append("**Example papers:**")
    lines.append("")
    lines.append(f"- **Low ESD (best):** {examples['high']}")  # Reversed because lower is better
    lines.append(f"- **Moderate ESD:** {examples['moderate']}")
    lines.append(f"- **High ESD (needs review):** {examples['low']}")
    lines.append("")
    lines.append("⚠️ **Note:** ESD counts items, not quality. A single strong evidence item may be more valuable than many weak ones. High ESD may reflect appropriate caution rather than weak research.")
    lines.append("")
    lines.append("---")
    lines.append("")

    # TCI
    lines.append("### TCI: Transparency Completeness Index")
    lines.append("")
    lines.append(f"**Corpus mean:** {corpus_stats['tci']['mean']:.2f}")
    lines.append(f"**Corpus median:** {corpus_stats['tci']['median']:.2f}")
    lines.append(f"**Standard deviation:** {corpus_stats['tci']['stdev']:.2f}")
    lines.append(f"**Range:** {corpus_stats['tci']['min']:.2f} - {corpus_stats['tci']['max']:.2f}")
    lines.append("")

    # Variance interpretation
    if corpus_stats['tci']['stdev'] < 0.05:
        lines.append("**Variance:** Very low variance. Corpus is homogeneous for RDMAP coverage.")
    elif corpus_stats['tci']['stdev'] < 0.15:
        lines.append("**Variance:** Low variance. Most papers have similar RDMAP coverage.")
    else:
        lines.append("**Variance:** Moderate to high variance. Papers vary in RDMAP completeness.")

    lines.append("")

    # Definition
    lines.append("**TCI measures:** Number of Research Design and Methods Assessment Protocol (RDMAP) items documented, relative to expected minimums (2 research designs, 5 methods, 8 protocols; 0-1 scale, higher is better).")
    lines.append("")

    # Corpus-specific interpretation
    tci_mean = corpus_stats['tci']['mean']
    tci_range = corpus_stats['tci']['max'] - corpus_stats['tci']['min']

    if tci_mean >= 0.95 and tci_range < 0.1:
        interpretation = f"The very high mean ({tci_mean:.2f}) and narrow range ({corpus_stats['tci']['min']:.2f}-{corpus_stats['tci']['max']:.2f}) indicate this corpus has uniformly strong methodological documentation, with all papers meeting or exceeding expected RDMAP thresholds. This limits TCI's ability to distinguish between papers in this corpus."
    elif tci_mean >= 0.8:
        interpretation = f"The high mean ({tci_mean:.2f}) indicates strong methodological documentation across most papers in this corpus."
    elif tci_mean >= 0.5:
        interpretation = f"The moderate mean ({tci_mean:.2f}) indicates mixed methodological documentation, with some papers providing comprehensive RDMAP coverage and others being more sparse."
    else:
        interpretation = f"The low mean ({tci_mean:.2f}) indicates generally sparse methodological documentation across this corpus, with most papers falling short of expected RDMAP thresholds."

    interpretation += " Note that TCI measures documentation *completeness* (how many RDMAP items), not *quality* (how detailed each item is)."

    lines.append(f"**Corpus-specific interpretation:** {interpretation}")
    lines.append("")

    examples = find_example_papers(papers_data, 'tci')
    lines.append("**Example papers:**")
    lines.append("")
    lines.append(f"- **Low TCI:** {examples['low']}")
    lines.append(f"- **Moderate TCI:** {examples['moderate']}")
    lines.append(f"- **High TCI:** {examples['high']}")
    lines.append("")
    lines.append("⚠️ **Note:** TCI measures documentation completeness (how many RDMAP items), not quality (how detailed each item is). Expected minimums are arbitrary bootstrapping thresholds, not validated standards.")
    lines.append("")
    lines.append("---")
    lines.append("")

    # SCS
    lines.append("### SCS: Scope Constraint Score")
    lines.append("")
    lines.append(f"**Corpus mean:** {corpus_stats['scs']['mean']:.2f}")
    lines.append(f"**Corpus median:** {corpus_stats['scs']['median']:.2f}")
    lines.append(f"**Standard deviation:** {corpus_stats['scs']['stdev']:.2f}")
    lines.append(f"**Range:** {int(corpus_stats['scs']['min'])} - {int(corpus_stats['scs']['max'])}")
    lines.append("")

    # Zero limitation papers
    zero_limitation_count = sum(1 for p in papers_data if p['metrics']['scs']['score'] == 0)
    zero_pct = (zero_limitation_count / corpus_size) * 100
    lines.append(f"**Papers with no limitations extracted:** {zero_limitation_count}/{corpus_size} ({zero_pct:.0f}%)")
    lines.append("")

    if corpus_stats['scs']['median'] < corpus_stats['scs']['mean'] / 2:
        lines.append("**Distribution:** Extremely right-skewed. Most papers have few/no limitations, some have many.")

    lines.append("")

    # Definition
    lines.append("**SCS measures:** Number of explicit limitation, qualification, or scope constraint statements in claims (count, higher indicates more transparent boundary acknowledgement).")
    lines.append("")

    # Corpus-specific interpretation
    scs_mean = corpus_stats['scs']['mean']
    scs_median = corpus_stats['scs']['median']

    if zero_limitation_count == 0:
        interpretation = f"All papers in this corpus acknowledge limitations (mean={scs_mean:.1f}, median={scs_median:.1f})."
    elif zero_pct < 20:
        interpretation = f"Most papers acknowledge limitations (mean={scs_mean:.1f}, median={scs_median:.1f}), with {zero_limitation_count}/{corpus_size} papers having none extracted."
    else:
        interpretation = f"Many papers lack explicit limitation statements ({zero_limitation_count}/{corpus_size}, {zero_pct:.0f}%)."

    if corpus_stats['scs']['stdev'] > scs_mean * 0.7:
        interpretation += f" The high variance (stdev={corpus_stats['scs']['stdev']:.1f}) indicates substantial differences in limitation discussion practices across papers."

    interpretation += " Remember: SCS counts limitation statements, not their quality or severity. A single serious unaddressed limitation may be more concerning than many trivial acknowledged limitations."

    lines.append(f"**Corpus-specific interpretation:** {interpretation}")
    lines.append("")

    examples = find_example_papers(papers_data, 'scs')
    lines.append("**Example papers:**")
    lines.append("")

    # Dynamic labels based on actual minimum
    min_scs = corpus_stats['scs']['min']
    if min_scs == 0:
        low_label = "No limitations"
    elif min_scs <= 2:
        low_label = "Few limitations"
    else:
        low_label = "Fewer limitations"

    lines.append(f"- **{low_label}:** {examples['low']}")
    lines.append(f"- **Moderate limitations:** {examples['moderate']}")
    lines.append(f"- **Many limitations:** {examples['high']}")
    lines.append("")
    lines.append("⚠️ **Note:** High SCS doesn't necessarily mean better research. Review limitation quality, not just quantity.")
    lines.append("")
    lines.append("---")
    lines.append("")

    # RTI
    lines.append("### RTI: Robustness Triangulation Index")
    lines.append("")
    lines.append(f"**Corpus mean:** {corpus_stats['rti']['mean']:.2f}")
    lines.append(f"**Corpus median:** {corpus_stats['rti']['median']:.2f}")
    lines.append(f"**Standard deviation:** {corpus_stats['rti']['stdev']:.2f}")
    lines.append(f"**Range:** {corpus_stats['rti']['min']:.2f} - {corpus_stats['rti']['max']:.2f}")
    lines.append("")

    # Shannon H interpretation
    mean_rti = corpus_stats['rti']['mean']
    if mean_rti < 1.0:
        lines.append("**Overall diversity:** Low (mean < 1.0). Corpus tends toward mono-method papers.")
    elif mean_rti < 2.0:
        lines.append("**Overall diversity:** Moderate-low (mean 1.0-2.0). Papers typically use 1-2 dominant evidence types.")
    elif mean_rti < 3.0:
        lines.append("**Overall diversity:** Moderate-high (mean 2.0-3.0). Papers show good methodological triangulation.")
    else:
        lines.append("**Overall diversity:** High (mean ≥ 3.0). Papers extensively triangulate across many evidence types.")

    lines.append("")

    # Definition
    lines.append("**RTI measures:** Diversity of evidence types using Shannon diversity index (0-3+ typical range, higher indicates more methodological triangulation).")
    lines.append("")

    # Corpus-specific interpretation
    interpretation = f"The mean of {mean_rti:.2f} suggests "
    if mean_rti < 1.0:
        interpretation += "this corpus primarily relies on single evidence types, with limited triangulation."
    elif mean_rti < 2.0:
        interpretation += "papers typically combine 2-3 evidence types, showing some triangulation."
    elif mean_rti < 3.0:
        interpretation += "strong methodological triangulation, with papers drawing on diverse evidence types to support claims."
    else:
        interpretation += "exceptional methodological diversity, with papers extensively triangulating across many evidence types."

    lines.append(f"**Corpus-specific interpretation:** {interpretation}")
    lines.append("")

    examples = find_example_papers(papers_data, 'rti')
    lines.append("**Example papers:**")
    lines.append("")
    lines.append(f"- **Low diversity:** {examples['low']}")
    lines.append(f"- **Moderate diversity:** {examples['moderate']}")
    lines.append(f"- **High diversity:** {examples['high']}")
    lines.append("")
    lines.append("⚠️ **Note:** RTI measures evidence type diversity, not appropriateness. Some research questions legitimately require focused mono-method approaches. High RTI doesn't automatically mean better research.")
    lines.append("")
    lines.append("---")
    lines.append("")

    # RIS
    lines.append("### RIS: Replicability Infrastructure Score")
    lines.append("")
    lines.append(f"**Corpus mean:** {corpus_stats['ris']['mean']:.2f} / 10")
    lines.append(f"**Corpus median:** {corpus_stats['ris']['median']:.2f} / 10")
    lines.append(f"**Standard deviation:** {corpus_stats['ris']['stdev']:.2f}")
    lines.append(f"**Range:** {int(corpus_stats['ris']['min'])} - {int(corpus_stats['ris']['max'])}")
    lines.append("")

    mean_pct = (corpus_stats['ris']['mean'] / 10) * 100
    if mean_pct < 30:
        lines.append(f"**Overall infrastructure:** Minimal (mean = {mean_pct:.0f}% of maximum). Corpus has poor replicability infrastructure.")
    elif mean_pct < 60:
        lines.append(f"**Overall infrastructure:** Moderate (mean = {mean_pct:.0f}% of maximum). Some infrastructure adoption.")
    else:
        lines.append(f"**Overall infrastructure:** Strong (mean = {mean_pct:.0f}% of maximum). Good infrastructure adoption.")

    lines.append("")

    # Definition
    lines.append("**RIS measures:** Availability of Persistent Identifiers (PIDs) and data/code/materials sharing infrastructure (0-10 scale: paper DOI, author ORCIDs, dataset PIDs, software PIDs, data/code availability statements, supplementary materials, preregistration).")
    lines.append("")

    # Corpus-specific interpretation
    interpretation = f"This corpus scores {mean_pct:.0f}% of maximum RIS, indicating "
    if mean_pct < 30:
        interpretation += "limited replicability infrastructure. Most papers lack PIDs for datasets/software and formal sharing statements."
    elif mean_pct < 60:
        interpretation += "moderate infrastructure adoption. Some papers provide PIDs and sharing statements, but practices are inconsistent."
    else:
        interpretation += "strong infrastructure adoption. Most papers provide comprehensive PIDs and sharing documentation."

    lines.append(f"**Corpus-specific interpretation:** {interpretation}")
    lines.append("")

    examples = find_example_papers(papers_data, 'ris')
    lines.append("**Example papers:**")
    lines.append("")
    lines.append(f"- **Minimal infrastructure:** {examples['low']}")
    lines.append(f"- **Moderate infrastructure:** {examples['moderate']}")
    lines.append(f"- **Strong infrastructure:** {examples['high']}")
    lines.append("")
    lines.append("⚠️ **Note:** RIS measures infrastructure availability, not actual use or quality. PIDs and repositories don't guarantee data/code are complete, well-documented, or usable. Low RIS for older papers may reflect pre-FAIR era publication norms.")
    lines.append("")
    lines.append("---")
    lines.append("")

    # PGCS
    lines.append("### PGCS: PID Graph Connectivity Score")
    lines.append("")
    lines.append(f"**Corpus mean:** {corpus_stats['pgcs']['mean']:.2f} / 10")
    lines.append(f"**Corpus median:** {corpus_stats['pgcs']['median']:.2f} / 10")
    lines.append(f"**Standard deviation:** {corpus_stats['pgcs']['stdev']:.2f}")
    lines.append(f"**Range:** {int(corpus_stats['pgcs']['min'])} - {int(corpus_stats['pgcs']['max'])}")
    lines.append("")

    mean_pct = (corpus_stats['pgcs']['mean'] / 10) * 100
    lines.append(f"**Overall connectivity:** {mean_pct:.0f}% of exemplary connectivity.")
    lines.append("")

    # Definition
    lines.append("**PGCS measures:** Number of Persistent Identifiers (PIDs) connected to the research (0-10 scale: paper DOI, author ORCIDs, dataset PIDs, software PIDs, sample PIDs, project PIDs, vocabulary PIDs; higher indicates stronger PID graph connectivity).")
    lines.append("")

    # Corpus-specific interpretation
    pgcs_mean = corpus_stats['pgcs']['mean']
    interpretation = f"This corpus averages {pgcs_mean:.1f} PIDs per paper ({mean_pct:.0f}% of exemplary connectivity), indicating "
    if mean_pct < 20:
        interpretation += "minimal PID adoption. Most papers have only paper DOIs, with limited author/data/software PIDs."
    elif mean_pct < 40:
        interpretation += "emerging PID adoption. Some papers include author ORCIDs or software repositories, but dataset/sample/project PIDs are rare."
    elif mean_pct < 60:
        interpretation += "moderate PID connectivity. Papers typically link to authors and code, with some dataset PIDs emerging."
    else:
        interpretation += "strong PID graph connectivity. Papers extensively use PIDs for authors, data, code, and research infrastructure."

    lines.append(f"**Corpus-specific interpretation:** {interpretation}")
    lines.append("")

    examples = find_example_papers(papers_data, 'pgcs')
    lines.append("**Example papers:**")
    lines.append("")
    lines.append(f"- **Minimal connectivity:** {examples['low']}")
    lines.append(f"- **Moderate connectivity:** {examples['moderate']}")
    lines.append(f"- **Strong connectivity:** {examples['high']}")
    lines.append("")
    lines.append("⚠️ **Note:** PGCS counts PIDs, not connectivity quality. PIDs must be properly linked and maintained to create functional knowledge graphs. Score depends heavily on publication year and disciplinary norms.")
    lines.append("")
    lines.append("---")
    lines.append("")

    # FCS
    lines.append("### FCS: FAIR Compliance Score")
    lines.append("")
    lines.append(f"**Corpus mean:** {corpus_stats['fcs']['mean']:.2f} / 15")
    lines.append(f"**Corpus median:** {corpus_stats['fcs']['median']:.2f} / 15")
    lines.append(f"**Standard deviation:** {corpus_stats['fcs']['stdev']:.2f}")
    lines.append(f"**Range:** {int(corpus_stats['fcs']['min'])} - {int(corpus_stats['fcs']['max'])}")
    lines.append("")

    mean_pct = (corpus_stats['fcs']['mean'] / 15) * 100
    if mean_pct < 50:
        lines.append(f"**Overall FAIR compliance:** Low (mean = {mean_pct:.0f}% of maximum).")
    elif mean_pct < 75:
        lines.append(f"**Overall FAIR compliance:** Moderate (mean = {mean_pct:.0f}% of maximum).")
    else:
        lines.append(f"**Overall FAIR compliance:** Strong (mean = {mean_pct:.0f}% of maximum).")

    lines.append("")

    # Definition
    lines.append("**FCS measures:** Compliance with FAIR (Findable, Accessible, Interoperable, Reusable) principles across four dimensions (0-15 scale: Findable 0-4, Accessible 0-4, Interoperable 0-3, Reusable 0-4; higher indicates stronger FAIR compliance).")
    lines.append("")

    # Corpus-specific interpretation
    fcs_mean = corpus_stats['fcs']['mean']
    fcs_range = corpus_stats['fcs']['max'] - corpus_stats['fcs']['min']
    interpretation = f"This corpus scores {mean_pct:.0f}% of maximum FAIR compliance (mean={fcs_mean:.1f}/15), indicating "
    if mean_pct < 50:
        interpretation += "limited adoption of FAIR principles. Many papers lack persistent identifiers, open access, or structured metadata."
    elif mean_pct < 75:
        interpretation += "moderate FAIR compliance. Papers typically satisfy basic findability and accessibility requirements, but may lack interoperability features or comprehensive metadata."
    else:
        interpretation += "strong FAIR compliance. Most papers are findable via PIDs, openly accessible, use standard formats, and provide rich reusable metadata."

    if fcs_range < 5:
        interpretation += f" The narrow range ({fcs_range:.0f} points) suggests consistent FAIR practices across the corpus."
    elif fcs_range >= 7:
        interpretation += f" The wide range ({fcs_range:.0f} points) indicates highly variable FAIR practices, likely reflecting temporal trends or different publication venues."

    lines.append(f"**Corpus-specific interpretation:** {interpretation}")
    lines.append("")

    examples = find_example_papers(papers_data, 'fcs')
    lines.append("**Example papers:**")
    lines.append("")
    lines.append(f"- **Low FAIR compliance:** {examples['low']}")
    lines.append(f"- **Moderate FAIR compliance:** {examples['moderate']}")
    lines.append(f"- **High FAIR compliance:** {examples['high']}")
    lines.append("")
    lines.append("⚠️ **Note:** FCS assesses surface-level FAIR indicators, not deep compliance. Metadata richness, licence clarity, and actual reusability require qualitative review. Temporal bias: older papers scored before FAIR principles were articulated.")
    lines.append("")
    lines.append("---")
    lines.append("")

    # MDD
    lines.append("### MDD: Methods Documentation Density")
    lines.append("")
    lines.append(f"**Corpus mean:** {corpus_stats['mdd']['mean']:.1f} chars/item")
    lines.append(f"**Corpus median:** {corpus_stats['mdd']['median']:.1f} chars/item")
    lines.append(f"**Standard deviation:** {corpus_stats['mdd']['stdev']:.1f}")
    lines.append(f"**Range:** {corpus_stats['mdd']['min']:.1f} - {corpus_stats['mdd']['max']:.1f}")
    lines.append("")

    mean_mdd = corpus_stats['mdd']['mean']
    if mean_mdd < 100:
        lines.append("**Overall documentation density:** Sparse (mean < 100 chars/item). Terse RDMAP descriptions typical.")
    elif mean_mdd < 200:
        lines.append("**Overall documentation density:** Moderate (mean 100-200 chars/item). Paragraph-length RDMAP descriptions typical.")
    elif mean_mdd < 300:
        lines.append("**Overall documentation density:** Detailed (mean 200-300 chars/item). Multi-paragraph RDMAP descriptions typical.")
    else:
        lines.append("**Overall documentation density:** Extensive (mean > 300 chars/item). Very detailed RDMAP descriptions typical.")

    lines.append("")

    # Definition
    lines.append("**MDD measures:** Mean character length of Research Design and Methods Assessment Protocol (RDMAP) item descriptions (continuous scale; higher indicates more detailed methodological documentation per item).")
    lines.append("")

    # Corpus-specific interpretation
    mdd_range = corpus_stats['mdd']['max'] - corpus_stats['mdd']['min']
    interpretation = f"The mean of {mean_mdd:.1f} chars/item suggests "
    if mean_mdd < 100:
        interpretation += "this corpus provides terse methodological descriptions, typically single sentences or brief phrases per RDMAP item."
    elif mean_mdd < 200:
        interpretation += "this corpus provides moderate methodological detail, typically paragraph-length descriptions per RDMAP item."
    elif mean_mdd < 300:
        interpretation += "this corpus provides detailed methodological documentation, typically multi-paragraph descriptions per RDMAP item."
    else:
        interpretation += "this corpus provides exceptionally detailed methodological documentation, with extensive descriptions for each RDMAP item."

    if mdd_range > 200:
        interpretation += f" The wide range ({corpus_stats['mdd']['min']:.0f}-{corpus_stats['mdd']['max']:.0f}) indicates substantial variation in documentation practices between papers."

    interpretation += " Note: MDD measures documentation *density* (how detailed), complementing TCI which measures *completeness* (how many items)."

    lines.append(f"**Corpus-specific interpretation:** {interpretation}")
    lines.append("")

    examples = find_example_papers(papers_data, 'mdd')
    lines.append("**Example papers:**")
    lines.append("")
    lines.append(f"- **Sparse documentation:** {examples['low']}")
    lines.append(f"- **Moderate documentation:** {examples['moderate']}")
    lines.append(f"- **Detailed documentation:** {examples['high']}")
    lines.append("")
    lines.append("⚠️ **Note:** MDD measures verbosity, not clarity or usefulness. Long descriptions may be verbose rather than informative; terse descriptions may be precise rather than incomplete. Complements TCI (completeness).")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Corpus Observations
    lines.append("## Corpus-Level Observations")
    lines.append("")

    lines.append("### Homogeneity vs Heterogeneity")
    lines.append("")

    # Calculate average coefficient of variation (CV = stdev/mean)
    cvs = []
    for metric_key in ['esd', 'tci', 'scs', 'rti', 'ris', 'pgcs', 'fcs', 'mdd']:
        if metric_key in corpus_stats:
            mean = corpus_stats[metric_key]['mean']
            stdev = corpus_stats[metric_key]['stdev']
            if mean > 0:
                cv = stdev / mean
                cvs.append(cv)

    avg_cv = statistics.mean(cvs) if cvs else 0

    if avg_cv < 0.3:
        lines.append("**Overall homogeneity:** High. Papers are similar across most metrics. May indicate corpus selection bias or limited genre/domain diversity.")
    elif avg_cv < 0.6:
        lines.append("**Overall homogeneity:** Moderate. Papers show some variation but cluster around typical values.")
    else:
        lines.append("**Overall homogeneity:** Low (heterogeneous corpus). Papers vary widely across metrics. Diverse corpus or wide quality range.")

    lines.append("")

    # Metrics with low variance
    low_variance_metrics = [k.upper() for k, v in corpus_stats.items() if v.get('stdev', 0) / max(v.get('mean', 1), 0.01) < 0.1]
    if low_variance_metrics:
        lines.append(f"**Low-variance metrics (CV < 0.1):** {', '.join(low_variance_metrics)}")
        lines.append("- These metrics show little variation across corpus. May not be discriminating in this sample.")

    lines.append("")

    # Metrics with high variance
    high_variance_metrics = [k.upper() for k, v in corpus_stats.items() if v.get('stdev', 0) / max(v.get('mean', 1), 0.01) > 1.0]
    if high_variance_metrics:
        lines.append(f"**High-variance metrics (CV > 1.0):** {', '.join(high_variance_metrics)}")
        lines.append("- These metrics show substantial variation across corpus. Good discriminating power.")

    lines.append("")
    lines.append("---")
    lines.append("")

    # Interpretation Notes
    lines.append("## Interpretation Notes")
    lines.append("")

    lines.append("### Limitations of This Corpus Profile")
    lines.append("")

    if corpus_size < 30:
        lines.append(f"- **Small sample (n={corpus_size})**: Statistics are unstable. Percentiles may shift dramatically with additional papers.")

    lines.append("- **No ground truth**: Metrics not validated against external quality assessments. High scores may reflect extraction quality, not research quality.")
    lines.append("- **Corpus-specific patterns**: Observations may not generalise to other domains, genres, or time periods.")
    lines.append("- **Extraction dependency**: All metrics depend on extraction quality and granularity decisions.")
    lines.append("")

    lines.append("### Using This Profile")
    lines.append("")
    lines.append("This profile should be used to:")
    lines.append("")
    lines.append("1. **Understand corpus characteristics** before interpreting individual paper scores")
    lines.append("2. **Identify metrics with good discriminating power** (high variance) vs poor power (low variance)")
    lines.append("3. **Calibrate expectations** for what constitutes \"typical\" vs \"exceptional\" scores")
    lines.append("4. **Compare corpora** (if multiple corpus profiles generated)")
    lines.append("5. **Inform metric refinement** (identify problematic metrics needing adjustment)")
    lines.append("")

    lines.append("Do NOT use this profile to:")
    lines.append("")
    lines.append("- Make definitive claims about research quality")
    lines.append("- Compare papers from different corpora without controlling for corpus characteristics")
    lines.append("- Treat corpus means as universal quality thresholds")
    lines.append("")

    lines.append("---")
    lines.append("")

    # Footer
    lines.append("**Profile generated:** {:%Y-%m-%d %H:%M:%S}".format(datetime.now()))
    lines.append("")
    lines.append("**Metrics reference:** See `docs/assessment-guide/credibility-metrics-reference.md`")
    lines.append("")
    lines.append("**Individual scorecards:** See `outputs/{paper-id}/metrics-scorecard.md`")
    lines.append("")

    return "\n".join(lines)


def main():
    """Main execution function."""
    print("=" * 60)
    print("CORPUS PROFILE GENERATOR")
    print("=" * 60)
    print()

    # Load dashboard
    print("Loading dashboard...")
    dashboard = load_dashboard()

    print(f"Corpus size: {dashboard['corpus_size']} papers")
    print()

    # Generate profile
    print("Generating corpus profile...")
    profile = generate_corpus_profile(dashboard)

    # Generate filename with timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d-%H%M")
    output_path = Path(f"outputs/corpus-profile-{timestamp}.md")

    # Save
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(profile)

    print(f"✓ Saved: {output_path}")
    print()
    print("=" * 60)
    print("COMPLETE!")
    print("=" * 60)


if __name__ == '__main__':
    main()
