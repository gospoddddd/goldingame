# Contributing to Redraft

Redraft пока находится в discovery. Вклад должен уменьшать неопределённость или поставлять ограниченный проверяемый результат, а не молча закреплять продуктовые и технические предположения.

## Перед началом

1. Прочитать `AGENTS.md`, `vault/00 Home/Project Home.md` и `vault/00 Home/Current Context.md`.
2. Найти существующий backlog ID, спецификацию, гипотезу или ADR.
3. Зафиксировать observable outcome и то, что не входит в scope.
4. Проверить связанные Product, IP, Data, Privacy, Fairness, Security и Quality gates.
5. Не добавлять production dependency, MCP, provider или dataset без владельца и review.

## Изменения

- Делать небольшой vertical slice с одним ответственным результатом.
- Сохранять обратимость решений и совместимость versioned contracts.
- Не смешивать рефакторинг, продуктовый эксперимент и изменение данных без необходимости.
- Не помещать в Git секреты, PII, licensed datasets или unlicensed media.
- Фиксировать решение в ADR, наблюдение в experiment/research note, задачу только в Backlog.
- Не копировать реализационные детали в vault; код и тесты являются источником истины.

## Проверка

После изменения конфигурации, agents, skills, hooks или vault выполнить:

```bash
make check
```

После появления продуктового кода также выполнить документированные targeted tests и более широкий CI-набор. Не придумывать команды, которых ещё нет в репозитории.

## Pull request

PR должен содержать:

- backlog ID и связанные спецификации/ADR;
- наблюдаемый результат и границы scope;
- evidence выполненных проверок;
- влияние на данные, права, privacy, accessibility и analytics;
- failure и rollback behavior;
- явное описание известных ограничений.

Внешние действия — deploy, publish, purchase, push в защищённую ветку или изменение production — требуют отдельного разрешения.
