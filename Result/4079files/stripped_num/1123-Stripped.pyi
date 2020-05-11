# (generated with --quick)

from typing import Any, Dict, TypeVar, Union

_T0 = TypeVar('_T0')
_T1 = TypeVar('_T1')

class Parameter:
    PARAM_FLAG: int
    PARAM_KV: int
    PARAM_LIST: int
    __doc__: str
    key: Any
    type: int
    value: Any
    def __init__(self, key, value = ...) -> None: ...
    def __str__(self) -> str: ...
    def toJSON(self, flagdefault: _T0 = ...) -> Dict[Union[str, _T1], Any]: ...

class ParameterList(list):
    __doc__: str
    flags: list
    paramnames: list
    def __contains__(self, param) -> bool: ...
    def __getitem__(self, paramname) -> Any: ...
    def __init__(self, params) -> None: ...
    def append(self, param) -> None: ...
    def toJSON(self, flagdefault = ...) -> Dict[nothing, nothing]: ...
