---
name: diligence-ops
description: >-
  Packages a company's data room for any third party under scrutiny: investors, due diligence,
  the board, or an auditor. Use when the user says "prep a data room for a fundraise", "get me
  ready for due diligence", "answer this DD questionnaire", "build a board pack", "write the
  monthly investor letter", "prepare for our audit", "what is missing for a Series A", "assemble
  evidence for SOC 2 / ISO / GDPR", or needs a curated, access-controlled package built from the
  canonical data room. Four modes: Fundraise Data Room Prep, Due Diligence Support (Q&A tracker
  plus evidence), Board and Investor Reporting, Audit Prep. Stage-adaptive and Swiss-calibrated
  (SICTIC seed, Innosuisse, Startup Board Academy governance, Elysium-grade M&A). Delivers a hybrid
  package: an access-filtered shared view plus an on-demand export bundle. Hard-blocks restricted
  content by default and logs every access. Consumes the corpus produced by dataroom-ops; never
  edits source files. Never uses em dashes in any output.
---

# diligence-ops

The **delivery counter** of Knowledge-Ops. It takes the canonical data room that `dataroom-ops` maintains and turns it into a curated, access-controlled package for a specific third party: an investor in a round, a due diligence team, the board, or an auditor. It selects, gates, tracks, and delivers. It does not create source material and does not edit the data room.

The same engine serves every audience: select from the data room, gate by sensitivity, check against a named checklist, assemble evidence, deliver, and log. Only the checklist and the audience change.

---

## Core principle

> Show exactly what this audience should see, prove it against a named standard, and log who saw what. Nothing sensitive leaks, nothing required is missing.

Rules that override everything else:

1. **Consume, never edit.** diligence-ops reads the data room and writes only into `99_DD_QA_&_Trackers` (Q&A, evidence index, access log). It never modifies a source file. If something is missing or stale, it routes the request back to dataroom-ops.
2. **Hard-block restricted by default.** Content tagged `restricted` (employee PII, litigation, key IP, anything principals/counsel-only) never enters a package automatically. Including it requires an explicit per-item override with a logged reason. See `references/packaging-and-access.md`.
3. **Completeness is relative to a named checklist.** Never claim "ready" in the abstract. Always state the stage or framework: "seed-ready per SICTIC", "Series A gaps: 3", "SOC 2 evidence 80 percent assembled".
4. **Every disclosure is logged.** Who was granted access, to what, at what sensitivity, and when. The access log lives in `99_DD_QA_&_Trackers/Access_Log` and is non-negotiable in a live process.
5. **Hybrid delivery.** Default to an access-filtered shared view on the data room platform (live, logged). Produce a standalone export bundle (zip or PDF) on demand when the third party needs it offline. See `references/packaging-and-access.md`.
6. **Per-company and isolated.** One company's package never contains another company's data, exactly as the underlying data room is isolated.

### Hard formatting bans (every mode, every output)

- **Never use an em dash anywhere.** Use a comma, a colon, parentheses, or split the sentence. The only exception is verbatim quoted source text.
- No bare URLs. Embed every link in descriptive text.

---

## Configuration and platform (read first)

Read `.knowledge-ops-config.yml` (prefer `.knowledge-ops-config.local.yml` if present) before acting. You need:

- `diligence.default_jurisdiction` (CH), `diligence.stage_profiles`, `diligence.sensitivity_tiers`, `diligence.qa_tracker`.
- `dataroom.platform`, `dataroom.canonical_structure`, `dataroom.metadata_schema` (you read the room these describe).
- `linked_founder_os_repos` and the **target company** for this run.
- `preferences.visual_artifact` (board packs and readiness dashboards may render as HTML) and `preferences.ai_ops_autonomous`.

If the data room has not been built or synced, say so and hand off to dataroom-ops first. If a required item is missing, route the request to dataroom-ops rather than fabricating it. Graceful degradation and the handoff contract: `references/config-and-handoff.md`.

---

## When to use which mode

| Mode | Trigger | What it does |
| --- | --- | --- |
| **Fundraise Data Room Prep** | "prep a data room for a fundraise / seed / Series A", "what is missing for <stage>" | Scopes the room to a stage checklist, flags missing items (routes to dataroom-ops), tags sensitivity, builds the access-filtered investor view plus optional export. |
| **Due Diligence Support** | "answer this DD questionnaire", "DD Q&A", "assemble evidence for <area>" | Ingests a questionnaire (or uses the built-in stage checklist), maps each question to evidence in the room, tracks status, drafts answers, maintains the Q&A and access logs. |
| **Board and Investor Reporting** | "build a board pack", "monthly investor letter", "quarterly update" | Assembles a board pack or investor letter on demand from `09_Traction` and the Founder-OS metrics dashboard, plus agenda, prior minutes, and supporting docs. Optional recurring schedule. |
| **Audit Prep** | "prepare for our audit", "SOC 2 / ISO 27001 / GDPR / financial audit evidence" | Maps an audit framework's controls to evidence in the room, assembles the evidence index, flags gaps. |

If ambiguous, ask which audience and stage, since the checklist depends on both.

---

## Fundraise Data Room Prep - the workflow

1. **Confirm target company and stage.** Stage drives the checklist (`references/checklists.md`): pre_seed/seed is SICTIC-grade, Series A/B heavier, M&A is Elysium-grade.
2. **Check the room exists and is fresh.** If not built or stale, hand off to dataroom-ops (Bootstrap/Sync/Audit) before packaging.
3. **Score against the stage checklist.** Mark each expected item present / thin / missing. Missing items route to dataroom-ops with a specific request. Never fabricate.
4. **Gate sensitivity.** Confirm every item's `sensitivity` tag. `restricted` items are excluded from the investor view by default; `confidential` items are NDA-gated; `public` items are open. Mis-tiered items are flagged (a leakage risk).
5. **Build the access-filtered view** for the investor's access level (see `references/packaging-and-access.md`), and offer an export bundle for offline sharing.
6. **Open the access log** entry for this investor/process and record what was granted.
7. **Deliver a readiness summary**: "<stage>-ready except N items", each with owner and the route to close it.

