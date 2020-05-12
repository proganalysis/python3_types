# (generated with --quick)

from typing import Any, Tuple

GObject: Any
lib_pulseaudio: Any

class Card(Any):
    __doc__: str
    description: str
    display_name: str
    driver: str
    index: int
    name: str
    ports: dict
    profiles: dict
    proplist: Any
    def __init__(self, index: int, name: str, display_name: str, driver: str, profiles: dict, ports: dict, proplist) -> None: ...
    @staticmethod
    def find_stream_port(card_port, sources: dict, sinks: dict) -> Tuple[Any, Any]: ...
    def get_descriptive_name(self) -> str: ...
    def get_display_name(self) -> str: ...
    def get_property_str(self, name: str) -> str: ...
    def update_port_activity(self, sources: dict, sinks: dict) -> None: ...

class CardProfile(Any):
    __doc__: str
    description: str
    is_active: bool
    name: str
    num_sinks: int
    num_sources: int
    priority: int
    def __init__(self, name: str, description: str, num_sinks: int, num_sources: int, priority: int, is_active: bool) -> None: ...
