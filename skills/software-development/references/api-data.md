# API and data

## Trusted boundary and compatibility

Trace request parsing, normal authentication, object/tenant authorization,
business rules and persistence. Validate untrusted inputs at the boundary and
enforce authorization where the trusted data/action is owned. Preserve framework
middleware and error contracts. Bound request size, pagination and execution time.
Avoid responses or logs that reveal credentials or unrelated users' data.

For updates, document how older clients behave with changed fields, enum values
and errors. Prefer compatible additions and reject unsupported input explicitly.
Keep transport DTOs separate from persistence models when their concerns differ.
Use existing schema/contract tooling rather than adding another parallel source.

## Writes, retries and migrations

Identify the transaction and concurrency boundary. Pair idempotency keys or
deduplication with durable uniqueness/consistency constraints as needed; a
client-side disabled button alone does not prevent duplicates. Retry only
operations known to be safe, with timeout, a limit and backoff. Define conflict
behavior for concurrent edits and partial external-service success.

Use versioned migrations and existing migration commands. Production does not
depend on development schema synchronization or automatic destructive recreation.
Before applying a consequential migration, identify target data, current schema,
backup/restore, lock impact and compatibility with both old and new application
versions. Exercise it on isolated representative data first. Code rollback does
not imply a reversible schema; provide a tested restore or forward repair when
reverse migration cannot preserve data. Existing authorization still determines
whether the target operation may run.

## Local development and dependencies

Use isolated local databases and deterministic seed data through normal supported
setup. Local test accounts use normal authentication and permissions. Keep mock
adapters explicit and selectable only for their intended development/test scope.
An authentication failure remains a failure; never silently replace it with
anonymous access, simulated success or production credentials.

If a cloud integration is unavailable, finish its independent parsing, UI,
business and error-handling work against a documented local contract. Retain
pending real-integration criteria. Use correlation IDs and redacted diagnostics
to distinguish transport, authentication, authorization and domain failures.

## Jobs and runtime

Name the owner of each scheduled job, queue consumer, database pool and service
process. Define concurrency, capacity, cancellation, shutdown and redelivery
behavior. Prevent uncontrolled duplicate workers. Distinguish liveness, readiness,
business completion and auxiliary telemetry; do not infer a healthy operation
solely from a running process or an open port.

Measure representative latency and query behavior before optimizing. Inspect
indexes, transaction duration, pool saturation, N+1 queries and memory growth for
the affected path. Verify recovery by actually restoring data when recovery is
the acceptance criterion; a successful backup job alone is insufficient.
