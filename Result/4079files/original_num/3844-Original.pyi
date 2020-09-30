# (generated with --quick)

import collections
from typing import Any, Callable, Iterable, List, Optional, Sized, Tuple, Type, TypeVar, Union

argparse: module
argparser: argparse.ArgumentParser
args: argparse.Namespace
argv: List[str]
blocks: List[Block]
cmd_fstar: Optional[Union[str, List[str]]]
cmd_fstar_ide: List[str]
cmd_vale: Optional[Union[str, List[str]]]
cmd_vale_split: List[str]
e: nothing
encoding: str
file_fstar: Any
file_vale: Any
file_vale_mod_time: Optional[float]
helper_text: str
inp: List[str]
json: module
l: List[str]
last: Optional[List[str]]
os: module
pipe: subprocess.Popen[bytes]
pushed_blocks: list
query_id: int
r: Any
shlex: module
subprocess: module
sys: module
time: module
typing: module

_T0 = TypeVar('_T0')
_TBlock = TypeVar('_TBlock', bound=Block)

class Block(tuple):
    __slots__ = ["line_number", "lines", "name"]
    __dict__: collections.OrderedDict[str, Union[int, list, str]]
    _field_defaults: collections.OrderedDict[str, Union[int, list, str]]
    _field_types: collections.OrderedDict[str, type]
    _fields: Tuple[str, str, str]
    line_number: int
    lines: list
    name: str
    def __getnewargs__(self) -> Tuple[str, list, int]: ...
    def __getstate__(self) -> None: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __new__(cls: Type[_TBlock], name: str, lines: list, line_number: int) -> _TBlock: ...
    def _asdict(self) -> collections.OrderedDict[str, Union[int, list, str]]: ...
    @classmethod
    def _make(cls: Type[_TBlock], iterable: Iterable[Union[int, list, str]], new = ..., len: Callable[[Sized], int] = ...) -> _TBlock: ...
    def _replace(self: _TBlock, **kwds: Union[int, list, str]) -> _TBlock: ...

class QueryError(Exception): ...

class ValeError(Exception): ...

def add_cmd(argv, short, long, args, name, dest, req) -> Any: ...
def check_block(pushed_blocks, blocks, name) -> None: ...
def get_cmd(cmd: _T0, arg) -> Union[str, _T0]: ...
def list_blocks(blocks) -> None: ...
def pop_block(pushed_blocks) -> None: ...
def push_block(pushed_blocks, block, kind) -> None: ...
def read_file() -> List[Block]: ...
def recv_response() -> None: ...
def send_query(q, args) -> None: ...
