# Extraction Examples

This directory contains curated examples of research paper extractions demonstrating the Research Assessor skill across different paper types, disciplines, and complexity levels.

---

## Purpose

Examples serve three purposes:

1. **Learning:** Demonstrate extraction quality and structure for new users
2. **Testing:** Validation cases for schema and prompt updates
3. **Reference:** Worked examples showing edge cases and best practices

---

## Directory Structure

```
examples/
├── README.md (this file)
├── sobotkova-et-al-2023/     # Complete worked example (archaeological methods)
│   ├── extraction.json        # Full extraction (Passes 0-6)
│   ├── sobotkova-et-al-2023.txt  # Source text (processed markdown)
│   └── NOTES.md               # Annotations explaining extraction decisions
├── templates/                 # Blank templates for new extractions
│   ├── extraction-template-v2.6.json  # Schema v2.6 blank template
│   └── queue-template.yaml    # Queue file template
└── quick-reference/           # Quick reference extractions
    └── mini-extraction-guide.md  # Condensed workflow guide
```

---

## Current Examples

### Sobotkova et al. (2023) - Archaeological Survey Methods

**Status:** Complete (Passes 0-6 + validation)
**Paper:** "Arbitrary Offline Data Capture on All of Your Androids: The FAIMS Mobile Platform"
**Type:** Methodological paper (archaeological field recording software)
**Complexity:** High (multi-component software system, 10-year development history)

**Extraction Statistics:**
- Evidence: 53 items
- Claims: 43 items
- Implicit Arguments: 16 items
- Research Designs: 6 items
- Methods: 15 items
- Protocols: 8 items
- Total: 141 items
- Cross-references: 200+ relationships

**Why This Example:**
- Demonstrates complete 7-pass workflow
- Shows implicit argument extraction
- Complex RDMAP hierarchy (strategic → tactical → operational)
- Infrastructure assessment included (Pass 6)
- Annotations explain borderline extraction decisions

**Location:** `outputs/sobotkova-et-al-2023/` (working extraction, copy to examples/ when finalised)

---

## Planned Examples (Future)

### High-Priority Examples

1. **Short empirical paper** (10-15 pages)
   - Demonstrates extraction from concise reporting
   - Focus on core claims and primary evidence
   - Example: Single-site excavation report

2. **Long multi-proxy study** (30+ pages)
   - Demonstrates section-by-section extraction
   - Multiple analytical methods (radiocarbon, ceramics, isotopes)
   - Example: Ancient DNA + archaeology integration paper

3. **Pre-FAIR baseline** (2010-2015 era)
   - Demonstrates infrastructure assessment on older papers
   - 0/15 or low FAIR scores (historical context)
   - Example: Pre-digital archaeology publication

4. **High-FAIR exemplar** (2020-2024)
   - Demonstrates excellent reproducibility infrastructure
   - 12-15/15 FAIR score
   - Example: Recent genomics or computational archaeology paper

### Medium-Priority Examples

5. **Software publication** (SoftwareX, JOSS)
   - Code-centric infrastructure assessment
   - Computational reproducibility focus
   - Example: Archaeological simulation software

6. **Minimal transparency case**
   - Demonstrates extraction when methods poorly reported
   - Many implicit arguments required
   - Teaching example for transparency assessment

7. **Multi-disciplinary fieldwork**
   - Ecology + archaeology, or geology + archaeology
   - Demonstrates vocabulary alignment across disciplines
   - Example: Geoarchaeology or zooarchaeology

---

## Using Examples

### For New Users

1. **Read the source paper** (`*-et-al-YYYY.txt` or PDF)
2. **Review the extraction** (`extraction.json`)
3. **Read annotations** (`NOTES.md` - explains why items were extracted or excluded)
4. **Compare to your extraction** (if practicing)

### For Developers

1. **Validation testing:** Run schema validator on example extractions after schema updates
2. **Prompt testing:** Re-extract examples after prompt changes to assess impact
3. **Regression testing:** Compare new extractions to annotated examples

### For Researchers

1. **Quality benchmarks:** Compare your extractions to worked examples
2. **Edge cases:** See how borderline items were handled in annotations
3. **FAIR assessment:** See infrastructure assessment methodology in practice

---

## Creating New Examples

When adding new examples to this directory:

### 1. Select Representative Papers

**Criteria:**
- Diverse disciplines (archaeology, ecology, ethnography, geology)
- Range of transparency levels (excellent to poor)
- Different paper types (empirical, methodological, software)
- Varied lengths (short 10-page to long 40-page papers)
- Historical spread (2010-2024)

