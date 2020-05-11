# (generated with --quick)

from typing import Any

BaseCommand: Any
create_conversion_rates: Any
update_conversion_rates: Any

class Command(Any):
    def add_arguments(self, parser) -> None: ...
    def handle(self, *args, **options) -> None: ...
