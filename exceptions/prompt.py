"""Prompt-layer exceptions for cliSoft.

Raised inside `prompts/` modules when an interactive flow is interrupted or
receives invalid input.  cli.py catches PromptAbortedError to handle a clean
user-initiated cancel without printing a full error message.

Usage:
    from exceptions import PromptAbortedError, PromptValidationError

    try:
        answer = inquirer.text(...).execute()
    except KeyboardInterrupt:
        raise PromptAbortedError(flow_name="action-one")

    if not answer.strip():
        raise PromptValidationError(field="target", reason="cannot be empty")
"""

from exceptions import CLISoftError


class PromptError(CLISoftError):
    """Base for all prompt-layer errors."""

    def __init__(self, message: str) -> None:
        super().__init__(message=message, layer="prompt")


class PromptAbortedError(PromptError):
    """Raised when the user deliberately cancels an interactive flow.

    cli.py catches this to exit cleanly with a warning instead of an error.

    Attributes:
        flow_name: The name of the flow that was aborted (e.g. "action-one").
    """

    def __init__(self, flow_name: str) -> None:
        self.flow_name = flow_name
        super().__init__(message=f"Flow '{flow_name}' was aborted by the user")


class PromptValidationError(PromptError):
    """Raised when user input fails validation inside a prompt flow.

    Attributes:
        field:  The prompt field name that failed (e.g. "target").
        reason: A human-readable explanation of why validation failed.
    """

    def __init__(self, field: str, reason: str) -> None:
        self.field = field
        self.reason = reason
        super().__init__(message=f"Validation failed for '{field}': {reason}")
