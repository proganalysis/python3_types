# (generated with --quick)

import collections
import decimal
from typing import Any, List, Type, Union

BinaryObject: Any
BoolObject: Any
Decimal: Type[decimal.Decimal]
DecimalObject: Any
GenericObjectMeta: Any
IntObject: Any
LongObject: Any
OrderedDict: Type[collections.OrderedDict]
String: Any
create_query: str
drop_query: str
insert_data: List[List[Union[int, str, decimal.Decimal]]]
insert_query: str
page_size: int
scheme_name: str
select_query: str
table_cache_name: str
table_sql_name: str

def __getattr__(name) -> Any: ...
def test_add_schema_to_binary_object(client) -> None: ...
def test_nested_binary_objects(client) -> None: ...
def test_sql_read_as_binary(client) -> None: ...
def test_sql_write_as_binary(client) -> None: ...
