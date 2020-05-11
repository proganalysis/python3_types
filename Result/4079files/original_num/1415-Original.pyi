# (generated with --quick)

from typing import Any

GObject: Any

class Sink(Stream):
    __doc__: str
    _is_active: bool
    card_index: int
    description: str
    display_name: str
    index: int
    name: str
    ports: dict

class Source(Stream):
    __doc__: str
    _is_active: bool
    card_index: int
    description: str
    display_name: str
    index: int
    name: str
    ports: dict

class Stream(Any):
    __doc__: str
    _is_active: bool
    card_index: int
    description: str
    display_name: str
    index: int
    is_active: Any
    name: str
    ports: dict
    def __init__(self, index: int, name: str, display_name: str, description: str, ports: dict, card_index: int) -> None: ...
    def activate_port_by_name(self, name: str) -> None: ...
    def get_display_name(self) -> str: ...
    def get_is_active(self) -> bool: ...
    def set_is_active(self, value: bool) -> None: ...
