# Environment Specification

## Key et al. 2024 Reproduction

### Software Versions

| Component | Version | Source |
|-----------|---------|--------|
| R | 4.3.2 (2023-10-31) | rocker/r-ver:4.3.2 Docker image |
| Docker base | rocker/r-ver:4.3.2 | Docker Hub |
| Host OS | Ubuntu (Linux 6.16.9) | Local execution |

### System Dependencies Added to Docker

None required. The Optimal Linear Estimation (OLE) function uses only base
R (matrix algebra, gamma function, solve). No external R packages or system
libraries needed.

### R Package Dependencies

None. The OLE.test function is self-contained, adapted from the `sExtinct`
package but implemented as pure base R. The only non-base dependency in the
author's scripts is `beepr` (audio notifications in mmc2), which is
non-analytical and excluded from this reproduction.

### Data Sources

- **File:** `olduvai-cleavers-key-et-al-2024.csv` (16 KB, 134 records)
  - **Source:** Martin-Ramos (2022/2023) PhD thesis supplementary Excel,
    UCL Discovery (open access, CC BY-NC 4.0)
  - **Citation chain:** Key et al. 2024 → Martin-Ramos 2022/2023
  - **Format:** 134 rows × 24 columns; 5 measurement variables extracted
    (length_mm, breadth_mm, thickness_mm, edge_length_mm, mass_g)
  - **Processing:** Filtered LCT sheet by `LCT SUB TYPE = "Cleaver"`,
    cross-referenced Principal sheet for edge length, converted mass from
    decigrams to grams

- **File:** `key-et-al-2024-paleoindian-points.csv` (42 KB, 1,281 records)
  - **Source:** Buchanan & Hamilton (2021) ESM2.xlsx, Springer static
    content servers (open access)
  - **Citation chain:** Key et al. 2024 → Buchanan & Hamilton 2021
  - **Format:** 1,281 rows × 6 columns (type, length_mm, breadth_mm,
    thickness_mm, mass_g, raw_material). Mass has NAs for many records
    (Clovis mass n=101, E. Clovis n=63, Folsom n=125, Midland n=64)
  - **Processing:** Filtered to 4 target types (Clovis, Eastern Clovis,
    Folsom, Midland), renamed "Width" → "Breadth" to match Key et al.
    terminology

### Data Not Available

10 of 13 datasets used in the paper could not be retrieved:

| Dataset | Records | Access Level | Reason |
|---------|---------|-------------|--------|
| Replica Acheulean handaxes | 500 | Level 3 | PhD thesis closed access |
| Replica Early Archaic points | 45 | Level 4 | Never published |
| Old Park flakes | 173 | Level 3 | Held at Cambridge |
| Boxgrove handaxes | 254 | Level 3 | PhD thesis closed access |
| Sibudu bipolar cores | 131 | Level 3 | Author-held |
| Capuchin flakes | 31 | Level 3 | Author-held |
| Copper tang points | 93 | Level 3 | Author-held |
| Middle Historic bowls | ~1,466 | Level 3 | Monograph only |
| Neolithic Impressed Ware | ~54 | Level 3 | Monograph only |
| Neolithic Stentinello | ~146 | Level 3 | Monograph only |

Geometric microliths (n=734) were partially available (Level 0) but the
full morphometric dataset matching Key et al.'s sample sizes (Phase A
n=344, Phase B n=390) was not found in the public GitHub repositories.
See `data-availability-inventory.md` for complete provenance analysis.

### Notes

- **R version selection:** R 4.3.2 chosen as a contemporary version for
  the 2024 publication date. Paper does not specify R version, provide
  sessionInfo, or include renv.lock.
- **Determinism:** The Main OLE script (mmc1) is fully deterministic. The
  Randomised (mmc2) and Resampling (mmc3) scripts use stochastic processes
  without `set.seed()`, preventing exact reproduction even with correct data.
- **Docker build:** Single iteration, no failures. Minimal image (base R
  only, no additional packages).
