---
name: design-basketball-game
description: Turn a basketball game idea into a testable, data-aware product specification. Use when proposing a new daily or practice game, changing game rules or scoring, comparing mechanics, defining fairness and edge cases, or preparing a prototype and validation experiment.
---

# Design Basketball Game

Optimize for a small experiment before a large build.

## Workflow

1. Read the product vision, current context, assumptions, and relevant accepted ADRs.
2. State the target segment and player job. Mark unknowns as hypotheses.
3. Define the core loop in one sentence: prompt, decisions, feedback, completion, and reason to return.
4. Specify:
   - session length and win or completion condition;
   - inputs, legal moves, scoring, tie-breaking, hints, and failure states;
   - daily reset, seed determinism, archive or practice behavior;
   - novice path and expert depth;
   - spoiler-safe sharing and social comparison;
   - accessibility, mobile behavior, and localization;
   - data dependencies, disputed-answer policy, and editorial override.
5. Enumerate ambiguous basketball cases: trades, relocations, eras, positions, playoffs, inactive players, name collisions, and corrected statistics.
6. Define the minimum prototype and experiment, including success metric, guardrail, sample, and go/no-go threshold.
7. Create or update a game spec from `vault/90 Templates/Game Spec.md`.

## Guardrails

- Prefer deterministic, explainable scoring.
- Do not assume rights to league marks, team logos, player likenesses, photos, video, or a data feed.
- Mark competitor patterns as evidence, not proof that a mechanic improves retention.
- Do not expand the game portfolio until the flagship loop shows repeat use.
