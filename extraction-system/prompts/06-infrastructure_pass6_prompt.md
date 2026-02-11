# Reproducibility Infrastructure Extraction - PASS 6: Infrastructure & FAIR Assessment v2.0

**Version:** 2.0 Pass 6
**Last Updated:** 2025-11-03
**Workflow Stage:** Pass 6 - Infrastructure extraction with FAIR assessment
**Schema Version:** Canonical v2.5 + Infrastructure v2.0

---

## Your Task

Extract reproducibility infrastructure and assess FAIR compliance from a research paper. This is **Pass 6: Infrastructure Extraction** - systematic capture of Persistent Identifiers (PIDs), funding, data/code availability, author contributions, ethics, permits, and supplementary materials.

**Input:** JSON extraction document (schema v2.5) with content extraction complete
- Evidence, claims, methods, protocols, research designs populated (Passes 1-5)
- `reproducibility_infrastructure` section empty

**Your responsibility:** Populate `reproducibility_infrastructure` with 14 sections:
1. `persistent_identifiers` (PIDs + PID graph analysis)
2. `funding`
3. `data_availability`
4. `code_availability`
5. `author_contributions`
6. `conflicts_of_interest`
7. `ethics_approval`
8. `permits_and_authorizations`
9. `preregistration`
10. `supplementary_materials`
11. `references_completeness`
12. `fair_assessment` (Findable, Accessible, Interoperable, Reusable)
13. `data_completeness` (dataset inventory and accessibility assessment)
14. `extraction_metadata`

**Leave untouched:** Evidence, claims, methods, protocols, research_designs arrays (already extracted)

**Output:** Same JSON document with `reproducibility_infrastructure` fully populated

---

## 🚨 CRITICAL: Paper Location Strategy

Infrastructure is NOT in Methods/Results/Discussion. Target these specific locations:

### Front Matter (check FIRST)
- Title page - Author affiliations, ORCIDs (often in superscripts/footnotes)
- Header/footer - DOI for paper itself
- Author list - Names and positions for author contributions mapping

### Back Matter (check SECOND)
- **Acknowledgements** - Funding, permits, institutional support
- **Data Availability Statement** - Repository links, DOIs, access conditions
- **Code Availability Statement** - Repository links, DOIs, software versions
- **Author Contributions** - CReDIT taxonomy or free text
- **Competing Interests / Conflicts of Interest** - Financial or intellectual
- **Ethics Statement** - IRB approval, consent procedures
- **Supplementary Information** - Additional files, datasets, protocols

### References Section (check THIRD)
- Self-citations to datasets published separately
- Software citations with DOIs or version numbers
- Repository references in citation list

### Methods Section (check FOURTH - selective)
- Permits mentioned in "Study Site" or "Field Methods" subsections
- Ethics approval referenced in "Participants" or "Sampling"
- Software versions and DOIs in "Data Analysis"

**Extraction order:** Front matter → Back matter → References → Methods (selective)

**If no back matter sections exist:** Mark sections as `statement_present: false` with `notes: "No dedicated statement section found"`. Don't skip the search.

---

## 🚨 CRITICAL: Persistent Identifier (PID) Requirements

**For complete PID types, formats, adoption context, validation rules, and connectivity scoring:**
→ See `references/infrastructure/pid-systems-guide.md` in research-assessor skill

**Key reference sections:**
- PID types (DOI, ORCID, RAiD, IGSN, accession numbers, software PIDs, vocabulary PIDs)
- Format specifications and validation patterns
- HASS-specific adoption context and timelines
- Software PIDs (Software Heritage, Zenodo, CodeMeta)
- ORCID coverage calculation and categories
- PID graph connectivity scoring framework

### PID Extraction Rules (Summary)

**For each PID found:**
1. **Extract identifier** - Exact format from paper
2. **Construct resolver URL** - Standard format (DOI: `https://doi.org/[id]`, ORCID: `https://orcid.org/[id]`)
3. **Record location** - Where in paper
4. **Do NOT verify resolution** - Verification happens in Pass 7

