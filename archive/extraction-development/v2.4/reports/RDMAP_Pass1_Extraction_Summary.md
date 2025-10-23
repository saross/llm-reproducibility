# RDMAP Pass 1 Extraction Summary
## Sobotkova et al. 2023 - Methods Section

**Date:** October 20, 2025  
**Pass:** RDMAP Pass 1 (Liberal Extraction)  
**Section:** Methods (Section 2: subsections 2.1-2.5)  
**Approach:** Liberal extraction with over-capture acceptable

---

## Extraction Results

### Total Items Extracted: 27 RDMAP items

**Research Designs (WHY decisions):** 5 items
- RD001: Research goal (extract archaeological features from Soviet maps)
- RD002: Crowdsourcing approach decision (vs expert/ML alternatives)
- RD003: Mobile platform choice (vs desktop GIS)
- RD004: Division of labor design (staff technical, volunteers digitise)
- RD005: Systematic evaluation approach (opportunistic decision)

**Methods (WHAT approaches):** 7 items
- M001: Target feature identification from map symbols
- M002: Crowdsourcing with student volunteers
- M003: Platform selection through comparative assessment
- M004: FAIMS Mobile customization
- M005: Streamlined interface design
- M006: Time-tracking for all participants
- M007: Random sampling for error characterization

**Protocols (HOW specifics):** 15 items
- P001: Map material specifications (scale, format, density)
- P002: Target symbol and feature specifications
- P003: Volunteer training protocol (minutes required)
- P004: Volunteer supervision protocol (30 min per season)
- P005: Work environment and timing (rainy days, contingent)
- P006: Platform evaluation criteria (comprehensive requirements)
- P007: Customization development protocol (35h developer, AUD $2k)
- P008: Seven-stage implementation workflow
- P009: System setup protocol (3h initial, 1h reuse)
- P010: Map preparation protocol (tiling, pyramids, transfer)
- P011: Automated system capabilities (metadata, validation, merging)
- P012: Interface design - dual view system (map/form toggle)
- P013: Interface design - control minimization
- P014: Time tracking data sources (timesheets, timestamps, journals)
- P015: Error checking via random map review

---

## Complete Extraction Status

### From Discussion Section (Pass 2 - completed previously):
- **Evidence:** 13 items
- **Claims:** 16 items  
- **Implicit Arguments:** 10 items

### From Methods Section (Pass 1 - just completed):
- **Research Designs:** 5 items
- **Methods:** 7 items
- **Protocols:** 15 items

**GRAND TOTAL: 66 items across all arrays**

---

## Key Features of This Extraction

### 1. Reasoning Approaches Classified
All 5 research designs analyzed for reasoning approach:
- **Unclear:** RD001 (inventory goal, not hypothesis-testing)
- **Abductive:** RD002 (problem-solving from 2010 failure)
- **Deductive:** RD003, RD004 (applying HCI/usability principles)
- **Inductive:** RD005 (emergent evaluation from observed success)

### 2. Opportunistic & Contingent Decisions Flagged
- **Opportunistic:** RD005 (evaluation plan emerged during fieldwork)
- **Contingent:** P005 (weather-dependent digitisation scheduling)

### 3. Theoretical Frameworks Extracted
- RD003 cites HCI and mobile data collection literature
- Usability principles: limit cognitive load, focus on essentials
- Mobile UI principles: unobtrusive, quick entry, automated metadata

### 4. Cross-References Populated
- All research designs link to methods they enable
- All methods link to protocols they use
- Bidirectional consistency maintained

### 5. Missing Information Documented
Expected information gaps flagged across all items, including:
- Formal research questions/hypotheses
- Systematic decision frameworks (scoring, weighting)
- Detailed protocols (training materials, error definitions)
- Inter-rater reliability testing
- Statistical justifications (sample sizes, power)

---

## Pass 1 Quality Notes

### Liberal Extraction Applied
✓ Included items even when tier assignment uncertain  
✓ Documented alternatives in extraction_notes  
✓ Preserved granularity for assessment flexibility  
✓ Over-extraction acceptable at this stage  

### Extraction Confidence
- **High:** Most research designs and methods (well-documented in source)
- **Medium:** Some protocols (lacking detailed documentation in Methods section)
- **Conservative:** Where source was vague, documented uncertainty

### Consolidation Candidates for Pass 2
- P009 + P010 could merge as "system preparation protocol"
- P012 + P013 could merge as "interface design protocol"
- Some protocol granularity may be excessive

---

## Ready for Pass 2

The extraction is **ready for RDMAP Pass 2 (rationalization)**.

### Pass 2 Focus Areas:
1. Consolidate related protocols (setup, preparation, configuration)
2. Verify tier assignments (particularly boundary cases)
3. Enhance cross-references to Discussion claims (if applicable)
4. Rationalize granularity against assessment needs
5. Target ~15-20% reduction through consolidation

### Expected Outcome:
- Research Designs: likely stable (5 items)
- Methods: possibly 6-7 items (minimal consolidation)
- Protocols: likely 10-12 items (consolidate setup/config/prep)
- **Total after Pass 2: approximately 21-24 RDMAP items**

---

## Notes on Extraction Decisions

### Tier Assignment Logic
- **Research Design:** Strategic WHY decisions and rationale
- **Method:** Tactical WHAT approaches at high level
- **Protocol:** Operational HOW with specific details

### Boundary Cases
- Platform selection (M003) vs requirements (P006): Separated by specificity
- Interface design principles (M005) vs specifications (P012, P013): Separated by abstraction level

### Temporal Coverage
- Both 2017 and 2018 field seasons documented
- Evolution tracked (development, setup, efficiency improvements)
- Opportunistic emergence noted (RD005)

---

## File Locations

**Complete JSON extraction:** `/mnt/user-data/outputs/sobotkova_rdmap_pass1_complete.json`

**Contains:**
- All evidence, claims, implicit arguments from Discussion (unchanged)
- All research designs, methods, protocols from Methods (newly added)
- Project metadata
- Comprehensive extraction notes

**Ready for:** RDMAP Pass 2 rationalization prompt
