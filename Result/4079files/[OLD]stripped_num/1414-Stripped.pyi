# (generated with --quick)

import asyncio.events
import asyncio.locks
import asyncio.protocols
import datetime
import functools
from typing import Any, Callable, NoReturn, Optional, TextIO, Type

TIMEOUT: datetime.timedelta
asyncio: module
concurrent: module
create_serial_connection: Any
decode_packet: Any
deserialize_packet_id: Any
encode_packet: Any
log: logging.Logger
logging: module
packet_events: Any
partial: Type[functools.partial]
rflink_log: Optional[TextIO]
timedelta: Type[datetime.timedelta]
valid_packet: Any

class CommandSerialization(ProtocolBase):
    __doc__: str
    _command_ack: asyncio.locks.Event
    _ready_to_send: asyncio.locks.Lock
    buffer: str
    disconnect_callback: None
    loop: asyncio.events.AbstractEventLoop
    packet: str
    packet_callback: Any
    def __init__(self, *args, packet_callback = ..., **kwargs) -> None: ...
    def send_command_ack(self, device_id, action) -> coroutine: ...

class EventHandling(PacketHandling):
    __doc__: str
    buffer: str
    disconnect_callback: None
    ignore: Any
    loop: asyncio.events.AbstractEventLoop
    packet: str
    packet_callback: Callable[[Any], Any]
    def __init__(self, *args, event_callback = ..., ignore = ..., **kwargs) -> None: ...
    def _handle_packet(self, packet) -> None: ...
    def event_callback(self, _1) -> Any: ...
    def handle_event(self, event) -> None: ...
    def ignore_event(self, event_id) -> bool: ...

class InverterProtocol(RflinkProtocol):
    __doc__: str
    _command_ack: asyncio.locks.Event
    _ready_to_send: asyncio.locks.Lock
    buffer: str
    disconnect_callback: None
    loop: asyncio.events.AbstractEventLoop
    packet: str
    packet_callback: Any

class PacketHandling(ProtocolBase):
    __doc__: str
    _last_ack: Any
    buffer: str
    disconnect_callback: None
    loop: asyncio.events.AbstractEventLoop
    packet: str
    def __init__(self, *args, packet_callback = ..., **kwargs) -> None: ...
    def handle_packet(self, packet) -> None: ...
    def handle_raw_packet(self, raw_packet) -> None: ...
    def packet_callback(self, _1) -> Any: ...
    def send_command(self, device_id, action) -> None: ...
    def send_packet(self, fields) -> None: ...

class ProtocolBase(asyncio.protocols.Protocol):
    __doc__: str
    buffer: str
    loop: Any
    packet: str
    transport: Any
    def __init__(self, loop = ..., disconnect_callback = ...) -> None: ...
    def connection_lost(self, exc) -> None: ...
    def connection_made(self, transport) -> None: ...
    def data_received(self, data) -> None: ...
    def disconnect_callback(self, _1) -> Any: ...
    def handle_lines(self) -> None: ...
    def handle_raw_packet(self, raw_packet) -> NoReturn: ...
    def log_all(self, file) -> None: ...
    def send_raw_packet(self, packet) -> None: ...

class RepeaterProtocol(RflinkProtocol):
    __doc__: str
    _command_ack: asyncio.locks.Event
    _ready_to_send: asyncio.locks.Lock
    buffer: str
    disconnect_callback: None
    loop: asyncio.events.AbstractEventLoop
    packet: str
    packet_callback: Any
    def handle_event(self, packet) -> None: ...

class RflinkProtocol(CommandSerialization, EventHandling):
    __doc__: str
    _command_ack: asyncio.locks.Event
    _ready_to_send: asyncio.locks.Lock
    buffer: str
    disconnect_callback: None
    loop: asyncio.events.AbstractEventLoop
    packet: str
    packet_callback: Any

def create_rflink_connection(port = ..., host = ..., baud = ..., protocol = ..., packet_callback = ..., event_callback = ..., disconnect_callback = ..., ignore = ..., loop = ...) -> Any: ...
