# Config and handoff

## Reading config (always first)

Every run begins by reading `.knowledge-ops-config.yml`. If `.knowledge-ops-config.local.yml` exists, prefer it (it holds machine-specific paths). The fields dataroom-ops depends on:

- `dataroom.platform` - where the room lives. All write/read operations honor this. Never hardcode a platform or an ID.
- `dataroom.root_name` - base name for the per-company room (`"<Company> Data Room"`).
- `dataroom.canonical_structure` - the top-level taxonomy to create and audit against.
- `dataroom.metadata_schema` - the fields stamped on every item.
- `linked_founder_os_repos` - the deliverable sources for Sync, each a `path` plus a `company`.
- `diligence.stage_profiles` and `diligence.sensitivity_tiers` - the Audit yardstick and the Sync sensitivity defaults.
- `knowledge_custodian.archive_folder_name` - reused as the data room archive convention.

## Resolving the target company

dataroom-ops operates on **one company per run**. Resolve the target in this order:

1. The company named in the user's request.
2. If the active Cowork folder maps to a `linked_founder_os_repos` entry, use that.
3. Otherwise ask once, and offer to add the company to `linked_founder_os_repos`.

Never assume a default company when several are configured, and never operate on two at once.

## Graceful degradation

Sources and platforms can be offline or unmounted in a given session.

- If a linked repo path is unreachable: do the rest, and report it under "skipped: unreachable" with the path. Do not fail the run.
- If the platform connector is unavailable: stop before writing, explain what is missing, and offer to proceed once connected. Do not write a partial room to a fallback location.
- If a config field is missing: use the documented default where one exists (for example archive folder name), and flag the gap. For safety-relevant fields with no safe default, ask.

## The handoff contract to diligence-ops

dataroom-ops is the producer; diligence-ops is the consumer. The contract that makes the handoff work:

1. **Structure is canonical and stable.** diligence-ops can rely on the top-level numbering and folder meaning in `canonical-structure.md`.
2. **Every item carries the full metadata schema**, especially `sensitivity` and `audience`. diligence-ops builds access-controlled packages from these tags without re-reading every file.
3. **`99_DD_QA_&_Trackers` exists** (Bootstrap creates the placeholders). diligence-ops writes the Q&A tracker, evidence index, and access log there. dataroom-ops does not write into these during normal Sync, but Audit may flag them as stale.
4. **The index reflects reality.** "Last synced" and the manifest history let diligence-ops know how fresh the corpus is before it packages anything.

When diligence-ops reports that a required item is missing for a given stage or examiner, that request routes back here: Sync it if it exists in Founder-OS, or flag it for Founder-OS to produce.

## The handoff from knowledge-custodian

knowledge-custodian organizes the raw files on disk and Drive. If Sync encounters a chaotic or ambiguous source (deliverables scattered, no clear "final"), it may recommend a knowledge-custodian Scan/Advise pass on that source, but dataroom-ops does not reorganize the source filesystem itself. It reads what is there and reports what made classification hard.
