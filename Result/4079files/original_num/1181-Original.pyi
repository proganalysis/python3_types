# (generated with --quick)

from typing import Any, Type, TypeVar

ANY_IS_PATCH: Any
P_IS_PATCH: Any
PackageFlags: Any
version_compare: Any

_T = TypeVar('_T')
_TUserVisibleVersionInfo = TypeVar('_TUserVisibleVersionInfo', bound=UserVisibleVersionInfo)

class UserVisibleVersionInfo:
    __slots__ = ["metaorder", "spread", "version", "versionclass", "versionflags"]
    metaorder: Any
    spread: Any
    version: Any
    versionclass: Any
    versionflags: Any
    def __eq__(self, other) -> Any: ...
    def __hash__(self) -> int: ...
    def __init__(self, package, spread = ...) -> None: ...
    def __lt__(self, other) -> Any: ...
    def as_with_spread(self: _TUserVisibleVersionInfo, spread) -> _TUserVisibleVersionInfo: ...

def copy(x: _T) -> _T: ...
def total_ordering(cls: Type[_T]) -> Type[_T]: ...
