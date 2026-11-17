# Security and distribution policy

## APK files
VYRA Repository is primarily a metadata and source-discovery repository. Do not commit proprietary APKs or redistribute them unless the publisher explicitly permits it. Prefer official stores, publisher-approved downloads, or a user-provided local APK. For split APKs, require a complete compatible split set.

Before patching, verify package name, exact version, signer certificate expectations, source provenance, SHA-256 and split/base APK completeness.

## Patch bundles
MPP bundles may contain executable DEX/JVM code. A valid ZIP/JAR structure or matching SHA-256 does not prove code is safe.

- HTTPS only; pin publisher, release URL and expected digest.
- Verify detached signatures when provided.
- Parse metadata without loading or executing bundle code.
- Third-party bundles start as experimental.
- Execute only through the isolated patcher runtime with memory/time limits, cancellation and logs.
- Never silently promote a candidate to verified.

## Verification levels
1. `candidate`: source lists the target version.
2. `inspected`: bundle digest and metadata inspected.
3. `patched`: patch engine completed successfully.
4. `rebuilt`: output APK rebuilt and signed.
5. `verified`: output installed and smoke-tested on a real device.

Only level 5 may be shown as supported/stable.

## Re-signing
A patched APK is normally signed with a different certificate from the original app. It may not install as an update over the official app; users may need to uninstall the original first, which can remove local data. Explain this before installation.

Never put access tokens, personal data or private APKs in this repository or its issue tracker.
