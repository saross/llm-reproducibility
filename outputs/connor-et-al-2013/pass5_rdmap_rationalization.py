#!/usr/bin/env python3
"""
Pass 5: RDMAP Rationalization
Connor et al. 2013 - Environmental conditions in the SE Balkans since the Last Glacial Maximum

Target: Conservative 5-10% reduction (4-8 items from 80)
Current: 9 designs, 25 methods, 46 protocols = 80 total RDMAP items
Expected: ~72-76 items after rationalization

Consolidation strategy:
- Sequential workflow steps within same analytical chain
- Implicit protocols redundant with explicit counterparts
- Specific case methods absorbed into general methods
- Sample preparation procedures combined

Preservation principles:
- Distinct proxy types (pollen, charcoal, magnetic susceptibility, NPPs)
- Distinct analytical approaches (DCA, cluster, indicator species)
- Distinct chronological methods (AMS vs age-depth modelling)
- Quality control vs primary analysis procedures
"""

import json
from datetime import datetime, timezone

# Load extraction
with open('/home/shawn/Code/llm-reproducibility/outputs/connor-et-al-2013/extraction.json', 'r') as f:
    data = json.load(f)

print("=" * 80)
print("PASS 5: RDMAP RATIONALIZATION - Connor et al. 2013")
print("=" * 80)
print(f"Starting RDMAP counts:")
print(f"  Research Designs: {len(data['research_designs'])}")
print(f"  Methods: {len(data['methods'])}")
print(f"  Protocols: {len(data['protocols'])}")
print(f"  Total RDMAP: {len(data['research_designs']) + len(data['methods']) + len(data['protocols'])}")
print()

before_counts = {
    'designs': len(data['research_designs']),
    'methods': len(data['methods']),
    'protocols': len(data['protocols']),
    'total': len(data['research_designs']) + len(data['methods']) + len(data['protocols'])
}

# =============================================================================
# RESEARCH DESIGNS - Review for consolidation
# =============================================================================
print("Research Designs: Reviewing for overlaps...")
print("  All 9 designs describe distinct aspects:")
print("  - RD001-RD007: Explicit research design components")
print("  - RD008-RD009: Implicit integration and selection strategies")
print("  No consolidation opportunities - all represent distinct WHY rationales")
print()

# =============================================================================
# METHODS - Consolidations
# =============================================================================
print("Methods: Identifying consolidation opportunities...")

methods_to_remove = []
consolidations = []

# CONSOLIDATION 1: M016 (Pollen concentrate dating) → M015 (AMS dating)
print("  CONS-01: M016 → M015 (pollen concentrate dating is specific case of AMS dating)")
for method in data['methods']:
    if method['id'] == "M015":
        # Update to encompass pollen concentrate dating
        old_content = method['content']
        method['content'] = "Radiocarbon dating using Accelerator Mass Spectrometer (AMS) on multiple sample types including pollen concentrates, organic residues, and macrobotanical material"
        method['consolidation_note'] = "Pass 5: Consolidated M016 (pollen concentrate dating) as specific application of AMS dating method"
        # Add P024 to implemented_by_protocols if M016 had it
        if 'implemented_by_protocols' not in method:
            method['implemented_by_protocols'] = []
        if 'P024' not in method['implemented_by_protocols']:
            method['implemented_by_protocols'].append('P024')

methods_to_remove.append('M016')
consolidations.append("M016 → M015: Pollen concentrate dating is specific application of general AMS method")

# Update protocols that implement M016 to implement M015
for protocol in data['protocols']:
    if 'implements_methods' in protocol:
        if 'M016' in protocol['implements_methods']:
            protocol['implements_methods'] = ['M015' if m == 'M016' else m for m in protocol['implements_methods']]
    elif 'implements_method' in protocol:
        if protocol['implements_method'] == 'M016':
            protocol['implements_method'] = 'M015'

# CONSOLIDATION 2: M018 (Linear extrapolation) → M017 (Bayesian age-depth modelling)
print("  CONS-02: M018 → M017 (extrapolation is extension step of age-depth model construction)")
for method in data['methods']:
    if method['id'] == "M017":
        old_content = method['content']
        method['content'] = "Bayesian age-depth modelling using Markov chain Monte-Carlo analysis in OxCal, extended by linear extrapolation to cover intervals beyond dated samples"
        if 'consolidation_note' not in method:
            method['consolidation_note'] = ""
        else:
            method['consolidation_note'] += "; "
        method['consolidation_note'] += "Pass 5: Consolidated M018 (linear extrapolation) as procedural extension of age-depth modelling"
        # Add P027 to protocols
        if 'implemented_by_protocols' not in method:
            method['implemented_by_protocols'] = []
        if 'P027' not in method['implemented_by_protocols']:
            method['implemented_by_protocols'].append('P027')

methods_to_remove.append('M018')
consolidations.append("M018 → M017: Linear extrapolation is sequential step in age-depth model construction")

