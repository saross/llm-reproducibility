# Pass 1 Extraction Complete - Sobotkova et al. 2023

**Date:** 2025-10-25
**Extractor:** Claude Sonnet 4.5 (research-assessor v2.6)

## Extraction Summary

### Items Extracted
- **Evidence:** 40 items (E001-E040)
- **Claims:** 46 items (C001-C046)
  - Core claims: 10
  - Intermediate claims: 15
  - Supporting claims: 21
- **Implicit Arguments:** 7 items (IA001-IA007)

### Sections Processed
✅ Abstract
✅ Introduction (1-1.4)
✅ Approach/Methods (2-2.5)
✅ Results (3-3.5)
✅ Discussion (4-4.3)
✅ Conclusion (5)

### Quality Metrics
- All evidence items have verbatim quotes
- All claims have verbatim quotes
- All implicit arguments have trigger_text + trigger_locations
- Systematic implicit argument search completed for all core claims
- Liberal extraction strategy applied (intentional over-capture)

### Core Claims Identified
1. C001: Crowdsourcing produced large, accurate, analysis-ready dataset
2. C002: Approach required little training/supervision
3. C003: Most efficient for 10,000-60,000 features
4. C004: Field data collection systems can be customised for participatory GIS
5. C005: Approach complements ML (less expertise/time/resourcing)
6. C039: Thresholds for when crowdsourcing becomes worthwhile
7. C040: Above 60,000 records, use ML (if expertise available)
8. C042: Crowdsourcing and ML are complementary
9. C043: Typical projects can deploy crowdsourcing but may not access ML
10. C045: Approach is readily transferable

### Known Limitations (for Pass 2)
- Some track record items (E008, E016) may move to project_metadata
- Liberal extraction produced granular items for consolidation
- Some claims lack direct evidence (literature review sections)

### Next: Pass 2 Rationalization
**Target reduction:** 15-20%
- Evidence: 40 → 32-34 items
- Claims: 46 → 36-39 items
- Review implicit arguments for completeness
