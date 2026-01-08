# Automation and Scaling Strategy

**Created:** 2025-12-09
**Source:** Extended discussion on modularisation, automation approaches, and context management
**Purpose:** Document decisions and recommendations for scaling to production runs (50+ papers)

---

## Executive Summary

**Key constraint:** No quality loss from current pipeline performance.

**Recommendation:** Keep interactive extraction with improved session management rather than pursuing full headless automation. The pipeline's quality comes from its multi-pass structure and skill context, which don't translate well to headless mode.

---

## Modularisation Decision

### User's Original Proposal

Three modules:
1. Basic processing
2. Open science infrastructure extraction and assessment
3. Evidence/claims/arguments/RDMAP extraction and evaluation

### Analysis Finding

**This split doesn't work** due to bidirectional dependencies:
- Cluster 3 (Reproducibility) needs BOTH infrastructure AND methods/protocols
- repliCATS Seven Signals assessment requires holistic view of paper
- FAIR assessment needs methods context to evaluate appropriately

### Recommended Alternative: Phase-Based Modularisation

```
┌─────────────────────────────────────────────────────────────────┐
│ EXTRACTION MODULE (Passes 0-7)                                  │
│ Input:  paper.txt                                               │
│ Output: extraction.json                                         │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
                      extraction.json (interface artifact)
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│ ASSESSMENT MODULE (Passes 8-10)                                 │
│ Input:  extraction.json                                         │
│ Output: classification.json, cluster-*.md, credibility-report.md│
└─────────────────────────────────────────────────────────────────┘
```

**Advantages:**
- Clean interface (extraction.json is complete, self-sufficient)
- Checkpoint recovery (if assessment fails, re-run from extraction.json)
- Selective re-assessment (update prompts without re-extracting)
- Matches natural workflow break points

---

## Automation Assessment

### Headless Mode Limitations

| Aspect | Suitability for Headless |
|--------|-------------------------|
| Single-pass deterministic tasks | ✅ Good |
| Multi-pass iterative refinement | ⚠️ Requires restructuring |
| Skill loading with references | ❌ Hard to replicate |
| Adaptive section handling | ❌ Fixed prompt only |
| Error recovery mid-process | ❌ Cannot adapt |

### Honest Assessment

The current pipeline's quality comes from:
1. 8-pass structure with context accumulation
2. Rich skill references loaded in context
3. Ability to adapt to unusual paper structures

**Headless doesn't speed up processing** — it reduces human attention requirements. For 50 papers at ~30 min each, that's ~25 hours regardless of automation approach.

### Options Under "No Quality Loss" Constraint

| Option | Quality Risk | Effort | Babysitting Reduction |
|--------|-------------|--------|----------------------|
| **Keep interactive, batch papers** | None | None | ~60% |
| **Headless assessment only** | Low | Moderate | ~30% |
| **API pipeline replicating skills** | None (if done right) | High | ~95% |
| **Prompt consolidation** | ❌ REJECTED | - | - |

**Decision:** Keep interactive extraction with improved session management for now. API pipeline is the "real" long-term solution if scale demands it.

---

## Context Management Strategy

### The Problem

User wants graceful exit at ~80% context rather than:
- Erratic behaviour near 100%
- Unexpected stops after auto-compact disabled
- "Hurrying" as context runs low

### Key Finding: No Programmatic Context Monitoring

**Claude cannot:**
- Check own context percentage
- Access token counts
- Know when near limit
- Call /context programmatically

**Hooks cannot:**
- Access real-time token counts
- Know remaining context budget
- Trigger graceful exit based on context %

**Feature request exists:** GitHub issue #5547 for real-time context monitoring

### Session Capacity Analysis (from ~/.claude history)

| Session Size | Typical Content | Estimated Capacity |
|--------------|-----------------|-------------------|
| 5-10 MB | 1 paper (extraction + assessment) | Safe single paper |
| 30-50 MB | 2-3 papers + discussion | Moderate session |
| 70-100 MB | 3-5 papers with multiple runs | Near capacity |
| 100-140 MB | Extended heavy work | At/exceeding safe limits |

**Rule of thumb:** ~5-10 MB per paper extraction+assessment cycle

