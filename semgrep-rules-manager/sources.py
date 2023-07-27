import yaml
from dataclasses import dataclass
import typing
import os
import git
import shutil

from exception import SemgrepRulesManagerException


@dataclass
class Source:
    identifier: str
    description: str
    repo_url: str
    repo_brach: str
    author: str
    license: str
    location: str
    is_downloaded: bool = False
    local_commit: str = None
    remote_commit: str = None
    is_synced: bool = False

    def __post_init__(self) -> None:
        self.is_downloaded = os.path.isdir(self.location)
        if self.is_downloaded:
            self.local_commit = self._get_last_local_commit()
            self.remote_commit = self._get_last_remote_commit()
            self.is_synced = self.local_commit == self.remote_commit

    def _get_last_local_commit(self) -> str:
        repo = git.Repo(self.location)

        return repo.head.object.hexsha

    def _get_last_remote_commit(self) -> str:
        repo = git.Repo(self.location)

        return repo.rev_parse("origin/" + self.repo_brach).hexsha

    def download(self) -> None:
        git.Repo.clone_from(self.repo_url, self.location)

    def remove(self) -> None:
        if self.is_downloaded:
            shutil.rmtree(self.location)


def read_sources(
    download_dir: str, identifier: str
) -> typing.Generator[Source, None, None]:
    sources_fn = os.path.join(
        os.path.dirname(__file__), os.pardir, "sources.yaml"
    )
    with open(sources_fn, "r") as sources_fd:
        sources = yaml.load(sources_fd, Loader=yaml.SafeLoader)

        yield_once = False
        for key, details in sources.items():
            if identifier and identifier != key:
                continue

            location = os.path.join(download_dir, key)

            yield Source(
                key,
                details["description"],
                details["repository_url"],
                details["repository_branch"],
                details["author"],
                details["license"],
                location,
            )
            yield_once = True

            if identifier and identifier == key:
                break

        if identifier and not yield_once:
            raise SourceNotFoundException()


class SourceNotFoundException(SemgrepRulesManagerException):
    """The specified source was not found."""
