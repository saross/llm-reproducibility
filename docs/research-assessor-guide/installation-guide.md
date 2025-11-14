# Installation Guide

**Version:** 2.6
**Last Updated:** 2025-11-13

Complete setup guide for the Research Assessor skill extraction system.

---

## Prerequisites

### System Requirements

- **Operating System:** Linux, macOS, or Windows with WSL
- **Python:** 3.8+ (for validation scripts)
- **Tools:** `pdftotext`, `jq`, `git`
- **Claude AI:** Access to Claude Sonnet 4.5 or later with Skills support

### Recommended Setup

- **Terminal:** Bash or Zsh
- **Text Editor:** VS Code, Sublime, or similar with JSON support
- **PDF Tools:** `pdftotext` (part of Poppler utilities)
- **JSON Tools:** `jq` for JSON validation and manipulation

---

## Installation Steps

### Step 1: Verify Skill Installation

The Research Assessor skill is located in `.claude/skills/research-assessor/` within the project repository.

**Check installation:**
```bash
cd /path/to/llm-reproducibility
ls -la .claude/skills/research-assessor/
```

**Expected structure:**
```
.claude/skills/research-assessor/
├── SKILL.md                    # Core skill definition
└── references/                 # Decision frameworks and guides
    ├── checklists/            # Evidence-vs-claims, tier assignment, expected info
    ├── consolidation/         # Consolidation patterns
    ├── infrastructure/        # PIDs, FAIR, permits, funding
    ├── rdmap/                 # Research design patterns
    └── schema/                # Schema definitions
```

**Test skill recognition:**
Ask Claude: "Do you have the research-assessor skill?"

---

### Step 2: Install System Dependencies

#### Linux (Ubuntu/Debian)

```bash
# Install pdftotext
sudo apt-get update
sudo apt-get install poppler-utils

# Install jq
sudo apt-get install jq

# Verify installations
pdftotext -v
jq --version
```

#### macOS

```bash
# Install via Homebrew
brew install poppler
brew install jq

# Verify installations
pdftotext -v
jq --version
```

#### Windows (WSL)

```bash
# Install pdftotext
sudo apt-get update
sudo apt-get install poppler-utils

# Install jq
sudo apt-get install jq
```

---

### Step 3: Verify Extraction Prompts

All extraction prompts are located in `extraction-system/prompts/`.

**Check prompts:**
```bash
ls -lh extraction-system/prompts/

Expected output:
00-metadata_pass0_prompt.md           (~400 lines)
01-claims-evidence_pass1_prompt.md    (~800 lines)
02-claims-evidence_pass2_prompt.md    (~900 lines)
03-rdmap_pass1a_explicit_prompt.md    (~1,000 lines)
04-rdmap_pass1b_implicit_prompt.md    (~800 lines)
05-rdmap_pass2_consolidation_prompt.md (~900 lines)
06-infrastructure_pass6_prompt.md     (~1,200 lines)
07-validation_pass3_prompt.md         (~600 lines)
```

**Total:** ~6,600 lines across 8 prompts

---

### Step 4: Set Up Working Directory

**Create project structure:**
```bash
cd /path/to/llm-reproducibility

# Verify key directories exist
ls -d input/ outputs/ extraction-system/ docs/

# Create new paper directory (example)
mkdir -p outputs/your-paper-slug/
```

**Directory structure:**
```
llm-reproducibility/
├── .claude/skills/research-assessor/   # Skill package
├── extraction-system/                   # Extraction workflow
│   ├── prompts/                         # 8 pass prompts
│   └── schema/                          # JSON schema files
├── input/                               # Input materials
│   ├── papers/                          # PDF papers
│   ├── queue.yaml                       # Processing queue
│   └── WORKFLOW.md                      # Complete workflow guide
├── outputs/                             # Extraction outputs
│   └── {paper-slug}/
│       ├── extraction.json              # Primary extraction
│       └── {paper-slug}.txt             # Extracted text
└── docs/                                # Documentation
    ├── research-assessor-guide/         # This guide
    └── user-guide/                      # User documentation
```

---

### Step 5: Extract Your First Paper

#### 5a. Convert PDF to Text

```bash
# Place PDF in input/papers/
cp /path/to/your-paper.pdf input/papers/

# Extract text (preserve layout)
pdftotext -layout input/papers/your-paper.pdf outputs/your-paper-slug/your-paper-slug.txt

# Verify extraction
head -50 outputs/your-paper-slug/your-paper-slug.txt
```

