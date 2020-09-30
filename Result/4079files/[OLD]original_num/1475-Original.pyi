# (generated with --quick)

import abc
from typing import Any, Coroutine, Type

ABCMeta: Type[abc.ABCMeta]
MONIT_SCHEDULE_EVENT: Any
MONIT_STATUS_EVENT: Any
MsgType: Any
TASK_EVENT: Any
WORKER_EVENT: Any
WORK_SCHEDULE_EVENT: Any
WORK_STATUS_EVENT: Any
async_recv_event: Any
asyncio: module
get_sub_socket: Any
json: module
json_util: Any
models: Any
now: Any
settings: Any
web: Any

class MonitCurrentWorkerHandler(WebSocketHandler):
    need_background: bool
    stop_background_timeout: float

class MonitResultHandler(WebSocketHandler):
    need_background: bool
    stop_background_timeout: float

class MonitSchedulesHandler(WebSocketHandler):
    need_background: bool
    stop_background_timeout: float

class MonitWaitingTaskHandler(WebSocketHandler):
    need_background: bool
    stop_background_timeout: float

class WebSocketHandler(metaclass=abc.ABCMeta):
    need_background: bool
    stop_background_timeout: int
    stop_msg: str
    def _receive_msg(self, ws) -> Coroutine[Any, Any, None]: ...
    def background(self, ws) -> Coroutine[Any, Any, None]: ...
    def get_handler(self, request) -> coroutine: ...
    def process_msg(self, msg_text: str) -> Coroutine[Any, Any, None]: ...

class WorkResultHandler(WebSocketHandler):
    need_background: bool
    stop_background_timeout: float

class WorkSchedulesHandler(WebSocketHandler):
    need_background: bool
    stop_background_timeout: float

def _get_task_represent(task: dict) -> dict: ...
def _get_worker_represent(worker) -> dict: ...
def add_routes(app) -> None: ...
def start_server() -> None: ...
