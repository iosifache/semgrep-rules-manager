<p align="center">
    <img src="https://raw.githubusercontent.com/iosifache/semgrep-rules-manager/main/logo.png" height="256" alt="semgrep-rules-manager logo"/>
</p>

## Description

Despite the fact that there is an open source repository containing community rules, some Semgrep users prefer to keep their custom rules in repositories that they manage.

The goal of **`semgrep-rules-manager`** is to collect **high-quality Semgrep rules from third-party sources**. It allows you to examine information about a source, download it, and check for and retrieve remote updates. If a downloaded source no longer meets your requirements, `semgrep-rules-manager` can handle deletion procedures.

## Included Sources

| Identifier    | Included Rules per Language                                                                                                                                                                                                                                                                                                                                                                             | Author        | License   |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|-----------|
| `community`   | `hcl`: 354, `python`: 322, `javascript`: 283, `typescript`: 214, `regex`: 210, `java`: 135, `ruby`: 100, `generic`: 87, `yaml`: 85, `go`: 80, `php`: 57, `dockerfile`: 38, `csharp`: 34, `scala`: 25, `c`: 17, `ocaml`: 17, `kt`: 16, `C#`: 14, `rust`: 11, `json`: 10, `bash`: 7, `ts`: 5, `js`: 4, `html`: 3, `clojure`: 3, `terraform`: 3, `solidity`: 1, `swift`: 1, `kotlin`: 1, `lua`: 1, `sh`: 1 | Semgrep       | LGPL 2.1  |
| `gitlab`      | `python`: 98, `java`: 97, `scala`: 94, `c`: 72, `go`: 35, `csharp`: 23, `javascript`: 15, `typescript`: 13                                                                                                                                                                                                                                                                                              | GitLab        | MIT       |
| `trailofbits` | `python`: 19, `go`: 15, `js`: 7, `ts`: 7, `rust`: 1                                                                                                                                                                                                                                                                                                                                                     | Trail of Bits | AGPL-3.0  |
| `0xdea`       | `cpp`: 40, `c`: 39, `generic`: 1                                                                                                                                                                                                                                                                                                                                                                        | Marco Ivaldi  | MIT       |
| `elttam`      | `java`: 35, `generic`: 15, `yaml`: 7, `javascript`: 3, `go`: 3, `typescript`: 2, `kotlin`: 1, `python`: 1, `c`: 1, `csharp`: 1, `php`: 1                                                                                                                                                                                                                                                                | elttam        | MIT       |
| `kondukto`    | `php`: 5, `dockerfile`: 5, `java`: 3, `go`: 3                                                                                                                                                                                                                                                                                                                                                           | Kondukto      |           |
| `dgryski`     | `go`: 42                                                                                                                                                                                                                                                                                                                                                                                                | Damian Gryski | MIT       |

## Read Further

This is only an excerpt from the [`README.md` hosted on GitHub](https://github.com/iosifache/semgrep-rules-manager#readme).
