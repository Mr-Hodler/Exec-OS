# DD Q&A and evidence

This is the workflow for Due Diligence Support: turn a stream of questions into tracked, evidence-backed answers, without ever fabricating a fact or leaking restricted content.

## The Q&A tracker

Lives in `99_DD_QA_&_Trackers/QA_Tracker`. One row per question:

- **id** and **area** (legal / financial / tech / commercial / governance).
- **question** (verbatim as received, or from the built-in checklist).
- **lens** (finance, legal, product, commercial, governance, hr, ip).
- **status:** answered, partial, missing, or N/A.
- **evidence:** the data room item(s) and version that support the answer (folder + item + version).
- **answer_draft:** the drafted response, grounded in the evidence.
- **sensitivity:** the highest tier of the evidence referenced (drives gating).
- **owner:** who must close a partial/missing item.

## 1. Source the questions

Two paths, often combined:

- **Received questionnaire.** Ingest the investor's or acquirer's DD list (legal DD, financial DD, tech DD, commercial DD). Normalize each line into a tracker row, preserving the original wording.
- **Built-in checklist.** If no questionnaire yet, start from the stage checklist in `references/checklists.md` so you can pre-empt what will be asked.

Deduplicate overlapping questions across lists into one row with multiple sources.

## 2. Map each question to evidence

For each row, find the supporting item in the data room: folder, item, version. A clean cap-table question maps to `08_Cap_Table`; an IP-ownership question to `04_IP_Data_&_Security`; a churn question to `09_Traction`. Record the exact item and version so the answer is reproducible and so a later sync can flag staleness.

If the evidence exists in Founder-OS but not yet in the room, mark the row **missing** and route a Sync request to dataroom-ops. Do not answer from memory or assumption.

## 3. Status and draft

- **answered:** evidence present and sufficient; draft the answer citing the evidence item.
- **partial:** evidence thin or indirect; draft what is supported and state precisely what is missing.
- **missing:** no evidence; route to dataroom-ops (sync) or to the relevant Founder-OS skill (produce). Never bluff.
- **N/A:** not applicable; record the reason (for example "no subsidiaries", "pre-revenue so no churn").

Drafting rules: ground every claim in a cited evidence item; never assert a fact the room does not support; mark anything uncertain as "to confirm with founder" rather than stating it; keep answers concise and examiner-ready; no em dashes, no bare URLs.

## 4. Gate and log every disclosure

- Apply `references/packaging-and-access.md` to every piece of evidence before it is shared.
- `restricted` evidence is hard-blocked unless the user overrides that specific item with a logged reason.
- Record each disclosure in `99_DD_QA_&_Trackers/Access_Log` at the moment it is shared.

## 5. Evidence index

Maintain `99_DD_QA_&_Trackers/Evidence_Index`: a flat list of every evidence item referenced across the Q&A, with its folder, version, sensitivity, and which questions/controls it satisfies. This is what you reuse across an audit (same evidence, different framing) and what proves completeness.

## 6. Progress snapshot

Deliver a status readout on demand: counts of answered / partial / missing / N/A by area, the top blockers (high-priority questions still missing evidence), and the route to close each. State readiness relative to the named DD scope, for example: "Financial DD 90 percent answered, 2 blockers (audited accounts, monthly cash flow); tech DD 60 percent, evidence sync pending from dataroom-ops."
