# Reproducibility Infrastructure Schema Proposal v2.0

**Date**: 2025-11-03
**Version**: 2.0 (Updated with PIDs, Permits, FAIR Assessment)
**Purpose**: Define schema and extraction approach for capturing extrinsic reproducibility markers from research papers

**Updates in v2.0**:
- Added comprehensive Persistent Identifier (PID) tracking (DOI, ORCID, RAiD, IGSN)
- Added Permits and Authorizations section (fieldwork-specific)
- Added FAIR Assessment framework
- Updated to Pass 6 numbering (infrastructure extraction before validation)

---

## Executive Summary

**Problem**: Current CEM+RDMAP extractions (Passes 0-5) focus on *intrinsic research content* (claims, evidence, methods) but miss *extrinsic reproducibility infrastructure* (PIDs, repositories, funding, permits, etc.).

**Evidence**: Infrastructure scans of three papers found zero actual reproducibility markers:
- Connor et al 2013: 4 false positives (metadata fields only)
- Eftimoski et al 2017: 12 false positives (metadata fields only)
- Penske et al 2023: 5 false positives (metadata fields only)

**Solution**: Add dedicated infrastructure extraction (**Pass 6**) to capture extrinsic markers from paper metadata, acknowledgements, data availability statements, author contribution sections, and supplementary materials.

**New in v2.0**: Integration of FAIR principles and PID graph framework (see `docs/background-research/FAIR_and_PIDs_for_HASS_reproducibility.md` for detailed research).

---

## Proposed Schema: Reproducibility Infrastructure

### Top-Level Structure

Add new top-level field `reproducibility_infrastructure` to `extraction.json`:

```json
{
  "paper_metadata": { ... },
  "evidence": [ ... ],
  "claims": [ ... ],
  "methods": [ ... ],
  "protocols": [ ... ],
  "research_designs": [ ... ],
  "reproducibility_infrastructure": {
    "persistent_identifiers": { ... },
    "funding": [ ... ],
    "data_availability": { ... },
    "code_availability": { ... },
    "author_contributions": [ ... ],
    "conflicts_of_interest": { ... },
    "ethics_approval": { ... },
    "permits_and_authorizations": { ... },
    "preregistration": { ... },
    "supplementary_materials": [ ... ],
    "references_completeness": { ... },
    "fair_assessment": { ... },
    "extraction_metadata": { ... }
  }
}
```

---

## Field Definitions

### 1. Persistent Identifiers (PIDs)

**Purpose**: Capture PIDs for all research objects to assess FAIR compliance and PID graph completeness.

**Foundation**: See FAIR Principles F1 - globally unique and persistent identifiers enable findability.

```json
"persistent_identifiers": {
  "paper_doi": {
    "doi": "10.1234/example",
    "resolves": true,
    "url": "https://doi.org/10.1234/example",
    "verified_date": "2025-11-03"
  },

  "author_orcids": [
    {
      "author_name": "Connor, S.",
      "author_position": "first",
      "orcid": "0000-0002-1234-5678",
      "orcid_url": "https://orcid.org/0000-0002-1234-5678",
      "profile_active": true,
      "verified_date": "2025-11-03"
    },
    {
      "author_name": "Thomas, I.",
      "author_position": "second",
      "orcid": "0000-0002-8765-4321",
      "orcid_url": "https://orcid.org/0000-0002-8765-4321",
      "profile_active": true,
      "verified_date": "2025-11-03"
    }
  ],
  "orcid_coverage": {
    "authors_with_orcid": 2,
    "total_authors": 5,
    "coverage_percentage": 40,
    "coverage_category": "partial"
  },

  "dataset_pids": [
    {
      "pid_id": "DPID001",
      "pid_type": "doi",
      "pid_value": "10.5281/zenodo.1234567",
      "pid_url": "https://doi.org/10.5281/zenodo.1234567",
      "resolves": true,
      "repository": "Zenodo",
      "dataset_description": "Raw survey data and site coordinates",
      "linked_in_paper": {
        "section": "Data Availability Statement",
        "page": 16
      },
      "verified_date": "2025-11-03"
    },
    {
      "pid_id": "DPID002",
      "pid_type": "accession",
      "pid_value": "PRJEB12345",
      "pid_url": "https://www.ebi.ac.uk/ena/browser/view/PRJEB12345",
      "resolves": true,
      "repository": "European Nucleotide Archive",
      "dataset_description": "Raw sequencing data",
      "linked_in_paper": {
        "section": "Data Availability Statement",
        "page": 16
      }
    }
  ],

  "software_pids": [
    {
      "pid_id": "SPID001",
      "pid_type": "doi",
      "pid_value": "10.5281/zenodo.7654321",
      "pid_url": "https://doi.org/10.5281/zenodo.7654321",
      "resolves": true,
      "repository": "Zenodo",
      "software_name": "aDNA-analysis-pipeline",
      "version": "v1.2.0",
      "github_url": "https://github.com/lab-name/adna-pipeline",
      "archived_snapshot": true,
      "linked_in_paper": {
        "section": "Methods",
        "page": 5
      }
    }
  ],

  "sample_pids": [
    {
      "pid_id": "SAMPID001",
      "pid_type": "igsn",
      "pid_value": "IEAU12345",
      "pid_url": "http://igsn.org/IEAU12345",
      "resolves": true,
      "sample_type": "sediment_core",
      "sample_description": "Lake sediment core from Lake Keilambete",
      "repository": "National Lacustrine Core Facility",
      "repository_location": "Australian National University",
      "linked_in_paper": {
        "section": "Methods",
        "page": 4
      }
    }
  ],

  "project_pid": {
    "pid_type": "raid",
    "pid_value": "10.1234/raid.5678",
    "pid_url": "https://raid.org/10.1234/raid.5678",
    "resolves": true,
    "project_name": "Holocene Climate Variability in Southeast Australia",
    "linked_in_paper": {
      "section": "Acknowledgements",
      "page": 15
    }
  },

  "vocabulary_pids": [
    {
      "pid_id": "VPID001",
      "pid_type": "doi",
      "pid_value": "10.5281/zenodo.periodo",
      "vocabulary_name": "PeriodO",
      "vocabulary_purpose": "chronological_framework",
      "linked_in_paper": {
        "section": "Methods",
        "page": 6
      }
    }
  ],

  "pid_graph_summary": {
    "paper_has_doi": true,
    "authors_have_orcids": "partial",
    "datasets_have_pids": true,
    "software_has_pids": true,
    "samples_have_pids": false,
    "project_has_pid": false,
    "vocabularies_have_pids": false,
    "connectivity_score": 4,
    "connectivity_rating": "moderate"
  }
}
```

