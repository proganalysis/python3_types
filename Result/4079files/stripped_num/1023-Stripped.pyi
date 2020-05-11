# (generated with --quick)

from typing import Any, Dict, List

BulkDimension: Any
CachedDimension: Any
Dimension: Any
FactTable: Any

class Dim(Any):
    __dbschema__: str
    _lookup_fields: List[nothing]
    id: Any
    @classmethod
    def cls_create_dbname(cls) -> str: ...
    @classmethod
    def cls_get_column_names_no_id(cls) -> list: ...
    @classmethod
    def cls_get_lookup_fields(cls) -> list: ...
    @classmethod
    def cls_to_pygram_bulk_dim(cls, schema_name, lookup_fields = ..., bulkloader = ...) -> Any: ...
    @classmethod
    def cls_to_pygram_dim(cls, schema_name, lookup_fields = ...) -> Any: ...
    @classmethod
    def cls_to_pygram_mapping(cls) -> Dict[Any, str]: ...

class DmReference(Any):
    fk: Any
    def __init__(self, dim_cls, fk_name = ...) -> None: ...

class Fact(Any):
    @classmethod
    def cls_create_dbname(cls) -> str: ...
    @classmethod
    def cls_get_key_names(cls) -> list: ...
    @classmethod
    def cls_get_measure_names(cls) -> list: ...
    @classmethod
    def cls_to_pygram_fact(cls, schema_name) -> Any: ...

def __getattr__(name) -> Any: ...
