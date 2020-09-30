# (generated with --quick)

from typing import Any

BaseCommand: Any
CommandError: Any
CommandParser: Any
json: module
pprint: module
publish_message: Any

class Command(Any):
    help: str
    def add_arguments(self, parser) -> None: ...
    def handle(self, *args, **options) -> None: ...
