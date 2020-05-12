# (generated with --quick)

from typing import Any, Optional, TypeVar, Union

GraphQLDate: Any
GraphQLScalarType: Any
StringValue: Any
Value: Any
datetime: module
iso8601: Any

_T0 = TypeVar('_T0')

def coerce_date(value: _T0) -> Optional[Union[datetime.datetime, _T0]]: ...
def parse_date_literal(ast) -> Optional[datetime.datetime]: ...
def serialize_date(value) -> Any: ...
def typed_parse_date(value) -> datetime.datetime: ...