# Update protocols that implement M018 to implement M017
for protocol in data['protocols']:
    if 'implements_methods' in protocol:
        if 'M018' in protocol['implements_methods']:
            protocol['implements_methods'] = ['M017' if m == 'M018' else m for m in protocol['implements_methods']]
    elif 'implements_method' in protocol:
        if protocol['implements_method'] == 'M018':
            protocol['implements_method'] = 'M017'

# CONSOLIDATION 3: M025 (implicit visualization) → M010 (Psimpoll visualization)
print("  CONS-03: M025 → M010 (implicit visualization methodology merged into explicit Psimpoll method)")
for method in data['methods']:
    if method['id'] == "M010":
        method['content'] = "Pollen diagram visualization using Psimpoll software with graphic design choices for exaggeration factors, color schemes, grouping, and axis scaling"
        if 'consolidation_note' not in method:
            method['consolidation_note'] = ""
        else:
            method['consolidation_note'] += "; "
        method['consolidation_note'] += "Pass 5: Consolidated M025 (implicit visualization methodology) into explicit Psimpoll method"

methods_to_remove.append('M025')
consolidations.append("M025 → M010: Implicit visualization design methodology absorbed into explicit software method")

# Update RD008 if it references M025 (actually, it doesn't based on output, but check anyway)
for design in data['research_designs']:
    if design['id'] == 'RD008' and 'supported_by_methods' in design:
        if 'M025' in design['supported_by_methods']:
            design['supported_by_methods'] = ['M010' if m == 'M025' else m for m in design['supported_by_methods']]

# Remove consolidated methods
data['methods'] = [m for m in data['methods'] if m['id'] not in methods_to_remove]
print(f"  Methods consolidated: {len(methods_to_remove)}")
print()

# =============================================================================
# PROTOCOLS - Consolidations
# =============================================================================
print("Protocols: Identifying consolidation opportunities...")

protocols_to_remove = []

# CONSOLIDATION 4: P024 + P025 → P024 (dating sample preparation workflow)
print("  CONS-04: P025 → P024 (organic residue pre-treatment merged with pollen concentrate extraction)")
for protocol in data['protocols']:
    if protocol['id'] == "P024":
        protocol['content'] = "Sample preparation for AMS radiocarbon dating: pollen concentrate extraction using Brown et al. (1989) procedure (for samples lacking macrobotanicals), and organic residue pre-treatment involving rootlet removal and acid washing in dilute HCl"
        if 'verbatim_quote' in protocol:
            # Keep existing quote but note consolidation
            pass
        protocol['consolidation_note'] = "Pass 5: Consolidated P025 (organic residue pre-treatment) into comprehensive dating sample preparation protocol"

protocols_to_remove.append('P025')
consolidations.append("P025 → P024: Both are dating sample preparation procedures, consolidated into comprehensive protocol")

# CONSOLIDATION 5: P034 (Calibration) → P026 (Bayesian modelling in OxCal)
print("  CONS-05: P034 → P026 (calibration using IntCal09 is part of OxCal Bayesian modelling)")
for protocol in data['protocols']:
    if protocol['id'] == "P026":
        protocol['content'] = "OxCal 4.1.7 Bayesian age-depth modelling using Markov chain Monte-Carlo analysis with IntCal09 calibration curve (also calibrated using Calib 6.02 for consistency)"
        if 'consolidation_note' not in protocol:
            protocol['consolidation_note'] = ""
        else:
            protocol['consolidation_note'] += "; "
        protocol['consolidation_note'] += "Pass 5: Consolidated P034 (IntCal09 calibration in Calib 6.02) as calibration is integral to OxCal Bayesian procedure"

protocols_to_remove.append('P034')
consolidations.append("P034 → P026: Radiocarbon calibration is procedural component of Bayesian age-depth modelling")

# CONSOLIDATION 6: P035 (implicit counting stopping rules) → P007 (explicit counting thresholds)
print("  CONS-06: P035 → P007 (implicit stopping rules merged into explicit counting threshold protocol)")
for protocol in data['protocols']:
    if protocol['id'] == "P007":
        protocol['content'] = "Pollen counting thresholds and stopping rules: minimum 200, average 600 terrestrial pollen per sample, with decision rules for when to stop at minimum vs. continue to average count based on assemblage diversity"
        if 'consolidation_note' not in protocol:
            protocol['consolidation_note'] = ""
        else:
            protocol['consolidation_note'] += "; "
        protocol['consolidation_note'] += "Pass 5: Consolidated P035 (implicit stopping rules) into explicit counting threshold protocol"
        # Update status note
        if 'protocol_status' in protocol:
            protocol['protocol_status'] = 'explicit with implicit details'

protocols_to_remove.append('P035')
consolidations.append("P035 → P007: Implicit counting stopping rules absorbed into explicit threshold protocol")

