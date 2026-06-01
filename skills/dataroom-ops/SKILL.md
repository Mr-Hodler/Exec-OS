---
name: dataroom-ops
description: >-
  Builds and maintains the canonical data room for a single company or project, assembled from
  Founder-OS deliverables, and keeps it clean and examiner-ready. Use when the user says "bootstrap
  my data room", "set up a data room for <company>", "sync my Founder-OS outputs into the data room",
  "pick up the latest deliverables", "audit my data room", "what is missing from the data room",
  "find stale or duplicate files in the data room", "organize my company documents for investors",
  or points to a company whose documents need to be assembled into one organized source of truth.
  Three modes: Bootstrap (lay down the canonical structure), Sync (index plus copy finals from linked
  Founder-OS repos, stamped with metadata), Audit (gaps, stale files, version conflicts, near-duplicates).
  Per-company and vertical: one isolated data room per company, never a shared portfolio. Platform-agnostic
  (Notion, Google Drive, SharePoint, Confluence) per .knowledge-ops-config.yml. The library that
  diligence-ops later packages for third parties. Never deletes; superseded files move to an archive.
  Never uses em dashes in any output.
---

# dataroom-ops

The **library** of Knowledge-Ops. It assembles everything you produce for a company into one canonical, organized, examiner-ready data room, then keeps it honest: no gaps, no stale files, no version conflicts, no duplicates. It is the single source of truth that `diligence-ops` later curates for investors, due diligence, the board, or an auditor.

This skill does not invent content. It collects, organizes, indexes, and stamps what already exists (chiefly Founder-OS deliverables) into a stable structure. Strategy lives in Founder-OS; the data room lives here.

---

## Core principle

> One organized source of truth per company. Fresh where it matters, stable where it counts, and always honest about what is missing.

Rules that override everything else:

1. **Per-company and vertical.** Each company or project gets its **own isolated data room**. Never merge two companies into one room, and never expose one company's data inside another's. The skill operates on one target company per run.
2. **Never delete.** A superseded or removed file is **moved** to the configured archive with a timestamp, never trashed. The data room keeps the latest version in place and the history in the archive.
3. **Index everything, copy the finals.** Sync indexes every relevant deliverable by reference and copies into the room only the approved, final artifact (hybrid mode). This keeps the room stable without losing the trail back to the source.
4. **Stamp metadata on everything.** Every item carries `audience`, `lens`, `version`, `source_skill`, and `sensitivity` (schema in config). Metadata is what lets `diligence-ops` build a package without re-reading every file.
5. **Honest gaps.** Audit reports what is missing against the canonical structure and the active stage profile. A confident "complete" is only ever true relative to a named checklist.
6. **Platform-agnostic.** The room can live on Notion, Google Drive, SharePoint, or Confluence. Read `dataroom.platform` from config; never hardcode a platform or an ID.

### Hard formatting bans (every mode, every output)

- **Never use an em dash anywhere.** Use a comma, a colon, parentheses, or split the sentence. The only exception is verbatim quoted source text.
- No bare URLs. Embed every link in descriptive text.

---

## Configuration and platform (read first)

Before doing anything, read `.knowledge-ops-config.yml` (prefer `.knowledge-ops-config.local.yml` if present). You need:

- `dataroom.platform`, `dataroom.root_name`, `dataroom.canonical_structure`, `dataroom.metadata_schema`.
- `linked_founder_os_repos` (the source of deliverables for Sync) and the **target company** for this run.
- `diligence.stage_profiles` and `diligence.sensitivity_tiers` (Audit checks completeness against a stage; Sync stamps sensitivity).
- `knowledge_custodian.archive_folder_name` (reused as the data room archive convention).

If a linked repo path or platform is unreachable, **degrade gracefully**: do the work you can, and report exactly what you could not reach. Never fail the whole run because one source is offline. Full rules: `references/config-and-handoff.md`.

---

## When to use which mode

| Mode | Trigger | What it does |
| --- | --- | --- |
| **Bootstrap** | "set up / bootstrap the data room for <company>" | Creates the canonical folder/page structure for one company on the configured platform. Idempotent: re-running fills gaps without clobbering. |
| **Sync** | "sync / pick up the latest deliverables", "pull my Founder-OS outputs in" | Indexes every relevant deliverable from linked repos, copies finals into the room, stamps metadata, archives superseded versions. |
| **Audit** | "audit the data room", "what is missing", "find stale / duplicate / conflicting files" | Reports gaps vs the canonical structure and stage profile, stale files, version conflicts, and near-duplicates. Read-only; proposes fixes, does not apply them unless asked. |

If the request is ambiguous, default to **Audit** (read-only, safe).

---

## Bootstrap mode - the workflow

1. **Identify the target company.** Match it to a `linked_founder_os_repos` entry (by `company`). If none matches, ask once for the company name and offer to add it to config.
2. **Read the canonical structure** from `dataroom.canonical_structure`. Do not invent folders; use the configured taxonomy. See `references/canonical-structure.md` for what each folder holds.
3. **Create the room** named per company (for example `"<Company> Data Room"`, derived from `dataroom.root_name`) on `dataroom.platform`, with the canonical folders/pages as children. Add `99_DD_QA_&_Trackers` with empty Q&A and access-log placeholders for `diligence-ops`.
4. **Idempotency.** If the room exists, create only missing folders. Never overwrite or reorder existing content. Report what was created vs already present.
5. **Seed an index page** at the root: the folder map, the target stage profile, and a "last synced" line (blank until first Sync).

