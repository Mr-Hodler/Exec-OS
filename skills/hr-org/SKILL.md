---
name: hr-org
description: >-
  Helps a founder or COO design team and organizational structure, optimize how the team operates,
  plan workforce needs, and run hiring. Use when the user says "how should I structure my team",
  "do I need to hire", "who should I hire next", "design our org", "should we use a Spotify / Team
  Topologies / functional / matrix model", "how should these teams work together", "our team feels
  slow / siloed", "plan our headcount", "write a job description / scorecard", "prepare a brief for
  candidates", or asks about departments, squads, cross-team operations, sites, or work modes. Four
  modes: Org Design (structure teams, departments, product lines, sites, and work modes using
  operating-model frameworks), Team Ops and Performance (how the team works, cross-team interaction,
  frictions, performance levers), Workforce Planning (need detection, gap analysis, build vs hire,
  sequencing), Hiring Prep (role definition, job description, scorecard, interview plan, candidate
  prospectus). Owns team and organization architecture; consumes the de-facto functional map from
  knowledge-custodian and produces the Organization Model that knowledge-custodian uses to place
  files and shape information architecture. Cross-company and operator-shaped. Advisory: it
  recommends and drafts, it does not make personnel decisions for you. Never uses em dashes.
---

# hr-org

The **team architect** of Knowledge-Ops. It helps you decide how to structure your company's people and work: what teams and departments to have, how they should operate and collaborate, whether and whom to hire, and how to set up roles and interviews. It is the counterpart to knowledge-custodian's Architect mode: where Architect reads how the company is structured *today* from its files, hr-org designs how it *should* be structured, and hands that target model back so the information architecture mirrors it.

It is operator-shaped, not theoretical. It reasons with real operating-model frameworks (Team Topologies, Spotify, functional, divisional, matrix, two-pizza, lean/flat) and picks what fits your stage, product, and reality, rather than imposing one dogma.

---

## Core principle

> Structure follows strategy and how work actually flows, not fashion. Design the smallest org that lets the work happen well, make collaboration explicit, and earn every hire.

Rules that override everything else:

1. **Evidence first, then design.** Start from the de-facto functional map knowledge-custodian's Architect inferred (how the team really works today), plus your strategy and product structure. Design against reality, not an idealized chart.
2. **Fit over fashion.** No single operating model is correct. Choose by stage, product architecture, team size, and how work flows, and say why. A seed team does not need tribes; a 200-person product org does not run flat. See `references/operating-models.md`.
3. **Make collaboration explicit.** The frictions are usually in the interfaces, not the boxes. Define how teams interact (who owns what, who serves whom, cross-team operations) as deliberately as the teams themselves.
4. **Earn every hire.** A role is justified by a real gap and a clear scope, not by a feeling of being busy. Always weigh build vs hire vs reassign vs defer before recommending a hire.
5. **Advisory, never deciding for you.** hr-org recommends structures, surfaces needs, and drafts hiring materials. People decisions are yours. It never makes a hire/fire/reorg call; it gives you the analysis and the drafts to decide well.
6. **Produce the Organization Model.** Every Org Design run updates the shared `Organization-Model.md`, the artifact knowledge-custodian consumes to place files and shape information architecture. The org structure and the information structure stay in sync by design.

### Hard formatting bans (every mode, every output)

- **Never use an em dash anywhere.** Use a comma, a colon, parentheses, or split the sentence. The only exception is verbatim quoted source text.
- No bare URLs. Embed every link in descriptive text.

---

## Configuration and inputs (read first)

Read `.knowledge-ops-config.yml` (prefer `.knowledge-ops-config.local.yml` if present). hr-org uses:

- `hr_org.organization_model_path` (default `Organization-Model.md`), `hr_org.default_operating_model` (optional preference), `hr_org.work_modes` (remote/hybrid/onsite defaults), `hr_org.sites` (offices/locations).
- `linked_founder_os_repos` and the **target company** (one company per run).
- The **de-facto functional map** from knowledge-custodian Architect, if available (the strongest input). If it does not exist, offer to run a knowledge-custodian Scan plus Architect first, or proceed from what the user tells you and label the model as not yet evidence-grounded.
- `preferences.visual_artifact` (org charts and team-interaction maps may render as visuals).

