# Contributing to Knowledge-Ops

Thanks for improving Knowledge-Ops. This is a skill/plugin suite, so most contributions are edits to Markdown rules and the config schema, not code.

## What lives where

- `skills/<skill>/SKILL.md` - the orchestrator for each skill. Change this for workflow, modes, or triggers.
- `skills/<skill>/references/*.md` - the rule library for each skill (checklists, taxonomies, operations, safeguards).
- `.knowledge-ops-config.yml` - the shared config every skill reads first. Extend the schema here when a skill needs new settings, and document the addition in SETUP.md.
- `.claude-plugin/` - plugin and marketplace manifests. Bump versions here on release.

## Ground rules for edits

These mirror what the skills enforce on their own output, so the repo stays consistent with what it preaches:

- **No em dashes (-) anywhere** in docs or skill text. Use a comma, a colon, parentheses, or split the sentence.
- **No bare URLs.** Embed links in descriptive text.
- Keep rules **dense and specific**. Prefer a concrete rule over a vague principle.
- **Safety is non-negotiable** in knowledge-custodian: never weaken a safeguard (never delete, archive + snapshot + undo log + confirmation + blacklist). Adding safeguards is welcome; removing one is not.
- Every skill **reads `.knowledge-ops-config.yml` first** and degrades gracefully when a path or platform is unreachable. Preserve that contract.

## Proposing changes

1. Fork and branch from `main`.
2. Make focused edits with a clear commit message.
3. If behavior changes, add an entry under "Unreleased" in `CHANGELOG.md`.
4. Open a pull request describing the motivation and any before/after examples.

## Versioning

Semantic Versioning. Bump the version in `CHANGELOG.md`, `.claude-plugin/plugin.json`, and `.claude-plugin/marketplace.json` together on release.

## Testing a change

Install the plugin locally and run the affected skill against a scratch workspace:

```
/plugin marketplace add /path/to/Knowledge-Ops-Repo
/plugin install knowledge-ops@knowledge-ops
```

For knowledge-custodian, always test against a disposable copy first and confirm no file is ever deleted, only archived.
