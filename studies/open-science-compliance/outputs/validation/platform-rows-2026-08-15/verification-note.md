# Platform-table row verification — dated entitlement check (plan C6)

**Produced:** 2026-08-15, by a clean-context Opus-class verification agent
(fetches 2026-08-14T14:15-14:55 UTC; 31 pages plain-fetched, 4
browser-rendered, 9 live API endpoint families; 34 assertions checked).
**Status:** findings are claims for registrant adjudication. The six
platform-table rows live in ratified amendment-2 draft text (erratum-log
Entry 3, item 3); every correction below is amendment-2 draft material
requiring the registrant's ruling at the D1 consolidation, not an edit
this note performs. **Every row verdict: HOLDS WITH CAVEAT** — the floors
are real but several are mis-stated; see §4 of the report for the
corrections list and §1d for disclosed fetch failures.

---

All verification complete. Here is the report.

---

# VERIFICATION NOTE — FAIR instrument platform table

**Retrieval date: 2026-08-15** (AEST; fetches executed 2026-08-14T14:15–14:55 UTC). All quotations below were extracted from raw fetched bytes and re-checked verbatim against the stored page text, not from memory or summarisation.

---

## 1. DENOMINATOR

### 1a. Documentation pages successfully fetched (31 distinct URLs, plain HTTP)

**DataCite** (4)
- `https://support.datacite.org/docs/tombstone-pages`
- `https://support.datacite.org/docs/doi-states`
- `https://support.datacite.org/docs/schema-mandatory-properties-v43`
- `https://support.datacite.org/docs/datacite-metadata-schema-v44-properties-overview`

**Zenodo** (8)
- `https://about.zenodo.org/policies/`
- `https://help.zenodo.org/docs/deposit/`
- `https://help.zenodo.org/docs/deposit/about-records/`
- `https://help.zenodo.org/docs/deposit/create-new-upload/`
- `https://help.zenodo.org/docs/deposit/describe-records/`
- `https://help.zenodo.org/docs/deposit/describe-records/creators/`
- `https://help.zenodo.org/docs/deposit/describe-records/descriptions/`
- `https://help.zenodo.org/docs/deposit/describe-records/licenses/`
- (`https://developers.zenodo.org/` also fetched)

**CRAN** (2)
- `https://cran.r-project.org/doc/manuals/r-release/R-exts.html`
- `https://cran.r-project.org/web/packages/policies.html`

**ADS** (3)
- `https://archaeologydataservice.ac.uk/help-guidance/instructions-for-depositors/`
- `https://archaeologydataservice.ac.uk/help-guidance/instructions-for-depositors/files-and-metadata/`
- `https://archaeologydataservice.ac.uk/help-guidance/instructions-for-depositors/file-level-metadata/`

**GitHub / GitLab** (8)
- `https://docs.github.com/en/rest/licenses/licenses`
- `https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository`
- `https://docs.github.com/en/repositories/creating-and-managing-repositories/deleting-a-repository`
- `https://docs.github.com/en/repositories/creating-and-managing-repositories/renaming-a-repository`
- `https://docs.github.com/en/site-policy/github-terms/github-terms-of-service`
- `https://docs.gitlab.com/api/projects/`
- `https://docs.gitlab.com/user/project/working_with_projects/`
- `https://about.gitlab.com/terms/`

**Crossref** (3)
- `https://www.crossref.org/membership/terms/`
- `https://www.crossref.org/documentation/schema-library/markup-guide-record-types/components/`
- `https://www.crossref.org/documentation/register-maintain-records/maintaining-your-metadata/`

### 1b. Pages requiring a real browser (bot-gated; 4 fetched, JS-rendered)

- `https://www.tdar.org/using-tdar/creating-and-editing-resources/datasets-create-and-edit/`
- `https://www.tdar.org/about/policies/`
- `https://www.tdar.org/about/policies/accession-policy/`
- `https://dans.knaw.nl/en/depositing-data-manual/during-depositing_ds/`

**Access finding (relevant to reproducibility of this note):** `www.tdar.org`, `core.tdar.org` return **HTTP 403** to curl and to WebFetch (Cloudflare challenge). `dans.knaw.nl` returns **HTTP 200 with a ~4.4 KB Anubis proof-of-work challenge body** — a *false-positive success* that a scripted harvester would silently record as content. Any automated census touching these two repositories must render JavaScript or it will mis-score them.

### 1c. Live API endpoints queried (empirical checks, 9 endpoint families)

Zenodo REST API (`/api/records`, legacy + `vnd.inveniordm.v1+json`); `doi.org` content negotiation (`vnd.datacite.datacite+json`); `doi.org/doiRA`; GitHub REST `/repos/{o}/{r}` (3 repos); GitLab REST `/projects/:id?license=true`; Crossref REST `/works`, `/works/{doi}` (2), `/types`; CRAN `src/contrib/Archive/dplyr/` directory listing.

### 1d. Failed / superseded fetches (9 — all disclosed, none papered over)

