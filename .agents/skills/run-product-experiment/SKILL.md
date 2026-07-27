---
name: run-product-experiment
description: Turn a Redraft product or game hypothesis into a decision-ready experiment and record the result without promoting weak evidence to fact. Use when planning interviews, prototype tests, concierge daily runs, A/B tests, usability studies, metric thresholds, experiment instrumentation, or go/no-go evaluation.
---

# Run Product Experiment

Design the smallest ethical test that can change a real product decision.

## Load context

1. Read `vault/00 Home/Project Home.md` and `vault/00 Home/Current Context.md`.
2. Read the linked hypothesis, audience, game concept, metrics, and relevant gate notes only.
3. Search for an existing experiment ID before creating a new note.
4. Use `vault/90 Templates/Experiment.md` for a durable experiment record.

## Define the decision first

Write down:

- the decision this experiment can change;
- one falsifiable hypothesis and its stable ID;
- the target segment and recruitment source;
- the smallest representative prototype;
- the primary success metric;
- guardrail metrics and stop conditions;
- thresholds fixed before observing results;
- duration, sample target, exclusions, and known limitations.

Do not run research whose possible outcomes lead to the same decision.

## Protect participants and evidence

- Collect only data required for the decision.
- Avoid names, contact details, raw recordings, and account identifiers in Git or the vault.
- Require an explicit privacy and age plan before recruiting minors or collecting personal data.
- Separate observed behavior, participant statements, interpretation, and recommendation.
- Mark small-sample or convenience-sample results as directional.
- Do not change thresholds after seeing results without recording the experiment as exploratory.
- Record failed instrumentation, dropouts, operator intervention, and protocol deviations.

## Instrument the minimum funnel

Prefer stable event names and properties that can survive implementation changes:

`exposed -> started -> valid_submission -> result_viewed -> shared -> returned`

For each event define its meaning, trigger, required properties, prohibited personal data, and deduplication rule. Manual logs are acceptable during discovery when their limitations are explicit.

## Evaluate the outcome

Classify the result:

- `supported` — the predefined threshold was met;
- `not-supported` — it was not met;
- `inconclusive` — evidence quality or sample was insufficient;
- `invalid` — the protocol or measurement failed.

Report effect size or raw counts where possible, not only percentages. Explain plausible alternative causes and operational cost. A successful usability session does not prove retention, and stated sharing intent does not equal actual sharing.

## Persist the learning

1. Complete the experiment note with sources and observations.
2. Update the canonical hypothesis status without deleting its history.
3. Add validated metric definitions to `Metrics.md`.
4. Add follow-up work only to `Backlog.md`.
5. Record a consequential choice as an ADR.
6. Update `Current Context.md` when the result changes current truth or the next step.

Never copy raw participant data into the vault.
