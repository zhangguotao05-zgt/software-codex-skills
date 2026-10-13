# Verification and delivery

## Environment is part of the candidate

Use the project's existing profile mechanism; for example, an explicit
`APP_PROFILE=dev-local|integration|production`. Parse and validate it once at
startup/build composition and inject immutable configuration. Do not silently
fall back to production for absent or invalid settings. Preserve framework
variables such as `NODE_ENV` for their original semantics.

Build mode controls optimization/assertions/debug support; the profile controls
endpoints, identity, data and permitted adapters. A `Release` build can be used
for local performance tests and is not automatically a production artifact.
Keep development and production app identities, storage and update sources
separate where supported. Display a useful development/test marker.

Production excludes mock adapters, debug entry points and test update sources.
Enforce its normal authentication, authorization and update verification at
trusted boundaries; a user-editable flag must not disable those protections.
Client compile-time values are extractable, so keep service secrets on the
server or in the appropriate protected secret store. Use test credentials only
in their isolated environment and keep their values out of handoffs and logs.

## Diagnose once, verify the affected behavior

Capture the failing command, candidate/profile and observable result. Form a
specific hypothesis and use the least invasive observation that distinguishes
it. Follow errors through the actual caller and shared state. Preserve first
failure evidence; do not repeatedly rerun an unchanged failing environment.
For a transient error, use a bounded retry with a reason. Continue independent
work when a dependency blocks only part of the task.

| Impact | Focus |
| --- | --- |
| L0: text/docs with no product contract or build-input effect | Diff, encoding, relevant links and display; no unrelated application rebuild. |
| L1: local UI or business behavior | Affected static/type/build checks plus normal, failure, cancellation and lifecycle behavior. |
| L2: shared contracts, identity, persistence, migration, concurrency or updates | Affected consumers/platforms, real integration seams and fault/recovery cases. |
| Release milestone | Promised platform matrix, packaged behavior, production profile, upgrades and applicable recovery/security/performance criteria. |

Classify by actual consequences, not file suffix or line count. Use existing test
commands and deterministic fixtures. Reuse unchanged builds and tests when source,
configuration, dependencies, fixtures and runtime conditions remain applicable.
After a failure or change, rerun that check and adjacent affected behavior; expand
only when findings justify it. Independent review inspects code and raw results,
and does not inherently require reinstalling tools or repeating every build.

## Candidate, installation and release

Record the source revision/diff, target platform, lockfile/tool versions, build
mode, profile, relevant resource/schema versions and artifact identity. A secret
is represented by a safe version identifier, never its value. Confirm that built
resources, migrations and native dependencies are packaged when relevant.

Integrate the accepted candidate, then check the actual effect of conflict or
dependency changes. Promote the same artifact when valid. If environment values
change compiled content, build and verify the matching production artifact
instead of renaming a development package. Follow existing authorization for
push/install/deploy; only ask when a necessary action is not already covered.

For a release, prepare the exact target, identity/signature/channel, migrations,
readiness and key-path observations, plus a compatible rollback or forward fix.
Do not apply database rollback assumptions to an irreversible schema change.
For routine installation of an unchanged accepted artifact, verify the target,
installation and necessary startup behavior; widen checks only for a change or
failure. External-service or physical-device operation requires its own scope.

## Accurate completion

Distinguish checks run now, checks reused with a valid basis, and checks not run
or blocked. Mock data, emulator behavior, target-device behavior and production
results are separate claims. Close an Issue only when its own original criteria,
required independent review and agreed delivery branch/state are satisfied.
Do not relabel missing requirements as passed or shrink scope to increase counts.

For a long-running test, define duration, required observations, stop conditions
and cleanup before starting. A bounded local runner owns stopping; a chat reminder
does not. Auxiliary diagnostic gaps remain explicit and invalidate claims that
depend on them, without automatically proving a product failure. Preserve primary
monitoring requirements. Completion includes persisted results and owned-resource
cleanup, not just elapsed time.

Report outcome, candidate/profile, executed/reused/missing checks and the next
responsible action in the existing task. Request one batch of genuinely necessary
human observations when automation cannot supply them. Avoid duplicate Issues,
parallel status documents and serial approvals that add no decision or evidence.
