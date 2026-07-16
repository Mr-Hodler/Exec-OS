# Sync protocol

Sync is **hybrid**: index everything by reference, copy only the approved finals into the room. The goal is a room that is stable enough to show an examiner, with an unbroken trail back to the live Founder-OS source.

## 1. Resolve sources

- From `linked_founder_os_repos`, find the entry whose `company` matches the target. Read its `outputs/` directory and any other declared deliverable folders.
- If the path is unreachable (not mounted, moved, offline), record it in the manifest under "skipped: unreachable" and continue with the sources you can read. Never abort the whole Sync for one missing source.
- Note the source's own version signal where available (a version in the filename, a CHANGELOG, a git tag, or the file mtime).

## 2. Classify each deliverable

For each candidate file, decide:

- **Canonical folder** (00 to 09): map by content and origin. A pitch deck goes to `00_Overview`; a financial model to `02_Financials`; a market report to `07_Market_&_Commercial`; the metrics dashboard to `09_Traction_&_Metrics`.
- **lens:** finance, legal, product, commercial, governance, hr, ip. One primary lens per item.
- **source_skill:** infer from the path or the file's own metadata (for example `market-intel-gap`, `business-model`, `metrics-dashboard`).
- **final vs draft:** "final" means approved/released. Signals: a `final`/`v1.0+` marker, presence in a `released/` or `final/` subfolder, or an explicit approval note. When unsure, treat as draft.

## 3. Hybrid pickup

- **Index every relevant deliverable** by reference: record title, source path (as a descriptive link, never a bare URL), classification, and detected version in the room's index.
- **Copy into the room only finals.** A copied item is a stable snapshot the examiner sees. A draft is indexed and flagged ("final pending"), not copied.
- If "final" is genuinely ambiguous, index and flag for one confirmation rather than copying a possibly-wrong draft into an examiner-facing room.

## 4. Stamp metadata

Apply the full `dataroom.metadata_schema` to every item (copied or indexed):

- `audience`: default by folder. 00 = public/investor; 02, 03, 08 = confidential; PII, litigation, key IP = restricted. Refine if the source declares an audience.
- `lens`: from classification.
- `version`: the detected source version, else the sync date.
- `source_skill`: from classification.
- `sensitivity`: from `diligence.sensitivity_tiers`, defaulted by folder (see the audience defaults above). This is what investor-ops uses for access control, so never leave it blank.

On Notion, metadata is page properties (read the live schema first). On Drive/SharePoint, metadata is rows in the folder's `_index` file. On Confluence, labels plus a page-properties macro.

## 5. Version and archive (never delete)

- If an item already exists in the room and a **newer version** arrives: place the new version in the room, then **move the prior version to the archive** (`workspace_ops.archive_folder_name`, default `_archive/`) under a path that preserves the folder and adds a timestamp, for example `_archive/02_Financials/model_2026-03-01T1200.xlsx`.
- Record the supersession in the index: what replaced what, when, and the version delta.
- If the incoming item is **older** than the room's copy, do not overwrite; flag a potential conflict for Audit.
- Deletion is never an option. A removed-at-source item stays in the room (flagged "source removed") until a human decides; if it must leave the room, it is archived, not trashed.

## 6. Deduplicate

- Compute a content hash (for example SHA-256) per file. **Identical hashes** mean one canonical copy in the correct folder; the others are indexed as references to the canonical copy, not re-copied.
- **Near-duplicates** (same title, different content; or high textual similarity) are reported for human judgment. Never auto-merge or auto-pick a winner.

## 7. Manifest

End every Sync with a manifest, grouped and counted:

- **Added** (newly copied finals), **Updated** (new version in, prior archived), **Indexed** (referenced, not copied), **Archived** (superseded), **Skipped** (unreachable or out-of-scope), **Flagged** (ambiguous final, version conflict, near-duplicate, source removed).
- Update the root index's "last synced" line with the date and the target stage profile.

Keep the manifest in chat and, optionally, append it to the room index so there is a running sync history.
