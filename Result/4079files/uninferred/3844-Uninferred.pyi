import typing
from typing import Any

def add_cmd(argv: Any, short: Any, long: Any, args: Any, name: Any, dest: Any, req: Any): ...

argv: Any
helper_text: str
argparser: Any
cmd_fstar: Any
cmd_vale: Any
args: Any

def get_cmd(cmd: Any, arg: Any): ...

cmd_fstar_ide: Any
file_fstar: Any
l: Any
file_vale: Any
cmd_vale_split: Any
file_vale_mod_time: Any
pipe: Any

class Block(typing.NamedTuple):
    name: str
    lines: list
    line_number: int

class QueryError(Exception): ...
class ValeError(Exception): ...

def read_file(): ...
def list_blocks(blocks: Any) -> None: ...

query_id: int
encoding: str

def send_query(q: Any, args: Any) -> None: ...
def recv_response() -> None: ...
def pop_block(pushed_blocks: Any) -> None: ...
def push_block(pushed_blocks: Any, block: Any, kind: Any) -> None: ...
def check_block(pushed_blocks: Any, blocks: Any, name: Any) -> None: ...

blocks: Any
pushed_blocks: Any
last: Any
inp: Any
inp = last
last = inp
e: Any