---

## Due Diligence Support - the workflow

1. **Source the questions.** Either ingest a received questionnaire (legal / financial / tech / commercial DD) or start from the built-in stage checklist. Normalize into one Q&A tracker. See `references/qa-and-evidence.md`.
2. **Map each question to evidence** in the data room (folder + item + version). Tag the lens (finance, legal, product, commercial, governance, hr, ip).
3. **Status each item:** answered (evidence attached), partial (evidence thin), missing (route to dataroom-ops), or N/A (with reason).
4. **Draft answers** grounded only in data room evidence. Cite the evidence item. Do not assert facts the room does not support; flag those as "to confirm with founder".
5. **Gate and log.** Apply sensitivity rules to every piece of evidence shared. Hard-block restricted unless explicitly overridden with a logged reason. Record each disclosure in the access log.
6. **Maintain the trackers** in `99_DD_QA_&_Trackers`: the Q&A tracker (question, status, evidence, owner, sensitivity) and the evidence index. Deliver a progress snapshot: answered / partial / missing by area.

---

## Board and Investor Reporting - the workflow

1. **Pick the artifact and cadence.** Board pack (deck plus supporting docs plus agenda plus prior minutes) or investor letter. On demand by default; offer a recurring schedule (monthly letter, quarterly board) if the user wants it.
2. **Pull the numbers** from `09_Traction_&_Metrics` and the Founder-OS metrics dashboard (`metrics-aggregation-view`). Never re-derive metrics here; reference the dashboard as the source.
3. **Assemble** against the board-pack template (`references/reporting.md`): highlights, metrics vs plan, financials and runway, pipeline, risks, asks, decisions sought, appendix.
4. **Audience-gate.** Board audience can see `confidential`; never include `restricted` HR/litigation detail unless the board explicitly owns it and it is logged.
5. **Render** to the configured target (deck/doc/PDF; HTML dashboard if `preferences.visual_artifact` allows), file it under `09_Traction` or a `Board` area, and log distribution.
6. **If scheduled**, register the cadence and the source pull so each run is reproducible.

---

## Audit Prep - the workflow

1. **Name the framework:** financial audit, SOC 2, ISO 27001, or GDPR / Swiss FADP. Each has a control-to-evidence map in `references/checklists.md`.
2. **Map controls to evidence** already in the room (chiefly `03_Legal_&_Compliance`, `04_IP_Data_&_Security`, `06_Product_&_Technology`, `02_Financials`).
3. **Assemble the evidence index** in `99_DD_QA_&_Trackers/Evidence_Index`, control by control, with the item and version that satisfies it.
4. **Flag gaps** (controls with no evidence) and route document needs to dataroom-ops or the relevant Founder-OS skill.
5. **Deliver** a readiness percentage per control area and a prioritized gap list. Gate and log exactly as in DD.

---

## When NOT to use

- **Do not build or reorganize the data room.** Structure, Sync, and Audit of the corpus are `dataroom-ops`. diligence-ops only consumes it and writes into the trackers.
- **Do not produce strategy, decks, or metrics from scratch.** Those come from Founder-OS. diligence-ops references and packages them.
- **Do not reorganize the filesystem.** That is `knowledge-custodian`.
- **Never include restricted content silently**, and never claim readiness without naming the checklist.

---

## Skill choreography

- **Upstream: dataroom-ops.** Consumes the canonical, metadata-stamped corpus. Missing or stale items route back to dataroom-ops (Sync/Audit). Writes only into `99_DD_QA_&_Trackers`.
- **Upstream: Founder-OS.** Pulls metrics from `metrics-aggregation-view` and references decks/financials produced there. Never re-derives them.
- **Peer: legal / compliance.** For deep contract review or a formal compliance opinion, diligence-ops assembles the evidence and defers the legal judgment to the relevant legal skill or counsel. It does not give legal advice.
- **Scheduling.** Recurring board/investor reporting can register a scheduled task; the generation logic stays here.

---

## Quality bar (check before delivering)

- The package is scoped to a **named** stage or framework, and readiness is stated relative to it.
- No `restricted` item is included without an explicit, logged override.
- Every disclosure is in the access log; the Q&A and evidence trackers are current.
- Answers and packs are grounded only in data room evidence; unsupported claims are flagged, not asserted.
- Nothing was written to source files; missing items were routed to dataroom-ops, not fabricated.
- Per-company isolation holds. No em dashes anywhere. No bare URLs.

---

## Reference files

- `references/checklists.md` - built-in stage DD checklists (SICTIC seed, Innosuisse, Startup Board Academy governance, Elysium M&A) and audit frameworks (financial, SOC 2, ISO 27001, GDPR), each mapped to canonical data room folders.
- `references/packaging-and-access.md` - hybrid delivery (access-filtered view plus export bundle), sensitivity enforcement, override-with-reason, the access log.
- `references/qa-and-evidence.md` - the DD Q&A tracker workflow, questionnaire ingestion, evidence mapping and answer drafting.
- `references/reporting.md` - board pack and investor letter templates, on-demand and scheduled generation, pulling from the metrics dashboard.
- `references/config-and-handoff.md` - reading config, consuming the dataroom-ops corpus, writing the trackers, graceful degradation.
