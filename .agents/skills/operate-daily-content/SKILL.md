---
name: operate-daily-content
description: Prepare, validate, version, publish, replace, or audit deterministic daily game content for Redraft. Use when creating daily packs, questions, lineups, answers, seeds, scoring inputs, correction workflows, content calendars, or production checks that depend on basketball data.
---

# Operate Daily Content

Treat every daily challenge as an immutable, reproducible release artifact.

## Select the operating mode

- `prototype`: fictional or manually curated content used only for a bounded research test.
- `production-candidate`: content may reach users and must pass all applicable gates.

For production-candidate work, stop if the game rules, scoring version, data source review, asset rights, timezone, or accountable approver is missing.

## Build the pack

Use `vault/90 Templates/Content Pack Review.md` to record a production-candidate review.

Give the pack stable, machine-readable fields:

- `pack_id` and scheduled date/timezone;
- game, rules, scoring, schema, and transform versions;
- deterministic seed;
- prompts, choices, constraints, answers, explanations, and tie-breakers;
- source and license references;
- created, reviewed, and approved timestamps;
- validation summary and content hash.

The running game must consume the versioned pack, not query a third-party provider directly.

## Validate before release

Run checks appropriate to the format:

1. Schema: required fields, types, IDs, references, and version compatibility.
2. Determinism: the same pack and rules always produce the same outcome.
3. Semantics: answers, constraints, score components, ties, and explanations agree.
4. Provenance: every real-world fact traces to an approved source and transform.
5. Rights: every name, mark, image, clip, and derived field has a recorded basis for use.
6. Fairness: no ambiguous answer, impossible state, hidden rule, or unstable dependency.
7. Difficulty: intended segment can complete the task without accidental triviality.
8. Accessibility: content does not depend only on color, sound, tiny targets, or unexplained jargon.
9. Operations: schedule, preview, kill switch, last-known-good pack, and rollback are ready.

Never infer that a public endpoint or visible web page grants reuse rights.

## Publish and correct safely

- Use a preview environment or local replay before activation.
- Separate creation from approval for production content.
- Publish by immutable `pack_id`; keep the previous known-good pack.
- On a material error, withdraw or supersede the pack instead of editing it silently.
- Preserve historical game results against their original pack and rules versions.
- Record the correction, affected scope, user-facing message, and prevention action.

## Update project memory

Record new providers in `Data Source Register.md`, new asset classes in `Asset Rights Register.md`, recurring operational work in `Backlog.md`, and changed policy as an ADR. Do not store licensed raw datasets, credentials, or private user data in Git or the vault.
