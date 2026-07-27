---
id: ADR-0002
type: adr
status: accepted
owner: project
created: 2026-07-27
updated: 2026-07-27
review_after: 2026-10-27
supersedes:
superseded_by:
---

# ADR-0002: Repository governance

## Context

Проекту нужен одинаковый минимальный quality contract для локальной работы, Codex и будущего GitHub CI до выбора продуктового стека. Проверки не должны зависеть от памяти чата или ручного списка файлов.

## Decision

- Использовать `make check` как стабильную локальную entry point для project-level проверок.
- Проверять обязательную структуру, agents, skills, hooks, TOML/JSON, note IDs и Obsidian wikilinks через `scripts/validate_workspace.py`.
- Запускать validator из project Stop hook; изменённый hook требует trust-review.
- Запускать тот же contract в GitHub Actions с read-only `contents` permission.
- Использовать pull request template для scope, gates, verification и rollback.
- Защитить `main`: требовать PR, актуальный успешный `Validate project configuration` и закрытые обсуждения; запретить force-push и удаление, применять правила к администратору.
- Для solo workflow не требовать второго approving review; владелец разрешает Codex самостоятельно вести и сливать проверенные PR.
- Не связывать этот workflow с автоматическим production deploy.
- Хранить исполнимые задачи в vault Backlog; GitHub issues в будущем могут быть execution mirrors только со стабильным project ID.

## Consequences

- Ошибка структуры или сломанная ссылка обнаруживается локально до PR.
- Добавление нового обязательного project artifact требует обновить validator.
- Локальный `make check` и required GitHub check используют один contract; изменение не попадает в `main` при красной проверке.
- Отсутствие обязательного второго reviewer сохраняет скорость solo workflow, но повышает важность CI, scoped diff review и обратимости.
- Product-specific lint, tests, security и browser jobs будут добавлены после выбора стека.
- Stop hook является guardrail, а не единственной enforcement boundary.

## Alternatives

- Только ручная проверка: отклонено как невоспроизводимое.
- Выбрать framework-specific CI сейчас: отложено до решения TECH-001.
- Автоматически deploy из каждого успешного PR: отклонено до hosting ADR, preview и rollback.
- Использовать GitHub issues вместо vault Backlog: отложено, чтобы не создавать два конкурирующих источника истины.
