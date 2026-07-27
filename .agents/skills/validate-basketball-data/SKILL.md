---
name: validate-basketball-data
description: Evaluate basketball data sources, files, schemas, transformations, and providers for provenance, permitted use, coverage, quality, reproducibility, and game fairness. Use before adopting or scraping a data source, importing a dataset, changing derived statistics, generating game content, or shipping rules that depend on basketball facts.
---

# Validate Basketball Data

Do not let convenient data become an unreviewed product dependency.

## Review

1. Identify the owner, provider, exact dataset or endpoint, access method, version, refresh cadence, and cost.
2. Capture the governing license, terms, attribution requirements, redistribution limits, retention limits, and commercial-use status. Mark legal conclusions for qualified review.
3. Reject scraping or reverse-engineering as a default. Require an explicit decision before relying on an unofficial endpoint.
4. Profile coverage and semantics:
   - seasons, leagues, teams, players, regular season and playoffs;
   - trades, relocations, renamed teams, two-way players, positions, and missing games;
   - IDs, time zones, corrections, nulls, duplicates, and source disagreements.
5. Define canonical IDs and raw-to-canonical transformations. Preserve source snapshots, transform version, and provenance.
6. Test representative and adversarial records. Compare a sample with an independent authoritative source when allowed.
7. Map each game rule to fields and transformations. Explain how corrections affect active daily games and historical scores.
8. Record an approve, conditional, or reject recommendation in `vault/30 Data/Data Source Register.md`.

## Release gates

- No production dependency without documented permitted use.
- No silent answer correction; publish a dispute and correction policy.
- No media assets unless their rights and attribution are recorded.
- No secrets or raw personal data in the repository or vault.
- Prefer versioned, reproducible daily seeds over live mutable queries.