| URL | Result | Disposition |
|---|---|---|
| `https://datacite.org/documents/DataCite-MetadataKernel_v4.6.pdf` | **403** | Substituted support.datacite.org schema pages |
| `https://support.datacite.org/docs/datacite-metadata-schema-44-mandatory-properties` | **404** | Substituted v4.3 mandatory-properties page |
| `https://www.crossref.org/documentation/content-registration/structural-metadata/components/` | Redirects | Followed to `schema-library/markup-guide-record-types/components/` |
| `https://www.crossref.org/documentation/metadata-principles-and-practices/` | **404** | No substitute needed |
| `https://help.zenodo.org/docs/deposit/manage-licenses/`, `.../describe-records/licenses-and-rights/`, `.../describe-records/doi/` | **404** | Correct path is `.../describe-records/licenses/` |
| `https://docs.github.com/.../managing-repository-settings/deleting-a-repository` | **404** | Correct path is `.../creating-and-managing-repositories/deleting-a-repository` |
| `https://www.tdar.org/about/policies/preservation-curation-policy/` | **404** | tDAR's policy hub links a "Preservation & Curation Policy"; my constructed URL was wrong. **tDAR's preservation policy text is NOT verified in this note.** |

### 1e. Claims checked

**34 discrete assertions** across 6 rows: 18 **HOLD**, 12 **HOLD WITH CAVEAT**, 3 **NOT VERIFIED / CONTRADICTED**, 1 **NOT VERIFIED (page unreachable)**.

---

## 2. PER-ROW VERIFICATION

### ROW 1 — DataCite-registered DOI

**Asserted:** (a) a metadata record carrying the identifier exists; (b) tombstone persistence — metadata remains accessible even if the resource goes away.

#### Evidence (a) — metadata record exists

`https://support.datacite.org/docs/schema-mandatory-properties-v43` (retrieved 2026-08-15). The page enumerates six mandatory properties: **1 Identifier, 2 Creator, 3 Title, 4 Publisher, 5 PublicationYear, 10 ResourceType** (each with "Occurrence: 1"). Of Identifier:

> "The Identifier is a unique string that identifies a resource."

> "DOI (Digital Object Identifier) registered by a DataCite member. Format should be "10.1234/foo""

**Floor-quality caveat, same page:**

> "If providing values for any of the mandatory properties presents a difficulty, use of standard machine-recognizable codes is strongly advised. A set of the codes is provided in DataCite Metadata Schema v4.1 Standard Values for Unknown Information."

The page then gives a worked example of a compliant citation built almost entirely from null-codes:

> ":unkn 9999: :none. :null. Dataset."

*Paraphrase:* schema-mandatory does not mean substantively populated — `:unkn`, `:none`, `:null` satisfy the mandate.

**Also note (not asserted by the table):** **Rights/licence is not among DataCite's mandatory properties.** Any licence guarantee at a DataCite-backed repository is a *repository-level* rule, never a DataCite-level one.

#### Evidence (b) — tombstone persistence: CONTRADICTED

`https://support.datacite.org/docs/tombstone-pages` (retrieved 2026-08-15):

> "DOIs are persistent identifiers (PIDs), which means that they are intended to be a permanent means of identifying and accessing a particular resource. Because of this, a DataCite DOI cannot be deleted."

> "A tombstone page should be created whenever the item a DOI describes is no longer available, for whatever reason."

But tombstoning is **best practice devolved to the repository, not an enforced platform floor**:

> "Tombstone pages are generally the responsibility of the organization responsible for maintaining the DOI (in other words, a DataCite Repository)."

> "DataCite does not currently provide any tombstone pages automatically."

And critically, the *prescribed workflow removes the metadata from public access*. Same page, under "How do I create a tombstone page?":

> "Update the state of the DOI to be "Registered". DOIs in the "Registered" state are still registered with the global handle server, so they will resolve if someone knows the exact DOI, but they are not indexed in DataCite Commons or the Public API."

Corroborated at `https://support.datacite.org/docs/doi-states` (retrieved 2026-08-15):

> "Registered DOIs are registered with the global Handle System. However, metadata for Registered DOIs is not openly available: they are not findable in DataCite Commons and are not retrievable via the Public API. Authenticated users can access metadata for Registered DOIs via the Member API."

> "Findable DOIs may be updated to Registered DOIs, which hides the metadata from publicly availability. This is useful in cases where a DOI is created by mistake or content is retracted."

*(The typo "from publicly availability" is in the source.)*

The same page's state table records, verbatim as column headings, "Registered in global Handle System" / "Publicly available metadata", with Findable = ✅/✅ and Registered = ✅/❌.

#### VERDICT — ROW 1: **HOLDS WITH CAVEAT (severe — limb (b) is contradicted)**

- Limb (a) **HOLDS**, with the caveat that mandatory ≠ informative (null-codes permitted).
- Limb (b) **NOT VERIFIED — actively contradicted.** The DOI string is undeletable, but *public machine-readable metadata accessibility is not guaranteed in exactly the withdrawal scenario the entitlement is meant to cover.* DataCite's own recommended retraction workflow flips the record to `Registered`, which withdraws it from the Public API. A census that harvests DataCite's Public API will see a tombstoned record as **absent**, not as tombstoned.

