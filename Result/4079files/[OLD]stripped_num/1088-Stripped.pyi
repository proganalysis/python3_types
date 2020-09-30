# (generated with --quick)

from typing import Tuple, TypeVar

pickle: module
struct: module

_T0 = TypeVar('_T0')
_T1 = TypeVar('_T1')
_T2 = TypeVar('_T2')

class PickleProtocol:
    def _format_data(self, metric: _T0, value: _T1, timestamp: _T2) -> Tuple[_T0, Tuple[_T2, _T1]]: ...
    def generate_message(self, listOfTuples) -> bytes: ...

class PlaintextProtocol:
    def _format_data(self, metric, value, timestamp) -> str: ...
    def generate_message(self, listOfTuples) -> bytes: ...