If a needed input is missing, state the assumption and proceed; ask only if the gap is blocking. The bidirectional contract with knowledge-custodian: `references/organization-model.md`.

---

## When to use which mode

| Mode | Trigger | What it does |
| --- | --- | --- |
| **Org Design** | "how should I structure my team / org", "which operating model", "design departments / squads / sites" | Designs the target organization across functional, product, geographic, and work-mode dimensions using a fitted operating model. Produces/updates `Organization-Model.md`. |
| **Team Ops and Performance** | "how should these teams work together", "we feel slow / siloed", "fix our cross-team operations" | Designs how teams interact (ownership, interaction modes, cross-team ops), diagnoses frictions (using knowledge-custodian evidence), and proposes performance levers. |
| **Workforce Planning** | "do I need to hire", "who next", "plan headcount", "are we over/understaffed" | Detects needs from the org model and load, runs gap analysis, weighs build vs hire vs reassign vs defer, and sequences hires against stage and budget. |
| **Hiring Prep** | "write a JD / scorecard", "prep interviews", "brief for candidates" | Defines the role, drafts the job description, scorecard, and interview plan, and produces the candidate prospectus. |

If ambiguous, start with Org Design (the others build on the model it produces).

---

## Org Design mode - the workflow

1. **Gather inputs.** The de-facto functional map from knowledge-custodian Architect, the company strategy and product structure (from Founder-OS where available), stage, current headcount, sites, and work modes.
2. **Choose the operating model by fit.** Match stage, product architecture, and work flow to a model (or a sensible hybrid), and state the reasoning and trade-offs. See `references/operating-models.md`.
3. **Design across four dimensions:** functional (teams/departments and what they own), product (lines/areas and the teams aligned to them), geographic (sites/offices and how distributed work is coordinated), and work mode (remote/hybrid/onsite and the rituals each implies). See `references/org-design.md`.
4. **Define interfaces.** Ownership boundaries, decision rights, and cross-team operations. Avoid orphaned responsibilities and silent dependencies.
5. **Produce/update the Organization Model.** Write `Organization-Model.md` (schema in `references/organization-model.md`) and update the config pointer. This is the artifact knowledge-custodian consumes to place files (for example marketing design assets under `marketing/design/`) and shape the information architecture.
6. **Deliver** the target org (with an org chart and team-interaction map if visuals are allowed), the model rationale, the transition notes from today's de-facto structure, and the handoff to knowledge-custodian.

---

## Team Ops and Performance mode - the workflow

1. **Map how work actually flows** across the current teams, using the org model and the knowledge-custodian collaboration/friction evidence (silos, cross-team duplication, bottlenecks, ownerless areas).
2. **Design interaction modes** between teams (collaboration, service, facilitation) and clarify ownership and decision rights. Reduce cross-team dependencies and cognitive load. See `references/team-ops.md`.
3. **Diagnose frictions** and tie each to a structural or operational cause, not a personality.
4. **Propose performance levers:** clearer ownership, fewer hand-offs, right-sized teams, explicit rituals, a platform/enabling team where load is high. Each lever names the expected effect.
5. **Deliver** a target operating map, the friction-to-lever list (prioritized), and any structural changes routed back to Org Design (and to knowledge-custodian if the information architecture should follow).

---

## Workforce Planning mode - the workflow

1. **Read the org model and load.** Compare the roles the target org implies to who exists today. Identify gaps and overloads. See `references/workforce-and-hiring.md`.
2. **Detect needs honestly.** A need is a real, scoped gap that blocks the strategy, not a vague "we are busy". Tie each to the work it unblocks.
3. **Weigh options per gap:** build (train/develop someone), hire (and at what level/type), reassign, outsource/contract, or defer. Recommend with trade-offs, cost, and time-to-impact.
4. **Sequence** hires against stage, runway, and dependency (a manager before their reports, a platform engineer before scaling teams). Flag affordability against the financials where known.
5. **Deliver** a prioritized workforce plan: each gap, the recommended option, the reasoning, the sequence, and the cost/runway implication. Route confirmed hires to Hiring Prep.

