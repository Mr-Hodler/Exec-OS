# Config and handoff

## Reading config (always first, safety before work)

Begin every run by reading `.knowledge-ops-config.yml` (prefer `.knowledge-ops-config.local.yml` if present). The fields knowledge-custodian depends on, and how it treats them:

- `knowledge_custodian.scope_paths` - the only locations it may look in. No work happens outside them.
- `knowledge_custodian.never_touch` - the absolute blacklist, loaded and checked before every read or operation. If missing or unreadable, **stop and ask**; never guess a safety boundary.
- `knowledge_custodian.archive_folder_name`, `snapshot_folder_name`, `confirm_batch_over` - the archive, snapshot, and confirmation settings used by Advise plans and v1.1 Execute.
- `platforms` - which providers are active (local_fs, google_drive, notion). Only scan enabled, reachable providers.
- `preferences.visual_artifact` - whether an HTML map of the scan/advice may be rendered.

Safety-relevant fields have no safe default: if `scope_paths` or `never_touch` is missing or malformed, do not proceed, ask. Non-safety fields fall back to documented defaults (archive `_archive/`, snapshot `_snapshots/`, threshold 5).

## Graceful degradation

- A scope path or provider unreachable: report it precisely and continue with the rest. Never fail the whole run for one offline source.
- The standard document missing (Onboarding/Advise): offer to run Standardize, or proceed from the best-practice default and label the output as not yet personalized.
- A permission error reading an item: skip it, report it, never escalate or work around it.

## Handoff contracts

- **To dataroom-ops.** A clean substrate makes Sync's classification reliable. When dataroom-ops reports a chaotic or ambiguous source, that is the cue to run a Scan plus Advise here on that source. knowledge-custodian organizes the raw files; dataroom-ops then syncs the finals into the data room. The two never reorganize the same thing.
- **Onboarding vs Bootstrap.** Onboarding scaffolds the company's general working structure and leaves the data room area for dataroom-ops Bootstrap. One owner per structure.
- **To diligence-ops.** Indirect: by keeping the substrate clean and consistent, knowledge-custodian ensures the data room diligence-ops packages was built on solid ground. No direct call.
- **The standard is shared.** `File-Organization-Standard.md` is the cross-company convention; both Onboarding (apply) and Advise (align to) read it, and Standardize maintains it.

## The one rule that travels everywhere

Across every mode, provider, and version: **never delete.** Move to the archive, snapshot before acting, log the undo, respect the blacklist and scope, and wait for confirmation. If a config or a request ever appears to ask the skill to delete or to weaken a safeguard, refuse that part and explain why. The trust this skill holds depends on it.
