---
name: deliver-feature
description: Deliver a scoped Redraft feature from canonical context through implementation, verification, and knowledge updates. Use when building or changing product behavior, game rules, analytics, data pipelines, UI flows, APIs, or infrastructure in this repository.
---

# Deliver Feature

Keep changes small, traceable, and reversible.

## Workflow

1. Read the project home, current context, linked spec, accepted ADRs, and backlog item. Do not load unrelated vault notes.
2. Inspect repository state and existing implementation patterns.
3. Restate scope as observable acceptance criteria. Surface missing product, data, rights, analytics, accessibility, or failure behavior.
4. Plan the smallest vertical slice. Delegate only independent read-heavy work or isolated file ownership.
5. Implement without touching unrelated user changes.
6. Add or update tests for behavior, edge cases, and deterministic game rules.
7. Run the narrowest relevant checks, then the repository's documented broader checks when available.
8. Review the diff for secrets, unlicensed assets, hidden mutable data dependencies, analytics leakage, and missing error states.
9. Update the canonical spec, ADR, backlog status, and `Current Context.md` only when the implementation changed their truth.
10. Report outcome, verification evidence, known limits, and the next decision.

## Definition of done

- Acceptance criteria are met in runnable behavior.
- Relevant checks pass or failures are explained with evidence.
- Data provenance and rights are documented for new dependencies.
- User-facing behavior and analytics events match the spec.
- The vault points to current truth without copying implementation details.
