from typing import Any

default_encoding: str
default_errors: str

def encode(str_obj: Any, encoding: Any = ..., errors: Any = ...): ...
def decode(bytes_obj: Any, encoding: Any = ..., errors: Any = ...): ...