**Text quality check:**
- Title and authors visible?
- Sections identifiable (Abstract, Methods, Results)?
- Tables readable?
- Minimal OCR errors?

**If text quality poor:** Try alternative extraction methods (see Troubleshooting).

---

#### 5b. Create Blank Template

```bash
# Copy blank template
cp extraction-system/schema/blank-template-v2.6.json outputs/your-paper-slug/extraction.json

# Verify structure
jq 'keys' outputs/your-paper-slug/extraction.json
```

**Expected output:**
```json
[
  "schema_version",
  "extraction_timestamp",
  "extractor",
  "paper_metadata",
  "evidence",
  "claims",
  "implicit_arguments",
  "research_designs",
  "methods",
  "protocols",
  "infrastructure",
  "extraction_notes"
]
```

---

#### 5c. Run Pass 0 (Metadata Extraction)

**Conversation with Claude:**
```
You: I'm using the research-assessor skill for metadata extraction.

Here's the Pass 0 prompt:
[paste extraction-system/prompts/00-metadata_pass0_prompt.md]

Extract metadata from this paper:
[paste title, authors, abstract, DOI from outputs/your-paper-slug/your-paper-slug.txt]

Use this JSON:
[paste outputs/your-paper-slug/extraction.json]

Claude: [Extracts metadata]
```

**Save output:**
```bash
# Claude will return JSON - copy to extraction.json
# Verify metadata populated
jq '.paper_metadata.title' outputs/your-paper-slug/extraction.json
```

**Backup:**
```bash
mkdir -p outputs/your-paper-slug/backups/
cp outputs/your-paper-slug/extraction.json outputs/your-paper-slug/backups/extraction-pass0-metadata.json
```

---

### Step 6: Verify Installation Success

**Checklist:**
- [ ] Skill recognised by Claude ("Do you have research-assessor skill?")
- [ ] All 8 prompts accessible in `extraction-system/prompts/`
- [ ] `pdftotext` installed and working
- [ ] `jq` installed and working
- [ ] Test paper extracted to text successfully
- [ ] Blank template copied and valid JSON
- [ ] Pass 0 metadata extraction completed

**If all checked:** Installation complete! Proceed to [usage-guide.md](usage-guide.md) for full workflow.

---

## Optional Tools

### Python Validation Scripts

**Install Python dependencies:**
```bash
# Create virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install JSON validation
pip install jsonschema
```

**Validation script (example):**
```bash
# Validate extraction against schema
python3 extraction-system/scripts/validate_extraction.py outputs/your-paper-slug/extraction.json
```

---

### JSON Formatting and Verification

**Useful jq commands:**
```bash
# Pretty print JSON
cat extraction.json | jq '.' > extraction-pretty.json

# Count items in each array
jq '{
  evidence: (.evidence|length),
  claims: (.claims|length),
  research_designs: (.research_designs|length),
  methods: (.methods|length),
  protocols: (.protocols|length)
}' extraction.json

# Check FAIR score
jq '.infrastructure.fair_assessment.overall_score' extraction.json

# Check PID connectivity
jq '.infrastructure.pid_connectivity_score' extraction.json

# List all evidence IDs
jq '.evidence[].id' extraction.json

# Find orphaned cross-references
jq '.claims[] | select(.supported_by_evidence | length == 0) | .id' extraction.json
```

---

## Troubleshooting

### Issue: pdftotext produces garbled text

**Symptoms:** Text extraction has many errors, tables unreadable, layout broken.

**Solutions:**

**Option 1: Alternative extraction (preserves layout better)**
```bash
pdftotext -layout -nopgbrk input/papers/your-paper.pdf outputs/your-paper-slug/your-paper-slug.txt
```

**Option 2: Without layout preservation (better for scanned PDFs)**
```bash
pdftotext -raw input/papers/your-paper.pdf outputs/your-paper-slug/your-paper-slug.txt
```

**Option 3: OCR for scanned PDFs**
```bash
# Install OCR tools
sudo apt-get install tesseract-ocr

# Use ocrmypdf
pip install ocrmypdf
ocrmypdf input/papers/your-paper.pdf input/papers/your-paper-ocr.pdf
pdftotext -layout input/papers/your-paper-ocr.pdf outputs/your-paper-slug/your-paper-slug.txt
```

---

### Issue: Skill not recognised by Claude

**Symptoms:** Claude says "I don't have that skill" when asked about research-assessor.

