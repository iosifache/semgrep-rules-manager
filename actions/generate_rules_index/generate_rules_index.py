#!/usr/bin/env python3

import tabulate
import typing


from semgrep_rules_manager.sources import read_sources, Source
from semgrep_rules_manager.helpers import translate_lang_id_to_name

INDEX_NAME = "RULES_INDEX.md"


def create_table_with_rules(sources: typing.Iterable[Source]) -> str:
    table = []
    for source in sources:
        for file in source.get_rule_files():
            for rule in file.rules:
                table.append(
                    [
                        f"`{rule.identifier}`",
                        rule.message,
                        f"`{source.identifier}`",
                        f"`{rule.severity.name}`",
                        ", ".join(
                            [
                                translate_lang_id_to_name(lang)
                                for lang in rule.languages
                            ]
                        ),
                    ]
                )

    return tabulate.tabulate(
        table,
        [
            "Identifier",
            "Message",
            "Parent source",
            "Severity",
            "Languages",
        ],
        tablefmt="github",
    )


def dump_to_index_file(table: str) -> None:
    with open(INDEX_NAME, "w", encoding="utf-8") as rules_index_file:
        rules_index_file.write(table)


def main() -> None:
    sources = read_sources("/tmp")
    table = create_table_with_rules(sources)

    dump_to_index_file(table)


if __name__ == "__main__":
    main()
