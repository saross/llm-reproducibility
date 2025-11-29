# Pass 6 Software Documentation Enhancement Recommendation

**Date:** 2025-11-11
**Context:** Testing Phase 1 infrastructure extraction on Ballsun-Stanton et al. 2018 (SoftwareX)
**Status:** Deferred pending completion of 4-paper test corpus

---

## Gap Identified

During Pass 6 infrastructure extraction on the FAIMS Mobile software publication (Ballsun-Stanton et al. 2018), I identified that **software documentation is not systematically assessed**, despite being critical for FAIR Reusability (R1) and computational reproducibility.

### Current Improvised Approach

Documentation was captured in three scattered locations:
1. Listed documentation URLs in `code_availability.repositories` array
2. Mentioned "Multiple documentation resources" in FAIR R1 rationale text
3. Noted documentation in `analysis_transparency.workflow_description`

**Problem:** No systematic structure, incomplete capture, difficult to query/assess across papers.

---

## Proposed Enhancement

Add a `documentation` sub-object within `code_availability`:

```json
"code_availability": {
  "statement_present": true,
  "statement_type": "available",
  "repositories": [ ... ],
  "computational_reproducibility": { ... },

  "documentation": {
    "types_present": [
      "readme",
      "api_reference",
      "user_manual",
      "installation_guide",
      "tutorial",
      "examples",
      "developer_guide",
      "troubleshooting",
      "changelog",
      "citation_file"
    ],
    "documentation_urls": [
      {
        "type": "api_reference",
        "url": "https://faimsproject.atlassian.net/wiki/x/RwAu",
        "description": "Module Beanshell API",
        "format": "wiki",
        "archived": true,
        "archived_url": "https://perma.cc/H6XJ-X6E2",
        "versioned": true
      },
      {
        "type": "user_manual",
        "url": "https://faimsproject.atlassian.net/wiki/spaces/MobileUser/overview",
        "description": "Getting started guide and user documentation",
        "format": "wiki",
        "archived": false,
        "versioned": true
      },
      {
        "type": "developer_guide",
        "url": "https://faimsproject.atlassian.net/wiki/spaces/FAIMS/overview",
        "description": "Developer documentation home",
        "format": "wiki",
        "archived": false,
        "versioned": false
      },
      {
        "type": "tutorial",
        "url": "https://faimsproject.atlassian.net/wiki/x/RgAu",
        "description": "Module Cookbook",
        "format": "wiki",
        "archived": true,
        "archived_url": "https://perma.cc/H6XJ-X6E2",
        "versioned": false
      },
      {
        "type": "developer_guide",
        "url": "https://github.com/FAIMS/UserToDev",
        "description": "User to Developer documentation",
        "format": "markdown",
        "archived": true,
        "archived_url": "https://perma.cc/M4B3-JJEA",
        "versioned": true
      }
    ],
    "completeness_assessment": "comprehensive",
    "completeness_rationale": "Documentation covers all user types: end users (user manual, getting started), developers (API reference, cookbook), and administrators (installation guide, server setup). Multiple tutorials and examples provided. Versioned with software releases.",
    "quality_indicators": {
      "versioned": true,
      "includes_examples": true,
      "includes_troubleshooting": false,
      "multiple_formats": true,
      "multilingual": false,
      "machine_readable": false,
      "citation_cff_present": false
    },
    "accessibility": {
      "publicly_accessible": true,
      "requires_authentication": false,
      "archive_preserved": true,
      "archive_service": "perma.cc"
    },
    "notes": "Exceptional documentation: API reference, cookbook tutorials, user manual, developer guide, and user-to-developer guide. Documentation versioned with software releases. Use of perma.cc for link persistence is good practice."
  }
}
```

---

## Rationale for Enhancement

### Strengthens FAIR Assessment

**R1 (Reusable - richly described with attributes):**
- Current: Subjective assessment buried in rationale text
- Enhanced: Systematic documentation type inventory, completeness rating, quality indicators

**I1 (Interoperable - formal language):**
- Documentation format matters (Markdown, Sphinx, Doxygen, wiki)
- Machine-readable docs (OpenAPI, citation.cff) vs human-only

**A1 (Accessible - retrievable by identifier):**
- Documentation URLs should be assessed for accessibility
- Archive preservation matters (perma.cc, Internet Archive)

### Supports Computational Reproducibility

Documentation types map to reproducibility levels:
- **Level 1 (code_only)**: Minimal/no documentation
- **Level 2 (code_dependencies)**: Installation guide, README with dependencies
- **Level 3 (containerised)**: Dockerfile documentation, container usage guide
- **Level 4 (fully_reproducible)**: Complete workflow documentation, execution examples

### Enables Cross-Paper Analysis

Systematic structure allows queries like:
- "What percentage of papers cite software with API documentation?"
- "How does documentation completeness correlate with citation count?"
- "Do papers using well-documented software show higher reproducibility?"

---

## Design Considerations from FAIMS Paper

### Documentation Types Taxonomy

**Essential types** (observed in FAIMS):
- `readme` - Basic project description
- `installation_guide` - Setup instructions
- `user_manual` - End-user documentation
- `api_reference` - Technical API documentation
- `developer_guide` - Contributing/development docs
- `tutorial` - Step-by-step learning materials
- `examples` - Working code examples
- `troubleshooting` - Common issues and solutions
- `changelog` - Version history
- `citation_file` - citation.cff, CITATION.txt

