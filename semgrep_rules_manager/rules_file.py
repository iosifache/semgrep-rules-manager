from dataclasses import dataclass
import collections
import yaml


from helpers import translate_lang_id_to_name


@dataclass
class RulesFile:
    location: str

    def get_rules_per_lang(
        self, beautified: bool = False
    ) -> collections.Counter:
        with open(self.location, "r", encoding="utf-8") as rules_fd:
            try:
                rules = yaml.safe_load(rules_fd)

                langs = []
                for rule in rules["rules"]:
                    languages = rule["languages"]
                    if beautified:
                        languages = [
                            translate_lang_id_to_name(lang)
                            for lang in languages
                        ]
                    langs.extend(languages)

                    return collections.Counter(langs)

            except (KeyError, yaml.composer.ComposerError):
                return collections.Counter([])
