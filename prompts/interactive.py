"""InquirerPy interactive flows — navigational screens, no data collection.

Each `_flow_*` function follows this pattern:
  1. Print a simple info message or panel for the action.
  2. Show a single "Go back" select so the user can return to the main menu.

To add a new action:
  1. Write a new `_flow_action_N` function below following the pattern.
  2. Add an entry to `_ACTIONS` mapping the display label to the function name.
  3. Create the matching module in `commands/action_N.py`.
  4. Wire up the argparse subcommand in `cli.py`.
"""

from InquirerPy import inquirer

from ui.output import (
    console,
    print_welcome,
    print_info,
)

# ── Menu registry ──────────────────────────────────────────────────────────────
# Maps the display label shown in the interactive select menu to the name of
# the handler function defined below.  Change the labels to match your project.
_ACTIONS = {
    "Action One":   "_flow_action_one",
    "Action Two":   "_flow_action_two",
    "Action Three": "_flow_action_three",
    "Exit":         None,
}


def start_interactive() -> None:
    """Show the welcome panel and run the main interactive selection loop."""
    # Customize the title and subtitle to match your project name.
    print_welcome(
        "CLI Visual Boilerplate",
        "Rich + InquirerPy template — replace actions with real logic",
    )

    while True:
        action = inquirer.select(
            message="What do you want to do?",
            choices=list(_ACTIONS.keys()),
            instruction="(use arrow keys, Enter to select)",
        ).execute()

        handler_name = _ACTIONS[action]
        if handler_name is None:
            # Exit chosen — print a farewell and leave the loop.
            console.print("\n[dim]See you! Keep building great CLIs.[/dim]\n")
            break

        # Look up and call the handler by name from this module's globals.
        handler = globals()[handler_name]
        handler()
        # Print a blank line between flows for visual breathing room.
        console.print()


# ── Individual flows ───────────────────────────────────────────────────────────

def _flow_action_one() -> None:
    """Display the Action One screen and wait for the user to go back.

    Customize: replace the print_info message with your action's actual UI.
    """
    console.print()
    # Customize: replace this message with a description of what Action One does.
    print_info("Action One — add your logic here.")
    inquirer.select(
        message="",
        choices=["← Go back"],
    ).execute()


def _flow_action_two() -> None:
    """Display the Action Two screen and wait for the user to go back.

    Customize: replace the print_info message with your action's actual UI.
    """
    console.print()
    # Customize: replace this message with a description of what Action Two does.
    print_info("Action Two — add your logic here.")
    inquirer.select(
        message="",
        choices=["← Go back"],
    ).execute()


def _flow_action_three() -> None:
    """Display the Action Three screen and wait for the user to go back.

    Customize: replace the print_info message with your action's actual UI.
    """
    console.print()
    # Customize: replace this message with a description of what Action Three does.
    print_info("Action Three — add your logic here.")
    inquirer.select(
        message="",
        choices=["← Go back"],
    ).execute()
