# Extraction Schema

JSON schema for research paper extraction output.

**Current Version:** 2.5
**Last Updated:** 2025-10-23
**File:** [extraction_schema.json](extraction_schema.json)

---

## Overview

The extraction schema defines the structure for all extracted content from research papers. It includes six main object types plus metadata and notes.

### Object Types

1. **Evidence** - Observations, measurements, data points
2. **Claims** - Interpretations, assertions, generalizations
3. **Implicit Arguments** - Unstated assumptions and implications
4. **Research Designs** - Strategic framing and rationale (WHY)
5. **Methods** - Tactical approaches (WHAT was done)
6. **Protocols** - Operational procedures (HOW specifically)

---

## Schema Versioning

### Current Version (2.5)

**Key Features:**
- All six object types fully specified
- Required verbatim_quote fields (hallucination prevention)
- Consolidation metadata for traceability
- Cross-reference system across all object types
- Source verification fields for validation
- Expected information checklists (TIDieR, CONSORT-Outcomes)

**Breaking Changes from v2.4:**
- Made verbatim_quote REQUIRED for evidence and claims
- Added trigger_text/trigger_locations REQUIRED for implicit arguments
- Added source_verification object to all three main types

### Version History

- **v2.5** (Oct 23, 2025): Hallucination prevention, repository rationalization
- **v2.4** (Oct 19-20, 2025): RDMAP objects added (research_designs, methods, protocols)
- **v2.3** (Oct 18, 2025): Consolidation metadata, multi-dimensional evidence
- **v2.2** (Oct 17, 2025): Two-pass workflow support, enhanced evidence structure
- **v2.0-v2.1** (Oct 16, 2025): Initial schema with evidence, claims, implicit_arguments

See [docs/skill-documentation/VERSION.md](../../docs/skill-documentation/VERSION.md) for complete changelog.

---

## Using the Schema

### For Extraction

**Blank Template:**
Use [../../examples/blank_template_v2.5.json](../../examples/blank_template_v2.5.json) to start new extractions.

**Validation:**
JSON must conform to this schema for:
- Successful Pass 3 validation
- Cross-reference integrity checks
- Assessment framework input (future)

### For Development

**Schema File:**
- `extraction_schema.json` - Complete JSON Schema (Draft 07)
- Includes all field definitions, enums, patterns
- Used for validation and documentation generation

**Related Documentation:**
- [Schema Reference](../../docs/user-guide/schema-reference.md) - User-friendly guide
- [Schema Evolution](../../docs/development/schema-evolution.md) - Version history and mappings

---

## Schema Structure

```json
{
  "schema_version": "2.5",
  "extraction_timestamp": "ISO 8601",
  "extractor": "string",
  "paper_metadata": {
    "title": "string",
    "authors": ["string"],
    "year": number,
    "doi": "string",
    ...
  },
  "evidence": [ {...} ],
  "claims": [ {...} ],
  "implicit_arguments": [ {...} ],
  "research_designs": [ {...} ],
  "methods": [ {...} ],
  "protocols": [ {...} ],
  "extraction_notes": {
    "general_notes": "string",
    "ambiguities": [...],
    "missing_information": [...]
  }
}
```

---

## Field Highlights

### Required Fields (All Objects)

- **ID**: Unique identifier (e.g., "EV001", "CL023", "RD003")
- **Text**: Primary content of the object
- **Location**: Section, page, paragraph in source paper
- **Verbatim Quote**: Exact text from paper (evidence/claims)
  - OR **Trigger Text**: Text that implies the argument (implicit_arguments)

### Cross-References

All objects can reference other objects:
- Evidence → Claims, Methods, Protocols
- Claims → Evidence, Claims (supporting/conflicting), Methods, Designs
- Implicit Arguments → Claims, Evidence, Designs, Methods
- Research Designs → Methods
- Methods → Protocols, Designs, Evidence, Claims
- Protocols → Methods, Evidence, Claims

### Consolidation Metadata

For objects created in Pass 2 rationalization:
- `consolidation_performed`: boolean
- `consolidated_from`: array of original IDs
- `consolidation_type`: enum (granularity_reduction, compound_finding, etc.)
- `information_preserved`: enum (complete, lossy_granularity, lossy_redundancy)
- `rationale`: explanation text

---

## Backward Compatibility

### v2.4 → v2.5
**Breaking:** verbatim_quote now REQUIRED (was optional)
**Migration:** Add verbatim quotes to all evidence/claims before using v2.5 validation

### v2.3 → v2.4
**Non-Breaking:** RDMAP arrays can be added to v2.3 extractions
**Migration:** Simply add empty arrays for research_designs, methods, protocols

### v2.2 → v2.3
**Non-Breaking:** Consolidation metadata optional
**Migration:** Can add metadata retroactively if needed

---

## Expected Information

The schema includes checklists for expected information adapted from:

- **TIDieR Framework** (Methods): 12 elements
- **CONSORT-Outcomes** (Protocols): 8 elements
- **Sampling Strategy** (Methods): 7 elements
- **Analysis Methods** (Methods): 7 elements

These checklists help assess transparency but are NOT requirements for valid extraction.

---

## Validation

### Schema Validation
Use JSON Schema validators to check conformance:
```bash
# Example with ajv-cli
ajv validate -s extraction_schema.json -d your_extraction.json
```

### Pass 3 Validation
The Pass 3 validation prompt performs:
- Schema conformance checking
- Cross-reference integrity verification
- Hierarchy validation (Design → Methods → Protocols)
- Expected information assessment
- Consolidation metadata verification

See [../../docs/user-guide/extraction-workflow.md](../../docs/user-guide/extraction-workflow.md) for validation workflow.

---

## Domain-Specific Extensions

The schema is designed for fieldwork-based research but can be extended:

**Controlled Vocabularies:**
- Evidence types (open list)
- Claim types (enumerated + extensible)
- Design types (open list)
- Method types (open list)
- Protocol types (open list)

**Expected to Evolve:**
- Domain-specific evidence types (archaeological, ecological, etc.)
- Field-specific method taxonomies
- Domain-specific expected information checklists

---

## Related Resources

- [Schema Reference](../../docs/user-guide/schema-reference.md) - Complete field documentation
- [Schema Evolution](../../docs/development/schema-evolution.md) - Version history and mappings
- [Blank Template](../../examples/blank_template_v2.5.json) - Starting point for extraction
- [Complete Example](../../examples/sobotkova_complete.json) - Real extraction example

---

## Questions?

- **Using the schema**: See [Getting Started](../../docs/user-guide/getting-started.md)
- **Understanding fields**: See [Schema Reference](../../docs/user-guide/schema-reference.md)
- **Schema changes**: See [VERSION.md](../../docs/skill-documentation/VERSION.md)
- **Contributing**: See [CONTRIBUTING.md](../../docs/skill-documentation/CONTRIBUTING.md)

---

**Ready to extract!** Use the blank template and follow the [extraction workflow](../../docs/user-guide/extraction-workflow.md).
