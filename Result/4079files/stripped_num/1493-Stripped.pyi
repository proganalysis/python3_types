# (generated with --quick)

from typing import Any, List, Tuple, Union

Page: Any
__all__: List[str]
blah_decorate: Any
exc: Any
re: module

class File(Any):
    _dimensions: Tuple[Any, Any]
    _exists: bool
    _hash: Any
    _mime: Any
    _size: Any
    _uploader: Any
    _url: Any
    dimensions: Any
    hash: Any
    mime: Any
    size: Any
    uploader: Any
    def load_attributes(self, res = ...) -> None: ...
    def upload(self, fileobj, text, summary, watch = ..., key = ...) -> Any: ...
    def url(self, width = ..., height = ...) -> str: ...

def decorate(meth) -> Any: ...
@overload
def quote(string: bytes, safe: Union[bytes, str] = ...) -> str: ...
@overload
def quote(string: str, safe: Union[bytes, str] = ..., encoding: str = ..., errors: str = ...) -> str: ...
