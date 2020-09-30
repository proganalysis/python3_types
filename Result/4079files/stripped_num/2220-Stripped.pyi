# (generated with --quick)

from typing import Any, Callable, Match, Pattern, TypeVar, Union

USER_NAME_REGEX: Any

AnyStr = TypeVar('AnyStr', str, bytes)

def sub(pattern: Union[Pattern[AnyStr], AnyStr], repl: Union[Callable[[Match[AnyStr]], AnyStr], AnyStr], string: AnyStr, count: int = ..., flags: int = ...) -> AnyStr: ...
def to_name(name) -> Any: ...
