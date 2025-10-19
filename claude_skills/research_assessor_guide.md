# Research Assessor Skill - Installation & Usage Guide

## What You Have

The **Research Assessor** skill is now packaged and ready to install. This skill enables systematic extraction and assessment of research methodology, claims, and evidence from fieldwork-based research papers.

## Skill Structure

```
research-assessor/
├── SKILL.md                           # Core skill guide (~500 lines)
├── references/
│   ├── README.md                      # Reference documentation overview
│   ├── workflow/
│   │   └── README.md                  # Workflow prompts guide
│   ├── schema/
│   │   └── schema-guide.md            # Complete schema documentation
│   ├── checklists/
│   │   ├── tier-assignment-guide.md   # Design/Method/Protocol decisions
│   │   ├── consolidation-patterns.md  # When to lump vs split
│   │   └── expected-information.md    # Completeness checklists
│   └── examples/
│       └── sobotkova-example.md       # Worked extraction example
```

## Installation

### Option 1: Install via Claude.ai (Recommended for Testing)

1. Download the `research-assessor.zip` file
2. Go to Claude.ai → Settings → Features → Skills
3. Click "Upload Skill"
4. Select the research-assessor.zip file
5. The skill will be available in all your Claude.ai conversations

### Option 2: Install via API (For Production)

```bash
# Upload the skill to your workspace
curl -X POST https://api.anthropic.com/v1/skills \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "anthropic-beta: skills-2025-10-02,files-api-2025-04-14" \
  -F "file=@research-assessor.zip"
```

### Option 3: Install in Claude Code

```bash
# For personal skills
unzip research-assessor.zip -d ~/.claude/skills/

# For project-specific skills
unzip research-assessor.zip -d .claude/skills/
```

## Using the Skill

### Basic Usage

Once installed, simply reference the skill in your prompts:

```
"Using the research-assessor skill, extract RDMAP Pass 1 from this paper."

"Extract claims and evidence Pass 1 from this section using the research-assessor skill."

"Validate this extraction using the research-assessor skill."
```

Claude will:
1. Automatically detect the skill is relevant
2. Load the appropriate workflow guidance
3. Extract following the structured methodology
4. Return properly formatted JSON

### Complete Workflow Example

```
1. Start with blank JSON template
2. "Extract claims Pass 1 from Methods section" → Liberal extraction
3. "Rationalize the claims Pass 2" → Consolidation
4. "Extract RDMAP Pass 1 from Methods section" → Liberal RDMAP extraction
5. "Rationalize RDMAP Pass 2" → Consolidation
6. "Validate the complete extraction Pass 3" → Integrity checks
```

### Testing on Sobotkova Paper

The skill was developed and tested on:
**Sobotkova et al. (2023)** "Arbitrary Offline Data Capture on All of Your Androids: The FAIMS Mobile Platform"

You can test with the same paper to compare results.

## What's Included vs What's in Project Knowledge

### ✅ Included in Skill (Fully Functional)

- Complete core guidance (SKILL.md)
- Comprehensive schema documentation
- Essential decision frameworks:
  - Tier assignment guide (Design/Method/Protocol)
  - Consolidation patterns (when to lump vs split)
  - Expected information checklists
- Worked example from real extraction
- Navigation and usage instructions

**The skill is fully functional as packaged.**

### 📚 Available in Project Knowledge (Optional Enhancement)

The COMPLETE extraction prompts (~4000+ lines total) with extensive examples are in project knowledge:

1. `Claims/Evidence Pass 1 v2.4 (Updated for Iterative Workflow).md` (~800 lines)
2. `Claims/Evidence Pass 2 v2.4 (Updated for Iterative Workflow).md` (~900 lines)
3. `Pass 1: RDMAP Liberal Extraction Prompt v2.4.md` (~1000 lines)
4. `Pass 2: RDMAP Rationalization Prompt v2.4.md` (~900 lines)
5. `Pass 3: RDMAP Validation Prompt v2.4.md` (~600 lines)

**To add these:**
1. Copy each file from project knowledge
2. Save to `research-assessor/references/workflow/`
3. Repackage the skill
4. Reinstall

**This is optional** - the skill works with the included guidance, but the full prompts provide even more extensive examples and edge case handling.

## Expected Performance

Based on testing:

**Pass 1 (Liberal Extraction):**
- Comprehensive capture with intentional over-extraction (40-50% more items)
- Preserves granularity
- Marks uncertainties

**Pass 2 (Rationalization):**
- 15-20% reduction through consolidation
- Refined boundaries
- Complete traceability via consolidation metadata

**Pass 3 (Validation):**
- Structural integrity checks
- Cross-reference validation
- Schema compliance verification

**Complete Extraction:**
- ~100-150 items per paper (varies by paper length/complexity)
- ~200+ cross-references
- Assessment-ready for transparency/replicability evaluation

## Iteration During Testing

If you encounter issues during test extractions:

1. **Check SKILL.md** - Core principles and workflow
2. **Check schema-guide.md** - Object structure questions
3. **Check tier-assignment-guide.md** - Design vs Method vs Protocol
4. **Check consolidation-patterns.md** - Lumping vs splitting decisions
5. **Check sobotkova-example.md** - Reference extraction patterns

If systematic issues emerge, you can:
- Edit specific reference files
- Repackage with `package_skill.py`
- Reinstall updated version

## Token Efficiency

The skill uses progressive disclosure:
- **Startup:** ~100 tokens (metadata only)
- **When invoked:** ~2,000-4,000 tokens (SKILL.md + relevant workflow)
- **Supporting references:** Only load as needed

This is dramatically more efficient than including 4,000+ lines of prompts in every conversation.

## Scaling to Production

Once validated on test papers:

1. **API deployment:** Upload to workspace, available for all API calls
2. **Claude Code:** Place in skills directory for automated processing
3. **Batch processing:** Process hundreds/thousands of papers consistently
4. **Version control:** Git track skill evolution

## Next Steps

1. ✅ Install the skill
2. ✅ Test on Sobotkova paper (Methods section)
3. ✅ Compare extraction quality
4. ✅ Iterate on any issues
5. ⏭️ Optionally add full prompts from project knowledge
6. ⏭️ Scale to additional papers
7. ⏭️ Move to API/Claude Code for production

## Support & Documentation

**Skill documentation:**
- SKILL.md - Core workflow and principles
- references/README.md - Documentation overview
- schema-guide.md - Complete schema reference

**Project knowledge has:**
- Complete extraction prompts
- Development history and decisions
- Testing results and refinements
- Schema evolution documentation

## Questions?

The skill includes comprehensive guidance, but if you need:
- Clarification on specific decisions → Check relevant checklist
- Schema structure questions → Check schema-guide.md
- Example patterns → Check sobotkova-example.md
- Full detailed prompts → Available in project knowledge

Happy extracting! 🎉