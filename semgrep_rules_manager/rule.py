from dataclasses import dataclass
import typing
from enum import Enum, auto


class Severity(Enum):
    ERROR = auto()
    WARNING = auto()
    INFO = auto()
    UNKNOWN = auto()


@dataclass
class Rule:
    identifier: str
    languages: typing.List[str]
    message: str
    severity: Severity
