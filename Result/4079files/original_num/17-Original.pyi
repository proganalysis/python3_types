# (generated with --quick)

from typing import Any, Coroutine, Pattern, TypeVar, Union

ClientSession: Any
Context: Any
CustomBot: Any
CustomEmbed: Any
Message: Any
TextChannel: Any
commands: Any

AnyStr = TypeVar('AnyStr', str, bytes)

class Okay_Google(object):
    bot: Any
    google: Any
    matcher: Pattern[str]
    session: Any
    def _Okay_Google__before_invoke(self, ctx) -> Coroutine[Any, Any, None]: ...
    def _Okay_Google__unload(self) -> None: ...
    def __init__(self, bot) -> None: ...
    def on_message(self, message) -> Coroutine[Any, Any, None]: ...
    def run_google_search(self, query: str, channel) -> coroutine: ...

def compile(pattern: Union[Pattern[AnyStr], AnyStr], flags: int = ...) -> Pattern[AnyStr]: ...
def setup(bot) -> None: ...
