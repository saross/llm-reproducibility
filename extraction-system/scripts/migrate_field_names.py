#!/usr/bin/env python3
"""
Schema Field Name Migration Script

Standardises field names across all extractions to canonical schema v2.5 names.
Uses canonical names from research-assessor skill schema-guide.md.

Usage:
    python3 migrate_field_names.py --audit              # Report variants only (read-only)
    python3 migrate_field_names.py --test PAPER_NAME    # Test single extraction, show diff
    python3 migrate_field_names.py --migrate-all        # Batch migrate all extractions
    python3 migrate_field_names.py --dry-run PAPER_NAME # Show changes without writing

Author: Claude Sonnet 4.5
Date: 2025-11-02
"""

import json
import sys
import argparse
from pathlib import Path
from typing import Dict, List, Set, Tuple
from collections import defaultdict
import shutil
from datetime import datetime


# Canonical field name mappings (from research-assessor skill schema-guide.md)
FIELD_MIGRATIONS = {
    'research_designs': {
        'child_methods': 'implemented_by_methods',
        'enables_methods': 'implemented_by_methods',
        'supported_by_methods': 'implemented_by_methods'
    },
    'methods': {
        'linked_designs': 'implements_designs',
        'design_context': 'implements_designs',
        'child_protocols': 'realized_through_protocols',
        'implemented_by_protocols': 'realized_through_protocols'
    },
    'protocols': {
        'implements_method': 'implements_methods',  # Singular → Plural
        'linked_methods': 'implements_methods'
    },
    'claims': {
        'supported_by_evidence': 'supported_by',
        'supporting_evidence': 'supported_by'
    }
}


