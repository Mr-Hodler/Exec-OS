---
name: investor-ops
description: >-
  Runs the whole investor and capital lifecycle for one company: build and maintain the canonical
  data room from Founder-OS outputs, find and reach investors (research, fit scoring, cold and warm
  outreach, pipeline and CRM), and package everything for any third party under scrutiny (fundraise
  prep, due diligence, board, audit, M&A). Merges the former dataroom-ops and diligence-ops and adds
  investor sourcing and outreach. Use when the user says: "set up my data room", "sync my Founder-OS
  outputs", "build an investor list", "who should I raise from", "investor fit", "draft cold outreach
  to investors", "track my raise pipeline", "prep a data room for a fundraise", "answer this DD
  questionnaire", "build a board pack", "monthly investor letter", "prepare for our audit", "get ready
  for M&A". Three mode families: Data Room (Bootstrap, Sync, Audit), Investor Sourcing and Outreach
  (List, Fit and Scoring, Outreach and Pipeline, Prospect Updates), Diligence and Delivery (Fundraise
  Prep, DD Support, Board and Investor Delivery, Audit Prep). Per-company and isolated, platform-
  agnostic, Swiss-calibrated (SICTIC, Innosuisse, Startup Board Academy, Elysium M&A). Never deletes,
  never edits Founder-OS source files, hard-blocks restricted content and logs access. Never uses em dashes.
---

# investor-ops

The **investor and capital engine** of Exec-OS. One skill for everything you do to raise money and to survive being examined. It does three jobs in sequence, and you enter at whichever one you need:

1. **Data Room (the library).** Assemble every deliverable you produce for a company into one canonical, organized, examiner-ready room, then keep it honest: no gaps, no stale files, no version conflicts, no duplicates.
2. **Investor Sourcing and Outreach (getting the money in).** Build the target investor list, score fit, run cold and warm outreach with materials from Founder-OS, and track the whole raise as a pipeline with a CRM.
3. **Diligence and Delivery (facing whoever examines you).** Package the room for a specific third party (an investor in a round, a due diligence team, the board, an auditor, an acquirer), gate by sensitivity, prove it against a named checklist, deliver, and log.

It does not invent strategy content. Decks, business models, GTM, and metrics come from Founder-OS. investor-ops collects and organizes them (job 1), uses them to raise (job 2), and packages them for examiners (job 3). This skill replaces the former `dataroom-ops` and `diligence-ops`, and adds sourcing and outreach.

---

## Core principle

> Keep one honest source of truth per company, use it to find and win the right investors, and show each outside party exactly what they should see, proven against a named standard, with every disclosure logged.

Rules that override everything else:

1. **Per-company and isolated.** Each company gets its own isolated data room, pipeline, and packages. Never merge two companies, never expose one company's data inside another's. One target company per run.
2. **Never delete.** A superseded or removed file is moved to the configured archive with a timestamp, never trashed. Latest version in place, history in the archive.
3. **Index everything, copy the finals, stamp metadata.** Sync indexes every relevant deliverable by reference and copies only approved finals into the room, each stamped with `audience`, `lens`, `version`, `source_skill`, `sensitivity`.
4. **Hard-block restricted by default.** Content tagged `restricted` (employee PII, litigation, key IP, principals/counsel-only) never enters a package or an investor share automatically. Including it needs an explicit per-item override with a logged reason.
5. **Completeness is relative to a named checklist.** Never claim "ready" in the abstract. Always name the stage or framework ("seed-ready per SICTIC", "Series A gaps: 3", "SOC 2 evidence 80 percent assembled").
6. **Every disclosure is logged.** Who was granted access, to what, at what sensitivity, and when. The access log in `99_DD_QA_&_Trackers/Access_Log` is non-negotiable in a live process.
7. **Outreach is grounded and consented.** Investor facts (thesis, check size, portfolio) are researched from real sources and cited, never fabricated. Materials sent to investors come from Founder-OS (`narrative-assets-ops`), not re-written here. Respect anti-spam and consent norms; log every touch.
8. **Platform-agnostic.** The room, pipeline, and packages can live on Notion, Google Drive, SharePoint, or Confluence. Read `dataroom.platform` from config, never hardcode a platform or an ID.

