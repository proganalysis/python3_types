from enum import Enum
from simulation.django_communicator import DjangoCommunicator as DjangoCommunicator
from types import CoroutineType
from typing import Any

LOGGER: Any
SECONDS_TILL_CONSIDERED_INACTIVE: int

class StatusOptions(Enum):
    RUNNING: str = ...
    PAUSED: str = ...
    STOPPED: str = ...

class ActivityMonitor:
    timer: Any = ...
    django_communicator: Any = ...
    def __init__(self, django_communicator: DjangoCommunicator) -> None: ...
    def _start_timer(self) -> None: ...
    def _stop_timer(self) -> None: ...
    @property
    def active_users(self): ...
    __active_users: Any = ...
    @active_users.setter
    def active_users(self, value: float) -> Any: ...
    async def change_status_to_stopped(self) -> None: ...

class Timer:
    _timeout: Any = ...
    _callback: Any = ...
    _task: Any = ...
    def __init__(self, timeout: float, callback: CoroutineType) -> None: ...
    async def _job(self) -> None: ...
    def cancel(self) -> None: ...
    def cancelled(self): ...
