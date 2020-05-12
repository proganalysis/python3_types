# (generated with --quick)

import logging
import squeezealexa.settings
import squeezealexa.transport.mqtt
from typing import Any, IO, Iterable, Optional, Type, TypeVar, Union

CustomClient: Type[squeezealexa.transport.mqtt.CustomClient]
DEBUG: int
INFO: int
LMS_SETTINGS: squeezealexa.settings.LmsSettings
MQTT_SETTINGS: squeezealexa.settings.MqttSettings
client: squeezealexa.transport.mqtt.CustomClient
e: Any
logger: logging.Logger
mqtt: Any
paho: Any
path: str
socket: module
sys: module
telnet: Optional[telnetlib.Telnet]
telnetlib: module

AnyStr = TypeVar('AnyStr', str, bytes)

def abspath(path: Union[_PathLike[AnyStr], AnyStr]) -> AnyStr: ...
def basicConfig(*, filename: Optional[Union[str, _PathLike[str]]] = ..., filemode: str = ..., format: str = ..., datefmt: Optional[str] = ..., style: str = ..., level: Optional[Union[int, str]] = ..., stream: Optional[IO[str]] = ..., handlers: Optional[Iterable[logging.Handler]] = ...) -> None: ...
def connect_cli() -> telnetlib.Telnet: ...
def dirname(path: Union[_PathLike[AnyStr], AnyStr]) -> AnyStr: ...
def getLogger(name: Optional[str] = ...) -> logging.Logger: ...
def on_connect(client, data, flags, rc) -> None: ...
def on_message(client, userdata, message) -> None: ...
def on_subscribe(client, data, mid, granted_qos) -> None: ...
