# Key et al. 2024 - Text vs PDF Extraction Comparison

**Date:** 2025-01-14
**Purpose:** Test extraction quality from plain text vs PDF source

## Experiment Design

Extracted Key et al. 2024 twice:
1. **PDF extraction** (baseline) - Direct PDF reading with context compactions
2. **Text extraction** (test) - Plain text extracted from PDF

Both runs used identical workflow (Passes 0, 6, 1-2, 3-5).

## Results

| Component          | PDF | Text | % of PDF |
|--------------------|-----|------|----------|
| Evidence           | 27  | 25   | 92.6%    |
| Claims             | 24  | 21   | 87.5%    |
| Implicit Arguments | 7   | 6    | 85.7%    |
| Research Designs   | 6   | 6    | 100%     |
| Methods            | 6   | 6    | 100%     |
| Protocols          | 12  | 11   | 91.7%    |
| **Total**          | 82  | 75   | **91.5%**|

## Key Findings

1. **RDMAP extraction equivalent** - Research designs, methods nearly identical between formats
2. **Claims/evidence ~10% lower from text** - Some nuance lost without visual context
3. **Context compaction maintains continuity** - PDF with multiple compactions performed as well or better than text
4. **Text viable fallback** - 91.5% capture rate acceptable when PDF doesn't fit

## Recommendation

**Prefer PDF** unless it genuinely exceeds context limits:
- PDF preserves page numbers for location fields
- Table structure and figure captions retained
- No text extraction artefacts
- Compaction continuity is robust

## Files

- `extraction-text-comparison.json` - Complete text-based extraction (Passes 0-5)
- `extraction-pdf-session-c.json` - PDF extraction checkpoint after Session C (Passes 3-5)
- PDF baseline: `studies/open-science-compliance/outputs/key-et-al-2024/extraction.json`
