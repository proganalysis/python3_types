# (generated with --quick)

from typing import Optional

db: functools._lru_cache_wrapper
functools: module
pathlib: module

class DB:
    __doc__: str
    def __repr__(self) -> str: ...

class MysqlDB(DB):
    charset: Optional[str]
    database: Optional[str]
    host: Optional[str]
    password: Optional[str]
    port: Optional[int]
    ssl: Optional[bool]
    user: Optional[str]
    def __init__(self, host: Optional[str] = ..., port: Optional[int] = ..., database: Optional[str] = ..., user: Optional[str] = ..., password: Optional[str] = ..., ssl: bool = ..., charset: Optional[str] = ...) -> None: ...

class OracleDB(DB):
    endpoint: Optional[str]
    host: Optional[str]
    password: Optional[str]
    port: int
    user: Optional[str]
    def __init__(self, host: Optional[str] = ..., port: int = ..., endpoint: Optional[str] = ..., user: Optional[str] = ..., password: Optional[str] = ...) -> None: ...

class PostgreSQLDB(DB):
    database: Optional[str]
    host: Optional[str]
    password: Optional[str]
    port: Optional[int]
    sslcert: Optional[str]
    sslkey: Optional[str]
    sslmode: Optional[str]
    sslrootcert: Optional[str]
    user: Optional[str]
    def __init__(self, host: Optional[str] = ..., port: Optional[int] = ..., database: Optional[str] = ..., user: Optional[str] = ..., password: Optional[str] = ..., sslmode: Optional[str] = ..., sslrootcert: Optional[str] = ..., sslcert: Optional[str] = ..., sslkey: Optional[str] = ...) -> None: ...

class RedshiftDB(PostgreSQLDB):
    database: Optional[str]
    host: Optional[str]
    password: Optional[str]
    port: Optional[int]
    sslcert: Optional[str]
    sslkey: Optional[str]
    sslmode: Optional[str]
    sslrootcert: Optional[str]
    user: Optional[str]
    def __init__(self, host: Optional[str] = ..., port: Optional[int] = ..., database: Optional[str] = ..., user: Optional[str] = ..., password: Optional[str] = ...) -> None: ...

class SQLServerDB(DB):
    database: Optional[str]
    host: Optional[str]
    password: Optional[str]
    user: Optional[str]
    def __init__(self, host: Optional[str] = ..., database: Optional[str] = ..., user: Optional[str] = ..., password: Optional[str] = ...) -> None: ...

class SQLiteDB(DB):
    file_name: pathlib.Path
    def __init__(self, file_name: pathlib.Path) -> None: ...
