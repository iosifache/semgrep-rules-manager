import os
import re
import shutil
import typing
from abc import abstractmethod
from dataclasses import dataclass

import git
import yaml

from semgrep_rules_manager.exception import SemgrepRulesManagerException


class Preprocessor:
    IDENTIFIER = None
    location: str

    def __init__(self, location: str) -> None:
        self.location = location

    @abstractmethod
    def preprocess(self) -> None:
        pass


class IDStandardizationPreprocessor(Preprocessor):
    IDENTIFIER = "id-standardization"

    def __init__(self, location: str):
        super().__init__(location)

    def preprocess(self) -> None:
        for file in self._get_all_yaml_files():
            self.process_content(file)

    def process_content(self, filename: str) -> None:
        with open(filename, "r+") as file:
            content = file.read()

            new_content = re.sub(
                r"\n- id: \".*\/(.*)\"\n", r"\n- id: \1\n", content
            )

            file.seek(0)
            file.truncate()
            file.write(new_content)

    def _get_all_yaml_files(self) -> typing.Generator[str, None, None]:
        for root, _, files in os.walk(self.location):
            for file in files:
                if file.endswith(".yaml") or file.endswith(".yml"):
                    yield os.path.join(root, file)


class PreprocessorsFactory:
    known_preprocessors = [IDStandardizationPreprocessor]

    @staticmethod
    def create(identifier: str, location: str) -> Preprocessor:
        for preprocessor in PreprocessorsFactory.known_preprocessors:
            if preprocessor.IDENTIFIER == identifier:
                return preprocessor(location)

        raise PreprocessorNotFoundException()


@dataclass
class Source:
    identifier: str
    description: str
    repo_url: str
    repo_brach: str
    author: str
    license: str
    preprocessors_ids: typing.List[str]
    ignored: typing.List[str]
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

        self._preprocess()
        self._remove_ignored()

    def _preprocess(self) -> None:
        for preprocessor_id in self.preprocessors_ids:
            preprocessor = PreprocessorsFactory.create(
                preprocessor_id, self.location
            )

            preprocessor.preprocess()

    def _remove_ignored(self) -> None:
        for current_ignored in self.ignored:
            path = os.path.join(self.location, current_ignored)

            if os.path.isfile(path):
                os.remove(path)
            elif os.path.isdir(path):
                shutil.rmtree(path)

    def update(self) -> None:
        repo = git.Repo(self.location)
        origin = repo.remotes.origin
        origin.pull()

    def remove(self) -> None:
        if self.is_downloaded:
            shutil.rmtree(self.location)


def read_sources(
    download_dir: str, identifier: str = None
) -> typing.Generator[Source, None, None]:
    sources_fn = os.path.join(os.path.dirname(__file__), "data/sources.yaml")
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
                details.get("preprocessors", []),
                details.get("ignored", []),
                location,
            )
            yield_once = True

            if identifier and identifier == key:
                break

        if identifier and not yield_once:
            raise SourceNotFoundException()


class PreprocessorNotFoundException(SemgrepRulesManagerException):
    """A preprocessor specified in sources YAML is not implemented."""


class SourceNotFoundException(SemgrepRulesManagerException):
    """The specified source was not found."""
