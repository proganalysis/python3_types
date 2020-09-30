# (generated with --quick)

import asyncio.events
from typing import Any, Callable, Dict, Tuple, Type, Union
import unittest.case

RpcMixin: Any
aiozmq: Any
asyncio: module
find_unused_port: Any
msgpack: Any
translation_table: Dict[int, Tuple[Type[Point], Callable[[Any], Any], Callable[[Any], Any]]]
unittest: module

class LoopRpcTranslatorsTests(unittest.case.TestCase, RpcTranslatorsMixin):
    client: None
    loop: Any
    server: None

class LooplessRpcTranslatorsTests(unittest.case.TestCase, RpcTranslatorsMixin):
    client: None
    loop: asyncio.events.AbstractEventLoop
    server: None

class MyHandler(Any):
    func: Any

class Point:
    x: Any
    y: Any
    def __eq__(self, other) -> Union[NotImplementedType, bool]: ...
    def __init__(self, x, y) -> None: ...

class RpcTranslatorsMixin(Any):
    client: Any
    server: Any
    def make_rpc_pair(self, *, error_table = ...) -> Tuple[Any, Any]: ...
    def test_simple(self) -> None: ...
