---
id: DATA-001
type: data-strategy
status: proposed
owner: data
created: 2026-07-27
updated: 2026-07-27
review_after: 2026-08-10
---

# Data Strategy

## Стартовая позиция

Для MVP предпочесть небольшой versioned curated-набор исторических фактов с документированным provenance. Не строить продукт на scraping, скрытых endpoint или mutable live-запросах.

## Обязательные слои

1. Source snapshot — неизменённый полученный материал, если лицензия разрешает хранение.
2. Normalized data — канонические IDs и значения.
3. Content pack — версия вопросов, ответов, правил и seed.
4. Game result — ссылка на версии pack, rules и scoring.

## Для каждой записи

- `source`;
- `license_version`;
- `retrieved_at`;
- `effective_at`;
- `transform_version`;
- `provenance_hash`.

## Guardrails

- UI и game logic не обращаются к провайдеру напрямую.
- Токены остаются на сервере.
- Для источника существуют adapter, contract tests, kill switch и last-known-good snapshot.
- Исправление данных не меняет прошлые результаты молча.
- HTML-разметка стороннего сайта не является production API.
- Публичный endpoint не считается разрешением на коммерческое использование.
