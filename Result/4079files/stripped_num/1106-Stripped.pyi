# (generated with --quick)

from typing import Any, Tuple

GObject: Any
lib_pulseaudio: Any

class Card(Any):
    __doc__: str
    description: Any
    display_name: Any
    driver: Any
    index: Any
    name: Any
    ports: Any
    profiles: Any
    proplist: Any
    def __init__(self, index, name, display_name, driver, profiles, ports, proplist) -> None: ...
    @staticmethod
    def find_stream_port(card_port, sources, sinks) -> Tuple[Any, Any]: ...
    def get_descriptive_name(self) -> Any: ...
    def get_display_name(self) -> Any: ...
    def get_property_str(self, name) -> Any: ...
    def update_port_activity(self, sources, sinks) -> None: ...

class CardProfile(Any):
    __doc__: str
    description: Any
    is_active: Any
    name: Any
    num_sinks: Any
    num_sources: Any
    priority: Any
    def __init__(self, name, description, num_sinks, num_sources, priority, is_active) -> None: ...
