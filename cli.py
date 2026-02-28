#!/usr/bin/env python3
"""Entry point for the CLI visual boilerplate.

How to add a new subcommand:
  1. Create `commands/action_N.py` with `run_action_N(target, option)` and a
     result dataclass that has `error: str | None`.
  2. Add a new `add_parser` block in `build_parser()` below.
  3. Add an `elif args.command == "action-N":` branch in `main()` below.
  4. Add a matching `_flow_action_N` function in `prompts/interactive.py` and
     register it in the `_ACTIONS` dict there.
"""

import argparse
import sys


def build_parser() -> argparse.ArgumentParser:
    """Build and return the top-level argument parser with all subcommands."""
    parser = argparse.ArgumentParser(
        prog="clisoft",
        description="CLI Visual Boilerplate — Rich + InquirerPy template.",
    )
    subparsers = parser.add_subparsers(dest="command")

    # ── action-one subcommand ──────────────────────────────────────────────────
    # Rename "action-one" and update help text to reflect the real purpose.
    action_one_parser = subparsers.add_parser(
        "action-one",
        help="Run a simulated tabular data flow (template for action one)",
    )
    action_one_parser.add_argument(
        "target",
        nargs="?",
        default="target",
        help="Arbitrary target label passed to action one",
    )

    # ── action-two subcommand ──────────────────────────────────────────────────
    # Rename "action-two" and update help text to reflect the real purpose.
    action_two_parser = subparsers.add_parser(
        "action-two",
        help="Run a simulated metrics/timing flow (template for action two)",
    )
    action_two_parser.add_argument(
        "target",
        nargs="?",
        default="target",
        help="Arbitrary target label passed to action two",
    )

    # ── action-three subcommand ────────────────────────────────────────────────
    # Rename "action-three" and update help text to reflect the real purpose.
    action_three_parser = subparsers.add_parser(
        "action-three",
        help="Run a simulated item-list flow (template for action three)",
    )
    action_three_parser.add_argument(
        "target",
        nargs="?",
        default="target",
        help="Arbitrary target label passed to action three",
    )

    return parser


def main() -> None:
    """Parse arguments and dispatch to the appropriate command or interactive mode."""
    parser = build_parser()
    args = parser.parse_args()

    try:
        if args.command == "action-one":
            from ui.output import print_info
            # Customize: replace this message with real non-interactive logic for action one.
            print_info("Run in interactive mode to use Action One: python cli.py")

        elif args.command == "action-two":
            from ui.output import print_info
            # Customize: replace this message with real non-interactive logic for action two.
            print_info("Run in interactive mode to use Action Two: python cli.py")

        elif args.command == "action-three":
            from ui.output import print_info
            # Customize: replace this message with real non-interactive logic for action three.
            print_info("Run in interactive mode to use Action Three: python cli.py")

        else:
            # No subcommand provided — fall through to interactive mode.
            from prompts.interactive import start_interactive
            start_interactive()

    except KeyboardInterrupt:
        from ui.output import console
        console.print("\n[dim]Interrupted. Goodbye![/dim]")
        sys.exit(0)


if __name__ == "__main__":
    main()
