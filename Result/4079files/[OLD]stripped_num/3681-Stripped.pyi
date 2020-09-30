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
    def download(self, raw_url, sha256sum) -> str: ...
    def download_latest_from_github(self, repo, branch = ..., username = ..., password = ...) -> str: ...
    def ensure_cache_exists(self) -> None: ...
    def inject_directory_tree(self, id, tree, base_target) -> bool: ...
    def is_cached_valid(self, filename, sha256sum) -> bool: ...
    def save_directory_tree(self, id, basepath, tree) -> None: ...

def stream_download(url, fn, output_file) -> None: ...
@overload
def urlparse(url: str, scheme: Optional[str] = ..., allow_fragments: bool = ...) -> urllib.parse.ParseResult: ...
@overload
def urlparse(url: Optional[bytes], scheme: Optional[bytes] = ..., allow_fragments: bool = ...) -> urllib.parse.ParseResultBytes: ...
