# Pass 0: Metadata Extraction Prompt

## Objective

Extract accurate bibliographic metadata from the first 2-3 pages of the research paper to populate the `project_metadata` object in extraction.json. This metadata provides essential context for the extraction and ensures proper citation and attribution.

## Critical Rules

1. **Extract from title page ONLY** - Do not use author mentions from acknowledgements, email addresses, or later sections
2. **Full author names required** - Use complete given names, not initials (e.g., "Shawn A. Ross" not "Ross, S.A.")
3. **Exact journal name** - Use the journal name exactly as printed on the title page or JSTOR header
4. **Primary source priority** - Title page > JSTOR/repository header > PDF embedded metadata
5. **Do not guess** - If DOI is not visible, set to null; if information is unclear, extract best available version
6. **Year is integer** - Publication year must be an integer (e.g., 2009, not "2009", not "Winter 2009")

## Field-by-Field Extraction Instructions

### 1. paper_title (string, required)

**Source:** Title page, article header

**Instructions:**
- Extract the complete paper title exactly as it appears
- Include subtitle if present (separated by colon)
- Preserve capitalisation as printed
- Do not include author names or journal information
- Remove any line breaks or formatting artefacts

**Example:**
```
"Remote Sensing and Archaeological Prospection in Apulia, Italy"
```

### 2. authors (array of strings, required)

**Source:** Title page author list (usually immediately below title)

**Instructions:**
- Extract ALL authors in the order they appear
- Use full given names, not initials (e.g., "Shawn A. Ross" not "S. A. Ross" or "Ross, S.")
- Format as "Firstname Middlename(s) Lastname"
- If only initials are provided, expand using information from affiliations or email addresses if available
- If expansion not possible, use the initials as provided but note this in extraction_notes
- Include all authors, not just first author or et al.

**Example:**
```json
["Shawn A. Ross", "Adela Sobotkova", "Gert-Jan Burgers"]
```

**Common pitfalls:**
- Using abbreviated names (S. Ross) instead of full names
- Using comma-reversed format (Ross, Shawn)
- Missing middle initials or names
- Extracting names from acknowledgements instead of title page

### 3. publication_year (integer, required)

**Source:** Title page, JSTOR header, journal citation line

**Instructions:**
- Extract the year as a 4-digit integer
- Use publication year, not access date or submission date
- If multiple years appear (e.g., "2008-2009" for volume), use the specific issue year
- Do not include season or month (those go in journal field if needed)

**Example:**
```
2009
```

### 4. journal (string, required)

**Source:** Title page, JSTOR header, running header

**Instructions:**
- Extract the complete journal name exactly as printed
- Do not abbreviate (e.g., "Journal of Field Archaeology" not "J. Field Archaeol.")
- Include volume, issue, and page numbers in this field using format: "Journal Name, Vol. X, No. Y, pp. A-B"
- If season or month is specified, include it: "Journal Name, Vol. X, No. Y (Season/Month, Year), pp. A-B"
- For book chapters, use format: "In: Book Title, Publisher"

**Example:**
```
"Journal of Field Archaeology, Vol. 34, No. 4 (Winter, 2009), pp. 423-437"
```

### 5. doi (string or null, optional)

**Source:** Title page, JSTOR header, first page footer

**Instructions:**
- Extract the DOI if explicitly printed on the paper
- Format as full DOI string (e.g., "10.1179/009346909791071393")
- Do not include "https://doi.org/" prefix
- If no DOI is visible, set to `null` (not empty string)
- Do not search external databases - only extract if printed on paper

**Example:**
```
"10.1179/009346909791071393"
```
or
```
null
```

### 6. paper_type (string, required)

**Source:** Inferred from paper structure, abstract, and content

**Instructions:**
- Classify the paper into one of these categories:
  - "research article" - Primary research reporting original fieldwork/analysis
  - "methods paper" - Methodological comparison or technique development
  - "review article" - Literature review or synthesis
  - "case study" - Detailed analysis of specific site/project
  - "theoretical paper" - Conceptual/theoretical framework development
  - "technical report" - Project report or preliminary findings
  - "commentary" - Response, commentary, or critique
