# (generated with --quick)

from typing import Any, Type

DbusProxy: Any
GObject: Any
Gconnect: Any
GdkPixbuf: Any
Notify: Any
gi: module
os: module
sys: module

class PingPlugin(Any, Any):
    CLASS_PROXY: Type[PingProxy]
    __gtype_name__: str
    device: Any
    proxy: Any
    worker: PingProxy
    def __init__(self, *args, **kwargs) -> None: ...
    def do_activate(self, name: str) -> None: ...
    def do_deactivate(self) -> None: ...
    def formatted_receive(self, body) -> None: ...

class PingProxy(Any):
    PACKET_TYPE_REQUEST: str
    def __init__(self, proxy) -> None: ...
    def formatted_receive(self, body) -> None: ...
    def introspection_xml(self) -> str: ...
    def m_dbus_sendMessage(self, parameters, invocation, *user_data) -> None: ...
    def m_dbus_sendPing(self, parameters, invocation, *user_data) -> None: ...