**Always extract (if present):** Paper DOI, author ORCIDs, dataset DOIs, software DOIs

**Extract if present (emerging):** RAiD, IGSN, vocabulary PIDs

**Calculate metrics:**
- ORCID coverage percentage and category (none/minimal/partial/high/complete)
- PID graph connectivity score (0-6 scale based on distinct PID types present)

**See pid-systems-guide.md for detailed extraction procedures and scoring formulas.**

---

## 🚨 CRITICAL: FAIR Assessment Framework (v2.0)

**Rubric version:** 2.0 (standardised 2026-02-11)

**For detailed criteria, examples, and context-dependent guidance:**
→ See `references/infrastructure/fair-principles-guide.md` in research-assessor skill

### Self-Contained Rubric: 15 Binary Sub-Principles

Score data and code **independently** as two parallel FAIR assessments.
Each sub-principle is binary: present (1) or absent (0).

```text
FINDABLE (max 4):
  F1: Globally unique persistent identifier (DOI, IGSN, SWHID, accession)  /1
  F2: Rich metadata (structured: authors, title, keywords, description)     /1
  F3: Metadata explicitly includes the identifier                           /1
  F4: Resource indexed in searchable registry (Zenodo, CRAN, DataCite)      /1

ACCESSIBLE (max 4):
  A1:   Retrievable via standard protocol — assess against FULL research    /1
        dataset, not just supplement. If data_completeness coverage is
        "minimal" or "partial", A1 = 0. Exception: ethical restrictions.
  A1.1: Protocol is open, free, universally implementable                   /1
  A1.2: Protocol allows authentication/authorisation where needed           /1
        (CARE-compliant restrictions = POSITIVE signal)
  A2:   Metadata remains accessible even if resource unavailable            /1

INTEROPERABLE (max 3 — NOT 4):
  I1: Uses formal, accessible, shared knowledge representation              /1
  I2: Vocabularies follow FAIR principles themselves                        /1
  I3: Includes qualified references to other resources (PIDs)               /1

REUSABLE (max 4):
  R1:   Richly described with plurality of relevant attributes              /1
  R1.1: Released with clear, accessible data usage licence                  /1
  R1.2: Associated with detailed provenance                                 /1
  R1.3: Meets domain-relevant community standards                           /1

TOTAL per artefact type: /15
```

### Independent Data and Code Scoring

- Score `data_fair` (/15) and `code_fair` (/15) separately
- Do NOT sum into a single aggregate — report independently
- When data or code is absent/not applicable, set `"available": false`
- Absence ≠ non-compliance (distinguish N/A from Not FAIR)

### Rating Thresholds (per artefact type, on /15)

| Score | Percentage | Rating |
|-------|------------|--------|
| 13-15 | 87-100% | Highly FAIR |
| 9-12 | 60-80% | Moderately FAIR |
| 5-8 | 33-53% | Minimally FAIR |
| 0-4 | 0-27% | Not FAIR |

### Output JSON Structure

```json
{
  "fair_assessment": {
    "version": "2.0",
    "scale": "binary_sub_principles",
    "data_fair": {
      "available": true,
      "findable": {
        "F1_persistent_identifier": { "present": true, "evidence": "..." },
        "F2_rich_metadata": { "present": true, "evidence": "..." },
        "F3_metadata_includes_identifier": { "present": true, "evidence": "..." },
        "F4_searchable_registry": { "present": true, "evidence": "..." },
        "subtotal": 4, "max": 4
      },
      "accessible": { "...same pattern...", "subtotal": 4, "max": 4 },
      "interoperable": { "...same pattern...", "subtotal": 2, "max": 3 },
      "reusable": { "...same pattern...", "subtotal": 3, "max": 4 },
      "total": 13, "max": 15, "percentage": 86.7,
      "rating": "highly_fair"
    },
    "code_fair": { "...same structure as data_fair..." },
    "research_type": "computational|data_centric|code_centric|mixed",
    "fair_profile": "Human-readable summary",
    "contextual_notes": "..."
  }
}
```

