# Corpus Assessment Profile

**Generated:** 2025-11-16 07:24:58
**Corpus Size:** 10 papers

---

## Corpus Description

**Publication years:** 2005-2024

**Papers in corpus:**

1. Simon E. Connor et al. (2013): Environmental conditions in the SE Balkans since the Last Glacial Maximum: New evidence from the Straldzha Mire, Bulgaria
2. Martin Eftimoski et al. (2017): The impact of land use and depopulation on burial mounds in the Kazanlak Valley, Bulgaria: An ordered logit predictive model
3. Sandra Penske et al. (2023): Early contact between late farming and pastoralist societies in southeastern Europe
4. Shawn A. Ross et al. (2005): Barbarophonos: Language and Panhellenism in the Iliad
5. Shawn A. Ross et al. (2021): Introducing Preregistration of Research Design to Archaeology
6. Shawn A. Ross et al. (2009): Remote Sensing and Archaeological Prospection in Apulia, Italy
7. Adela Sobotkova et al. (2016): Measure Twice, Cut Once: Cooperative Deployment of a Generalized, Archaeology-Specific Field Data Collection System
8. Adela Sobotkova et al. (2021): Deploying an Offline, Multi-User, Mobile System for Digital Recording in the Perachora Peninsula, Greece
9. Adela Sobotkova et al. (2023): Creating large, high-quality geospatial datasets from historical maps using novice volunteers
10. Adela Sobotkova et al. (2024): Validating predictions of burial mounds with field data: the promise and reality of machine learning

---

## Corpus-Wide Metric Statistics

| Metric | Mean | Median | StDev | Min | Max | Range |
|--------|------|--------|-------|-----|-----|-------|
| ESD (Evidential Support Density) | 2.32 | 1.25 | 1.96 | 0.77 | 6.60 | 5.83 |
| TCI (Transparency Completeness) | 0.99 | 1.00 | 0.02 | 0.94 | 1.00 | 0.06 |
| SCS (Scope Constraints) | 7.30 | 7.50 | 4.69 | 1.00 | 17.00 | 16.00 |
| RTI (Robustness Triangulation) | 2.26 | 2.53 | 1.24 | 0.22 | 3.81 | 3.59 |
| RIS (Replicability Infrastructure) | 2.80 | 3.00 | 1.87 | 0.00 | 6.00 | 6.00 |
| PGCS (PID Connectivity) | 2.80 | 2.00 | 2.78 | 1.00 | 10.00 | 9.00 |
| FCS (FAIR Compliance) | 11.50 | 11.50 | 2.51 | 8.00 | 15.00 | 7.00 |
| MDD (Methods Documentation) | 187.07 | 174.70 | 80.95 | 104.60 | 386.30 | 281.70 |

---

## Detailed Metric Analysis

### ESD: Evidential Support Density

**Corpus mean:** 2.32
**Corpus median:** 1.25
**Standard deviation:** 1.96
**Range:** 0.77 - 6.60

**Distribution:** Right-skewed (mean > median). Most papers have low ESD, with some high-ESD outliers.

**ESD measures:** Ratio of claims to evidence items (lower is better, more evidence per claim).

**Corpus-specific interpretation:** The mean of 2.32 indicates more claims than evidence on average, suggesting some papers may need stronger empirical support. The wide range (0.77-6.60) shows substantial variation between papers, providing good discriminating power for this metric.

**Example papers:**

- **Low ESD (best):** Environmental conditions in the SE Balkans since t... (2013, score=0.77)
- **Moderate ESD:** Remote Sensing and Archaeological Prospection in A... (2009, score=1.21)
- **High ESD (needs review):** Introducing Preregistration of Research Design to ... (2021, score=6.6)

⚠️ **Note:** ESD counts items, not quality. A single strong evidence item may be more valuable than many weak ones. High ESD may reflect appropriate caution rather than weak research.

---

### TCI: Transparency Completeness Index

**Corpus mean:** 0.99
**Corpus median:** 1.00
**Standard deviation:** 0.02
**Range:** 0.94 - 1.00

**Variance:** Very low variance. Corpus is homogeneous for RDMAP coverage.

**TCI measures:** Number of Research Design and Methods Assessment Protocol (RDMAP) items documented, relative to expected minimums (2 research designs, 5 methods, 8 protocols; 0-1 scale, higher is better).

**Corpus-specific interpretation:** The very high mean (0.99) and narrow range (0.94-1.00) indicate this corpus has uniformly strong methodological documentation, with all papers meeting or exceeding expected RDMAP thresholds. This limits TCI's ability to distinguish between papers in this corpus. Note that TCI measures documentation *completeness* (how many RDMAP items), not *quality* (how detailed each item is).

**Example papers:**

