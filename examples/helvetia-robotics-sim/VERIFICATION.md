# Exec-OS simulated test - VERIFICATION

Company: Helvetia Robotics AG (Swiss, seed). Generated artifacts for all four skills.

| # | check | result | detail |
|---|-------|--------|--------|
| 1 | action-plan: valid JSON | PASS | 3 ops |
| 2 | action-plan: only move/archive verbs (no delete) | PASS | {'move', 'archive'} |
| 3 | action-plan: every op has a reverse | PASS |  |
| 4 | action-plan: reverses are move-back (reversible) | PASS |  |
| 5 | dedup: exact duplicate found by hash | PASS | 2025 budget.xlsx,2025 budget copy.xlsx |
| 6 | org-model: all required schema sections present | PASS | missing: [] |
| 7 | org-model: RACI has exactly one Accountable per decision | PASS | 4 decisions |
| 8 | bidirectional: org-model placement and advise plan agree (marketing/design/) | PASS |  |
| 9 | dataroom: canonical folders match config | PASS | 11 folders |
| 10 | dataroom: sector overlays (hardware+ai) applied additively, base intact | PASS | 12 overlay subfolders over 11 base |
| 11 | dataroom: 99 trackers scaffolded for investor-ops | PASS |  |
| 12 | diligence: readiness names the stage and checklist (seed / SICTIC) | PASS |  |
| 13 | diligence: no restricted item disclosed in access log | PASS |  |
| 14 | style: no em dashes in any artifact | PASS | offenders: [] |

**14/14 checks passed.**