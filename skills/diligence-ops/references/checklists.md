# Built-in checklists

These ship with the skill so it can proactively tell you what an examiner will expect, per stage and per framework. They are calibrated on real Swiss venture references and mapped to the canonical data room folders (00 to 99) in `dataroom-ops/references/canonical-structure.md`. Use the checklist as the yardstick; when an item is present in the room, mark it; when missing, route the request to dataroom-ops.

A heavier stage is a superset of a lighter one. Always state readiness relative to the named checklist.

**Gap detection defers to dataroom-ops Audit.** These checklists are the shared yardstick, but the authoritative gap list comes from running dataroom-ops Audit against the stage. diligence-ops consumes that punch-list and adds audience and sensitivity on top, rather than recomputing which items are missing. Use the checklist directly only when no Audit is available. This prevents the library and the delivery counter from disagreeing on completeness.

## Seed / angel (SICTIC-grade)

Source pattern: SICTIC / Swiss ICT Investor Club and the Swiss Angel Investor Handbook. Light depth, but the cap table and the IP ownership chain must be airtight.

1. **Business and product overview** -> 00_Overview. Pitch deck, business model canvas, one-pager, the ask.
2. **Company** -> 01_Corporate. Corporation (incorporation, statutes, register extract), shareholders (cap table, evolution, investment policy), tax and legal basics, key risks.
3. **Team** -> 05_Team. Founders and key people, roles, commitment, gaps.
4. **Financial situation** -> 02_Financials. 3-5 year plan, annual budget, burn and runway, basic bookkeeping, financing need for the next 24 months.
5. **Customers** -> 07_Market_&_Commercial and 09_Traction. Traction, pipeline, references.
6. **IP, data protection and security** -> 04_IP_Data_&_Security. Who owns the IP, contractor assignment, freedom to operate, data protection (Swiss FADP / GDPR), security basics.
7. **Software development and production** -> 06_Product_&_Technology. Product, stack, how it is built and shipped.

Innosuisse-style screening adds emphasis on innovation substance, scientific/technical merit, and the team's capacity to execute; map these to 06_Product and 05_Team.

## Governance / board (Startup Board Academy-grade)

Source pattern: the Startup Board Academy DD list (bilingual FR/EN). Used for board due diligence and ongoing governance, not only a raise.

1. **Shareholder information and governance** -> 01_Corporate. Shareholder alignment and exit expectations, ownership structure and cap table, shareholders' agreements (SHA) vs org rules, board structure and type, board operation, dynamics, evolution, impact, delegation to management, chair and secretary, strategy documentation and follow-up.
2. **Financials and financing** -> 02_Financials. Plan and budget, investment/financing plan, frequency of financial statements, monthly cash-flow plan, burn rate, basic bookkeeping. Compliance: audit of accounts, bank signatories and approval policy, HR legal framework (timesheets, overtime, vacations, minimum salaries), social charges and tax-at-source proof, VAT status, proactive tax management, regulatory red flags.
3. **Legal** -> 03_Legal_&_Compliance. Company structure and entities, litigation and disputes, conflicts of interest, D&O insurance, insurance status, IP ownership and assignment and freedom to operate, key contracts and main terms.
4. **Business** -> 07_Market_&_Commercial and 06_Product. Organisation and operations sizing, org chart, delegation.

(The full list extends into operations, customers, and risk; treat 1 to 4 as the governance core and expand per the received list.)

## Series A / B

Superset of seed plus governance. Expect depth on: full 01_Corporate (board minutes for 3 years, SHA, org rules, registers), full 02_Financials (historicals, monthly cash flow, audit where applicable), 03_Legal (litigation, insurance incl. D&O, regulatory, tax), 06_Product_&_Technology (engineering and QA practices, infra), 05_Team (ESOP, HR compliance), 08_Cap_Table (prior rounds, fully diluted), and a maintained Q&A tracker. Sensitivity discipline matters more: investors get `confidential`, not `restricted`.

## M&A / exit (Elysium-grade)

Source pattern: the Elysium Lab acquisition request list (corporate DD plus an engineering and infrastructure DD), with explicit data-room folder mapping and per-item priority. Expect line-item evidence requests.

Corporate request areas:

- **A. Corporate matters** -> 01_Corporate. Incorporation and governing docs, registers of directors/officers/stockholders and ownership percentages, jurisdictions of operation, board and committee minutes (3+ years), ownership/control agreements (SHA, voting trusts), option/incentive plans, prior acquisitions/mergers, related-party transactions, all prior and assumed names (5 years), investments in other entities, legal-entity org chart.
- **B. Litigation and contingencies** -> 03_Legal. Auditor management letters and audit-letter responses (5 years), pending litigation/arbitration/administrative proceedings, plaintiff/defendant status and counterclaims, status and damages, insurance coverage of claims, settled/adjudicated matters (3 years), contingent liabilities, product/service liability, warranty and recall programs and costs (5 years), liens and encumbrances.
- **C. Regulatory matters** -> 03_Legal and 04_Security. Licenses, regulatory filings, compliance posture.
- **D / E. Material contracts, assets, real estate, etc.** -> 03_Legal, 07_Commercial as applicable.

Engineering and infrastructure DD -> 06_Product_&_Technology:

- **EA General:** team size and structure (org chart), roles, experience and seniority mix, key-person dependencies, contractor vs employee ratio, locations, remote policy, retention/turnover.
- **EB Technical expertise:** core competencies, languages/frameworks/tools, experience with the stack, skill gaps, security-practice familiarity.
- **EC Development practices:** methodology, version control, CI/CD, code review, release frequency and process, specs, documentation, coding guidelines, bug/incident handling.
- **ED Quality and testing:** automated vs manual, test frameworks, test types and coverage, engineer-to-QA ratio, production-incident rate, security testing, compliance standards followed (ISO, SOC).

## Audit frameworks

Map controls to evidence already in the room; the Evidence Index in `99_DD_QA_&_Trackers` records which item and version satisfies each control.

- **Financial audit** -> 02_Financials. Financial statements, GL, reconciliations, revenue recognition, bank confirmations, auditor letters.
- **SOC 2** -> 06_Product, 04_Security, 03_Legal. Trust Services Criteria: security, availability, processing integrity, confidentiality, privacy. Access control, change management, monitoring, incident response, vendor management, HR/onboarding-offboarding.
- **ISO 27001** -> 04_Security, 06_Product. ISMS scope, risk assessment and treatment, Statement of Applicability, Annex A controls, policies, internal audit, management review.
- **GDPR / Swiss FADP** -> 04_IP_Data_&_Security, 03_Legal. Records of processing (ROPA), DPAs with processors, privacy notices, data subject request process, DPIAs, breach process, cross-border transfer basis, retention policy.

These are evidence-assembly maps, not legal opinions. diligence-ops assembles and flags; the formal opinion is a legal/compliance skill or counsel.
