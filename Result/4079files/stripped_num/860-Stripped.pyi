# (generated with --quick)

from typing import Any, Optional

NMCLI_DELIMITER: str
NMCLI_DEVICE: None
NMCLI_LINETERMINATOR: str
logger: logging.Logger
logging: module
os: module
pyre: Any
subprocess: module
time: module

def _network_device() -> Optional[str]: ...
def _network_device_enable(device, enable) -> None: ...
def _network_device_is_enabled(device) -> bool: ...
def test_network_disconnect(group = ...) -> None: ...
