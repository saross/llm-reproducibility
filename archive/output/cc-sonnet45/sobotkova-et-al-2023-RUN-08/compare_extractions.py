#!/usr/bin/env python3
"""
Compare RUN-08 extraction to previous best extraction (extraction-02).

Assess:
- Item counts and coverage differences
- RDMAP extraction quality (new in RUN-08)
- Extraction completeness
- Quality improvements from Phase 2 implicit RDMAP work
"""

import json
from pathlib import Path
from typing import Dict, Any

def load_extraction(filepath: str) -> Dict[str, Any]:
    """Load extraction JSON file."""
    path = Path(filepath)
    if not path.exists():
        print(f"ERROR: File not found: {filepath}")
        return None

    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def count_items(data: Dict[str, Any]) -> Dict[str, int]:
    """Count items in each category."""
    counts = {
        'evidence': len(data.get('evidence', [])),
        'claims': len(data.get('claims', [])),
        'implicit_arguments': len(data.get('implicit_arguments', [])),
        'research_designs': len(data.get('research_designs', [])),
        'methods': len(data.get('methods', [])),
        'protocols': len(data.get('protocols', []))
    }
    counts['total'] = sum(counts.values())
    return counts

def analyze_rdmap(data: Dict[str, Any]) -> Dict[str, Any]:
    """Analyze RDMAP extraction quality."""
    designs = data.get('research_designs', [])
    methods = data.get('methods', [])
    protocols = data.get('protocols', [])

    rdmap_stats = {
        'total_rdmap': len(designs) + len(methods) + len(protocols),
        'designs': {
            'total': len(designs),
            'explicit': sum(1 for d in designs if d.get('design_status') == 'explicit'),
            'implicit': sum(1 for d in designs if d.get('design_status') == 'implicit')
        },
        'methods': {
            'total': len(methods),
            'explicit': sum(1 for m in methods if m.get('method_status') == 'explicit'),
            'implicit': sum(1 for m in methods if m.get('method_status') == 'implicit')
        },
        'protocols': {
            'total': len(protocols),
            'explicit': sum(1 for p in protocols if p.get('protocol_status') == 'explicit'),
            'implicit': sum(1 for p in protocols if p.get('protocol_status') == 'implicit')
        }
    }

    return rdmap_stats

def analyze_relationships(data: Dict[str, Any]) -> Dict[str, Any]:
    """Analyze evidence-claim and RDMAP relationships."""
    evidence = data.get('evidence', [])
    claims = data.get('claims', [])
    designs = data.get('research_designs', [])
    methods = data.get('methods', [])
    protocols = data.get('protocols', [])

    # Evidence → Claims
    ev_to_claim_links = sum(len(e.get('supporting_claims', [])) for e in evidence)
    claims_with_evidence = sum(1 for c in claims if c.get('supported_by_evidence', []))

    # RDMAP relationships
    methods_with_designs = sum(1 for m in methods if m.get('implements_designs', []))
    protocols_with_methods = sum(1 for p in protocols if p.get('implements_methods', []))

    # Reverse relationships (bidirectional mapping)
    designs_with_methods = sum(1 for d in designs if d.get('realized_through_methods', []))
    methods_with_protocols = sum(1 for m in methods if m.get('realized_through_protocols', []))

    return {
        'evidence_to_claims': ev_to_claim_links,
        'claims_with_evidence': claims_with_evidence,
        'claims_total': len(claims),
        'evidence_coverage_pct': (claims_with_evidence / len(claims) * 100) if claims else 0,
        'avg_evidence_per_claim': (sum(len(c.get('supported_by_evidence', [])) for c in claims) / len(claims)) if claims else 0,
        'methods_with_designs': methods_with_designs,
        'protocols_with_methods': protocols_with_methods,
        'designs_with_methods': designs_with_methods,
        'methods_with_protocols': methods_with_protocols,
        'rdmap_bidirectional': designs_with_methods > 0 or methods_with_protocols > 0
    }