---

### ROW 2 — Zenodo

**Asserted:** (a) deposits carry DataCite metadata; (b) a licence field exists on every record.

#### Evidence (a) — DataCite metadata: HOLDS

`https://about.zenodo.org/policies/` (retrieved 2026-08-15):

> "Metadata types and sources: All metadata is stored internally in JSON-format according to a defined JSON schema. Metadata is exported in several standard formats such as MARCXML, Dublin Core, and DataCite Metadata Schema (according to the OpenAIRE Guidelines)."

**Empirical confirmation** (2026-08-15): `https://doi.org/doiRA/10.5281/zenodo.21935645` returns `{"DOI": "10.5281/zenodo.21935645", "RA": "DataCite"}`. Content negotiation for `application/vnd.datacite.datacite+json` on the same DOI returns `schemaVersion: http://datacite.org/schema/kernel-4` with a populated `rightsList` carrying an SPDX `rightsIdentifier`.

#### Evidence (b) — licence on EVERY record: FALSIFIED

`https://help.zenodo.org/docs/deposit/describe-records/licenses/` (retrieved 2026-08-15):

> "The license field is a required field. Providing the license for your record is important for other users to be able to reuse your upload. Zenodo defaults to the Creative Commons Attribution 4.0 International (CC-BY) license."

But the policy scopes the requirement to *public* files — `https://about.zenodo.org/policies/`:

> "Licenses: Users must specify a license for all publicly available files. Licenses for closed access files may be specified in the description field."

**Empirical test, Zenodo legacy REST API, 2026-08-15** (`https://zenodo.org/api/records`):

| Population | n (unique) | records carrying `metadata.license` |
|---|---|---|
| Newest records (mixed access) | 298 | **298 / 298 (100%)** |
| `q=access_right:open` | 25 | 25 / 25 (100%) |
| `q=access_right:embargoed` | 100 | **83 / 100 (83%)** |
| `q=access_right:restricted` | 100 | **27 / 100 (27%)** |

Direct single-record confirmation: Zenodo record `20660471` (`access_right: restricted`) — the `license` key is **absent** from `metadata` entirely; keys present are `access_right, alternate_identifiers, communities, creators, description, doi, journal, keywords, publication_date, references, related_identifiers, relations, resource_type, title`.

**73 of 100 sampled restricted records carry no licence field at all.** The assertion "a licence field exists on every record" is false for restricted and embargoed deposits.

*Sampling limitation (stated for honesty):* these are recency-ordered / query-ordered API pages, not a random sample of the 7,120,060-record corpus. The direction and magnitude of the gap are unambiguous; the exact percentage is not a corpus-wide estimate.

#### Persistence (not asserted, but relevant and favourable)

`https://about.zenodo.org/policies/`:

> "Withdrawal: If the uploaded research object must later be withdrawn, the reason for the withdrawal will be indicated on a tombstone page, which will henceforth be served in its place. Withdrawal is considered an exceptional action, which normally should be requested and fully justified by the original uploader. In any other circumstance reasonable attempts will be made to contact the original uploader to obtain consent. The DOI and the URL of the original object are retained."

> "Records can be retracted from public view; however, the data files and record are preserved."

> "Retention period: Items will be retained for the lifetime of the repository. This is currently the lifetime of the host laboratory CERN, which currently has an experimental programme defined for the next 20 years at least."

And from `https://help.zenodo.org/docs/deposit/create-new-upload/`: "(note, the metadata is always publicly accessible)".

**This is materially stronger than the bare DataCite floor** — Zenodo commits to serving a tombstone page and retaining the record, where DataCite only recommends it.

#### VERDICT — ROW 2: **HOLDS WITH CAVEAT**

- (a) **HOLDS** — verified both in policy and empirically at the DOI-resolution layer.
- (b) **HOLDS WITH CAVEAT, materially mis-stated.** A licence field is effectively universal for *open* records but is *absent* on the majority of restricted records. Restate as: "licence field guaranteed for open-access records; not guaranteed for restricted/closed deposits."

---

## 3. FLOOR VS CEILING — ZENODO (mandatory at deposit vs optional enrichment)

`https://help.zenodo.org/docs/deposit/create-new-upload/` (retrieved 2026-08-15):

> "Fill in the minimal required metadata fields under "Basic information". The fields are marked with a small red star."

The walkthrough then enumerates the Basic-information fields in order: **Digital Object Identifier (DOI), Resource type, Title, Publication date, Creators**.

| Field | Status | Verbatim source |
|---|---|---|
| **Creators** | **MANDATORY** | "The creators field is a required field." (`help.zenodo.org/docs/deposit/describe-records/creators/`) |
| **Title** | **MANDATORY** | Basic information, red-star set |
| **Publication date** | **MANDATORY** (auto-filled) | "By default, the publication date is set to the date you create the draft upload." |
| **Resource type** | **MANDATORY** | Basic information, red-star set |
| **DOI** | **MANDATORY-by-construction** | "The DOI will only be registered once the record is published." |
| **Licence** | **MANDATORY *but pre-filled with a default*** | "The license field is a required field. … Zenodo defaults to the Creative Commons Attribution 4.0 International (CC-BY) license." |
| **Description** | **RECOMMENDED — NOT mandatory** | "Description is a recommended field." (`.../describe-records/descriptions/`) |
| Contributors, Keywords/subjects, Publisher, Funding, additional titles/descriptions | **OPTIONAL enrichment (ceiling)** | Listed as separate optional sections under "Describe records" |

