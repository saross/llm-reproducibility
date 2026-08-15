# Repository-evaluation enrichment addendum (plan D1-prep)

**Date:** 2026-08-15 (all retrievals this date)
**Companion to:** `verification-note.md` (same directory) — this addendum enriches the
platform-table rows at the registry layer; it does not re-verify the per-row entitlement
assertions.
**Authorising ruling:** Shawn, 2026-08-15 (instrument-clarification plan, decision log):
evaluate at the infrastructure layer, where all lodged artefacts inherit the platform's
characteristics; repositories are assessed once, so enrich table rows with CoreTrustSeal
(CTS) certification status and re3data.org registry evidence.
**Raw evidence:** `evidence/` (five re3data Application Programming Interface (API)
records, two CTS register extracts; `checksums.sha256` covers all seven files).

## 1. Method and denominator

Thirteen HTTP requests, two registries:

1. **re3data.org** — REST API. Full repository list
   (`https://www.re3data.org/api/v1/repositories`, 1,022,585 bytes; the `query` parameter
   is ignored by the endpoint — it returns the complete unfiltered list, so matching was
   done locally). Five repository records fetched by identifier and archived:
   ADS `r3d100000006`, tDAR `r3d100010347`, Zenodo `r3d100010468`, DANS Data Station
   Archaeology `r3d100014005`, CRAN `r3d100010411`.
2. **CoreTrustSeal register** — the public register page
   (`https://www.coretrustseal.org/why-certification/certified-repositories/`) 301s to
   `https://amt.coretrustseal.org/certificates/`, a Nuxt single-page application that
   returns an **empty JavaScript shell to scripted fetches** — the same silent-failure
   class as verification-note item 12. Data was therefore pulled from the SPA's own
   GraphQL backend (`https://backend.amt.coretrustseal.org/graphql`), which is the
   register's data source: schema introspection (three queries), then
   `{ certificates { id certificationRequest { repository { name } validUntil status
   pidUrl } } }` (290 issued certificates; `evidence/cts-certificates.json`) and
   `{ allCertificationRequests { id status validUntil reviewDueDate repository { name } } }`
   (556 requests across all statuses: 290 Accepted, 164 Rejected, 40 Pre Submit,
   22 First Submit, 19 Revision, 13 Board Review, 8 In Review;
   `evidence/cts-requests.json`).

Nothing below is inferred from an unfetched source; where a register is silent, that
silence is stated as the finding.

## 2. Per-repository findings

### Archaeology Data Service (ADS)

- **CTS: CERTIFIED, current.** Certificate valid until **2027-02-12** (request 277,
  status Accepted, PID `https://doi.org/10.34894/GZFRVY`). A prior certificate (request
  211) expired 2023-04-28 — a visible **renewal chain**: certification is maintained,
  not a one-off.
- **re3data `r3d100000006`** (DOI 10.17616/R3MW23, lastUpdate 2025-02-25): pidSystem
  DOI; qualityManagement **yes**; metadata standards DataCite Metadata Schema, Dublin
  Core, OAI-ORE, and repository-developed schemas; certificate field records only
  "other" (see §3 divergence).

### The Digital Archaeological Record (tDAR)

- **CTS: LAPSED.** The only issued certificate (request 164, status Accepted, PID
  `https://doi.org/10.34894/NIOIBV`) is recorded valid until **2025-12-16** — roughly
  eight months before this retrieval. A renewal application exists at status
  **"First Submit"** (request 539, no validUntil): submitted, not reviewed, not
  re-certified as of 2026-08-15.
- **re3data `r3d100010347`** (DOI 10.17616/R3HK56, lastUpdate 2026-03-04): pidSystem
  DOI; qualityManagement yes; metadata standard **Dublin Core only** — the registry
  layer independently corroborates verification-note row 4's finding that tDAR names no
  external domain metadata standard; **no certificate element at all**.

### DANS Data Station Archaeology