### Data Completeness Assessment

Assess whether the paper shares **all** the data needed for reproduction, not just the subset deposited in a supplement or repository. This captures a dimension that FAIR infrastructure scoring alone misses.

**Procedure:**

1. **Enumerate datasets** referenced in Methods/Results (including upstream sources)
2. **Classify each** using the 5-level access taxonomy:
   - Level 0: Direct download (DOI-based repository, open supplement)
   - Level 1: Programmatic extraction (HTML tables, API)
   - Level 2: Available but requires manual steps (registration, paywall, PDF table extraction)
   - Level 3: Exists but inaccessible (closed thesis, paywalled monograph, co-author held)
   - Level 4: Not found / never published
3. **Calculate coverage**: datasets accessible (Level 0-2) / total datasets. Where feasible, also compute record-weighted coverage.
4. **Assign category**: complete (100%), substantial (75-99%), partial (25-74%), minimal (0-24%)
5. **Identify barriers**: co-author gatekeeping, closed monograph, unpublished, embargoed, proprietary, ethics restricted, paywall, registration required

**Assessment scope** (for meta-analyses or papers aggregating many datasets):
- `straightforward`: <20 datasets — full inventory
- `complex`: 20-99 datasets — sampled inventory with extrapolation
- `infeasible`: 100+ datasets — estimate only, with rationale

**Cross-reference with A1 scoring:** If `coverage_category` is "minimal" or "partial", set A1 = 0 for data FAIR. Exception: ethically restricted data (CARE principles, human subjects) does not count against completeness.

**Output JSON structure:**

```json
{
  "data_completeness": {
    "assessment_scope": "straightforward | complex | infeasible",
    "assessment_scope_rationale": "String",
    "datasets_referenced": 13,
    "datasets_accessible": 3,
    "datasets_inaccessible": 10,
    "coverage_percentage": 23.1,
    "coverage_category": "minimal | partial | substantial | complete",
    "record_weighted": {
      "total_records": 5042,
      "accessible_records": 2149,
      "coverage_percentage": 42.6
    },
    "barriers": [
      {
        "type": "co_author_gatekeeping",
        "datasets_affected": 6,
        "description": "Six datasets held by co-authors with no independent deposit"
      }
    ],
    "notes": "Free text summary"
  }
}
```

**Coverage category thresholds:**

| Category | Range | Definition |
|----------|-------|------------|
| complete | 100% | All datasets accessible |
| substantial | 75-99% | Most accessible, minor gaps |
| partial | 25-74% | Significant gaps |
| minimal | 0-24% | Few or no datasets accessible |

**Barrier types:** `co_author_gatekeeping`, `closed_monograph`, `unpublished`, `embargoed`, `proprietary`, `ethics_restricted`, `paywall`, `registration_required`, `other`

For papers where record counts are unavailable, `record_weighted` is null. For `infeasible` scope, inventory is omitted and coverage is estimated.

### Context-Dependent Assessment

- Publication year expectations (pre-2016 vs 2016-2019 vs 2020+)
- Discipline baseline (HASS 17-24% ORCID vs natural sciences 91-93%)
- Research type (fieldwork, laboratory, computational, archival)
- CARE principles integration (ethical restrictions = positive)
- Machine-actionability rating: None / Low / Moderate / High

---

## Extraction Workflow

### STEP 1: Front Matter Scan (PIDs)

**Extract from title page, headers, footers:**
1. **Paper DOI** - Header/footer of first page
   - Record exact DOI
   - Construct resolver URL
   - Mark `resolves: null` (Pass 7 verifies)

2. **Author ORCIDs** - Superscripts, footnotes, author affiliations
   - Match each ORCID to author name
   - Record author position (first, middle, last, corresponding)
   - Calculate ORCID coverage metrics
   - Construct ORCID URLs

