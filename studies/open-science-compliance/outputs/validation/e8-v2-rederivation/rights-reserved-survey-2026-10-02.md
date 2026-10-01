# "All rights reserved" under R1.1 — FAIR-framework survey (2026-10-02)

**Purpose:** evidence base for the open boundary of adjudication-log AP-8:
does an explicit "all rights reserved" (ARR) notice satisfy R1.1 ("(meta)data
are released with a clear and accessible data usage license")?

**Method:** a background research agent (Claude Opus) fetched each source
directly on 2026-10-02 and quoted only from fetched text. The clerk (Claude)
then re-verified every decisive quote below against the fetched files; three
initially failed exact matching only because line breaks or HTML markup split
the text, and all three were confirmed. The fetched copies were temporary and
are not committed (third-party content); URLs are given for re-fetching.

## Findings by source

| Source | Treats ARR as | Key wording (verbatim) |
|---|---|---|
| Wilkinson et al. 2016, *Scientific Data* 3:160018 (<https://www.nature.com/articles/sdata201618>) | Silent | R1.1 text only |
| GO FAIR Foundation R1.1 page (<https://www.gofair.foundation/r1-1>; text from Jacobsen et al. 2020) | Silent on an explicit notice; absence of a licence ≠ open | "include a license that describes under which conditions the resource can be used, even if that is “unconditional”"; "a license that cannot be found by an agent, is effectively the same as no license at all"; "the absence of a license does not indicate “open”" |
| Research Data Alliance (RDA) FAIR Data Maturity Model v1.0, 2020 (<https://zenodo.org/records/3909563>) | Silent; non-standard licences flagged as an open question | RDA-R1.1-01M: "In the absence of licence information, data cannot be reused."; glossary: "Licence (re-use) — A legal document that specifies what a user can do with a resource." |
| F-UJI / FAIRsFAIR FsF-R1.1-01M (<https://github.com/pangaea-data-publisher/fuji>) | Counts "rights statements"; current default tests presence only, so ARR would pass | "Licenses can be of standard type … or bespoke licenses, and rights statements which indicate the conditions under which data can be reused." Default metric set `metrics_v0.8` (`fair_check.py:200`) has the single test "Licence information is given in an appropriate metadata element". |
| ARDC (Australian Research Data Commons) FAIR self-assessment tool (<https://github.com/au-research/FAIR-Data-Assessment-Tool>) | **No licence = ARR**, scored 0 | "If data is not licensed no-one else can use it. In Australia, no licence is regarded as the same as 'all rights reserved', confining any reuse to very limited circumstances." Answer scale includes "Non-standard text-based license" 2 and "No license" 0. |
| Labastida & Margoni 2020, *Data Intelligence* (R1.1 paper in the FAIR special issue; <https://eprints.gla.ac.uk/203694/1/203694.pdf>) | **No notice = the ARR regime** | "the absence of any legal notice must be understood as the default “all rights reserved” regime … Right holders could use any text to state the reusability of data" |
| FAIR4RS (RDA recommendation v1.0, 2022; <https://zenodo.org/records/6623556>) | Silent | "The FAIR4RS Principles can be applied to any research software, regardless of the license." |
| Creative Commons FAQ (<https://creativecommons.org/faq/>) | Definition | ARR is "used by owners to indicate that they reserve all of the rights granted to them under the law" |
| Digital Curation Centre (DCC), Ball 2014 (<https://www.dcc.ac.uk/guidance/how-guides/license-research-data>) | Definition of a licence | "a legal instrument for a rights holder to permit a second party to do things that would otherwise infringe on the rights held" |
| choosealicense.com "No License" (<https://choosealicense.com/no-permission/>) | Copyright notice = no licence offered | recommends "a copyright notice and statement that you are not offering any license" |

Also checked and silent on ARR: GO FAIR's older R1.1 page, the FAIR Maturity
Indicators (Gen1/Gen2), FAIRshake rubrics, How to FAIR, and The Turing Way.
No published FAIR-assessment study coding ARR was found.

## Synthesis

1. **No consensus; no major framework scores an explicit ARR notice.**
2. **Where ARR is mentioned, it is equated with having no licence** (ARDC;
   Labastida & Margoni): legally, silence and ARR are the same state.
3. **Frameworks split by what they test.** Metadata-presence tests (F-UJI's
   current default; RDA-01M) would credit any rights statement. Tests of
   licence substance (RDA-02M/03M; the definitions in DCC and the RDA
   glossary, where a licence *permits* something) would not credit ARR, which
   grants nothing.
4. **Partial credit has precedent** (RDA would meet the essential indicator
   only; ARDC grades non-standard text licences 2/4), but this instrument's
   sub-principles are binary.

The registrant's ruling and its rationale are recorded in
`adjudication-log.md` (AP-8).
