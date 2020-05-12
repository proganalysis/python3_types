# (generated with --quick)

import decimal
from typing import Any, Dict, NoReturn, Optional, Type, TypeVar, Union

Decimal: Type[decimal.Decimal]
_zmq: Any
logging: module
loglevels: Dict[str, int]
msgpack: Any
ports: Dict[str, Dict[str, str]]
time: module
traceback: module
zmq: Any

_T0 = TypeVar('_T0')

class AlgoObject(object):
    _context: Any
    _control_socket: Any
    _data_socket: Any
    _logger: logging.Logger
    _name: str
    _poller: Any
    timeout: None
    def __init__(self, name: str, socket_type) -> None: ...
    def debug(self, s) -> None: ...
    def error(self, s) -> None: ...
    def info(self, s) -> None: ...
    def process_control(self, data) -> Optional[bool]: ...
    def process_data(self, data) -> NoReturn: ...
    def recv_control(self) -> Any: ...
    def recv_data(self) -> Any: ...
    def run(self) -> None: ...
    def run_once(self) -> None: ...
    def set_logger_level(self, level) -> None: ...
    def socket(self, socket_type) -> Any: ...
    def warning(self, s) -> None: ...

class Broker(AlgoObject):
    _context: Any
    _control_socket: Any
    _data_socket: Any
    _logger: Any
    _name: str
    _poller: Any
    timeout: None
    def __init__(self, name, **kwargs) -> None: ...

class Strategy(AlgoObject):
    _action_socket: Any
    _context: Any
    _control_socket: Any
    _data_socket: Any
    _logger: Any
    _name: str
    _poller: Any
    timeout: None
    def __init__(self, name, tickers, **kwargs) -> None: ...
    def send_action(self, message) -> None: ...
    def send_control(self, to, message) -> None: ...

class Ticker(AlgoObject):
    _context: Any
    _control_socket: Any
    _data_socket: Any
    _logger: Any
    _name: str
    _poller: Any
    timeout: int
    def __init__(self, name, **kwargs) -> None: ...
    def get_quotes(self) -> None: ...
    def send_quotes(self, quotes) -> None: ...
    def test(self) -> None: ...

def decode_decimal(obj: _T0) -> Union[decimal.Decimal, _T0]: ...
def encode_decimal(obj: _T0) -> Union[Dict[str, Union[bool, str]], _T0]: ...
def logger(s: str) -> logging.Logger: ...
def pack(i) -> Any: ...
def send(data) -> None: ...
def set_zmq(zmq) -> None: ...
def unpack(i) -> Any: ...
