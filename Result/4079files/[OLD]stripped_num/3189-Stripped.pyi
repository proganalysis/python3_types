# (generated with --quick)

from typing import Any

db: functools._lru_cache_wrapper
functools: module
pathlib: module

class DB:
    __doc__: str
    def __repr__(self) -> str: ...

class MysqlDB(DB):
    charset: Any
    database: Any
    host: Any
    password: Any
    port: Any
    ssl: Any
    user: Any
    def __init__(self, host = ..., port = ..., database = ..., user = ..., password = ..., ssl = ..., charset = ...) -> None: ...

class OracleDB(DB):
    endpoint: Any
    host: Any
    password: Any
    port: Any
    user: Any
    def __init__(self, host = ..., port = ..., endpoint = ..., user = ..., password = ...) -> None: ...

class PostgreSQLDB(DB):
    database: Any
    host: Any
    password: Any
    port: Any
    sslcert: Any
    sslkey: Any
    sslmode: Any
    sslrootcert: Any
    user: Any
    def __init__(self, host = ..., port = ..., database = ..., user = ..., password = ..., sslmode = ..., sslrootcert = ..., sslcert = ..., sslkey = ...) -> None: ...

class RedshiftDB(PostgreSQLDB):
    database: Any
    host: Any
    password: Any
    port: Any
    sslcert: None
    sslkey: None
    sslmode: None
    sslrootcert: None
    user: Any
    def __init__(self, host = ..., port = ..., database = ..., user = ..., password = ...) -> None: ...

class SQLServerDB(DB):
    database: Any
    host: Any
    password: Any
    user: Any
    def __init__(self, host = ..., database = ..., user = ..., password = ...) -> None: ...

class SQLiteDB(DB):
    file_name: Any
    def __init__(self, file_name) -> None: ...
