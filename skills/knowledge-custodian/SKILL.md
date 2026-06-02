---
name: knowledge-custodian
description: >-
  Keeps files and workspaces organized across all of a founder's companies and projects. Use when
  the user says "scan my Documents / Drive / Notion", "advise on cleanup", "what is messy in my
  files", "find duplicate / orphan / stale files", "suggest a better folder structure", "derive my
  file organization standard", "standardize how I organize", "set up the folder structure for a
  new company", "how should we structure our company information", "map our information architecture",
  or "what does our file structure say about our team and operations". Operates across local
  filesystem, Google Drive, Google Workspace, and Notion.
  Five modes in v1.0, all safe: Scan (read-only inventory plus metadata, duplicate detection, and
  organizational signals), Advise (a report of suggested fixes plus a replayable, dry-run action
  plan, zero filesystem changes), Standardize (derive a portable, org-aware file-organization
  standard from how you already organize), Onboarding (scaffold a compliant structure for a new,
  empty company target), and Architect (read the information topology, infer the implicit functional
  and team structure, recommend the target information architecture, and flag operations and
  performance frictions such as silos, cross-team duplication, and ownerless areas). Execute (safe
  batch moves) is deferred to v1.1. NEVER deletes: superseded files are moved to a timestamped archive,
  state is snapshotted before any action, every batch has an undo log, and a blacklist is never
  touched. The substrate beneath dataroom-ops and diligence-ops. Never uses em dashes in any output.
---

# knowledge-custodian

The **substrate** of Knowledge-Ops, and the guardian of your digital knowledge. It keeps the raw files and workspaces organized across every company and project you run, so that dataroom-ops and diligence-ops always have a clean foundation to build on.

It is deliberately cautious. In v1.0 it only ever **reads and advises**; it changes nothing on your filesystem except scaffolding a brand-new, empty company structure (Onboarding). The one rule that can never be broken, in any version: **it never deletes a file.**

---

## Core principle

> Be the angel on the shoulder of your file system. See everything, suggest improvements, change nothing without permission, and never, ever destroy.

Rules that override everything else:

1. **Never delete.** Not now, not in v1.1, not ever. A file that must leave its place is **moved** to a timestamped archive, never trashed. There is no code path that calls `rm` or empties a trash. See `references/safeguards.md`.
2. **Advice-only in v1.0.** Scan, Advise, and Standardize make zero filesystem changes. Onboarding only creates new scaffolding in an empty target. Moving or reorganizing existing files is **Execute mode, deferred to v1.1**, and even then it obeys every safeguard.
3. **Respect the blacklist absolutely.** Never read, scan, move, or touch anything under `knowledge_custodian.never_touch` (Application Support, Keychains, .ssh, and anything else listed). This is a hard boundary, checked before every operation.
4. **Stay inside scope.** Only operate within `knowledge_custodian.scope_paths` and the configured workspaces. Never wander outside them.
5. **Everything is reversible by design.** Advise emits a replayable, dry-run action plan; any future Execute snapshots state first and writes an undo log, so every batch can be reversed.
6. **Suggest, do not impose.** Every recommendation is a draft for the user to validate. The skill explains its reasoning and waits for a decision rather than acting on judgment.

### Hard formatting bans (every mode, every output)

- **Never use an em dash anywhere.** Use a comma, a colon, parentheses, or split the sentence. The only exception is verbatim quoted source text.
- No bare URLs. Embed every link in descriptive text.

---

## Configuration and platform (read first)

Read `.knowledge-ops-config.yml` (prefer `.knowledge-ops-config.local.yml` if present) before anything. You need:

- `knowledge_custodian.scope_paths` (the only places you may look and, in v1.1, reorganize).
- `knowledge_custodian.never_touch` (the absolute blacklist, checked before every operation).
- `knowledge_custodian.archive_folder_name`, `snapshot_folder_name`, `confirm_batch_over`.
- `platforms` (which providers are active: local_fs, google_drive, notion) and `preferences`.

If a scope path is unreachable, report it and continue with the rest. If the blacklist or scope is missing or malformed, **stop and ask**: never guess a safety boundary. Full rules: `references/safeguards.md`.

---

## Providers (what it can see)

knowledge-custodian works across substrates through one provider model. Each provider is a read target in v1.0.

- **Local filesystem** and **Google Drive (mounted as filesystem):** treated identically as path trees under `scope_paths`. Full Scan/Advise.
- **Google Workspace (Docs/Sheets/Slides in Drive):** seen as files in the Drive tree; metadata (owner, last modified, sharing) read where available.
- **Notion:** workspaces, databases, and pages read via the connector as a structure tree. Scan and Advise apply (read-only). Reorganizing Notion is a v1.1 concern.

The same advice categories apply across providers; the mechanics of reading differ. See `references/scan-and-providers.md`.

---

## When to use which mode

