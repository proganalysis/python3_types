# (generated with --quick)

from typing import Any, Optional

basethread: Any
command: Any
connections: Any
controller: Any
ctx: Any
exceptions: Any
flow: Any
http: Any
http1: Any
human: Any
io: Any
log: Any
mitmproxy: Any
options: Any
queue: module
server_spec: Any
threading: module
tls: Any
typing: module

class ClientPlayback:
    count: Any
    load_file: Any
    q: queue.Queue[nothing]
    start_replay: Any
    stop_replay: Any
    thread: Optional[RequestReplayThread]
    def __init__(self) -> None: ...
    def check(self, f) -> Optional[str]: ...
    def configure(self, updated) -> None: ...
    def load(self, loader) -> None: ...
    def running(self) -> None: ...

class RequestReplayThread(Any):
    channel: Any
    daemon: bool
    inflight: threading.Event
    options: Any
    queue: Any
    def __init__(self, opts, channel, queue) -> None: ...
    def replay(self, f) -> None: ...
    def run(self) -> Any: ...
