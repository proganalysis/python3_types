# (generated with --quick)

import argparse
from typing import Any, Callable, List, Optional, Type, Union

ARCHIVE_DIR: Any
ArgumentParser: Type[argparse.ArgumentParser]
OUTPUT_DIR: Any
args: argparse.Namespace
p: argparse.ArgumentParser
re: module

def cleanup_index(regexes: List[str], proceed: bool, delete: bool) -> None: ...
def exists(path: Union[_PathLike, bytes, int, str]) -> bool: ...
@overload
def join(path: Union[bytes, _PathLike[bytes]], *paths: Union[bytes, _PathLike[bytes]]) -> bytes: ...
@overload
def join(path: Union[str, _PathLike[str]], *paths: Union[str, _PathLike[str]]) -> str: ...
def parse_json_links_index(out_dir = ...) -> Any: ...
def rmtree(path: Union[bytes, str, _PathLike[str]], ignore_errors: bool = ..., onerror: Optional[Callable[[Any, Any, Any], Any]] = ...) -> None: ...
def write_html_links_index(out_dir, links, finished = ...) -> None: ...
def write_json_links_index(out_dir, links) -> None: ...