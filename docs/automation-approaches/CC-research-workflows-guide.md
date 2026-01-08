# Claude Code for Research Workflows: The "Coding Plus" Guide

**For**: LLM-enabled pipelines, document extraction, taxonomy development, corpus analysis, archaeological/historical data mining

**Context**: Claude Code is marketed as a "coding assistant" but is increasingly used at Anthropic and elsewhere for research automation, data extraction, and knowledge work. This guide addresses the **actual** workflows researchers use, not idealized software engineering patterns.

---

## Table of Contents

1. [The Research Automation Reality](#the-research-automation-reality)
2. [Document Extraction Workflows](#document-extraction-workflows)
3. [Taxonomy & Classification Development](#taxonomy--classification-development)
4. [Legacy Data Mining](#legacy-data-mining)
5. [Corpus Analysis Patterns](#corpus-analysis-patterns)
6. [The "Coding Plus" Mindset](#the-coding-plus-mindset)
7. [Research-Specific MCP Servers](#research-specific-mcp-servers)
8. [Case Study: 15-Year Archaeological Project](#case-study-15-year-archaeological-project)

---

## The Research Automation Reality

### What Anthropic Doesn't Advertise (But Does Internally)

Researchers and data scientists at Anthropic use Claude Code to read and write Jupyter notebooks, interpret outputs including images, providing a fast way to explore and interact with data.

Over the past several months, Claude Code has become far more than a coding tool; at Anthropic, we've been using it for deep research, video creation, and note-taking, among countless other non-coding applications.

**The gap**: Most Claude Code documentation assumes you're building software. You're **building knowledge** - extracting, structuring, analyzing, and synthesizing information from messy sources.

### The "Coding Plus" Definition

Code is the **means**, not the **end**:
- You write Python scripts to **structure archaeological data**, not to build web apps
- You use bash to **batch process documents**, not to manage servers  
- You create JSON schemas to **formalize taxonomies**, not to build APIs
- You leverage automation to **scale intellectual work**, not to deploy products

### Why Claude Code Works for This

**Traditional tools fail because**:
- OCR software extracts text but can't understand context
- Spreadsheets can't handle narrative data
- Database tools require predefined schemas
- Manual coding is too slow for one-off research tasks

**Claude Code succeeds because**:
- It understands **semantic content** of documents
- It can work with **heterogeneous formats** (PDFs, scans, spreadsheets, narratives)
- It **generates code on-demand** for specific extraction needs
- It operates **in situ** on your filesystem
- It handles **fuzzy, messy, real-world data**

### Validation: Others Are Doing This

A feature request (#6208) explicitly asks for "Non-Coding Focused Modes" - business analysis, data exploration, and analytical workflows noting that Claude Code currently lacks optimization for these analytical, non-coding workflows common among Product Managers, Business Analysts, Data Analysts.

You're not misusing the tool - **you're pioneering legitimate use cases** that Anthropic is actively considering formalizing.

---

## Document Extraction Workflows

### The Core Challenge

You have:
- Scanned PDFs with variable quality
- Handwritten field notes  
- Historical documents with inconsistent formatting
- Spreadsheets with non-standard structures
- Narrative reports mixing text, tables, and figures

Traditional OCR extracts **text** but loses **meaning**.

### Claude Code's Advantage: Vision + Understanding

When a PDF contains scanned pages or embedded charts, the model applies vision-based OCR reasoning to reconstruct the content.

The Claude 3 model is likely the most flexible, allowing for quick creation of a custom extraction schema.

Claude doesn't just read text - it **interprets documents**.

### Workflow Pattern: Iterative Extraction Refinement

```bash
# Phase 1: Exploration (Interactive)
claude "Analyze this scanned field report: @reports/site_survey_1998.pdf
What types of data does it contain? 
Suggest an extraction schema."

# Phase 2: Schema Development (Interactive)
# Claude proposes: site locations, artifact counts, dating estimates, observations
"Create a JSON schema for this data type. 
Include fields for:
- Uncertainty (e.g., 'circa 500 BCE' vs 'definitively 500 BCE')
- Data quality indicators
- Source references (page numbers, section headings)"

# Phase 3: Test Extraction (Interactive)
"Extract data from first 3 pages using this schema.
Show me the results."

# Phase 4: Validation & Refinement (Interactive)
"I see you missed the artifact density measurements in Table 2.
Add a 'measurements' field with nested structure for quantitative data."

# Phase 5: Scale to Corpus (Headless)
# Once satisfied with interactive results, automate:
for report in reports/*.pdf; do
  claude -p "Extract archaeological data from report using schema @extraction_schema.json" \
    @"$report" \
    --output-format json \
    > "extractions/$(basename $report .pdf).json"
done
```

### Handling Mixed-Format Documents

**Real-world scenario**: 15-year archaeological project with:
- Scanned handwritten field notes (1990s)
- Excel spreadsheets with non-standard layouts
- Word documents with embedded tables
- PDF reports mixing narrative and data

**Claude Code approach**:

```bash
# Create a unified inventory first
claude "Scan ./project_archive/ recursively.
For each file, determine:
1. File type and format
2. Data content type (narrative, tabular, images, mixed)
3. Extraction difficulty (easy/medium/hard)
4. Recommended extraction approach

Output as CSV: filepath, type, content_type, difficulty, approach"

# This gives you a strategic view of the corpus
# Then tackle by difficulty level
```

**Format-specific strategies**:

```python
# Claude can write and execute extraction scripts
# Example for Excel with non-standard layouts

"""
Claude prompt: "This Excel file has data in unusual locations:
- Site names are in merged cells
- Data starts at row 15, not row 1  
- Some sheets have different structures

Write a Python script using openpyxl to:
1. Identify sheet structure automatically
2. Find table start rows
3. Extract to standardized JSON format
4. Handle merged cells properly
5. Preserve formula results for calculated fields
"""
```

### OCR + Understanding Combo

**For truly challenging scans**:

```bash
# First pass: Extract text with OCR
claude -p "Extract all text from this scanned document. 
Preserve layout and structure as much as possible." \
@field_notes_1995_site_12.pdf > raw_text.txt

# Second pass: Structured extraction with context
claude -p "Using this raw OCR text @raw_text.txt and 
the original scanned document @field_notes_1995_site_12.pdf:

1. Interpret handwritten annotations
2. Reconstruct tables that may have poor OCR
3. Identify uncertain readings (mark with [?])
4. Cross-reference text with visible diagrams/maps
5. Extract to structured format: @archaeology_schema.json

Be conservative: if unsure, mark as uncertain rather than guessing." \
--output-format json > structured_extraction.json
```

### Batch Processing with Quality Control

```bash
#!/bin/bash
# batch_extract_with_validation.sh

DOCS_DIR="./archive_docs"
EXTRACT_DIR="./extractions"
REVIEW_DIR="./needs_review"
SCHEMA="./schemas/site_data_v3.json"

for doc in "$DOCS_DIR"/*; do
  doc_id=$(basename "$doc")
  
  echo "Extracting: $doc_id"
  
  # Extract with confidence scores
  claude -p "Extract data from document using schema @$SCHEMA.
  
  CRITICAL: Include confidence scores (0.0-1.0) for each extracted field:
  - 1.0: Explicitly stated, unambiguous
  - 0.7-0.9: Clearly implied or standard interpretation
  - 0.4-0.6: Requires inference or has ambiguity
  - 0.0-0.3: Uncertain, needs human review
  
  Also include 'extraction_notes' field explaining any uncertainties." \
  @"$doc" \
  --output-format json > "$EXTRACT_DIR/${doc_id}.json"
  
  # Auto-triage based on confidence
  avg_confidence=$(jq '[.. | .confidence? | select(. != null)] | add/length' \
    "$EXTRACT_DIR/${doc_id}.json")
  
  if (( $(echo "$avg_confidence < 0.6" | bc -l) )); then
    echo "Low confidence extraction - flagging for review"
    cp "$EXTRACT_DIR/${doc_id}.json" "$REVIEW_DIR/"
    
    # Create review summary
    claude -p "Summarize extraction uncertainties from this file for human reviewer.
    List specific fields needing attention and why.
    Format as markdown checklist." \
    @"$EXTRACT_DIR/${doc_id}.json" > "$REVIEW_DIR/${doc_id}_review.md"
  fi
done
```

### Multi-Modal Document Analysis

**For documents with diagrams, maps, photos**:

```bash
# Claude can interpret visual + textual content together
claude "Analyze this archaeological site report: @site_report_complex.pdf

This document contains:
- Narrative description of excavation
- Site map with grid coordinates
- Photos of artifacts with annotations
- Data tables with measurements

Extract:
1. Spatial data from map (grid locations, features)
2. Artifact descriptions linked to photos
3. Quantitative measurements from tables
4. Contextual narrative explaining interpretations

Link extracted elements by cross-references in text.
Output structured JSON showing relationships between data types."
```

---

## Taxonomy & Classification Development

### The Taxonomy Challenge

Building taxonomies and ontologies requires:
- Analyzing corpus to identify natural categories
- Detecting patterns and relationships
- Developing consistent labeling schemes
- Creating controlled vocabularies
- Handling edge cases and ambiguity

This is fundamentally **iterative intellectual work** that code can support but not replace.

### Claude Code as Taxonomy Development Partner

#### Phase 1: Exploratory Analysis

```bash
# Interactive session to understand your corpus
claude "Analyze these 100 archaeological site reports: @reports/*.pdf

I need to develop a taxonomy for artifact types mentioned across the corpus.

1. Extract all artifact references
2. Identify natural groupings (materials, functions, periods)
3. Detect inconsistent terminology (same item, different names)
4. Suggest hierarchical structure
5. Flag ambiguous or overlapping categories

Output preliminary taxonomy as hierarchical JSON."
```

#### Phase 2: Iterative Refinement

```bash
# Continue in same session or use CLAUDE.md
"Issues with proposed taxonomy:

1. 'Ceramics' vs 'Pottery' used inconsistently
2. Some items are both tool and ornament
3. Temporal categories (Bronze Age, Iron Age) overlap spatial categories

Revise taxonomy to:
- Use 'Ceramics' as primary term, map 'Pottery' as synonym
- Support multi-classification with primary/secondary designation
- Separate temporal, functional, and material dimensions

Show revised structure with examples."
```

#### Phase 3: Validation Against Corpus

```bash
# Test taxonomy by applying to corpus
claude -p "Using taxonomy @taxonomy_v2.json, 
classify all artifacts mentioned in this document: @site_report.pdf

Output:
1. Classified items with confidence scores
2. Items that don't fit taxonomy (new categories needed?)
3. Ambiguous cases requiring human judgment
4. Cross-reference suggestions (related items)

Format as JSON with annotations." \
--output-format json > classifications/site_report_classified.json

# Aggregate results to find taxonomy gaps
claude "Review all classification outputs: @classifications/*.json

Identify:
1. Frequently occurring 'doesn't fit taxonomy' items
2. Common ambiguous cases
3. Patterns in low-confidence classifications
4. Suggested taxonomy additions or modifications

Generate report: taxonomy_refinement_recommendations.md"
```

#### Phase 4: Building Controlled Vocabularies

```bash
# Generate standardized terminology mappings
claude "From taxonomy @taxonomy_final.json and corpus analysis,
create controlled vocabulary mappings:

1. Primary terms (canonical forms)
2. Accepted synonyms
3. Deprecated terms (don't use)
4. Scope notes (when to use each term)
5. Related terms (see also)

Format as JSON-LD for future semantic web use:
{
  'term': 'ceramic',
  'prefLabel': {'en': 'Ceramic'},
  'altLabel': ['pottery', 'earthenware'],
  'deprecated': ['pot', 'crockery'],
  'scopeNote': 'Use for fired clay objects...',
  'related': ['glaze', 'kiln', 'vessel']
}

Output: controlled_vocabulary.jsonld"
```

### Getty AAT Integration Example

**Real-world use case**: Mapping your local terminology to Getty Art & Architecture Thesaurus standards

```bash
# Interactive exploration
claude "My taxonomy uses these artifact categories: @local_taxonomy.json

For each category, find closest Getty AAT match:
1. Query Getty AAT concepts
2. Show URI, preferred label, and scope note
3. Indicate if exact match, close match, or no match
4. For 'no match', explain why and suggest broader/narrower AAT term

Include Getty URIs for semantic linking."

# Then create mapping file
claude "Generate SKOS mapping file linking my taxonomy to Getty AAT:

For each local term, create skos:exactMatch or skos:closeMatch to Getty URI.
Include skos:note explaining mapping decisions.
Flag terms needing expert review (no good AAT match).

Output as RDF/Turtle format for triple store import."
```

### Classification Scripts with Human-in-Loop

```python
# Claude generates and you run
"""
Prompt: "Write Python script for semi-automated artifact classification:

1. Load taxonomy and controlled vocabulary
2. For each document in corpus:
   a. Extract artifact mentions
   b. Attempt auto-classification using taxonomy
   c. Calculate confidence score
3. If confidence < 0.7, flag for human review:
   - Show artifact in context (surrounding text)
   - Display suggested classifications with scores
   - Provide input interface for human decision
4. Learn from human corrections:
   - Update classification rules
   - Add examples to improve future accuracy
5. Export results with provenance:
   - Who classified (AI or human)
   - When classified
   - Confidence score
   
Use rich library for nice terminal UI.
"""
```

### Tag Management Workflows

```bash
# Historical data often has informal tagging that needs rationalization
claude "Analyze tags used across all project documents: @project_files/*

Current situation:
- Tags applied inconsistently
- Overlapping meanings
- No controlled vocabulary
- Mix of subject, temporal, spatial, and material tags

Generate tag rationalization plan:
1. Tag frequency analysis
2. Cluster similar/related tags
3. Identify synonym groups ('pottery' vs 'ceramics' vs 'clay vessels')
4. Propose standardized tag schema with facets:
   - Material (what it's made of)
   - Function (what it's used for)
   - Period (when it's from)
   - Location (where it's from)
5. Mapping from old tags to new schema
6. Migration script to retag all documents

Save as: tag_rationalization_plan.md"
```

---

## Legacy Data Mining

### The 15-Year Project Scenario

**Your situation**: Archaeological project from 2008-2023 with:
- Evolving digital practices (early 2000s â†’ modern)
- Multiple field directors with different documentation styles
- Mix of analog (scanned) and digital materials
- Inconsistent naming conventions
- Missing metadata
- Some corrupted files
- Institutional knowledge locked in narratives

**Goal**: Extract structured data for reanalysis and archival deposit.

### Step 1: Inventory & Triage

```bash
# Create comprehensive inventory
claude "Perform deep analysis of project archive: /archive/

For directory structure and every file:

1. File metadata:
   - Type, size, dates (created/modified)
   - Software version if detectable
   - Preservation condition (corrupted? readable?)

2. Content assessment:
   - What type of data does it contain?
   - How is it structured?
   - What temporal/spatial coverage?
   - Who created it (if detectable from metadata/content)?

3. Extraction feasibility:
   - Can be auto-processed
   - Needs manual attention
   - Requires specialized tools
   - May be unrecoverable

4. Research value:
   - Core project data
   - Supporting documentation
   - Administrative/ephemeral
   - Duplicates of other files

Output comprehensive inventory as CSV with columns:
filepath, type, size_mb, date_created, date_modified, 
content_type, structure, coverage, creator, 
extraction_feasibility, research_value, notes

This creates your strategic extraction roadmap."
```

### Step 2: Handling Format Evolution

**Problem**: Excel files from 2008 may not open in modern software, or have broken formulas.

```bash
# Format conversion and preservation
claude "This is an Excel file from 2008: @excavation_data_2008.xls

Modern Excel warns about compatibility issues.

1. Open with openpyxl and identify issues:
   - Broken formulas
   - Deprecated functions
   - Corrupted cells

2. Extract data preserving:
   - Original formula logic (translate to working formulas)
   - Cell comments and annotations
   - Multiple sheets with relationships

3. Create both:
   - Modern XLSX with fixed formulas
   - JSON export with all data + metadata

4. Document conversion process in CHANGELOG for provenance."
```

### Step 3: Reconstructing Context from Narratives

**Real archaeological scenario**: Field director wrote rich narrative reports but didn't maintain structured databases.

```bash
# Extract implicit structured data from narratives
claude "This is a field report from 2012: @field_notes_july_2012.docx

It's written as narrative text, but contains implicit structured data:
- Site visit dates
- Grid square locations
- Artifact discoveries with descriptions
- Soil layer observations
- Interpretive conclusions

Extract structured data:

1. Create timeline of field activities
2. Build spatial index (which grid squares mentioned, what found there)
3. Catalog artifact discoveries with:
   - What was found
   - Where (spatial context)
   - When (temporal context)
   - Associated features/layers
4. Extract observations about stratigraphy
5. Separate facts from interpretations

Output as JSON with source traceability:
Each extracted fact should reference specific paragraph/sentence.

This enables verification and understanding data provenance."
```

### Step 4: Cross-Document Synthesis

**Challenge**: Information about single artifact scattered across field notes, lab analysis reports, photo logs, and publication drafts.

```bash
# Entity resolution across documents
claude "I need to reconstruct complete records for all artifacts from project.

Relevant files: @field_notes/*.docx @lab_reports/*.pdf @photo_log.xlsx @publications/*.pdf

For artifact ID 'SF-2015-142':

1. Find all mentions across documents
2. Extract information from each source:
   - Discovery context (field notes)
   - Physical description (lab reports)
   - Analysis results (lab reports)
   - Visual documentation (photo log)
   - Published interpretations (publications)
3. Resolve conflicts/inconsistencies
4. Create unified record with source attribution
5. Flag missing information

Repeat for all artifact IDs detected.

Output as:
- Individual JSON files per artifact
- Master index linking artifacts to documents
- Report of data quality issues"
```

### Step 5: Standardizing Terminology Across Time

**Problem**: Project vocabulary evolved over 15 years. Early reports use different terms than later ones.

```bash
# Diachronic terminology mapping
claude "Analyze terminology evolution across project timeline:
@reports/2008-2012/*.pdf
@reports/2013-2017/*.pdf  
@reports/2018-2023/*.pdf

Track how artifact type names, site terminology, and analytical methods 
terminology changed over time.

Create:
1. Temporal terminology map showing:
   - What each term meant in each period
   - When term usage changed
   - Synonyms and replacements

2. Standardization recommendations:
   - Canonical terms to use for archive
   - Mapping from historical â†’ standard terms
   - Scope notes explaining any ambiguity

3. Automated translation script:
   - Converts old terminology to standardized vocabulary
   - Preserves original in metadata
   - Flags ambiguous cases for human review

This enables consistent querying across full project timeline."
```

### Step 6: Metadata Reconstruction

**Problem**: Early digital files lack proper metadata (who, when, what, where, why).

```bash
# Forensic metadata recovery
claude "This file has minimal metadata: @unidentified_excavation_photos.zip

Using available clues:
1. File timestamps
2. Photo EXIF data (camera, GPS if present)
3. Content analysis (what's in photos)
4. Cross-reference with field notes from similar dates
5. Compare with other photos from project (people, locations, contexts)

Reconstruct probable:
- Date range of photos
- Site/grid square
- Field director responsible
- Archaeological context (what was being excavated)
- Related documentation

Create metadata file with confidence scores:
{
  'photos': [
    {
      'filename': 'IMG_0234.jpg',
      'inferred_date': '2011-07-15',
      'confidence_date': 0.8,
      'evidence_date': ['EXIF timestamp', 'cross-ref with field notes mentioning this trench'],
      'inferred_location': 'Trench 3, Grid Square N102E084',
      'confidence_location': 0.6,
      'evidence_location': ['visible site markers in photo', 'context in adjacent photos']
    }
  ]
}
"
```

### Step 7: Validation & Quality Assurance

```bash
# Comprehensive validation after extraction
claude "Review all extracted data for internal consistency:

1. Temporal consistency:
   - Artifacts found before excavation started?
   - Analysis dates before collection dates?
   - Publication references to unpublished data?

2. Spatial consistency:
   - GPS coordinates within site boundaries?
   - Grid square references valid for each season's layout?
   - Depth measurements physically possible?

3. Relational integrity:
   - All referenced IDs exist?
   - Parent-child relationships valid (e.g., sherd belongs to vessel)?
   - Cross-document references resolvable?

4. Data quality metrics:
   - Completeness (required fields populated?)
   - Precision (measurements with appropriate uncertainty?)
   - Provenance (source documentation traceable?)

Generate validation report with:
- Error categories and counts
- Specific problematic records
- Recommended fixes
- Priority for human review"
```

---

## Corpus Analysis Patterns

### Full-Corpus Question Answering

```bash
# Using MCP filesystem for corpus-wide queries
claude "Using filesystem MCP to search entire corpus @papers/

Answer: What are all the different methods used for ceramic dating 
across the 250 papers in this collection?

For each method:
1. Count papers using it
2. Extract descriptions of how it's applied
3. Note temporal/geographic contexts where used
4. Identify papers that compare multiple methods
5. Flag methodological controversies or debates

Synthesize into comprehensive methods overview."
```

### Pattern Detection Across Documents

```bash
# Identify research trends
claude "Analyze corpus @archaeological_papers/ for evolving methodologies:

Track over time (2000-2024):
1. Most cited analytical techniques
2. Adoption of new technologies (isotope analysis, aDNA, etc.)
3. Shifts in theoretical frameworks
4. Changes in sampling strategies
5. Evolution of reporting standards

Create timeline visualization data showing:
- When new methods appear
- How quickly they're adopted
- Geographic diffusion patterns
- Competing approaches

Output as JSON for visualization."
```

### Cross-Referencing and Citation Networks

```bash
# Build knowledge graph from corpus
claude "From all papers in @corpus/:

Extract and link:
1. Sites mentioned (entities)
2. Artifacts discussed (entities)
3. Methods applied (activities)
4. Researchers cited (agents)
5. Interpretive claims (propositions)

Create knowledge graph:
- Nodes: sites, artifacts, people, concepts
- Edges: 'mentioned in', 'analyzed with', 'similar to', 'disputes'
- Properties: temporal, spatial, evidential

Output as GraphML for network analysis tools.

Also generate:
- Most central sites (mentioned in most papers)
- Methodological clusters (papers using similar approaches)
- Interpretive lineages (citation chains)
- Controversial claims (papers with conflicting interpretations)"
```

---

## The "Coding Plus" Mindset

### Principle 1: Code is Disposable, Knowledge is Permanent

Traditional software development:
- Write maintainable, reusable code
- Extensive testing and documentation
- Production deployment

Research automation:
- **Write code that works once**
- Document the **results**, not the code
- Iterate rapidly, throw away failed approaches

```bash
# This is fine:
claude "Write quick script to extract dates from these 50 PDFs.
Doesn't need error handling, I'll manually check results."

# One-time extraction - code gets deleted after running
# Extracted data is what matters
```

### Principle 2: Human-AI Division of Labor

**Claude does**:
- Pattern detection across many documents
- Schema generation from examples
- Initial extraction attempts
- Suggesting classifications
- Identifying edge cases

**You do**:
- Final judgment on ambiguous cases
- Domain expertise application
- Quality assessment
- Deciding when "good enough" is reached
- Steering the analysis direction

```bash
# Typical workflow
claude "Extract all radiocarbon dates from these papers.
For each date:
- Calibrated age
- Uncertainty
- Lab ID
- Material dated
- Archaeological context

Output with confidence scores - I'll review low-confidence cases."

# You review the 15% flagged as low-confidence
# Accept the 85% high-confidence automatically
```

### Principle 3: Iterative Exploration Over Perfect Planning

Don't try to specify everything upfront:

```bash
# âŒ Bad: Trying to design perfect schema before seeing data
"Create comprehensive archaeological site record schema 
with all possible fields..."

# âœ… Good: Start with data, evolve schema
"Look at these 5 site reports @reports/samples/*.pdf
What data fields appear consistently?
Propose initial schema."

# Then iterate:
"That schema missed the stratigraphic relationships.
Add support for layer sequencing."

"Some sites have multiple occupation phases.
Make schema support temporal complexity."
```

### Principle 4: Validate Through Use, Not Through Specification

```bash
# Don't spend weeks designing the perfect extraction schema
# Instead:

# Week 1: Extract from 10 documents, see what breaks
# Week 2: Fix schema, extract from 50 more documents  
# Week 3: Refine based on errors, extract from 100 more
# Week 4: Finalize schema, batch process 1000 documents

# The corpus tells you what the schema should be
# Not the other way around
```

### Principle 5: Embrace Mixed Methods

**You're allowed to**:
- Use Claude Code for 80% of documents
- Manually handle the 20% difficult cases
- Combine automated extraction with human validation
- Use different tools for different formats
- Have varying quality standards for different data types

```bash
# Pragmatic hybrid approach
"Extract from all PDFs automatically.
For scanned handwritten documents, just flag them for me to do manually.
For Excel files, extract what you can and note missing data.

I'll do quality pass on everything - just get me 80% of the way there."
```

### Principle 6: Documentation for Humans, Not Computers

```bash
# Document your process in plain language
claude "Create research log entry for extraction process:

# 2024-01-15: Site Report Extraction

## Approach
Tried three different extraction strategies...

## Issues Encountered  
- Scanned maps not reliably extractable
- Inconsistent date formats across reports
- Some reports missing key metadata

## Solutions Implemented
- Manual map digitization for critical sites
- Built date parser handling 5 common formats
- Cross-referenced reports with field notes for metadata

## Quality Assessment
- 85% of records complete
- 12% missing spatial data (flagged for followup)
- 3% potential errors (needs expert review)

## Next Steps
- Review flagged records
- Enhance spatial data from GIS files
- Run consistency checks

Save to: research_logs/extraction_2024-01-15.md"
```

---

## Research-Specific MCP Servers

### Custom MCP for Archaeological Data

**Scenario**: You work with archaeological databases, spatial data, and specialized formats.

```javascript
// archaeology-mcp-server.js
// Gives Claude direct access to archaeological data sources

import { Server } from '@modelcontextprotocol/sdk/server/index.js';
import Database from 'better-sqlite3';

const server = new Server({
  name: 'archaeology-mcp',
  version: '1.0.0',
});

// Tool: Query artifact database
server.tool('query_artifacts',
  'Search archaeological artifact database',
  {
    site: { type: 'string', required: false },
    period: { type: 'string', required: false },
    material: { type: 'string', required: false },
    date_range: { type: 'object', required: false }
  },
  async (params) => {
    const db = new Database('./data/artifacts.db');
    
    let query = 'SELECT * FROM artifacts WHERE 1=1';
    const values = [];
    
    if (params.site) {
      query += ' AND site_code = ?';
      values.push(params.site);
    }
    if (params.period) {
      query += ' AND period = ?';
      values.push(params.period);
    }
    // ... build query dynamically
    
    const results = db.prepare(query).all(...values);
    return { content: [{ type: 'text', text: JSON.stringify(results, null, 2) }] };
  }
);

// Tool: Spatial queries
server.tool('spatial_query',
  'Find artifacts within geographic area',
  {
    latitude: { type: 'number', required: true },
    longitude: { type: 'number', required: true },
    radius_km: { type: 'number', required: true }
  },
  async (params) => {
    // Use PostGIS or similar for spatial queries
    // Return artifacts within radius
  }
);

// Tool: Chronological queries
server.tool('temporal_query',
  'Find contexts from specific time periods',
  {
    period: { type: 'string' },
    start_date: { type: 'integer' },
    end_date: { type: 'integer' }
  },
  async (params) => {
    // Query by date range or period
    // Handle BCE/CE and calibrated dates
  }
);

server.listen();
```

**Usage**:
```bash
claude mcp add archaeology -- node archaeology-mcp-server.js

# Now Claude has direct database access
claude "Using archaeology MCP, find all Bronze Age ceramics from sites within 
50km of coordinates 40.7128, -74.0060. 

For each artifact:
- Show discovery context
- Related C14 dates
- Similar artifacts from other sites
- Publication references

Generate comparative analysis report."
```

### Document Collection MCP

```javascript
// corpus-mcp-server.js
// Semantic search over document collection

import { Server } from '@modelcontextprotocol/sdk/server/index.js';
import fs from 'fs';
import path from 'path';

const server = new Server({
  name: 'corpus-mcp',
  version: '1.0.0',
});

// Tool: Semantic document search
server.tool('search_corpus',
  'Semantically search across document collection',
  {
    query: { type: 'string', required: true },
    document_type: { type: 'string', required: false },
    date_range: { type: 'object', required: false },
    max_results: { type: 'integer', default: 10 }
  },
  async (params) => {
    // Use vector embeddings for semantic search
    // Could integrate with ChromaDB, Pinecone, etc.
    
    const results = await semanticSearch(params.query, {
      type: params.document_type,
      dateRange: params.date_range,
      limit: params.max_results
    });
    
    return {
      content: [{
        type: 'text',
        text: JSON.stringify(results.map(r => ({
          document: r.filepath,
          relevance: r.score,
          excerpt: r.context
        })), null, 2)
      }]
    };
  }
);

// Tool: Cross-document entity tracking
server.tool('track_entity',
  'Find all mentions of entity across corpus',
  {
    entity_name: { type: 'string', required: true },
    entity_type: { type: 'string' } // person, site, artifact, concept
  },
  async (params) => {
    // Find entity mentions across documents
    // Track relationships and co-occurrences
  }
);

server.listen();
```

### Taxonomy Management MCP

```javascript
// taxonomy-mcp-server.js
// Manage and query taxonomies/ontologies

import { Server } from '@modelcontextprotocol/sdk/server/index.js';

const server = new Server({
  name: 'taxonomy-mcp',
  version: '1.0.0',
});

server.tool('query_taxonomy',
  'Query taxonomy for term relationships',
  {
    term: { type: 'string', required: true },
    relationship: { type: 'string' } // broader, narrower, related
  },
  async (params) => {
    // Query SKOS taxonomy
    // Return term relationships, definitions, scope notes
  }
);

server.tool('validate_classification',
  'Check if classification follows taxonomy rules',
  {
    item: { type: 'object', required: true },
    taxonomy: { type: 'string', required: true }
  },
  async (params) => {
    // Validate that classification is legal per taxonomy
    // Check for invalid combinations, missing required fields
  }
);

server.listen();
```

---

## Case Study: 15-Year Archaeological Project

### Project Context

**Project**: Multi-season excavation (2008-2023)
**Data volume**: ~5TB
**Formats**: Everything imaginable
**Challenge**: Create archival deposit for institutional repository

### Month 1: Assessment & Planning

```bash
# Week 1: Inventory
claude "Deep scan of project archive at /archive/

Create inventory tracking:
- File types and counts
- Date ranges
- Data categories (field notes, analysis, admin)
- Format condition (current vs legacy)
- Estimated extraction difficulty

Prioritize extraction by:
1. Research value
2. Format stability (most at risk first)
3. Extraction difficulty (easy wins first)

Output: extraction_priority_plan.md"

# Week 2: Sample Testing
# Pick 10 representative documents across formats
# Test extraction approaches
# Refine strategies

# Week 3: Schema Development
claude "From sample extractions, design unified data model for:
- Sites
- Contexts (stratigraphic units)
- Artifacts  
- Samples (C14, soil, etc.)
- Observations
- Interpretations

Support:
- Temporal uncertainty
- Spatial relationships
- Data provenance
- Quality indicators

Output: project_data_model_v1.jsonld"

# Week 4: Pilot Extraction
# Extract from 50 documents using refined schema
# Identify remaining issues
# Revise as needed
```

### Month 2-3: Bulk Extraction

```bash
# Parallel processing by format type

# Track 1: Field documentation
for season in {2008..2023}; do
  claude -p "Extract from field notes: @archive/field_notes/$season/*.pdf
  Schema: @schemas/field_data.json" \
  --output-format json > extractions/field_${season}.json
done

# Track 2: Laboratory records
for analysis_type in ceramics lithics fauna flora; do
  claude -p "Extract from lab reports: @archive/lab/$analysis_type/*.pdf
  Schema: @schemas/analysis_data.json" \
  --output-format json > extractions/lab_${analysis_type}.json
done

# Track 3: Spatial data
claude "Process all site maps, plans, and sections from @archive/spatial/
Convert to GeoJSON with standardized coordinate system.
Link to archaeological contexts via ID references."

# Track 4: Photography
claude "Create image catalog from @archive/photos/*
Extract EXIF metadata, cross-reference with field notes.
Generate structured catalog with:
- Subject identification
- Context linking
- Temporal/spatial metadata
- Rights and permissions info"
```

### Month 4: Quality Assurance & Synthesis

```bash
# Comprehensive validation
claude "Load all extraction outputs: @extractions/*.json

Run validation suite:
1. Schema compliance
2. Internal consistency (dates, IDs, relationships)
3. Cross-document verification (same entity, consistent data?)
4. Completeness checks (required fields populated?)
5. Outlier detection (suspicious values?)

Generate:
- Validation report by extraction batch
- List of high-priority issues for manual review
- Statistics on data coverage and quality
- Recommendations for re-extraction where needed

Output: validation_report_comprehensive.md"

# Synthesize into unified database
claude "Merge all validated extractions into unified project database:

Create:
1. PostgreSQL schema
2. Import scripts for each data type
3. Foreign key relationships
4. Spatial indices (PostGIS)
5. Full-text search indices
6. Metadata tables (provenance, versions)

Handle:
- Duplicate detection and resolution
- Conflicting data reconciliation
- Missing data documentation
- Quality scores per record

Generate database with complete audit trail."
```

### Month 5: Documentation & Archival Package

```bash
# Create archival documentation
claude "Generate comprehensive project documentation for archive:

1. Data Dictionary:
   - All fields defined
   - Controlled vocabularies documented
   - Relationships explained
   - Examples provided

2. Methodology Report:
   - Extraction procedures
   - Quality assurance processes
   - Known limitations
   - Recommended uses

3. Technical Documentation:
   - Database schema
   - File formats
   - Required software
   - Migration procedures

4. Research Context:
   - Project history
   - Research questions
   - Major findings
   - Publication record

5. Access Guide:
   - Query examples
   - Common analyses
   - Visualization suggestions
   - Citation guidance

Format as archival-quality PDF/A with embedded metadata."

# Package for repository
claude "Create OAIS-compliant archival package:

Structure:
/archive_package/
  /data/ - all extracted data in preservation formats
  /metadata/ - METS/MODS descriptive metadata
  /documentation/ - all generated documentation
  /original_files/ - normalized copies of source materials
  /tools/ - any custom extraction scripts preserved
  manifest.xml - complete package inventory with checksums

Generate BagIt package for validation and transfer."
```

### Results

**Extraction metrics**:
- 12,847 documents processed
- 89% automatic extraction success
- 11% requiring manual review (handled in parallel)
- Average 3.5 minutes per document
- Total processing: ~750 compute hours

**Data quality**:
- 92% completeness for core fields
- 87% completeness for optional fields
- High-confidence: 78% of records
- Medium-confidence: 18% of records
- Requires expert review: 4% of records

**Time saved**:
- Estimated manual extraction: 2,000 person-hours
- Actual with Claude Code: 200 person-hours + 750 compute hours
- 90% reduction in human labor
- Higher consistency than manual extraction

---

## Advanced Patterns

### Using Jupyter Notebooks for Exploration

Researchers and data scientists at Anthropic use Claude Code to read and write Jupyter notebooks, with Claude able to interpret outputs including images.

```bash
# Have Claude Code and notebook open side-by-side in VS Code
claude "Review notebook @exploration.ipynb

For the data analysis cells:
1. Identify issues with current approach
2. Suggest alternative visualization methods
3. Add statistical tests for significance
4. Generate summary interpretation of results

Also: Clean up code for readability and add markdown documentation."
```

### Bash Mode for Tight Iteration Loops

Prefix prompts with exclamation mark to execute shell commands and inject output into context: This runs your analysis script and adds complete output to Claude Code's context, creating tight feedback loop for iterative data exploration.

```bash
# Inside Claude Code session
! python extract_dates.py corpus/*.pdf > dates_raw.txt

"Review the extracted dates in dates_raw.txt
Issues I see:
- Mixed formats (ISO, MDY, DMY)
- Some invalid entries
- Missing dates marked inconsistently

Write improved parser handling all formats.
Test on dates_raw.txt and show success rate."

! python improved_parser.py dates_raw.txt

"Better! Now still some errors. 
Debug the cases in error_log.txt"
```

### Extended Thinking for Complex Problems

Include "think", "think harder", or "ultrathink" in prompts for thorough analysis.

```bash
# For genuinely difficult problems
claude "ultrathink: 

I have conflicting radiocarbon dates for a single archaeological context:
- Sample A: 450 Â± 40 BP
- Sample B: 1200 Â± 35 BP  
- Sample C: 520 Â± 50 BP

These should all date the same event.

Possible explanations:
1. Old wood problem (Sample B)
2. Contamination
3. Sample A or C actually from different context
4. Stratigraphic disturbance
5. Lab error

Using @full_site_data.json:
- Stratigraphic relationships
- Artifact associations
- Other dated contexts

Evaluate each hypothesis. What's the most likely explanation?
How should I handle this for publication?"
```

---

## Key Takeaways

### 1. You're Not Alone

Many researchers use Claude Code this way. Anthropic knows and is considering formalizing "non-coding modes".

### 2. Embrace the Hybrid Workflow

- Automation for scale
- Human judgment for quality
- Iterative refinement for accuracy
- Documentation for reproducibility

### 3. Start Small, Scale Gradually

- Test on samples first
- Validate before bulk processing
- Keep humans in loop for critical decisions
- Build confidence through iteration

### 4. The Goal is Knowledge, Not Code

- Code is disposable
- Data quality matters most
- Documentation preserves decisions
- Results speak for themselves

### 5. Leverage Your Domain Expertise

Claude Code handles:
- Format conversion
- Pattern detection
- Initial extraction
- Consistency checking

You handle:
- Interpretation
- Ambiguity resolution
- Quality assessment
- Research direction

### 6. Build Reusable Patterns, Not Perfect Code

- CLAUDE.md files for project conventions
- Schema templates for similar data types
- Extraction prompt templates
- Validation checklists

### 7. Document the Journey

Your research logs are more valuable than your code:
- What approaches you tried
- What worked and what didn't
- Decisions made and why
- Limitations acknowledged

---

## Resources for "Coding Plus" Researchers

**Communities**:
- GitHub Issue #6208 - Join discussion on non-coding modes
- Claude Code discussions - Share research use cases

**Tools**:
- LlamaIndex `vibe-llama` - Document understanding for agentic workflows
- Anthropic Analysis Tool - Built-in data analysis capabilities
- MCP Servers - Filesystem, database, and custom integrations

**Your Existing Assets**:
- Research-assessor skill - Already designed for this workflow
- Extraction schema v2.5 - Proven in archaeological contexts
- CWTS collaboration - Access to validation data

---

## Next Steps for Your Current Project

### 15-Year Archaeological Data Extraction

**Immediate (Week 1)**:
1. Run comprehensive inventory using Claude Code
2. Test extraction on 10 representative documents
3. Develop initial schema from results

**Short-term (Month 1)**:
1. Pilot extraction on 100 documents
2. Build validation workflow
3. Refine schema based on errors

**Medium-term (Months 2-3)**:
1. Batch process with quality control
2. Human review of flagged items
3. Merge into unified database

**Long-term (Months 4-5)**:
1. Comprehensive validation
2. Documentation for archive
3. Delivery to repository

### Setting Realistic Expectations

- Expect 80-90% automation success
- Plan for 10-20% manual handling
- Budget time for validation
- Accept "good enough" for non-critical data
- Focus perfection on core datasets

---

## Conclusion

You're not "misusing" Claude Code - you're pioneering legitimate research automation workflows. The "coding plus" approach recognizes that code is a means to knowledge, not an end in itself.

Your work extracting research data, building taxonomies, and mining historical corpora represents exactly the kind of intellectual work that AI should augment: tedious pattern matching at scale, with human judgment applied where it matters.

Keep using Claude Code as your research infrastructure. The distinction between "coding" and "research automation" will fade as tools mature. You're ahead of the curve.