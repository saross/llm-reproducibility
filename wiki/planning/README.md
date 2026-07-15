# Planning Documents

This folder contains **active planning documents** for the LLM-based research extraction and assessment project.

**Project Status:**
✅ **Phase 1 Complete**: Extraction system development (v2.0 → v2.6)
🚧 **Phase 2 In Progress**: Assessment framework development

---

## Active Planning Documents

### Master Plan

#### [credibility-implementation-plan-v2.0.md](credibility-implementation-plan-v2.0.md)
**Status:** Active master plan
**Focus:** Complete credibility assessment framework

This is the current authoritative plan, covering:
- Three Pillars Framework (Transparency → Credibility → Reproducibility)
- repliCATS Seven Signals adaptation for HASS
- Cluster-based assessment architecture
- Quality gating approach
- Implementation roadmap

### Active Working Documents

#### [agentic-modernisation-plan.md](agentic-modernisation-plan.md)
**Status:** Active (v0.3, 2026-07-07) — direction approved; Phase 1 on hold pending verdicts on §9
**Focus:** Migration of the reproduction + FAIR lanes to agents/workflows; JAS production run

#### [agent-content-routing-design.md](agent-content-routing-design.md)
**Status:** Draft for review (v0.1, 2026-07-15) — resolves modernisation plan §9 item 3;
queued for /review-implementation + prior-art scout before Phase 1 build
**Focus:** Skill/agent content division — embed role behaviour, push instruments (with
read receipts), pull pattern libraries; canonical-file registry and maintenance rules

#### [cosmos-grant-application-framing.md](cosmos-grant-application-framing.md)
**Status:** Active (v0.1, 2026-07-05) — framing agreed; budget section brainstorm-grade
**Focus:** Cosmos Institute grant application — project choice, proximity scan, pitch, budget

#### [cosmos-application-form-questions.md](cosmos-application-form-questions.md)
**Status:** Complete capture (v1.0, 2026-07-07)
**Focus:** Verbatim Cosmos application form fields + drafting implications; scopes the draft

#### [cosmos-application-draft.md](cosmos-application-draft.md)
**Status:** Working draft (v0.2, 2026-07-07) — proposal text under Shawn's review
**Focus:** Cosmos application proposal (<500 words) + framing resolutions + remaining fields

#### [scout-reports/](scout-reports/)
**Status:** Complete (2026-07-08) — 19 verified reports + synthesis (lanes P1–P6, arXiv
sweeps S1–S2, chains C1–C3, guard G1)
**Focus:** Whole-stack positioning sweep vs state of the art (reproduction, CEM, RDMAP,
credibility, FAIR, literature engagement); start at the synthesis

#### [corpus-management-plan.md](corpus-management-plan.md)
**Status:** Agreed direction (v0.1, 2026-07-13) — implementation deferred; pre-Phase-1
prerequisite for the agentic modernisation
**Focus:** Third-party article/supplement handling — out-of-tree corpus store, DOI
manifest + fetch-with-checksum, LFS/pre-commit guardrails; ends OA-vigilance for good

#### [long-tail-credibility-framework-paper.md](long-tail-credibility-framework-paper.md)
**Status:** Plan externalised (v0.1, 2026-07-13) — awaiting prioritisation after Shawn's
current paper; authorship model (solo state-of-play vs consortium) undecided
**Focus:** Framework/state-of-play paper staking out long-tail research credibility
assessment with AI; phase × status decomposition built on the verified scout sweeps

#### [active-todo-list.md](active-todo-list.md)
**Status:** Active
**Focus:** Current tasks and priorities

#### [fair-vocabularies-development-plan.md](fair-vocabularies-development-plan.md)
**Status:** Active
**Focus:** Controlled vocabulary development for extraction and assessment

### Fellowship Materials

#### [fellowship/](fellowship/)
Original fellowship proposal and supporting documents:
- `cwts_implementation_plan.md` - Original 6-month fellowship plan
- `implementation_plan_supplement.md` - Strategic decisions
- `README.md` - Fellowship overview

---

## Archived Documents

The following documents were superseded by `credibility-implementation-plan-v2.0.md` and
have been archived to [archive/planning-completed/](../../archive/planning-completed/)
(archival verified 2026-07-03):

- `assessment-implementation-plan.md` - Superseded by v2.0
- `credibility-assessment-implementation-roadmap.md` - Superseded
- `credibility-implementation-plan-detailed.md` - Superseded by v2.0
- `corpus-interpretation-framework.md` - Integrated into main plan
- `paper-credibility-analysis-framework.md` - Superseded
- `research-approach-classification-framework.md` - Now in prompts
- `extraction-assessment-rubric-v1.md` - Superseded
- `extraction-metrics-guidance-analysis.md` - Historical analysis
- `extraction-to-analysis-transition.md` - Completed transition
- `pass6-phase1-testing-findings.md` - Completed testing
- `pass6-software-documentation-enhancement.md` - Completed
- `secondary-source-attribution-analysis.md` - Completed analysis
- `synthesis-external-feedback.md` - Historical feedback
- `gpt51-feedback/` - Historical feedback from other models

---

## Previous Phase Archives

Completed planning from the extraction development phase:

### v2.0-v2.5 Planning (Archived)
See [archive/extraction-development/](../../archive/extraction-development/) for:
- Claims extraction project plans
- RDMAP implementation documents
- Schema evolution documentation
- Version-specific planning

See [archive/README.md](../../archive/README.md) for complete development history.

---

## Next Steps

**Current** (Phase 2 - Assessment):
- Complete cluster prompts (Clusters 1-3) ✅
- Quality gating refinement
- Reliability testing on additional papers
- Batch assessment tooling

**Upcoming**:
- Multi-paper corpus analysis
- FAIR vocabulary finalisation
- Community validation

---

## Related Documentation

- [Main README](../../README.md) - Project overview
- [User Guide](../../docs/user-guide/getting-started.md) - Using the extraction system
- [Research Assessor Guide](../../docs/research-assessor-guide/) - Skill documentation
- [Archive README](../../archive/README.md) - Development history

---

**Questions about planning?** See the [credibility-implementation-plan-v2.0.md](credibility-implementation-plan-v2.0.md) for the most comprehensive overview.
