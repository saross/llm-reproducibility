# Research Assessor Skill - Installation & Usage Guide

**Version:** 2.4  
**Architecture:** Skill + Runtime Prompts

## What You Have

The **Research Assessor** skill is now packaged and ready to install. This skill enables systematic extraction and assessment of research methodology, claims, and evidence from fieldwork-based research papers.

## Skill Structure

```
research-assessor/
├── SKILL.md                           # Core skill guide (228 lines)
└── references/
    ├── schema/
    │   └── schema-guide.md            # Complete schema documentation
    ├── checklists/
    │   ├── tier-assignment-guide.md   # Design/Method/Protocol decisions
    │   ├── consolidation-patterns.md  # When to lump vs split
    │   └── expected-information.md    # Completeness checklists
    └── examples/
        └── sobotkova-example.md       # Worked extraction example
```

**Total:** 6 files, ~1,350 lines

## Architecture: Skill + Runtime Prompts

### What's IN the Skill Package
✅ Core decision frameworks (evidence vs claims, tier assignment, consolidation logic)  
✅ Complete schema definitions (all six object types)  
✅ Reference materials (checklists, examples)  

### What You PROVIDE at Runtime
📝 Extraction prompts (detailed instructions for each pass)  
📄 Source material (research paper sections)  
📋 JSON document (template or partially populated)  

**Why this separation?** Prompts evolve frequently through testing and refinement. This architecture allows you to tune prompts without repackaging or reinstalling the skill, minimizing versioning conflicts.

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

## Getting the Extraction Prompts

The five extraction prompts (~4,400 lines total) are **NOT included in the skill package**. You provide them at runtime.

### The Five Prompts

1. **Claims/Evidence Pass 1 v2.4** (~800 lines) - Liberal extraction
2. **Claims/Evidence Pass 2 v2.4** (~900 lines) - Rationalization
3. **RDMAP Pass 1 v2.4** (~1,000 lines) - Liberal RDMAP extraction
4. **RDMAP Pass 2 v2.4** (~900 lines) - RDMAP rationalization
5. **Validation Pass 3 v2.4** (~600 lines) - Integrity checks

### Where to Store Prompts

**Option A: Project Knowledge** (Recommended)
- Add all five prompts to your Project Knowledge
- Reference by name when needed
- Easily accessible, version controlled

**Option B: Local Files**
- Save prompts as markdown files
- Copy/paste when needed
- Maintain your own versions

**Option C: GitHub Repository**
- Store in `prompts/` directory
- Version control with git
- Share with collaborators

## Using the Skill

### Basic Usage Pattern

The skill is invoked by **providing the extraction prompt along with your request**:

```
You: I'm using the research-assessor skill for extraction.

Here's the Claims/Evidence Pass 1 prompt:
[paste entire ~800 line prompt]

Extract from this section:
[paste source text]

Use this JSON document:
[paste blank template or partially populated JSON]

Claude: [Follows prompt to extract, consulting skill references as needed]
```

### The skill provides support by:
- Loading decision frameworks when uncertain
- Consulting tier-assignment-guide.md for boundary cases
- Checking consolidation-patterns.md for rationalization
- Referencing schema-guide.md for structure questions
- Reviewing examples for pattern guidance

### Complete Workflow Example

```
1. Start with blank JSON template
2. Provide Claims Pass 1 prompt + section → Liberal extraction
3. Provide Claims Pass 2 prompt + Pass 1 JSON → Consolidation
4. Provide RDMAP Pass 1 prompt + section → Liberal RDMAP extraction  
5. Provide RDMAP Pass 2 prompt + Pass 1 JSON → RDMAP consolidation
6. Provide Validation Pass 3 prompt + complete JSON → Integrity checks
```

### Why You Provide Prompts

**Flexibility:**
- Refine prompts based on testing without reinstalling skill
- Create domain-specific prompt variations
- Experiment with different approaches
- Maintain multiple prompt versions

**Version Control:**
- You control which prompt version to use
- Can A/B test prompt improvements
- Easy rollback if needed

**Transparency:**
- Explicit about what instructions Claude receives
- Clear separation of framework (skill) and implementation (prompts)
- Reproducible research practice

## Testing on Sobotkova Paper

The skill was developed and tested on:
**Sobotkova et al. (2023)** "Arbitrary Offline Data Capture on All of Your Androids: The FAIMS Mobile Platform"

**Recommended first test:**
1. Install the skill
2. Get all five extraction prompts
3. Extract Sobotkova Methods section
4. Compare to example extraction in skill references
5. Verify quality and patterns

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

**Time per Section:**
- Pass 1: 10-15 minutes
- Pass 2: 10-15 minutes
- Pass 3: 5-10 minutes
- **Total: 30-40 minutes per section**

## Working with Prompts

### Storing in Project Knowledge

**Recommended setup:**
1. Create Project in Claude
2. Add all five prompts as separate documents
3. Name clearly: "Claims Pass 1 v2.4", "RDMAP Pass 1 v2.4", etc.
4. Reference when needed: "Use the Claims Pass 1 v2.4 prompt from Project Knowledge"

### Customizing Prompts

You can adapt prompts for your needs:
- Add domain-specific examples
- Modify expected information checklists
- Adjust consolidation patterns
- Change vocabulary

