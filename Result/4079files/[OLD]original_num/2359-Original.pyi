# (generated with --quick)

import asyncio.base_events
from typing import Any, Coroutine, Dict, Optional

ChatBot: Any
ServerSelectionTimeoutError: Any
Statement: Any
asyncio: module
checks: Any
commands: Any
logic: Any
random: module
re: module
requests: module
trainers: Any
utils: Any

class AsyncChatBot(Any):
    loop: asyncio.base_events.BaseEventLoop
    def __init__(self, loop: asyncio.base_events.BaseEventLoop, *args, **kwargs) -> None: ...
    def async_get_response(self, statement: str, session_id: Optional[str] = ...) -> coroutine: ...
    def generate_response(self, input_statement, session_id) -> Any: ...

class CleverCacheLogicAdapter(Any):
    __doc__: str
    api_key: Any
    sessions: dict
    def __init__(self, **kwargs) -> None: ...
    def can_process(self, statement) -> bool: ...
    def process(self, input_statement) -> Any: ...

class Conversation:
    __doc__: str
    bot: Any
    chatbot: Optional[AsyncChatBot]
    chatname: str
    services: Dict[str, str]
    sessions: dict
    train: Any
    def __init__(self, bot) -> None: ...
    def on_message(self, message) -> Coroutine[Any, Any, None]: ...

class TagLogicAdapter(Any):
    def can_process(self, statement) -> bool: ...
    def process(self, statement) -> Any: ...

class ThanksLogicAdapter(Any):
    def can_process(self, statement) -> bool: ...
    def process(self, statement) -> Any: ...

def setup(bot) -> None: ...
