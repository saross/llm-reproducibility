# Skill Improvement Implementation Plan

**Created**: 2025-10-27
**Completed**: 2025-10-27
**Context**: Fix two critical regressions from extraction comparison:
1. Cross-reference breakage during consolidation (41 broken refs)
2. Zero implicit RDMAP extraction (lost capability)

**Status**: ✅ COMPLETED
**All changes**: Paper-agnostic (work with any research paper)

---

## Implementation Checklist

- [x] 1. Enhance `.claude/skills/research-assessor/references/checklists/consolidation-patterns.md`
- [x] 2. Enhance `.claude/skills/research-assessor/references/extraction-fundamentals.md`
- [x] 3. Update `.claude/skills/research-assessor/SKILL.md`
- [x] 4. Create `extraction-system/scripts/extraction/consolidation_template.py`
- [x] 5. Create `extraction-system/scripts/extraction/section_rdmap_template.py`
- [x] 6. Mark this plan complete

---

## 1. Enhance consolidation-patterns.md

**File**: `.claude/skills/research-assessor/references/checklists/consolidation-patterns.md`

**Action**: Add new section at end (before final notes)

**New Section**:

```markdown
---

## Cross-Reference Repair After Consolidation (MANDATORY)

### The Problem

When consolidating items, references from other arrays become stale:
- Consolidate E012+E013+E014 → E011
- But claims still reference E012, E013, E014 (now deleted)
- Result: Broken cross-references

### The Solution: Automated Repair

**After ALL consolidations, before writing JSON, repair references using consolidation_metadata.**

#### Algorithm

1. **Build consolidation map** from metadata:
   ```python
   consolidation_map = {}  # old_id → new_id

   for evidence in data['evidence']:
       if evidence.get('consolidation_metadata'):
           new_id = evidence['evidence_id']
           for old_id in evidence['consolidation_metadata']['consolidated_from']:
               consolidation_map[old_id] = new_id

   # Repeat for methods, protocols, research_designs
   ```

2. **Update all cross-references**:
   ```python
   # Claims → Evidence
   for claim in data['claims']:
       if 'supported_by_evidence' in claim:
           claim['supported_by_evidence'] = [
               consolidation_map.get(eid, eid)
               for eid in claim['supported_by_evidence']
           ]

   # Methods → Protocols
   for method in data['methods']:
       if 'realized_through_protocols' in method:
           method['realized_through_protocols'] = [
               consolidation_map.get(pid, pid)
               for pid in method['realized_through_protocols']
           ]

   # Research Designs → Methods
   for rd in data['research_designs']:
       if 'enables_methods' in rd:
           rd['enables_methods'] = [
               consolidation_map.get(mid, mid)
               for mid in rd['enables_methods']
           ]

   # Protocols → Methods (single value, not array)
   for protocol in data['protocols']:
       if 'implements_method' in protocol:
           old = protocol['implements_method']
           protocol['implements_method'] = consolidation_map.get(old, old)
   ```

3. **Remove duplicates** (consolidation may create duplicate refs):
   ```python
   claim['supported_by_evidence'] = list(dict.fromkeys(refs))
   ```

4. **Validate** no broken references remain (see validation section below)

#### Complete Reference Implementation

See `extraction-system/scripts/extraction/consolidation_template.py` for complete, commented implementation.

### Validation After Repair

After repair, validate cross-references:

```python
# Build ID sets
evidence_ids = {e['evidence_id'] for e in data['evidence']}
method_ids = {m['method_id'] for m in data['methods']}
protocol_ids = {p['protocol_id'] for p in data['protocols']}
rd_ids = {rd['design_id'] for rd in data['research_designs']}

# Check claims → evidence
for claim in data['claims']:
    for eid in claim.get('supported_by_evidence', []):
        assert eid in evidence_ids, f"Broken: {claim['claim_id']} → {eid}"

# Check methods → protocols
for method in data['methods']:
    for pid in method.get('realized_through_protocols', []):
        assert pid in protocol_ids, f"Broken: {method['method_id']} → {pid}"

# Check research_designs → methods
for rd in data['research_designs']:
    for mid in rd.get('enables_methods', []):
        assert mid in method_ids, f"Broken: {rd['design_id']} → {mid}"

# Check protocols → methods
for protocol in data['protocols']:
    if protocol.get('implements_method'):
        mid = protocol['implements_method']
        assert mid in method_ids, f"Broken: {protocol['protocol_id']} → {mid}"
