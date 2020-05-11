# (generated with --quick)

import typing
from typing import Any, Generator, List, Optional, Tuple, Type

Counter: Type[typing.Counter]
csv: module
gzip: module

class FormalPreferences:
    __doc__: str
    _csv_file: Any
    atl_n: Any
    btl_n: Any
    header_2016: List[str]
    header_2019: List[str]
    def __init__(self, csv_file, atl_n, btl_n) -> None: ...
    def __iter__(self) -> Generator[Tuple[Tuple[Optional[int], ...], int], Any, None]: ...