**The skill's frameworks remain stable**, supporting whatever prompt variations you create.

## Troubleshooting

### Claude doesn't follow the prompt
**Solution:** Ensure you:
- Provided the COMPLETE prompt (full ~800-1000 lines)
- Mentioned "using research-assessor skill"
- Included source text and JSON template

### Uncertain about tier assignment
**Solution:** The skill will automatically read `tier-assignment-guide.md` when uncertain about Design vs Method vs Protocol decisions.

### Consolidation seems wrong
**Solution:** The skill can consult `consolidation-patterns.md` for guidance on when to lump vs split items.

### Schema questions
**Solution:** The skill references `schema-guide.md` for complete object structure definitions.

## Token Efficiency

The skill uses progressive disclosure:
- **Skill metadata:** ~100 tokens (always loaded)
- **SKILL.md:** ~1,500 tokens (when skill invoked)
- **Supporting references:** ~1,000-2,000 tokens each (only when needed)
- **Your prompts:** ~4,000-5,000 tokens (you provide when needed)

**Total per extraction:** ~5,500-8,500 tokens (efficient for complex work)

## Iteration During Testing

If you encounter issues:

1. **Review skill references:**
   - Check SKILL.md for core principles
   - Check schema-guide.md for structure
   - Check tier-assignment-guide.md for boundary decisions
   - Check consolidation-patterns.md for rationalization
   - Check sobotkova-example.md for patterns

2. **Refine your prompts:**
   - Modify extraction instructions
   - Add clarifying examples
   - Adjust decision frameworks
   - Save as new version

3. **Retest:**
   - Use refined prompt
   - Compare to previous results
   - Measure quality improvement

**No need to touch the skill package** - just iterate on your prompts.

## Scaling to Production

Once validated on test papers:

### API Deployment
```bash
# Skill installed once in workspace
# Prompts provided in each API call
curl -X POST https://api.anthropic.com/v1/messages \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -d '{
    "model": "claude-sonnet-4-20250514",
    "messages": [{
      "role": "user", 
      "content": "Using research-assessor skill. [prompt] [source]"
    }]
  }'
```

### Claude Code
```python
# Skill automatically available
# Provide prompts programmatically
with open('prompts/claims-pass1-v2.4.md') as f:
    prompt = f.read()

response = client.extract(
    prompt=prompt,
    source=paper_section,
    template=json_template
)
```

### Batch Processing
- Process hundreds/thousands of papers consistently
- Version control prompts with git
- Track quality metrics over time
- Iterate based on patterns

## What's Included in the Skill

### ✅ Fully Functional as Packaged

**SKILL.md** - Core workflow guide
- Architecture explanation
- Decision frameworks
- Usage instructions
- Quality principles

**references/schema/schema-guide.md** - Complete schema
- All six object types
- Field definitions
- Cross-reference patterns
- Examples

**references/checklists/** - Decision support
- tier-assignment-guide.md - Design/Method/Protocol
- consolidation-patterns.md - Lump vs split
- expected-information.md - Completeness checklists

**references/examples/** - Worked extraction
- sobotkova-example.md - Complete RDMAP extraction from real paper

**The skill is fully functional as packaged.** The extraction prompts you provide at runtime add the detailed step-by-step instructions.

## Next Steps

1. ✅ Install the skill from research-assessor.zip
2. ✅ Store the five extraction prompts (Project Knowledge or local files)
3. ✅ Test on Sobotkova paper Methods section
4. ✅ Verify extraction quality
5. ⏭️ Refine prompts based on your domain needs
6. ⏭️ Scale to additional papers
7. ⏭️ Move to API/Claude Code for production

## Documentation & Support

**Complete documentation available:**
- **README.md** - Project overview
- **USAGE_GUIDE.md** - Detailed how-to instructions
- **ARCHITECTURE.md** - Complete design rationale
- **PROMPT_REVISION_SUMMARY.md** - Development history
- **TESTING.md** - Testing procedures
- **CONTRIBUTING.md** - How to contribute
- **VERSION.md** - Version history

**All documentation in GitHub repository.**

**In the skill package:**
- SKILL.md - Core workflow
- schema-guide.md - Object structures
- Checklists - Decision frameworks
- Example - Reference patterns

## Questions?

**About using the skill:**
- Check SKILL.md in skill package
- Review USAGE_GUIDE.md in repository
- Consult reference materials

**About prompts:**
- See PROMPT_REVISION_SUMMARY.md for development
- Check examples in prompts for patterns
- Repository documentation has complete details

**About architecture:**
- See ARCHITECTURE.md for design rationale
- Understand skill + runtime prompts model
- Learn why prompts separate from skill

## Key Differences from Previous Versions

**v2.4 Changes:**
- ❌ Prompts NOT in skill package (you provide at runtime)
- ❌ No workflow/ directory
- ❌ No READMEs in skill (per best practices)
- ✅ Ultra-lean skill (1,350 lines vs 5,000+)
- ✅ Skill + Runtime Prompts architecture
- ✅ Rapid prompt iteration without reinstallation
- ✅ Flexible, version-controllable prompts

**Why this is better:**
- Prompts evolve faster than framework
- No reinstallation friction
- User controls prompt versions
- Experimentation encouraged
- Cleaner separation of concerns

Happy extracting! 🎉