def generate_comparison_report(current: Dict[str, Any], previous: Dict[str, Any]) -> str:
    """Generate comprehensive comparison report."""

    # Count comparisons
    current_counts = count_items(current)
    previous_counts = count_items(previous)

    # RDMAP analysis
    current_rdmap = analyze_rdmap(current)
    previous_rdmap = analyze_rdmap(previous)

    # Relationship analysis
    current_rels = analyze_relationships(current)
    previous_rels = analyze_relationships(previous)

    # Generate report
    report = f"""# Extraction Comparison Report: RUN-08 vs extraction-02

**Current Run (RUN-08):** outputs/sobotkova-et-al-2023/extraction.json
**Previous Best (extraction-02):** archive/output/chatbot-sonnet45/with-skill/extraction-02/extraction.json

**Paper:** Sobotkova et al. (2023) - Creating large, high-quality geospatial datasets from historical maps using novice volunteers

**Comparison Date:** 2025-10-28

---

## 1. Item Count Comparison

| Category | RUN-08 | extraction-02 | Change | % Change |
|----------|--------|---------------|--------|----------|
| Evidence | {current_counts['evidence']} | {previous_counts['evidence']} | {current_counts['evidence'] - previous_counts['evidence']:+d} | {((current_counts['evidence'] - previous_counts['evidence']) / previous_counts['evidence'] * 100) if previous_counts['evidence'] else 0:+.1f}% |
| Claims | {current_counts['claims']} | {previous_counts['claims']} | {current_counts['claims'] - previous_counts['claims']:+d} | {((current_counts['claims'] - previous_counts['claims']) / previous_counts['claims'] * 100) if previous_counts['claims'] else 0:+.1f}% |
| Implicit Arguments | {current_counts['implicit_arguments']} | {previous_counts['implicit_arguments']} | {current_counts['implicit_arguments'] - previous_counts['implicit_arguments']:+d} | {((current_counts['implicit_arguments'] - previous_counts['implicit_arguments']) / previous_counts['implicit_arguments'] * 100) if previous_counts['implicit_arguments'] else 0:+.1f}% |
| Research Designs | {current_counts['research_designs']} | {previous_counts['research_designs']} | {current_counts['research_designs'] - previous_counts['research_designs']:+d} | {((current_counts['research_designs'] - previous_counts['research_designs']) / previous_counts['research_designs'] * 100) if previous_counts['research_designs'] else 'N/A'}% |
| Methods | {current_counts['methods']} | {previous_counts['methods']} | {current_counts['methods'] - previous_counts['methods']:+d} | {((current_counts['methods'] - previous_counts['methods']) / previous_counts['methods'] * 100) if previous_counts['methods'] else 'N/A'}% |
| Protocols | {current_counts['protocols']} | {previous_counts['protocols']} | {current_counts['protocols'] - previous_counts['protocols']:+d} | {((current_counts['protocols'] - previous_counts['protocols']) / previous_counts['protocols'] * 100) if previous_counts['protocols'] else 'N/A'}% |
| **Total** | **{current_counts['total']}** | **{previous_counts['total']}** | **{current_counts['total'] - previous_counts['total']:+d}** | **{((current_counts['total'] - previous_counts['total']) / previous_counts['total'] * 100) if previous_counts['total'] else 0:+.1f}%** |

---

## 2. RDMAP Extraction Quality

### RUN-08 (Current)

| Category | Total | Explicit | Implicit |
|----------|-------|----------|----------|
| Research Designs | {current_rdmap['designs']['total']} | {current_rdmap['designs']['explicit']} | {current_rdmap['designs']['implicit']} |
| Methods | {current_rdmap['methods']['total']} | {current_rdmap['methods']['explicit']} | {current_rdmap['methods']['implicit']} |
| Protocols | {current_rdmap['protocols']['total']} | {current_rdmap['protocols']['explicit']} | {current_rdmap['protocols']['implicit']} |
| **Total RDMAP** | **{current_rdmap['total_rdmap']}** | **{current_rdmap['designs']['explicit'] + current_rdmap['methods']['explicit'] + current_rdmap['protocols']['explicit']}** | **{current_rdmap['designs']['implicit'] + current_rdmap['methods']['implicit'] + current_rdmap['protocols']['implicit']}** |

### extraction-02 (Previous)

| Category | Total | Explicit | Implicit |
|----------|-------|----------|----------|
| Research Designs | {previous_rdmap['designs']['total']} | {previous_rdmap['designs']['explicit']} | {previous_rdmap['designs']['implicit']} |
| Methods | {previous_rdmap['methods']['total']} | {previous_rdmap['methods']['explicit']} | {previous_rdmap['methods']['implicit']} |
| Protocols | {previous_rdmap['protocols']['total']} | {previous_rdmap['protocols']['explicit']} | {previous_rdmap['protocols']['implicit']} |
| **Total RDMAP** | **{previous_rdmap['total_rdmap']}** | **{previous_rdmap['designs']['explicit'] + previous_rdmap['methods']['explicit'] + previous_rdmap['protocols']['explicit']}** | **{previous_rdmap['designs']['implicit'] + previous_rdmap['methods']['implicit'] + previous_rdmap['protocols']['implicit']}** |

### RDMAP Assessment

**Total RDMAP items:** RUN-08 has {current_rdmap['total_rdmap'] - previous_rdmap['total_rdmap']:+d} items compared to extraction-02

**Implicit RDMAP:**
- RUN-08: {current_rdmap['designs']['implicit'] + current_rdmap['methods']['implicit'] + current_rdmap['protocols']['implicit']} implicit items
- extraction-02: {previous_rdmap['designs']['implicit'] + previous_rdmap['methods']['implicit'] + previous_rdmap['protocols']['implicit']} implicit items
- **Change:** {(current_rdmap['designs']['implicit'] + current_rdmap['methods']['implicit'] + current_rdmap['protocols']['implicit']) - (previous_rdmap['designs']['implicit'] + previous_rdmap['methods']['implicit'] + previous_rdmap['protocols']['implicit']):+d} implicit items

**Significance:** {"✓ RUN-08 successfully extracted implicit RDMAP (Phase 2 improvement)" if (current_rdmap['designs']['implicit'] + current_rdmap['methods']['implicit'] + current_rdmap['protocols']['implicit']) > (previous_rdmap['designs']['implicit'] + previous_rdmap['methods']['implicit'] + previous_rdmap['protocols']['implicit']) else "Both runs have similar implicit RDMAP coverage"}

---

## 3. Evidence-Claim Relationship Coverage

### RUN-08 (Current)

- Total evidence → claim links: {current_rels['evidence_to_claims']}
- Claims with evidence support: {current_rels['claims_with_evidence']} / {current_rels['claims_total']} ({current_rels['evidence_coverage_pct']:.1f}%)
- Average evidence per claim: {current_rels['avg_evidence_per_claim']:.1f}

### extraction-02 (Previous)

- Total evidence → claim links: {previous_rels['evidence_to_claims']}
- Claims with evidence support: {previous_rels['claims_with_evidence']} / {previous_rels['claims_total']} ({previous_rels['evidence_coverage_pct']:.1f}%)
- Average evidence per claim: {previous_rels['avg_evidence_per_claim']:.1f}

### Coverage Comparison

- **Evidence-claim links:** {current_rels['evidence_to_claims'] - previous_rels['evidence_to_claims']:+d} links ({((current_rels['evidence_to_claims'] - previous_rels['evidence_to_claims']) / previous_rels['evidence_to_claims'] * 100) if previous_rels['evidence_to_claims'] else 0:+.1f}%)
- **Claims with evidence:** {current_rels['claims_with_evidence'] - previous_rels['claims_with_evidence']:+d} claims ({current_rels['evidence_coverage_pct'] - previous_rels['evidence_coverage_pct']:+.1f}% coverage change)
- **Average evidence per claim:** {current_rels['avg_evidence_per_claim'] - previous_rels['avg_evidence_per_claim']:+.1f} evidence items

---

## 4. RDMAP Relationship Completeness

### RUN-08 (Current)

- Methods implementing designs: {current_rels['methods_with_designs']} / {current_counts['methods']}
- Protocols implementing methods: {current_rels['protocols_with_methods']} / {current_counts['protocols']}
- **Bidirectional mapping:** {"✓ Yes" if current_rels['rdmap_bidirectional'] else "✗ No"}
  - Designs with reverse method links: {current_rels['designs_with_methods']} / {current_counts['research_designs']}
  - Methods with reverse protocol links: {current_rels['methods_with_protocols']} / {current_counts['methods']}

### extraction-02 (Previous)

- Methods implementing designs: {previous_rels['methods_with_designs']} / {previous_counts['methods']}
- Protocols implementing methods: {previous_rels['protocols_with_methods']} / {previous_counts['protocols']}
- **Bidirectional mapping:** {"✓ Yes" if previous_rels['rdmap_bidirectional'] else "✗ No"}
  - Designs with reverse method links: {previous_rels['designs_with_methods']} / {previous_counts['research_designs'] if previous_counts['research_designs'] > 0 else 0}
  - Methods with reverse protocol links: {previous_rels['methods_with_protocols']} / {previous_counts['methods'] if previous_counts['methods'] > 0 else 0}

---

## 5. Quality Improvements Assessment

### Strengths of RUN-08

"""

    # Assess strengths
    strengths = []

    if current_rdmap['total_rdmap'] > previous_rdmap['total_rdmap']:
        strengths.append(f"**Enhanced RDMAP coverage:** {current_rdmap['total_rdmap']} items vs {previous_rdmap['total_rdmap']} items ({current_rdmap['total_rdmap'] - previous_rdmap['total_rdmap']:+d})")

    if (current_rdmap['designs']['implicit'] + current_rdmap['methods']['implicit'] + current_rdmap['protocols']['implicit']) > (previous_rdmap['designs']['implicit'] + previous_rdmap['methods']['implicit'] + previous_rdmap['protocols']['implicit']):
        strengths.append(f"**Implicit RDMAP extraction:** Successfully extracted {current_rdmap['designs']['implicit'] + current_rdmap['methods']['implicit'] + current_rdmap['protocols']['implicit']} implicit items (Phase 2 improvement)")

    if current_rels['rdmap_bidirectional'] and not previous_rels['rdmap_bidirectional']:
        strengths.append("**Bidirectional RDMAP relationships:** Complete reverse mapping added in Pass 5")

    if current_rels['evidence_coverage_pct'] > previous_rels['evidence_coverage_pct']:
        strengths.append(f"**Better evidence coverage:** {current_rels['evidence_coverage_pct']:.1f}% vs {previous_rels['evidence_coverage_pct']:.1f}% ({current_rels['evidence_coverage_pct'] - previous_rels['evidence_coverage_pct']:+.1f}%)")

    if current_rels['avg_evidence_per_claim'] > previous_rels['avg_evidence_per_claim']:
        strengths.append(f"**Higher evidence density:** {current_rels['avg_evidence_per_claim']:.1f} vs {previous_rels['avg_evidence_per_claim']:.1f} evidence per claim")

    if not strengths:
        strengths.append("Maintained extraction quality with updated workflow")

    for strength in strengths:
        report += f"\n{strength}\n"

    report += "\n### Strengths of extraction-02\n\n"

    # Assess previous strengths
    previous_strengths = []

    if previous_counts['evidence'] > current_counts['evidence']:
        previous_strengths.append(f"**More evidence items:** {previous_counts['evidence']} vs {current_counts['evidence']} ({previous_counts['evidence'] - current_counts['evidence']:+d})")

    if previous_counts['implicit_arguments'] > current_counts['implicit_arguments']:
        previous_strengths.append(f"**More implicit arguments:** {previous_counts['implicit_arguments']} vs {current_counts['implicit_arguments']} ({previous_counts['implicit_arguments'] - current_counts['implicit_arguments']:+d})")

    if previous_rels['evidence_to_claims'] > current_rels['evidence_to_claims']:
        previous_strengths.append(f"**More evidence-claim links:** {previous_rels['evidence_to_claims']} vs {current_rels['evidence_to_claims']} ({previous_rels['evidence_to_claims'] - current_rels['evidence_to_claims']:+d})")

    if not previous_strengths:
        previous_strengths.append("RUN-08 shows improvements across most metrics")

    for strength in previous_strengths:
        report += f"\n{strength}\n"

    report += """

---

## 6. Overall Assessment

### Key Findings

"""

    # Overall assessment
    if current_rdmap['total_rdmap'] > 0 and previous_rdmap['total_rdmap'] == 0:
        report += "\n**Major improvement:** RUN-08 successfully extracted comprehensive RDMAP hierarchy (Research Designs → Methods → Protocols), which was absent or minimal in extraction-02.\n"

    if (current_rdmap['designs']['implicit'] + current_rdmap['methods']['implicit'] + current_rdmap['protocols']['implicit']) > 0:
        report += f"\n**Phase 2 validation:** Implicit RDMAP extraction is working ({current_rdmap['designs']['implicit'] + current_rdmap['methods']['implicit'] + current_rdmap['protocols']['implicit']} implicit items identified).\n"

    if current_rels['rdmap_bidirectional']:
        report += "\n**Relationship completeness:** RUN-08 includes bidirectional RDMAP relationships, enabling traversal up and down the hierarchy.\n"

    # Overall recommendation
    report += """

### Recommendation

"""

    if current_counts['total'] >= previous_counts['total'] and current_rdmap['total_rdmap'] > previous_rdmap['total_rdmap']:
        report += "**Use RUN-08** - Provides comprehensive RDMAP extraction with equal or better coverage in other areas.\n"
    elif current_counts['total'] < previous_counts['total'] and current_rdmap['total_rdmap'] > previous_rdmap['total_rdmap']:
        report += "**Consider RUN-08 for RDMAP analysis** - Better methodological extraction, though extraction-02 has more evidence/claim items.\n"
    else:
        report += "**Further investigation needed** - Both extractions have distinct strengths.\n"

    report += """

---

## 7. Extraction Metadata Comparison

### RUN-08 (Current)

"""

    if 'project_metadata' in current:
        meta = current['project_metadata']
        report += f"- **Title:** {meta.get('paper_title', 'N/A')}\n"
        report += f"- **Authors:** {', '.join(meta.get('authors', []))}\n"
        report += f"- **DOI:** {meta.get('doi', 'N/A')}\n"
        report += f"- **Research Context:** {meta.get('research_context', 'N/A')[:100]}...\n"

    report += "\n### extraction-02 (Previous)\n\n"

    if 'project_metadata' in previous:
        meta = previous['project_metadata']
        report += f"- **Title:** {meta.get('paper_title', 'N/A')}\n"
        report += f"- **Authors:** {', '.join(meta.get('authors', []))}\n"
        report += f"- **DOI:** {meta.get('doi', 'N/A')}\n"
        report += f"- **Research Context:** {meta.get('research_context', 'N/A')[:100]}...\n"

    report += """

---

*Comparison generated: 2025-10-28*

*Comparison script: compare_extractions.py*
"""

    return report

