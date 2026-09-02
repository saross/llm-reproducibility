# Data repair rule (dated protocol note, 2026-09-03)

**Status:** adopted by the registrant (Shawn) 2026-09-03; recorded here and
in the plan decision log — no Open Science Framework (OSF) amendment (same
governance class as the effort study: exploratory-lane procedure, scores
untouched). Fold into a future amendment only if one is otherwise needed.

## Rule

Where a paper's research surface depends on an artefact served from an
unreliable location — a personal or unmanaged server being the type case —
the FAIR score assesses the surface as published: the artefact fails the
sub-principles the evidence shows it fails (typically F1 no persistent
identifier, A2 no persistence, R1.1 no licence), per the research-surface
rule. Repair is then attempted as a **score-independent**,
above-and-beyond step in the reproduction lane, in the spirit of the
lane's minimal documented code corrections and amendment 2 §2's
identifier-recovery rule:

1. **Route (a) — archived-equivalent retrieval.** Where a properly
   archived deposit of the at-risk artefact exists (ADS or another
   reliable service), the reproduction is attempted with the archived
   copy in place of the unreliable one.
2. **Route (b) — documented re-derivation.** Where only the artefact's
   *generator* is archived or published (e.g. an OxCal model whose MCMC
   output lives on a personal server), the artefact is re-derived from
   the archived/published inputs, with the derivation scripted and
   committed. Stochastic outputs compare statistically, with the
   tolerance stated in advance — preferring the authors' own
   replicability figures where published.

A successful repair is reported as a **recoverable error** finding, with
explanation; a failed or unavailable repair leaves an **unrecoverable
error** finding. Neither outcome modifies any FAIR score. Differential
*scoring* of recoverable vs unrecoverable errors is explicitly **held in
reserve** — considered, not adopted (registrant, 2026-09-03).

## Bounds

Repair is bounded good-will work, not heroics: no cap is set today;
compute/model-time caps are to be set **empirically** if such cases recur
(registrant, 2026-09-03). Every repair records what was attempted, what it
cost, and its outcome, so a future cap has an evidence base.

## Precedent

dye-et-al-2023: `https://tsdye.online/AP/beads-1.csv` — MCMC output read
by the supplement's R code, hosted on shared commercial hosting
(last-modified 2022-10-20; live at the 2026-09-03 check), no PID, no
licence; no archived copy exists, so the case is route (b). E8-v2
adjudication log, Sitting 1, records the scoring consequences (F1, A2,
R1.1) and the queued attempt-02.
