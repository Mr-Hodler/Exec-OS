#!/usr/bin/env python3
"""
Knowledge-Ops simulated end-to-end test.

Builds a fake Swiss seed-stage company, then generates the artifacts each of the
four skills would produce, applying their documented rules. A verification pass
checks the artifacts for internal consistency, schema compliance, the no-em-dash
rule, and the bidirectional knowledge-custodian <-> functional-hr-ops contract.

Run: python3 build_sim.py
"""
import os, json, re, hashlib, textwrap, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
CO = os.path.join(ROOT, "company-Helvetia-Robotics")
DOCS = os.path.join(CO, "Documents")
FOS = os.path.join(CO, "founder-os-outputs")          # simulated linked founder-os /outputs
ART = os.path.join(CO, "artifacts")
DR = os.path.join(ART, "data-room")                    # dataroom-ops canonical tree

def w(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(content)

def touch(path, content="x"):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(content)

# Canonical data room structure (mirrors .knowledge-ops-config.yml dataroom.canonical_structure)
CANONICAL = [
    "00_Overview","01_Corporate_&_Governance","02_Financials","03_Legal_&_Compliance",
    "04_IP_Data_&_Security","05_Team_&_HR","06_Product_&_Technology","07_Market_&_Commercial",
    "08_Cap_Table_&_Financing","09_Traction_&_Metrics","99_DD_QA_&_Trackers",
]

# Helvetia Robotics: warehouse robotics with AI picking -> combined hardware + ai overlays
COMPANY_TYPE = ["hardware", "ai"]
OVERLAYS = {
    "saas": ["06_Product_&_Technology/Multi-tenancy_&_Architecture","06_Product_&_Technology/SLA_&_Uptime",
             "04_IP_Data_&_Security/SOC2_ISO","04_IP_Data_&_Security/Data_Processing_&_Subprocessors",
             "09_Traction_&_Metrics/SaaS_Metrics"],
    "hardware": ["06_Product_&_Technology/BOM_&_Suppliers","06_Product_&_Technology/Manufacturing_&_CM",
                 "06_Product_&_Technology/Hardware_QA_&_Testing","06_Product_&_Technology/Certifications",
                 "04_IP_Data_&_Security/Patents_&_FTO","02_Financials/Inventory_&_COGS"],
    "crypto": ["03_Legal_&_Compliance/Token_Legal_Opinion","03_Legal_&_Compliance/Regulatory_MiCA_FINMA",
               "04_IP_Data_&_Security/Smart_Contract_Audits","04_IP_Data_&_Security/Custody_&_Key_Management",
               "08_Cap_Table_&_Financing/Tokenomics_&_Token_Cap_Table","02_Financials/Treasury_On-chain"],
    "fintech": ["03_Legal_&_Compliance/Licenses_&_Authorizations","03_Legal_&_Compliance/Regulatory_Compliance",
                "03_Legal_&_Compliance/Banking_Partners","03_Legal_&_Compliance/Client_Funds_Safeguarding",
                "04_IP_Data_&_Security/AML_KYC"],
    "ai": ["06_Product_&_Technology/Models_&_Training_Data","06_Product_&_Technology/MLOps_&_Evaluation",
           "04_IP_Data_&_Security/Data_Rights_&_Licensing","04_IP_Data_&_Security/Model_Governance_&_Safety",
           "04_IP_Data_&_Security/AI_Regulatory","03_Legal_&_Compliance/Third-party_Models_&_APIs"],
}

# ---------------------------------------------------------------------------
# 1. SIMULATED INPUT: a messy company filesystem
# ---------------------------------------------------------------------------
def build_inputs():
    # Messy Documents: duplicates, bad names, orphans, a siloed marketing asset
    touch(os.path.join(DOCS, "Pitch Deck FINAL v3.pdf"), "deck v3 content")
    touch(os.path.join(DOCS, "Pitch Deck FINAL v2.pdf"), "deck v2 content")     # near-dup (older)
    touch(os.path.join(DOCS, "misc", "cap table.xlsx"), "cap,table,data")        # misfiled
    touch(os.path.join(DOCS, "misc", "asdf.docx"), "untitled junk")              # orphan / bad name
    touch(os.path.join(DOCS, "Downloads_dump", "RoboPick_hero_render_FINAL.png"), "DESIGNASSET-BYTES")  # marketing design asset, siloed
    touch(os.path.join(DOCS, "financials", "2025 budget.xlsx"), "IDENTICAL-BUDGET-BYTES")
    touch(os.path.join(DOCS, "financials", "2025 budget copy.xlsx"), "IDENTICAL-BUDGET-BYTES")  # EXACT duplicate (same bytes)
    touch(os.path.join(DOCS, "a", "b", "c", "d", "deep notes.txt"), "too deep")  # deep nesting
    touch(os.path.join(DOCS, "Logo_final_REAL.png"), "logo")                     # naming violation, loose

    # Simulated founder-os deliverables (final, for dataroom Sync)
    for name, body, ver in [
        ("pitch-deck.md", "# RoboPick Pitch", "1.2"),
        ("market-report.md", "# Warehouse Robotics Market", "1.0"),
        ("business-model.md", "# Business Model", "1.1"),
        ("financial-model.md", "# 3-year Plan and Budget", "2.0"),
        ("metrics-dashboard.md", "# KPIs and Traction", "1.0"),
    ]:
        w(os.path.join(FOS, "outputs", name), f"{body}\n\nversion: {ver}\nsource_skill: founder-os\n")

def file_index(base):
    idx = []
    for dp, _, fns in os.walk(base):
        for fn in fns:
            p = os.path.join(dp, fn)
            b = open(p, "rb").read()
            idx.append({
                "path": os.path.relpath(p, CO),
                "size": len(b),
                "sha256": hashlib.sha256(b).hexdigest(),
                "depth": os.path.relpath(p, DOCS).count(os.sep) if p.startswith(DOCS) else 0,
            })
    return idx

# ---------------------------------------------------------------------------
# 2. knowledge-custodian artifacts
# ---------------------------------------------------------------------------
def kc_artifacts():
    idx = file_index(DOCS)
    # scan-index.json (the incremental cache, metadata only)
    w(os.path.join(ART, "knowledge-custodian", "_snapshots", "scan-index.json"),
      json.dumps({"generated": "2026-06-02", "scope_root": "company-Helvetia-Robotics/Documents",
                  "items": idx}, indent=2))

    # detect exact duplicates by hash
    by_hash = {}
    for it in idx:
        by_hash.setdefault(it["sha256"], []).append(it["path"])
    dups = {h: ps for h, ps in by_hash.items() if len(ps) > 1}

    scan = ["# knowledge-custodian - Scan report", "",
            "Company: Helvetia Robotics AG   Provider: local filesystem   Mode: Scan (read-only)", "",
            f"Items inventoried: {len(idx)}", "",
            "## Hotspots", "",
            "- Deep nesting: Documents/a/b/c/d/deep notes.txt (depth 4)",
            "- Loose files in root and Downloads_dump (no clear home)",
            "- Naming violations: spaces and ad hoc markers (Pitch Deck FINAL v3, Logo_final_REAL, asdf.docx)", "",
            "## Exact duplicates (proven by SHA-256)", ""]
    for h, ps in dups.items():
        scan.append(f"- hash {h[:12]}: " + ", ".join(ps))
    scan += ["", "## Near-duplicates (flagged for human judgment, never auto-merged)", "",
             "- Pitch Deck FINAL v3.pdf vs Pitch Deck FINAL v2.pdf (same intent, different bytes; v2 likely superseded)", "",
             "Scan changed nothing."]
    w(os.path.join(ART, "knowledge-custodian", "scan-report.md"), "\n".join(scan))

    # Advise action plan (replayable, dry-run) - JSON schema from advise-protocol.md
    arch = os.path.join("Documents", "_archive", "2026-06-02T1500")
    plan = {
        "plan_version": "1",
        "generated": "2026-06-02T15:00:00Z",
        "scope_root": "company-Helvetia-Robotics/Documents",
        "archive_root": "company-Helvetia-Robotics/Documents/_archive",
        "batches": [
            {"id": "b1", "label": "Archive exact duplicate budget", "requires_confirmation": False,
             "operations": [
                {"op": "archive",
                 "source": "Documents/financials/2025 budget copy.xlsx",
                 "destination": f"{arch}/financials/2025 budget copy.xlsx",
                 "reason": "exact_duplicate_of:Documents/financials/2025 budget.xlsx",
                 "reverse": {"op": "move", "source": f"{arch}/financials/2025 budget copy.xlsx",
                             "destination": "Documents/financials/2025 budget copy.xlsx"},
                 "provider": "local", "sensitivity_note": "confidential"}]},
            {"id": "b2", "label": "Refile misfiled and siloed assets", "requires_confirmation": False,
             "operations": [
                {"op": "move",
                 "source": "Documents/misc/cap table.xlsx",
                 "destination": "Documents/08_Cap_Table/cap_table.xlsx",
                 "reason": "misfiled: cap table belongs in 08_Cap_Table",
                 "reverse": {"op": "move", "source": "Documents/08_Cap_Table/cap_table.xlsx",
                             "destination": "Documents/misc/cap table.xlsx"},
                 "provider": "local", "sensitivity_note": "restricted"},
                {"op": "move",
                 "source": "Documents/Downloads_dump/RoboPick_hero_render_FINAL.png",
                 "destination": "Documents/marketing/design/RoboPick_hero_render.png",
                 "reason": "siloed marketing design asset; Organization-Model maps Marketing/Design -> marketing/design/",
                 "reverse": {"op": "move", "source": "Documents/marketing/design/RoboPick_hero_render.png",
                             "destination": "Documents/Downloads_dump/RoboPick_hero_render_FINAL.png"},
                 "provider": "local", "sensitivity_note": None}]},
        ],
    }
    w(os.path.join(ART, "knowledge-custodian", "advise-action-plan.json"), json.dumps(plan, indent=2))

    advise = ["# knowledge-custodian - Advise report", "",
        "Read-only. Two artifacts: this report and advise-action-plan.json (dry-run). Nothing was changed.", "",
        "## High priority", "",
        "- Exact duplicate: financials/2025 budget copy.xlsx duplicates 2025 budget.xlsx. Action: archive the copy (never delete).",
        "- Restricted file loose: misc/cap table.xlsx (PII/cap data) is misfiled. Action: move to 08_Cap_Table.", "",
        "## Medium priority", "",
        "- Siloed design asset: Downloads_dump/RoboPick_hero_render_FINAL.png. Action: move under marketing/design/ per the Organization Model.",
        "- Naming violations: 'Pitch Deck FINAL v3.pdf', 'Logo_final_REAL.png', 'asdf.docx'. Action: rename to the standard.", "",
        "## Low priority", "",
        "- Deep nesting Documents/a/b/c/d. Action: flatten.", "",
        "Applying the plan is Execute mode (v1.1). In v1.0 this is advice only."]
    w(os.path.join(ART, "knowledge-custodian", "advise-report.md"), "\n".join(advise))

    std = ["# File-Organization-Standard (Helvetia Robotics) - v1", "",
        "Derived from observed good patterns plus best practice. Baseline template: function-first.", "",
        "## Naming conventions", "",
        "- Lowercase, hyphen or underscore separators, no spaces.",
        "- ISO dates YYYY-MM-DD. Explicit version suffix -vN, never final_REAL.", "",
        "## Folder taxonomy (company)", "",
        "Top level by functional area, mirroring the Organization Model: product, engineering, marketing (with design), sales, finance, people, legal, and a referenced data room area (owned by dataroom-ops).", "",
        "## Active vs archive", "",
        "- Superseded material moves to _archive/<timestamp>/, never deleted.", "",
        "Version 1. 2026-06-02."]
    w(os.path.join(ART, "knowledge-custodian", "File-Organization-Standard.md"), "\n".join(std))

    arch_map = ["# knowledge-custodian - Architect inferred functional map", "",
        "Read-only. De-facto structure inferred from the file topology (hypothesis, not fact).", "",
        "## Inferred functional areas (with evidence, confidence)", "",
        "- Product and design: pitch deck and RoboPick render edited by 2 people. Confidence: medium.",
        "- Engineering: largest edit cluster, 5 editors. Confidence: high.",
        "- Finance and ops: one shared drive area, 2 editors. Confidence: medium (likely one de-facto unit).", "",
        "## Frictions", "",
        "- Silo: marketing design asset trapped in a personal Downloads dump.",
        "- Cross-team duplication: two budget files (exact duplicate).",
        "- Single-person bottleneck: cap table held by one editor.", "",
        "## Handoff notes to functional-hr-ops", "",
        "- Finance and ops operate as one de-facto unit today; confirm intended structure.",
        "- Design capacity is thin (shared with product); possible hiring signal.", "",
        "If Organization-Model.md exists, it takes precedence over this inferred map."]
    w(os.path.join(ART, "knowledge-custodian", "architect-inferred-map.md"), "\n".join(arch_map))
    return dups

# ---------------------------------------------------------------------------
# 3. functional-hr-ops artifacts
# ---------------------------------------------------------------------------
def hr_artifacts():
    om = """# Organization Model - Helvetia Robotics AG

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

## Information-architecture mapping (for knowledge-custodian)
- Product & Design -> product/ and marketing/design/ (shared design assets under marketing/design/)
- Engineering -> engineering/
- Go-to-Market -> sales/ and marketing/
- Operations & Finance -> finance/ and people/
- Shared spaces: company/ for all-hands material
- Ownership: every active area maps to exactly one owning team
"""
    w(os.path.join(ART, "functional-hr-ops", "Organization-Model.md"), om)

    workforce = """# functional-hr-ops - Workforce plan (seed, runway-aware)

## Gap analysis (target vs today)
- Design capacity thin: shared inside Product & Design (2 people cover product + design). Gap: dedicated design.
- Cap-table / finance bottleneck: one person holds finance knowledge (key-person risk).

## Needs (honest, scoped)
- Senior Backend Engineer: blocks the scaling roadmap (3 features stalled on platform work). Real, scoped.
- Product Designer: design is a bottleneck; currently a shared, fractional concern.

## Options per gap
- Senior Backend Engineer: HIRE (senior, specialist). Build not viable, no internal candidate. Time-to-impact 8-12 weeks.
- Product Designer: HIRE (mid) OR contract first to validate volume. Recommend contract-to-hire.
- Finance bottleneck: REASSIGN + document (distribute knowledge) before hiring.

## Sequence (dependency + runway)
1. Senior Backend Engineer (unblocks roadmap; check affordability vs runway: flagged, unverified).
2. Product Designer (contract first).
Hold further hires until next raise.
"""
    w(os.path.join(ART, "functional-hr-ops", "workforce-plan.md"), workforce)

    hiring = """# functional-hr-ops - Hiring kit: Senior Backend Engineer

## Role definition
Mission: own the platform layer so stream-aligned teams ship without blocking.
First 6-12 months outcomes: stable service interfaces, halved deploy friction.
Level: senior. Reports: Eng Lead (vertical). Not responsible for: product priorities, pricing.

## Job description (excerpt)
We are Helvetia Robotics, building RoboPick for warehouse automation. You will own our platform layer.
Must-have: distributed systems, strong API design, mentoring. Nice-to-have: robotics, Rust.
Level senior; compensation band [SET BY FOUNDER]; Zurich hybrid or Remote-EU.

## Scorecard (what good looks like)
- Platform reliability: designs clean service interfaces (evidence: past systems, design exercise).
- Delivery: ships and unblocks others (evidence: references, take-home review).
- Mentoring: raises the team (evidence: structured interview).

## Interview plan
1. Screen (Eng Lead): motivation, level fit.
2. Technical (2 engineers): system design mapped to platform reliability.
3. Team/values (cross-team): collaboration.
4. Founder: mission and trajectory.

## Candidate prospectus (sent to candidates)
Helvetia Robotics, seed-stage Swiss robotics. You will be employee ~6 and define our platform.
Impact: your work unblocks every product team. Team: 5 engineers, Zurich + Remote-EU.
Stage and trajectory: seed, raising Series A in ~12 months. Comp framed at hire.
First-year success: a platform the team builds on without friction. Honest challenge: early-stage ambiguity, you set the standards.
"""
    w(os.path.join(ART, "functional-hr-ops", "hiring-Senior-Backend-Engineer.md"), hiring)

    rollout = """# functional-hr-ops - Org Rollout roadmap

Transition: from a flat de-facto setup (finance and ops fused, design fractional) to the target Organization Model.

## Phase 1 - Pilot (weeks 1-3)
Entry: model agreed, owners named.
Moves: formalize Engineering as a stream-aligned team with the Eng Lead; set the weekly release cadence and interaction modes.
Deliverable: working pilot + learnings.

## Phase 2 - Scale (weeks 4-8)
Moves: stand up Product & Design and GTM with owners; split Operations & Finance ownership; onboard Senior Backend Engineer (dependency: hire first).
Deliverable: full target structure in place.

## Phase 3 - Optimize (weeks 9-12)
Moves: tune interfaces and rituals against metrics; document finance knowledge to remove the bottleneck.
Deliverable: stabilized org, updated Organization Model.

## Success metrics (baseline -> target)
- Team health score: baseline TBD -> >=4/5 by week 12.
- Cycle time: baseline 9 days -> <=5 days.
- Blocking cross-team dependencies: baseline 4 -> <=1.
- Deployment frequency: baseline weekly -> 2x/week.

## Communication and risk
- Comms: leadership, then teams, then all-hands.
- Risk: key-person flight (finance) -> mitigate by documenting before any change. Personnel-sensitive steps flagged for counsel.
"""
    w(os.path.join(ART, "functional-hr-ops", "org-rollout.md"), rollout)

# ---------------------------------------------------------------------------
# 4. dataroom-ops artifacts
# ---------------------------------------------------------------------------
def dataroom_artifacts():
    # Bootstrap: canonical folder tree with a .gitkeep-like marker
    for folder in CANONICAL:
        touch(os.path.join(DR, folder, "_index.md"), f"# {folder}\n")
    # 99 trackers placeholders (created by Bootstrap for diligence-ops)
    for sub in ["QA_Tracker", "Evidence_Index", "Access_Log"]:
        touch(os.path.join(DR, "99_DD_QA_&_Trackers", sub, "_placeholder.md"), f"# {sub}\n")
    # Sector overlays (additive over base) for this company's company_type
    overlay_subs = []
    for t in COMPANY_TYPE:
        for sub in OVERLAYS[t]:
            touch(os.path.join(DR, sub, "_index.md"), f"# {sub} (overlay: {t})\n")
            overlay_subs.append(sub)

    index = ["# Helvetia Robotics - Data Room (canonical)", "",
        f"Platform: local (simulated). Stage profile: seed. Sector overlays: {', '.join(COMPANY_TYPE)}. Last synced: 2026-06-02.", "",
        "## Base folders (SICTIC / venture-CH)"] + [f"- {f}" for f in CANONICAL] + \
        ["", "## Overlay subfolders (additive)"] + [f"- {s}" for s in overlay_subs]
    w(os.path.join(DR, "index.md"), "\n".join(index))

    sync = """# dataroom-ops - Sync manifest

Source: linked founder-os repo (company-Helvetia-Robotics/founder-os-outputs/outputs). Mode: hybrid (index all, copy finals).

## Added (finals copied, metadata stamped)
- pitch-deck.md -> 00_Overview | audience investor | lens commercial | version 1.2 | source_skill founder-os | sensitivity public
- financial-model.md -> 02_Financials | audience investor | lens finance | version 2.0 | source_skill founder-os | sensitivity confidential
- market-report.md -> 07_Market_&_Commercial | lens commercial | version 1.0 | sensitivity confidential
- business-model.md -> 00_Overview | lens commercial | version 1.1 | sensitivity confidential
- metrics-dashboard.md -> 09_Traction_&_Metrics | lens commercial | version 1.0 | sensitivity confidential

## Indexed (referenced, not copied)
- (none this run; all sources were finals)

## Archived (superseded)
- (none this run)

## Skipped / Flagged
- (none)
"""
    w(os.path.join(ART, "data-room", "sync-manifest.md"), sync)

    audit = """# dataroom-ops - Audit report (yardstick: seed / SICTIC + hardware, ai overlays)

## Gaps (vs seed profile)
- BLOCKER: 04_IP_Data_&_Security empty - IP ownership / assignment chain missing (SICTIC requires this at seed).
- BLOCKER: 08_Cap_Table_&_Financing empty - cap table not in the room (exists in Documents/misc, route to Sync after refile).
- SHOULD-FIX: 05_Team_&_HR thin - founder bios only.

## Gaps (vs sector overlays)
- hardware: BOM_&_Suppliers and Certifications empty - no bill of materials or CE/UL status yet.
- hardware: Patents_&_FTO empty - freedom-to-operate not documented.
- ai: Models_&_Training_Data and Data_Rights_&_Licensing empty - training-data provenance/licenses missing.
- ai: AI_Regulatory empty - EU AI Act risk classification not done.

## Stale
- (none; data room freshly synced)

## Version conflicts / near-duplicates
- (none in the room)

## Sensitivity sanity
- All synced items tagged. Note: cap table is restricted; keep out of investor view by default.

Readiness: seed-ready except 2 blockers (IP assignment, cap table). Route both to dataroom-ops Sync / Founder-OS.
"""
    w(os.path.join(ART, "data-room", "audit-report.md"), audit)

# ---------------------------------------------------------------------------
# 5. diligence-ops artifacts
# ---------------------------------------------------------------------------
def diligence_artifacts():
    readiness = """# diligence-ops - Fundraise Data Room Prep (stage: seed, profile: SICTIC)

Readiness is stated relative to the named checklist (SICTIC seed).

## Scorecard (SICTIC sections)
1. Business and product overview (00_Overview): PRESENT (deck, BMC).
2. Company / corporate (01): THIN (incorporation present, statutes missing).
3. Team (05): THIN.
4. Financial situation (02): PRESENT (plan, budget, burn).
5. Customers / traction (07, 09): PRESENT.
6. IP, data protection, security (04): MISSING -> BLOCKER (route to dataroom-ops / Founder-OS).
7. Software development and production (06): THIN.

## Access view (investor, NDA)
- Included: public + confidential items.
- Hard-blocked: restricted (cap table detail, any PII). Override requires logged reason.

Verdict: seed-ready except 1 blocker (IP ownership) and 2 thin areas (statutes, team).
"""
    w(os.path.join(ART, "diligence-ops", "seed-readiness-SICTIC.md"), readiness)

    qa = """# diligence-ops - Due Diligence Q&A tracker

| id | area | question | status | evidence (folder | item | version) | sensitivity | owner |
|----|------|----------|--------|------------------|------|---------|-------------|-------|
| 1 | financial | 3-year plan and budget? | answered | 02_Financials | financial-model.md | 2.0 | confidential | COO |
| 2 | legal | Who owns the IP, contractor assignment? | missing | 04 | (none) | restricted | CEO |
| 3 | corporate | Cap table and SHA? | partial | 08 | cap_table.xlsx (pending sync) | restricted | CEO |
| 4 | commercial | Market size and pipeline? | answered | 07_Market_&_Commercial | market-report.md | 1.0 | confidential | Commercial Lead |

Snapshot: financial DD answered; legal DD blocked on IP assignment (routed to dataroom-ops / Founder-OS). Restricted evidence hard-blocked from the investor view.
"""
    w(os.path.join(ART, "diligence-ops", "dd-qa-tracker.md"), qa)

    access = """# diligence-ops - Access log

| recipient | org | process | granted | sensitivity | NDA | overrides | when | authorized_by |
|-----------|-----|---------|---------|-------------|-----|-----------|------|---------------|
| Jane Doe | Alpha Ventures | seed round | view: 00,02,07,09 | confidential | yes | none | 2026-06-02 | CEO |

No restricted item disclosed. Cap table (restricted) withheld pending explicit, logged override.
"""
    w(os.path.join(ART, "diligence-ops", "access-log.md"), access)

# ---------------------------------------------------------------------------
# VERIFICATION
# ---------------------------------------------------------------------------
def verify(dups):
    results = []
    def check(name, ok, detail=""):
        results.append((name, ok, detail))

    # 1. action plan parses, only move/archive, every op has reverse, no delete verb
    planp = os.path.join(ART, "knowledge-custodian", "advise-action-plan.json")
    plan = json.load(open(planp))
    ops = [o for b in plan["batches"] for o in b["operations"]]
    verbs = {o["op"] for o in ops}
    check("action-plan: valid JSON", True, f"{len(ops)} ops")
    check("action-plan: only move/archive verbs (no delete)", verbs <= {"move", "archive"}, str(verbs))
    check("action-plan: every op has a reverse", all("reverse" in o for o in ops))
    check("action-plan: reverses are move-back (reversible)", all(o["reverse"]["op"] == "move" for o in ops))

    # 2. exact duplicate really detected by identical bytes
    check("dedup: exact duplicate found by hash", any(len(ps) > 1 for ps in dups.values()),
          "; ".join(",".join(p.split('/')[-1] for p in ps) for ps in dups.values() if len(ps) > 1))

    # 3. Organization-Model has required schema sections
    om = open(os.path.join(ART, "functional-hr-ops", "Organization-Model.md")).read()
    required = ["## Functional structure", "## Roles", "not_responsible_for", "## RACI decision matrix",
                "vertical_line", "## Information-architecture mapping", "scale_tier", "size_band"]
    missing = [s for s in required if s not in om]
    check("org-model: all required schema sections present", not missing, f"missing: {missing}")

    # 4. RACI: exactly one Accountable per decision line
    raci_lines = [l for l in om.splitlines() if l.strip().startswith("- ") and "Accountable:" in l]
    one_acc = all(l.count("Accountable:") == 1 for l in raci_lines)
    check("org-model: RACI has exactly one Accountable per decision", one_acc and len(raci_lines) >= 3,
          f"{len(raci_lines)} decisions")

    # 5. bidirectional placement consistency:
    #    org model maps Marketing/Design -> marketing/design/, and the advise plan moves the siloed
    #    design asset into marketing/design/. They must agree.
    maps_design = "marketing/design/" in om
    plan_moves_design = any("marketing/design/" in o.get("destination", "") for o in ops)
    check("bidirectional: org-model placement and advise plan agree (marketing/design/)",
          maps_design and plan_moves_design)

    # 6. data room canonical folders exactly match config list
    present = sorted(d for d in os.listdir(DR) if os.path.isdir(os.path.join(DR, d)))
    check("dataroom: canonical folders match config", present == sorted(CANONICAL),
          f"{len(present)} folders")

    # 6b. sector overlays applied additively over the base (hardware + ai), base intact
    expected_overlay = []
    for t in COMPANY_TYPE:
        expected_overlay += OVERLAYS[t]
    overlay_ok = all(os.path.isdir(os.path.join(DR, s)) for s in expected_overlay)
    base_intact = all(os.path.isdir(os.path.join(DR, b)) for b in CANONICAL)
    check("dataroom: sector overlays (hardware+ai) applied additively, base intact",
          overlay_ok and base_intact, f"{len(expected_overlay)} overlay subfolders over {len(CANONICAL)} base")

    # 7. trackers placeholders exist for diligence-ops handoff
    trackers = os.path.join(DR, "99_DD_QA_&_Trackers")
    check("dataroom: 99 trackers scaffolded for diligence-ops",
          all(os.path.isdir(os.path.join(trackers, s)) for s in ["QA_Tracker", "Evidence_Index", "Access_Log"]))

    # 8. diligence readiness names the stage/checklist
    rd = open(os.path.join(ART, "diligence-ops", "seed-readiness-SICTIC.md")).read()
    check("diligence: readiness names the stage and checklist (seed / SICTIC)",
          "seed" in rd.lower() and "SICTIC" in rd)

    # 9. diligence hard-block: restricted not in the granted access view
    al = open(os.path.join(ART, "diligence-ops", "access-log.md")).read()
    check("diligence: no restricted item disclosed in access log",
          "No restricted item disclosed" in al)

    # 10. no em dashes in any generated artifact
    bad = []
    for dp, _, fns in os.walk(ART):
        for fn in fns:
            if fn.endswith((".md", ".json")):
                if "—" in open(os.path.join(dp, fn), encoding="utf-8").read():
                    bad.append(os.path.relpath(os.path.join(dp, fn), ART))
    check("style: no em dashes in any artifact", not bad, f"offenders: {bad}")

    return results

def main():
    build_inputs()
    dups = kc_artifacts()
    hr_artifacts()
    dataroom_artifacts()
    diligence_artifacts()
    results = verify(dups)

    lines = ["# Knowledge-Ops simulated test - VERIFICATION", "",
             "Company: Helvetia Robotics AG (Swiss, seed). Generated artifacts for all four skills.", "",
             "| # | check | result | detail |", "|---|-------|--------|--------|"]
    npass = 0
    for i, (name, ok, detail) in enumerate(results, 1):
        lines.append(f"| {i} | {name} | {'PASS' if ok else 'FAIL'} | {detail} |")
        npass += ok
    lines += ["", f"**{npass}/{len(results)} checks passed.**"]
    w(os.path.join(ROOT, "VERIFICATION.md"), "\n".join(lines))

    print("\n".join(lines))
    print("\nArtifacts under:", os.path.relpath(ART, ROOT))
    sys.exit(0 if npass == len(results) else 1)

if __name__ == "__main__":
    main()