```

### When to Apply

- **Pass 2 rationalization**: After consolidating claims/evidence
- **Pass 4 rationalization**: After consolidating RDMAP items
- **Required**: Not optional - consolidation without repair causes validation failures
```

---

## 2. Enhance extraction-fundamentals.md

**File**: `.claude/skills/research-assessor/references/extraction-fundamentals.md`

**Action**: Add new section after "Implicit Content" section (around line 65)

**New Section**:

```markdown
---

## Implicit RDMAP Extraction in Section-by-Section Passes

### The Challenge

When extracting RDMAP section-by-section (Abstract+Intro, Methods, Results, Discussion),
each section must extract **BOTH explicit AND implicit** RDMAP items.

**Common failure mode**: Only extracting explicit items (what's documented in Methods),
missing implicit items (procedures mentioned but not described).

### Where Implicit RDMAP Items Hide

**Implicit Methods** - Procedures mentioned but not described:
- ✓ Results: "We cleaned the data" → Data cleaning method (implicit if procedure not in Methods)
- ✓ Discussion: "We validated against external datasets" → Validation method (implicit)
- ✓ Results: "Error checking revealed..." → QA method (implicit if process not described)

**Implicit Protocols** - Implementation details inferred from execution:
- ✓ Results: "2,500 records per device caused performance degradation" → Load threshold monitoring protocol
- ✓ Results: "Students were assigned specific map tiles" → Map assignment protocol
- ✓ Results: "We corrected spatial omissions by re-extracting coordinates" → Error correction protocol

**Implicit Research Designs** - Strategic decisions apparent but unstated:
- ✓ Introduction: Positioning study relative to other approaches (if framing not in Methods)
- ✓ Discussion: Threshold analysis framework (if decision criteria not explicitly designed)

### Section-by-Section Extraction Workflow

**For EACH section (Abstract+Intro, Methods, Results, Discussion):**

1. **First**: Extract explicit RDMAP
   - Items documented in Methods section OR clearly stated in current section
   - Use `*_status = "explicit"` with `verbatim_quote`

2. **Then**: Scan for implicit RDMAP
   - Look for **VERBS without procedures**: cleaned, validated, checked, assigned, corrected
   - Look for **EFFECTS implying causes**: "performance degraded at 2,500 records" → monitoring
   - Look for **MENTIONS without descriptions**: "assigned maps" → assignment protocol

3. **For each implicit item**:
   - Extract `trigger_text` array (verbatim passages mentioning the procedure)
   - Record `trigger_locations` (where each trigger found)
   - Write `inference_reasoning` (explain how triggers imply the RDMAP item)
   - Add `implicit_metadata` with basis and assessment_implication

### Recognition Patterns

**Pattern 1: Mentioned Procedure**
- Trigger: Paper mentions doing something but doesn't describe how
- Example: "We quality-checked digitized features"
- Extract: Implicit protocol for QA procedure
- Reasoning: "Paper states QA occurred but provides no procedural details"

**Pattern 2: Inferred from Results**
- Trigger: Results section reveals operational detail not in Methods
- Example: "Performance degraded after ~2,500 records per device"
- Extract: Implicit protocol for load monitoring
- Reasoning: "Precise threshold detection implies monitoring, but monitoring method undocumented"

**Pattern 3: Undocumented Assignment**
- Trigger: References to "assigned" tasks without assignment method
- Example: "Students assigned specific map tiles"
- Extract: Implicit protocol for task assignment
- Reasoning: "Assignment mentioned multiple times but allocation method never described"

**Pattern 4: Implied Strategic Decision**
- Trigger: Discussion positions study but framing not in Methods
- Example: Paper compares approach to ML without stating this was design goal
- Extract: Implicit research design for comparative positioning
- Reasoning: "Systematic comparison implies design choice, but not stated as objective"

### Quick Reference: Explicit vs Implicit RDMAP

| Aspect | Explicit | Implicit |
|--------|----------|----------|
| **Location** | Documented in Methods OR clearly stated | Mentioned/inferred from Results/Discussion |
| **Test** | "Is procedure described?" | "Is procedure mentioned but not described?" |
| **Status field** | `"explicit"` | `"implicit"` |
| **Source field** | `verbatim_quote` | `trigger_text` array |
| **Reasoning** | Not required | `inference_reasoning` required |

### Common Mistakes to Avoid

❌ **Assuming implicit = absent**: If paper never mentions a procedure, it's absent (don't extract). Implicit means mentioned but undocumented.

❌ **Extracting standard practices**: Don't infer "they must have done X" from domain knowledge. Only extract what paper mentions.

❌ **Marking Methods section items as implicit**: Items documented in Methods section are explicit, even if terse.

✓ **Correct approach**: Implicit items have textual triggers (mentions) but lack procedural detail.

---
```

