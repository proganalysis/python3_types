# (generated with --quick)

from typing import Any, Dict, Type, TypeVar

Colr: Any

_T = TypeVar('_T')
_TPreset = TypeVar('_TPreset', bound=Preset)

class Preset(object):
    __slots__ = ["back", "fore", "style"]
    __doc__: str
    back: Any
    fore: Any
    style: Any
    def __call__(self, text, fore = ..., back = ..., style = ...) -> Any: ...
    def __eq__(self, other) -> Any: ...
    def __init__(self, fore = ..., back = ..., style = ...) -> None: ...
    def as_dict(self) -> Dict[str, Any]: ...
    def merge(self: _TPreset, styleobj, fore = ..., back = ..., style = ...) -> _TPreset: ...

def total_ordering(cls: Type[_T]) -> Type[_T]: ...
