# (generated with --quick)

from typing import Any, Callable, Coroutine, Dict, Tuple, Type, Union

aiozmq: Any
asyncio: module
msgpack: Any
translation_table: Dict[int, Tuple[Type[Point], Callable[[Any], Any], Callable[[Any], Any]]]

class Point:
    x: Any
    y: Any
    def __eq__(self, other) -> Union[NotImplementedType, bool]: ...
    def __init__(self, x, y) -> None: ...

class ServerHandler(Any):
    remote: Any

def go() -> Coroutine[Any, Any, None]: ...
def main() -> None: ...
