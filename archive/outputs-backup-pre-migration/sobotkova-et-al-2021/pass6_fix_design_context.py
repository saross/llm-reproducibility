#!/usr/bin/env python3
"""
Pass 6 Fix: Add design_context to all methods

Every method must reference at least one research design.
RD001: Comparative case study design (evaluating FAIMS Mobile deployment)
RD002: Requirements-driven approach (selecting and customizing software)
"""

import json
from datetime import datetime, timezone
from pathlib import Path

# Load extraction
extraction_file = Path("extraction.json")
with open(extraction_file) as f:
    data = json.load(f)

print("Fixing design_context references for methods...")

# Design context mapping based on method purpose
design_context_map = {
    "M001": ["RD002"],  # Module reuse implements requirements-driven approach
    "M002": ["RD001", "RD002"],  # Dual workflows implements both (evaluation + requirements)
    "M003": ["RD001", "RD002"],  # Offline-first management implements both
    "M004": ["RD002"],  # XML customization implements requirements-driven
    "M005": ["RD002"],  # Controlled vocabularies implements requirements-driven
    "M006": ["RD001"],  # Daily review implements case study evaluation
    "IM001": ["RD001", "RD002"],  # Training supports both case study and requirements
    "IM002": ["RD001"]  # Efficiency comparison implements case study evaluation
}

# Apply design_context to each method
for m in data['methods']:
    method_id = m['method_id']
    if method_id in design_context_map:
        m['design_context'] = design_context_map[method_id]
        print(f"  ✓ {method_id}: design_context = {m['design_context']}")
    else:
        print(f"  ✗ {method_id}: No mapping found (this shouldn't happen)")

# Also update implements_designs field for consistency
for m in data['methods']:
    if 'design_context' in m and m['design_context']:
        m['implements_designs'] = m['design_context']

# Update timestamp
data['extraction_timestamp'] = datetime.now(timezone.utc).isoformat()

# Save
with open(extraction_file, 'w') as f:
    json.dump(data, f, indent=2)

print("\n✓ All methods now have design_context references")
print("✓ Extraction updated")
