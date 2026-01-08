# Advanced Claude Code Techniques for Research Assessment Pipelines

**Focus Areas**: Automation & Headless Mode, Model Context Protocol (MCP), Test-Driven Development

**Context**: This guide is tailored for automated extraction of Claims-Evidence-Methods (CEM) and Research Design-Methods-Protocols (RDMAP) data from academic papers.

---

## Table of Contents

1. [Automation & Headless Mode](#automation--headless-mode)
2. [Model Context Protocol (MCP)](#model-context-protocol-mcp)
3. [Test-Driven Development with Claude](#test-driven-development-with-claude)
4. [Integration: Combining All Three](#integration-combining-all-three)

---

## Automation & Headless Mode

### What Is Headless Mode?

Headless mode enables non-interactive Claude Code usage for:
- CI/CD pipelines
- Pre-commit hooks
- Build scripts
- Batch processing
- Scheduled automation

Unlike interactive sessions, headless mode executes a single prompt and exits, making it ideal for scripted workflows.

### Basic Syntax

```bash
# Simple headless execution
claude -p "your prompt here"

# With JSON output for parsing
claude -p "analyze this code" --output-format stream-json

# With specific file context
claude -p "extract claims from this paper" @paper.pdf --output-format json
```

### Headless Mode Flags

| Flag | Purpose | Example |
|------|---------|---------|
| `-p` | Headless prompt mode | `claude -p "task"` |
| `--output-format` | Output type: `text`, `json`, `stream-json` | `--output-format json` |
| `--max-turns` | Limit conversation depth | `--max-turns 1` |
| `--add-dir` | Add directories to context | `--add-dir ./papers` |
| `--continue` | Continue previous session | `claude --continue -p "next step"` |

**Note**: Headless mode does NOT persist between sessions - you must trigger it each time.

### Research Pipeline Use Cases

#### 1. Batch Paper Processing

```bash
#!/bin/bash
# process_corpus.sh - Extract from all papers in directory

PAPERS_DIR="./corpus/papers"
OUTPUT_DIR="./extractions"
SCHEMA="./schemas/extraction_v2.5.json"

mkdir -p "$OUTPUT_DIR"

for paper in "$PAPERS_DIR"/*.pdf; do
    filename=$(basename "$paper" .pdf)
    echo "Processing: $filename"
    
    claude -p "Extract claims, evidence, and methods from this paper. 
    Follow the schema at @$SCHEMA. 
    Output valid JSON only." \
    @"$paper" \
    --output-format json \
    --max-turns 3 \
    > "$OUTPUT_DIR/${filename}_extraction.json" 2>&1
    
    # Validate output
    if jq empty "$OUTPUT_DIR/${filename}_extraction.json" 2>/dev/null; then
        echo "âœ“ $filename: Valid JSON"
    else
        echo "âœ— $filename: Invalid JSON - check logs"
    fi
done

echo "Batch processing complete: $(ls -1 $OUTPUT_DIR | wc -l) files processed"
```

#### 2. Validation Pipeline

```bash
#!/bin/bash
# validate_extractions.sh - Validate extracted data against schema

for extraction in extractions/*.json; do
    filename=$(basename "$extraction")
    
    claude -p "Validate this extraction against the schema requirements:
    1. All claims must have source_quote or trigger_text
    2. Evidence must map to specific claims via claim_ids
    3. Methods must have both description and justification_claims
    4. Check for hallucinations (content not in source)
    
    Return JSON: {\"valid\": bool, \"errors\": [list], \"warnings\": [list]}" \
    @"$extraction" \
    @schemas/extraction_v2.5.json \
    --output-format json \
    > "validations/${filename%.json}_validation.json"
done
```

#### 3. GitHub Issue Automation

```bash
#!/bin/bash
# auto_label_issues.sh - Automatically label and triage GitHub issues

# Triggered by GitHub webhook or cron
issue_number=$1
issue_body=$(gh issue view $issue_number --json body -q .body)

labels=$(claude -p "Analyze this GitHub issue and suggest appropriate labels.
Issue: $issue_body

Available labels: bug, feature, documentation, schema-change, extraction-quality, needs-validation

Return JSON array of relevant labels only." \
--output-format json | jq -r '.[]')

# Apply labels
for label in $labels; do
    gh issue edit $issue_number --add-label "$label"
done

echo "Applied labels: $labels"
```

#### 4. Pre-Commit Hook for Schema Changes

```bash
#!/bin/bash
# .git/hooks/pre-commit

# Check if schema files changed
if git diff --cached --name-only | grep -q "schemas/"; then
    echo "Schema changes detected, validating..."
    
    claude -p "Review these schema changes for:
    1. Breaking changes that affect existing extractions
    2. Missing documentation in CHANGELOG
    3. Need for migration scripts
    4. Backward compatibility issues
    
    If critical issues found, exit with error." \
    @schemas/extraction_v2.5.json \
    --output-format text
    
    if [ $? -ne 0 ]; then
        echo "Schema validation failed - commit blocked"
        exit 1
    fi
fi
```

#### 5. Scheduled Corpus Analysis

```bash
#!/bin/bash
# weekly_corpus_report.sh - Run via cron every Monday

claude -p "Analyze all extractions from the past week:
1. Count total papers processed
2. Identify papers with validation errors
3. Track most common extraction patterns
4. Flag papers needing manual review
5. Calculate extraction confidence scores

Generate markdown report." \
@extractions/*_$(date -v-7d +%Y%m%d)*.json \
--output-format text \
> reports/weekly_$(date +%Y%m%d).md

# Email report to team
mail -s "Weekly Extraction Report" team@example.com < reports/weekly_$(date +%Y%m%d).md
```

### Advanced Patterns

#### Piped Input Processing

```bash
# Process stdin
cat paper_metadata.json | claude -p "Extract DOIs and generate bibliographic entries"

# Chain multiple Claude calls
claude -p "Extract claims from paper" @paper.pdf --output-format json | \
claude -p "Rate credibility of each claim on 1-5 scale" --output-format json | \
jq '.claims[] | select(.credibility < 3)'
```

#### Parallel Processing

```bash
#!/bin/bash
# parallel_extraction.sh - Process multiple papers simultaneously

MAX_PARALLEL=4
export PAPERS_DIR="./corpus"
export OUTPUT_DIR="./extractions"

process_paper() {
    paper=$1
    filename=$(basename "$paper" .pdf)
    
    claude -p "Extract CEM data from paper" @"$paper" \
    --output-format json \
    > "$OUTPUT_DIR/${filename}.json"
}

export -f process_paper

# Process papers in parallel
find "$PAPERS_DIR" -name "*.pdf" | \
parallel -j $MAX_PARALLEL process_paper {}

echo "Parallel processing complete"
```

### Error Handling

```bash
#!/bin/bash
# robust_extraction.sh - With retry logic and error handling

extract_with_retry() {
    paper=$1
    max_attempts=3
    attempt=1
    
    while [ $attempt -le $max_attempts ]; do
        echo "Attempt $attempt for $(basename $paper)"
        
        output=$(claude -p "Extract claims and evidence" @"$paper" \
                --output-format json 2>&1)
        
        if echo "$output" | jq empty 2>/dev/null; then
            echo "$output" > "extractions/$(basename $paper .pdf).json"
            return 0
        else
            echo "Failed attempt $attempt: Invalid JSON"
            attempt=$((attempt + 1))
            sleep 5
        fi
    done
    
    echo "FAILED after $max_attempts attempts: $paper" >> failed_extractions.log
    return 1
}

# Process with error tracking
for paper in papers/*.pdf; do
    extract_with_retry "$paper" || continue
done
```

### Output Format Strategies

#### JSON Output

```bash
# Clean JSON for parsing
claude -p "Extract data" @paper.pdf \
--output-format json | \
jq '.claims[] | {id, text, confidence}'

# Stream JSON for large outputs
claude -p "Process large dataset" \
--output-format stream-json | \
while IFS= read -r line; do
    # Process each JSON object as it arrives
    echo "$line" | jq -r '.claim_text'
done
```

#### Text Output with Structured Parsing

```bash
# Get text output and parse
result=$(claude -p "Analyze paper structure. 
Output format:
SECTIONS: list
CLAIMS: count
METHODS: list" \
@paper.pdf --output-format text)

# Parse structured text
sections=$(echo "$result" | grep "SECTIONS:" | cut -d: -f2)
claims_count=$(echo "$result" | grep "CLAIMS:" | cut -d: -f2)
```

### Performance Optimization

```bash
# Limit context for faster processing
claude -p "Quick extraction" @paper.pdf \
--max-turns 1 \
--output-format json

# Use compact mode for minimal context
claude -p "Analyze with minimal context" \
--compact-mode \
@small_file.txt

# Cache results for repetitive tasks
claude -p "Standard extraction pattern" \
--cache-results \
@paper.pdf
```

---

## Model Context Protocol (MCP)

### What Is MCP?

Model Context Protocol is Claude Code's system for connecting to external tools and data sources. Think of it as giving Claude direct access to databases, filesystems, APIs, and services without manual data piping.

### Why MCP Matters for Research Pipelines

Instead of:
```bash
# Manual approach
sqlite3 extractions.db "SELECT * FROM claims" > claims.txt
claude -p "analyze these claims" @claims.txt
```

You can:
```bash
# MCP approach  
claude "Query the extractions database for all claims with confidence < 0.7 and analyze patterns"
# Claude directly queries SQLite, no intermediate files
```

### Installing MCP Servers

```bash
# List available MCP servers
claude mcp list

# Add MCP server
claude mcp add <server-name> -- npx <package-name>

# Remove MCP server
claude mcp remove <server-name>

# Check status
claude mcp get <server-name>
```

### Core MCP Servers for Research Workflows

#### 1. Filesystem MCP - Advanced File Operations

```bash
# Install
claude mcp add filesystem -- npx @modelcontextprotocol/server-filesystem

# Usage examples
claude "Search all PDF files in corpus/ for papers about crowdsourcing"

claude "Find all extraction JSON files modified in last 7 days with validation errors"

claude "Compare extraction_v2.4.json and extraction_v2.5.json, show differences in schema structure"

claude "Create index of all papers processed, grouped by discipline (archaeology, ecology, ethnography)"
```

**Real use case**:
```bash
# Find papers needing re-extraction after schema update
claude "Search extractions/ for files created before 2025-01-01. 
Check each extraction against current schema at schemas/extraction_v2.5.json. 
Generate list of papers needing re-extraction with reasons."
```

#### 2. PostgreSQL/SQLite MCP - Database Integration

```bash
# Install PostgreSQL MCP
claude mcp add postgres -- npx @modelcontextprotocol/server-postgres

# Or SQLite for local databases
claude mcp add sqlite -- npx @modelcontextprotocol/server-sqlite
```

**Configuration** (add to ~/.claude/config.json):
```json
{
  "mcpServers": {
    "postgres": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-postgres"],
      "env": {
        "POSTGRES_CONNECTION": "postgresql://user:pass@localhost:5432/extractions_db"
      }
    }
  }
}
```

**Usage examples**:
```bash
# Direct database queries
claude "Query extractions database: 
SELECT paper_id, COUNT(claim_id) as claim_count 
FROM claims 
WHERE credibility_score < 0.6 
GROUP BY paper_id 
ORDER BY claim_count DESC"

# Complex analysis
claude "From the extractions database:
1. Find all papers with >10 claims but <3 evidence items
2. Calculate evidence-to-claim ratio by discipline
3. Identify papers with highest ratio of implicit vs explicit claims
4. Generate summary report as markdown"

# Data validation
claude "Check extractions database for:
- Orphaned evidence items (no matching claim_ids)
- Claims without source_quote or trigger_text
- Methods without justification_claims
Generate fix script for identified issues"
```

**Research-specific queries**:
```bash
# Calibration analysis with repliCATS data
claude "Join extractions database with replicats_judgements table.
For papers in both datasets:
1. Compare extracted claims vs expert-identified claims
2. Calculate precision/recall metrics
3. Identify systematic extraction gaps
4. Suggest prompt improvements"

# Track extraction evolution
claude "Query extractions database timeline:
Show how extraction schema versions affected:
- Average claims per paper
- Evidence granularity distribution  
- Method description completeness
Generate visualization data as JSON"
```

#### 3. GitHub MCP - Repository Integration

```bash
# Install
claude mcp add github -- npx @modelcontextprotocol/server-github

# Configuration
# Set GITHUB_TOKEN environment variable with repo access
```

**Usage examples**:
```bash
# Issue management
claude "Search GitHub issues for 'extraction hallucination' problems. 
Analyze patterns in reported issues.
Suggest which prompt modifications address most issues."

# PR review automation  
claude "Review this PR for extraction schema changes.
Check for:
- Breaking changes requiring migration
- Missing test coverage for new fields
- Documentation updates needed
- Backward compatibility issues"

# Collaboration tracking
claude "Analyze GitHub commits from @collaborator in last month.
What schema changes did they make?
Are there unresolved design decisions in PR comments?"
```

**Automated workflows**:
```bash
# Create issues from validation failures
claude "For each file in validation_errors/:
1. Read validation report
2. Create GitHub issue with:
   - Title: 'Extraction validation failed: [paper_name]'
   - Body: validation errors + paper context
   - Labels: extraction-quality, needs-review
   - Assignment: appropriate team member based on error type"
```

#### 4. Puppeteer MCP - Web Scraping & Screenshots

```bash
# Install
claude mcp add puppeteer -- npx @modelcontextprotocol/server-puppeteer

# Use cases
claude "Navigate to https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0123456
Take screenshot of methodology section
Extract supplementary material URLs"

# Corpus building
claude "Scrape https://archaeologydataservice.ac.uk/search?query=crowdsourcing
Extract paper DOIs, titles, and PDF links
Save as corpus_metadata.json"
```

#### 5. Custom MCP Server for RepliCATS Data

You can create custom MCP servers for your specific needs.

**Example: RepliCATS API MCP** (conceptual):
```javascript
// replicats-mcp-server.js
import { Server } from '@modelcontextprotocol/sdk/server/index.js';

const server = new Server({
  name: 'replicats-server',
  version: '1.0.0',
});

// Tool: Query repliCATS judgements
server.tool('query_replicats_judgements', 
  'Query repliCATS credibility judgements database',
  {
    paper_id: { type: 'string', required: false },
    signal_type: { 
      type: 'string', 
      enum: ['transparency', 'plausibility', 'robustness']
    },
    min_score: { type: 'number', required: false }
  },
  async (params) => {
    // Query your repliCATS database
    const results = await db.query(
      'SELECT * FROM judgements WHERE ...',
      params
    );
    return { content: [{ type: 'text', text: JSON.stringify(results) }] };
  }
);

server.listen();
```

**Usage**:
```bash
claude mcp add replicats -- node ./replicats-mcp-server.js

claude "Query repliCATS judgements for papers with transparency score > 4.
Compare with my extractions to see if I'm capturing the same transparent elements."
```

### MCP Scope Management

```bash
# Project-specific (default) - only in this project
claude mcp add memory-keeper npx mcp-memory-keeper

# Shared with team via .mcp.json (committed to repo)
claude mcp add --scope project memory-keeper npx mcp-memory-keeper

# User-global - available across all your projects
claude mcp add --scope user memory-keeper npx mcp-memory-keeper
```

### MCP Best Practices

**1. Start with filesystem and database MCPs** - highest impact for research workflows

**2. Chain MCP operations**:
```bash
claude "Use filesystem MCP to find all papers from 2024.
Use postgres MCP to check which have extractions.
Use github MCP to create extraction queue issue for missing papers."
```

**3. MCP for validation loops**:
```bash
# Continuous validation
claude "Monitor extractions/ directory with filesystem MCP.
When new extraction appears:
1. Validate against schema
2. Check database for duplicates
3. Run hallucination detection
4. If issues found, create GitHub issue
5. If clean, insert into postgres database"
```

**4. Security**: MCP servers have full access to their configured resources
- Use read-only database credentials where possible
- Restrict filesystem MCP to specific directories
- Review MCP server code before installation

### Debugging MCP

```bash
# Enable MCP debug mode
claude --mcp-debug

# Check MCP server logs
# Output appears in Claude Code's output panel in IDE

# Test MCP server manually
npx @modelcontextprotocol/server-postgres # should start without errors
```

---

## Test-Driven Development with Claude

### Why TDD for Extraction Pipelines?

Traditional coding TDD: Write tests â†’ Tests fail â†’ Write code â†’ Tests pass

Extraction pipeline TDD: Define expected outputs â†’ Claude extracts â†’ Validate â†’ Refine prompts

This creates:
- Regression detection when prompt changes affect quality
- Objective validation metrics vs subjective "looks good"
- Calibration data for comparing against repliCATS judgements
- Documentation of expected behavior

### TDD Workflow

```
1. Define expected extraction for calibration paper
2. Create test that checks for those specific elements
3. Run extraction (fails test initially)
4. Refine prompt/schema
5. Re-extract until test passes
6. Commit passing prompt as validated
7. Apply to corpus with confidence
```

### Implementation Strategies

#### Strategy 1: JSON Schema Validation

**Create test suite**:
```javascript
// tests/extraction_validation.test.js
import Ajv from 'ajv';
import fs from 'fs';

const ajv = new Ajv();

// Load schema
const schema = JSON.parse(
  fs.readFileSync('./schemas/extraction_v2.5.json')
);
const validate = ajv.compile(schema);

// Load test extraction
const extraction = JSON.parse(
  fs.readFileSync('./test_data/sobotkova2023_extraction.json')
);

describe('Schema Validation', () => {
  test('Extraction matches schema v2.5', () => {
    const valid = validate(extraction);
    if (!valid) console.log(validate.errors);
    expect(valid).toBe(true);
  });
  
  test('All claims have source attribution', () => {
    extraction.claims.forEach(claim => {
      expect(
        claim.source_quote || claim.trigger_text
      ).toBeTruthy();
    });
  });
  
  test('Evidence maps to valid claim IDs', () => {
    const claimIds = new Set(extraction.claims.map(c => c.id));
    extraction.evidence.forEach(ev => {
      ev.supports_claims.forEach(claimId => {
        expect(claimIds.has(claimId)).toBe(true);
      });
    });
  });
});
```

**Run TDD cycle**:
```bash
# 1. Tests fail initially
npm test

# 2. Extract with current prompt
claude -p "Extract CEM from paper following extraction_v2.5 schema" \
  @papers/sobotkova2023.pdf \
  --output-format json \
  > test_data/sobotkova2023_extraction.json

# 3. Tests still fail - check which assertions failed
npm test

# 4. Refine prompt based on failures
claude -p "Extract CEM from paper. 
CRITICAL: Every claim MUST have either source_quote (direct quote) 
or trigger_text (paraphrase indicator).
Evidence items must list claim IDs they support." \
  @papers/sobotkova2023.pdf \
  --output-format json \
  > test_data/sobotkova2023_extraction.json

# 5. Tests pass
npm test

# 6. Commit validated prompt
git add extraction_prompts/v2.5_pass1.md
git commit -m "Validated prompt: source attribution now 100%"
```

#### Strategy 2: Expected Output Testing

**Define ground truth**:
```json
// test_data/sobotkova2023_expected.json
{
  "paper_id": "sobotkova2023",
  "expected_claims": [
    {
      "text_contains": "crowdsourced data collection can achieve professional quality",
      "claim_type": "effectiveness",
      "must_have_evidence_count": 3
    },
    {
      "text_contains": "TRAP platform enabled collaborative fieldwork",
      "claim_type": "methodological",
      "must_have_method_link": true
    }
  ],
  "expected_methods": [
    {
      "method_type": "data_collection",
      "text_contains": "mobile application for archaeological survey"
    }
  ],
  "minimum_claim_count": 12,
  "minimum_evidence_count": 25
}
```

**Test implementation**:
```javascript
// tests/expected_output.test.js
import fs from 'fs';

const expected = JSON.parse(
  fs.readFileSync('./test_data/sobotkova2023_expected.json')
);
const actual = JSON.parse(
  fs.readFileSync('./test_data/sobotkova2023_extraction.json')
);

describe('Expected Output Validation', () => {
  test('Minimum claim count met', () => {
    expect(actual.claims.length).toBeGreaterThanOrEqual(
      expected.minimum_claim_count
    );
  });
  
  test('Key claims extracted', () => {
    expected.expected_claims.forEach(expectedClaim => {
      const found = actual.claims.some(claim => 
        claim.text.includes(expectedClaim.text_contains)
      );
      expect(found).toBe(true);
    });
  });
  
  test('Claims have required evidence', () => {
    expected.expected_claims.forEach(expectedClaim => {
      const claim = actual.claims.find(c => 
        c.text.includes(expectedClaim.text_contains)
      );
      
      if (claim && expectedClaim.must_have_evidence_count) {
        const evidenceCount = actual.evidence.filter(e =>
          e.supports_claims.includes(claim.id)
        ).length;
        
        expect(evidenceCount).toBeGreaterThanOrEqual(
          expectedClaim.must_have_evidence_count
        );
      }
    });
  });
});
```

#### Strategy 3: Calibration Against RepliCATS

**Leverage existing judgements**:
```javascript
// tests/replicats_calibration.test.js
import fs from 'fs';

const replicatsData = JSON.parse(
  fs.readFileSync('./calibration_data/replicats_judgements.json')
);

const extraction = JSON.parse(
  fs.readFileSync('./test_data/sobotkova2023_extraction.json')
);

describe('RepliCATS Calibration', () => {
  test('Transparency elements match expert judgements', () => {
    const replicatsTransparency = replicatsData.papers
      .find(p => p.id === 'sobotkova2023')
      .transparency_elements;
    
    // Check if extraction captured same transparency signals
    const extractedTransparency = [
      extraction.methods.some(m => m.text.includes('sample size')),
      extraction.methods.some(m => m.text.includes('measurement procedure')),
      extraction.methods.some(m => m.description_completeness === 'complete')
    ];
    
    const matchRate = extractedTransparency.filter(Boolean).length / 
                      replicatsTransparency.length;
    
    expect(matchRate).toBeGreaterThan(0.7); // 70% alignment threshold
  });
  
  test('Claim count within expert range', () => {
    const replicatsClaims = replicatsData.papers
      .find(p => p.id === 'sobotkova2023')
      .expert_claim_count;
    
    const variance = Math.abs(extraction.claims.length - replicatsClaims.mean);
    
    expect(variance).toBeLessThan(replicatsClaims.std_dev * 2);
  });
});
```

#### Strategy 4: Claude-as-Validator (Meta-Testing)

**Have Claude test Claude**:
```bash
# Extract
claude -p "Extract claims from paper" \
  @papers/sobotkova2023.pdf \
  --output-format json \
  > extraction.json

# Validate with different Claude instance
claude -p "You are a validation agent. Check this extraction for:

1. Hallucinations: Claims not supported by paper text
2. Missing key claims: Compare against paper's main findings
3. Evidence quality: Is evidence specific and verifiable?
4. Method completeness: Are protocols described adequately?

For each issue found, provide:
- Issue type
- Specific location (claim/evidence ID)
- Severity (critical/major/minor)
- Recommended fix

Output JSON: {\"issues\": [...], \"overall_quality_score\": 0-100}" \
  @extraction.json \
  @papers/sobotkova2023.pdf \
  --output-format json \
  > validation_report.json

# Test passes if quality score > threshold
validation_score=$(jq '.overall_quality_score' validation_report.json)
if [ "$validation_score" -lt 85 ]; then
  echo "FAIL: Quality score $validation_score below threshold 85"
  exit 1
fi
```

### TDD Workflow Integration

**Full TDD pipeline script**:
```bash
#!/bin/bash
# tdd_extraction_pipeline.sh

PAPER=$1
PAPER_ID=$(basename "$PAPER" .pdf)
PROMPT_VERSION="v2.5"
PASS="pass1"

echo "=== TDD Extraction Pipeline ==="
echo "Paper: $PAPER_ID"
echo "Prompt: $PROMPT_VERSION $PASS"

# Step 1: Run extraction
echo "Step 1: Extracting..."
claude -p "@prompts/extraction_${PROMPT_VERSION}_${PASS}.md" \
  @"$PAPER" \
  --output-format json \
  > "test_output/${PAPER_ID}_extraction.json"

# Step 2: Schema validation
echo "Step 2: Schema validation..."
ajv validate \
  -s schemas/extraction_v2.5.json \
  -d "test_output/${PAPER_ID}_extraction.json"

if [ $? -ne 0 ]; then
  echo "FAIL: Schema validation failed"
  exit 1
fi

# Step 3: Run test suite
echo "Step 3: Running test suite..."
npm test -- "test_output/${PAPER_ID}_extraction.json"

if [ $? -ne 0 ]; then
  echo "FAIL: Tests failed"
  echo "Review test output and refine prompt"
  exit 1
fi

# Step 4: Calibration check (if applicable)
if [ -f "calibration_data/${PAPER_ID}_expected.json" ]; then
  echo "Step 4: Calibration check..."
  npm test -- --testPathPattern=calibration
  
  if [ $? -ne 0 ]; then
    echo "WARN: Calibration mismatch - review differences"
  fi
fi

# Step 5: Meta-validation
echo "Step 5: Meta-validation (Claude-as-validator)..."
quality_score=$(claude -p "Validate this extraction for quality. 
Output JSON with overall_quality_score (0-100) only." \
  @"test_output/${PAPER_ID}_extraction.json" \
  @"$PAPER" \
  --output-format json | jq -r '.overall_quality_score')

echo "Quality score: $quality_score"

if [ "$quality_score" -lt 85 ]; then
  echo "FAIL: Quality score below threshold"
  exit 1
fi

# All tests passed
echo "âœ“ All tests passed!"
echo "Extraction validated for $PAPER_ID"
```

**Usage**:
```bash
# Run TDD pipeline on calibration paper
./tdd_extraction_pipeline.sh papers/sobotkova2023.pdf

# If tests fail, refine prompt and re-run
vim prompts/extraction_v2.5_pass1.md
./tdd_extraction_pipeline.sh papers/sobotkova2023.pdf

# Once passing, apply to corpus with confidence
for paper in corpus/*.pdf; do
  ./tdd_extraction_pipeline.sh "$paper"
done
```

### Pre-Commit Hook for Prompt Changes

```bash
#!/bin/bash
# .git/hooks/pre-commit - Run tests when prompt files change

if git diff --cached --name-only | grep -q "^prompts/"; then
  echo "Prompt changes detected, running validation tests..."
  
  # Run on calibration papers
  for paper in test_data/calibration_papers/*.pdf; do
    ./tdd_extraction_pipeline.sh "$paper" || exit 1
  done
  
  echo "âœ“ All calibration tests passed with updated prompts"
fi
```

### Continuous Integration Example

```yaml
# .github/workflows/extraction_validation.yml
name: Extraction Validation

on:
  pull_request:
    paths:
      - 'prompts/**'
      - 'schemas/**'

jobs:
  validate:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Setup Node
        uses: actions/setup-node@v3
        with:
          node-version: '18'
      
      - name: Install dependencies
        run: npm install
      
      - name: Install Claude Code
        run: npm install -g @anthropic-ai/claude-code
      
      - name: Run TDD pipeline on calibration papers
        run: |
          for paper in test_data/calibration_papers/*.pdf; do
            ./tdd_extraction_pipeline.sh "$paper"
          done
      
      - name: Upload test results
        if: always()
        uses: actions/upload-artifact@v3
        with:
          name: test-results
          path: test_output/
```

---

## Integration: Combining All Three

### End-to-End Automated Pipeline

**Scenario**: Fully automated extraction, validation, and storage pipeline

```bash
#!/bin/bash
# automated_research_pipeline.sh

CORPUS_DIR="./corpus/new_papers"
EXTRACT_DIR="./extractions"
FAILED_DIR="./extractions_failed"

mkdir -p "$EXTRACT_DIR" "$FAILED_DIR"

# Process each paper
for paper in "$CORPUS_DIR"/*.pdf; do
  paper_id=$(basename "$paper" .pdf)
  echo "Processing: $paper_id"
  
  # 1. Headless extraction with TDD prompt
  claude -p "@prompts/extraction_validated_v2.5.md" \
    @"$paper" \
    --output-format json \
    > "$EXTRACT_DIR/${paper_id}_raw.json"
  
  # 2. Run test suite (TDD validation)
  npm test -- "$EXTRACT_DIR/${paper_id}_raw.json" > /dev/null 2>&1
  
  if [ $? -eq 0 ]; then
    echo "âœ“ Tests passed for $paper_id"
    
    # 3. Store in database (via MCP)
    claude "Using postgres MCP, insert this extraction into database:
    - Table: extractions
    - Include paper_id: $paper_id
    - Include extraction_date: $(date -I)
    - Include validation_status: 'passed'
    
    If paper_id already exists, update instead." \
    @"$EXTRACT_DIR/${paper_id}_raw.json"
    
    # 4. Create GitHub issue for review (via MCP)
    claude "Using github MCP, create issue:
    Title: 'Review extraction: $paper_id'
    Labels: extraction-complete, needs-review
    Body: Extraction completed and validated. 
          Database entry created.
          Awaiting expert review.
    Assignee: expert-reviewer"
    
  else
    echo "âœ— Tests failed for $paper_id"
    mv "$EXTRACT_DIR/${paper_id}_raw.json" "$FAILED_DIR/"
    
    # Create failure issue
    claude "Using github MCP, create issue:
    Title: 'Extraction validation failed: $paper_id'
    Labels: extraction-quality, needs-attention
    Body: Automated extraction failed validation tests.
          Paper requires manual review or prompt refinement.
          See failed_extractions/$paper_id for details."
  fi
done

# Generate summary report
claude "Using filesystem MCP and postgres MCP:
1. Count papers processed today
2. Query database for success rate
3. List papers in failed_extractions/
4. Generate markdown summary report

Save to reports/daily_$(date -I).md"
```

### Dashboard with Real-Time Monitoring

**Setup MCP-enabled monitoring**:
```bash
#!/bin/bash
# monitor_pipeline.sh - Run continuously or via cron

while true; do
  claude "Using postgres MCP and filesystem MCP:
  
  1. Query extractions database:
     - Papers processed in last hour
     - Current success rate (last 24h)
     - Papers awaiting validation
  
  2. Check filesystem for:
     - Papers in processing queue
     - Papers in failed directory
     - Disk space remaining
  
  3. Generate status dashboard as markdown:
     - Metrics summary
     - Recent activity log
     - Alerts if failure rate > 10%
  
  Output to stdout for terminal display" | tee pipeline_status.txt
  
  # Display in terminal
  cat pipeline_status.txt
  
  sleep 300  # Update every 5 minutes
done
```

### Comparative Analysis Pipeline

**Compare extraction approaches using TDD**:
```bash
#!/bin/bash
# compare_approaches.sh - A/B test different extraction strategies

PAPER="papers/test_paper.pdf"
APPROACHES=("whole_paper" "section_by_section" "iterative_refinement")

for approach in "${APPROACHES[@]}"; do
  echo "Testing approach: $approach"
  
  # Extract with different prompt
  claude -p "@prompts/extraction_${approach}.md" \
    @"$PAPER" \
    --output-format json \
    > "comparison/${approach}_extraction.json"
  
  # Run TDD validation
  test_results=$(npm test -- "comparison/${approach}_extraction.json" 2>&1)
  
  # Meta-validate
  quality=$(claude -p "Rate extraction quality 0-100" \
    @"comparison/${approach}_extraction.json" \
    --output-format json | jq -r '.score')
  
  # Store results
  echo "$approach: quality=$quality" >> comparison/results.txt
done

# Compare via MCP
claude "Using filesystem MCP:
1. Read all extraction files in comparison/
2. Compare claim counts, evidence density, method completeness
3. Identify which approach captured most complete data
4. Generate recommendation for production use

Save analysis to comparison/recommendation.md"
```

### Self-Healing Pipeline

**Pipeline that automatically refines prompts based on test failures**:
```bash
#!/bin/bash
# self_healing_pipeline.sh

PAPER=$1
MAX_ITERATIONS=3
iteration=0

while [ $iteration -lt $MAX_ITERATIONS ]; do
  echo "Iteration $((iteration+1)): Extracting..."
  
  # Extract
  claude -p "@prompts/extraction_current.md" @"$PAPER" \
    --output-format json > extraction_attempt.json
  
  # Test
  test_output=$(npm test -- extraction_attempt.json 2>&1)
  
  if [ $? -eq 0 ]; then
    echo "âœ“ Tests passed!"
    mv extraction_attempt.json extractions/final.json
    exit 0
  fi
  
  # Tests failed - ask Claude to fix the prompt
  echo "âœ— Tests failed, refining prompt..."
  
  claude -p "These tests failed:
$test_output

Current prompt:
$(cat prompts/extraction_current.md)

Analyze the test failures and suggest specific modifications 
to the prompt that will address these issues.

Output only the revised prompt text, no explanation." \
  > prompts/extraction_current.md
  
  iteration=$((iteration+1))
done

echo "Failed to extract successfully after $MAX_ITERATIONS iterations"
exit 1
```

---

## Quick Start Checklist

### Week 1: Headless Mode
- [ ] Convert one manual extraction to headless script
- [ ] Create batch processing script for 10 papers
- [ ] Set up error handling and retry logic
- [ ] Create validation pipeline script

### Week 2: MCP
- [ ] Install filesystem MCP
- [ ] Install postgres/sqlite MCP
- [ ] Set up extraction database
- [ ] Create MCP-enabled query scripts

### Week 3: TDD
- [ ] Write JSON schema validation tests
- [ ] Create expected output tests for 3 calibration papers
- [ ] Integrate tests into pre-commit hook
- [ ] Document TDD workflow for team

### Week 4: Integration
- [ ] Combine all three into end-to-end pipeline
- [ ] Set up monitoring dashboard
- [ ] Create GitHub Actions for CI
- [ ] Document full pipeline for CWTS presentation

---

## Troubleshooting

### Headless Mode Issues

**Problem**: Claude times out on long papers
```bash
# Solution: Split into phases
claude -p "Phase 1: Extract claims only" @paper.pdf > claims.json
claude -p "Phase 2: Extract evidence for these claims" @claims.json @paper.pdf > evidence.json
```

**Problem**: JSON output contains text wrapper
```bash
# Solution: Parse and extract JSON
claude -p "..." --output-format json | \
  sed -n '/^{/,/^}/p' | \
  jq '.'
```

### MCP Issues

**Problem**: MCP server won't start
```bash
# Debug mode
claude --mcp-debug

# Check manually
npx @modelcontextprotocol/server-postgres
# Should start without errors

# Check config
cat ~/.claude/config.json
```

**Problem**: Permission denied accessing database
```bash
# Use read-only credentials for MCP
# In config: "POSTGRES_CONNECTION": "postgresql://readonly_user:..."
```

### TDD Issues

**Problem**: Tests too brittle - fail on minor variations
```bash
# Solution: Test patterns, not exact matches
expect(claim.text).toMatch(/crowdsourc(ed|ing)/i);  // Flexible
expect(claim.text).toBe("crowdsourced data");        // Brittle
```

**Problem**: Unclear why test failed
```bash
# Solution: Add descriptive test messages
expect(evidenceCount).toBeGreaterThan(3, 
  `Expected >3 evidence items for claim "${claim.text}", found ${evidenceCount}`
);
```

---

## Additional Resources

- [Claude Code Official Docs](https://docs.claude.com/en/docs/claude-code)
- [MCP Specification](https://spec.modelcontextprotocol.io/)
- [Anthropic Best Practices](https://www.anthropic.com/engineering/claude-code-best-practices)
- Your existing research-assessor skill package
- CWTS Implementation Plan documents

---

## Next Steps for Your Research Pipeline

1. **Start with headless batch processing** - immediate productivity gain on the ~3,900 paper corpus

2. **Add PostgreSQL MCP** - enables sophisticated analysis of extraction patterns

3. **Implement TDD on calibration papers** - validates prompt quality before scaling

4. **Create automated validation pipeline** - combines all three for continuous quality assurance

5. **Present at CWTS** - show fully automated, validated extraction pipeline with measurable quality metrics

The combination of these three techniques transforms Claude Code from an interactive assistant into a production-grade research automation platform.