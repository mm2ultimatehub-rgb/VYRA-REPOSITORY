#!/usr/bin/env python3
import json
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]

def load(path):
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)

def require_https(value, where):
    if urlparse(value).scheme != "https":
        raise SystemExit(f"{where}: URL must use HTTPS: {value}")

for path in sorted(ROOT.rglob("*.json")):
    load(path)

index = load(ROOT / "index.json")
assert index["schemaVersion"] == 1
for key in ("apps", "patchSources"):
    require_https(index["catalog"][key], f"index.catalog.{key}")

apps_index = load(ROOT / "apps/index.json")
sources_index = load(ROOT / "sources/index.json")
source_ids = {item["id"] for item in sources_index["sources"]}
app_ids = set()
for app in apps_index["apps"]:
    assert app["id"] not in app_ids, f"duplicate app id: {app['id']}"
    app_ids.add(app["id"])
    assert app["packageName"] and "." in app["packageName"]
    record = load(ROOT / "apps" / app["appRecord"])
    assert record["id"] == app["id"]
    assert record["packageName"] == app["packageName"]
    for source_id in app["patchSourceIds"]:
        assert source_id in source_ids, f"{app['id']}: unknown source {source_id}"

for source in sources_index["sources"]:
    release = source["latestRelease"]
    require_https(release["page"], f"{source['id']}.release.page")
    require_https(release["assetUrl"], f"{source['id']}.release.assetUrl")
    digest = release.get("sha256", "")
    if len(digest) != 64 or any(c not in "0123456789abcdef" for c in digest.lower()):
        raise SystemExit(f"{source['id']}: invalid SHA-256 digest")

print(f"Catalog OK: {len(app_ids)} apps, {len(source_ids)} patch sources.")
