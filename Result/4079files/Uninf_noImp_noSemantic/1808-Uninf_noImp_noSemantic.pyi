from .info import DriveMode, ModeValue
from typing import Any

def config(param_map: Any, mastercode: Any = ...): ...
def _process_params(params: Any) -> None: ...
def post(param_map: Any, url: Any = ...): ...

_prep_post: Any
value_validators: Any

def _validator(parameter: Any): ...
def _validate_timeout(seconds: float) -> Any: ...
def _validate_app_info(info: str) -> Any: ...
def _validate_wifi_mode(mode: ModeValue) -> Any: ...
def _validate_wifi_key(network_key: str) -> Any: ...
def _validate_wifi_ssid(network_ssid: str) -> Any: ...
def _validate_passthrough_key(network_key: str) -> Any: ...
def _validate_passthroughssid(network_ssid: str) -> Any: ...
def _validate_mastercode(code: str) -> Any: ...
def _validate_bootscreen_path(path: str) -> Any: ...
def _validate_clear_mastercode(_: Any): ...
def _validate_timezone(hours_offset: int) -> Any: ...
def _validate_drive_mode(mode: DriveMode) -> Any: ...
