"""Template action three — simulated item list with size/count metadata.

This module is intentionally generic. To adapt it to a real project:

  1. Rename `ActionThreeItem`, `ActionThreeResult`, and `run_action_three`
     to something meaningful (e.g. `Allocation` / `MemoryResult` / `run_memory`,
     or `LogEntry` / `LogReport` / `run_log_scan`).
  2. Replace the TODO block below with your actual logic.
  3. Update the dataclass fields to match what your logic produces.
  4. Remove the `time.sleep(1.5)` line once real I/O provides natural delay.
  5. Mirror any field renames in `prompts/interactive.py` and `cli.py`.

Return contract (never break this):
  - Always return an `ActionThreeResult` instance.
  - Set `error` to a non-empty string on failure; leave it `None` on success.
  - Never print or raise inside this function — the caller handles UI.
"""

import random
import time
from dataclasses import dataclass, field


# Placeholder source paths used to fill the simulated table.
# Replace with real identifiers (file paths, queue names, table names, etc.)
_PLACEHOLDER_SOURCES = [
    "module/models.py",
    "module/serializer.py",
    "lib/query.py",
    "lib/cache.py",
    "module/views.py",
    "lib/middleware.py",
    "module/tasks.py",
    "lib/utils.py",
    "module/validators.py",
    "lib/codec.py",
]


@dataclass
class ActionThreeItem:
    """A single item in the ActionThreeResult list.

    Fields:
        source:    Where this item originates (file, queue, table name, etc.).
        position:  Line number, offset, index, or other positional reference.
        size_kb:   Magnitude of the item (KB, MB, rows, bytes — your choice).
        count:     Number of sub-items, occurrences, or objects.
    """

    source: str
    position: int
    size_kb: float
    count: int


@dataclass
class ActionThreeResult:
    """Result returned by `run_action_three`.

    Fields:
        peak_value:    Largest observed scalar (e.g. peak memory KB, max latency).
        current_value: Current / final scalar (e.g. current memory KB, last value).
        items:         Sorted list of ActionThreeItem instances (desc by size_kb).
        error:         Non-None string if the action failed; None on success.
    """

    peak_value: float = 0.0
    current_value: float = 0.0
    items: list[ActionThreeItem] = field(default_factory=list)
    error: str | None = None


def run_action_three(target: str, option: int = 10) -> ActionThreeResult:
    """Execute action three against *target* and return the result.

    Args:
        target: Arbitrary string label that identifies what to act on.
                In a real implementation this might be a process name, module,
                service name, etc.
        option: Integer tuning parameter (e.g. max items to return).

    Returns:
        ActionThreeResult populated with either data or an error message.
    """
    # Simulate work so the spinner is visible during the demo.
    # Remove or replace this line with real I/O / computation.
    time.sleep(1.5)

    # ── TODO: replace this block with real logic ──────────────────────────────
    # Example shape of real logic (tracemalloc / memory profiling):
    #
    #   import tracemalloc
    #   try:
    #       tracemalloc.start()
    #       your_function(target)
    #       snapshot = tracemalloc.take_snapshot()
    #       current, peak = tracemalloc.get_traced_memory()
    #       tracemalloc.stop()
    #   except YourError as exc:
    #       return ActionThreeResult(error=str(exc))
    #
    #   stats = snapshot.statistics("lineno")[:option]
    #   items = [
    #       ActionThreeItem(
    #           source=str(stat.traceback[0].filename),
    #           position=stat.traceback[0].lineno,
    #           size_kb=round(stat.size / 1024, 2),
    #           count=stat.count,
    #       )
    #       for stat in stats
    #   ]
    #   items.sort(key=lambda i: i.size_kb, reverse=True)
    #   return ActionThreeResult(
    #       peak_value=round(peak / 1024, 2),
    #       current_value=round(current / 1024, 2),
    #       items=items,
    #       error=None,
    #   )
    #
    # Until then, random values keep the visual demo functional:

    peak_value = round(random.uniform(1_024, 8_192), 2)
    current_value = round(peak_value * random.uniform(0.6, 0.95), 2)

    sources = random.sample(_PLACEHOLDER_SOURCES, k=min(option, len(_PLACEHOLDER_SOURCES)))
    items = [
        ActionThreeItem(
            source=src,
            position=random.randint(10, 300),
            size_kb=round(random.uniform(8, 512), 2),
            count=random.randint(50, 5_000),
        )
        for src in sources
    ]
    # Sort descending by size so the table reads naturally (largest first)
    items.sort(key=lambda i: i.size_kb, reverse=True)

    # ── end TODO ──────────────────────────────────────────────────────────────

    return ActionThreeResult(
        peak_value=peak_value,
        current_value=current_value,
        items=items,
        error=None,
    )
