---
id: GATE-001
type: gate-register
status: active
owner: project
created: 2026-07-27
updated: 2026-07-27
review_after: 2026-08-03
---

# Pre-code Gates

Статус `approved` разрешает только зафиксированный scope. Это продуктовый контроль, не юридическое заключение.

| Gate | Что нужно решить | Статус |
|---|---|---|
| Product | Сегмент, job, флагманская петля, эксперимент | Blocked |
| Brand/IP | Название, оригинальная айдентика, допустимые реальные сущности | Blocked |
| Data Rights | Источник, коммерческие права, хранение, derived metrics | Blocked |
| Privacy/Age | География, возраст, guest/account, retention, processors | Blocked |
| Fairness | Версия правил, tie-breakers, correction и appeal | Blocked |
| Monetization | Бесплатность, реклама, подписка, призы, pay-to-win | Blocked |
| Operations | Daily SLA, валидатор, отмена задания, degraded mode | Blocked |
| Security | Threat model, secrets, server-authoritative scoring, abuse | Blocked |
| Quality | Test strategy, accessibility, observability, performance, recovery | Blocked |

Функция, зависящая от незакрытого gate, может существовать только как локальный прототип с явно записанным ограничением.
