#!/usr/bin/python3

import click
import typing

from core import get_sources, Source

from rich.console import Console
from rich.table import Table
from exception import SemgrepRulesManagerException

console = Console()


@click.group()
@click.pass_context
@click.option(
    "--dir",
    type=click.Path(exists=True, writable=True, dir_okay=True),
    required=True,
    help="Directory in which the Semgrep rules are stores",
)
def cli(ctx: click.Context, dir: str):
    ctx.ensure_object(dict)

    ctx.obj["WORKING_DIR"] = dir


@cli.command
@click.pass_context
@click.option(
    "--source",
    type=str,
    help="Identifier of a source",
)
def get(ctx: click.Context, source: str = None) -> None:
    download_dir = ctx.obj["WORKING_DIR"]

    sources = get_sources(download_dir, source)
    if source:
        output = _create_description_of_source(sources[0])
    else:
        output = _create_table_for_sources(sources)

    console.print(output)


def _create_description_of_source(source: Source) -> str:
    download_text = (
        f":white_check_mark: (in {source.location})"
        if source.is_downloaded
        else ":x:"
    )
    sync_text = _create_sync_text(source)

    return f"""[bold]Identifier[/bold]: {source.identifier}
[bold]Description[/bold]: {source.description}
[bold]Resository URL[/bold]: {source.repo_url}
[bold]Repository brach[/bold]: {source.repo_brach}
[bold]Author[/bold]: {source.author}
[bold]License[/bold]: {source.license}
[bold]Downloaded[/bold]: {download_text}
[bold]Synced[/bold]: {sync_text}"""


def _create_sync_text(source: Source) -> str:
    if source.local_commit is not None and source.remote_commit is not None:
        comparison_sign = "==" if source.is_synced else "!="
        comparison_reason = (
            f" because {source.local_commit} (local)"
            f" {comparison_sign} {source.remote_commit} (remote)"
        )
    else:
        comparison_reason = ""

    synced_text = ":white_check_mark:" if source.is_synced else ":x:"
    synced_text += comparison_reason

    return synced_text


def _create_table_for_sources(sources: typing.List[Source]) -> Table:
    table = Table(title="Available sources of Semgrep rules")

    table.add_column("Identifier")
    table.add_column("Description")
    table.add_column("Author")
    table.add_column("Downloaded")
    table.add_column("Synced with remote")

    for source in sources:
        is_downloaded = ":white_check_mark:" if source.is_downloaded else ":x:"
        is_synced = ":white_check_mark:" if source.is_synced else ":x:"

        table.add_row(
            source.identifier,
            source.description,
            source.author,
            is_downloaded,
            is_synced,
        )

    return table


@cli.command
@click.pass_context
def download(ctx: click.Context) -> None:
    print(f"Download to {ctx.obj['WORKING_DIR']}")


@cli.command
@click.pass_context
def remove(ctx: click.Context) -> None:
    print(f"Remove from {ctx.obj['WORKING_DIR']}")


def main() -> None:
    try:
        cli()
    except SemgrepRulesManagerException as e:
        console.print(f":exclamation: {str(e)}")


if __name__ == "__main__":
    main()
