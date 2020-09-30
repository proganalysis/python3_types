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
    interface: Any
    networks: Any
    node_data: Any
    reflect: Any
    reflected: Any
    router_id: Any
    routing_data: Any
    rx_time: Any
    seq: Any
    def __init__(self, msg, interface, router_id, rx_time) -> None: ...
    def _apply_full(self, msg) -> bool: ...
    def _apply_partial(self, msg) -> bool: ...
    def _get_path(self, path, link_attributes) -> Any: ...
    def _save_networks(self, msg) -> bool: ...
    def _validate_msg(self, msg) -> None: ...
    def apply_new_msg(self, msg, rx_time) -> Any: ...
