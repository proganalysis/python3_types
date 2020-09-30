# (generated with --quick)

from typing import Any, Dict, Tuple

log: logging.Logger
logging: module
os: module
select: module
socket: module
subprocess: module
sys: module
time: module

class FeedService:
    __doc__: str
    iqfeed_host: str
    iqfeed_ports: Tuple[int, int, int, int, int]
    login: Any
    password: Any
    product: Any
    version: Any
    def __init__(self, product, version, login, password) -> None: ...
    def admin_variables(self) -> Dict[str, Any]: ...
    def launch(self, timeout = ..., check_conn = ..., headless = ..., nohup = ...) -> None: ...

def _is_iqfeed_running(iqfeed_host = ..., iqfeed_ports = ...) -> bool: ...
