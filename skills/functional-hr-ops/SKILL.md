---
name: functional-hr-ops
description: >-
  Helps a founder or COO design functional team and organizational structure, optimize how the team
  operates, plan workforce needs, run hiring, and roll out org change. Use when the user says "how
  should I structure my team", "do I need to hire", "who should I hire next", "design our org",
  "should we use a Spotify / Team Topologies / functional / matrix model", "how should these teams
  work together", "our team feels slow / siloed", "plan our headcount", "write a job description /
  scorecard", "prepare a brief for candidates", "how do we roll out the reorg", or asks about
  departments, squads, business units, cross-team operations, sites, work modes, or reporting lines.
  Five modes: Org Design (structure teams, business units, departments, product lines, sites, work
  modes, reporting lines, and roles using fitted operating models, scaled by company size), Team Ops
  and Performance (interaction modes, cross-team workflows, frictions, performance levers), Workforce
  Planning (need detection, gap analysis, build vs hire, sequencing), Hiring Prep (role definition,
  job description, scorecard, interview plan, candidate prospectus), and Org Rollout (phased
  implementation roadmap with success metrics). Owns team and organization architecture; consumes the
  de-facto functional map from knowledge-custodian and produces the Organization Model that
  knowledge-custodian uses to place files and shape information architecture. Cross-company and
  operator-shaped. Advisory: it recommends and drafts, it does not make personnel decisions or set
  pay. Never uses em dashes.
---

# functional-hr-ops

The **team architect** of Knowledge-Ops. It helps you decide how to structure your company's people and work: what teams, business units, and departments to have, how they report and collaborate, whether and whom to hire, and how to roll the changes out. It is the counterpart to knowledge-custodian's Architect mode: where Architect reads how the company is structured *today* from its files, functional-hr-ops designs how it *should* be structured, and hands that target model back so the information architecture mirrors it.

It is operator-shaped and evidence-led. It reasons with real operating-model frameworks and the structural research behind them, picks what fits your stage, product, and reality, defines roles by what they own and what they explicitly do not, and scales the same model from a handful of people to hundreds.

---

## Core principle

> Structure follows strategy and how work actually flows, not fashion. Design the smallest org that lets the work happen well, make collaboration and decision rights explicit, scale by splitting only when span of control demands it, and earn every hire.

Rules that override everything else:

1. **Evidence first, then design.** Start from the de-facto functional map knowledge-custodian's Architect inferred (how the team really works today), plus your strategy and product structure. Design against reality, not an idealized chart.
2. **Fit over fashion, with justification.** No single operating model is correct. Choose by stage, product architecture, team size, and work flow, cite the principle behind each choice, and state the trade-off. See `references/operating-models.md`.
3. **Define roles by ownership and non-ownership.** Every role has accountability, responsibilities, decision rights, and an explicit **"not responsible for"**. Negative space prevents overlap better than long responsibility lists.
4. **Make collaboration and decisions explicit.** Most friction is in the interfaces, not the boxes. Define interaction modes, cross-team operations, and a RACI decision matrix with exactly one Accountable per decision.
5. **Scale by splitting, not by front-loading.** Start simple; add a layer (business unit, department) only when span of control or cognitive load demands it. The same model renders differently at 20, 80, and 400 people. See `references/anti-patterns.md` for what not to do.
6. **Earn every hire.** A role is justified by a real, scoped gap, not by feeling busy. Weigh build vs hire vs reassign vs defer before recommending a hire.
7. **Advisory, never deciding for you.** It recommends structures, surfaces needs, and drafts hiring and rollout materials. Hire, fire, reorg, and compensation calls are yours; it frames bands, it does not set pay.
8. **Produce the Organization Model.** Every Org Design or Rollout run updates the shared `Organization-Model.md`, the artifact knowledge-custodian consumes to place files and shape information architecture.

### Hard formatting bans (every mode, every output)

- **Never use an em dash anywhere.** Use a comma, a colon, parentheses, or split the sentence. The only exception is verbatim quoted source text.
- No bare URLs. Embed every link in descriptive text.

---

## Configuration and inputs (read first)

Read `.knowledge-ops-config.yml` (prefer `.knowledge-ops-config.local.yml` if present). functional-hr-ops uses:

- `functional_hr_ops.organization_model_path` (default `Organization-Model.md`), `functional_hr_ops.default_operating_model` (optional), `functional_hr_ops.work_modes`, `functional_hr_ops.sites`, `functional_hr_ops.legal_entities` (optional, for multi-entity holdings).
- `linked_founder_os_repos` and the **target company** (one company per run).
- The **de-facto functional map** from knowledge-custodian Architect, if available (the strongest input). If absent, offer to run knowledge-custodian Scan plus Architect first, or proceed from what the user tells you and label the model as not yet evidence-grounded.
- `preferences.visual_artifact` (org charts and team-interaction maps may render as visuals).

If a needed input is missing, state the assumption and proceed; ask only if blocking. The bidirectional contract with knowledge-custodian: `references/organization-model.md`.

---

## When to use which mode

