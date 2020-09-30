# (generated with --quick)

import functools
import typing
from typing import Any, Coroutine, Optional, Type

Collection: Type[typing.Collection]
Field: Any
Func: Any
Mapping: Type[typing.Mapping]
aiofiles: Any
asyncio: module
os: module
partial: Type[functools.partial]

class csv_writer:
    delimiter: Any
    fh: Any
    fieldnames: Optional[list]
    def __init__(self, fh, fieldnames = ..., delimiter = ...) -> None: ...
    def writeheader(self, fieldnames = ...) -> Coroutine[Any, Any, None]: ...
    def writerow(self, row) -> Coroutine[Any, Any, None]: ...

def aiodump_csv(query, file_or_name, loop = ..., include_header = ..., close_file = ..., append = ..., csv_writer = ...) -> coroutine: ...
