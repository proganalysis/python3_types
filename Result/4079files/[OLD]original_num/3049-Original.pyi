# (generated with --quick)

from typing import Any, Dict, Optional, Sequence

CompanyId: Any
datetime: module
uuid_to_string: Any

class Device(object):
    active: bool
    address: Any
    appearance: Any
    connected: Any
    device_class: Any
    first_seen: datetime.datetime
    last_seen: datetime.datetime
    manufacturer_data: Dict[Any, list]
    name: Any
    paired: Any
    path: str
    rssis: list
    service_data: Dict[Any, list]
    services: Dict[str, GATTService]
    services_resolved: Any
    tx_power: Any
    uuids: Any
    def __getitem__(self, path: str) -> GATTService: ...
    def __init__(self, path: str, address: str, paired: bool, connected: bool, services_resolved: bool, name: Optional[str] = ..., device_class: Optional[int] = ..., appearance: Optional[int] = ..., uuids: Optional[Sequence[str]] = ..., rssi: Optional[int] = ..., tx_power: Optional[int] = ..., manufacturer_data: Optional[Dict[int, Sequence[int]]] = ..., service_data: Optional[Dict[str, Sequence[int]]] = ...) -> None: ...
    def __setitem__(self, path: str, service: GATTService) -> None: ...
    @classmethod
    def create_from_dbus_dict(cls, path: str, data: Dict[str, Any]) -> Device: ...
    def update_from_dbus_dict(self, path: str, data: Dict[str, Any]) -> None: ...
    def update_from_device(self, device: Device) -> None: ...

class GATTCharacteristic(object):
    descriptors: Dict[str, GATTDescriptor]
    flags: Sequence[str]
    uuid: str
    value: Any
    def __getitem__(self, path: str) -> GATTDescriptor: ...
    def __init__(self, uuid: str, value: Optional[Sequence[int]], flags: Sequence[str]) -> None: ...
    def __setitem__(self, path: str, descriptor: GATTDescriptor) -> None: ...

class GATTDescriptor(object):
    flags: Any
    uuid: str
    value: Any
    def __init__(self, uuid: str, value: Optional[Sequence[int]], flags: Optional[Sequence[str]]) -> None: ...

class GATTService(object):
    characteristics: Dict[str, GATTCharacteristic]
    primary: bool
    uuid: str
    def __getitem__(self, path: str) -> GATTCharacteristic: ...
    def __init__(self, uuid: str, primary: bool) -> None: ...
    def __setitem__(self, path: str, characteristic: GATTCharacteristic) -> None: ...

def print_device(device, prefix = ...) -> None: ...
