## kak-rope

Integrating [rope](https://github.com/python-rope/rope) refactoring
library with kakoune.

## Installation

First, install the `kak-rope` binary and its dependencies:

```bash
pipx install kak-rope
```

Then, configure kakoune, for instance using `plug.kak`:


```
plug "git+https://git.sr.ht/~dmerej/kak-rope" config %{
  # Suggested mappings
  declare-user-mode rope
  map global user r ' :enter-user-mode rope<ret>' -docstring 'enter rope mode'
  map global rope a ':rope-add-import ' -docstring 'add import'
}
```

## Usage

See builtin kakoune help. All commands defined in this module starts with `rope-`.

## Contributing

* Install [poetry](https://python-poetry.org/)
* Install required dependencies

```
poetry install
```

Before submitting a change, run the following commands:

```
poetry run invoke lint
```

You can now use [git-send-email](https://git-send-email.io/) and send a patch to  https://lists.sr.ht/~dmerej/kak-rope
