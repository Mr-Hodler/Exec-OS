# Config and handoff

## Reading config (always first)

Begin every run by reading `.knowledge-ops-config.yml` (prefer `.knowledge-ops-config.local.yml` if present). diligence-ops depends on:

- `diligence.default_jurisdiction` (CH), `diligence.stage_profiles`, `diligence.sensitivity_tiers`, `diligence.qa_tracker`.
- `dataroom.platform`, `dataroom.canonical_structure`, `dataroom.metadata_schema` (the room it reads).
- `linked_founder_os_repos` plus the target company.
- `preferences.visual_artifact`, `preferences.ai_ops_autonomous`, `preferences.language`.

Never hardcode a platform, an ID, or a tier; read them. Default output language is English unless config or the user says otherwise.

## Resolving the target company

One company per run, exactly as dataroom-ops. Resolve from the user's request, else the active folder's mapping to `linked_founder_os_repos`, else ask once. Never package two companies together; never default silently when several are configured.

## Consuming the dataroom-ops corpus

diligence-ops is a pure consumer of the canonical data room:

- It reads items and their metadata (`audience`, `lens`, `version`, `source_skill`, `sensitivity`). The `sensitivity` tag is the gate; if an item lacks one, treat it as `restricted` until dataroom-ops tags it.
- It relies on the canonical structure (00 to 99) being stable. It does not create or move source items.
- The only place it writes is `99_DD_QA_&_Trackers` (Q&A tracker, evidence index, access log).

If the room does not exist or is stale, stop and hand off to dataroom-ops (Bootstrap / Sync / Audit) before packaging. Packaging a stale or incomplete room is a worse outcome than a short delay.

## Routing missing items (never fabricate)

When a checklist item or a DD question has no evidence in the room:

1. If it exists in Founder-OS, route a **Sync request** to dataroom-ops naming the specific item.
2. If it does not exist yet, route a **produce request** to the relevant Founder-OS skill (for example a financial model, a market report, the metrics dashboard).
3. Mark the tracker row **missing** with the owner and the route. Never answer from assumption.

## Graceful degradation

- Data room platform unreachable: stop before disclosing anything; explain what is missing; offer to proceed once connected. Never ship a partial package from a guessed location.
- Metrics dashboard unavailable for reporting: build the pack with the room's `09_Traction` data and flag which numbers are pending from the dashboard. Do not re-derive metrics.
- A linked repo offline: report it; do not fail the whole run.

## Handoff contracts

- **From dataroom-ops:** canonical structure, full metadata (especially `sensitivity` and `audience`), and the existence of `99_DD_QA_&_Trackers`. diligence-ops trusts these and writes the trackers back.
- **To dataroom-ops:** missing/stale item requests, and mis-tier corrections (diligence-ops flags; dataroom-ops retags, since it owns the source).
- **To legal/compliance:** diligence-ops assembles evidence and drafts factual answers; it defers legal judgment and formal opinions to a legal skill or counsel. It never gives legal advice.
- **To scheduling:** recurring reporting registers a scheduled task; the generation and gating logic stay in diligence-ops.
