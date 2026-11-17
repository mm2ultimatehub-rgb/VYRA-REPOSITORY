# VYRA Repository

Central machine-readable catalog for VYRA Studio. This repository stores metadata and trusted source references, not unauthorized copies of proprietary APKs.

## Contents
- `index.json`: entry point consumed by VYRA Studio.
- `apps/`: Android package identities, candidate target versions and validation status.
- `sources/`: patch publishers, release URLs, digests and trust classification.
- `schemas/`: catalog format contract.
- `docs/`: validation and security policy.

## Status meanings
- `candidate`: identified upstream compatibility; not tested end-to-end by VYRA.
- `experimental`: third-party or incomplete source; manual review required.
- `verified`: exact APK + bundle patched, rebuilt, signature-checked, installed and smoke-tested.
- `unsupported`: no compatible source currently known.

An upstream compatibility table is not proof that VYRA has tested a version.

## First test target
YouTube `com.google.android.youtube`, version `21.30.216`. Morphe Patches v2.3.0 lists this version. A matching APK was previously supplied for local testing and is not mirrored here.

Third-party patches, APKs, names, logos and source code retain their own licenses and terms. See [security policy](docs/SECURITY.md).
