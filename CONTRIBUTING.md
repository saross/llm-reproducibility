# Contributing to LLM-Based Research Extraction and Assessment

**Version:** 2.6
**Last Updated:** 2025-11-13

Thank you for your interest in contributing to this project! This document explains how you can contribute to improving this open research tool for systematic extraction and assessment of research methodology, evidence, claims, and reproducibility infrastructure.

---

## Table of Contents

1. [Ways to Contribute](#ways-to-contribute)
2. [Getting Started](#getting-started)
3. [Contribution Workflow](#contribution-workflow)
4. [Testing and Quality Standards](#testing-and-quality-standards)
5. [Code of Conduct](#code-of-conduct)
6. [Licence](#licence)

---

## Ways to Contribute

### 1. Domain Adaptations

**Expand extraction to new fieldwork disciplines:**
- Ecology and environmental science
- Ethnography and qualitative fieldwork
- Field geology and earth sciences
- Marine and freshwater biology
- Geography and remote sensing
- Heritage conservation

**What's needed:**
- Domain-specific examples (3+ papers extracted)
- Adapted vocabulary and expected information patterns
- Test extractions with quality metrics
- Infrastructure norms documentation (PID adoption, FAIR compliance by discipline)

**See:** [docs/research-assessor-guide/CONTRIBUTING.md](docs/research-assessor-guide/CONTRIBUTING.md#domain-adaptations) for detailed guidelines

---

### 2. Worked Extraction Examples

**Provide complete extraction examples:**
- Full 7-pass extractions (Passes 0-6 + validation)
- Annotated edge case examples
- Domain-specific demonstrations
- Historical papers (pre-FAIR baselines)
- High-FAIR exemplars (14-15/15 scores)

**Value:** Examples improve extraction quality, demonstrate patterns, enable validation testing.

**See:** [examples/README.md](examples/README.md) for contribution guidelines and quality standards

---

### 3. FAIR Vocabulary Development

**Build controlled vocabularies empirically:**
- Research design types (evidence-based from 20+ paper corpus)
- Methods taxonomy (aggregated across disciplines)
- Protocol types (operational procedures)
- SKOS vocabularies with Zenodo DOIs

**Approach:** Bottom-up from real extractions, not top-down theory.

**See:** [planning/fair-vocabularies-development-plan.md](planning/fair-vocabularies-development-plan.md) for complete roadmap

---

### 4. Prompt and Skill Refinement

**Improve extraction quality based on:**
- Cross-paper error analysis
- Quality metrics (precision, recall, relationship mapping)
- User feedback and testing results
- Infrastructure assessment gaps

**Areas:**
- Clearer decision frameworks (evidence vs claims, method vs protocol)
- Enhanced consolidation guidance (Pass 2, Pass 5)
- Infrastructure decision trees (missing statements, ethics, CARE principles)
- Validation rules and quality checks

**See:** [docs/research-assessor-guide/CONTRIBUTING.md](docs/research-assessor-guide/CONTRIBUTING.md#prompt-refinement) for prompt improvement process

---

### 5. Infrastructure Assessment Enhancement

**Improve reproducibility assessment (Pass 6):**
- Additional PID systems (RRIDs, w3ids, RAiD, Software Heritage)
- FAIR principles domain-specific interpretations
- Software documentation assessment framework
- Licence taxonomy (SPDX identifiers)
- Regional ethics variation (ancient DNA, Indigenous data governance)
- Computational environment specification

**Needs:**
- Worked examples from diverse papers
- Edge cases (book chapters, GitHub-only sharing, pre-FAIR papers)
- Cross-disciplinary FAIR adoption comparisons

**See:** [planning/pass6-phase1-testing-findings.md](planning/pass6-phase1-testing-findings.md) for identified gaps

---

### 6. Testing and Validation

**Contribute test results:**
- Inter-rater reliability studies (compare extractions)
- Multi-run extraction studies (quantify variability)
- Quality benchmarking against hand-coded papers
- Cross-model comparison (Claude vs GPT vs Gemini)
- Infrastructure assessment validation (PID connectivity, FAIR scores)
- Historical trend analysis (reproducibility infrastructure 2005-2024)

**Priority needs:**
- 20+ paper corpus for vocabulary development
- Multi-discipline testing (archaeology, ecology, ethnography, geology)
- Scale testing (long papers 40+ pages, multi-proxy studies)

**See:** [planning/active-todo-list.md](planning/active-todo-list.md#testing--validation-queue) for testing priorities

---

### 7. Documentation Improvements

**Help others use the tool:**
- Tutorials and walkthroughs
- Troubleshooting guides
- Domain-specific quick starts
- Video demonstrations
- Use case descriptions
- Infrastructure assessment examples

**See:** [docs/documentation-index.md](docs/documentation-index.md) for documentation map and gaps

---

### 8. Assessment Framework Development (Phase 2)

**Build transparency and credibility scoring:**
- Rubrics using extraction patterns
- Automated scoring algorithms
- Benchmark datasets
- Validation studies
- RepliCATS adaptation for HASS disciplines

**Status:** Deferred to Phase 2 (post-extraction system completion)

**See:** [planning/cwts_implementation_plan.md](planning/cwts_implementation_plan.md) for assessment roadmap

---

### 9. Bug Reports and Feature Requests

**Report issues or suggest features:**
- Extraction errors (boundary confusion, tier misassignment)
- Documentation gaps or unclear instructions
- Usability problems
- Schema improvements
- Infrastructure guidance gaps

**Where to report:** [GitHub Issues](https://github.com/shawngraham/llm-reproducibility/issues)

**When reporting bugs, include:**
- What you were trying to do
- What happened (actual behaviour)
- What you expected to happen
- Steps to reproduce
- Paper being extracted (if applicable)
- Schema version and Claude Code version

---

## Getting Started

### Prerequisites

**To contribute, you should have:**
- Access to Claude Code 2.0.36+ with Skills support
- Claude Sonnet 4.5 or later
- Research Assessor skill v2.6 installed (`.claude/skills/research-assessor/`)
- Familiarity with research methodology
- (Optional) Domain expertise in fieldwork-based research

**Helpful but not required:**
- Experience with JSON and YAML
- Understanding of FAIR principles and PID systems
- Background in research transparency initiatives (RepliCATS, FAIR4RS)
- Python 3.8+ for PDF extraction and validation scripts

---

### Set Up for Contributing

1. **Fork and clone the repository:**
   ```bash
   git clone https://github.com/shawngraham/llm-reproducibility.git
   cd llm-reproducibility
   ```

2. **Install the Research Assessor skill:**
   ```bash
   # Skill already present in .claude/skills/research-assessor/
   # Verify installation
   ls -la .claude/skills/research-assessor/
   ```

3. **Install Python dependencies (for PDF extraction):**
   ```bash
   pip install -r requirements.txt
   ```

4. **Test on example paper:**
   ```bash
   # Follow docs/user-guide/getting-started.md
   # Complete first extraction to understand workflow
   ```

---

## Contribution Workflow

### 1. Propose Your Contribution

**For major contributions (new features, domain adaptations):**
- Open a GitHub Issue describing the contribution
- Discuss approach and scope with maintainers
- Get feedback before starting significant work

**For minor contributions (documentation fixes, small improvements):**
- Can proceed directly to pull request

---

### 2. Make Your Changes

**Branch naming:**
- Feature: `feature/vocabulary-development`
- Bug fix: `fix/relationship-validation`
- Documentation: `docs/troubleshooting-guide`
- Domain: `domain/ecology-adaptation`

**Commit messages:**
Use conventional commits format:
```text
type(scope): subject

body

Co-Authored-By: Claude <noreply@anthropic.com>
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

**Examples:**
```text
feat(vocab): add SKOS research designs vocabulary

Created fieldwork research designs vocabulary v1.0 with 50 concepts
aggregated from 20-paper corpus. Published to Zenodo with DOI.

Co-Authored-By: Claude <noreply@anthropic.com>
```

```text
docs(guide): add troubleshooting section for validation errors

Added common validation errors and solutions to user guide based on
testing feedback from 10-paper corpus.

Co-Authored-By: Claude <noreply@anthropic.com>
```

---

### 3. Test Your Changes

**For extraction examples:**
- Complete all 7 passes (0-6 + validation)
- Run validation script: `python extraction-system/scripts/validate_extraction.py`
- Verify quality metrics (relationship coverage >75%)
- Create NOTES.md documenting edge cases

**For prompt changes:**
- Test on 2-3 diverse papers
- Compare before/after quality metrics
- Document improvements in pull request

**For infrastructure enhancements:**
- Test on papers with diverse FAIR scores (0/15, 5/15, 15/15)
- Verify guidance clarity on edge cases
- Compare assessments to published evaluations (if available)

**For documentation:**
- Verify all links work
- Check formatting (markdownlint)
- Test instructions with fresh eyes (ask someone unfamiliar to follow)

---

### 4. Submit Pull Request

**Pull request template:**

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Domain adaptation
- [ ] Extraction example
- [ ] Vocabulary development
- [ ] Prompt improvement
- [ ] Infrastructure enhancement
- [ ] Documentation
- [ ] Bug fix
- [ ] Other (specify)

## Testing
How was this tested?

## Quality Metrics (if extraction)
- Extraction completeness: X/7 passes
- Relationship coverage: X%
- Validation: Pass/Fail
- FAIR score (if infrastructure): X/15

## Checklist
- [ ] Follows contribution guidelines
- [ ] Code follows UK spelling conventions
- [ ] Documentation updated (if applicable)
- [ ] Tests pass (if applicable)
- [ ] Commits follow conventional format
```

---

### 5. Code Review

Maintainers will review your contribution and may:
- Request changes or clarifications
- Suggest improvements
- Approve and merge

**Review criteria:**
- Quality and completeness
- Consistency with existing patterns
- Documentation clarity
- Test coverage
- Adherence to standards (UK spelling, FAIR principles)

---

## Testing and Quality Standards

### Extraction Quality Standards

**Completeness:**
- All 7 passes complete (0-6 + validation)
- Infrastructure assessment included (Pass 6)
- Validation passing without errors

**Accuracy:**
- Verbatim quotes verified against source
- Location metadata accurate (section, page, paragraph)
- Object classifications correct (evidence vs claim, method vs protocol)
- Tier assignments justified (strategic/tactical/operational)

**Relationship Quality:**
- Bidirectional mapping >75% complete
- No orphaned cross-references
- Relationship types semantically correct

**Documentation:**
- NOTES.md with extraction annotations (for examples)
- Edge cases documented with rationale
- Quality metrics calculated

---

### Documentation Standards

**Formatting:**
- UK/Australian spelling throughout
- Markdown linting passes (MD022, MD031, MD032, MD040)
- Maximum line length: 100 characters
- Oxford comma in lists

**Content:**
- Acronyms expanded on first usage per file
- Examples included for complex concepts
- Links verified and working
- Code blocks have language specifiers

**Accessibility:**
- Clear headings and structure
- Context provided for all references
- Written for intelligent non-specialists

---

### Code Standards

**Python scripts:**
- PEP 8 compliance
- Type hints for function parameters
- Docstrings for all functions
- Verbose comments explaining logic
- Header block with purpose, usage, inputs, outputs

**JSON/YAML:**
- Valid syntax (validate before committing)
- Consistent indentation (2 spaces)
- Comments where helpful (YAML only)

---

## Code of Conduct

### Our Pledge

We are committed to providing a welcoming and inclusive environment for all contributors, regardless of experience level, background, or identity.

### Expected Behaviour

- Be respectful and constructive in all interactions
- Provide helpful, specific feedback
- Acknowledge contributions and credit appropriately
- Focus on what is best for the community and project

### Unacceptable Behaviour

- Harassment, discrimination, or exclusionary language
- Personal attacks or insults
- Trolling or inflammatory comments
- Publishing others' private information
- Other unprofessional conduct

### Reporting

Report unacceptable behaviour to project maintainers via:
- GitHub Issues (for public concerns)
- Email (for private concerns - see repository)

### Enforcement

Maintainers may:
- Issue warnings
- Temporarily ban from contributions
- Permanently ban from project

---

## Licence

### Dual Licensing Structure

This project uses dual licensing:

**Code and Scripts:**
- Licence: [Apache-2.0](LICENSE-CODE)
- Applies to: Python scripts, validation tools, automation code

**Documentation and Data:**
- Licence: [CC-BY-4.0 International](LICENSE-DOCS)
- Applies to: Guides, prompts, examples, schema, extraction outputs

### Contributor Agreement

By contributing, you agree:
- Your contributions will be licensed under the same licence as the component you're modifying (Apache-2.0 for code, CC-BY-4.0 for documentation)
- You have the right to contribute the content
- You understand contributions may be modified or redistributed

### Attribution

Contributors will be acknowledged:
- In commit history (Co-Authored-By tags)
- In CITATION.cff (for significant contributions)
- In documentation (where appropriate)

---

## Questions?

**For contribution questions:**
- Open a GitHub Issue with label `question`
- See [docs/user-guide/getting-started.md](docs/user-guide/getting-started.md)
- Check [docs/documentation-index.md](docs/documentation-index.md) for relevant guides

**For technical support:**
- See [docs/research-assessor-guide/README.md](docs/research-assessor-guide/README.md)
- Check [examples/](examples/) for worked examples

**For skill-specific contributions:**
- See [docs/research-assessor-guide/CONTRIBUTING.md](docs/research-assessor-guide/CONTRIBUTING.md) for detailed skill contribution guidelines

---

## Acknowledgements

We appreciate all contributions, whether:
- Testing and feedback
- Documentation improvements
- Code contributions
- Examples and use cases
- Bug reports
- Feature suggestions

Every contribution helps improve research transparency and reproducibility!

---

**Thank you for contributing to open research tools!**

**Navigation:** [Main README](README.md) | [Documentation Index](docs/documentation-index.md) | [Research Assessor Guide](docs/research-assessor-guide/)
