---
id: ENG-001
type: engineering-strategy
status: proposed
owner: architecture
created: 2026-07-27
updated: 2026-07-27
review_after: 2026-08-10
---

# Engineering Quality Strategy

Эти ограничения помогают масштабировать продукт без преждевременного усложнения. Конкретные технологии появятся только после ADR по MVP-стеку.

## Архитектурная позиция

- Начать с одного deployable web-продукта и ясных внутренних модулей.
- Отделить game engine, content packs, identity, analytics и внешние data adapters контрактами.
- Версионировать schema, rules, scoring, transforms и content packs.
- Считать сервер авторитетным для результатов, challenge и competitive state.
- Добавлять очередь, cache, отдельный сервис или event bus только после измеренного ограничения.

## Среды и поставка

- `local` — вымышленные или безопасные тестовые данные.
- `preview` — изолированная проверка каждого изменения.
- `production` — только через воспроизводимый pipeline и одобренную версию.
- Конфигурация отделена от кода; секреты не попадают в репозиторий.
- Миграции данных имеют forward-путь, проверку и recovery plan.
- Feature flags имеют владельца и дату удаления.

## Обязательные quality lanes

1. Static: formatting, types, lint, dependency and secret checks.
2. Unit: game rules, scoring, tie-breakers, transforms.
3. Contract: content schema, provider adapters, analytics events.
4. Integration: persistence, identity, corrections, degraded mode.
5. Browser: start-to-result, share/challenge, mobile viewport, keyboard.
6. Property and replay: determinism, idempotency, historical pack replay.
7. Accessibility: semantics, focus, contrast, motion, screen-reader labels.
8. Security and privacy: authorization, abuse, retention, deletion, logging redaction.

## Наблюдаемость

Определить до beta:

- product events с владельцем и data dictionary;
- technical logs с correlation ID без секретов и PII;
- ошибки, latency и content publication status;
- SLO для критического игрового пути;
- алерты, которые ведут к конкретному runbook;
- стоимость по среде и основной cost driver.

## Масштабирование команды

- Один владелец у каждого модуля, метрики, интеграции и operational workflow.
- Малые vertical slices с reviewable acceptance criteria.
- ADR для решений с высокой стоимостью отмены.
- CODEOWNERS, PR template и branch protection после появления GitHub remote и команды.
- Базовый `Workspace Quality` CI проверяет конфигурацию и vault независимо от будущего app-стека.
- Автоматизация проверки важнее автоматизации безусловного выпуска.

## Anti-goals

- Microservices до доказанной необходимости.
- Общая база как неявный API между будущими сервисами.
- Live-зависимость игрового результата от стороннего API.
- Неограниченный production-доступ агентов или MCP.
- Несколько параллельных флагманских игр до подтверждения первой.
