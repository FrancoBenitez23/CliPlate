"""Centralized Rich Console, spinners, panels, and output helpers.

This module owns the single `Console()` instance for the entire application.
All output must go through the helpers defined here — no other module should
create its own `Console()` or call `print()` directly.

To customize the visual style:
  - Change `box.ROUNDED` / `box.SIMPLE_HEAVY` to another Rich box style.
  - Change the border and text styles in `print_welcome`.
  - Add new helper functions following the same pattern as `print_error` etc.
"""

from contextlib import contextmanager

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import SpinnerColumn, TextColumn, Progress
from rich import box

# Single Console instance shared across the entire application.
# Import this directly when you need low-level access: `from ui.output import console`.
console = Console()


# ── Status symbols ────────────────────────────────────────────────────────────
# Change these if you prefer different glyphs or color schemes.
SYM_ERROR   = "[bold red]✖[/bold red]"
SYM_SUCCESS = "[bold green]✔[/bold green]"
SYM_INFO    = "[bold blue]ℹ[/bold blue]"
SYM_WARN    = "[bold yellow]⚠[/bold yellow]"


def print_error(msg: str) -> None:
    """Print a red error message prefixed with the error symbol (✖)."""
    console.print(f"{SYM_ERROR}  {msg}")


def print_success(msg: str) -> None:
    """Print a green success message prefixed with the success symbol (✔)."""
    console.print(f"{SYM_SUCCESS}  {msg}")


def print_info(msg: str) -> None:
    """Print a blue informational message prefixed with the info symbol (ℹ)."""
    console.print(f"{SYM_INFO}  {msg}")


def print_warn(msg: str) -> None:
    """Print a yellow warning message prefixed with the warning symbol (⚠)."""
    console.print(f"{SYM_WARN}  {msg}")


def print_welcome(title: str, subtitle: str = "") -> None:
    """Print a rounded cyan panel with a title and an optional subtitle.

    Args:
        title:    Main heading displayed in bold cyan inside the panel.
        subtitle: Optional secondary line displayed in dim text below the title.
    """
    content = f"[bold cyan]{title}[/bold cyan]"
    if subtitle:
        content += f"\n[dim]{subtitle}[/dim]"
    console.print(Panel(content, box=box.ROUNDED, border_style="cyan", padding=(1, 4)))


@contextmanager
def spinner(message: str):
    """Context manager that shows an animated spinner while work is in progress.

    Usage:
        with spinner("Loading data..."):
            result = do_expensive_work()

    Args:
        message: Text displayed next to the spinner animation.
    """
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
        transient=True,  # Clears the spinner line when the block exits.
    ) as progress:
        progress.add_task(description=message, total=None)
        yield


def print_table(title: str, columns: list[tuple[str, str]], rows: list[list]) -> None:
    """Render a Rich table with a title, styled columns, and data rows.

    Args:
        title:   Text displayed above the table.
        columns: List of (header_name, rich_style) tuples, one per column.
                 Example: [("Name", "bold cyan"), ("Value", "white")]
        rows:    List of row value lists; each inner list must have the same
                 length as `columns`.  All values are coerced to strings.
    """
    table = Table(title=title, box=box.SIMPLE_HEAVY, show_lines=False)
    for name, style in columns:
        table.add_column(name, style=style, no_wrap=True)
    for row in rows:
        table.add_row(*[str(v) for v in row])
    console.print(table)