**ORCID Extraction Protocol:**

**Primary source:** Author affiliations section, acknowledgements, author contribution statements in PDF text

**Secondary source (optional):** CrossRef metadata API query (not required for standard extraction)

**Status values:**
- `present_in_pdf`: ORCIDs found in paper content (extract and record)
- `none_found_in_extracted_text`: Checked affiliations/acknowledgements but no ORCIDs present
- `not_checked_publisher_metadata`: Did not query external CrossRef/publisher APIs

**Important note:** ORCIDs may exist in journal publisher systems (online version, CrossRef metadata) but absent from PDF. Record absence in PDF explicitly; do not infer "no ORCID" means author lacks one.

**Do not:** Attempt external searches for ORCIDs beyond paper content (out of scope for paper-based extraction)

**Example from test corpus:**
- Sobotkova et al. 2024 (Journal of Documentation, 2024): `orcid_status: "none_found_in_extracted_text"`
- Penske et al. 2023 (Nature, 2023): `orcid_status: "none_found_in_extracted_text"`
- Note: Both recent papers from journals with ORCID policies, but PDFs lack ORCIDs in text

3. **Update extraction_metadata.sections_examined** - "title_page", "author_affiliations"

---

### STEP 2: Back Matter Scan (Acknowledgements, Statements)

**Scan for dedicated sections in this order:**

**2.1 Acknowledgements**
- **Funding** - Grant numbers, funder names, project IDs
  - Extract verbatim_text for each funding source
  - Record funder name, grant_number (if stated)
  - Check for RAiD project identifiers (rare but possible)
  - Note location

- **Permits** - Archaeological permits, excavation licences, land access, heritage consent
  - **For complete permit types, CARE principles integration, and assessment guidance:**
    → See `references/infrastructure/fieldwork-permits-guide.md` in research-assessor skill
  - Extract verbatim_text for each permit
  - Classify permit_type (10 types: excavation, sampling, land access, heritage consent, export, import, collection access, survey, diving, protected area)
  - Record issuing_authority, jurisdiction, permit_number, dates
  - Note CARE principles integration (Traditional Owner agreements, community research agreements)
  - Cross-reference with Methods section if needed

**2.2 Data Availability Statement**
- Statement present? (yes/no)
- Statement type: "available", "included", "restricted", "not_applicable", "none"
- Repositories used:
  - Name, URL, type (domain_specific, general, institutional, supplementary)
  - Dataset DOIs (extract all)
  - Access conditions (open, restricted, embargoed)
  - Licence information
- Machine-actionability assessment (none/low/moderate/high)

**2.3 Code Availability Statement**
- Statement present? (yes/no)
- Statement type: "available", "included", "not_applicable", "none"
- Repositories used:
  - Name (GitHub, GitLab, Zenodo), URL
  - Software DOIs (extract all)
  - Version numbers, commit hashes
  - Licence information
- Machine-actionability assessment

**2.4 Author Contributions**
- **For complete CReDIT taxonomy (14 roles), format variations, and extraction guidance:**
  → See `references/infrastructure/credit-taxonomy.md` in research-assessor skill
- Statement present? (yes/no)
- Format: "credit" (structured), "narrative" (free text), "mixed", "equal_contribution", "not_stated"
- Extract contribution for each author:
  - Author name
  - CReDIT roles (if structured format): 14 standardised roles (Conceptualisation, Data Curation, Formal Analysis, Funding Acquisition, Investigation, Methodology, Project Administration, Resources, Software, Supervision, Validation, Visualisation, Writing – Original Draft, Writing – Review & Editing)
  - Free-text description (if narrative format)
- Cross-reference with ORCIDs if available
- Validate author count matches paper_metadata.authors

**2.5 Conflicts of Interest / Competing Interests**
- Statement present? (yes/no)
- Conflicts declared? (yes/no)
- Extract verbatim_text
- Type: financial, intellectual, none_declared, not_stated

**2.6 Ethics Approval and Permissions**

