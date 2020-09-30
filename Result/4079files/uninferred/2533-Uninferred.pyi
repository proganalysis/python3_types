from bot.conf.cfg import getConfig as getConfig
from bot.log.log import setup_logging as setup_logging
from django.core.management.base import BaseCommand, CommandError as CommandError
from os.path import stat as stat
from typing import Any

logger: Any

class Command(BaseCommand):
    help: str = ...
    def add_arguments(self, parser: Any) -> None: ...
    def handle(self, *args: Any, **options: Any) -> None: ...
