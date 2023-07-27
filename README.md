# `semgrep-rules-manager`

## Description

`semgrep-rules-manager` is a manager of third-party sources of Semgrep rules.

All available sources are listed in `sources.yaml`.

## Usage

### Download

```bash
$ semgrep-rules-manager --dir /home/iosifache/semgrep-rules download
✅ 6 sources were successfully downloaded
```

```bash
$ semgrep-rules-manager --dir /home/iosifache/semgrep-rules download --source 0xdea
✅ The source was successfully downloaded.
```

### List

```bash
$ semgrep-rules-manager --dir /home/iosifache/semgrep-rules list     
                                                 Available sources of Semgrep rules                                                 
┏━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┓
┃ Identifier  ┃ Description                                                      ┃ Author        ┃ Downloaded ┃ Synced with remote ┃
┡━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━┩
│ community   │ Official repository of rules                                     │ Semgrep       │ ✅         │ ✅                 │
│ gitlab      │ Rules used in GitLab SAST                                        │ GitLab        │ ✅         │ ✅                 │
│ trailofbits │ Rules used in the audits, research and projects of Trail of Bits │ Trail of Bits │ ✅         │ ✅                 │
│ 0xdea       │ Custom rules written by Marco Ivaldi                             │ Marco Ivaldi  │ ✅         │ ✅                 │
│ elttam      │ Custom rules used in elttam                                      │ elttam        │ ✅         │ ✅                 │
│ kondukto    │ Custom rules used in Kondukto                                    │ Kondukto      │ ✅         │ ✅                 │
└─────────────┴──────────────────────────────────────────────────────────────────┴───────────────┴────────────┴────────────────────┘
```

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

### Sync

```bash
$ semgrep-rules-manager --dir /home/iosifache/semgrep-rules sync
✅ All sources are already synced.
```

```bash
$ semgrep-rules-manager --dir /home/iosifache/semgrep-rules sync --source 0xdea
✅ All sources are already synced.
```

### Remove

```bash
$ semgrep-rules-manager --dir /home/iosifache/semgrep-rules remove               
✅ 6 sources were successfully deleted
```

```bash
$ semgrep-rules-manager --dir /home/iosifache/semgrep-rules remove --source 0xdea
✅ The source was successfully deleted.
```
