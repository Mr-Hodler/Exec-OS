# Knowledge-Ops

The **horizontal operations layer** for founders and COO-shaped operators. Where [Founder-OS](https://github.com/Mr-Hodler/founder-os) runs the strategic verticals of a *single* company (validation, market intel, GTM, branding, business model, legal), Knowledge-Ops runs the *cross-company* operations that sit **above** any one venture: assembling a clean data room, surviving due diligence, reporting to a board, and keeping the underlying files and workspaces in order.

It is built for the operator who manages several companies or projects at once and needs the same standard applied everywhere, not the founder who lives inside one product.

## Why a separate repo

Founder-OS is company-scoped: one chat, one company, one strategy. Knowledge-Ops is meta-level: one chat, your whole portfolio. Keeping them apart buys scope cleanliness, a smaller attack surface for Founder-OS, a clear mental model (strategy vs operations), and the ability to standardize across companies. Knowledge-Ops *consumes* Founder-OS outputs; it never duplicates its strategy work.

## The skills

Three skills, split by job, trigger, and audience rather than by topic.

| Skill | Role | Job | Audience | Trigger |
| --- | --- | --- | --- | --- |
| **dataroom-ops** | The library | Build and maintain the canonical data room as a single organized source of truth, assembled from Founder-OS outputs | You, internal | Ongoing hygiene |
| **diligence-ops** | The delivery counter | Package the data room for any third party under scrutiny: investors, due diligence, board, audit. Stage-adaptive (seed to M&A) | External examiner | A fundraise, DD request, board cycle, or audit |
| **knowledge-custodian** | The substrate | Keep files and workspaces organized across all companies, and infer the de-facto org from the file topology. Advice-only in v1.0; safe batch reorganization in v1.1 | You, internal | Always-on |
| **hr-org** | The team architect | Design team and org structure, optimize team operations, plan workforce, and run hiring. Produces the Organization Model that knowledge-custodian mirrors in information architecture | You, internal | Org design, performance, hiring |

The handoff is clean: **dataroom-ops** produces the canonical corpus, **diligence-ops** consumes it and curates examiner-facing packages, and **knowledge-custodian** organizes the raw substrate beneath both. None of them duplicate Founder-OS, which owns the strategy artifacts and the metrics dashboard that feed board packs and the data room.

knowledge-custodian and hr-org form a bidirectional pair: knowledge-custodian's Architect infers the de-facto org from the file topology and hands it to hr-org; hr-org designs the target Organization Model and hands it back, which knowledge-custodian uses to place files (for example marketing design assets under `marketing/design/`) and shape information architecture. One owns team architecture, the other owns information architecture, via a shared `Organization-Model.md`.

**Status:** all four skills are built and packaged. knowledge-custodian is advice-only in v1.0 (its Execute mode, safe batch moves, lands in v1.1).

### dataroom-ops (the library)

Modes: **Bootstrap** (lay down the canonical folder/page structure on your chosen platform), **Sync** (pick up deliverables from linked Founder-OS repos and stamp them with metadata: audience, lens, version, source skill, sensitivity), **Audit** (gap detection, stale files, version conflicts, near-duplicates).

### diligence-ops (the delivery counter)

Modes by audience: **Fundraise Data Room Prep** (stage checklists, sensitivity tagging, missing items), **Due Diligence Support** (legal / financial / tech / commercial DD questionnaires, Q&A tracker, evidence assembly, access log), **Board & Investor Reporting** (board packs, investor letters, recurring cadence), **Audit Prep** (evidence assembly for financial, security, and compliance audits: ISO, SOC 2, GDPR). Calibrated on Swiss venture standards (SICTIC, Innosuisse) and M&A-grade acquisition lists.

### knowledge-custodian (the substrate) - built, advice-only v1.0

Modes: **Scan** (read-only inventory of structure, metadata, and organizational signals), **Advise** (a report of suggested consolidations, orphan files, naming violations, duplicates, stale files, with zero filesystem changes), **Standardize** (derive an org-aware "Aron's File Organization Standard" from how you already organize, plus best practice), **Onboarding** (set up a compliant structure for a new company), and **Architect** (read the information topology, infer the implicit functional and team structure, recommend the target information architecture, and flag operations/performance frictions such as silos, cross-team duplication, and ownerless areas). **Execute** (safe batch moves) is deferred to v1.1. The skill **never deletes**: it moves to a timestamped `_archive/`, snapshots state before any action, keeps an undo log, and never touches the blacklist.

Architect owns information architecture, not team design: it infers the functional map and flags frictions from the topology, then hands people and team-scaling decisions to **hr-org**, which consumes that evidence and hands back the Organization Model.

### hr-org (the team architect)

Modes: **Org Design** (structure teams, departments, product lines, sites, and work modes using a fitted operating model: Team Topologies, Spotify, functional, divisional, matrix, two-pizza, lean), **Team Ops & Performance** (interaction modes, cross-team operations, cognitive load, friction diagnosis, performance levers), **Workforce Planning** (need detection, gap analysis, build vs hire, sequencing), **Hiring Prep** (role definition, job description, scorecard, interview plan, candidate prospectus). It produces `Organization-Model.md`, the shared artifact knowledge-custodian consumes. It is advisory: it recommends and drafts, it does not make personnel decisions or set pay.

## Roadmap and pipeline

Knowledge-Ops is designed to grow into a full COO operations suite. Skills under consideration for later versions, all horizontal and cross-company:

- **vendor-ops** - vendor/tooling inventory, contract renewals, spend, TCO across companies.
- **compliance-ops** - cross-company compliance posture (GDPR, ISO 27001, SOC 2) and audit readiness as a standing capability rather than a one-off prep.
- **process-ops** - SOPs, RACI, and runbooks for the operations that repeat across companies.
- **security-ops / iam-ops** - identity and access management, Google Workspace and directory governance (groups, org units, roles, security policies). Consumes the governance signals knowledge-custodian's Architect surfaces, and owns the IAM decisions knowledge-custodian deliberately does not.
- **reporting-ops** - a recurring-reporting engine if board/investor reporting outgrows being a mode inside diligence-ops.

These are intentionally *not* built yet. The repo ships the three skills above first and earns each addition.

## Repository layout

This repo is a self-contained Claude plugin (and a one-plugin marketplace), so it installs directly. The four skills ship as one plugin; each also ships as a standalone `.skill` for one-click install.

```
Knowledge-Ops-Repo/                      # repo root = the plugin AND the marketplace
├── .claude-plugin/
│   ├── plugin.json                      # plugin manifest (bundles all three skills)
│   └── marketplace.json                 # marketplace manifest listing this plugin
├── .knowledge-ops-config.yml            # single source of truth every skill reads first
├── README.md
├── SETUP.md                             # config schema, platform connect, first run
├── CHANGELOG.md                         # version history (Keep a Changelog)
├── CONTRIBUTING.md
├── LICENSE                              # MIT
├── .gitignore
└── skills/
    ├── dataroom-ops/                    # built
    │   ├── SKILL.md
    │   └── references/                  # canonical-structure, sync-protocol, audit-protocol, config-and-handoff
    ├── dataroom-ops.skill               # packaged for one-click install
    ├── diligence-ops/                   # built
    │   ├── SKILL.md
    │   └── references/                  # checklists, packaging-and-access, qa-and-evidence, reporting, config-and-handoff
    ├── diligence-ops.skill
    ├── knowledge-custodian/             # built (advice-only v1.0; Execute in v1.1)
    │   ├── SKILL.md
    │   └── references/                  # safeguards, scan-and-providers, advise-protocol, information-architecture, standard-and-onboarding, config-and-handoff
    ├── knowledge-custodian.skill
    ├── hr-org/                          # built
    │   ├── SKILL.md
    │   └── references/                  # operating-models, org-design, organization-model, team-ops, workforce-and-hiring, config-and-handoff
    └── hr-org.skill
```

Each skill's `.skill` file is the packaged zip (SKILL.md plus references), sitting alongside its source folder in `skills/` for one-click install.

## Setup

See [SETUP.md](SETUP.md). In short: connect the platform where your data room lives (platform-agnostic: Notion, Google Drive, SharePoint, or Confluence, set in `dataroom.platform`), point `.knowledge-ops-config.yml` at your linked Founder-OS repos and your `knowledge_custodian.scope_paths`, then run a skill. The config file is read first by every skill.

## Install

### Option A - one-click `.skill` (Cowork)

Open the relevant `.skill` file (e.g. `skills/dataroom-ops.skill`) and use **Save skill**.

### Option B - marketplace (Claude Code or Cowork)

```
/plugin marketplace add Mr-Hodler/Knowledge-Ops
/plugin install knowledge-ops@knowledge-ops
```

The first command registers this repo as a marketplace; the second installs the plugin with all four skills.

### Option C - manual / local

```
/plugin marketplace add /path/to/Knowledge-Ops-Repo
/plugin install knowledge-ops@knowledge-ops
```

## Versioning and contributing

Version history lives in [CHANGELOG.md](CHANGELOG.md). To propose changes, see [CONTRIBUTING.md](CONTRIBUTING.md). The project follows [Semantic Versioning](https://semver.org/).

## License

MIT. See [LICENSE](LICENSE). Copyright (c) 2026 Aron Clementi.