---

## 3. Update SKILL.md

**File**: `.claude/skills/research-assessor/SKILL.md`

**Action**: Update "Core Extraction Principles" section (around line 99)

**Current**:
```markdown
**Core Extraction Principles:**
- `references/extraction-fundamentals.md` - Universal sourcing requirements (ALWAYS read first for Pass 1 & 2)
```

**Change to**:
```markdown
**Core Extraction Principles:**
- `references/extraction-fundamentals.md` - Universal sourcing requirements, explicit vs implicit extraction, section-by-section implicit RDMAP patterns (ALWAYS read first for Pass 1 & 2)
- `references/checklists/consolidation-patterns.md` - When to consolidate, cross-reference repair procedure (CRITICAL for Pass 2 & Pass 4)
```

---

## 4. Create consolidation_template.py

**File**: `extraction-system/scripts/extraction/consolidation_template.py`

**Purpose**: Reference implementation of cross-reference repair

**Full contents**: See detailed Python code in consolidated plan (included in sections below)

**Key Functions**:
- `repair_cross_references(data)` - Builds consolidation map and updates all references
- `validate_cross_references(data)` - Validates no broken refs remain
- Example workflow showing integration

```python
#!/usr/bin/env python3
"""
Consolidation Template with Cross-Reference Repair

This is a TEMPLATE showing the standard consolidation workflow.
Adapt this for specific Pass 2 (Claims/Evidence) or Pass 4 (RDMAP) consolidations.
"""

import json

def repair_cross_references(data):
    """Repair all cross-references after consolidation."""
    consolidation_map = {}

    # Build map from all consolidation_metadata
    for evidence in data.get('evidence', []):
        if evidence.get('consolidation_metadata'):
            new_id = evidence['evidence_id']
            for old_id in evidence['consolidation_metadata'].get('consolidated_from', []):
                consolidation_map[old_id] = new_id

    for method in data.get('methods', []):
        if method.get('consolidation_metadata'):
            new_id = method['method_id']
            for old_id in method['consolidation_metadata'].get('consolidated_from', []):
                consolidation_map[old_id] = new_id

    for protocol in data.get('protocols', []):
        if protocol.get('consolidation_metadata'):
            new_id = protocol['protocol_id']
            for old_id in protocol['consolidation_metadata'].get('consolidated_from', []):
                consolidation_map[old_id] = new_id

    for rd in data.get('research_designs', []):
        if rd.get('consolidation_metadata'):
            new_id = rd['design_id']
            for old_id in rd['consolidation_metadata'].get('consolidated_from', []):
                consolidation_map[old_id] = new_id

    # Repair all cross-references
    for claim in data.get('claims', []):
        if 'supported_by_evidence' in claim:
            updated = [consolidation_map.get(eid, eid) for eid in claim['supported_by_evidence']]
            claim['supported_by_evidence'] = list(dict.fromkeys(updated))

    for method in data.get('methods', []):
        if 'realized_through_protocols' in method:
            updated = [consolidation_map.get(pid, pid) for pid in method['realized_through_protocols']]
            method['realized_through_protocols'] = list(dict.fromkeys(updated))
        if 'enabled_by_designs' in method:
            updated = [consolidation_map.get(rdid, rdid) for rdid in method['enabled_by_designs']]
            method['enabled_by_designs'] = list(dict.fromkeys(updated))

    for rd in data.get('research_designs', []):
        if 'enables_methods' in rd:
            updated = [consolidation_map.get(mid, mid) for mid in rd['enables_methods']]
            rd['enables_methods'] = list(dict.fromkeys(updated))

    for protocol in data.get('protocols', []):
        if protocol.get('implements_method'):
            old = protocol['implements_method']
            protocol['implements_method'] = consolidation_map.get(old, old)

    return len(consolidation_map)

def validate_cross_references(data):
    """Validate all cross-references. Raises AssertionError if broken."""
    evidence_ids = {e['evidence_id'] for e in data.get('evidence', [])}
    method_ids = {m['method_id'] for m in data.get('methods', [])}
    protocol_ids = {p['protocol_id'] for p in data.get('protocols', [])}
    rd_ids = {rd['design_id'] for rd in data.get('research_designs', [])}

    valid_count = 0

    for claim in data.get('claims', []):
        for eid in claim.get('supported_by_evidence', []):
            assert eid in evidence_ids, f"Broken: {claim['claim_id']} → {eid}"
            valid_count += 1

    for method in data.get('methods', []):
        for pid in method.get('realized_through_protocols', []):
            assert pid in protocol_ids, f"Broken: {method['method_id']} → {pid}"
            valid_count += 1

    for rd in data.get('research_designs', []):
        for mid in rd.get('enables_methods', []):
            assert mid in method_ids, f"Broken: {rd['design_id']} → {mid}"
            valid_count += 1

    for protocol in data.get('protocols', []):
        if protocol.get('implements_method'):
            mid = protocol['implements_method']
            assert mid in method_ids, f"Broken: {protocol['protocol_id']} → {mid}"
            valid_count += 1

    return valid_count

# EXAMPLE USAGE
if __name__ == "__main__":
    with open('extraction.json', 'r') as f:
        data = json.load(f)

    # [Your consolidation logic here]

    # CRITICAL: Repair cross-references
    num_repairs = repair_cross_references(data)
    print(f"✅ Repaired {num_repairs} ID mappings")

    # Validate
    valid = validate_cross_references(data)
    print(f"✅ Validated {valid} cross-references - all valid")

    with open('extraction.json', 'w') as f:
        json.dump(data, f, indent=2)
```