- Read abstract and introduction if classification unclear from title alone
- Use "research article" as default if unclear

**Example:**
```
"methods paper"
```

### 7. discipline (string, required)

**Source:** Journal name, paper content, author affiliations

**Instructions:**
- Identify the primary disciplinary context
- Common values: "archaeology", "ethnography", "anthropology", "history", "geography", "environmental science", "classics"
- Use most specific appropriate term
- For interdisciplinary work, choose the dominant discipline
- Infer from journal name, research methods, and theoretical framework

**Example:**
```
"archaeology"
```

### 8. research_context (string, required)

**Source:** Abstract, introduction, title

**Instructions:**
- Write 1-2 sentences summarising the research topic and location/context
- Include: geographic location, time period, research question/goal, and primary methods
- Keep concise but informative (50-150 words)
- Write in complete sentences
- Focus on "what was studied and where"

**Example:**
```
"Comparative evaluation of QuickBird satellite imagery versus traditional field survey methods for archaeological prospection in a 100 sq km study area centred on L'Amastuola, Apulia, Italy. Tests the efficacy of high-resolution multispectral remote sensing for detecting archaeological sites in Mediterranean karst landscape."
```

## Extraction Strategy

### Source Priority Order

1. **Title page** - Primary source for title, authors, affiliations
2. **JSTOR/repository header** - Secondary source for full bibliographic citation (journal, volume, pages)
3. **Running headers** - Tertiary source if title page ambiguous
4. **PDF metadata** - Cross-check only, do not rely on as primary source
5. **Abstract** - For research_context and paper_type only

### Validation Checks

Before finalising metadata extraction, verify:

1. **Author count matches** - Count on title page = count in author array
2. **Year consistency** - Same year appears in title page, JSTOR header (if present), and any reference to "this paper was published in..."
3. **Full names** - No periods in author names except after middle initials (e.g., "A." is OK, "S." at end of name is not)
4. **Journal completeness** - Journal field includes volume, issue, pages
5. **No empty strings** - All required fields have substantive content (use null for optional DOI only)

### Common Title Page Formats

**Format 1: JSTOR digitised paper**
- JSTOR header at top with full citation
- Title page follows with title, authors, affiliations
- Use JSTOR header for journal/volume/pages, title page for authors

**Format 2: Publisher PDF**
- Journal name in header or footer
- Title centred on page
- Authors below title with affiliations as superscripts/footnotes
- Volume/issue/pages in footer

**Format 3: Preprint or working paper**
- May lack journal information
- May have "Submitted to..." or "Accepted for publication in..."
- Use available information, note limitations in extraction_notes

## Output Format

Populate the `project_metadata` object in extraction.json with this structure:

```json
{
  "project_metadata": {
    "paper_title": "Complete title from title page",
    "authors": ["Firstname Lastname", "Firstname Middleinitial Lastname", "..."],
    "publication_year": 2009,
    "journal": "Journal Name, Vol. X, No. Y (Season, Year), pp. A-B",
    "doi": "10.xxxx/xxxxx" or null,
    "paper_type": "research article|methods paper|review article|case study|...",
    "discipline": "archaeology|ethnography|anthropology|...",
    "research_context": "1-2 sentence summary of research topic, location, and methods."
  }
}
```

## Extraction Notes Documentation

Add an entry to `extraction_notes` documenting the Pass 0 extraction:

```json
{
  "extraction_notes": {
    "pass0_metadata": {
      "completion_date": "ISO 8601 timestamp",
      "primary_source": "title page|JSTOR header|publisher PDF header",
      "author_name_format": "full names|initials only|mixed",
      "doi_present": true|false,
      "notes": "Any relevant observations about metadata quality, ambiguities resolved, or information gaps"
    }
  }
}
```

## PDF Metadata Cross-Check (Optional)

If `pdfinfo` command is available, extract embedded PDF metadata for cross-validation:

```bash
pdfinfo "path/to/paper.pdf" | grep -E "Title|Author|Subject|Creator"
```

**Use for validation only:**
- If PDF metadata differs from title page, prefer title page
- PDF metadata is often incomplete, malformed, or incorrect
- Document significant discrepancies in extraction_notes
- Common issues: Authors as "User", Title as filename, missing journal info

