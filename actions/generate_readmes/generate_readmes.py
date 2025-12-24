#!/usr/bin/env python3

import typing

import tabulate
import collections

from semgrep_rules_manager.sources import Source, read_sources


def generate_table(sources: typing.List[Source]) -> str:
    table = [
        [
            f"`{source.identifier}`",
            stringify_lang_counter(source.count_rules(beautified=True)),
            source.author,
            source.license,
        ]
        for source in sources
    ]

    return tabulate.tabulate(
        table,
        ["Identifier", "Rules per Language", "Author", "License"],
        tablefmt="github",
    )


def write_readmes(source_count:int, rules_count: int, table: str) -> str:
    for readme in ["README.template.md", "README.pypi.template.md"]:
        generate_readme(readme, source_count, rules_count, table)

def generate_readme(template_readme: str, source_count: int, rules_count: int, table: str) -> str:
    output_file = template_readme.replace(".template", "")
    with open(template_readme, "r", encoding="utf-8") as template_file:
        content = template_file.read()
        content = content.replace("<!-- INCLUDED_SOURCES -->", table)
        content = content.replace("<!-- SOURCES_COUNT -->", str(source_count))
        content = content.replace("<!-- RULES_COUNT -->", str(rules_count))
        with open(output_file, "w", encoding="utf-8") as readme_file:
            readme_file.write(content)


def stringify_lang_counter(counter: collections.Counter) -> str:
    return ", ".join(
        [f"{count} for {lang}" for lang, count in counter.items()]
    )


def main() -> None:
    # Convert generator to list to allow multiple iterations
    sources = list(read_sources("/tmp"))

    source_count = len(sources)
    rules_count = sum(
        [source.count_all_rules() for source in sources]
    )

    table = generate_table(sources)

    write_readmes(source_count, rules_count, table)


if __name__ == "__main__":
    main()