**Fields**:
- **paper_doi**: Paper's DOI (should always be present for modern papers)
- **author_orcids**: Array of ORCID identifiers for authors
  - Track coverage: how many authors have ORCIDs vs total
  - Categories: `none`, `corresponding_only`, `partial`, `all`
- **dataset_pids**: DOIs, accession numbers, persistent URLs for datasets
- **software_pids**: DOIs for software/code (Zenodo, Software Heritage)
- **sample_pids**: IGSNs or DOIs for physical samples
- **project_pid**: RAiD for research project/activity
- **vocabulary_pids**: DOIs for controlled vocabularies, gazetteers, ontologies
- **pid_graph_summary**: Completeness assessment (connectivity score 0-6)

**PID Types**:
- `doi`: Digital Object Identifier
- `orcid`: Open Researcher and Contributor ID
- `raid`: Research Activity Identifier
- `igsn`: International Generic Sample Number
- `accession`: Repository accession number (GenBank, ENA, etc.)
- `url`: Non-PID URL (note as lower FAIR quality)

**Connectivity Score** (0-6):
- +1 for paper DOI
- +1 for authors with ORCIDs (any)
- +1 for dataset PIDs
- +1 for software PIDs
- +1 for sample PIDs
- +1 for project PID or vocabulary PIDs

---

### 2. Funding

Capture funding sources, grant numbers, and acknowledgements.

```json
"funding": [
  {
    "funder_id": "FND001",
    "funder_name": "Australian Research Council",
    "grant_number": "DP0878543",
    "grant_type": "Discovery Project",
    "recipients": ["Connor, S.", "Thomas, I."],
    "verbatim_text": "This research was funded by Australian Research Council Discovery Project grant DP0878543 to SC and IT.",
    "location": {
      "section": "Acknowledgements",
      "page": 15,
      "text_span": [1245, 1389]
    },
    "structured_metadata": {
      "funder_ror": "https://ror.org/05mmh0f86",
      "funder_ror_name": "Australian Research Council",
      "grant_doi": null,
      "funder_jurisdiction": "Australia"
    }
  }
]
```

**Fields**:
- `funder_id`: Unique identifier within extraction
- `funder_name`: Organisation name as stated in paper
- `grant_number`: Grant/award number if provided
- `grant_type`: Type of funding (grant, fellowship, studentship, consortium, etc.)
- `recipients`: Named investigators if specified
- `verbatim_text`: Exact funding acknowledgement text
- `location`: Where in paper this appears
- `structured_metadata`: Optional linked identifiers
  - `funder_ror`: Research Organisation Registry ID (if available)
  - `grant_doi`: Grant DOI (rare but emerging)
  - `funder_jurisdiction`: Country/region

---

### 3. Data Availability

Capture data repository links, access conditions, and availability statements.

```json
"data_availability": {
  "statement_present": true,
  "statement_type": "available_with_restrictions",
  "verbatim_statement": "Raw sequencing data are available through the European Nucleotide Archive under accession PRJEB12345. Site location data are available from the corresponding author upon reasonable request, subject to permission from Traditional Owners.",
  "repositories": [
    {
      "repository_id": "REPO001",
      "repository_name": "European Nucleotide Archive",
      "repository_type": "domain_specific",
      "accession_number": "PRJEB12345",
      "persistent_identifier": "https://www.ebi.ac.uk/ena/browser/view/PRJEB12345",
      "persistent_identifier_type": "accession",
      "data_type": "raw_sequencing_data",
      "access_conditions": "open",
      "licence": "CC0",
      "machine_readable": true,
      "api_access": true
    },
    {
      "repository_id": "REPO002",
      "repository_name": "Upon reasonable request",
      "repository_type": "author_contact",
      "data_type": "site_coordinates",
      "access_conditions": "restricted",
      "access_justification": "requires_permission_traditional_owners",
      "ethical_considerations": "CARE_principles_applied",
      "machine_readable": false
    }
  ],
  "location": {
    "section": "Data Availability Statement",
    "page": 16
  }
}
```

