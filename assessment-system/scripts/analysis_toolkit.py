#!/usr/bin/env python3
"""
Analysis Toolkit for Credibility Assessment

Provides graph query functions and quantitative metric calculations for
extraction.json files from the research-assessor workflow.

Functions organised into:
1. Graph Query Library: Extract patterns from CEM/RDMAP graphs
2. Quantitative Metrics: Calculate 8 credibility metrics
3. Utility Functions: Helper methods for data processing

Usage:
    from analysis_toolkit import load_extraction, calculate_all_metrics

    extraction = load_extraction("outputs/paper-id/extraction.json")
    metrics = calculate_all_metrics(extraction)
    print(metrics)

Metrics Calculated:
    - ESD: Evidential Support Density
    - TCI: Transparency Completeness Index
    - SCS: Scope Constraint Score
    - RTI: Robustness Triangulation Index
    - RIS: Replicability Infrastructure Score
    - PGCS: PID Graph Connectivity Score
    - FCS: FAIR Compliance Score
    - MDD: Methods Documentation Density

Author: Claude Sonnet 4.5
Date: 2025-11-14
Version: 1.0
"""

import json
import math
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from collections import Counter, defaultdict


# =============================================================================
# GRAPH QUERY LIBRARY
# =============================================================================

def load_extraction(filepath: str) -> Dict[str, Any]:
    """
    Load extraction.json file and return parsed dictionary.

    Args:
        filepath: Path to extraction.json file

    Returns:
        Parsed extraction dictionary

    Raises:
        FileNotFoundError: If file doesn't exist
        json.JSONDecodeError: If file is not valid JSON
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


def get_claims(extraction: Dict[str, Any], section: Optional[str] = None) -> List[Dict]:
    """
    Extract claim items, optionally filtered by section.

    Args:
        extraction: Parsed extraction dictionary
        section: Optional section filter (e.g., "Introduction", "Discussion")

    Returns:
        List of claim dictionaries
    """
    claims = extraction.get('claims', [])

    if section:
        return [c for c in claims if c.get('location', {}).get('section') == section]
    return claims


def get_evidence(extraction: Dict[str, Any], section: Optional[str] = None) -> List[Dict]:
    """
    Extract evidence items, optionally filtered by section.

    Args:
        extraction: Parsed extraction dictionary
        section: Optional section filter

    Returns:
        List of evidence dictionaries
    """
    evidence = extraction.get('evidence', [])

    if section:
        return [e for e in evidence if e.get('location', {}).get('section') == section]
    return evidence


def get_rdmap_items(extraction: Dict[str, Any],
                    item_type: Optional[str] = None) -> List[Dict]:
    """
    Extract RDMAP items (research_designs, methods, protocols).

    Args:
        extraction: Parsed extraction dictionary
        item_type: Optional filter ("research_designs", "methods", "protocols")

    Returns:
        List of RDMAP item dictionaries
    """
    if item_type:
        return extraction.get(item_type, [])

    # Return all RDMAP items combined
    rdmap = []
    rdmap.extend(extraction.get('research_designs', []))
    rdmap.extend(extraction.get('methods', []))
    rdmap.extend(extraction.get('protocols', []))
    return rdmap


def get_claim_evidence_mappings(extraction: Dict[str, Any]) -> List[Tuple[str, str]]:
    """
    Extract all claim→evidence relationship mappings.

    Args:
        extraction: Parsed extraction dictionary

    Returns:
        List of (claim_id, evidence_id) tuples
    """
    mappings = []

    # Check claims for evidence links
    for claim in extraction.get('claims', []):
        claim_id = claim.get('id')
        evidence_links = claim.get('supported_by_evidence',
                        claim.get('supported_by',
                        claim.get('evidence_links', [])))

        for evidence_id in evidence_links:
            mappings.append((claim_id, evidence_id))

    # Check evidence for claim links (bidirectional)
    for evidence in extraction.get('evidence', []):
        evidence_id = evidence.get('id')
        claim_links = evidence.get('supports_claims',
                     evidence.get('linked_claims', []))

        for claim_id in claim_links:
            if (claim_id, evidence_id) not in mappings:
                mappings.append((claim_id, evidence_id))

    return mappings


def get_infrastructure_items(extraction: Dict[str, Any]) -> Dict[str, Any]:
    """
    Extract infrastructure assessment data (PIDs, FAIR, permits, etc.).

    Args:
        extraction: Parsed extraction dictionary

    Returns:
        Dictionary with infrastructure categories
    """
    return extraction.get('reproducibility_infrastructure', {})


def get_sections(extraction: Dict[str, Any]) -> List[str]:
    """
    Get list of unique sections in extraction.

    Args:
        extraction: Parsed extraction dictionary

    Returns:
        Sorted list of section names
    """
    sections = set()

    for item in (extraction.get('claims', []) +
                 extraction.get('evidence', []) +
                 extraction.get('research_designs', []) +
                 extraction.get('methods', []) +
                 extraction.get('protocols', [])):
        section = item.get('location', {}).get('section')
        if section:
            sections.add(section)

    return sorted(sections)


def count_items_by_section(extraction: Dict[str, Any],
                          item_type: str) -> Dict[str, int]:
    """
    Count items of a specific type grouped by section.

    Args:
        extraction: Parsed extraction dictionary
        item_type: Type to count ("claims", "evidence", "methods", etc.)

    Returns:
        Dictionary mapping section name to count
    """
    items = extraction.get(item_type, [])
    counts = Counter()

    for item in items:
        section = item.get('location', {}).get('section', 'Unknown')
        counts[section] += 1

    return dict(counts)


# =============================================================================
# QUANTITATIVE METRICS
# =============================================================================

def calculate_esd(extraction: Dict[str, Any]) -> Dict[str, Any]:
    """
    Calculate Evidential Support Density (ESD).

    Measures: Claims:Evidence ratio by section
    Purpose: Detect under-supported claims
    Interpretation: Lower is better (more evidence per claim)

    Args:
        extraction: Parsed extraction dictionary

    Returns:
        Dictionary with overall ESD and per-section breakdown
    """
    sections = get_sections(extraction)

    section_ratios = {}
    total_claims = 0
    total_evidence = 0

    # If sections exist, try calculating per-section and aggregate
    if sections:
        for section in sections:
            claims = get_claims(extraction, section=section)
            evidence = get_evidence(extraction, section=section)

            claim_count = len(claims)
            evidence_count = len(evidence)

            total_claims += claim_count
            total_evidence += evidence_count

            # Calculate ratio (avoid division by zero)
            if evidence_count > 0:
                ratio = claim_count / evidence_count
            else:
                ratio = float('inf') if claim_count > 0 else 0.0

            section_ratios[section] = {
                'claims': claim_count,
                'evidence': evidence_count,
                'ratio': ratio
            }

        # Check if section-based counting actually found claims/evidence
        # If not, fall back to counting all items (handles case where sections
        # exist in RDMAP but not in claims/evidence)
        if total_claims == 0 and total_evidence == 0:
            all_claims = get_claims(extraction)
            all_evidence = get_evidence(extraction)

            total_claims = len(all_claims)
            total_evidence = len(all_evidence)

            # Clear section_ratios and add fallback entry
            section_ratios = {}
            if total_claims > 0 or total_evidence > 0:
                if total_evidence > 0:
                    ratio = total_claims / total_evidence
                else:
                    ratio = float('inf') if total_claims > 0 else 0.0

                section_ratios['[No section data in claims/evidence]'] = {
                    'claims': total_claims,
                    'evidence': total_evidence,
                    'ratio': ratio
                }
    else:
        # Fallback: No section data available, count all items
        all_claims = get_claims(extraction)
        all_evidence = get_evidence(extraction)

        total_claims = len(all_claims)
        total_evidence = len(all_evidence)

        # Add a single "No sections" entry for reporting
        if total_claims > 0 or total_evidence > 0:
            if total_evidence > 0:
                ratio = total_claims / total_evidence
            else:
                ratio = float('inf') if total_claims > 0 else 0.0

            section_ratios['[No section data]'] = {
                'claims': total_claims,
                'evidence': total_evidence,
                'ratio': ratio
            }

    # Calculate overall ESD
    if total_evidence > 0:
        overall_esd = total_claims / total_evidence
    else:
        overall_esd = float('inf') if total_claims > 0 else 0.0

    return {
        'metric': 'ESD',
        'name': 'Evidential Support Density',
        'score': round(overall_esd, 2),
        'interpretation': 'Lower is better (more evidence per claim)',
        'total_claims': total_claims,
        'total_evidence': total_evidence,
        'by_section': section_ratios
    }


def calculate_tci(extraction: Dict[str, Any]) -> Dict[str, Any]:
    """
    Calculate Transparency Completeness Index (TCI).

    Measures: RDMAP coverage and detail level
    Purpose: Assess methods documentation completeness
    Interpretation: Higher is better (0-1 scale)

    Args:
        extraction: Parsed extraction dictionary

    Returns:
        Dictionary with TCI score and components
    """
    research_designs = extraction.get('research_designs', [])
    methods = extraction.get('methods', [])
    protocols = extraction.get('protocols', [])

    # Count items
    rd_count = len(research_designs)
    method_count = len(methods)
    protocol_count = len(protocols)
    total_rdmap = rd_count + method_count + protocol_count

    # Assess completeness of each tier
    # Expected minimums based on typical papers (calibrated to corpus)
    expected_rd = 2  # At least 2 research designs
    expected_methods = 5  # At least 5 methods
    expected_protocols = 8  # At least 8 protocols

    # Calculate completeness scores (capped at 1.0)
    rd_completeness = min(rd_count / expected_rd, 1.0) if expected_rd > 0 else 0.0
    method_completeness = min(method_count / expected_methods, 1.0) if expected_methods > 0 else 0.0
    protocol_completeness = min(protocol_count / expected_protocols, 1.0) if expected_protocols > 0 else 0.0

    # Weighted average (protocols weighted more as they indicate detail)
    # Weights: RD=0.2, Methods=0.3, Protocols=0.5
    tci_score = (
        0.2 * rd_completeness +
        0.3 * method_completeness +
        0.5 * protocol_completeness
    )

    return {
        'metric': 'TCI',
        'name': 'Transparency Completeness Index',
        'score': round(tci_score, 2),
        'interpretation': 'Higher is better (0-1 scale)',
        'total_rdmap_items': total_rdmap,
        'breakdown': {
            'research_designs': {
                'count': rd_count,
                'expected': expected_rd,
                'completeness': round(rd_completeness, 2)
            },
            'methods': {
                'count': method_count,
                'expected': expected_methods,
                'completeness': round(method_completeness, 2)
            },
            'protocols': {
                'count': protocol_count,
                'expected': expected_protocols,
                'completeness': round(protocol_completeness, 2)
            }
        }
    }


def calculate_scs(extraction: Dict[str, Any]) -> Dict[str, Any]:
    """
    Calculate Scope Constraint Score (SCS).

    Measures: Explicit scope/limitation statements
    Purpose: Detect overclaiming or insufficient qualification
    Interpretation: Higher is better (raw count)

    Args:
        extraction: Parsed extraction dictionary

    Returns:
        Dictionary with SCS and breakdown
    """
    claims = extraction.get('claims', [])

    # Count scope constraints in claims
    scope_constraints = 0
    scoped_claims = 0

    for claim in claims:
        # Check for scope_constraint field
        if claim.get('scope_constraint'):
            scope_constraints += 1
            scoped_claims += 1
            continue

        # Check for limitation/qualification in claim text
        # Handle both 'claim_text' (newer schema) and 'content' (older schema)
        claim_text = claim.get('claim_text', claim.get('content', '')).lower()

        # Scope constraint indicators
        scope_indicators = [
            'in this study',
            'in our study',
            'within the',
            'limited to',
            'constrained by',
            'only applies',
            'specific to',
            'in the context of',
            'for this dataset',
            'in this case'
        ]

        # Limitation indicators
        limitation_indicators = [
            'however',
            'although',
            'limitation',
            'caveat',
            'but',
            'may not',
            'might not',
            'unclear',
            'uncertain',
            'requires further'
        ]

        has_scope = any(indicator in claim_text for indicator in scope_indicators)
        has_limitation = any(indicator in claim_text for indicator in limitation_indicators)

        if has_scope or has_limitation:
            scope_constraints += 1
            if has_scope:
                scoped_claims += 1

    # Calculate percentage
    total_claims = len(claims)
    scoped_pct = (scoped_claims / total_claims * 100) if total_claims > 0 else 0.0

    return {
        'metric': 'SCS',
        'name': 'Scope Constraint Score',
        'score': scope_constraints,
        'interpretation': 'Higher is better (more explicit boundaries)',
        'total_claims': total_claims,
        'scoped_claims': scoped_claims,
        'scoped_percentage': round(scoped_pct, 1),
        'breakdown': {
            'explicit_scope_fields': scoped_claims,
            'limitation_statements': scope_constraints - scoped_claims
        }
    }


def calculate_rti(extraction: Dict[str, Any]) -> Dict[str, Any]:
    """
    Calculate Robustness Triangulation Index (RTI).

    Measures: Evidence type diversity
    Purpose: Assess whether claims rest on single vs multiple evidence types
    Interpretation: Higher is better (Shannon diversity index, 0-3 typical range)

    Args:
        extraction: Parsed extraction dictionary

    Returns:
        Dictionary with RTI and evidence type distribution
    """
    evidence = extraction.get('evidence', [])

    # Count evidence by type
    evidence_types = Counter()
    for item in evidence:
        etype = item.get('evidence_type', 'Unknown')
        evidence_types[etype] += 1

    # Calculate Shannon diversity index
    # H = -Σ(p_i * ln(p_i)) where p_i is proportion of type i
    total = sum(evidence_types.values())

    if total == 0:
        shannon_h = 0.0
    else:
        shannon_h = 0.0
        for count in evidence_types.values():
            if count > 0:
                proportion = count / total
                shannon_h -= proportion * math.log(proportion)

    # Also calculate effective number of types (exp(H))
    effective_types = math.exp(shannon_h) if shannon_h > 0 else 0.0

    return {
        'metric': 'RTI',
        'name': 'Robustness Triangulation Index',
        'score': round(shannon_h, 2),
        'interpretation': 'Higher is better (Shannon H, typical range 0-3)',
        'effective_types': round(effective_types, 1),
        'total_evidence': total,
        'unique_types': len(evidence_types),
        'evidence_type_distribution': dict(evidence_types)
    }


def calculate_ris(extraction: Dict[str, Any]) -> Dict[str, Any]:
    """
    Calculate Replicability Infrastructure Score (RIS).

    Measures: PIDs for data/code/materials + sharing statements
    Purpose: Assess data/code/materials availability for replication
    Interpretation: Higher is better (0-10 scale)

    Args:
        extraction: Parsed extraction dictionary

    Returns:
        Dictionary with RIS and infrastructure breakdown
    """
    infrastructure = get_infrastructure_items(extraction)
    pids = infrastructure.get('persistent_identifiers', {})
    data_avail = infrastructure.get('data_availability', {})
    code_avail = infrastructure.get('code_availability', {})

    score = 0
    components = {}

    # Paper DOI (1 point)
    paper_doi = pids.get('paper_doi')
    if paper_doi and isinstance(paper_doi, dict) and paper_doi.get('doi'):
        score += 1
        components['paper_doi'] = 1
    else:
        components['paper_doi'] = 0

    # Author ORCIDs (1 point if >0% coverage)
    orcid_coverage = pids.get('orcid_coverage', {}).get('coverage_percentage', 0)
    if orcid_coverage > 0:
        score += 1
        components['author_orcids'] = 1
    else:
        components['author_orcids'] = 0

    # Dataset PIDs (2 points)
    dataset_pids = pids.get('dataset_pids', [])
    if len(dataset_pids) > 0:
        score += 2
        components['dataset_pids'] = 2
    else:
        components['dataset_pids'] = 0

    # Software PIDs (2 points)
    software_pids = pids.get('software_pids', [])
    if len(software_pids) > 0:
        score += 2
        components['software_pids'] = 2
    else:
        components['software_pids'] = 0

    # Data availability statement (1 point)
    if data_avail.get('statement_present', False):
        score += 1
        components['data_statement'] = 1
    else:
        components['data_statement'] = 0

    # Code availability statement (1 point)
    if code_avail.get('statement_present', False):
        score += 1
        components['code_statement'] = 1
    else:
        components['code_statement'] = 0

    # Supplementary materials (1 point)
    supp = infrastructure.get('supplementary_materials', {})
    if supp.get('present', False):
        score += 1
        components['supplementary_materials'] = 1
    else:
        components['supplementary_materials'] = 0

    # Preregistration (1 point)
    prereg = infrastructure.get('preregistration', {})
    if prereg.get('preregistered', False):
        score += 1
        components['preregistration'] = 1
    else:
        components['preregistration'] = 0

    return {
        'metric': 'RIS',
        'name': 'Replicability Infrastructure Score',
        'score': score,
        'max_score': 10,
        'interpretation': 'Higher is better (0-10 scale)',
        'percentage': round((score / 10) * 100, 1),
        'components': components,
        'breakdown': {
            'paper_doi': components['paper_doi'],
            'author_orcids': components['author_orcids'],
            'dataset_pids': components['dataset_pids'],
            'software_pids': components['software_pids'],
            'data_statement': components['data_statement'],
            'code_statement': components['code_statement'],
            'supplementary_materials': components['supplementary_materials'],
            'preregistration': components['preregistration']
        }
    }


def calculate_pgcs(extraction: Dict[str, Any]) -> Dict[str, Any]:
    """
    Calculate PID Graph Connectivity Score (PGCS).

    Measures: How many PIDs are linked (DOI→dataset DOI→software, etc.)
    Purpose: Evaluate FAIR infrastructure integration
    Interpretation: Higher is better (uses existing connectivity score from Pass 6)

    Args:
        extraction: Parsed extraction dictionary

    Returns:
        Dictionary with PGCS and connectivity details
    """
    infrastructure = get_infrastructure_items(extraction)
    pids = infrastructure.get('persistent_identifiers', {})

    # Use existing connectivity score from Pass 6
    pid_graph = pids.get('pid_graph_summary', {})
    connectivity_score = pid_graph.get('connectivity_score', 0)
    connectivity_rating = pid_graph.get('connectivity_rating', 'none')
    rationale = pid_graph.get('rationale', 'No PID graph connectivity assessment available')

    # Count different PID types for additional context
    paper_doi = pids.get('paper_doi')
    pid_counts = {
        'paper_doi': 1 if (paper_doi and isinstance(paper_doi, dict) and paper_doi.get('doi')) else 0,
        'author_orcids': len(pids.get('author_orcids', [])),
        'dataset_pids': len(pids.get('dataset_pids', [])),
        'software_pids': len(pids.get('software_pids', [])),
        'sample_pids': len(pids.get('sample_pids', [])),
        'project_pid': 1 if pids.get('project_pid') else 0,
        'vocabulary_pids': len(pids.get('vocabulary_pids', []))
    }

    total_pids = sum(pid_counts.values())

    return {
        'metric': 'PGCS',
        'name': 'PID Graph Connectivity Score',
        'score': connectivity_score,
        'rating': connectivity_rating,
        'interpretation': 'Higher is better (connectivity between PIDs)',
        'total_pids': total_pids,
        'pid_counts': pid_counts,
        'rationale': rationale
    }


def calculate_fcs(extraction: Dict[str, Any]) -> Dict[str, Any]:
    """
    Calculate FAIR Compliance Score (FCS).

    Measures: Aggregate Pass 6 FAIR assessment (0-15 scale)
    Purpose: Direct measure of Findable, Accessible, Interoperable, Reusable compliance
    Interpretation: Higher is better (0-15 scale)

    Args:
        extraction: Parsed extraction dictionary

    Returns:
        Dictionary with FCS and FAIR breakdown
    """
    infrastructure = get_infrastructure_items(extraction)
    fair = infrastructure.get('fair_assessment', {})

    # Check if FAIR assessment was conducted
    if not fair.get('assessed', False):
        return {
            'metric': 'FCS',
            'name': 'FAIR Compliance Score',
            'score': 0,
            'max_score': 15,
            'interpretation': 'Higher is better (0-15 scale)',
            'percentage': 0.0,
            'assessed': False,
            'message': 'FAIR assessment not conducted for this paper'
        }

    # Extract scores from each FAIR dimension
    findable = fair.get('findable', {})
    accessible = fair.get('accessible', {})
    interoperable = fair.get('interoperable', {})
    reusable = fair.get('reusable', {})

    findable_score = findable.get('score', 0)
    accessible_score = accessible.get('score', 0)
    interoperable_score = interoperable.get('score', 0)
    reusable_score = reusable.get('score', 0)

    # Total score
    total_score = findable_score + accessible_score + interoperable_score + reusable_score

    # Maximum possible (from schema: F=4, A=4, I=3, R=4)
    max_score = 15

    return {
        'metric': 'FCS',
        'name': 'FAIR Compliance Score',
        'score': total_score,
        'max_score': max_score,
        'interpretation': 'Higher is better (0-15 scale)',
        'percentage': round((total_score / max_score) * 100, 1),
        'assessed': True,
        'breakdown': {
            'findable': {
                'score': findable_score,
                'max_score': findable.get('max_score', 4),
                'rationale': findable.get('rationale', '')
            },
            'accessible': {
                'score': accessible_score,
                'max_score': accessible.get('max_score', 4),
                'rationale': accessible.get('rationale', '')
            },
            'interoperable': {
                'score': interoperable_score,
                'max_score': interoperable.get('max_score', 3),
                'rationale': interoperable.get('rationale', '')
            },
            'reusable': {
                'score': reusable_score,
                'max_score': reusable.get('max_score', 4),
                'rationale': reusable.get('rationale', '')
            }
        }
    }


def calculate_mdd(extraction: Dict[str, Any]) -> Dict[str, Any]:
    """
    Calculate Methods Documentation Density (MDD).

    Measures: Average verbatim quote length for RDMAP items
    Purpose: Assess level of methodological detail (longer quotes = more detail)
    Interpretation: Higher is better (mean characters per RDMAP item)

    Args:
        extraction: Parsed extraction dictionary

    Returns:
        Dictionary with MDD and breakdown by tier
    """
    research_designs = extraction.get('research_designs', [])
    methods = extraction.get('methods', [])
    protocols = extraction.get('protocols', [])

    def get_text_length(item: Dict) -> int:
        """Extract text length from various possible fields."""
        # Try different text field names
        text = (item.get('verbatim_quote') or
                item.get('text') or
                item.get('description') or
                item.get('research_design_text') or
                item.get('method_text') or
                item.get('protocol_text') or
                '')
        return len(text)

    # Calculate lengths for each tier
    rd_lengths = [get_text_length(rd) for rd in research_designs]
    method_lengths = [get_text_length(m) for m in methods]
    protocol_lengths = [get_text_length(p) for p in protocols]

    # Calculate means (avoid division by zero)
    rd_mean = sum(rd_lengths) / len(rd_lengths) if rd_lengths else 0
    method_mean = sum(method_lengths) / len(method_lengths) if method_lengths else 0
    protocol_mean = sum(protocol_lengths) / len(protocol_lengths) if protocol_lengths else 0

    # Overall mean across all RDMAP items
    all_lengths = rd_lengths + method_lengths + protocol_lengths
    overall_mean = sum(all_lengths) / len(all_lengths) if all_lengths else 0

    return {
        'metric': 'MDD',
        'name': 'Methods Documentation Density',
        'score': round(overall_mean, 1),
        'interpretation': 'Higher is better (mean characters per RDMAP item)',
        'total_rdmap_items': len(all_lengths),
        'breakdown': {
            'research_designs': {
                'count': len(rd_lengths),
                'mean_length': round(rd_mean, 1),
                'total_chars': sum(rd_lengths)
            },
            'methods': {
                'count': len(method_lengths),
                'mean_length': round(method_mean, 1),
                'total_chars': sum(method_lengths)
            },
            'protocols': {
                'count': len(protocol_lengths),
                'mean_length': round(protocol_mean, 1),
                'total_chars': sum(protocol_lengths)
            }
        }
    }


# =============================================================================
# MAIN CALCULATION FUNCTION
# =============================================================================

def calculate_all_metrics(extraction: Dict[str, Any]) -> Dict[str, Any]:
    """
    Calculate all quantitative credibility metrics.

    Args:
        extraction: Parsed extraction dictionary

    Returns:
        Dictionary with all 8 metrics
    """
    return {
        'esd': calculate_esd(extraction),
        'tci': calculate_tci(extraction),
        'scs': calculate_scs(extraction),
        'rti': calculate_rti(extraction),
        'ris': calculate_ris(extraction),
        'pgcs': calculate_pgcs(extraction),
        'fcs': calculate_fcs(extraction),
        'mdd': calculate_mdd(extraction)
    }


# =============================================================================
# UTILITY FUNCTIONS
# =============================================================================

def get_paper_metadata(extraction: Dict[str, Any]) -> Dict[str, Any]:
    """
    Extract paper metadata from extraction.

    Args:
        extraction: Parsed extraction dictionary

    Returns:
        Dictionary with metadata fields
    """
    metadata = extraction.get('project_metadata', {})
    return {
        'title': metadata.get('paper_title', metadata.get('title', 'Unknown')),
        'authors': metadata.get('authors', []),
        'year': metadata.get('publication_year', 'Unknown'),
        'doi': metadata.get('doi', None)
    }


def summarise_extraction(extraction: Dict[str, Any]) -> Dict[str, Any]:
    """
    Generate summary statistics for extraction.

    Args:
        extraction: Parsed extraction dictionary

    Returns:
        Dictionary with summary counts
    """
    return {
        'total_items': (
            len(extraction.get('evidence', [])) +
            len(extraction.get('claims', [])) +
            len(extraction.get('research_designs', [])) +
            len(extraction.get('methods', [])) +
            len(extraction.get('protocols', []))
        ),
        'evidence': len(extraction.get('evidence', [])),
        'claims': len(extraction.get('claims', [])),
        'implicit_arguments': len(extraction.get('implicit_arguments', [])),
        'research_designs': len(extraction.get('research_designs', [])),
        'methods': len(extraction.get('methods', [])),
        'protocols': len(extraction.get('protocols', [])),
        'sections': len(get_sections(extraction)),
        'claim_evidence_mappings': len(get_claim_evidence_mappings(extraction))
    }


# =============================================================================
# CLI INTERFACE (for testing)
# =============================================================================

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Usage: python3 analysis_toolkit.py <extraction.json>")
        print("\nCalculates quantitative credibility metrics for extraction.")
        sys.exit(1)

    filepath = sys.argv[1]

    try:
        # Load extraction
        print(f"Loading extraction from: {filepath}")
        extraction = load_extraction(filepath)

        # Get metadata
        metadata = get_paper_metadata(extraction)
        print(f"\nPaper: {metadata['title']}")
        print(f"Authors: {', '.join(metadata['authors'][:3])}" +
              (" et al." if len(metadata['authors']) > 3 else ""))
        print(f"Year: {metadata['year']}")

        # Summary
        summary = summarise_extraction(extraction)
        print(f"\nExtraction Summary:")
        print(f"  Total items: {summary['total_items']}")
        print(f"  Evidence: {summary['evidence']}")
        print(f"  Claims: {summary['claims']}")
        print(f"  RDMAP: {summary['research_designs'] + summary['methods'] + summary['protocols']}")
        print(f"  Sections: {summary['sections']}")

        # Calculate metrics
        print(f"\nCalculating metrics...")
        metrics = calculate_all_metrics(extraction)

        # Display results
        print(f"\n{'='*60}")
        print(f"QUANTITATIVE CREDIBILITY METRICS")
        print(f"{'='*60}")

        for metric_key, metric_data in metrics.items():
            print(f"\n{metric_data['name']} ({metric_data['metric']})")
            print(f"  Score: {metric_data['score']}")
            print(f"  {metric_data['interpretation']}")

        print(f"\n{'='*60}")

    except FileNotFoundError:
        print(f"Error: File not found: {filepath}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in file: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