### The load-bearing point for the census

**The licence "floor" at Zenodo is a *presence* floor, not a *choice* floor.** Because the field is pre-populated with CC-BY-4.0, a depositor who never touches it still publishes a record that looks, to any API harvester, exactly like a deliberate CC-BY election.

Empirically (298 newest records, 2026-08-15): **246/298 = 82.6% carry `cc-by-4.0`** — i.e. the default value — against mit-license 10.4%, gpl-3.0 1.3%, bsd-3-clause 1.0%, cc-by-nc-4.0 1.0%, apache2.0 0.7%.

An instrument that scores "has a licence" from a Zenodo record is, ~83% of the time, scoring Zenodo's form default rather than an author's act. The project's stated decision to score the licence *itself* separately is correct and should be recorded as **load-bearing**, not incidental.

**Second-order point:** the same default-licence trap exists at DANS (see Row 4) — `https://dans.knaw.nl/en/depositing-data-manual/during-depositing_ds/`: "the licence of the dataset will initially by default be set to CC0 1.0". Two of the platform table's rows share this artefact.

**Description is the honest floor-vs-ceiling boundary:** it is *recommended*, not required, and empirically **32/298 (10.7%)** of sampled Zenodo records carry no description at all. The table should not treat description as guaranteed.

---

### ROW 3 — CRAN

**Asserted:** (a) structured package metadata, which DESCRIPTION fields are mandatory (especially License); (b) archival — are versions retained when superseded or removed?

#### Evidence (a) — mandatory DESCRIPTION fields: HOLDS

`https://cran.r-project.org/doc/manuals/r-release/R-exts.html` (Writing R Extensions, §1.1.1; retrieved 2026-08-15). Verbatim, preserving the manual's typographic quotes:

> "The ‘Package’, ‘Version’, ‘License’, ‘Description’, ‘Title’, ‘Author’, and ‘Maintainer’ fields are mandatory, all other fields are optional."

> "Fields ‘Author’ and ‘Maintainer’ can be auto-generated from ‘Authors@R’, and may be omitted if the latter is provided"

> "The mandatory ‘License’ field is discussed in the next subsection."

From the Licensing subsection:

> "It is very important that you include license information! Otherwise, it may not even be legally correct for others to distribute copies of the package, let alone use it."

> "Do not use the ‘License’ field for information on copyright holders: if needed, use a ‘Copyright’ field."

Licence values are **constrained to a controlled list** — `https://cran.r-project.org/web/packages/policies.html`:

> "Packages with licenses not listed at https://svn.r-project.org/R/trunk/share/licenses/license.db will generally not be accepted."

> "The package’s license must give the right for CRAN to distribute the package in perpetuity. Any change to a package’s license must be highlighted when an update is submitted (for there have been instances of an undocumented license change removing even the right of CRAN to distribute the package)."

**This is the strongest licence floor of any row in the table** — it is mandatory, machine-checked at submission, drawn from a controlled vocabulary, has *no default value*, and carries a perpetual-distribution grant. It is materially stronger than Zenodo's.

#### Evidence (b) — archival: HOLDS WITH CAVEAT

`https://cran.r-project.org/web/packages/policies.html` (retrieved 2026-08-15):

> "Packages will not normally be removed from CRAN: however, they may be archived, including at the maintainer’s request."

> "Packages for which R CMD check gives an ‘ERROR’ when a new R x.y.0 version is released will be archived (or in exceptional circumstances updated by the CRAN team) unless the maintainer has set a firm deadline for an upcoming update (and keeps to it)."

> "Packages which are not updated are liable to be archived."

> "Package names on CRAN are persistent and in general it is not permitted to change a package’s name."

> "Packages should be named in a way that does not conflict (irrespective of case) with any current or past CRAN package (the Archive area can be consulted)"

**Empirical confirmation of superseded-version retention** (2026-08-15): `https://cran.r-project.org/src/contrib/Archive/dplyr/` lists **46 archived source tarballs**, from `dplyr_0.1.1.tar.gz` through `dplyr_1.2.0.tar.gz` — i.e. every superseded version is retained and directly downloadable.

Also documented: `https://cran-archive.r-project.org/web/checks/` retains check-result snapshots "For packages which have been archived since February 2018, a snapshot of the CRAN results page at the time of archival will be available".

#### VERDICT — ROW 3: **HOLDS WITH CAVEAT**

Mandatory-field and licence assertions **HOLD strongly**. Archival **HOLDS** in practice but the caveats are real and should be stated:

