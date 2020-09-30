# (generated with --quick)

from typing import Any

Addstatus: Any
BaseCommand: Any
CommandError: Any
getAuth: Any
getConfig: Any
tweepy: Any

class Command(Any):
    help: str
    def add_arguments(self, parser) -> None: ...
    def handle(self, *args, **options) -> None: ...
