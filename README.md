# CliPlate

A reusable Python CLI boilerplate built with [Rich](https://github.com/Textualize/rich) and [InquirerPy](https://github.com/kazhala/InquirerPy). Drop it into any project and replace the placeholder actions with your own logic to get a fully styled, interactive terminal application in minutes.

---

## Features

- Interactive arrow-key menu with a welcome panel and clean exit
- Styled terminal output with consistent symbols for errors, success, info, and warnings
- Animated spinner shown while any action runs
- Rich tables for structured result display
- "Go back" navigation from every action screen — no dead ends
- Every command returns a dataclass with an `error` field — uniform, predictable error handling

---

## Stack

| Library | Purpose |
|---|---|
| [Rich](https://github.com/Textualize/rich) | Styled terminal output: panels, tables, spinners, color |
| [InquirerPy](https://github.com/kazhala/InquirerPy) | Interactive prompts: select, text, confirm, checkbox |
| argparse | Subcommand parsing for non-interactive use |
| Python 3.10+ | Required for `str \| None` union syntax in dataclasses |

---

## Project Structure

```
cliSoft/
├── cli.py                    # Entry point; argparse subcommands; falls through to interactive mode
├── requirements.txt          # InquirerPy, Rich
├── prompts/
│   └── interactive.py        # All InquirerPy flows; dispatches to commands/
├── ui/
│   └── output.py             # Single Console() instance; all output helpers
└── commands/
    ├── action_one.py         # Template action one   -> ActionOneResult dataclass
    ├── action_two.py         # Template action two   -> ActionTwoResult dataclass
    └── action_three.py       # Template action three -> ActionThreeResult dataclass
```

---

## Getting Started

**Install dependencies**

```bash
pip install -r requirements.txt
```

**Run the CLI**

```bash
python cli.py
```

This opens the interactive menu. The three placeholder actions each run a simulated flow (spinner + table) so you can see the full UI stack before writing any real logic.

**Run a subcommand directly**

```bash
python cli.py action-one
python cli.py action-two
python cli.py action-three
```

---

## How to Adapt It to Your Project

### Step 1 — Rename the actions in `prompts/interactive.py`

Open `interactive.py` and update the `_ACTIONS` dict to use labels that match your domain:

```python
# Before
_ACTIONS = {
    "Action One":   "_flow_action_one",
    "Action Two":   "_flow_action_two",
    "Action Three": "_flow_action_three",
    "Exit":         None,
}

# After (example)
_ACTIONS = {
    "Scan dependencies": "_flow_scan",
    "Deploy":            "_flow_deploy",
    "Migrate database":  "_flow_migrate",
    "Exit":              None,
}
```

Rename the corresponding `_flow_*` functions to match, and update the welcome panel title in `start_interactive()`.

### Step 2 — Add real logic in `commands/action_*.py`

Each command module contains a clearly marked `TODO` block. Replace it with your implementation:

```python
def run_action_one(target: str, option: int = 10) -> ActionOneResult:
    time.sleep(1.5)  # remove once real I/O provides natural delay

    # ── TODO: replace this block with real logic ──────────────────────────────
    try:
        data = your_library.run(target, limit=option)
    except YourError as exc:
        return ActionOneResult(error=str(exc))

    rows = [{"label": item.name, ...} for item in data.items]
    return ActionOneResult(rows=rows, total_count=data.total, error=None)
    # ── end TODO ──────────────────────────────────────────────────────────────
```

Rename the dataclass and function to something meaningful (e.g. `ScanResult` / `run_scan`), and update the field names to match what your logic produces. The `error: str | None` field must always be present.

### Step 3 — Update prompts and messages in each `_flow_*` function

Each flow function in `prompts/interactive.py` contains inline comments marking every string to customize: the `print_info` message, prompt text, `instruction=` context, table column headers, and any warning thresholds.

```python
def _flow_action_one() -> None:
    console.print()
    # Customize: replace this message with a description of what this action does.
    print_info("Action One — add your logic here.")
    inquirer.select(message="", choices=["← Go back"]).execute()
```

For actions that need user input, follow the full command flow pattern: collect with `inquirer.text()` / `inquirer.number()`, run logic under `with spinner("...")`, then check `result.error` before rendering output.

---

## UI Helpers Reference

All helpers live in `ui/output.py` and use the single shared `Console()` instance.

```python
from ui.output import (
    console,
    print_error,
    print_success,
    print_info,
    print_warn,
    print_welcome,
    print_table,
    spinner,
)
```

| Helper | Description |
|---|---|
| `console` | The single shared `rich.Console` instance; use for low-level `console.print()` calls |
| `print_error(msg)` | Prints `✖ msg` in red bold |
| `print_success(msg)` | Prints `✔ msg` in green bold |
| `print_info(msg)` | Prints `ℹ msg` in blue bold |
| `print_warn(msg)` | Prints `⚠ msg` in yellow bold |
| `print_welcome(title, subtitle)` | Prints a rounded cyan panel with a title and an optional dim subtitle |
| `print_table(title, columns, rows)` | Renders a Rich table; `columns` is a list of `(header, style)` tuples |
| `spinner(message)` | Context manager that shows an animated spinner; clears itself on exit |

Example usage:

```python
from ui.output import spinner, print_success, print_error

with spinner("Running scan..."):
    result = run_scan(target, limit)

if result.error:
    print_error(result.error)
else:
    print_success(f"Scan complete — {result.total_count} items found")
```

---

## Architecture Rules

- `ui/output.py` owns the **single** `Console()` instance. No other module may create its own `Console()` or call `print()` directly.
- `commands/` modules contain **pure logic only** — no imports from `ui/` or `prompts/`. They accept plain arguments and return a dataclass.
- Every command function must return a dataclass with an `error: str | None` field. Always check `result.error` before rendering output.
- `prompts/interactive.py` is the **only** layer that imports from both `ui/` and `commands/` — it is the bridge between user input and business logic.

---

## License

MIT