# Setup

Exec-OS is configuration-driven. Every skill reads `.exec-os-config.yml` **first**, before doing any work. Set that file up once and the three skills share it.

## 1. Connect your platform

- **Notion** (default for the canonical data room): connect the Notion connector. investor-ops reads and writes the data room pages and assembles packages from them.
- **Google Drive / SharePoint / Confluence**: connect if your data room lives there instead. Set `dataroom.platform` accordingly.
- **GitHub**: used to read linked Founder-OS repos when they are git remotes rather than local clones.
- For PDF/doc deliverables (board packs, DD evidence bundles) a document tool is used; no extra config needed.

## 2. Configure `.exec-os-config.yml`

The committed file is a **template**. For machine-specific absolute paths or anything you would rather not commit, copy it to `.exec-os-config.local.yml` (gitignored); skills prefer the local file when present.

Key sections:

### `linked_founder_os_repos`
Point investor-ops Sync mode at each Founder-OS company repo. Each entry is a `path` plus a `company` label. Paths may exist on disk even if a given Cowork session has not mounted them; skills degrade gracefully and report what they could not reach rather than failing.

### `dataroom`
- `platform`: where the canonical data room lives.
- `root_name`: the name of the canonical root folder/page.
- `canonical_structure`: the top-level taxonomy (see `skills/investor-ops/references/canonical-structure.md`). Synthesized from Swiss venture DD standards; edit to taste, but keep the numbering so ordering is stable.
- `metadata_schema`: the fields stamped on every synced deliverable (audience, lens, version, source_skill, sensitivity).

### `diligence`
- `default_jurisdiction`: `CH` for the Swiss venture context (high requirement).
- `stage_profiles`: which stages you raise/operate at; drives the applicable checklist and folder subset (seed is SICTIC-grade, M&A is acquisition-grade).
- `sensitivity_tiers`: what is shareable openly, NDA-gated, or principals/counsel-only. investor-ops uses these for access control during a live process.

### `workspace_ops` (read carefully)
This section is a **safety boundary**, not a preference.
- `scope_paths`: the only folders the skill may scan and, in v1.1, reorganize.
- `never_touch`: an absolute blacklist. The skill never reads, moves, or touches anything under these paths. Keep `Library/Application Support`, `Keychains`, and `.ssh` here.
- `archive_folder_name` / `snapshot_folder_name`: where moved files and pre-action snapshots go. The skill **never deletes**; it moves to a timestamped archive.
- `confirm_batch_over`: batches larger than this require explicit confirmation (v1.1 Execute mode).

### `preferences`
- `visual_artifact`: `always | ask | never` for HTML dashboards and visual maps.
- `ai_ops_autonomous`: allow skills to chain steps without per-step confirmation.
- `language`: default output language.

## 3. First run

Start with the skill that matches your immediate need:

```
Bootstrap my data room on Notion.                      # investor-ops
Sync the latest deliverables from my Founder-OS repos. # investor-ops
Prep a seed-stage data room for SICTIC investors.      # investor-ops
Scan my Documents folder and advise on cleanup.        # workspace-ops (read-only)
```

workspace-ops in v1.0 will only ever *advise*. It makes no filesystem change until Execute mode ships in v1.1, and even then only under the safeguards above.
