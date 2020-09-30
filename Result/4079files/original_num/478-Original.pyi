# (generated with --quick)

import collections
from typing import Any, Type, Union

deque: Type[collections.deque]

class CallableDeep:
    _ctx: Any
    foo: type
    def __init__(self: Union[CallableDeep, CallableMixed, CallableShallow, Simple], context = ...) -> None: ...

class CallableMixed:
    _ctx: Any
    foo: type
    def __call__(self, *args) -> str: ...
    def __init__(self: Union[CallableDeep, CallableMixed, CallableShallow, Simple], context = ...) -> None: ...

class CallableShallow:
    _ctx: Any
    def __call__(self, *args) -> str: ...
    def __init__(self: Union[CallableDeep, CallableMixed, CallableShallow, Simple], context = ...) -> None: ...

class Simple:
    _ctx: Any
    _protected: bool
    foo: type
    static: str
    def __init__(self: Union[CallableDeep, CallableMixed, CallableShallow, Simple], context = ...) -> None: ...

def function(context, *args) -> str: ...
def init(self: Union[CallableDeep, CallableMixed, CallableShallow, Simple], context = ...) -> None: ...
def path(path) -> collections.deque: ...
