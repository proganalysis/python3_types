# (generated with --quick)

from typing import Any, Coroutine

StoppableMixin: Any
WORKER_EVENT: Any
WORKER_HEART_BEAT_PERIOD: Any
async_recv_event: Any
asyncio: module
cancel_dead_worker_tasks: Any
datetime: module
get_sub_socket: Any
json: module
json_util: Any
models: Any
now: Any
process_worker_data: Any
settings: Any
zmq: Any

class WorkerProcessor(Any):
    context: Any
    sleep_period: Any
    verbose: Any
    def __init__(self, verbose = ..., sleep_period = ...) -> None: ...
    def clear_dead_workers(self) -> Coroutine[Any, Any, None]: ...
    def process_workers(self) -> Coroutine[Any, Any, None]: ...
    def register_workers(self) -> Coroutine[Any, Any, None]: ...