- **CTS: CERTIFIED, current.** Certificate valid until **2028-02-27** (request 148,
  status Accepted, PID `https://doi.org/10.34894/UTK2AL`). Platform-migration context is
  visible in the register: legacy DANS:EASY held a certificate that expired 2024-09-03
  (request 47) and a separate EASY request was Rejected (request 314) — the current
  Data Station certification supersedes EASY's.
- **re3data `r3d100014005`** (DOI 10.17616/R31NJNAT, lastUpdate 2025-06-18): pidSystem
  DOI; metadata standards Data Documentation Initiative (DDI), Dublin Core, OAI-ORE —
  generic standards, consistent with the verification note's finding that DANS's
  *mandatory* floor is generic and the archaeology (ABR+) block optional; certificate
  field records only "other".

### Zenodo

- **CTS: ABSENT — never applied.** Zenodo appears in **zero of the 556 certification
  requests of any status** in the register. This is stronger than "not certified": no
  application is on record at all.
- **re3data `r3d100010468`** (DOI 10.17616/R3QP53, lastUpdate 2026-05-07): pidSystem
  DOI; metadata standards DataCite Metadata Schema and Dublin Core; enhancedPublication
  yes; **qualityManagement: no**; no certificate element.
- **Implication for the table:** Zenodo's persistence entitlements (verification-note
  item 9 — tombstone page, DOI retained, metadata always accessible) are the platform's
  **own policy assertions, third-party-unaudited**. They remain adoptable as ruled, but
  the row should carry this provenance note alongside them.

### Comprehensive R Archive Network (CRAN)

- **CTS: not in scope** — absent from the register (as expected for a software package
  archive).
- **re3data `r3d100010411`** (DOI 10.17616/R3J88J, lastUpdate 2023-09-13 — the stalest
  record consulted): **pidSystem: none**, corroborating verification-note item 10 (no
  persistent identifier) at the registry layer; qualityManagement unknown; licence
  evidence via CRAN's own policy page and the R licence database
  (`https://svn.r-project.org/R/trunk/share/licenses/license.db`).

## 3. Registry divergence — check at the service

re3data's `certificate` field records "other" for ADS and DANS Data Station Archaeology
(both currently CTS-certified) and nothing for tDAR (formerly certified). **The
CoreTrustSeal register is authoritative over re3data's certificate assertion** — the
same principle as the ruled licence-conflict rule: verify entitlements at the service
that grants them, not at an aggregator. Table rows citing certification must cite the
CTS register (with validUntil), never re3data's certificate field.

## 4. Implications for the graded row 4 and the table build-out

The registry layer independently corroborates the 2026-08-15 grading ruling
(ADS ≫ DANS > tDAR), and adds a certification axis:

| Repository | CTS status (2026-08-15) | Domain-standard limb (verification note) |
|---|---|---|
| ADS | Certified to 2027-02-12, renewal chain | Mandatory validated template at ingest — HOLDS |
| DANS Data Station Archaeology | Certified to 2028-02-27 | Mandatory floor generic; ABR+ block optional |
| tDAR | Lapsed 2025-12-16; renewal at First Submit | No external standard named; preservation policy unverified |
| Zenodo | Never applied (0/556 requests) | n/a (generalist row) |
| CRAN | Not in scope | n/a (no PID confirmed at registry layer) |

Build-out notes for the D1 window text:

1. The graded row 4 can now cite certification evidence per platform, with dates. tDAR's
   lapsed-certification status compounds its grade (weakest of the three) but is
   time-sensitive — the First Submit renewal may complete; the row should carry the
   as-of date, and re-checks ride any dated table amendment.
2. Certification status is a **presence-floor credential, not a scoring input**: no FAIR
   sub-principle scores CTS certification. It informs how much weight the by-construction
   inference can bear (the infrastructure-layer principle), and belongs in the table's
   evidence column, not in the score.
3. Future rows (Dataverse, Australian Data Archive, Figshare, Dryad) get the same
   two-registry check at addition time; the CTS GraphQL queries above are repeatable
   verbatim, and the SPA-shell failure mode confirms verification-note item 12's
   rendering-or-API requirement for register checks.
