# Changelog

All notable changes to Exec-OS are documented here. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.5.1] - 2026-07-15

### Fixed
- **Metrics reference standardized:** all references to the Founder-OS metrics skill now use its real name `metrics-dashboard` (was inconsistently `metrics-aggregation-view` in 4 places across investor-ops references).

### Changed (board boundary)
- **`investor-ops` Family 3 mode renamed `Board & Investor Reporting` -> `Board & Investor Delivery`.** The board pack and investor letter are now authored and assembled by Founder-OS `narrative-assets-ops`; `investor-ops` only delivers them (files in the data room, audience-gates, logs distribution, manages the recurring cadence). Removes the overlap with Founder-OS on board-pack assembly.

### Roadmap
- Added `finance-ops` (operational finance beyond fundraising: bookkeeping, invoicing, real burn/runway, budget vs actual), `sales-ops`, and `customer-success-ops` to the pipeline.

## [0.5.0] - 2026-07-15

### Renamed (repo and skill)
- **Repo/product renamed `Knowledge-Ops` to `Exec-OS`** (the operator/COO operations layer above companies, parallel to Founder-OS). Plugin name `knowledge-ops` to `exec-os`; config file `.knowledge-ops-config.yml` to `.exec-os-config.yml`; all references, manifests, README, and SETUP updated. Plugin version 0.4.0 to 0.5.0.
- **Skill `knowledge-custodian` renamed to `workspace-ops`** (clearer, and `-ops`-consistent with the other skills). Directory, skill name, `.skill` package, config key `knowledge_custodian` to `workspace_ops`, and all cross-references updated.
- Manual follow-up for the founder: rename the repo folder on disk and the GitHub repo to match (`Exec-OS`), and update the git remote. All in-repo identity is already `Exec-OS`.
- Note: `examples/helvetia-robotics-sim/` left untouched (historical snapshot; still uses old names), to be regenerated on next example refresh.

## [0.4.0] - 2026-07-15

### Changed (merge into investor-ops)
- **Merged `dataroom-ops` + `diligence-ops` into a single skill, `investor-ops`**, the investor & capital engine. One skill, three mode families: **Data Room** (Bootstrap, Sync, Audit), **Investor Sourcing & Outreach** (new), **Diligence & Delivery** (Fundraise Prep, DD Support, Board & Investor Reporting, Audit Prep). Rationale: for a single founder the library/delivery-counter split was over-granular, and investor outreach had no home. Fewer skills (4 to 3), one place for the whole raise-and-be-examined lifecycle. All reference files preserved.

### Added (investor sourcing & outreach, Family 2)
- New reference `investor-sourcing-and-outreach.md` and config block `outreach:` (sources, pipeline_stages, fit_weights, crm_location, update_cadence, daily_send_cap). Modes: **Investor List** (build the target list from directories, funding maps, warm network), **Fit & Scoring** (weighted rubric, tiered shortlist), **Outreach & Pipeline** (cold/warm outreach pulling materials from Founder-OS `narrative-assets-ops`, a CRM through the raise stages), **Prospect Updates** (nurture). Never fabricates investor data; never re-writes pitch materials (those stay in Founder-OS); legal docs stay in `corporate-legal`.

### Changed (cross-references)
- `workspace-ops` (SKILL + references), `.exec-os-config.yml`, `README.md`, `SETUP.md`, and both plugin manifests updated to reference `investor-ops`. Founder-OS `narrative-assets-ops` handoff updated from `dataroom-ops` (future) to `investor-ops` (built). Plugin version 0.3.0 to 0.4.0.
- Note: `examples/helvetia-robotics-sim/` artifacts still use the old skill names; left as a historical snapshot, to be regenerated on next example refresh.

## [0.3.0] - 2026-06-02

### Changed
- Renamed the team-architecture skill **hr-org** to **functional-hr-ops** (directory, skill name, `.skill` package, config key `functional_hr_ops`, manifests, and all cross-references in workspace-ops).
- diligence-ops now **consumes the dataroom-ops Audit** as the single gap source of truth (against the relevant stage) instead of recomputing gaps, layering only audience and sensitivity on top. Keeps the library and the delivery counter from diverging on completeness.

### Added (sector overlays)
- dataroom-ops **sector overlays** (`references/sector-overlays.md`): additive, combinable profiles over the SICTIC/venture-CH base, selected by a per-company `company_type` (saas, hardware, crypto, fintech, ai). Each adds sector subfolders into the base folders and sector DD items. Bootstrap applies them, Audit measures against stage plus overlay, and diligence-ops inherits the overlay DD items. Config gains `company_type` per linked repo and `dataroom.default_company_type`.

### Added (visual outputs and example)
- functional-hr-ops **visual outputs** (`references/visual-outputs.md`): render the Organization Model as an org chart, team-interaction map, cross-team flows, mind map, and RACI, and assemble an onboarding/training pack in HTML (default), PDF, or PPT, generated from the model so picture and model never drift.
- A worked **example** under `examples/helvetia-robotics-sim/`: a simulated Swiss seed company with a deterministic generator (`build_sim.py`), artifacts for all four skills, an HTML onboarding pack, and a `VERIFICATION.md` (13/13 automated checks: action-plan reversibility, hash dedup, org-model schema, single-Accountable RACI, bidirectional placement consistency, canonical folders, restricted hard-block, no em dashes).

