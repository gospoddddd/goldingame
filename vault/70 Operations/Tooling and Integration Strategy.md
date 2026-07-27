---
id: OPS-INT-001
type: integration-strategy
status: proposed
owner: architecture
created: 2026-07-27
updated: 2026-07-27
review_after: 2026-08-10
---

# Tooling and Integration Strategy

Интеграция добавляется только тогда, когда у неё появляется конкретная система-источник, повторяемая задача и владелец. MCP не является долговременной памятью и не заменяет API-контракт приложения.

## Текущая конфигурация

| Возможность | Решение сейчас | Причина |
|---|---|---|
| OpenAI Developer Docs MCP | Enabled глобально | Актуальная документация Codex и OpenAI |
| GitHub plugin/connector | Private remote `gospoddddd/goldingame` создан | PR, review и CI; writes только по явному запросу |
| Browser / Computer Use | Использовать после появления интерфейса | Реальный mobile-flow, accessibility и smoke QA |
| Obsidian MCP | Не добавлять | Vault доступен как обычные versioned-файлы |
| Filesystem или Git MCP | Не добавлять | Нативных средств Codex достаточно |
| Generic memory / vector MCP | Не добавлять | `project-context` и канонический vault уже решают память |
| Basketball-data MCP | Не добавлять | Нужны лицензия, provenance и собственный adapter, а не доверие к произвольному серверу |
| Database MCP | Не добавлять до выбора backend | Ранний прямой доступ повышает риск и связывает архитектуру |
| Figma plugin | Отложить до UI-направления | Полезен, только если Figma станет источником истины дизайна |
| Analytics / error tracking | Выбрать после event plan и стека | Сначала определить события, privacy и бюджет |
| Cloud / deploy integration | Выбрать после ADR по hosting | Деплой должен иметь preview, rollback и отдельное подтверждение |

Project Stop hook запускает `scripts/validate_workspace.py` перед завершением хода Codex. Изменённый hook требует повторного trust-review в Codex.

GitHub Actions workflow `Workspace Quality` опубликован в bootstrap-ветке. До успешного первого run и настройки branch protection он не считается required check.

## Условия допуска MCP или connector

Подключать инструмент только если одновременно выполнено следующее:

1. Названа система-источник и повторяемая задача.
2. Официальный или проверяемый поставщик поддерживает сервер.
3. Зафиксированы владелец, scope, стоимость и способ отключения.
4. Выданы минимальные права; по умолчанию read-only.
5. Записывающие действия требуют отдельного подтверждения.
6. Секреты находятся в environment или secret store, а не в Git и vault.
7. Результат инструмента считается недоверенным входом и валидируется.
8. Есть тестовая область, audit trail и план на случай недоступности.

## Поэтапное подключение

### Discovery

- OpenAI docs для актуальной конфигурации.
- Web research с первичными источниками.
- Локальные файлы и ручные prototype logs.
- Никаких production-данных или пользовательских аккаунтов.

### Technical MVP

- GitHub для PR, review и CI.
- Browser testing для критического игрового пути.
- Выбранная аналитика с минимальной event taxonomy.
- Hosting через проверяемый pipeline с preview и rollback.

### Closed beta

- Error tracking и operational alerts.
- Read-only production diagnostics с редактированием чувствительных полей.
- Support workflow без передачи лишних персональных данных.

### Production

- Отдельные сервисные аккаунты на среду.
- Периодическая ревизия разрешений и неиспользуемых интеграций.
- Записывающие production-инструменты только для ограниченных runbook-действий.

## Правило выбора

Если задачу надёжно решают код, тест, CLI или versioned-файл в репозитории, не добавлять MCP. Если нужен живой контекст внешней системы или строго ограниченное действие в ней, рассмотреть connector или MCP.
