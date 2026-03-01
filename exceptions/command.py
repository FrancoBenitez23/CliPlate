"""Command-layer exceptions for cliSoft.

Raised inside `commands/` modules when a command fails to execute correctly.
Callers (prompts/interactive.py, cli.py) catch these to display error output
via ui/output.py without the command modules needing to import any UI code.

Usage:
    from exceptions import CommandExecutionError, CommandTimeoutError

    raise CommandTimeoutError(command_name="action-one", timeout_s=30.0)

    try:
        result = your_library.run(target)
    except Exception as exc_raw:
        raise CommandExecutionError(
            message=str(exc_raw),
            command_name="action-one",
            original=exc_raw,
        )
"""

from __future__ import annotations

from exceptions import CLISoftError


class CommandError(CLISoftError):
    """Base for all command-layer errors.

    Attributes:
        command_name: The name of the command that failed (e.g. "action-one").
    """

    def __init__(self, message: str, command_name: str) -> None:
        self.command_name = command_name
        super().__init__(message=message, layer="command")


class CommandExecutionError(CommandError):
    """Raised when a command fails during execution.

    Wraps the original exception so the full traceback is available to
    callers that want to log it, while the `message` attribute is safe to
    display directly to the user.

    Attributes:
        command_name: Name of the command that failed.
        original:     The underlying exception, if available.
    """

    def __init__(
        self,
        message: str,
        command_name: str,
        original: Exception | None = None,
    ) -> None:
        self.original = original
        super().__init__(message=message, command_name=command_name)


class CommandTimeoutError(CommandError):
    """Raised when a command exceeds its allowed execution time.

    Attributes:
        command_name: Name of the command that timed out.
        timeout_s:    The timeout threshold in seconds.
    """

    def __init__(self, command_name: str, timeout_s: float) -> None:
        self.timeout_s = timeout_s
        super().__init__(
            message=f"Command '{command_name}' timed out after {timeout_s}s",
            command_name=command_name,
        )
