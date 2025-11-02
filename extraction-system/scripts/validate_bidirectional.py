#!/usr/bin/env python3
"""
Bidirectional Mapping Validator with Auto-Correction

Validates and auto-corrects bidirectional consistency in extraction.json files.
Part of systematic quality improvement to prevent 88+ bidirectional inconsistency errors.

Usage:
    python3 validate_bidirectional.py <path_to_extraction.json>

    Or from extraction workflow:
    python3 extraction-system/scripts/validate_bidirectional.py outputs/paper-name/extraction.json

Validation checks:
    - Claim→Evidence: If C001 in E005.supports_claims, verify E005 in C001.supporting_evidence
    - Method→Design: If M001 in RD001.implemented_by_methods, verify RD001 in M001.implements_designs
    - Protocol→Method: If P001 in M001.implemented_by_protocols, verify M001 in P001.implements_methods

Auto-correction:
    - Builds missing reverse mappings from forward direction
    - Flags conflicts (forward contradicts reverse) for human review
    - Preserves existing correct mappings

Author: Claude Sonnet 4.5
Date: 2025-11-02
"""

import json
import sys
from pathlib import Path
from typing import Dict, List, Set, Tuple
from collections import defaultdict


class BidirectionalValidator:
    """Validates and auto-corrects bidirectional mapping consistency."""

    def __init__(self, extraction_path: str):
        self.extraction_path = Path(extraction_path)
        self.data = self._load_extraction()
        self.corrections_made = []
        self.conflicts_found = []
        self.stats = {
            'claims_checked': 0,
            'evidence_checked': 0,
            'methods_checked': 0,
            'protocols_checked': 0,
            'designs_checked': 0,
            'corrections_made': 0,
            'conflicts_found': 0
        }

    def _load_extraction(self) -> dict:
        """Load extraction.json file."""
        if not self.extraction_path.exists():
            raise FileNotFoundError(f"Extraction file not found: {self.extraction_path}")

        with open(self.extraction_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def _save_extraction(self):
        """Save corrected extraction.json file."""
        with open(self.extraction_path, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, indent=2, ensure_ascii=False)

    def _get_item_by_id(self, item_type: str, item_id: str) -> dict | None:
        """Retrieve item by ID from appropriate array."""
        items = self.data.get(item_type, [])

        # Handle multiple possible ID field names
        id_fields = {
            'claims': ['claim_id', 'id'],
            'evidence': ['evidence_id', 'id'],
            'methods': ['method_id', 'id'],
            'protocols': ['protocol_id', 'id'],
            'research_designs': ['design_id', 'id', 'research_design_id']
        }

        for item in items:
            for field in id_fields.get(item_type, ['id']):
                if item.get(field) == item_id:
                    return item
        return None

    def _get_id(self, item: dict, item_type: str) -> str | None:
        """Get ID from item, handling multiple field name variants."""
        id_fields = {
            'claims': ['claim_id', 'id'],
            'evidence': ['evidence_id', 'id'],
            'methods': ['method_id', 'id'],
            'protocols': ['protocol_id', 'id'],
            'research_designs': ['design_id', 'research_design_id', 'id']
        }

        for field in id_fields.get(item_type, ['id']):
            if field in item:
                return item[field]
        return None

    def validate_claim_evidence_mappings(self) -> None:
        """
        Validate Claim↔Evidence bidirectional consistency.

        Forward: claims[].supporting_evidence (or variants) → evidence IDs
        Reverse: evidence[].supports_claims → claim IDs
        """
        claims = self.data.get('claims', [])
        evidence = self.data.get('evidence', [])

        # Build forward index: claim_id → set of evidence_ids
        forward = defaultdict(set)
        for claim in claims:
            claim_id = self._get_id(claim, 'claims')
            if not claim_id:
                continue

            self.stats['claims_checked'] += 1

            # Check multiple possible field names for evidence references
            evidence_refs = (
                claim.get('supporting_evidence', []) or
                claim.get('supported_by_evidence', []) or
                claim.get('supported_by', []) or
                claim.get('evidence_links', []) or
                []
            )

            for eid in evidence_refs:
                forward[claim_id].add(eid)

        # Build reverse index: evidence_id → set of claim_ids
        reverse = defaultdict(set)
        for ev in evidence:
            evidence_id = self._get_id(ev, 'evidence')
            if not evidence_id:
                continue

            self.stats['evidence_checked'] += 1

            claim_refs = (
                ev.get('supports_claims', []) or
                ev.get('linked_claims', []) or
                []
            )

            for cid in claim_refs:
                reverse[evidence_id].add(cid)

        # Check consistency and auto-correct
        self._check_and_correct_mappings(
            forward, reverse,
            'claims', 'evidence',
            'Claim', 'Evidence',
            ['supporting_evidence', 'supported_by_evidence', 'supported_by', 'evidence_links'],
            ['supports_claims', 'linked_claims']
        )

    def validate_method_design_mappings(self) -> None:
        """
        Validate Method↔Design bidirectional consistency.

        Forward: methods[].implements_designs (or variants) → design IDs
        Reverse: research_designs[].implemented_by_methods → method IDs
        """
        methods = self.data.get('methods', [])
        designs = self.data.get('research_designs', [])

        # Build forward index
        forward = defaultdict(set)
        for method in methods:
            method_id = self._get_id(method, 'methods')
            if not method_id:
                continue

            self.stats['methods_checked'] += 1

            design_refs = (
                method.get('implements_designs', []) or
                method.get('linked_designs', []) or
                method.get('design_context', []) or
                []
            )

            for did in design_refs:
                forward[method_id].add(did)

        # Build reverse index
        reverse = defaultdict(set)
        for design in designs:
            design_id = self._get_id(design, 'research_designs')
            if not design_id:
                continue

            self.stats['designs_checked'] += 1

            method_refs = (
                design.get('implemented_by_methods', []) or
                design.get('supported_by_methods', []) or
                []
            )

            for mid in method_refs:
                reverse[design_id].add(mid)

        # Check consistency
        self._check_and_correct_mappings(
            forward, reverse,
            'methods', 'research_designs',
            'Method', 'Design',
            ['implements_designs', 'linked_designs', 'design_context'],
            ['implemented_by_methods', 'supported_by_methods']
        )

    def validate_protocol_method_mappings(self) -> None:
        """
        Validate Protocol↔Method bidirectional consistency.

        Forward: protocols[].implements_methods (or variants) → method IDs
        Reverse: methods[].implemented_by_protocols → protocol IDs
        """
        protocols = self.data.get('protocols', [])
        methods = self.data.get('methods', [])

        # Build forward index
        forward = defaultdict(set)
        for protocol in protocols:
            protocol_id = self._get_id(protocol, 'protocols')
            if not protocol_id:
                continue

            self.stats['protocols_checked'] += 1

            method_refs = (
                protocol.get('implements_methods', []) or
                protocol.get('linked_methods', []) or
                []
            )

            for mid in method_refs:
                forward[protocol_id].add(mid)

        # Build reverse index
        reverse = defaultdict(set)
        for method in methods:
            method_id = self._get_id(method, 'methods')
            if not method_id:
                continue

            protocol_refs = (
                method.get('implemented_by_protocols', []) or
                []
            )

            for pid in protocol_refs:
                reverse[method_id].add(pid)

        # Check consistency
        self._check_and_correct_mappings(
            forward, reverse,
            'protocols', 'methods',
            'Protocol', 'Method',
            ['implements_methods', 'linked_methods'],
            ['implemented_by_protocols']
        )

    def _check_and_correct_mappings(
        self,
        forward: Dict[str, Set[str]],
        reverse: Dict[str, Set[str]],
        source_type: str,
        target_type: str,
        source_label: str,
        target_label: str,
        forward_fields: List[str],
        reverse_fields: List[str]
    ) -> None:
        """
        Generic bidirectional mapping validator and auto-corrector.

        Args:
            forward: {source_id: {target_ids}} from source items
            reverse: {target_id: {source_ids}} from target items
            source_type: 'claims', 'methods', 'protocols'
            target_type: 'evidence', 'research_designs', 'methods'
            source_label: Human-readable label for source
            target_label: Human-readable label for target
            forward_fields: Possible field names for forward references
            reverse_fields: Possible field names for reverse references
        """
        # Check forward → reverse consistency
        for source_id, target_ids in forward.items():
            for target_id in target_ids:
                # Check if reverse mapping exists
                if source_id not in reverse.get(target_id, set()):
                    # Missing reverse mapping - auto-correct
                    target_item = self._get_item_by_id(target_type, target_id)
                    if target_item:
                        # Find which reverse field exists (or use first option)
                        reverse_field = None
                        for field in reverse_fields:
                            if field in target_item:
                                reverse_field = field
                                break
                        if not reverse_field:
                            reverse_field = reverse_fields[0]
                            target_item[reverse_field] = []

                        # Add missing reverse mapping
                        if source_id not in target_item[reverse_field]:
                            target_item[reverse_field].append(source_id)
                            self.corrections_made.append(
                                f"Added reverse mapping: {target_label} {target_id}.{reverse_field} ← {source_label} {source_id}"
                            )
                            self.stats['corrections_made'] += 1

        # Check reverse → forward consistency
        for target_id, source_ids in reverse.items():
            for source_id in source_ids:
                # Check if forward mapping exists
                if target_id not in forward.get(source_id, set()):
                    # Missing forward mapping - could be conflict
                    source_item = self._get_item_by_id(source_type, source_id)
                    if source_item:
                        # Check if source has ANY forward references
                        has_forward = False
                        for field in forward_fields:
                            if field in source_item and source_item[field]:
                                has_forward = True
                                break

                        if not has_forward:
                            # No forward refs - auto-correct by adding
                            forward_field = None
                            for field in forward_fields:
                                if field in source_item:
                                    forward_field = field
                                    break
                            if not forward_field:
                                forward_field = forward_fields[0]
                                source_item[forward_field] = []

                            source_item[forward_field].append(target_id)
                            self.corrections_made.append(
                                f"Added forward mapping: {source_label} {source_id}.{forward_field} → {target_label} {target_id}"
                            )
                            self.stats['corrections_made'] += 1
                        else:
                            # Has forward refs but doesn't include this target - potential conflict
                            self.conflicts_found.append(
                                f"CONFLICT: {target_label} {target_id} points to {source_label} {source_id}, "
                                f"but {source_label} {source_id} points elsewhere. Manual review needed."
                            )
                            self.stats['conflicts_found'] += 1

    def run(self) -> dict:
        """Run all validation checks and return results."""
        print(f"Validating bidirectional mappings in: {self.extraction_path}")
        print("=" * 80)

        # Run validators
        self.validate_claim_evidence_mappings()
        self.validate_method_design_mappings()
        self.validate_protocol_method_mappings()

        # Generate report
        self._print_report()

        # Save corrections if any were made
        if self.stats['corrections_made'] > 0:
            print(f"\nSaving {self.stats['corrections_made']} corrections to {self.extraction_path}")
            self._save_extraction()

        return {
            'stats': self.stats,
            'corrections': self.corrections_made,
            'conflicts': self.conflicts_found
        }

    def _print_report(self):
        """Print validation report."""
        print("\n" + "=" * 80)
        print("VALIDATION RESULTS")
        print("=" * 80)

        print(f"\nItems checked:")
        print(f"  Claims: {self.stats['claims_checked']}")
        print(f"  Evidence: {self.stats['evidence_checked']}")
        print(f"  Methods: {self.stats['methods_checked']}")
        print(f"  Protocols: {self.stats['protocols_checked']}")
        print(f"  Research Designs: {self.stats['designs_checked']}")

        print(f"\nCorrections made: {self.stats['corrections_made']}")
        if self.corrections_made:
            for correction in self.corrections_made:
                print(f"  ✓ {correction}")

        print(f"\nConflicts requiring human review: {self.stats['conflicts_found']}")
        if self.conflicts_found:
            for conflict in self.conflicts_found:
                print(f"  ⚠️  {conflict}")

        if self.stats['corrections_made'] == 0 and self.stats['conflicts_found'] == 0:
            print("\n✅ All bidirectional mappings are consistent! No corrections needed.")
        elif self.stats['conflicts_found'] > 0:
            print(f"\n⚠️  {self.stats['conflicts_found']} conflicts require manual resolution.")
        else:
            print(f"\n✅ {self.stats['corrections_made']} corrections made successfully.")


def main():
    """Main entry point."""
    if len(sys.argv) != 2:
        print("Usage: python3 validate_bidirectional.py <path_to_extraction.json>")
        print("\nExample:")
        print("  python3 validate_bidirectional.py outputs/paper-name/extraction.json")
        sys.exit(1)

    extraction_path = sys.argv[1]

    try:
        validator = BidirectionalValidator(extraction_path)
        results = validator.run()

        # Exit with appropriate code
        if results['stats']['conflicts_found'] > 0:
            sys.exit(2)  # Conflicts require human review
        elif results['stats']['corrections_made'] > 0:
            sys.exit(0)  # Corrections made successfully
        else:
            sys.exit(0)  # Already consistent

    except Exception as e:
        print(f"\n❌ Error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
