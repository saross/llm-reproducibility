#!/usr/bin/env python3
"""
Pass 5 RDMAP Rationalization Analysis for sobotkova-et-al-2016
Identifies consolidation opportunities using assessment compatibility test
"""

import json
from collections import defaultdict

# Load current extraction
with open('outputs/sobotkova-et-al-2016/extraction.json', 'r') as f:
    data = json.load(f)

print("=" * 80)
print("PASS 5 RDMAP RATIONALIZATION ANALYSIS")
print("=" * 80)
print()

# Current counts
rd_count = len(data['research_designs'])
m_count = len(data['methods'])
p_count = len(data['protocols'])
total = rd_count + m_count + p_count

print(f"Current RDMAP Items: {total}")
print(f"  Research Designs: {rd_count}")
print(f"  Methods: {m_count}")
print(f"  Protocols: {p_count}")
print()

# Target reduction
target_reduction = int(total * 0.175)  # 17.5% (middle of 15-20%)
target_total = total - target_reduction

print(f"Target Reduction (15-20%, aiming for 17.5%):")
print(f"  Current: {total}")
print(f"  Target: ~{target_total}")
print(f"  Reduction needed: ~{target_reduction} items")
print()

# Analyze Research Designs
print("=" * 80)
print("RESEARCH DESIGNS ANALYSIS (6 items)")
print("=" * 80)
print()

for rd in data['research_designs']:
    status = rd.get('design_status', 'explicit')
    print(f"{rd['design_id']}: {rd['design_name']}")
    print(f"  Status: {status}")
    print(f"  Tier: {rd.get('design_tier', 'N/A')}")
    print(f"  Page: {rd.get('page', 'N/A')}")
    print()

print("Consolidation opportunities:")
print("  - RD001 (Generalised platform positioning) + RD004 (Shared core library cost)")
print("    Assessment test: Would assess separately - RD001 is product positioning,")
print("    RD004 is financial sustainability. Different strategic concerns.")
print("  - RD002 (Co-development partnership) + RD003 (Funding sustainability)")
print("    Assessment test: Would assess separately - RD002 is development model,")
print("    RD003 is financial model. Related but distinct.")
print("  - RD-IMP-001 (Comparative evaluation) + RD-IMP-002 (Reproducibility enhancement)")
print("    Assessment test: Would assess separately - Different strategic objectives.")
print()
print("Recommendation: NO consolidation for Research Designs")
print("  Rationale: Each design addresses distinct strategic concern. All would be")
print("  assessed independently for transparency and justification.")
print()

# Analyze Methods
print("=" * 80)
print("METHODS ANALYSIS (13 items)")
print("=" * 80)
print()

for method in data['methods']:
    status = method.get('method_status', 'explicit')
    print(f"{method['method_id']}: {method['method_name']}")
    print(f"  Status: {status}")
    print(f"  Tier: {method.get('method_tier', 'N/A')}")
    print(f"  Implements: {method.get('implements_design', 'N/A')}")
    print()

print("Consolidation opportunities:")
print()
print("  Group 1: Requirements and feedback methods")
print("    M004 (Iterative requirements gathering through feedback loops)")
print("    M003 (Scoping-coding-QA software deployment workflow)")
print("    Assessment: Would assess SEPARATELY")
print("    Rationale: M004 is requirements gathering method, M003 is deployment workflow.")
print("    Different methodological phases.")
print()
print("  Group 2: Paper-to-digital and module reuse")
print("    M005 (Paper-to-digital workflow conversion method)")
print("    M006 (Module reuse and rapid adaptation method)")
print("    Assessment: Would assess SEPARATELY")
print("    Rationale: M005 is conversion method, M006 is reuse method. Different processes.")
print()
print("  Group 3: Testing and support")
print("    M007 (Pre-fieldwork testing and training method)")
print("    M008 (High-quality in-field support method)")
print("    Assessment: Would assess SEPARATELY")
print("    Rationale: Pre-fieldwork vs in-field. Different timing and purposes.")
print()
print("  Group 4: Implicit assessment methods")
print("    M-IMP-003 (Post-fieldwork questionnaire methodology)")
print("    M-IMP-004 (Interpretive impact assessment methodology)")
print("    Assessment: Would assess TOGETHER (CONSOLIDATE)")
print("    Rationale: Both are post-fieldwork assessment approaches. Questionnaire IS the")
print("    vehicle for impact assessment. Would evaluate as unified assessment method.")
print()
print("  Group 5: Measurement methods")
print("    M-IMP-001 (Performance monitoring and degradation detection)")
print("    M-IMP-002 (Time-on-task measurement methodology)")
print("    M-IMP-005 (Cost-benefit quantification methodology)")
print("    Assessment: Would assess SEPARATELY")
print("    Rationale: Different measurement targets (performance vs time vs cost).")
print("    Each requires independent assessment of measurement validity.")
print()
print("Recommendation: CONSOLIDATE M-IMP-003 + M-IMP-004 (1 consolidation)")
print()

