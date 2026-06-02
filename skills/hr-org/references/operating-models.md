# Operating-model library

No model is correct in the abstract. Each fits a stage, a product architecture, a team size, and a way of working. Choose by fit, state the trade-offs, and prefer the smallest structure that lets the work happen well. Hybrids are normal and often right.

## The models

### Lean / flat (early stage)
Few people, no formal teams, everyone close to the founder. Fast and cheap to coordinate, but it breaks around 10 to 20 people as communication paths explode. Right for pre-seed and seed. The failure mode is keeping it too long: when nobody owns anything because everybody owns everything, it is time to add structure.

### Functional (the "Apple" archetype)
Organized by discipline (engineering, design, product, sales, marketing, finance). Deep expertise, clear craft ownership, strong standards. Coordination across functions is the cost: shipping anything cross-functional needs deliberate interfaces. Works well when the product is unified and excellence within a craft matters more than autonomous speed per product line. Apple famously runs functionally at very large scale.

### Divisional / product-line
Organized by product, business unit, or customer segment, each with its own cross-functional resources. High autonomy and accountability per line, fast within a division. The cost is duplication across divisions and weaker shared standards. Right when product lines are genuinely distinct and need to move independently.

### Matrix
Two axes at once (for example function and product): a person belongs to a craft and to a product team. Balances expertise with product focus, but creates dual reporting and decision ambiguity if accountability is not explicit. Use only when both axes truly need strong representation, and make decision rights unmistakable.

### Spotify model (squads, tribes, chapters, guilds)
Autonomous cross-functional squads grouped into tribes; chapters align a craft across squads; guilds are interest communities. Designed for product-led autonomy at scale. Caveat: even Spotify has noted it was aspirational and often mis-copied. Adopt the intent (autonomy plus craft alignment), not the labels, and only when you have enough people for squads to be real.

### Amazon two-pizza / single-threaded leader (STL)
Small teams (feedable by two pizzas) each owned by a single leader fully accountable for one initiative. Maximizes ownership, autonomy, and speed; minimizes dependencies. Requires real platform investment so small teams are not blocked. Excellent for ownership and velocity once you can staff dedicated owners.

### Team Topologies (the modern default for product/eng)
Four team types and three interaction modes, organized around fast flow and cognitive load:

- **Stream-aligned team:** owns a slice of value end to end (a product, a journey). The default team type; most teams should be this.
- **Platform team:** provides internal services that reduce the cognitive load of stream-aligned teams.
- **Enabling team:** helps other teams adopt capabilities, then steps away.
- **Complicated-subsystem team:** owns a part that needs deep specialist knowledge.
- **Interaction modes:** collaboration (work closely, temporary), X-as-a-service (one consumes what another provides), facilitating (one helps another). 

The core lever is **cognitive load**: a team should own only as much as it can hold well. Team Topologies pairs naturally with two-pizza and with stream-aligned product lines, and is the most actionable frame for designing team boundaries and interfaces.

## Choosing by fit

- **Stage / size.** Under ~15: lean/flat. 15 to ~50: functional or stream-aligned teams. 50+: introduce product/divisional lines, platform and enabling teams; consider tribes only when squads are real. 
- **Product architecture.** A unified product favors functional; distinct product lines favor divisional/stream-aligned; a shared technical core favors a platform team.
- **Work flow.** If most work is cross-functional and slowed by hand-offs, move toward autonomous cross-functional teams (stream-aligned / two-pizza). If craft excellence and standards dominate, keep functional strength (or chapters).
- **Distribution and work mode.** Remote/distributed raises coordination cost, which favors clearer ownership and fewer cross-team dependencies, and explicit asynchronous interfaces.
- **Conway's law.** Teams ship software shaped like the org. Design team boundaries to match the architecture you want, not the one you inherited.

Recommend a model (or hybrid) with: why it fits this stage/product/flow, the main trade-off accepted, and the first structural move. Revisit as the company grows; the right model at 20 is rarely the right model at 80.
