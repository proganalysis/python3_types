# (generated with --quick)

from typing import Any

NMCLI_DELIMITER: str
NMCLI_DEVICE: str
NMCLI_LINETERMINATOR: str
logger: logging.Logger
logging: module
os: module
pyre: Any
subprocess: module
time: module

def _network_device() -> str: ...
def _network_device_enable(device: str, enable: bool) -> None: ...
def _network_device_is_enabled(device: str) -> bool: ...
def test_network_disconnect(group = ...) -> None: ...
