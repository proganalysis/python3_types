# (generated with --quick)

from typing import Any

ack: AckFrame
blocked: BlockedFrame
conn_close: ConnectionCloseFrame
f: StreamFrame
goaway: GoAwayFrame
io: module
max_data: MaxDataFrame
max_stream_id: MaxStreamIDFrame
new_conn_id: NewConnectionIDFrame
rst_stream: ResetStreamFrame
stream_blocked: StreamBlockedFrame
sys: module

class AckFrame(Frame):
    __doc__: str
    def __init__(self, largest_acknowledged, ack_delay, ack_blocks, timestapms) -> None: ...
    @classmethod
    def from_bytes(cls, buffer) -> Any: ...
    def to_bytes(self) -> Any: ...

class BlockedFrame(Frame):
    TYPE_BYTE: bytes
    __doc__: str
    stream_id: Any
    def __init__(self, stream_id) -> None: ...
    @classmethod
    def from_bytes(cls, buffer) -> Any: ...
    def to_bytes(self) -> bytes: ...

class ConnectionCloseFrame(RegularFrame):
    TYPE_BYTE: bytes
    __doc__: str
    def __init__(self, error, reason) -> None: ...
    @classmethod
    def from_bytes(cls, buffer) -> Any: ...

class Frame:
    __doc__: str
    def __eq__(self, other) -> bool: ...
    def __init__(self, locals_) -> None: ...
    @classmethod
    def from_bytes(cls, buffer) -> Any: ...

class GoAwayFrame(RegularFrame):
    TYPE_BYTE: bytes
    __doc__: str
    def __init__(self, largest_client_stream_id, largest_server_stream_id) -> None: ...
    @classmethod
    def from_bytes(cls, buffer) -> Any: ...

class LongHeaderPacket(QUICPacket):
    __doc__: str

class MaxDataFrame(Frame):
    TYPE_BYTE: bytes
    def __init__(self, max_data) -> None: ...
    @classmethod
    def from_bytes(cls, buffer) -> Any: ...
    def to_bytes(self) -> bytes: ...

class MaxStreamDataFrame(Frame):
    TYPE_BYTE: bytes
    __doc__: str
    offset: Any
    stream_id: Any
    def __init__(self, stream_id, offset) -> None: ...
    @classmethod
    def from_bytes(cls, buffer) -> Any: ...
    def to_bytes(self) -> bytes: ...

class MaxStreamIDFrame(Frame):
    TYPE_BYTE: bytes
    __doc__: str
    def __init__(self, max_stream_id) -> None: ...
    @classmethod
    def from_bytes(cls, buffer) -> Any: ...
    def to_bytes(self) -> bytes: ...

class NewConnectionIDFrame(Frame):
    TYPE_BYTE: bytes
    __doc__: str
    def __init__(self, sequence, connection_id) -> None: ...
    @classmethod
    def from_bytes(cls, buffer) -> Any: ...
    def to_bytes(self) -> bytes: ...

class PaddingFrame(RegularFrame):
    TYPE_BYTE: bytes
    __doc__: str

class PingFrame(RegularFrame):
    TYPE_BYTE: bytes
    __doc__: str

class QUICPacket:
    __doc__: str
    @classmethod
    def from_bytes(cls, buffer) -> Any: ...
    def to_bytes(self) -> None: ...

class RegularFrame(Frame):
    TYPE_BYTE: bytes
    __doc__: str
    @classmethod
    def from_byte(cls, buffer) -> Any: ...
    def to_bytes(self) -> bytes: ...

class ResetStreamFrame(RegularFrame):
    TYPE_BYTE: bytes
    __doc__: str
    def __init__(self, stream_id, offset, error) -> None: ...
    @classmethod
    def from_bytes(cls, buffer) -> Any: ...

class ShortHeaderPacket(QUICPacket):
    __doc__: str

class StreamBlockedFrame(Frame):
    TYPE_BYTE: bytes
    __doc__: str
    def __init__(self, stream_id) -> None: ...
    @classmethod
    def from_bytes(cls, buffer) -> Any: ...
    def to_bytes(self) -> bytes: ...

class StreamFrame(Frame):
    fin: Any
    offset: Any
    payload: Any
    stream_id: Any
    def __init__(self, stream_id, offset, fin, payload) -> None: ...
    def _get_offset_length(self) -> Any: ...
    def _get_sream_id_length(self) -> Any: ...
    @classmethod
    def from_bytes(cls, buffer) -> Any: ...
    def to_bytes(self) -> Any: ...

class StreamIDNeededFrame(RegularFrame):
    TYPE_BYTE: bytes
    __doc__: str

def read_int(size, buffer) -> int: ...
def read_ufloat16(buffer) -> Any: ...
def write_int(size, i) -> Any: ...
def write_ufloat16(value) -> Any: ...
