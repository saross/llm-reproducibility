#!/usr/bin/env python3
"""
Pass 6: Validation & Integrity Checks

Validates extraction.json for:
1. Cross-reference integrity (claims ↔ evidence, implicit_arguments → claims)
2. RDMAP hierarchy integrity (protocols → methods → designs)
3. Metadata completeness
4. Schema compliance
5. Sourcing completeness (verbatim_quote or trigger_text)
6. Page number validity

Target: PASS or PASS_WITH_WARNINGS
"""

import json
from pathlib import Path

extraction_path = Path("outputs/ross-2005/extraction.json")
with open(extraction_path, 'r', encoding='utf-8') as f:
    extraction = json.load(f)

print("Pass 6: Validation starting...\n")

# Collect all IDs for reference checking
evidence_ids = {e["id"] for e in extraction["evidence"]}
claim_ids = {c["id"] for c in extraction["claims"]}
ia_ids = {ia["id"] for ia in extraction["implicit_arguments"]}
design_ids = {rd["id"] for rd in extraction["research_designs"]}
method_ids = {m["id"] for m in extraction["methods"]}
protocol_ids = {p["id"] for p in extraction["protocols"]}

errors = []
warnings = []
info = []

# 1. Cross-Reference Integrity: Claims ↔ Evidence
print("1. Validating cross-reference integrity...")
for claim in extraction["claims"]:
    # Check supporting_evidence references
    if "supporting_evidence" in claim:
        for ev_id in claim["supporting_evidence"]:
            if ev_id not in evidence_ids:
                errors.append(f"Claim {claim['id']} references non-existent evidence {ev_id}")

for evidence in extraction["evidence"]:
    # Check supports_claims references
    if "supports_claims" in evidence:
        for claim_id in evidence["supports_claims"]:
            if claim_id not in claim_ids:
                errors.append(f"Evidence {evidence['id']} references non-existent claim {claim_id}")

# Check implicit_arguments → claims
for ia in extraction["implicit_arguments"]:
    if "related_claims" in ia:
        for claim_id in ia["related_claims"]:
            if claim_id not in claim_ids:
                errors.append(f"Implicit argument {ia['id']} references non-existent claim {claim_id}")

print(f"   Cross-reference integrity: {len(errors)} errors found")

# 2. RDMAP Hierarchy Integrity
print("2. Validating RDMAP hierarchy...")
for protocol in extraction["protocols"]:
    if "implements_method" in protocol:
        for method_id in protocol["implements_method"]:
            if method_id not in method_ids:
                errors.append(f"Protocol {protocol['id']} references non-existent method {method_id}")
    else:
        warnings.append(f"Protocol {protocol['id']} has no implements_method link (orphaned)")

for method in extraction["methods"]:
    if "implements_design" in method:
        for design_id in method["implements_design"]:
            if design_id not in design_ids:
                errors.append(f"Method {method['id']} references non-existent design {design_id}")
    else:
        warnings.append(f"Method {method['id']} has no implements_design link (orphaned)")

print(f"   RDMAP hierarchy: {len([e for e in errors if 'RDMAP' in str(e) or 'Protocol' in str(e) or 'Method' in str(e)])} errors, {len([w for w in warnings if 'Method' in str(w) or 'Protocol' in str(w)])} warnings")

# 3. Metadata Completeness
print("3. Validating metadata completeness...")
required_metadata = ["paper_title", "authors", "publication_year", "journal", "doi", "paper_type", "discipline", "research_context"]
for field in required_metadata:
    if field not in extraction["project_metadata"]:
        errors.append(f"Missing required metadata field: {field}")
    elif extraction["project_metadata"][field] is None and field != "doi":
        errors.append(f"Required metadata field {field} is null")
    elif extraction["project_metadata"][field] == "" and field != "doi":
        errors.append(f"Required metadata field {field} is empty string")

# Check authors format
if "authors" in extraction["project_metadata"]:
    for author in extraction["project_metadata"]["authors"]:
        if "." in author and author.count(".") < 3:  # Likely initials
            warnings.append(f"Author '{author}' may use initials instead of full name")

print(f"   Metadata completeness: {len([e for e in errors if 'metadata' in e.lower()])} errors, {len([w for w in warnings if 'Author' in w])} warnings")

# 4. Schema Compliance & Sourcing Completeness
print("4. Validating sourcing completeness...")
sourcing_errors = 0
sourcing_warnings = 0

# Check evidence sourcing
for evidence in extraction["evidence"]:
    if evidence.get("evidence_status") == "explicit":
        if not evidence.get("verbatim_quote"):
            sourcing_errors += 1
            errors.append(f"Evidence {evidence['id']} (explicit) missing verbatim_quote")
    elif evidence.get("evidence_status") == "implicit":
        if not evidence.get("trigger_text"):
            sourcing_errors += 1
            errors.append(f"Evidence {evidence['id']} (implicit) missing trigger_text")

# Check claims sourcing
for claim in extraction["claims"]:
    if not claim.get("verbatim_quote"):
        sourcing_warnings += 1
        warnings.append(f"Claim {claim['id']} missing verbatim_quote")

