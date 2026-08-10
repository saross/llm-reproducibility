# Prior-art report (VERIFIED): how FAIR and reproducibility-assessment instruments handle third-party/reused digital artefacts

**Verification date:** 2026-08-10 · **Verifier:** prior-art-scout-verifier (fresh context, no shared state with proposer)
**Source draft:** `wiki/planning/scout-reports/2026-08-10-fair-third-party-artefacts-prior-art.md`
**Provenance note:** the verifier returned its integrated report inline (its operating constraints forbid file writes); the orchestrating session saved it here with HTML transport entities unescaped and two bulk sections condensed rather than mirrored: (1) the "original candidates table" section is not duplicated — it is the candidates table of the draft file above, unchanged; (2) the verifier's machine-readable `corrections.jsonl` block (68 rows mirroring the proposer's claims ledger: 65 pass, 2 fail on row 1, 1 unverifiable on row 19) is summarised in the Verification section rather than reproduced — its driver warning ("do not treat a passing claims-ledger as clearance; the quotation defects sit outside the emitted claim set") is carried in the High-vigilance note. All verdicts, corrections, quotes, and the corrected table are reproduced in full. The draft file was not modified by the verifier.

> **⚠ DO NOT CITE ROWS 9 OR 18 FROM THE ORIGINAL DRAFT.** The report's second- and third-most load-bearing quoted claims (ACM "Artifacts Available" operative text; *Journal of Industrial Ecology* "not data ownership") are, respectively, **inverted relative to the source** and **not present at the source**. Both are named in the registrant's list of quotes intended for a preregistered-instrument amendment. Details in the Verification section.

## Executive summary

