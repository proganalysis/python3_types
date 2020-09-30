# (generated with --quick)

from typing import Any

ASSET_NAME: str
PLUGIN_NAME: str
SOUTH_PLUGIN: str
SVC_NAME: str
__author__: str
__copyright__: str
__license__: str
__version__: str
http: module
json: module
pytest: Any
socket: module
time: module
utils: Any

class TestE2EModbusCPI:
    start_south_north: Any
    def _verify_egress(self, read_data_from_pi, pi_host, pi_admin, pi_passwd, pi_db, wait_time, retries) -> None: ...
    def _verify_ingest(self, conn) -> None: ...
    def check_connect(self, modbus_host, modbus_port) -> None: ...
    def get_ping_status(self, foglamp_url) -> Any: ...
    def get_statistics_map(self, foglamp_url) -> Any: ...
    def test_end_to_end(self, start_south_north, enable_schedule, disable_schedule, foglamp_url, read_data_from_pi, pi_host, pi_admin, pi_passwd, pi_db, wait_time, retries, skip_verify_north_interface, modbus_host, modbus_port) -> None: ...
