# Organization Model - Helvetia Robotics AG

version: 1    last_updated: 2026-06-02    stage: seed
scale_tier: small
operating_model: lean with stream-aligned teams (principle: two-pizza, Tuckman stable teams; rationale: 12 people, one product, speed over craft depth; trade-off: thin craft standards, revisit at ~30)

## Legal entities
- Helvetia Robotics AG: single entity; shared corporate resources (finance, legal) central.

## Functional structure (units)
- Product & Design (team): mission own the product and its UX; owned_outcomes roadmap, design system; size_band {min: 2, max: 5}; current_headcount 2; owner_role Head of Product; rituals [weekly product sync, quarterly planning].
- Engineering (team): mission build and ship RoboPick; owned_outcomes delivery, quality; size_band {min: 4, max: 8}; current_headcount 5; owner_role Eng Lead; rituals [daily standup, weekly release].
- Go-to-Market (team): mission pipeline and revenue; size_band {min: 2, max: 6}; current_headcount 2; owner_role Commercial Lead; rituals [weekly pipeline review].
- Operations & Finance (team): mission runway, bookkeeping, people ops; size_band {min: 1, max: 3}; current_headcount 2; owner_role COO; rituals [monthly close].

## Product structure
- RoboPick (single product line): aligned team Engineering + Product & Design; platform_dependencies none yet.

## Geographic / sites
- Zurich: product, eng, ops. Central decisions.
- Remote-EU: 2 engineers; async-first; anchor day Tuesday.

## Work modes
- Engineering: hybrid, anchor day Tuesday.
- Operations & Finance: onsite Zurich.

## Roles
- Head of Product:
    accountability: product outcomes
    decision_rights: [roadmap priorities, release scope]
    not_responsible_for: [technical architecture, salaries, hiring budget]
    reporting: { vertical_line: CEO }
- Eng Lead:
    accountability: delivery and quality
    decision_rights: [technical architecture, release readiness]
    not_responsible_for: [product priorities, pricing]
    reporting: { vertical_line: CEO }
    discipline_type: embedded
    lead_scope: company

## RACI decision matrix
- Set product priorities: { Accountable: Head of Product, Responsible: [Product & Design], Consulted: [Eng Lead], Informed: [GTM] }
- Release to production: { Accountable: Eng Lead, Responsible: [Engineering], Consulted: [Head of Product], Informed: [GTM] }
- Approve a hire: { Accountable: CEO, Responsible: [hiring manager], Consulted: [COO], Informed: [team] }
- Set a salary: { Accountable: CEO, Responsible: [COO], Consulted: [hiring manager], Informed: [] }

## Interfaces and cross-team operations
- Eng <-> Product & Design: interaction_mode collaboration; cadence weekly.
- GTM <-> Product: interaction_mode as-a-service (roadmap intake); cadence monthly.
- Cross-team ops: release: owner Eng Lead, cadence weekly, lead_time 1 day, escalation_path Eng Lead -> CEO.

## Information-architecture mapping (for workspace-ops)
- Product & Design -> product/ and marketing/design/ (shared design assets under marketing/design/)
- Engineering -> engineering/
- Go-to-Market -> sales/ and marketing/
- Operations & Finance -> finance/ and people/
- Shared spaces: company/ for all-hands material
- Ownership: every active area maps to exactly one owning team