# CONSOLIDATION 7: P036 (implicit Lycopodium specs) → P004 (explicit Lycopodium addition)
print("  CONS-07: P036 → P004 (implicit Lycopodium tablet specifications merged into explicit protocol)")
for protocol in data['protocols']:
    if protocol['id'] == "P004":
        protocol['content'] = "Pollen subsample extraction: 1 cm³ subsamples combined with Lycopodium spore tablets (University of Lund) at specified concentration and addition volume for concentration calculation"
        if 'consolidation_note' not in protocol:
            protocol['consolidation_note'] = ""
        else:
            protocol['consolidation_note'] += "; "
        protocol['consolidation_note'] += "Pass 5: Consolidated P036 (implicit Lycopodium tablet concentration/volume specifications) into explicit Lycopodium addition protocol"
        if 'protocol_status' in protocol:
            protocol['protocol_status'] = 'explicit with implicit details'

protocols_to_remove.append('P036')
consolidations.append("P036 → P004: Implicit Lycopodium specifications absorbed into explicit addition protocol")

# CONSOLIDATION 8: P046 (implicit sampling interval rationale) → P002 (explicit variable sampling)
print("  CONS-08: P046 → P002 (implicit interval selection rationale merged into explicit variable sampling protocol)")
for protocol in data['protocols']:
    if protocol['id'] == "P002":
        protocol['content'] = "Variable resolution sampling strategy: 5-cm intervals to 140 cm depth (higher resolution for recent sediments), then 20-cm intervals to bottom (maintaining coverage while balancing temporal resolution and practical constraints)"
        if 'consolidation_note' not in protocol:
            protocol['consolidation_note'] = ""
        else:
            protocol['consolidation_note'] += "; "
        protocol['consolidation_note'] += "Pass 5: Consolidated P046 (implicit sampling interval rationale) into explicit variable sampling protocol"
        if 'protocol_status' in protocol:
            protocol['protocol_status'] = 'explicit with implicit details'

protocols_to_remove.append('P046')
consolidations.append("P046 → P002: Implicit sampling interval justification absorbed into explicit variable sampling protocol")

# Remove consolidated protocols
data['protocols'] = [p for p in data['protocols'] if p['id'] not in protocols_to_remove]
print(f"  Protocols consolidated: {len(protocols_to_remove)}")
print()

# =============================================================================
# UPDATE METADATA AND SAVE
# =============================================================================

after_counts = {
    'designs': len(data['research_designs']),
    'methods': len(data['methods']),
    'protocols': len(data['protocols']),
    'total': len(data['research_designs']) + len(data['methods']) + len(data['protocols'])
}

reduction_count = before_counts['total'] - after_counts['total']
reduction_pct = (reduction_count / before_counts['total']) * 100

data['extraction_timestamp'] = datetime.now(timezone.utc).isoformat()

data['extraction_notes']['pass5_rdmap_rationalization'] = {
    'completion_date': datetime.now(timezone.utc).isoformat(),
    'approach': 'Conservative consolidation for multi-proxy palaeoenvironmental paper',
    'before': before_counts,
    'after': after_counts,
    'reductions': {
        'designs': 0,
        'methods': len([c for c in consolidations if '→ M' in c or '→ RD' in c.split(':')[0]]),
        'protocols': len([c for c in consolidations if '→ P' in c]),
        'total': reduction_count
    },
    'reduction_percentage': round(reduction_pct, 1),
    'consolidations': consolidations,
    'rationale': 'Palaeoenvironmental paper with well-differentiated proxy methods. Conservative 10.0% reduction merges sequential workflow steps, absorbs specific-case methods into general methods, and integrates implicit protocol specifications into explicit counterparts while preserving distinct analytical approaches for pollen, charcoal, magnetic susceptibility, and NPP analyses.'
}

with open('/home/shawn/Code/llm-reproducibility/outputs/connor-et-al-2013/extraction.json', 'w') as f:
    json.dump(data, f, indent=2)

print("=" * 80)
print("PASS 5 COMPLETE - RDMAP RATIONALIZATION")
print("=" * 80)
print(f"Final RDMAP counts:")
print(f"  Research Designs: {after_counts['designs']} (no change)")
print(f"  Methods: {after_counts['methods']} (reduced from {before_counts['methods']})")
print(f"  Protocols: {after_counts['protocols']} (reduced from {before_counts['protocols']})")
print(f"  Total RDMAP: {after_counts['total']} (reduced from {before_counts['total']})")
print()
print(f"Reduction: {reduction_count} items ({round(reduction_pct, 1)}%)")
print()
print(f"Total extraction items: {len(data['evidence']) + len(data['claims']) + len(data['implicit_arguments']) + after_counts['total']}")
print()
print("Consolidations performed:")
for i, cons in enumerate(consolidations, 1):
    print(f"  {i}. {cons}")
print()
print("=" * 80)
print("Ready for Pass 6: Validation")
print("=" * 80)
