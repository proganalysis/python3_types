from typing import Any

def resolve(func: Any, query_value: Any, value: Any, operator_str: str) -> Any: ...
def matcher_level(value: Any, query: Any, operator_str: str) -> Any: ...
def find(obj: Any, query: Any, operator_str: str=...) -> Any: ...
def contains(item: Any, array: Any): ...
def equal(a: Any, b: Any): ...
def has_key(key: Any, value: Any): ...
def in_(array: Any, value: Any): ...
def greater(a: Any, b: Any): ...
def greater_equal(a: Any, b: Any): ...
def less(a: Any, b: Any): ...
def less_equal(a: Any, b: Any): ...

FUNCS: Any
