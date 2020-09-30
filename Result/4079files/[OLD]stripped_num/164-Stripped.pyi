# (generated with --quick)

from typing import Any, Optional, TypeVar, Union

BuildStrategy: Any
ExtensionLibBuildStrategy: Any
_strategies: dict

_V = TypeVar('_V')
_V2 = TypeVar('_V2')

@overload
def get_strategy(k) -> Optional[_V]: ...
@overload
def get_strategy(k, d: _V2) -> Union[_V, _V2]: ...
def register_strategy(name, strategy) -> None: ...
def show_strategies() -> None: ...
