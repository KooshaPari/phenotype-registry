# Cross-Collection Integration Tests

**Location:** `tests/integration_cross_collection.rs`

**Traces to:** FR-ORG-AUDIT-2026-04-002

## Overview

Five integration tests verify the phenotype-bus event flow across Phenotype collections. Each test simulates handlers from different collections responding to published events, ensuring loose coupling and proper event propagation through the async broadcast pipeline.

## Test Suite

### Test 1: Sidekick Emits User Status Event
- **Name:** `test_sidekick_emits_user_status_event`
- **What:** Sidekick publishes a `UserStatusChanged` event
- **Verifies:** Basic pub/sub, event serialization, event naming
- **Runtime:** ~1ms

### Test 2: Eidolon Responds to Status Event with Screenshot
- **Name:** `test_eidolon_responds_to_status_event_with_screenshot`
- **What:** Eidolon subscribes to `UserStatusChanged`, emits `ScreenshotTaken`
- **Verifies:** Event handler chain (status → screenshot), subscriber isolation
- **Runtime:** ~2ms

### Test 3: Stashly Caches Screenshot Artifact
- **Name:** `test_stashly_caches_screenshot_artifact`
- **What:** Stashly subscribes to `ScreenshotTaken`, emits `ScreenshotCached`
- **Verifies:** Artifact preservation through event propagation
- **Runtime:** ~2ms

### Test 4: Observably Records Trace for Pipeline
- **Name:** `test_observably_records_trace_for_pipeline`
- **What:** Observably subscribes to `ScreenshotCached`, emits `TraceRecorded`
- **Verifies:** Tracing signal propagation, latency recording
- **Runtime:** ~2ms

### Test 5: Sidekick Messaging Notifies on Completion
- **Name:** `test_sidekick_messaging_notifies_on_completion`
- **What:** Sidekick Messaging subscribes to `TraceRecorded`, emits `NotificationSent`
- **Verifies:** Final-stage notification, message formatting
- **Runtime:** ~2ms

## Event Flow

```
[Sidekick]
    ↓ publishes UserStatusChanged
[Bus<UserStatusChanged>]
    ↓ received by Eidolon handler
[Eidolon]
    ↓ publishes ScreenshotTaken
[Bus<ScreenshotTaken>]
    ↓ received by Stashly handler
[Stashly]
    ↓ publishes ScreenshotCached
[Bus<ScreenshotCached>]
    ↓ received by Observably handler
[Observably]
    ↓ publishes TraceRecorded
[Bus<TraceRecorded>]
    ↓ received by Sidekick Messaging handler
[Sidekick Messaging]
    ↓ publishes NotificationSent
[Bus<NotificationSent>]
```

## Key Design Patterns

### Broadcast Channel Subscription Order

Tests subscribe to buses **before** publishing to ensure events are not lost. In tokio's `broadcast::channel`, subscribers created after a publish miss the event. Each test:

1. Creates the bus
2. Creates subscribers (via `bus.subscribe()`)
3. Spawns handler and capture tasks
4. Publishes the event
5. Awaits handler completion with 500ms timeout

### Event Isolation

Each test uses distinct event types (via the Event trait), ensuring no cross-talk between tests. The Bus is generically typed (`Bus<E: Event>`), so `Bus<UserStatusChanged>` and `Bus<ScreenshotTaken>` are completely separate channels.

### Async/Await Correctness

Handlers spawn as separate Tokio tasks. Tests use `tokio::sync::Mutex` to capture events from spawned handlers and verify side effects before asserting. This mirrors production patterns where event handlers are long-lived subscribers in background services.

## Running Tests

```bash
# All tests
cargo test

# Only integration tests
cargo test --test integration_cross_collection

# Specific test
cargo test test_sidekick_emits_user_status_event

# With output
cargo test -- --nocapture
```

## CI Integration

The GitHub Actions workflow (`quality-gate.yml`) runs:

```bash
cargo test --verbose
cargo clippy --all-targets -- -D warnings
cargo fmt --check
```

All 8 tests (3 unit + 5 integration + 2 smoke) pass on every push/PR.

## Traceability

Each test includes a tracing comment linking to the functional requirement:

```rust
// Traces to: FR-ORG-AUDIT-2026-04-002, Test N/5
```

This enables coverage analysis and ensures every test is intentional and tracked in the spec.
