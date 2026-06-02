# Changelog

All notable changes to Knowledge-Ops are documented here. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2026-06-01

### Added
- Repository scaffolding: README, LICENSE (MIT), `.gitignore`, CHANGELOG, CONTRIBUTING, SETUP.
- `.knowledge-ops-config.yml` template: the single source of truth every skill reads first (platforms, linked Founder-OS repos, dataroom canonical structure, diligence stage profiles and sensitivity tiers, knowledge-custodian sandbox safety).
- Plugin packaging: `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json` bundling all three skills as one plugin.
- Skill directories scaffolded: `dataroom-ops`, `diligence-ops`, `knowledge-custodian`.
- **dataroom-ops** skill (the library): `SKILL.md` with three modes (Bootstrap, Sync, Audit) and references for the canonical structure, sync protocol, audit protocol, and config/handoff. Packaged as `dataroom-ops.skill`.
- **diligence-ops** skill (the delivery counter): `SKILL.md` with four modes (Fundraise Data Room Prep, Due Diligence Support, Board and Investor Reporting, Audit Prep) and references for built-in Swiss stage checklists, packaging and access control, Q&A and evidence, reporting, and config/handoff. Packaged as `diligence-ops.skill`.
- **knowledge-custodian** skill (the substrate): `SKILL.md` with five v1.0 modes (Scan, Advise, Standardize, Onboarding, Architect; Execute deferred to v1.1) across local filesystem, Google Drive, Google Workspace, and Notion, and references for the safety model, scan/providers and hybrid dedup plus an organizational-signals pass, advise protocol with a replayable dry-run action plan, information architecture (Architect), the org-aware file-organization standard and onboarding, and config/handoff. Advice-only and never-delete. Packaged as `knowledge-custodian.skill`.
- **Architect mode** in knowledge-custodian: reads the information topology and organizational signals (file/drive types, product/team areas, collaboration and access graph, hotspots, ownership concentration), infers the implicit functional and team structure, recommends the target information architecture, and flags operations/performance frictions (silos, cross-team duplication, ownerless areas, single-person bottlenecks). Owns information architecture only; routes people and team-scaling decisions to a future hr-org skill.
- knowledge-custodian refinements: incremental scan cache (`_snapshots/scan-index.json`) for fast re-scans on large drives; a concrete JSON action-plan schema with example for v1.1 Execute; an Advise decisions register so previously declined findings are not re-suggested; optional file-organization templates (PARA, Johnny.Decimal, function-first) for Standardize; and a governance/IAM seam in Architect (read-only Workspace groups/OU/policy signals when a connector exists, routed to hr-org / compliance-ops / a future security-ops).
- Roadmap: added hr-org (team architecture, counterpart to Architect) and security-ops / iam-ops (identity and access governance).

### Design decisions
- Three-skill decomposition by job/trigger/audience: dataroom-ops (library, internal), diligence-ops (delivery counter, external), knowledge-custodian (substrate, internal).
- Knowledge-Ops consumes Founder-OS outputs and never duplicates its strategy or metrics work.
- Diligence calibrated on Swiss venture standards (SICTIC seed, Startup Board Academy governance) and M&A-grade acquisition lists (Elysium Lab).
- knowledge-custodian v1.0 is advice-only; Execute mode (safe batch moves) deferred to v1.1 under mandatory safeguards (never delete, archive + snapshot + undo log + confirmation).

[0.1.0]: https://github.com/Mr-Hodler/Knowledge-Ops/releases/tag/v0.1.0
