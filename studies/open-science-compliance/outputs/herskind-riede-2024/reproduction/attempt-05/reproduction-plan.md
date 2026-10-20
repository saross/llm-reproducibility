# Reproduction plan — herskind-riede-2024

Generated from `reproduction-plan.json` by `scripts/reproduction-lane.py persist-plans`; do not edit (the approval binds to the JSON's sha256).

- **Run:** gate-1-3-2-planner-pilot-2026-10 (workflow run `wf_88429e16-a85`, agent `ad5e8bf0d54af5ebb`)
- **Launch commit:** `904d70d7acbeafc94110f4a5f65f4a66c6fb90fb`; effort `high`
- **Status:** OK
- **Paper:** A computational linguistic methodology for assessing semiotic structure in prehistoric art and the meaning of southern Scandinavian Mesolithic ornamentation — doi:10.1016/j.jas.2024.105969
- **Reproduction type:** C — The authors supply one annotated R script (S2.R) written to be run interactively ('run the code all at once ... or go through it one line at a time'). There is no container or lockfile, but README.txt states R 4.3.2 and seven package versions. Statement 27 (extrafont::font_import for the proprietary Gill Sans MT font) produces an error the authors note and ignore, so an unwrapped Rscript run may halt there. Plots are autoprinted, Tables 1 and 2 were copied by hand from console output into Word, and Figs. 3 and 4 were finished in GIMP. Fig. 2's map, Fig. 5, and Table 3 have no code at all. The computational core runs top to bottom in batch once a wrapper adds mechanics only: working directory, graphics device, per-expression error capture, and a declared tolerance for statement 27. Risk assessment: low compute risk, a deterministic pipeline, and moderate build risk (seven pinned CRAN versions on R 4.3.2). The main scoring risks are the code-less targets that need verification aids, and visual comparison of figures assembled outside R.

## Materials

| Name | Kind | Location | Version | Access route | Checksum |
|---|---|---|---|---|---|
| Paper (version of record) | other | /home/shawn/corpora/llm-reproducibility/herskind-riede-2024/vor.pdf | JAS 165 (2024) 105969 | Local corpus store; read directly | sha256:5c60cc3d6fce9f297c44fc62384e0caada1251416066d872ea020feec145fad0 |
| Herskind&Riede_S1.xlsx (data, Supplementary Information S1) | data | https://zenodo.org/api/records/10801706/files/Herskind&Riede_S1.xlsx/content | Zenodo record 10801706 (version 2, published 2024-03-10) | Zenodo REST API, anonymous HTTPS GET (standard protocol, no authentication) | md5:0bcde6d178b5a8f3da80a023a64ff510 |
| Herskind&Riede_S2.R (authors' code, Supplementary Information S2) | code | https://zenodo.org/api/records/10801706/files/Herskind&Riede_S2.R/content | Zenodo record 10801706 (version 2) | Zenodo REST API, anonymous HTTPS GET | md5:6760ccb30ecc1de7c280bc1e0fa182e5 |
| Herskind&Riede_S3.xlsx (precomputed skipgram tables, Supplementary Information S3) | supplement | https://zenodo.org/api/records/10801706/files/Herskind&Riede_S3.xlsx/content | Zenodo record 10801706 (version 2) | Zenodo REST API, anonymous HTTPS GET | md5:812be5456d7e0e2adb97ecb5a975239e |
| README.txt (deposit documentation) | environment | https://zenodo.org/api/records/10801706/files/README.txt/content | Zenodo record 10801706 (version 2) | Zenodo REST API, anonymous HTTPS GET | md5:8b5ef4c5a8c1f75c5d61ed25f799521b |
| Zenodo record metadata (version 2) | other | https://zenodo.org/api/records/10801706 | 2 | Zenodo REST API, anonymous | — |
| rocker/r-ver:4.3.2 base image | environment | docker.io/rocker/r-ver:4.3.2 | 4.3.2 | Docker Hub pull at image build | — |
| CRAN package archive and Posit Public Package Manager dated snapshot | environment | https://packagemanager.posit.co/cran/2024-04-03 ; https://cran.r-project.org/src/contrib/Archive/ | snapshot 2024-04-03 (article first online appearance) | HTTPS at image build only (no runtime installs) | — |

## Environment

- Provided by authors: README.txt in the Zenodo v2 deposit states 'R version: 4.3.2' and lists package versions: extrafont 0.19, data.table 1.15.0, dplyr 1.1.4, ggplot2 3.5.0, readxl 1.4.3, quanteda 3.3.1, and forcats 1.0.0. There is no lockfile, no container, and no transitive-dependency versions. The paper's methods (p. 3) state R v.4.2.2, which conflicts with the README. Code uses the proprietary font 'Gill Sans MT' via extrafont.
- Planned base image: `rocker/r-ver:4.3.2`
- Language version target: R 4.3.2 (README pin; supplied pins take precedence). R 4.2.2 from the paper text is noted and held as the approver's alternative.
- Packages: quanteda 3.3.1 (README pin), readxl 1.4.3 (README pin), ggplot2 3.5.0 (README pin), dplyr 1.1.4 (README pin), data.table 1.15.0 (README pin), forcats 1.0.0 (README pin), extrafont 0.19 (README pin), Unspecified transitive dependencies (e.g., Rttf2pt1, extrafontdb, stringi, Rcpp, RcppParallel, fastmatch, stopwords, cellranger, tibble) from the Posit Package Manager CRAN snapshot of 2024-04-03, the release current at first online appearance, Base R recommended packages (e.g., Matrix) as bundled with R 4.3.2, remotes (build-time only, to install pinned versions with install_version), fontconfig and fonts-dejavu-core (system) as fallback fonts; Gill Sans MT is proprietary and not installed, Version-search cap per invariant 2 corollary: pin, then the preceding release, then the following release; every attempt logged

## Execution steps

1. Retrieve the four Zenodo v2 files (S1.xlsx, S2.R, S3.xlsx, README.txt) by anonymous REST API into the attempt's materials directory; verify each md5 against Zenodo's published checksums; record sha256; log route, steps, and outcome per dataset for L-level assignment. — *expected:* Four files with md5 0bcde6d1..., 6760ccb3..., 812be545..., and 8b5ef4c5...; a retrieval log; the S2.R sha256 487a00a0... recorded as the byte-identity anchor.
2. Write the Dockerfile: FROM rocker/r-ver:4.3.2; point the CRAN repo at the PPM snapshot 2024-04-03; install remotes; remotes::install_version for the seven README pins; install fontconfig and DejaVu fonts; set LANG=en_US.UTF-8. Build through run-container. On a build failure, apply the version-search cap (pin, preceding release, following release) and log each attempt. — *expected:* Built image with digest recorded; environment.md listing R 4.3.2, all package versions, and whether the pins were honoured in full (number of fallbacks).
3. Write the wrapper run-analysis.R (mechanics only, never inside the authors' file). It: copies S1 to a working directory and sets it as wd; sets the default graphics device to a file-based cairo PNG so autoprinted plots never hit the pdf font database; parses S2.R unchanged (sha256 checked before and after); evaluates top-level expressions in the authors' order in the global environment with per-expression error and warning capture, printing visible values as autoprint would; maps each expression to its PART by srcref line; declares an error tolerance only for statement 27 (extrafont::font_import, font registration that enters no result) and logs whether it fired; records PART completion status; saves an RDS snapshot of the global environment at the end of each PART and an RDS list of all visible values. — *expected:* run-analysis.R; a declared-tolerance list containing only S2.R line 27.
4. Run the wrapper in the container via run-container, with no network and the deposit read-only. — *expected:* outputs/: artefact_type_chronology.png, bigramsBYfrequency.png, bigramsBYpmi.png, trigramsBYfrequency.png, trigramsBYpmi.png, quadrigramsBYfrequency.png, quadrigramsBYpmi.png, heatmapPMI.png, Bigrams.csv, Trigrams.csv, Quadrigrams.csv; console log; per-PART status table (P1-P8 completed or failed, with errors); per-PART snapshots; visible-values RDS; tolerance-fired log for line 27.
5. Deterministic stage gate: S2.R byte-identical after the run; every expected artefact exists and is non-empty; record PART completion status; derive each target's credit eligibility from the Q6 dependency map (T01: P1,P3,P4; T02: P1,P3,P5; T04: P1,P2; T05: P1,P3,P5,P6; T06: P1,P3,P5,P6,P7; T08: P1,P3,P5,P6,P7,P8; aid targets: the PARTs whose objects they read). — *expected:* Gate report with per-target section-eligibility flags.
6. Transcribe published values into machine-readable files, double-entered and diffed: Table 1 (130 values), Table 2 (18), Table 3 (50), the Fig. 3 bar labels and 4-dp PMI labels for all six panels (128 bars), the Fig. 4 axis order and boxed cells (count the small boxes in the published figure before any comparison), the Fig. 5 pie compositions, and the named values T09-T17. S3 is read directly from the deposited xlsx. — *expected:* published-values/ files with a zero-difference double-entry check.
7. Write and run compare.R, kept separate from the authors' code. Its sections are: (a) code-produced targets T01, T02, T05, T08 and the T04 bar panel and T06 heatmap cells, compared from snapshots and outputs; (b) clearly labelled VERIFICATION AID blocks (R1/Q5) for T03, the T04 map, the T06 box overlay, T07, and T09-T17, using only read-only lookups in the authors' run objects (data, corpus, freqs, bigrams_subset, bigramsBYpmi$data, Part 7 bigrams) plus documented quanteda, dplyr, and ggplot2 functions, with the pre-stated rules given in the targets. Each inferred rule is first run on its printed-input qualification test. The script also runs a deterministic element-count gate per target (7c). — *expected:* compare.R; per-target comparison tables; element-count gate output (declared count against elements checked); aid outputs labelled as aids.
8. Visual comparisons for T04, T05 (bar lengths), T06, and T07: side-by-side panels of reproduced and published images, assessed against the pre-stated criteria. — *expected:* comparisons/visual/ side-by-side images with a written assessment per element.
9. Write comparisons/comparison-report.md with per-target discrepancy categories, Q6 section-credit status, 7c partial-verification flags, R4 notes (log-base and t=482 text/code inconsistencies; the T13 list of eight against 'nine'), any PAPER_ERROR candidates with the evidence tier named (escalated for human confirmation), coverage = reproduced / 17, and the verdict. Then hand off to fresh-context adversarial review (invariant 4). — *expected:* Comparison report, log.md, environment.md; coverage over the locked denominator of 17 targets.

## Verification targets (17 — the locked denominator on approval)

| Id | Display item | Location | Values | Type | Tolerance | Published values |
|---|---|---|---|---|---|---|
| T01 | Table 1 | p. 4, §3 Results | 130 | deterministic | Deterministic, tolerance 0: each of the 130 integers must be EXACT_MATCH; any difference is a discrepancy (MAJOR_DISCREPANCY unless the 7(a) PAPER_ERROR protocol applies). | Paper text, Table 1 (p. 4), transcribed |
| T02 | Table 2 | p. 6, §3 Results (table placed in §4) | 18 | deterministic | Deterministic, printed to 2 dp: EXACT_MATCH when the reproduced value rounded to 2 dp equals the printed value; WITHIN_PRECISION when \|reproduced - printed\| <= 0.005 but rounding direction differs (half-up vs half-even); any larger difference is a discrepancy. | Paper text, Table 2 (p. 6), transcribed |
| T03 | Table 3 | p. 7, §4 Discussion | 50 | deterministic | Deterministic lookup, tolerance 0: EXACT_MATCH per cell after normalising whitespace, letter case, and quotation marks; motif lists compared as sets. Any other difference is a discrepancy. | Paper text, Table 3 (p. 7), transcribed |
| T04 | Figure 2 | p. 3, §2 Materials and methods | — | visual | Visual (verdicts-and-precision v1.1: scientific content must match; no pixel matching). Bar order, relative lengths, and composition must match; map point pattern and chronology colours must match. Typeface (Gill Sans MT unavailable), projection, basemap, and layout are not scored. A difference caused only by an unpublished cartographic convention is MINOR_DISCREPANCY (R1). | Paper text, Fig. 2 (p. 3), visual |
| T05 | Figure 3 | p. 5, §3 Results | 128 | deterministic | Deterministic: the 128 PMI labels must be EXACT_MATCH as 4-dp strings; bar identity and order exact in every panel; stacked chronology frequencies are integers compared visually against the axis, and any visible difference is a discrepancy. GIMP assembly, typeface, and layout are not scored. | Paper text, Fig. 3 (p. 5) labels transcribed; deposit Herskind&Riede_S3.xlsx as a numeric cross-check |
| T06 | Figure 4 | p. 6, §3 Results | — | visual | Visual for the colour gradient; exact for axis order, cell set, and box membership. A difference caused only by the unpublished treatment of 'Kongemose/Ertebølle' objects, or by the unpublished 'particularly high PMI' threshold for large boxes, is MINOR_DISCREPANCY (R1). Any other box or cell difference is a discrepancy. | Paper text, Fig. 4 (p. 6), visual; deposit Herskind&Riede_S3.xlsx (bigrams sheet) for cell PMI values |
| T07 | Figure 5 | p. 7, §4 Discussion | — | visual | Visual: pie positions and compositions must match (composition is an exact set); patch-coverage checks are visual. Basemap, projection, and legend artwork are not scored; unpublished patch-drawing conventions give MINOR_DISCREPANCY (R1). | Paper text, Fig. 5 (p. 7), visual |
| T08 | Supplementary Information S3 (Herskind&Riede_S3.xlsx: bigrams, trigrams, quadrigrams sheets) | Zenodo record 10801706 v2, file Herskind&Riede_S3.xlsx (three sheets) | 2329 | deterministic | Deterministic: tokens and integers EXACT_MATCH; expected frequency and PMI EXACT_MATCH or WITHIN_PRECISION (equal when rounded to the significant digits stored in the S3 cell, at most 15). Row-order differences confined to tied PMI values are MINOR_DISCREPANCY; any other difference is a discrepancy. | Deposited precomputed reference file Herskind&Riede_S3.xlsx (Zenodo v2, md5 812be5456d7e0e2adb97ecb5a975239e) |
| T09 | Named value: 483 ornamented objects in the corpus | p. 2, §2 ('a total of 483 objects'); p. 3, §2.1 ('the 483 ornamented artefacts are converted into ... equally as many ornamentation strings') | 1 | deterministic | Deterministic, tolerance 0: EXACT_MATCH. | Paper text, pp. 2-3 |
| T10 | Named value: maximum of 15 individual motifs on a single object | p. 3, §2.2 | 1 | deterministic | Deterministic, tolerance 0: the primary value must be EXACT_MATCH (15). | Paper text, p. 3 |
| T11 | Named value: two combinations occur 44 times each (A1-C1 and C1-G1), on approximately 9% of all objects | p. 4, §3 Results | 3 | deterministic | Deterministic: counts and identities EXACT_MATCH; the percentage is WITHIN_PRECISION when it rounds to 9 at integer-percent precision ('approximately 9%'). | Paper text, p. 4 |
| T12 | Named value: A1-G1 is the third most frequent bigram at frequency 28 | p. 4, §3 Results | 1 | deterministic | Deterministic, tolerance 0: EXACT_MATCH for frequency, identity, and rank. | Paper text, p. 4 |
| T13 | Named value: culture-exclusive salient bigrams in Fig. 3b (none Maglemose, one Kongemose B10-F38, nine Ertebølle) | p. 4, §3 Results | 3 | deterministic | Deterministic, tolerance 0: counts EXACT_MATCH; every named identity must be among the exclusive bars of its stated culture. | Paper text, p. 4 (stated counts); Fig. 3b (p. 5) for the R4 check |
| T14 | Named value: highest co-occurrence frequency among the culture-specific salient bigrams is five | p. 4, §3 Results | 1 | deterministic | Deterministic, tolerance 0: EXACT_MATCH. | Paper text, p. 4 |
| T15 | Named value: the cluster's ornament strings occur on ten objects | p. 7, §5 Conclusion ('these ornament strings only occur on ten objects'); also Table 3 caption | 1 | deterministic | Deterministic, tolerance 0: count EXACT_MATCH (10); a set difference is reported as a discrepancy. | Paper text, p. 7 |
| T16 | Named value: all ten objects are antler axes, barring one antler shaft | p. 4, §3 Results ('the ornamentations in question are all applied on antler axes, barring one antler shaft (Table 3)') | 2 | deterministic | Deterministic, tolerance 0: EXACT_MATCH (9 and 1). | Paper text, p. 4; Table 3 |
| T17 | Named value: A1, A24, B10, C1, G1, and H1 are the motifs with the highest individual frequencies | p. 4, §3 Results | 6 | deterministic | Deterministic, tolerance 0: set equality (EXACT_MATCH); any other result is a discrepancy, with ranks reported. | Paper text, p. 4 |

Target descriptions and comparison methods:

- **T01** Frequency distributions of unigrams (individual motifs, n = 230), 13-skip-2-grams (n = 1543), 13-skip-3-grams (n = 4422) and 13-skip-4-grams (n = 8466): 63 (frequency, n) rows (31 unigram, 18 bigram, 9 trigram, 5 quadrigram) plus 4 header totals. *Method:* Execute S2.R unmodified through the wrapper. Part 4 (S2.R lines 222-264) outputs table(freqs) (presence columns data[,31:289], zero columns dropped), table(bigramfreqs), table(trigramfreqs), table(quadrigramfreqs), and the four length() totals; the wrapper captures them as visible values. Compare every (frequency, n) pair and the four totals with the double-entered transcription. Scope: the whole table, 130 values; a deterministic gate confirms 130 elements compared (7c). Credit only if PARTs 1, 3, and 4 complete without error (Q6; Part 4 reads data from P1 and corpus and k from P3). Planning check: the printed n columns sum to the printed headers (230, 1543, 4422, 8466).
- **T02** Summary statistics (maximum, 3rd quartile, mean, median, 1st quartile, minimum) of whole-corpus bigram PMI values for bigrams occurring in each culture complex (Maglemose, Kongemose, Ertebølle), observed frequency >= 3: 6 x 3 = 18 values at 2 dp. *Method:* Part 5 (S2.R lines 265-322) prints summary() of magle/konge/erte_ksngram_subset$PMI. The wrapper captures the full-precision summary objects; compare.R rounds them to 2 dp and maps Max., 3rd Qu., Mean, Median, 1st Qu., and Min. onto the table rows. Scope: all 18 cells; element gate 18 (7c). Credit only if PARTs 1, 3, and 5 complete (Q6). R4: the printed values are the scoring reference. The paper's formula says log2, but S2.R lines 174, 186, and 197 use natural log(), and t is hard-coded as 482 where the text defines t as the total number of objects. These text/code inconsistencies are reported and never used to rescore. If the reproduced values disagree with the printed ones, the 7(a) PAPER_ERROR protocol applies and the finding escalates. S3's bigram sheet is an additional cross-check of the underlying PMI values.
- **T03** The ten objects in Fig. 5 bearing the most salient motif collocations: site, region, artefact type, motifs, and figure number in Płonka (2003) for each of 10 rows. *Method:* No authors' code produces Table 3. A labelled verification aid (R1/Q5) in compare.R does a read-only lookup in `data` (S1 as read by the authors' Part 1, from the P1 snapshot), matching each row by Site and Płonka figure number (S1 'Figure'). For each row it compares Region (S1 'Region'), artefact type (S1 'Material' + 'Artefact type'), the motif set (S1 'Motifs' slot columns P:AD, order-insensitive), and Figure. Scope: 10 rows x 5 columns = 50 values; element gate 50 (7c). Row number # is an index into Fig. 5 and is not scored. Credit only if PART 1 completes (Q6).
- **T04** Two panels. Left: horizontal bars of 18 artefact-type levels (axe ... slotted point, other) stacked by four chronology levels (Maglemose, Kongemose, Kongemose/Ertebølle, Ertebølle), x axis 0-100. Right: map of all South Scandinavian ornamented objects coloured by chronology. *Method:* Bar panel: produced by PART 2 (S2.R lines 33-75; ggsave artefact_type_chronology.png). Compare visually with the published panel for bar order, relative lengths against the 0-100 axis, and chronology composition, and report the counts behind the plot (table of Artefact_Type x Chronology from the authors' DS object). Map panel: README says the coordinate columns were used to produce the map, but S2.R contains no map code. A labelled verification aid (R1/Q5) plots Coord.Long/Coord.Lat from `data` with ggplot2::geom_point coloured by Chronology under coord_quickmap(), and the point distribution and colours are compared visually. Scope: 18 bars (up to 4 segments each) plus one point per S1 object with non-missing coordinates (count recorded at run); element gate on both (7c). Basemap, scale bar, and north arrow are excluded as non-data elements (see exclusions). Credit only if PARTs 1 and 2 complete (Q6).
- **T05** Six panels of chronology-stacked bars with 4-dp PMI labels: (a) 21 most frequent bigrams (observed > 9); (b) 21 bigrams by highest PMI (observed > 2); (c) 23 most frequent trigrams (observed > 4); (d) 23 trigrams by highest PMI; (e) 20 most frequent quadrigrams (observed > 2); (f) 20 quadrigrams by highest PMI. 128 bars in total. *Method:* Produced by PART 6 (S2.R lines 323-625; ggsave lines 615-620); the panels were assembled in GIMP. From the six ggplot objects (bigramsBYfrequency ... quadrigramsBYpmi) compare.R extracts each panel's bar identities and order, the 4-dp PMI label strings (geom_text sprintf('%.4f')), and the stacked frequencies by chronology. Labels and orders are compared exactly with the transcription; stacked bar lengths are compared visually with the published panels. Scope: 6 panels, 128 bars, 128 PMI labels; element gate 128 (7c). Cross-check: all 128 skipgrams have observed frequency > 2, so S3 holds their PMI values. Credit only if PARTs 1, 3, 5, and 6 complete (Q6). R4 applies to the log-base text/code inconsistency as for T02: scored against the printed labels.
- **T06** PMI heatmap of bigrams with observed frequency >= 3 over 49 motif tokens in the authors' manual chronological order (A14 ... RELIEF), red gradient (midpoint 0.5). A GIMP overlay adds small coloured boxes (purple Maglemose, red Kongemose, yellow Ertebølle) marking combinations limited to one culture complex, plus large boxes for culture-specific high-PMI groups (A14-A24; B10-F38; D33-H1; I5-I13; the C4/C5/C12/C13/D7 cluster) with motif pictograms. *Method:* Heatmap skeleton: PART 7 (S2.R lines 626-697; heatmapPMI.png). Compare visually for the 49-label axis order (exact) and the cell shading pattern; the cell PMI values (165 bigrams) are checked numerically against S3's bigram sheet. Box overlay: no code (added in GIMP). A labelled verification aid (R1/Q5) does a read-only lookup in `data` (dplyr::filter on the presence columns) of the Chronology values of objects bearing both motifs, for each of the 165 Part 7 bigrams. Pre-stated inferred rule: a cell carries a small box iff all such objects share exactly one of Maglemose, Kongemose, or Ertebølle, in that culture's colour; pairs involving any 'Kongemose/Ertebølle' object are expected unboxed. Qualification test (Q5): the rule is applied first to the bigrams whose chronology composition is printed in Fig. 3a/3b and must reproduce their published boxing; otherwise the overlay is not credited and goes to 7(a). Large boxes: check that every large-boxed pair is small-boxed in the stated culture, and report its PMI rank. Scope: 49 axis labels, 165 cells, every published small box (counted from the published figure before comparison), and 5 large boxes; element gate (7c). Pictograms are excluded as illustrations. Credit only if PARTs 1, 3, 5, 6, and 7 complete (Q6). R4 log-base note as T02.
- **T07** Map of the five Ertebølle-cluster motifs (C4, C5, C12, C13, D7): a coloured patch for the known extent of each motif, and 10 numbered pie charts (numbered as in Table 3) showing which of the five motifs each object carries. The Discussion (p. 6) reads it as C12 and C13 more eastern, C4, C5, and D7 more western. *Method:* No authors' code. Labelled verification aids (R1/Q5) do read-only lookups in `data`. For each Table 3 object they take its coordinates and which of the five motifs it carries (pie composition), plotted with ggplot2 geom_point under coord_quickmap(). For each motif they plot every S1 object carrying it (Coord.Long/Lat), then check visually that the published patch covers those objects and that the east/west reading holds. Scope: 10 pies (position + composition = 20 checks) plus 5 patches = 25 elements; element gate (7c). The patch construction method is unpublished. Shape differences that stem only from it are MINOR_DISCREPANCY (R1). If the patches turn out to rest on information outside S1, the patch elements are untestable under R2 and the target is recorded as partially verified (7c), counting against coverage. Credit only if PART 1 completes (Q6).
- **T08** All bi-, tri-, and quadrigrams with observed frequency >= 3, sorted by PMI: tokens, token frequencies, observed frequency, expected frequency, and PMI. bigrams 165 rows x 7 columns, trigrams 106 x 9, quadrigrams 20 x 11. *Method:* Produced by PART 8 (S2.R lines 698-759; fwrite Bigrams.csv, Trigrams.csv, Quadrigrams.csv); the authors then imported these into Excel. compare.R reads the three S3 sheets (two header rows each) and aligns rows by token tuple. Tokens and integer frequencies are compared exactly; expected frequency and PMI are compared at the precision stored in the S3 cells. Row order (PMI descending) is checked separately. Scope: 2329 cells (1155 + 954 + 220); element gate 2329 (7c). Credit only if PARTs 1, 3, 5, 6, 7, and 8 complete (Q6; the bigram sheet rests on Part 7's subset, the trigram and quadrigram sheets on Part 6's recomputation). R4 log-base note as T02.
- **T09** Corpus size: 483 objects, converted into 483 ornamentation strings. *Method:* Labelled verification aid (R1/Q5): nrow(data) from the PART 1 snapshot, and quanteda::ndoc(corpus) for the full-data corpus built in PART 3. S2.R never computes 483 (it hard-codes t <- 482 at line 86, explained in a comment as excluding one empty string). Scope: 1 value, checked twice; element gate 1. Credit only if PARTs 1 and 3 complete (Q6).
- **T10** 'the maximum number of individual motifs on a single object is 15', the stated basis for k = 13. *Method:* Labelled verification aid (R1/Q5), a documented quanteda call: max over documents of quanteda::ntype(quanteda::tokens(corpus)) on the PART 3 full-data corpus (primary, pre-stated). As secondary checks it reports max ntoken and the maximum number of non-empty S1 'Motifs' slot cells (P:AD) per row; a difference between primary and secondary is reported, not used to choose. Scope: 1 value; element gate 1. Credit only if PARTs 1 and 3 complete (Q6).
- **T11** Two bigrams each with observed frequency 44, identified as A1-C1 and C1-G1, said to be on about 9% of all objects. *Method:* Labelled verification aid (R1/Q5). The '44: 2' entry is read from PART 4's table(bigramfreqs), and the two identities from PART 6's bigrams_subset (sorted by observed_freq). The percentage uses the inferred formula 44 / nrow(data) x 100; its printed-input check (44/483 = 9.1%) is recorded. Scope: 3 values (44, 44, ~9%) plus the two identities; element gate 3. Credit only if PARTs 1, 3, 4, 5, and 6 complete (Q6).
- **T12** 'with A1-G1 being the third highest at a frequency of 28'. *Method:* Labelled verification aid (R1/Q5): read-only lookup of row 3 of PART 6's bigrams_subset (the authors' arrange(desc(observed_freq))), checking its identity (A1 G1) and observed_freq (28). Scope: 1 value plus identity and rank; element gate 1. Credit only if PARTs 1, 3, 5, and 6 complete (Q6).
- **T13** 'None of these most salient bigrams are exclusive to the Maglemosean, only one is specific to the Kongemose culture (B10-F38), and nine are unique for the Ertebølle period (I5-I13, C5-D7, C4-C12, C12-C13, C4-C5, I1-I13, C5-C13, and I1-I5)'. The text says nine but lists eight; the published Fig. 3b shows C5-C12 as a ninth Ertebølle-only bar. *Method:* Labelled verification aid (R1/Q5) applying a pre-stated inferred rule to bigramsBYpmi$data (PART 6, the authors' createResultTable output for the 21 Fig. 3b bigrams): a bar is exclusive to culture X iff every chronology row with Frequency > 0 is X. Its printed-input check is recorded: applied to the published Fig. 3b stacks the rule gives 0, 1, and 9. Scored values: the counts 0, 1, and 9, with identities B10-F38 and the eight listed Ertebølle pairs. R4: the stated count 'nine' is the scoring reference. The list's omission of a ninth pair is reported as a text inconsistency and, if the reproduction confirms it, escalated under 7(a) with tier (1) evidence (the paper's own Fig. 3b) for human confirmation. Scope: 3 counts plus 9 named identities; element gate 3. Credit only if PARTs 1, 3, 5, and 6 complete (Q6).
- **T14** 'These recurrent combinations are rare overall, however, with the highest frequency of cooccurrence being five.' *Method:* Labelled verification aid (R1/Q5). Pre-stated reading: 'these recurrent combinations' are the culture-exclusive Fig. 3b bigrams identified by the T13 rule, and the value is their maximum total frequency in bigramsBYpmi$data (PART 6). Printed-input check: on the published Fig. 3b this gives 5 (C4-C5). The alternative reading (maximum over all 21 Fig. 3b bars, where E1-F12 shows 6) is declared here and not used. Scope: 1 value; element gate 1. Credit only if PARTs 1, 3, 5, and 6 complete (Q6).
- **T15** Number of objects bearing the salient Ertebølle-cluster collocations: ten. *Method:* Labelled verification aid (R1/Q5) applying a pre-stated inferred rule: count the objects in `data` (PART 1) that carry at least two of {C4, C5, C12, C13, D7} (presence columns), and compare the selected set with the ten Table 3 objects. Printed-input check: every Table 3 row carries at least two of the five motifs, so on the printed inputs the rule selects ten. Scope: 1 value plus set identity; element gate 1. Credit only if PART 1 completes (Q6).
- **T16** Artefact composition of the ten cluster objects: 9 antler axes and 1 antler shaft. *Method:* Labelled verification aid (R1/Q5): read-only lookup of S1 'Material' and 'Artefact type' in `data` (PART 1) for the ten objects identified in T03. Scope: 2 counts; element gate 2. Credit only if PART 1 completes (Q6).
- **T17** 'the same motifs, most prominently A1, A24, B10, C1, G1, and H1, recur often ... These are also the motifs with the highest individual frequencies'. *Method:* Labelled verification aid (R1/Q5): read-only lookup of the six largest entries of PART 4's `freqs` (colSums of presence columns 31:289), compared as a set with the six named motifs (pre-stated reading: the six named are the top six). Scope: 6 identities; element gate 6. Credit only if PARTs 1 and 4 complete (Q6).

## Lodged rules applied

### Q5

> Where no authors' code produces a published result, the reproducer may test it with a labelled verification aid: a read-only lookup in the deposited data, or a call to a documented function of the package the authors used, making no new statistical choice. A formula the reproducer infers from the paper's wording qualifies only where it reproduces the paper's own printed values from the paper's own printed inputs, and it is credited only where its inputs come from executing the authors' code. A result resting on inputs the reproducer reconstructed, for example from upstream datasets the authors cite, never counts toward coverage or the verdict: the target stays in the denominator as expected-untestable, and the reconstructed result is reported as uplift evidence. A printed value that the formula does not reproduce is never credited and goes to the paper-error protocol of section 7(a), as the ruling directs for its two inconsistent cells.

| Target | Condition | Holds | Evidence | Credit |
|---|---|---|---|---|
| T03 | no-authors-code | yes | S2.R (PARTs 1-8) contains no code producing Table 3; its CONTENTS block lists no Table 3. | creditable |
| T03 | printed-inputs | not-applicable | No formula is inferred: each of the 50 cells is a read-only lookup of S1 columns Site, Region, Material, Artefact type, Motifs (P:AD), and Figure. | creditable |
| T03 | inputs-from-authors-code | yes | The aid reads `data`, the object created by executing the authors' PART 1 (read_excel on the deposited S1), from the wrapper's PART 1 snapshot, unmodified. | creditable |
| T03 | reconstructed-inputs | no | Only the deposited S1 is used; the upstream Płonka (2003) catalogue is not consulted or reconstructed. | creditable |
| T04 | no-authors-code | yes | The map panel has no code: README says the long./lat. columns 'were used to produce the fig.2 map', but S2.R has no mapping code. The bar panel is produced by PART 2 and needs no aid. | creditable |
| T04 | printed-inputs | not-applicable | No formula is inferred: the map aid plots deposited coordinates and chronology with documented ggplot2 functions (geom_point, coord_quickmap). | creditable |
| T04 | inputs-from-authors-code | yes | Coordinates and Chronology are read from `data` as created by executing the authors' PART 1; the bar panel comes from executing PART 2. | creditable |
| T04 | reconstructed-inputs | no | No upstream data are reconstructed; the basemap is excluded as non-data and is not rebuilt. | creditable |
| T06 | no-authors-code | yes | The box overlay and large boxes were added in GIMP (S2.R comment after line 692: 'adding coloured boxes etc. ... performed in ... GIMP'); only the heatmap skeleton comes from PART 7. | creditable |
| T06 | printed-inputs | unknown | The inferred boxing rule ('limited to one specific culture complex' means all objects bearing both motifs share one chronology) is first tested on the bigrams whose chronology compositions are printed in Fig. 3a/3b. Whether it reproduces their published boxing is decided by the run; if it does not, the overlay is not credited and goes to 7(a). | creditable |
| T06 | inputs-from-authors-code | yes | The cell set and PMI come from the PART 7 `bigrams` object produced by executing the authors' code; per-object chronology and motif presence are read from `data` created by executing PART 1. | creditable |
| T06 | reconstructed-inputs | no | No input is reconstructed from upstream sources; only the authors' run objects from the deposited S1 are used. | creditable |
| T07 | no-authors-code | yes | S2.R has no code for Fig. 5 (its CONTENTS block lists Figs. 2, 3, and 4 only). | creditable |
| T07 | printed-inputs | not-applicable | No formula is inferred: pie compositions and positions are lookups of S1 motif presence and coordinates, and patch coverage is a visual containment check of plotted S1 objects, not a computed value. | creditable |
| T07 | inputs-from-authors-code | yes | All aid inputs are read from `data` as created by executing the authors' PART 1. | creditable |
| T07 | reconstructed-inputs | no | Patches are not reconstructed from external sources. If their extent rests on non-deposited information, the patch elements are recorded untestable (R2) and partially verified (7c), not rebuilt. | creditable |
| T09 | no-authors-code | yes | S2.R never computes 483; it hard-codes t <- 482 (line 86). | creditable |
| T09 | printed-inputs | not-applicable | No formula is inferred: nrow() and the documented quanteda::ndoc() read the size of existing objects. | creditable |
| T09 | inputs-from-authors-code | yes | `data` (PART 1) and the full-data `corpus` (PART 3) are objects created by executing the authors' code. | creditable |
| T09 | reconstructed-inputs | no | No reconstructed input; deposited S1 only. | creditable |
| T10 | no-authors-code | yes | S2.R does not compute the maximum number of motifs per object; k <- 0:13 is set by hand (PART 3). | creditable |
| T10 | printed-inputs | not-applicable | No formula is inferred: documented quanteda functions ntype() and ntoken() on the authors' corpus, read out by max. | creditable |
| T10 | inputs-from-authors-code | yes | The corpus is the PART 3 object created by executing the authors' code (corpus(data$Motifs_as_text)). | creditable |
| T10 | reconstructed-inputs | no | No reconstructed input; deposited S1 only. | creditable |
| T11 | no-authors-code | yes | PART 4 prints the count table (including '44: 2'), but no code names A1-C1/C1-G1 as the pair or computes the ~9% share. | creditable |
| T11 | printed-inputs | yes | The inferred share formula, frequency / number of objects, reproduces the printed 'approximately 9%' from the paper's printed inputs 44 and 483: 44/483 = 9.1%. | creditable |
| T11 | inputs-from-authors-code | yes | 44 comes from PART 4's table(bigramfreqs) and PART 6's bigrams_subset, and 483 from nrow(data) of PART 1, all objects produced by executing the authors' code. | creditable |
| T11 | reconstructed-inputs | no | No reconstructed input. | creditable |
| T12 | no-authors-code | yes | No code states 'third highest'; PART 6 sorts bigrams_subset but reports no rank. | creditable |
| T12 | printed-inputs | not-applicable | No formula is inferred: a read-only lookup of row 3 of the authors' own sorted object. | creditable |
| T12 | inputs-from-authors-code | yes | bigrams_subset is created by executing PART 6 (arrange(desc(observed_freq))). | creditable |
| T12 | reconstructed-inputs | no | No reconstructed input. | creditable |
| T13 | no-authors-code | yes | No code counts culture-exclusive bigrams; the counts appear only in the text. | creditable |
| T13 | printed-inputs | yes | Applied to the printed Fig. 3b stacks, the exclusivity rule gives the printed counts. Single-colour bars: red only B10 F38 (1); yellow only I5 I13, C5 D7, C4 C12, C12 C13, C4 C5, I1 I13, C5 C13, C5 C12, I1 I5 (9); no purple-only bar (0). | creditable |
| T13 | inputs-from-authors-code | yes | The rule is applied to bigramsBYpmi$data, the createResultTable output stored in the PART 6 ggplot object created by executing the authors' code. | creditable |
| T13 | reconstructed-inputs | no | No reconstructed input. | creditable |
| T14 | no-authors-code | yes | No code computes the maximum frequency among culture-exclusive bigrams. | creditable |
| T14 | printed-inputs | yes | On the printed Fig. 3b, the largest total among single-culture bars is 5 (C4 C5, yellow only), matching the printed 'five'. | creditable |
| T14 | inputs-from-authors-code | yes | Frequencies come from bigramsBYpmi$data produced by executing PART 6. | creditable |
| T14 | reconstructed-inputs | no | No reconstructed input. | creditable |
| T15 | no-authors-code | yes | No code selects or counts the cluster objects. | creditable |
| T15 | printed-inputs | yes | Applied to the paper's printed inputs (Table 3 motif lists), the rule 'at least two of C4, C5, C12, C13, D7' selects all ten printed objects, reproducing the printed 'ten'. The run then applies it to all objects in `data`. | creditable |
| T15 | inputs-from-authors-code | yes | Presence columns are read from `data` created by executing the authors' PART 1. | creditable |
| T15 | reconstructed-inputs | no | No reconstructed input. | creditable |
| T16 | no-authors-code | yes | No code tabulates the artefact types of the cluster objects. | creditable |
| T16 | printed-inputs | not-applicable | No formula is inferred: a read-only lookup of S1 Material and Artefact type for the ten Table 3 objects. | creditable |
| T16 | inputs-from-authors-code | yes | Read from `data` created by executing PART 1. | creditable |
| T16 | reconstructed-inputs | no | No reconstructed input. | creditable |
| T17 | no-authors-code | yes | PART 4 computes `freqs` but no code ranks or names the most frequent motifs. | creditable |
| T17 | printed-inputs | not-applicable | No formula is inferred: a read-only lookup of the six largest entries in the authors' `freqs` object. | creditable |
| T17 | inputs-from-authors-code | yes | `freqs` is created by executing PART 4 (colSums(data[,31:289])). | creditable |
| T17 | reconstructed-inputs | no | No reconstructed input. | creditable |

### R1

> R1 No author code: a target whose published result has no supplied code may be tested with clearly labelled verification aids. Aids are read-only lookups in the deposited data, and calls to documented functions of the package the authors used. They make no new statistical choices, and they live in a separate comparison script, never in the authors' code. A difference caused only by an unpublished convention (for example histogram bin edges) is MINOR_DISCREPANCY.

| Target | Condition | Holds | Evidence | Credit |
|---|---|---|---|---|
| T03 | — | — | — | creditable |
| T04 | — | — | — | creditable |
| T06 | — | — | — | creditable |
| T07 | — | — | — | creditable |
| T09 | — | — | — | creditable |
| T10 | — | — | — | creditable |
| T11 | — | — | — | creditable |
| T12 | — | — | — | creditable |
| T13 | — | — | — | creditable |
| T14 | — | — | — | creditable |
| T15 | — | — | — | creditable |
| T16 | — | — | — | creditable |
| T17 | — | — | — | creditable |

### R2

> R2 Unavailable inputs: a target whose inputs cannot be obtained stays in the locked denominator as expected-untestable and counts against coverage. Never drop it to narrow scope.

| Target | Condition | Holds | Evidence | Credit |
|---|---|---|---|---|
| T01 | inputs-unobtainable | no | Inputs S1 and S2 were retrieved anonymously from Zenodo v2 at planning with md5 matching the published checksums; the executor re-retrieves them. | creditable |
| T02 | inputs-unobtainable | no | S1 and S2 obtained (Zenodo v2, md5 verified). | creditable |
| T03 | inputs-unobtainable | no | S1 obtained; it contains Site, Region, Material, Artefact type, Motifs, and Figure columns (headers inspected at planning). | creditable |
| T04 | inputs-unobtainable | no | S1 obtained, with Coord.Long, Coord.Lat, Chronology, and Artefact type columns; S2 PART 2 obtained. | creditable |
| T05 | inputs-unobtainable | no | S1 and S2 obtained. | creditable |
| T06 | inputs-unobtainable | no | S1 and S2 obtained; the box-rule inputs are S1 chronology and presence columns. | creditable |
| T07 | inputs-unobtainable | unknown | Pie and position inputs are in S1 (obtained). The patches show the 'known extent of each individual motif', and their source is unstated. If they rest on information outside S1 (e.g., Płonka 2003 or other finds), those elements' inputs are unobtainable. The run decides this. | creditable |
| T08 | inputs-unobtainable | no | S1 and S2 obtained; the reference S3 also obtained (md5 verified). | creditable |
| T09 | inputs-unobtainable | no | S1 obtained. | creditable |
| T10 | inputs-unobtainable | no | S1 obtained (Motifs_as_text and slot columns P:AD). | creditable |
| T11 | inputs-unobtainable | no | S1 and S2 obtained. | creditable |
| T12 | inputs-unobtainable | no | S1 and S2 obtained. | creditable |
| T13 | inputs-unobtainable | no | S1 and S2 obtained. | creditable |
| T14 | inputs-unobtainable | no | S1 and S2 obtained. | creditable |
| T15 | inputs-unobtainable | no | S1 obtained. | creditable |
| T16 | inputs-unobtainable | no | S1 obtained (Material and Artefact type columns). | creditable |
| T17 | inputs-unobtainable | no | S1 and S2 obtained. | creditable |

### R3

> R3 Granularity: one target per display item. A multi-panel figure is one target, and its panels are described within it. Named values in the text are separate targets.

| Target | Condition | Holds | Evidence | Credit |
|---|---|---|---|---|
| T01 | — | — | — | creditable |
| T02 | — | — | — | creditable |
| T03 | — | — | — | creditable |
| T04 | — | — | — | creditable |
| T05 | — | — | — | creditable |
| T06 | — | — | — | creditable |
| T07 | — | — | — | creditable |
| T08 | — | — | — | creditable |
| T09 | — | — | — | creditable |
| T10 | — | — | — | creditable |
| T11 | — | — | — | creditable |
| T12 | — | — | — | creditable |
| T13 | — | — | — | creditable |
| T14 | — | — | — | creditable |
| T15 | — | — | — | creditable |
| T16 | — | — | — | creditable |
| T17 | — | — | — | creditable |

### R4

> R4 Internal inconsistency: where the paper's text and its own tables or figures disagree, score against the stated value. Apply the PAPER_ERROR protocol if the reproduction disagrees, and escalate.

| Target | Condition | Holds | Evidence | Credit |
|---|---|---|---|---|
| T02 | — | — | — | creditable |
| T05 | — | — | — | creditable |
| T06 | — | — | — | creditable |
| T08 | — | — | — | creditable |
| T13 | — | — | — | creditable |

### 7a-paper-error

> When a reproduced value disagrees with a published value, the reproduction is internally consistent, and the authors' own materials support the reproduced value, classify as PAPER_ERROR rather than MAJOR_DISCREPANCY. Admissible evidence, in descending strength: (1) the paper's own tabulated data; (2) the authors' deposited data for that analysis; (3) the authors' own code, run unmodified (invariant 2), on the authors' own data. The reproduction's own re-implementation is never evidence. The comparison report names the tier used. PAPER_ERROR findings escalate for human confirmation before entering study data.

| Target | Condition | Holds | Evidence | Credit |
|---|---|---|---|---|
| T02 | — | — | — | creditable |
| T05 | — | — | — | creditable |
| T06 | — | — | — | creditable |
| T08 | — | — | — | creditable |
| T13 | — | — | — | creditable |

### 7c-check-scope

> Each target's verification method states its scope, which must equal the target's full published scope at the pre-stated tolerance. A check that covers part of a target is completed before the target counts as reproduced; otherwise the target is recorded as partially verified and counts against coverage. Where feasible, the plan declares the target's element count, and a deterministic gate compares it with the elements checked.

| Target | Condition | Holds | Evidence | Credit |
|---|---|---|---|---|
| T01 | — | — | — | creditable |
| T02 | — | — | — | creditable |
| T03 | — | — | — | creditable |
| T04 | — | — | — | creditable |
| T05 | — | — | — | creditable |
| T06 | — | — | — | creditable |
| T07 | — | — | — | creditable |
| T08 | — | — | — | creditable |
| T09 | — | — | — | creditable |
| T10 | — | — | — | creditable |
| T11 | — | — | — | creditable |
| T12 | — | — | — | creditable |
| T13 | — | — | — | creditable |
| T14 | — | — | — | creditable |
| T15 | — | — | — | creditable |
| T16 | — | — | — | creditable |
| T17 | — | — | — | creditable |

### Q6

> A wrapper may make an authors' statement error-tolerant only where the statement computes nothing that enters a result, such as registering a font; the tolerance is declared, and the run log records whether it fired. Per-section error capture is routine, but a target is credited only from a section that completed without error and whose inputs come only from sections that also completed. Sections may run in another order only when they are independent, none reading an object another defines; otherwise re-ordering changes the execution logic and is fail-and-uplift. A dependency fetched from a public repository is installed when the environment is built, pinned to a tagged release or, where the repository has none, to a recorded commit, preferring the one current at publication. An unpinned install at run time is not routine. Independence between sections is judged on every state a section can pass to another, namely named objects, files written and read, global options, and random-number state. The dependency sentence is read with the precedence rule above, so where the authors pinned the dependency, their pin is used.

| Target | Condition | Holds | Evidence | Credit |
|---|---|---|---|---|
| T01 | — | — | — | creditable |
| T02 | — | — | — | creditable |
| T03 | — | — | — | creditable |
| T04 | — | — | — | creditable |
| T05 | — | — | — | creditable |
| T06 | — | — | — | creditable |
| T07 | — | — | — | creditable |
| T08 | — | — | — | creditable |
| T09 | — | — | — | creditable |
| T10 | — | — | — | creditable |
| T11 | — | — | — | creditable |
| T12 | — | — | — | creditable |
| T13 | — | — | — | creditable |
| T14 | — | — | — | creditable |
| T15 | — | — | — | creditable |
| T16 | — | — | — | creditable |
| T17 | — | — | — | creditable |

### 7d-fail-and-uplift

> Routine (execution environment): choosing among publicly available versions of dependencies and language runtimes, meaning releases from the package's official archive (for example CRAN or PyPI) or a tagged public repository, preferring the version current at publication. The search and the chosen versions are recorded. Fail-and-uplift: any edit to the authors' code that changes logic, indices, data selection, parameters, or the functions called, however obvious the intent. A deprecated function is handled by pinning a public version that still runs it; if none exists, replacing it is an edit, and so fail-and-uplift. A repaired result is recorded as uplift evidence and never counts toward coverage or the verdict.

| Target | Condition | Holds | Evidence | Credit |
|---|---|---|---|---|
| T01 | — | — | — | creditable |
| T02 | — | — | — | creditable |
| T03 | — | — | — | creditable |
| T04 | — | — | — | creditable |
| T05 | — | — | — | creditable |
| T06 | — | — | — | creditable |
| T07 | — | — | — | creditable |
| T08 | — | — | — | creditable |
| T09 | — | — | — | creditable |
| T10 | — | — | — | creditable |
| T11 | — | — | — | creditable |
| T12 | — | — | — | creditable |
| T13 | — | — | — | creditable |
| T14 | — | — | — | creditable |
| T15 | — | — | — | creditable |
| T16 | — | — | — | creditable |
| T17 | — | — | — | creditable |

### 7d-mechanics

> A mechanical change made inside an authors' file rather than in a wrapper, such as a changed input path, breaks the wrapper rule even when it changes nothing computed. A result that rests on such a file does not count toward coverage or the verdict until it is re-run with the mechanics moved into a wrapper and the authors' file restored byte-identical. A change of logic, indices, data selection, parameters, or functions called remains fail-and-uplift whatever its effect, including a restructuring that gives the same result.

| Target | Condition | Holds | Evidence | Credit |
|---|---|---|---|---|
| T01 | — | — | — | creditable |
| T02 | — | — | — | creditable |
| T03 | — | — | — | creditable |
| T04 | — | — | — | creditable |
| T05 | — | — | — | creditable |
| T06 | — | — | — | creditable |
| T07 | — | — | — | creditable |
| T08 | — | — | — | creditable |
| T09 | — | — | — | creditable |
| T10 | — | — | — | creditable |
| T11 | — | — | — | creditable |
| T12 | — | — | — | creditable |
| T13 | — | — | — | creditable |
| T14 | — | — | — | creditable |
| T15 | — | — | — | creditable |
| T16 | — | — | — | creditable |
| T17 | — | — | — | creditable |


## Exclusions

- Fig. 1 (photographs of four decorated artefacts) (p. 2): Museum photographs (National Museum of Denmark, CC-BY-SA) with no computational or numerical content; nothing to reproduce.
- Supplementary Information S1 (Herskind&Riede_S1.xlsx) (Zenodo v2; cited p. 2): The input dataset, not a result. Its integrity is checked by md5 and its values enter every target as input; scoring it would only compare the file with itself.
- Supplementary Information S2 (Herskind&Riede_S2.R) (Zenodo v2; cited p. 3): The authors' code, which is executed rather than scored; byte identity is verified by sha256.
- Skip distance k = 13 (p. 3, §2.2; Table 1 caption): A method parameter set in code (k <- 0:13), not a result. Its stated rationale (a maximum of 15 motifs) is scored as T10.
- 'nearly half of the total number of European Mesolithic ornamented artefacts listed by Płonka (2003)' (p. 2, §2): Literature-derived background: the European total lies in the analogue Płonka catalogue, which is neither deposited nor analysed. Flagged: if the approver rules it a named value, it enters the denominator as expected-untestable under R2.
- Culture-complex date ranges (~11,000-5950 BP; Maglemose ~11,000-8400, Kongemose ~8400-7400, Ertebølle ~7400-5950 BP) (p. 2, §2): Literature values cited as context, not analysis results.
- Non-data graphical elements: basemap coastlines, scale bar, and north arrow (Figs. 2 and 5); motif pictograms and legend artwork (Figs. 4 and 5) (pp. 3, 6, 7): Cartographic and illustrative elements with no data content. The data-bearing content of these figures is fully within T04, T06, and T07. Listed so the approver sees the scope boundary used for the 7(c) element counts.
- Interpretive statements (e.g., 'no evident semiotic structure'; 'the potential for meaningful collocations increase towards the Late Mesolithic') (Abstract; pp. 4-7): Conclusions drawn from scored targets (T02, T05, T06, T07), with no separate value of their own. The east/west reading of Fig. 5 is scored inside T07 rather than excluded.

## Enumeration-completeness check

- Method: Paper captions: pdftotext /home/shawn/corpora/llm-reproducibility/herskind-riede-2024/vor.pdf - | grep -oE '^(Fig\. [0-9]+\. [A-Z]|Table [0-9]+$)' | grep -oE '(Fig\. [0-9]+|Table [0-9]+)' | sort -u | wc -l  -> 8 (Fig. 1-5, Table 1-3). Cross-check of in-text references: pdftotext <same pdf> - | grep -oE '(Fig\.? [0-9]+|Table [0-9]+|Supplementary Information S[0-9]+( and S[0-9]+)?)' | sed -E 's/Fig /Fig. /' | sort -u  -> the same 8 items plus 'Supplementary Information S1' ('S2 and S3' is hyphen-split across a line on p. 3). Supplementary items: curl -s https://zenodo.org/api/records/10801706 file list -> S1.xlsx, S2.R, S3.xlsx, README.txt; README is documentation, which leaves 3 supplementary items. Display items detected = 8 + 3 = 11.
- Display items detected: 11; targets enumerated: 17; excluded: 8; flagged for human: True
- Notes: Reconciliation: the 11 detected display items = 8 display-item targets (T01 Table 1, T02 Table 2, T03 Table 3, T04 Fig. 2, T05 Fig. 3, T06 Fig. 4, T07 Fig. 5, T08 S3) + 3 excluded display items (Fig. 1, S1, S2). In addition there are 9 named-value targets (T09-T17), one per text statement (R3), and 5 non-display exclusions (k = 13; the 'nearly half' literature claim; date ranges; non-data graphic elements; interpretive statements). There is no shortfall. The flag is raised for granularity doubts, not for a below-threshold count: (1) S3 is enumerated as one target with three sheets, by analogy with R3's multi-panel rule; treating each sheet as a table would give 3 targets. (2) Named values are grouped per sentence (e.g., T11 holds 44, 44, and ~9%; T13 holds 0, 1, and 9); per-number granularity would raise the count. (3) Whether the 'nearly half' Płonka claim is a named value (R2 expected-untestable) or background.

## Eligibility

- computational_component: True
- code_available: True
- primary_language_r: True
- estimated_compute_hours: 1.5
- within_compute_cap: True
- study_team_coauthorship: no
- notes: Authors: Lasse Lukas Platz Herskind and Felix Riede (Aarhus University); the study registrant Shawn Ross is not an author. Code: Herskind&Riede_S2.R (759 lines, UTF-8, CRLF line endings), one R script in 8 PARTs that reads S1 and produces Fig. 2 (bar panel), Table 1, Table 2, Fig. 3, the Fig. 4 skeleton, and the S3 tables. No random numbers anywhere, so the run is fully deterministic. Estimated compute: image build 0.5-1 h (binary packages from Posit Package Manager for the rocker jammy base), script run a few minutes, so about 1.5 h in total against the 168 h cap. No API calls or paid services. Tolerance instrument verdicts-and-precision.md v1.1 read in full (Receipt-token 46eb4ad0bfcb3b92). The agent brief's pulled references verification-strategies.md and pilot-reproduction-summary.md are on the blinded list, so they were skipped and are not declared. BLINDING DISCLOSURE: while looking for the run-container entry point I ran an ls of /home/shawn/Code/llm-reproducibility/reproduction-system/ that was filtered only for 'workflows'. Its output printed the blinded filename lodged-rules.yaml. That file was not opened, read, searched, or otherwise accessed, and none of its content was seen; the lodged rules were quoted only from the spawn prompt. Reported for the approver's ruling on admissibility (see questions_for_approver).

## Data retrieval plan

- **Herskind&Riede_S1.xlsx (motif presence/absence, chronology, coordinates; input to every target)** — stated: Data availability statement (p. 8): https://zenodo.org/records/10801706 (Zenodo v2). The methods (p. 3) cite v1 https://zenodo.org/records/10623550, which run-note AP-12 excludes. Publisher Appendix A supplementary files are byte-identical to v2 per the run notes.; planned: Anonymous GET via the Zenodo REST API files endpoint of record 10801706; verify md5 0bcde6d178b5a8f3da80a023a64ff510; log route, steps, and outcome so the executor can assign the L-level from the actual attempt. The planner's trial retrieval on 2026-10-21 succeeded with matching md5.
- **Herskind&Riede_S2.R (authors' code)** — stated: Zenodo v2 record (data availability statement; README); planned: As for S1; verify md5 6760ccb30ecc1de7c280bc1e0fa182e5 and record sha256 487a00a0... before and after the run (byte identity).
- **Herskind&Riede_S3.xlsx (published reference tables)** — stated: Zenodo v2 record ('Dedicated R code and complete data tables are reported in Supplementary Information S2 and S3', p. 3); planned: As for S1; verify md5 812be5456d7e0e2adb97ecb5a975239e. This is a published-values source, not an analysis input.
- **Płonka (2003) analogue catalogue (upstream source transcribed into S1)** — stated: Cited printed monograph (Acta Universitatis Wratislaviensis 2527); no digital route; planned: Not retrieved. No target requires it as an input, so under the L2 counting unit it is provenance only. If the Fig. 5 patch extents turn out to rest on information outside S1, those elements are recorded as untestable under R2 rather than reconstructed.

## Risks

- (high) extrafont::font_import(pattern = 'GIL') (S2.R line 27) errors because Gill Sans MT is proprietary and absent; in a plain Rscript run this would halt the script (the authors note an error message they ignored interactively). — *mitigation:* Declared Q6 error tolerance in the wrapper for line 27 only (font registration, enters no result); the run log records whether it fired. Typeface differences are not scored.
- (medium) Autoprinted ggplot objects under batch execution open the default pdf device, which may fail with an unknown font family ('Gill Sans MT'). — *mitigation:* The wrapper sets the default device to a file-based cairo PNG (mechanics, output capture), so fontconfig fallback applies. ggsave PNG output is unaffected.
- (low) PART 7 subsets the matrix by a hard-coded list of 49 tokens (line 651); if any listed token is absent from the observed > 2 bigrams, a subscript error stops PART 7. T06 and T08 would then be uncreditable under Q6. — *mitigation:* No edit is allowed (7d). The error is captured and logged, PART 7 is marked failed, and T06 and T08 are recorded as not reproduced (counted against coverage). Any repair would be uplift evidence only.
- (low) Pinned package versions fail to build on R 4.3.2 (e.g., quanteda 3.3.1 compilation or dependency conflicts with the 2024-04-03 snapshot). — *mitigation:* Use PPM binaries for jammy; apply the invariant 2 version-search cap (pin, then preceding, then following release) and log every attempt and fallback against the component.
- (low) Non-ASCII names ('Ertebølle' object name and string literal) mis-handled in a non-UTF-8 locale, so the Ertebølle subset comes out empty. — *mitigation:* Set LANG=en_US.UTF-8 in the image and parse S2.R with encoding UTF-8 (wrapper mechanics); check the subset row counts in the log.
- (low) The trigram and quadrigram plots use 3-colour manual fill scales; if a fourth chronology level appears in those subsets, ggplot errors at print or ggsave and the Fig. 3 panels fail. — *mitigation:* The published Fig. 3d-f show three colours. Errors are captured per expression; Q6 crediting applies and nothing is edited.
- (high) Text/code inconsistencies: the PMI formula says log2 but the code uses natural log(); t is defined as the total number of objects (483) but hard-coded as 482; R v4.2.2 (paper) against 4.3.2 (README). — *mitigation:* Scoring is against the printed values (R4); the inconsistencies are reported in the comparison report and raised with the approver. The README pin is used for R.
- (medium) The inferred aid rules (T06 boxes, T13, T14, T15) may not reproduce the printed values. — *mitigation:* Rules and readings are pre-stated here. A printed value the rule does not reproduce is never credited and goes to the 7(a) paper-error protocol with the evidence tier named.
- (medium) Fig. 5 patch extents and the Fig. 4 large-box threshold rest on unpublished conventions or non-deposited information, so those targets may only be partially verified. — *mitigation:* Elements are declared with their counts; untestable elements are recorded under R2/7c as partially verified and counted against coverage, never dropped.
- (medium) Visual comparison of GIMP-assembled figures is subjective. — *mitigation:* Side-by-side panels against pre-stated criteria; numeric checks wherever plot data exist (Fig. 3 labels, S3 cross-checks); the adversarial review audits the visual judgements.
- (high) Blinding incident at planning: a directory listing printed the blinded filename lodged-rules.yaml (the file was not accessed). This may affect run admissibility. — *mitigation:* Disclosed in full in this plan for the approver's ruling; no content was seen, and the rules were quoted only from the spawn prompt.

## Compute strategy

All builds and runs happen on this machine through the run-container procedure named in the run notes (I did not locate a script by that name under scripts/ or reproduction-system/runtime/, so the executor uses the project's standard run-container entry point). Step 1: build one image from rocker/r-ver:4.3.2 with the seven README-pinned packages and the 2024-04-03 snapshot for everything else; record the digest, sessionInfo(), and installed.packages(). Step 2: one serial container run of the wrapper run-analysis.R, with the deposit mounted read-only, no network, and LANG=en_US.UTF-8. Step 3: the comparison script (compare.R, containing the labelled verification aids) runs in the same image, against the run's snapshots and the published values. Expected wall-clock is under 2 h (build-dominated); the script itself takes minutes, there is no RNG, and nothing is parallelised because nothing needs to be. Conservative default flagged: serial build and run. Parallel package compilation (Ncpus) could shorten the build if PPM binaries are unavailable, but it is not needed within the cap.

## Scope limitations

- Gill Sans MT (proprietary) is unavailable, so reproduced figures use a fallback typeface; typeface is not scored.
- Figs. 3 and 4 were finished in GIMP and Tables 1 and 2 were copied by hand from console output into Word. The reproduction compares scientific content, not the manual layout.
- Fig. 2 (map panel), Fig. 4 (box overlay), Fig. 5, Table 3, and the named values T09-T17 have no authors' code. They are tested only with labelled verification aids (R1/Q5) in a separate comparison script.
- Basemaps, scale bars, north arrows, and motif pictograms are outside the scored scope (non-data elements; see exclusions).
- The Fig. 5 patch construction and the Fig. 4 'particularly high PMI' threshold are unpublished; differences arising only from them are MINOR_DISCREPANCY, and elements resting on non-deposited information are partially verified.
- Upstream source data (Płonka 2003 analogue catalogue) are not reconstructed; S1 is taken as deposited.

## Questions for the approver

- BLINDING: at planning, `ls /home/shawn/Code/llm-reproducibility/reproduction-system/ | grep -v -E 'workflows'` printed the blinded filename lodged-rules.yaml. The file was not opened, read, or searched, and its content was not seen; the rules were quoted only from the spawn prompt. Please rule on whether this run remains admissible.
- R version: the README (deposit v2) states R 4.3.2 with seven package pins, but the paper's methods state R v.4.2.2. The plan honours the README as the authors' environment specification (rocker/r-ver:4.3.2). Approve, or direct R 4.2.2?
- S3 granularity: Supplementary Information S3 is enumerated as one target (T08) with three sheets, by analogy with R3's multi-panel rule. Should each sheet be a separate target instead (+2 targets)?
- Log base and t: the paper's PMI formula uses log2 and defines t as the total number of objects (483), but S2.R uses natural log() and t = 482. Under R4 the plan scores the printed values and reports the inconsistency. Should the formula-text mismatch also be escalated as a PAPER_ERROR finding if the printed values prove to be natural-log based?
- T13: the text says 'nine are unique for the Ertebølle period' but lists eight pairs; Fig. 3b shows C5-C12 as the ninth. The plan scores the stated counts (0, 1, 9) and the listed identities, and escalates the omission. Approve?
- T14: the plan pre-states that 'highest frequency of cooccurrence being five' refers to the culture-exclusive Fig. 3b bigrams. Over all 21 bars the published maximum is 6 (E1-F12). Approve this reading?
- T06 convention: pairs involving 'Kongemose/Ertebølle' objects are expected unboxed in Fig. 4, and deviations are MINOR (R1). Approve?
- Q5 reading for the inferred aid rules (T06, T11, T13, T14, T15): the plan treats `data` and the other run objects created by executing the authors' S2.R as 'inputs from executing the authors' code', and records each rule's printed-input qualification check. Approve this reading of the inputs-from-authors-code condition?
- Exclusions: Fig. 1 (photographs), S1 (input data), S2 (code), k = 13 (parameter), the 'nearly half of Płonka's European total' claim (literature background; if ruled a named value it enters as expected-untestable under R2), date ranges, non-data graphic elements, and interpretive statements. Approve?
- Reproduction type: classified C (an interactive-style script with a known error at line 27 and manual post-processing), although the computational core runs in batch through a wrapper. Approve, or reclassify as B?

## Orchestrator warnings

- planner flagged the enumeration for human attention
