---
name: software-development
description: "Implement, debug, refactor and validate mobile apps, websites, desktop applications, APIs and data services using cohesive modules, narrow interfaces and focused checks. Use for software feature delivery, architecture cleanup, cross-client data or lifecycle bugs, development/production configuration and release readiness. Routine small fixes stay small; firmware and physical device operation are outside this skill."
metadata:
  version: "1.0.1"
---

# Software Development

Deliver the requested working behavior with explicit ownership, simple control
flow and evidence proportional to the change. Apply this to the existing stack;
the skill does not prescribe Flutter, React, Electron, a backend or a database.

## Recover the actual project

- Read applicable project instructions, the current handoff and relevant pipeline
  configuration, including `config.json` when present, before modifying scripts.
- Identify the real repository, branch, uncommitted work, target platforms,
  package manifests, lockfiles, runnable commands and already valid results.
  Preserve unrelated changes and the relationships inside an existing monorepo.
- Translate the request into observable behavior and a bounded change. Resolve
  routine choices from the project. Ask only when missing information changes
  the result or an action lacks authorization; continue independent work.
- Use actual command definitions rather than inventing generic build commands.
  Reuse a working toolchain; install or change dependencies only when needed.

## Load only the relevant detail

| Task | Reference |
| --- | --- |
| New feature, shared contract, state ownership or architecture refactor | [Architecture and contracts](references/architecture.md) |
| App, Web or PC interaction, asynchronous state and platform lifecycle | [Client behavior](references/clients.md) |
| API, authorization, persistence, migration or background jobs | [API and data](references/api-data.md) |
| Environment selection, local substitutes, diagnosis, tests, packaging or delivery | [Verification and delivery](references/delivery.md) |

Read the relevant sections, not every platform checklist. These references ship
with the skill and work without access to a separate handbook repository.

## Implement one complete behavior

1. Follow the affected path from input through rules and external boundaries to
   the visible result or persisted state. Identify the authoritative data and
   the owner of cancellation, connections, subscriptions and transactions.
2. Fix demonstrated defects before restructuring. Reproduce a bug at the narrowest
   useful boundary; preserve its original failure. A refactor needs a concrete
   ownership, duplication, testability or measured performance benefit.
3. Make the smallest coherent change including its affected callers, error paths
   and compatibility needs. Keep framework and IO details out of business rules
   where doing so clarifies ownership. Do not manufacture layers or interfaces
   for simple functions that have no substitution or testing need.
4. Complete normal, empty, failure and cancellation behavior where applicable.
   Give retries, buffers, caches and background work explicit bounds. Propagate
   useful errors to the layer that can handle them; release owned resources.
5. Inspect the diff and run the affected checks. For a behavioral defect, prefer
   a regression that fails on the old behavior. Do not add tests that merely
   mirror implementation, or broaden passing checks without a new reason.

## Check code principles in the existing handoff

| Check | Required reasoning |
| --- | --- |
| Q1 Cohesion | A module owns one business capability or clear technical boundary; UI is not also the parser, database and permission engine. |
| Q2 Coupling | Callers use a narrow public contract; no cycle, internal-state mutation or accidental global service dependency. |
| Q3 Ownership | State, tasks, subscriptions, files and connections have one owner with explicit cancellation and cleanup. |
| Q4 Recovery | Timeout, duplicate operations, partial writes and restart have defined outcomes; no swallowed failures or unbounded retries. |
| Q5 Simplicity and efficiency | Remove real duplication and dead paths; keep descriptive names and bounded work. Measure before claiming performance gains. |
| Q6 Integration | Checks exercise the affected production call path; substitutes preserve relevant failure, identity and cancellation semantics. |

Record material findings and their resolution, not six extra approval documents.
Use project formatters and nearby conventions; avoid unrelated formatting.

## Keep development moving with honest boundaries

Use an explicit local development profile, isolated fixtures and normal local
test identities when production services are unavailable. Keep build mode
(`Debug`/`Release`) separate from environment selection. Resolve configuration
once at the composition boundary; unknown or invalid profiles fail clearly.
Production excludes test adapters and test update channels, and enforces its
normal authentication, authorization and update verification requirements.

Local substitutes can validate UI and business rules. They do not prove real
authentication, external synchronization, native platform behavior or production
readiness. Leave only the dependent acceptance items pending, while finishing
everything independently executable. See [delivery](references/delivery.md).

## Finish and report

Keep routine standalone fixes in their existing scope. Apply role handoffs only
when the current change is covered by a registered work-package agreement: C
delivers the integrated change, D reviews the affected code and original evidence,
and A resolves actual shared boundaries or blockers. Follow existing design gates;
seek design input for a new interaction decision, not merely for restoring
already intended behavior. This skill creates no chats, delegates no work and
grants no acceptance authority. An implementer cannot present their own checks
as independent acceptance.

Reuse valid results with a reason tied to unchanged inputs. Repeat checks when
affected code, configuration, dependencies, fixtures or runtime conditions change,
when a check fails, when evidence is missing, or when the project requires it.

Use existing authorization for commits, pushes, installation and deployment.
If authorization for an external action is missing, complete the reviewable
candidate and target-specific plan first, then ask only for that action.
Close an Issue only after its original required criteria and agreed delivery
state are met; keep missing platform, integration or release evidence explicit.

Report the working result, candidate/profile, checks run, justified reuse,
remaining limitations and next responsible action. Keep one existing Issue or
handoff as the entry point. Installation of this skill alone changes no project's
accepted baseline, role assignments or release requirements.
