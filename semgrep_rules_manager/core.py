import typing

from semgrep_rules_manager.sources import Source, read_sources


def _execute_bulk_operation(
    download_dir: str,
    operation: typing.Callable[[Source], bool],
    source_id: str = None,
) -> int:
    counter = 0
    for source in read_sources(download_dir, source_id):
        if operation(source):
            counter += 1

    return counter


def get_sources(download_dir: str, source_id: str) -> typing.List[Source]:
    return list(read_sources(download_dir, source_id))


def download_sources(download_dir: str, source_id: str = None) -> int:
    def process_source(source: Source) -> bool:
        if not source.is_downloaded:
            source.download()

            return True

        return False

    return _execute_bulk_operation(download_dir, process_source, source_id)


def sync_sources(download_dir: str, source_id: str = None) -> int:
    def process_source(source: Source) -> bool:
        if source.is_downloaded and not source.is_synced:
            source.update()

            return True

        return False

    return _execute_bulk_operation(download_dir, process_source, source_id)


def delete_sources(download_dir: str, source_id: str = None) -> int:
    def process_source(source: Source) -> bool:
        if source.is_downloaded:
            source.remove()

            return True

        return False

    return _execute_bulk_operation(download_dir, process_source, source_id)
