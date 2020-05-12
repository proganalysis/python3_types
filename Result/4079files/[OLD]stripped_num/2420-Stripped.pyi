# (generated with --quick)

from typing import Any, Dict

BASE: int
NEG_SYMBOL: str
SYMBOLS: str
SYMBOLS_VALUE: Dict[str, int]
argparse: module
collections: module
hashlib: module
is_list_or_tuple: Any
json: module
numbers: module
random: module
string: module

class HashableNamespace(argparse.Namespace):
    hash_ignore: set
    def __init__(self, *args, **kwargs) -> None: ...

def compact_hash_obj(obj, ignore_unhashable = ...) -> str: ...
def decode_compact64(value, symbols_value = ..., base = ..., neg_symbol = ...) -> Any: ...
def encode_compact64(value, symbols = ..., base = ..., neg_symbol = ...) -> str: ...
def get_file_hash(fname, fn = ...) -> Any: ...
def hash_obj(obj, ignore_unhashable = ...) -> int: ...
def numpy_hash(arr) -> int: ...
def randstr(n) -> str: ...