**Emerging types** (not in FAIMS but important):
- `openapi_spec` - Machine-readable API docs
- `jupyter_notebooks` - Executable documentation
- `video_tutorials` - Multimedia documentation

### Completeness Assessment Scale

Proposed 5-level scale:
- **none**: No documentation beyond code comments
- **minimal**: README only
- **basic**: README + installation guide
- **good**: README + installation + user manual or API reference
- **comprehensive**: Multiple documentation types covering all user personas (end user, developer, admin)

### Quality Indicators

**Boolean flags** easy to extract:
- `versioned` - Documentation tracks software versions
- `includes_examples` - Working code examples present
- `includes_troubleshooting` - FAQ/troubleshooting section
- `multiple_formats` - HTML + PDF, wiki + Markdown, etc.
- `multilingual` - Non-English documentation available
- `machine_readable` - OpenAPI, citation.cff, CodeMeta, codemeta.json
- `citation_cff_present` - CITATION.cff file in repository

---

## Questions for Testing on Papers 2-4

### From Software Creator Perspective (FAIMS paper showed):
- ✅ Multiple documentation types provided
- ✅ Documentation versioned with releases
- ✅ Archive preservation used (perma.cc)
- ❌ No machine-readable citation file (citation.cff)

### From Software User Perspective (next 3 papers will show):
1. **How is software cited?**
   - With version numbers?
   - With documentation URLs?
   - With generic package names only?

2. **Which documentation types are referenced?**
   - Installation guides for reproducibility?
   - API references for methods?
   - User manuals for training?

3. **Software with poor/missing documentation:**
   - How does that affect reproducibility assessment?
   - How do we score absence?

4. **Proprietary vs open-source software:**
   - Different documentation expectations?
   - Vendor docs vs community docs?

5. **Domain-specific tools:**
   - Archaeological GIS tools
   - Statistical packages (R, Python)
   - Specialised field software
   - How is documentation quality/accessibility different?

---

## Implementation Timeline

**Phase 1 (Current):** Test Pass 6 on 4 papers
- Ballsun-Stanton et al. 2018 (software publication) ✅ COMPLETED
- Sobotkova et al. 2024 (recent fieldwork)
- Penske et al. 2023 (collaborative)
- Sobotkova et al. 2016 (mid-period)

**Phase 2 (After testing):** Design enhancement based on evidence
- Finalize `documentation` object structure
- Add documentation assessment to FAIR R1 scoring rubric
- Update `fair-principles-guide.md` with documentation guidance
- Extend `reproducibility-infrastructure-schema.md`
- Update Pass 6 prompt with documentation extraction workflow

**Phase 3 (Implementation):** Deploy enhancement
- Test on 2-3 papers with revised schema
- Validate documentation assessment approach
- Document in skill references

---

## Expected Benefits

### Improved FAIR Assessment Precision

**Before enhancement:**
```json
"R1_richly_described_with_attributes": {
  "score": 1,
  "rationale": "Extensive attributes... Multiple documentation resources (Cookbook, API docs, User guide)."
}
```

**After enhancement:**
```json
"R1_richly_described_with_attributes": {
  "score": 1,
  "rationale": "Comprehensive documentation with 5 distinct types (API reference, user manual, developer guide, cookbook, installation guide). All documentation versioned and publicly accessible. Archive preserved via perma.cc. Missing machine-readable citation file (citation.cff) which would further enhance discoverability.",
  "documentation_completeness": "comprehensive",
  "documentation_types_count": 5,
  "documentation_versioned": true,
  "documentation_archived": true
}
```

### Quantifiable Metrics

Enable assessment metrics like:
- Documentation completeness percentage (types present / types expected for software type)
- Documentation accessibility score (public + versioned + archived + machine-readable)
- Documentation-reproducibility correlation

### Cross-Paper Comparison

Enable questions like:
- "Which papers cite software with comprehensive documentation?"
- "Does documentation quality predict successful replication?"
- "What documentation types are most frequently missing?"

---

## Alternative Approaches Considered

### Option A: Separate Documentation Assessment Section
**Rejected** - Documentation is intrinsic to code availability, not separate infrastructure

### Option B: Documentation URLs Only (No Quality Assessment)
**Rejected** - Loses critical reusability information. Need completeness/quality indicators.

### Option C: Free-Text Documentation Notes Only
**Rejected** - Not queryable, not comparable across papers. Need structured data.

### Option D: Recommended Approach (Structured Sub-Object)
**Selected** - Systematic, queryable, preserves context within code_availability

---

## Next Steps

1. **Complete Pass 6 testing on 3 remaining papers** (sobotkova-et-al-2024, penske-et-al-2023, sobotkova-et-al-2016)
2. **Document observations** about software citation and documentation patterns
3. **Refine documentation object structure** based on empirical evidence
4. **Update schema and prompts** with documentation assessment workflow
5. **Re-test** on diverse papers to validate approach

---

## References

- **FAIR4RS Principles** (Chue Hong et al. 2022): R1.1 - "Software is given a clear and accessible license", R1.2 - "Software is associated with detailed provenance"
- **Software Citation Principles** (Smith et al. 2016): Importance of version, documentation, and persistent identifiers
- **CodeMeta** - Machine-readable software metadata standard including documentation fields
- **citation.cff format** - CITATION.cff files for software citation metadata

---

**Document Version:** 1.0
**Status:** Recommendation pending testing completion
**Next Review:** After completion of 4-paper test corpus