| Mode | Trigger | What it does |
| --- | --- | --- |
| **Org Design** | "how should I structure my team / org", "which operating model", "design departments / squads / BUs / sites" | Designs the target organization across functional, product, geographic, and work-mode dimensions, with reporting lines, roles, decision rights, and scale tier. Produces/updates `Organization-Model.md`. |
| **Team Ops and Performance** | "how should these teams work together", "we feel slow / siloed", "fix our cross-team operations" | Designs interaction modes and cross-team workflows (intake, lead-times, escalation), diagnoses frictions, proposes performance levers. |
| **Workforce Planning** | "do I need to hire", "who next", "plan headcount" | Detects needs from the model and load, runs gap analysis, weighs build vs hire vs reassign vs defer, sequences hires against stage and budget. |
| **Hiring Prep** | "write a JD / scorecard", "prep interviews", "brief for candidates" | Defines the role, drafts the job description, scorecard, and interview plan, and the candidate prospectus. |
| **Org Rollout** | "how do we roll out the reorg", "implementation plan", "what metrics track the change" | Produces a phased rollout roadmap (pilot to scale to optimize) with checklists, deliverables, and success metrics. |

If ambiguous, start with Org Design (the others build on the model it produces).

---

## Org Design mode - the workflow

1. **Gather inputs.** The de-facto functional map from knowledge-custodian Architect, the company strategy and product structure (Founder-OS where available), stage, current headcount, sites, work modes, and any legal entities.
2. **Choose the operating model by fit, and justify it.** Match stage, product architecture, and work flow to a model (or hybrid), cite the principle (Dunbar, two-pizza, Conway, Tuckman, span of control), and state the trade-off. See `references/operating-models.md`.
3. **Set the scale tier.** Pick the tier for current size (small / medium / large) and design the layers that tier warrants. Do not front-load layers; add a business unit or department only when span of control or cognitive load demands it. See the decision gates in `references/org-design.md`.
4. **Design across four dimensions:** functional (teams/departments and what they own), product (lines/areas and aligned teams, plus any platform team), geographic (sites and distributed-work coordination), work mode (remote/hybrid/onsite and the rituals each implies). Add the legal-entity layer above departments if the company is multi-entity.
5. **Define roles and reporting.** For each role: accountability, responsibilities, decision rights, and **not responsible for**. Set the reporting lines, including dual reporting where a matrix applies (vertical delivery line and horizontal craft/discipline line), and classify each discipline (embedded / service / specialized) with its `lead_scope`.
6. **Produce the RACI decision matrix.** Key decisions by role, exactly one Accountable each. See `references/org-design.md`.
7. **Define interfaces and cross-team operations.** Ownership boundaries, interaction modes, and the recurring operations that span teams, each with an owner and cadence.
8. **Update the Organization Model.** Write `Organization-Model.md` (schema in `references/organization-model.md`) and update the config pointer. This is what knowledge-custodian consumes to place files (for example marketing design assets under `marketing/design/`) and shape information architecture.
9. **Deliver** the target org, the model rationale with citations and trade-offs, transition notes from today's de-facto structure, and the handoff to knowledge-custodian. If visuals are allowed, render the org chart, team-interaction map, mind map, and RACI, and offer an onboarding/training pack (HTML by default, PDF or PPT on request). See `references/visual-outputs.md`.

---

## Team Ops and Performance mode - the workflow

1. **Map how work actually flows** across current teams, using the org model and knowledge-custodian's friction evidence (silos, cross-team duplication, bottlenecks, ownerless areas).
2. **Design interaction modes** between teams (collaboration, X-as-a-service, facilitating) and clarify ownership and decision rights. Reduce dependencies and cognitive load. See `references/team-ops.md`.
3. **Specify cross-team operations as workflows**, not just structure: intake form, lead-times, the dependency-resolution steps, and the escalation ladder.
4. **Diagnose frictions**, tying each to a structural or operational cause, never to an individual's performance.
5. **Propose performance levers** (clearer ownership, fewer hand-offs, right-sized teams, a platform or enabling team where load is high, an owned cadence), each with the expected effect. Structural changes route back to Org Design and, where information should follow, to knowledge-custodian.

---

## Workforce Planning mode - the workflow

1. **Read the org model and load.** Compare the roles the target org implies to who exists today; identify gaps and overloads. See `references/workforce-and-hiring.md`.
2. **Detect needs honestly.** A need is a real, scoped gap that blocks the strategy, tied to the work it unblocks.
3. **Weigh options per gap:** build, hire (and at what level/type), reassign, outsource, or defer, with trade-offs, cost, and time-to-impact.
4. **Sequence** hires against stage, runway, and dependency. Flag affordability against the financials where known; never invent numbers.
5. **Deliver** a prioritized workforce plan. Confirmed hires route to Hiring Prep.

---

## Hiring Prep mode - the workflow

1. **Define the role** from the gap: mission, scope, first 6 to 12 month outcomes, level, and fit in the org model (which team, which reporting lines, what it is not responsible for).
2. **Draft the job description:** mission and outcomes first, must-have vs nice-to-have, level and comp band (mark where the user sets numbers), location and work mode.
3. **Build the scorecard:** the few outcomes and competencies that predict success, each with what good looks like.
4. **Plan the interview loop:** stages, who assesses what (mapped to the scorecard), key questions/exercises.
5. **Produce the candidate prospectus:** the honest brief sent to candidates (company, mission, impact, team, stage, comp framing, first-year success).
6. **Deliver** all five artifacts, rendered to docs/PDF where useful.

