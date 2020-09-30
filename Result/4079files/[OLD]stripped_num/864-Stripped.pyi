# (generated with --quick)

from typing import Any, Dict

InternalException: Any

class LinkAttributes(dict):
    __doc__: str
    current_id: int
    def __init__(self, attributes = ...) -> None: ...
    def get_next_id(self) -> str: ...

class Path(object):
    __slots__ = ["_global_attributes", "attributes", "links", "next_hop", "next_hop_interface", "nodes", "policy_cache"]
    __doc__: str
    _global_attributes: Any
    attributes: Any
    links: list
    next_hop: Any
    next_hop_interface: Any
    nodes: list
    policy_cache: Dict[nothing, nothing]
    def __init__(self, path, attributes, next_hop, next_hop_interface) -> None: ...
    def __str__(self) -> Any: ...
    def append(self, node, new_next_hop_interface, attributes) -> None: ...
    def apply_attributes(self, attributes) -> None: ...

def dict_reverse_lookup(d, value) -> Any: ...