**Fields**:
- `statement_present`: Boolean
- `statement_type`: `fully_available` | `available_with_restrictions` | `upon_request` | `not_available` | `not_stated`
- `repositories`: Array of repository entries
  - `repository_type`: `institutional` | `domain_specific` | `general` | `author_contact` | `project_website`
  - `persistent_identifier_type`: `doi` | `accession` | `url` | `none`
  - `access_conditions`: `open` | `restricted` | `embargoed` | `closed`
  - `licence`: Data licence if stated (CC0, CC-BY, etc.)
  - `machine_readable`: Boolean (API, structured export vs PDF only)
  - `api_access`: Boolean (programmatic access available)
  - `ethical_considerations`: CARE principles, Indigenous data sovereignty, human subjects protection

**FAIR Note**: Restricted access with ethical justification (CARE principles) is FAIR-compliant (A1.2).

---

### 4. Code Availability

Capture software, analysis scripts, and computational reproducibility resources.

```json
"code_availability": {
  "statement_present": true,
  "statement_type": "available_open",
  "verbatim_statement": "Analysis code is available at https://github.com/lab-name/project-name (DOI: 10.5281/zenodo.1234567). Code is provided under MIT licence.",
  "repositories": [
    {
      "repository_id": "CODE001",
      "repository_type": "github",
      "repository_name": "GitHub",
      "url": "https://github.com/lab-name/project-name",
      "persistent_identifier": "https://doi.org/10.5281/zenodo.1234567",
      "persistent_identifier_type": "doi",
      "licence": "MIT",
      "licence_machine_readable": true,
      "executable": true,
      "environment_specified": true,
      "language": "R",
      "version": "v1.2.0",
      "dependencies_documented": true,
      "archived_snapshot": true,
      "snapshot_date": "2023-05-15"
    }
  ],
  "software_tools": [
    {
      "tool_id": "SW001",
      "tool_name": "OxCal",
      "version": "4.4",
      "purpose": "Bayesian radiocarbon calibration",
      "url": "https://c14.arch.ox.ac.uk/oxcal.html",
      "citation": "Bronk Ramsey, C., 2009. Bayesian analysis of radiocarbon dates. Radiocarbon 51(1), 337-360.",
      "persistent_identifier": null,
      "persistent_identifier_type": null
    }
  ],
  "computational_reproducibility": {
    "level": "code_dependencies",
    "level_rationale": "R scripts provided with renv.lock specifying exact package versions. No container but dependencies fully specified. Random seeds documented in scripts.",
    "environment_specification": {
      "type": "lock_file",
      "files_present": ["analysis.R", "renv.lock", "README.md"],
      "platform_specified": true,
      "platform_details": "R 4.3.1 on Ubuntu 22.04"
    },
    "analysis_transparency": {
      "random_seeds_documented": true,
      "random_seed_values": ["set.seed(42) for bootstrapping", "set.seed(123) for Monte Carlo"],
      "parameters_documented": true,
      "parameter_details": "MCMC: 100,000 iterations, burn-in 10,000, thinning 10",
      "workflow_specified": true,
      "workflow_description": "README describes 5-step analysis pipeline with script execution order",
      "alternative_analyses_considered": true,
      "alternative_analyses_description": "Supplementary materials report sensitivity analysis with alternative priors"
    }
  },
  "location": {
    "section": "Code Availability Statement",
    "page": 16
  }
}
```

**Fields**:
- `statement_present`: Boolean
- `statement_type`: `available_open` | `upon_request` | `proprietary` | `not_available` | `not_stated`
- `repositories`: Analysis code repositories
  - `executable`: Can code be run as-is?
  - `environment_specified`: Dependencies/environment documented (Dockerfile, requirements.txt)?
  - `archived_snapshot`: Zenodo/Software Heritage snapshot vs live GitHub only
- `software_tools`: Non-code software used (GIS, statistical packages, domain tools)
  - Track whether tools have PIDs (DOIs, citations)
- `computational_reproducibility`: **NEW** - Assesses depth of computational reproducibility
  - `level`: Reproducibility spectrum level (see below)
  - `level_rationale`: Explanation of level assessment
  - `environment_specification`: Type and details of environment documentation
  - `analysis_transparency`: Random seeds, parameters, workflow, alternative analyses

**Computational Reproducibility Levels** (based on FAIR4RS principles):
- `none`: No code shared
- `code_only`: Scripts shared but no dependency/environment specification
- `code_dependencies`: Scripts + dependency specification (requirements.txt, renv.lock)
- `containerised`: Scripts + complete computational environment (Docker, Singularity)
- `fully_reproducible`: Complete pipeline with data + code + container + workflow orchestration

