# The Organization Model (shared artifact)

`Organization-Model.md` is the artifact functional-hr-ops produces and knowledge-custodian consumes. It is the single description of how the company is organized: legal entities, departments, business units, teams, products, sites, work modes, roles, reporting lines, rituals, decisions, and the interfaces between them. It keeps the **team** structure (owned by functional-hr-ops) and the **information** structure (owned by knowledge-custodian) in sync.

Default location: a versioned document at `functional_hr_ops.organization_model_path` (default `Organization-Model.md` in the company workspace), referenced in `.knowledge-ops-config.yml`.

## Document schema

```
# Organization Model - <Company>

version: <n>    last_updated: <YYYY-MM-DD>    stage: <pre_seed|seed|series_a|...>
scale_tier: <small|medium|large>
operating_model: <chosen model or hybrid> (principle: <Dunbar|two-pizza|Conway|...>; rationale: ...; trade-off: ...)

## Legal entities (if multi-entity)
- <Entity>: governance, shared corporate resources, which departments sit under it

## Functional structure (units)
- <Unit> (team | business_unit | department):
    mission, owned_outcomes
    size_band: { min: <n>, max: <n> }, current_headcount: <n>
    owner_role: <role>
    rituals: [<cadence>, ...]            # e.g. weekly dependency sync, quarterly planning + retro

## Product structure
- <Product line/area>: aligned_team(s), platform_dependencies

## Geographic / sites
- <Site>: functions present, time zone, local vs central decisions

## Work modes
- <Unit>: remote | hybrid | onsite, rituals/anchor days

## Roles
- <Role>:
    accountability: <the one outcome>
    responsibilities: [...]
    decision_rights: [...]
    not_responsible_for: [...]           # explicit non-ownership, prevents overlap
    reporting:
      vertical_line: <delivery owner>     # outcomes/priorities
      horizontal_line: <discipline lead>  # craft/standards (omit if no matrix)
    discipline_type: <embedded|service|specialized>   # for craft roles
    lead_scope: <bu|department|company>               # for discipline leads

## RACI decision matrix
- <decision>: { Accountable: <one role>, Responsible: [...], Consulted: [...], Informed: [...] }
  # exactly one Accountable per decision

## Interfaces and cross-team operations
- <Boundary>: owner, interaction_mode (collaboration | as-a-service | facilitating), cadence
- Cross-team ops: <release | incident | planning | GTM>: owner, cadence, lead_time, escalation_path

## Information-architecture mapping (for knowledge-custodian)
- <Team/area> -> <canonical location>, e.g. "Marketing/Design -> marketing/design/"
- Shared spaces: <where dense cross-team collaboration lives>
- Ownership: every active area maps to exactly one owning team
```

Keep it readable and versioned. Bump `version` on each Org Design or Org Rollout run and update the config pointer if the path changes.

## The bidirectional contract with knowledge-custodian

Two directions, one shared map, no overlap.

**knowledge-custodian -> functional-hr-ops (evidence in).** Architect infers the de-facto functional map and frictions from the file topology and hands them over. functional-hr-ops treats this as the strongest input: it is how the company actually works today, not how a chart claims.

**functional-hr-ops -> knowledge-custodian (target model out).** Org Design writes/updates `Organization-Model.md`. knowledge-custodian reads it to:

- **Place files.** The "Information-architecture mapping" section tells knowledge-custodian where artifacts belong (marketing design assets under `marketing/design/`, a product team's specs under that product's area, shared collaboration in the named shared space).
- **Shape the standard and structure.** Standardize makes the company variant org-aware from the model; Architect's IA recommendations align to it; Onboarding scaffolds a new company from it.

**Ownership boundary.** functional-hr-ops owns the *team* architecture (who exists, which units, how they report and interact). knowledge-custodian owns the *information* architecture (where files and workspaces live). The Organization Model is the contract; neither edits the other's domain.

## Keeping them in sync

- When functional-hr-ops changes the org (a new team, a split, a site, a rollout phase), it bumps the model; knowledge-custodian's next Architect/Standardize run picks up the change and proposes the information-architecture moves (advice-only; applying them is its Execute mode in v1.1).
- When knowledge-custodian's Architect finds the de-facto structure has drifted from the model, it flags it back as evidence for a redesign. The loop closes.
