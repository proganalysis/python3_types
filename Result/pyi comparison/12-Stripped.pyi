# (generated with --quick)

from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple, TypeVar

BAD_MAC: List[str]
CTRL_ACK: Tuple[int, int]
CTRL_CFECFA: Tuple[int, int]
CTRL_CFEND: Tuple[int, int]
CTRL_CTS: Tuple[int, int]
CTRL_POLL: Tuple[int, int]
CTRL_RTS: Tuple[int, int]
DATA_ANY: Tuple[int, Tuple[int, int, int, int, int, int, int, int, int, int, int, int]]
FIVEHERTZ: List[int]
MACFILTER: str
MGMT_ASSOC_REQ: Tuple[int, int]
MGMT_ASSOC_RESP: Tuple[int, int]
MGMT_ATIM: Tuple[int, int]
MGMT_AUTH: Tuple[int, int]
MGMT_BEACON: Tuple[int, int]
MGMT_DEAUTH: Tuple[int, int]
MGMT_DISASSOC: Tuple[int, int]
MGMT_PROBE_REQ: Tuple[int, int]
MGMT_PROBE_RESP: Tuple[int, int]
MGMT_REASSOC_REQ: Tuple[int, int]
MGMT_REASSOC_RESP: Tuple[int, int]
WPA_key: Any
logging: module
nl: Any
os: module
pyric: Any
pyw: Any
sys: module
time: module

_T = TypeVar('_T')

class BoopSniff:
    filter: Optional[str]
    handler_map: Dict[int, dict]
    hopper: Any
    interface: Any
    logger: logging.Logger
    pthread: Any
    def __init__(self, interface, hopper = ..., target = ...) -> None: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    def channel(self) -> Any: ...
    def handler(self, ptype) -> Callable[[Any], Any]: ...
    def pkt_router(self, pkt) -> Any: ...
    def printer(self) -> Callable[[Any], Any]: ...
    def run(self, f = ..., timeout = ...) -> None: ...

class Hopper:
    channels: list
    interface: Any
    logger: logging.Logger
    def __call__(self) -> None: ...
    def __init__(self, interface, frequencies = ..., channels = ...) -> None: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    def channel(self, chan = ...) -> Any: ...
    def run(self) -> Any: ...

def __getattr__(name) -> Any: ...
def choice(seq: Sequence[_T]) -> _T: ...
def gchan(card) -> Any: ...
def root() -> bool: ...
def wraps(wrapped: Callable, assigned: Sequence[str] = ..., updated: Sequence[str] = ...) -> Callable[[Callable], Callable]: ...
