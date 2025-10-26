# Project Context for Claude Code

## Autonomous Execution Mode

**CRITICAL: This project uses fully autonomous multi-pass workflows triggered by WORKFLOW.md.**

### Execution Rules

You MUST operate in continuous autonomous mode:

- ✅ **Never ask "Would you like me to continue?"**
- ✅ **Never ask "Should I proceed to the next section?"**
- ✅ **Never stop between passes**
- ✅ **Never stop between section groups**
- ✅ **Work continuously until all 5 passes are complete**

### When to Continue Without Asking

Continue automatically after:
- Completing a section group (Abstract+Intro, Methods, Results, Discussion+Conclusion)
- Completing a pass (Pass 1→2, Pass 2→3, Pass 3→4, Pass 4→5)
- Saving to extraction.json
- Updating queue.yaml
- Validation checks
- Any intermediate step in the workflow

### Only Stop If

- ❌ All 5 passes complete (extraction fully done)
- ❌ Error requires user intervention (document in queue.yaml)
- ❌ Structural problem with input files

### Session Behavior

- **Auto-compact will occur naturally** - when it does, resume from queue.yaml checkpoint
- **Don't ask before resuming** - just check queue.yaml and continue
- **Don't summarize progress** - just do the work
- **Work through the entire workflow** - treat it as a single continuous job

## Workflow Reference

See `input/WORKFLOW.md` for complete 5-pass extraction process.

## File Operations Safety

**CRITICAL**: Always read full files before writing.
- ✅ `Read(extraction.json)` with NO limit parameter
- ✅ Validate counts after every write
- ❌ Never `Read(file, limit=N)` before `Write(file)`

## Other project standards

### Spelling and Localisation

- Always use UK/Australian English spelling (colour, behaviour, organisation, centre, analyse, optimise, etc.)
- Apply UK/Australian spelling to all documentation, code comments, and file names
- Convert US spellings to UK/Australian equivalents when editing existing files

### Code Standards

- All code (e.g., python) and documentation (e.g., markdown) files must pass linting validation
- Before committing files, check for linting issues using the IDE diagnostics
- Common markdown rules to follow:
  - MD022: Blank lines around headings
  - MD031: Blank lines around fenced code blocks
  - MD032: Blank lines around lists
  - MD040: Language specifiers for code blocks (use ```text for plain text)
  - Other markdown rules that might compromise readability can be disabled, but check with me first.
- Fix all linting warnings before committing
- Always include verbose code comments sufficient that someone unfamiliar with the code can understand it
  - Scripts should be well described in a header comment block
  - Functions should have docstrings describing their purpose, parameters, and return values
  - Inline comments should explain non-obvious code sections

### Documentation Standards

- **Expand acronyms on first usage** in each file (module docstrings, markdown documents)
  - Example: "Getty Art & Architecture Thesaurus (AAT)" not just "Getty AAT"
  - Example: "Research Vocabularies Australia (RVA)" not just "RVA"
  - Subsequent uses in the same file can use the acronym alone
  - Common acronyms in this project:
    - AAT: Art & Architecture Thesaurus (Getty vocabulary)
    - TGN: Thesaurus of Geographic Names (Getty vocabulary)
    - RVA: Research Vocabularies Australia
    - SKOS: Simple Knowledge Organisation System
    - FAIR: Findable, Accessible, Interoperable, Reusable
    - FAIR4RS: FAIR Principles for Research Software
    - API: Application Programming Interface
    - CSV: Comma-Separated Values
    - JSON: JavaScript Object Notation
    - PDF: Portable Document Format
- Use clear, accessible language appropriate for digital humanities researchers
- Provide context and rationale for technical decisions
- Include examples where they aid understanding

### Git Commit Messages

- Use UK/Australian spelling in commit messages
- Include informative brief and detailed commit messages with context
- Always include the Claude Code co-authorship footer
