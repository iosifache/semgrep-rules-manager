from dataclasses import dataclass
import typing


@dataclass
class Rule:
    languages: typing.List[str]
