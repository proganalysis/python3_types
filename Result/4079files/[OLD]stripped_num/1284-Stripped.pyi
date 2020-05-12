# (generated with --quick)

import enum
import pathlib
from typing import Any, Type

Enum: Type[enum.Enum]
Path: Type[pathlib.Path]
StrBytes: Any
json: Any
pickle: module

class Protocol(str, enum.Enum):
    json: str
    pickle: str

def load_file(path, *, content_type = ..., encoding = ..., proto = ..., allow_pickle = ...) -> Any: ...
def load_str_bytes(b, *, content_type = ..., encoding = ..., proto = ..., allow_pickle = ...) -> Any: ...
