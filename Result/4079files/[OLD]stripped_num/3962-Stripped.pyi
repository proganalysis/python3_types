# (generated with --quick)

import types
import typing
from typing import Any, IO, Optional, Type

BU_353_Antenna: types.SimpleNamespace
CP300i: types.SimpleNamespace
Counter: Type[typing.Counter]
Listener: Any
Logging: Any
Sentence_Factory: Any
SimpleNamespace: Type[types.SimpleNamespace]
device: types.SimpleNamespace
listener: Any
logged: Any
logging: module
sys: module

def pprint(object: object, stream: Optional[IO[str]] = ..., indent: int = ..., width: int = ..., depth: Optional[int] = ..., *, compact: bool = ...) -> None: ...
def sample_CP(listener) -> None: ...
def sample_GPS(listener, limit = ...) -> None: ...
