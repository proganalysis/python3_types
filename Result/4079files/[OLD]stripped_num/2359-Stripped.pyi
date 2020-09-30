# (generated with --quick)

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
    loop: Any
    def __init__(self, loop, *args, **kwargs) -> None: ...
    def async_get_response(self, statement, session_id = ...) -> coroutine: ...
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
