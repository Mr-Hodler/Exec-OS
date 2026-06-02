# The Organization Model (shared artifact)

`Organization-Model.md` is the artifact hr-org produces and knowledge-custodian consumes. It is the single description of how the company is organized: teams, products, sites, work modes, and the interfaces between them. It is what keeps the **team** structure (owned by hr-org) and the **information** structure (owned by knowledge-custodian) in sync.

Default location: a versioned document at `hr_org.organization_model_path` (default `Organization-Model.md` in the company workspace), with the path referenced in `.knowledge-ops-config.yml`.

## Document schema

```
# Organization Model - <Company>

version: <n>    last_updated: <YYYY-MM-DD>    stage: <pre_seed|seed|series_a|...>
operating_model: <chosen model or hybrid> (rationale: ...)

## Functional structure
- <Team/Department>: mission, owned outcomes, decision rights, head/owner, headcount
  ...

## Product structure
- <Product line/area>: aligned team(s), platform dependencies
  ...

## Geographic / sites
- <Site>: functions present, time zone, local vs central decisions
  ...

## Work modes
- <Team>: remote | hybrid | onsite, rituals/anchor days

## Interfaces and cross-team operations
- <Boundary>: owner, interaction mode (collaboration | as-a-service | facilitating), cadence
- Cross-team ops: <release | incident | planning | GTM>: owner, cadence, participants

## Information-architecture mapping (for knowledge-custodian)
- <Team/area> -> <canonical location>, e.g. "Marketing/Design -> marketing/design/"
- Shared spaces: <where dense cross-team collaboration lives>
- Ownership: every active area maps to exactly one owning team
```

Keep it readable and versioned. Bump `version` on each Org Design run and update the config pointer if the path changes.

## The bidirectional contract with knowledge-custodian

Two directions, one shared map, no overlap.

**knowledge-custodian -> hr-org (evidence in).**
Architect infers the de-facto functional map and frictions from the file topology and hands them over. hr-org treats this as the strongest input to Org Design and Team Ops: it is how the company actually works today, not how a chart claims.

**hr-org -> knowledge-custodian (target model out).**
Org Design writes/updates `Organization-Model.md`. knowledge-custodian reads it to:

- **Place files.** The "Information-architecture mapping" section tells knowledge-custodian where artifacts belong. Marketing design assets go under `marketing/design/`; a product team's specs go under that product's area; shared collaboration lands in the shared space the model names.
- **Shape the standard and structure.** Standardize makes the company variant org-aware from the model; Architect's IA recommendations align to it; Onboarding scaffolds a new company from it.

**Ownership boundary.** hr-org owns the *team* architecture (who exists, which teams, how they interact). knowledge-custodian owns the *information* architecture (where files and workspaces live). The Organization Model is the contract between them: hr-org decides the org, knowledge-custodian mirrors it in the information structure. Neither edits the other's domain.

## Keeping them in sync

- When hr-org changes the org (a new team, a split, a site), it bumps the model; knowledge-custodian's next Architect/Standardize run picks up the change and proposes the information-architecture moves (advice-only; applying them is its Execute mode in v1.1).
- When knowledge-custodian's Architect finds the de-facto structure has drifted from the model (teams collaborating in ways the model does not reflect), it flags it back to hr-org as evidence for a redesign. The loop closes.
