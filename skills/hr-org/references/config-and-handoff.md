# Config and handoff

## Reading config and inputs (first)

Begin by reading `.knowledge-ops-config.yml` (prefer `.knowledge-ops-config.local.yml` if present). hr-org uses:

- `hr_org.organization_model_path` (default `Organization-Model.md`), `hr_org.default_operating_model` (optional), `hr_org.work_modes`, `hr_org.sites`.
- `linked_founder_os_repos` plus the target company (one per run).
- `preferences.visual_artifact`, `preferences.language`.

The strongest input is the **de-facto functional map** from knowledge-custodian Architect. Look for a recent Architect output; if absent, offer to run knowledge-custodian Scan plus Architect first, or proceed from the user's description and clearly label the design as not yet evidence-grounded.

Default output language is English unless config or the user says otherwise. Never hardcode; read.

## Resolving the target company

One company per run. Resolve from the request, else the active folder's mapping in `linked_founder_os_repos`, else ask once. Never mix two companies' org models.

## Graceful degradation

- No de-facto map available: proceed from strategy and user input, label as not evidence-grounded, and recommend a knowledge-custodian pass to ground it.
- No financials for affordability: sequence hires by dependency and stage, flag affordability as unverified rather than inventing numbers.
- `Organization-Model.md` missing: create it on the first Org Design run.

## Handoffs

- **knowledge-custodian (bidirectional).** Consumes the de-facto map and frictions; produces `Organization-Model.md`. knowledge-custodian reads the model to place files and shape information architecture. hr-org owns team architecture, knowledge-custodian owns information architecture; the model is the contract. Details: `organization-model.md`.
- **Founder-OS (upstream).** Reads company and product strategy to design the org around them; does not write strategy.
- **Financials.** Checks hire affordability against the data room or Founder-OS financials where available; does not produce the financial model.
- **Legal.** Employment contracts, employment-law, and termination specifics route to a legal skill or counsel. hr-org provides structure and drafts, never legal advice.
- **Future security-ops / iam-ops.** When org-level identity exists, groups and org units should mirror the Organization Model; hr-org owns team structure, security-ops owns identity and access provisioning.

## The advisory boundary

hr-org recommends and drafts. It does not make hire, fire, reorg, or compensation decisions, and it does not set salary numbers (it frames bands for the user to fill). Personnel decisions and their consequences are the user's. Surface analysis and options; let the operator decide.
