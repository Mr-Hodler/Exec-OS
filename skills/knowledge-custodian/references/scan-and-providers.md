# Scan and providers

Scan is read-only. It builds the picture that Advise reasons over, across every active provider, and never changes anything.

## The provider model

One scan target abstraction, four substrates:

- **Local filesystem.** Path trees under `scope_paths`. Read structure and metadata directly.
- **Google Drive (mounted).** When Drive is mounted as a filesystem (for example a Drive folder under a user path), treat it exactly like local paths. Read the tree and metadata.
- **Google Workspace files (Docs/Sheets/Slides).** These appear in the Drive tree as files. Read their metadata (owner, last modified, sharing/visibility) where the provider exposes it. Content of native Workspace files is not parsed for dedup; identity is judged by metadata and any exported representation.
- **Notion.** Read workspaces, databases, and pages via the connector as a structure tree (titles, parents, last edited, type). Notion is a structure to advise on in v1.0, never to reorganize.

Activate a provider only if it is enabled in `platforms` and reachable. Report any provider that is configured but unreachable, and continue with the rest.

## What Scan reads

Per item, where available: path or location, type, size, last modified, owner, sharing/visibility, depth in the tree. Per tree: total counts, size distribution, depth distribution, largest folders, deepest paths, and sprawl (folders with too many loose files).

Never descend into a `never_touch` path. Never follow a link out of scope. Stat nothing in the blacklist.

## Hybrid duplicate detection

Exact duplicates must be proven, not guessed; full hashing must not be wasteful.

1. **Prefilter.** Group candidates by a cheap signature: same size, and same or similar name, optionally same mtime. Files with a unique size cannot be exact duplicates of anything, so they are excluded from hashing.
2. **Hash the candidates.** For each candidate group, compute a content hash (SHA-256) per file. Files with identical hashes are **exact duplicates**, proven.
3. **Report duplicate groups.** For each group: the canonical copy (the one in the most correct location, or the oldest original), and the redundant copies, with paths and sizes. Advise proposes archiving the redundant copies (move to `_archive/`), never deleting them, and never before the user confirms.
4. **Near-duplicates.** Same name with different content, or high textual similarity across documents, are flagged in a separate list for human judgment. Never auto-merge, never auto-pick a winner.

For very large trees, hash lazily (only candidate groups) and report progress; never block on hashing the whole tree.

## Scan cache and incremental re-scan

Full scans of large Drives are expensive. Persist a scan index so re-runs only process what changed.

- **Index location.** Store under the snapshot folder, for example `_snapshots/scan-index.json`. The index is metadata only (paths, sizes, mtimes, content hashes, provider), never file contents, and never anything from the blacklist.
- **Incremental re-scan.** On a re-run, compare current paths/sizes/mtimes against the index. Only changed or new items are re-hashed and re-classified. Unchanged items are reused from the index. Deleted-at-source items are noted (knowledge-custodian does not act on them, it reports).
- **Invalidation.** A changed size or mtime invalidates that item's cached hash. A moved item (same hash, new path) is recognized as a move, not a new file.
- **Full rescan.** Always offer a forced full rescan (ignore the index), and rebuild the index when scope paths or providers change.
- **Freshness.** Report the index age and what was reused vs recomputed, so the user knows how current the picture is.

The cache is an optimization, never a source of truth that overrides reality: if the index and the filesystem disagree, the filesystem wins and the index is corrected.

## Organizational signals pass (for Architect)

Beyond hygiene, Scan can collect the signals Architect needs to read the company's structure from its information topology. This pass is read-only and optional (run it when Architect is the goal).

Signals to capture, where the providers expose them:

- **File-type mix.** The distribution of types per area (docs, sheets, code, design, media), which hints at what each area does.
- **Provider/drive types.** What lives where (local vs Drive vs Notion vs Workspace), and which provider a function actually works in.
- **Product and team areas.** Folder/space names and clustering that map to products, functions, and teams.
- **Collaboration and access graph.** Who creates, edits, and shares what, across people and providers (from Drive sharing, Workspace ownership, Notion editors). This reveals how teams actually collaborate, not how the org chart says they do.
- **Activity hotspots and dead zones.** Where edits concentrate, and what has gone cold.
- **Ownership concentration.** Areas owned or edited by a single person (bottleneck/key-person risk) vs broadly shared areas.

Privacy and safety: this pass reads metadata and structure (names, owners, timestamps, sharing), not the private contents of personal files. Never read inside the blacklist; never infer about individuals beyond what the file topology plainly shows; surface patterns about structure and collaboration, not judgments about people.

## Output

A structured inventory: tree shape and hotspots, the duplicate groups (exact, proven) and near-duplicate flags, orphan and stale candidates by metadata, naming-pattern observations, and (when run) the organizational-signals set above. This object is the input Advise and Architect need; Scan itself recommends nothing and changes nothing.