class FieldNameMigrator:
    """Migrates field names in extraction.json files to canonical schema v2.5 names."""

    def __init__(self, outputs_dir: str = "outputs"):
        self.outputs_dir = Path(outputs_dir)
        self.variant_report = defaultdict(lambda: defaultdict(list))

    def find_all_extractions(self) -> List[Path]:
        """Find all extraction.json files in outputs directory."""
        extractions = []
        for paper_dir in sorted(self.outputs_dir.iterdir()):
            if paper_dir.is_dir():
                extraction_file = paper_dir / "extraction.json"
                if extraction_file.exists():
                    extractions.append(extraction_file)
        return extractions

    def load_extraction(self, path: Path) -> dict:
        """Load extraction.json file."""
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def save_extraction(self, path: Path, data: dict, backup: bool = True):
        """Save extraction.json file with optional backup."""
        if backup:
            backup_path = path.parent / f"{path.stem}.backup-{datetime.now().strftime('%Y%m%d-%H%M%S')}.json"
            shutil.copy2(path, backup_path)
            print(f"  Backup created: {backup_path.name}")

        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def audit_extraction(self, path: Path) -> Dict[str, List[str]]:
        """Audit single extraction for field name variants."""
        data = self.load_extraction(path)
        variants_found = {}

        for object_type in ['research_designs', 'methods', 'protocols', 'claims']:
            items = data.get(object_type, [])
            if not items:
                continue

            type_variants = []
            migrations = FIELD_MIGRATIONS.get(object_type, {})

            for item in items:
                item_id = item.get(f'{object_type[:-1]}_id') or item.get('design_id') or item.get('id', 'UNKNOWN')
                for variant_name in migrations.keys():
                    if variant_name in item:
                        type_variants.append(f"{item_id}: {variant_name}")
                        self.variant_report[path.parent.name][f"{object_type}.{variant_name}"].append(item_id)

            if type_variants:
                variants_found[object_type] = type_variants

        return variants_found

    def migrate_extraction(self, path: Path, dry_run: bool = False) -> Tuple[int, Dict[str, int]]:
        """Migrate field names in single extraction."""
        data = self.load_extraction(path)
        total_changes = 0
        changes_by_type = defaultdict(int)

        for object_type in ['research_designs', 'methods', 'protocols', 'claims']:
            items = data.get(object_type, [])
            if not items:
                continue

            migrations = FIELD_MIGRATIONS.get(object_type, {})

            for item in items:
                for variant_name, canonical_name in migrations.items():
                    if variant_name in item:
                        # Get the value
                        value = item[variant_name]

                        # If canonical field already exists, merge values
                        if canonical_name in item:
                            # Merge arrays, remove duplicates
                            if isinstance(value, list) and isinstance(item[canonical_name], list):
                                merged = list(set(item[canonical_name] + value))
                                item[canonical_name] = merged
                                print(f"    Merged {variant_name} → {canonical_name}: {value} + {item[canonical_name]} = {merged}")
                            else:
                                print(f"    WARNING: Both {variant_name} and {canonical_name} exist with incompatible types")
                        else:
                            # Simple rename
                            item[canonical_name] = value

                        # Remove old field
                        del item[variant_name]

                        total_changes += 1
                        changes_by_type[f"{object_type}.{variant_name}→{canonical_name}"] += 1

        # Add migration metadata to extraction_notes
        if total_changes > 0 and not dry_run:
            if 'extraction_notes' not in data:
                data['extraction_notes'] = {}

            # Handle case where extraction_notes might be a list (legacy format)
            if isinstance(data['extraction_notes'], list):
                # Convert list to dict, preserving list content as 'notes' field
                data['extraction_notes'] = {
                    'legacy_notes': data['extraction_notes']
                }

            data['extraction_notes']['field_migration'] = {
                'migrated_at': datetime.now().isoformat(),
                'script_version': '1.0',
                'changes_applied': total_changes,
                'canonical_schema_version': '2.5'
            }

        if not dry_run and total_changes > 0:
            self.save_extraction(path, data, backup=True)

        return total_changes, dict(changes_by_type)

    def audit_all(self):
        """Audit all extractions and report variants found."""
        print("=" * 80)
        print("FIELD NAME VARIANT AUDIT")
        print("=" * 80)
        print()

        extractions = self.find_all_extractions()
        print(f"Found {len(extractions)} extraction(s) to audit\n")

        papers_with_variants = 0
        total_variants = 0

        for extraction_path in extractions:
            variants = self.audit_extraction(extraction_path)
            if variants:
                papers_with_variants += 1
                paper_name = extraction_path.parent.name
                print(f"\n{paper_name}:")
                for object_type, variant_list in variants.items():
                    print(f"  {object_type}:")
                    for variant in variant_list:
                        print(f"    - {variant}")
                        total_variants += 1

        print("\n" + "=" * 80)
        print("SUMMARY")
        print("=" * 80)
        print(f"Papers with variants: {papers_with_variants}/{len(extractions)}")
        print(f"Total variant instances: {total_variants}")

        if self.variant_report:
            print("\nVariant frequency across corpus:")
            variant_counts = defaultdict(int)
            for paper, variants in self.variant_report.items():
                for variant_name, items in variants.items():
                    variant_counts[variant_name] += len(items)

            for variant_name in sorted(variant_counts.keys(), key=lambda x: variant_counts[x], reverse=True):
                count = variant_counts[variant_name]
                print(f"  {variant_name}: {count} instance(s)")

        return papers_with_variants > 0

    def test_migration(self, paper_name: str, dry_run: bool = False):
        """Test migration on single paper."""
        extraction_path = self.outputs_dir / paper_name / "extraction.json"

        if not extraction_path.exists():
            print(f"ERROR: Extraction not found: {extraction_path}")
            return False

        print("=" * 80)
        print(f"{'DRY RUN: ' if dry_run else ''}MIGRATION TEST: {paper_name}")
        print("=" * 80)
        print()

        # Audit first
        print("Variants found:")
        variants = self.audit_extraction(extraction_path)
        if not variants:
            print("  None - extraction already uses canonical field names")
            return True

        for object_type, variant_list in variants.items():
            print(f"  {object_type}:")
            for variant in variant_list:
                print(f"    - {variant}")

        print("\nApplying migrations...")
        total_changes, changes_by_type = self.migrate_extraction(extraction_path, dry_run=dry_run)

        if total_changes > 0:
            print(f"\n{'Would apply' if dry_run else 'Applied'} {total_changes} change(s):")
            for change_type, count in sorted(changes_by_type.items()):
                print(f"  {change_type}: {count}")
        else:
            print("\nNo changes needed")

        return True

    def migrate_all(self, dry_run: bool = False):
        """Migrate all extractions."""
        print("=" * 80)
        print(f"{'DRY RUN: ' if dry_run else ''}BATCH MIGRATION")
        print("=" * 80)
        print()

        extractions = self.find_all_extractions()
        print(f"Found {len(extractions)} extraction(s) to migrate\n")

        if not dry_run:
            response = input("This will modify all extraction files. Continue? (yes/no): ")
            if response.lower() != 'yes':
                print("Cancelled")
                return False

        total_papers_migrated = 0
        total_changes = 0
        all_changes = defaultdict(int)

        for extraction_path in extractions:
            paper_name = extraction_path.parent.name
            changes, changes_by_type = self.migrate_extraction(extraction_path, dry_run=dry_run)

            if changes > 0:
                total_papers_migrated += 1
                total_changes += changes
                print(f"\n{paper_name}: {changes} change(s)")
                for change_type, count in changes_by_type.items():
                    print(f"  {change_type}: {count}")
                    all_changes[change_type] += count
            else:
                print(f"\n{paper_name}: No changes needed")

        print("\n" + "=" * 80)
        print("MIGRATION SUMMARY")
        print("=" * 80)
        print(f"Papers migrated: {total_papers_migrated}/{len(extractions)}")
        print(f"Total changes: {total_changes}")

        if all_changes:
            print("\nChanges by type:")
            for change_type in sorted(all_changes.keys()):
                print(f"  {change_type}: {all_changes[change_type]}")

        return True


