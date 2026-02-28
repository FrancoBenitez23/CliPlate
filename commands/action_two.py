"""Template action two — simulated key/value metrics with statistical summary.

This module is intentionally generic. To adapt it to a real project:

  1. Rename `ActionTwoResult` and `run_action_two` to something meaningful
     (e.g. `BenchmarkResult` / `run_benchmark`, or `ImportResult` / `run_import`).
  2. Replace the TODO block below with your actual logic.
  3. Update the dataclass fields to match what your logic produces.
  4. Remove the `time.sleep(1.5)` line once real I/O provides natural delay.
  5. Mirror any field renames in `prompts/interactive.py` and `cli.py`.

Return contract (never break this):
  - Always return an `ActionTwoResult` instance.
  - Set `error` to a non-empty string on failure; leave it `None` on success.
  - Never print or raise inside this function — the caller handles UI.
"""

import random
import time
from dataclasses import dataclass, field


@dataclass
class ActionTwoResult:
    """Result returned by `run_action_two`.

    Fields:
        iterations:  How many iterations were performed (e.g. runs, retries, pages).
        total_value: Sum of all measured values (e.g. total elapsed seconds).
        avg_value:   Mean value per iteration.
        min_value:   Minimum observed value.
        max_value:   Maximum observed value.
        values:      Raw list of per-iteration values (for charting or audit).
        error:       Non-None string if the action failed; None on success.
    """

    iterations: int = 0
    total_value: float = 0.0
    avg_value: float = 0.0
    min_value: float = 0.0
    max_value: float = 0.0
    values: list[float] = field(default_factory=list)
    error: str | None = None


def run_action_two(target: str, option: int = 10) -> ActionTwoResult:
    """Execute action two against *target* and return the result.

    Args:
        target: Arbitrary string label that identifies what to act on.
                In a real implementation this might be a file path, URL,
                endpoint name, etc.
        option: Integer tuning parameter (e.g. number of iterations to run).

    Returns:
        ActionTwoResult populated with either data or an error message.
    """
    # Simulate work so the spinner is visible during the demo.
    # Remove or replace this line with real I/O / computation.
    time.sleep(1.5)

    # ── TODO: replace this block with real logic ──────────────────────────────
    # Example shape of real logic:
    #
    #   try:
    #       raw_values = []
    #       for _ in range(option):
    #           t0 = time.perf_counter()
    #           your_function(target)
    #           raw_values.append(time.perf_counter() - t0)
    #   except YourError as exc:
    #       return ActionTwoResult(error=str(exc))
    #
    #   total = sum(raw_values)
    #   return ActionTwoResult(
    #       iterations=option,
    #       total_value=round(total, 4),
    #       avg_value=round(total / option, 6),
    #       min_value=min(raw_values),
    #       max_value=max(raw_values),
    #       values=raw_values,
    #       error=None,
    #   )
    #
    # Until then, random values keep the visual demo functional:

    values = [round(random.uniform(0.03, 0.08), 4) for _ in range(option)]
    total_value = round(sum(values), 4)
    avg_value = round(total_value / option, 6)

    # ── end TODO ──────────────────────────────────────────────────────────────

    return ActionTwoResult(
        iterations=option,
        total_value=total_value,
        avg_value=avg_value,
        min_value=min(values),
        max_value=max(values),
        values=values,
        error=None,
    )
