# Investor Sourcing and Outreach (investor-ops Family 2)

Getting the money in: build the target list, score fit, run outreach, track the raise as a pipeline. Grounded in real sources, materials pulled from Founder-OS, every touch logged. No em dashes anywhere. No bare URLs.

---

## Config block (`.exec-os-config.yml`)

```yaml
outreach:
  crm_location: "10_Fundraise/Investor_Pipeline"   # where the living tracker lives in the data room
  sources:                                         # where the investor list is built from
    - warm_network        # the founder's own contacts and prior-round investors (highest priority)
    - directories         # VC and angel directories, syndicate lists
    - funding_maps        # ecosystem funding maps (e.g. Swiss venture / crypto maps)
    - portfolio_signals   # funds active in comparable companies
    - accelerators        # relevant programs and their investor networks
  pipeline_stages: [Researched, Contacted, Replied, Meeting, Diligence, Term Sheet, Closed, Passed]
  fit_weights:            # sum to 100; tune per raise
    stage_match: 25
    sector_match: 20
    check_size_match: 15
    geography: 10
    portfolio_fit: 10
    value_add: 10
    warm_path: 10
  update_cadence: monthly # prospect nurture cadence: weekly | biweekly | monthly | off
  daily_send_cap: 15      # anti-spam guardrail: max new cold contacts per day
```

If the block is absent, use these defaults and note it once.

---

## 1. Investor List

Build one living **investor tracker** for the target company's stage, sector, geography, and round size. Draw from `outreach.sources`, warm network first. Research each candidate from real, citable sources; never fabricate a thesis or a check size.

Tracker columns (one row per investor):

| Column | Content |
| --- | --- |
| Investor | Person or firm name |
| Firm / vehicle | Fund, syndicate, angel, family office, strategic, grant body |
| Type | VC / Angel / Family office / Strategic / Grant |
| Stage focus | Pre-seed / Seed / A / B ... |
| Sector focus | The theses that match (or note mismatch) |
| Geography | Where they invest |
| Check size | Typical ticket range |
| Thesis / notes | Why they might care about this company |
| Portfolio / conflicts | Relevant portfolio, plus any direct competitor they back |
| Warm path | Named intro route, or "cold" if none |
| Source | Where this row came from (directory, map, warm contact, research) |
| Fit score | From section 2 (filled by Fit & Scoring) |
| Stage (pipeline) | From section 3 |
| Next action + date | The single next step and when |

Flag unknown fields as `unknown` rather than guessing. Cite the source for every non-obvious fact.

---

## 2. Fit & Scoring

Score each investor 0 to 100 using `outreach.fit_weights`. For each factor, rate 0 to 1 and multiply by its weight:

- **stage_match:** do they lead or follow at this company's stage.
- **sector_match:** does the company sit inside a stated thesis.
- **check_size_match:** does their typical ticket fit the round and the ask.
- **geography:** do they invest in this jurisdiction.
- **portfolio_fit:** adjacent portfolio helps; a direct competitor is a hard conflict (set to 0 and flag).
- **value_add:** relevant operational help, network, follow-on capacity.
- **warm_path:** strength of the intro route (warm named intro high, second-degree medium, cold low).

Output a ranked shortlist: investor, score, a one-line "why", and the recommended path (always prefer a warm intro before a cold send). Group into Tier 1 (pursue now), Tier 2 (after Tier 1 signal), Tier 3 (park). Recommend running outreach in tiers, not all at once, so the pitch improves between batches.

---

## 3. Outreach & Pipeline (CRM)

**Materials come from Founder-OS.** Pull the current teaser, deck, and one-pager from `narrative-assets-ops`. Do not re-write them here; reference the canonical files and their versions. If a needed asset is missing, route to `narrative-assets-ops` rather than improvising.

**Drafting.** For each investor, draft the appropriate opener:
- Warm intro: a short forwardable blurb for the introducer, plus the follow-up to the investor once introduced.
- Cold: 4 to 6 sentences: one line of relevance (why them specifically, from their thesis), one line of traction, the ask, and the material link. Personalize the relevance line from the tracker, never send a generic blast.

**Cadence and guardrails.** Sequence sends and follow-ups (a common pattern: send, follow-up at day 4, second nudge at day 10, then stop). Respect `outreach.daily_send_cap` and normal consent and anti-spam norms. One thread per investor.

**Pipeline.** Maintain the tracker in `outreach.crm_location`, moving each investor through `outreach.pipeline_stages`:

`Researched -> Contacted -> Replied -> Meeting -> Diligence -> Term Sheet -> Closed | Passed`

Log every interaction (date, channel, summary, sentiment) and set the next action. When an investor reaches Diligence, hand the data room work to Family 3 (Fundraise Prep and DD Support). When they reach Term Sheet, involve `corporate-legal` (Founder-OS) for the legal documents.

**Pipeline snapshot** (deliver on each update): count by stage, conversion between stages, this-week actions, and stale contacts (no touch past the cadence) to nudge or close.

---

## 4. Prospect Updates

Short, honest nurture updates to warm-but-not-closed investors on `outreach.update_cadence`. Content: traction since last touch, notable momentum, round status and remaining allocation, one clear ask. Keep to a screen. Log the send in the tracker.

For investors who have already invested, do not use this: switch to Family 3 Board and Investor Delivery, which is examination-grade and pulls from the metrics dashboard.

---

## Boundaries

- **Never fabricate investor data.** Thesis, check size, and portfolio are researched and cited, or marked `unknown`.
- **Never re-write pitch materials here.** They belong to `narrative-assets-ops`.
- **Never send restricted internal detail** in outreach. Outreach uses public and confidential-with-NDA materials only, per the sensitivity tiers.
- **Legal documents (term sheet, SAFE, SHA)** are `corporate-legal` in Founder-OS, not here.
