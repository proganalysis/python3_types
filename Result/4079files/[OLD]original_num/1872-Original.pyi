# (generated with --quick)

from typing import Any, Type, TypeVar

c_float: Type[ctypes.c_float]
ctypes: module
os: module

_T = TypeVar('_T')

class DynamicStructure:
    _fields_: None
    def __new__(cls, file_path = ..., *args, **kwargs) -> Any: ...

def copy(x: _T) -> _T: ...
def get_offset(struct_ob, name) -> Any: ...
def get_size(struct_ob, name) -> Any: ...
def parse_fields(sequence_of_tuples, file_path_or_buffer = ..., **kwargs) -> tuple: ...
