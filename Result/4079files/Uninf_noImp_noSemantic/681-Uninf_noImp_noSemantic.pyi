from django.core.management.base import BaseCommand
from typing import Any

VARS: Any
YEARS: Any
WGS84: str

class Command(BaseCommand):
    help: str = ...
    def add_arguments(self, parser: Any) -> None: ...
    def handle(self, region_name: Any, *args: Any, **options: Any) -> None: ...
