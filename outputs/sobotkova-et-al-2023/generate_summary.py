#!/usr/bin/env python3
"""
Generate summary.md for completed extraction.
"""

import json
from datetime import datetime
from pathlib import Path

def load_extraction():
    path = Path("/home/shawn/Code/llm-reproducibility/outputs/sobotkova-et-al-2023/extraction.json")
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def generate_summary(data):
    """Generate summary markdown."""

    summary = f"""# Extraction Summary: Sobotkova et al. (2023)

**Paper:** {data['project_metadata']['paper_title']}

**Authors:** {', '.join(data['project_metadata']['authors'])}

**Publication:** {data['project_metadata']['journal']} ({data['project_metadata']['publication_year']})

**DOI:** {data['project_metadata']['doi']}

**Extraction Date:** {datetime.now().strftime('%Y-%m-%d')}

**Extractor:** Claude Code (Sonnet 4.5)

---

## Extraction Statistics

| Category | Count |
|----------|-------|
| Evidence | {len(data['evidence'])} |
| Claims | {len(data['claims'])} |
| Implicit Arguments | {len(data['implicit_arguments'])} |
| Research Designs | {len(data['research_designs'])} |
| Methods | {len(data['methods'])} |
| Protocols | {len(data['protocols'])} |
| **Total Extracted** | **{len(data['evidence']) + len(data['claims']) + len(data['implicit_arguments']) + len(data['research_designs']) + len(data['methods']) + len(data['protocols'])}** |

---

## Paper Overview

### Research Context

{data['project_metadata']['research_context']}

**Study Period:** {data['project_metadata']['timeline']['fieldwork_dates']}

**Location:** {data['project_metadata']['location']['study_area']} ({data['project_metadata']['location']['coverage_area_sq_km']:,} sq km)

### Key Research Designs

"""

    for design in data['research_designs'][:4]:
        summary += f"- **{design['design_id']}:** {design['content'][:120]}...\n"

    summary += f"""

### Core Methods ({len(data['methods'])} total)

"""

    for method in data['methods'][:5]:
        status = method.get('method_status', 'explicit')
        summary += f"- **{method['method_id']}** [{status}]: {method['content'][:100]}...\n"

    summary += f"""

### Key Findings (Sample Claims)

"""

    # Show core claims
    core_claims = [c for c in data['claims'] if c.get('claim_type') == 'core']
    for claim in core_claims[:5]:
        summary += f"- **{claim['claim_id']}:** {claim['content']}\n"

    summary += f"""

---

## Extraction Quality

### RDMAP Coverage

- **Research Designs:** {sum(1 for d in data['research_designs'] if d.get('design_status') == 'explicit')} explicit, {sum(1 for d in data['research_designs'] if d.get('design_status') == 'implicit')} implicit
- **Methods:** {sum(1 for m in data['methods'] if m.get('method_status') == 'explicit')} explicit, {sum(1 for m in data['methods'] if m.get('method_status') == 'implicit')} implicit
- **Protocols:** {sum(1 for p in data['protocols'] if p.get('protocol_status') == 'explicit')} explicit, {sum(1 for p in data['protocols'] if p.get('protocol_status') == 'implicit')} implicit

### Evidence-Claim Relationships

- Total evidence → claim links: {sum(len(e.get('supporting_claims', [])) for e in data['evidence'])}
- Claims with evidence support: {sum(1 for c in data['claims'] if c.get('supported_by_evidence', []))} / {len(data['claims'])}
- Average evidence per claim: {(sum(len(c.get('supported_by_evidence', [])) for c in data['claims']) / len(data['claims'])):.1f}

### Implicit Arguments

- Total implicit arguments: {len(data['implicit_arguments'])}
- Types: {', '.join(set(ia.get('argument_type', 'unknown') for ia in data['implicit_arguments']))}

---

## Paper Characteristics

**Type:** Methods paper / Case study

**Domain:** Digital Humanities / Archaeology

**Focus:** Crowdsourced map digitization using mobile GIS

**Key Innovation:** Customization of FAIMS Mobile platform for novice volunteer digitization with minimal training

**Transparency Level:** High - extensive explicit documentation of methodology

**Reproducibility:** Good - open source code available, procedures documented

---

## Extraction Notes

### Pass Completion

✓ Pass 1: Claims & Evidence (Liberal extraction)
✓ Pass 2: Claims & Evidence (Rationalization)
✓ Pass 3: RDMAP Explicit extraction
✓ Pass 4: RDMAP Implicit scan
✓ Pass 5: RDMAP Rationalization
✓ Pass 6: Validation & reporting

### Key Observations

1. **Well-documented methods paper:** Most procedures explicitly described in Section 2 (Approach)
2. **Quantitative evaluation:** Extensive time-on-task and error rate data
3. **Comparative framework:** Systematic comparison of digitization approaches
4. **Minimal implicit RDMAP:** Only 5 implicit items (2 methods, 3 protocols) due to thorough explicit documentation

### Extraction Strategy

- Conservative rationalization in Pass 2 (6.5% reduction)
- Section-by-section approach for liberal passes (1 & 3)
- Minimal RDMAP consolidation needed (0% reduction in Pass 5)
- Relationship verification and bidirectional mapping in Pass 5

---

## Files Generated

- `extraction.json` - Complete structured extraction (159 items)
- `validation-pass6.md` - Validation report with quality assessment
- `summary.md` - This summary document

---

*Extraction completed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*

*Extraction system: research-assessor skill v2.7.0*

*Model: Claude Code (Sonnet 4.5)*
"""

    return summary

def main():
    print("="*80)
    print("GENERATING EXTRACTION SUMMARY")
    print("="*80)

    # Load extraction
    print("\nLoading extraction.json...")
    data = load_extraction()

    # Generate summary
    print("Generating summary...")
    summary = generate_summary(data)

    # Write summary
    summary_path = Path("/home/shawn/Code/llm-reproducibility/outputs/sobotkova-et-al-2023/summary.md")
    with open(summary_path, 'w', encoding='utf-8') as f:
        f.write(summary)

    print(f"✓ Summary generated: {summary_path}")

    print("\n" + "="*80)
    print("SUMMARY GENERATION COMPLETE")
    print("="*80)

if __name__ == "__main__":
    main()
