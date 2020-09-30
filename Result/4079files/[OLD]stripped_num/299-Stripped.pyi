# (generated with --quick)

from typing import Any, List

GPIO: Any
datetime: module
dbname: str
dtpair: Any
i: Any
j: Any
mariadb: Any
numdtpairs: int
outputpins: List[int]
override: Any
password: str
relay: Any
relaycount: range
relaynum: List[nothing]
relayon: Any
servername: str
timer_data: Any
username: str
z: Any

def get_relay_timer_data(tablename, row) -> Any: ...
def read_override_data() -> Any: ...
def sleep(secs: float) -> None: ...
def timercheck(timer_data, relay) -> str: ...
