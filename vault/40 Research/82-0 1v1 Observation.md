---
id: RES-002
type: research
status: observed
owner: research
created: 2026-07-27
updated: 2026-07-27
review_after: 2026-08-10
source_urls:
  - https://www.82-0.com/
---

# Research: 82-0 public 1v1 flow

## Decision to support

Определить место 1v1 в competitive roadmap Goldingame и отличить текущий публичный паттерн 82-0 от асинхронного challenge-response.

## Method and comparison set

Прямое наблюдение публичной mobile-web поверхности [82-0](https://www.82-0.com/) 2026-07-27 в portrait viewport. Использован автоматически созданный guest без регистрации. Сравнение ограничено одним продуктом, потому что пользователь указал конкретный референс.

## Observations

- На стартовой поверхности рядом с Classic и Hoop IQ присутствует отдельная кнопка `Play 1v1`.
- Нажатие `Play 1v1` показывает состояние `Finding an opponent…`.
- Примерно через пять секунд guest был переведён в игровую сессию без sign-in gate.
- Сессия отображала `Round 1/5`, пять позиций состава и team/era spin.
- После spin был показан пул игроков выбранных команды и десятилетия с позициями и статистикой; игрок выбирает состав по раундам.
- На сайте отдельно доступны Challenges, My Stats и Leaderboards; наблюдавшийся leaderboard имел Classic/HoopIQ и All time/Daily/Weekly фильтры, а попадание в рейтинг предлагало sign-up.

## Inferences

- Наблюдаемый 1v1 использует быструю очередь и совместную match session, а не ссылку с ожиданием ответа через часы или дни.
- Гостевой вход уменьшает трение до первой игры, а постоянный leaderboard отделён от гостевого опыта.
- Конкретный draft-loop 82-0 не следует копировать; переносимый паттерн — быстрый переход `queue → shared match → result`.

## Hypotheses

- Queue-based 1v1 может усилить competitive-привлекательность Goldingame после появления достаточного пула игроков.
- До появления пула same-seed leaderboard и сезонная лига могут дать большую часть competitive-ценности с меньшей операционной сложностью.

## Limits and inaccessible evidence

- Матч не был завершён, поэтому не наблюдались opponent UI, scoring, rating delta, tie, reconnect, abandon и rematch.
- Публичная поверхность не подтверждает, всегда ли найденный соперник является человеком, используется ли bot fallback и насколько синхронны действия.
- Наличие режима не доказывает retention, популярность или коммерческий эффект.

## Recommendation

Считать queue-based 1v1 обязательной целевой возможностью Goldingame, но не блокировать им первый MVP. Сначала проверить флагман, same-seed competition и двухслойную прогрессию; затем спроектировать 1v1 с server-authoritative session, reconnect, abandon, empty-queue fallback и отдельными abuse guardrails.

## Follow-up experiment

После подтверждения флагманской петли сделать малый 1v1-прототип на 10–20 участниках и измерить queue success, match completion, replay intent, спорные outcomes и понимание rating delta.
