from typing import Any

servername: str
username: str
password: str
dbname: str
outputpins: Any
relaynum: Any
relaycount: Any
numdtpairs: int

def read_override_data(): ...
def get_relay_timer_data(tablename: Any, row: Any): ...
def timercheck(timer_data: Any, relay: Any): ...

override: Any
relay = j
relayon: str
dtpair: int
timer_data: Any