**Avoid:**
- Paywalled papers (use open access for examples)
- Overly complex papers (40+ pages, 10+ methods)
- Papers with sensitive/confidential data

### 2. Complete Full Extraction

**Required:**
- All 7 passes (0-6) plus validation (Pass 7)
- Complete relationship mapping (80%+ coverage)
- Infrastructure assessment (Pass 6)
- Quality metrics documented

**Quality Thresholds:**
- Pass validation without errors
- Relationship coverage >75%
- All verbatim quotes verified
- Consolidation metadata complete

### 3. Annotate Extraction Decisions

**Create NOTES.md with:**

```markdown
# Extraction Notes: [Paper Title]

## Overview
- Paper type, discipline, complexity
- Key challenges encountered
- Notable features

## Pass-by-Pass Notes

### Pass 0: Metadata
- Any metadata extraction challenges

### Pass 1: Claims/Evidence (Liberal)
- Borderline items and decisions
- Items initially extracted but later removed

### Pass 2: Claims/Evidence (Consolidation)
- Consolidation decisions (what was merged, why)
- Items removed during rationalisation

### Pass 3-5: RDMAP
- Research design classification decisions
- Method vs protocol distinctions
- Tier assignments (strategic/tactical/operational)

### Pass 6: Infrastructure
- FAIR assessment rationale
- PID connectivity notes
- Computational reproducibility level justification

## Edge Cases

Document 3-5 edge cases with:
- Item ID
- Challenge (why borderline)
- Decision made
- Rationale
- Alternative interpretations considered

## Lessons Learned

What would you do differently on second extraction?
```

### 4. Copy to Examples Directory

```bash
mkdir examples/author-et-al-YYYY/
cp outputs/author-et-al-YYYY/extraction.json examples/author-et-al-YYYY/
cp outputs/author-et-al-YYYY/author-et-al-YYYY.txt examples/author-et-al-YYYY/
# Create NOTES.md with annotations
```

### 5. Update This README

Add new example to "Current Examples" section with statistics and rationale.

---

## Templates

### Blank Extraction Template

Use `templates/extraction-template-v2.6.json` to start new extractions:

```bash
cp examples/templates/extraction-template-v2.6.json outputs/new-paper/extraction.json
```

Template includes:
- All required schema fields with null/empty values
- Metadata structure
- Object arrays (evidence, claims, research_designs, methods, protocols)
- Infrastructure assessment structure

### Queue Template

Use `templates/queue-template.yaml` for batch processing:

```bash
cp examples/templates/queue-template.yaml input/queue.yaml
# Edit queue.yaml to add papers
```

---

## Quality Standards

Examples in this directory must meet quality thresholds:

### Completeness
- ✅ All 7 passes complete (0-6)
- ✅ Validation passing (Pass 7)
- ✅ Infrastructure assessment included (Pass 6)

### Accuracy
- ✅ Verbatim quotes verified against source
- ✅ Location metadata accurate (section, page, paragraph)
- ✅ Object classifications correct (evidence vs claim, method vs protocol)

### Relationship Quality
- ✅ Bidirectional mapping >75% complete
- ✅ No orphaned cross-references
- ✅ Relationship types semantically correct

### Documentation
- ✅ NOTES.md with extraction annotations
- ✅ Edge cases documented
- ✅ Quality metrics calculated

---

## Contribution Guidelines

To contribute new examples:

1. **Propose the paper:** Open issue describing why this paper makes a good example
2. **Complete extraction:** Follow full 7-pass workflow
3. **Annotate decisions:** Create NOTES.md explaining borderline cases
4. **Submit pull request:** Include extraction.json, source text, NOTES.md
5. **Peer review:** At least one other extractor reviews for quality

See [CONTRIBUTING.md](../CONTRIBUTING.md) for detailed contribution guidelines.

---

## Licence

Examples in this directory are dual-licensed:

- **Extraction data** (`extraction.json`, `NOTES.md`): [CC-BY-4.0](../LICENSE-DOCS)
- **Source texts**: Respective publishers' licences (open access papers only)

---

## Contact

Questions about examples or suggestions for new examples:
- Open an issue on GitHub
- See [docs/user-guide/getting-started.md](../docs/user-guide/getting-started.md)

---

**Last Updated:** 2025-11-13
**Examples Count:** 1 (sobotkova-et-al-2023)
**Planned:** 7 additional examples
