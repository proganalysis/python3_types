# (generated with --quick)

from typing import Any, Generator, Tuple

class SpecReader:
    resource_reader: Any
    def __init__(self, resource_reader) -> None: ...
    def read(self, spec_locations) -> Generator[Tuple[Any, Any], Any, None]: ...
