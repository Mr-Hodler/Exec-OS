# Information architecture (Architect mode)

Architect treats the information architecture as a mirror of the company's real functional, product, and team structure. It reads the topology, infers how the company actually works, recommends how its information should be structured to match, and flags the operations and performance frictions the topology reveals. It is read-only: it produces a map, a recommendation, and a friction list, and changes nothing.

It owns **information** architecture. It does not own **team** architecture: people, roles, team boundaries, and scaling decisions belong to the functional-hr-ops skill, which consumes Architect's evidence.

## 1. Organizational signals (input)

From Scan's signals pass (`scan-and-providers.md`): file-type mix per area, provider/drive types, product and team folder clustering, the collaboration and access graph (who creates/edits/shares what), activity hotspots and dead zones, and ownership concentration. If those signals were not collected, run the signals pass first.

### Governance signals (optional, when a connector exists)

Today Architect reads file-level access (sharing and permissions) from the Drive connector, which already powers the access-mismatch frictions. Org-level governance (Google Workspace groups, org units, admin roles, security policies like 2FA/SSO/DLP, or an external directory/Active Directory) is **not read by default** and is not available without an Admin SDK or Cloud Identity connector.

When such a connector exists, Architect may consume these as **read-only signals** to sharpen the functional map (groups and org units often reveal de facto teams) and the friction list (access policy gaps). It still does not own them: governance and IAM are a separate domain. The seam:

- **Groups and org units** are evidence routed to the future `functional-hr-ops` skill (they map to team structure).
- **Security and access policies** are evidence routed to `compliance-ops` / `investor-ops` (SOC 2, ISO 27001, GDPR).
- **Identity and access management** proper (provisioning, roles, SSO) belongs to a future `security-ops` / `iam-ops` skill.

Architect reads these signals if available, attributes them, and hands the decisions to the owning skill. It never manages identities, groups, or policies.

## 2. Infer the implicit functional map

Reconstruct the de facto structure from the evidence, not from a claimed org chart:

- **Functional areas:** clusters of files/spaces that serve one function (product, engineering, sales, finance, ops, legal, people).
- **Product lines:** areas organized around a product or offering.
- **Team boundaries:** who collaborates with whom, inferred from the access/edit graph. Dense collaboration clusters are de facto teams.
- **Collaboration patterns:** where work crosses boundaries (healthy interfaces) and where it does not (silos).

State the inferred map as a hypothesis grounded in named evidence ("finance and ops share one drive and three editors, so they operate as one unit today"), not as fact. Mark confidence and note where the signals are thin.

### The Organization Model takes precedence (from functional-hr-ops)

If `functional_hr_ops.organization_model_path` (default `Organization-Model.md`) exists, read it: it is the **target** team and org structure functional-hr-ops designed, and it wins over the purely inferred map. Architect then recommends an information architecture that mirrors the Organization Model, using its "Information-architecture mapping" section to place artifacts (for example marketing design assets under `marketing/design/`, a product team's specs under that product's area, shared collaboration in the named shared space).

The split: functional-hr-ops owns the team architecture and writes the model; workspace-ops owns the information architecture and mirrors the model. When the inferred de-facto map diverges from the Organization Model, flag the drift back to functional-hr-ops as evidence (the org may have changed, or the model may be stale), and do not silently override the model.

## 3. Recommend the target information architecture

Propose how information should be structured to mirror the inferred reality (and the Organization Model when present) and to scale:

- **Top level by company** (isolation holds, as everywhere in Exec-OS), then by functional area / product / team as the evidence warrants.
- **Shared spaces where collaboration is dense**, so the structure supports how the team actually works rather than fighting it.
- **Clear ownership** for every area; no ownerless zones.
- **A seam for the data room** per company (owned by investor-ops Bootstrap), referenced not recreated.
- **Alignment to the standard** (`File-Organization-Standard.md`); note where the standard itself should evolve to fit what the company has become.

Present the target IA as a proposal to validate, with the reasoning from the map. Never impose.

## 4. Friction taxonomy (what to flag)

Operations and performance frictions visible in the topology:

- **Silos:** a function or team with no shared space, or knowledge trapped in one person's drive.
- **Cross-team duplication:** the same artifact maintained in several places by several teams (drift and wasted effort).
- **Ownerless / orphaned areas:** active content no one clearly owns.
- **Single-person bottlenecks:** critical knowledge concentrated in one editor (key-person risk).
- **Access mismatches:** sensitive material too open, or material a team needs locked away from it.
- **Structure-vs-reality mismatch:** the folder structure encodes an old org that no longer matches how work flows.

Prioritize: high (risk or active drag on operations), medium (findability/consistency), low (cosmetic).

## 5. Hand off people and scaling to functional-hr-ops

Where the evidence points beyond information into team design, surface it as evidence and route the decision, do not decide it here:

- A function carrying disproportionate load (signal of a missing role or a team that should split).
- A bottleneck person (signal of a hiring or knowledge-distribution need).
- A collaboration pattern that suggests two teams should merge or split.

Write these as explicit handoff notes: the observed signal, the information-architecture implication (which Architect owns), and the team/people question for functional-hr-ops (which it does not). The functional-hr-ops skill consumes the inferred functional map and these notes to design team structure and help scale the team (roles, boundaries, vision), exactly as investor-ops consumes the data room.

## 6. Deliverable

- The **inferred functional map** (with evidence and confidence).
- The **target IA recommendation** (aligned to the standard, with reasoning).
- The **prioritized friction list**.
- The **functional-hr-ops handoff notes**.
- Optionally a visual map if `preferences.visual_artifact` allows.

Everything is read-only and advisory. Applying any resulting file moves is Execute mode (v1.1), under every safeguard, and never includes deletion.