**Solutions:**
✓ Check skill location: `.claude/skills/research-assessor/SKILL.md` exists?
✓ Verify SKILL.md format (proper YAML frontmatter)
✓ Restart Claude Code session
✓ Check Claude Code version (v2.0.36+)

---

### Issue: JSON syntax errors after extraction

**Symptoms:** `jq` reports "parse error", Claude returns invalid JSON.

**Solutions:**
✓ Copy JSON carefully (don't include markdown code fence markers)
✓ Validate with: `cat extraction.json | jq .` (will show specific error line)
✓ Use JSON linter in text editor
✓ Check for unescaped quotes in verbatim_quote fields

**Fix common issues:**
```bash
# Check for unescaped quotes
grep -n '": ".*".*",' extraction.json

# Validate JSON structure
jq empty extraction.json
# No output = valid JSON
# Error message = invalid JSON (shows line number)
```

---

### Issue: Pass prompts not loading

**Symptoms:** Claude doesn't follow extraction prompt, uses default behaviour.

**Solutions:**
✓ Verify you pasted COMPLETE prompt (check line count)
✓ Ensure no truncation (prompts are 400-1,200 lines)
✓ Copy from source file, not from terminal output
✓ Check file encoding (should be UTF-8)

**Verify prompt:**
```bash
# Check prompt line count
wc -l extraction-system/prompts/01-claims-evidence_pass1_prompt.md
# Should show ~800 lines

# Check first and last lines
head -5 extraction-system/prompts/01-claims-evidence_pass1_prompt.md
tail -5 extraction-system/prompts/01-claims-evidence_pass1_prompt.md
```

---

### Issue: Extraction takes too long

**Symptoms:** Single pass takes >30 minutes, full paper >6 hours.

**Solutions:**
✓ Extract shorter sections (5-10 pages per pass, not full paper)
✓ Use Pass 1-2 for Results only (skip Methods if RDMAP not needed)
✓ Infrastructure-only extraction (Pass 0 + Pass 6, skip 1-5)
✓ Check context window not overloaded (keep prompts + text < 50,000 tokens)

**Optimisation:**
- Methods section: ~15-20 min (Passes 3-5)
- Results section: ~10-15 min (Passes 1-2)
- Infrastructure: ~20-30 min (Pass 6)
- Full paper optimised: ~2-3 hours

---

## Next Steps

**After successful installation:**

1. **Read the quick start:** [quick-reference.md](quick-reference.md)
2. **Follow complete workflow:** [usage-guide.md](usage-guide.md)
3. **Understand architecture:** [architecture.md](architecture.md)
4. **Review worked examples:** `outputs/sobotkova-et-al-2023/extraction.json`
5. **Check workflow guidance:** `input/WORKFLOW.md`

**For your first extraction:**
- Start with Pass 0 (metadata)
- Then Pass 1-2 (Claims/Evidence from one section)
- Verify item counts match expected ranges
- Review [usage-guide.md](usage-guide.md) for detailed pass instructions

**Questions or issues?**
- Check [usage-guide.md](usage-guide.md) troubleshooting section
- Review skill reference materials in `.claude/skills/research-assessor/references/`
- Consult worked examples in `outputs/` directory

---

## Uninstallation

**To remove the skill:**
```bash
# Remove skill directory
rm -rf .claude/skills/research-assessor/

# Optionally remove extraction outputs
rm -rf outputs/

# Keep prompts and documentation
# (extraction-system/ and docs/ are part of project repository)
```

**To reinstall:**
- Follow Step 1 again to restore `.claude/skills/research-assessor/` from repository
- Extraction prompts and documentation are version controlled, no action needed

---

## Version Information

**Current Version:** 2.6
**Schema Version:** 2.6
**Compatible Prompts:** Pass 0-7 (v2.6)
**Last Updated:** 2025-11-13

**Breaking Changes from v2.5:**
- Added Pass 0 (metadata extraction)
- Split RDMAP into 3 passes (explicit, implicit, consolidation)
- Added Pass 6 (infrastructure assessment)
- Updated to 7-pass workflow (was 5-pass in v2.4)
- Infrastructure object added to schema

**Migration from v2.4/v2.5:**
- Existing extractions compatible with v2.6 schema
- Add infrastructure object for Pass 6 capability
- Update extraction_notes.current_pass to reflect 7-pass workflow
- See `archive/planning-completed/migration-log.md` for field name changes (v2.4 → v2.5)
