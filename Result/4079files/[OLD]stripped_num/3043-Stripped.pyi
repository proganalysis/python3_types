# (generated with --quick)

import functools
from typing import Any, Coroutine, Tuple, Type, TypeVar

IdentityNotInitialized: Any
MemoryChannelEventHandler: Any
Nursery: Any
SyncryptBaseException: Any
Vault: Any
VaultState: Any
Watchdog: Any
logging: module
os: module
partial: Type[functools.partial]
trio: Any

_T0 = TypeVar('_T0')

class VaultController:
    __doc__: str
    app: Any
    cancel_scope: Any
    do_init: Any
    do_push: Any
    file_changes_receive_channel: Any
    file_changes_send_channel: Any
    logger: VaultLoggerAdapter
    nursery: Any
    ready: Any
    task_status: Any
    update_on_idle: Any
    vault: Any
    def __init__(self, app, vault, update_on_idle = ...) -> None: ...
    def autopull_vault_task(self) -> coroutine: ...
    def cancel(self) -> Coroutine[Any, Any, None]: ...
    def handle_state_transition(self, new_state, old_state) -> Coroutine[Any, Any, None]: ...
    def loop(self) -> Coroutine[Any, Any, nothing]: ...
    def respond_to_file_changes(self) -> Coroutine[Any, Any, None]: ...
    def resync(self) -> Coroutine[Any, Any, None]: ...
    def run(self, do_init, do_push, task_status = ...) -> Coroutine[Any, Any, None]: ...
    def watchdog_task(self) -> Coroutine[Any, Any, None]: ...

class VaultLoggerAdapter(logging.LoggerAdapter):
    vault: Any
    def __init__(self, vault, logger) -> None: ...
    def process(self, msg: _T0, kwargs) -> Tuple[_T0, dict]: ...
