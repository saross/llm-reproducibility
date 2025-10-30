#!/usr/bin/env python3
"""Fix broken cross-reference: E006 C24 → C024"""

import json
from datetime import datetime, timezone
from pathlib import Path

extraction_file = Path("extraction.json")
with open(extraction_file) as f:
    data = json.load(f)

# Fix E006
for e in data['evidence']:
    if e['evidence_id'] == 'E006':
        e['supports_claims'] = ['C024', 'C026', 'C027']
        break

# Update timestamp
data["extraction_timestamp"] = datetime.now(timezone.utc).isoformat()

# Save
with open(extraction_file, 'w') as f:
    json.dump(data, f, indent=2)

print("✓ Fixed E006 cross-reference: C24 → C024")
