# (generated with --quick)

import pathlib
import requests.auth
from typing import Any, Optional, Type
import urllib.parse

HTTPBasicAuth: Type[requests.auth.HTTPBasicAuth]
Path: Type[pathlib.Path]
default_cache_dir: pathlib.Path
get_logger: Any
hashlib: module
logger: Any
os: module
requests: module
shutil: module
sys: module
tempfile: module

class FileCache:
    cache_dir: pathlib.Path
    def __init__(self, cache_dir = ...) -> None: ...
    def download(self, raw_url: str, sha256sum: str) -> str: ...
    def download_latest_from_github(self, repo: str, branch: str = ..., username: Optional[str] = ..., password: Optional[str] = ...) -> str: ...
    def ensure_cache_exists(self) -> None: ...
    def inject_directory_tree(self, id: str, tree: str, base_target: str) -> bool: ...
    def is_cached_valid(self, filename: str, sha256sum: str) -> bool: ...
    def save_directory_tree(self, id: str, basepath: str, tree: str) -> None: ...

def stream_download(url: str, fn: str, output_file: str) -> None: ...
@overload
def urlparse(url: str, scheme: Optional[str] = ..., allow_fragments: bool = ...) -> urllib.parse.ParseResult: ...
@overload
def urlparse(url: Optional[bytes], scheme: Optional[bytes] = ..., allow_fragments: bool = ...) -> urllib.parse.ParseResultBytes: ...
