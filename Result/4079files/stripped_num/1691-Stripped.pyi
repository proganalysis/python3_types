# (generated with --quick)

from typing import Any, Coroutine, Dict, TypeVar

db: Any
pg: Any

_T0 = TypeVar('_T0')

def add_env(env_name: _T0) -> Coroutine[Any, Any, Dict[str, _T0]]: ...
def delete_env(env_name) -> Coroutine[Any, Any, None]: ...
def get_envs(*, env_list = ...) -> Coroutine[Any, Any, list]: ...
