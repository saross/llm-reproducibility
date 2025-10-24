# Research Assessor Skill v2.5 - Deployment Guide

**Package Version:** 2.5  
**Package Date:** 2025-10-22  
**Status:** Production Ready

---

## What's Been Packaged

This is the complete research-assessor skill with all Phase 1 updates applied. The package includes:

✅ **Updated skill files:**
- Complete RDMAP verification procedures
- Updated schema guide (v2.5)
- New JSON schema file
- Updated navigation README

✅ **All supporting materials:**
- Extraction fundamentals
- Decision frameworks
- Worked examples
- Checklists

✅ **Documentation:**
- Version history
- Package manifest
- This deployment guide

---

## Package Files

### Archive File
**File:** `research-assessor-v2.5.tar.gz` (48 KB)  
**Checksum:** `research-assessor-v2.5.tar.gz.sha256`

### Directory Structure
**Directory:** `research-assessor-skill-v2.5/` (uncompressed for browsing)

**Contents:** 13 files organized in proper skill structure
- 1 SKILL.md (required)
- 2 documentation files (VERSION_HISTORY, PACKAGE_MANIFEST)
- 10 reference files (organized in subdirectories)

---

## Deployment Options

### Option 1: Deploy to Existing Skill Location (Recommended)

If you have the research-assessor skill already installed:

```bash
# Backup existing skill
mv /mnt/skills/user/research-assessor /mnt/skills/user/research-assessor-backup-v2.4

# Extract new version
cd /mnt/skills/user
tar -xzf /path/to/research-assessor-v2.5.tar.gz
mv research-assessor-packaged research-assessor

# Verify
ls -la /mnt/skills/user/research-assessor/
```

### Option 2: Fresh Installation

If this is a new installation:

```bash
# Extract to skills directory
cd /mnt/skills/user
tar -xzf /path/to/research-assessor-v2.5.tar.gz
mv research-assessor-packaged research-assessor

# Verify structure
ls -la research-assessor/references/
```

### Option 3: Update Files Individually

If you want to update only specific files:

1. **Unpack the archive:**
   ```bash
   tar -xzf research-assessor-v2.5.tar.gz
   cd research-assessor-packaged
   ```

2. **Copy specific files to existing skill:**
   ```bash
   # Update verification procedures
   cp references/verification-procedures.md /mnt/skills/user/research-assessor/references/
   
   # Update schema guide
   cp references/schema/schema-guide.md /mnt/skills/user/research-assessor/references/schema/
   
   # Add new schema JSON
   cp references/schema/extraction_schema.json /mnt/skills/user/research-assessor/references/schema/
   
   # Update README
   cp references/README.md /mnt/skills/user/research-assessor/references/
   ```

---

## Verification Steps

After deployment, verify the installation:

### 1. Check File Structure
```bash
cd /mnt/skills/user/research-assessor

# Verify root files
ls SKILL.md VERSION_HISTORY.md

# Verify references structure
ls references/
ls references/schema/
ls references/checklists/
ls references/examples/
```

**Expected output:**
```
SKILL.md
VERSION_HISTORY.md
references/
  README.md
  extraction-fundamentals.md
  verification-procedures.md
  schema/
    extraction_schema.json
    schema-guide.md
  checklists/
    tier-assignment-guide.md
    consolidation-patterns.md
    expected-information.md
  examples/
    sobotkova-example.md
```

### 2. Verify Key Updates

```bash
# Check verification-procedures has RDMAP section
grep -A 5 "PART 3: Verification for RDMAP" references/verification-procedures.md

# Check schema-guide is v2.5
grep "Schema v2.5" references/schema/schema-guide.md

# Check schema JSON exists
ls -lh references/schema/extraction_schema.json
```

### 3. Check File Permissions

```bash
# All files should be readable
find research-assessor -type f -exec test -r {} \; || echo "Permission issues found"
```

---

## What's Changed in v2.5

### Critical Updates (Must Review)

**1. Mandatory Sourcing Requirements**
- Evidence/Claims: Must have `verbatim_quote`
- Implicit content: Must have `trigger_text` + `trigger_locations`
- RDMAP: Status field distinguishes explicit vs implicit

**2. RDMAP Verification**
- Complete verification procedures now available
- Three-step process for explicit RDMAP
- Three-step process for implicit RDMAP
- Worked examples and decision trees

**3. Schema Completeness**
- New JSON schema file added
- All source_verification fields defined
- Status fields documented
- Implicit metadata structure explained

### Breaking Changes

⚠️ **v2.4 extractions will NOT validate with v2.5:**
- Missing verbatim_quotes will fail validation
- Missing trigger infrastructure will fail validation
- Missing status fields will fail validation