**FAIR Note**: Live GitHub link without archived snapshot = lower FAIR score (not persistent).

**FAIR4RS Note**: Computational reproducibility level directly affects Reusable (R) dimension scoring. Containerised environments score higher than dependency files alone.

---

### 5. Author Contributions

Capture CReDIT statements or narrative contribution descriptions.

```json
"author_contributions": {
  "statement_present": true,
  "format": "credit_taxonomy",
  "verbatim_statement": "S.C.: Conceptualisation, Methodology, Investigation, Writing – Original Draft. I.T.: Funding acquisition, Resources, Writing – Review & Editing. A.B.: Formal Analysis, Visualisation.",
  "contributions": [
    {
      "author": "Connor, S.",
      "orcid": "0000-0002-1234-5678",
      "roles": [
        "Conceptualisation",
        "Methodology",
        "Investigation",
        "Writing – Original Draft"
      ]
    },
    {
      "author": "Thomas, I.",
      "orcid": "0000-0002-8765-4321",
      "roles": [
        "Funding acquisition",
        "Resources",
        "Writing – Review & Editing"
      ]
    },
    {
      "author": "Brown, A.",
      "orcid": null,
      "roles": [
        "Formal Analysis",
        "Visualisation"
      ]
    }
  ],
  "location": {
    "section": "Author Contributions",
    "page": 16
  }
}
```

**Fields**:
- `format`: `credit_taxonomy` | `narrative` | `equal_contribution` | `not_stated`
- `contributions`: Parsed contribution list (if structured format used)
- Link to ORCIDs if available (cross-reference with `persistent_identifiers.author_orcids`)

**CReDIT Taxonomy** (14 roles):
Conceptualisation, Methodology, Software, Validation, Formal Analysis, Investigation, Resources, Data Curation, Writing – Original Draft, Writing – Review & Editing, Visualisation, Supervision, Project Administration, Funding Acquisition

---

### 6. Conflicts of Interest

Capture COI declarations.

```json
"conflicts_of_interest": {
  "statement_present": true,
  "declaration": "none_declared",
  "verbatim_statement": "The authors declare no competing interests.",
  "conflicts": [],
  "location": {
    "section": "Competing Interests",
    "page": 16
  }
}
```

**Fields**:
- `declaration`: `none_declared` | `conflicts_declared` | `not_stated`
- `conflicts`: Array of specific conflicts if any

---

### 7. Ethics Approval

Capture ethics committee approvals, informed consent, and human/Indigenous research protocols.

```json
"ethics_approval": {
  "statement_present": true,
  "approval_type": "institutional_and_community",
  "verbatim_statement": "Research was approved by University Human Research Ethics Committee (HREC 2018/123) and conducted with permission from Gunditjmara Traditional Owners Aboriginal Corporation under research agreement dated 15 March 2018.",
  "approvals": [
    {
      "approval_id": "ETH001",
      "ethics_body": "University Human Research Ethics Committee",
      "approval_number": "HREC 2018/123",
      "approval_date": null,
      "jurisdiction": "Australia",
      "approval_type": "human_research"
    },
    {
      "approval_id": "ETH002",
      "ethics_body": "Gunditjmara Traditional Owners Aboriginal Corporation",
      "approval_type": "indigenous_community_consent",
      "agreement_date": "2018-03-15",
      "care_principles": true,
      "notes": "Community research agreement"
    }
  ],
  "informed_consent": "obtained",
  "location": {
    "section": "Ethics",
    "page": 2
  }
}
```

**Fields**:
- `approval_type`: `institutional` | `community` | `institutional_and_community` | `not_required` | `not_stated`
- `approvals`: Array of ethics approvals
  - `approval_type`: `human_research` | `indigenous_community_consent` | `animal_research` | `environmental`
- `informed_consent`: `obtained` | `not_required` | `not_stated`
- `care_principles`: Boolean for Indigenous data protocols

**CARE Principles**: Collective benefit, Authority to control, Responsibility, Ethics

---

### 8. Permits and Authorisations

**NEW IN v2.0**: Fieldwork-specific permits and authorisations.

**Purpose**: Capture regulatory compliance and ethical practice for fieldwork (archaeology, ecology, geography, anthropology).

