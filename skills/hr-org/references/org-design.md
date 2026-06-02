# Org design method

Design the organization across four dimensions at once, grounded in the de-facto map from knowledge-custodian and the company strategy. The output is the Organization Model.

## Inputs

- **De-facto functional map** (knowledge-custodian Architect): how the company actually works today, with confidence and evidence. The strongest starting point.
- **Strategy and product structure** (Founder-OS): where the company is going and what it builds.
- **Stage, headcount, sites, work modes** (config and the user).

If the de-facto map is missing, offer to run knowledge-custodian first, or proceed from the user's description and label the design as not yet evidence-grounded.

## The four dimensions

### 1. Functional
Teams and departments, and what each owns. Define for every area: mission, scope, owned outcomes, and decision rights. Avoid orphaned responsibilities (work no team owns) and overlaps (two teams owning the same thing). Map to the chosen operating model from `operating-models.md`.

### 2. Product
Product lines or areas, and the teams aligned to them. Decide where teams are stream-aligned to a product slice vs functional craft groups serving all products. Identify a shared technical or operational core that warrants a platform team.

### 3. Geographic (sites / offices)
Locations and how distributed work is coordinated. For each site: what functions live there, time-zone overlap, and which decisions are local vs central. Distribution raises coordination cost; compensate with clearer ownership and explicit asynchronous interfaces rather than more meetings.

### 4. Work mode
Remote, hybrid, or onsite per team, and the rituals each implies. Remote-first needs strong written norms and async decision records; hybrid needs deliberate overlap and anchor days; onsite leans on presence. Match the mode to the work, and make the implied rituals explicit so the mode actually functions.

## Interfaces and ownership (where most frictions live)

Boxes are easy; interfaces are where orgs fail. For every boundary, define:

- **Ownership:** exactly one team owns each outcome. No orphans, no duplicates.
- **Decision rights:** who decides, who is consulted, who is informed (a light RACI). Keep it minimal and explicit.
- **Interaction mode** (from Team Topologies): collaboration (temporary, close), X-as-a-service (clean consume/provide), or facilitating (help then leave). Default to as-a-service to reduce coupling.
- **Cross-team operations:** the recurring operations that span teams (release, incident, planning, GTM hand-off), each with an owner and a cadence.

## From de-facto to target

State the current de-facto structure, the target, and the gap. Recommend the smallest set of moves that closes the highest-value gap first (a missing owner, a silo to bridge, a team that should split for cognitive load). Avoid big-bang reorgs; sequence changes. Note where Conway's law means the team change must precede the architecture change (or vice versa).

## Output

Update `Organization-Model.md` (schema in `organization-model.md`) with the four-dimensional design and the interfaces. Deliver an org chart and a team-interaction map (visuals if allowed), the model rationale and trade-offs, the transition notes, and the explicit handoff to knowledge-custodian so the information architecture follows the org (for example marketing design assets land under `marketing/design/`, product specs under the owning product team).
