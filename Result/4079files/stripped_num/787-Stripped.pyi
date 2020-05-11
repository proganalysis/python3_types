# (generated with --quick)

from typing import Any, Callable, Coroutine, Dict, IO, Optional, TypeVar

CosineSimilarity: Any
MotorBase: Any
asyncio: module
collections: module
get_time: Any
os: module
uvloop: Any

_T = TypeVar('_T')

def deepcopy(x: _T, memo: Optional[Dict[int, _T]] = ..., _nil = ...) -> _T: ...
def get_user_tag() -> Coroutine[Any, Any, None]: ...
def get_user_tag_test() -> None: ...
def itemgetter(*items) -> Callable[[Any], tuple]: ...
def pprint(object: object, stream: Optional[IO[str]] = ..., indent: int = ..., width: int = ..., depth: Optional[int] = ..., *, compact: bool = ...) -> None: ...
