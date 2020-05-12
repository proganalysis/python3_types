# (generated with --quick)

from typing import Any, Dict

InvalidMessage: Any
InvalidPartialUpdate: Any
LinkAttributes: Any
Path: Any
copy: module

class BaseMessage(object):
    __doc__: str
    addr_v4: Any
    addr_v6: Any
    id: Any
    networks: Any
    node_data: Any
    reflect: Dict[nothing, nothing]
    reflected: Any
    routing_data: Any
    seq: Any
    def apply_base_data(self, msg) -> None: ...

class Message(BaseMessage):
    __doc__: str
    _base: BaseMessage
    addr_v4: Any
    addr_v6: Any
    id: None
    interface: dict
    networks: Any
    node_data: Any
    reflect: Any
    reflected: Any
    router_id: str
    routing_data: Any
    rx_time: Any
    seq: Any
    def __init__(self, msg: dict, interface: dict, router_id: str, rx_time) -> None: ...
    def _apply_full(self, msg: dict) -> bool: ...
    def _apply_partial(self, msg: dict) -> bool: ...
    def _get_path(self, path: str, link_attributes) -> Any: ...
    def _save_networks(self, msg: dict) -> bool: ...
    def _validate_msg(self, msg: dict) -> None: ...
    def apply_new_msg(self, msg: dict, rx_time) -> bool: ...
