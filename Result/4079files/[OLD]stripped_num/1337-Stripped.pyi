# (generated with --quick)

from typing import Any, TypeVar

csv: module

_TRF2DictWriter = TypeVar('_TRF2DictWriter', bound=RF2DictWriter)

class RF2DictWriter(csv.DictWriter):
    __doc__: str
    _f: Any
    def __enter__(self: _TRF2DictWriter) -> _TRF2DictWriter: ...
    def __exit__(self, exc_type, exc_val, exc_tb) -> None: ...
    def __init__(self, f, *args, **argv) -> None: ...
