from sources import read_sources, Source
import typing


def get_sources(download_dir: str, source_id: str) -> typing.List[Source]:
    return list(read_sources(download_dir, source_id))


def download_sources(download_dir: str, source_id: str = None) -> None:
    downloaded = 0
    for source in read_sources(download_dir, source_id):
        if not source.is_downloaded:
            source.download()

            downloaded += 1

    return downloaded


def update_sources(download_dir: str, source_id: str = None) -> None:
    pass


def delete_sources(download_dir: str, source_id: str = None) -> None:
    removed = 0
    for source in read_sources(download_dir, source_id):
        if source.is_downloaded:
            source.remove()

            removed += 1

    return removed
