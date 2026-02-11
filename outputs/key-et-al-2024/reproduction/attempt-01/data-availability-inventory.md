# Data Availability Inventory: Key et al. 2024

**Paper:** Key, A. et al. (2024). Identifying accurate artefact morphological ranges
using optimal linear estimation: Method validation, case studies, and code.
*Journal of Archaeological Science*, 162, 105921.

**Date:** 2026-02-10
**Assessor:** Claude (machine-accessible reproduction attempt)

---

## Summary Metrics

### Dataset-Count Availability

| Access Level | Datasets | Percentage |
|---|---|---|
| Level 0 (direct download) | 3 of 13 | 23.1% |
| Level 1 (programmatic extraction) | 0 of 13 | 0% |
| Level 2 (manual steps required) | 0 of 13 | 0% |
| Level 3 (exists but inaccessible) | 9 of 13 | 69.2% |
| Level 4 (never published) | 1 of 13 | 7.7% |

### Record-Weighted Availability

| Category | Records | Percentage |
|---|---|---|
| Available (Level 0) | 2,149 | 42.6% |
| Not available (Level 3-4) | 2,893 | 57.4% |
| **Total unique artefacts** | **5,042** | 100% |

### Projected vs Actual Reproducibility

| Metric | Research-Assessor Projection | Actual |
|---|---|---|
| FAIR score | 60% (9/15) | — |
| Reproducibility score | 68/100 | — |
| Execution feasibility | needs_work | — |
| Record-weighted data availability | not assessed | 42.6% |
| Dataset-count data availability | not assessed | 23.1% |

**Finding:** The research-assessor pipeline scored reproducibility at 68/100 and
flagged execution feasibility as "needs_work", which directionally anticipated
the difficulty. However, the pipeline did not decompose data availability by
source dataset or weight by record count. The actual situation — 77% of
datasets inaccessible, comprising 57% of total records — is worse than the
68/100 score suggests. The pipeline should incorporate a data-provenance
trace for papers that aggregate external datasets.

---

## Access Level Taxonomy

| Level | Definition |
|---|---|
| **0** | Direct download (CSV/ZIP from repository with DOI) |
| **1** | Programmatic extraction from open paper (HTML tables, API) |
| **2** | Available but requires manual steps (registration, paywall you have access to, PDF table extraction) |
| **3** | Exists but inaccessible (closed thesis, paywalled monograph, unpublished but held by authors) |
| **4** | Not found / never published |

---

## Complete Dataset Inventory

### Validation Datasets (Tables 2-4, Figures 3-5)

#### 1. Replica Acheulean Handaxes

- **Records:** 500 artefacts, 8 variables (length, breadth, thickness, mass,
  elongation, refinement, PC1, PC2)
- **Source:** Key & Lycett (2017); Key (2015) PhD thesis, University of Kent
- **Access Level:** 3
- **Citation-chain depth:** 1 hop (Key et al. 2024 → Key & Lycett 2017)
- **Effort to retrieve:** Author contact required (ak2389@cam.ac.uk)
- **Status:** PhD thesis permanently closed access at Kent Academic Repository.
  No data deposit on Zenodo, Figshare, OSF, or any other platform.
  The `mmc4.csv` supplement in Key et al. 2024 is an empty template
  (header row only, 75 bytes) — likely a publishing error.
- **Blocks:** Tables 2, 4; Figures 3A-D, 4, 5; Supplementary Tables 1, 3

#### 2. Replica Early Archaic Points

- **Records:** 45 artefacts, 5 variables (length, shoulder breadth, neck breadth,
  basal breadth, thickness)
- **Source:** Produced by M.I. Eren in 2021; curated at Kent State University
  Experimental Archaeology Laboratory
- **Access Level:** 4
- **Citation-chain depth:** 0 hops (original data in Key et al. 2024)
- **Effort to retrieve:** Author contact required; data has never been published
  anywhere. Paper states these points "have not been used in any other
  published studies."
- **Status:** Never deposited. Physical artefacts at Kent State.
- **Blocks:** Tables 3, 4; Figures 3E-F, 4, 5; Supplementary Table 2

### Case Study Datasets (Tables 5-7, Figures 6-8)

#### 3. Old Park Flakes (Lower Palaeolithic)

