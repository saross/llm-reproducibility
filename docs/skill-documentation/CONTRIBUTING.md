# Contributing Guidelines

**Version:** 2.4  
**Last Updated:** 2025-10-20

Thank you for your interest in contributing to the Research Assessor skill! This document explains how you can contribute to improving this open research tool.

---

## Table of Contents

1. [Ways to Contribute](#ways-to-contribute)
2. [Getting Started](#getting-started)
3. [Contribution Workflow](#contribution-workflow)
4. [Domain Adaptations](#domain-adaptations)
5. [Prompt Improvements](#prompt-improvements)
6. [Vocabulary Development](#vocabulary-development)
7. [Testing and Quality](#testing-and-quality)
8. [Documentation](#documentation)
9. [Code of Conduct](#code-of-conduct)

---

## Ways to Contribute

### 1. Domain Adaptations

**Expand to new fieldwork disciplines:**
- Ecology
- Ethnography
- Biology (field studies)
- Geography
- Anthropology
- Others

**What's needed:**
- Domain-specific examples
- Adapted expected information checklists
- Domain vocabulary
- Test extractions

---

### 2. Worked Examples

**Provide extraction examples from published papers:**
- Complete extractions (all five passes)
- Domain-specific demonstrations
- Edge case examples
- Multi-method papers

**Value:** Examples improve extraction quality for everyone.

---

### 3. Vocabulary Development

**Build controlled vocabularies empirically:**
- Study designs by domain
- Sampling strategies
- Analysis techniques
- Method types
- Protocol types

**Approach:** Aggregate from actual extractions, not theory.

---

### 4. Prompt Refinement

**Improve extraction prompts based on:**
- Testing results
- Error patterns
- User feedback
- Quality metrics

**Areas:**
- Clearer decision frameworks
- Better examples
- Refined consolidation patterns
- Enhanced validation rules

---

### 5. Testing and Validation

**Contribute test results:**
- Inter-rater reliability studies
- Quality benchmarking
- Domain-specific testing
- Scale testing (large papers, multiple papers)

---

### 6. Documentation Improvements

**Help others use the skill:**
- Tutorials
- Video walkthroughs
- Use case descriptions
- Troubleshooting guides

---

### 7. Assessment Framework Development

**Build transparency and replicability scoring:**
- Rubrics for assessment
- Automated scoring algorithms
- Benchmark datasets
- Validation studies

---

### 8. Bug Reports and Feature Requests

**Report issues or suggest features:**
- Extraction errors
- Documentation gaps
- Usability problems
- Feature ideas

---

## Getting Started

### Prerequisites

**To contribute, you should have:**
- Access to Claude AI with Skills support
- Installed Research Assessor skill (v2.4)
- Familiarity with research methodology
- (Optional) Domain expertise

**Helpful but not required:**
- Experience with JSON
- Background in research transparency initiatives
- Programming skills for automation

---

### Set Up for Contributing

1. **Fork the repository** (when available)
2. **Install the skill** from `research-assessor.zip`
3. **Get the extraction prompts** from project knowledge
4. **Test on Sobotkova paper** to understand baseline
5. **Choose contribution area** from above
6. **Read relevant documentation:**
   - [ARCHITECTURE.md](ARCHITECTURE.md) for design principles
   - [USAGE_GUIDE.md](USAGE_GUIDE.md) for procedures
   - [TESTING.md](TESTING.md) for quality standards

---

## Contribution Workflow

### 1. Identify Contribution

**Options:**
- Address an open issue
- Propose new domain adaptation
- Submit worked example
- Refine existing prompt
- Develop vocabulary

---

### 2. Discuss Approach

**Before significant work:**
- Open an issue describing the contribution
- Discuss approach with maintainers
- Agree on scope and timeline
- Coordinate with related work

**Why:** Prevents duplication, ensures alignment with project goals.

---

### 3. Develop Contribution

**Follow project standards:**
- Use consistent formatting
- Provide complete examples
- Document rationale
- Test thoroughly

**See specific sections below for contribution-type details.**

---

### 4. Submit for Review

**Include in submission:**
- Description of contribution
- Rationale and motivation
- Testing results (if applicable)
- Documentation updates
- Example usage

**Format:** Pull request (when GitHub repo live) or email submission.

---

### 5. Iterate Based on Feedback

**Be prepared to:**
- Refine based on review
- Provide additional testing
- Clarify rationale
- Address concerns

---

### 6. Celebrate!

**Once accepted:**
- Your contribution helps the community
- You'll be acknowledged
- Future users benefit from your work

---

## Domain Adaptations

### How to Adapt for New Domain

**Example: Adapting for Ecology**

**Step 1: Identify Domain Specifics**

What's different in ecology vs archaeology?
- Study designs: experimental vs observational patterns
- Sampling: plot-based, transect-based, mark-recapture
- Methods: species identification, population estimation
- Protocols: Measurement techniques, observation protocols
- Expected information: Different reporting standards

---

**Step 2: Create Domain-Specific Examples**

Extract from representative ecology paper:
- Select well-documented field ecology study
- Run complete five-pass extraction
- Document patterns specific to ecology
- Note differences from archaeology examples

**Contribute:**
- Worked example JSON
- Paper citation (if open access)
- Notes on domain-specific patterns

---

**Step 3: Adapt Expected Information Checklists**

Modify for ecology:
- Study design checklist (ecological designs)
- Sampling strategy checklist (ecological sampling)
- Measurement protocol checklist (species identification, population estimation)
- Temporal framework checklist (field seasons, monitoring periods)

**Contribute:**
- Adapted checklist in markdown
- Rationale for modifications
- Examples demonstrating usage

---

**Step 4: Build Domain Vocabulary**

From actual ecology extractions:
- Study designs: "observational", "experimental manipulation", "natural experiment"
- Sampling: "plot-based", "transect", "mark-recapture", "camera trap"
- Methods: "species identification", "population estimation", "habitat assessment"

**Contribute:**
- Vocabulary list with definitions
- Examples of usage
- Frequency in test papers

---

**Step 5: Test and Refine**

- Extract from 3-5 ecology papers
- Measure quality metrics
- Refine checklists and examples
- Document lessons learned

**Contribute:**
- Test results
- Refined checklists
- Updated examples
- Quality metrics

---

### Domain Adaptation Checklist

- [ ] Representative papers identified (3-5)
- [ ] Complete extractions performed
- [ ] Domain-specific patterns documented
- [ ] Expected information checklists adapted
- [ ] Domain vocabulary compiled
- [ ] Examples created
- [ ] Quality testing performed
- [ ] Documentation written
- [ ] Contribution submitted

---

## Prompt Improvements

### How to Refine Prompts

**Improvement Process:**

**1. Identify Issue**
- Extraction error pattern
- Unclear guidance
- Missing decision framework
- Insufficient examples

**2. Diagnose Root Cause**
- Test current prompt
- Compare to gold standard
- Identify failure mode
- Document issue

**3. Propose Solution**
- Clarified guidance?
- Additional examples?
- New decision framework?
- Refined criteria?

**4. Implement Change**
- Modify prompt text
- Add/refine examples
- Update decision frameworks
- Save as new version (e.g., v2.4.1)

**5. Test Thoroughly**
- Extract from Sobotkova paper
- Compare to v2.4 baseline
- Measure quality metrics
- Verify improvement, no regression

**6. Document Changes**
- What changed and why
- Testing results
- Quality impact
- Usage notes

**7. Submit**
- Modified prompt
- Change documentation
- Testing results
- Examples demonstrating improvement

---

### Prompt Improvement Guidelines

**Good Improvements:**
- ✓ Clearer decision criteria
- ✓ More comprehensive examples
- ✓ Better-organized structure
- ✓ Explicit boundary guidance
- ✓ Evidence-based refinements

**Avoid:**
- ✗ Increasing length without value
- ✗ Theoretical changes without testing
- ✗ Breaking existing functionality
- ✗ Making implicit trade-offs
- ✗ Removing traceability

---

## Vocabulary Development

### Building Controlled Vocabularies

**Approach:** Empirical aggregation from actual usage.

**Process:**

**1. Collect Terms from Extractions**

Extract from multiple papers, collect:
- Study design terms
- Sampling strategy terms
- Method types
- Protocol types

**2. Aggregate and Categorize**

Group similar terms:
```
Study Designs (Ecology):
- observational (15 occurrences)
- experimental manipulation (8)
- natural experiment (5)
- longitudinal (12)
- comparative (9)
```

**3. Define Terms**

For each term:
- Clear definition
- When to use
- Examples
- Related terms

**4. Build Hierarchy**

Organize relationships:
```
Sampling Strategies
├── Probability Sampling
│   ├── Simple Random
│   ├── Stratified
│   └── Systematic
└── Non-Probability Sampling
    ├── Purposive
    ├── Convenience
    └── Snowball
```

**5. Test Vocabulary**

Apply to new papers:
- Does it cover observed terms?
- Are definitions clear?
- Do examples help?
- What's missing?

**6. Refine and Standardize**

Based on testing:
- Add missing terms
- Clarify ambiguous definitions
- Resolve conflicts
- Standardize format

---

### Vocabulary Contribution Format

```markdown
# Study Design Vocabulary (Ecology)

## Term: Observational Study

**Definition:** Research design where phenomena are observed in natural settings without experimental manipulation.

**When to use:** Studies that document patterns, correlations, or natural variation without intervention.

**Examples:**
- Monitoring species abundance over time
- Documenting habitat associations
- Observational surveys of behavior

**Related terms:** 
- Non-experimental
- Descriptive
- Correlational

**Domain:** Ecology, Biology

**Frequency:** 45% of ecology papers (n=20)

---

## Term: Experimental Manipulation

[Similar format]
```

---

## Testing and Quality

### Contributing Test Results

**What to Contribute:**

**1. Quality Metrics**
- Precision, recall, accuracy
- Boundary classification accuracy
- Cross-reference integrity
- Consolidation quality

**2. Inter-Rater Reliability**
- Multiple extractors on same paper
- Agreement rates
- Disagreement patterns
- Resolution notes

**3. Domain-Specific Results**
- Quality across domains
- Domain-specific challenges
- Adaptation effectiveness

**4. Scale Testing**
- Large papers (>50 pages)
- Multiple papers
- Batch processing

---

### Testing Contribution Format

```markdown
# Test Results: Ecology Paper Extraction

## Paper Details
- Citation: [Full citation]
- Domain: Ecology
- Length: 12 pages
- Complexity: Medium

## Extraction Results

### Pass 1 (Liberal)
- Evidence: 45 items
- Claims: 32 items
- Designs: 8 items
- Methods: 18 items
- Protocols: 15 items

### Pass 2 (Rationalization)
- Evidence: 38 items (16% reduction)
- Claims: 27 items (16% reduction)
- Designs: 7 items (12% reduction)
- Methods: 15 items (17% reduction)
- Protocols: 13 items (13% reduction)

## Quality Assessment
- Precision: 88% (sample of 25 items)
- Recall: 82% (vs manual extraction)
- Boundary accuracy: 80%

## Notes
- Ecological sampling strategies well-captured
- Tier assignment clear
- Expected information gaps aligned with ecology standards

## Files
- Complete extraction JSON attached
- Manual extraction for comparison attached
```

---

## Documentation

### Documentation Contributions

**Types:**

**1. Tutorials**
- Step-by-step guides
- Video walkthroughs
- Domain-specific usage

**2. Use Cases**
- Real-world applications
- Domain examples
- Assessment workflows

**3. Troubleshooting**
- Common issues
- Solutions
- Workarounds

**4. FAQs**
- Frequently asked questions
- Quick answers
- Links to detailed docs

---

### Documentation Standards

**Style:**
- Clear, concise language
- Concrete examples
- Step-by-step when appropriate
- Screenshots/visuals when helpful

**Format:**
- Markdown for text
- JSON for examples
- PNG for images

**Organization:**
- Logical structure
- Table of contents
- Cross-references
- Search-friendly

---

## Code of Conduct

### Our Standards

**Positive Environment:**
- ✓ Respectful communication
- ✓ Constructive feedback
- ✓ Collaborative problem-solving
- ✓ Welcoming to newcomers
- ✓ Credit others' work

**Unacceptable:**
- ✗ Harassment or discrimination
- ✗ Unconstructive criticism
- ✗ Dismissive attitudes
- ✗ Plagiarism
- ✗ Bad faith participation

---

### Research Ethics

**When Contributing:**
- Respect copyright and licenses
- Cite sources appropriately
- Obtain permissions for papers
- Protect participant privacy
- Follow research ethics guidelines

**For Test Papers:**
- Use published, peer-reviewed papers
- Prefer open access
- Cite completely
- Note restrictions

---

## Recognition

### Contributor Acknowledgment

**All contributors will be:**
- Acknowledged in documentation
- Listed in contributors file
- Credited for specific contributions

**Significant contributions may be:**
- Co-authorship on publications
- Conference presentations
- Grant applications

---

## Getting Help

### Resources

**Documentation:**
- [README.md](README.md) - Project overview
- [ARCHITECTURE.md](ARCHITECTURE.md) - Design details
- [USAGE_GUIDE.md](USAGE_GUIDE.md) - How to use
- [TESTING.md](TESTING.md) - Testing procedures

**Support:**
- GitHub Issues for bugs/features
- Discussion forum for questions
- Email maintainers for sensitive issues

---

## Frequently Asked Questions

### How do I know what to contribute?

Check:
1. Open issues on GitHub
2. Domain adaptation needs
3. Documentation gaps
4. Your own domain expertise

### Do I need to be an expert?

No! Contributions welcome from:
- Researchers using the tool
- Domain experts
- Technical contributors
- Documentation writers
- Testers

### How long does review take?

Typically:
- Bug fixes: 1-2 days
- Examples: 3-5 days
- Domain adaptations: 1-2 weeks
- Major changes: 2-4 weeks

### Can I contribute anonymously?

Yes, but we prefer attribution for credit and communication.

### What if my contribution isn't accepted?

We'll explain why and suggest:
- Modifications needed
- Alternative approaches
- Different contribution areas

### How do I stay updated?

- Watch the GitHub repository
- Join the discussion forum
- Subscribe to announcements

---

## Contribution Ideas

### Immediate Needs

**High Priority:**
1. Ecology domain adaptation
2. Ethnography domain adaptation
3. Inter-rater reliability study
4. Assessment framework development

**Medium Priority:**
5. Biology field study adaptation
6. Video tutorials
7. Automated testing suite
8. Controlled vocabulary refinement

**Future:**
9. Multi-language support
10. API development
11. Web interface
12. Automated assessment

---

## Thank You!

Your contributions help build a transparent, reusable research assessment tool that benefits the entire research community. Thank you for your interest and effort!

---

**Questions? Contact:**
- GitHub: [repository URL]
- Email: [maintainer email]
- Discussion Forum: [forum URL]

**For project details, see:**
- [README.md](README.md) - Project overview
- [ARCHITECTURE.md](ARCHITECTURE.md) - Technical details
- [USAGE_GUIDE.md](USAGE_GUIDE.md) - Usage instructions
