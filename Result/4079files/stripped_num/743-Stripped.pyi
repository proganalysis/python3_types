# (generated with --quick)

import flask.app
import flask.wrappers
from typing import Any, Callable, NoReturn, Optional, Tuple, Type, TypeVar, Union
import werkzeug.wrappers

Flask: Type[flask.app.Flask]
app: flask.app.Flask
codecs_enabled: bool
decode: Callable
decode_audio: Any
download_audio: Callable
e: Any
encode: Callable
encode_ogg: Any
index: Callable
os: module
request: flask.wrappers.Request
rstatic: Callable
s: Callable
wave: module

AnyStr = TypeVar('AnyStr', str, bytes)

def abort(status: Union[int, werkzeug.wrappers.Response], *args, **kwargs) -> NoReturn: ...
def after_this_request(f) -> Any: ...
@overload
def join(path: Union[bytes, _PathLike[bytes]], *paths: Union[bytes, _PathLike[bytes]]) -> bytes: ...
@overload
def join(path: Union[str, _PathLike[str]], *paths: Union[str, _PathLike[str]]) -> str: ...
def make_response(*args) -> Any: ...
def mkstemp(suffix: Optional[AnyStr] = ..., prefix: Optional[AnyStr] = ..., dir: Optional[Union[_PathLike[AnyStr], AnyStr]] = ..., text: bool = ...) -> Tuple[int, AnyStr]: ...
def send_file(filename_or_fp, mimetype = ..., as_attachment: bool = ..., attachment_filename = ..., add_etags: bool = ..., cache_timeout = ..., conditional: bool = ..., last_modified = ...) -> Any: ...
def send_from_directory(directory, filename, **options) -> Any: ...
