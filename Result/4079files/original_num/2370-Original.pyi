# (generated with --quick)

from typing import Any, List, TextIO

DEFAULT_MAX_MESSAGE_SIZE: int
argv: List[str]
argvs: int
batchsize: int
clear: str
count: int
end: float
host: str
i: int
jafka: module
messages: List[bytearray]
messagesize: int
out: TextIO
package_size: int
port: int
producer: jafka.Producer
send_bytes: int
start: float
sys: module
time: module
topic: str

def check_message_size(messagesize, batchsize, topic) -> Any: ...
def packagesize(messagesize, batchsize, topic) -> Any: ...
