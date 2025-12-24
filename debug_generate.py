#!/usr/bin/env python3

from semgrep_rules_manager.sources import read_sources

sources = list(read_sources("/tmp"))

print(f"Total sources: {len(sources)}\n")

for source in sources:
    print(f"{source.identifier}:")
    print(f"  Location: {source.location}")
    print(f"  is_downloaded: {source.is_downloaded}")

    try:
        count = source.count_all_rules()
        print(f"  Rule count: {count}")
    except Exception as e:
        print(f"  ERROR counting rules: {e}")

    print()