### Added
- functional-hr-ops **Org Rollout** mode (fifth mode): a phased implementation roadmap (pilot, scale, optimize) with entry criteria, checklists, owners, a communication and risk plan, and a success-metrics catalog with baselines and targets (team health, velocity, cycle time, blocking cross-team dependencies, deployment frequency, discipline-community participation).
- functional-hr-ops **anti-patterns** reference: a catalog of what not to do (project-based resourcing, functional silos, too many reporting lines, fractional resource pooling, front-loading layers, premature org-by-segment, owner-less cross-team operations), each with the counter-solution, plus the conditions under which a functional org is the right call.
- functional-hr-ops **cited structural foundations** in operating-models (Dunbar, two-pizza, span of control, Conway, Tuckman, cognitive load) and a "why each layer exists" rationale, so each design choice is justified, not asserted.
- functional-hr-ops **richer Organization Model**: roles defined by accountability, decision rights, and an explicit "not responsible for"; dual reporting (vertical delivery line and horizontal craft/discipline line); discipline types (embedded/service/specialized) with allocation rule and lead scope; unit size bands and a company scale tier; per-unit rituals; layer decision gates (no business unit for a single team; split at span of control); a RACI decision matrix with exactly one Accountable per decision; and an optional legal-entity layer for multi-entity holdings.
- functional-hr-ops cross-team operations specified as **workflows** (intake, lead-times, dependency-resolution steps, escalation ladder), not just structure.
- workspace-ops now consumes `functional_hr_ops.organization_model_path`, with the Organization Model taking precedence over the inferred map for file placement.

### Added (introduced in development as 0.2.0, shipped here)
- **hr-org** skill (the team architect): `SKILL.md` with four modes (Org Design, Team Ops and Performance, Workforce Planning, Hiring Prep) and references for the operating-model library (Team Topologies, Spotify, functional, divisional, matrix, two-pizza / single-threaded leader, lean/flat), org design across functional/product/geographic/work-mode dimensions, the `Organization-Model.md` shared artifact and bidirectional contract, team ops (interaction modes, cognitive load, frictions, levers), workforce planning and the hiring toolkit (role, JD, scorecard, interview plan, candidate prospectus), and config/handoff. Advisory: recommends and drafts, never makes personnel decisions or sets pay. Packaged as `hr-org.skill`.
- **Architect mode** in workspace-ops: reads the information topology and organizational signals (file/drive types, product/team areas, collaboration and access graph, hotspots, ownership concentration), infers the implicit functional and team structure, recommends the target information architecture, and flags operations/performance frictions (silos, cross-team duplication, ownerless areas, single-person bottlenecks).
- Bidirectional `workspace-ops <-> hr-org` contract via `Organization-Model.md`: Architect infers the de-facto org and hands it to hr-org; hr-org designs the target model and hands it back; workspace-ops reads it (`hr_org.organization_model_path`) to place files and shape information architecture, the model taking precedence over the inferred map.
- workspace-ops refinements: incremental scan cache (`_snapshots/scan-index.json`); a concrete JSON action-plan schema with example for v1.1 Execute; an Advise decisions register; optional file-organization templates (PARA, Johnny.Decimal, function-first); and a governance/IAM seam in Architect (read-only Workspace groups/OU/policy signals when a connector exists, routed to hr-org / compliance-ops / a future security-ops).
- `.exec-os-config.yml`: added the `hr_org` section (organization model path, default operating model, work modes, sites).
- Plugin and marketplace manifests updated to bundle all four skills.
- Roadmap: added security-ops / iam-ops (identity and access governance); hr-org graduated from roadmap to built.

### Changed
- workspace-ops Architect, Standardize, and Onboarding now consume `Organization-Model.md` when present, mirroring the target org in the information architecture.

## [0.1.0] - 2026-06-01

### Added
- Repository scaffolding: README, LICENSE (MIT), `.gitignore`, CHANGELOG, CONTRIBUTING, SETUP.
- `.exec-os-config.yml` template: the single source of truth every skill reads first (platforms, linked Founder-OS repos, dataroom canonical structure, diligence stage profiles and sensitivity tiers, workspace-ops sandbox safety).
- Plugin packaging: `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json` bundling the skills as one plugin.
- **dataroom-ops** skill (the library): `SKILL.md` with three modes (Bootstrap, Sync, Audit) and references for the canonical structure, sync protocol, audit protocol, and config/handoff. Packaged as `dataroom-ops.skill`.
- **diligence-ops** skill (the delivery counter): `SKILL.md` with four modes (Fundraise Data Room Prep, Due Diligence Support, Board and Investor Reporting, Audit Prep) and references for built-in Swiss stage checklists, packaging and access control, Q&A and evidence, reporting, and config/handoff. Packaged as `diligence-ops.skill`.
- **workspace-ops** skill (the substrate): `SKILL.md` with v1.0 modes (Scan, Advise, Standardize, Onboarding; Execute deferred to v1.1) across local filesystem, Google Drive, Google Workspace, and Notion, with the safety model, scan/providers and hybrid dedup, advise protocol, the file-organization standard and onboarding, and config/handoff. Advice-only and never-delete. Packaged as `workspace-ops.skill`.

### Design decisions
- Decomposition by job/trigger/audience: dataroom-ops (library, internal), diligence-ops (delivery counter, external), workspace-ops (substrate, internal).
- Exec-OS consumes Founder-OS outputs and never duplicates its strategy or metrics work.
- Diligence calibrated on Swiss venture standards (SICTIC seed, Startup Board Academy governance) and M&A-grade acquisition lists (Elysium Lab).
- workspace-ops v1.0 is advice-only; Execute mode (safe batch moves) deferred to v1.1 under mandatory safeguards (never delete, archive + snapshot + undo log + confirmation).

[0.3.0]: https://github.com/Mr-Hodler/Exec-OS/releases/tag/v0.3.0
[0.2.0]: https://github.com/Mr-Hodler/Exec-OS/releases/tag/v0.2.0
[0.1.0]: https://github.com/Mr-Hodler/Exec-OS/releases/tag/v0.1.0
