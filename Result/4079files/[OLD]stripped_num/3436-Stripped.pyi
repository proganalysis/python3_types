# (generated with --quick)

import __future__
from typing import Any, TypeVar

THeaderProtocol: Any
TTransport: Any
absolute_import: __future__._Feature
division: __future__._Feature
print_function: __future__._Feature
unicode_literals: __future__._Feature

AnyStr = TypeVar('AnyStr', str, bytes)
T = TypeVar('T')

def deserialize(protocol_factory, data: AnyStr, thr_out: T) -> T: ...
def serialize(protocol_factory, thr) -> AnyStr: ...
