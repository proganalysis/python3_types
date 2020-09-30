# (generated with --quick)

import array
import mmap
from typing import Any, List, Optional, Tuple, Union

FETCH_TYPE: int
MULTIFETCH_TYPE: int
MULTIPRODUCE_TYPE: int
OFFSETS_TYPE: int
PRODUCE_TYPE: int
binascii: module
count: int
end: float
host: str
i: int
line: str
port: int
producer: Producer
socket: module
start: float
sys: module
testable: bool
time: module
topic: str

class Consumer:
    connection: socket.socket
    def __init__(self, host = ..., port = ...) -> None: ...
    def close(self) -> None: ...
    def fetch(self, topic, partition, offset, maxsize = ...) -> Optional[List[Tuple[Any, Any]]]: ...
    def getoffsetsbefore(self, topic, partition = ..., time = ..., maxnumoffsets = ...) -> Union[tuple, List[nothing]]: ...

class FetchRequest:
    maxsize: Any
    offset: Any
    partition: Any
    topic: Any
    def __init__(self, topic, partition = ..., offset = ..., maxsize = ...) -> None: ...
    def tobytes(self) -> bytes: ...

class OffsetRequest:
    maxnumoffsets: Any
    partition: Any
    time: Any
    topic: Any
    def __init__(self, topic, partition = ..., time = ..., maxnumoffsets = ...) -> None: ...
    def tobytes(self) -> bytes: ...

class Producer:
    connection: socket.socket
    def __init__(self, host = ..., port = ...) -> None: ...
    def close(self) -> None: ...
    def send(self, topic, messages, partition = ...) -> None: ...

class RequestTypes:
    FETCH: int
    MULTIFETCH: int
    MULTIPRODUCE: int
    OFFSETS: int
    PRODUCE: int

def encode_message(message) -> bytes: ...
def encode_produce_request(topic, partition, messages) -> bytes: ...
def pack(fmt: Union[bytes, str], *v) -> bytes: ...
def sleep(secs: float) -> None: ...
def unpack(fmt: Union[bytes, str], buffer: Union[bytearray, bytes, memoryview, mmap.mmap, array.array[int]]) -> tuple: ...
