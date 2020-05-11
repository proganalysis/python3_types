# (generated with --quick)

from typing import Any, Dict

BACK_CITIES_IN_BBOX_URL: str
BACK_INITDB_URL: str
BACK_TASKS_URL: str
FileSystemEventHandler: Any
LOG: logging.Logger
Observer: Any
config: configparser.ConfigParser
configparser: module
logging: module
os: module
requests: module
time: module
verbosity: Dict[str, int]
w: Watcher

class Handler(Any):
    @staticmethod
    def on_any_event(event) -> None: ...
    @staticmethod
    def parse_entries(file_path) -> None: ...

class Watcher:
    DIRECTORY_TO_WATCH: str
    observer: Any
    def __init__(self) -> None: ...
    def run(self) -> None: ...
