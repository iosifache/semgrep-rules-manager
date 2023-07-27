from sources import read_sources, Source
import typing
import os


def get_sources(download_dir: str, identifier: str) -> typing.List[Source]:
    return list(read_sources(download_dir, identifier))


def download_source(download_dir: str, source_id: str = None) -> None:
    pass


def update_source(download_dir: str, source_id: str = None) -> None:
    pass


def remove_source(download_dir: str, source_id: str = None) -> None:
    pass
