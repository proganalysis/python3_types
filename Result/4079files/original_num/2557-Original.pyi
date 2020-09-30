# (generated with --quick)

from typing import Any, Coroutine, Optional, Tuple

TLRequest: Any
TelegramClient: Any
_NOT_A_REQUEST: Any
functions: Any
functools: module
helpers: Any
inspect: module
typing: module
utils: Any

class AccountMethods:
    def end_takeout(self, success: bool) -> Coroutine[Any, Any, bool]: ...
    def takeout(self, finalize: bool = ..., *, contacts: bool = ..., users: bool = ..., chats: bool = ..., megagroups: bool = ..., channels: bool = ..., files: bool = ..., max_file_size: bool = ...) -> Any: ...

class _TakeoutClient:
    _TakeoutClient__PROXY_INTERFACE: Tuple[str, str, str, str]
    _TakeoutClient__client: Any
    _TakeoutClient__finalize: Any
    _TakeoutClient__request: Any
    _TakeoutClient__success: Optional[bool]
    __doc__: str
    __enter__: Any
    __exit__: Any
    success: Any
    def __aenter__(self) -> Coroutine[Any, Any, _TakeoutClient]: ...
    def __aexit__(self, exc_type, exc_value, traceback) -> Coroutine[Any, Any, None]: ...
    def __call__(self, request, ordered = ...) -> coroutine: ...
    def __getattr__(self, name) -> Any: ...
    def __getattribute__(self, name) -> Any: ...
    def __init__(self, finalize, client, request) -> None: ...
    def __setattr__(self, name, value) -> None: ...
