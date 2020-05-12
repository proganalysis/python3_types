# (generated with --quick)

import ctypes
from typing import Any, Dict, Optional, Type, TypeVar, Union

CDLL: Type[ctypes.CDLL]
RESULT_SETTERS: Dict[Any, ctypes._FuncPointer]
SQLITE_DETERMINISTIC: Any
SQLITE_OK: Any
SQLITE_UTF8: Any
VALUE_EXTRACTORS: dict
_sqlite3_errmsg: ctypes._FuncPointer
c_char_p: Type[ctypes.c_char_p]
c_double: Type[ctypes.c_double]
c_int: Type[ctypes.c_int]
c_int64: Type[ctypes.c_int64]
c_void_p: Type[ctypes.c_void_p]
destroyfunc: Type[ctypes._FuncPointer]
finalizefunc: Type[ctypes._FuncPointer]
float64: Any
int32: Any
int64: Any
inversefunc: Type[ctypes._FuncPointer]
libsqlite3: ctypes.CDLL
optional: Any
scalarfunc: Type[ctypes._FuncPointer]
sqlite3_aggregate_context: ctypes._FuncPointer
sqlite3_create_function: ctypes._FuncPointer
sqlite3_create_window_function: ctypes._FuncPointer
sqlite3_path: Optional[str]
sqlite3_restype: Type[ctypes.c_int]
sqlite3_result_double: ctypes._FuncPointer
sqlite3_result_int: ctypes._FuncPointer
sqlite3_result_int64: ctypes._FuncPointer
sqlite3_result_null: ctypes._FuncPointer
sqlite3_value_type: ctypes._FuncPointer
stepfunc: Type[ctypes._FuncPointer]
value_methods: Dict[str, Type[Union[ctypes.c_double, ctypes.c_int, ctypes.c_int64]]]
valuefunc: Type[ctypes._FuncPointer]

_CT = TypeVar('_CT', bound=ctypes._CData)
_CT = TypeVar('_CT', bound=ctypes._CData)

def CFUNCTYPE(restype: Optional[Type[ctypes._CData]], *argtypes: Type[ctypes._CData], use_errno: bool = ..., use_last_error: bool = ...) -> Type[ctypes._FuncPointer]: ...
def POINTER(type: Type[_CT]) -> Type[ctypes.pointer[_CT]]: ...
def add_value_method(typename: str, restype) -> Any: ...
def find_library(name: str) -> Optional[str]: ...
def sqlite3_errmsg(db) -> Any: ...
