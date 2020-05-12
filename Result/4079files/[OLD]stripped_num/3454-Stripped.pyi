# (generated with --quick)

from typing import Any

EXISTS_MORE_LATE_TASK_CANCEL_REASON: Any
WORKER_DEAD_CANCEL_REASON: Any
models: Any
now: Any

def cancel_dead_worker_tasks() -> None: ...
def cancel_double(last_task_data, task_type) -> None: ...
def process_task_data(data) -> None: ...
