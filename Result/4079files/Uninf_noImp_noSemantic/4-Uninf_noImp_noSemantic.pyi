from typing import Any

nodes: Any

def int_literal(number: Any): ...
def float_literal(number: Any): ...
def string_literal(string: Any): ...
def list_literal(seq: Any): ...
def tuple_literal(seq: Any): ...
def time_literal(time: Any) -> None: ...
def set_literal(seq: Any) -> None: ...
def dict_literal(dic: Any) -> None: ...

parsers: Any

def parse_item(item: Any): ...
def stack_literal(stack: Any): ...