# Verification-target coverage rules v1.0 — canonical file

**Status: FROZEN by OSF registration 2026-07-20 (DOI 10.17605/OSF.IO/DQNHG)** —
changes require the §8 regression gate + an erratum-log entry + an OSF amendment
before any affected analysis runs.
**Version:** 1.0 (extracted 2026-07-24 from preregistration §7.6)
**Canonical home** per routing design §4. Coverage is the H2 outcome; the
denominator lock below is the single most silent-failure-prone rule in the
study — treat every word as load-bearing.
**Consumers:** `reproduction-planner` and `reproduction-executor` (pushed, with
read receipt); registered in `manifest.yaml` `shared_content`.

---

## The rule (preregistration §7.6)

For each reproduction-subset paper, the approved reproduction plan enumerates
verification targets (published tables, figures, and named values) **before
execution begins**; this locked list is the denominator.

```text
Coverage = (targets reproduced exactly or within pre-stated tolerance)
           / (targets enumerated)
```

- Targets that cannot be tested (missing data, unbuildable environment)
  **count against coverage**.
- BLOCKED papers: targets enumerated from the paper text; coverage 0.
- The denominator lock prevents post hoc redefinition of scope. No target may
  be added, removed, or redefined after plan approval; a discovered enumeration
  error is a deviation to document, not a list to edit.

## Planner-side duties

- Enumerate every published table, figure, and named value as a candidate
  target; the plan records the enumerated list and any exclusions with reasons.
- **Enumeration-completeness check** (routing design §5, review D8): a
  deterministic count of display items detected in the paper is compared with
  targets enumerated; below-threshold plans are flagged for explicit human
  attention at batch approval.
- Tolerances are pre-stated per analysis in the plan (see
  `verdicts-and-precision.md`), before execution.

## Executor-side duties

- Score only against the locked list; every target is accounted for in the
  comparison report — no silent scope reduction (pipeline invariant 3).
- Untestable targets are reported with their failure mode and counted in the
  denominator.
- Compute-cap papers (preregistration §5.4): where archived intermediates
  substitute for over-cap regeneration, coverage is scored on the testable
  targets and the substitution is documented in the plan and report.

---

Receipt-token: a2a4c0a899291c2b
