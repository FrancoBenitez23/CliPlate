"""Template action one — simulated tabular data with row items and summary scalars.

This module is intentionally generic. To adapt it to a real project:

  1. Rename `ActionOneResult` and `run_action_one` to something meaningful
     (e.g. `ScanResult` / `run_scan`).
  2. Replace the TODO block below with your actual logic.
  3. Update the dataclass fields to match what your logic produces.
  4. Remove the `time.sleep(1.5)` line once real I/O provides natural delay.
  5. Mirror any field renames in `prompts/interactive.py` and `cli.py`.

Return contract (never break this):
  - Always return an `ActionOneResult` instance.
  - Set `error` to a non-empty string on failure; leave it `None` on success.
  - Never print or raise inside this function — the caller handles UI.
"""

import random
import time
from dataclasses import dataclass, field


# Placeholder row labels used to fill the simulated table.
# Replace with real identifiers (file paths, function names, endpoint names, etc.)
_PLACEHOLDER_ITEMS = [
    "module/core.py:42(process_request)",
    "module/db.py:118(fetch_records)",
    "module/utils.py:77(serialize)",
    "module/cache.py:31(lookup)",
    "module/pipeline.py:204(transform)",
    "lib/parser.py:88(parse_tokens)",
    "lib/encoder.py:55(encode_utf8)",
    "{built-in method builtins.exec}",
    "{method 'acquire' of '_thread.lock' objects}",
    "{built-in method posix.read}",
]


@dataclass
class ActionOneResult:
    """Result returned by `run_action_one`.

    Fields:
        rows:        List of dicts, one per table row.
                     Keys: label, value_a, value_b, value_c, identifier.
        total_count: Integer summary scalar (e.g. total calls, total records).
        total_time:  Float summary scalar (e.g. elapsed seconds).
        output_file: Optional path if the action writes a file; otherwise None.
        error:       Non-None string if the action failed; None on success.
    """

    rows: list[dict] = field(default_factory=list)
    total_count: int = 0
    total_time: float = 0.0
    output_file: str | None = None
    error: str | None = None


def run_action_one(target: str, option: int = 10) -> ActionOneResult:
    """Execute action one against *target* and return the result.

    Args:
        target: Arbitrary string label that identifies what to act on.
                In a real implementation this might be a file path, URL,
                module name, etc.
        option: Integer tuning parameter (e.g. max rows to return).

    Returns:
        ActionOneResult populated with either data or an error message.
    """
    # Simulate work so the spinner is visible during the demo.
    # Remove or replace this line with real I/O / computation.
    time.sleep(1.5)

    # ── TODO: replace this block with real logic ──────────────────────────────
    # Example shape of real logic:
    #
    #   try:
    #       data = your_library.run(target, limit=option)
    #   except YourError as exc:
    #       return ActionOneResult(error=str(exc))
    #
    #   rows = [
    #       {
    #           "label":      item.name,
    #           "value_a":    str(item.calls),
    #           "value_b":    f"{item.time:.4f}",
    #           "value_c":    f"{item.cumtime:.4f}",
    #           "identifier": item.location,
    #       }
    #       for item in data.items
    #   ]
    #   return ActionOneResult(
    #       rows=rows,
    #       total_count=data.total_calls,
    #       total_time=data.elapsed,
    #       error=None,
    #   )
    #
    # Until then, random values keep the visual demo functional:

    total_count = random.randint(8_000, 120_000)
    total_time = round(random.uniform(0.4, 3.2), 4)

    sample = random.sample(_PLACEHOLDER_ITEMS, k=min(option, len(_PLACEHOLDER_ITEMS)))
    rows = []
    for item in sample:
        value_a = random.randint(1, 5_000)
        value_b = round(random.uniform(0.001, 0.4), 4)
        value_c = round(value_b + random.uniform(0.0, 0.3), 4)
        value_ratio = round(value_c / value_a, 6)
        rows.append({
            "label":      str(value_a),
            "value_a":    f"{value_b:.4f}",
            "value_b":    f"{value_c:.4f}",
            "value_c":    f"{value_ratio:.6f}",
            "identifier": item,
        })
    # ── end TODO ──────────────────────────────────────────────────────────────

    return ActionOneResult(
        rows=rows,
        total_count=total_count,
        total_time=total_time,
        output_file=None,
        error=None,
    )