- **Records:** 173 artefacts, 4 variables (length, width, thickness, mass)
- **Source:** Key et al. (2022), *R. Soc. Open Sci.* 9(6), 211904
- **Access Level:** 3
- **Citation-chain depth:** 1 hop
- **Effort to retrieve:** Author contact required. Figshare collection for the
  2022 paper (DOI: 10.6084/m9.figshare.c.6032515) contains only 3D models
  and dating data — no morphometric measurements.
- **Status:** Data held at University of Cambridge, not deposited.
- **Blocks:** Table 5 (Old Park rows); Figure 8A

#### 4. Boxgrove Handaxes (Lower Palaeolithic)

- **Records:** 254 artefacts (size metrics), 214 (shape/PC data), 7 variables
- **Source:** Key (2015) PhD thesis; Key & Lycett (2017)
- **Access Level:** 3
- **Citation-chain depth:** 1 hop
- **Effort to retrieve:** Author contact required. Same closed-access thesis as
  Dataset 1. Alternative partial dataset: Clark et al. 2024 (PLoS ONE) has 30
  Boxgrove handaxes with different variables — not compatible.
- **Status:** Not deposited. Closed thesis.
- **Blocks:** Table 5 (Boxgrove rows); Figure 8B

#### 5. Olduvai Bed IV Cleavers

- **Records:** 134 artefacts, 5 variables (length, breadth, thickness, edge
  length, mass)
- **Source:** Martin-Ramos (2022/2023) PhD thesis, University College London
- **Access Level:** 0
- **Citation-chain depth:** 1 hop
- **Effort to retrieve:** Downloaded directly from UCL Discovery.
  Supplementary Excel file from open-access thesis (CC BY-NC 4.0).
  Required filtering LCT sheet by `LCT SUB TYPE = "Cleaver"` and
  cross-referencing Principal sheet for edge length. Mass stored in
  decigrams (conversion needed).
- **Verified:** All 5 variables match Table 5 summary statistics exactly.
- **Files:** `/tmp/key-et-al-data/olduvai-cleavers/olduvai-cleavers-key-et-al-2024.csv`
- **Blocks:** Table 5 (Olduvai rows); Figure 8B

#### 6. Sibudu Bipolar Cores (Middle Stone Age)

- **Records:** 131 artefacts, 4 variables (length, breadth, thickness, mass)
- **Source:** de la Pena & Wadley (2014), *PLoS ONE* 9(7), e101534
- **Access Level:** 3
- **Citation-chain depth:** 1 hop
- **Effort to retrieve:** Author contact required (de la Pena, Cambridge).
  PLoS ONE paper (2014) predates mandatory data sharing policy. Only
  summary statistics in Table 7 (and varying n per variable: 130/129/131/130).
- **Status:** Individual specimen data never deposited.
- **Blocks:** Table 5 (Sibudu rows)

#### 7. Capuchin Stone-on-Stone Flakes

- **Records:** 31 artefacts, 4 variables (length, breadth, thickness, mass)
- **Source:** Proffitt et al. (2016), *Nature* 539, 85-88
- **Access Level:** 3
- **Citation-chain depth:** 1 hop
- **Effort to retrieve:** Author contact required (Proffitt, ICArEHB Algarve).
  Nature Extended Data Table 2 has aggregated statistics only, not individual
  measurements. Supplementary Information PDF (13 pp) is narrative.
- **Status:** Individual specimen data never deposited.
- **Blocks:** Table 5 (Capuchin rows); Figure 8A

#### 8. Copper Socketed Tang Points (Old Copper Culture)

- **Records:** 93 artefacts, 4 variables (length, breadth, thickness, mass)
- **Source:** Bebber & Key (2022), *Am. Antiq.* 87(2), 267-283; Bebber (2021)
- **Access Level:** 3
- **Citation-chain depth:** 1 hop
- **Effort to retrieve:** Author contact required (Bebber, Kent State). Data
  collected from museum collections at 4 institutions. No supplementary
  data in Bebber 2021 (Springer). Not on tDAR, OSF, Zenodo, or Figshare.
- **Status:** Individual specimen data never deposited.
- **Blocks:** Table 5 (Copper tang rows)

#### 9. Middle Historic Ceramic Bowls (Bannu Basin, Pakistan)

- **Records:** ~1,466 artefacts (rim diameter n=1,466; rim thickness n=1,463;
  base diameter n=77; height n=59)