- **Low TCI:** The impact of land use and depopulation on burial ... (2017, score=0.94)
- **Moderate TCI:** Remote Sensing and Archaeological Prospection in A... (2009, score=1.0)
- **High TCI:** Validating predictions of burial mounds with field... (2024, score=1.0)

⚠️ **Note:** TCI measures documentation completeness (how many RDMAP items), not quality (how detailed each item is). Expected minimums are arbitrary bootstrapping thresholds, not validated standards.

---

### SCS: Scope Constraint Score

**Corpus mean:** 7.30
**Corpus median:** 7.50
**Standard deviation:** 4.69
**Range:** 1 - 17

**Papers with no limitations extracted:** 0/10 (0%)


**SCS measures:** Number of explicit limitation, qualification, or scope constraint statements in claims (count, higher indicates more transparent boundary acknowledgement).

**Corpus-specific interpretation:** All papers in this corpus acknowledge limitations (mean=7.3, median=7.5). Remember: SCS counts limitation statements, not their quality or severity. A single serious unaddressed limitation may be more concerning than many trivial acknowledged limitations.

**Example papers:**

- **Few limitations:** Early contact between late farming and pastoralist... (2023, score=1)
- **Moderate limitations:** Creating large, high-quality geospatial datasets f... (2023, score=8)
- **Many limitations:** Measure Twice, Cut Once: Cooperative Deployment of... (2016, score=17)

⚠️ **Note:** High SCS doesn't necessarily mean better research. Review limitation quality, not just quantity.

---

### RTI: Robustness Triangulation Index

**Corpus mean:** 2.26
**Corpus median:** 2.53
**Standard deviation:** 1.24
**Range:** 0.22 - 3.81

**Overall diversity:** Moderate-high (mean 2.0-3.0). Papers show good methodological triangulation.

**RTI measures:** Diversity of evidence types using Shannon diversity index (0-3+ typical range, higher indicates more methodological triangulation).

**Corpus-specific interpretation:** The mean of 2.26 suggests strong methodological triangulation, with papers drawing on diverse evidence types to support claims.

**Example papers:**

- **Low diversity:** Barbarophonos: Language and Panhellenism in the Il... (2005, score=0.22)
- **Moderate diversity:** Remote Sensing and Archaeological Prospection in A... (2009, score=2.53)
- **High diversity:** Deploying an Offline, Multi-User, Mobile System fo... (2021, score=3.81)

⚠️ **Note:** RTI measures evidence type diversity, not appropriateness. Some research questions legitimately require focused mono-method approaches. High RTI doesn't automatically mean better research.

---

### RIS: Replicability Infrastructure Score

**Corpus mean:** 2.80 / 10
**Corpus median:** 3.00 / 10
**Standard deviation:** 1.87
**Range:** 0 - 6

**Overall infrastructure:** Minimal (mean = 28% of maximum). Corpus has poor replicability infrastructure.

**RIS measures:** Availability of Persistent Identifiers (PIDs) and data/code/materials sharing infrastructure (0-10 scale: paper DOI, author ORCIDs, dataset PIDs, software PIDs, data/code availability statements, supplementary materials, preregistration).

**Corpus-specific interpretation:** This corpus scores 28% of maximum RIS, indicating limited replicability infrastructure. Most papers lack PIDs for datasets/software and formal sharing statements.

**Example papers:**

- **Minimal infrastructure:** Remote Sensing and Archaeological Prospection in A... (2009, score=0)
- **Moderate infrastructure:** Early contact between late farming and pastoralist... (2023, score=4)
- **Strong infrastructure:** Deploying an Offline, Multi-User, Mobile System fo... (2021, score=6)

⚠️ **Note:** RIS measures infrastructure availability, not actual use or quality. PIDs and repositories don't guarantee data/code are complete, well-documented, or usable. Low RIS for older papers may reflect pre-FAIR era publication norms.

---

### PGCS: PID Graph Connectivity Score

**Corpus mean:** 2.80 / 10
**Corpus median:** 2.00 / 10
**Standard deviation:** 2.78
**Range:** 1 - 10

**Overall connectivity:** 28% of exemplary connectivity.

**PGCS measures:** Number of Persistent Identifiers (PIDs) connected to the research (0-10 scale: paper DOI, author ORCIDs, dataset PIDs, software PIDs, sample PIDs, project PIDs, vocabulary PIDs; higher indicates stronger PID graph connectivity).

**Corpus-specific interpretation:** This corpus averages 2.8 PIDs per paper (28% of exemplary connectivity), indicating emerging PID adoption. Some papers include author ORCIDs or software repositories, but dataset/sample/project PIDs are rare.

**Example papers:**