1. The governing wording is **"will not normally be removed"** — a norm, not a guarantee. There is no retention commitment analogous to Zenodo's "retained for the lifetime of the repository".
2. **CRAN issues no persistent identifier.** There is no DOI, no tombstone, and no resolvable PID for a package or version — retention is a filesystem convention on a URL path. The table should not let CRAN's genuinely excellent metadata floor imply a *persistence* floor of the same grade.
3. "Archived" is CRAN's word for *withdrawn from the active index*: the package leaves the main repository (and `install.packages()`) and moves to `/src/contrib/Archive/`. Retention ≠ continued availability by the normal install path.

---

### ROW 4 — Accredited domain repositories (ADS, tDAR, DANS)

**Asserted:** ingest enforces a domain metadata standard.

#### ADS — VERIFIED, strongest of the three

`https://archaeologydataservice.ac.uk/help-guidance/instructions-for-depositors/file-level-metadata/` (retrieved 2026-08-15):

> "All digital objects deposited with ADS must be accompanied by core file-level metadata. Core file-level metadata is the mandatory information required for ADS to archive and disseminate digital objects (files) within a larger dataset. This type of metadata includes file name, file description, creator and copyright information and other key contextual information on a digital object basis."

> "Certain data categories also require technical metadata."

`https://archaeologydataservice.ac.uk/help-guidance/instructions-for-depositors/files-and-metadata/` (retrieved 2026-08-15):

> "Ingest utilises a single Core Metadata Template for depositing all types of data. This means that all files deposited are listed in a single template."

> "For some data categories additional technical metadata is required. Below is a full list of the Data Categories."

> "Any Data Categories denoted with a * require technical metadata to be deposited alongside your files."

Category-specific templates are enumerated in the page's data-requirements table (Audiovisual*, GIS*, Geophysics*, Geophysics (Proprietary)*, etc.). **ADS enforces a mandatory template at ingest with machine validation** — "This template can be directly uploaded via our Ingest deposit system for validation."

#### DANS — VERIFIED, but the *domain* limb is weaker than asserted

`https://dans.knaw.nl/en/depositing-data-manual/during-depositing_ds/` (retrieved 2026-08-15 via rendered browser; document footer states "© DANS. R.5.3. Version 1.7, February 5, 2026"):

> "A small number of these metadata fields are mandatory. However, the more fields you enter, the better your data can be found and understood."

Enforcement is confirmed as a submission gate:

> "If the submission fails, there may be a mandatory field that has not been completed. The system will indicate the missing field."

Human curation on top of the machine gate:

> "Our Data Processing Team reviews the incoming datasets to ensure that the quality is high and the data are FAIR."

**But the archaeology-specific vocabulary block is optional, not enforced:**

> "In this section, several metadata fields can be used to add appropriate terms from the Dutch vocabulary ‘archaeological basic register’ (Archeologisch Basisregister, ABR+) and the Getty Art and Architecture Thesaurus."

"**can be used**" — this is availability, not enforcement. DANS's *mandatory* floor is a small generic (Dataverse-style Citation-block) core; the **domain** standard sits in the optional layer.

Also captured (favourable, unasserted): "All metadata are publicly available." and "The metadata, however, is always freely available under CC0 1.0."

#### tDAR — WEAKEST; assertion only partly supported

`https://www.tdar.org/using-tdar/creating-and-editing-resources/datasets-create-and-edit/` (retrieved 2026-08-15 via rendered browser). The page carries the heading **"Metadata Required for Datasets"**, and:

> "Check out our Metadata Guide for Datasets. This downloadable document summarizes the metadata required to create a Dataset in a condensed, easy-to-reference document."

> "Basic information for a Dataset includes the name of the associated Project, the status of the Dataset metadata, the title of the Dataset, the year the Dataset was created, and an abstract/description of the Dataset."

**Caveats:**
1. The page **describes** what to enter; it does not state per-field mandatory status, nor does it name any **external domain metadata standard**. What is enforced is tDAR's own internal resource model.
2. `https://www.tdar.org/about/policies/accession-policy/` (retrieved 2026-08-15) reserves removal rights: "Digital Antiquity retains the right to review and remove files and metadata records that do not comply with its policies."
3. tDAR's "Preservation & Curation Policy" is linked from its policy hub but **I could not retrieve it** — my constructed URL 404'd. **tDAR's preservation commitments are NOT verified in this note.**

#### VERDICT — ROW 4: **HOLDS WITH CAVEAT**

- **ADS: HOLDS.** Mandatory core template + category-specific technical metadata, validated at ingest.
- **DANS: HOLDS WITH CAVEAT.** A mandatory-field submission gate is verified, but it is explicitly "a small number" of *generic* fields; the archaeology/ABR+/AAT domain block is **optional**. The row's phrase "enforces a domain metadata standard" over-claims for DANS.
- **tDAR: HOLDS WITH CAVEAT (weak).** Required metadata is asserted by heading and enumerated, but no external domain standard is named and no per-field mandatory list was verified on a primary page.

The row treats three repositories as one uniform floor. **They are not uniform** — ADS ≫ DANS > tDAR on enforcement strength. If the census scores them identically it will over-credit tDAR and DANS deposits.

---

