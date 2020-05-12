# (generated with --quick)

from typing import Any, Dict, NoReturn, Optional, TypeVar

_REZ_ATTR_NAMES: Dict[Any, Optional[str]]
_TRANSLATE_NONPRINTABLES: Dict[Any, str]
__version__: Any
api: Any
argparse: module
collections: module
compress: Any
enum: module
sys: module
textwrap: module
typing: module

F = TypeVar('F', bound=enum.Flag)

def _bytes_escape(bs, *, quote = ...) -> str: ...
def _bytes_unescape(string) -> bytes: ...
def _decompose_flags(value) -> list: ...
def _filter_resources(rf, filters) -> list: ...
def _hexdump(data) -> None: ...
def _raw_hexdump(data) -> None: ...
def main() -> NoReturn: ...
