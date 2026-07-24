# Census and reproduction eligibility criteria v1.0 — canonical file

**Status: FROZEN by OSF registration 2026-07-20 (DOI 10.17605/OSF.IO/DQNHG)** —
changes require the §8 regression gate + an erratum-log entry + an OSF amendment
before any affected analysis runs.
**Version:** 1.0 (extracted 2026-07-24 from preregistration §4–§5)
**Canonical home** per routing design §4.
**Consumers:** `reproduction-planner` (pushed, with read receipt); the census
screener consumes §1–§2 via its triage prompt (separate instrument-like file,
built with the screener); registered in `manifest.yaml` `shared_content`.

---

## 1. Frame construction (preregistration §4)

CrossRef and OpenAlex sweep of *Journal of Archaeological Science* (main
journal) and *Journal of Archaeological Science: Reports*, publication window
2022-01-01 to 2026-06-30 inclusive. Window membership is defined on the
**earliest recorded publication date** (online-first or issue) reported by
CrossRef; both dates are recorded. The two sources are merged as a union;
DOI-level discrepancies between them are logged and resolved against the
publisher record.

## 2. Census inclusion (preregistration §4)

Research articles (excluding editorials, corrigenda, letters, review articles
without new analysis) with accessible full text, in English, that are
**quantitative** — defined as reporting numerical analysis of data
(measurements, counts, statistics, or model outputs).

Rationale: the H1 sample must be restricted on a characteristic the policy
cannot influence. Whether a paper mentions or shares code is itself a plausible
policy outcome, so conditioning the sample on code presence would condition on
a post-treatment variable. Code-sharing prevalence is analysed as an outcome,
never used as a filter (§6 H1a).

**Recorded for every frame paper (including census-excluded):** DOI,
publication dates (online-first and issue), received/accepted dates where
published, open-access status, presence of data and code availability
statements, quantitative flag, computational-component flag (code-based
analysis), analysis language(s).

## 3. Reproduction subset eligibility (preregistration §5)

A JAS main census paper enters the reproduction subset if **ALL** of:

1. **Computational component present** — analysis producing published
   numerical/graphical results from code.
2. **Code available in any form** (repository, archive, supplement) —
   availability claims that cannot be fulfilled are recorded as such and the
   paper is retained with verdict BLOCKED (an outcome, not an exclusion).
3. **Primary analysis in R.** Python/Julia/mixed papers are recorded and
   deferred to a documented follow-on (pipeline extension points exist but are
   untested; deferral avoids conflating language support with reproducibility
   findings).
4. **Estimated compute within cap:** ≤168 hours (7 days) wall-clock per paper
   on the study's reference hardware (hardware documented per run in
   `environment.md`). The cap bounds scope, not membership: where a paper's
   full analysis exceeds the cap but the paper archives intermediate outputs
   (e.g. posterior draws or fitted model objects), downstream verification
   targets are regenerated from those archives — the table-regeneration path
   exercised by the §8 regression gate — and coverage is scored on the testable
   targets. Papers over cap with no archived intermediates are recorded as
   over-cap, not silently dropped.
5. **No study-team co-authorship.** Papers co-authored by study personnel are
   census-included (flagged) but excluded from reproduction to avoid
   self-assessment.

**Data availability is deliberately NOT an eligibility criterion** — it is the
H2 predictor and must vary across the subset. Papers with inaccessible data are
attempted and their coverage and verdicts recorded as the data warrant.

## 4. Resource cap (preregistration §5)

If the eligible subset exceeds 25 papers, a simple random sample of 25 is drawn
(seeded; seed and sampling code published). If fewer than 15 are eligible, all
are reproduced and the shortfall is reported as a limitation. The pre-scale
cost gate may raise the sampling cap above 25 (with the same seeded procedure,
recorded before the subset is drawn) as budget permits.

---

Receipt-token: 8f88ae3af8e03284