def main():
    """Generate extraction comparison report."""
    print("="*80)
    print("EXTRACTION COMPARISON: RUN-08 vs extraction-02")
    print("="*80)

    # File paths
    current_path = "/home/shawn/Code/llm-reproducibility/outputs/sobotkova-et-al-2023/extraction.json"
    previous_path = "/home/shawn/Code/llm-reproducibility/archive/output/chatbot-sonnet45/with-skill/extraction-02/sobotkova_rdmap_pass3_corrected.json"

    # Load extractions
    print("\nLoading current extraction (RUN-08)...")
    current = load_extraction(current_path)
    if not current:
        print("ERROR: Could not load current extraction")
        return

    print("Loading previous extraction (extraction-02)...")
    previous = load_extraction(previous_path)
    if not previous:
        print("ERROR: Could not load previous extraction")
        return

    # Generate comparison
    print("\nGenerating comparison report...")
    report = generate_comparison_report(current, previous)

    # Save report
    output_path = Path("/home/shawn/Code/llm-reproducibility/outputs/sobotkova-et-al-2023/comparison-report.md")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(report)

    print(f"\n✓ Comparison report generated: {output_path}")
    print(f"  Report size: {output_path.stat().st_size / 1024:.1f}K")

    # Print summary
    current_counts = count_items(current)
    previous_counts = count_items(previous)
    current_rdmap = analyze_rdmap(current)
    previous_rdmap = analyze_rdmap(previous)

    print("\n" + "="*80)
    print("QUICK SUMMARY")
    print("="*80)
    print(f"\nTotal items: {current_counts['total']} (RUN-08) vs {previous_counts['total']} (extraction-02)")
    print(f"RDMAP items: {current_rdmap['total_rdmap']} (RUN-08) vs {previous_rdmap['total_rdmap']} (extraction-02)")
    print(f"Implicit RDMAP: {current_rdmap['designs']['implicit'] + current_rdmap['methods']['implicit'] + current_rdmap['protocols']['implicit']} (RUN-08) vs {previous_rdmap['designs']['implicit'] + previous_rdmap['methods']['implicit'] + previous_rdmap['protocols']['implicit']} (extraction-02)")

    print("\n" + "="*80)
    print("COMPARISON COMPLETE")
    print("="*80)

if __name__ == "__main__":
    main()
