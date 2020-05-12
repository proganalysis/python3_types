# (generated with --quick)

from typing import Any, Generator, Type, TypeVar

_graph: Any
credentials: Any
datetime: Type[datetime.datetime]
dateutil: module
facebook: Any
json: module
requests: module
sys: module

_T0 = TypeVar('_T0')

def add_likers(post) -> None: ...
def distill_post(post: _T0, keys_to_delete) -> _T0: ...
def gen_all_posts(pageid: str, date_from: str, date_to: str, post_filter: object = ..., keys_to_delete: list = ...) -> list: ...
def gen_likers(postid) -> Generator[Any, Any, None]: ...
def init() -> None: ...
