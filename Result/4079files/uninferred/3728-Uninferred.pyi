import django
from typing import Any

EMAIL_RE: str

class Command(django.core.management.base.BaseCommand):
    def add_arguments(self, parser: Any) -> None: ...
    def handle(self, *args: Any, **options: Any) -> None: ...