- **Source:** Petrie (2020), *Resistance at the Edge of Empires*, Oxbow Books
- **Access Level:** 3
- **Citation-chain depth:** 1 hop
- **Effort to retrieve:** Author contact required (Petrie, Cambridge — co-author
  with CRediT role "Resources"). Data exists digitally but locked in
  monograph. No data deposit on any platform.
- **Status:** Monograph only. Largest single dataset in the paper.
- **Blocks:** Table 5 (Middle Historic rows); Figure 8C

#### 10. Neolithic Impressed Ware Pots (Penitenzeria, Italy)

- **Records:** ~54 artefacts (rim diameter n=38; rim thickness n=54)
- **Source:** Robb (2007), *The Early Mediterranean Village*, Cambridge UP
- **Access Level:** 3
- **Citation-chain depth:** 1 hop
- **Effort to retrieve:** Author contact required (Robb, Cambridge — co-author
  with CRediT role "Resources"). Data locked in monograph.
- **Status:** Monograph only.
- **Blocks:** Table 5 (Impressed Ware rows)

#### 11. Neolithic Stentinello Pots (Penitenzeria, Italy)

- **Records:** ~146 artefacts (rim diameter n=114; rim thickness n=146)
- **Source:** Robb (2007), same monograph as Dataset 10
- **Access Level:** 3
- **Citation-chain depth:** 1 hop
- **Effort to retrieve:** Same as Dataset 10.
- **Status:** Monograph only.
- **Blocks:** Table 5 (Stentinello rows); Figure 8C

#### 12. Paleoindian Projectile Points (4 types)

- **Records:** 1,281 artefacts (Clovis n=810, Eastern Clovis n=228, Folsom
  n=179, Midland n=64), 4 variables (length, breadth, thickness, mass —
  mass incomplete for some types)
- **Source:** Buchanan & Hamilton (2021), *J. Archaeol. Method Theor.* 28, 580-602
- **Access Level:** 0
- **Citation-chain depth:** 1 hop
- **Effort to retrieve:** Downloaded directly from Springer Electronic
  Supplementary Material (ESM2.xlsx). Required filtering to 4 target types
  and renaming "Width" → "Breadth" to match Key et al. terminology.
- **Verified:** All 16 summary statistics (4 types x 4 variables) match Table 6
  exactly.
- **Files:** `/tmp/key-et-al-data/paleoindian-points/key-et-al-2024-paleoindian-points.csv`
- **Blocks:** Table 6; Figure 7

#### 13. Geometric Microliths (2 phases)

- **Records:** ~734 artefacts (Phase A n=344, Phase B n=390), 7 variables
  (length, breadth, thickness, area, PC1, PC2 — plus metadata)
- **Source:** Garcia-Puchol et al. (2023), *Quat. Int.* 677-678, 51-64;
  Cortell-Nicolau et al. (2020), *Archaeol. Anthropol. Sci.* 12, 186
- **Access Level:** 0
- **Citation-chain depth:** 1-2 hops
- **Effort to retrieve:** Downloaded from GitHub repositories
  (acortell3/Geometrics_Cocina and acortell3/GS_GM_AAS). CSVs have
  formatting issues (no newline separators in phase files). Sample size
  discrepancies vs Key et al. (Phase A: 345 Cocina vs 344 stated; Phase B:
  417 Cocina vs 390 stated) suggest undocumented filtering criteria.
  The `gs-data.csv` (336 records) has the richest variable set including
  length, width, max thickness, and area.
- **Partially verified:** Cocina record counts close but not exact matches.
- **Files:** `/tmp/key-et-al-data/geometric-microliths/` (7 CSV files from 3 repos)
- **Blocks:** Table 7

---

## Supplementary Materials Inventory

The paper itself provides 5 supplementary files via Elsevier CDN:

| File | Contents | Data? |
|---|---|---|
| mmc1.zip | R script: Main OLE analysis (67 lines) | Code only |
| mmc2.zip | R script: Randomised duplicate handling (213 lines) | Code only |
| mmc3.zip | R script: Resampling validation (83 lines) | Code only |
| mmc4.csv | CSV template — **header row only, zero data rows** (75 bytes) | Empty |
| mmc5.docx | Supplementary Tables 1-3, Figures 1-3 (validation results) | Summary stats only |

