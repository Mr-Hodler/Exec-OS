# Standard and onboarding

## What the standard is

"Aron's File Organization Standard" is a portable document that captures how files and workspaces should be organized across every company and project. It is derived first from how the user already organizes well, then topped up with best practice where their patterns are thin. It is the shared convention that keeps each new company consistent from day one, and the yardstick Advise aligns to.

Default location: a document named `File-Organization-Standard.md` written to the workspace, with its path referenced in config so Advise and Onboarding can read it. It is versioned; bump the version when it changes.

## Standardize mode: deriving it

1. **Observe the good patterns.** Across the scanned scope, find the conventions the user already applies consistently: how they name files, how deep they nest, how they date and version, how they separate active work from archive, how they group by company vs project vs topic.
2. **Extract the implicit rules.** Turn observed patterns into explicit rules. Prefer the user's working conventions over generic advice; the goal is to formalize what works for them, not to impose a foreign system.
3. **Fill gaps with best practice.** Where there is no consistent pattern (or a clearly harmful one), add a sensible rule: shallow over deep nesting, ISO dates (YYYY-MM-DD), explicit version suffixes over `final_REAL_v3`, a consistent separator, a clear archive convention.

   Optional starting templates when there is little to learn from (a new or very messy setup). Offer one as a baseline, then adapt it rather than impose it:
   - **PARA** (Projects, Areas, Resources, Archive): for a personal or operator workspace organized by actionability.
   - **Johnny.Decimal** (numbered areas and categories, for example `10-19 Finance`, `11 Invoices`): when findability and a stable, speakable index matter across a team.
   - **Function-first** (top level by functional area / product / team): the default for a company workspace, and the natural target when Architect has inferred a functional map.
   The chosen template is a scaffold; the user's working conventions still win where they exist.
4. **Write the document.** Sections to include:
   - **Naming conventions:** case, separators, dates, versioning, language.
   - **Folder taxonomy:** the standard top-level structure for a company and for a project, with depth limits.
   - **Active vs archive:** where finished and superseded material goes (`_archive/` convention, never deletion).
   - **Per-context variants:** a company, a personal area, a client project may differ; document each. Where Architect has inferred a functional map, make the company variant org-aware (functional areas, product lines, shared spaces) rather than generic.
   - **Cross-company consistency:** what must be identical across companies so tooling and habits transfer.
5. **Version and reference.** Stamp a version and date. Update the config reference if the path or name changes.

## Onboarding mode: applying it

1. **Confirm an empty/new target.** Onboarding is for a **new** company or project. If the target already has files, do not impose the structure: switch to Scan plus Advise and offer the structure as a recommendation instead.
2. **Read the standard.** Load `File-Organization-Standard.md`. If it does not exist yet, offer to run Standardize first, or scaffold from the best-practice default and note that it is not yet personalized.
3. **Create the structure.** Build the standard top-level folders for the new target. Create only new, empty folders. Never move, rename, or touch anything that exists.
4. **Leave a seam for the data room.** For a company that will have a data room, do not recreate the canonical data room folders here; leave a clear place for `investor-ops` Bootstrap to lay them down, so the two skills do not duplicate or fight over structure.
5. **Report.** List exactly what was created and what was intentionally left to other skills (the data room to investor-ops).

## Boundary with investor-ops Bootstrap

Onboarding sets up a company's **general working structure** (where day-to-day files live). Bootstrap sets up the **data room** specifically (the examiner-facing canonical corpus). Onboarding references the data room as a known area but defers its internal structure to Bootstrap. This keeps one owner per structure and avoids drift.
