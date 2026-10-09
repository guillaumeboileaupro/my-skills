---
name: analog-vu-meter-ui
description: Build accessible analog VU meter interfaces with a moving-coil needle, electromagnetic torque, spring return, inertia and damping. Use for vintage audio dashboards, audio widgets, interactive instrument simulations, and needle-based UI.
---

# Analog VU Meter UI

Create a reusable, responsive, vintage analog VU meter component. Preserve the physical feel of a moving-coil instrument rather than animating the needle with a linear CSS transition.

## Visual specification

- Warm ivory dial, dark metal bezel, black tick marks, red needle, central pivot and clearly labeled VU.
- Display calibrated marks at -20, -10, -5, 0 and +3 VU. Mark the positive range in red.
- Render with SVG or Canvas; use an accessible HTML control layer. Do not rely on color alone.
- Expose a responsive layout for desktop, Android and widgets. Honor reduced-motion preferences.
- Make the dial and needle the visual focus, with optional controls below.

## Physical model

A classic moving-coil mechanism has a permanent magnet, moving coil, spring, inertia and damping. Audio AC is rectified before driving the meter. Approximate the dynamics by:

```text
J * theta'' + c * theta' + k * theta = K * I(t)
```

Where J is rotational inertia, c damping, k spring stiffness, K the electromagnetic coupling and I the rectified/smoothed drive current. Equilibrium is theta = K*I/k.

Implement a semi-implicit Euler or stable fixed-step integrator:

```text
acceleration = (driveTorque - springK * angle - damping * velocity) / inertia
velocity += acceleration * dt
angle += velocity * dt
```

Use a fixed timestep near 1/120 s with a bounded accumulator, and pause when hidden. Avoid resetting velocity on ordinary input changes: the needle should accelerate, overshoot if underdamped, and settle naturally. Bound physical stops and optionally model a small rebound. Allow critical, under- and over-damped presets.

## VU calibration and behavior

- Do not treat 0 VU as digital full scale. Reference calibration is configurable; +4 dBu is common for professional analog equipment.
- Distinguish true VU response from an arbitrary spring animation: a standard VU meter reaches about 99% of final indication after 300 ms for a reference step, with limited overshoot. Tune and test the default parameters against this response.
- Do not map VU linearly to dB across the entire scale; use calibrated tick angles and an interpolated or measured transfer function.
- Treat audio peaks separately from the average-level needle. Use Web Audio API RMS or an appropriate rectified and filtered signal, with adjustable reference.
- Include silence, clipping, invalid-input and audio-permission states.

## Interaction contract

Provide a signal-level slider, spring-stiffness slider, damping slider, a 0 VU step button, release button and simulated music mode. Show current signal, needle reading and angular velocity. Simulated music is explicitly labeled, never confused with microphone or actual audio input.

## Implementation and tests

- Separate physics, calibration, rendering and input acquisition modules. Keep physics deterministic and unit-testable.
- Unit-test zero drive, equilibrium, step response, damping regimes, frame-rate independence, bounded stops and invalid values.
- Integration-test animation start/stop, keyboard controls, touch input, screen reader labels and reduced motion.
- Test on mobile and desktop, including battery/CPU usage. Avoid unnecessary dependencies.
- For React, encapsulate animation lifecycle in a hook and clean up requestAnimationFrame and audio streams.
- Document default values, units, calibration and any intentional departures from historical accuracy.

## Acceptance criteria

1. Needle visibly accelerates and returns with a convincing spring response.
2. Default preset approximates the standard 300 ms VU step behavior.
3. Under-damped preset shows overshoot; heavily damped preset does not.
4. No memory leaks, unstable integration or off-scale needle positions.
5. Responsive, accessible, and visually faithful to vintage analog meters.

## Executable reference

Open [`examples/vu-meter.html`](examples/vu-meter.html) directly in a browser for the standalone HTML/CSS/SVG/JavaScript prototype. It demonstrates spring dynamics, damping, step and release controls, and simulated music. The prototype uses an illustrative VU scale and is not calibrated as a standards-compliant measurement instrument. Treat the physics and calibration requirements above as the production acceptance target.
