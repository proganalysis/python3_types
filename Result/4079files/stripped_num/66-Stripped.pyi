# (generated with --quick)

import collections
from typing import Any, Callable, Iterable, Sized, Tuple, Type, TypeVar, Union

Request = `namedtuple-Request-json`

BadResponseError: Any
BaseTestRunner: Any
EthereumProxy: Any
RPCServer: Any
json: module
patch: Any
pytest: Any

_Tnamedtuple-Request-json = TypeVar('_Tnamedtuple-Request-json', bound=`namedtuple-Request-json`)

class TestServer(Any):
    run_with_node: bool
    test_server_handler_index_attr_error_call: Any
    test_server_handler_index_bad_response_call: Any
    test_server_handler_index_invalid_rpc_data: Any
    test_server_handler_index_success_call: Any
    test_server_handler_index_type_error_call: Any
    def init_server(self, loop) -> coroutine: ...

class `namedtuple-Request-json`(tuple):
    __slots__ = ["json"]
    __dict__: collections.OrderedDict[str, Any]
    _fields: Tuple[str]
    json: Any
    def __getnewargs__(self) -> Tuple[Any]: ...
    def __getstate__(self) -> None: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __new__(cls: Type[`_Tnamedtuple-Request-json`], json) -> `_Tnamedtuple-Request-json`: ...
    def _asdict(self) -> collections.OrderedDict[str, Any]: ...
    @classmethod
    def _make(cls: Type[`_Tnamedtuple-Request-json`], iterable: Iterable, new = ..., len: Callable[[Sized], int] = ...) -> `_Tnamedtuple-Request-json`: ...
    def _replace(self: `_Tnamedtuple-Request-json`, **kwds) -> `_Tnamedtuple-Request-json`: ...

def namedtuple(typename: str, field_names: Union[str, Iterable[str]], *, verbose: bool = ..., rename: bool = ...) -> type: ...
