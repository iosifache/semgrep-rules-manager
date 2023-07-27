import yaml
from dataclasses import dataclass
import typing
import os


@dataclass
class Source:
    identifier: str
    description: str
    repo_url: str
    author: str
    license: str
    is_downloaded: bool


def read_sources() -> typing.Generator[Source, None, None]:
    sources_fn = os.path.join(os.path.dirname(__file__), os.pardir, "sources.yaml")
    with open(sources_fn, "r") as sources_fd:
        sources = yaml.load(sources_fd, Loader=yaml.SafeLoader)

        for key, details in sources.items():
            yield (
                key,
                details["description"],
                details["repository_url"],
                details["author"],
                details["license"],
                False,
            )
