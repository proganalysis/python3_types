# (generated with --quick)

from typing import Any, Dict, List, Union

InternalException: Any

class LinkAttributes(dict):
    __doc__: str
    current_id: int
    def __init__(self, attributes = ...) -> None: ...
    def get_next_id(self) -> str: ...

class Path(object):
    __slots__ = ["_global_attributes", "attributes", "links", "next_hop", "next_hop_interface", "nodes", "policy_cache"]
    __doc__: str
    _global_attributes: Union[LinkAttributes, Dict[nothing, nothing]]
    attributes: LinkAttributes
    links: List[str]
    next_hop: str
    next_hop_interface: str
    nodes: List[str]
    policy_cache: Dict[nothing, nothing]
    def __init__(self, path: str, attributes: LinkAttributes, next_hop: str, next_hop_interface: str) -> None: ...
    def append(self, node: str, new_next_hop_interface: str, attributes: dict) -> None: ...
    def apply_attributes(self, attributes: LinkAttributes) -> None: ...

def dict_reverse_lookup(d: dict, value) -> Any: ...
