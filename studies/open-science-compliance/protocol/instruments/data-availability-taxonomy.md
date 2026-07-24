# Data-availability taxonomy v1.0 — canonical file

**Status: FROZEN by OSF registration 2026-07-20 (DOI 10.17605/OSF.IO/DQNHG)** —
changes require the §8 regression gate + an erratum-log entry + an OSF amendment
before any affected analysis runs.
**Version:** 1.0 (six-level friction ordering adopted 2026-07-18; new instrument
drafted for the Phase 2 registration per pilot report §8.2)
**Canonical home** per routing design §4 (extracted 2026-07-24 from
preregistration §7.3).
**Registration consistency:** matches preregistration §7.3 word-for-word in the
normative definitions; formatting adapted for instrument use.
**Consumers:** `reproduction-planner` (pushed, with read receipt; L-levels are
assigned at reproduction time); registered in `manifest.yaml` `shared_content`.

---

## Six levels, ordered by access friction

The scale encodes two boundaries: whether a machine can retrieve the data
without human intervention (the L2/L3 boundary), and whether the human step is
procedural or discretionary (the L3/L4 boundary).

- **L1 open-complete:** all analysis data machine-retrievable via standard
  protocol (persistent identifier resolves to the data), no authentication.
- **L2 open-partial:** more than 50% of the paper's datasets (counting unit:
  distinct datasets enumerated in the paper's data availability statement and
  methods) machine-retrievable as for L1; remainder higher-friction or missing.
- **L3 authenticated:** retrievable after standard registration or
  authentication with a repository or service whose access grant is procedural
  (automatic, or routine review under published criteria — e.g. registration
  with a data archive), not case-by-case discretionary.
- **L4 discretionary:** available only by case-by-case permission of authors or
  custodians ("data available on request", bespoke creator or institutional
  approval); a route exists in name but the grant may be refused or go
  unanswered.
- **L5 restricted:** documented legal or ethical restriction with no access
  route for this study.
- **L6 absent:** no availability route (no statement, dead links) or an
  unfulfilled open-availability claim.

## Assignment rules

Assigned **at reproduction time from actual retrieval attempts**, not
statements alone: the level records the highest-friction step actually required
(or the terminal failure mode), and per-dataset logs record route, steps, and
outcome.

**Never assign L-levels at census time.** The census records
`stated_availability` (descriptive, from availability statements) and never
maps it to L1–L6 (routing design §5; preregistration §7.3).

**L4 request protocol:** for L4 papers a standardised data request is sent
(template published; one reminder after ten days; three-week response window
from first contact) and the outcome logged — request compliance is itself a
reported descriptive outcome. Responses arriving after the window are recorded
but do not enter the preregistered analyses; they may be incorporated in later,
clearly demarcated updates (e.g. during peer-review revision), with the timing
documented.

## Analysis collapse (3 ordered levels)

| Collapsed level | Levels | Meaning |
|---|---|---|
| open | L1–L2 | machine-retrievable without human intervention |
| mediated | L3 | procedural human step (registration/authentication) |
| effectively closed | L4–L6 | discretionary, restricted, or absent |

---

Receipt-token: 068d5f05793429d7
