# dataroom-ops - Audit report (yardstick: seed / SICTIC + hardware, ai overlays)

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
