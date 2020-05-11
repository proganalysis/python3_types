# (generated with --quick)

from typing import Any, Generator, Iterable, Set, Tuple, TypeVar

BaseDialect: Any
DEFAULT_CONNECTOR: str
DatabaseException: Any
NO_DEFAULT: Any
__path__: Iterable[str]
io: module
itertools: module
md_column: Any
md_index: Any
md_types: Any
operator: module

_T1 = TypeVar('_T1')

class MysqlDialect(Any):
    __doc__: str
    has_cascade: bool
    has_checkpoints: bool
    has_default: bool
    has_ilike: bool
    has_returns: bool
    has_serial: bool
    has_truncate: bool
    lastval_method: str
    def get_column_sql(self, table_name = ..., *, emitter) -> str: ...
    def get_index_sql(self, table_name = ..., *, emitter) -> str: ...
    def get_primary_key_index_name(self, table) -> str: ...
    def get_unique_column_index_name(self, table_name, column_name: _T1) -> _T1: ...
    def get_upsert_sql(self, table_name, *, on_conflict_update = ...) -> Tuple[str, Set[str]]: ...
    def transform_rows_to_columns(self, *rows, table_name = ...) -> Generator[Any, Any, None]: ...
    def transform_rows_to_indexes(self, *rows, table_name = ...) -> Generator[Any, Any, None]: ...

def extend_path(path: Iterable[str], name: str) -> Iterable[str]: ...