```json
"permits_and_authorizations": {
  "statement_present": true,
  "permits": [
    {
      "permit_id": "PERM001",
      "permit_type": "excavation_permit",
      "issuing_authority": "New South Wales Heritage Council",
      "permit_number": "NSW-ARCH-2018-045",
      "jurisdiction": "New South Wales, Australia",
      "validity_period": {
        "start_date": "2018-06-01",
        "end_date": "2021-05-31"
      },
      "verbatim_text": "Excavation conducted under NSW Heritage Council permit NSW-ARCH-2018-045.",
      "location": {
        "section": "Acknowledgements",
        "page": 15
      }
    },
    {
      "permit_id": "PERM002",
      "permit_type": "land_access_agreement",
      "issuing_authority": "Gunditjmara Traditional Owners Aboriginal Corporation",
      "agreement_type": "community_research_agreement",
      "date_signed": "2018-03-15",
      "care_principles_applied": true,
      "verbatim_text": "Fieldwork conducted with permission and support from Gunditjmara Traditional Owners Aboriginal Corporation under research agreement dated 15 March 2018.",
      "location": {
        "section": "Acknowledgements",
        "page": 15
      },
      "notes": "Demonstrates Authority to Control (CARE principle)"
    },
    {
      "permit_id": "PERM003",
      "permit_type": "sampling_permit",
      "issuing_authority": "Parks Victoria",
      "permit_number": "10008234",
      "jurisdiction": "Victoria, Australia",
      "purpose": "sediment_coring",
      "location_description": "Lake Surprise, Grampians National Park",
      "verbatim_text": "Sediment coring conducted under Parks Victoria research permit 10008234.",
      "location": {
        "section": "Methods",
        "page": 5
      }
    },
    {
      "permit_id": "PERM004",
      "permit_type": "export_permit",
      "issuing_authority": "Department of Agriculture, Water and the Environment",
      "permit_number": "PWS-2018-AU-001234",
      "jurisdiction": "Australia (federal)",
      "purpose": "export_biological_samples",
      "destination_country": "United Kingdom",
      "verbatim_text": "Samples exported under CITES permit PWS-2018-AU-001234.",
      "location": {
        "section": "Methods",
        "page": 6
      }
    }
  ],
  "location": {
    "section": "Multiple",
    "notes": "Permits mentioned in Acknowledgements and Methods sections"
  }
}
```

**Permit Types** (common in HASS fieldwork):
- `excavation_permit`: Archaeological/palaeontological excavation
- `sampling_permit`: Environmental sampling (sediment, water, biological)
- `land_access_agreement`: Permission to access private/traditional lands
- `heritage_consent`: Work near/on heritage sites
- `export_permit`: Remove samples from country (CITES, biosecurity)
- `import_permit`: Bring samples into country
- `collection_permit`: Museum/repository access
- `survey_permit`: Non-destructive survey work
- `diving_permit`: Underwater archaeology/research
- `protected_area_permit`: Research in national parks, reserves

**Fields**:
- `permit_id`: Unique identifier within extraction
- `permit_type`: Type of permit/authorisation
- `issuing_authority`: Government agency, Traditional Owners, land manager
- `permit_number`: Official permit number if provided
- `jurisdiction`: Geographic/political jurisdiction
- `validity_period`: Permit dates if specified
- `care_principles_applied`: Boolean for Indigenous agreements
- `verbatim_text`: Exact text from paper
- `location`: Where mentioned in paper

**Transparency Implications**:
- Proper permitting demonstrates:
  - Regulatory compliance
  - Ethical practice
  - Respect for jurisdictions and communities
  - Methodological legitimacy
- Particularly critical for:
  - Indigenous lands (CARE principles)
  - Protected areas (environmental compliance)
  - Heritage sites (cultural heritage protection)
  - Cross-border research (international agreements)

---

### 9. Preregistration

Capture preregistration links and registered reports.

```json
"preregistration": {
  "preregistered": false,
  "registered_report": false,
  "registrations": [],
  "notes": "Preregistration not common in palaeoecological research",
  "location": null
}
```

**Fields**:
- `preregistered`: Boolean
- `registered_report`: Boolean (published as registered report?)
- `registrations`: Array of registration links (OSF, AsPredicted, clinicaltrials.gov, etc.)

**HASS Note**: Preregistration rare in archaeology/palaeoecology (exploratory/inductive research); more common in experimental psychology, clinical research.

---

### 10. Supplementary Materials

Capture supplementary information files, appendices, and extended data.

```json
"supplementary_materials": {
  "present": true,
  "materials": [
    {
      "material_id": "SUPP001",
      "title": "Supplementary Information",
      "type": "document",
      "description": "Additional methods, figures S1-S15, tables S1-S8",
      "format": "PDF",
      "pages": 45,
      "persistent_identifier": null,
      "persistent_identifier_type": null,
      "machine_readable": false
    },
    {
      "material_id": "SUPP002",
      "title": "Supplementary Data 1",
      "type": "data",
      "description": "Radiocarbon date calibration outputs",
      "format": "XLSX",
      "persistent_identifier": "https://doi.org/10.1234/supplementary.data.1",
      "persistent_identifier_type": "doi",
      "machine_readable": true
    },
    {
      "material_id": "SUPP003",
      "title": "Supplementary Code 1",
      "type": "code",
      "description": "R scripts for statistical analyses",
      "format": "R",
      "persistent_identifier": "https://github.com/lab-name/project-name/tree/main/supplementary-analyses",
      "persistent_identifier_type": "url",
      "machine_readable": true,
      "archived_snapshot": false
    }
  ]
}
```

**Fields**:
- `present`: Boolean
- `materials`: Array of supplementary items
  - `type`: `document` | `data` | `code` | `video` | `interactive` | `appendix`
  - `machine_readable`: Boolean (structured data vs PDF images)
  - `archived_snapshot`: Boolean (for code supplements)

