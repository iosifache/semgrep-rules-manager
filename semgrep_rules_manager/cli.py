#!/usr/bin/python3

import typing

import click
from rich.console import Console
from rich.table import Table

from semgrep_rules_manager.core import (
    Source,
    delete_sources,
    download_sources,
    get_sources,
    sync_sources,
)
from semgrep_rules_manager.exception import SemgrepRulesManagerException

console = Console()


@click.group()
@click.pass_context
@click.option(
    "--dir",
    type=click.Path(exists=True, writable=True, dir_okay=True),
    required=True,
    help="Directory in which the Semgrep rules are stored",
)
def cli(ctx: click.Context, dir: str):
    """Manages third-party sources of Semgrep rules."""
    ctx.ensure_object(dict)

    ctx.obj["WORKING_DIR"] = dir


@cli.command(name="list")
@click.pass_context
@click.option(
    "--source",
    type=str,
    help="Identifier of a source",
)
def list_cmd(ctx: click.Context, source: str = None) -> None:
    """Lists sources."""
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
@click.option(
    "--source",
    type=str,
    help="Identifier of a source",
)
def download(ctx: click.Context, source: str = None) -> None:
    """Downloads sources."""
    download_dir = ctx.obj["WORKING_DIR"]

    sources_count = download_sources(download_dir, source)

    if sources_count == 1:
        console.print(
            ":white_check_mark: The source was successfully downloaded."
        )
    else:
        console.print(
            f":white_check_mark: {sources_count} sources were successfully"
            " downloaded"
        )


@cli.command
@click.pass_context
@click.option(
    "--source",
    type=str,
    help="Identifier of a source",
)
def remove(ctx: click.Context, source: str = None) -> None:
    """Removes downloaded sources."""
    download_dir = ctx.obj["WORKING_DIR"]

    sources_count = delete_sources(download_dir, source)

    if sources_count == 1:
        console.print(
            ":white_check_mark: The source was successfully deleted."
        )
    else:
        console.print(
            f":white_check_mark: {sources_count} sources were successfully"
            " deleted"
        )


@cli.command
@click.pass_context
@click.option(
    "--source",
    type=str,
    help="Identifier of a source",
)
def sync(ctx: click.Context, source: str = None) -> None:
    """Syncs downloaded sources."""
    download_dir = ctx.obj["WORKING_DIR"]

    sources_count = sync_sources(download_dir, source)

    if sources_count == 0:
        console.print(":white_check_mark: All sources are already synced.")
    elif sources_count == 1:
        console.print(":white_check_mark: The source was successfully synced.")
    else:
        console.print(
            f":white_check_mark: {sources_count} sources were successfully"
            " synced"
        )


def main() -> None:
    try:
        cli()
    except SemgrepRulesManagerException as e:
        console.print(f":exclamation: {str(e)}")


if __name__ == "__main__":
    main()
