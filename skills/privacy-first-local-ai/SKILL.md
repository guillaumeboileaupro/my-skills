---
name: privacy-first-local-ai
description: Design or audit local-first AI features that process sensitive audio, text, documents, or personal data. Use for privacy boundaries, model execution, storage, consent, export, deletion, and optional remote processing.
---

# Privacy-First Local AI

Keep processing local by default and make every data boundary visible.

- Inventory collected data, derived data, model inputs, logs, caches, exports, retention, and deletion paths.
- Treat audio, voiceprints, transcripts, documents, identifiers, and embeddings as sensitive.
- Do not add network transmission, telemetry, cloud inference, or remote backup by default.
- Require an explicit user action, clear destination, purpose, and documented retention for optional remote processing.
- Store data in user-controlled locations, minimize permissions, encrypt where justified, and avoid secrets in logs.
- Make deletion cover databases, files, caches, temporary data, and derived artifacts.
- Verify offline behavior and failure modes with the network unavailable.

Run `python scripts/scan_network_usage.py <source-root>` as a heuristic review of network-capable code. Review every finding manually.
