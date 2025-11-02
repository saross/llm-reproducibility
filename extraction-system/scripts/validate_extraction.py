#!/usr/bin/env python3
"""
JSON Schema Validator for Extraction Files

Validates extraction.json files against extraction_schema.json and checks
reference integrity. Part of systematic quality improvement to prevent
data quality issues.

Usage:
    python3 validate_extraction.py <path_to_extraction.json>

    Or from extraction workflow:
    python3 extraction-system/scripts/validate_extraction.py outputs/paper-name/extraction.json

Validation checks:
    - JSON Schema compliance (uniqueItems, minimum values, required fields)
    - Reference integrity (all referenced IDs exist in their respective arrays)
    - Duplicate ID detection
    - Page number validity (≥1 or null, not -1)

Author: Claude Sonnet 4.5
Date: 2025-11-02
"""

import json
import sys
from pathlib import Path
from typing import Dict, List, Set, Tuple
from collections import defaultdict

try:
    import jsonschema
    from jsonschema import validate, ValidationError, Draft7Validator
except ImportError:
    print("Error: jsonschema package not installed")
    print("Install with: pip install jsonschema")
    sys.exit(1)


class ExtractionValidator:
    """Validates extraction.json against schema and reference integrity."""

    def __init__(self, extraction_path: str, schema_path: str = None):
        self.extraction_path = Path(extraction_path)

        # Default schema path relative to script location
        if schema_path is None:
            script_dir = Path(__file__).parent
            self.schema_path = script_dir.parent / 'schema' / 'extraction_schema.json'
        else:
            self.schema_path = Path(schema_path)

        self.data = self._load_extraction()
        self.schema = self._load_schema()
        self.errors = []
        self.warnings = []
        self.stats = {
            'schema_errors': 0,
            'reference_errors': 0,
            'duplicate_ids': 0,
            'invalid_pages': 0
        }

    def _load_extraction(self) -> dict:
        """Load extraction.json file."""
        if not self.extraction_path.exists():
            raise FileNotFoundError(f"Extraction file not found: {self.extraction_path}")

        with open(self.extraction_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def _load_schema(self) -> dict:
        """Load extraction_schema.json file."""
        if not self.schema_path.exists():
            raise FileNotFoundError(f"Schema file not found: {self.schema_path}")

        with open(self.schema_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def validate_schema(self) -> None:
        """
        Validate extraction data against JSON Schema.

        Checks:
        - Required fields present
        - Correct data types
        - uniqueItems constraints
        - Minimum value constraints
        """
        try:
            validator = Draft7Validator(self.schema)
            schema_errors = sorted(validator.iter_errors(self.data), key=lambda e: e.path)

            for error in schema_errors:
                # Format the error path
                path = '.'.join(str(p) for p in error.path) if error.path else 'root'

                # Create human-readable error message
                error_msg = f"Schema violation at {path}: {error.message}"

                self.errors.append(error_msg)
                self.stats['schema_errors'] += 1

        except Exception as e:
            self.errors.append(f"Schema validation failed: {e}")
            self.stats['schema_errors'] += 1

    def validate_unique_ids(self) -> None:
        """
        Check for duplicate IDs within each array.

        Checks all ID fields:
        - evidence_id
        - claim_id
        - method_id
        - protocol_id
        - research_design_id / design_id
        """
        id_checks = [
            ('evidence', ['evidence_id', 'id']),
            ('claims', ['claim_id', 'id']),
            ('methods', ['method_id', 'id']),
            ('protocols', ['protocol_id', 'id']),
            ('research_designs', ['design_id', 'research_design_id', 'id'])
        ]

        for array_name, id_fields in id_checks:
            items = self.data.get(array_name, [])
            seen_ids = set()

            for idx, item in enumerate(items):
                # Get ID from item
                item_id = None
                for field in id_fields:
                    if field in item:
                        item_id = item[field]
                        break

                if not item_id:
                    self.errors.append(
                        f"Missing ID in {array_name}[{idx}]: expected one of {id_fields}"
                    )
                    self.stats['duplicate_ids'] += 1
                    continue

                if item_id in seen_ids:
                    self.errors.append(
                        f"Duplicate ID in {array_name}: '{item_id}' appears multiple times"
                    )
                    self.stats['duplicate_ids'] += 1
                else:
                    seen_ids.add(item_id)

    def validate_page_numbers(self) -> None:
        """
        Check that all page numbers are ≥1 or null (not -1 placeholders).
        """
        def check_location(location: dict, context: str):
            if location and 'page' in location:
                page = location['page']
                if page is not None and (not isinstance(page, int) or page < 1):
                    self.errors.append(
                        f"Invalid page number in {context}: page={page} (must be ≥1 or null)"
                    )
                    self.stats['invalid_pages'] += 1

        # Check evidence
        for idx, item in enumerate(self.data.get('evidence', [])):
            evidence_id = item.get('evidence_id', item.get('id', f'evidence[{idx}]'))
            check_location(item.get('location'), f"evidence {evidence_id}")

        # Check claims
        for idx, item in enumerate(self.data.get('claims', [])):
            claim_id = item.get('claim_id', item.get('id', f'claim[{idx}]'))
            check_location(item.get('location'), f"claim {claim_id}")

        # Check methods
        for idx, item in enumerate(self.data.get('methods', [])):
            method_id = item.get('method_id', item.get('id', f'method[{idx}]'))
            check_location(item.get('location'), f"method {method_id}")

        # Check protocols
        for idx, item in enumerate(self.data.get('protocols', [])):
            protocol_id = item.get('protocol_id', item.get('id', f'protocol[{idx}]'))
            check_location(item.get('location'), f"protocol {protocol_id}")

        # Check research designs
        for idx, item in enumerate(self.data.get('research_designs', [])):
            design_id = item.get('design_id', item.get('research_design_id',
                                  item.get('id', f'design[{idx}]')))
            check_location(item.get('location'), f"design {design_id}")

    def validate_reference_integrity(self) -> None:
        """
        Check that all referenced IDs exist in their respective arrays.

        Validates:
        - Claim→Evidence: claims.supported_by references exist in evidence array
        - Evidence→Claim: evidence.supports_claims references exist in claims array
        - Method→Design: methods.implements_designs references exist in research_designs
        - Protocol→Method: protocols.implements_methods references exist in methods
        """
        # Build ID indexes
        evidence_ids = self._get_all_ids('evidence', ['evidence_id', 'id'])
        claim_ids = self._get_all_ids('claims', ['claim_id', 'id'])
        method_ids = self._get_all_ids('methods', ['method_id', 'id'])
        protocol_ids = self._get_all_ids('protocols', ['protocol_id', 'id'])
        design_ids = self._get_all_ids('research_designs',
                                        ['design_id', 'research_design_id', 'id'])

        # Validate claim→evidence references
        for idx, claim in enumerate(self.data.get('claims', [])):
            claim_id = claim.get('claim_id', claim.get('id', f'claim[{idx}]'))

            # Check all possible field names
            evidence_refs = (
                claim.get('supported_by', []) or
                claim.get('supported_by_evidence', []) or
                claim.get('evidence_links', []) or
                []
            )

            for eid in evidence_refs:
                if eid not in evidence_ids:
                    self.errors.append(
                        f"Reference error: claim {claim_id} references non-existent "
                        f"evidence '{eid}'"
                    )
                    self.stats['reference_errors'] += 1

        # Validate evidence→claim references
        for idx, evidence in enumerate(self.data.get('evidence', [])):
            evidence_id = evidence.get('evidence_id', evidence.get('id', f'evidence[{idx}]'))

            claim_refs = (
                evidence.get('supports_claims', []) or
                evidence.get('linked_claims', []) or
                []
            )

            for cid in claim_refs:
                if cid not in claim_ids:
                    self.errors.append(
                        f"Reference error: evidence {evidence_id} references non-existent "
                        f"claim '{cid}'"
                    )
                    self.stats['reference_errors'] += 1

        # Validate method→design references
        for idx, method in enumerate(self.data.get('methods', [])):
            method_id = method.get('method_id', method.get('id', f'method[{idx}]'))

            design_refs = (
                method.get('implements_designs', []) or
                method.get('linked_designs', []) or
                []
            )

            for did in design_refs:
                if did not in design_ids:
                    self.errors.append(
                        f"Reference error: method {method_id} references non-existent "
                        f"design '{did}'"
                    )
                    self.stats['reference_errors'] += 1

        # Validate protocol→method references
        for idx, protocol in enumerate(self.data.get('protocols', [])):
            protocol_id = protocol.get('protocol_id', protocol.get('id', f'protocol[{idx}]'))

            method_refs = (
                protocol.get('implements_methods', []) or
                protocol.get('linked_methods', []) or
                []
            )

            for mid in method_refs:
                if mid not in method_ids:
                    self.errors.append(
                        f"Reference error: protocol {protocol_id} references non-existent "
                        f"method '{mid}'"
                    )
                    self.stats['reference_errors'] += 1

        # Validate design→method reverse references
        for idx, design in enumerate(self.data.get('research_designs', [])):
            design_id = design.get('design_id', design.get('research_design_id',
                                   design.get('id', f'design[{idx}]')))

            method_refs = (
                design.get('implemented_by_methods', []) or
                design.get('supported_by_methods', []) or
                []
            )

            for mid in method_refs:
                if mid not in method_ids:
                    self.errors.append(
                        f"Reference error: design {design_id} references non-existent "
                        f"method '{mid}'"
                    )
                    self.stats['reference_errors'] += 1

    def _get_all_ids(self, array_name: str, id_fields: List[str]) -> Set[str]:
        """Extract all IDs from an array, trying multiple field names."""
        ids = set()
        for item in self.data.get(array_name, []):
            for field in id_fields:
                if field in item:
                    ids.add(item[field])
                    break
        return ids

    def run(self) -> dict:
        """Run all validation checks and return results."""
        print(f"Validating extraction against schema: {self.extraction_path}")
        print("=" * 80)

        # Run validators
        print("Checking JSON Schema compliance...")
        self.validate_schema()

        print("Checking for duplicate IDs...")
        self.validate_unique_ids()

        print("Checking page number validity...")
        self.validate_page_numbers()

        print("Checking reference integrity...")
        self.validate_reference_integrity()

        # Generate report
        self._print_report()

        return {
            'stats': self.stats,
            'errors': self.errors,
            'warnings': self.warnings
        }

    def _print_report(self):
        """Print validation report."""
        print("\n" + "=" * 80)
        print("VALIDATION RESULTS")
        print("=" * 80)

        print(f"\nItem counts:")
        print(f"  Evidence: {len(self.data.get('evidence', []))}")
        print(f"  Claims: {len(self.data.get('claims', []))}")
        print(f"  Methods: {len(self.data.get('methods', []))}")
        print(f"  Protocols: {len(self.data.get('protocols', []))}")
        print(f"  Research Designs: {len(self.data.get('research_designs', []))}")

        total_errors = sum(self.stats.values())
        print(f"\nTotal errors found: {total_errors}")
        print(f"  Schema violations: {self.stats['schema_errors']}")
        print(f"  Reference errors: {self.stats['reference_errors']}")
        print(f"  Duplicate IDs: {self.stats['duplicate_ids']}")
        print(f"  Invalid pages: {self.stats['invalid_pages']}")

        if self.errors:
            print(f"\nErrors ({len(self.errors)}):")
            for error in self.errors:
                print(f"  ❌ {error}")

        if self.warnings:
            print(f"\nWarnings ({len(self.warnings)}):")
            for warning in self.warnings:
                print(f"  ⚠️  {warning}")

        if total_errors == 0:
            print("\n✅ All validation checks passed!")
        else:
            print(f"\n❌ Validation failed with {total_errors} error(s)")


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: python3 validate_extraction.py <path_to_extraction.json> [schema_path]")
        print("\nExample:")
        print("  python3 validate_extraction.py outputs/paper-name/extraction.json")
        print("  python3 validate_extraction.py outputs/paper-name/extraction.json schema.json")
        sys.exit(1)

    extraction_path = sys.argv[1]
    schema_path = sys.argv[2] if len(sys.argv) > 2 else None

    try:
        validator = ExtractionValidator(extraction_path, schema_path)
        results = validator.run()

        # Exit with appropriate code
        total_errors = sum(results['stats'].values())
        if total_errors > 0:
            sys.exit(1)  # Validation failed
        else:
            sys.exit(0)  # Success

    except Exception as e:
        print(f"\n❌ Error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
