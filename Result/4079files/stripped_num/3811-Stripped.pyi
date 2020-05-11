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

class BatteryPlugin(Any, Any):
    CLASS_PROXY: Type[BatteryProxy]
    __gtype_name__: str
    device: Any
    proxy: Any
    worker: BatteryProxy
    def __init__(self, *args, **kwargs) -> None: ...
    def do_activate(self, name) -> None: ...
    def do_deactivate(self) -> None: ...
    def formatted_receive(self, body) -> None: ...

class BatteryProxy(Any):
    PACKET_TYPE_REQUEST: str
    charge: Any
    is_charging: Any
    def __init__(self, proxy) -> None: ...
    def formatted_receive(self, body) -> None: ...
    def introspection_xml(self) -> str: ...
    def m_dbus_charge(self, parameters, invocation, *user_data) -> None: ...
    def m_dbus_isCharging(self, parameters, invocation, *user_data) -> None: ...
    def m_dbus_request(self, parameters, invocation, *user_data) -> None: ...
