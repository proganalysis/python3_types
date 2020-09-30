# (generated with --quick)

import asyncio.futures
import pathlib
from typing import Any, Coroutine, Dict, List, Optional, Type

Alert: Any
Hooks: Any
Path: Type[pathlib.Path]
ResumeData: Any
Torrent: Any
asyncio: module
functools: module
log: logging.Logger
logging: module
lt: Any
pkg_resources: module

class Core(object):
    alert: Any
    config: Any
    hooks: Any
    resume_data: Any
    session: Any
    session_stats_future: Optional[asyncio.futures.Future[nothing]]
    state_dir: Any
    torrent: Any
    torrent_data: Dict[nothing, nothing]
    def __init__(self, config, state_dir = ...) -> None: ...
    def get_session_stats(self) -> coroutine: ...
    def get_torrent_tags(self, info_hash) -> List[nothing]: ...
    def load_session_state(self) -> Coroutine[Any, Any, None]: ...
    def on_session_stats_alert(self, alert) -> Coroutine[Any, Any, None]: ...
    def on_state_changed_alert(self, alert) -> Coroutine[Any, Any, None]: ...
    def on_status_notification_alert(self, alert) -> Coroutine[Any, Any, None]: ...
    def save_session_state(self) -> Coroutine[Any, Any, None]: ...
    def start(self, settings = ...) -> Coroutine[Any, Any, None]: ...
    def stop(self) -> Coroutine[Any, Any, None]: ...
