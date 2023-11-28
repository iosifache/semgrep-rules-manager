from dataclasses import dataclass
import collections
import yaml

from semgrep_rules_manager.exception import SemgrepRulesManagerException

LOOKUP_TABLE = {
    "Apex": ["apex"],
    "Bash": ["bash", "sh"],
    "C": ["c"],
    "Cairo": ["cairo"],
    "Clojure": ["clojure"],
    "C++": ["cpp", "c++"],
    "C#": ["csharp", "c#", "C#"],
    "Dart": ["dart"],
    "Dockerfile": ["dockerfile", "docker"],
    "Elixir": ["ex", "elixir"],
    "Generic": ["generic"],
    "Go": ["go", "golang"],
    "HTML": ["html"],
    "Java": ["java"],
    "JavaScript": ["js", "javascript"],
    "JSON": ["json"],
    "Jsonnet": ["jsonnet"],
    "JSX": ["js", "javascript"],
    "Julia": ["julia"],
    "Kotlin": ["kt", "kotlin"],
    "Lisp": ["lisp"],
    "Lua": ["lua"],
    "OCaml": ["ocaml"],
    "PHP": ["php"],
    "Python": ["python", "python2", "python3", "py"],
    "R": ["r"],
    "Ruby": ["ruby"],
    "Rust": ["rust"],
    "Scala": ["scala"],
    "Scheme": ["scheme"],
    "Solidity": ["solidity", "sol"],
    "Swift": ["swift"],
    "Terraform": ["tf", "hcl", "terraform"],
    "TypeScript": ["ts", "typescript"],
    "YAML": ["yaml"],
    "XML": ["xml"],
    "Regex": ["regex"],
}


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


def translate_lang_id_to_name(identifier: str) -> str:
    for key, value in LOOKUP_TABLE.items():
        if identifier in value:
            return key

    raise LanguageIDNotFoundException()


class LanguageIDNotFoundException(SemgrepRulesManagerException):
    """A language identifier was not found."""