**Critical finding:** `mmc4.csv` appears to be a publishing error. The file contains
column headers (`mass,length,width,thickness,circumference,elongationindex,refinementindex`)
but no data. The header columns also do not match Table 1 variables (missing PC1, PC2;
includes circumference which is not mentioned in the paper). This strongly suggests the
data was intended to be included but was not.

---

## Additional Reproducibility Concerns

### Missing Random Seeds

Three scripts use stochastic processes without `set.seed()`:

| Script | Stochastic Operation | Affected Results |
|---|---|---|
| mmc3 (Resampling) | `sample()` — 10,000 random subsamples | Tables 2-3; Supplementary Tables 1-2 |
| mmc2 (Randomised) | `rnorm()` — 1,000 jittered iterations | Table 7 |
| mmc3 (Resampling) | CI coverage calculation | Table 4; Figures 4-5 |

Even with perfect data, these results can only be verified within expected
variance (median values across thousands of iterations should be similar
but not identical).

### Script Design Issues

- All scripts use `"###file location###"` placeholder paths — no
  parameterisation or command-line arguments
- mmc2 (Randomised script) has Phase B data loading commented out
  (line 132: `#datalist_B <- read.csv(...)`) — Phase B expects `datalist_B`
  to exist in the R workspace from a prior interactive step
- The `beepr` package (mmc2 only) is used for audio notifications — non-essential
  for reproduction but will cause an error if not installed

---

## Reproducibility by Paper Section

| Paper Section | Tables/Figures | Data Available? | Reproducible? |
|---|---|---|---|
| Validation (replica handaxes) | Tables 2, 4; Figs 3A-D, 4, 5 | No (Level 3) | No |
| Validation (archaic points) | Tables 3, 4; Figs 3E-F, 4, 5 | No (Level 4) | No |
| Case studies: Olduvai | Table 5 (partial) | Yes (Level 0) | Yes (deterministic) |
| Case studies: Paleoindian | Table 6; Fig 7 | Yes (Level 0) | Yes (deterministic) |
| Case studies: Microliths | Table 7 | Partial (Level 0, n discrepancy) | Partial (stochastic) |
| Case studies: 7 others | Table 5 (partial); Figs 6, 8 | No (Level 3) | No |
| OLE function correctness | N/A | N/A | Yes (code review) |

---

## Record-Count Detail

| Dataset | n (artefacts) | Access Level | Available? |
|---|---|---|---|
| Replica handaxes | 500 | 3 | No |
| Replica archaic points | 45 | 4 | No |
| Old Park flakes | 173 | 3 | No |
| Boxgrove handaxes | 254 | 3 | No |
| Olduvai cleavers | 134 | 0 | **Yes** |
| Sibudu bipolar cores | 131 | 3 | No |
| Capuchin flakes | 31 | 3 | No |
| Copper tang points | 93 | 3 | No |
| Middle Historic bowls | 1,466 | 3 | No |
| Neolithic Impressed Ware | 54 | 3 | No |
| Neolithic Stentinello | 146 | 3 | No |
| Paleoindian points | 1,281 | 0 | **Yes** |
| Geometric microliths | 734 | 0 | **Yes** |
| **Total** | **5,042** | | |
| **Available** | **2,149** | | **42.6%** |
| **Not available** | **2,893** | | **57.4%** |

---

## Data Provenance Pattern

All 13 datasets are exactly 0-1 citation hops from Key et al. 2024. The paper
does not use data from deeply nested citation chains. Instead, the pattern is:

- **6 datasets from co-authors:** Old Park (Key), Boxgrove (Key), replica
  handaxes (Key), Sibudu (de la Pena), Middle Historic bowls (Petrie),
  Neolithic pots (Robb) — all Level 3, none deposited
- **4 datasets from external collaborators:** Olduvai (Martin-Ramos thesis),
  Paleoindian (Buchanan & Hamilton), capuchin (Proffitt), copper tang
  (Bebber) — mixed levels
- **2 datasets from open repositories:** geometric microliths (Cortell-Nicolau
  GitHub), Paleoindian (Buchanan & Hamilton Springer ESM)
- **1 dataset never published:** replica archaic points (Eren, unpublished)

The strongest predictor of data availability is whether the data collector
published it independently with a data-sharing mandate. The three accessible
datasets (Olduvai, Paleoindian, microliths) were all deposited as part of
other publications with open-access or open-data requirements (UCL thesis,
Springer ESM, GitHub for journal submission). Co-author-held data was
universally inaccessible.
