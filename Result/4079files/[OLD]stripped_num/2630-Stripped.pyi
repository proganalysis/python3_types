# (generated with --quick)

from typing import Any, Generator

BaseZhihu: Any
JsonAsSoupMixin: Any

class Column(Any, Any):
    __doc__: str
    __init__: Any
    follower_num: Any
    name: Any
    post_num: Any
    posts: Generator[Any, Any, None]
    def _get_content(self) -> Any: ...
    def _make_soup(self) -> None: ...
    def _parse_post_data(self, post) -> Any: ...

def __getattr__(name) -> Any: ...
