"""UI-layer exceptions for cliSoft.

Raised inside `ui/output.py` helpers when rendering or spinner operations
fail.  These are rarely expected in normal use but allow callers to
distinguish a rendering failure from a command failure.

Usage:
    from exceptions import RenderError, SpinnerError

    try:
        console.print(table)
    except Exception as exc_raw:
        raise RenderError(helper="print_table", original=exc_raw)

    try:
        with spinner("Working..."):
            do_work()
    except Exception as exc_raw:
        raise SpinnerError(operation="action-one")
"""

from __future__ import annotations

from exceptions import CLISoftError


class UIError(CLISoftError):
    """Base for all UI-layer errors."""

    def __init__(self, message: str) -> None:
        super().__init__(message=message, layer="ui")


class RenderError(UIError):
    """Raised when a Rich output helper fails to render its content.

    Attributes:
        helper:   Name of the ui/output.py function that failed
                  (e.g. "print_table").
        original: The underlying exception, if available.
    """

    def __init__(self, helper: str, original: Exception | None = None) -> None:
        self.helper = helper
        self.original = original
        super().__init__(message=f"Render error in '{helper}'")


class SpinnerError(UIError):
    """Raised when a spinner context manager fails during an operation.

    Attributes:
        operation: Label identifying the work that was running inside the
                   spinner (e.g. the command name or flow name).
    """

    def __init__(self, operation: str) -> None:
        self.operation = operation
        super().__init__(message=f"Spinner failed during '{operation}'")
