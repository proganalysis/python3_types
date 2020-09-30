# (generated with --quick)

from typing import Any, Callable, Mapping, Optional, TextIO, Type, TypeVar

BOT_CONFIG: Config
f: TextIO
os: module
yaml: module

_T = TypeVar('_T')

class Config(yaml.YAMLObject):
    yaml_tag: str
    def __init__(self, **kwargs) -> None: ...

def _env_var_constructor(loader, node) -> Optional[str]: ...
@overload
def dataclass(_cls: Type[_T]) -> Type[_T]: ...
@overload
def dataclass(*, init: bool = ..., repr: bool = ..., eq: bool = ..., order: bool = ..., unsafe_hash: bool = ..., frozen: bool = ...) -> Callable[[Type[_T]], Type[_T]]: ...
@overload
def field(*, default: _T, init: bool = ..., repr: bool = ..., hash: bool = ..., compare: bool = ..., metadata: Optional[Mapping[str, Any]] = ...) -> _T: ...
@overload
def field(*, default_factory: Callable[[], _T], init: bool = ..., repr: bool = ..., hash: bool = ..., compare: bool = ..., metadata: Optional[Mapping[str, Any]] = ...) -> _T: ...
@overload
def field(*, init: bool = ..., repr: bool = ..., hash: bool = ..., compare: bool = ..., metadata: Optional[Mapping[str, Any]] = ...) -> Any: ...
