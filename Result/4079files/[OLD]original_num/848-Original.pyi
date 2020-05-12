# (generated with --quick)

from typing import Any

BaseCommand: Any
CommandError: Any
logger: logging.Logger
logging: module
setup_tracing: Any

class Command(Any):
    help: str
    def add_arguments(self, parser) -> None: ...
    def handle(self, *args, **options) -> None: ...

def __getattr__(name) -> Any: ...