---

### 11. References Completeness

Assess whether all in-text citations appear in bibliography.

```json
"references_completeness": {
  "assessed": true,
  "complete": true,
  "in_text_citations_count": 156,
  "bibliography_entries_count": 156,
  "missing_references": [],
  "notes": "All in-text citations matched to bibliography entries. No orphaned citations detected."
}
```

**Fields**:
- `assessed`: Boolean (was this checked?)
- `complete`: Boolean
- `missing_references`: Array of citations found in text but not in bibliography

**Note**: This may be difficult to assess from extracted text; consider low priority.

---

### 12. FAIR Assessment

**NEW IN v2.0**: Structured FAIR compliance assessment based on infrastructure extraction.

**Foundation**: See `docs/background-research/FAIR_and_PIDs_for_HASS_reproducibility.md` for complete framework.

```json
"fair_assessment": {
  "assessed": true,
  "assessment_date": "2025-11-03",
  "assessor": "claude-sonnet-4-5",
  "publication_year": 2023,
  "discipline": "palaeoecology",

  "findable": {
    "score": 3,
    "max_score": 4,
    "rationale": "Paper DOI + all author ORCIDs + dataset DOIs present. No sample or project PIDs.",
    "criteria_met": [
      "F1: Paper has persistent identifier (DOI)",
      "F1: All authors have ORCIDs",
      "F1: Datasets have persistent identifiers",
      "F4: Datasets registered in searchable repositories"
    ],
    "criteria_not_met": [
      "F1: Physical samples lack PIDs (IGSNs)",
      "F2: Metadata richness variable across repositories"
    ]
  },

  "accessible": {
    "score": 4,
    "max_score": 4,
    "rationale": "All PIDs resolve. Data in Zenodo with open CC-BY licence. Code in GitHub + Zenodo archived snapshot. Restricted site coordinate data with ethical justification (CARE-compliant).",
    "criteria_met": [
      "A1: Data retrievable via persistent identifier",
      "A1.1: Protocol open and free (HTTPS)",
      "A1.2: Restricted access properly justified (Indigenous data)",
      "A2: Metadata accessible even if data removed"
    ],
    "criteria_not_met": []
  },

  "interoperable": {
    "score": 3,
    "max_score": 4,
    "rationale": "Data in CSV format with schema documentation. No API access. Vocabulary used (PeriodO) has DOI. Some supplementary data in PDF (not machine-readable).",
    "criteria_met": [
      "I1: Structured data format (CSV, JSON)",
      "I2: Controlled vocabulary with PID (PeriodO)",
      "I3: Qualified references to related datasets"
    ],
    "criteria_not_met": [
      "I1: No API for programmatic access",
      "I1: Some data in PDF format (not machine-actionable)"
    ]
  },

  "reusable": {
    "score": 4,
    "max_score": 4,
    "rationale": "Machine-readable licence (CC-BY-4.0 via SPDX). Rich metadata in DataCite schema. Provenance documented. Follows community standards (ARIADNEplus recommended practices).",
    "criteria_met": [
      "R1: Rich metadata describing data",
      "R1.1: Clear machine-readable licence (SPDX: CC-BY-4.0)",
      "R1.2: Detailed provenance (methods, software versions)",
      "R1.3: Domain-relevant standards (ARIADNEplus)"
    ],
    "criteria_not_met": []
  },

  "total_fair_score": 14,
  "max_total_score": 16,
  "fair_percentage": 87.5,
  "fair_rating": "highly_fair",

  "machine_actionability": {
    "rating": "high",
    "rationale": "Data downloadable via structured API, metadata in machine-readable format (JSON-LD), licence SPDX-compliant, controlled vocabularies with PIDs.",
    "human_readable_only": false,
    "machine_readable_metadata": true,
    "structured_data_format": true,
    "api_access": true,
    "typed_relationships": true
  },

  "pid_graph_completeness": {
    "connectivity_score": 4,
    "max_connectivity_score": 6,
    "rating": "moderate",
    "rationale": "Paper + authors + datasets + software have PIDs. Missing: sample PIDs (IGSN), project RAiD.",
    "components_with_pids": [
      "paper",
      "authors",
      "datasets",
      "software"
    ],
    "components_without_pids": [
      "samples",
      "project"
    ]
  },

  "discipline_context": {
    "fair_expectations_by_year": "high",
    "rationale": "Paper published 2023; FAIR principles well-established (2016). Archaeology/palaeoecology increasingly adopting FAIR practices.",
    "discipline_baseline": "ORCID adoption ~20-30% in HASS (2024 data); this paper exceeds baseline with 100% coverage.",
    "care_principles_relevant": true,
    "care_principles_applied": true
  },

  "recommendations": [
    "Consider registering physical samples with IGSNs for improved traceability",
    "Register research project with RAiD to complete PID graph",
    "Provide API access to datasets for full machine-actionability",
    "Convert PDF supplementary materials to machine-readable formats (CSV, JSON)"
  ]
}
```