### Hard formatting bans (every mode, every output)

- **Never use an em dash anywhere.** Use a comma, a colon, parentheses, or split the sentence. The only exception is verbatim quoted source text.
- No bare URLs. Embed every link in descriptive text.

---

## Configuration and platform (read first)

Read `.exec-os-config.yml` (prefer `.exec-os-config.local.yml` if present) before acting. You need:

- **Data Room:** `dataroom.platform`, `dataroom.root_name`, `dataroom.canonical_structure`, `dataroom.metadata_schema`.
- **Diligence:** `diligence.default_jurisdiction` (CH), `diligence.stage_profiles`, `diligence.sensitivity_tiers`, `diligence.qa_tracker`.
- **Outreach:** `outreach.sources`, `outreach.pipeline_stages`, `outreach.fit_weights`, `outreach.crm_location`, `outreach.update_cadence` (new block; defaults in `references/investor-sourcing-and-outreach.md`).
- `linked_founder_os_repos` and the **target company** for this run (source of both deliverables and the materials outreach sends).
- `preferences.visual_artifact` (board packs, readiness dashboards, and pipeline boards may render as HTML) and `preferences.ai_ops_autonomous`.

If a source, platform, or linked repo is unreachable, **degrade gracefully**: do the work you can and report exactly what you could not reach. Never fail the whole run because one source is offline. Full rules: `references/config-and-handoff.md`.

---

## When to use which mode

| Family | Mode | Trigger |
| --- | --- | --- |
| **Data Room** | **Bootstrap** | "set up / bootstrap the data room for <company>" |
| | **Sync** | "sync / pick up the latest deliverables", "pull my Founder-OS outputs in" |
| | **Audit** | "audit the data room", "what is missing", "find stale / duplicate / conflicting files" |
| **Sourcing & Outreach** | **Investor List** | "build an investor list", "who should I raise from", "find investors for <stage/sector>" |
| | **Fit & Scoring** | "score these investors", "rank my targets", "is <fund> a fit" |
| | **Outreach & Pipeline** | "draft outreach to <investor>", "track my raise", "update the pipeline", "who do I follow up" |
| | **Prospect Updates** | "send a prospect update", "nurture my warm investors" |
| **Diligence & Delivery** | **Fundraise Prep** | "prep a data room for a fundraise / seed / Series A", "what is missing for <stage>" |
| | **DD Support** | "answer this DD questionnaire", "DD Q&A", "assemble evidence for <area>" |
| | **Board & Investor Delivery** | "file / share the board pack", "send the monthly investor letter", "distribute the quarterly update" |
| | **Audit Prep** | "prepare for our audit", "SOC 2 / ISO 27001 / GDPR / financial audit evidence" |

If the request is ambiguous, default to **Audit** (read-only, safe) for the room, or ask which audience and stage for a package (the checklist depends on both).

---

## Family 1: Data Room

The library. Builds and keeps the canonical corpus honest. It does not curate examiner-facing packages (that is Family 3) and does not write strategy (that is Founder-OS).

- **Bootstrap.** Identify the target company (match a `linked_founder_os_repos` entry). Create the room named per company on `dataroom.platform` using `dataroom.canonical_structure` (do not invent folders). Apply sector overlay(s) by `company_type`. Add `99_DD_QA_&_Trackers` with empty Q&A and access-log placeholders. Idempotent: re-running fills gaps without clobbering. Seed a root index page. See `references/canonical-structure.md`, `references/sector-overlays.md`.
- **Sync.** Resolve sources from the company's Founder-OS `outputs/`. Classify each deliverable to a canonical folder and a `lens`. Hybrid pickup: index every relevant item by reference, copy only approved finals. Stamp the full `metadata_schema`. Version and archive superseded items (never delete). Deduplicate by hash, report near-duplicates for human judgment. Update the index and manifest. See `references/sync-protocol.md`.
- **Audit.** Read-only. Pick the yardstick (stage profile plus sector overlay). Detect gaps, stale items, version conflicts, near-duplicates, sensitivity-tag issues. Deliver a prioritized punch list (blocker / should-fix / nice-to-have) and offer to run the fixes. See `references/audit-protocol.md`.

