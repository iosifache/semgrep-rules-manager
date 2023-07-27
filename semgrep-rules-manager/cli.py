#!/usr/bin/python3

import click

@click.group()
def cli():
    pass

@cli.command
def download() -> None:
    print("Download..")

if __name__ == "__main__":
    cli()
