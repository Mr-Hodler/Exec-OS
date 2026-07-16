# Exec-OS

The **horizontal operations layer** for founders and COO-shaped operators. Where [Founder-OS](https://github.com/Mr-Hodler/founder-os) runs the strategic verticals of a *single* company (validation, market intel, GTM, branding, business model, legal), Exec-OS runs the *cross-company* operations that sit **above** any one venture: assembling a clean data room, surviving due diligence, reporting to a board, and keeping the underlying files and workspaces in order.

It is built for the operator who manages several companies or projects at once and needs the same standard applied everywhere, not the founder who lives inside one product.

## Founder-OS + Exec-OS: two OS, one company

Exec-OS is one half of a pair. With its companion [Founder-OS](https://github.com/Mr-Hodler/founder-os) it forms an operating system for the **company of the future**: the founder and the team stay in charge and are amplified, while the AI carries the management, the execution, and the flow of information between people, data, decisions, and levels.

**Vocabulary, three levels, never overloaded:**

| Level | Marker | What it is | Examples |
| --- | --- | --- | --- |
| **OS** | `-OS` | a system: a repo that runs one whole side of the company | Founder-OS, Exec-OS |
| **Ops** | `-ops` | a skill: the operational engine for one domain | `investor-ops`, `workspace-ops`, `functional-hr-ops` |
| **Mode** | inside a skill | a step, or how you enter a skill | Bootstrap, Sync, Audit; Mode 1 / Mode 2 |

The rule that keeps names clean: `-OS` is the system level, `-ops` is the skill level, a Mode lives inside a skill. The word "ops" never names a system, so the levels never blur.

**Who does what:**

| | Founder-OS | Exec-OS |
| --- | --- | --- |
| Persona | the founder or CEO's strategic brain | the AI executive team that runs the company (CFO, COO, Chief People) |
| Scope | one company, deep | cross-company, operational |
| Owns | strategy: validation, market, product, GTM, brand, business model, legal, risk, narrative | execution: data room, fundraising, due diligence, board, files, org, hiring |
| Answers | what to build and why | get it done, keep it running, keep everyone connected |

Exec-OS consumes Founder-OS outputs (it never re-does strategy). Founder-OS feeds Exec-OS: its deliverables are the raw material Exec-OS files, packages, and executes on. Neither duplicates the other.

The bet: a founder plus a small, empowered team, each amplified by an AI that owns the management and execution layer, can run a company that used to need a full back office.

## Why a separate repo

Founder-OS is company-scoped: one chat, one company, one strategy. Exec-OS is meta-level: one chat, your whole portfolio. Keeping them apart buys scope cleanliness, a smaller attack surface for Founder-OS, a clear mental model (strategy vs operations), and the ability to standardize across companies. Exec-OS *consumes* Founder-OS outputs; it never duplicates its strategy work.

## The skills

Three skills, split by job, trigger, and audience rather than by topic.

| Skill | Role | Job | Audience | Trigger |
| --- | --- | --- | --- | --- |
| **investor-ops** | The investor & capital engine | Build and maintain the canonical data room from Founder-OS outputs, find and reach investors (sourcing, fit, outreach, pipeline/CRM), and package the room for any third party under scrutiny: investors, due diligence, board, audit, M&A | You, internal + external examiner | Any raise, DD request, board cycle, or audit |
| **workspace-ops** | The substrate | Keep files and workspaces organized across all companies, and infer the de-facto org from the file topology. Advice-only in v1.0; safe batch reorganization in v1.1 | You, internal | Always-on |
| **functional-hr-ops** | The team architect | Design team and org structure, optimize team operations, plan workforce, run hiring, and roll out org change. Produces the Organization Model that workspace-ops mirrors in information architecture | You, internal | Org design, performance, hiring, rollout |

The handoff is clean: **investor-ops** owns the whole investor and capital lifecycle (build the data room, find and reach investors, package it for examiners), and **workspace-ops** organizes the raw substrate beneath it. Neither duplicates Founder-OS, which owns the strategy artifacts, the fundraise materials (`narrative-assets-ops`), and the metrics dashboard that feed board packs and the data room.

workspace-ops and functional-hr-ops form a bidirectional pair: workspace-ops's Architect infers the de-facto org from the file topology and hands it to functional-hr-ops; functional-hr-ops designs the target Organization Model and hands it back, which workspace-ops uses to place files (for example marketing design assets under `marketing/design/`) and shape information architecture. One owns team architecture, the other owns information architecture, via a shared `Organization-Model.md`.

**Status:** all three skills are built and packaged. workspace-ops is advice-only in v1.0 (its Execute mode, safe batch moves, lands in v1.1).

### investor-ops (the investor & capital engine)

One skill for the whole raise-and-be-examined lifecycle, in three mode families. It merges the former `dataroom-ops` and `diligence-ops` and adds investor sourcing and outreach.

- **Family 1: Data Room.** **Bootstrap** (lay down the canonical folder/page structure on your chosen platform), **Sync** (pick up deliverables from linked Founder-OS repos and stamp them with metadata: audience, lens, version, source skill, sensitivity), **Audit** (gap detection, stale files, version conflicts, near-duplicates).
- **Family 2: Investor Sourcing & Outreach.** **Investor List** (build the target list from directories, funding maps, warm network), **Fit & Scoring** (rank by stage/sector/check-size/geography/portfolio/value-add/warm-path), **Outreach & Pipeline** (cold and warm outreach pulling materials from Founder-OS `narrative-assets-ops`, a CRM through the raise stages), **Prospect Updates** (nurture warm investors).
- **Family 3: Diligence & Delivery.** **Fundraise Data Room Prep** (stage checklists, sensitivity tagging, missing items), **Due Diligence Support** (legal / financial / tech / commercial DD questionnaires, Q&A tracker, evidence assembly, access log), **Board & Investor Delivery** (deliver the board pack / investor letter authored by Founder-OS `narrative-assets-ops`: file, audience-gate, log distribution, manage cadence), **Audit Prep** (evidence assembly for financial, security, and compliance audits: ISO, SOC 2, GDPR). Calibrated on Swiss venture standards (SICTIC, Innosuisse) and M&A-grade acquisition lists.

### workspace-ops (the substrate) - built, advice-only v1.0

Modes: **Scan** (read-only inventory of structure, metadata, and organizational signals), **Advise** (a report of suggested consolidations, orphan files, naming violations, duplicates, stale files, with zero filesystem changes), **Standardize** (derive an org-aware "Aron's File Organization Standard" from how you already organize, plus best practice), **Onboarding** (set up a compliant structure for a new company), and **Architect** (read the information topology, infer the implicit functional and team structure, recommend the target information architecture, and flag operations/performance frictions such as silos, cross-team duplication, and ownerless areas). **Execute** (safe batch moves) is deferred to v1.1. The skill **never deletes**: it moves to a timestamped `_archive/`, snapshots state before any action, keeps an undo log, and never touches the blacklist.

Architect owns information architecture, not team design: it infers the functional map and flags frictions from the topology, then hands people and team-scaling decisions to **functional-hr-ops**, which consumes that evidence and hands back the Organization Model.

### functional-hr-ops (the team architect)

Modes: **Org Design** (structure teams, business units, departments, product lines, sites, work modes, reporting lines, and roles using a fitted operating model scaled by company size), **Team Ops & Performance** (interaction modes, cross-team operations as workflows, cognitive load, friction diagnosis, performance levers), **Workforce Planning** (need detection, gap analysis, build vs hire, sequencing), **Hiring Prep** (role definition, job description, scorecard, interview plan, candidate prospectus), **Org Rollout** (phased implementation roadmap with success metrics). It reasons with operating-model frameworks and the structural research behind them (Team Topologies, Spotify, functional/divisional/matrix, two-pizza, lean; Dunbar, Conway, Tuckman, span of control), defines roles by what they own and explicitly do not, carries an anti-patterns catalog, and produces `Organization-Model.md`, the shared artifact workspace-ops consumes. It is advisory: it recommends and drafts, it does not make personnel decisions or set pay.

## Roadmap and pipeline

Exec-OS is designed to grow into a full COO operations suite. Skills under consideration for later versions, all horizontal and cross-company:

- **finance-ops** - the CFO's operational finance beyond fundraising: bookkeeping, invoicing, real burn and runway tracking, budget vs actual. Complements investor-ops (capital) and Founder-OS business-model (projections).
- **sales-ops** - pipeline, CRM hygiene, and sales execution operations.
- **customer-success-ops** - onboarding, health scoring, and retention operations (consumes the churn signals Founder-OS product-design surfaces).
- **vendor-ops** - vendor/tooling inventory, contract renewals, spend, TCO across companies.
- **compliance-ops** - cross-company compliance posture (GDPR, ISO 27001, SOC 2) and audit readiness as a standing capability rather than a one-off prep.
- **process-ops** - SOPs, RACI, and runbooks for the operations that repeat across companies.
- **security-ops / iam-ops** - identity and access management, Google Workspace and directory governance (groups, org units, roles, security policies). Consumes the governance signals workspace-ops's Architect surfaces, and owns the IAM decisions workspace-ops deliberately does not.
- **reporting-ops** - a recurring-reporting engine if board/investor reporting outgrows being a mode inside investor-ops.

These are intentionally *not* built yet. The repo ships the three skills above first and earns each addition.

## Repository layout

This repo is a self-contained Claude plugin (and a one-plugin marketplace), so it installs directly. The three skills ship as one plugin; each also ships as a standalone `.skill` for one-click install.

```
Exec-OS-Repo/                      # repo root = the plugin AND the marketplace
├── .claude-plugin/
│   ├── plugin.json                      # plugin manifest (bundles all three skills)
│   └── marketplace.json                 # marketplace manifest listing this plugin
├── .exec-os-config.yml            # single source of truth every skill reads first
├── README.md
├── SETUP.md                             # config schema, platform connect, first run
├── CHANGELOG.md                         # version history (Keep a Changelog)
├── CONTRIBUTING.md
├── LICENSE                              # MIT
├── .gitignore
└── skills/
    ├── investor-ops/                    # built (merges former dataroom-ops + diligence-ops + sourcing/outreach)
    │   ├── SKILL.md
    │   └── references/                  # canonical-structure, sync-protocol, audit-protocol, investor-sourcing-and-outreach, checklists, packaging-and-access, qa-and-evidence, reporting, sector-overlays, config-and-handoff
    ├── investor-ops.skill               # packaged for one-click install
    ├── workspace-ops/             # built (advice-only v1.0; Execute in v1.1)
    │   ├── SKILL.md
    │   └── references/                  # safeguards, scan-and-providers, advise-protocol, information-architecture, standard-and-onboarding, config-and-handoff
    ├── workspace-ops.skill
    ├── functional-hr-ops/              # built
    │   ├── SKILL.md
    │   └── references/                  # operating-models, anti-patterns, org-design, organization-model, team-ops, workforce-and-hiring, rollout-and-metrics, config-and-handoff
    └── functional-hr-ops.skill
```

Each skill's `.skill` file is the packaged zip (SKILL.md plus references), sitting alongside its source folder in `skills/` for one-click install.

## Setup

See [SETUP.md](SETUP.md). In short: connect the platform where your data room lives (platform-agnostic: Notion, Google Drive, SharePoint, or Confluence, set in `dataroom.platform`), point `.exec-os-config.yml` at your linked Founder-OS repos and your `workspace_ops.scope_paths`, then run a skill. The config file is read first by every skill.

## Install

### Option A - one-click `.skill` (Cowork)

Open the relevant `.skill` file (e.g. `skills/investor-ops.skill`) and use **Save skill**.

### Option B - marketplace (Claude Code or Cowork)

```
/plugin marketplace add Mr-Hodler/Exec-OS
/plugin install exec-os@exec-os
```

The first command registers this repo as a marketplace; the second installs the plugin with all four skills.

### Option C - manual / local

```
/plugin marketplace add /path/to/Exec-OS-Repo
/plugin install exec-os@exec-os
```

## Foundations and sources

The skills are not invented from first principles; each is calibrated on established references so its recommendations carry weight.

**Due diligence and data room** (investor-ops) are calibrated on Swiss venture standards: the [SICTIC / Swiss ICT Investor Club](https://www.sictic.ch/) due diligence checklist and the Swiss Angel Investor Handbook, [Innosuisse](https://www.innosuisse.admin.ch/) screening criteria, a Startup Board Academy governance due diligence list, and an Elysium-grade M&A acquisition request list (corporate plus engineering and infrastructure). These map to the canonical data room taxonomy and the per-stage profiles (seed to M&A).

**Team and organization design** (functional-hr-ops) draws on [Team Topologies](https://teamtopologies.com/) (Skelton and Pais) for team types, interaction modes, and cognitive load; the Spotify engineering model (squads, tribes, chapters, guilds); Apple's functional organization as described in the Harvard Business Review article [How Apple Is Organized for Innovation](https://hbr.org/2020/11/how-apple-is-organized-for-innovation); Amazon's two-pizza and single-threaded-leader model; and the classic structural heuristics, Dunbar's number for group size, Conway's law for team-to-architecture alignment, span-of-control limits, and Tuckman's stages as the case for stable over project teams.

**Information architecture** (workspace-ops) offers [PARA](https://fortelabs.com/blog/para/) and [Johnny.Decimal](https://johnnydecimal.com/) as optional baseline templates when there is little existing structure to learn from.

**Repository conventions** follow [Keep a Changelog](https://keepachangelog.com/) and [Semantic Versioning](https://semver.org/).

## Versioning and contributing

Version history lives in [CHANGELOG.md](CHANGELOG.md). To propose changes, see [CONTRIBUTING.md](CONTRIBUTING.md). The project follows [Semantic Versioning](https://semver.org/).

## License

MIT. See [LICENSE](LICENSE). Copyright (c) 2026 Aron Clementi.
