# (generated with --quick)

import typing
from typing import Any, Type, TypeVar

Atomic: Any
Sequence: Type[typing.Sequence]
SerializationError: Any

_T0 = TypeVar('_T0')

def deserialize(serial: _T0) -> _T0: ...
def serializable(obj) -> bool: ...
def serialize(obj: _T0) -> _T0: ...
