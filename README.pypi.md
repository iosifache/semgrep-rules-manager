<p align="center">
    <img src="https://raw.githubusercontent.com/iosifache/semgrep-rules-manager/main/logo.png" height="256" alt="semgrep-rules-manager logo"/>
</p>

## Description

Despite the fact that there is an open source repository containing community rules, some Semgrep users prefer to keep their custom rules in repositories that they manage.

The goal of **`semgrep-rules-manager`** is to collect **high-quality Semgrep rules from third-party sources**. It allows you to examine information about a source, download it, and check for and retrieve remote updates. If a downloaded source no longer meets your requirements, `semgrep-rules-manager` can handle deletion procedures.

## Included rules

[This online search engine](https://semgrep.iosifache.me) allows you to explore the rules included in `semgrep-rules-manager`.

## Included sources

| Identifier    | Rules per Language                                                                                                                                                                                                                                                                                                                                                                                           | Author         | License   |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|-----------|
| `community`   | 374 for Python, 362 for Terraform, 237 for Regex, 210 for JavaScript, 204 for TypeScript, 126 for Java, 107 for YAML, 94 for Go, 93 for Generic, 87 for Ruby, 59 for PHP, 50 for Solidity, 49 for C#, 37 for Dockerfile, 34 for OCaml, 25 for Scala, 24 for JSON, 19 for Kotlin, 17 for C, 12 for Apex, 11 for Rust, 9 for Bash, 7 for Elixir, 7 for Swift, 5 for Clojure, 4 for HTML, 1 for Dart, 1 for Lua | Semgrep        | LGPL 2.1  |
| `gitlab`      | 101 for Java, 96 for JavaScript, 88 for Scala, 81 for Python, 62 for C, 62 for C++, 58 for Kotlin, 40 for Ruby, 27 for Go, 22 for C#, 14 for TypeScript, 9 for PHP, 5 for Swift, 2 for Generic                                                                                                                                                                                                               | GitLab         | MIT       |
| `trailofbits` | 24 for Python, 17 for YAML, 16 for Go, 11 for Generic, 9 for JavaScript, 9 for TypeScript, 2 for Java, 2 for Kotlin, 1 for Rust                                                                                                                                                                                                                                                                              | Trail of Bits  | AGPL-3.0  |
| `0xdea`       | 47 for C++, 46 for C, 1 for Generic                                                                                                                                                                                                                                                                                                                                                                          | Marco Ivaldi   | MIT       |
| `elttam`      | 40 for Java, 15 for Generic, 7 for YAML, 3 for JavaScript, 3 for Go, 2 for TypeScript, 1 for Python, 1 for Kotlin, 1 for C#, 1 for C, 1 for PHP                                                                                                                                                                                                                                                              | elttam         | MIT       |
| `kondukto`    | 5 for Dockerfile, 5 for PHP, 3 for Go, 3 for Java                                                                                                                                                                                                                                                                                                                                                            | Kondukto       |           |
| `dgryski`     | 66 for Go                                                                                                                                                                                                                                                                                                                                                                                                    | Damian Gryski  | MIT       |
| `dotta`       | 7 for PHP, 3 for Kotlin, 1 for Java                                                                                                                                                                                                                                                                                                                                                                          | Federico Dotta | MIT       |
| `hashicorp`   | 4 for Terraform, 1 for Generic                                                                                                                                                                                                                                                                                                                                                                               | Hashicorp      | MPL-2.0   |

## Read more

This is only an excerpt from the [`README.md` hosted on GitHub](https://github.com/iosifache/semgrep-rules-manager#readme).
