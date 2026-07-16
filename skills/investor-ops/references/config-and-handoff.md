# Config and Handoff (investor-ops)

Merged from the former investor-ops and investor-ops. Part A covers the data room (build/sync/audit); Part B covers diligence and delivery (consume the corpus, write the trackers).

## Part A: Data Room (library)


## Reading config (always first)

Every run begins by reading `.exec-os-config.yml`. If `.exec-os-config.local.yml` exists, prefer it (it holds machine-specific paths). The fields investor-ops depends on:

- `dataroom.platform` - where the room lives. All write/read operations honor this. Never hardcode a platform or an ID.
- `dataroom.root_name` - base name for the per-company room (`"<Company> Data Room"`).
- `dataroom.canonical_structure` - the top-level taxonomy to create and audit against.
- `dataroom.metadata_schema` - the fields stamped on every item.
- `linked_founder_os_repos` - the deliverable sources for Sync, each a `path` plus a `company`.
- `diligence.stage_profiles` and `diligence.sensitivity_tiers` - the Audit yardstick and the Sync sensitivity defaults.
- `workspace_ops.archive_folder_name` - reused as the data room archive convention.

## Resolving the target company

investor-ops operates on **one company per run**. Resolve the target in this order:

1. The company named in the user's request.
2. If the active Cowork folder maps to a `linked_founder_os_repos` entry, use that.
3. Otherwise ask once, and offer to add the company to `linked_founder_os_repos`.

Never assume a default company when several are configured, and never operate on two at once.

## Graceful degradation

Sources and platforms can be offline or unmounted in a given session.

- If a linked repo path is unreachable: do the rest, and report it under "skipped: unreachable" with the path. Do not fail the run.
- If the platform connector is unavailable: stop before writing, explain what is missing, and offer to proceed once connected. Do not write a partial room to a fallback location.
- If a config field is missing: use the documented default where one exists (for example archive folder name), and flag the gap. For safety-relevant fields with no safe default, ask.

## The handoff contract to investor-ops

investor-ops is the producer; investor-ops is the consumer. The contract that makes the handoff work:

1. **Structure is canonical and stable.** investor-ops can rely on the top-level numbering and folder meaning in `canonical-structure.md`.
2. **Every item carries the full metadata schema**, especially `sensitivity` and `audience`. investor-ops builds access-controlled packages from these tags without re-reading every file.
3. **`99_DD_QA_&_Trackers` exists** (Bootstrap creates the placeholders). investor-ops writes the Q&A tracker, evidence index, and access log there. investor-ops does not write into these during normal Sync, but Audit may flag them as stale.
4. **The index reflects reality.** "Last synced" and the manifest history let investor-ops know how fresh the corpus is before it packages anything.

When investor-ops reports that a required item is missing for a given stage or examiner, that request routes back here: Sync it if it exists in Founder-OS, or flag it for Founder-OS to produce.

**Audit is the shared gap source of truth.** investor-ops does not recompute gaps; it runs or consumes this skill's Audit (against the relevant stage) as the authoritative punch-list, then layers audience and sensitivity on top. Keep Audit output stable and stage-named so investor-ops can rely on it. If investor-ops surfaces a discrepancy, treat the Audit as canonical and reconcile here rather than letting the two skills diverge.

## The handoff from workspace-ops

workspace-ops organizes the raw files on disk and Drive. If Sync encounters a chaotic or ambiguous source (deliverables scattered, no clear "final"), it may recommend a workspace-ops Scan/Advise pass on that source, but investor-ops does not reorganize the source filesystem itself. It reads what is there and reports what made classification hard.

## Part B: Diligence and Delivery


## Reading config (always first)

Begin every run by reading `.exec-os-config.yml` (prefer `.exec-os-config.local.yml` if present). investor-ops depends on:

- `diligence.default_jurisdiction` (CH), `diligence.stage_profiles`, `diligence.sensitivity_tiers`, `diligence.qa_tracker`.
- `dataroom.platform`, `dataroom.canonical_structure`, `dataroom.metadata_schema` (the room it reads).
- `linked_founder_os_repos` plus the target company.
- `preferences.visual_artifact`, `preferences.ai_ops_autonomous`, `preferences.language`.

Never hardcode a platform, an ID, or a tier; read them. Default output language is English unless config or the user says otherwise.

## Resolving the target company

One company per run, exactly as investor-ops. Resolve from the user's request, else the active folder's mapping to `linked_founder_os_repos`, else ask once. Never package two companies together; never default silently when several are configured.

## Consuming the investor-ops corpus

investor-ops is a pure consumer of the canonical data room:

- It reads items and their metadata (`audience`, `lens`, `version`, `source_skill`, `sensitivity`). The `sensitivity` tag is the gate; if an item lacks one, treat it as `restricted` until investor-ops tags it.
- It relies on the canonical structure (00 to 99) being stable. It does not create or move source items.
- The only place it writes is `99_DD_QA_&_Trackers` (Q&A tracker, evidence index, access log).

If the room does not exist or is stale, stop and hand off to investor-ops (Bootstrap / Sync / Audit) before packaging. Packaging a stale or incomplete room is a worse outcome than a short delay.

**Audit is the shared gap source of truth.** For any stage or framework, investor-ops runs or refreshes the investor-ops Audit against that stage and consumes its gap punch-list, instead of independently recomputing what is missing. investor-ops owns only what Audit does not: audience scoping, sensitivity gating, the access log, the Q&A and evidence trackers, and the examiner-facing package. If the two ever disagree, the Audit wins and investor-ops routes the discrepancy back to investor-ops. This single-source rule is what keeps the library and the delivery counter aligned.

## Routing missing items (never fabricate)

When a checklist item or a DD question has no evidence in the room:

1. If it exists in Founder-OS, route a **Sync request** to investor-ops naming the specific item.
2. If it does not exist yet, route a **produce request** to the relevant Founder-OS skill (for example a financial model, a market report, the metrics dashboard).
3. Mark the tracker row **missing** with the owner and the route. Never answer from assumption.

## Graceful degradation

- Data room platform unreachable: stop before disclosing anything; explain what is missing; offer to proceed once connected. Never ship a partial package from a guessed location.
- Metrics dashboard unavailable for reporting: build the pack with the room's `09_Traction` data and flag which numbers are pending from the dashboard. Do not re-derive metrics.
- A linked repo offline: report it; do not fail the whole run.

## Handoff contracts

- **From investor-ops:** canonical structure, full metadata (especially `sensitivity` and `audience`), and the existence of `99_DD_QA_&_Trackers`. investor-ops trusts these and writes the trackers back.
- **To investor-ops:** missing/stale item requests, and mis-tier corrections (investor-ops flags; investor-ops retags, since it owns the source).
- **To legal/compliance:** investor-ops assembles evidence and drafts factual answers; it defers legal judgment and formal opinions to a legal skill or counsel. It never gives legal advice.
- **To scheduling:** recurring reporting registers a scheduled task; the generation and gating logic stay in investor-ops.
