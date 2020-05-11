# (generated with --quick)

from typing import Any, Coroutine

BaseSerializer: Any
Cache: Any
Schema: Any
asyncio: module
cache: Any
fields: Any
post_load: Any
random: module
string: module

class MarshmallowSerializer(Any, Any):
    Meta: type
    build_my_type: Any
    dict_type: Any
    encoding: str
    int_type: Any
    list_type: Any
    str_type: Any
    def dumps(self, *args, **kwargs) -> Any: ...
    def loads(self, *args, **kwargs) -> Any: ...

class RandomModel:
    MY_CONSTANT: str
    dict_type: Any
    int_type: Any
    list_type: Any
    str_type: Any
    def __eq__(self, obj) -> bool: ...
    def __init__(self, int_type = ..., str_type = ..., dict_type = ..., list_type = ...) -> None: ...

def serializer() -> Coroutine[Any, Any, None]: ...
def test_serializer() -> None: ...