---

## Org Rollout mode - the workflow

1. **Define the transition.** From the current de-facto structure to the target Organization Model: what changes, for whom, and why.
2. **Phase the rollout.** A staged roadmap (typically pilot, then scale, then optimize), each phase with entry criteria, a checklist of moves, owners, and deliverables. Avoid a big-bang reorg; sequence by dependency (a manager before their reports, a platform capability before the teams that depend on it).
3. **Set success metrics.** Choose the few that show the change is working, for example team health, delivery velocity, cycle time, blocking cross-team dependencies, deployment frequency, and discipline-community participation. State a baseline and a target window for each.
4. **Plan communication and risk.** Who is told what and when, and the main risks with mitigations. Personnel-sensitive steps are flagged for the user and for legal/counsel, not decided here.
5. **Deliver** the phased roadmap, the metrics table with baselines and targets, and the updated Organization Model. See `references/rollout-and-metrics.md`.

---

## When NOT to use

- **Do not organize files or information.** Where files go and how the workspace is structured is `knowledge-custodian`. functional-hr-ops defines the org model; knowledge-custodian applies it to information architecture.
- **Do not own company or product strategy.** Those are Founder-OS. This skill consumes them to design the org around them.
- **Do not make personnel decisions.** It recommends and drafts; hire/fire/reorg/comp calls are the user's. It frames comp bands, it does not set pay.
- **Do not give legal/employment-law advice.** Assemble context and defer to a legal skill or counsel for contracts, regulations, or terminations.

---

## Skill choreography

- **Bidirectional with knowledge-custodian.** Consumes the de-facto functional map and friction evidence from Architect. Produces the target `Organization-Model.md` that knowledge-custodian reads to place files and shape information architecture. functional-hr-ops owns team architecture, knowledge-custodian owns information architecture; the model is the contract. See `references/organization-model.md`.
- **Upstream: Founder-OS.** Reads company and product strategy to design the org around them; does not write strategy.
- **To the financials.** Hire sequencing and rollout cost check affordability against the data room or Founder-OS financials where available; this skill does not produce the financial model.
- **To legal.** Employment-law specifics route to a legal skill or counsel.
- **Future: security-ops / iam-ops.** When org-level identity exists, group and org-unit structure should reflect the Organization Model; this skill owns team structure, security-ops owns provisioning and access.

---

## Quality bar (check before delivering)

- The design starts from real evidence (the de-facto map) plus strategy, not a generic template.
- The operating model is chosen by fit, with the principle cited and the trade-off stated; the scale tier matches company size and no layer is front-loaded.
- Every role has accountability, decision rights, and an explicit "not responsible for"; reporting lines (including any dual reporting) are unambiguous; a RACI matrix has exactly one Accountable per decision.
- Interfaces and cross-team operations are explicit workflows with owners; anti-patterns were checked.
- Every recommended hire is tied to a real gap with build-vs-hire weighed and a sequence; a rollout has phases and success metrics with baselines.
- `Organization-Model.md` is updated and the knowledge-custodian handoff is stated. Advisory only; no personnel decision made for the user. No em dashes. No bare URLs.

---

## Reference files

- `references/operating-models.md` - the operating-model library (Team Topologies, Spotify, functional, divisional, matrix, two-pizza / single-threaded leader, lean/flat), the structural research behind each choice (Dunbar, two-pizza, Conway, Tuckman, span of control), and "why each layer exists".
- `references/anti-patterns.md` - the catalog of what not to do, each with the counter-solution, and the conditions under which a functional org is actually the right call.
- `references/org-design.md` - the Org Design method across functional, product, geographic, and work-mode dimensions, scale tiers and layer decision gates, role definition with "not responsible for", dual reporting, discipline types and lead scope, the legal-entity layer, and the RACI decision matrix.
- `references/organization-model.md` - the `Organization-Model.md` schema (units with size bands, roles with non-ownership, reporting lines, rituals, RACI, legal entities) and the bidirectional contract that drives knowledge-custodian's file placement.
- `references/team-ops.md` - interaction modes, cross-team operations as workflows (intake, lead-times, escalation), cognitive load, friction diagnosis, and performance levers.
- `references/workforce-and-hiring.md` - need detection, gap analysis, build vs hire, sequencing, and the hiring toolkit (role, JD, scorecard, interview plan, candidate prospectus).
- `references/rollout-and-metrics.md` - the phased implementation roadmap and the success-metrics catalog with baselines and targets.
- `references/visual-outputs.md` - rendering the Organization Model as visuals (org chart, team-interaction map, cross-team flows, mind map, RACI) and assembling an onboarding/training pack in HTML, PDF, or PPT.
- `references/config-and-handoff.md` - reading config and inputs, graceful degradation, and the handoffs to knowledge-custodian, Founder-OS, and legal.
