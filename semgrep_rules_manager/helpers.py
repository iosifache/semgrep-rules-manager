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


def translate_lang_id_to_name(identifier: str) -> str:
    for key, value in LOOKUP_TABLE.items():
        if identifier in value:
            return key

    raise LanguageIDNotFoundException()


class LanguageIDNotFoundException(SemgrepRulesManagerException):
    """A language identifier was not found."""
