# Anti-patterns

What not to do, each with the counter-solution. A design that avoids these is usually better than one that chases an ideal chart. Check a proposed org against this list before delivering.

## Structural anti-patterns

- **Project-based resourcing.** Spinning teams up and down per project. Why it fails: every reform resets Tuckman's clock, so teams never reach performance, and ownership evaporates between projects. Counter: stable, long-lived teams that own a domain or value stream; bring work to the team, not people to the project.

- **Functional silos.** Functions that optimize locally and hand off over walls. Why it fails: cross-functional delivery stalls at every boundary. Counter: stream-aligned teams that own outcomes end to end, or, if you keep a functional org, explicit cross-functional workflows with owners and lead-times (see `team-ops.md`).

- **Too many reporting lines.** A person reporting to three or more people, or a matrix with unclear accountability. Why it fails: no one is truly accountable, decisions stall. Counter: at most a dual line (vertical delivery plus horizontal craft), with a RACI that names exactly one Accountable per decision.

- **Fractional resource pooling.** "I need a designer at 20 percent next quarter." Why it fails: fractional allocation creates scheduling hell, context-switching cost, and no ownership. Counter: allocate service disciplines full-time or not at all; if demand is genuinely partial, use an as-a-service interface with a queue, not a fractional assignment.

- **Front-loading layers.** Creating departments and business units before the headcount needs them. Why it fails: bureaucracy with no job, slow decisions, made-up management roles. Counter: start flat, add a layer only when span of control (>15 to 20 reports) or cognitive load forces it. A one-team business unit is the classic tell.

- **Org by customer segment (prematurely).** Splitting teams by customer type before the product or go-to-market truly diverges. Why it fails: duplicates product work and fragments the roadmap. Counter: segment in go-to-market and sales, keep product/engineering aligned to the product until lines genuinely diverge.

- **Owner-less cross-team operations.** Releases, incidents, planning, and hand-offs that no one owns. Why it fails: the work that spans teams is exactly where things drop. Counter: give every cross-team operation an owner and a cadence in the Organization Model.

## When a functional org is actually the right call

Divisional/autonomous-team models are fashionable, but the functional org is correct when:

- The company is early or small (under about 50 people, or only a handful of engineers): there are not enough people to staff autonomous cross-functional teams without spreading craft too thin.
- The product is a single, unified product with a largely shared technical stack (high reuse): divisional duplication would cost more than it buys.
- Craft excellence and consistency matter more than per-line speed (the Apple case).

When you do recommend divisional/autonomous teams over functional, say why the duplication is acceptable (speed and ownership outweigh the redundancy), so the trade-off is explicit rather than hidden.

## How to use this list

In Org Design and Team Ops, check the proposed structure against each anti-pattern, and for any that applies, either remove it or state explicitly why this case is the justified exception. Never ship a design that trips an anti-pattern silently.
