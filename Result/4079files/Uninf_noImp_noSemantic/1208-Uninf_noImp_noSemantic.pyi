from typing import Any
from watchdog.events import FileSystemEventHandler

config: Any
LOG: Any
verbosity: Any
BACK_CITIES_IN_BBOX_URL: Any
BACK_INITDB_URL: Any
BACK_TASKS_URL: Any

class Watcher:
    DIRECTORY_TO_WATCH: str = ...
    observer: Any = ...
    def __init__(self) -> None: ...
    def run(self) -> None: ...

class Handler(FileSystemEventHandler):
    @staticmethod
    def on_any_event(event: Any): ...
    @staticmethod
    def parse_entries(file_path: Any) -> None: ...
