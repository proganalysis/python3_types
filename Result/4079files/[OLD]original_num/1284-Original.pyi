# (generated with --quick)

import enum
import pathlib
from typing import Any, Optional, Type, Union

Enum: Type[enum.Enum]
Path: Type[pathlib.Path]
StrBytes: Any
json: Any
pickle: module

class Protocol(str, enum.Enum):
    json: str
    pickle: str

def load_file(path: Union[str, pathlib.Path], *, content_type: Optional[str] = ..., encoding: str = ..., proto: Optional[Protocol] = ..., allow_pickle: bool = ...) -> Any: ...
def load_str_bytes(b, *, content_type: Optional[str] = ..., encoding: str = ..., proto: Optional[Protocol] = ..., allow_pickle: bool = ...) -> Any: ...
