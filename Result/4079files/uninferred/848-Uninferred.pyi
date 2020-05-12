from catmaid.models import *
from django.core.management.base import BaseCommand, CommandError as CommandError
from typing import Any

logger: Any

class Command(BaseCommand):
    help: str = ...
    def add_arguments(self, parser: Any) -> None: ...
    def handle(self, *args: Any, **options: Any) -> None: ...