---

## Family 2: Investor Sourcing and Outreach

Getting the money in. This is the piece the old two skills did not cover. Grounded in real sources, materials pulled from Founder-OS, every touch logged. Full mechanics, templates, and schemas: `references/investor-sourcing-and-outreach.md`.

- **Investor List.** Build a target investor list for the company's stage, sector, geography, and round size. Draw from configured `outreach.sources` (VC and angel directories, funding maps, syndicates, the founder's warm network, and prior-round investors), plus research. Output one living **investor tracker** with, per investor: name, firm, type (VC / angel / family office / strategic / grant body), stage focus, sector focus, geography, typical check size, thesis, portfolio and conflicts, warm-intro path, source, and status. Never fabricate: cite where each fact came from, flag unknowns.
- **Fit & Scoring.** Score and rank each investor by `outreach.fit_weights`: stage match, sector match, check-size match, geography, portfolio fit vs conflict, value-add, and warm-path strength. Output a ranked shortlist with a one-line "why" per investor and the recommended intro path (warm before cold).
- **Outreach & Pipeline (CRM).** Draft cold and warm outreach that pulls the current teaser / deck / one-pager from Founder-OS `narrative-assets-ops` (do not re-write materials here, reference them). Sequence the sends and follow-ups on the configured cadence. Maintain the pipeline in `outreach.crm_location`, moving each investor through `outreach.pipeline_stages` (Researched, Contacted, Replied, Meeting, Diligence, Term Sheet, Closed or Passed). Log every interaction and next action. Deliver a pipeline snapshot: count by stage, this-week actions, stale contacts to nudge.
- **Prospect Updates.** Draft periodic nurture updates to warm-but-not-closed investors (traction since last touch, momentum, round status). Keep them short and honest. For updates to investors who have already invested, use Family 3 Board and Investor Delivery instead (that is examination-grade reporting, this is nurture).

---

## Family 3: Diligence and Delivery

Facing whoever examines you. Takes the Family 1 room and curates a gated, logged package for a named audience and checklist. Consumes the room, writes only into `99_DD_QA_&_Trackers`, never edits source files.

- **Fundraise Prep.** Confirm company and stage (stage drives the checklist: seed is SICTIC-grade, Series A/B heavier, M&A is Elysium-grade). Consume the Family 1 Audit as the single gap source of truth (do not recompute gaps). Gate sensitivity, build the access-filtered investor view plus optional export, open the access-log entry, deliver a readiness summary ("<stage>-ready except N items"). See `references/checklists.md`, `references/packaging-and-access.md`.
- **DD Support.** Ingest a received questionnaire (legal / financial / tech / commercial) or start from the built-in stage checklist. Map each question to evidence in the room, status it (answered / partial / missing / N/A), draft answers grounded only in room evidence, gate and log every disclosure, maintain the Q&A and evidence trackers. See `references/qa-and-evidence.md`.
- **Board & Investor Delivery.** The board pack and investor letter are **authored and assembled by Founder-OS `narrative-assets-ops`**, not here. investor-ops **delivers** them: file the finished pack in the data room, audience-gate (board may see `confidential`, never `restricted` unless the board owns it and it is logged), log distribution, and manage the recurring cadence (monthly letter, quarterly board). If the pack is missing or stale, route to `narrative-assets-ops`. It does not author or re-derive content. See `references/reporting.md`.
- **Audit Prep.** Name the framework (financial audit, SOC 2, ISO 27001, GDPR / Swiss FADP), map controls to evidence, assemble the evidence index, flag gaps, deliver a readiness percentage per control area. See `references/checklists.md`.

