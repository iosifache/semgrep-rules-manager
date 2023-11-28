#!/usr/bin/env python3

import json
import typing


from semgrep_rules_manager.sources import read_sources, Source
from semgrep_rules_manager.helpers import translate_lang_id_to_name

INDEX_NAME = "semgrep_rules_manager/data/index.json"


def create_index_from_rules(sources: typing.Iterable[Source]) -> list:
    index = []
    for source in sources:
        for file in source.get_rule_files():
            for rule in file.rules:
                index.append(
                    {
                        "identifier": f"{rule.identifier}",
                        "message": rule.message,
                        "parent_source": f"{source.identifier}",
                        "severity": f"{rule.severity.name}",
                        "languages": ", ".join(
                            [
                                translate_lang_id_to_name(lang)
                                for lang in rule.languages
                            ]
                        ),
                    }
                )

    return index


def dump_to_index_file(table: list) -> None:
    with open(INDEX_NAME, "w", encoding="utf-8") as rules_index_file:
        rules_index_file.write(json.dumps(table))


def main() -> None:
    sources = read_sources("/tmp")
    index = create_index_from_rules(sources)

    dump_to_index_file(index)


if __name__ == "__main__":
    main()
