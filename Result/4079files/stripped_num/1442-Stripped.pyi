# (generated with --quick)

import sqlite3.dbapi2
from typing import Any, List, Optional

__all__: List[str]
__author__: str
__version__: str
os: module
sqlite3: module
uuid: module

class NamesDB(object):
    __slots__ = ["_db"]
    __doc__: str
    _db: Optional[SQLiteDB]
    def __init__(self, data_path) -> None: ...
    def close(self) -> None: ...
    def query_instid() -> None: ...
    def retrieve(version: NamesDB, keys) -> None: ...
    def submit(version: NamesDB, names) -> None: ...

class SQLiteDB(sqlite3.dbapi2.Connection):
    __slots__ = ["query"]
    __doc__: str
    query: Optional[sqlite3.dbapi2.Cursor]
    def cursor(self) -> Any: ...
