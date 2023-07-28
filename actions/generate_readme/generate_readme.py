#!/usr/bin/env python3

import typing

import tabulate

from semgrep_rules_manager.sources import Source, read_sources


def generate_table(sources: typing.List[Source]) -> str:
    table = [
        [
            f"`{source.identifier}`",
            source.repo_url,
            source.author,
            source.license,
        ]
        for source in sources
    ]

    return tabulate.tabulate(
        table,
        ["Identifier", "Repository URL", "Author", "License"],
        tablefmt="github",
    )


def write_readme(table: str) -> str:
    with open("README.template.md", "r") as template_file:
        content = template_file.read()
        content = content.replace("<!-- INCLUDED_SOURCES -->", table)

        with open("README.md", "w") as readme_file:
            readme_file.write(content)


def main() -> None:
    sources = read_sources("/tmp")
    table = generate_table(sources)
    write_readme(table)


if __name__ == "__main__":
    main()
