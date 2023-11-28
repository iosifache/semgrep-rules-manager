from dataclasses import dataclass
import collections
import yaml
import typing


from semgrep_rules_manager.helpers import translate_lang_id_to_name
from semgrep_rules_manager.rule import Rule, Severity
from semgrep_rules_manager.exception import SemgrepRulesManagerException


@dataclass
class RulesFile:
    location: str
    rules: typing.List[Rule]

    def __init__(self, location: str) -> None:
        with open(location, "r", encoding="utf-8") as rules_fd:
            try:
                raw_rules = yaml.safe_load(rules_fd)

                self.rules = [
                    Rule(
                        rule.get("id", ""),
                        rule.get("languages", ""),
                        rule.get("message", ""),
                        Severity[rule.get("severity", Severity.UNKNOWN.name)],
                    )
                    for rule in raw_rules.get("rules", [])
                    if rule.get("languages", False)
                ]

            except (KeyError, yaml.composer.ComposerError):
                raise InvalidRulesFileException()

        self.location = location

    def get_rules_per_lang(
        self, beautified: bool = False
    ) -> collections.Counter:
        langs = []
        for rule in self.rules:
            languages = (
                [translate_lang_id_to_name(lang) for lang in rule.languages]
                if beautified
                else rule.languages
            )
            langs.extend(languages)

        return collections.Counter(langs)


class InvalidRulesFileException(SemgrepRulesManagerException):
    """The rule files is invalid and cannot be loaded."""