### ROW 5 — GitHub and GitLab

**Asserted:** (a) machine-readable licence detection field via API where a licence file is present; (b) NO persistence entitlement.

#### Evidence (a) — licence detection: HOLDS, with a GitLab asymmetry

`https://docs.github.com/en/rest/licenses/licenses` (retrieved 2026-08-15):

> "GitHub uses the open source Ruby Gem Licensee to attempt to identify the license for a project. Licensee matches the contents of a project's LICENSE file (if it exists) against a short list of known licenses. As a result, the API does not take into account the licenses of project dependencies or other means of documenting a project's license such as references to the license name in the documentation. If a license is matched, the license key and name returned conforms to the SPDX specification."

`https://docs.github.com/.../licensing-a-repository` (retrieved 2026-08-15):

> "If your repository is using a license that is listed on the Choose a License website and it's not displaying clearly at the top of the repository page, it may contain multiple licenses or other complexity. To have your license detected, simplify your LICENSE file and note the complexity somewhere else, such as your repository's README file."

**Empirical, GitHub REST API, 2026-08-15:**

| Repository | `license` result |
|---|---|
| `pandas-dev/pandas` | `spdx_id: "BSD-3-Clause"`, `key: "bsd-3-clause"` — clean detection |
| `tidyverse/dplyr` | `key: "other"`, **`spdx_id: "NOASSERTION"`**, `url: null` — file present, not resolved to SPDX |
| `octocat/Spoon-Knife` | **`license: null`** — no licence file |

**GitLab** — `https://docs.gitlab.com/api/projects/` (retrieved 2026-08-15) documents `license` as an **opt-in boolean query parameter**, "Include project license data.", and the response fields as: `license_url`, `license.key`, `license.name`, `license.nickname`, `license.html_url`, `license.source_url`.

**Empirical, GitLab REST API, 2026-08-15** (`gitlab-org/gitlab-runner?license=true`): returns `license.key: "mit"`, `license.name: "MIT License"`, `license_url: https://gitlab.com/gitlab-org/gitlab-runner/-/blob/main/LICENSE`.

**Asymmetry the table does not capture:** GitLab exposes **no SPDX identifier field** — neither the docs nor the live response contain `spdx_id`. GitHub does. Additionally GitLab's licence data is **absent unless the caller passes `license=true`**; a harvester using the default project payload will read GitLab licences as missing across the board. This is a live false-negative risk for the census harvester, not a theoretical one.

#### Evidence (b) — NO persistence entitlement: HOLDS decisively

**GitHub**, `https://docs.github.com/en/repositories/creating-and-managing-repositories/deleting-a-repository` (retrieved 2026-08-15):

> "You can delete any repository or fork if you're either an organization owner or have admin permissions for the repository or fork."

> "Deleting a repository will permanently delete team permissions. This action cannot be undone."

> "Some deleted repositories can be restored within 90 days of deletion."

**GitHub Terms of Service**, `https://docs.github.com/en/site-policy/github-terms/github-terms-of-service` (Effective date stated on page: April 27, 2026; retrieved 2026-08-15):

> "You may cancel this agreement and close your Account at any time."

> "We will retain and use your information as necessary to comply with our legal obligations, resolve disputes, and enforce our agreements, but barring legal requirements, we will delete your full profile and the Content of your repositories within 90 days of cancellation or termination (though some information may remain in encrypted backups). This information cannot be recovered once your Account is canceled."

**Renaming**, `https://docs.github.com/en/repositories/creating-and-managing-repositories/renaming-a-repository` (retrieved 2026-08-15):

> "When you rename a repository, all existing information, with the exception of project site URLs, is automatically redirected to the new name"

but the redirect is explicitly breakable:

> "If you create a new repository under your account in the future, do not reuse the original name of the renamed repository. If you do, redirects to the renamed repository will no longer work."

**GitLab**, `https://docs.gitlab.com/user/project/working_with_projects/` (retrieved 2026-08-15):

> "By default, when you delete a project for the first time, it enters a pending deletion state. Delete a project again to remove it immediately."

> "On GitLab.com, the project is deleted after 30 days. On GitLab Self-Managed, you can modify the retention period through the instance settings."

#### VERDICT — ROW 5: **HOLDS WITH CAVEAT**

- (b) **HOLDS** — no archival guarantee on either platform, confirmed from docs *and* terms. Deletion is unilateral, immediate-on-request at GitLab, and irreversible past 90 days at GitHub.
- (a) **HOLDS WITH CAVEAT.** The detection field exists on both, but the table's single-cell treatment hides three operational facts: GitHub returns `NOASSERTION`/`"other"` for unrecognised licence files (field present, value useless); GitHub returns `null` where no file exists; and **GitLab exposes no SPDX identifier and requires an opt-in parameter.** "A machine-readable licence detection field exists" is true; "a usable SPDX licence identifier is retrievable" is not.

---

### ROW 6 — Publisher supplement of a Crossref-registered article

**Asserted:** served from the article landing page; article-level record persistence via Crossref; NO independent metadata record, licence field, registry indexing, or resource-level identifier of its own. Verify the Crossref side; note the component-DOI caveat and define a component DOI.

