# Packaging and access

Delivery is **hybrid**: a live, access-filtered view by default, plus a standalone export bundle on demand. Sensitivity is enforced hard, and every disclosure is logged.

## Sensitivity tiers (the gate)

Read `diligence.sensitivity_tiers`. The default meaning:

- **public** - shareable openly (pitch deck, public one-pager). Goes into any package.
- **confidential** - NDA-gated (financials, contracts, cap table, most of the room). Goes into a package only after the recipient is under NDA; the NDA status is recorded in the access log.
- **restricted** - principals and counsel only (employee PII, active litigation detail, core IP/source, anything whose leak is irreversible). **Hard-blocked from packages by default.**

## Hard-block rule for restricted

A `restricted` item never enters a package automatically. To include one:

1. The user must explicitly request that specific item.
2. A reason is recorded with the override (why this recipient needs it).
3. The access log captures the override, the item, the recipient, and the timestamp.

Never override silently, never override a whole tier at once, and never include restricted content in a board pack or investor view unless that exact body owns it and the override is logged. When in doubt, exclude and ask.

## Gating granularity

Gating is **file-level by default**: an item is either in the package or not, based on its tier and the recipient's access level. This is robust and auditable.

Document-level **redaction** (obscuring parts of a file while sharing the rest) is offered only when the user explicitly asks, and is treated as higher risk: it is fragile on PII and legal documents, must be reviewed by the user before sharing, and the redacted output is saved as a new file (the source is never modified). Prefer excluding a sensitive document over redacting it.

## Mis-tier handling

If an item's tier looks wrong for its content (PII tagged public, a deck tagged restricted for no reason), flag it before packaging. A too-open tag on sensitive content is a blocker: stop and confirm, do not ship it. Route the correction to dataroom-ops (which owns the tags); diligence-ops does not silently retag source items.

## Delivery mode A: access-filtered view (default)

On the data room platform (`dataroom.platform`), build a view scoped to the recipient's access level:

- **Notion:** a filtered view or a shared sub-page tree exposing only items at or below the granted tier; share with the recipient's access and capture the share event.
- **Google Drive / SharePoint:** a shared folder (or a copy-curated folder) containing only the permitted items, with link sharing set to the recipient.
- **Confluence:** a space or page tree with restricted permissions matching the tier.

The view is live: as dataroom-ops syncs updates, the recipient sees current versions. This is the preferred mode for an active process because it is current and fully logged.

## Delivery mode B: export bundle (on demand)

When the third party needs an offline package:

- Assemble the permitted items into a standalone bundle: a zip preserving the canonical folder structure, or a single combined PDF for a reading package (use the relevant document skill).
- Stamp a cover sheet: company, stage/framework, generation date, sensitivity level of the bundle, and a contents index.
- An export is a **snapshot**: record its generation in the access log and note that it does not auto-update. Regenerate on material change.
- Never put `restricted` content in an export without a logged override.

## The access log (non-negotiable)

Maintained in `99_DD_QA_&_Trackers/Access_Log`. One row per disclosure:

- recipient (name, organization), process (which raise / DD / audit / board),
- what was granted (view or export, which folders/items),
- sensitivity level granted, NDA status,
- any restricted-item overrides with their reasons,
- timestamp, and who authorized it.

In a live process the access log is updated at the moment of disclosure, not reconstructed later. It is the record that lets you answer "who saw what" months later, which is exactly what an examiner or a dispute will ask.
