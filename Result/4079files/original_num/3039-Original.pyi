# (generated with --quick)

from typing import Any, Dict, NoReturn, Optional, Sequence, TypeVar

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

def _bytes_escape(bs: bytes, *, quote: Optional[str] = ...) -> str: ...
def _bytes_unescape(string: str) -> bytes: ...
def _decompose_flags(value: F) -> Sequence[F]: ...
def _filter_resources(rf, filters: Sequence[str]) -> Sequence: ...
def _hexdump(data: bytes) -> None: ...
def _raw_hexdump(data: bytes) -> None: ...
def main() -> NoReturn: ...