**FAIR Rating Scale**:
- **0-4**: Not FAIR
- **5-8**: Minimally FAIR
- **9-12**: Moderately FAIR
- **13-16**: Highly FAIR

**Scoring Rationale**:
Each FAIR dimension scored 0-4:
- **0**: No compliance
- **1**: Minimal compliance (e.g., data "available upon request")
- **2**: Partial compliance (e.g., data in repository but no PID)
- **3**: Good compliance (e.g., data with PID, some machine-readability)
- **4**: Exemplary compliance (e.g., full machine-actionability, rich metadata, community standards)

**Context-Dependent Assessment**:
- Publication year matters: Pre-2016 papers not expected to be FAIR
- Discipline matters: HASS lags natural sciences in PID adoption
- Research type matters: Exploratory vs confirmatory, field vs computational
- Ethical restrictions: CARE-compliant restrictions = POSITIVE signal, not penalty

---

### 13. Extraction Metadata

Standard metadata for Pass 6.

```json
"extraction_metadata": {
  "extraction_timestamp": "2025-11-03T10:30:00Z",
  "extractor_model": "claude-sonnet-4-5",
  "extraction_pass": "pass_6_infrastructure",
  "schema_version": "2.0",
  "sections_examined": [
    "Front matter (title page, author affiliations)",
    "Abstract",
    "Acknowledgements",
    "Data Availability Statement",
    "Code Availability Statement",
    "Author Contributions",
    "Competing Interests",
    "Ethics Statement",
    "Supplementary Information"
  ],
  "validation_performed": true,
  "validation_notes": "All PIDs verified to resolve. ORCID profiles checked for activity. FAIR assessment completed.",
  "notes": "Paper demonstrates exemplary data sharing practices with domain-specific repository (ENA), Zenodo archive, and ethically appropriate restricted access for sensitive cultural site data (CARE-compliant)."
}
```

---

## Implementation Approach

### Pass Numbering Update

**Original proposal**: Pass 7 for infrastructure
**Updated**: Pass 6 for infrastructure (before comprehensive validation)

**New workflow**:
```
Pass 0: Section identification + planning
Pass 1: Evidence extraction
Pass 2: Claims extraction + rationalization
Pass 3: Methods extraction
Pass 4: Protocols extraction
Pass 5: Research designs extraction
Pass 6: Infrastructure extraction ← THIS PASS
Pass 7: Comprehensive validation (relationships + infrastructure)
```

**Rationale**: Infrastructure is independent of research content relationships; extract early. Pass 7 can validate both content relationships AND infrastructure PIDs/FAIR compliance.

---

## Self-Validation Checklist (Built into Pass 6)

After extraction, verify:

### Format Validity
- [ ] DOIs start with "10." (if present)
- [ ] ORCIDs follow format "0000-0000-0000-000X" (if present)
- [ ] URLs use https:// (if present)
- [ ] RAiDs are DOI-based (if present)
- [ ] IGSNs follow expected alphanumeric format (if present)

### Completeness
- [ ] All infrastructure sections examined (even if "not present")
- [ ] `extraction_metadata.sections_examined` lists all checked sections
- [ ] All identified PIDs have resolver URLs recorded
- [ ] PID graph summary completed
- [ ] FAIR assessment completed (all four dimensions scored)

### Cross-Checks
- [ ] Author count matches between `paper_metadata` and `author_contributions`
- [ ] ORCID list matches author list
- [ ] Funding acknowledgements consistent with `funding` array
- [ ] Data Availability Statement matches `repositories` array
- [ ] Permits mentioned in Methods cross-referenced with `permits_and_authorizations`

### PID Verification (Optional – can be automated post-extraction)
- [ ] Paper DOI resolves
- [ ] ORCIDs resolve to active profiles
- [ ] Dataset DOIs resolve
- [ ] Software DOIs resolve
- [ ] Sample PIDs resolve (if present)

Report any issues in `extraction_metadata.validation_notes`.

---

## Connection to repliCATS Seven Signals

### Direct Mapping

| repliCATS Signal | Infrastructure Support | Schema Fields Used |
|------------------|----------------------|-------------------|
| **Transparency** | **PRIMARY** | All fields; especially PIDs, data/code availability, funding, permits |
| **Replicability (Analytic)** | **PRIMARY** | Code availability, executable environment, data PIDs, software PIDs |
| **Validity** | **MODERATE** | Sample PIDs (traceability), ethics approval, permits (procedural validity) |
| **Robustness** | **MODERATE** | Supplementary materials, sensitivity analyses archived |
| **Generalisability** | **MINIMAL** | Data availability enables reanalysis in new contexts |
| **Comprehensibility** | **MINIMAL** | Rich metadata (FAIR R1) supports understanding |
| **Plausibility** | **MINIMAL** | Vocabulary PIDs aid checks (standardised terminology) |

### Transparency Signal Enhancement

**Formula**: Transparency = Intrinsic Transparency (method documentation) + Extrinsic Transparency (infrastructure)

