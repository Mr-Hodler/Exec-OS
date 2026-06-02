# Team ops and performance

This mode designs how teams work and interact, diagnoses why work is slow or siloed, and proposes structural levers. It reasons about interfaces and cognitive load, not personalities.

## Interaction modes (from Team Topologies)

Every pair of teams that must work together uses one of three modes. Name the mode explicitly; ambiguity here is where time is lost.

- **Collaboration:** two teams work closely for a defined period to figure something out. High bandwidth, high cost; keep it temporary. Permanent collaboration signals a wrong boundary or a needed merge.
- **X-as-a-service:** one team consumes what another provides through a clean interface. Low coupling; the default for stable relationships.
- **Facilitating:** one team (often enabling) helps another build a capability, then steps away.

Record each important boundary and its mode in the Organization Model. Prefer as-a-service for stable interfaces; reserve collaboration for genuine discovery.

## Cognitive load (the core lever)

A team performs when it owns only as much as it can hold well. To reduce load: narrow a team's domain to a coherent slice; move shared, undifferentiated work to a platform team; use an enabling team to inject a capability rather than permanently expanding scope. When a team is a bottleneck, ask whether its cognitive load is too high before asking whether its people are the problem.

## Cross-team operations as workflows

The recurring operations that span teams are where companies actually run. Define each not just as "who owns it" but as a workflow:

- **Owner and cadence.** Exactly one owner; a fixed rhythm.
- **Intake.** How a request enters (a form, a channel, a queue), and what it must contain.
- **Lead-times.** How much notice the operation needs, sized to its weight. State concrete windows (for example a major launch needs weeks of notice, a small content request needs days), so requesters plan instead of firefighting.
- **Steps.** The path from request to delivery, with acceptance criteria.
- **Escalation path.** The ladder when it stalls (for example team owner, then business-unit owner, then department head, then leadership).

Common cross-team operations to specify: release, incident response, planning, go-to-market hand-off, design intake, hiring. An owner-less cross-team operation is a top friction source (see `anti-patterns.md`).

Service-discipline intake deserves special care: route demand through an as-a-service queue with lead-times, never through fractional per-quarter allocation.

## Friction diagnosis

Use knowledge-custodian's friction evidence (silos, cross-team duplication, ownerless areas, single-person bottlenecks, access mismatches) plus the org model. For each friction, name the structural or operational cause:

- **Silo:** no shared interface or space; fix with an interaction mode and a shared area.
- **Duplication across teams:** unclear ownership; fix with a single owner and an as-a-service interface.
- **Bottleneck team or person:** cognitive overload or key-person concentration; fix with platform support, scope narrowing, or a hire (route to Workforce Planning).
- **Slow hand-offs:** too many collaboration interfaces that should be as-a-service.
- **Structure-vs-reality drift:** the org no longer matches how work flows; route to Org Design.

Never attribute a structural friction to an individual's performance. The skill diagnoses systems.

## Performance levers

Propose levers, each with the expected effect: clearer single ownership, fewer hand-offs, right-sized teams, an explicit interaction mode, a platform or enabling team where load is high, an owned cadence and intake for a cross-team operation. Prioritize by impact and effort. Structural changes route back to Org Design and, where information should follow, to knowledge-custodian.
