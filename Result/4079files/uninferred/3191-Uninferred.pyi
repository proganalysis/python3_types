from rx.core.typing import RelativeTime as RelativeTime, Scheduler as Scheduler
from typing import Any, Optional

new_thread_scheduler: Any

def _to_marbles(scheduler: Optional[Scheduler]=..., timespan: RelativeTime=...) -> Any: ...
def stringify(value: Any): ...