| Intrinsic | Infrastructure | Overall Transparency |
|-----------|----------------|---------------------|
| High | High FAIR (13-16) | **EXEMPLARY** |
| High | Moderate FAIR (9-12) | **GOOD** |
| High | Low FAIR (5-8) | **MODERATE** (well-documented but not FAIR) |
| Low | High FAIR (13-16) | **MODERATE** (FAIR but opaque) |
| Low | Low FAIR (0-8) | **POOR** |

---

## Migration Strategy for Existing Extractions

### Option 1: Full Re-extraction (Recommended)

Run Pass 6 on all 10 pilot papers:
- Connor et al 2013
- Eftimoski et al 2017
- Penske et al 2023
- Ross 2005
- Ross-Ballsun-Stanton 2022
- Ross et al 2009
- Sobotkova et al 2016, 2021, 2023, 2024

**Estimated time**: 5-10 minutes per paper = 50-100 minutes total

**Advantages**:
- ✅ Consistent schema across all papers
- ✅ Creates clean baseline
- ✅ Enables cross-paper FAIR comparison

### Option 2: Selective Re-extraction

Run Pass 6 only on papers likely to have infrastructure:
- Penske et al 2023 (most recent)
- Sobotkova et al 2024, 2023, 2021
- Eftimoski et al 2017

**Estimated time**: 5 papers × 10 minutes = 50 minutes

**Advantages**:
- ⚠️ Saves time but creates inconsistency

**Recommendation**: Option 1 (full re-extraction) — time cost is minimal for long-term value.

---

## Priority Recommendations

### Phase 1: Core Implementation (Immediate)

**Must-have for all papers**:
1. Paper DOI
2. Author ORCIDs (all authors)
3. Dataset DOIs/URLs
4. Code repository DOIs/URLs
5. Funding information
6. Permits (if fieldwork paper)
7. Basic FAIR assessment (scores 0-4 per dimension)

**Estimated time**: 10 minutes per paper

### Phase 2: Enhanced Assessment (Near-term)

**After core extraction**:
1. PID resolution checks (automated)
2. Machine-actionability assessment
3. PID graph completeness
4. Detailed FAIR scoring rationale

**Estimated time**: Additional 5 minutes per paper (manual) or <1 minute (if automated)

### Phase 3: Emerging PIDs (Future)

**Monitor for adoption**:
1. RAiD (expect uptake 2026-2028)
2. IGSN (relevant for palaeoecology/geoarchaeology)
3. Vocabulary DOIs (PeriodO, Pleiades, AAT)
4. Software Heritage PIDs

**Strategy**: Note if present; don't penalise absence until critical mass adoption

---

## Open Questions for User

### 1. Scope Confirmation

Is the v2.0 schema appropriate? Consider:
- **Add**: Sample repositories (museum collections), material archiving beyond IGSN
- **Keep**: All 13 sections as proposed
- **Remove**: Preregistration (very rare in HASS), References completeness (hard to assess)

### 2. FAIR Assessment Depth

Should Pass 6 include:
- **Option A**: Lightweight self-assessment (check PIDs present, basic scoring)
- **Option B**: Detailed FAIR assessment with full rationale (as shown in schema)
- **Option C**: Defer FAIR assessment to Pass 7 validation

**Recommendation**: Option A for Pass 6, with Pass 7 adding detailed validation

### 3. PID Verification

Should Pass 6:
- **Option A**: Extract PIDs only; verify in Pass 7
- **Option B**: Extract + verify (check resolution) in Pass 6
- **Option C**: Extract in Pass 6; automated post-processing script verifies

**Recommendation**: Option C (separation of concerns, enables batch verification)

### 4. Assessment Philosophy

Confirm approach:
- **Descriptive + context-dependent normative** ✓
- Adjust expectations by publication year, discipline, research type ✓
- CARE-compliant restrictions = POSITIVE signal ✓
- PID graph completeness as key metric ✓

---

## Next Steps

1. ✅ Infrastructure scans complete (Connor, Eftimoski, Penske)
2. ✅ FAIR research complete (`docs/background-research/FAIR_and_PIDs_for_HASS_reproducibility.md`)
3. ✅ Schema v2.0 complete (this document)
4. **User confirmation**: Schema appropriate? Any additions/changes?
5. **Draft Pass 6 prompt**: Infrastructure extraction with lightweight self-validation
6. **Test Pass 6**: Run on Penske et al 2023 (most recent paper, likely best infrastructure)
7. **Validate schema**: Adjust based on test results
8. **Batch extraction**: Run Pass 6 on all 10 pilot papers
9. **Update workflow**: Modify WORKFLOW.md, update Pass 7 validation to include infrastructure

---

## Conclusion

Schema v2.0 provides comprehensive infrastructure extraction framework supporting:

1. **FAIR assessment**: 15 principles mapped to extractable infrastructure
2. **PID graphs**: Complete tracking of research object identifiers
3. **Transparency**: Funding, permits, ethics, COI, contributions
4. **Replicability**: Data/code availability with machine-actionability checks
5. **Context-awareness**: Discipline, publication year, research type, CARE principles

**Ready for prompt development**: Schema complete pending user confirmation.

---

**Document Status**: Schema v2.0 complete; awaiting user feedback before prompt development.
