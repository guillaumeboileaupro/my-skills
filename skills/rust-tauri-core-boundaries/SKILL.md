---
name: rust-tauri-core-boundaries
description: Design Rust/Tauri 2 applications with business and protocol logic independent from the Tauri shell. Use when implementing a reusable Rust core shared by GUI commands, local integrations, MCP tools, tests, or platform packaging.
---

# Rust Tauri Core Boundaries

Keep Tauri thin and make Rust the authoritative application core.

## Architecture

- Put domain logic, device state, protocol handling, validation, and orchestration in ordinary Rust modules or crates that do not depend on Tauri APIs.
- Treat Tauri commands as adapters: deserialize input, call the core, translate typed results, and return.
- Do not duplicate business behavior between the GUI and MCP or other automation interfaces.
- Make every external interface call the same core operations.
- Keep HTML, CSS, and JavaScript focused on presentation and user interaction.

## Rust rules

- Prefer explicit types and enums for states and errors.
- Avoid `unwrap` and `expect` in runtime paths unless an invariant is both local and proven.
- Propagate errors with useful context without exposing secrets or unnecessary implementation details.
- Keep asynchronous boundaries explicit and avoid holding locks across network awaits.
- Add dependencies only when they replace meaningful complexity; prefer the standard library and focused crates.

## Tauri rules

- Keep the command surface small and intentional.
- Validate all data crossing the frontend/native boundary.
- Grant only capabilities and permissions required by implemented features.
- Do not move protocol code into frontend JavaScript to bypass Rust implementation work.
- Do not add a frontend framework when native HTML, CSS, and JavaScript satisfy the UI requirement.

## Shared interfaces

Model core operations so the GUI and MCP adapters can expose equivalent behavior such as discovery, device selection, playback state, play, pause, stop, seek, and volume without knowing each other's transport.

## Testing

- Test deterministic core behavior at Rust module boundaries.
- Use integration tests for protocol boundaries where they provide real value.
- Do not create tests solely to inflate coverage.
- Keep hardware-dependent Chromecast tests separate and explicitly report when a real device was not exercised.

## Review

Reject changes that make Tauri, the frontend, or MCP the owner of business logic; duplicate an operation in multiple adapters; introduce an unnecessary runtime/service; or add substantial dependencies without a concrete requirement.