# (generated with --quick)

import enum
from typing import Any, Callable, Coroutine, Type

Enum: Type[enum.Enum]
GraphQLArgument: Any
GraphQLEnumTest: Any
GraphQLField: Any
GraphQLObjectType: Any
GraphQLPythonEnumType: Any
GraphQLSchema: Any
graphql: Any
pytest: Any
pytestmark: Any

class EnumTest(enum.Enum):
    VALUE_ONE: str
    VALUE_TWO: str

def define_schema(resolver: Callable, enumType) -> Any: ...
def test_enum_args() -> Coroutine[Any, Any, None]: ...
def test_out_enum() -> Coroutine[Any, Any, None]: ...