# Check implicit arguments sourcing
for ia in extraction["implicit_arguments"]:
    if not ia.get("trigger_text"):
        sourcing_errors += 1
        errors.append(f"Implicit argument {ia['id']} missing trigger_text")
    if not ia.get("inference_reasoning"):
        sourcing_errors += 1
        errors.append(f"Implicit argument {ia['id']} missing inference_reasoning")

# Check RDMAP sourcing
for rd in extraction["research_designs"]:
    if not rd.get("verbatim_quote"):
        sourcing_warnings += 1
        warnings.append(f"Research design {rd['id']} missing verbatim_quote")

for method in extraction["methods"]:
    if method.get("status") == "implicit":
        if not method.get("inference_reasoning"):
            sourcing_errors += 1
            errors.append(f"Method {method['id']} (implicit) missing inference_reasoning")
    elif not method.get("verbatim_quote"):
        sourcing_warnings += 1
        warnings.append(f"Method {method['id']} missing verbatim_quote")

for protocol in extraction["protocols"]:
    if protocol.get("status") == "implicit":
        if not protocol.get("inference_reasoning"):
            sourcing_errors += 1
            errors.append(f"Protocol {protocol['id']} (implicit) missing inference_reasoning")
    elif not protocol.get("verbatim_quote"):
        sourcing_warnings += 1
        warnings.append(f"Protocol {protocol['id']} missing verbatim_quote")

print(f"   Sourcing completeness: {sourcing_errors} errors, {sourcing_warnings} warnings")

# 5. Page Number Validity
print("5. Validating page numbers...")
page_errors = 0
for item_type, items in [("evidence", extraction["evidence"]), ("claims", extraction["claims"]),
                          ("implicit_arguments", extraction["implicit_arguments"]),
                          ("research_designs", extraction["research_designs"]),
                          ("methods", extraction["methods"]), ("protocols", extraction["protocols"])]:
    for item in items:
        if "page" in item:
            if not isinstance(item["page"], int) or item["page"] < 299 or item["page"] > 316:
                page_errors += 1
                errors.append(f"{item_type.capitalize()} {item['id']} has invalid page number: {item['page']}")

print(f"   Page number validity: {page_errors} errors")

# Summary
print(f"\n{'='*60}")
print("VALIDATION SUMMARY")
print(f"{'='*60}")
print(f"Total Errors: {len(errors)}")
print(f"Total Warnings: {len(warnings)}")
print(f"\nItems Validated:")
print(f"  - Evidence: {len(extraction['evidence'])}")
print(f"  - Claims: {len(extraction['claims'])}")
print(f"  - Implicit Arguments: {len(extraction['implicit_arguments'])}")
print(f"  - Research Designs: {len(extraction['research_designs'])}")
print(f"  - Methods: {len(extraction['methods'])}")
print(f"  - Protocols: {len(extraction['protocols'])}")
print(f"  - TOTAL: {len(extraction['evidence']) + len(extraction['claims']) + len(extraction['implicit_arguments']) + len(extraction['research_designs']) + len(extraction['methods']) + len(extraction['protocols'])}")

# Determine validation status
if len(errors) == 0 and len(warnings) == 0:
    status = "PASS"
elif len(errors) == 0 and len(warnings) > 0:
    status = "PASS_WITH_WARNINGS"
elif len(errors) > 0 and len(errors) <= 5:
    status = "WARN"
else:
    status = "FAIL"

print(f"\nValidation Status: {status}")

if errors:
    print(f"\nErrors ({len(errors)}):")
    for error in errors[:10]:  # Show first 10
        print(f"  - {error}")
    if len(errors) > 10:
        print(f"  ... and {len(errors)-10} more")

if warnings:
    print(f"\nWarnings ({len(warnings)}):")
    for warning in warnings[:10]:  # Show first 10
        print(f"  - {warning}")
    if len(warnings) > 10:
        print(f"  ... and {len(warnings)-10} more")

# Update extraction notes
extraction["extraction_notes"].append(
    f"Pass 6 Validation complete: Status {status}. "
    f"Total items validated: {len(extraction['evidence']) + len(extraction['claims']) + len(extraction['implicit_arguments']) + len(extraction['research_designs']) + len(extraction['methods']) + len(extraction['protocols'])} "
    f"({len(extraction['evidence'])} evidence + {len(extraction['claims'])} claims + {len(extraction['implicit_arguments'])} implicit_arguments + "
    f"{len(extraction['research_designs'])} research_designs + {len(extraction['methods'])} methods + {len(extraction['protocols'])} protocols). "
    f"Errors: {len(errors)}, Warnings: {len(warnings)}. "
    f"Cross-reference integrity: {'OK' if len([e for e in errors if 'references' in e.lower()]) == 0 else 'ISSUES'}. "
    f"RDMAP hierarchy: {'OK' if len([e for e in errors if 'RDMAP' in str(e) or 'implements' in e.lower()]) == 0 else 'ISSUES'}. "
    f"Sourcing completeness: {sourcing_errors} errors, {sourcing_warnings} warnings."
)

with open(extraction_path, 'w', encoding='utf-8') as f:
    json.dump(extraction, f, indent=2, ensure_ascii=False)

print(f"\n✓ Pass 6 Validation complete")
print(f"  Status: {status}")
print(f"  {'PROCEED TO SUMMARY' if status in ['PASS', 'PASS_WITH_WARNINGS'] else 'REPAIR REQUIRED'}")