- **Minimal connectivity:** Environmental conditions in the SE Balkans since t... (2013, score=1)
- **Moderate connectivity:** Measure Twice, Cut Once: Cooperative Deployment of... (2016, score=2)
- **Strong connectivity:** Deploying an Offline, Multi-User, Mobile System fo... (2021, score=10)

⚠️ **Note:** PGCS counts PIDs, not connectivity quality. PIDs must be properly linked and maintained to create functional knowledge graphs. Score depends heavily on publication year and disciplinary norms.

---

### FCS: FAIR Compliance Score

**Corpus mean:** 11.50 / 15
**Corpus median:** 11.50 / 15
**Standard deviation:** 2.51
**Range:** 8 - 15

**Overall FAIR compliance:** Strong (mean = 77% of maximum).

**FCS measures:** Compliance with FAIR (Findable, Accessible, Interoperable, Reusable) principles across four dimensions (0-15 scale: Findable 0-4, Accessible 0-4, Interoperable 0-3, Reusable 0-4; higher indicates stronger FAIR compliance).

**Corpus-specific interpretation:** This corpus scores 77% of maximum FAIR compliance (mean=11.5/15), indicating strong FAIR compliance. Most papers are findable via PIDs, openly accessible, use standard formats, and provide rich reusable metadata. The wide range (7 points) indicates highly variable FAIR practices, likely reflecting temporal trends or different publication venues.

**Example papers:**

- **Low FAIR compliance:** Barbarophonos: Language and Panhellenism in the Il... (2005, score=8)
- **Moderate FAIR compliance:** Validating predictions of burial mounds with field... (2024, score=12)
- **High FAIR compliance:** Deploying an Offline, Multi-User, Mobile System fo... (2021, score=15)

⚠️ **Note:** FCS assesses surface-level FAIR indicators, not deep compliance. Metadata richness, licence clarity, and actual reusability require qualitative review. Temporal bias: older papers scored before FAIR principles were articulated.

---

### MDD: Methods Documentation Density

**Corpus mean:** 187.1 chars/item
**Corpus median:** 174.7 chars/item
**Standard deviation:** 81.0
**Range:** 104.6 - 386.3

**Overall documentation density:** Moderate (mean 100-200 chars/item). Paragraph-length RDMAP descriptions typical.

**MDD measures:** Mean character length of Research Design and Methods Assessment Protocol (RDMAP) item descriptions (continuous scale; higher indicates more detailed methodological documentation per item).

**Corpus-specific interpretation:** The mean of 187.1 chars/item suggests this corpus provides moderate methodological detail, typically paragraph-length descriptions per RDMAP item. The wide range (105-386) indicates substantial variation in documentation practices between papers. Note: MDD measures documentation *density* (how detailed), complementing TCI which measures *completeness* (how many items).

**Example papers:**

- **Sparse documentation:** Early contact between late farming and pastoralist... (2023, score=104.6)
- **Moderate documentation:** Creating large, high-quality geospatial datasets f... (2023, score=189.9)
- **Detailed documentation:** Deploying an Offline, Multi-User, Mobile System fo... (2021, score=386.3)

⚠️ **Note:** MDD measures verbosity, not clarity or usefulness. Long descriptions may be verbose rather than informative; terse descriptions may be precise rather than incomplete. Complements TCI (completeness).

---

## Corpus-Level Observations

### Homogeneity vs Heterogeneity

**Overall homogeneity:** Moderate. Papers show some variation but cluster around typical values.

**Low-variance metrics (CV < 0.1):** TCI
- These metrics show little variation across corpus. May not be discriminating in this sample.


---

## Interpretation Notes

### Limitations of This Corpus Profile

- **Small sample (n=10)**: Statistics are unstable. Percentiles may shift dramatically with additional papers.
- **No ground truth**: Metrics not validated against external quality assessments. High scores may reflect extraction quality, not research quality.
- **Corpus-specific patterns**: Observations may not generalise to other domains, genres, or time periods.
- **Extraction dependency**: All metrics depend on extraction quality and granularity decisions.

### Using This Profile

This profile should be used to:

1. **Understand corpus characteristics** before interpreting individual paper scores
2. **Identify metrics with good discriminating power** (high variance) vs poor power (low variance)
3. **Calibrate expectations** for what constitutes "typical" vs "exceptional" scores
4. **Compare corpora** (if multiple corpus profiles generated)
5. **Inform metric refinement** (identify problematic metrics needing adjustment)

Do NOT use this profile to:

- Make definitive claims about research quality
- Compare papers from different corpora without controlling for corpus characteristics
- Treat corpus means as universal quality thresholds

---

**Profile generated:** 2025-11-16 07:24:58

**Metrics reference:** See `docs/assessment-guide/credibility-metrics-reference.md`

**Individual scorecards:** See `outputs/{paper-id}/metrics-scorecard.md`
