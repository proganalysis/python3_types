# (generated with --quick)

import chattymarkov.database.databases
from typing import Any, Callable, Dict, Optional, Tuple, Type, Union

JSONFileDatabase: Type[chattymarkov.database.databases.JSONFileDatabase]
MemoryDatabase: Type[chattymarkov.database.databases.MemoryDatabase]
MemoryDatabaseAsync: Type[chattymarkov.database.databases.MemoryDatabaseAsync]
RedisDatabase: Type[chattymarkov.database.databases.RedisDatabase]
RedisDatabaseAsync: Type[chattymarkov.database.databases.RedisDatabaseAsync]
_DATABASE_PREFIXES: Dict[str, Any]

class ChattymarkovDatabaseError(Exception):
    __doc__: str

class InvalidConnectionStringError(ChattymarkovDatabaseError):
    __doc__: str

class UnknownDatabasePrefixError(ChattymarkovDatabaseError):
    __doc__: str

def _get_connection_params(resource) -> Tuple[Any, Any]: ...
def build_async_memory_database(resource) -> chattymarkov.database.databases.MemoryDatabaseAsync: ...
def build_database_connection(connect_string) -> Any: ...
def build_json_database(resource) -> chattymarkov.database.databases.JSONFileDatabase: ...
def build_memory_database(resource) -> chattymarkov.database.databases.MemoryDatabase: ...
def build_redis_database(resource, is_async = ...) -> Optional[Union[chattymarkov.database.databases.RedisDatabase, chattymarkov.database.databases.RedisDatabaseAsync]]: ...
def build_redis_database_async(resource) -> Optional[chattymarkov.database.databases.RedisDatabaseAsync]: ...
def database(prefix) -> Callable[[Any], Any]: ...
def get_database_builder(prefix) -> Callable: ...