Distinguish three types of research governance:

**2.6a Ethics Committee Approval**

**Scope:** Living human subjects, contemporary communities, identifiable personal data

**Indicators:**
- Institutional Review Board (IRB) approval (USA)
- Human Research Ethics Committee (HREC) approval (Australia)
- Ethics committee protocol numbers (e.g., "Approved by University Ethics Committee #2023-45")
- Informed consent procedures described

**Extract:**
- Statement present? (yes/no)
- Ethics body name, protocol number, institution
- Approval date, jurisdiction
- Consent procedures described

**2.6b Institutional Permissions**

**Scope:** Archaeological materials, museum collections, archival research, ancient DNA

**Indicators:**
- Permission from excavators, curators, museum directors
- Often granted via co-authorship (authorities as co-authors)
- Government permits for archaeological work
- Museum access agreements

**Regional Variation in Ancient DNA Ethics:**

**Critical**: Ancient DNA ethical frameworks vary substantially by region.

| Region | Typical Requirement | Approval Type | Example |
|--------|---------------------|---------------|---------|
| **Europe** | Institutional permissions | Excavators/curators control materials | "Permission granted by museum directors" |
| **Australia** | Formal ethics committee approval | HREC often required even for ancient remains | AIATSIS Code of Ethics applies |
| **North America** | Varies by Indigenous affiliation | NAGPRA, tribal consultation, THPO involvement | Native American remains require tribal approval |

**Europe:**
- Typically requires institutional permissions (excavators/curators as co-authors)
- Ethics committees less common unless involving contemporary descendant communities
- Permission statements standard: "Permission granted by site directors and museum curators who are co-authors"

**Australia:**
- Often requires formal HREC approval even for ancient remains, especially if Indigenous affiliation
- Australian Institute of Aboriginal and Torres Strait Islander Studies (AIATSIS) Code of Ethics applies
- Community consultation expected for Indigenous materials

**North America:**
- Varies by Indigenous affiliation and federal land status
- Native American Graves Protection and Repatriation Act (NAGPRA) applies to federally affiliated remains
- Tribal consultation and Tribal Historical Preservation Office (THPO) involvement for Indigenous materials
- State-level regulations vary

**Extract:**
- Permission statements present? (yes/no)
- Type: archaeological_samples, museum_collections, archival_materials, ancient_DNA
- Authority: excavators, curators, museum directors, government agency
- Verbatim statement
- Regional context noted

**Example (Penske 2023):**
```json
{
  "permission_statements": [{
    "type": "archaeological_samples",
    "authority": "excavators, archaeologists, curators, museum directors (as co-authors)",
    "verbatim": "Permission to work on the archaeological samples was granted by the respective excavators, archaeologist and curators and museum directors of the sites, who are co-authoring the study.",
    "regional_context": "Europe - standard institutional permissions"
  }]
}
```

**2.6c Cultural Protocols**

**Scope:** Indigenous remains, descendant communities, sensitive cultural materials

**Indicators:**
- CARE principles compliance (Collective benefit, Authority to control, Responsibility, Ethics)
- Indigenous data sovereignty statements
- Community consultation documented
- Traditional owner permissions
- Restrictions on data use or publication

**Cross-reference:** See `fieldwork-permits-guide.md` for detailed CARE principles guidance

**Extract:**
- Cultural protocols documented? (yes/no)
- CARE principles addressed?
- Indigenous consultation described?
- Data sovereignty restrictions?
- Community agreements mentioned?

**Example structure:**
```json
{
  "cultural_protocols": {
    "care_compliant": true,
    "indigenous_consultation": "Extensive consultation with X descendant community documented",
    "data_sovereignty": "Data access restrictions per community agreements",
    "notes": "CARE principle emphasis: Authority to control (community approves analyses)"
  }
}
```

**2.7 Preregistration**
- Statement present? (yes/no)
- Study preregistered? (yes/no)
- Platform: osf, clinicaltrials_gov, aspredicted, other
- Registration ID, URL
- Registration date vs study start date

