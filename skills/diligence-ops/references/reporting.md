# Board and investor reporting

Generates board packs and investor letters from the data room and the Founder-OS metrics dashboard. On demand by default, with an optional recurring schedule. diligence-ops never re-derives metrics: it pulls them from the source and references it.

## Sources (pull, do not re-derive)

- **Metrics:** `09_Traction_&_Metrics` in the data room and the Founder-OS `metrics-aggregation-view` dashboard. Use the dashboard as the single source of the numbers; cite it.
- **Financials and runway:** `02_Financials` (management accounts, cash flow, burn).
- **Pipeline and commercial:** `07_Market_&_Commercial`.
- **Prior board minutes and agenda:** the company's `Board` area (or `01_Corporate/Board_Minutes`).

If a number is not in the room or the dashboard, do not invent it; flag it as missing and route to dataroom-ops or Founder-OS.

## Board pack template

A board pack is a deck plus a supporting bundle. Default sections:

1. **Cover and agenda.** Company, period, attendees, agenda, links to prior minutes.
2. **Highlights and lowlights.** 3 to 5 each, plain and honest.
3. **Metrics vs plan.** Headline KPIs from the dashboard, actual vs plan vs prior period, with one-line drivers.
4. **Financials and runway.** Cash position, burn, months of runway, budget variance.
5. **Commercial.** Pipeline, wins/losses, key customer movements.
6. **Product and team.** Shipped, next, hiring, key-person notes (no `restricted` HR detail unless the board owns it and it is logged).
7. **Risks and mitigations.** Top risks, owners, status.
8. **Asks and decisions sought.** Explicit decisions the board must make, each with options and a recommendation.
9. **Appendix.** Detailed tables, supporting docs, prior minutes.

Render to a deck (use the pptx skill), a doc/PDF (docx or pdf skill), or an HTML dashboard if `preferences.visual_artifact` allows. File the output and log distribution in the access log.

## Investor letter template

A monthly or quarterly narrative, shorter than a board pack:

1. **TL;DR.** The month in three lines.
2. **Metrics.** Headline numbers vs prior, from the dashboard.
3. **Wins.** What moved.
4. **Challenges.** What did not, honestly.
5. **Asks.** Intros, hires, help needed.
6. **Runway and plan.** Cash, burn, what the next period funds.

Investors get `confidential` at most; never `restricted`. Keep it candid and short.

## On-demand vs scheduled

- **On demand (default):** generate when asked, for the requested period.
- **Scheduled (optional):** if the user wants recurring reporting, register a scheduled task (monthly investor letter, quarterly board pack). Store the source pull and template so each run is reproducible and consistent. Each scheduled run still gates sensitivity and logs distribution.

If board/investor reporting later outgrows being a mode here (high volume, complex recurring cadence), it is the clean candidate to graduate into a dedicated `reporting-ops` skill; until then it lives in diligence-ops.

## Honesty bar

A board pack or investor letter that hides bad news is worse than useless: it destroys the trust the document exists to build. Report lowlights and risks plainly, ground every number in the cited source, and never dress up a metric the dashboard does not support.
