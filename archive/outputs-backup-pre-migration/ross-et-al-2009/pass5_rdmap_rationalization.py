#!/usr/bin/env python3
"""
Pass 5: RDMAP Rationalization
Ross et al. 2009 - Remote Sensing and Archaeological Prospection in Apulia, Italy

Target: 15-20% reduction through consolidation
Current: 4 designs, 13 methods, 28 protocols = 45 total
Expectation: Conservative consolidation for well-differentiated technical paper

Review areas:
- Protocol consolidations (band combination procedures, georeferencing steps)
- Method consolidations (overlapping analytical approaches)
- Research designs appear distinct - unlikely consolidation
"""

import json
from datetime import datetime, timezone
from pathlib import Path

extraction_file = Path("extraction.json")
with open(extraction_file) as f:
    data = json.load(f)

print("=" * 70)
print("PASS 5: RDMAP RATIONALIZATION")
print("=" * 70)
print(f"Starting RDMAP counts:")
print(f"  - Research Designs: {len(data['research_designs'])}")
print(f"  - Methods: {len(data['methods'])}")
print(f"  - Protocols: {len(data['protocols'])}")
print(f"  - Total RDMAP: {len(data['research_designs']) + len(data['methods']) + len(data['protocols'])}")
print()

# =================================================================
# RESEARCH DESIGNS - Review for consolidation
# =================================================================
print("Research Designs: Reviewing for overlaps...")
print("  All 4 designs describe distinct aspects:")
print("  - RD001: Integrated multi-method approach")
print("  - RD002: Comparative evaluation design")
print("  - RD003: Iterative feedback design")
print("  - RD004: Blind interpretation control")
print("  No consolidation opportunities - keeping all 4")
print()

# =================================================================
# METHODS - Check for consolidations
# =================================================================
print("Methods: Analyzing for consolidation...")

# Consolidate M010 (manual band recombination) and M011 (NDVI)
# into comprehensive spectral analysis method
print("  CONSOLIDATING: M010 + M011 → M010 (spectral analysis method)")

methods_to_remove = ["M011"]

for method in data['methods']:
    if method['method_id'] == "M010":
        method['content'] = "Spectral analysis combining manual band recombination (emphasizing red/NIR) with NDVI transformation for vegetation assessment"
        method['verbatim_quote'] = "Our analysis began with band combinations prioritizing red and NIR, as they best reveal differences in vegetation growth sometimes associated with subsurface archaeological remains. Contrasts between high NIR values (healthy vegetation) and high red values (stressed vegetation) were sought primarily through manual band recombination... The results of manual band recombination were then supplemented with transformations such as NDVI"
        method['child_protocols'] = ["P018", "P019", "P020"]  # Add P020 from M011
        method['consolidation_note'] = "Pass 5: Consolidated M011 (NDVI method) into comprehensive spectral analysis method"

# Update protocols that implement M011 to now implement M010
for protocol in data['protocols']:
    if protocol.get('implements_method') == "M011":
        protocol['implements_method'] = "M010"

data['methods'] = [m for m in data['methods'] if m['method_id'] not in methods_to_remove]
print()

# =================================================================
# PROTOCOLS - Check for consolidations
# =================================================================
print("Protocols: Analyzing for consolidation...")

protocols_to_remove = []

# Consolidate P002 + P003 (georeferencing + projection) into P021
print("  CONSOLIDATING: P002 + P003 → P021 (comprehensive georeferencing)")

for protocol in data['protocols']:
    if protocol['protocol_id'] == "P021":
        protocol['content'] = "Comprehensive georeferencing and projection: using ground control points to improve RMSE from 14m to 3m, then projecting onto WGS 84, UTM 33N coordinate system"
        protocol['verbatim_quote'] = "Before georeferencing using ground control points, the image had a root mean square error (RMSE) of 14 m... After georeferencing by Samsung Lim, its accuracy was improved to an RMSE of approximately 3 m, an excellent result facilitated by the low off-nadir angle of the image. After georeferencing, the image was projected onto a local coordinate system (WGS 84, UTM 33N)"
        protocol['consolidation_note'] = "Pass 5: Consolidated P002 (georeferencing) and P003 (projection) into comprehensive procedure"

protocols_to_remove.extend(["P002", "P003"])

# Consolidate P005 + P019 (both describe same limited band combination set)
print("  CONSOLIDATING: P019 → P005 (redundant band combination procedure)")
protocols_to_remove.append("P019")

for protocol in data['protocols']:
    if protocol['protocol_id'] == "P005":
        protocol['consolidation_note'] = "Pass 5: P019 removed as redundant restatement of same band combination set (4-2-1; 4-1-2; 4-1-4)"

data['protocols'] = [p for p in data['protocols'] if p['protocol_id'] not in protocols_to_remove]
print()

print(f"Total RDMAP consolidations: {len(methods_to_remove)} methods + {len(protocols_to_remove)} protocols = {len(methods_to_remove) + len(protocols_to_remove)} items")
print()

# =================================================================
# UPDATE EXTRACTION FILE
# =================================================================

data['extraction_timestamp'] = datetime.now(timezone.utc).isoformat()

before_total = 45
after_total = len(data['research_designs']) + len(data['methods']) + len(data['protocols'])

data['extraction_notes']['pass5_rdmap_rationalization'] = {
    'completion_date': datetime.now(timezone.utc).isoformat(),
    'approach': 'Conservative consolidation for well-differentiated technical paper',
    'before': {
        'research_designs': 4,
        'methods': 13,
        'protocols': 28,
        'total_rdmap': 45
    },
    'after': {
        'research_designs': len(data['research_designs']),
        'methods': len(data['methods']),
        'protocols': len(data['protocols']),
        'total_rdmap': after_total
    },
    'reductions': {
        'methods': 1,
        'protocols': 3,
        'total': 4
    },
    'reduction_percentage': round((before_total - after_total) / before_total * 100, 1),
    'consolidations': [
        "M010 + M011 → M010 (spectral analysis combining manual band recombination and NDVI)",
        "P002 + P003 → P021 (comprehensive georeferencing and projection)",
        "P005 absorbed P019 (redundant band combination set specification)"
    ],
    'rationale': 'Technical methods paper with well-differentiated procedures. Conservative 8.9% reduction preserves distinct methodological steps. Each remaining RDMAP item describes unique procedure or design element.'
}

with open(extraction_file, 'w') as f:
    json.dump(data, f, indent=2)

print("=" * 70)
print("PASS 5 COMPLETE - RDMAP Rationalization")
print("=" * 70)
print(f"Final RDMAP counts:")
print(f"  - Research Designs: {len(data['research_designs'])} (no change)")
print(f"  - Methods: {len(data['methods'])} (reduced from 13)")
print(f"  - Protocols: {len(data['protocols'])} (reduced from 28)")
print(f"  - Total RDMAP: {after_total} (reduced from {before_total})")
print()
print(f"Reduction: {before_total - after_total} items ({data['extraction_notes']['pass5_rdmap_rationalization']['reduction_percentage']}%)")
print()
print(f"Total extraction: {len(data['evidence']) + len(data['claims']) + len(data['implicit_arguments']) + len(data['research_designs']) + len(data['methods']) + len(data['protocols'])} items")
print("=" * 70)
