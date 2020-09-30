from pyignite.datatypes.prop_codes import *
from typing import Any

insert_data: Any
page_size: int
scheme_name: str
table_sql_name: str
table_cache_name: Any
create_query: Any
insert_query: Any
select_query: Any
drop_query: Any

def test_sql_read_as_binary(client: Any) -> None: ...
def test_sql_write_as_binary(client: Any) -> None: ...
def test_nested_binary_objects(client: Any) -> None: ...
def test_add_schema_to_binary_object(client: Any) -> None: ...
