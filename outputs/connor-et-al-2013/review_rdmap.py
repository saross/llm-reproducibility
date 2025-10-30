#!/usr/bin/env python3
"""
Temporary script to review RDMAP items for Pass 5 rationalization analysis.
Extracts all RDMAP items with their IDs, content, and relationships.
"""

import json

with open('/home/shawn/Code/llm-reproducibility/outputs/connor-et-al-2013/extraction.json', 'r') as f:
    data = json.load(f)

print("=" * 80)
print("CONNOR ET AL. 2013 - RDMAP REVIEW FOR PASS 5 RATIONALIZATION")
print("=" * 80)
print()

print(f"Current RDMAP Counts:")
print(f"  Research Designs: {len(data['research_designs'])}")
print(f"  Methods: {len(data['methods'])}")
print(f"  Protocols: {len(data['protocols'])}")
print(f"  Total: {len(data['research_designs']) + len(data['methods']) + len(data['protocols'])}")
print()

print("=" * 80)
print("RESEARCH DESIGNS (WHY)")
print("=" * 80)
for rd in data['research_designs']:
    status = rd.get('design_status', 'explicit')
    print(f"\n{rd['id']} [{status}]:")
    print(f"  Content: {rd['content']}")
    if 'supported_by_methods' in rd and rd['supported_by_methods']:
        print(f"  Methods: {', '.join(rd['supported_by_methods'])}")

print()
print("=" * 80)
print("METHODS (WHAT)")
print("=" * 80)
for m in data['methods']:
    status = m.get('method_status', 'explicit')
    print(f"\n{m['id']} [{status}]:")
    print(f"  Content: {m['content']}")
    if 'implemented_by_protocols' in m and m['implemented_by_protocols']:
        print(f"  Protocols: {', '.join(m['implemented_by_protocols'])}")
    if 'supports_design' in m and m['supports_design']:
        print(f"  Supports: {m['supports_design']}")

print()
print("=" * 80)
print("PROTOCOLS (HOW)")
print("=" * 80)
for p in data['protocols']:
    status = p.get('protocol_status', 'explicit')
    print(f"\n{p['id']} [{status}]:")
    print(f"  Content: {p['content']}")
    if 'implements_methods' in p and p['implements_methods']:
        print(f"  Implements: {', '.join(p['implements_methods'])}")
    elif 'implements_method' in p and p['implements_method']:
        print(f"  Implements: {p['implements_method']}")

print()
print("=" * 80)
print("END OF RDMAP REVIEW")
print("=" * 80)
