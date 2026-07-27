---
id: AGT-001
type: operating-model
status: active
owner: project
created: 2026-07-27
updated: 2026-07-27
review_after: 2026-08-27
---

# Agent Team

| Агент | Зона ответственности | Доступ |
|---|---|---|
| `product_strategist` | Позиционирование, аудитория, эксперименты, метрики | Read-only |
| `game_designer` | Игровые петли, правила, скоринг, fairness | Project write |
| `data_steward` | Provenance, лицензии, схемы, качество данных | Read-only |
| `solution_architect` | Границы, ADR, безопасность, надёжность | Read-only |
| `feature_builder` | Реализация небольших вертикальных срезов | Project write |
| `qa_reviewer` | Корректность, fairness, privacy, accessibility, тесты | Read-only |

## Основные workflows

| Workflow | Ведущие роли |
|---|---|
| `$run-product-experiment` | `product_strategist`, review от `qa_reviewer` |
| `$operate-daily-content` | `game_designer`, review от `data_steward` и `qa_reviewer` |
| `$review-product-readiness` | `solution_architect`, evidence от всех владельцев gates |
| `$deliver-feature` | `feature_builder`, review от `qa_reviewer` |

## Протокол

1. Родительский агент формулирует независимую и ограниченную задачу.
2. Read-only роли возвращают доказательства и рекомендации.
3. Записывающий агент получает конкретные файлы или изолированную область.
4. Родительский агент объединяет результат, проверяет противоречия и отвечает пользователю.
5. Параллельное редактирование одних файлов не допускается.
