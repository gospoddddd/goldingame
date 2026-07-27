---
id: RISK-REG-001
type: risk-register
status: active
owner: project
created: 2026-07-27
updated: 2026-07-27
review_after: 2026-08-03
---

# Risk Register

Риск описывает возможное будущее событие. Уже произошедшая проблема становится incident или backlog item. Этот реестр не заменяет [[../10 Product/Pre-code Gates|Pre-code Gates]].

## Шкалы

- Impact: `Critical`, `High`, `Medium`, `Low`.
- Likelihood: `Likely`, `Possible`, `Unlikely`, `Unknown`.
- Status: `Open`, `Mitigating`, `Accepted`, `Closed`.
- `Accepted` требует владельца, срока пересмотра и ADR для существенного риска.

## Активные риски

| ID | Риск | Impact | Likelihood | Владелец | Mitigation / сигнал пересмотра | Статус |
|---|---|---|---|---|---|---|
| RISK-001 | Флагманская петля не создаёт фактический возврат | High | Unknown | Product | [[../10 Product/Assumption Register|Hypotheses]], недельный experiment с observed return | Open |
| RISK-002 | Использование брендов, likeness, медиа или данных не разрешено | Critical | Unknown | Product + Data | Fictional-only prototype, source и rights review до реальных сущностей | Open |
| RISK-003 | Неоднозначный ответ или tie-breaker разрушает доверие | High | Possible | Game + QA | Versioned rules, deterministic replay, correction и appeal flow | Open |
| RISK-004 | Ежедневный контент слишком дорог или нестабилен | High | Possible | Product + Operations | Семь manual packs, измерение времени редактора и error rate | Open |
| RISK-005 | География, возраст или технические логи создают privacy-обязательства | Critical | Unknown | Product + Architecture | Data-flow и privacy review до публичного теста | Open |
| RISK-006 | Leaderboard, challenge или rewards стимулируют abuse | High | Possible | Architecture + QA | Server authority, rate limits, abuse model; не запускать ranked преждевременно | Open |
| RISK-007 | Сторонний provider недоступен или меняет исторические данные | High | Possible | Data + Architecture | Adapter, snapshot, content pack, kill switch, last-known-good | Open |
| RISK-008 | Преждевременная сложность замедляет проверку продукта | Medium | Likely | Architecture | Один deployable product, reversible ADR, complexity только по измерению | Mitigating |
| RISK-009 | Стоимость инфраструктуры и content operations растёт быстрее аудитории | Medium | Unknown | Product + Architecture | Cost owner, budget alert и cost-per-completed-game до beta | Open |
| RISK-010 | Игра недоступна с клавиатуры, screen reader или reduced motion | High | Possible | QA + Product | Accessibility criteria, browser checks и реальные usability sessions | Open |

## Протокол review

1. Проверять реестр перед переходом между фазами и после incident.
2. Обновлять likelihood только по новым evidence, а не по уверенности команды.
3. Указывать backlog item для mitigation, если работа стала исполнимой.
4. Не закрывать риск только потому, что соответствующая функция отложена; помечать trigger.
5. Переносить существенное принятие риска в ADR с последствиями и сроком пересмотра.
