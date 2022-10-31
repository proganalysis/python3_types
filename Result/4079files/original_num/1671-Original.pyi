# (generated with --quick)

import requests.models
from typing import Any, Callable, List, Optional, Tuple, Type, TypeVar, Union
import urllib.parse

PARSERS: List[str]
RequestException: type
__version__: str
argparse: module
base64: module
bs4: Any
datetime: Type[datetime.datetime]
mimetypes: module
requests_get: Optional[Callable[..., requests.models.Response]]
sys: module

AnyStr = TypeVar('AnyStr', str, bytes)

def _get_options() -> argparse.Namespace: ...
def _get_resource(resource_url: str) -> Tuple[Any, Any]: ...
def _main() -> None: ...
def _main_wrapper() -> None: ...
def convert_page(page_path: str, parser: str = ..., callback: Callable[[str, str, str], None] = ..., ignore_errors: bool = ..., ignore_images: bool = ..., ignore_css: bool = ..., ignore_js: bool = ...) -> str: ...
def get_available_parsers() -> List[str]: ...
def make_data_uri(mimetype: str, data: bytes) -> str: ...
@overload
def quote(string: bytes, safe: Union[bytes, str] = ...) -> str: ...
@overload
def quote(string: str, safe: Union[bytes, str] = ..., encoding: str = ..., errors: str = ...) -> str: ...
def urljoin(base: AnyStr, url: Optional[AnyStr], allow_fragments: bool = ...) -> AnyStr: ...
@overload
def urlparse(url: str, scheme: Optional[str] = ..., allow_fragments: bool = ...) -> urllib.parse.ParseResult: ...
@overload
def urlparse(url: Optional[bytes], scheme: Optional[bytes] = ..., allow_fragments: bool = ...) -> urllib.parse.ParseResultBytes: ...