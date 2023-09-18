#!/usr/bin/env python3

import typing

import tabulate
import collections

from semgrep_rules_manager.sources import Source, read_sources


def generate_table(sources: typing.List[Source]) -> str:
    table = [
        [
            f"`{source.identifier}`",
            stringify_lang_counter(source.count_rules()),
            source.author,
            source.license,
        ]
        for source in sources
    ]

    return tabulate.tabulate(
        table,
        ["Identifier", "Included Rules per Language", "Author", "License"],
        tablefmt="github",
    )


def write_readmes(table: str) -> str:
    for readme in ["README.template.md", "README.pypi.template.md"]:
        generate_readme(readme, table)


def generate_readme(template_readme: str, table: str) -> str:
    output_file = template_readme.replace(".template", "")
    with open(template_readme, "r") as template_file:
        content = template_file.read()
        content = content.replace("<!-- INCLUDED_SOURCES -->", table)

        with open(output_file, "w") as readme_file:
            readme_file.write(content)


def stringify_lang_counter(counter: collections.Counter) -> str:
    return ", ".join([f"`{lang}`: {count}" for lang, count in counter.items()])


def main() -> None:
    sources = read_sources("/tmp")
    table = generate_table(sources)
    write_readmes(table)


if __name__ == "__main__":
    main()
