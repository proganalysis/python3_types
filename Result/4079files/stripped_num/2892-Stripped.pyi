# (generated with --quick)

from typing import List

hashlib: module
os: module
sys: module
tmpdir: None

def _cache_path(key) -> str: ...
def _cache_path_prefix(key) -> str: ...
def _hash(x) -> str: ...
def _prefixes(key) -> List[str]: ...
def clear_storage() -> None: ...
def cp(src, dst, recursive = ...) -> None: ...
def ls(url, recursive = ...) -> List[str]: ...
def main() -> None: ...
def rm(url, recursive = ...) -> None: ...