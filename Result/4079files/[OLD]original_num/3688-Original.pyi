# (generated with --quick)

import multiprocessing.context
import multiprocessing.queues
import multiprocessing.synchronize
from typing import Any, Optional

ctypes: module
io: module
logger: logging.Logger
logging: module
mitmproxy: Any
mitmproxy_extensions: Any
multiprocessing: module
seproxer: Any
seproxer_enums: Any
signal: module
t: module
time: module

class ProxyError(Exception):
    __doc__: str

class ProxyMalformedData(ProxyError):
    __doc__: str

class ProxyNotRunningError(ProxyError):
    __doc__: str

class ProxyProc(multiprocessing.context.Process):
    proxy_master: Any
    def __init__(self, proxy_master) -> None: ...
    def _handle_sig(self, signum, frame) -> None: ...

class ProxyRunningError(ProxyError):
    __doc__: str

class Runner:
    _has_active_flows_state: multiprocessing.Value
    _producer_push_event: multiprocessing.synchronize.Event
    _proxy_proc: Optional[ProxyProc]
    _proxy_server: Any
    _results_queue: multiprocessing.queues.Queue[nothing]
    is_running: bool
    mitmproxy_options: Any
    def __init__(self, mitmproxy_options) -> None: ...
    def clear_flows(self) -> None: ...
    def done(self) -> None: ...
    @staticmethod
    def from_options(options) -> Runner: ...
    def get_results(self) -> bytes: ...
    def has_pending_requests(self) -> bool: ...
    def run(self) -> None: ...
