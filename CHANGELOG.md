# Changelog

All notable changes to Knowledge-Ops are documented here. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.3.0] - 2026-06-02

### Changed
- Renamed the team-architecture skill **hr-org** to **functional-hr-ops** (directory, skill name, `.skill` package, config key `functional_hr_ops`, manifests, and all cross-references in knowledge-custodian).
- diligence-ops now **consumes the dataroom-ops Audit** as the single gap source of truth (against the relevant stage) instead of recomputing gaps, layering only audience and sensitivity on top. Keeps the library and the delivery counter from diverging on completeness.

### Added (visual outputs and example)
- functional-hr-ops **visual outputs** (`references/visual-outputs.md`): render the Organization Model as an org chart, team-interaction map, cross-team flows, mind map, and RACI, and assemble an onboarding/training pack in HTML (default), PDF, or PPT, generated from the model so picture and model never drift.
- A worked **example** under `examples/helvetia-robotics-sim/`: a simulated Swiss seed company with a deterministic generator (`build_sim.py`), artifacts for all four skills, an HTML onboarding pack, and a `VERIFICATION.md` (13/13 automated checks: action-plan reversibility, hash dedup, org-model schema, single-Accountable RACI, bidirectional placement consistency, canonical folders, restricted hard-block, no em dashes).

### Added
- functional-hr-ops **Org Rollout** mode (fifth mode): a phased implementation roadmap (pilot, scale, optimize) with entry criteria, checklists, owners, a communication and risk plan, and a success-metrics catalog with baselines and targets (team health, velocity, cycle time, blocking cross-team dependencies, deployment frequency, discipline-community participation).
- functional-hr-ops **anti-patterns** reference: a catalog of what not to do (project-based resourcing, functional silos, too many reporting lines, fractional resource pooling, front-loading layers, premature org-by-segment, owner-less cross-team operations), each with the counter-solution, plus the conditions under which a functional org is the right call.
- functional-hr-ops **cited structural foundations** in operating-models (Dunbar, two-pizza, span of control, Conway, Tuckman, cognitive load) and a "why each layer exists" rationale, so each design choice is justified, not asserted.
- functional-hr-ops **richer Organization Model**: roles defined by accountability, decision rights, and an explicit "not responsible for"; dual reporting (vertical delivery line and horizontal craft/discipline line); discipline types (embedded/service/specialized) with allocation rule and lead scope; unit size bands and a company scale tier; per-unit rituals; layer decision gates (no business unit for a single team; split at span of control); a RACI decision matrix with exactly one Accountable per decision; and an optional legal-entity layer for multi-entity holdings.
- functional-hr-ops cross-team operations specified as **workflows** (intake, lead-times, dependency-resolution steps, escalation ladder), not just structure.
- knowledge-custodian now consumes `functional_hr_ops.organization_model_path`, with the Organization Model taking precedence over the inferred map for file placement.

### Added (introduced in development as 0.2.0, shipped here)
- **hr-org** skill (the team architect): `SKILL.md` with four modes (Org Design, Team Ops and Performance, Workforce Planning, Hiring Prep) and references for the operating-model library (Team Topologies, Spotify, functional, divisional, matrix, two-pizza / single-threaded leader, lean/flat), org design across functional/product/geographic/work-mode dimensions, the `Organization-Model.md` shared artifact and bidirectional contract, team ops (interaction modes, cognitive load, frictions, levers), workforce planning and the hiring toolkit (role, JD, scorecard, interview plan, candidate prospectus), and config/handoff. Advisory: recommends and drafts, never makes personnel decisions or sets pay. Packaged as `hr-org.skill`.
- **Architect mode** in knowledge-custodian: reads the information topology and organizational signals (file/drive types, product/team areas, collaboration and access graph, hotspots, ownership concentration), infers the implicit functional and team structure, recommends the target information architecture, and flags operations/performance frictions (silos, cross-team duplication, ownerless areas, single-person bottlenecks).
- Bidirectional `knowledge-custodian <-> hr-org` contract via `Organization-Model.md`: Architect infers the de-facto org and hands it to hr-org; hr-org designs the target model and hands it back; knowledge-custodian reads it (`hr_org.organization_model_path`) to place files and shape information architecture, the model taking precedence over the inferred map.
- knowledge-custodian refinements: incremental scan cache (`_snapshots/scan-index.json`); a concrete JSON action-plan schema with example for v1.1 Execute; an Advise decisions register; optional file-organization templates (PARA, Johnny.Decimal, function-first); and a governance/IAM seam in Architect (read-only Workspace groups/OU/policy signals when a connector exists, routed to hr-org / compliance-ops / a future security-ops).
- `.knowledge-ops-config.yml`: added the `hr_org` section (organization model path, default operating model, work modes, sites).
- Plugin and marketplace manifests updated to bundle all four skills.
- Roadmap: added security-ops / iam-ops (identity and access governance); hr-org graduated from roadmap to built.

### Changed
- knowledge-custodian Architect, Standardize, and Onboarding now consume `Organization-Model.md` when present, mirroring the target org in the information architecture.

## [0.1.0] - 2026-06-01

### Added
- Repository scaffolding: README, LICENSE (MIT), `.gitignore`, CHANGELOG, CONTRIBUTING, SETUP.
- `.knowledge-ops-config.yml` template: the single source of truth every skill reads first (platforms, linked Founder-OS repos, dataroom canonical structure, diligence stage profiles and sensitivity tiers, knowledge-custodian sandbox safety).
- Plugin packaging: `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json` bundling the skills as one plugin.
- **dataroom-ops** skill (the library): `SKILL.md` with three modes (Bootstrap, Sync, Audit) and references for the canonical structure, sync protocol, audit protocol, and config/handoff. Packaged as `dataroom-ops.skill`.
- **diligence-ops** skill (the delivery counter): `SKILL.md` with four modes (Fundraise Data Room Prep, Due Diligence Support, Board and Investor Reporting, Audit Prep) and references for built-in Swiss stage checklists, packaging and access control, Q&A and evidence, reporting, and config/handoff. Packaged as `diligence-ops.skill`.
- **knowledge-custodian** skill (the substrate): `SKILL.md` with v1.0 modes (Scan, Advise, Standardize, Onboarding; Execute deferred to v1.1) across local filesystem, Google Drive, Google Workspace, and Notion, with the safety model, scan/providers and hybrid dedup, advise protocol, the file-organization standard and onboarding, and config/handoff. Advice-only and never-delete. Packaged as `knowledge-custodian.skill`.

### Design decisions
- Decomposition by job/trigger/audience: dataroom-ops (library, internal), diligence-ops (delivery counter, external), knowledge-custodian (substrate, internal).
- Knowledge-Ops consumes Founder-OS outputs and never duplicates its strategy or metrics work.
- Diligence calibrated on Swiss venture standards (SICTIC seed, Startup Board Academy governance) and M&A-grade acquisition lists (Elysium Lab).
- knowledge-custodian v1.0 is advice-only; Execute mode (safe batch moves) deferred to v1.1 under mandatory safeguards (never delete, archive + snapshot + undo log + confirmation).

[0.3.0]: https://github.com/Mr-Hodler/Knowledge-Ops/releases/tag/v0.3.0
[0.2.0]: https://github.com/Mr-Hodler/Knowledge-Ops/releases/tag/v0.2.0
[0.1.0]: https://github.com/Mr-Hodler/Knowledge-Ops/releases/tag/v0.1.0
