# (generated with --quick)

import contextlib
import pathlib
from typing import Any, Callable, List, Type, Union

CHUNK_SIZE: int
CREATED: List[str]
DELAY: int
DOWNLOAD: str
FILENAME: str
LOGGER: logging.Logger
LONG_DELAY: int
MAX_RETRIES: int
PREFIX_LEN: int
Path: Type[pathlib.Path]
SEARCH: str
STATUS_FILENAME: str
YEARS: List[int]
_download_file: Callable
_fetch_items: Callable
argparse: module
closing: Type[contextlib.closing]
config_dict: Any
config_logging: Any
functools: module
logging: module
random: module
requests: module
time: module

def _download_repos(language, repos, destination) -> None: ...
def _rest() -> None: ...
def _retrieve_repo_details(language, nb_repos, token) -> list: ...
def _wait() -> None: ...
def main() -> None: ...
@overload
def quote_plus(string: bytes, safe: Union[bytes, str] = ...) -> str: ...
@overload
def quote_plus(string: str, safe: Union[bytes, str] = ..., encoding: str = ..., errors: str = ...) -> str: ...
def retry(default = ...) -> Callable[[Any], Any]: ...
