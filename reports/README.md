# Reports

Key testing and quality assurance reports for the extraction system.

**Note:** Development reports (task summaries, correction reports, phase completions) are archived in [archive/extraction-development/](../archive/extraction-development/) organized by version.

---

## Active Reports

### Extraction Testing

Testing reports for v2.5 extraction system validation:

#### [extraction-testing/extraction-comparison.md](extraction-testing/extraction-comparison.md)
Comparison of extraction quality between different approaches:
- Before-skill vs. with-skill results
- Pass 1 vs. Pass 2 refinement
- Quality metrics and improvements

#### [extraction-testing/skill-validation-summary.md](extraction-testing/skill-validation-summary.md)
Summary of skill validation testing:
- Test methodology
- Quality benchmarks achieved
- Known limitations
- Recommendations

#### [extraction-testing/skill-validation-report.md](extraction-testing/skill-validation-report.md)
Detailed validation report including:
- Test cases and results
- Precision/recall metrics
- Boundary accuracy testing
- Cross-reference integrity verification

---

### Quality Assurance

Comprehensive QA performed on the extraction system:

#### [quality-assurance/QA_EXECUTIVE_SUMMARY.md](quality-assurance/QA_EXECUTIVE_SUMMARY.md)
High-level QA summary for stakeholders:
- Overall quality assessment
- Critical issues identified and resolved
- System readiness
- Recommendations for use

#### [quality-assurance/QA_REPORT_COMPREHENSIVE.md](quality-assurance/QA_REPORT_COMPREHENSIVE.md)
Complete QA report including:
- Testing methodology
- Detailed findings by component
- Issue severity classifications
- Remediation tracking

#### [quality-assurance/QA_REMEDIATION_PLAN.md](quality-assurance/QA_REMEDIATION_PLAN.md)
Plan for addressing QA findings:
- Issue prioritization
- Remediation steps
- Timeline and responsibility
- Verification procedures

#### [quality-assurance/SESSION_HANDOFF.md](quality-assurance/SESSION_HANDOFF.md)
QA session handoff documentation:
- Session context
- Work completed
- Outstanding issues
- Next steps

---

## Archived Reports

Development and iteration reports are archived by version:

### v2.5 Development Reports
Located in [archive/extraction-development/v2.5/reports/](../archive/extraction-development/v2.5/reports/):

- Phase completion summaries
- Task-specific reports (TASK_1.4, TASK_1.5, TASK_1.7, etc.)
- Correction summaries (schema, prompts)
- Investigation and error analysis reports
- Packaging completion report

### Earlier Version Reports
- **v2.4**: [archive/extraction-development/v2.4/reports/](../archive/extraction-development/v2.4/reports/)
  - RDMAP pass summaries
  - Correction reports
- **v2.2-v2.3**: [archive/extraction-development/v2.2-v2.3/reports/](../archive/extraction-development/v2.2-v2.3/reports/)
  - Claims/evidence development reports

See [archive/README.md](../archive/README.md) for complete development history.

---

## Report Categories

### Testing Reports
**Purpose:** Validate extraction quality and system performance
**Audience:** Users, developers, researchers
**Content:**
- Test methodology and datasets
- Quantitative metrics (precision, recall, accuracy)
- Qualitative assessment
- Comparison to baselines

### QA Reports
**Purpose:** Ensure system readiness for production use
**Audience:** Project stakeholders, users
**Content:**
- Comprehensive quality assessment
- Issue identification and severity
- Remediation plans
- Readiness recommendations

### Development Reports (Archived)
**Purpose:** Document development iterations and decisions
**Audience:** Developers, contributors, project historians
**Content:**
- Task completion summaries
- Correction and refinement reports
- Investigation findings
- Phase milestone documentation

---

## Using These Reports

### For Users
**"Is the system ready to use?"**
→ See [quality-assurance/QA_EXECUTIVE_SUMMARY.md](quality-assurance/QA_EXECUTIVE_SUMMARY.md)

**"How well does extraction work?"**
→ See [extraction-testing/skill-validation-summary.md](extraction-testing/skill-validation-summary.md)

**"What are known limitations?"**
→ Check both testing and QA reports for caveats

### For Developers
**"What testing has been done?"**
→ See all extraction-testing/ reports

**"What issues were found and fixed?"**
→ See quality-assurance/ reports + archived development reports

**"How did the system evolve?"**
→ See [archive/extraction-development/](../archive/extraction-development/) organized by version

### For Researchers
**"How do I assess extraction quality for my paper?"**
→ Use metrics from testing reports as benchmarks

**"What validation procedures should I follow?"**
→ See QA reports for recommended procedures

---

## Quality Metrics Summary

### Current System (v2.5)

**Extraction Quality:**
- Precision: ~85% (objects correctly classified)
- Recall: ~80% (completeness vs. hand-coding)
- Boundary Accuracy: ~75% (evidence/claim distinctions)
- Cross-reference Integrity: 100% (bidirectional consistency)

**System Performance:**
- Pass 1 → Pass 2 reduction: 15-20% (as expected)
- Validation pass rate: 100% (zero CRITICAL issues)
- Average extraction time: 4-5 hours for full paper (5 passes)

**Known Limitations:**
- Optimized for fieldwork-based research (archaeology, ecology, ethnography)
- Best results with Claude Sonnet 4.5+
- Large papers (>50 pages) may need sectioning
- Domain-specific vocabularies still evolving

See testing reports for detailed methodology.

---

## Contributing Reports

Have you tested the system on your papers? Consider contributing:

- **Testing results**: Run extractions, compare to hand-coding, share metrics
- **Domain adaptation**: Test on new fields, document adaptations needed
- **Use cases**: Document real-world applications and lessons learned
- **Benchmarks**: Create gold-standard extractions for validation

See [docs/skill-documentation/CONTRIBUTING.md](../docs/skill-documentation/CONTRIBUTING.md) for guidelines.

---

## Related Documentation

- [Examples](../examples/) - See complete extractions
- [User Guide](../docs/user-guide/) - Learn extraction workflow
- [Skill Documentation](../docs/skill-documentation/) - Technical details
- [Archive](../archive/) - Development history and reports

---

**Questions about testing or quality?** Start with the QA Executive Summary for a high-level overview.