#### Evidence — article-record persistence: HOLDS WITH CAVEAT

`https://www.crossref.org/membership/terms/` (retrieved 2026-08-15), §2 Member's Obligations, "Maintaining and Updating Metadata":

> "The Member shall ensure that each Identifier assigned to the Member's Content continuously resolves to a landing response page (a "Landing Page") containing, at a minimum, (i) complete bibliographic information about the corresponding Content (including the Identifier), visible on the initial page, with reasonably sufficient information detailing how the Content can be cited and accessed, and/or (ii) a hyperlink leading to the Content itself, in each case in accordance with the Display Guidelines. The Identifier shall serve as the permanent URL link to the Response Page."

The same clause names withdrawal-without-notification as a **breach**:

> "Some examples of failures to maintain and update Metadata as required by this Section 2(i) include: … 2) withdrawing content without posting a notification and updating the record's URL/metadata with Crossref"

Under "Archives":

> "The Member shall use best efforts to contract with a third-party archive or other content host (an "Archive") … for such Archive to preserve the Member's Content and, in the event that the Member ceases to host the Member's Content, to make such Content available for persistent linking."

> "The Member agrees that, in the event that the Content permanently ceases to be maintained by the Member, Crossref is entitled to redirect Identifiers to an Archive or a "Defunct DOI" page hosted by Crossref."

On termination:

> "With respect to Metadata deposited and Identifiers registered prior to such suspension or termination: (i) Crossref shall have the right to keep, maintain and use such Metadata and Identifiers within the Crossref Infrastructure and Services"

And Crossref's own service commitment:

> "Crossref shall use commercially reasonable efforts to maintain the Crossref Infrastructure and Services and to make it continually available for use by Members."

**The load-bearing caveat:** every persistence obligation above binds the **member/publisher**, not Crossref. Crossref's own retention is drafted as a **right** ("is entitled to", "shall have the right to keep"), and its availability commitment is **"commercially reasonable efforts"**. Crossref *guarantees* the metadata record's continued existence in the sense that it is entitled to retain it; it does not warrant that the landing page resolves — that is the publisher's contractual duty, enforced only by Crossref's discretion ("Crossref shall take reasonable steps to enforce these Terms").

#### Component DOI — definition per Crossref docs

`https://www.crossref.org/documentation/schema-library/markup-guide-record-types/components/` (retrieved 2026-08-15) — note this URL is where `.../content-registration/structural-metadata/components/` now redirects:

> "Component records are often registered for figures, tables, and supplemental materials associated with a journal article."

> "Components may be deposited along with their parent DOI or they can be deposited by themselves in a separate XML file as a stand-alone component. Components have their own metadata which is distinct from that of the parent DOI(s)."

> "Components may belong to more than one parent item. For example, two journal articles may include the same component DOI."

Corroborated in the Terms, which lists "components" among registrable content types: "Should the Member choose to register different types of Content and Metadata, such as journal articles, book chapters, datasets, conference proceedings, preprints, components, data, peer review reports, versions, or relations, the Member shall comply with all obligations applicable to each specific record type".

#### Empirical scale and quality of the component caveat (2026-08-15, Crossref REST API)

- `https://api.crossref.org/works?filter=type:component` → **`total-results: 9,311,551`**. `https://api.crossref.org/types` confirms the registered type ids `component` and `report-component`.
- **The caveat is therefore not marginal** — over nine million component DOIs exist. A census assuming supplements never have their own DOI will misclassify a non-trivial share.
- **But component records are metadata-poor.** Worked example, `10.1371/journal.pone.0000308.s001`: `type: component`, **`title: []` (empty)**, **no `license` field**, no author/creator field. Present keys: `DOI, URL, container-title, content-domain, created, deposited, indexed, is-referenced-by-count, issued, member, original-title, prefix, publisher, reference-count, references-count, relation, resource, score, short-container-title, short-title, source, subject, subtitle, title, type`.
- By contrast the **parent article** `10.1371/journal.pone.0000308` (`type: journal-article`) **does** carry a populated `license` array.

#### VERDICT — ROW 6: **HOLDS WITH CAVEAT**

- "No independent metadata record / no licence field / no resource-level identifier" **HOLDS as the default case**, and the empirical component record confirms that even the exception is close to empty (no title, no licence, no creators).
- "Article-level record persistence via Crossref" **HOLDS WITH CAVEAT**: it is a *member obligation* backed by a Crossref *right* of retention and "commercially reasonable efforts", not a Crossref warranty. The table should not present it as a platform-enforced guarantee of the same class as DataCite's undeletable DOI.
- The component-DOI caveat is **correctly flagged and should be strengthened** — 9.3M records is a population, not an edge case.

---

## 4. WHAT THE TABLE SHOULD ASSERT BUT DOESN'T — OR ASSERTS WRONGLY

### A. Asserts wrongly (must be corrected before the census relies on it)