*(Verbatim from proposer's draft. Retained unedited per protocol — but note that the sentences on ACM badging and on "no instrument requires authorship as a precondition" are contradicted by the verified ACM text; see Verification.)*

This is a **partially-solved problem with one strong, directly-applicable precedent** and a great deal of instructive silence. Every object-scoped FAIR assessment instrument examined (RDA FAIR Data Maturity Model, F-UJI, FAIRshake, FAIR-Checker, FAIR4RS/FAIRsoft) is architecturally incapable of discriminating by authorship, because their unit of assessment is the digital object itself, identified by its own persistent identifier — "who created it" simply never enters the indicator set. Self-assessment/awareness tools (FAIR-Aware, ARDC's tools) are explicitly framed as pre-deposit, first-person exercises ("your dataset, before depositing") and were never designed to retrospectively audit third-party inputs at all. Paper-scoped badging and audit schemes (ACM Artifact Review and Badging, CODECHECK, COS/*Psychological Science* Open Data and Open Materials badges) are, on close reading of their actual operative criteria, **status-based, not origin-based**: they ask whether the input is permanently, publicly, and citably available — not who put it there — despite looser popular paraphrases (including ACM's own marketing language) sometimes implying "author-created." Large-scale meta-research audits of data/code availability (Stodden 2018, Colavizza 2020, Culina 2020) code availability as a binary/ordinal access-method variable and do not implement any category for reused/secondary data — the silence is by omission, not by considered policy, as far as retrievable text shows. The one clear exception — and the closest direct precedent to the registrant's problem — is the **Journal of Industrial Ecology's Data Openness Badges**, which explicitly separate "foreground" (author-generated) from "background" (third-party/secondary, e.g. ecoinvent) data and award full badge credit when background data is precisely cited/linked rather than re-deposited or re-authored. No instrument found imposes a *penalty* specifically for blameless reliance on well-archived third-party data, and none found requires authorship as a precondition for full marks on an artefact's own FAIRness — which is consistent with, though does not itself dictate, the registrant's working position.

## Verification

**Summary — candidate rows**

- Rows verified: 19
- Precise row-level tallies: **PASS** — 3, 4, 5, 7, 8, 10, 13, 14, 16 (9 rows). **FAIL** — 1, 9, 18 (3 rows). **PARTIAL** — 2, 6, 11, 12, 15, 17 (6 rows). **UNVERIFIABLE** — 19 (1 row).

**Summary — emitted claims (`claims.jsonl`)**

- Claims verified: 68
- Pass: 65
- Fail: 2 (both on row 1)
- Unverifiable: 1 (row 19)

**⚠ The two tallies diverge, and the divergence is the headline finding.**

**Confabulation risk assessment**

- Hard-failure rate (rows): 3/19 = **16 %**
- Hard-failure rate (emitted claims): 2/68 = 2.9 %
- **Dominant failure pattern: systematic quotation confabulation in cells and prose that the proposer emitted no claims for.** Every claim in the `claims.jsonl` block is mechanical and cheap (GitHub API fields, DOI existence, author/year/title). **Not one of the five load-bearing quoted claims the registrant flagged was emitted as a checkable claim.** Four of the report's direct quotations do not exist at their cited sources, and one of those four asserts the *opposite* of what the source says. The clean 65/68 claims-ledger result is therefore an artefact of claim-set selection, not evidence of a clean report.
- Secondary pattern: **version staleness** — the RDA specification cited is the superseded April 2020 draft (v0.90) rather than the June 2020 endorsed Recommendation (v1.00), and the CoreTrustSeal cycle described as "in preparation" was published in November 2025.
- **Recommendation: DO NOT forward this report to the preregistered-instrument amendment in its current form.** Rows 9 and 18 must be rewritten from the corrected source text before any of Sections 5 or 6 is acted on; Recommendation bullet 1 ("Use directly as documented justification") and Recommendation bullet 5 (the ACM cautionary example) are both built on failed claims. Review proposer methodology specifically on **quotation discipline**: the substance of the negative findings is largely sound, but the proposer repeatedly rendered its own inferences inside quotation marks and attributed them to fetched source text.

### Corrections applied

| Row | Field | Claimed | Verified |
|-----|-------|---------|----------|
| 1 | URL | `https://doi.org/10.15497/rda00045` | Resolves 200, but to **"FAIR Data Maturity Model: specification and guidelines – draft", v0.90, dated 2020-04-14**. The endorsed RDA Recommendation is **`https://doi.org/10.15497/rda00050`** (v1.00, 2020-06-25, Zenodo 3909563, CC BY 4.0) |
| 1 | Title | "FAIR Data Maturity Model: specification and guidelines" | DataCite title at the *cited* DOI is "FAIR Data Maturity Model: specification and guidelines **- draft**". The claimed title belongs to `10.15497/rda00050` |
| 1 | Last active | "2020-04 (doc); RDA Recommendation status June 2020" | Draft v0.90 issued 2020-04-14; Recommendation v1.00 published 2020-06-25. The row conflates the two documents |
| 1 | Notes (glossary quote) | "anything that is accessed and/or reused… of which the FAIRness is being assessed" | **VERIFIED VERBATIM** in both v0.90 and v1.00: "Anything that is accessed and/or reused and of which the FAIRness is being assessed, including metadata and datasets." Substance survives the DOI correction |
| 1 | §3(a) resource definition | Glossary defines "resource" as "a resource consisting of units of information… being the primary subject of the FAIR evaluation" | **MISATTRIBUTED.** That is the glossary entry for **"Data, digital object"**, not "Resource". Two different, adjacent glossary rows |
| 1 | §3(c) indicator count | "all 41 indicators (F1–R1.3)" | **Not reproducible.** Identifier extraction yields **42** unique indicator IDs in v1.00 and **43** in v0.90 (draft-only `RDA-I2-02D` was dropped in the final). Recount manually before citing |
| 2 | Notes | "Implements 16/17 RDA FDMM indicators" | **Unsupported at source.** `fuji_server/yaml/metrics_v0.5.yaml` defines **17 FAIRsFAIR metrics** (`FsF-*`); v0.8 defines 18. **Zero** `RDA-*` indicator identifiers appear in the metrics file; `metric_specification` points to Zenodo 6461229 (FAIRsFAIR), not the RDA FDMM |
| 6 | §3(b) quotation | Fetched text of Recommendation 1 "confirms it 'makes no distinction between original code and other components'" | **Quote absent.** The page contains no such string. The *substance* (no original-vs-third-party distinction) is correct as a negative finding, but it is the proposer's inference, not a source quotation |
| 9 | Notes / §3(b) — **operative badge text** | "the artifacts associated with the paper have been made available for retrieval, permanently and publicly"; "contains no authorship gate" | **INVERTED.** The ACM policy page's v1.1 definition reads: **"Artifacts Available v1.1 — Author-created artifacts relevant to this paper have been placed on a publically accessible archival repository. A DOI or link to this repository along with a unique identifier for the object is provided."** Confirmed in two independent captures (2021-04-16 and 2026-07-03). The sentence the proposer quoted is a loose rendering of the badge-family *header*, not the v1.1 definition. **ACM's authoritative text does contain an authorship gate** |
| 11 | §3(b) quotation | Open Data badge requires "all digitally shareable data relevant to the publication" / "all data necessary to reproduce the reported results" | **Not locatable** at the cited page (returns ~7 kB of chrome). Remove or re-source from the OSF badge wiki |
| 12 | Last active | "Requirements cycle 2023-2025 (2026-2028 in preparation)" | **Stale.** **CoreTrustSeal Requirements 2026-2028** was published **2025-11-20** (Zenodo `10.5281/zenodo.17660463`) and is current |
| 12 | §3(d) Zenodo record | "Requirements 2023–2025. Zenodo: `zenodo.org/records/7051096`" | **Wrong record.** 7051096 is the **Extended Guidance**; the Requirements document is Zenodo **7051012** (`10.5281/zenodo.7051012`) |
| 12 | §3(b) R07 title + quote | R07 "(Data Integrity and Authenticity)"; "the degree of reliability of the original deposited data and its provenance" | **Both wrong for the cited cycle.** In 2023-2025, R07 is **"Provenance and authenticity"**: "The repository guarantees the authenticity of the digital objects and provides provenance information." The quoted sentence appears nowhere in the 2023-2025 document |
| 12 | §3(a) group names | "organisational/digital-object-management/technical-infrastructure groups" | Third group is **"Information Technology & Security"**. R01–R16 count and "equally weighted, standalone items" both **VERIFIED** |
| 15 | §3(b) quotation | The paper "does not address whether code merely calling third-party packages counts toward availability" | **Quote absent from the paper** ("third-party", "dependency": 0 hits). The *substance* is correct — Culina et al. genuinely never discuss third-party packages — but the sentence is the proposer's, not the authors' |
| 15 | §3(b) screenshot claim | screenshot-based protocols count as "code" | **VERIFIED VERBATIM** |
| 17 | Name (article number) | "*Scientific Data* **8:3**" | **Wrong.** CrossRef: vol. 8, **article 192**. The report's own §3(d) citation gives 192 correctly |
| 18 | §3(b) quotation | "the critical requirement is 'transparency and reproducibility, not data ownership'" | **Quote absent** ("ownership": 0 hits; "reproducib*": 0 hits). **A fabricated quotation presented as the source's own framing** — and the sentence Recommendation bullet 1 proposes to quote into the amendment |
| 18 | Notes — "background" terminology | "Explicit foreground … vs **background** … distinction" | **Half-supported.** The page uses "**foreground**" once and otherwise says "**secondary data**" / "external or secondary data sets". "Background" is the proposer's gloss from LCA jargon |
| 18 | §3(b) quotations (the real ones) | LCA foreground/secondary example; ecoinvent version-and-process requirement | **BOTH VERIFIED VERBATIM.** "An LCA study makes available its foreground (all process descriptions based on own research and primary data) and also publishes all the links to a published data set (e.g., ecoinvent) for all secondary data used." And: "naming the exact database version (e.g., ecoinvent v3.5, cut-off allocation) and all referenced processes" |
| 18 | §3(d) Hertwich DOI | "exact DOI not independently confirmed" | **Now confirmed:** Hertwich, E. et al. (2018). "Nullius in Verba: Advancing Data Transparency in Industrial Ecology." *JIE* 22(1), 6–17. **`10.1111/jiec.12738`** |
| 3 | §3(d) citation | bioRxiv 657676 with the *Cell Systems* title | The bioRxiv preprint (`10.1101/657676`) has a different title; the quoted title belongs to the version of record: *Cell Systems*, Nov 2019, **`10.1016/j.cels.2019.09.011`** |
| 8 | §3(d) citation | "PMC10315041" (no DOI) | PMC ID correct; resolves to **`10.1186/s13326-023-00289-5`**, *Journal of Biomedical Semantics*, 2023-07-01 |
| 10 | §3(b)/(c) quotations | remote-repository/synthetic/subset data; "codecheckers record but don't investigate or fix" | **BOTH VERIFIED VERBATIM.** Author-guide source: `https://codecheck.org.uk/guide/community-workflow-author` |
| 14 | §3(b) coding scheme | four categories 0–3 | **VERIFIED VERBATIM** |
| 4 | §3(b) quotation | "You can use this tool at any point during your research before depositing your data(set)" | Exact sentence **not located** (JS application); second-person pre-deposit framing **amply supported**. Treat as paraphrase |
| 5 | Notes | four F/A/I/R sections for "your research dataset" | **VERIFIED** |

**No corrections required** on: all 34 GitHub API field claims (rows 2, 3, 6, 8, 10 — every one an exact match); all 32 DOI/author/year/title claims for rows 7, 11, 13, 14, 15, 16, 17.

### Load-bearing quoted claims — verdict table

| # | Quoted claim | Verdict |
|---|---|---|
| 1a | RDA FDMM glossary "resource" definition | **VERIFIED VERBATIM** (v0.90 and v1.00 identical) |
| 1b | RDA FDMM glossary "reuse" definition | **VERIFIED VERBATIM** |
| 1c | "No indicator references creator/depositor identity" | **SUBSTANTIVELY VERIFIED** — soften to "no indicator conditions scoring on creator or depositor identity" |
| 1d | Cited under DOI `10.15497/rda00045` | **FAIL** — superseded draft. Substitute `10.15497/rda00050` |
| 2 | ACM v1.1 "Artifacts Available" text + absence of authorship gate | **FAIL — inverted.** Source says "**Author-created** artifacts…" |
| 3a | JIE foreground/secondary rule and requirement language | **VERIFIED VERBATIM** |
| 3b | JIE "transparency and reproducibility, not data ownership" | **FAIL — quote does not exist at source** |
| 3c | JIE "background" terminology | **PARTIAL** — source says "secondary data" |
| 4 | CODECHECK remote-repository/synthetic/subset language | **VERIFIED VERBATIM** |
| 5 | Colavizza et al. four-category DAS coding scheme | **VERIFIED VERBATIM** |

### Unverifiable rows

| Row | URL | Reason |
|-----|-----|--------|
| 19 | COPE case page | HTTP **403** site-wide (anti-bot); **zero Wayback captures** of this exact URL path. No independent confirmation the page exists. This is exactly the shape a confabulated URL would take; open in a browser before citing |

Rows 9 and 13 also return live 403s (`acm.org`, `pnas.org` anti-bot) but were independently confirmed (Wayback; CrossRef). Both scored **pass** on `url_resolves`.

### High-vigilance note

Had the audit covered only the proposer's `claims.jsonl` block, it would have returned 65/68 pass and cleared the report. The three most damaging defects (ACM inversion, JIE fabricated quote, Culina fabricated quote) sit entirely outside the emitted claim set. **A proposer that emits claims only for the fields it queried mechanically, and none for the prose it wrote from reading, can pass a claims-ledger audit while being wrong about everything that matters.** Recommendation: require claim emission for every direct quotation, not merely for table cells.

### Injection-watch note

No prompt-injection attempts observed. All fetched content was treated as data.

## Corrected candidates table (final)

Fit ratings are preserved verbatim per protocol (they are the proposer's judgement) — **but the Fit ratings on rows 9 and 18 are now unsafe** where they rested on failed claims. Corrected cells are marked **[CORRECTED]**; verification-derived additions are marked **[VERIFIED]**.

| # | Name | Type | URL | Stars/DLs | Last active | Fit | Notes |
|---|------|------|-----|-----------|-------------|-----|-------|
| 1 | RDA FAIR Data Maturity Model: Specification and Guidelines, v1.00 | RDA Recommendation (spec, CC BY 4.0) **[VERIFIED]** | **[CORRECTED]** https://doi.org/10.15497/rda00050 (Zenodo 3909563). *Draft v0.90 = 10.15497/rda00045* | N/A | **[CORRECTED]** v1.00 published 2020-06-25; draft v0.90 issued 2020-04-14 | HIGH | Object-scoped; glossary **[VERIFIED VERBATIM]**: **Resource** = "Anything that is accessed and/or reused and of which the FAIRness is being assessed, including metadata and datasets"; **Reuse** = "The act of using an existing resource for a different purpose or in a different context…". No indicator *conditions scoring on* creator or depositor identity **[VERIFIED across full v1.00 text]**. **[CORRECTED]** 42 unique indicators in v1.00 (43 in draft). **[CORRECTED]** the "units of information / primary subject" definition belongs to the glossary entry *"Data, digital object"*, not *"Resource"* |
| 2 | F-UJI | Python tool / GitHub **[VERIFIED]** | https://github.com/pangaea-data-publisher/fuji | 79 **[VERIFIED]** | 2026-08-01 **[VERIFIED]** | HIGH | **[CORRECTED]** Implements **17 FAIRsFAIR data-object assessment metrics** (`FsF-*`, `metrics_v0.5.yaml`; 18 in v0.8) against a dataset PID — **not** the RDA FDMM indicator set. Takes any resolvable PID/URL regardless of depositor. Licence MIT **[VERIFIED]** |
| 3 | FAIRshake | Django toolkit / GitHub | https://github.com/MaayanLab/FAIRshake | 10 **[VERIFIED]** | 2025-08-28 **[VERIFIED]** | MEDIUM | Rubric-based assessment of "any digital object"; no authorship field in data model. Licence NOASSERTION **[VERIFIED]**. **[CORRECTED]** version of record: Clarke et al. (2019), *Cell Systems*, `10.1016/j.cels.2019.09.011` |
| 4 | FAIR-Aware (DANS/FAIRsFAIR) | Self-assessment web tool | https://fairaware.dans.knaw.nl/ | N/A | Current **[VERIFIED 200]** | LOW-MEDIUM | Second-person, pre-deposit framing **[VERIFIED in substance]**; the "before depositing" sentence is paraphrase, not quotation **[CORRECTED]**. Not built for retrospective third-party audit |
| 5 | ARDC FAIR Data Self-Assessment Tool | Self-assessment web tool | https://ardc.edu.au/resource/fair-data-self-assessment-tool/ | N/A | Current **[VERIFIED 200]** | LOW-MEDIUM | Four F/A/I/R sections for "your research dataset" **[VERIFIED VERBATIM]** |
| 6 | fair-software.eu / howfairis | Recommendations + CLI / GitHub | https://github.com/fair-software/howfairis | 74 **[VERIFIED]** | 2025-05-07 **[VERIFIED]** | HIGH | Repository-scoped, not authorship-scoped; no dependency-vs-own-code distinction **[VERIFIED as a negative finding]**. **[CORRECTED]** the "makes no distinction…" phrase is the proposer's inference, not a quotation. Licence Apache-2.0 **[VERIFIED]** |
| 7 | FAIR4RS Principles | Principles + journal article | https://doi.org/10.1038/s41597-022-01710-x | N/A; RDA rec. 10.15497/RDA00068 **[VERIFIED]** | 2022-10 **[VERIFIED]** | HIGH | Dependencies addressed as documentation-quality signal (qualified references via package managers), not an authorship gate. Barker, Michelle + 10 authors **[VERIFIED]** |
| 8 | FAIR-Checker | Web tool + Jupyter / GitHub | https://github.com/IFB-ElixirFr/FAIR-checker | 29 **[VERIFIED]** | 2026-08-05 **[VERIFIED]** | MEDIUM-HIGH | Object-scoped; authorship not a parameter. MIT **[VERIFIED]**. **[VERIFIED]** paper: Gaignard et al. (2023), `10.1186/s13326-023-00289-5` |
| 9 | ACM Artifact Review and Badging, v1.1 | Publisher policy | https://www.acm.org/publications/policies/artifact-review-and-badging-current **[VERIFIED via Wayback; live 403 anti-bot]** | N/A | Current since 2020-08-24 **[VERIFIED]** | HIGH *(rating no longer supported)* | **[CORRECTED — CLAIM INVERTED]** Operative v1.1 definition: **"Author-created artifacts relevant to this paper have been placed on a publically accessible archival repository. A DOI or link to this repository along with a unique identifier for the object is provided."** ACM's authoritative badge text **does** contain an authorship gate. **ACM is a counter-example to the report's thesis, not an ambiguous case in its favour** |
| 10 | CODECHECK | Workflow / R package / GitHub | https://github.com/codecheckers/codecheck | 11 **[VERIFIED]** | 2026-08-05 **[VERIFIED]** | HIGH | **[VERIFIED VERBATIM]** author guide: data "may be deposited depending on community practices in remote repositories, synthetic data may be used, subsets or preprocessed data may be included…". Five principles **[VERIFIED VERBATIM]**. MIT **[VERIFIED]** |
| 11 | COS / *Psychological Science* Open Data & Open Materials badges | Publisher badge scheme | https://doi.org/10.1371/journal.pbio.1002456 **[VERIFIED]** | N/A | Ongoing | HIGH | **[CORRECTED]** the quoted criterion phrases are not locatable at cos.io/initiatives/badges (page chrome only); re-source from the OSF badge wiki before citing. The no-secondary-data-rule gap stands |
| 12 | CoreTrustSeal | Repository certification | https://www.coretrustseal.org/why-certification/requirements/ **[VERIFIED 200]** | N/A | **[CORRECTED]** Requirements **2026-2028 published 2025-11-20** (`10.5281/zenodo.17660463`); 2023-2025 (`10.5281/zenodo.7051012`) superseded | HIGH (contrast case) | Unit = the repository. R01–R16, "equally weighted, standalone items" **[VERIFIED]**. **[CORRECTED]** 2023-2025 R07 = "**Provenance and authenticity**": "The repository guarantees the authenticity of the digital objects and provides provenance information." Third requirement group is "Information Technology & Security" |
| 13 | Stodden, Seiler & Ma (2018), PNAS | Meta-research paper | https://doi.org/10.1073/pnas.1708290115 **[VERIFIED via CrossRef]** | N/A | 2018-03 **[VERIFIED]** | MEDIUM | Binary availability outcome per paper; no reused/secondary-data category found |
| 14 | Colavizza et al. (2020), PLOS ONE | Meta-research paper | https://doi.org/10.1371/journal.pone.0230416 **[VERIFIED 200]** | N/A | 2020-04 **[VERIFIED]** | HIGH | **[VERIFIED VERBATIM]** four-category DAS coding; category 3 indifferent to deposit provenance **[VERIFIED as negative finding]** |
| 15 | Culina et al. (2020), PLOS Biology | Meta-research paper | https://doi.org/10.1371/journal.pbio.3000763 **[VERIFIED 200]** | N/A | 2020-07 **[VERIFIED]** | MEDIUM-HIGH | Screenshot-protocols-as-code **[VERIFIED VERBATIM]**. **[CORRECTED]** the "does not address…" sentence is the proposer's inference — verified as a negative finding (zero occurrences of "third-party"/"dependency") |
| 16 | Marwick (2017), *JAMT* 24(2), 424–450 | Methodological paper | https://doi.org/10.1007/s10816-015-9272-9 **[VERIFIED 200]** | N/A | 2017 **[VERIFIED print; CrossRef `issued` = 2016-01-07 online-first]** | MEDIUM | Full text not obtained by the scout; open preprint **[VERIFIED HTTP 200]**. *(Closed by the orchestrating session's direct read, 2026-08-10 — see instrument-clarification-plan.md)* |
| 17 | **[CORRECTED]** Tedersoo et al. (2021), *Scientific Data* **8:192** | Meta-research paper | https://doi.org/10.1038/s41597-021-00981-0 **[VERIFIED 200]** | N/A | 2021-07 **[VERIFIED]** | MEDIUM | Full text not obtained by the scout. *(Closed by the orchestrating session's direct read, 2026-08-10 — see instrument-clarification-plan.md)* |
| 18 | *Journal of Industrial Ecology* Data Openness Badges | Journal badge scheme | https://jie.yale.edu/data-openness-badges **[VERIFIED 200]** | N/A | Ongoing | **HIGH — closest direct precedent** *(rating defensible on the verified text; the fabricated quote must be removed)* | **[CORRECTED]** 2×2 scheme (data contribution × accessibility, gold/silver). **[VERIFIED VERBATIM]**: "An LCA study makes available its foreground (all process descriptions based on own research and primary data) and also publishes all the links to a published data set (e.g., ecoinvent) for all secondary data used"; "naming the exact database version (e.g., ecoinvent v3.5, cut-off allocation) and all referenced processes". Gold contribution permits "links to external or secondary data sets (including licensed databases)" **[VERIFIED]**. **[CORRECTED]** source's term is "**secondary data**", not "background"; **the "transparency and reproducibility, not data ownership" quotation does not exist — do not cite it**. **[VERIFIED]** policy note: Hertwich et al. (2018), *JIE* 22(1), 6–17, `10.1111/jiec.12738` |
| 19 | COPE — "Authorship when data sets are reused as secondary data" | Publication-ethics case guidance | **[UNVERIFIABLE — 403 site-wide; zero Wayback captures. Open in a browser before citing]** | N/A | — | LOW-MEDIUM | Content unverified; the page could not be retrieved by any available method |

## Recommendations (proposer's, with verifier flags)

*(Bullets 1 and 5 are built on failed claims — bullet 1 proposes quoting JIE language that includes a fabricated sentence; bullet 5 rests on an inverted reading of the ACM text. Both require rewriting before use. Remaining bullets stand.)*

- ~~**Use directly as documented justification:** the JIE "foreground/background" language~~ → **rewrite**: cite JIE's *verified* rule (gold contribution via precise citation of "external or secondary data sets") using the scheme's own "secondary data" terminology.
- **Cite as structural precedent for object-blindness-to-authorship:** RDA FDMM v1.00 (`10.15497/rda00050`) glossary definitions — verified verbatim.
- **Cite as the "status not origin" precedent for the code side:** CODECHECK (verified verbatim) and Culina et al. (verified negative finding).
- **Adapt approach, not implementation:** CoreTrustSeal as the unit-of-assessment contrast case (with corrected cycle and R07 text).
- ~~**Note the ACM inconsistency as a cautionary example**~~ → **rewrite**: ACM Artifact Badging v1.1 is an explicit **origin-gated counter-example** ("Author-created artifacts…"); cite it as the named contrast the instrument deliberately departs from, with reasons.
- **Ignore as non-transferable:** FAIR-Aware and the ARDC self-assessment tool.
- **Follow-up reads:** Marwick (2017) and Tedersoo et al. (2021) — *both closed by direct reads on 2026-08-10; findings in the instrument clarification plan.*

## Build-vs-adopt verdict (proposer's, with verifier flags)

Point 2 must cite `10.15497/rda00050`. Point 3's "uniformly status-based" characterisation is weakened by the verified ACM text — the registrant's rule now involves one named, deliberate departure (ACM) alongside the supporting precedent set (RDA FDMM, JIE, CODECHECK, Colavizza, Culina). The core verdict stands: **adopt existing conceptual precedent, then build the registrant's own explicit named rule**, because no instrument reviewed states the registrant's exact rule as a general-purpose policy.

## Verifier's one-line summary

The report's structural metadata is immaculate — all 34 GitHub fields and all DOI/author/year/title fields match their APIs exactly — but **four of its direct quotations do not exist at their cited sources, and the ACM one says the opposite of what the report claims**, so the two rows the registrant most wanted to lean on (9 and 18) are the two that failed hardest.
