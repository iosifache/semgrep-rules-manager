#!/usr/bin/env python3

import typing

import tabulate
import git
import tempfile
import shutil
import pathlib
import collections
import yaml

from semgrep_rules_manager.sources import Source, read_sources


def generate_table(sources: typing.List[Source]) -> str:
    table = [
        [
            f"`{source.identifier}`",
            generate_rules_count_from_url(source.repo_url),
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


def generate_rules_count_from_url(repo_url: str) -> str:
    temp_dir_fn = tempfile.mkdtemp()

    git.Repo.clone_from(repo_url, temp_dir_fn)
    details = generate_rules_count_from_dir(temp_dir_fn)
    shutil.rmtree(temp_dir_fn)

    return details


def generate_rules_count_from_dir(location: str) -> str:
    counter = collections.Counter()
    for fn in pathlib.Path(location).rglob("*"):
        if fn.name.endswith(".yaml") or fn.name.endswith(".yml"):
            counter += process_rules_file(fn.resolve())

    return stringify_lang_counter(counter)


def process_rules_file(rules_file: str) -> collections.Counter:
    with open(rules_file, "r") as rules_fd:
        try:
            rules = yaml.safe_load(rules_fd)

            langs = []
            for rule in rules["rules"]:
                langs.extend(rule["languages"])

                return collections.Counter(langs)

        except (KeyError, yaml.composer.ComposerError):
            return collections.Counter([])


def stringify_lang_counter(counter: collections.Counter) -> str:
    return ", ".join(
        [f"`{lang}`: {count}" for lang, count in counter.most_common()]
    )


def main() -> None:
    sources = read_sources("/tmp")
    table = generate_table(sources)
    write_readmes(table)


if __name__ == "__main__":
    main()
