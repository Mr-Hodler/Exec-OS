# Audit protocol

Audit is **read-only**. It measures the room against a named yardstick and produces a prioritized punch list. It applies nothing unless the user explicitly says "fix it", at which point fixes route back to Sync (for refresh) or to an archive move (for supersession). It never deletes.

## 1. Pick the yardstick

Completeness is meaningless in the abstract. Read the target **stage profile** from `diligence.stage_profiles`, or ask which stage to audit against (seed, series_a, ..., m_and_a). The stage decides which canonical folders and which depth are expected. See the per-stage subsets in `canonical-structure.md`.

## 2. Gap detection

- For each expected folder at the active stage, check presence and thinness. An empty `02_Financials/Cashflow_&_Burn` at Series A is a blocker; a thin `07_Partnerships` at seed is nice-to-have.
- Distinguish **missing** (no item) from **thin** (present but clearly incomplete: a cap table with no fully-diluted scenario, a financials folder with a plan but no historicals at a stage that needs them).
- Group findings by canonical folder and tag each with a suggested action: sync (it exists in Founder-OS, pull it), request (it does not exist yet, ask Founder-OS to produce it), or consolidate.

## 3. Stale detection

Flag items past their freshness window or lagging their source.

Freshness windows (default; tune per company):

- `09_Traction_&_Metrics` (KPIs, dashboard, unit economics): **30 days**.
- `02_Financials` (management accounts, cash flow, burn): **30-45 days**.
- `08_Cap_Table`: refresh on any change; flag if older than the latest financing event.
- `00_Overview` (pitch deck, one-pager): **90 days** or on any material change.
- `01_Corporate`, `03_Legal`, `04_IP`: event-driven; flag only if a known event (new round, new contract, new entity) postdates the file.

Also flag any room item whose `version` is behind the current Founder-OS source version.

## 4. Version conflicts

- Multiple live versions of the same item inside the room (the archive does not count): flag for consolidation to one latest.
- A room version older than the source version: flag for Sync.
- An item present in the room but "source removed" at Founder-OS: flag for a human decision (keep, archive, or request replacement).

## 5. Near-duplicates

Surface content-similar items (same title different content, or high textual overlap) that should be consolidated. Report them; never auto-pick a winner.

## 6. Sensitivity sanity

- Flag any item missing a `sensitivity` tag.
- Flag mis-tiered items (employee PII or litigation tagged `public`, a pitch deck tagged `restricted` for no reason). Mis-tiering is a leakage risk for diligence-ops, so treat a too-open tag on sensitive content as a blocker.

## 7. Report

Deliver a single prioritized punch list:

- **Blocker** (would fail or embarrass at the active stage): missing core item, sensitive content mis-tiered open, stale financials/cap table at an active raise.
- **Should-fix:** thin items, version lags, near-duplicates, stale overview.
- **Nice-to-have:** optional folders, cosmetic consolidation.

Each line carries: finding, canonical location, why it matters at this stage, and the one-click action (sync / archive / consolidate / request from Founder-OS). End with a one-line readiness verdict relative to the named stage, for example: "Seed-ready except two blockers (cap table stale, IP assignment missing)."

Offer to execute the safe actions (Sync refresh, archive move). Never execute consolidation or anything destructive without explicit confirmation, and never delete.
