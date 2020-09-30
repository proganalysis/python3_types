# (generated with --quick)

from typing import Any, Dict, List, Union

CPUS: int
HEARTBEAT_PATH: str
MY_IP_ADDRESS: str
SERVICES: List[Dict[str, Union[int, str]]]
ZOOKEEPER_CONNECT_STRING: str
json: module
kazoo: Any
multiprocessing: module
os: module
pytest: Any
setup: Any
socket: module
subprocess: module
time: module

def _check_zk_for_services(zk, expected_services, all_services = ...) -> None: ...
def test_clean_nerve(setup) -> None: ...
def test_nerve_restarted_if_stale_heartbeat(setup) -> None: ...
def test_nerve_service_config(setup) -> None: ...
def test_nerve_services(setup) -> None: ...
def test_sighup_handling(setup) -> None: ...
def test_updown_up_when_hadown_all(setup) -> None: ...
def test_v2_nerve_service_config(setup) -> None: ...
