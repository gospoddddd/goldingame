---
name: project-context
description: Route work through the Redraft Obsidian vault without loading the whole knowledge base, and update canonical context after material changes. Use when starting a project task, looking for product or technical decisions, recording facts or hypotheses, updating current context, or deciding where new project knowledge belongs.
---

# Project Context

Use the vault as durable project memory and load only the smallest relevant slice.

## Read context

1. Read `vault/00 Home/Project Home.md`.
2. Read `vault/00 Home/Current Context.md`.
3. Follow only links relevant to the task. Do not scan the entire vault.
4. Search by stable ID, title, and keywords before creating a note.
5. Treat code and tests as the source of truth for implemented behavior.

## Classify knowledge

- Put verifiable information with a source in a fact note.
- Put an unverified claim in a hypothesis note.
- Put a chosen option with consequences in an ADR.
- Put executable work in the backlog.
- Put product behavior in a game or feature specification.

Never promote a hypothesis to fact without evidence. Add an observation date and source to time-sensitive facts.

## Write context

1. Update the canonical note instead of duplicating content.
2. Link to related notes rather than copying them.
3. Preserve accepted decisions; supersede them with a new ADR.
4. Update `Current Context.md` after material work with current truth, open risks, and the next step. Do not paste chat history.
5. Never store secrets, credentials, private user data, or unlicensed media in the vault.
