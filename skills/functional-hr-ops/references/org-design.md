# Org design method

Design the organization across four dimensions at once, grounded in the de-facto map from knowledge-custodian and the company strategy, scaled to the company's size. The output is the Organization Model.

## Inputs

- **De-facto functional map** (knowledge-custodian Architect): how the company actually works today, with confidence and evidence. The strongest starting point.
- **Strategy and product structure** (Founder-OS): where the company is going and what it builds.
- **Stage, headcount, sites, work modes, legal entities** (config and the user).

If the de-facto map is missing, offer to run knowledge-custodian first, or proceed from the user's description and label the design as not yet evidence-grounded.

## Scale tiers and layer decision gates

The same model renders differently by size. Pick the tier, design only the layers it warrants, and add layers by trigger, never by default.

- **Small (roughly under 50):** flat or a few stable teams. Usually no business units, no departments. One layer of management at most.
- **Medium (roughly 50 to 400):** teams grouped into business units where coordination needs an owner; functions/departments emerging.
- **Large (roughly 400+):** departments over business units over teams; company-wide craft standards; possibly multiple legal entities.

Decision gates:

- **Add a team** when an outcome needs a single small owner (two-pizza size).
- **Add a business unit** only when several teams in a domain create cross-team dependencies that need an owner. Never create a BU for a single team.
- **Add a department** when a domain grows past Dunbar and needs a senior owner and craft standards.
- **Split a unit / add a layer** when span of control exceeds about 15 to 20 reports, or cognitive load is clearly too high.
- **Golden rule:** start simple, split only when span of control or cognitive load demands it.

## The four dimensions

### 1. Functional
Teams and departments, and what each owns: mission, scope, owned outcomes, decision rights. Avoid orphaned responsibilities and overlaps. Map to the chosen operating model.

### 2. Product
Product lines or areas and the teams aligned to them. Decide where teams are stream-aligned to a product slice vs functional craft groups serving all products. Identify a shared technical or operational core that warrants a platform team.

### 3. Geographic (sites / offices)
Locations and how distributed work is coordinated. Per site: functions present, time-zone overlap, local vs central decisions. Distribution raises coordination cost; compensate with clearer ownership and explicit asynchronous interfaces, not more meetings.

### 4. Work mode
Remote, hybrid, or onsite per team, and the rituals each implies. Remote-first needs written norms and async decision records; hybrid needs deliberate overlap and anchor days; onsite leans on presence. Match the mode to the work and make the implied rituals explicit.

### Legal-entity layer (when multi-entity)
For holdings with multiple legal entities (subsidiaries, a foundation, several corporations): place entities above departments, each with its own governance, and make shared corporate resources (finance, legal, people) explicit so they are not duplicated or orphaned.

## Roles: define by ownership and non-ownership

For every leadership/role definition, specify all four:

- **Accountability:** the one outcome this role is answerable for.
- **Responsibilities:** what it does.
- **Decision rights:** what it decides (and what it is consulted on).
- **Not responsible for:** the explicit non-ownership. This negative space is the best anti-overlap device. For example a delivery owner is typically "not responsible for: technical architecture, craft hiring, salaries"; a craft/discipline lead is typically "not responsible for: product priorities, release decisions".

## Reporting lines and dual reporting

State the reporting lines. In a matrix, a person has two:

- **Vertical line (delivery):** to the team/BU/department owner, accountable for outcomes and priorities.
- **Horizontal line (craft / discipline):** to a discipline lead, accountable for craft quality, standards, and craft hiring/growth.

Classify each discipline and set its lead's scope:

- **Discipline type:** embedded (works inside a stream-aligned team: backend, frontend, mobile, QA), service (provides to many teams: design, marketing, sales, finance), or specialized (cross-cutting expertise: security, DevOps, data).
- **Allocation rule:** service disciplines allocate full-time or not at all; never fractional. If demand is partial, use an as-a-service interface with a queue.
- **Lead scope:** BU-scoped, department-scoped, or company-wide, chosen by company size and span of control (split a lead's scope when reports exceed about 15 to 20).

## RACI decision matrix (standard output)

Produce a matrix of the key recurring decisions by role, with exactly one **Accountable** per decision (plus Responsible, Consulted, Informed as needed). Typical decisions: set product priorities, release to production, resolve a cross-team dependency, set a salary, approve a hire, set craft standards, approve budget. The rule that prevents matrix paralysis: one Accountable per decision, always.

## From de-facto to target

State the current de-facto structure, the target, and the gap. Recommend the smallest set of moves that closes the highest-value gap first (a missing owner, a silo to bridge, a team to split for cognitive load). Avoid big-bang reorgs; sequence them (Org Rollout mode). Note where Conway's law means the team change must precede the architecture change.

## Output

Update `Organization-Model.md` (schema in `organization-model.md`) with the four dimensions, scale tier, roles with non-ownership, reporting lines, the RACI matrix, rituals, and any legal entities. Deliver an org chart and a team-interaction map (visuals if allowed), the rationale with cited principles and trade-offs, transition notes, and the explicit handoff to knowledge-custodian so the information architecture follows the org (for example marketing design assets under `marketing/design/`, a product team's specs under that team's area). Check the design against `anti-patterns.md` before delivering.
