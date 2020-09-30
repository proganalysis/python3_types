# (generated with --quick)

from typing import Any

CompanyId: Any
datetime: module
uuid_to_string: Any

class Device(object):
    active: Any
    address: Any
    appearance: Any
    connected: Any
    device_class: Any
    first_seen: datetime.datetime
    last_seen: Any
    manufacturer_data: dict
    name: Any
    paired: Any
    path: Any
    rssis: list
    service_data: dict
    services: dict
    services_resolved: Any
    tx_power: Any
    uuids: set
    def __eq__(self, other) -> Any: ...
    def __getitem__(self, path) -> Any: ...
    def __init__(self, path, address, paired, connected, services_resolved, name = ..., device_class = ..., appearance = ..., uuids = ..., rssi = ..., tx_power = ..., manufacturer_data = ..., service_data = ...) -> None: ...
    def __setitem__(self, path, service) -> None: ...
    @classmethod
    def create_from_dbus_dict(cls, path, data) -> Any: ...
    def update_from_dbus_dict(self, path, data) -> None: ...
    def update_from_device(self, device) -> None: ...

class GATTCharacteristic(object):
    descriptors: dict
    flags: Any
    uuid: Any
    value: Any
    def __getitem__(self, path) -> Any: ...
    def __init__(self, uuid, value, flags) -> None: ...
    def __setitem__(self, path, descriptor) -> None: ...

class GATTDescriptor(object):
    flags: Any
    uuid: Any
    value: Any
    def __init__(self, uuid, value, flags) -> None: ...

class GATTService(object):
    characteristics: dict
    primary: Any
    uuid: Any
    def __getitem__(self, path) -> Any: ...
    def __init__(self, uuid, primary) -> None: ...
    def __setitem__(self, path, characteristic) -> None: ...

def print_device(device, prefix = ...) -> None: ...
