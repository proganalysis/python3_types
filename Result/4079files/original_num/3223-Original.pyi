# (generated with --quick)

from typing import Any, Optional

GraphQLDate: Any
GraphQLScalarType: Any
StringValue: Any
Value: Any
datetime: module
iso8601: Any

def coerce_date(value) -> Optional[datetime.datetime]: ...
def parse_date_literal(ast) -> Optional[datetime.datetime]: ...
def serialize_date(value: datetime.datetime) -> str: ...
def typed_parse_date(value) -> datetime.datetime: ...
