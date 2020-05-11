# (generated with --quick)

from typing import List, Tuple

pickle: module
struct: module

class PickleProtocol:
    def _format_data(self, metric: str, value: int, timestamp: int) -> Tuple[str, Tuple[int, int]]: ...
    def generate_message(self, listOfTuples: List[Tuple[str, int, int]]) -> bytes: ...

class PlaintextProtocol:
    def _format_data(self, metric: str, value: int, timestamp: int) -> str: ...
    def generate_message(self, listOfTuples: List[Tuple[str, int, int]]) -> bytes: ...