Details and platform-specific block syntax: `references/canonical-structure.md`.

---

## Sync mode - the workflow

1. **Resolve sources.** From `linked_founder_os_repos`, locate the target company's repo and its `outputs/` (and any other deliverable folders). Skip and report unreachable paths.
2. **Classify each deliverable.** Map it to a canonical folder and a `lens` (finance, legal, product, commercial, governance, hr, ip), and infer `source_skill` from path/metadata. See `references/sync-protocol.md`.
3. **Hybrid pickup.** Index every relevant deliverable by reference (link back to source). Copy into the room only the **approved final** artifact. When "final" is ambiguous, index it and flag it for confirmation rather than copying a draft.
4. **Stamp metadata.** Apply the full `metadata_schema`: `audience`, `lens`, `version`, `source_skill`, `sensitivity` (default sensitivity from the folder's tier; see `references/sync-protocol.md`).
5. **Version and archive.** If a newer version of an existing item arrives, place the new version in the room and **move the prior one to the archive** (timestamped), recording the supersession. Never delete.
6. **Deduplicate.** Detect identical content by hash; keep one canonical copy and reference the rest. Report near-duplicates for human judgment (do not auto-merge).
7. **Update the index** and the "last synced" line. Report a manifest: added, updated, archived, skipped, flagged.

Full mechanics, metadata defaults, hashing, and version rules: `references/sync-protocol.md`.

---

## Audit mode - the workflow

Read-only. Produces a report; applies nothing unless the user explicitly says "fix it".

1. **Pick the yardstick.** Read the target **stage profile** (`diligence.stage_profiles`) or ask which stage to audit against. Completeness is always relative to a named checklist.
2. **Gap detection.** Compare room contents to the canonical structure and the stage's expected items. List missing and thin items, grouped by canonical folder. See `references/audit-protocol.md`.
3. **Stale detection.** Flag items older than their freshness window (financials, cap table, metrics age fastest) and anything whose `version` lags its Founder-OS source.
4. **Version conflicts.** Flag multiple live versions of the same item in the room, or a room version older than the source.
5. **Near-duplicates.** Surface content-similar items that should be consolidated.
6. **Sensitivity sanity.** Flag items missing a `sensitivity` tag or mis-tiered for their folder.
7. **Report.** A prioritized punch list: blocker / should-fix / nice-to-have, each with the suggested action (sync, archive, consolidate, request from Founder-OS). Offer to run the fixes (which route back to Sync or to an archive move).

Report format and freshness windows: `references/audit-protocol.md`.

---

## Agnostic by design

- **Company-agnostic.** Works for any company in `linked_founder_os_repos`; one isolated room each.
- **Platform-agnostic.** Honors `dataroom.platform`; never hardcodes IDs, property names, or a platform. Reads live structure at runtime.
- **Stage-agnostic.** Audits and structures against whatever stage profile is active (seed to M&A).
- **Language.** Default output is English; switch only if the user asks.

---

## When NOT to use

- **Do not curate examiner-facing packages here.** Selecting, redacting, and assembling a package for an investor, a DD request, the board, or an auditor is `diligence-ops`. dataroom-ops only builds and maintains the underlying library.
- **Do not produce strategy or metrics content.** Pitch decks, business models, GTM, and the metrics dashboard come from Founder-OS. dataroom-ops collects and organizes them, it does not write them.
- **Do not reorganize the raw filesystem.** Cleaning up Documents/Drive structure is `knowledge-custodian`. dataroom-ops touches only the canonical data room.
- **Never delete a file.** If something must go, it is archived.

---

## Skill choreography

- **Upstream: Founder-OS.** Sync reads each company's Founder-OS `outputs/`. The metrics dashboard (`metrics-aggregation-view`) and decks/financials produced there are the raw material; dataroom-ops does not duplicate them.
- **Downstream: diligence-ops.** dataroom-ops produces the canonical, metadata-stamped corpus. diligence-ops consumes it to build stage- and audience-specific packages, and writes its Q&A and access logs back into `99_DD_QA_&_Trackers`.
- **Beneath: knowledge-custodian.** Organizes the raw files on disk/Drive before they ever reach the data room. If Sync finds a chaotic source, it can suggest a knowledge-custodian pass, but does not run it.

---

## Quality bar (check before delivering)

- The room is per-company and isolated; no cross-company leakage.
- Every item in the room carries the full metadata schema, including a sensitivity tier.
- Sync copied only finals, indexed the rest, and archived (never deleted) superseded versions.
- Audit measured completeness against a **named** stage profile and produced a prioritized punch list.
- Platform, structure, and IDs were read from config and the live workspace, never hardcoded.
- No em dashes anywhere. No bare URLs. Unreachable sources reported rather than silently skipped.

---

## Reference files

- `references/canonical-structure.md` - the canonical taxonomy, what each folder holds, and per-stage subsets (calibrated on SICTIC, Startup Board Academy, Elysium Lab).
- `references/sync-protocol.md` - hybrid index-plus-copy mechanics, metadata stamping, versioning and archive rules, hashing and dedup.
- `references/audit-protocol.md` - gap/stale/conflict/duplicate detection, freshness windows, report format.
- `references/config-and-handoff.md` - reading config, resolving linked repos, graceful degradation, the handoff contract to diligence-ops.
