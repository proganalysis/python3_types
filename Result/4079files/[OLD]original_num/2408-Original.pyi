# (generated with --quick)

from typing import Any, Coroutine

Event: Any
READ_CHUNK_SIZE: int
h2: Any
host: str
mimetypes: module
os: module
run: Any
socket: Any
spawn: Any
ssl: Any
sys: module

class H2Server:
    __doc__: str
    conn: Any
    flow_control_events: dict
    root: Any
    sock: Any
    def __init__(self, sock, root) -> None: ...
    def _send_file_data(self, fileobj, stream_id) -> Coroutine[Any, Any, None]: ...
    def request_received(self, headers, stream_id) -> Coroutine[Any, Any, None]: ...
    def run(self) -> Coroutine[Any, Any, None]: ...
    def send_file(self, file_path, stream_id) -> Coroutine[Any, Any, None]: ...
    def wait_for_flow_control(self, stream_id) -> Coroutine[Any, Any, None]: ...
    def window_updated(self, event) -> Coroutine[Any, Any, None]: ...

def create_listening_ssl_socket(address, certfile, keyfile) -> coroutine: ...
def h2_server(address, root, certfile, keyfile) -> coroutine: ...
