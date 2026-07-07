# Scout report P1 (prior-art, VERIFIED): LLM-assisted reproduction/replication tooling

**Pipeline:** P1 of the 2026-07-07/08 overnight stack-positioning sweep
**Proposer:** prior-art-scout agent (2026-07-07); **Verifier:** prior-art-scout-verifier
(fresh context, authoritative-API re-query)
**Verification outcome:** 98/98 claims PASS (16 GitHub repos via `gh api`, 2 live sites via
curl; all 7 cited arXiv IDs independently confirmed real). Zero corrections. Cleared for use.
**Orchestrator note:** the verifier's integrated report follows verbatim (original and
corrected tables are identical because no cell changed). Draft provenance:
scratchpad `scout-p1-prior-art-reproduction-draft.md`.

---

## Executive summary

This is an **active-but-unsolved** space, moving fast, with a clear and defensible gap for humanities, arts, and social sciences (HASS) generally and archaeology specifically. Every serious benchmark and pipeline found targets machine learning/computer science (PaperBench, SUPER, RE-Bench, CSR-Bench, BixBench, NatureBench) or, at best, quantitative social science with standardised statistical outputs (CORE-Bench, REPRO-Bench, SocSci-Repro-Bench, the Kohler/Ash "Read the Paper, Write the Code" line, the Institute for Replication's "AI Replication Engine"). None of the candidates found execute qualitative, mixed-methods, or archaeological/fieldwork-based analyses, and none combine Docker-based execution with an explicit FAIR scoring pass and an adversarial-review stage in the way the user's pipeline does. A meaningful fraction of the "social science" candidates (REPRO-Bench, ReproRepo, the ARA metadata-graph tool) explicitly do *not* execute code — they compare against existing human reproduction reports or static paper/repo metadata, which is a materially weaker claim than what the user's pipeline already does. The genuinely code-executing social-science-facing work (CORE-Bench, SocSci-Repro-Bench, "Read the Paper, Write the Code", the LLM-Assisted Replication for Quantitative Social Science prototype) is all less than 18 months old, mostly single-paper preprints rather than maintained tooling, and concentrated in economics/political science/psychology rather than archaeology or HASS broadly. The grant framing "we do end-to-end Docker reproduction + FAIR + adversarial review, for archaeology specifically" appears to be unclaimed territory as of this search.

## Verification

**Summary**

- Rows verified: 18 (16 GitHub repositories, 2 live websites) — 98 individual claims
- Pass: 98 / 98 claims (all 18 rows)
- Fail: 0 (no dead URLs, no absent repositories, no licence mismatches, no wrong-source errors)
- Partial: 0 (no numeric drift beyond tolerance)
- Unverifiable: 0 (no API errors, rate limits, or timeouts)

**Confabulation risk assessment**

- Hard-failure rate: 0/98 = 0%
- Dominant failure pattern: **No failures.** Every star count, last-active date, primary
  language, and SPDX licence identifier reproduced *exactly* against the GitHub API — not
  merely within tolerance, but to the digit and to the day. Both non-repository rows
  (i4replication.org, sciscore.com) returned HTTP 200. Notably, the proposer did **not**
  confabulate star counts or last-active dates for the two non-repository rows (14, 18) —
  it correctly recorded "n/a" and "ongoing", which is the honest-methodology signature, not
  the confabulation signature.
- Recommendation: **Report cleared for use.**

**Corrections applied:** none required. Two cosmetic notes (not mismatches): SPDX
"NOASSERTION" glossed as "custom/Other" in rows 7/9/16; row 4's display name "PaperBench"
vs canonical repo `openai/frontier-evals` (project-within-repo label).

**Supplementary diligence:** all seven arXiv IDs cited in prose resolve to real papers with
matching titles — 2606.11447 (AI Coding Agents Can Reproduce Social Science Findings;
Alizadeh et al. 2026), 2606.11456, 2602.18453, 2606.13670, 2604.18752 (SHARP), 2605.16377
(CheckSupport), 2604.24658 ("The Last Human-Written Paper: Agent-Native Research
Artifacts").

**High-vigilance acknowledgment (verifier):** a zero-correction result on an 18-row table
was treated as a red flag; every row individually re-queried (no sampling), the four
highest-suspicion rows re-queried twice (values stable), all repos confirmed
`archived: false`, `fork: false`. The cleanliness is genuine.

## Candidates table (verified; no cells changed from draft)

| # | Name | Type | URL | Stars/DLs | Last active | Fit | Notes |
|---|------|------|-----|-----------|-------------|-----|-------|
| 1 | Paper2Agent | GitHub repo (Python/Jupyter) | github.com/jmiao24/Paper2Agent | 2,290 | 2026-02-10 | LOW-MEDIUM | Turns a paper into an interactive MCP-server agent (mainly bioinformatics/AlphaGenome-style use cases); reproducibility checking is one downstream capability, not the core purpose. Not Docker-based; not HASS. |
| 2 | "Read the Paper, Write the Code" / `social_science_replicability` | GitHub repo (Python) — companion to Kohler, Zollikofer, Einsiedler, Hoyle & Ash preprint | github.com/benjamin-kohler/social_science_replicability | 25 | 2026-04-26 | MEDIUM-HIGH | Closest conceptual match found: agents reimplement analyses from method description alone (code withheld), cell-level comparison against 48 human-verified social-science papers. R/Python/Stata. No licence file declared — reuse would need author contact. No archaeology papers in the set. |
| 3 | i4replication "AI Replication Engine" | GitHub repo + blog (Institute for Replication) | github.com/recite/i4replication | 1 | 2025-03-12 | LOW (as shipped) | The repo itself is I4R's older replication-*data* analysis, not the agentic "Engine" described in 2026 blog posts. Per I4R's own blog, the three-agent (Reproducibility/Error-Detection/Robustness) toolkit is still pre-release, promised "later in 2026." Treat as aspirational/blog-grade until the toolkit repo actually ships. No licence declared on the existing repo. |
| 4 | PaperBench | GitHub repo (OpenAI, benchmark) | github.com/openai/frontier-evals (project/paperbench) | 1,234 | 2026-04-21 | LOW-MEDIUM | The best-resourced benchmark in the space; 20 ICML papers, 8,316 gradable sub-tasks, LLM-judge grading. MIT licence, active. But it targets *AI research* replication (build-the-codebase-from-scratch), not re-execution of an existing archaeology/R codebase — different task shape. |
| 5 | CORE-Bench | GitHub repo (Princeton, benchmark) | github.com/siegelz/core-bench | 77 | 2025-11-23 | HIGH | Closest benchmark fit: 270 tasks over 90 papers spanning CS, **social science**, and medicine; three difficulty tiers (pre-run output → Dockerfile → README only) that map almost exactly onto the user's own reproduction workflow. MIT licence, active issues/forks. No archaeology/HASS papers in the corpus as far as documented, but the task design is directly reusable as an evaluation harness or inspiration for one. |
| 6 | SUPER | GitHub repo (AI2/UW, benchmark) | github.com/allenai/super-benchmark | 53 | 2025-04-04 | LOW | Setting up and executing ML/NLP research repositories (dependency resolution, dataset config) — adjacent skill, wrong domain (pure ML engineering, not statistical/fieldwork analysis). Apache-2.0. |
| 7 | RE-Bench | GitHub repo (METR, benchmark) | github.com/METR/RE-Bench | 144 | 2025-10-16 | LOW | Frontier AI R&D capability benchmark (scaling laws, GPU kernels) vs human experts. Licence NOASSERTION — check before reuse. Not reproduction-of-published-work; it's open-ended ML research engineering. |
| 8 | REPRO-Bench | GitHub repo (UIUC Kang Lab, benchmark, ACL 2025 Findings) | github.com/uiuc-kang-lab/REPRO-Bench | 11 | 2025-11-03 | MEDIUM | 112 social-science paper/reproduction-report pairs. Important caveat: agents assess reproducibility by reading the paper + reproduction package, **they do not execute code**. This is metadata/documentation-level assessment, weaker than the user's actual Docker re-execution. No licence declared. |
| 9 | SocSci-Repro-Bench | GitHub repo (companion to "AI Coding Agents Can Reproduce Social Science Findings", arXiv:2606.11447) | github.com/malizad/SocSci-Repro-Bench | 10 | 2026-03-06 | HIGH | 221 tasks, 54 papers, political science/sociology/psychology/communication, R/Python/Stata, agents *do* execute code and reproduce with original data+code provided. Very recent (paper June 2026), R-language repo. Licence NOASSERTION — check terms. Still no archaeology/fieldwork papers. |
| 10 | NatureBench | GitHub repo (benchmark) | github.com/FrontisAI/NatureBench | 68 | 2026-07-07 | LOW | 90 tasks from Nature-family papers, containerised execution via "NatureGym." Actively updated. MIT. Purely natural-science/quantitative; no HASS coverage stated in the abstract. |
| 11 | CSR-Bench | GitHub repo (Amazon Science, benchmark) | github.com/amazon-science/CSR-Bench | 5 | 2025-07-23 | LOW | Deployment of CS research repositories (dependency/runtime fixing), not results reproduction. No licence declared. |
| 12 | BixBench | GitHub repo (Future-House, benchmark) | github.com/Future-House/BixBench | 129 | 2025-10-06 | LOW | Computational-biology data-analysis agent benchmark; well-maintained (Apache-2.0), but bioinformatics-specific, no relevance to archaeology/HASS beyond general agent-harness design ideas. |
| 13 | ReproRepo | GitHub repo (benchmark) | github.com/LithiumDA/ReproRepo | 5 | 2026-06-17 | LOW-MEDIUM | Novel idea — mines GitHub Issues as ground truth for reproducibility blockers across 1,149 ML papers — but explicitly **static-analysis only, no code execution**, and CS/ML-only. MIT. Interesting methodological idea (using issue trackers as a signal) that could be adapted, not a direct fit. |
| 14 | Institute for Replication (I4R) | Organisation/programme | i4replication.org | n/a (nonprofit) | ongoing | MEDIUM (context) | Established (2021-) nonprofit running "replication games" across economics/social science, 232+ discussion papers. The AI Replication Engine is their newest initiative (see row 3) but is pre-release. Directly relevant as the closest institutional analogue/potential collaborator or comparator for a HASS-focused grant. |
| 15 | FAIR-Checker | GitHub repo (IFB-ElixirFr) | github.com/IFB-ElixirFr/FAIR-checker | 29 | 2026-06-08 | LOW | Web tool + knowledge-graph/semantic-web approach to FAIR metadata scoring — **not LLM-based**, bioinformatics/Bioschemas-oriented. MIT. Useful precedent for what a FAIR-scoring architecture looks like, but a different technical approach (ontology matching, not LLM judgement) from the user's FAIR-assessment pass. |
| 16 | FAIRshake | GitHub repo (Maayan Lab) | github.com/MaayanLab/FAIRshake | 10 | 2025-08-28 | LOW | Older (2018-origin) human-evaluation FAIR scoring platform for biomedical digital objects. Licence NOASSERTION. Largely superseded/stale relative to newer LLM-native approaches; useful as a historical rubric-design reference only. |
| 17 | ARA (Agentic Reproducibility Assessment via Structured Reasoning) | GitHub repo (NeurIPS 2026 submission) | github.com/AndresLaverdeMarin/agentic_reproducibility_assessment | 0 | 2026-06-16 | MEDIUM | Cross-domain (213 ReScience C articles spanning multiple fields), builds a workflow-dependency graph from the paper text and scores "reconstructability" — again **no code execution**, ~61% accuracy against human-validated ground truth. GPL-3.0 (copyleft — flag if adopting code). Brand-new, zero stars, single-paper repo — very low maturity signal despite interesting method. |
| 18 | SciScore | Commercial/hosted tool | sciscore.com | n/a (100+ journals use it) | ongoing | LOW | Mature (NIH-funded, SBIR-backed), NLP/ML-based automated rigor-and-transparency checker used by Cell, J. Neuroscience, eLife, etc. Biomedical resource-identification focus (RRIDs, antibodies, cell lines) — conceptually the "FAIR/compliance checker" end of the space, but not applicable to archaeological method sections and not open source. |

## Recommendations

- **Use directly**: None. Nothing found is a drop-in replacement for the user's pipeline; everything either targets the wrong discipline (ML/CS/biomedical) or performs a strictly weaker check (metadata comparison, not execution).
- **Adapt approach**:
  - **CORE-Bench's** three-tier difficulty design (pre-run output → Dockerfile-only → README-only) is directly reusable as an internal maturity ladder for how "reproducible" each archaeology paper's materials already are before the user's pipeline even starts — worth citing as methodological precedent in the grant.
  - **SocSci-Repro-Bench** and **"Read the Paper, Write the Code"** are the two closest published methodologies for *evaluating* whether an agent's reproduction is faithful (cell-level comparison, information-isolation between agent and original code/results). Their evaluation protocol (not their code) is worth adapting for the reproduction-assessor skill's own internal validation.
  - **ReproRepo's** use of GitHub Issues as a supervision signal for "what actually goes wrong" is a cheap, novel idea for building an archaeology-specific failure taxonomy without hand-labelling.
  - **FAIR-Checker's** two-module (Check/Inspect) structure is a reasonable rubric-and-recommendation UX pattern for the FAIR-assessment pass, even though its underlying tech (knowledge graphs) differs from an LLM-judge approach.
- **Ignore**: PaperBench, SUPER, RE-Bench, CSR-Bench, BixBench, NatureBench — all strong, active, well-resourced benchmarks, but they solve a different problem (building/deploying ML codebases or evaluating frontier-model R&D capability, not re-executing a fixed statistical analysis against a fixed dataset). Paper2Agent — solves "turn paper into a queryable tool," not "verify reproducibility." FAIRshake — stale, human-scored, no LLM component, biomedical-specific.

## Build-vs-adopt verdict

**Build, informed by approaches found — with one collaboration option worth exploring.** No existing tool does end-to-end Docker-based computational reproduction plus FAIR scoring plus adversarial review for HASS/archaeology; the closest analogues (CORE-Bench, SocSci-Repro-Bench, I4R's AI Replication Engine) are economics/political-science/psychology-only, code-execution-optional, and — in I4R's case — not yet shipped as usable code. The user's pipeline is genuinely ahead of the published field on two specific axes: (1) it already executes code end-to-end via Docker rather than doing metadata-level or static comparison (which is what a majority of the 2026 "reproducibility assessment" papers settle for), and (2) it pairs reproduction with a FAIR pass and an explicit adversarial-review stage, a combination not found in any single candidate above. For the grant application, this positions the project as filling a genuine, citable gap rather than duplicating existing infrastructure — worth stating plainly that CORE-Bench/SocSci-Repro-Bench exist as social-science precedent, but that archaeology/HASS has zero comparable published tooling. The Institute for Replication is the one organisation whose trajectory (replication games → AI Replication Engine) is close enough that a scoping conversation or partnership mention could strengthen a grant narrative about "who else is in this space and why we're not duplicating them."

**Gap analysis, explicitly:**

- Does anything do end-to-end computational reproduction for HASS/archaeology specifically? **No.** Zero candidates found with archaeology, cultural heritage, or broader-HASS (beyond quantitative social science) paper corpora.
- Is the space solved, active-but-unsolved, or unclaimed? **Active-but-unsolved** for quantitative social science (a cluster of 2026 preprints, one ACL-Findings paper, one active nonprofit initiative); **essentially unclaimed** for archaeology/HASS as a discipline target, despite the general method (agentic code reproduction) clearly being technically mature enough to attempt it (per CORE-Bench and SocSci-Repro-Bench's results on adjacent social-science material).

## Search gaps and coverage notes (verifier-annotated)

- **No dedicated archaeology/HASS reproducibility benchmark or tool was found** despite multiple targeted searches (digital archaeology, computational archaeology, tDAR/Archaeology Data Service FAIR tooling, MAIA network). ADS and tDAR are FAIR-oriented data repositories, not automated/AI reproducibility checkers.
- **Established manual (non-AI) infrastructure worth citing as precedent in a grant narrative**: **CODECHECK** (codecheck.org.uk, Nüst & Eglen, human-run code review during peer review since ~2019), **ReScience C** (rescience.github.io, peer-reviewed computational-replication journal — source corpus for the ARA benchmark), and the **AEA Data Editor's** manual/semi-automated reproducibility checks for economics journals.
- **DARPA SCORE programme**: real and directly relevant to the "predicting/assessing replicability" framing (865 researchers, Nature publications April 2026), but human-forecaster-plus-classical-ML, pre-LLM era — funding-landscape context, not a technical competitor.
- **Additional single-paper preprints** (all five arXiv IDs verified real by the verifier): LLM-Assisted Replication for Quantitative Social Science (arXiv:2602.18453); Automated reproducibility assessments in the social and behavioral sciences using LLMs (arXiv:2606.13670, Holtdirk et al., 180 studies); SHARP (arXiv:2604.18752, particle physics); AI Coding Agents in Social Science (arXiv:2606.11456); CheckSupport (arXiv:2605.16377).
- **PyPI/npm**: nothing productised for "reproduce paper + Docker + R" — research-preprint code only; a polished tool would be differentiated.
- **GitLab** not separately queried (all substantive candidates GitHub-hosted; verifier confirmed).
- **Hugging Face**: Paper2Agent (tabled) and "Agent-Native Research Artifacts" (arXiv:2604.24658, verified real) — a paper-authoring protocol, not a reproduction tool; acronym collision with row 17's ARA noted.

*Machine-readable audit trail (98 pass records) retained in the session transcript; the
verifier logged its instrumentation line (checked=98, flagged=0, confab=0).*