---

## When NOT to use

- **Do not produce strategy, decks, financials, or metrics from scratch.** Those come from Founder-OS (`narrative-assets-ops`, `business-model`, `gtm`, `metrics-dashboard`). investor-ops collects, raises with, and packages them.
- **Do not reorganize the raw filesystem.** Cleaning up Documents/Drive structure is `workspace-ops`. investor-ops touches only the canonical data room, the pipeline, and the trackers.
- **Do not design the team or org.** Headcount, hiring, and org structure are `functional-hr-ops`.
- **Do not give legal advice.** For deep contract review or a formal compliance opinion, assemble the evidence and defer the judgment to the relevant legal skill or counsel.
- **Never delete a file, never include restricted content silently, never claim readiness without naming the checklist, never fabricate investor data.**

---

## Skill choreography

- **Upstream: Founder-OS.** Sync reads each company's `outputs/`. Outreach pulls investor-facing materials from `narrative-assets-ops` and numbers from `metrics-dashboard`. Never duplicates or re-derives them.
- **Beneath: workspace-ops.** Organizes the raw files on disk/Drive before they reach the data room. If Sync finds a chaotic source, it can suggest a workspace-ops pass, but does not run it.
- **Peer: functional-hr-ops.** Owns team and org design. investor-ops references the org where a package needs it (for example team slides in a board pack), but does not design it.
- **Scheduling.** Recurring reporting and outreach cadences can register a scheduled task; the generation logic stays here.

---

## Quality bar (check before delivering)

- Per-company isolation holds across room, pipeline, and packages; no cross-company leakage.
- Every room item carries the full metadata schema including a sensitivity tier; Sync copied only finals and archived (never deleted) superseded versions.
- Audit and packages measured completeness against a **named** stage profile or framework.
- Investor list and scores cite their sources; unknowns are flagged, nothing fabricated. Outreach materials came from Founder-OS, not re-written here.
- Pipeline reflects every logged touch; the CRM is current and the next action per live investor is set.
- No `restricted` item was included or shared without an explicit, logged override; every disclosure is in the access log.
- Nothing was written to Founder-OS source files; missing items were routed upstream, not fabricated.
- No em dashes anywhere. No bare URLs. Unreachable sources reported rather than silently skipped.

---

## Reference files

- `references/canonical-structure.md` - the canonical data room taxonomy, what each folder holds, per-stage subsets (SICTIC, Startup Board Academy, Elysium Lab).
- `references/sector-overlays.md` - additive sector overlays (saas, hardware, crypto, fintech, ai) that extend base folders and the DD checklist by company type.
- `references/sync-protocol.md` - hybrid index-plus-copy mechanics, metadata stamping, versioning and archive, hashing and dedup.
- `references/audit-protocol.md` - gap / stale / conflict / duplicate detection, freshness windows, report format.
- `references/investor-sourcing-and-outreach.md` - investor list sources, the fit-scoring rubric, pipeline stages, the CRM tracker schema, outreach templates and cadence, consent and anti-spam. (new)
- `references/checklists.md` - built-in stage DD checklists and audit frameworks (financial, SOC 2, ISO 27001, GDPR), mapped to canonical folders.
- `references/packaging-and-access.md` - hybrid delivery (access-filtered view plus export bundle), sensitivity enforcement, override-with-reason, the access log.
- `references/qa-and-evidence.md` - the DD Q&A tracker workflow, questionnaire ingestion, evidence mapping and answer drafting.
- `references/reporting.md` - board pack and investor letter templates, on-demand and scheduled generation, pulling from the metrics dashboard.
- `references/config-and-handoff.md` - reading config, resolving linked repos, graceful degradation, writing the trackers.
