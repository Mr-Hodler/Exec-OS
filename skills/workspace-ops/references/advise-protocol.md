# Advise protocol

Advise turns the Scan picture into a prioritized set of recommendations and a replayable, dry-run action plan. It changes nothing on the scanned tree. It writes only its report and plan to the working output, then waits for the user.

## Finding categories

- **Folder consolidation.** Multiple folders serving the same purpose, or deep nesting that should collapse. Propose a target structure.
- **Orphan files.** Files with no clear home (loose in a root, in a misc/ dump). Propose a destination by type or topic.
- **Naming violations.** Inconsistent with the file-organization standard (spaces vs underscores, missing dates, ad hoc versioning like `final_v2_REAL`). Propose conformant names.
- **Exact duplicates.** Proven by hash. Propose keeping the canonical copy and archiving the redundant ones.
- **Near-duplicates.** Flagged for human judgment; propose a review, not an automatic action.
- **Stale / unused.** Untouched past a freshness window for their area, or clearly superseded. Propose archiving (never deleting).
- **Misfiled items.** In the wrong folder for their type or topic. Propose the correct location.
- **Structural improvements.** Where the tree diverges from the standard. Propose alignment.

## Prioritization

- **High:** clear win or real risk (large duplicate clusters wasting space, sensitive files loose in an open location, a structure that actively causes mistakes).
- **Medium:** consistency and findability gains (naming, consolidation, misfiles).
- **Low:** cosmetic or marginal.

Each finding states: what, where (path/location), why it matters, and the proposed action.

## Artifact 1: the human report

A readable, grouped, prioritized document: a short summary (counts and the top three things to do), then findings by category and priority, each with its proposed action. Plain and honest; no pressure to act. End with a one-line statement that applying changes is Execute mode (v1.1) and that nothing has been changed.

## Artifact 2: the replayable action plan (dry-run)

A machine-readable, ordered list of proposed operations. This is exactly what v1.1 Execute will replay, one to one, so it must be precise and self-contained. Each operation:

- `op`: always a safe relocation. The only verbs are `move` (to a new destination) and `archive` (move under `_archive/<timestamp>/...`). There is no `delete` verb, ever.
- `source`: absolute source path or provider location.
- `destination`: absolute target path (for `move`) or the archive path (for `archive`).
- `reason`: the finding that justifies it.
- `reverse`: the operation that undoes it (a `move` back). This is what seeds the undo log.
- `provider`: which substrate (local, drive, notion).
- `sensitivity_note`: a flag if the item looks sensitive (PII, credentials-like names), so Execute and the user treat it carefully.

Ordering: independent operations first, dependent ones (a move into a folder that another op creates) after, so the plan applies cleanly. Group operations into batches; mark any batch larger than `confirm_batch_over` as requiring confirmation.

The plan is a proposal. Advise neither applies it nor schedules it. It hands the report and the plan to the user and stops.

### Action-plan schema and example

The plan is a JSON object so v1.1 Execute can consume it directly. Shape:

```json
{
  "plan_version": "1",
  "generated": "2026-06-01T14:30:00Z",
  "scope_root": "/Users/aron/Documents/CompanyX",
  "archive_root": "/Users/aron/Documents/CompanyX/_archive",
  "batches": [
    {
      "id": "b1",
      "label": "Archive exact duplicates",
      "requires_confirmation": true,
      "operations": [
        {
          "op": "archive",
          "source": "/Users/aron/Documents/CompanyX/old/pitch_v1.pdf",
          "destination": "/Users/aron/Documents/CompanyX/_archive/2026-06-01T1430/old/pitch_v1.pdf",
          "reason": "exact_duplicate_of:/Users/aron/Documents/CompanyX/00_Overview/pitch.pdf",
          "reverse": { "op": "move", "source": "/Users/aron/Documents/CompanyX/_archive/2026-06-01T1430/old/pitch_v1.pdf", "destination": "/Users/aron/Documents/CompanyX/old/pitch_v1.pdf" },
          "provider": "local",
          "hash": "sha256:9f2b...",
          "sensitivity_note": null
        },
        {
          "op": "move",
          "source": "/Users/aron/Documents/CompanyX/misc/cap_table.xlsx",
          "destination": "/Users/aron/Documents/CompanyX/08_Cap_Table/cap_table.xlsx",
          "reason": "misfiled: cap table belongs in 08_Cap_Table",
          "reverse": { "op": "move", "source": "/Users/aron/Documents/CompanyX/08_Cap_Table/cap_table.xlsx", "destination": "/Users/aron/Documents/CompanyX/misc/cap_table.xlsx" },
          "provider": "local",
          "hash": "sha256:1a77...",
          "sensitivity_note": "confidential"
        }
      ]
    }
  ]
}
```

Rules the schema enforces: `op` is only `move` or `archive` (never `delete`); every operation carries its `reverse`; batches over `confirm_batch_over` set `requires_confirmation: true`; operations are ordered so dependencies (a destination folder created by an earlier op) resolve first. Execute replays this object exactly; it does not re-decide.

## Decisions register

Advise remembers what the user already accepted or declined, so it does not re-suggest the same things on every run.

- **Location.** `_snapshots/advise-decisions.json` (metadata only).
- **Content.** Per finding: a stable finding id (derived from the operation signature, for example op plus source plus reason), the decision (`accepted`, `declined`, `deferred`), a timestamp, and an optional note.
- **On each run.** Suppress or down-rank findings the user `declined` (show them only in a collapsed "previously declined" list), skip those already `accepted` and applied, and resurface `deferred` ones. A finding that reappears because the underlying file changed is treated as new, not as previously declined.
- **Reversibility.** The register records decisions, never performs actions. The user can clear it to start fresh.

## Notion and Workspace specifics

For Notion and native Workspace items, v1.0 Advise still reports findings (duplicate pages, orphan pages, naming drift, stale pages) and expresses proposed actions in the plan, but flags them as **v1.1-execute** since reorganizing those providers is deferred. The user gets the advice now; the safe automated apply comes later.
