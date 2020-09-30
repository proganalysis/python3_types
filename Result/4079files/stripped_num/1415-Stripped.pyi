# (generated with --quick)

from typing import Any

GObject: Any

class Sink(Stream):
    __doc__: str
    _is_active: bool
    card_index: Any
    description: Any
    display_name: Any
    index: Any
    name: Any
    ports: Any

class Source(Stream):
    __doc__: str
    _is_active: bool
    card_index: Any
    description: Any
    display_name: Any
    index: Any
    name: Any
    ports: Any

class Stream(Any):
    __doc__: str
    _is_active: Any
    card_index: Any
    description: Any
    display_name: Any
    index: Any
    is_active: Any
    name: Any
    ports: Any
    def __init__(self, index, name, display_name, description, ports, card_index) -> None: ...
    def activate_port_by_name(self, name) -> None: ...
    def get_display_name(self) -> Any: ...
    def get_is_active(self) -> bool: ...
    def set_is_active(self, value) -> None: ...