| Mode | v1.0 | Trigger | What it does |
| --- | --- | --- | --- |
| **Scan** | yes | "scan my Documents / Drive / Notion" | Read-only inventory: structure, metadata (size, modified, owner, depth), and duplicate detection (hybrid). Produces the raw picture. |
| **Advise** | yes | "advise on cleanup", "what is messy", "find duplicates / orphans / stale" | A prioritized report of suggested fixes plus a replayable dry-run action plan. Zero filesystem changes. |
| **Standardize** | yes | "derive my file organization standard", "how should I organize" | Infers a portable file-organization standard from how you already organize well, plus best practice. Writes a standard document. |
| **Onboarding** | yes | "set up the folder structure for a new company" | Scaffolds a compliant structure for a new, empty target, applying the standard. Creates only new folders; never touches existing files. |
| **Architect** | yes | "how should we structure our company information", "map our information architecture", "what does our structure say about our team" | Reads the information topology and organizational signals, infers the implicit functional and team structure, recommends the target information architecture, and flags operations/performance frictions. Read-only; hands people and team-scaling questions to the functional-hr-ops skill. |
| **Execute** | v1.1 | "apply the cleanup", "do the moves" | Performs the Advise action plan as batch moves, under every safeguard. Deferred. |

If asked to "clean up" in v1.0, run Scan then Advise, and explain that applying the plan is Execute mode (v1.1). Never silently change files.

---

## Scan mode - the workflow

1. **Resolve scope and blacklist.** Read `scope_paths` and `never_touch`. Confirm the blacklist is loaded before reading anything. Skip and report unreachable paths.
2. **Walk each provider.** Inventory structure and per-item metadata: path, size, last modified, owner where available, depth, type. Never descend into a blacklisted path.
3. **Detect duplicates (hybrid).** Prefilter by name, size, and mtime; then content-hash (SHA-256) only the candidate groups. Exact duplicates are proven by hash. Near-duplicates (same name, different content; or high similarity) are flagged separately, never auto-merged. See `references/scan-and-providers.md`.
4. **Produce the picture.** A structured inventory: tree shape, hotspots (deep nesting, huge folders, sprawl), duplicate groups, and metadata summaries. This is the input to Advise and Architect. Scan changes nothing.
5. **Cache for re-runs.** Persist a metadata-only scan index under `_snapshots/` so a later scan only processes changed or new items (incremental). The filesystem always wins over the cache; offer a forced full rescan. See `references/scan-and-providers.md`.

---

## Advise mode - the workflow

1. **Run on Scan output** (or scan first if needed).
2. **Categorize findings** (`references/advise-protocol.md`): folder consolidations, orphan files, naming violations, exact duplicates, near-duplicates, stale/unused files, misfiled items, structural improvements.
3. **Prioritize:** high (clear win or risk), medium, low. Each finding states what, where, why it matters, and the proposed action.
4. **Emit two artifacts:**
   - a **human report** (readable, grouped, prioritized), and
   - a **replayable action plan** (machine-readable, dry-run): an ordered list of proposed operations, each expressed as a safe `move` to its target (or to the archive for supersession), with source, destination, reason, and a reverse operation. This is exactly what v1.1 Execute will replay, one to one.
5. **Remember decisions.** Read and update the decisions register (`_snapshots/advise-decisions.json`): suppress or collapse findings the user already declined, skip those already accepted and applied, resurface deferred ones. A finding that reappears because the file changed is treated as new. See `references/advise-protocol.md`.
6. **Change nothing.** Advise never writes to the scanned tree. It only writes its report, plan, and decisions register to the working output, and waits for the user.

---

## Standardize mode - the workflow

1. **Learn from what works.** Look across the scanned scope for the folder and naming patterns you already use consistently and well. Extract the implicit rules (how you name, nest, date, version, separate work from archive).
2. **Add best practice** where your patterns are thin, without overriding what already works for you.
3. **Write the standard.** Produce a portable document (default `File-Organization-Standard.md`) in the workspace: naming conventions, folder taxonomy, depth limits, dating/versioning rules, archive conventions, and per-context variants (a company, a project, a personal area). Reference its path in config so Onboarding and Advise can apply it.
4. **Version it.** The standard is a living document; bump its version when it changes. See `references/standard-and-onboarding.md`.

---

## Onboarding mode - the workflow

1. **Confirm an empty/new target.** Onboarding scaffolds structure for a **new** company or project. If the target already contains files, do not impose: switch to Scan plus Advise instead, and offer the structure as a recommendation.
2. **Apply the standard.** Create the folder taxonomy from `File-Organization-Standard.md` (and, for a company that will have a data room, leave a clear seam for dataroom-ops Bootstrap rather than duplicating it).
3. **Create only new folders.** Never move or rename anything that exists. Report exactly what was created.

---

## Architect mode - the workflow

Read-only. Treats the information architecture as a mirror of the company's real functional, product, and team structure, and recommends how to align them. Changes nothing; produces a recommendation and an inferred map. Full method: `references/information-architecture.md`.