**2.8 Supplementary Information**
- Supplementary files listed? (yes/no)
- For each file:
  - Type: dataset, protocol, figure, table, code, video, other
  - Description
  - Location: publisher_site, repository, supplementary_pdf, author_website
  - DOI or URL (if provided)
- Access status: publicly_accessible, available_on_request, publisher_website, unclear, mentioned_unavailable

**Supplementary Materials Access Status Taxonomy:**

| Status | When to Use | Example |
|--------|-------------|---------|
| `publicly_accessible` | URL provided, freely accessible without login | Figshare link in paper |
| `available_on_request` | Explicit "available from authors on request" | Email contact provided |
| `publisher_website` | Behind journal paywall with paper | Nature supplementary info tab |
| `unclear` | Mentioned but no access information | "See supplementary videos" (no URL) |
| `mentioned_unavailable` | Referenced but explicitly cannot be accessed | "Videos no longer available" |

**Extraction Protocol:**
1. Extract access information **exactly as stated in paper** (URL, "available from authors", "see publisher website")
2. **Do not** attempt external searches (publisher websites, institutional repositories, author websites)
3. Record only what paper explicitly provides
4. Note ambiguity in `notes` field when access unclear

**Example (unclear access):**
```json
{
  "supplementary_materials": {
    "present": true,
    "description": "Supplementary videos mentioned in text demonstrating FAIMS interface",
    "access_status": "unclear",
    "repository_url": null,
    "notes": "Videos referenced in discussion but no access information, URL, or repository provided"
  }
}
```

**2.9 Handling Missing or Informal Statements**

Many papers lack formal "Data Availability" or "Code Availability" statements but reference datasets or software informally. Use this decision tree:

**Decision Tree:**

```
Does paper have formal "Data/Code Availability" statement?
├─ YES → Extract verbatim, use appropriate statement_type
├─ NO → Check paper body for dataset/software references
    ├─ Dataset/software referenced but no access info
    │   └─ statement_type: "implicit_reference"
    │   └─ Capture references in notes
    │   └─ datasets: [] (empty - no structured info)
    ├─ No dataset/software mentions at all
    │   └─ statement_present: false
    │   └─ statement_type: "not_applicable"
    └─ Proprietary/unpublished data mentioned
        └─ statement_type: "restricted_access"
        └─ Note restrictions in rationale
```

**statement_type Taxonomy:**
- `available_with_accession`: Formal statement with repository accession
- `available_on_request`: Formal statement, contact authors
- `available_in_supplementary`: Data/code in supplementary files
- `implicit_reference`: Informal mentions, no access information
- `restricted_access`: Access restrictions stated (ethics, commercial, privacy)
- `not_applicable`: No relevant outputs to share

**Examples:**

**Formal statement (Penske 2023):**
```json
{
  "statement_present": true,
  "statement_type": "available_with_accession",
  "verbatim_statement": "The DNA sequences reported in this paper have been deposited in the European Nucleotide Archive under the accession number PRJEB62503."
}
```

**Implicit reference (Sobotkova 2024):**
```json
{
  "statement_present": false,
  "statement_type": "implicit_reference",
  "verbatim_statement": "No formal data availability statement. References 'TRAP survey data from 2009-2015' and 'fieldwork data' but no repository or access information provided.",
  "datasets": []
}
```

**Not applicable (theory paper):**
```json
{
  "statement_present": false,
  "statement_type": "not_applicable",
  "verbatim_statement": "No data availability statement. Theoretical paper with no empirical data collection."
}
```

**3. Update extraction_metadata.sections_examined** - List all sections checked (even if "not found")

---

### STEP 3: References Section Scan

**Look for self-citations to research outputs:**
- Dataset publications (author-name overlap with paper authors)
- Software publications (author-name overlap)
- Prior publications from same project

**Extract PIDs from references:**
- Dataset DOIs referenced
- Software DOIs referenced
- Vocabulary/ontology DOIs referenced