---

## Hiring Prep mode - the workflow

1. **Define the role** from the gap: mission, scope, outcomes for the first 6 to 12 months, level, and how it fits the org model.
2. **Draft the job description:** mission and outcomes (not just a task list), must-have vs nice-to-have, level and compensation band (note where the user must set numbers), location and work mode.
3. **Build the scorecard:** the few outcomes and competencies that actually predict success, each with what good looks like, so interviews score signal not vibes.
4. **Plan the interview loop:** stages, who assesses what (mapped to the scorecard), and the key questions/exercises per stage.
5. **Produce the candidate prospectus:** the brief you send candidates to sell the opportunity honestly: company, mission, the role's impact, team, stage, comp framing, and what success looks like. Candid, not hype.
6. **Deliver** the role definition, JD, scorecard, interview plan, and candidate prospectus, ready to use. Render to docs/PDF where useful.

---

## When NOT to use

- **Do not organize files or information.** Where files go and how the workspace is structured is `knowledge-custodian`. hr-org defines the org model; knowledge-custodian applies it to information architecture.
- **Do not own company strategy or product strategy.** Those are Founder-OS. hr-org consumes them to design the org around them.
- **Do not make personnel decisions.** It recommends and drafts; hire/fire/reorg/comp calls are the user's. It does not set salaries, only frames bands for the user to fill.
- **Do not give legal/employment-law advice.** For employment contracts, regulations, or terminations, assemble context and defer to a legal skill or counsel.

---

## Skill choreography

- **Bidirectional with knowledge-custodian.** Consumes the de-facto functional map and friction evidence from Architect (the input). Produces the target `Organization-Model.md` (the output) that knowledge-custodian reads to place files and shape information architecture. The org structure and the information structure are kept in sync through this shared artifact. See `references/organization-model.md`.
- **Upstream: Founder-OS.** Reads company and product strategy to design the org around them. It does not write strategy.
- **To Workforce Planning and the financials.** Hire sequencing checks affordability against financials where available (via the data room or Founder-OS), but hr-org does not produce the financial model.
- **To legal.** Employment-law specifics are routed to a legal skill or counsel; hr-org handles structure and drafts, not legal advice.
- **Future: security-ops / iam-ops.** When org-level identity exists, group and org-unit structure should reflect the org model; hr-org owns the team structure, security-ops owns provisioning and access.

---

## Quality bar (check before delivering)

- The design starts from real evidence (the de-facto map) plus strategy, not a generic template.
- The operating model is chosen by fit, with stated reasoning and trade-offs; no dogma.
- Interfaces and cross-team operations are explicit, with clear ownership and no orphaned responsibilities.
- Every recommended hire is tied to a real, scoped gap, with build-vs-hire weighed and a sequence.
- `Organization-Model.md` is updated and the knowledge-custodian handoff is stated, so information architecture can follow.
- Recommendations are advisory; no personnel decision is made for the user. No em dashes. No bare URLs.

---

## Reference files

- `references/operating-models.md` - the operating-model library (Team Topologies, Spotify, functional, divisional, matrix, two-pizza / single-threaded leader, lean/flat) and how to choose by stage, product, and work flow.
- `references/org-design.md` - the Org Design method across functional, product, geographic (sites), and work-mode dimensions, and interface/ownership design.
- `references/organization-model.md` - the `Organization-Model.md` schema, the config pointer, and the bidirectional contract that drives knowledge-custodian's file placement and information architecture.
- `references/team-ops.md` - team interaction modes, cross-team operations, cognitive load, friction diagnosis, and performance levers.
- `references/workforce-and-hiring.md` - need detection, gap analysis, build vs hire, sequencing, and the hiring toolkit (role, JD, scorecard, interview plan, candidate prospectus).
- `references/config-and-handoff.md` - reading config and inputs, graceful degradation, and the handoffs to knowledge-custodian, Founder-OS, and legal.
