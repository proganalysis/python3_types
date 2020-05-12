# (generated with --quick)

from typing import Any, Coroutine, Optional

Bot: Any
Channel: Any
CommandNotFound: Any
ConnectionClosed: Any
Context: Any
Forbidden: Any
Game: Any
MongoClient: Any
Object: Any
SessionManager: Any
argument_parser: Any
command_error_handler: Any
command_formatter: Any
format_command_error: Any
format_traceback: Any
get_help: Any
logging: module

class HahaNoUR(Any):
    all_help: Any
    colour: int
    db: Any
    error_log: Any
    feedbag_log: Any
    help_general: Any
    idol_names: Any
    logger: Any
    prefix: str
    session_manager: Any
    start_time: int
    def _HahaNoUR__change_presence(self) -> Coroutine[Any, Any, None]: ...
    def _HahaNoUR__try_send_msg(self, channel, author, msg) -> Coroutine[Any, Any, None]: ...
    def __init__(self, prefix: str, start_time: int, colour: int, logger, session_manager, db, error_log: int, feedback_log: int, shard_id: int, shard_count: int) -> None: ...
    def on_command_error(self, exception, context) -> Coroutine[Any, Any, None]: ...
    def on_error(self, event_method, *args, **kwargs) -> Coroutine[Any, Any, None]: ...
    def on_ready(self) -> Coroutine[Any, Any, None]: ...
    def process_commands(self, message) -> Coroutine[Any, Any, None]: ...
    def send_traceback(self, tb, header) -> Coroutine[Any, Any, None]: ...
    def start_bot(self, cogs: list, token: str) -> None: ...

def format_exc(limit: Optional[int] = ..., chain: bool = ...) -> str: ...
