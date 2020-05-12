# (generated with --quick)

from typing import Any

class EmptySegment(Segment):
    __doc__: str
    _is_executable: Any
    _is_readable: Any
    _is_writable: Any
    filesize: int
    is_executable: Any
    is_readable: Any
    is_writable: Any
    memsize: Any
    offset: int
    only_contains_uninitialized_data: bool
    vaddr: Any
    def __init__(self, vaddr, memsize, is_readable = ..., is_writable = ..., is_executable = ...) -> None: ...

class Region:
    __doc__: str
    filesize: Any
    max_addr: Any
    max_offset: Any
    memsize: Any
    min_addr: Any
    offset: Any
    vaddr: Any
    def __init__(self, offset, vaddr, filesize, memsize) -> None: ...
    def __repr__(self) -> str: ...
    def _rebase(self, delta) -> None: ...
    def addr_to_offset(self, addr) -> Any: ...
    def contains_addr(self, addr) -> Any: ...
    def contains_offset(self, offset) -> Any: ...
    def is_executable(self) -> bool: ...
    def is_readable(self) -> bool: ...
    def is_writable(self) -> bool: ...
    def min_offset(self) -> Any: ...
    def offset_to_addr(self, offset) -> Any: ...

class Section(Region):
    __doc__: str
    filesize: Any
    memsize: Any
    name: Any
    offset: Any
    vaddr: Any
    def __init__(self, name, offset, vaddr, size) -> None: ...

class Segment(Region):
    filesize: Any
    memsize: Any
    offset: Any
    vaddr: Any
