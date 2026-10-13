# Client behavior

## Async state and resource ownership

Follow existing UI/state conventions. Represent loading, success, empty, partial
failure, offline, denied permission, cancellation and retry where the use case
needs them. A successful local save is distinct from acknowledged remote sync.

Bind subscriptions, timers, requests and file handles to a named owner and its
lifetime. Propagate cancellation. Where cancellation cannot stop a completion,
use a request generation or context identity check before publishing results.
Changing route, account, tenant or selected entity invalidates earlier work.
Cache keys include all identity and query dimensions that change meaning; logout
clears or isolates private cache and pending callbacks, not just the token.

Keep expensive parsing and computation off the UI thread with bounded work and
progress/cancel support. A cancel action must stop new work and define what
happens to partial writes. Test the race that caused the bug, not only a mock
returning immediately. Reuse existing design tokens and accessible components.

## Mobile App

Inspect the actual platform, SDK, app identity and selected profile. Use existing
flavors/configuration mechanisms instead of scattering environment conditions.
Give development installations isolated identity/storage where supported.

Cover relevant foreground/background transitions, permission refusal/revocation,
network changes and process recreation. A connection service owns reconnect,
timeouts and shutdown; widgets do not each open another device connection.
Store credentials through the platform's intended protected storage. Work on
software protocol fixtures without initiating physical device operation.

Framework tests prove their scoped logic. Native plugins, OS permission dialogs,
background restrictions, package signing and store behavior require the relevant
target environment. Inspect the built package's assets and configuration when
they affect the change; a source-tree run does not prove packaged resources.

## Web and static sites

Use the current stack. A static site need not gain a backend or application
framework. Check affected routes by direct URL, refresh, back/forward and any
required base path. Separate cacheable assets from user-specific responses.
Browser-visible environment variables and bundles contain no secrets.

For interaction changes, cover the agreed responsive sizes, keyboard/focus,
labels, loading errors, text overflow and relevant languages. Validate form
inputs, duplicate submission and failure recovery. When authentication changes,
inspect the actual cookie/token strategy, CSRF/CORS and server authorization
instead of treating client-side hiding as access control.

Use available browser tools only within their access rules. If runtime rendering
cannot be tested, report the exact gap; source checks are not browser acceptance.

## Desktop / PC

Identify supported operating systems, native dependencies, installer and update
channel. Keep renderer capabilities narrow. For Electron, prefer isolated
renderers and a small preload bridge; validate IPC sender, operation and payload.
Do not expose arbitrary filesystem paths or command execution to remote content.
Use equivalent trust boundaries in other desktop stacks.

Importers validate size, version, encoding, truncation and paths before committing
data. Use streaming or bounded chunks for large inputs and transactions or atomic
replacement for failure recovery. Cover duplicate imports, occupied files,
window closure during work and Unicode/space-containing paths when affected.

Check upgrade preservation of settings/data, process cleanup and the actual
packaged application when those areas change. A successful build or another
operating system's run is not a Windows installer or clean-machine result.
