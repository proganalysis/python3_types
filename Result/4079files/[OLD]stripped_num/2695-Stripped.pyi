# (generated with --quick)

from typing import Any

BaseCommand: Any
tools: Any

class Command(Any):
    help: str
    def add_arguments(self, parser) -> None: ...
    def handle(self, *args, **options) -> None: ...
