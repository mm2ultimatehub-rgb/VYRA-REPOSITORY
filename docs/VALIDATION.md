# Catalog validation workflow

Every app/version record must identify its Android package name, patch publisher, bundle release and exact target versions.

## Test record required for stable support
- APK source URL/type and acquisition date;
- package name, version name/version code, signer certificate digest and APK SHA-256;
- base/split APK list and ABI;
- patch bundle URL, publisher, release, SHA-256 and signature result;
- patch selection and options;
- engine exit status and logs;
- output APK SHA-256 and signing certificate digest;
- install result and smoke-test result on a named Android API level/device ABI.

Do not set `validation.status` to `verified` until all required steps pass. A release README compatibility table is only a candidate signal.

## First target
YouTube `com.google.android.youtube` 21.30.216. Morphe Patches v2.3.0 lists this target. The project has a locally supplied APK for testing; it is intentionally not mirrored here. Download the exact upstream bundle and verify its SHA-256 before allowing the patch engine to inspect or execute it.
