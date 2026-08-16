# Preregistration register — llm-reproducibility project layer

**Load order (academic-prose gate).** Read in full, in this order:

1. `~/personal-assistant/data/notes/style-guides/academic/reference_register-academic.md`
   (canonical academic register — always applies)
2. `~/personal-assistant/data/notes/style-guides/academic/reference_register-preregistration.md`
   (canonical preregistration supplement — applies to registered text)
3. This file (project specifics; overrides on conflict)

This note carries only what would NOT transfer to another preregistered
project. Created 2026-08-17 (Shawn's decision, generalise-then-specialise);
the amendment-1 precedents cited below are anchored in
`studies/open-science-compliance/prereg/amendment-1-draft.md`.

## Registration identity

- OSF DOI **10.17605/OSF.IO/DQNHG** — never changes across versions.
- Placement precedent (amendment 1, 2026-08-03): amendment text is
  **appended to the registration's Summary field under a dated banner**;
  round-trip verification confirmed byte-identical storage and
  `updated_response_keys` exactly `["summary"]`.
- Repository tag convention: `osf-amendment-N-YYYY-MM-DD`.

## Registered vocabulary — where it lives

- The lodged registration text (prereg v0.7 at `ee3fda3`) and its
  amendments.
- Ratified operative text: `studies/open-science-compliance/prereg/erratum-log.md`
  (Entry 3 + queued amendment 2 scope).
- Instrument canon: `studies/open-science-compliance/protocol/instruments/fair-instrument.md`
  (the `canon-begin`/`canon-end` region; v2.1 vocabulary includes: research
  surface, principal artefact, rung (i)/(ii), by-construction entitlement,
  evidence pack, operative default).
- Never conflate the Tier 0–4 access tiers with the registered L1–L6
  data-availability taxonomy (demarcation note in the instrument).

## Project tooling and checks

- **Paste artefact tool:** `scripts/unwrap-paste-file.py` (M14–M16 fixes;
  `tests/test_unwrap_paste.py` anchors idempotence on the lodged
  amendment-1 artefact).
- **Consistency check = maintenance rule 4:** amendment operative text
  word-for-word against the canonical instrument, the Pass 6 prompt
  mirror, and the erratum log; deliberate differences recorded in the
  amendment draft's record section.
- **Quality gates at the lodgement commit:** D5 manifest-consistency gate
  PASS (includes C7 content-integrity hashes) and the full test suite
  green.
- **Token classes verified at promotion** (amendment-1 precedent, four
  classes): numbers/statistics; identifiers (DOIs, versions, model pins,
  dates); registered vocabulary terms; quoted strings.
- Lodgement route: OSF API versioned registration update (amendment-1
  session records the working recipe).
