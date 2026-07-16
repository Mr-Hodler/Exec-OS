# Safeguards (mandatory, every version)

These rules are not preferences. They are the reason this skill can be trusted with a real file system. They hold in v1.0 and in every future version. Weakening any of them is a breaking change that must never ship.

## 1. Never delete

There is no deletion path. Not `rm`, not `unlink`, not "empty trash", not "permanently remove". A file that must leave its location is **moved** to the archive (below). If a user explicitly asks to delete something, explain that workspace-ops only archives, never deletes, and that they can delete from the archive themselves if they truly want to. The skill does not do it.

## 2. The blacklist is absolute

Before any read or any operation, load `workspace_ops.never_touch` and confirm the target is not under it. Never read, scan, index, move, or even stat anything under a blacklisted path (Application Support, Keychains, .ssh, and whatever else is listed). If a requested operation would touch the blacklist, refuse that part and report it. If the blacklist is missing or unreadable, stop and ask; never proceed without it.

## 3. Stay inside scope

Operate only within `workspace_ops.scope_paths` and the configured providers. Never follow a symlink, mount, or reference that leads outside scope. If scanning reveals a link pointing outside scope or into the blacklist, report it and do not traverse it.

## 4. Archive, not trash

When Execute (v1.1) supersedes or relocates a file out of the way, it **moves** it under `workspace_ops.archive_folder_name` (default `_archive/`), preserving the relative path and adding a timestamp, for example `_archive/2026-06-01T1430/<original/relative/path>`. The archive is append-only from the skill's side. The original is never overwritten in place and never destroyed.

## 5. Snapshot before any action

Before Execute performs a batch, write a state snapshot under `workspace_ops.snapshot_folder_name` (default `_snapshots/`): the listing (paths, sizes, hashes, mtimes) of every file the batch will touch, plus the action plan being applied. The snapshot is what makes a reversal provable, not just hopeful.

## 6. Undo log per batch

Every Execute batch writes an undo log: for each operation, the reverse operation that restores the prior state (a move back from archive or from the new location to the old). One command, derived from the log, reverses the whole batch. The Advise action plan already carries the reverse operation per item, so the undo log is a byproduct, not extra work.

## 7. Confirmation thresholds

Execute requires explicit user confirmation for any batch larger than `workspace_ops.confirm_batch_over` (default 5) files. Below the threshold, still show the plan; above it, require a clear go. A "yes" applies to the shown plan only, never to a standing authorization.

## 8. Dry-run first, always

Execute always presents the action plan as a dry-run first (the same plan Advise produced), and applies only after confirmation. There is no "just do it" path that skips the dry-run.

## The Execute (v1.1) contract

When Execute ships, it must:

- consume the **exact** replayable action plan from Advise (no re-deciding at apply time),
- check the blacklist and scope before every single operation,
- snapshot, then apply moves only (never deletes), to the archive or to the planned destination,
- write the undo log, and
- honor the confirmation threshold.

If any precondition fails mid-batch (a path moved, a permission changed), Execute stops, reports, and leaves the snapshot and partial undo log intact so the user can reverse what was done. It never pushes through an inconsistent state.

## v1.0 boundary

In v1.0, only Onboarding writes to the filesystem, and only by **creating new empty folders in an empty target**. It never moves, renames, overwrites, or deletes an existing file. Scan, Advise, and Standardize make no change to the scanned tree at all (Standardize writes only its own standard document to the working output).
