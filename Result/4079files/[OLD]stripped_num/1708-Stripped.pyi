# (generated with --quick)

from typing import Any, Tuple, Union

Artist: Any
Jukebox: Any
Provider: Any
Request: Any
ResourceManager: Any
Track: Any
User: Any
re: module

class DeezerProvider(Any):
    __doc__: str
    jukebox: Any
    me: Any
    token: Any
    def __init__(self, token = ...) -> None: ...
    @staticmethod
    def authorize() -> Any: ...
    @staticmethod
    def get_entity_from_dz_url(url) -> Any: ...
    @staticmethod
    def get_info_from_dz_url(url) -> Tuple[int, Any]: ...

@overload
def quote(string: bytes, safe: Union[bytes, str] = ...) -> str: ...
@overload
def quote(string: str, safe: Union[bytes, str] = ..., encoding: str = ..., errors: str = ...) -> str: ...