**Migration:** Re-extract with v2.5 prompts rather than patching v2.4 extractions

---

## Integration with Prompts

This skill package works with v2.5 prompts (provided separately by user):

**Required prompts (user-provided at runtime):**
1. claims-evidence_pass1_prompt_v2.5.md
2. claims-evidence_pass2_prompt_v2.5.md
3. claims-evidence_pass2_prompt_v2.5.md
4. rdmap_pass1_prompt_v2.5.md
5. rdmap_pass2_prompt_v2.5.md
6. rdmap_pass3_prompt_v2.5.md

**Note:** Prompts are NOT included in this skill package. They must be provided by the user at runtime.

---

## Testing After Deployment

### Quick Test

1. **Test skill invocation:**
   ```
   User: "Extract methodology from this paper"
   Expected: Skill should trigger, ask for extraction prompt
   ```

2. **Test reference loading:**
   ```
   User: "What are the sourcing requirements?"
   Expected: Claude should read extraction-fundamentals.md
   ```

3. **Test schema access:**
   ```
   User: "Show me the evidence object structure"
   Expected: Claude should read schema-guide.md
   ```

### Full End-to-End Test

1. Run Pass 1 claims-evidence on test paper
2. Run Pass 2 claims-evidence consolidation
3. Run Pass 1 RDMAP on same paper
4. Run Pass 2 RDMAP consolidation
5. Run Pass 3 unified validation
6. Verify all source_verification fields populated
7. Calculate quality metrics (should achieve >95% pass rate)

---

## Troubleshooting

### "Skill not triggering"
- Check SKILL.md is in correct location
- Verify YAML frontmatter intact
- Check file permissions

### "References not loading"
- Verify references/ directory structure
- Check file paths in error messages
- Ensure all files readable

### "Schema validation failing"
- Verify extraction_schema.json exists in references/schema/
- Check JSON is valid (no syntax errors)
- Ensure prompts are using v2.5 versions

### "Pass 3 can't verify RDMAP"
- Check verification-procedures.md has RDMAP section
- Verify file updated (should be 1,524 lines)
- Search for "PART 3: Verification for RDMAP"

---

## Rollback Procedure

If you need to rollback to v2.4:

```bash
# Remove v2.5
mv /mnt/skills/user/research-assessor /mnt/skills/user/research-assessor-v2.5-backup

# Restore v2.4 backup
mv /mnt/skills/user/research-assessor-backup-v2.4 /mnt/skills/user/research-assessor

# Verify
ls -la /mnt/skills/user/research-assessor/
```

---

## Support Resources

### Documentation Files (in package)
- **PACKAGE_MANIFEST.md** - Complete package inventory
- **VERSION_HISTORY.md** - Detailed v2.5 changes
- **references/README.md** - Navigation guide

### Key References (for extractors)
- **extraction-fundamentals.md** - Sourcing requirements
- **verification-procedures.md** - Validation procedures
- **schema-guide.md** - Object structure documentation

### For Questions About v2.5
Consult VERSION_HISTORY.md for:
- What changed
- Why it changed
- How to migrate from v2.4
- Testing recommendations

---

## Package Verification

**Package integrity:**
```bash
# Verify checksum
sha256sum -c research-assessor-v2.5.tar.gz.sha256
```

**Expected checksum:** See .sha256 file

**Package size:** 48 KB (compressed)  
**Unpacked size:** ~200 KB (13 files)

---

## Production Readiness Checklist

Before using in production:

- [ ] Package deployed to correct location
- [ ] File structure verified (13 files)
- [ ] Key updates confirmed (RDMAP section exists, schema v2.5)
- [ ] File permissions correct (all readable)
- [ ] Test invocation successful
- [ ] Test reference loading successful
- [ ] V2.5 prompts available for runtime use
- [ ] Backup of previous version created
- [ ] Rollback procedure tested (if applicable)

---

## Next Steps

1. **Deploy package** using one of the deployment options above
2. **Verify installation** using verification steps
3. **Test skill** with quick test or full end-to-end test
4. **Update prompts** ensure you're using v2.5 prompts at runtime
5. **Begin extraction** skill is ready for production use

---

## Contact & Updates

**Version:** 2.5  
**Release Date:** 2025-10-22  
**Status:** Production Ready  
**Breaking Changes:** Yes (see VERSION_HISTORY.md)

**Package Files:**
- `research-assessor-v2.5.tar.gz` (archive)
- `research-assessor-v2.5.tar.gz.sha256` (checksum)
- `research-assessor-skill-v2.5/` (uncompressed directory)

**All files available in:** `/mnt/user-data/outputs/`

---

**Deployment guide complete. Skill is ready for production use with v2.5 prompts.** 🚀