**Cross-reference with Data/Code Availability Statements:**
- Do referenced datasets match availability statement?
- Flag discrepancies in extraction_notes

---

### STEP 4: Methods Section Scan (Selective)

**Target specific subsections:**

**Study Site / Field Site:**
- Permits mentioned? Extract details
- Ethics approval mentioned? Cross-reference with ethics statement

**Participants / Sampling:**
- Ethics approval referenced? Extract details
- Informed consent procedures

**Data Analysis / Statistical Analysis:**
- Software packages with version numbers
- Software DOIs or repository links
- Sample PIDs mentioned (rare)

**Do NOT re-extract methods/protocols** - those are in methods/protocols arrays from Pass 4

---

### STEP 5: PID Graph Summary

**After extracting all PIDs:**

1. **Calculate connectivity score** (0-6)
   - Paper DOI present? +1
   - Any author ORCID? +1
   - Dataset DOI? +1
   - Software DOI? +1
   - Sample PID? +1
   - Project RAiD OR vocabulary DOI? +1

2. **Assign connectivity rating:**
   - 0-1: minimal
   - 2-3: moderate
   - 4-5: strong
   - 6: complete

3. **Populate pid_graph_summary** in persistent_identifiers section

---

### STEP 6: FAIR Assessment

**For data_availability and code_availability:**

1. **If no data/code shared:** Skip detailed FAIR assessment, mark `assessed: false`

2. **If data/code shared:** Assess all four FAIR dimensions:
   - **Findable** - PIDs, metadata, indexing (F1-F4)
   - **Accessible** - Protocol, openness, auth, persistence (A1-A2)
   - **Interoperable** - Format, vocabularies, references (I1-I3)
   - **Reusable** - Documentation, licence, provenance, standards (R1-R1.3)

3. **Score each criterion** (0 or 1) with rationale

4. **Calculate totals:**
   - Sum per dimension (e.g., Findable: 3/4)
   - Total FAIR score (e.g., 14/16)
   - FAIR percentage (e.g., 87.5%)
   - FAIR rating (not_fair, minimally_fair, moderately_fair, highly_fair)

5. **Assess machine-actionability:**
   - Rating: none, low, moderate, high
   - Rationale: API? Structured format? Documented schema?

6. **Record discipline context:**
   - Publication year expectations
   - Discipline baseline (HASS vs natural sciences)
   - Research type considerations
   - Rationale for contextual scoring decisions

7. **Generate recommendations:**
   - What would improve FAIR compliance?
   - Specific missing elements (PID types, metadata, licence, documentation)

---

### STEP 7: References Completeness

**Simple check:**
- Are references formatted with DOIs where available?
- Percentage estimate of references with DOIs vs without
- Note: "doi_usage": "high" (>80%), "moderate" (40-80%), "low" (<40%)

---

### STEP 8: Extraction Metadata

**Record:**
- Extraction date (ISO 8601: YYYY-MM-DD)
- Extractor (claude-sonnet-4-5)
- Sections examined (array of all sections checked, even if empty)
- Extraction notes (uncertainties, ambiguities, missing sections)

---

## Self-Validation Checklist

**Before finalizing, verify:**

### Format Validity
- [ ] DOIs start with "10." (if present)
- [ ] ORCIDs follow format "0000-0000-0000-000X" (if present)
- [ ] URLs use https:// (if present)
- [ ] RAiDs are DOI-based starting with "10.RAID/" (if present)
- [ ] IGSNs follow expected alphanumeric format (if present)

### Completeness
- [ ] All 14 infrastructure sections examined (even if "not present")
- [ ] extraction_metadata.sections_examined lists all checked sections
- [ ] All identified PIDs have resolver URLs recorded
- [ ] PID graph summary completed (connectivity_score calculated)
- [ ] FAIR assessment completed if data/code shared (all four dimensions scored)
- [ ] `data_completeness` populated (or `assessment_scope` = "infeasible" with rationale)
- [ ] Author contributions count matches paper_metadata.authors count