---

## 5. Create section_rdmap_template.py

**File**: `extraction-system/scripts/extraction/section_rdmap_template.py`

**Purpose**: Template showing section extraction with explicit + implicit RDMAP

```python
#!/usr/bin/env python3
"""
Section-by-Section RDMAP Extraction Template

Demonstrates extracting BOTH explicit and implicit RDMAP from a single section.
Adapt for each section: Abstract+Intro, Methods, Results, Discussion.
"""

import json

with open('extraction.json', 'r') as f:
    data = json.load(f)

# EXPLICIT RDMAP (documented/stated)
explicit_methods = [
    {
        "method_id": "M001",
        "method_text": "Data collection using mobile GIS",
        "method_tier": "data_collection",
        "method_status": "explicit",
        "verbatim_quote": "We collected data using a customized mobile GIS application.",
        "location": {"section": "Methods", "subsection": "2.3", "page": 5},
        "enabled_by_designs": ["RD001"],
        "realized_through_protocols": ["P001"]
    }
]

# IMPLICIT RDMAP (mentioned but not described)
implicit_protocols = [
    {
        "protocol_id": "P002",
        "protocol_text": "Map assignment protocol for volunteers",
        "protocol_tier": "task_allocation",
        "protocol_status": "implicit",
        "trigger_text": [
            "Students were assigned specific map tiles",
            "Student C failing to digitise assigned sections"
        ],
        "trigger_locations": [
            {"section": "Results", "page": 7, "paragraph": 1},
            {"section": "Results", "page": 8, "paragraph": 2}
        ],
        "inference_reasoning": "Multiple references to 'assigned maps' indicate assignment protocol existed, but allocation method never described.",
        "implicit_metadata": {
            "basis": "mentioned_undocumented",
            "confidence": "high",
            "assessment_implication": "Cannot assess if assignment strategy affected error patterns"
        },
        "location": {"section": "Results", "page": 7},
        "implements_method": "M001"
    }
]

# Add to arrays
data['methods'].extend(explicit_methods)
data['protocols'].extend(implicit_protocols)

with open('extraction.json', 'w') as f:
    json.dump(data, f, indent=2)
```

---

## Implementation Notes

### Implementation Order
1. consolidation-patterns.md (most critical - fixes broken refs)
2. extraction-fundamentals.md (restores implicit extraction)
3. SKILL.md (navigation)
4. consolidation_template.py (reference)
5. section_rdmap_template.py (reference)

### Testing
After implementation, test with new paper extraction:
- Verify cross-reference repair runs automatically in Pass 2/4
- Verify implicit RDMAP items extracted in Pass 3
- Check validation shows 0 broken cross-references

### Expected Outcomes
- **Zero broken cross-references** (automated repair in consolidation)
- **Implicit RDMAP restored** (clear guidance + patterns)
- **Paper-agnostic** (all changes work for any paper)
- **Lean prompts** (procedural knowledge in skill, not prompts)

---

## Related Documents

- **Regression Analysis**: `outputs/sobotkova-et-al-2023/REGRESSION_ANALYSIS.md`
- **Comparison Report**: Generated in session showing 0 implicit RDMAP vs 1-4 in prior runs
- **Conversation Export**: `2025-10-27-b.txt` (this session)
