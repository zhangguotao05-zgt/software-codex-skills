# Architecture and contracts

## Select a useful boundary

Map the existing structure before proposing directories. Organize around actual
capabilities such as accounts, records or reporting. A small feature can remain
one cohesive module. Prefer a modular monolith until independent deployment,
scaling or team ownership creates a concrete reason to split services.

- Views own interaction and presentation; use cases coordinate one operation.
- Domain rules own calculations and valid state transitions using ordinary data.
- Adapters own HTTP, files, databases and platform-specific protocol conversion.
- Composition owns construction, environment selection and startup/shutdown.

These are responsibility boundaries, not a demand for four classes per feature.
Introduce an interface where there is a real external boundary, substitution or
test seam. Use a direct call before adding a bus, registry or generic framework.

For each affected boundary, identify input/output types, errors, authoritative
state, lifetime and the code allowed to mutate it. Change callers together when
the contract changes. Avoid passing ORM entities, UI controllers or raw sockets
through unrelated modules. Use derived UI state instead of a second writable
copy of authoritative data.

## Preserve a precise contract

Specify the relevant fields, nullability, units, precision, versions, timestamps,
pagination, cancellation, timeout and error semantics. Reject invalid external
values at their boundary. Keep parsing separate from business interpretation.

Persist instants with an explicit time basis; define the business timezone for
daily grouping separately. Measure elapsed time with a monotonic clock. Give
money, measurement scaling and enum mappings one authoritative definition.

Across languages, share schema, compatibility examples and invalid fixtures
before sharing a runtime. Generate transport types when already supported.
Share code only for stable common semantics with an owner; do not accumulate
unrelated helpers in a global `utils` module. Version external contracts and
state which deployed older clients remain supported.

## Refactor for a demonstrated benefit

Write a brief current problem, intended benefit and behavior-to-preserve note in
the existing task. Prioritize correctness and data integrity, then ownership and
cycles, duplicated rules, measured bottlenecks, and finally local cleanup.
Make the transition around a runnable use case; retain the old behavior contract
until callers are migrated. Delete obsolete paths only after checking callers,
configuration, persisted formats and supported older versions.

Evaluate efficiency with representative input size and concurrency. Watch UI
thread blocking, repeated IO, N+1 queries, full-list refresh, unbounded buffers
and cache growth. Record workload and before/after measurements for performance
claims. Do not equate fewer lines, more files or more abstractions with quality.