### Cross-Checks
- [ ] ORCID list matches author list from paper_metadata
- [ ] Funding acknowledgements consistent with funding array
- [ ] Data Availability Statement matches repositories array
- [ ] Code Availability Statement matches software repositories array
- [ ] Permits mentioned in Methods cross-referenced with permits_and_authorizations
- [ ] Ethics approval in Methods matches ethics_approval section
- [ ] Supplementary materials DOIs extracted to dataset_pids or software_pids (if applicable)

### Contextual Assessment
- [ ] FAIR assessment includes discipline_context with publication year
- [ ] Context rationale explains scoring expectations
- [ ] Recommendations are specific and actionable

**Mark any failed checks in extraction_metadata.notes for Pass 7 validation.**

---

## Common Pitfalls

**❌ Searching Methods section first**
- Infrastructure is in back matter (Acknowledgements, Availability Statements)
- Search Methods only for permits/ethics cross-references

**❌ Skipping absent sections**
- If no Data Availability Statement found, mark `statement_present: false`
- Don't leave fields blank - record absence explicitly

**❌ Treating "available on request" as FAIR**
- Email request = NOT machine-actionable
- Score Accessible A1 as 0 points (no standard protocol)

**❌ Extracting URLs without checking for DOIs**
- Repository landing page may show DOI not visible in paper
- Record paper-stated identifiers only; Pass 7 verifies

**❌ Penalizing older papers for missing PIDs**
- ORCID adoption pre-2016 was minimal
- Adjust FAIR expectations by publication year

**❌ Forgetting CARE principles context**
- Restricted access to Indigenous data with community authorization = POSITIVE signal
- Mark A1.2 as 1 point with ethical justification rationale

**❌ Not calculating PID graph connectivity**
- Sum distinct PID types (0-6), assign rating
- This metric is critical for assessment

**❌ Author count mismatch**
- Author contributions must cover all authors from paper_metadata
- Flag discrepancies in extraction_notes

---

## Output Format

**Return the same JSON document you received, with `reproducibility_infrastructure` populated.**

**Complete structure:**
```json
{
  "reproducibility_infrastructure": {
    "persistent_identifiers": { ... },
    "funding": [ ... ],
    "data_availability": { ... },
    "code_availability": { ... },
    "author_contributions": { ... },
    "conflicts_of_interest": { ... },
    "ethics_approval": { ... },
    "permits_and_authorizations": { ... },
    "preregistration": { ... },
    "supplementary_materials": { ... },
    "references_completeness": { ... },
    "fair_assessment": { ... },
    "data_completeness": { ... },
    "extraction_metadata": { ... }
  }
}
```

**For complete field definitions, examples, and PID formats:**
→ See `planning/REPRODUCIBILITY_INFRASTRUCTURE_SCHEMA.md`

**Leave unchanged:** Evidence, claims, methods, protocols, research_designs arrays

**Update:** extraction_metadata with infrastructure sections examined

---

## Remember

**Pass 6 completes the extraction phase** - all intrinsic content (Passes 1-5) + extrinsic infrastructure (Pass 6) captured.

**Infrastructure is NOT in Methods/Results:**
- Start with front matter (PIDs)
- Focus on back matter (Acknowledgements, Availability Statements)
- Validate with references and selective Methods checks

**FAIR assessment requires context:**
- Publication year expectations
- Discipline baseline (HASS vs natural sciences)
- Ethical restrictions = positive when justified

**Machine-actionability is the key distinction:**
- "Available" ≠ FAIR
- Computational systems must be able to find, access, interoperate, reuse

**Self-validation before Pass 7:**
- Format validity (DOI, ORCID, URL patterns)
- Completeness (all sections examined, all metrics calculated)
- Cross-checks (author counts, statement consistency)

**Your goal:** Systematic infrastructure capture enabling comprehensive reproducibility assessment in Pass 7.
