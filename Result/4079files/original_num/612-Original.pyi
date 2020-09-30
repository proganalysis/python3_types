# (generated with --quick)

import functools
import sqlite3.dbapi2
from typing import Any, Optional, Type

SQLITE3_UPDATE_HOOK_CB: Type[ctypes._FuncPointer]
_sqlite3: Any
ctypes: module
enum: module
is_debug_python: bool
partial: Type[functools.partial]
sqlite3: module
sqlite3_conn_db_field_offset: int
sqlite3_lib: ctypes.PyDLL
sys: module

class Connection(sqlite3.dbapi2.Connection):
    _update_hook: Any
    _update_hook_cb: Optional[ctypes._FuncPointer]
    _update_hook_last_error: None
    def last_update_hook_error(self) -> Any: ...
    def set_update_hook(self, hook = ...) -> Any: ...

class UpdateHookOps(enum.Enum):
    SQLITE_DELETE: int
    SQLITE_INSERT: int
    SQLITE_UPDATE: int

def connect(database, **kwargs) -> sqlite3.dbapi2.Connection: ...
def hook_adapter(hook, conn, _, op, db_name, table_name, rowid) -> None: ...
