# Changelog

All notable changes to Knowledge-Ops are documented here. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Repository scaffolding: README, LICENSE (MIT), `.gitignore`, CHANGELOG, CONTRIBUTING, SETUP.
- `.knowledge-ops-config.yml` template: the single source of truth every skill reads first (platforms, linked Founder-OS repos, dataroom canonical structure, diligence stage profiles and sensitivity tiers, knowledge-custodian sandbox safety).
- Plugin packaging: `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json` bundling all three skills as one plugin.
- Skill directories scaffolded: `dataroom-ops`, `diligence-ops`, `knowledge-custodian`.
- **dataroom-ops** skill (the library): `SKILL.md` with three modes (Bootstrap, Sync, Audit) and references for the canonical structure, sync protocol, audit protocol, and config/handoff. Packaged as `dataroom-ops.skill`.
- **diligence-ops** skill (the delivery counter): `SKILL.md` with four modes (Fundraise Data Room Prep, Due Diligence Support, Board and Investor Reporting, Audit Prep) and references for built-in Swiss stage checklists, packaging and access control, Q&A and evidence, reporting, and config/handoff. Packaged as `diligence-ops.skill`.

### Design decisions
- Three-skill decomposition by job/trigger/audience: dataroom-ops (library, internal), diligence-ops (delivery counter, external), knowledge-custodian (substrate, internal).
- Knowledge-Ops consumes Founder-OS outputs and never duplicates its strategy or metrics work.
- Diligence calibrated on Swiss venture standards (SICTIC seed, Startup Board Academy governance) and M&A-grade acquisition lists (Elysium Lab).
- knowledge-custodian v1.0 is advice-only; Execute mode (safe batch moves) deferred to v1.1 under mandatory safeguards (never delete, archive + snapshot + undo log + confirmation).

[Unreleased]: https://github.com/Mr-Hodler/Knowledge-Ops/compare/main...HEAD
