# (generated with --quick)

from typing import Dict, Sequence, Tuple

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
    login: str
    password: str
    product: str
    version: str
    def __init__(self, product: str, version: str, login: str, password: str) -> None: ...
    def admin_variables(self) -> Dict[str, str]: ...
    def launch(self, timeout: int = ..., check_conn: bool = ..., headless: bool = ..., nohup: bool = ...) -> None: ...

def _is_iqfeed_running(iqfeed_host: str = ..., iqfeed_ports: Sequence = ...) -> bool: ...
