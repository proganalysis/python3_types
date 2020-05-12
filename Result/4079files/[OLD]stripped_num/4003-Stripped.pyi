# (generated with --quick)

from typing import Any, List

__package__: None
io: module
os: module
pkgutil: module
subprocess: module
sys: module
tempfile: module
time: module

class WiFiAp:
    _auth: Any
    _bssid: Any
    _encrypt: Any
    _raw_data: Any
    _ssid: Any
    _strength: Any
    auth: Any
    bssid: Any
    encrypt: Any
    raw_data: Any
    ssid: Any
    strength: Any
    def __init__(self, ssid = ..., auth = ..., encrypt = ..., bssid = ..., strength = ..., raw_data = ...) -> None: ...
    @classmethod
    def parse_netsh(cls, raw_data) -> Any: ...

class WiFiConstant:
    STATE_CONNECTED: str
    STATE_DISCONNECTED: str

class WiFiInterface:
    _bssid: Any
    _name: Any
    _ssid: Any
    _state: Any
    bssid: Any
    name: Any
    ssid: Any
    state: Any
    def __init__(self, name = ..., state = ..., ssid = ..., bssid = ...) -> None: ...
    @classmethod
    def parse_netsh(cls, raw_data) -> Any: ...

class WinWiFi:
    @classmethod
    def add_profile(cls, profile) -> None: ...
    @classmethod
    def connect(cls, ssid, passwd = ..., remember = ...) -> None: ...
    @classmethod
    def disable_interface(cls, interface) -> None: ...
    @classmethod
    def disconnect(cls) -> None: ...
    @classmethod
    def enable_interface(cls, interface) -> None: ...
    @classmethod
    def forget(cls, *ssids) -> None: ...
    @classmethod
    def gen_profile(cls, ssid = ..., auth = ..., encrypt = ..., passwd = ..., remember = ...) -> Any: ...
    @classmethod
    def get_connected_interfaces(cls) -> list: ...
    @classmethod
    def get_interfaces(cls) -> List[nothing]: ...
    @classmethod
    def get_profile_template(cls) -> str: ...
    @classmethod
    def get_profiles(cls, callback = ...) -> list: ...
    @classmethod
    def netsh(cls, args, timeout = ..., check = ...) -> subprocess.CompletedProcess: ...
    @classmethod
    def scan(cls, refresh = ..., callback = ...) -> List[nothing]: ...
