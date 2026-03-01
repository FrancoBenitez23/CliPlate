"""CLI-layer exceptions for cliSoft.

Raised when argument parsing or command routing fails before any real work
has started.  These are distinct from CommandError (which is raised by the
logic inside a command) and PromptError (which is raised inside a flow).

Usage:
    from exceptions import UnknownCommandError, MissingArgumentError

    raise UnknownCommandError(command="deploy")
    raise MissingArgumentError(argument="--target")
"""

from exceptions import CLISoftError


class CLIError(CLISoftError):
    """Base for all CLI-layer errors (argument parsing, command routing)."""

    def __init__(self, message: str) -> None:
        super().__init__(message=message, layer="cli")


class UnknownCommandError(CLIError):
    """Raised when a subcommand name is not registered in the parser.

    Attributes:
        command: The unrecognised command string supplied by the user.
    """

    def __init__(self, command: str) -> None:
        self.command = command
        super().__init__(message=f"Unknown command: '{command}'")


class MissingArgumentError(CLIError):
    """Raised when a required argument is absent from the parsed namespace.

    Attributes:
        argument: The name of the missing argument (e.g. "--target").
    """

    def __init__(self, argument: str) -> None:
        self.argument = argument
        super().__init__(message=f"Missing required argument: '{argument}'")