### Recommended Approach: Conservative Fixed Limits + PreCompact Hook

#### 1. Disable Auto-Compact

Add to `~/.claude/settings.json`:
```json
{
  "autoCompact": false,
  "cleanupPeriodDays": 99999
}
```

This prevents mid-extraction disruption. Manual /compact or /clear when needed.

#### 2. Set Hard Limit: 3 Papers Per Session

Conservative but guarantees:
- No quality degradation from context pressure
- Predictable stopping points
- No surprises

#### 3. Add PreCompact Hook as Backup Alert

```json
{
  "hooks": {
    "PreCompact": {
      "command": "echo '[$(date)] CONTEXT NEARLY FULL - session $(pwd)' >> ~/claude-context-alerts.log && notify-send 'Claude Code' 'Context nearly full - consider clearing'"
    }
  }
}
```

**Note:** PreCompact fires at 95% threshold. With auto-compact disabled, this becomes a "stop now" alert rather than "too late" notification.

#### 4. Workflow Modification for Auto-Continue

Current workflow stops after each paper. Modify to:

```markdown
## After Completing Assessment

1. Update queue.yaml with completion status
2. Check papers_completed_this_session counter
3. If counter < 3 AND next pending paper exists:
   - Report: "Paper X complete. Continuing to Paper Y..."
   - Begin extraction for next paper automatically
4. If counter >= 3 OR no pending papers:
   - Report: "Reached session limit (3 papers). Recommend /clear before continuing."
   - Stop and wait for user
```

---

## Production Workflow (Recommended)

### For 50 Papers

**Phase 1: Batched Interactive Extraction**
```
Session 1: Papers 1-3 (extract + assess) → /clear
Session 2: Papers 4-6 (extract + assess) → /clear
...
Session 17: Papers 49-50 (extract + assess) → done
```

**Estimated time:** 17 sessions × ~1.5 hours = ~25 hours total
**Human attention:** Start session, return after ~1.5 hours, /clear, repeat

**Phase 2: Aggregation and Analysis**
- Run aggregation script on all credibility-report.md files
- Generate corpus-level statistics
- Identify patterns and outliers

### Alternative: Weekend Run Approach

1. Start Friday evening
2. Process 3 papers, /clear
3. Check Saturday morning, start next batch
4. Continue through weekend
5. ~50 papers over 2-3 days with periodic check-ins

---

## Future Improvements (If Scale Demands)

### Short-Term (No Development)
- [x] Document workflow (this file)
- [ ] Configure PreCompact hook
- [ ] Test 3-paper batching on production corpus

### Medium-Term (Moderate Effort)
- [ ] Headless assessment only (extraction stays interactive)
- [ ] Automated queue management script
- [ ] Post-run aggregation script

### Long-Term (Significant Effort)
- [ ] API pipeline replicating full skill context
- [ ] Parallel paper processing
- [ ] Real-time progress dashboard

---

## Files to Modify for Implementation

| File | Change |
|------|--------|
| `~/.claude/settings.json` | Add autoCompact: false, hooks config |
| `input/workflow.md` | Add session paper limit, auto-continue logic |
| `.claude/commands/production-run.md` | New command for batched production |
| `scripts/aggregate-corpus-results.py` | Post-run analysis (create when needed) |

---

## Related Documentation

- `planning/open-science-production-readiness.md` — FAIR scoring issues, corpus selection
- `planning/research-design-anchoring-assessment.md` — RD extraction anchoring (low priority)
- `planning/extraction-as-data-improvements.md` — Extraction consistency (if needed)
- `docs/automation-approaches/CC-advanced-techniques.md` — Headless mode patterns
- `docs/automation-approaches/CC-research-workflows-guide.md` — Research automation philosophy

---

## Decision Summary

| Question | Decision |
|----------|----------|
| Modularise by content type? | No — use phase-based (Extraction/Assessment) |
| Go fully headless? | No — quality loss unacceptable |
| Consolidate prompts? | No — loses pass-by-pass nuance |
| How many papers per session? | 3 (conservative, safe) |
| How to monitor context? | PreCompact hook + fixed limits |
| Long-term automation path? | API pipeline (future work) |

---

*Document created from automation strategy discussion, 2025-12-09*
