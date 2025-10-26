# Research Assessor - Reference Documentation

**Version:** 2.6.2
**Last Updated:** 2025-10-26

This directory contains decision frameworks, schema definitions, and examples to support the extraction workflow.

## Directory Structure

```
references/
├── schema/                        # Schema documentation
│   └── schema-guide.md            # Human-readable schema documentation (v2.6.2)
├── checklists/                    # Decision frameworks and guidelines
│   ├── tier-assignment-guide.md
│   ├── consolidation-patterns.md
│   └── expected-information.md
├── examples/                      # Worked examples from real extractions
│   └── sobotkova-example.md
├── extraction-fundamentals.md     # Universal sourcing requirements (v2.5)
└── verification-procedures.md     # Source verification procedures (Pass 3, with RDMAP)
```

---

## Version 2.5 Updates

**Critical changes in v2.5:**
- **Mandatory sourcing:** All items require verbatim_quote OR trigger_text infrastructure
- **RDMAP explicit/implicit:** Status fields distinguish Methods-documented vs inferred procedures
- **Hallucination prevention:** Three-step verification procedures for all object types
- **Complete RDMAP verification:** New section in verification-procedures.md

---

## What's Included

### Schema Documentation (`schema/`)

Complete object structure definitions for v2.6.2:
- **schema-guide.md** - Human-readable documentation for all six object types
  - Defines: evidence, claims, implicit_arguments, research_designs, methods, protocols
  - V2.5 sourcing requirements (verbatim_quote, trigger_text, trigger_locations)
  - V2.6.2 Research Design simplification (conditional objects fully optional)
  - Explicit vs implicit RDMAP distinction
  - Complete field requirements, enumerations, cross-reference patterns

Note: The canonical JSON schema is at `extraction-system/schema/extraction_schema.json` (provided in execution context)

### Decision Frameworks (`checklists/`)

Core decision support for extraction:
- **tier-assignment-guide.md** - How to distinguish Design vs Method vs Protocol
- **consolidation-patterns.md** - When to lump vs split items during Pass 2
- **expected-information.md** - Domain-specific completeness checklists (TIDieR, CONSORT-Outcomes adapted)

### Core Extraction Principles

Universal requirements for all extraction passes:
- **extraction-fundamentals.md** - Mandatory v2.5 sourcing requirements
  - Explicit content: verbatim_quote required
  - Implicit content: trigger_text + trigger_locations + inference_reasoning required
  - Hallucination prevention discipline
  
- **verification-procedures.md** - Complete source verification procedures for Pass 3
  - Evidence & Claims verification (3-step process)
  - Implicit Arguments verification (3-step process)
  - **RDMAP verification (NEW in v2.5)** - Explicit and implicit RDMAP procedures
  - Decision trees, worked examples, quality metrics
  - Red flags for hallucination detection

### Examples (`examples/`)

Worked extractions demonstrating:
- **sobotkova-example.md** - Complete RDMAP extraction from real paper
- Evidence/claim distinctions
- Three-tier hierarchy application
- Cross-reference patterns

---

## Usage Pattern

When working with extraction prompts:

1. **User provides extraction prompt** - Detailed instructions for specific pass
2. **Claude follows prompt** - Executes extraction according to provided instructions
3. **Claude consults skill references as needed:**

**For Pass 1 & Pass 2 (Extraction & Consolidation):**
- **ALWAYS read first:** `extraction-fundamentals.md` (v2.5 sourcing requirements)
- Schema questions? → Read `schema/schema-guide.md`
- Uncertain about tier assignment? → Read `checklists/tier-assignment-guide.md`
- Need consolidation guidance? → Read `checklists/consolidation-patterns.md`
- Want to see examples? → Read `examples/sobotkova-example.md`

**For Pass 3 (Validation):**
- **ALWAYS read first:** `verification-procedures.md` (complete verification procedures)
- Includes all object types: Evidence, Claims, Implicit Arguments, RDMAP
- Decision trees and worked examples for systematic validation

---

## Architecture Benefits

- **Separation of concerns:** Framework (stable) vs prompts (evolving)
- **Minimal versioning conflicts:** Prompt refinements don't require skill repackaging
- **Efficient context use:** Only load references when needed via progressive disclosure
- **Flexibility:** User controls prompt versions and variations
- **V2.5 integrity:** All sourcing requirements centralized and consistently documented

---

## V2.5 Quick Reference

**When extracting:**
- Evidence/Claims → Must have `verbatim_quote`
- Implicit Arguments → Must have `trigger_text` + `trigger_locations` + `inference_reasoning`
- Explicit RDMAP → Must have `verbatim_quote` from Methods section
- Implicit RDMAP → Must have `trigger_text` + `trigger_locations` + `inference_reasoning` + `implicit_metadata`

**When validating:**
- All items → Three-step verification (location, quote, content-alignment)
- Quality target → >95% verification pass rate
- Zero tolerance → No hallucinated content

See extraction-fundamentals.md and verification-procedures.md for complete guidance.
