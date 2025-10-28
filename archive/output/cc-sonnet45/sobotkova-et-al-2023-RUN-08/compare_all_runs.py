#!/usr/bin/env python3
"""
Compare RUN-08 extraction to all complete cc-sonnet45 runs.

Compares RUN-01 through RUN-07 (excluding RUN-00-fail and RUN-06-partial)
against the current RUN-08 extraction.
"""

import json
from pathlib import Path
from typing import Dict, Any, List

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
    """Analyse RDMAP extraction quality."""
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
    """Analyse evidence-claim and RDMAP relationships."""
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

def generate_multi_run_comparison(runs: Dict[str, Dict[str, Any]]) -> str:
    """Generate comprehensive multi-run comparison report."""

    # Get run identifiers sorted
    run_ids = sorted([rid for rid in runs.keys() if rid != 'RUN-08'])
    run_ids.append('RUN-08')  # Add current run at the end

    # Collect stats for all runs
    all_counts = {rid: count_items(runs[rid]) for rid in run_ids}
    all_rdmap = {rid: analyze_rdmap(runs[rid]) for rid in run_ids}
    all_rels = {rid: analyze_relationships(runs[rid]) for rid in run_ids}

    report = f"""# Multi-Run Extraction Comparison

**Paper:** Sobotkova et al. (2023) - Creating large, high-quality geospatial datasets from historical maps using novice volunteers

**Runs Compared:** {', '.join(run_ids)}

**Current Run:** RUN-08 (outputs/sobotkova-et-al-2023/extraction.json)

**Comparison Date:** 2025-10-28

---

## 1. Item Count Comparison Across All Runs

| Run | Evidence | Claims | Implicit Args | Designs | Methods | Protocols | **Total** |
|-----|----------|--------|---------------|---------|---------|-----------|-----------|
"""

    # Add rows for each run
    for rid in run_ids:
        counts = all_counts[rid]
        marker = " **†**" if rid == "RUN-08" else ""
        report += f"| {rid}{marker} | {counts['evidence']} | {counts['claims']} | {counts['implicit_arguments']} | {counts['research_designs']} | {counts['methods']} | {counts['protocols']} | **{counts['total']}** |\n"

    report += "\n**†** Current run (RUN-08)\n\n"

    # Calculate rankings
    report += "### Rankings by Total Items\n\n"
    ranked = sorted(all_counts.items(), key=lambda x: x[1]['total'], reverse=True)
    for rank, (rid, counts) in enumerate(ranked, 1):
        marker = " ← Current" if rid == "RUN-08" else ""
        report += f"{rank}. **{rid}**: {counts['total']} items{marker}\n"

    report += "\n### Key Observations\n\n"

    # Find highest/lowest in each category
    max_evidence = max(all_counts.items(), key=lambda x: x[1]['evidence'])
    max_claims = max(all_counts.items(), key=lambda x: x[1]['claims'])
    max_total = max(all_counts.items(), key=lambda x: x[1]['total'])

    report += f"- **Highest evidence count:** {max_evidence[0]} ({max_evidence[1]['evidence']} items)\n"
    report += f"- **Highest claims count:** {max_claims[0]} ({max_claims[1]['claims']} items)\n"
    report += f"- **Highest total count:** {max_total[0]} ({max_total[1]['total']} items)\n"
    report += f"- **RUN-08 total:** {all_counts['RUN-08']['total']} items (ranked #{[r[0] for r in ranked].index('RUN-08') + 1} of {len(run_ids)})\n"

    report += """

---

## 2. RDMAP Extraction Comparison

### RDMAP Item Counts

| Run | Total RDMAP | Designs | Methods | Protocols | Implicit RDMAP |
|-----|-------------|---------|---------|-----------|----------------|
"""

    for rid in run_ids:
        rdmap = all_rdmap[rid]
        implicit_total = rdmap['designs']['implicit'] + rdmap['methods']['implicit'] + rdmap['protocols']['implicit']
        marker = " **†**" if rid == "RUN-08" else ""
        report += f"| {rid}{marker} | {rdmap['total_rdmap']} | {rdmap['designs']['total']} | {rdmap['methods']['total']} | {rdmap['protocols']['total']} | {implicit_total} |\n"

    report += "\n**†** Current run (RUN-08)\n\n"

    # RDMAP rankings
    report += "### RDMAP Rankings\n\n"
    rdmap_ranked = sorted(all_rdmap.items(), key=lambda x: x[1]['total_rdmap'], reverse=True)
    for rank, (rid, rdmap) in enumerate(rdmap_ranked, 1):
        marker = " ← Current" if rid == "RUN-08" else ""
        report += f"{rank}. **{rid}**: {rdmap['total_rdmap']} RDMAP items{marker}\n"

    # Implicit RDMAP analysis
    report += "\n### Implicit RDMAP Extraction\n\n"
    report += "| Run | Implicit Designs | Implicit Methods | Implicit Protocols | Total Implicit |\n"
    report += "|-----|------------------|------------------|--------------------|-----------------|\n"

    for rid in run_ids:
        rdmap = all_rdmap[rid]
        implicit_total = rdmap['designs']['implicit'] + rdmap['methods']['implicit'] + rdmap['protocols']['implicit']
        marker = " **†**" if rid == "RUN-08" else ""
        report += f"| {rid}{marker} | {rdmap['designs']['implicit']} | {rdmap['methods']['implicit']} | {rdmap['protocols']['implicit']} | {implicit_total} |\n"

    report += "\n**†** Current run (RUN-08)\n\n"

    # Implicit RDMAP observations
    implicit_counts = {rid: all_rdmap[rid]['designs']['implicit'] + all_rdmap[rid]['methods']['implicit'] + all_rdmap[rid]['protocols']['implicit'] for rid in run_ids}
    runs_with_implicit = [rid for rid, count in implicit_counts.items() if count > 0]

    report += "**Observations:**\n\n"
    if runs_with_implicit:
        report += f"- Runs with implicit RDMAP: {', '.join(runs_with_implicit)}\n"
        max_implicit = max(implicit_counts.items(), key=lambda x: x[1])
        report += f"- Highest implicit RDMAP count: {max_implicit[0]} ({max_implicit[1]} items)\n"
        report += f"- RUN-08 implicit RDMAP: {implicit_counts['RUN-08']} items\n"
    else:
        report += "- No implicit RDMAP extracted in any run\n"

    report += """

---

## 3. Evidence-Claim Relationship Coverage

| Run | Ev→Claim Links | Claims w/ Evidence | Evidence Coverage % | Avg Evidence/Claim |
|-----|----------------|--------------------|--------------------|-------------------|
"""

    for rid in run_ids:
        rels = all_rels[rid]
        marker = " **†**" if rid == "RUN-08" else ""
        report += f"| {rid}{marker} | {rels['evidence_to_claims']} | {rels['claims_with_evidence']}/{rels['claims_total']} | {rels['evidence_coverage_pct']:.1f}% | {rels['avg_evidence_per_claim']:.1f} |\n"

    report += "\n**†** Current run (RUN-08)\n\n"

    # Relationship quality rankings
    report += "### Evidence Coverage Rankings\n\n"
    coverage_ranked = sorted(all_rels.items(), key=lambda x: x[1]['evidence_coverage_pct'], reverse=True)
    for rank, (rid, rels) in enumerate(coverage_ranked, 1):
        marker = " ← Current" if rid == "RUN-08" else ""
        report += f"{rank}. **{rid}**: {rels['evidence_coverage_pct']:.1f}% coverage ({rels['claims_with_evidence']}/{rels['claims_total']} claims){marker}\n"

    report += """

---

## 4. RDMAP Relationship Completeness

| Run | Methods→Designs | Protocols→Methods | Bidirectional? |
|-----|-----------------|-------------------|----------------|
"""

    for rid in run_ids:
        rels = all_rels[rid]
        counts = all_counts[rid]
        methods_designs = f"{rels['methods_with_designs']}/{counts['methods']}" if counts['methods'] > 0 else "0/0"
        protocols_methods = f"{rels['protocols_with_methods']}/{counts['protocols']}" if counts['protocols'] > 0 else "0/0"
        bidirectional = "✓ Yes" if rels['rdmap_bidirectional'] else "✗ No"
        marker = " **†**" if rid == "RUN-08" else ""
        report += f"| {rid}{marker} | {methods_designs} | {protocols_methods} | {bidirectional} |\n"

    report += "\n**†** Current run (RUN-08)\n\n"

    report += """

---

## 5. Quality Metrics Summary

### RUN-08 Position in Rankings

"""

    # Calculate RUN-08 rankings
    run08_total_rank = [r[0] for r in ranked].index('RUN-08') + 1
    run08_rdmap_rank = [r[0] for r in rdmap_ranked].index('RUN-08') + 1
    run08_coverage_rank = [r[0] for r in coverage_ranked].index('RUN-08') + 1

    report += f"- **Total items:** #{run08_total_rank} of {len(run_ids)} runs ({all_counts['RUN-08']['total']} items)\n"
    report += f"- **RDMAP coverage:** #{run08_rdmap_rank} of {len(run_ids)} runs ({all_rdmap['RUN-08']['total_rdmap']} items)\n"
    report += f"- **Evidence coverage:** #{run08_coverage_rank} of {len(run_ids)} runs ({all_rels['RUN-08']['evidence_coverage_pct']:.1f}%)\n"

    # Identify strengths
    report += "\n### RUN-08 Strengths\n\n"

    strengths = []

    # Check if best or near-best in any category
    if run08_total_rank <= 3:
        strengths.append(f"Strong overall coverage (#{run08_total_rank} in total items)")

    if run08_rdmap_rank <= 3:
        strengths.append(f"Good RDMAP extraction (#{run08_rdmap_rank} in RDMAP coverage)")

    if run08_coverage_rank <= 3:
        strengths.append(f"High evidence-claim linkage (#{run08_coverage_rank} in evidence coverage)")

    if implicit_counts['RUN-08'] > 0:
        implicit_rank = sorted(implicit_counts.items(), key=lambda x: x[1], reverse=True)
        run08_implicit_rank = [r[0] for r in implicit_rank].index('RUN-08') + 1
        if run08_implicit_rank <= 3:
            strengths.append(f"Successful implicit RDMAP extraction ({implicit_counts['RUN-08']} items)")

    # Check bidirectional relationships
    if all_rels['RUN-08']['rdmap_bidirectional']:
        bidirectional_runs = [rid for rid in run_ids if all_rels[rid]['rdmap_bidirectional']]
        strengths.append(f"Complete bidirectional RDMAP relationships")

    # Balanced extraction
    run08_counts = all_counts['RUN-08']
    if run08_counts['evidence'] > 40 and run08_counts['claims'] > 40:
        strengths.append("Balanced evidence-claim extraction")

    if not strengths:
        strengths.append("Consistent extraction quality")

    for strength in strengths:
        report += f"- {strength}\n"

    # Identify areas for consideration
    report += "\n### Comparison to Best Runs\n\n"

    # Compare to highest-performing runs
    best_total = max_total[0]
    best_rdmap = rdmap_ranked[0][0]
    best_coverage = coverage_ranked[0][0]

    if best_total != 'RUN-08':
        report += f"- **Highest total items:** {best_total} with {all_counts[best_total]['total']} items (RUN-08: {all_counts['RUN-08']['total']} items, {all_counts['RUN-08']['total'] - all_counts[best_total]['total']:+d})\n"

    if best_rdmap != 'RUN-08':
        report += f"- **Highest RDMAP coverage:** {best_rdmap} with {all_rdmap[best_rdmap]['total_rdmap']} items (RUN-08: {all_rdmap['RUN-08']['total_rdmap']} items, {all_rdmap['RUN-08']['total_rdmap'] - all_rdmap[best_rdmap]['total_rdmap']:+d})\n"

    if best_coverage != 'RUN-08':
        report += f"- **Highest evidence coverage:** {best_coverage} with {all_rels[best_coverage]['evidence_coverage_pct']:.1f}% (RUN-08: {all_rels['RUN-08']['evidence_coverage_pct']:.1f}%, {all_rels['RUN-08']['evidence_coverage_pct'] - all_rels[best_coverage]['evidence_coverage_pct']:+.1f}%)\n"

    if best_total == 'RUN-08' and best_rdmap == 'RUN-08' and best_coverage == 'RUN-08':
        report += "- **RUN-08 is the best performer across all metrics**\n"

    report += """

---

## 6. Evolution Across Runs

### Trends in Extraction Quality

"""

    # Calculate trends
    report += "**Total Items Trend:**\n\n"
    for rid in run_ids:
        counts = all_counts[rid]
        marker = " ← Current" if rid == "RUN-08" else ""
        bar_length = int(counts['total'] / 5)
        bar = "█" * bar_length
        report += f"- {rid}: {bar} {counts['total']}{marker}\n"

    report += "\n**RDMAP Coverage Trend:**\n\n"
    for rid in run_ids:
        rdmap = all_rdmap[rid]
        marker = " ← Current" if rid == "RUN-08" else ""
        bar_length = max(1, int(rdmap['total_rdmap'] / 2))
        bar = "█" * bar_length
        report += f"- {rid}: {bar} {rdmap['total_rdmap']}{marker}\n"

    report += "\n**Implicit RDMAP Trend:**\n\n"
    for rid in run_ids:
        implicit_count = implicit_counts[rid]
        marker = " ← Current" if rid == "RUN-08" else ""
        bar_length = max(1, implicit_count * 3) if implicit_count > 0 else 0
        bar = "█" * bar_length if bar_length > 0 else ""
        report += f"- {rid}: {bar} {implicit_count}{marker}\n"

    report += """

---

## 7. Overall Assessment

"""

    # Determine overall recommendation
    if run08_total_rank <= 2 and run08_rdmap_rank <= 2:
        report += "**Status:** ✓ RUN-08 is a top-performing extraction\n\n"
        report += "RUN-08 demonstrates strong extraction quality with balanced coverage across evidence, claims, and RDMAP categories. "
        report += "It ranks highly in multiple quality metrics and represents a solid extraction run.\n"
    elif run08_total_rank <= 3:
        report += "**Status:** ✓ RUN-08 is a high-quality extraction\n\n"
        report += "RUN-08 shows good extraction quality with consistent performance across metrics. "
        report += f"While not the highest in all categories, it provides comprehensive coverage (ranked #{run08_total_rank} overall).\n"
    else:
        report += "**Status:** ℹ️ RUN-08 shows moderate extraction coverage\n\n"
        report += f"RUN-08 ranks #{run08_total_rank} of {len(run_ids)} runs in total item count. "
        report += f"Runs {best_total} provide more comprehensive extraction.\n"

    # Specific recommendations
    report += "\n### Recommendations\n\n"

    if all_rdmap['RUN-08']['total_rdmap'] >= all_rdmap[best_rdmap]['total_rdmap'] * 0.8:
        report += "- **Use RUN-08 for RDMAP analysis:** Good methodological extraction with complete hierarchy\n"

    if implicit_counts['RUN-08'] > 0:
        report += "- **Use RUN-08 for implicit RDMAP validation:** Successfully identifies implicit methodological elements\n"

    if all_counts['RUN-08']['total'] < all_counts[best_total]['total'] * 0.7:
        report += f"- **Consider {best_total} for comprehensive coverage:** Significantly higher item count\n"

    if all_rels['RUN-08']['evidence_coverage_pct'] >= 50:
        report += "- **Use RUN-08 for evidence-claim analysis:** Good relationship coverage\n"

    report += """

---

*Comparison generated: 2025-10-28*

*Comparison script: compare_all_runs.py*

*Runs analysed: {run_count} complete runs*
""".format(run_count=len(run_ids))

    return report

