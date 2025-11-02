#!/usr/bin/env python3
"""
RDMAP Completeness Checker

Validates RDMAP extraction completeness and hierarchy integrity. Part of systematic
quality improvement to catch missing RDMAP elements and broken hierarchies.

Usage:
    python3 check_rdmap_completeness.py <path_to_extraction.json>

    Or from extraction workflow:
    python3 extraction-system/scripts/check_rdmap_completeness.py outputs/paper-name/extraction.json

Validation checks:
    - RDMAP hierarchy completeness (Design → Method → Protocol chains)
    - Orphaned items (Methods without Designs, Protocols without Methods)
    - Missing tier coverage (papers with no Designs, Methods, or Protocols)
    - Protocol→Method linkage rate (should be ≥80%)
    - Expected RDMAP minimum thresholds based on paper type

Author: Claude Sonnet 4.5
Date: 2025-11-02
"""

import json
import sys
from pathlib import Path
from typing import Dict, List, Set, Tuple
from collections import defaultdict


class RDMAPCompletenessChecker:
    """Validates RDMAP extraction completeness and hierarchy integrity."""

    def __init__(self, extraction_path: str):
        self.extraction_path = Path(extraction_path)
        self.data = self._load_extraction()
        self.issues = []
        self.warnings = []
        self.stats = {
            'designs_count': 0,
            'methods_count': 0,
            'protocols_count': 0,
            'orphaned_methods': 0,
            'orphaned_protocols': 0,
            'unlinked_protocols': 0,
            'protocol_linkage_rate': 0.0,
            'missing_tiers': []
        }

    def _load_extraction(self) -> dict:
        """Load extraction.json file."""
        if not self.extraction_path.exists():
            raise FileNotFoundError(f"Extraction file not found: {self.extraction_path}")

        with open(self.extraction_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def _get_id(self, item: dict, item_type: str) -> str | None:
        """Get ID from item, handling multiple field name variants."""
        id_fields = {
            'methods': ['method_id', 'id'],
            'protocols': ['protocol_id', 'id'],
            'research_designs': ['design_id', 'research_design_id', 'id']
        }

        for field in id_fields.get(item_type, ['id']):
            if field in item:
                return item[field]
        return None

    def check_tier_coverage(self) -> None:
        """Check that all three RDMAP tiers are present."""
        designs = self.data.get('research_designs', [])
        methods = self.data.get('methods', [])
        protocols = self.data.get('protocols', [])

        self.stats['designs_count'] = len(designs)
        self.stats['methods_count'] = len(methods)
        self.stats['protocols_count'] = len(protocols)

        missing_tiers = []

        if len(designs) == 0:
            missing_tiers.append('research_designs')
            self.issues.append(
                "CRITICAL: No research designs extracted. Every paper should have ≥1 design "
                "describing the strategic approach (e.g., 'Systematic survey design', "
                "'Comparative analysis design', 'Experimental control design')."
            )

        if len(methods) == 0:
            missing_tiers.append('methods')
            self.issues.append(
                "CRITICAL: No methods extracted. Every empirical paper should have ≥1 method "
                "describing WHAT was done (e.g., 'Remote sensing analysis', 'Survey sampling', "
                "'Statistical analysis')."
            )

        if len(protocols) == 0:
            missing_tiers.append('protocols')
            self.warnings.append(
                "WARNING: No protocols extracted. Most papers have ≥1 protocol describing HOW "
                "methods were implemented. Check if methodological details are missing or "
                "implicitly referenced."
            )

        self.stats['missing_tiers'] = missing_tiers

    def check_hierarchy_integrity(self) -> None:
        """
        Check RDMAP hierarchy completeness and identify orphaned items.

        Every Method should connect to ≥1 Design.
        Every Protocol should connect to ≥1 Method.
        """
        methods = self.data.get('methods', [])
        protocols = self.data.get('protocols', [])
        designs = self.data.get('research_designs', [])

        # Build ID sets for existence checking
        design_ids = {self._get_id(d, 'research_designs') for d in designs}
        method_ids = {self._get_id(m, 'methods') for m in methods}

        # Check orphaned methods (no parent design)
        # Note: Some methods may be referenced from designs via child_methods/enables_methods
        # but not have reverse references. Build forward index from designs first.
        design_to_methods = defaultdict(set)
        for design in designs:
            design_id = self._get_id(design, 'research_designs')
            # Check multiple possible field names for forward references
            method_refs = (
                design.get('child_methods', []) or
                design.get('enables_methods', []) or
                design.get('implemented_by_methods', []) or
                []
            )
            for mid in method_refs:
                design_to_methods[mid].add(design_id)

        orphaned_methods = []
        for method in methods:
            method_id = self._get_id(method, 'methods')

            # Check reverse references in method
            design_refs = (
                method.get('implements_designs', []) or
                method.get('linked_designs', []) or
                method.get('design_context', []) or
                []
            )

            # Also check if method is referenced from any design
            referenced_from_designs = design_to_methods.get(method_id, set())

            # Method is orphaned if it has no reverse refs AND is not referenced from any design
            if not design_refs and not referenced_from_designs:
                orphaned_methods.append(method_id)
                self.issues.append(
                    f"Orphaned method {method_id}: No parent design referenced. "
                    f"Every method must implement ≥1 research design."
                )

            # Check if referenced designs exist
            for did in design_refs:
                if did not in design_ids:
                    self.issues.append(
                        f"Broken reference: method {method_id} references non-existent "
                        f"design '{did}'"
                    )

        self.stats['orphaned_methods'] = len(orphaned_methods)

        # Check orphaned protocols (no parent method)
        # Build forward index from methods to protocols first
        method_to_protocols = defaultdict(set)
        for method in methods:
            method_id = self._get_id(method, 'methods')
            # Check multiple possible field names for forward references
            protocol_refs = (
                method.get('realized_through_protocols', []) or
                method.get('child_protocols', []) or
                method.get('implemented_by_protocols', []) or
                []
            )
            for pid in protocol_refs:
                method_to_protocols[pid].add(method_id)

        orphaned_protocols = []
        unlinked_protocols = []

        for protocol in protocols:
            protocol_id = self._get_id(protocol, 'protocols')

            # Check reverse references in protocol (handles both plural and singular forms)
            method_refs_list = protocol.get('implements_methods', [])
            method_refs_singular = protocol.get('implements_method')

            if method_refs_singular and not method_refs_list:
                # Handle singular form by converting to list
                method_refs = [method_refs_singular]
            else:
                method_refs = method_refs_list or protocol.get('linked_methods', []) or []

            # Also check if protocol is referenced from any method
            referenced_from_methods = method_to_protocols.get(protocol_id, set())

            # Protocol is orphaned if it has no reverse refs AND is not referenced from any method
            if not method_refs and not referenced_from_methods:
                orphaned_protocols.append(protocol_id)
                unlinked_protocols.append(protocol_id)
                self.issues.append(
                    f"Orphaned protocol {protocol_id}: No parent method referenced. "
                    f"Every protocol must implement ≥1 method."
                )

            # Check if referenced methods exist
            for mid in method_refs:
                if mid not in method_ids:
                    self.issues.append(
                            f"Broken reference: protocol {protocol_id} references non-existent "
                            f"method '{mid}'"
                        )

        self.stats['orphaned_protocols'] = len(orphaned_protocols)
        self.stats['unlinked_protocols'] = len(unlinked_protocols)

        # Calculate protocol linkage rate
        if len(protocols) > 0:
            linked_protocols = len(protocols) - len(unlinked_protocols)
            self.stats['protocol_linkage_rate'] = (linked_protocols / len(protocols)) * 100
        else:
            self.stats['protocol_linkage_rate'] = 0.0

    def check_linkage_completeness(self) -> None:
        """
        Check Protocol→Method linkage rate and flag if below acceptable threshold.

        Acceptable: ≥80% of protocols linked
        Warning: 50-79% of protocols linked
        Critical: <50% of protocols linked
        """
        protocol_count = self.stats['protocols_count']
        linkage_rate = self.stats['protocol_linkage_rate']

        if protocol_count == 0:
            return  # Already flagged in tier coverage check

        if linkage_rate < 50:
            self.issues.append(
                f"CRITICAL: Only {linkage_rate:.1f}% of protocols linked to methods "
                f"({protocol_count - self.stats['unlinked_protocols']}/{protocol_count}). "
                f"Target: ≥80%. This indicates systematic extraction issue - protocols not "
                f"connected to methodological framework."
            )
        elif linkage_rate < 80:
            self.warnings.append(
                f"WARNING: Only {linkage_rate:.1f}% of protocols linked to methods "
                f"({protocol_count - self.stats['unlinked_protocols']}/{protocol_count}). "
                f"Target: ≥80%. Consider reviewing protocol extraction for missing parent "
                f"method references."
            )
        else:
            # Good linkage rate
            pass

    def check_minimum_thresholds(self) -> None:
        """
        Check against expected minimum RDMAP counts based on paper type heuristics.

        Heuristics (empirical papers):
        - Research Designs: ≥1 (strategic approach)
        - Methods: ≥2 (typically data collection + analysis)
        - Protocols: ≥3 (operational details for methods)

        Lower thresholds acceptable for:
        - Short papers (<10 pages)
        - Purely theoretical papers
        - Review papers
        """
        designs = self.stats['designs_count']
        methods = self.stats['methods_count']
        protocols = self.stats['protocols_count']

        # Get paper metadata if available
        metadata = self.data.get('project_metadata', {})
        paper_title = metadata.get('paper_title', 'Unknown')

        # Design threshold (always ≥1 for empirical papers)
        if designs == 0:
            self.issues.append(
                f"CRITICAL: Zero research designs. Every empirical paper should describe "
                f"≥1 strategic design decision."
            )
        elif designs < 1:
            self.warnings.append(
                f"WARNING: Only {designs} research design(s). Most papers have 2-4 designs "
                f"(e.g., sampling design, analytical design, validation design)."
            )

        # Method threshold (typically ≥2 for empirical papers)
        if methods < 2:
            self.warnings.append(
                f"WARNING: Only {methods} method(s). Most empirical papers have ≥2 methods "
                f"(data collection + analysis). Check for under-extraction."
            )

        # Protocol threshold (typically ≥3 for empirical papers)
        if protocols < 3:
            self.warnings.append(
                f"WARNING: Only {protocols} protocol(s). Most empirical papers have ≥3 "
                f"protocols providing operational details. Check if HOW-level details missed."
            )

    def check_design_method_balance(self) -> None:
        """
        Check if Methods:Designs ratio is reasonable.

        Typical ratios:
        - Simple papers: 2-4 methods per design
        - Complex papers: 4-8 methods per design
        - Very high ratio (>10): Possible over-extraction of methods or under-extraction of designs
        """
        designs = self.stats['designs_count']
        methods = self.stats['methods_count']

        if designs == 0:
            return  # Already flagged

        ratio = methods / designs

        if ratio > 10:
            self.warnings.append(
                f"WARNING: Methods:Designs ratio is {ratio:.1f}:1 ({methods} methods, "
                f"{designs} designs). Very high ratio may indicate: (1) over-extraction of "
                f"methods, (2) under-extraction of designs, or (3) genuinely complex multi-method "
                f"paper. Review design extraction for missing strategic approaches."
            )
        elif ratio < 1:
            self.warnings.append(
                f"WARNING: Methods:Designs ratio is {ratio:.1f}:1 ({methods} methods, "
                f"{designs} designs). More designs than methods is unusual. Check if items "
                f"misclassified between tiers."
            )

    def run(self) -> dict:
        """Run all completeness checks and return results."""
        print(f"Checking RDMAP completeness: {self.extraction_path}")
        print("=" * 80)

        # Run checks
        self.check_tier_coverage()
        self.check_hierarchy_integrity()
        self.check_linkage_completeness()
        self.check_minimum_thresholds()
        self.check_design_method_balance()

        # Generate report
        self._print_report()

        return {
            'stats': self.stats,
            'issues': self.issues,
            'warnings': self.warnings
        }

    def _print_report(self):
        """Print completeness report."""
        print("\n" + "=" * 80)
        print("RDMAP COMPLETENESS REPORT")
        print("=" * 80)

        print(f"\nRDMAP item counts:")
        print(f"  Research Designs: {self.stats['designs_count']}")
        print(f"  Methods: {self.stats['methods_count']}")
        print(f"  Protocols: {self.stats['protocols_count']}")

        print(f"\nHierarchy integrity:")
        print(f"  Orphaned methods (no parent design): {self.stats['orphaned_methods']}")
        print(f"  Orphaned protocols (no parent method): {self.stats['orphaned_protocols']}")
        print(f"  Protocol→Method linkage rate: {self.stats['protocol_linkage_rate']:.1f}%")

        if self.stats['missing_tiers']:
            print(f"\n⚠️  Missing RDMAP tiers: {', '.join(self.stats['missing_tiers'])}")

        if self.issues:
            print(f"\nCritical issues ({len(self.issues)}):")
            for issue in self.issues:
                print(f"  ❌ {issue}")

        if self.warnings:
            print(f"\nWarnings ({len(self.warnings)}):")
            for warning in self.warnings:
                print(f"  ⚠️  {warning}")

        if not self.issues and not self.warnings:
            print("\n✅ RDMAP extraction appears complete with good hierarchy integrity!")
        elif self.issues:
            print(f"\n❌ RDMAP completeness check failed with {len(self.issues)} critical issue(s)")
        else:
            print(f"\n⚠️  RDMAP extraction has {len(self.warnings)} warning(s) - review recommended")


def main():
    """Main entry point."""
    if len(sys.argv) != 2:
        print("Usage: python3 check_rdmap_completeness.py <path_to_extraction.json>")
        print("\nExample:")
        print("  python3 check_rdmap_completeness.py outputs/paper-name/extraction.json")
        sys.exit(1)

    extraction_path = sys.argv[1]

    try:
        checker = RDMAPCompletenessChecker(extraction_path)
        results = checker.run()

        # Exit with appropriate code
        if results['issues']:
            sys.exit(1)  # Critical issues found
        elif results['warnings']:
            sys.exit(0)  # Warnings only (success with notes)
        else:
            sys.exit(0)  # All good

    except Exception as e:
        print(f"\n❌ Error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
