# (generated with --quick)

from typing import Any

DispatcherManager: Any
StatusMonitor: Any
json: module
logging: module
os: module

class SchoolTracker(object):
    DispatcherManager: Any
    StatusMonitor: Any
    logger: logging.Logger
    def __init__(self, log_level) -> None: ...
    def start(self) -> None: ...