1. **Row 1, tombstone persistence — the most serious error.** The table asserts metadata "remains accessible even if the resource goes away." DataCite's own prescribed retraction workflow sets the DOI to `Registered`, which is *by definition* not publicly retrievable ("not retrievable via the Public API"). The entitlement fails precisely in the scenario it exists to cover. **A harvester reading DataCite's Public API cannot distinguish "tombstoned" from "never existed."** Rewrite as: *DOI string is undeletable and Handle-resolvable; public metadata accessibility is NOT guaranteed post-withdrawal.*

2. **Row 2, "a licence field exists on every record" — false as stated.** Verified 27/100 restricted and 83/100 embargoed Zenodo records carry the field. Zenodo's policy scopes the requirement to "all publicly available files". Rewrite to scope the guarantee to open-access records.

3. **Row 4 treats ADS, tDAR, and DANS as one uniform floor.** They differ materially. ADS enforces a mandatory validated template; DANS enforces only "a small number" of generic fields and makes its *archaeology* vocabulary block optional ("can be used"); tDAR names no external domain standard at all. Split the row or grade it.

4. **Row 5's licence cell over-generalises across two platforms.** GitLab exposes no SPDX identifier and requires opt-in `license=true`. GitHub returns `NOASSERTION` for unrecognised files. "Machine-readable licence detection field" ≠ "usable SPDX identifier".

5. **Row 6's "article-level record persistence via Crossref"** is a member obligation plus a Crossref retention *right*, under "commercially reasonable efforts". It is not a by-construction platform guarantee and should not be scored as one.

### B. Should assert but doesn't

6. **DataCite mandatory metadata can be legally satisfied with null-codes** (`:unkn`, `:none`, `:null`). Any "DataCite metadata exists" floor should carry this alongside it, or the instrument will read schema-compliance as substantive description.

7. **The default-licence artefact — the single most important addition.** Zenodo pre-fills CC-BY-4.0; DANS pre-fills CC0 1.0. Empirically **82.6% of sampled Zenodo records carry the default value**. Any licence-presence score at these two platforms is dominated by form defaults, not author choices. This should be an explicit column or footnote on both rows.

8. **DataCite does not mandate a rights/licence property at all.** The table should make clear that every licence guarantee in it is repository-level, never DataCite-level — otherwise "DataCite-registered DOI" reads as implying a licence floor it does not provide.

9. **Zenodo's persistence entitlement is stronger than the table gives it credit for** and should be asserted: guaranteed tombstone page on withdrawal, DOI and URL retained, record and files preserved on retraction, retention "for the lifetime of the repository", metadata always publicly accessible. This is *stronger than the bare DataCite row* and the table currently under-claims it.

10. **CRAN has no persistent identifier.** Its metadata floor is the strongest in the table (mandatory, controlled-vocabulary, no default, perpetual-distribution grant) but its persistence floor is a URL-path convention governed by "will not normally be removed". The table should not let the former imply the latter. Also worth asserting: **CRAN's licence floor has no default value**, making it the only row where a licence value is genuine evidence of an author decision.

11. **Description is not guaranteed anywhere.** It is "recommended" at Zenodo (10.7% of sampled records lack it), mandatory at CRAN, and unverified elsewhere. If the instrument scores description, the floor row must say so.

12. **Harvester-integrity finding (operational, belongs in the preregistration's methods, not the table).** `dans.knaw.nl` returns **HTTP 200 with a JavaScript proof-of-work challenge body** to scripted fetches — a silent false positive. `www.tdar.org` and `core.tdar.org` return **403**. A census that scores these repositories by scripted fetch will record DANS as content-bearing-but-empty and tDAR as unreachable. **Both must be rendered, and the preregistration should commit to a rendering step plus a challenge-page detector.**

13. **Component DOIs are 9.3M strong and metadata-poor.** Row 6 should state both halves: the exception is common, *and* the exception buys almost nothing (empty title, no licence, no creators on the worked example).

---

## 5. VERDICT SUMMARY

| Row | Verdict |
|---|---|
| 1. DataCite DOI | **HOLDS WITH CAVEAT** — (a) record exists holds (null-codes permitted); (b) tombstone metadata accessibility **CONTRADICTED** by DataCite's own docs |
| 2. Zenodo | **HOLDS WITH CAVEAT** — DataCite metadata holds; "licence on every record" **falsified for restricted/embargoed** |
| 3. CRAN | **HOLDS WITH CAVEAT** — metadata/licence floor strongest in table; archival is a norm not a guarantee, and there is no PID |
| 4. ADS / tDAR / DANS | **HOLDS WITH CAVEAT** — ADS holds; DANS's domain block is optional; tDAR names no external standard. Not a uniform floor |
| 5. GitHub / GitLab | **HOLDS WITH CAVEAT** — no-persistence holds decisively; licence-detection cell over-generalises (GitLab: no SPDX, opt-in) |
| 6. Crossref supplement | **HOLDS WITH CAVEAT** — no-independent-record holds; Crossref persistence is a member obligation + Crossref *right*, not a warranty |

**No row was scored on unfetched evidence.** One asserted sub-item — tDAR's preservation and curation policy — is recorded as **NOT VERIFIED (page unreachable at constructed URL)** rather than inferred.
