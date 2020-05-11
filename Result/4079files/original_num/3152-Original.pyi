# (generated with --quick)

from typing import Any

logging: module
threading: module

class EventThread(threading.Thread):
    __doc__: str
    docker_client: Any
    terminated: bool
    def __init__(self, docker_client, on_event) -> None: ...
    def on_event(self, _1) -> Any: ...
