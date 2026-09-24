---
name: chromecast-control-rust
description: Implement and review Chromecast or Google Cast device control in Rust, including LAN discovery, connection lifecycle, receiver/media state, commands, protocol errors, and real-device validation. Use when building the Cast core of a Rust application.
---

# Chromecast Control in Rust

Build the Cast layer as a typed, recoverable Rust subsystem independent from the GUI and MCP adapters.

## Discovery and identity

- Discover devices on the local network using the appropriate Cast/mDNS service information.
- Keep stable device identity separate from user-facing names.
- Handle devices appearing, disappearing, changing address, sleeping, or becoming unreachable.
- Do not assume the first discovered device is the intended target.

## Connection lifecycle

- Model disconnected, connecting, connected, and unavailable states explicitly.
- Apply bounded timeouts to discovery, connection, and command operations.
- Recover from dropped connections without spawning unbounded retry loops.
- Keep protocol tasks cancellable during application shutdown or target changes.

## Cast behavior

- Keep receiver state and media state distinct.
- Represent play, pause, stop, seek, volume, mute, and media loading as core operations only when supported by the chosen protocol implementation.
- Validate volume ranges, seek values, media metadata, URLs, content types, and receiver/application identifiers before sending commands.
- Never report success solely because a command was written to a socket; use protocol responses or subsequent device state when available.

## Dependencies and protocol work

- Evaluate existing maintained Rust crates before implementing protocol framing manually.
- Inspect dependency maintenance, supported Cast protocol features, TLS/protobuf requirements, platform compatibility, and transitive dependency cost.
- If a crate is incomplete, isolate missing protocol code behind the same core interface rather than leaking workarounds into Tauri or JavaScript.
- Do not silently switch to Python, Go, Node, or a separate daemon to avoid implementing the Rust boundary.

## Media resolution

Treat finding a playable media URL or service-specific receiver target as a separate concern from Cast transport. The Cast core accepts resolved media or an explicit receiver action; it does not scrape arbitrary services unless that capability is deliberately implemented in a resolver module.

## Testing

- Unit-test message/state translation and validation without hardware.
- Keep protocol integration tests bounded and deterministic.
- Mark tests requiring a physical Chromecast separately.
- For real-device validation, verify discovery, connection, status, volume, playback control, reconnection, and failure behavior as applicable.
- Never claim a Chromecast operation works end-to-end until it has been exercised against a real compatible device.