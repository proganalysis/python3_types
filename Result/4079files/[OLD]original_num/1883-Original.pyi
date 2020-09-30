# (generated with --quick)

from typing import Any, List, Type
import ws4py.client

Greenlet: Any
Queue: Any
WebSocketBaseClient: Type[ws4py.client.WebSocketBaseClient]
__all__: List[str]
copy: module
gevent: Any

class WebSocketClient(ws4py.client.WebSocketBaseClient):
    _th: Any
    messages: Any
    def closed(self, code, reason = ...) -> None: ...
    def receive(self, block = ...) -> Any: ...
    def received_message(self, message) -> None: ...