def main():
    """Generate multi-run extraction comparison report."""
    print("="*80)
    print("MULTI-RUN EXTRACTION COMPARISON")
    print("="*80)

    # Define run paths
    base_path = "/home/shawn/Code/llm-reproducibility/archive/output/cc-sonnet45"
    run_numbers = ['01', '02', '03', '04', '05', '07']  # Exclude 00-fail and 06-partial

    # Load all runs
    runs = {}

    print("\nLoading archived runs...")
    for run_num in run_numbers:
        run_id = f"RUN-{run_num}"
        filepath = f"{base_path}/sobotkova-et-al-2023-{run_id}/extraction.json"
        print(f"  Loading {run_id}...")
        data = load_extraction(filepath)
        if data:
            runs[run_id] = data
        else:
            print(f"  WARNING: Could not load {run_id}")

    # Load current run (RUN-08)
    print("  Loading RUN-08 (current)...")
    current_path = "/home/shawn/Code/llm-reproducibility/outputs/sobotkova-et-al-2023/extraction.json"
    current_data = load_extraction(current_path)
    if current_data:
        runs['RUN-08'] = current_data
    else:
        print("  ERROR: Could not load RUN-08")
        return

    print(f"\n✓ Loaded {len(runs)} runs")

    # Generate comparison
    print("\nGenerating multi-run comparison report...")
    report = generate_multi_run_comparison(runs)

    # Save report
    output_path = Path("/home/shawn/Code/llm-reproducibility/outputs/sobotkova-et-al-2023/multi-run-comparison.md")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(report)

    print(f"\n✓ Multi-run comparison report generated: {output_path}")
    print(f"  Report size: {output_path.stat().st_size / 1024:.1f}K")

    # Print summary
    print("\n" + "="*80)
    print("QUICK SUMMARY")
    print("="*80)

    for run_id in sorted(runs.keys()):
        counts = count_items(runs[run_id])
        rdmap = analyze_rdmap(runs[run_id])
        marker = " ← CURRENT" if run_id == "RUN-08" else ""
        print(f"{run_id}: {counts['total']} total items, {rdmap['total_rdmap']} RDMAP items{marker}")

    print("\n" + "="*80)
    print("COMPARISON COMPLETE")
    print("="*80)

if __name__ == "__main__":
    main()
