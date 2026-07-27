---
name: review-product-readiness
description: Review whether a Redraft prototype, feature, beta, content release, integration, or launch is ready for its next stage. Use for go/no-go reviews, pre-code gates, release checklists, risk acceptance, launch readiness, or deciding whether work may move from local prototype to users.
---

# Review Product Readiness

Issue an evidence-backed stage decision without turning a checklist into false assurance.

## Establish the review boundary

1. Name the exact artifact or scope under review.
2. Name the target transition: discovery test, technical MVP, closed beta, or public release.
3. Read `vault/10 Product/Pre-code Gates.md` and only the linked evidence relevant to the scope.
4. Exclude unrelated future features explicitly.

## Review each applicable gate

Use one status per gate:

- `approved`: evidence and an accountable owner support this exact scope;
- `conditional`: bounded work may proceed under written conditions and an expiry;
- `blocked`: a missing decision or unacceptable risk prevents the transition;
- `not-applicable`: explain why the gate cannot affect this scope.

Assess:

- Product: segment, job, loop, experiment, and success criteria.
- Brand/IP: naming, marks, likenesses, media, and review scope.
- Data Rights: source, license, storage, transforms, and exit plan.
- Privacy/Age: geography, age, consent, retention, processors, and deletion.
- Fairness: versioned rules, tie-breakers, corrections, and appeals.
- Monetization: pricing, advertising, prizes, and pay-to-win risks.
- Operations: daily SLA, validation, rollback, degraded mode, and ownership.
- Security: threat model, secrets, authorization, abuse, and server authority.
- Quality: tests, accessibility, observability, performance, and recovery.

## Require evidence

For every non-blocked conclusion, cite the decision, test, contract, source review, or verified artifact that supports it. A plan to produce evidence is not evidence. Do not provide legal certification; record when qualified legal or privacy review is still required.

## Issue the decision

Return:

1. `go`, `conditional-go`, or `no-go`;
2. the exact scope covered;
3. blockers ordered by severity;
4. conditions, owners, and expiry dates;
5. residual risks explicitly accepted;
6. the smallest next verification step.

Never approve an entire platform because one prototype passed. Never let a conditional approval silently become permanent.

## Persist the review

Use `vault/90 Templates/Readiness Review.md`. Update gate status only when the supporting evidence exists, put new work in `Backlog.md`, create an ADR for accepted consequential risk, and update `Current Context.md` when the project stage changes.