## Example Complete Extraction

**Input:** Ross et al. 2009 - Remote Sensing and Archaeological Prospection in Apulia, Italy (Journal of Field Archaeology)

**Output:**

```json
{
  "project_metadata": {
    "paper_title": "Remote Sensing and Archaeological Prospection in Apulia, Italy",
    "authors": ["Shawn A. Ross", "Adela Sobotkova", "Gert-Jan Burgers"],
    "publication_year": 2009,
    "journal": "Journal of Field Archaeology, Vol. 34, No. 4 (Winter, 2009), pp. 423-437",
    "doi": null,
    "paper_type": "methods paper",
    "discipline": "archaeology",
    "research_context": "Comparative evaluation of QuickBird satellite imagery versus traditional field survey for archaeological prospection in 100 sq km study area centred on L'Amastuola, Apulia, Italy. Assesses relative utility of high-resolution multispectral remote sensing and intensive surface survey in Mediterranean karst environment."
  },
  "extraction_notes": {
    "pass0_metadata": {
      "completion_date": "2025-10-30T12:00:00Z",
      "primary_source": "JSTOR header + title page",
      "author_name_format": "full names with middle initials",
      "doi_present": false,
      "notes": "Paper accessed through JSTOR. Full bibliographic information available in JSTOR header. Authors listed with full names and institutional affiliations on title page."
    }
  }
}
```

## Common Pitfalls and How to Avoid Them

### Pitfall 1: Using Initials Instead of Full Names

**Wrong:**
```json
"authors": ["S. A. Ross", "A. Sobotkova", "G.-J. Burgers"]
```

**Correct:**
```json
"authors": ["Shawn A. Ross", "Adela Sobotkova", "Gert-Jan Burgers"]
```

**How to avoid:** Look at affiliations section where authors often appear with full first names.

### Pitfall 2: Extracting Wrong Authors

**Wrong:** Using acknowledgement section ("We thank Samsung Lim for georeferencing...")

**Correct:** Using title page author list only

**How to avoid:** Stop reading after first 2-3 pages, focus only on title page author list.

### Pitfall 3: Wrong Journal Name

**Wrong:** Using different journal with similar title, or using journal abbreviation

**Correct:** Using exact journal name from title page or JSTOR header

**How to avoid:** Read carefully, check JSTOR header if present, verify volume/issue make sense.

### Pitfall 4: Year as String

**Wrong:**
```json
"publication_year": "2009"
```

**Correct:**
```json
"publication_year": 2009
```

**How to avoid:** Ensure no quotes around year value in JSON.

### Pitfall 5: Incomplete Journal Field

**Wrong:**
```json
"journal": "Journal of Field Archaeology"
```

**Correct:**
```json
"journal": "Journal of Field Archaeology, Vol. 34, No. 4 (Winter, 2009), pp. 423-437"
```

**How to avoid:** Always include volume, issue, and pages from JSTOR header or title page footer.

## Post-Extraction Validation

After populating project_metadata, verify:

1. ✓ All 7 required fields have non-empty values
2. ✓ DOI is either valid DOI string or null
3. ✓ Authors array has at least one author
4. ✓ Authors use full names (check for periods at end of names)
5. ✓ publication_year is 4-digit integer between 1900-2030
6. ✓ journal field includes volume and pages
7. ✓ research_context is 1-2 complete sentences
8. ✓ pass0_metadata entry added to extraction_notes

If any validation fails, review extraction and correct before proceeding to Pass 1.

## Integration with Workflow

Pass 0 executes:
- **After:** Pre-Flight initialisation creates blank extraction.json
- **Before:** Pass 1 begins content extraction
- **Autonomous:** No user confirmation required
- **Fast:** 2-3 minutes typical execution time
- **Blocking:** Pass 1 should not proceed if Pass 0 fails validation

Upon completion:
1. Save updated extraction.json with populated project_metadata
2. Update queue.yaml checkpoint: "Pass 0 complete - metadata extracted"
3. Print metadata summary to console for review
4. Proceed immediately to Pass 1 (no stopping)

---

**Version:** 1.0.0
**Last updated:** 2025-10-30
**Compatible with:** Schema v2.5
