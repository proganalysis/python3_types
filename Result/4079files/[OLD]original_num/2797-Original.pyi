# (generated with --quick)

import collections
from typing import Any, Callable, Coroutine, Iterable, List, Sized, Tuple, Type, TypeVar, Union

ASCII_SEARCH_SPACE: Any
AttackContext: Any
E: Any
Expression: Any
Functions: Any
Injection: Any
asyncio: module
check: Any
features: List[Feature]
fs_func: Any
func: Any
saxon_func: Any

_TFeature = TypeVar('_TFeature', bound=Feature)

class Feature(tuple):
    __slots__ = ["name", "tests"]
    __dict__: collections.OrderedDict[str, Union[list, str]]
    _field_defaults: collections.OrderedDict[str, Union[list, str]]
    _field_types: collections.OrderedDict[str, type]
    _fields: Tuple[str, str]
    name: str
    tests: list
    def __getnewargs__(self) -> Tuple[str, list]: ...
    def __getstate__(self) -> None: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __new__(cls: Type[_TFeature], name: str, tests: list) -> _TFeature: ...
    def _asdict(self) -> collections.OrderedDict[str, Union[list, str]]: ...
    @classmethod
    def _make(cls: Type[_TFeature], iterable: Iterable[Union[list, str]], new = ..., len: Callable[[Sized], int] = ...) -> _TFeature: ...
    def _replace(self: _TFeature, **kwds: Union[list, str]) -> _TFeature: ...

def detect_features(context, injector) -> Coroutine[Any, Any, List[Feature]]: ...
def test_oob(path) -> Callable[[Any, Any], Any]: ...
