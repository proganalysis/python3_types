# (generated with --quick)

from typing import Any, Callable, List, Optional

__package__: None
io: module
os: module
pkgutil: module
subprocess: module
sys: module
tempfile: module
time: module

class WiFiAp:
    _auth: str
    _bssid: str
    _encrypt: str
    _raw_data: str
    _ssid: str
    _strength: int
    auth: str
    bssid: str
    encrypt: str
    raw_data: str
    ssid: str
    strength: int
    def __init__(self, ssid: str = ..., auth: str = ..., encrypt: str = ..., bssid: str = ..., strength: int = ..., raw_data: str = ...) -> None: ...
    @classmethod
    def parse_netsh(cls, raw_data: str) -> WiFiAp: ...

class WiFiConstant:
    STATE_CONNECTED: str
    STATE_DISCONNECTED: str

class WiFiInterface:
    _bssid: Any
    _name: str
    _ssid: Any
    _state: str
    bssid: Optional[str]
    name: str
    ssid: Optional[str]
    state: str
    def __init__(self, name: str = ..., state: str = ..., ssid: Optional[str] = ..., bssid: Optional[str] = ...) -> None: ...
    @classmethod
    def parse_netsh(cls, raw_data: str) -> WiFiInterface: ...

class WinWiFi:
    @classmethod
    def add_profile(cls, profile: str) -> None: ...
    @classmethod
    def connect(cls, ssid: str, passwd: str = ..., remember: bool = ...) -> None: ...
    @classmethod
    def disable_interface(cls, interface: str) -> None: ...
    @classmethod
    def disconnect(cls) -> None: ...
    @classmethod
    def enable_interface(cls, interface: str) -> None: ...
    @classmethod
    def forget(cls, *ssids: str) -> None: ...
    @classmethod
    def gen_profile(cls, ssid: str = ..., auth: str = ..., encrypt: str = ..., passwd: str = ..., remember: bool = ...) -> str: ...
    @classmethod
    def get_connected_interfaces(cls) -> List[WiFiInterface]: ...
    @classmethod
    def get_interfaces(cls) -> List[WiFiInterface]: ...
    @classmethod
    def get_profile_template(cls) -> str: ...
    @classmethod
    def get_profiles(cls, callback: Callable = ...) -> List[str]: ...
    @classmethod
    def netsh(cls, args: List[str], timeout: int = ..., check: bool = ...) -> subprocess.CompletedProcess: ...
    @classmethod
    def scan(cls, refresh: bool = ..., callback: Callable = ...) -> List[WiFiAp]: ...
