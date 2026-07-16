# Operating-model library

No model is correct in the abstract. Each fits a stage, a product architecture, a team size, and a way of working. Choose by fit, cite the principle behind the choice, state the trade-off, and prefer the smallest structure that lets the work happen well. Hybrids are normal and often right.

## Structural foundations (cite these when justifying a choice)

These are the research-backed principles a design should rest on. Name the relevant one when recommending a structure, so the recommendation is justified, not asserted.

- **Dunbar's number.** Humans sustain roughly 150 stable relationships. Above it, a single group loses cohesion and needs sub-structure. Drives the upper bound on a department or site before it must split.
- **Two-pizza teams (Amazon).** A team small enough to be fed by two pizzas (about 6 to 10 people) keeps ownership and communication tight. Drives squad/team size.
- **Span of control.** A manager can effectively lead roughly 5 to 9 direct reports, and beyond about 15 to 20 a layer must be added or the unit split. The single most useful trigger for "when to add a layer".
- **Conway's law.** Organizations ship systems that mirror their communication structure. Design team boundaries to match the architecture you want, not the one you inherited; if the architecture must change, the team boundaries usually change first.
- **Tuckman's stages (forming, storming, norming, performing).** Teams take time to reach performance. This is the case for **stable, long-lived teams** over project-based resourcing that disbands and reforms, resetting the clock every time.
- **Cognitive load (Team Topologies).** A team performs when it owns only as much as it can hold well. Overloaded teams slow down and drop quality before their people are "the problem".

## Why each layer exists

Add a layer only to solve a named problem. The logic, per layer:

- **Team / squad.** Problem: work needs an owner small enough to move fast and be accountable. Principle: two-pizza, Tuckman (keep it stable). The default unit; most teams should be stream-aligned (own a slice of value end to end).
- **Business unit / group (a cluster of teams).** Problem: several teams share a domain and create cross-team dependencies no single team can resolve. Principle: span of control, dependency locality. Gate: do **not** create a business unit for a single team; a one-team BU is a bureaucracy layer with no job. Add it only when there are enough teams that coordination needs an owner.
- **Department / function.** Problem: a domain grows past Dunbar and needs craft standards and a senior owner. Principle: Dunbar, span of control. Add when headcount and breadth exceed what one BU lead can hold.
- **Legal entity (above departments).** Problem: distinct legal, tax, or governance boundaries (subsidiaries, a foundation, multiple corporations) with shared corporate resources. Add only when the legal reality demands it; keep shared services explicit. Relevant for multi-entity holdings.

## The models

### Lean / flat (early stage)
Few people, no formal teams, everyone close to the founder. Fast and cheap to coordinate; breaks around 10 to 20 people as communication paths explode. Right for pre-seed and seed. Failure mode: keeping it past the point where nobody owns anything because everybody owns everything.

### Functional (the "Apple" archetype)
Organized by discipline (engineering, design, product, sales, marketing, finance). Deep expertise, clear craft ownership, strong standards. Cross-functional delivery needs deliberate interfaces. Works when the product is unified and craft excellence matters more than autonomous speed per line. Apple runs functionally at very large scale.

### Divisional / product-line
Organized by product, business unit, or segment, each with its own cross-functional resources. High autonomy and accountability per line. Cost: duplication across divisions and weaker shared standards (often an acceptable trade for speed). Right when product lines are genuinely distinct and need to move independently.

### Matrix
Two axes at once (for example function and product): a person belongs to a craft and to a product team. Balances expertise with product focus, but creates dual reporting and decision ambiguity unless accountability is explicit. Use only when both axes truly need strong representation, and make decision rights unmistakable (see the RACI matrix in `org-design.md`).

### Spotify model (squads, tribes, chapters, guilds)
Autonomous cross-functional squads grouped into tribes; chapters align a craft across squads; guilds are interest communities. Designed for product-led autonomy at scale. Caveat: even Spotify noted it was aspirational and often mis-copied. Adopt the intent (autonomy plus craft alignment via chapters/guilds), not the labels, and only when you have enough people for squads to be real.

### Amazon two-pizza / single-threaded leader (STL)
Small teams each owned by a single leader fully accountable for one initiative. Maximizes ownership, autonomy, and speed; minimizes dependencies. Requires real platform investment so small teams are not blocked. Excellent for ownership and velocity once you can staff dedicated owners.

### Team Topologies (the modern default for product/eng)
Four team types and three interaction modes, organized around fast flow and cognitive load:

- **Stream-aligned:** owns a slice of value end to end. The default; most teams should be this.
- **Platform:** internal services that reduce the cognitive load of stream-aligned teams.
- **Enabling:** helps other teams adopt a capability, then steps away.
- **Complicated-subsystem:** owns a part needing deep specialist knowledge.
- **Interaction modes:** collaboration (close, temporary), X-as-a-service (clean consume/provide), facilitating (help then leave).

Pairs naturally with two-pizza and stream-aligned product lines, and is the most actionable frame for team boundaries and interfaces.

### Context not control (the "Netflix" archetype)
Lead with context, not control: give teams the information, strategy, and guardrails to decide well, and push decisions to the people closest to the work. High autonomy, low process. Requires unusually high talent density and clarity of strategy, so it fits a senior team more than a junior one. Adopt the principle (context over approval gates) even in other models; adopt the full high-autonomy version only when talent density genuinely supports it.

### Foundation governance
A foundation or non-profit entity holds a mission, standard, or protocol, with an operating company alongside it. Common where neutrality or public-good governance matters (open source, protocols, crypto). It is a governance layer above the org, not a team model: pair it with one of the team models below for how work actually gets done. Ties to the legal-entity layer and to the crypto sector overlay.

## What to adopt, what to leave

Borrow the mechanism that fits your context; leave the parts that assume a scale or culture you do not have.

| Model | Adopt | Leave |
| --- | --- | --- |
| Functional (Apple) | Deep craft ownership, single functional accountability | Full functional org if you are small or multi-product (cross-functional delivery stalls) |
| Divisional | Autonomy and accountability per line | Duplication and weak shared standards when lines are not truly distinct |
| Matrix (Google) | Dual strength on function and product | Dual reporting without one clear Accountable per decision |
| Spotify | Autonomy plus craft alignment (chapters/guilds) | The labels and the org-chart cargo-culting; it was aspirational |
| Two-pizza (Amazon) | Small single-owner teams, working backwards | Small teams without the platform investment that unblocks them |
| Context not control (Netflix) | Context over approval gates, decisions at the edge | Low-process autonomy without high talent density |
| Team Topologies | Team types, interaction modes, cognitive-load limits | Nothing major; it is the default frame |

## Choosing by fit

- **Stage / size.** Under ~15: lean/flat. 15 to ~50: functional or a few stream-aligned teams. 50+: introduce product/divisional lines, platform and enabling teams; consider tribes/BUs only when teams are numerous enough to need coordination owners.
- **Product architecture.** Unified product favors functional; distinct lines favor divisional/stream-aligned; a shared technical core favors a platform team (Conway).
- **Work flow.** Cross-functional work slowed by hand-offs favors autonomous cross-functional teams; craft excellence and standards favor functional strength (or chapters).
- **Distribution and work mode.** Remote/distributed raises coordination cost, favoring clearer ownership, fewer cross-team dependencies, and explicit asynchronous interfaces.

Recommend a model (or hybrid) with: the principle it rests on, why it fits this stage/product/flow, the trade-off accepted, and the first structural move. Revisit as the company grows; the right model at 20 is rarely the right model at 80.