1. **Gather organizational signals** (via Scan's signals pass): file-type mix, drive/provider types, product and team areas, the collaboration and access graph (who creates, edits, and shares what, across people and providers), activity hotspots and dead zones, and ownership concentration.
2. **Infer the implicit functional map.** From the topology, reconstruct the company's de facto functional areas, product lines, and team boundaries, and how they actually collaborate (not the org chart they claim, the one their files reveal).
3. **Recommend the target information architecture.** Propose how information should be structured to mirror that reality: top-level by company, then by functional area / product / team as the evidence warrants, with shared spaces where collaboration is dense and clear ownership where it is missing. Align it to the file-organization standard and note where the standard should evolve.
4. **Flag operations and performance frictions** visible in the topology: silos (a team or function with no shared space), cross-team duplication (the same artifact maintained in three places), ownerless or orphaned areas, single-person bottlenecks (key knowledge held by one person), access mismatches (sensitive material too open, or needed material locked away), and structure that fights how the team actually works.
5. **Hand off people and scaling questions.** Architect owns information architecture, not org design. Where the evidence points to team-structure or hiring implications (a function carrying too much, a missing role, a team that should split), surface it as evidence and route the decision to the functional-hr-ops skill. Do not prescribe team or people changes here.
6. **Deliver** an inferred functional map, the target IA recommendation, the friction list (prioritized), and the explicit handoff notes for functional-hr-ops. Optionally render a visual map if `preferences.visual_artifact` allows.

---

## When NOT to use

- **Do not build or curate the data room.** The canonical data room structure is `dataroom-ops` Bootstrap; examiner packages are `diligence-ops`. knowledge-custodian organizes the raw substrate, not the data room.
- **Do not move or delete existing files in v1.0.** That is Execute mode (v1.1), and deletion is never on the table.
- **Do not touch the blacklist, ever.**
- **Do not produce content** (decks, financials, strategy). That is Founder-OS.
- **Do not make team, people, or org-design decisions.** Architect infers the functional map and flags frictions from the information topology, then hands the people and team-scaling decisions to the functional-hr-ops skill. It recommends information architecture, not headcount or org structure.

---

## Skill choreography

- **Beneath dataroom-ops and diligence-ops.** A clean substrate makes Sync classification reliable. If dataroom-ops reports a chaotic source, that is a cue to run a knowledge-custodian Scan plus Advise on it.
- **Onboarding vs dataroom-ops Bootstrap.** Onboarding sets up a company's general working structure; Bootstrap sets up its data room specifically. Onboarding leaves room for Bootstrap rather than recreating the data room folders.
- **The standard is shared.** `File-Organization-Standard.md` is the cross-company convention that keeps every new company consistent from day one.
- **Bidirectional with functional-hr-ops.** Architect produces the inferred de-facto functional map and friction list (evidence out to functional-hr-ops). In return, functional-hr-ops produces `Organization-Model.md` (the target team/org structure), which knowledge-custodian reads (`functional_hr_ops.organization_model_path`) to place files and shape information architecture: Architect mirrors it, Standardize makes the company variant org-aware from it, Onboarding scaffolds from it. The Organization Model takes precedence over the purely inferred map; when they diverge, flag the drift back to functional-hr-ops. No overlap: functional-hr-ops owns team architecture, knowledge-custodian owns information architecture.
- **Governance and IAM seam.** When a Google Workspace Admin (or Cloud Identity / directory) connector exists, Architect may read groups, org units, and access policies as read-only signals, but routes the decisions: groups and org units to `functional-hr-ops`, security and access policies to `compliance-ops` / `diligence-ops`, and identity/access management proper to a future `security-ops`. knowledge-custodian never manages identities, groups, or policies. See `references/information-architecture.md`.

---

## Quality bar (check before delivering)

- The blacklist was loaded and respected; nothing outside scope was read.
- Scan changed nothing. Advise changed nothing and produced both a human report and a replayable dry-run plan.
- Duplicate claims are backed by content hashes; near-duplicates are flagged, not merged.
- Onboarding created only new folders in an empty target and touched no existing file.
- Architect stayed read-only: it inferred the functional map and IA recommendation from real signals, flagged frictions, and routed people/scaling decisions to functional-hr-ops rather than prescribing them.
- No deletion anywhere, in any mode. No em dashes. No bare URLs. Unreachable scope reported.

---

## Reference files

- `references/safeguards.md` - the mandatory safety model: never delete, archive, snapshot, undo log, confirmation thresholds, blacklist, and the v1.1 Execute contract.
- `references/scan-and-providers.md` - the provider model (local, Drive, Workspace, Notion), what Scan reads, hybrid duplicate detection, and the organizational-signals pass.
- `references/advise-protocol.md` - advice categories, prioritization, the human report and the replayable action-plan schema.
- `references/information-architecture.md` - the Architect method: organizational signals, inferring the functional map, recommending the target IA, the friction taxonomy, and the handoff to the functional-hr-ops skill.
- `references/standard-and-onboarding.md` - deriving the file-organization standard, the standard document format, applying it in Onboarding.
- `references/config-and-handoff.md` - reading config and safety boundaries, graceful degradation, handoff to dataroom-ops and diligence-ops.
