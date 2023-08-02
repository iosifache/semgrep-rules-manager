<p align="center">
    <img src="logo.png" height="256" alt="semgrep-rules-manager logo"/>
</p>
<h2 align="center">Manager of third-party sources of Semgrep rules</h2>
<p align="center" float="left">
    <img src="https://snapcraft.io/semgrep-rules-manager/badge.svg" height="17" alt="Snapcraft's Version"/>
    &nbsp; &nbsp;
    <img src="https://img.shields.io/pypi/v/semgrep-rules-manager?label=PyPi&color=1c8223" height="17" alt="PyPI's Version">
</p>

## Description

Despite the fact that there is an open source repository containing community rules, some Semgrep users prefer to keep their custom rules in repositories that they manage.

The goal of **`semgrep-rules-manager`** is to collect **high-quality Semgrep rules from third-party sources**. It allows you to examine information about a source, download it, and check for and retrieve remote updates. If a downloaded source no longer meets your requirements, `semgrep-rules-manager` can handle deletion procedures.

## Included Sources

All sources in `semgrep-rules-manager` are defined in `semgrep_rules_manager/data/sources.yaml`. They are listed in the table below.

| Identifier    | Included Rules per Language                                                                                                                                                                                                                                                                                                                                                                             | Author        | License   |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|-----------|
| `community`   | `hcl`: 354, `python`: 322, `javascript`: 283, `typescript`: 214, `regex`: 210, `java`: 135, `ruby`: 100, `generic`: 87, `yaml`: 85, `go`: 80, `php`: 57, `dockerfile`: 38, `csharp`: 34, `scala`: 25, `c`: 17, `ocaml`: 17, `kt`: 16, `C#`: 14, `rust`: 11, `json`: 10, `bash`: 7, `ts`: 5, `js`: 4, `html`: 3, `clojure`: 3, `terraform`: 3, `solidity`: 1, `swift`: 1, `kotlin`: 1, `lua`: 1, `sh`: 1 | Semgrep       | LGPL 2.1  |
| `gitlab`      | `python`: 98, `java`: 97, `scala`: 94, `c`: 72, `go`: 35, `csharp`: 23, `javascript`: 15, `typescript`: 13                                                                                                                                                                                                                                                                                              | GitLab        | MIT       |
| `trailofbits` | `python`: 19, `go`: 15, `js`: 7, `ts`: 7, `rust`: 1                                                                                                                                                                                                                                                                                                                                                     | Trail of Bits | AGPL-3.0  |
| `0xdea`       | `cpp`: 40, `c`: 39, `generic`: 1                                                                                                                                                                                                                                                                                                                                                                        | Marco Ivaldi  | MIT       |
| `elttam`      | `java`: 35, `generic`: 15, `yaml`: 7, `javascript`: 3, `go`: 3, `typescript`: 2, `kotlin`: 1, `python`: 1, `c`: 1, `csharp`: 1, `php`: 1                                                                                                                                                                                                                                                                | elttam        | MIT       |
| `kondukto`    | `php`: 5, `dockerfile`: 5, `java`: 3, `go`: 3                                                                                                                                                                                                                                                                                                                                                           | Kondukto      |           |
| `dgryski`     | `go`: 42                                                                                                                                                                                                                                                                                                                                                                                                | Damian Gryski | MIT       |

## Installation

Snap (`snap install semgrep-rules-manager`) or pip (`pip install semgrep-rules-manager`) are the simplest ways to install `semgrep-rules-manager`.

[![Get it from the Snap Store](https://snapcraft.io/static/images/badges/en/snap-store-black.svg)](https://snapcraft.io/semgrep-rules-manager)

If you don't want to use a package management, simply clone this repository and install Poetry as well as the Python dependencies (`poetry install`).

> See also: [Poetry | Installation](https://python-poetry.org/docs/#installation)

## Usage

1. Install `semgrep`: `snap install semgrep`
2. Install `semgrep-rules-manager`: `snap install semgrep-rules-manager`
3. Get help:

    ```bash
    $ semgrep-rules-manager --help
    Usage: semgrep-rules-manager [OPTIONS] COMMAND [ARGS]...

    Manages third-party sources of Semgrep rules.

    Options:
    --dir PATH  Directory in which the Semgrep rules are stored  [required]
    --help      Show this message and exit.

    Commands:
    download  Downloads sources.
    list      Lists sources.
    remove    Removes downloaded sources.
    sync      Syncs downloaded sources.
    ```

4. Download a source:

    ```bash
    $ semgrep-rules-manager --dir /home/iosifache/semgrep-rules download --source 0xdea
    ✅ The source was successfully downloaded.
    ```

5. List all sources:

    ```bash
    $ semgrep-rules-manager --dir /home/iosifache/semgrep-rules list     
                                                    Available sources of Semgrep rules                                                 
    ┏━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┓
    ┃ Identifier  ┃ Description                                                      ┃ Author        ┃ Downloaded ┃ Synced with remote ┃
    ┡━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━┩
    │ community   │ Official repository of rules                                     │ Semgrep       │ ❌         │ ❌                 │
    │ gitlab      │ Rules used in GitLab SAST                                        │ GitLab        │ ❌         │ ❌                 │
    │ trailofbits │ Rules used in the audits, research and projects of Trail of Bits │ Trail of Bits │ ❌         │ ❌                 │
    │ 0xdea       │ Custom rules written by Marco Ivaldi                             │ Marco Ivaldi  │ ✅         │ ✅                 │
    │ elttam      │ Custom rules used in elttam                                      │ elttam        │ ❌         │ ❌                 │
    │ kondukto    │ Custom rules used in Kondukto                                    │ Kondukto      │ ❌         │ ❌                 │
    └─────────────┴──────────────────────────────────────────────────────────────────┴───────────────┴────────────┴────────────────────┘
    ```

6. List only the downloaded source:

    ```bash
    $ semgrep-rules-manager --dir /home/iosifache/semgrep-rules list --source 0xdea
    Identifier: 0xdea
    Description: Custom rules written by Marco Ivaldi
    Resository URL: https://github.com/0xdea/semgrep-rules
    Repository brach: main
    Author: Marco Ivaldi
    License: MIT
    Downloaded: ✅ (in /home/iosifache/semgrep-rules/0xdea)
    Synced: ✅ because fd3bcad54de9dc76d4a8780a4125d42475d560ce (local) == fd3bcad54de9dc76d4a8780a4125d42475d560ce (remote)
    ```

7. Use the downloaded source to scan a codebase: `semgrep --config /home/iosifache/semgrep-rules .`
8. Sync the source:

    ```bash
    $ semgrep-rules-manager --dir /home/iosifache/semgrep-rules sync --source 0xdea
    ✅ All sources are already synced.
    ```
9. Remove the source

    ```bash
    $ semgrep-rules-manager --dir /home/iosifache/semgrep-rules remove --source 0xdea
    ✅ The source was successfully deleted.
    ```

## Acknowledgements

Thanks to the [Semgrep team](https://semgrep.dev) for making their work available to the open source community!

This project's logo was created with [Adobe Firefly](https://firefly.adobe.com).
