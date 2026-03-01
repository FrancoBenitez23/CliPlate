"""Centralized exception hierarchy for cliSoft.

All project exceptions inherit from CLISoftError.  Submodules are organized
by layer so callers can catch at any granularity:

    except CLISoftError         # catch anything from this project
    except CommandError         # catch only command-layer failures
    except CommandTimeoutError  # catch one specific failure mode

Import from this package — never from the submodules directly:

    from exceptions import CLISoftError, CommandError, PromptAbortedError

Constraint: this package MUST NOT import from ui/, prompts/, commands/, or cli.py.
"""


# ── Base exception ─────────────────────────────────────────────────────────────

class CLISoftError(Exception):
    """Base class for all cliSoft exceptions.

    Attributes:
        message: Human-readable description of the error.
        layer:   Architectural layer that raised the exception
                 ("cli", "command", "prompt", or "ui").
    """

    def __init__(self, message: str, layer: str) -> None:
        self.message = message
        self.layer = layer
        super().__init__(message)


# ── Re-exports from submodules ─────────────────────────────────────────────────
# Imported here so callers only need `from exceptions import <Name>`.

from exceptions.cli import (       # noqa: E402  (imports after class definition)
    CLIError,
    UnknownCommandError,
    MissingArgumentError,
)
from exceptions.command import (   # noqa: E402
    CommandError,
    CommandExecutionError,
    CommandTimeoutError,
)
from exceptions.prompt import (    # noqa: E402
    PromptError,
    PromptAbortedError,
    PromptValidationError,
)
from exceptions.ui import (        # noqa: E402
    UIError,
    RenderError,
    SpinnerError,
)

__all__ = [
    # Base
    "CLISoftError",
    # CLI layer
    "CLIError",
    "UnknownCommandError",
    "MissingArgumentError",
    # Command layer
    "CommandError",
    "CommandExecutionError",
    "CommandTimeoutError",
    # Prompt layer
    "PromptError",
    "PromptAbortedError",
    "PromptValidationError",
    # UI layer
    "UIError",
    "RenderError",
    "SpinnerError",
]