def main():
    parser = argparse.ArgumentParser(
        description="Migrate field names to canonical schema v2.5",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 migrate_field_names.py --audit
  python3 migrate_field_names.py --test ross-et-al-2009
  python3 migrate_field_names.py --dry-run penske-et-al-2023
  python3 migrate_field_names.py --migrate-all
        """
    )

    parser.add_argument('--audit', action='store_true',
                        help='Audit all extractions for field name variants (read-only)')
    parser.add_argument('--test', metavar='PAPER_NAME',
                        help='Test migration on single paper')
    parser.add_argument('--migrate-all', action='store_true',
                        help='Migrate all extractions (requires confirmation)')
    parser.add_argument('--dry-run', metavar='PAPER_NAME',
                        help='Show changes without writing (for single paper)')
    parser.add_argument('--outputs-dir', default='outputs',
                        help='Path to outputs directory (default: outputs)')

    args = parser.parse_args()

    # Validate arguments
    if not any([args.audit, args.test, args.migrate_all, args.dry_run]):
        parser.print_help()
        sys.exit(1)

    if sum([bool(args.audit), bool(args.test), bool(args.migrate_all), bool(args.dry_run)]) > 1:
        print("ERROR: Only one mode can be specified at a time")
        sys.exit(1)

    # Create migrator
    migrator = FieldNameMigrator(outputs_dir=args.outputs_dir)

    # Execute requested mode
    try:
        if args.audit:
            has_variants = migrator.audit_all()
            sys.exit(0 if not has_variants else 1)

        elif args.test:
            success = migrator.test_migration(args.test, dry_run=False)
            sys.exit(0 if success else 1)

        elif args.dry_run:
            success = migrator.test_migration(args.dry_run, dry_run=True)
            sys.exit(0 if success else 1)

        elif args.migrate_all:
            success = migrator.migrate_all(dry_run=False)
            sys.exit(0 if success else 1)

    except Exception as e:
        print(f"\nERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
