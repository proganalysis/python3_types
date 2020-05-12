# (generated with --quick)

from typing import Any, Callable, Coroutine, Dict, Iterable, Optional

Context: Any
asyncio: module
discord: Any
typing: module

class ListPaginator(Paginator):
    _client: Any
    _embed: None
    _message: None
    _page: None
    _stopped: None
    delete_msg: bool
    delete_msg_timeout: bool
    footer: str
    navigation: Dict[str, Callable]
    pages: list
    predicate: Callable[[Any, Any], Any]
    target: Any
    timeout: int
    def __init__(self, ctx, _list: list, per_page = ..., **kwargs) -> None: ...

class Paginator:
    _client: Any
    _embed: Any
    _message: Any
    _page: Any
    _stopped: Optional[bool]
    delete_msg: Any
    delete_msg_timeout: Any
    footer: str
    navigation: Dict[str, Callable]
    pages: list
    predicate: Any
    target: Any
    timeout: Any
    def __init__(self, ctx, pages: Iterable, *, timeout = ..., delete_message = ..., predicate = ..., delete_message_on_timeout = ...) -> None: ...
    def _clear_reactions(self) -> Coroutine[Any, Any, None]: ...
    def begin(self) -> Coroutine[Any, Any, nothing]: ...
    def first_page(self) -> Coroutine[Any, Any, None]: ...
    def format_page(self) -> Coroutine[Any, Any, None]: ...
    def last_page(self) -> Coroutine[Any, Any, None]: ...
    def next_page(self) -> Coroutine[Any, Any, None]: ...
    def previous_page(self) -> Coroutine[Any, Any, None]: ...
    def stop(self, *, delete = ...) -> Coroutine[Any, Any, None]: ...
