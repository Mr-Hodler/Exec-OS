# Visual outputs

Structure is far easier to understand as a picture than as prose, and a clear visual is one of the most useful onboarding and training assets a company has. When `preferences.visual_artifact` is `always` or `ask` (and the user agrees), functional-hr-ops renders the Organization Model into visuals, and can assemble an onboarding/training pack from them.

Always generate the visuals **from `Organization-Model.md`** so the picture and the model never drift. Regenerate after any Org Design or Org Rollout change.

## What to visualize

- **Org chart.** Reporting structure: entities (if any), departments, business units, teams, with owners and headcounts. Show the vertical (delivery) lines; show horizontal (craft/discipline) lines as dashed where a matrix applies.
- **Team-interaction map.** Teams as nodes, interaction modes as labeled edges (collaboration, as-a-service, facilitating). This is often more valuable than the org chart, since it shows how work actually flows.
- **Cross-team operations flow.** For a key operation (release, incident, planning, GTM hand-off): the steps, owners, and the escalation ladder, as a flow diagram.
- **Mind map.** The company at the center, functional areas as branches, owned outcomes and key roles as leaves. Good for a one-glance orientation.
- **RACI matrix.** The decision table, rendered for scanning, with the single Accountable highlighted per decision.

## Output formats

Choose by use, and offer the others:

- **HTML (default, best for onboarding).** A single self-contained page: org chart, interaction map, mind map, RACI, cross-team operations, and short "how we work" notes. Inline CSS and inline SVG (no external dependencies, or Mermaid from CDN only). Print-friendly so it exports to PDF from the browser. Interactive and reusable. This is the natural onboarding/training artifact.
- **PDF.** For a fixed, shareable document, render with the pdf skill (or print the HTML). Good for a handbook page or a board appendix.
- **PPT.** For a training session or all-hands, build a deck with the pptx skill: one slide per view (org chart, interaction map, key flows, the RACI), with speaker notes.

## Onboarding and training pack

Assemble the visuals plus orientation text into one artifact aimed at a new hire or the whole team:

- Who we are and how we are organized (org chart).
- How teams work together (interaction map and cross-team operations).
- Who decides what (RACI, in plain language).
- Where things live (the information-architecture mapping, the bridge to knowledge-custodian: "marketing design assets live under marketing/design/").
- How we work (work modes, rituals, anchor days).

Keep it honest and current; a stale org chart is worse than none. Stamp it with the Organization Model version and date so a reader knows how fresh it is.

## Rules

- Generate from the model, never hand-drawn divergent structures.
- No em dashes in any rendered text. No bare URLs.
- Do not put sensitive personnel data (compensation, performance, PII) in a broadly shared onboarding artifact; structure and roles only.
- If the model is missing or stale, say so and offer to run Org Design first rather than visualizing a guess.