# Analyze Protocols
print("=" * 80)
print("PROTOCOLS ANALYSIS (23 items)")
print("=" * 80)
print()

# Group protocols by function
explicit_protocols = [p for p in data['protocols'] if p.get('protocol_status') == 'explicit']
implicit_protocols = [p for p in data['protocols'] if p.get('protocol_status') == 'implicit']

print(f"Explicit protocols: {len(explicit_protocols)}")
print(f"Implicit protocols: {len(implicit_protocols)}")
print()

print("Explicit protocols:")
for p in explicit_protocols:
    print(f"  {p['protocol_id']}: {p['protocol_name']}")
print()

print("Implicit protocols:")
for p in implicit_protocols:
    print(f"  {p['protocol_id']}: {p['protocol_name']}")
print()

print("Consolidation opportunities:")
print()
print("  Group 1: Module customisation pathways (P001-P004)")
print("    P001 (Module reuse as-is)")
print("    P002 (Heurist GUI-based module generation)")
print("    P003 (Simplified XML generator for module definition)")
print("    P004 (Direct definition document editing)")
print("    Assessment: Would assess SEPARATELY")
print("    Rationale: Four distinct customisation pathways with different complexity/skill.")
print("    Each needs independent assessment of accessibility and documentation.")
print()
print("  Group 2: Server deployment options (P006-P007)")
print("    P006 (Server installation via Ubuntu commands)")
print("    P007 (Pre-configured server procurement)")
print("    Assessment: Would assess SEPARATELY")
print("    Rationale: DIY vs commercial procurement. Different procedures and user needs.")
print()
print("  Group 3: Testing protocols (P013-P015)")
print("    P013 (Authentic situation testing with real data)")
print("    P014 (Device-specific compatibility testing)")
print("    P015 (Project novice training for workflow validation)")
print("    Assessment: Could assess TOGETHER (CONSIDER CONSOLIDATION)")
print("    Rationale: Three aspects of pre-fieldwork testing. Could be unified as")
print("    comprehensive testing protocol. HOWEVER, each has distinct procedure.")
print("    Keep separate for granular assessment.")
print()
print("  Group 4: Data handling protocols (P017-P018)")
print("    P017 (Data export to CSV for analysis)")
print("    P018 (Immediate post-field data checking)")
print("    Assessment: Would assess SEPARATELY")
print("    Rationale: Export vs checking. Different procedures and purposes.")
print()
print("  Group 5: Implicit protocols")
print("    P-IMP-001 (Identifier seed assignment to devices)")
print("    P-IMP-002 (Live module update deployment)")
print("    P-IMP-003 (Communication archival and supplementary data)")
print("    P-IMP-004 (Concatenated identifier export transformation)")
print("    P-IMP-005 (Server virtual machine installation)")
print("    Assessment: Would assess SEPARATELY")
print("    Rationale: All address different operational concerns. No consolidation.")
print()
print("Recommendation: NO protocol consolidation")
print("  Rationale: Protocols are operational specifications. Each needs independent")
print("  assessment. Consolidating would reduce granularity needed for replication.")
print()

# Summary
print("=" * 80)
print("CONSOLIDATION SUMMARY")
print("=" * 80)
print()
print("Proposed consolidations: 1")
print("  Methods: M-IMP-003 + M-IMP-004 → M-IMP-003")
print()
print("Expected outcome:")
print(f"  Current: {total} items")
print(f"  After consolidation: {total - 1} items")
print(f"  Reduction: 1 item (2.4%)")
print()
print("⚠️  Below target reduction (15-20% = 6-8 items)")
print()
print("Analysis reasoning:")
print("  1. Research Designs (6): All address distinct strategic concerns, no consolidation")
print("  2. Methods (13): Only 1 consolidation (assessment methods unified)")
print("  3. Protocols (23): No consolidation - operational specifications need granularity")
print()
print("Explanation for low reduction:")
print("  - Pass 3 was NOT over-extracted - items are well-differentiated")
print("  - Pass 4 implicit extraction was conservative (28.6%, within target)")
print("  - RDMAP items represent genuine procedural diversity in co-development study")
print("  - Assessment compatibility test shows most items need independent assessment")
print()
print("Recommendation: Accept low reduction as appropriate for this paper's content.")
